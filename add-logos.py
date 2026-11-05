#!/usr/bin/env python3
"""Post-process all articles: fix provider names + inject official provider logos.

- Replaces the template-default '<strong>AICTE / NSP</strong><span>Central Government</span>'
  with the real provider name + category.
- Adds the official provider logo to the main provider tile and to related cards.
  Logo <img> sits on top of the monogram; onerror removes it so the monogram
  remains as a graceful fallback. Missing logo files are skipped silently.
"""
import pathlib, re, html as htmllib

ART = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')
LOGODIR = ART / 'logos'

# slug -> (prov_short, category, logo_key)
INFO = {
 'university-of-calgary-international-entrance-scholarship-2027-canada': ('University of Calgary', 'University \u00b7 Canada', 'ucalgary'),
 'university-of-copenhagen-danish-government-scholarship-2026-27': ('University of Copenhagen', 'University \u00b7 Denmark', 'ucph'),
 'kaist-university-scholarship-2027-south-korea': ('KAIST', 'University \u00b7 South Korea', 'kaist'),
 'hasselt-university-master-mind-scholarship-2027-belgium': ('Hasselt University', 'University \u00b7 Belgium', 'hasselt'),
 'guangxi-normal-university-csc-scholarship-2027-china': ('Guangxi Normal University', 'University \u00b7 China', 'gxnu'),
 'prince-sultan-university-scholarships-2027-28-saudi-arabia': ('Prince Sultan University', 'University \u00b7 Saudi Arabia', 'psu'),
 'university-of-gloucestershire-merit-scholarships-2027-28-uk': ('University of Gloucestershire', 'University \u00b7 United Kingdom', 'glos'),
 'umy-international-student-scholarships-2027-28-indonesia': ('Universitas Muhammadiyah Yogyakarta', 'University \u00b7 Indonesia', 'umy'),
 'boustany-foundation-cambridge-mba-scholarship-2027-uk': ('Boustany Foundation', 'Foundation \u00b7 United Kingdom', 'boustany'),
 'sdef-india-scholarship-2026-27': ('SDEF', 'Private', 'sdef'),
 'vidyadhan-mathura-women-stem-scholarship-2026': ('Vidyadhan', 'Private', 'vidyadhan'),
 'sml-mahindra-scholarship-saarthi-2026-27': ('SML Mahindra', 'CSR', 'mahindra'),
 'ujjivan-transgender-scholarship-2026-27': ('Ujjivan SFB', 'CSR', 'ujjivan'),
 'concentrix-scholarship-2026-27': ('Concentrix', 'CSR', 'concentrix'),
 'wings-women-stem-iit-bombay-2027-28': ('IIT Bombay', 'IIT Bombay', 'iitb'),
 'infocepts-innovate-impact-scholarship-2026-27': ('Infocepts Foundation', 'CSR', 'infocepts'),
 'aditya-birla-capital-scholarship-2026-27': ('Aditya Birla Capital Foundation', 'CSR', 'abc'),
 'satya-scholarship-program-2026': ('Nehru Sidhant Kender Trust', 'Trust', 'satya'),
 'muskaan-scholarship-2-2026-27': ('Valvoline Cummins', 'CSR', 'muskaan'),
 'pathani-samanta-maths-talent-scholarship-2026-27': ('Govt. of Odisha', 'Odisha Government', 'odisha'),
 'icar-nts-ug-scholarship-2026': ('ICAR', 'Central Government', 'icar'),
 'ambedkar-medhavi-chatravriti-himachal-2026-27': ('Govt. of Himachal Pradesh', 'Himachal Pradesh', 'hp'),
 'nirman-shramik-kalyan-yojana-odisha-2026-27': ('Govt. of Odisha', 'Odisha Government', 'odisha'),
 'nsp-post-matric-sc-meghalaya-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'icar-nts-pg-scholarship-2026': ('ICAR', 'Central Government', 'icar'),
 'nsp-top-class-education-sc-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'nasa-hubble-fellowship-program-2027': ('NASA', 'NASA', 'nasa'),
 'bloomberg-harvard-visiting-scholars-2027': ('Harvard University', 'Harvard', 'harvard'),
 'oasis-post-matric-sc-st-west-bengal-2026-27': ('Govt. of West Bengal', 'West Bengal', 'wb'),
 'pm-yasasvi-post-matric-obc-sikkim-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'oasis-post-matric-obc-west-bengal-2026-27': ('Govt. of West Bengal', 'West Bengal', 'wb'),
 'nsp-post-matric-sc-sikkim-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'nsp-pre-matric-st-manipur-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'icar-junior-research-fellowship-pgs-2026': ('ICAR', 'Central Government', 'icar'),
 'pm-scholarship-scheme-ministry-railways-2026-27': ('Ministry of Railways', 'Central Government', 'railways'),
 'isi-kolkata-stipend-scheme-ug-pg-2026-27': ('ISI Kolkata', 'Institute', 'isi'),
 'pm-yasasvi-pre-matric-obc-sikkim-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'nsp-pre-matric-sc-sikkim-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'pm-yasasvi-post-matric-obc-andaman-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'umbrella-scheme-post-matric-st-tripura-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'nsp-pre-matric-st-goa-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'sakal-india-foundation-career-development-scholarship-2026': ('Sakal India Foundation', 'Private Foundation', 'sakal'),
 'super-50-by-aayam-neet-jee-2026-27': ('AAYAM Career Institute', 'Coaching Scholarship', 'aayam'),
 'swiss-government-excellence-phd-scholarships-2027-28': ('Swiss Confederation', 'Switzerland', 'swiss'),
 'epfl-summer-internship-2027': ('EPFL', 'Switzerland', 'epfl'),
 'sage-it-india-scholarship-2026': ('Sage IT Inc.', 'Private', 'sageit'),
 'zonta-amelia-earhart-fellowship-2026': ('Zonta International', 'Women', 'zonta'),
 'world-bank-government-analytics-fellowship-2027': ('World Bank Group', 'Professionals', 'worldbank'),
 'dakshana-scholarship-jdst-2027': ('Dakshana Foundation', 'Coaching', 'dakshana'),
 'nirankari-rajmata-scholarship-scheme-2026-27': ('Sant Nirankari Charitable Foundation', 'Private Foundation', 'nirankari'),
 'nsp-post-matric-sc-goa-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'odisha-banishree-scholarship-2026': ('Govt. of Odisha (SSEPD)', 'Odisha', 'odisha'),
 'umbrella-scheme-post-matric-st-meghalaya-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'national-fellowship-sc-students-nfsc-2026': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'hanns-seidel-scholarships-2027-germany': ('Hanns Seidel Foundation', 'Germany', 'hanns-seidel'),
 'post-matric-scholarship-sc-st-obc-chhattisgarh-2026-27': ('Govt. of Chhattisgarh', 'Chhattisgarh', 'cg'),
 'post-matric-sc-chandigarh-2026-27': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'griffith-vc-international-scholarship-2027': ('Griffith University', 'Australia', 'griffith'),
 'umbrella-pre-matric-st-meghalaya-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'malayalee-engineers-mea-scholarship-2026': ('Malayalee Engineers Association', 'Private', 'mea'),
 'centrally-sponsored-pre-matric-st-andaman-nicobar-2026-27': ('Ministry of Tribal Affairs', 'Central Government', 'mota'),
 'additional-scholarship-st-higher-studies-andaman-nicobar-2026-27': ('Tribal Welfare, A&N', 'Andaman & Nicobar', 'andaman'),
 'iiser-berhampur-pdrf-2025-26': ('IISER Berhampur', 'Institute', 'iiserbpr'),
 'malabar-charitable-trust-scholarship-2026': ('Malabar Charitable Trust', 'CSR', 'malabar'),
 'ramanujan-fellowship-2025-anrf': ('ANRF', 'Central Government', 'anrf'),
 'sof-dsas-defence-services-scholarship-2026-27': ('Science Olympiad Foundation', 'Private', 'sof'),
 'aalto-university-scholarships-2027-finland': ('Aalto University', 'Finland', 'aalto'),
 'nsp-pre-matric-sc-cleaning-health-hazard-tripura-2025-26': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'nsp-pre-matric-sc-tripura-2025-26': ('Ministry of Social Justice', 'Central Government', 'msje'),
 'dundee-global-excellence-scholarship-2027': ('University of Dundee', 'UK', 'dundee'),
 'karnataka-ssp-dme-nursing-scholarship-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-dte-prathibha-puraskara-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-dme-post-matric-st-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-dmw-minority-fee-reimbursement-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-dte-special-category-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-hosteller-maintenance-swd-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'karnataka-ssp-vidyasiri-minorities-2026-27': ('Govt. of Karnataka', 'Karnataka', 'karnataka'),
 'ieg-mainz-phd-fellowship-2027': ('Leibniz Institute of European History', 'Germany', 'ieg-mainz'),
 'joint-japan-world-bank-graduate-scholarship-2027': ('World Bank', 'International', 'worldbank'),
 'japan-imf-jispa-phd-scholarships-2027': ('IMF', 'International', 'imf'),
 'flex-global-abroad-exchange-program-2027-28': ('American Councils', 'USA', 'americancouncils'),
 'lille-eiffel-phd-scholarship-2027': ('University of Lille', 'France', 'lille'),
 'clara-collet-phd-scholarship-2027-ucl': ('UCL', 'UK', 'ucl'),
 'lincoln-global-leaders-scholarship-2027': ('University of Lincoln', 'UK', 'lincoln'),
 'america-world-consortium-fellowships-2027-28': ('America in the World Consortium', 'USA', 'awc'),
 'dayton-merit-scholarship-2027': ('University of Dayton', 'USA', 'dayton'),
 'perugia-phd-scholarships-2026-27': ('University of Perugia', 'Italy', 'perugia'),
 'toronto-oise-graduate-funding-2027': ('University of Toronto', 'Canada', 'utoronto'),
 'ubd-graduate-scholarship-2027-brunei': ('Universiti Brunei Darussalam', 'Brunei', 'ubd'),
 'hzdr-summer-student-program-2027-germany': ('HZDR', 'Germany', 'hzdr'),
 'brunei-darussalam-government-scholarship-2027-28': ('Govt. of Brunei Darussalam', 'Brunei', 'brunei-gov'),
 'utrip-summer-internship-2027-japan': ('University of Tokyo', 'Japan', 'utokyo'),
 'queen-elizabeth-commonwealth-scholarships-2027-28': ('ACU', 'Commonwealth', 'acu'),
 'unu-junior-fellows-internship-spring-2027': ('United Nations University', 'United Nations', 'unu'),
 'ceu-scholarships-2027-hungary': ('Central European University', 'Hungary', 'ceu'),
 'aixbio-research-fellowship-2027': ('ERA / Cambridge Biosecurity Hub', 'UK', 'aixbio'),
 'yeungnam-psps-scholarship-2027-korea': ('Yeungnam University', 'South Korea', 'yeungnam'),
 'erasmus-mundus-glocal-scholarship-2027': ('GLOCAL Consortium', 'Europe', 'glocal'),
 'eiffel-excellence-scholarship-2027-france': ('Campus France', 'France', 'campusfrance'),
 'justcool-phd-scholarship-2027-china': ('JUSTCOOL', 'China', 'justcool'),
 'ippa-chiang-mai-winter-school-2026': ('IPPA', 'Thailand', 'ippa'),
 'manchester-rolls-royce-phd-scholarship-2027': ('University of Manchester', 'UK', 'manchester'),
 'st-johns-university-pharma-fellowship-2027-usa': ("St. John's University", 'USA', 'stjohns'),
 'amazon-research-awards-fall-2026': ('Amazon', 'Private', 'amazon'),
 'erasmus-mundus-emmir-scholarship-2027': ('University of Oldenburg', 'Europe', 'emmir'),
 'unil-masters-scholarship-2027-switzerland': ('University of Lausanne', 'Switzerland', 'unil'),
 'sabanci-university-scholarship-2027-turkey': ('Sabanci University', 'Turkey', 'sabanci'),
 'qassim-university-scholarships-2027-saudi-arabia': ('Qassim University', 'Saudi Arabia', 'qu'),
 'ustc-international-winter-camp-2027-china': ('USTC', 'China', 'ustc'),
 'uq-arc-future-fellowships-2027-australia': ('University of Queensland', 'Australia', 'uq'),
 'apu-adb-scholarship-2027-japan': ('Ritsumeikan APU', 'Japan', 'apu'),
 'monash-university-research-scholarships-2027-australia': ('Monash University', 'Australia', 'monash'),
 'university-erfurt-doctoral-scholarships-2027-germany': ('University of Erfurt', 'Germany', 'erfurt'),
 'sir-james-mcneill-postgraduate-research-scholarship-2027-australia': ('Monash University', 'Australia', 'monash'),
 'tu-eindhoven-excellence-scholarship-2027-netherlands': ('Eindhoven University of Technology', 'Netherlands', 'tue'),
 'tilburg-university-research-master-scholarship-2027-netherlands': ('Tilburg University', 'Netherlands', 'tilburg'),
 'anz-summer-internship-program-2027-australia': ('Australia and New Zealand Banking Group (ANZ)', 'Australia', 'anz'),
 'honjo-international-scholarship-2027-japan': ('Honjo Foundation', 'Japan', 'honjo'),
 'mopga-fellowship-2027-france': ('Campus France', 'France', 'campusfrance'),
 'uiii-scholarships-2027-indonesia': ('UIII', 'Indonesia', 'uiii'),
 'oxford-clarendon-scholarship-2027-uk': ('University of Oxford', 'UK', 'oxford'),
 'science-tokyo-mext-scholarship-2027-japan': ('Institute of Science Tokyo', 'Japan', 'titech'),
 'university-of-tokyo-mext-scholarship-2027-japan': ('University of Tokyo', 'Japan', 'utokyo'),
 'yale-world-fellows-program-2027-usa': ('Yale University', 'USA', 'yale'),
 'mbzuai-postgraduate-scholarships-2027-uae': ('MBZUAI', 'UAE', 'mbzuai'),
 'maastricht-nl-high-potential-scholarship-2027': ('Maastricht University', 'Netherlands', 'maastricht'),
 'heyning-roelli-foundation-scholarship-2027': ('Heyning-Roelli Foundation', 'Switzerland', 'heyning'),
 'daad-university-summer-courses-2027-germany': ('DAAD', 'Germany', 'daad'),
 'canadian-international-development-scholarships-bcdi-2030': ('Global Affairs Canada', 'Canada', 'canada'),
 'msu-out-of-state-resident-scholarship-2027-usa': ('Mississippi State University', 'USA', 'msstate'),
 'said-foundation-scholarship-2027-uk': ('Saïd Foundation', 'UK', 'said'),
 'university-of-malaya-bright-scholarship-2027-malaysia': ('University of Malaya', 'Malaysia', 'um'),
 'national-taiwan-university-scholarship-2027-taiwan': ('National Taiwan University', 'Taiwan', 'ntu'),
 'knu-international-graduate-scholarship-2027-korea': ('KNU', 'South Korea', 'knu'),
 'denmark-fulbright-program-2027': ('Fulbright Denmark', 'Denmark', 'fulbrightcenter-dk'),
 'erasmus-mundus-each-scholarships-2027-europe': ('EACH Consortium', 'Europe', 'each-ut-ee'),
 'keio-university-adb-scholarship-2027-japan': ('Keio University', 'Japan', 'keio-ac-jp'),
 'ursinus-gateway-international-scholarship-2027-usa': ('Ursinus College', 'USA', 'ursinus-edu'),
 'university-of-auckland-scholarship-2027-new-zealand': ('University of Auckland', 'New Zealand', 'auckland-ac-nz'),
 'queen-mary-university-scholarships-2027-uk': ('Queen Mary University of London', 'University · United Kingdom', 'qmul'),
 'university-of-chicago-undergraduate-scholarships-2027-usa': ('University of Chicago', 'University · United States', 'uchicago'),
 'erasmus-mundus-emabg-scholarship-2027': ('Erasmus Mundus (European Commission)', 'European Union · Master\u2019s', 'emabg'),
 'university-of-ottawa-admission-scholarship-2026': ('University of Ottawa', 'University · Canada', 'uottawa'),
 'international-university-of-japan-scholarship-2027': ('International University of Japan', 'University · Japan', 'iuj'),
 # Batch 17 (cron run 17, 18 Oct 2026)
 'how-to-get-fully-funded-scholarships-in-italy-2026-27': ('Italy · Study in Italy', 'Country Guide · Europe', 'italy'),
 'korean-government-gks-scholarship-2027-korea': ('National Institute for International Education (NIIED)', 'Government of Korea', 'gks'),
 'kaust-vsrp-internship-program-2026-saudi-arabia': ('King Abdullah University of Science and Technology', 'University · Saudi Arabia', 'kaust'),
 'oecd-internship-program-2026-france': ('Organisation for Economic Co-operation and Development', 'International Organisation · France', 'oecd'),
 'erasmus-mundus-globed-scholarship-2027': ('Erasmus Mundus GLOBED (UAB)', 'European Union · Master\u2019s', 'globed'),
 # Batch 18 (cron run 18, 18 Oct 2026)
 'university-of-melbourne-research-scholarships-2027-australia': ('University of Melbourne', 'University · Australia', 'unimelb'),
 'study-in-canada-without-ielts-2026': ('Canadian Universities', 'Country Guide · Canada', 'canada'),
 'webster-university-vienna-scholarships-2027-austria': ('Webster Vienna Private University', 'University · Austria', 'webster'),
 'tiffin-university-dragon-flight-fellowship-2027-usa': ('Tiffin University', 'University · USA', 'tiffin'),
 'national-university-of-singapore-scholarships-2027-28-singapore': ('National University of Singapore', 'University · Singapore', 'nus'),
 # Batch 19 (cron run 19, 18 Oct 2026)
 'kaunas-university-of-technology-scholarships-2027-lithuania': ('Kaunas University of Technology', 'University · Lithuania', 'ktu'),
 'turkiye-burslari-scholarships-2027-turkey': ('Türkiye Burslari', 'Government of Turkey', 'turkiyeburslari'),
 'singapore-international-graduate-award-singa-2027': ('A*STAR, NUS, NTU, SUTD', 'Research · Singapore', 'astar'),
 'erasmus-mundus-meta4-0-scholarship-2027': ('META4.0 Consortium (Erasmus Mundus)', 'European Union · Master’s', 'meta40'),
 'kas-international-talent-development-scholarship-2027-germany': ('Konrad Adenauer Stiftung', 'Foundation · Germany', 'kas'),
 # Batch 20 (cron run 20, 18 Oct 2026)
 'adelaide-university-research-scholarships-2027-australia': ('Adelaide University', 'University · Australia', 'adelaide-edu-au'),
 'unilever-internships-2027-guide': ('Unilever', 'Company · Global', 'unilever'),
 'stowers-summer-scholars-program-2027-usa': ('Stowers Institute for Medical Research', 'Research Institute · USA', 'stowers-org'),
 'erasmus-mundus-gem-scholarship-2027': ('GEM Consortium (Erasmus Mundus)', 'European Union · Master\u2019s', 'gem-msc-eu'),
 'erasmus-mundus-densys-scholarship-2027': ('DENSYS Consortium (Erasmus Mundus)', 'European Union · Master\u2019s', 'densys'),
 # Batch 21 (cron run 21, 19 Oct 2026)
 'bevisioneers-mercedes-benz-fellowship-2027': ('Mercedes-Benz × The DO School', 'Corporate Foundation · Fellowship', 'bevisioneers-world'),
 'tampere-university-scholarships-2027-finland': ('Tampere University', 'University · Finland', 'tuni-fi'),
 'kyoto-university-of-advanced-science-scholarships-2027-japan': ('Kyoto University of Advanced Science', 'University · Japan', 'kuas-ac-jp'),
 'nims-internship-program-japan': ('National Institute for Materials Science', 'Research Institute · Japan', 'nims-go-jp'),
 'university-of-waikato-vice-chancellors-international-excellence-scholarship-2027': ('University of Waikato', 'University · New Zealand', 'waikato-ac-nz'),
 # Batch 23 (cron run 23, 19 Oct 2026)
 'broad-summer-research-program-2027-usa': ('Broad Institute', 'Research Institute · USA', 'broadinstitute'),
 'saitama-university-mext-scholarship-2027-japan': ('Saitama University', 'University · Japan', 'saitama'),
 'xiamen-university-csc-scholarships-2027-china': ('Xiamen University', 'University · China', 'xmu'),
 'trent-university-international-scholarships-2027-canada': ('Trent University', 'University · Canada', 'trent'),
 'warwick-chancellors-international-scholarships-2027-uk': ('University of Warwick', 'University · UK', 'warwick'),
 # Batch 24 (cron run 24, 19 Oct 2026)
 'eth-zurich-excellence-scholarship-2027-switzerland': ('ETH Zurich', 'University · Switzerland', 'ethz'),
 'hust-csc-scholarship-program-2027-china': ('Huazhong University of Science and Technology', 'University · China', 'hust'),
 'mit-summer-research-program-msrp-2027-usa': ('Massachusetts Institute of Technology', 'University · USA', 'mit'),
 'taiwanicdf-international-higher-education-scholarship-2027-taiwan': ('TaiwanICDF', 'Government · Taiwan', 'icdf'),
 'bis-phd-fellowship-programme-2027-switzerland': ('Bank for International Settlements', 'International Organisation · Switzerland', 'bis'),
 'holland-nl-scholarship-2026-holland': ('Nuffic', 'Government \u00b7 Netherlands', 'nuffic'),
 'uae-university-undergraduate-scholarship-2026': ('UAE University', 'University \u00b7 UAE', 'uaeu'),
 'unicef-internship-program-2026': ('UNICEF', 'UN \u00b7 Worldwide', 'unicef'),
 'british-airways-summer-internship-2027-uk': ('British Airways', 'Corporate \u00b7 UK', 'ba'),
 'erasmus-mundus-membiomed-scholarship-2027': ('MemBioMed consortium', 'Erasmus Mundus \u00b7 Europe', 'membiomed'),
\
 'nus-amgen-scholars-program-2027-singapore': ('Amgen Foundation', 'Foundation \u00b7 Singapore', 'amgen'),
 'hku-adb-scholarship-2027-hong-kong': ('Asian Development Bank', 'Multilateral \u00b7 Hong Kong', 'adb'),
 'dalian-university-csc-scholarship-2027-china': ('Dalian University of Technology', 'University \u00b7 China', 'dut'),
 'npu-international-scholarships-2027-china': ('Northwestern Polytechnical University', 'University \u00b7 China', 'npu'),
 'erasmus-mundus-mipdal-scholarship-2027': ('MIPDaL consortium (TU Dresden)', 'Erasmus Mundus \u00b7 Europe', 'mipdal'),
\
 'taiwan-international-graduate-program-2027-taiwan': ('Academia Sinica', 'Research Institute \\u00b7 Taiwan', 'tigp'),
 'deakin-vice-chancellors-international-scholarship-2027-australia': ('Deakin University', 'University \\u00b7 Australia', 'deakin'),
 'deutsche-welle-dw-traineeship-2028-29-germany': ('Deutsche Welle', 'Broadcaster \\u00b7 Germany', 'dw'),
 'erasmus-mundus-noha-scholarship-2027-29-europe': ('NOHA Network on Humanitarian Action', 'Erasmus Mundus \\u00b7 Europe', 'noha'),
 'crossculture-programme-ccp-fellowships-2027-germany': ('ifa (Institut für Auslandsbeziehungen)', 'Cultural Institute \\u00b7 Germany', 'ifa'),
 'ens-international-selection-2027-france': ('\u00c9cole Normale Sup\u00e9rieure \u2013 PSL', 'University \u00b7 France', 'ens'),
 'nanjing-university-csc-scholarship-2027-china': ('Nanjing University', 'University \u00b7 China', 'nju'),
 'erasmus-mundus-global-minds-2027': ('Global MINDS consortium', 'Erasmus Mundus \u00b7 Europe', 'globalminds'),
 'epfl-excellence-fellowships-2027-switzerland': ('EPFL', 'University \u00b7 Switzerland', 'epfl'),
 'nanyang-scholarship-2027-ntu-singapore': ('Nanyang Technological University', 'University \u00b7 Singapore', 'ntusg'),
 # Batch 29 (cron run 29, 20 Oct 2026)
 'georg-arnhold-senior-fellowship-2028-germany': ('Georg Arnhold Program', 'Fellowship \u00b7 Germany', 'gei'),
 'new-york-times-fellowship-2027-28-usa': ('The New York Times Company', 'Fellowship \u00b7 USA', 'nytco'),
 'concordia-college-talent-scholarships-usa': ('Concordia College', 'College \u00b7 USA', 'concordiacollege'),
 'bi-presidential-scholarship-2027-norway': ('BI Norwegian Business School', 'University \u00b7 Norway', 'bi'),
 'harvard-lead-fellowship-2027-28-usa': ('Harvard Global Health Institute', 'Fellowship \u00b7 USA', 'harvard'),
 # Batch 30 (cron run 30, 21 Oct 2026)
 'boston-university-trustee-scholarship-2026-usa': ('Boston University', 'University · USA', 'bu'),
 'sciences-po-mastercard-foundation-scholarship-2026-france': ('Sciences Po', 'University · France', 'sciencespo'),
 'kaist-international-undergraduate-scholarship-2026-south-korea': ('KAIST', 'University · South Korea', 'kaist'),
 'reach-oxford-undergraduate-scholarship-2026-uk': ('University of Oxford', 'University · UK', 'oxford'),
 'montreal-university-exemption-scholarships-2026-canada': ('Université de Montréal', 'University · Canada', 'udem'),
 # Batch 31 (cron run 31, 21 Oct 2026)
 'weidenfeld-hoffmann-scholarships-2027-28-uk': ('Weidenfeld-Hoffmann Trust', 'University · UK', 'oxford'),
 'echidna-global-scholar-program-2027-usa': ('Brookings Institution', 'Think Tank · USA', 'brookings'),
 'university-of-amsterdam-merit-scholarship-2027-28': ('University of Amsterdam', 'University · Netherlands', 'uva'),
 'emile-boutmy-scholarships-2027-france': ('Sciences Po', 'University · France', 'sciencespo'),
 'tu-delft-excellence-scholarship-2027-28-netherlands': ('TU Delft', 'University · Netherlands', 'tudelft'),
 # Batch 32 (cron run 32, 21 Oct 2026)
 'ylp-mext-grips-scholarship-2027-japan': ('National Graduate Institute for Policy Studies (GRIPS)', 'Government · Japan', 'grips'),
 'erasmus-mundus-mespom-scholarship-2027-29-europe': ('MESPOM Consortium', 'Erasmus Mundus · Europe', 'mespom'),
 'tomorrows-leaders-scholarship-2027-28': ('U.S. Department of State (MEPI)', 'Government · USA', 'tlp'),
 'radboud-scholarship-programme-2027-28-netherlands': ('Radboud University', 'University · Netherlands', 'radboud'),
 'imperial-college-mba-scholarships-2027-uk': ('Imperial College Business School', 'University · UK', 'imperial'),
 # Batch 33 (cron run 33, 21 Oct 2026)
 'arc-future-fellowships-2027-australia': ('Australian Research Council (ARC)', 'Government · Australia', 'arc'),
 'politecnico-di-torino-phd-scholarships-42nd-cycle-italy': ('Politecnico di Torino', 'University · Italy', 'polito'),
 'edith-cowan-university-scholarships-2027-australia': ('Edith Cowan University', 'University · Australia', 'ecu'),
 'vistec-scholarship-2027-thailand': ('Vidyasirimedhi Institute of Science and Technology (VISTEC)', 'Institute · Thailand', 'vistec'),
 'nus-adb-japan-scholarship-program-2027-singapore': ('ADB–Japan Scholarship Program / National University of Singapore', 'Multilateral · Singapore', 'adb'),
 # Batch 34 (cron run 34, 22 Oct 2026)
 'cern-research-fellowship-2026': ('CERN', 'Research · Switzerland', 'cern'),
 'faspe-fellowship-2027': ('FASPE', 'Fellowship · Ethics Education', 'faspe'),
 'polimi-scholarships-2027-28': ('Politecnico di Milano', 'University · Italy', 'polimi'),
 'swiss-government-scholarships-2027-28': ('Swiss Confederation', 'Switzerland', 'swiss'),
 'fulbright-swedish-scholar-program-2027-28': ('Swedish Fulbright Commission', 'Commission · Sweden–USA', 'fulbrightse'),
 # Batch 35 (cron run 35, 22 Oct 2026)
 'uic-barcelona-university-scholarship-2026': ('Universitat Internacional de Catalunya (UIC Barcelona)', 'University \u00b7 Spain', 'uic'),
 'daad-international-postgraduate-scholarship-2026': ('German Academic Exchange Service (DAAD)', 'Exchange Service \u00b7 Germany', 'daad'),
 'leiden-university-mandela-scholarship-2026': ('Leiden University (Mandela Scholarship Fund)', 'University \u00b7 Netherlands', 'leiden'),
 'dcse-global-talent-scholarship-2025': ('Department of Computer Science and Electronics (DCSE), Universitas Gadjah Mada', 'University \u00b7 Indonesia', 'ugm'),
 'high-point-university-scholarships-2026-usa': ('High Point University', 'University \u00b7 USA', 'hpu'),
 # Batch 36 (cron run 36, 22 Oct 2026)
 'university-of-kassel-expose-scholarships-2026-germany': ('University of Kassel', 'University \u00b7 Germany', 'kassel'),
 'oxford-optiver-foundation-scholarship-2027-uk': ('University of Oxford', 'University \u00b7 UK', 'oxford'),
 'nvidia-graduate-fellowship-2027-28': ('NVIDIA Research', 'Corporate \u00b7 Global', 'nvidia'),
 'cologne-cga-phd-fellowship-2026-germany': ('Cologne Graduate School of Ageing Research', 'Graduate School \u00b7 Germany', 'cga'),
 'university-of-minnesota-global-excellence-scholarship-2027-usa': ('University of Minnesota', 'University \u00b7 USA', 'umn'),
 # Batch 37 (manual recovery run, 22 Oct 2026)
 'chang-gung-university-scholarships-2027-taiwan': ('Chang Gung University', 'University \u00b7 Taiwan', 'cgu'),
 'wageningen-university-scholarships-2027-netherlands': ('Wageningen University & Research', 'University \u00b7 Netherlands', 'wur'),
 'nias-safe-haven-fellowship-2027-28-netherlands': ('NIAS-KNAW', 'Institute \u00b7 Netherlands', 'nias'),
 'western-australian-premier-university-scholarship-2027-australia': ('University of Western Australia', 'University \u00b7 Australia', 'uwa'),
 'stockholm-university-scholarship-scheme-2027-sweden': ('Stockholm University', 'University \u00b7 Sweden', 'su'),
 # Batch 40 (cron run 40, 23 Oct 2026)
 'hansen-leadership-institute-2027-usa': ('Fred J. Hansen Foundation', 'Foundation \u00b7 USA', 'hansen'),
 'salzburg-global-internship-2027-austria': ('Salzburg Global', 'Nonprofit \u00b7 Austria', 'salzburg'),
 'gates-cambridge-scholarship-2027-28-uk': ('Gates Cambridge Trust', 'Trust \u00b7 University of Cambridge', 'gatescambridge'),
 'richmond-scholars-program-2027-usa': ('University of Richmond', 'University \u00b7 USA', 'richmond'),
 'auc-graduate-fellowships-2027-egypt': ('The American University in Cairo', 'University \u00b7 Egypt', 'auc'),
 'pierre-elliott-trudeau-scholarship-2027-canada': ('Pierre Elliott Trudeau Foundation', 'Foundation \u00b7 Canada', 'trudeau'),
 'hdfc-bank-parivartan-ecss-programme-2026-27-india': ('HDFC Bank', 'CSR \u00b7 India', 'hdfc'),
 'un-young-professionals-programme-ypp-2026': ('United Nations', 'UN \u00b7 Worldwide', 'un'),
 'florida-bright-futures-scholarship-2026-27-usa': ('Florida Dept. of Education', 'USA \u00b7 Florida', 'flbf'),
 'up-scholarship-2026-27-online-apply': ('Govt. of Uttar Pradesh', 'Uttar Pradesh', 'upgov'),
 'lawai-summer-research-fellowship-2027-usa': ('Institute for Law & AI (LawAI)', 'Institute \u00b7 USA', 'lawai'),
 'swinburne-university-scholarships-2027-australia': ('Swinburne University of Technology', 'University \u00b7 Australia', 'swinburne'),
 'hawaii-ewc-graduate-fellowship-2027-usa': ('East-West Center', 'Research Institute \u00b7 USA', 'ewc'),
 'hawaii-adb-jsp-scholarship-2027-usa': ('Asian Development Bank / East-West Center', 'Multilateral \u00b7 USA', 'ewc'),
 'inpex-scholarship-program-2027-japan': ('INPEX Scholarship Foundation', 'Foundation \u00b7 Japan', 'inpex'),
 'british-academy-elevate-leadership-program-2027': ('British Academy', 'Academy \u00b7 UK', 'britishacademy'),
 'dartmouth-neukom-postdoctoral-fellowship-2027-usa': ('Neukom Institute, Dartmouth College', 'Institute \u00b7 USA', 'neukom'),
 'university-of-tokyo-adb-scholarship-2027-japan': ('University of Tokyo', 'University \u00b7 Japan', 'utokyo'),
 'european-space-agency-internship-2027': ('European Space Agency', 'Agency \u00b7 Europe', 'esa'),
 'hong-kong-phd-fellowship-scheme-2027': ('Research Grants Council (RGC)', 'Research Council \u00b7 Hong Kong', 'rgc'),
 'franz-werfel-scholarship-program-2027-austria': ('OeAD', 'Agency \u00b7 Austria', 'oead'),
 'asea-uninet-ernst-mach-scholarship-2027-austria': ('OeAD / ASEA-UNINET', 'Agency \u00b7 Austria', 'oead'),
 'cardiff-university-vice-chancellors-scholarship-2027-uk': ('Cardiff University', 'University \u00b7 United Kingdom', 'cardiff'),
 'nctu-international-student-scholarships-2027-taiwan': ('NYCU (formerly NCTU)', 'University \u00b7 Taiwan', 'nycu'),
 'university-of-stirling-vice-chancellor-scholarship-2027-uk': ('University of Stirling', 'University \u00b7 United Kingdom', 'stirling'),
 'robert-gordon-university-vice-chancellors-scholarship-2027-scotland': ('Robert Gordon University', 'University \u00b7 Scotland', 'rgu'),
 'ustc-research-internship-program-2027-china': ('University of Science and Technology of China (USTC)', 'University \u00b7 China', 'ustc'),
 'peking-university-yenching-academy-scholarship-2027-china': ('Yenching Academy, Peking University', 'University \u00b7 China', 'pku'),
 'harvard-environmental-fellows-program-2027-usa': ('Harvard University Center for the Environment', 'Fellowship \u00b7 USA', 'harvard'),
 'university-of-potsdam-scholarships-2027-germany': ('University of Potsdam', 'University \u00b7 Germany', 'potsdam'),
 'university-of-st-andrews-postgraduate-scholarships-2027-scotland': ('University of St Andrews', 'University \u00b7 Scotland', 'standrews'),
 'ubc-killam-fellowship-2027-canada': ('University of British Columbia (UBC)', 'University \u00b7 Canada', 'ubc'),
 'sophia-university-scholarship-2027-japan': ('Sophia University', 'University \u00b7 Japan', 'sophia'),
 'loyola-university-maryland-undergraduate-merit-scholarships-usa': ('Loyola University Maryland', 'University \u00b7 USA', 'loyola'),
 'university-of-vechta-phd-scholarships-2027-germany': ('University of Vechta', 'University \u00b7 Germany', 'vechta'),
 # Batch 47 (cron run 47, 25 Oct 2026)
 'open-door-russian-scholarship-2027-russia': ('Association of Global Universities', 'Government of Russia \u00b7 Open Doors', 'globaluni'),
 'harvard-university-berenson-fellowship-2027-italy': ('Villa I Tatti, Harvard University', 'Fellowship \u00b7 Italy', 'harvard'),
 'nvidia-amri-research-phd-internship-2027': ('NVIDIA Research', 'Corporate \u00b7 Global', 'nvidia'),
 'eu-jean-monnet-scholarship-2027-2028': ('Jean Monnet Scholarship Programme', 'European Union \u00b7 T\u00fcrkiye', 'jeanmonnet'),
 'dartmouth-college-daad-master-scholarship-2027-germany': ('DAAD (via Dartmouth College)', 'Exchange Service \u00b7 Germany', 'daad'),
 # Batch 48 (cron run 48, 25 Oct 2026)
 'university-of-southampton-scholarships-2027-uk': ('University of Southampton', 'University \u00b7 United Kingdom', 'southampton'),
 'leiden-university-excellence-scholarships-2027-netherlands': ('Leiden University', 'University \u00b7 Netherlands', 'leiden'),
 'erasmus-mundus-mapp-scholarship-2027': ('Mundus MAPP Consortium', 'Erasmus Mundus \u00b7 Europe', 'mapp'),
 'monash-university-redileep-phd-scholarship-2027-australia': ('Monash University', 'University \u00b7 Australia', 'monash'),
 'stanford-university-hoover-fellowship-2027-usa': ('Hoover Institution, Stanford University', 'Fellowship \u00b7 United States', 'hoover'),
 # Batch 49 (cron run 49, 25 Oct 2026)
 'university-of-alabama-presidential-scholarship-2027-usa': ('University of Alabama', 'University \u00b7 United States', 'ua'),
 'kut-special-scholarship-program-2027-japan': ('Kochi University of Technology', 'University \u00b7 Japan', 'kut'),
 'king-abdullah-university-scholarship-2027-saudi-arabia': ('King Abdullah University of Science and Technology', 'University \u00b7 Saudi Arabia', 'kaust'),
 'world-trade-organization-internship-2027-switzerland': ('World Trade Organization', 'International Organisation \u00b7 Switzerland', 'wto'),
 'google-student-researcher-program-2027': ('Google', 'Company \u00b7 United States', 'google'),
 # Batch 50 (cron run 50, 25 Oct 2026)
 'university-of-manitoba-graduate-fellowship-2026-canada': ('University of Manitoba', 'University \u00b7 Canada', 'umanitoba'),
 'al-qasimi-foundation-internship-2027-uae': ('Al Qasimi Foundation', 'Foundation \u00b7 United Arab Emirates', 'alqasimi'),
 'dalarna-university-masters-scholarships-2027-sweden': ('Dalarna University', 'University \u00b7 Sweden', 'dalarna'),
 'university-of-vienna-andreas-tietze-memorial-fellowship-2027-austria': ('University of Vienna', 'University \u00b7 Austria', 'univie'),
 'american-university-emerging-global-leader-scholarship-2027-usa': ('American University', 'University \u00b7 United States', 'american'),
 # Batch 51 (cron run 51, 26 Oct 2026)
 'doha-institute-graduate-studies-scholarships-2027-qatar': ('Doha Institute for Graduate Studies', 'Institute \u00b7 Qatar', 'doha'),
 'leeds-doctoral-scholarship-2027-uk': ('University of Leeds', 'University \u00b7 United Kingdom', 'leeds'),
 'oxford-pershing-square-graduate-scholarship-2027-uk': ('University of Oxford', 'University \u00b7 United Kingdom', 'oxford'),
 'anhalt-university-stibet-scholarships-2027-germany': ('Anhalt University of Applied Sciences', 'University \u00b7 Germany', 'anhalt'),
 'wissenschaftskolleg-berlin-fellowships-2027-germany': ('Wissenschaftskolleg zu Berlin', 'Institute for Advanced Study \u00b7 Germany', 'wiko'),
 'westminster-international-postgraduate-excellence-award-2027-uk': ('University of Westminster', 'University \u00b7 United Kingdom', 'westminster'),
 'asia-pacific-university-mext-scholarship-2027-japan': ('Ritsumeikan Asia Pacific University', 'University \u00b7 Japan', 'apu'),
 'daad-re-invitation-programme-2027-germany': ('German Academic Exchange Service (DAAD)', 'Exchange Service \u00b7 Germany', 'daad'),
 'eric-bleumink-scholarship-2027-netherlands': ('University of Groningen', 'University \u00b7 Netherlands', 'rug'),
 'ontario-graduate-scholarship-2027-canada': ('Government of Ontario', 'Government \u00b7 Canada', 'ontario'),
 'cyprus-international-university-scholarships-2027': ('Cyprus International University', 'University \u00b7 Northern Cyprus', 'ciu'),
 'taiwan-government-scholarship-2027': ('Ministry of Education, Taiwan', 'Government \u00b7 Taiwan', 'moe'),
 'university-of-virginia-jefferson-scholarship-2027-usa': ('Jefferson Scholars Foundation', 'Foundation \u00b7 United States', 'jefferson'),
 'erasmus-mundus-emhrpp-scholarship-2027-europe': ('University of Gothenburg', 'University \u00b7 Sweden (Erasmus Mundus consortium)', 'gu'),
 'unicef-traineeship-summer-internship-2027': ('UNICEF', 'United Nations \u00b7 Worldwide', 'unicef'),
 'ceepus-scholarship-program-2027-hungary': ('CEEPUS', 'Exchange Programme \u00b7 Central Europe', 'ceepus'),
 'university-of-stuttgart-scholarships-2027-germany': ('University of Stuttgart', 'University \u00b7 Germany', 'stuttgart'),
 'gem-fellowship-program-2027-usa': ('National GEM Consortium', 'Consortium \u00b7 United States', 'gem-usa'),
 'university-of-british-columbia-fellowships-2027-canada': ('University of British Columbia', 'University \u00b7 Canada', 'ubc'),
 'lincoln-university-scholarships-2027-new-zealand': ('Lincoln University', 'University \u00b7 New Zealand', 'lincoln-nz'),
 # Batch 55 (cron run 55, 27 Oct 2026)
 'dongguan-university-of-technology-scholarships-2027-china': ('Dongguan University of Technology', 'University \u00b7 China', 'dgut'),
 'qatar-government-scholarships-2027': ('Ministry of Education and Higher Education, Qatar', 'Government \u00b7 Qatar', 'qatar-moehe'),
 'sbw-berlin-international-scholarships-2027-germany': ('SBW Berlin', 'Foundation \u00b7 Germany', 'sbw-berlin'),
 'macquarie-university-research-scholarship-2026-27-australia': ('Macquarie University', 'University \u00b7 Australia', 'macquarie'),
 'abertay-university-scholarships-2026-uk': ('Abertay University', 'University \u00b7 United Kingdom', 'abertay'),
 # Batch 56 (cron run 56, 27 Oct 2026)
 'florida-state-university-scholarships-2027-usa': ('Florida State University', 'University \u00b7 USA', 'fsu'),
 'shenzhen-university-phd-scholarships-2027-china': ('Shenzhen University', 'University \u00b7 China', 'szu'),
 'yale-university-scholarships-2027-usa': ('Yale University', 'University \u00b7 USA', 'yale'),
 'jsps-postdoctoral-fellowship-2027-japan': ('Japan Society for the Promotion of Science', 'JSPS \u00b7 Japan', 'jsps'),
 'victoria-university-of-wellington-scholarships-2027-new-zealand': ('Victoria University of Wellington', 'University \u00b7 New Zealand', 'wgtn'),
 'kpmg-global-internship-program-2026': ('KPMG', 'Professional Services \u00b7 Global', 'kpmg'),
 'university-of-idaho-scholarships-2027-usa': ('University of Idaho', 'University \u00b7 USA', 'uidaho'),
 'cape-breton-university-scholarships-2027-canada': ('Cape Breton University', 'University \u00b7 Canada', 'cbu'),
 'ieee-usa-government-fellowship-program-2027': ('IEEE-USA', 'Professional Association \u00b7 USA', 'ieee'),
 'australian-government-research-training-program-rtp-2027': ('Australian Government', 'Government \u00b7 Australia', 'australia'),
 # Batch 58 (cron run 58, 27 Oct 2026)
 'hugo-lab-phd-positions-2027': ('University of South Carolina', 'University \u00b7 USA', 'sc'),
 'tdtu-international-graduate-scholarship-2027-vietnam': ('Ton Duc Thang University', 'University \u00b7 Vietnam', 'tdtu'),
 'ucl-impact-scholarship-2027-uk': ('UCL', 'University \u00b7 United Kingdom', 'ucl'),
 'anthropic-claude-corps-fellowships-2027': ('Anthropic / CodePath', 'Fellowship \u00b7 USA', 'anthropic'),
 'university-of-gottingen-daad-scholarship-2027-germany': ('University of Göttingen', 'University \u00b7 Germany', 'gottingen'),
 'al-qasimi-foundation-scholarships-2026-uae': ('Al Qasimi Foundation', 'Foundation \u00b7 United Arab Emirates', 'alqasimi'),
 'york-university-presidents-international-scholarship-excellence-2027-canada': ('York University', 'University \u00b7 Canada', 'yorku'),
 'university-of-tsukuba-mext-scholarship-2027-japan': ('University of Tsukuba', 'University \u00b7 Japan', 'tsukuba'),
 'duke-university-karsh-scholarship-2026-usa': ('Duke University', 'University \u00b7 USA', 'duke'),
 'epfl-cyd-fellowship-2027-switzerland': ('EPFL / CYD Campus', 'University \u00b7 Switzerland', 'epfl'),
 'ista-scientific-internships-year-round-austria': ('Institute of Science and Technology Austria (ISTA)', 'Institute \u00b7 Austria', 'ista'),
 'adidas-internships-2027-herzogenaurach-germany': ('adidas', 'Company \u00b7 Germany', 'adidas'),
 'nsp-national-scholarship-programme-slovakia-2027': ('SAIA', 'Government \u00b7 Slovakia', 'saia'),
 'university-of-miami-stamps-scholarship-2027-usa': ('University of Miami', 'University \u00b7 USA', 'miami'),
 'university-of-pisa-dsu-scholarship-2027-italy': ('University of Pisa', 'University \u00b7 Italy', 'unipi'),
 'fbi-honors-internships-2027-usa': ('Federal Bureau of Investigation (FBI)', 'Federal Agency \u00b7 USA', 'fbi'),
 'university-of-glasgow-global-leadership-scholarships-2027-uk': ('University of Glasgow', 'University \u00b7 United Kingdom', 'gla'),
 'university-of-melbourne-graduate-research-scholarships-2027-australia': ('University of Melbourne', 'University \u00b7 Australia', 'unimelb'),
 'hokkaido-university-mext-scholarships-2027-japan': ('Hokkaido University', 'University \u00b7 Japan', 'hokudai'),
 'boston-university-presidential-scholarship-2027-usa': ('Boston University', 'University \u00b7 USA', 'bu'),
 'unilever-future-leaders-programme-2026': ('Unilever', 'Company \u00b7 Global', 'unilever'),
 'islamic-university-of-madinah-scholarship-2026-saudi-arabia': ('Islamic University of Madinah', 'University \u00b7 Saudi Arabia', 'iu'),
 'anu-international-research-scholarships-2026-australia': ('Australian National University', 'University \u00b7 Australia', 'anu'),
 'university-of-melbourne-human-rights-scholarship-2027-australia': ('University of Melbourne', 'University \u00b7 Australia', 'unimelb'),
 'heinrich-boll-foundation-scholarships-2027-germany': ('Heinrich Böll Foundation', 'Foundation \u00b7 Germany', 'boell'),
 'european-university-institute-traineeships-2026-italy': ('European University Institute', 'Institute \u00b7 Italy', 'eui'),
 'scout-adventures-volunteer-program-2026-uk': ('Scout Adventures', 'The Scout Association \u00b7 United Kingdom', 'scoutadventures'),
 'purdue-university-scholarship-2026-usa': ('Purdue University', 'University \u00b7 USA', 'purdue'),
 'simmons-university-kotzen-scholarship-2026-usa': ('Simmons University', 'University \u00b7 USA', 'simmons'),
 'united-nations-volunteer-program-2026': ('United Nations Volunteers', 'United Nations \u00b7 Global', 'un'),
 # Batch 64 (29 Oct 2026)
 'texas-tech-university-presidential-merit-scholarship-2027-usa': ('Texas Tech University', 'University \u00b7 USA', 'ttu'),
 'eth-zurich-postdoctoral-fellowship-2027-switzerland': ('ETH Zurich', 'Institute \u00b7 Switzerland', 'ethz'),
 'ruhr-university-daad-epos-scholarships-2028-germany': ('Ruhr University Bochum', 'University \u00b7 Germany', 'ruhr'),
 'qatar-airways-university-undergraduate-scholarship-2026': ('Qatar Airways', 'Airline \u00b7 Qatar', 'qatarairways'),
 'anu-international-chancellors-scholarship-2026-australia': ('Australian National University', 'University \u00b7 Australia', 'anu'),
 'unicaf-online-scholarship-program-2026': ('UNICAF', 'Online Education \u00b7 International', 'unicaf'),
 'harvard-university-mba-scholarship-2027-usa': ('Boustany Foundation', 'Foundation \u00b7 USA', 'boustany'),
 'unhcr-internship-2026-online-apply': ('UNHCR', 'United Nations \u00b7 Worldwide', 'unhcr'),
 'university-of-michigan-dearborn-scholarship-2026-usa': ('University of Michigan-Dearborn', 'University \u00b7 USA', 'umdearborn'),
 'friedrich-ebert-foundation-scholarship-2026-germany': ('Friedrich Ebert Foundation', 'Foundation \u00b7 Germany', 'fes'),
 # Batch 66 (29 Oct 2026)
 'ifad-internship-program-2026': ('IFAD', 'United Nations \u00b7 International', 'ifad'),
 'humboldt-research-fellowship-2026-germany': ('Alexander von Humboldt Foundation', 'Foundation \u00b7 Germany', 'humboldt'),
 'cern-short-term-internship-2026-switzerland': ('CERN', 'Research Organisation \u00b7 Switzerland', 'cern'),
 'university-of-huddersfield-international-scholarships-2026-uk': ('University of Huddersfield', 'University \u00b7 United Kingdom', 'huddersfield'),
 'hennge-global-internship-program-2026-japan': ('HENNGE', 'Technology Company \u00b7 Japan', 'hennge'),
 'university-of-malta-scholarships-2026-malta': ('University of Malta', 'University \u00b7 Malta', 'um'),
 'uwa-global-excellence-scholarship-2026-australia': ('University of Western Australia', 'University \u00b7 Australia', 'uwa'),
 'university-of-twente-scholarship-2027-netherlands': ('University of Twente', 'University \u00b7 Netherlands', 'utwente'),
 'master-mind-scholarship-2027-belgium': ('KU Leuven', 'University \u00b7 Belgium', 'kuleuven'),
 'imf-fund-internship-program-2027-usa': ('International Monetary Fund', 'International Organisation', 'imf'),
 'university-of-georgia-undergraduate-scholarships-2026-usa': ('University of Georgia', 'University \u00b7 USA', 'uga'),
 'university-of-detroit-mercy-scholarships-2026-usa': ('University of Detroit Mercy', 'University \u00b7 USA', 'udmercy'),
 'central-queensland-university-rtp-scholarship-2026-australia': ('Central Queensland University', 'University \u00b7 Australia', 'cqu'),
 'boehringer-ingelheim-fonds-md-fellowships': ('Boehringer Ingelheim Fonds', 'Foundation \u00b7 Germany', 'bifonds'),
 'bookachange-music-scholarship-2025': ('BookMyShow Foundation (BookAChange)', 'Foundation \u00b7 India', 'bookachange'),
 # Batch 69 (cron run 69, 30 Oct 2026)
 'csir-nehru-science-postdoctoral-research-fellowship': ('Council of Scientific & Industrial Research (CSIR)', 'Central Government \u00b7 India', 'csir'),
 'eastman-powerup-eduskill-scholarship-program-2026-27': ('Eastman Auto and Power Limited (EAPL)', 'CSR \u00b7 India', 'eastman'),
 'environmental-leaders-fellowship': ('Sadhana Forest', 'Non-profit \u00b7 India & International', 'sadhana'),
 'nsp-kalpana-chawla-chatravriti-yojana-himachal-pradesh-2026-27': ('Govt. of Himachal Pradesh', 'Himachal Pradesh \u00b7 NSP', 'hp'),
 'kind-circle-scholarship-for-meritorious-students-2026-27': ('Kind Circle (Buddy4Study India Foundation initiative)', 'Philanthropy \u00b7 India', 'kindcircle'),
 'nsp-maharishi-balmiki-chatravriti-yojana-himachal-pradesh-2026-27': ('Govt. of Himachal Pradesh', 'Himachal Pradesh \u00b7 NSP', 'hp'),
 'nsp-mukhya-mantri-protsahan-yojana-himachal-pradesh-2026-27': ('Govt. of Himachal Pradesh', 'Himachal Pradesh \u00b7 NSP', 'hp'),
 'nsp-national-scholarship-post-graduate-studies-2026-27': ('University Grants Commission (UGC)', 'Central Government \u00b7 NSP', 'ugc'),
 'navgurukul-residential-programmes-pune': ('NavGurukul', 'Non-profit \u00b7 India', 'navgurukul'),
 'navgurukul-school-of-business-residential-programme-sarjapur': ('NavGurukul', 'Non-profit \u00b7 India', 'navgurukul'),
 'navgurukul-school-of-programming-residential-programme-sarjapur': ('NavGurukul', 'Non-profit \u00b7 India', 'navgurukul'),
 'nshm-knowledge-campus-asha-jyoti-scholarship-2025': ('NSHM Knowledge Campus', 'Private Institute \u00b7 West Bengal', 'nshm'),
 'nsp-prime-ministers-scholarship-scheme-for-wards-of-states-uts-police-personnel-2026-27': ('Ministry of Home Affairs', 'Central Government', 'mha'),
 'nsp-scholarships-for-top-class-education-for-students-with-disabilities-2026-27': ('DEPwD', 'Central Government', 'depwd'),
 'nurtr-nurturing-minds-with-chess-program-50-fee-waiver-2025-26': ('nurtr', 'Private \u00b7 Chess Academy', 'nurtr'),
 'prime-minister-vidyalaxmi-education-loan-scheme': ('Government of India', 'Central Government \u00b7 Education Loan', 'vidyalaxmi'),
 'nsp-ishan-uday-special-scholarship-ner-2026-27': ('University Grants Commission (UGC)', 'Central Government \u00b7 NSP', 'ugc'),
 'nsp-thakur-sen-negi-utkrisht-chatravriti-yojana-himachal-pradesh-2026-27': ('Department of Education, Himachal Pradesh', 'State Government \u00b7 NSP', 'hp'),
 'aicte-swanath-scholarship-scheme-2026-27': ('All India Council for Technical Education (AICTE)', 'Central Government \u00b7 NSP', 'aicte'),
 'pm-yasasvi-top-class-college-scholarship-2026-27': ('Ministry of Social Justice and Empowerment', 'Central Government \u00b7 NSP', 'msje'),
 'sadhana-forest-fellowship': ('Sadhana Forest', 'Community Fellowship \u00b7 Tamil Nadu', 'sadhana'),
 'sadhana-forest-scholarship': ('Sadhana Forest', 'Community Scholarship \u00b7 Tamil Nadu', 'sadhana'),
 'pm-scholarship-capf-assam-rifles-2026-27': ('Ministry of Home Affairs', 'Central Government', 'mha'),
 'icar-post-graduate-scholarship-pgs-2026': ('ICAR', 'Central Government', 'icar'),
 'post-matric-beedi-cine-iomc-lsdm-workers-2026-27': ('Ministry of Labour and Employment', 'Central Government', 'labour'),
 'teach-trust-education-assistance-2026': ('TEACH Trust', 'Charitable Trust · Tamil Nadu', 'teach'),
 'vylor-agritech-scholarship-undergraduate-fy-26-27': ('Vylor Agritech', 'Private · Agriculture', 'vylor'),
 'aicte-post-doctoral-fellowship-pdf-2024-25': ('All India Council for Technical Education (AICTE)', 'Central Government · AICTE', 'aicte'),
 'aicte-productization-fellowship-apf-2026': ('All India Council for Technical Education (AICTE)', 'Central Government · AICTE', 'aicte'),
 'aicte-saksham-scholarship-scheme-2024-25': ('All India Council for Technical Education (AICTE)', 'Central Government · AICTE', 'aicte'),
 'aicte-yashasvi-scholarship-scheme-2024': ('All India Council for Technical Education (AICTE)', 'Central Government · AICTE', 'aicte'),
}

LOGO_CSS = ('.plogo.monogram.has-logo{position:relative;overflow:hidden;background:#fff;padding:0}'
            '.plogo.monogram.has-logo img{position:absolute;inset:0;width:100%;height:100%;'
            'object-fit:contain;background:#fff}'
            '.plogo.monogram.has-logo.dark{background:linear-gradient(135deg,#1a2145,#2e4a8f)}'
            '.plogo.monogram.has-logo.dark img{background:transparent}')
# white-on-transparent emblems need the dark tile
DARK_LOGOS = {'msje', 'mota', 'railways', 'satya', 'knu', 'maastricht', 'qmul', 'xmu', 'hust'}

def resolve_logo(key):
    """Prefer the live-site favicon; fall back to the downloaded official logo.
    Returns (filename, dark_tile_needed)."""
    for cand, dark in [(f'fav-{key}.png', False), (f'{key}.png', key in DARK_LOGOS)]:
        p = LOGODIR / cand
        if p.exists() and p.stat().st_size > 200:
            return cand, dark
    return None, False

def logo_file(key):
    f, _ = resolve_logo(key)
    return LOGODIR / f if f else None

def inject_tile(html, mono_text, logo_key, alt, lg=True):
    """Add logo img inside the provider tile span (monogram stays as fallback)."""
    fname, dark = resolve_logo(logo_key)
    if not fname:
        return html, False
    cls = 'plogo lg monogram' if lg else 'plogo monogram'
    old = f'<span class="{cls}">{mono_text}</span>'
    if old not in html:
        return html, False
    darkcls = ' dark' if dark else ''
    new = (f'<span class="{cls} has-logo{darkcls}">{mono_text}'
           f'<img src="logos/{fname}" alt="{htmllib.escape(alt)}" '
           f'loading="lazy" onerror="this.remove()"></span>')
    return html.replace(old, new, 1), True

fixed_names = 0
logo_main = 0
logo_cards = 0
for slug, (prov, cat, lkey) in INFO.items():
    f = ART / f'{slug}.html'
    if not f.exists():
        print('MISSING FILE', slug); continue
    html = f.read_text()

    # 0. Strip any previous logo injections for a clean re-run
    html = re.sub(r'<span class="(plogo (?:lg )?monogram)(?: has-logo(?: dark)?)?">([^<]*)<img[^>]*></span>',
                  r'<span class="\1">\2</span>', html)
    # remove old logo CSS block if present
    html = re.sub(r'\.plogo\.monogram\.has-logo\{[^}]*\}'
                  r'\.plogo\.monogram\.has-logo img\{[^}]*\}'
                  r'(\.plogo\.monogram\.has-logo\.dark\{[^}]*\}'
                  r'\.plogo\.monogram\.has-logo\.dark img\{[^}]*\})?',
                  '', html)

    # 1. Fix provider name + category (template default bug)
    old_prov = '<div><strong>AICTE / NSP</strong><span>Central Government</span></div>'
    if old_prov in html:
        html = html.replace(old_prov,
            f'<div><strong>{htmllib.escape(prov)}</strong><span>{htmllib.escape(cat)}</span></div>', 1)
        fixed_names += 1

    # 2. Ensure logo CSS present and current
    if '.plogo.monogram.has-logo{' not in html:
        html = html.replace('</style>', LOGO_CSS + '\n</style>', 1)

    # 3. Main provider tile: find its mono text
    m = re.search(r'<span class="plogo lg monogram">([^<]*)</span>', html)
    if m and 'has-logo' not in html[m.start():m.start()+200]:
        html, ok = inject_tile(html, m.group(1), lkey, prov + ' logo', lg=True)
        logo_main += ok

    # 4. Related cards: parse each scard block, map its href slug -> logo
    def fix_card(mo):
        block = mo.group(0)
        if 'has-logo' in block:
            return block
        hm = re.search(r'<h3><a href="([^"]+)">', block)
        sm = re.search(r'<span class="plogo monogram">([^<]*)</span>', block)
        if not hm or not sm:
            return block
        href = hm.group(1)
        cslug = href[:-5] if href.endswith('.html') else href
        if cslug not in INFO:
            return block
        fname, dark = resolve_logo(INFO[cslug][2])
        if not fname:
            return block
        darkcls = ' dark' if dark else ''
        newspan = (f'<span class="plogo monogram has-logo{darkcls}">{sm.group(1)}'
                   f'<img src="logos/{fname}" alt="" loading="lazy" '
                   f'onerror="this.remove()"></span>')
        return block.replace(sm.group(0), newspan, 1)

    cards_before = len(re.findall(r'<article class="scard rv">', html))
    html = re.sub(r'<article class="scard rv">[\s\S]*?</article>', fix_card, html)
    logo_cards += len(re.findall(r'<article class="scard rv">[\s\S]*?has-logo', html))
    f.write_text(html)

print(f'provider names fixed: {fixed_names}, main tiles with logo: {logo_main}, cards with logo: {logo_cards}')

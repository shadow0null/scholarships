#!/usr/bin/env python3
"""Batch F2 (subagent): 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'tripura-cleaning': dict(mono='NSP', title='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2026-27', href='pre-matric-sc-cleaning-health-hazard-tripura-2026-27.html',
              dpill='86 days to go', award='Up to Rs 700/month + grant', elig='SC Class 1–10; Tripura; wards of sanitation/hazard workers.',
              tags=[('SC','blue'),('Tripura','teal')]),
 'ieg-mainz': dict(mono='IEG', title='IEG Mainz PhD Fellowship 2027 in Germany', href='ieg-mainz-phd-fellowship-2027.html',
              dpill='122 days to go', award='€1,650/month + family allowance', elig='PhD researchers; European history; all nationalities.',
              tags=[('PhD','blue'),('Germany','teal')]),
 'jjwbgsp': dict(mono='WB', title='Joint Japan/World Bank Graduate Scholarship (JJ/WBGSP) 2027', href='joint-japan-world-bank-jjwbgsp-2027.html',
              dpill='133 days to go', award='Tuition + stipend + airfare', elig='Developing-country nationals; 3 yrs development work; admitted to partner Master’s.',
              tags=[('Master’s','blue'),('International','teal')]),
 'jispa': dict(mono='IMF', title='IMF JISPA PhD Scholarships 2027 in Japan', href='imf-jispa-phd-scholarship-2027-japan.html',
              dpill='228 days to go', award='Fully funded PhD', elig='Govt officials (India incl.); economics PhD; employer-nominated.',
              tags=[('PhD','blue'),('Japan','teal')]),
 'manchester-rr': dict(mono='UoM', title='University of Manchester Rolls-Royce PhD Scholarship 2027', href='manchester-rolls-royce-phd-scholarship-2027.html',
              dpill='84 days to go', award='Tuition + ~£25,518/yr stipend', elig='First/2:1 in engineering/science; check fee status per project.',
              tags=[('PhD','blue'),('UK','teal')]),
}

ARTICLES = [
dict(
 slug='pre-matric-sc-cleaning-health-hazard-tripura-2026-27',
 title='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2026-27 | StudyDesk Scholarships',
 meta='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2026-27: up to Rs 700/month for children of sanitation and hazardous-occupation workers. Deadline 10 Jan 2027.',
 short='Tripura Cleaning & Health Hazard Scholarship', kicker='Central Government · NSP · Tripura',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment, Govt. of India (via NSP)',
 h1='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2026–27',
 sub='Up to Rs 700 a month plus an annual grant — for schoolchildren of Tripura whose parents work in sanitation and hazardous occupations.',
 dpill='86 days to go', dl_long='10 Jan 2027',
 facts=facts([('Award','Up to Rs 700 / month<small>Hostellers; 10 months</small>'),
              ('Ad-hoc grant','Rs 750–1,000 / year<small>Day scholar / hosteller</small>'),
              ('Who can apply','SC, Class 1–10<small>Tripura domicile; wards of sanitation/hazard workers</small>'),
              ('Income ceiling','None for this component<small>Occupation-based, not income-based</small>'),
              ('Deadline','10 Jan 2027<small>Via NSP</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2026–27</strong> is a component of the Ministry of Social Justice and Empowerment's pre-matric scheme for Scheduled Castes, implemented in Tripura through the <strong>National Scholarship Portal</strong>. It supports <strong>children and wards of people engaged in manual scavenging, tanning and flaying, waste picking, and hazardous cleaning</strong> — so that the nature of a parent's work never becomes a reason to drop out of school.</p>
      <div class="honest-note"><strong>Two components, one scheme:</strong> this article covers <strong>Component 2</strong> (children of parents in unclean/hazardous occupations). The separate <strong>Component 1</strong> covers SC students of Classes 9–10 generally and has an income ceiling — different eligibility, same portal.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domiciled in Tripura</strong>.</li>
        <li>Enrolled in <strong>Class 1 to 10</strong> in a recognised institution (<strong>hostellers: Class 3 onwards</strong>).</li>
        <li>Be the <strong>child or ward of a person engaged in</strong>: manual scavenging (as defined in Section 2(1)(g) of the Manual Scavengers Act, 2013); <strong>tanning and flaying</strong>; <strong>waste picking</strong>; or <strong>hazardous cleaning</strong> (Section 2(1)(d)).</li>
        <li>Submit a <strong>certificate from the District Social Welfare Officer</strong> (or the officer/authority designated by the State Government) confirming the parent's occupation.</li>
        <li><strong>No family income ceiling</strong> applies to this component.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th></th><th>Day scholars</th><th>Hostellers</th></tr>
      <tr><td>Monthly scholarship (10 months)</td><td>Rs 225/month (Class 1–10)</td><td>Rs 700/month (Class 3–10)</td></tr>
      <tr><td>Ad-hoc grant (per year)</td><td>Rs 750</td><td>Rs 1,000</td></tr></table>
      <p>Additional allowances apply for students with disabilities under the scheme guidelines. Paid through <strong>DBT</strong>.</p>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Tripura)</li><li>SC/community certificate</li>
        <li><strong>Parent's occupation certificate</strong> from the District Social Welfare Officer or designated authority</li>
        <li>Previous year's marksheet</li><li>Bank account details (student's own account)</li><li>Passport-size photograph</li><li>Aadhaar</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Tripura + the pre-matric cleaning &amp; health hazard component.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>10 January 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there an income limit?","No — this component is occupation-based, not income-based."),
 ("Who counts as a hazardous-occupation worker?","Manual scavengers (per the 2013 Act), tanners and flayers, waste pickers, and persons engaged in hazardous cleaning."),
 ("Which classes are covered?","Class 1 to 10 for day scholars; hostellers from Class 3."),
 ("Where do I apply?","On the National Scholarship Portal, scholarships.gov.in."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Tripura listing (10 Jan 2027; Rs 225 day / Rs 700 hostel per month for 10 months; Rs 750/1,000 ad-hoc grant; occupation categories) and JagranJosh (component 2 structure; no income ceiling; Manual Scavengers Act references).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['umbrella-tripura','goa-sc','prematric-st-goa'],
),

dict(
 slug='ieg-mainz-phd-fellowship-2027',
 title='IEG Mainz PhD Fellowship 2027 in Germany (€1,650/month) | StudyDesk Scholarships',
 meta='IEG Mainz PhD Fellowship 2027: €1,650/month for 6–12 months for doctoral researchers in European history. Deadline 15 Feb 2027.',
 short='IEG Mainz PhD Fellowship', kicker='Germany · PhD · International',
 mono='IEG', prov_short='Leibniz Institute of European History', prov_long='Leibniz Institute of European History (IEG), Mainz',
 h1='IEG Mainz PhD Fellowship 2027 in Germany',
 sub='€1,650 a month for 6–12 months — dedicated writing time in Mainz for doctoral researchers in European history.',
 dpill='122 days to go', dl_long='15 Feb 2027',
 facts=facts([('Award','€1,650 / month<small>6–12 months; family allowance extra</small>'),
              ('Who can apply','Doctoral researchers<small>All nationalities; European history focus</small>'),
              ('Stage','Dissertation writing phase<small>Research already well advanced</small>'),
              ('Residence','Mainz, Germany<small>Full-time presence required</small>'),
              ('Deadline','15 Feb 2027<small>Online application</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Leibniz Institute of European History (IEG), Mainz</strong> awards fellowships for <strong>doctoral students in European history, the history of religion, and other historically oriented disciplines</strong>. The fellowship funds a <strong>6 to 12-month writing stay in Mainz</strong> — it is designed for researchers whose dissertation is well advanced and who need dedicated time, mentoring and library access to finish it.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Doctoral researcher</strong> (international and German applicants welcome).</li>
        <li>PhD project in <strong>European history from the early modern period to contemporary history</strong> — the IEG is especially interested in comparative or cross-border approaches, Europe's relations with the wider world, intellectual and religious history, digital methods, and environmental history.</li>
        <li>Normally <strong>no more than three years into the dissertation</strong> by the deadline (justified exceptions possible).</li>
        <li><strong>Source research already well advanced</strong>; a mature dissertation concept.</li>
        <li>Willing to <strong>live in Mainz full-time</strong>, join weekly colloquia and academic life, and present the work at least once.</li>
        <li><strong>No paid employment or parallel funding</strong> during the fellowship.</li>
      </ul>
      <div class="honest-note"><strong>Not for:</strong> initial preparatory research, language courses, or turning a finished dissertation into a book — the fellowship funds the <strong>writing and completion stage</strong>.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€1,650 per month</strong> for 6–12 months.</li>
        <li><strong>Family allowance:</strong> €250 (partner), €400 (first child), €100 (each additional child).</li>
        <li><strong>Mentoring</strong> by IEG researchers, library and workspace access.</li>
        <li>Option to rent an <strong>affordable room in the institute's residence</strong> (subject to availability).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed application form</li><li>Passport</li><li>Academic transcripts + degree certificate</li>
        <li>Academic CV and publication list (if any)</li><li>Dissertation table of contents</li>
        <li><strong>Project description (max 15,000 characters, excluding spaces and footnotes)</strong></li>
        <li>Detailed work plan and timeline for the stay</li><li>Language certificates (where applicable)</li>
        <li><strong>Two academic references</strong> — referees must send signed PDF letters <strong>directly to application@ieg-mainz.de</strong> by the deadline</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the fit</strong>Make sure your dissertation matches IEG's European-history research profile.</li>
        <li><strong>Prepare in English or German</strong>Choose the language you write best in.</li>
        <li><strong>Line up referees early</strong>They — not you — must email the signed letters by <strong>15 February 2027</strong>.</li>
        <li><strong>Submit via the IEG application portal</strong>ieg-mainz.de</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who can apply?","Doctoral researchers of any nationality working on European history or related historical disciplines."),
 ("How much is the stipend?","€1,650 per month, plus family allowances where applicable."),
 ("Can I work alongside the fellowship?","No — paid employment and parallel financial support are not permitted."),
 ("Do I have to live in Mainz?","Yes — full-time residence and presence in Mainz is required (special arrangements for fellows with children are negotiable)."),
]),
 verify='Verified 16 Oct 2026 against the official IEG application portal (bewerbung.ieg-mainz.de: €1,650; family allowance; 6–12 months; Mainz residence; March 2027 start) and Bright Scholarship/daadscholarship.com (15 Feb 2027 deadline; document list; referee rule).',
 offlinks=[('IEG Fellowships for Doctoral Students (official)','https://www.ieg-mainz.de/en/fellowships')],
 related_titles=['hanns-seidel','swiss-phd','zonta-ae'],
),

dict(
 slug='joint-japan-world-bank-jjwbgsp-2027',
 title='Joint Japan/World Bank Graduate Scholarship (JJ/WBGSP) 2027 | StudyDesk Scholarships',
 meta='JJ/WBGSP 2027: fully funded Master’s in development fields for developing-country nationals. Window 1 deadline 26 Feb 2027.',
 short='JJ/WBGSP 2027', kicker='World Bank · Master’s · International',
 mono='WB', prov_short='World Bank', prov_long='World Bank Development Economics Vice Presidency (funded by Japan)',
 h1='Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP) 2027',
 sub='Tuition, living stipend, airfare and insurance — a fully funded Master’s for development professionals from developing countries.',
 dpill='133 days to go', dl_long='26 Feb 2027 (Window 1)',
 facts=facts([('Award','Fully funded Master’s<small>Tuition + stipend + airfare + insurance</small>'),
              ('Who can apply','Developing-country nationals<small>Incl. India; 3 yrs development work</small>'),
              ('Programmes','44 Master’s at 24 universities<small>Development-related fields</small>'),
              ('Windows','18 Jan–26 Feb 2027<small>Window 2: 29 Mar–21 May 2027</small>'),
              ('First step','University admission<small>Must be admitted to a partner programme first</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP)</strong>, funded by the <strong>Government of Japan</strong> and administered by the World Bank, funds <strong>Master's degrees in development-related fields</strong> for professionals from developing countries. For 2027 there are <strong>44 participating Master's programmes at 24 universities</strong> across the US, Europe, Africa, Oceania and Japan. After the degree, scholars are expected to <strong>return home and contribute to their country's development</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>National of a World Bank member developing country</strong> — including <strong>India</strong>; no dual citizenship of a developed country.</li>
        <li><strong>Bachelor's degree earned at least 3 years before</strong> the application deadline.</li>
        <li><strong>At least 3 years of paid development-related employment</strong> since the bachelor's (acquired within the past 6 years), and <strong>currently employed full-time</strong> in development work.</li>
        <li><strong>Admitted unconditionally</strong> (except for financing) to one of the 44 participating Master's programmes <strong>outside the applicant's home country</strong>.</li>
        <li>Good health; commitment to return home after the degree.</li>
        <li><strong>Not eligible:</strong> those already enrolled in a participating programme; World Bank Group staff and close relatives.</li>
      </ul>
      <div class="honest-note"><strong>Admission comes first:</strong> you cannot apply for JJ/WBGSP until a participating university has admitted you and shortlisted you as eligible. The scholarship application link is sent only to those candidates.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for the programme (up to 2 years).</li>
        <li><strong>Monthly living stipend.</strong></li>
        <li><strong>Round-trip economy airfare</strong> + <strong>USD 600 travel allowance</strong> per trip.</li>
        <li><strong>Basic medical insurance</strong> through the institution.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Unconditional admission offer from a participating programme</li><li>Bachelor's degree certificate + transcripts</li>
        <li>Proof of employment and 3 years' development work experience</li><li>Employer support statement</li>
        <li>CV</li><li>Passport / nationality proof</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to a participating Master's programme</strong>Check the 44-programme list on the World Bank site; secure unconditional admission.</li>
        <li><strong>Get shortlisted by the university</strong>The university forwards eligible admitted candidates to the World Bank.</li>
        <li><strong>Receive the scholarship link and apply</strong>Window 1: <strong>18 January – 26 February 2027</strong> · Window 2: <strong>29 March – 21 May 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is India eligible?","Yes — India is a World Bank member developing country."),
 ("Do I apply to the World Bank directly?","No — first get admitted to a participating programme; the university shortlists you, then you receive the scholarship application link."),
 ("What does it cover?","Tuition, monthly living stipend, round-trip airfare, basic medical insurance and a travel allowance."),
 ("Can current students of a partner programme apply?","No — students already enrolled in a participating programme are ineligible."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study JJ/WBGSP 2027 listing (26 Feb 2027 Window 1; India eligible; 3 yrs experience; unconditional admission required) and opportunitiesforyouth.org / opportunitiesfeed.com (44 programmes, 24 universities; Window 2: 29 Mar–21 May 2027; benefits).',
 offlinks=[('JJ/WBGSP (World Bank, official)','https://www.worldbank.org/en/programs/scholarships')],
 related_titles=['bloomberg-harvard','griffith-vc','swiss-phd'],
),

dict(
 slug='imf-jispa-phd-scholarship-2027-japan',
 title='IMF JISPA PhD Scholarships 2027 in Japan (Fully Funded) | StudyDesk Scholarships',
 meta='IMF JISPA PhD 2027: fully funded economics PhD in Japan for government officials (India eligible). Deadline 1 June 2027.',
 short='IMF JISPA PhD 2027', kicker='IMF · PhD · Japan',
 mono='IMF', prov_short='International Monetary Fund', prov_long='International Monetary Fund (funded by Japan)',
 h1='IMF JISPA PhD Scholarships 2027 in Japan',
 sub='A fully funded economics PhD in Japan — for government officials from Asia-Pacific countries including India.',
 dpill='228 days to go', dl_long='1 Jun 2027',
 facts=facts([('Award','Fully funded PhD<small>Tuition + stipend + airfare</small>'),
              ('Who can apply','Government officials<small>India eligible; economics policymaking</small>'),
              ('Field','Economics / public policy<small>PhD at accredited Japanese universities</small>'),
              ('Window','1 May – 1 Jun 2027<small>23:59 JST deadline</small>'),
              ('Nomination','Employer-nominated<small>Must return to agency after</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Japan-IMF Scholarship Program for Asia (JISPA), PhD track</strong>, funded by the Government of Japan and administered by the IMF, trains <strong>government officials from eligible Asian and Pacific countries</strong> — including <strong>India</strong> — as applied economists. Scholars pursue a <strong>PhD in economics or public-policy-related fields</strong> at accredited Japanese universities and are expected to <strong>return to their government agency</strong> afterwards.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of an eligible Asian/Pacific country</strong> (India, Bangladesh, Nepal, Sri Lanka, Indonesia, Vietnam and others).</li>
        <li><strong>Employed as a government official</strong> involved in economic policymaking (central banks, finance ministries, planning agencies).</li>
        <li><strong>Nominated and supported by the employer</strong>; expected to return to the agency after the PhD.</li>
        <li><strong>Strong Master's degree</strong> or equivalent (16 years of education may be accepted with official explanation).</li>
        <li><strong>At least 2 years of public-sector work experience</strong> preferred; priority to applicants <strong>under 38</strong>.</li>
        <li><strong>English proficiency:</strong> TOEFL iBT 79–80 or IELTS 6.0+.</li>
        <li>Apply for admission to an <strong>accredited Japanese university</strong> offering a relevant PhD.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees.</strong></li>
        <li><strong>Monthly living stipend.</strong></li>
        <li><strong>Round-trip economy airfare.</strong></li>
        <li>Financial support for <strong>approved field research</strong> and <strong>international conferences</strong>.</li>
        <li>Access to <strong>IMF seminars and policy dialogues</strong>.</li>
      </ul>
      <div class="honest-note"><strong>Scholar only:</strong> the scholarship does not fund accompanying family members.</div>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Official employer nomination / support letter</li><li>Master's degree certificate + transcripts</li>
        <li>Proof of government employment and experience</li><li>Research proposal in economic policymaking</li>
        <li>English proficiency proof (TOEFL/IELTS)</li><li>Passport</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure your employer's nomination</strong>This is mandatory — start early.</li>
        <li><strong>Apply to a Japanese university PhD</strong>In economics or a policy-related field, for September/October 2027 or April 2028 intake.</li>
        <li><strong>Submit the JISPA application</strong>Window: <strong>1 May – 1 June 2027 (23:59 JST)</strong>. The AY2027-28 guidelines are posted by early March 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is India eligible?","Yes — India is on the JISPA eligible-countries list."),
 ("Do I need Japanese?","No — PhD programmes under this track are delivered in English; TOEFL/IELTS is required instead."),
 ("Must my employer nominate me?","Yes — nomination and support from your government agency is mandatory."),
 ("Does it cover my family?","No — funding covers the scholar only."),
]),
 verify='Verified 16 Oct 2026 against the official IMF JISPA PhD-track page (imf.org: window 1 May–1 Jun 2027, 23:59 JST; India eligible; employer nomination; return-to-agency; TOEFL 79-80/IELTS 6.0) and Bright Scholarship (same window and benefits).',
 offlinks=[('JISPA PhD track (IMF, official)','https://www.imf.org/en/countries/resrep/oap-home/jispa-home/phd-track')],
 related_titles=['swiss-phd','hanns-seidel','bloomberg-harvard'],
),

dict(
 slug='manchester-rolls-royce-phd-scholarship-2027',
 title='University of Manchester Rolls-Royce PhD Scholarship 2027 (Funded) | StudyDesk Scholarships',
 meta='Rolls-Royce PhD projects at the University of Manchester 2027: funded doctoral research in engineering. Deadline 8 Jan 2027.',
 short='Manchester Rolls-Royce PhD', kicker='UK · PhD · Engineering',
 mono='UoM', prov_short='University of Manchester', prov_long='University of Manchester with Rolls-Royce',
 h1='University of Manchester Rolls-Royce PhD Scholarship 2027',
 sub='Funded PhD projects in engineering and materials — tuition plus a tax-free stipend, with real industrial research experience.',
 dpill='84 days to go', dl_long='8 Jan 2027',
 facts=facts([('Award','Tuition + tax-free stipend<small>~£25,518/yr on some projects</small>'),
              ('Who can apply','First/2:1 graduates<small>Engineering, science, materials</small>'),
              ('Format','Individual PhD projects<small>Not one form — apply per project</small>'),
              ('Fee status','Varies by project<small>Some Home-only; check each advert</small>'),
              ('Deadline','8 Jan 2027<small>Advertised projects</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Rolls-Royce PhD Scholarship 2027</strong> is not one scholarship with one form — it is a set of <strong>funded, industry-linked PhD projects at the University of Manchester</strong>, run with Rolls-Royce (some with EPSRC support). Projects span <strong>aerospace, mechanical and electrical engineering, materials science, propulsion, energy systems and advanced manufacturing</strong>. Funded projects typically cover <strong>tuition fees plus an annual tax-free stipend</strong> (around £25,518 a year on current adverts).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>First-class or upper second-class degree</strong> in a relevant technical or scientific discipline (Master's where the project requires it).</li>
        <li>Suitable background in <strong>engineering, science or a related field</strong>; strong analytical and problem-solving skills.</li>
        <li>Relevant <strong>technical or research experience</strong> (programming, simulation, lab work).</li>
        <li><strong>English language</strong> to University of Manchester requirements.</li>
        <li>Meet the <strong>specific project's eligibility rules</strong>.</li>
      </ul>
      <div class="honest-note"><strong>Fee status matters:</strong> eligibility varies significantly by project — some Rolls-Royce adverts are restricted to <strong>UK/Home fee-paying students</strong>, while others are open internationally. Always confirm the fee conditions on the specific project listing before applying.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition fee support</strong> (where the project's fee eligibility is met).</li>
        <li><strong>Annual tax-free stipend</strong> — about £25,518 a year on current Manchester adverts.</li>
        <li><strong>Industrial research experience</strong> with Rolls-Royce and access to specialist research centres and labs.</li>
        <li>Academic supervision and research training.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Updated CV</li><li>Bachelor's and Master's transcripts</li>
        <li>Research proposal</li><li>References</li><li>English language evidence</li>
        <li>Evidence of research experience / publications</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Search the Manchester project database</strong>University of Manchester postgraduate research listings — search <strong>"Rolls-Royce"</strong>.</li>
        <li><strong>Read the full project advert</strong>Check the topic, required background, fee-status rules and deadline.</li>
        <li><strong>Contact the supervisor</strong>Where the advert recommends it.</li>
        <li><strong>Submit the online PhD application</strong>By <strong>8 January 2027</strong> for the advertised projects (some CDT rounds list 5 March / 14 May 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it fully funded?","Funded projects cover tuition plus a tax-free stipend — but the package varies by project, so read each advert."),
 ("Can international students apply?","Some projects can; some are Home-fee only. Check the fee-status line on the specific project advert."),
 ("Is there one application form?","No — you apply to individual PhD projects through Manchester's postgraduate research portal."),
 ("What is the deadline?","8 January 2027 for the currently advertised projects; some CDT rounds list later dates."),
]),
 verify='Verified 16 Oct 2026 via Bright Scholarship (8 Jan 2027; funded; project database route) and scholarpositions.com (project-level detail: fee-status varies — one project Home-only; stipend ~£25,518; CDT rounds 5 Mar / 14 May 2027).',
 offlinks=[('University of Manchester postgraduate research','https://www.manchester.ac.uk/study/postgraduate-research/')],
 related_titles=['swiss-phd','epfl-summer','hanns-seidel'],
),
]

from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.bad=False
    def handle_starttag(self,t,a):
        if t not in ('meta','link','br','img','input','hr','source'): self.stack.append(t)
    def handle_endtag(self,t):
        if self.stack and self.stack[-1]==t: self.stack.pop()
        else: self.bad=True

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    f = OUT / (a['slug'] + '.html')
    h = f.read_text(); p = P(); p.feed(h)
    issues = []
    if p.stack or p.bad: issues.append('parse')
    if 'wa.me/919905166009' not in h: issues.append('no-whatsapp')
    if 'href="#"' in h: issues.append('dead-link')
    if 'AICTE Pragati' in h and 'pragati' not in a['slug']: issues.append('template-text')
    if 'Lorem' in h: issues.append('lorem')
    print('wrote', a['slug'], n, 'bytes', '| issues:', issues if issues else 'none')
print('ALL DONE')

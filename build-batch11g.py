#!/usr/bin/env python3
"""Group G: 5 verified international articles. Verified 16 Oct 2026.
Skipped: Chevening British Fellowship (see report)."""
import pathlib, sys, re
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY)
CARDINFO.update({
 'emmir': dict(mono='EM', title='Erasmus Mundus EMMIR Scholarship 2027', href='erasmus-mundus-emmir-scholarship-2027.html',
              dpill='65 days to go', award='€1,400/month × 24 months', elig='First degree; relevant field; C1 English; any nationality.',
              tags=[('Master’s','blue'),('Europe','teal')]),
 'unil': dict(mono='UN', title="UNIL Master's Scholarship 2027", href='unil-masters-scholarship-2027-switzerland.html',
              dpill='16 days to go', award='CHF 1,600/month', elig='Foreign graduates; outstanding record; C1 French/English.',
              tags=[('Master’s','blue'),('Switzerland','teal')]),
 'sabanci': dict(mono='SU', title='Sabanci University Scholarship 2027', href='sabanci-university-scholarship-2027-turkey.html',
              dpill='42 days to go', award='Full tuition waiver + stipend', elig='International; Bachelor’s/Master’s/PhD; automatic consideration.',
              tags=[('UG/PG/PhD','blue'),('Turkey','teal')]),
 'qassim': dict(mono='QU', title='Qassim University Scholarships 2027', href='qassim-university-scholarships-2027-saudi-arabia.html',
              dpill='118 days to go', award='Route-dependent funding', elig='International; Master’s/PhD; GPA 4.50/4.25; age limits apply.',
              tags=[('Master’s/PhD','blue'),('Saudi Arabia','teal')]),
 'ustc': dict(mono='UC', title='USTC International Winter Camp 2027', href='ustc-international-winter-camp-2027-china.html',
              dpill='23 days to go', award='Fellowships for outstanding students', elig='Non-Chinese; UG/Master’s students or recent graduates.',
              tags=[('Short programme','blue'),('China','teal')]),
})

ARTICLES = [
dict(
 slug='erasmus-mundus-emmir-scholarship-2027',
 title='Erasmus Mundus EMMIR Scholarship 2027 | StudyDesk Scholarships',
 meta='Erasmus Mundus EMMIR Scholarship 2027: €1,400/month for 24 months for a two-year joint Master’s in Migration and Intercultural Relations. Deadline 20 Dec 2026.',
 short='Erasmus Mundus EMMIR 2027', kicker='Europe · Master’s · International',
 mono='EM', prov_short='European Union (Erasmus+)', prov_long='Erasmus+ Programme — EMMIR consortium, coordinated by the University of Oldenburg',
 h1='Erasmus Mundus EMMIR Scholarship 2027',
 sub='€1,400 a month for two years — a joint Master’s in Migration and Intercultural Relations across Europe, Africa and Asia.',
 dpill='65 days to go', dl_long='20 Dec 2026',
 facts=facts([('Award','€1,400 / month × 24<small>+ insurance + registration fees</small>'),
              ('Who can apply','First degree holders<small>Relevant field; min grade C+</small>'),
              ('English','C1 level<small>IELTS 6.5 listed; waivers exist</small>'),
              ('Deadline','20 Dec 2026<small>23:59 CET, via eMundus</small>'),
              ('Programme','2-year joint Master’s<small>Starts 1 Sep 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Erasmus Mundus EMMIR Scholarship 2027</strong> funds Edition 14 (2027–2029) of the <strong>European Master in Migration and Intercultural Relations (EMMIR)</strong>, a two-year Erasmus Mundus Joint Master’s coordinated by the <strong>University of Oldenburg, Germany</strong>, with partners in Norway, the Czech Republic, Slovenia, Ghana, Uganda, South Africa and India. Students begin in Oldenburg, continue in Stavanger (Norway), and complete an individual academic and internship pathway — including fieldwork options in Africa or Asia.</p>
      <p>Scholarship holders receive <strong>€1,400 per month for 24 months</strong>, plus health insurance and university registration fees. Around 15–20 full scholarships are awarded each year. Two other routes exist: <strong>non-fee-paying</strong> places (fees waived, living costs your own) and <strong>fee-paying</strong> places (€4,500 per semester).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>completed first university degree</strong> (bachelor’s or equivalent), with final grade <strong>C+ or equivalent</strong> — diploma and transcript required by the deadline.</li>
        <li>Degree in a <strong>related field</strong>: social sciences, history, cultural studies, education, law, economics, development studies or journalism.</li>
        <li><strong>Documented knowledge</strong> of migration studies, intercultural relations and empirical methods (modules, papers, essays or exam results).</li>
        <li><strong>English proficiency</strong> at C1 level (IELTS 6.5 listed in the programme’s test chart); waivers exist for documented English-medium study.</li>
        <li>Native English speakers must show <strong>proficiency in a second language</strong> relevant to migration studies.</li>
        <li>Applicants of <strong>all nationalities</strong> may apply; those who already hold an Erasmus Mundus Joint Master’s scholarship are <strong>not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€1,400 per month for 24 months</strong> (up to €33,600).</li>
        <li><strong>No participation (tuition) fee</strong>; health insurance and registration fees covered.</li>
        <li>Joint Master’s degree from an <strong>international university consortium</strong>.</li>
        <li>Selection by the consortium board considers academic qualifications, <strong>research/professional experience, motivation and language skills</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Valid passport</li><li>CV</li><li>Statement of Purpose (1–2 pages)</li>
        <li>Degree diploma and transcripts (with official English translations if needed)</li>
        <li>English-language proficiency proof</li>
        <li>Referee email addresses — referees submit references <strong>directly</strong></li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on eMundus</strong>Select “EMMIR APPLICATION edition 14 2027–2029” on the official application platform.</li>
        <li><strong>Complete the form in English</strong>Upload all documents as PDFs. Submit by <strong>20 December 2026, 23:59 CET</strong> — modifications are not possible after submission.</li>
        <li><strong>Wait for the selection board</strong>The board meets end of March 2027; notifications go out from <strong>early April 2027</strong>. Selected candidates submit certified hardcopies within 10 calendar days.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is EMMIR fully funded?","Only the scholarship tier: €1,400/month for 24 months plus insurance and fees. Travel, visas and residence permits come out of the stipend."),
 ("Do I need a migration studies degree?","No. Social sciences, history, cultural studies, education, law, economics, development studies and journalism all qualify — but you must document relevant knowledge."),
 ("Can I apply for a self-funded place?","Yes. Non-fee-paying places share the 20 December 2026 deadline; fee-paying places (€4,500/semester) are open until 15 July 2027, subject to availability."),
 ("When do I hear back?","Selection-board decisions are notified from early April 2027; reserve-list offers may follow in May or June 2027."),
]),
 verify='Verified 16 Oct 2026 via the official EMMIR application page at emmir.org (20 Dec 2026, 23:59 CET; €1,400/month × 24; eMundus; board meets end March 2027) and corroborating listings (daadscholarship.com, scholarpositions.com, scholarshipunion.com: same dates and amounts).',
 offlinks=[('EMMIR — Applying (official)','https://www.emmir.org/application-procedures')],
 related_titles=['hanns-seidel','swiss-phd','griffith-vc'],
),

dict(
 slug='unil-masters-scholarship-2027-switzerland',
 title='UNIL Master’s Scholarship 2027 in Switzerland | StudyDesk Scholarships',
 meta='UNIL Master’s Scholarship 2027: CHF 1,600/month for foreign graduates pursuing a Master’s at the University of Lausanne. Deadline 1 Nov 2026.',
 short='UNIL Master’s Scholarship 2027', kicker='Switzerland · Master’s · International',
 mono='UN', prov_short='University of Lausanne', prov_long='Université de Lausanne (UNIL), Switzerland',
 h1='UNIL Master’s Scholarship 2027 in Switzerland',
 sub='CHF 1,600 a month — for outstanding foreign graduates pursuing a Master’s at the University of Lausanne.',
 dpill='16 days to go', dl_long='1 Nov 2026',
 facts=facts([('Award','CHF 1,600 / month<small>10 months per year</small>'),
              ('Who can apply','Foreign graduates<small>Outstanding record; ~10 grants/yr</small>'),
              ('Language','C1 French or English<small>Per programme’s language</small>'),
              ('Deadline','1 Nov 2026<small>Midnight Swiss time</small>'),
              ('Fees','CHF 200 admin fee<small>+ CHF 80 per semester</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>UNIL Master’s Scholarship 2027</strong> (officially the UNIL Master’s Excellence Grant) is awarded by the <strong>University of Lausanne, Switzerland</strong> to around <strong>10 outstanding graduates of foreign universities</strong> each year. It pays <strong>CHF 1,600 per month</strong> for 10 months of each academic year (mid-September to mid-July), for the minimum statutory duration of the chosen Master’s programme.</p>
      <div class="honest-note"><strong>Important:</strong> UNIL states explicitly that this is <strong>not a fully funded scholarship</strong> — CHF 1,600 falls short of Lausanne’s living costs (roughly CHF 2,000+/month). Have additional funds lined up before committing.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>foreign university degree</strong> deemed equivalent to a Swiss bachelor’s (180 ECTS), obtained before the Master’s begins. Final-year students may apply with current transcripts.</li>
        <li><strong>Outstanding academic results</strong> — assessed holistically, with no published grade threshold.</li>
        <li><strong>C1 language level</strong> in the programme’s teaching language (French or English), with a certificate.</li>
        <li><strong>Never registered at UNIL</strong> before; students who already started a Master’s at UNIL are excluded.</li>
        <li>All nationalities eligible; <strong>no age limit</strong> (though higher age plus an existing Master’s can affect Swiss visa issuance — check with your Swiss representation).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CHF 1,600/month</strong>, 10 months per year, for the statutory programme duration.</li>
        <li><strong>Exemption from fixed course-registration fees</strong> (only CHF 80 per semester remains).</li>
        <li>Support navigating <strong>student housing and services</strong> (not funding for them).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application form (PDF upload)</li><li>Degree certificate + transcripts</li>
        <li>Language certificate (C1)</li><li><strong>Two recommendation letters</strong> — sent directly by referees to mastergrants@unil.ch</li>
        <li>Proof of <strong>CHF 200 administration fee</strong> payment</li>
        <li>Certified copies by post for applicants from countries outside the Lisbon Recognition Convention (postmarked by 1 Nov 2026)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose an eligible Master’s</strong>Check the programme’s language and entry conditions on UNIL’s site.</li>
        <li><strong>Pay the CHF 200 fee</strong>Non-refundable; include proof of payment.</li>
        <li><strong>Apply online before 1 Nov 2026</strong>The scholarship application <strong>doubles as your Master’s admission application</strong> — no separate application to the Admissions Office. Outcomes are notified in <strong>early April 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it fully funded?","No. UNIL explicitly says CHF 1,600/month does not cover Lausanne’s full living costs — plan additional funds."),
 ("Do I apply separately for admission?","No. The scholarship application also serves as your Master’s admission application."),
 ("Can final-year students apply?","Yes, with current transcripts — the qualifying degree must be completed before the Master’s begins."),
 ("What if I’m not selected?","If admitted to the programme, you’ll be offered registration as a regular (non-grant) student without paying the CHF 200 fee again."),
]),
 verify='Verified 16 Oct 2026 via UNIL’s official Master’s grants page at unil.ch (CHF 1,600/month; 1 Nov 2026 deadline; CHF 200 fee; application doubles as admission; ~10 grants) and corroborating listings (scholars4dev, leapscholar.com, opportunitiesnexus.com).',
 offlinks=[('UNIL Master’s grants (official)','https://www.unil.ch/unil/en/home/menuinst/etudier/mobilite-et-echange/etudiantes-et-etudiants-internationaux/etudiantes-internationaux-reguliers/bourse-de-master.html')],
 related_titles=['swiss-phd','epfl-summer','griffith-vc'],
),

dict(
 slug='sabanci-university-scholarship-2027-turkey',
 title='Sabanci University Scholarship 2027 in Turkey | StudyDesk Scholarships',
 meta='Sabanci University Scholarship 2027: full tuition waiver, monthly stipend and dormitory for international Bachelor’s, Master’s and PhD students in Istanbul. Deadline 27 Nov 2026.',
 short='Sabanci University Scholarship 2027', kicker='Turkey · Bachelor’s/Master’s/PhD · International',
 mono='SU', prov_short='Sabanci University', prov_long='Sabancı University, Istanbul, Türkiye',
 h1='Sabanci University Scholarship 2027 in Turkey',
 sub='Full tuition waiver, monthly stipend and dormitory — automatic scholarship consideration for every international applicant in Istanbul.',
 dpill='42 days to go', dl_long='27 Nov 2026',
 facts=facts([('Award','Full tuition waiver<small>+ monthly stipend + dormitory</small>'),
              ('Who can apply','International students<small>Bachelor’s, Master’s, PhD</small>'),
              ('Application','Automatic<small>No separate scholarship form</small>'),
              ('Deadline','27 Nov 2026<small>All programmes</small>'),
              ('Language','English-medium<small>TOEFL iBT unless exempt</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Sabanci University Scholarship 2027</strong> supports international students admitted to <strong>Sabancı University in Istanbul, Türkiye</strong> — a private research university whose programmes run entirely in English. Awards cover <strong>Bachelor’s, Master’s and PhD</strong> study across engineering and natural sciences, arts and social sciences, and the Sabancı Business School.</p>
      <p>There is <strong>no separate scholarship application</strong>: every international applicant who meets the admission requirements is automatically evaluated by the Scholarship Committee. Awards are limited and competition is keen — <strong>early applicants get priority consideration</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student</strong> from any country, applying for Bachelor’s, Master’s or PhD admission.</li>
        <li>Meet the <strong>academic admission requirements</strong> of the chosen programme.</li>
        <li>Selection is <strong>merit-based</strong>: academic background, transcripts, exam scores, reference letters, interview results and evidence of achievement (competition prizes, Olympiad certificates).</li>
        <li><strong>English proficiency</strong> (e.g. TOEFL iBT) unless exempted by institutional criteria.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee waiver</strong> for the regular duration of study.</li>
        <li><strong>Monthly stipend</strong> (reported: 2,500 TL/month for 10 months for Master’s; 3,000 TL/month for 12 months for PhD).</li>
        <li><strong>Dormitory accommodation</strong> for dormitory-scholarship recipients.</li>
        <li>Scholarship <strong>continues for the regular education period</strong> once awarded.</li>
      </ul>
      <div class="honest-note"><strong>Read the fine print:</strong> per the university’s own FAQ, the admission scholarship is a <strong>tuition waiver</strong> — a dormitory scholarship covers only a <strong>4-person room</strong>, and meals and personal expenses are not included. Award levels vary by candidate.</div>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online admission application</li><li>Academic transcripts</li><li>Exam results (as required by programme)</li>
        <li>Reference letters</li><li>English proficiency proof</li>
        <li>Evidence of academic achievement (competitions, Olympiads, prizes)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply on the official portal</strong>Undergraduate or graduate application — upload all achievement documents; you may also tick the scholarship-consideration option, though evaluation is automatic either way.</li>
        <li><strong>Submit before 27 Nov 2026</strong>Early submission improves scholarship chances.</li>
        <li><strong>Await one offer letter</strong>The scholarship decision arrives <strong>together with the admission offer</strong>, within several weeks.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate scholarship form?","No. All international applicants are automatically evaluated by the Scholarship Committee."),
 ("Is it really fully funded?","It is merit-based and tiered: the top tier waives tuition and adds stipend and dormitory. Lower tiers may cover tuition only — check your offer letter."),
 ("Does it cover meals?","No. The university states meals and personal expenses are not included."),
 ("How long does the scholarship last?","For the regular duration of your programme, provided you meet the university’s continuation rules."),
]),
 verify='Verified 16 Oct 2026 via Sabancı University’s official IRO scholarships page (iro.sabanciuniv.edu: automatic evaluation; limited awards; early applicants prioritised) and official FAQ (tuition-waiver basis; dormitory = 4-person room; meals excluded), plus corroborating listings (scholarinfo.net, opportunityportal.info: 27 Nov 2026 deadline).',
 offlinks=[('Sabancı IRO — Scholarships (official)','http://iro.sabanciuniv.edu/en/scholarships'),
           ('Sabancı FAQ — Scholarships (official)','https://www.sabanciuniv.edu/en/frequently-asked-questions')],
 related_titles=['griffith-vc','hanns-seidel','epfl-summer'],
),

dict(
 slug='qassim-university-scholarships-2027-saudi-arabia',
 title='Qassim University Scholarships 2027 in Saudi Arabia | StudyDesk Scholarships',
 meta='Qassim University Scholarships 2027: funded Master’s and PhD routes for international students in Saudi Arabia. Applications 27 Jan – 11 Feb 2027.',
 short='Qassim University Scholarships 2027', kicker='Saudi Arabia · Master’s/PhD · International',
 mono='QU', prov_short='Qassim University', prov_long='Qassim University, Kingdom of Saudi Arabia',
 h1='Qassim University Scholarships 2027 in Saudi Arabia',
 sub='Funded Master’s and PhD routes in Saudi Arabia — with an honest caveat: funding varies by route, so confirm your package before planning.',
 dpill='118 days to go', dl_long='11 Feb 2027',
 facts=facts([('Window','27 Jan – 11 Feb 2027<small>International applications</small>'),
              ('Who can apply','International students<small>Master’s and PhD</small>'),
              ('Grades','GPA 4.50 / 4.25<small>Theoretical / applied majors</small>'),
              ('Age limit','30 (Master’s) · 35 (PhD)<small>Per Ministry regulations</small>'),
              ('Funding','Route-dependent<small>Full, partial or paid</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Qassim University Scholarships 2027</strong> support international students in <strong>Master’s and PhD programmes</strong> at Qassim University, Saudi Arabia, as part of the country’s Vision 2030 research push. Applications for the 2027 cycle are reported to open <strong>27 January 2027</strong> and close <strong>11 February 2027</strong>.</p>
      <div class="honest-note"><strong>Read this before applying:</strong> these are <strong>not a single uniformly “fully funded” package</strong>. Saudi state universities offer <strong>full, partial and paid</strong> scholarship routes, and Qassim’s published information does not guarantee a living allowance for every admitted applicant. Confirm your exact funding route and package before making plans.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student</strong> applying for a Master’s or PhD programme.</li>
        <li>Qualifying degree from a <strong>recognised university</strong>.</li>
        <li><strong>Cumulative GPA of at least 4.50</strong> for theoretical majors, <strong>4.25</strong> for applied majors.</li>
        <li><strong>Age limits</strong> per Ministry regulations: <strong>30 for Master’s</strong>, <strong>35 for PhD</strong>.</li>
        <li>Choose the right route: applicants <strong>outside Saudi Arabia</strong> use the <strong>external scholarship</strong> route; residents without university sponsorship use the internal route.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full-route packages</strong> can include tuition waiver, <strong>monthly stipend</strong>, <strong>accommodation</strong>, healthcare and annual return airfare.</li>
        <li>Research support: labs, libraries and academic databases for thesis work.</li>
        <li>Packages <strong>vary by route</strong> — verify yours on the official listing for your intake.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed application form</li><li>Academic transcripts + degree certificate</li>
        <li>CV / resume</li><li>Personal statement</li><li>Valid passport</li>
        <li>Language test results (as required)</li><li>Medical evidence and attestations (route-dependent)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick your route</strong>Outside Saudi Arabia: external scholarship route via the national <strong>“Study in Saudi Arabia”</strong> platform. Confirm the intake listing names your programme.</li>
        <li><strong>Prepare documents early</strong>Attestations and medical evidence take time; have everything ready before <strong>27 January 2027</strong>.</li>
        <li><strong>Submit 27 Jan – 11 Feb 2027</strong>Details like passport numbers and names cannot be changed after submission.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it fully funded?","Not guaranteed. Qassim offers full, partial and paid routes — confirm which route and package your intake listing offers."),
 ("What are the age limits?","30 for Master’s and 35 for PhD applicants, per Ministry regulations."),
 ("How do I apply from India?","Through the external scholarship route on the national “Study in Saudi Arabia” platform, after checking Qassim’s graduate admissions pages for your programme."),
 ("Does admission mean funding?","No. Admission to Qassim does not automatically mean a full scholarship — funding depends on your route."),
]),
 verify='Verified 16 Oct 2026 via scholarpositions.com (11 Feb 2027 deadline; 27 Jan opening; age limits 30/35; route-dependent funding; external vs internal routes), brightscholarship.com (same window; route guidance) and scholarshipunion.com (document list; Study in Saudi platform). Funding is not uniformly fully funded — stated honestly above.',
 offlinks=[],
 related_titles=['griffith-vc','swiss-phd','nasa-hubble'],
),

dict(
 slug='ustc-international-winter-camp-2027-china',
 title='USTC International Winter Camp 2027 in China | StudyDesk Scholarships',
 meta='USTC International Winter Camp 2027: two-week academic camp in Hefei, China (19 Dec 2026 – 1 Jan 2027) with USTC Fellowships for outstanding students. Apply by 8 Nov 2026.',
 short='USTC Winter Camp 2027', kicker='China · Short programme · International',
 mono='UC', prov_short='USTC', prov_long='University of Science and Technology of China, Hefei',
 h1='USTC International Winter Camp 2027 in China',
 sub='Two weeks of lectures, national lab tours and Chinese language in Hefei — with USTC Fellowships for outstanding students.',
 dpill='23 days to go', dl_long='8 Nov 2026',
 facts=facts([('Dates','19 Dec 2026 – 1 Jan 2027<small>Hefei, China</small>'),
              ('Programme fee','3,000 CNY<small>Tuition + twin room + trips</small>'),
              ('Fellowship','For outstanding students<small>Travel, insurance, stipend</small>'),
              ('Who can apply','Non-Chinese citizens<small>UG/Master’s or graduates</small>'),
              ('Deadline','8 Nov 2026<small>UTC+8, online</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>USTC International Winter Camp 2027</strong> is a two-week, non-degree academic programme run by the <strong>University of Science and Technology of China (USTC)</strong> in <strong>Hefei</strong>, from <strong>19 December 2026 to 1 January 2027</strong>. Participants attend expert lectures, tour national laboratories, take daily Chinese lessons and join cultural site visits — a compact way to experience one of China’s top research universities.</p>
      <p>The standard <strong>programme fee is 3,000 CNY</strong>, covering tuition, twin-room accommodation and field trips. <strong>Outstanding students</strong> can receive a <strong>USTC Fellowship</strong> covering travel subsidy, medical insurance, accommodation and stipend — fully or partially.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizen</strong> with a valid foreign passport; good mental and physical health.</li>
        <li><strong>Good command of English</strong>.</li>
        <li><strong>Registered undergraduate or Master’s student</strong> — or a recent graduate wishing to continue learning at USTC.</li>
        <li>Applicants who <strong>already attended a USTC Winter or Summer Camp are not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Expert <strong>lectures</strong>, <strong>national lab tours</strong>, daily <strong>Chinese lessons</strong>, cultural site visits.</li>
        <li><strong>USTC Fellowship</strong> for outstanding students: travel subsidy, medical insurance, local accommodation and stipend, fully or partially.</li>
        <li>Invitation documents for the <strong>Chinese visa</strong> application.</li>
      </ul>
      <div class="honest-note"><strong>Costs to plan for:</strong> the 3,000 CNY fee does <strong>not</strong> include travel or insurance — self-funded unless you win a fellowship. Apply early: results, invitation letters and visa processing must all complete before 19 December.</div>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application form (fields marked * are required)</li>
        <li>Supporting documents as requested in the portal</li>
        <li>Valid passport</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on the USTC portal</strong>Log in and go to <strong>Start Application → Application → Non-Degree Programs Application → Winter Camp</strong>.</li>
        <li><strong>Complete and upload</strong>Fill every required field and upload documents.</li>
        <li><strong>Submit by 8 Nov 2026 (UTC+8)</strong>Questions: <strong>visiting@ustc.edu.cn</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the camp free?","No. The fee is 3,000 CNY (tuition, twin room, field trips). Travel and insurance are extra unless you receive a USTC Fellowship."),
 ("Who gets the fellowship?","Outstanding students, selected by USTC — it can cover travel, insurance, accommodation and stipend fully or partially. It is not guaranteed."),
 ("I attended a USTC summer camp before. Can I apply?","No — prior Winter or Summer Camp participants are ineligible."),
 ("When does the camp run?","19 December 2026 to 1 January 2027 in Hefei, China."),
]),
 verify='Verified 16 Oct 2026 via USTC International College’s official Winter Camp page at ic.ustc.edu.cn (8 Nov 2026 deadline UTC+8; 3,000 CNY fee; fellowship terms; visiting@ustc.edu.cn) and corroborating listings (openopportunities.org, scholarshipsedge.com).',
 offlinks=[('USTC International College — Winter Camp (official)','https://ic.ustc.edu.cn/?abroad=179')],
 related_titles=['epfl-summer','nasa-hubble','griffith-vc'],
),
]

written = []
for a in ARTICLES:
    build_article(BASE, OUT, a, CARDINFO)
    written.append(a['slug'])
    print('wrote', a['slug'])

# validation
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.bad=False
    def handle_starttag(self,t,attrs):
        if t not in ('meta','link','br','img','input','hr','source'): self.stack.append(t)
    def handle_endtag(self,t):
        if self.stack and self.stack[-1]==t: self.stack.pop()
        else: self.bad=True
bad=[]
for s in written:
    h=(OUT/(s+'.html')).read_text(); p=P(); p.feed(h)
    iss=[]
    if p.stack or p.bad: iss.append('parse')
    if 'AICTE Pragati' in h: iss.append('template')
    if 'Lorem' in h: iss.append('lorem')
    if 'href="#"' in h: iss.append('deadlink')
    if 'wa.me/919905166009' not in h: iss.append('nowa')
    if iss: bad.append((s,iss))
print('validation:', bad if bad else 'ALL CLEAN')

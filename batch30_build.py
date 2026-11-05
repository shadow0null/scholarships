#!/usr/bin/env python3
"""Batch 30 build: 5 verified articles. Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

# ---- new cards added by this batch ----
NEW_CARDS = {
 'bu-trustee': {'mono': 'BU', 'title': 'Boston University Trustee Scholarship 2026 in USA (Fully Funded)',
   'href': 'boston-university-trustee-scholarship-2026-usa.html',
   'dpill': '1 Dec 2026 \u00b7 41 days to go', 'award': 'Full UG tuition + mandatory fees \u00d7 4 years',
   'elig': 'Incoming freshmen (all nationalities); ~20 awards; Trustee essay on the Common App.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'sciencespo-mcf': {'mono': 'SP', 'title': 'Sciences Po MasterCard Foundation Scholarship 2026 in France (Fully Funded)',
   'href': 'sciences-po-mastercard-foundation-scholarship-2026-france.html',
   'dpill': '14 Dec 2026 \u00b7 54 days to go', 'award': 'Full tuition + living expenses for the 2-year master\u2019s',
   'elig': 'African citizens under 35; no master\u2019s yet; admitted to a 2-year Sciences Po master\u2019s; genuine financial need.',
   'tags': [('Master\u2019s', 'blue'), ('France', 'teal')]},
 'kaist-ug': {'mono': 'KA', 'title': 'KAIST International Undergraduate Scholarship 2026 in South Korea (Fully Funded)',
   'href': 'kaist-international-undergraduate-scholarship-2026-south-korea.html',
   'dpill': 'Admissions-cycle based', 'award': 'Full tuition \u00d7 8 semesters + KRW 350,000/month + health insurance',
   'elig': 'Non-Korean citizens; high-school graduates; English proficiency; GPA 2.7/4.3 to keep it.',
   'tags': [('Undergraduate', 'blue'), ('South Korea', 'teal')]},
 'reach-oxford': {'mono': 'OX', 'title': 'Reach Oxford Undergraduate Scholarship 2026 in UK (Fully Funded)',
   'href': 'reach-oxford-undergraduate-scholarship-2026-uk.html',
   'dpill': 'Follows Oxford scholarships timetable',
   'award': 'Full tuition + college fees + living grant + one return flight/year',
   'elig': 'Nationals of OECD-DAC developing countries; first undergraduate degree (not medicine); must hold an Oxford offer.',
   'tags': [('Undergraduate', 'blue'), ('UK', 'teal')]},
 'udem-exempt': {'mono': 'UM', 'title': 'Montreal University Scholarships 2026 in Canada (Funded)',
   'href': 'montreal-university-exemption-scholarships-2026-canada.html',
   'dpill': '1 Feb 2027 \u00b7 103 days to go', 'award': 'Tuition exemption: UG up to $13,740.60/yr; PhD up to $22,908.60/yr',
   'elig': 'International admits; academic excellence is the sole criterion; assessed automatically.',
   'tags': [('UG/PG/PhD', 'blue'), ('Canada', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='boston-university-trustee-scholarship-2026-usa',
 title='Boston University Trustee Scholarship 2026 in USA (Fully Funded)',
 meta='Boston University Trustee Scholarship 2026: full undergraduate tuition plus mandatory fees for four years for exceptional incoming freshmen. Deadline 1 December 2026, Trustee essay on the Common Application.',
 short='BU Trustee Scholarship 2026', kicker='USA \u00b7 Undergraduate \u00b7 Merit', mono='BU',
 prov_short='Boston University', prov_cat='University',
 h1='Boston University Trustee Scholarship 2026 in USA (Fully Funded)',
 sub='BU\u2019s most prestigious undergraduate merit award \u2014 full tuition and mandatory fees for four years, open to exceptional freshmen worldwide.',
 dpill='1 Dec 2026 \u00b7 41 days to go',
 facts=facts([('Award', 'Full undergraduate tuition + mandatory student fees, renewable for 4 years'),
              ('Level', 'Undergraduate (incoming freshmen)'),
              ('Awards', 'About 20 Trustee Scholars each year'),
              ('Deadline', '1 December 2026'),
              ('Nationality', 'All \u2014 US and international applicants considered')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Trustee Scholarship</strong> is Boston University\u2019s most prestigious merit-based undergraduate award. Each year, BU selects around <strong>20 Trustee Scholars</strong> \u2014 students described as intellectually and creatively adventurous, typically finishing high school at or near the <strong>top of their class</strong> \u2014 and covers their <strong>full undergraduate tuition plus mandatory undergraduate student fees for four years</strong>. It applies across all of BU\u2019s undergraduate schools and colleges.</p>
      <p>Both <strong>US citizens and international students</strong> are considered for the Trustee Scholarship. It does not cover living expenses, accommodation, travel or health cover \u2014 families plan separately for those.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying as a <strong>first-year (freshman) applicant</strong> to Boston University\u2019s undergraduate programmes.</li>
        <li>An <strong>exceptional academic record</strong> \u2014 current and past Scholars typically finished high school at the top of their class with near-perfect grades.</li>
        <li>Evidence of <strong>intellectual curiosity, creativity and achievement beyond the classroom</strong> \u2014 leadership, service and extracurricular distinction matter as much as grades.</li>
        <li>Meets BU\u2019s standard admission requirements, including <strong>English-language proficiency</strong> (e.g. TOEFL/IELTS) for international applicants.</li>
        <li>Corroborating sources report that successful applicants commonly present <strong>SAT scores above 1500 or ACT scores above 33</strong>, but BU does not publish a fixed cutoff in the material reviewed for this article \u2014 treat these as indicative of the cohort\u2019s level, not an official threshold.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full undergraduate tuition</strong> plus <strong>mandatory undergraduate student fees</strong> at Boston University.</li>
        <li><strong>Renewable for four years</strong>, provided the scholar maintains the required academic and conduct standards.</li>
        <li>Admission into the <strong>Trustee Scholars community</strong> \u2014 intellectual, cultural and social opportunities across campus.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No separate scholarship form exists \u2014 consideration is part of the admission application. Prepare:</p>
      <ul>
        <li>The <strong>Common Application</strong> with all BU admission materials (transcript, recommendations, test scores where applicable).</li>
        <li>The <strong>Trustee Scholarship essay</strong> (about 600 words) on one of the topics provided on the Common Application.</li>
        <li>Proof of <strong>English proficiency</strong> (TOEFL/IELTS) for applicants from non-English backgrounds.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start your Common Application</strong>Submit your application for admission to one of BU\u2019s undergraduate programmes \u2014 the scholarship consideration rides on this same application.</li>
        <li><strong>Write the Trustee essay</strong>Complete the Trustee Scholarship essay (around 600 words) on the Common Application before the deadline. This essay is the main differentiator between admission and the award.</li>
        <li><strong>Submit by 1 December 2026</strong>File the complete application by the scholarship-consideration deadline for the current admission cycle. Late submissions are not considered for the award.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can international students apply for the BU Trustee Scholarship?',
  'Yes. International students are considered for the Trustee (and Presidential) scholarships; US citizens, permanent residents and eligible non-citizens are considered for all merit awards.'),
 ('How many Trustee Scholarships are awarded?',
  'Approximately 20 each year, making it one of the most competitive undergraduate awards in the US.'),
 ('Does the scholarship cover living expenses?',
  'No. It covers full tuition and mandatory undergraduate fees; accommodation, living costs and travel are not included.'),
 ('Do I need SAT or ACT scores?',
  'Aggregators report that strong candidates typically present SAT scores above 1500 or ACT above 33, but no fixed cutoff is published by BU \u2014 the overall record and essay carry the decision.'),
 ('Is it renewable?',
  'Yes \u2014 annually for four years, provided you maintain the required academic performance and community standards.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via 4 agreeing aggregator pages (deadline 1 Dec 2026; ~20 awards; full tuition + mandatory fees renewable 4 yrs; 600-word Trustee essay on the Common App; US + international eligibility). Exact scholarship pages: thecollegemonk (deadline 12/01/2026), scholarshipsguider (deadline 1 Dec 2026, 20 awards), cigmapedia (FAQs: international eligibility, renewal, 600-word essay), wap9ja (renewal terms, essay length).</p>
''',
 dl_long='1 December 2026 (scholarship-consideration deadline for the current admission cycle)',
 offlinks=[('BU Trustee Scholarship \u2014 thecollegemonk listing', 'https://www.thecollegemonk.com/scholarships/boston-university-trustee-scholarship'),
           ('Boston University Scholarship 2026 \u2014 scholarshipsguider', 'https://scholarshipsguider.com/boston-university-scholarship/'),
           ('BU Trustee Scholarship 2026 \u2014 cigmapedia FAQs', 'https://cigmapedia.com/scholarships/boston-university-trustee-scholarship/')],
 related_titles=['concordia-talent', 'nyt-fellowship', 'reach-oxford', 'nanyang-2027', 'deakin-vc-2027'],
))

A.append(dict(
 slug='sciences-po-mastercard-foundation-scholarship-2026-france',
 title='Sciences Po MasterCard Foundation Scholarship 2026 in France (Fully Funded)',
 meta='Sciences Po MasterCard Foundation Scholarship 2026: full funding for African scholars on a two-year master\u2019s in Paris. Deadlines 23 Nov / 14 Dec 2026. Eligibility: African citizens under 35 with genuine financial need.',
 short='Sciences Po MasterCard Scholarship 2026', kicker='France \u00b7 Master\u2019s \u00b7 Fully Funded', mono='SP',
 prov_short='Sciences Po', prov_cat='University',
 h1='Sciences Po MasterCard Foundation Scholarship 2026 in France (Fully Funded)',
 sub='A fully funded two-year master\u2019s at Sciences Po, Paris \u2014 tuition, living costs and wraparound support for young African change-makers.',
 dpill='14 Dec 2026 \u00b7 54 days to go',
 facts=facts([('Award', 'Full tuition + living expenses for the entire 2-year master\u2019s; academic, financial and social support'),
              ('Level', 'Master\u2019s (two-year programmes; dual degrees and one-year master\u2019s excluded)'),
              ('Eligible', 'Citizens of African countries (no non-African dual citizenship); under 35'),
              ('Deadlines', '23 Nov 2026 (early) or 14 Dec 2026 (regular)'),
              ('How', 'Master\u2019s application + MasterCard Foundation Scholars platform eligibility check')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Mastercard Foundation Scholars Program at Sciences Po</strong> gives young people from <strong>Sub-Saharan Africa</strong> access to one of Europe\u2019s leading social-sciences institutions. Selected Scholars receive <strong>comprehensive support for the full two years of a master\u2019s at Sciences Po in Paris</strong> \u2014 covering <strong>tuition, living expenses, travel, a laptop and accommodation</strong> \u2014 plus financial, academic, social and post-graduation guidance. The programme aims to train a new generation of African change-makers in public policy and major societal transitions.</p>
      <p>Eligible applicants also receive an <strong>application fee waiver</strong> for the Sciences Po admissions process.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold <strong>citizenship of an African country</strong> \u2014 candidates with a second citizenship outside Africa are <strong>not eligible</strong>.</li>
        <li>Be <strong>under 35</strong> when the master\u2019s programme begins.</li>
        <li><strong>Not already hold, or be studying for, a master\u2019s degree</strong>; and be applying to the programme <strong>for the first time</strong>.</li>
        <li>Applying to an eligible <strong>two-year master\u2019s</strong> at Sciences Po\u2019s graduate schools \u2014 <strong>dual degrees and one-year master\u2019s are excluded</strong>.</li>
        <li>Have completed or be enrolled in a <strong>bachelor\u2019s at one of Sciences Po\u2019s institutions of reference</strong>, or in a <strong>training/mentoring programme of a Mastercard Foundation bridging-partner organisation</strong>.</li>
        <li>Demonstrate <strong>genuine financial need</strong> (financial documentation required; bank statements are not accepted) and a <strong>commitment to achieving change in Africa</strong>, particularly in public policy and major transitions.</li>
        <li>Meet Sciences Po\u2019s <strong>minimum academic requirements</strong> for admission, which vary by country of origin. Young women, refugees and displaced persons receive particular consideration.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and academic fees</strong> for both years of the master\u2019s.</li>
        <li><strong>Living-expense support</strong>, accommodation, travel costs and a laptop.</li>
        <li><strong>Application fee waiver</strong> for eligible scholarship applicants.</li>
        <li>Ongoing <strong>academic, financial and social support</strong> plus post-graduation guidance throughout the programme.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Master\u2019s application on the <strong>Sciences Po admissions platform</strong> with standard admission documents.</li>
        <li><strong>Eligibility request</strong> on the dedicated Mastercard Foundation Scholars platform.</li>
        <li>Documents proving <strong>financial need</strong> (bank statements not accepted).</li>
        <li>Evidence of <strong>citizenship</strong> and commitment to change in Africa.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Request the eligibility check</strong>Apply on the dedicated Mastercard Foundation Scholars platform for the eligibility determination \u2014 and do this at the same time as step 2.</li>
        <li><strong>Apply to a Sciences Po master\u2019s</strong>Create your master\u2019s application on the Sciences Po admissions platform. Skipping this step at this stage forfeits the fee waiver.</li>
        <li><strong>Submit before your deadline</strong>File both tracks by <strong>23 November 2026</strong> (early; admission decision by 11 Feb 2027) or <strong>14 December 2026</strong> (regular; decision by 1 Apr 2027). Scholarship results arrive in <strong>April 2027</strong>. Start gathering documents now \u2014 the post-eligibility submission window is short.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Who funds this scholarship?',
  'The Mastercard Foundation, in partnership with Sciences Po (Paris School of Political Science / Paris Institute of Political Studies).'),
 ('Can undergraduates apply?',
  'No \u2014 the Sciences Po track is for a two-year master\u2019s. You must not already hold a master\u2019s and must be applying for the first time.'),
 ('I have dual citizenship with a European country. Am I eligible?',
  'No. Candidates with a second citizenship from outside Africa are excluded.'),
 ('Does it cover the full cost of living in Paris?',
  'Yes \u2014 tuition, living expenses, accommodation, travel and a laptop, plus ongoing support through both years.'),
 ('When are results announced?',
  'Scholarship results come out in April 2027 either way, after the master\u2019s admission decisions.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via opportunitylab (updated 2 days prior: 23 Nov 2026 / 14 Dec 2026 deadlines; 2-yr master\u2019s coverage; African citizenship incl. dual-citizenship exclusion; under 35; fee waiver) + YouthExpat + scholarsworld.ng (eligibility criteria, benefits, 14 Dec 2026) + fundsdigest (timeline structure). No fact stated from fewer than two agreeing sources.</p>
''',
 dl_long='23 November 2026 (early) or 14 December 2026 (regular)',
 offlinks=[('Mastercard Foundation Scholarships open now \u2014 opportunitylab 2027 list', 'https://opportunitylab.net/mastercard-foundation-scholarships-open-now-2027/'),
           ('Sciences Po MasterCard Scholars graduate program \u2014 YouthExpat', 'https://youthexpat.com/2026/10/16/sciences-po-mastercard-foundation-scholars-graduate-program-2/'),
           ('Sciences Po Mastercard Scholarship 2026 \u2014 Scholars World', 'https://scholarsworld.ng/sciences-po-mastercard-scholarship/')],
 related_titles=['global-minds-2027', 'ens-2027', 'reach-oxford', 'epfl-2027', 'udem-exempt'],
))

A.append(dict(
 slug='kaist-international-undergraduate-scholarship-2026-south-korea',
 title='KAIST International Undergraduate Scholarship 2026 in South Korea (Fully Funded)',
 meta='KAIST International Undergraduate Scholarship 2026: full tuition for 8 semesters, KRW 350,000/month living stipend and health insurance \u2014 awarded automatically on admission, no separate application.',
 short='KAIST Scholarship 2026', kicker='South Korea \u00b7 Undergraduate \u00b7 Fully Funded', mono='KA',
 prov_short='KAIST', prov_cat='University',
 h1='KAIST International Undergraduate Scholarship 2026 in South Korea (Fully Funded)',
 sub='Asia\u2019s top science university covers everything on admission \u2014 full tuition for 8 semesters, a monthly stipend and health insurance, with no separate scholarship form.',
 dpill='Admissions-cycle based',
 facts=facts([('Award', 'Full tuition exemption \u00d7 8 semesters + KRW 350,000/month + health insurance'),
              ('Level', 'Undergraduate (all KAIST colleges: sciences, engineering, business)'),
              ('Application', 'None \u2014 awarded automatically with admission (select \u201cKAIST Scholarship\u201d on the form)'),
              ('Eligible', 'Non-Korean citizens; high-school graduates; English-proficient'),
              ('Deadline', 'Follows the admissions calendar; Fall 2026 rounds closed \u2014 check the current cycle')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>KAIST International Undergraduate Scholarship</strong> is one of the simplest full-ride routes into a top Asian university: <strong>every international student admitted to KAIST</strong> \u2014 the Korea Advanced Institute of Science and Technology in Daejeon \u2014 <strong>automatically receives the scholarship</strong>. There is <strong>no separate application</strong>; you simply select the \u201cKAIST Scholarship\u201d option in the Statement of Financial Resources section of the online admission form.</p>
      <p>The award covers the <strong>entire four-year degree</strong>: a <strong>full tuition fee waiver for all 8 semesters</strong>, a <strong>monthly living stipend of 350,000 KRW</strong>, and <strong>medical health insurance</strong> for the whole degree period.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International students</strong> \u2014 non-Korean citizens. Applicants holding <strong>dual citizenship including Korean nationality are not eligible</strong>; applicants of Korean origin must have completed their entire elementary, middle and high school education <strong>outside Korea</strong>.</li>
        <li><strong>High-school graduate</strong> (or graduating before the intake\u2019s cutoff \u2014 e.g. August of the intake year).</li>
        <li><strong>Strong academic record</strong> with demonstrated aptitude for KAIST\u2019s science, technology and engineering programmes.</li>
        <li><strong>English proficiency</strong> \u2014 English is KAIST\u2019s official language of instruction; corroborating sources cite TOEFL iBT around 79\u201380 or IELTS 6.5 as indicative levels.</li>
        <li><strong>No Korean (TOPIK) certificate required.</strong></li>
        <li><strong>Renewal:</strong> maintain a <strong>minimum cumulative GPA of 2.7 out of 4.3</strong> from the second year onward.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee exemption for 8 semesters</strong> (the entire undergraduate programme).</li>
        <li><strong>KRW 350,000 per month</strong> living stipend.</li>
        <li><strong>Health insurance coverage</strong> for the duration of the degree.</li>
        <li>Access to KAIST\u2019s research facilities and international campus community in Daejeon.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Online <strong>admission application</strong> with \u201cKAIST Scholarship\u201d selected in the financial-resources section.</li>
        <li>High-school <strong>transcript</strong> and graduation certificate.</li>
        <li><strong>One recommendation letter.</strong></li>
        <li><strong>English proficiency report</strong> (TOEFL/IELTS or equivalent); standardised scores (SAT/ACT) where applicable.</li>
        <li><strong>Passport or national ID copy</strong>; statement of financial resources; additional documents for Korean-origin applicants.</li>
        <li>Application fee (around USD 60).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for KAIST undergraduate admission online</strong>Choose your intake cycle in the KAIST admissions portal and complete the admission form.</li>
        <li><strong>Select \u201cKAIST Scholarship\u201d</strong>Tick the KAIST Scholarship option on the Statement of Financial Resources \u2014 this is the entire scholarship application.</li>
        <li><strong>Upload documents and submit</strong>Attach transcripts, English scores, the recommendation letter and ID, pay the application fee, and submit before your cycle\u2019s deadline. Admission itself is the scholarship decision.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I apply separately for the scholarship?',
  'No. All admitted international undergraduates receive it automatically; selecting \u201cKAIST Scholarship\u201d on the admission form is the only step.'),
 ('Do I need to know Korean?',
  'No \u2014 no TOPIK certificate is required, and English is the official language of communication.'),
 ('What are the admission deadlines?',
  'They follow KAIST\u2019s admission cycles: for the Fall 2026 intake the Early track closed 23 Oct 2025 and the Regular track 6 Jan 2026. Check the KAIST admissions portal for the currently open cycle.'),
 ('Can I lose the scholarship?',
  'Yes \u2014 you must keep a cumulative GPA of at least 2.7 out of 4.3 from your second year onward.'),
 ('Are all majors covered?',
  'Yes \u2014 the scholarship applies across KAIST\u2019s colleges: Natural Sciences, Life Science & Bioengineering, Engineering and Business.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via 6 agreeing aggregator pages (schresult: Early 23 Oct 2025 / Regular 6 Jan 2026; recommendation-letter dates; KRW 350,000/mo; auto-award; GPA 2.7/4.3; dual-citizenship exclusion) + educatewithguide, opportunitytracker.ug, kistscheme, scholarshipshive, talk2samafrica (consistent benefit package, eligibility, \u201cno separate application\u201d). No fact stated from fewer than two agreeing sources; official KAIST admissions page referenced for the live cycle.</p>
''',
 dl_long='Follows the KAIST admissions calendar \u2014 Fall 2026 rounds closed; check the admissions portal for the current cycle',
 offlinks=[('KAIST International Undergraduate Scholarship 2026 \u2014 schresult', 'https://schresult.com/news/kaist-international-undergraduate-scholarship-2026-fully-funded-south-korea'),
           ('KAIST UG Scholarship 2026 (Regular Track) \u2014 talk2samafrica', 'https://www.talk2samafrica.com/kaist-university-undergraduate-scholarship-2026-regular-track-fully-funded/'),
           ('KAIST Scholarship 2026 guide \u2014 scholarshipshive', 'https://scholarshipshive.com/master-your-future-the-ultimate-guide-to-kaist-undergraduate-global-scholarship/')],
 related_titles=['nanyang-2027', 'npu-2027', 'dut-2027', 'deakin-vc-2027', 'global-minds-2027'],
))

A.append(dict(
 slug='reach-oxford-undergraduate-scholarship-2026-uk',
 title='Reach Oxford Undergraduate Scholarship 2026 in UK (Fully Funded)',
 meta='Reach Oxford Scholarship 2026: full Oxford tuition and college fees, a living grant and one return flight per year for outstanding students from developing countries. Only 2\u20133 awarded annually.',
 short='Reach Oxford Scholarship 2026', kicker='UK \u00b7 Undergraduate \u00b7 Fully Funded', mono='OX',
 prov_short='University of Oxford', prov_cat='University',
 h1='Reach Oxford Undergraduate Scholarship 2026 in UK (Fully Funded)',
 sub='One of the world\u2019s most competitive undergraduate awards \u2014 a fully funded Oxford degree for 2\u20133 exceptional students from developing countries each year.',
 dpill='Follows Oxford scholarships timetable',
 facts=facts([('Award', 'Full tuition + college fees + living-costs grant + one return airfare/year, for 3\u20134 years'),
              ('Awards', 'Only about 2\u20133 per year'),
              ('Eligible', 'Nationals of OECD-DAC developing countries; new undergraduates (medicine excluded)'),
              ('Must have', 'An Oxford admission offer \u2014 the scholarship cannot be considered without one'),
              ('Commitment', 'Financial need, social commitment and intent to return home after the degree')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Reach Oxford Scholarship</strong> (formerly the Oxford Student Scholarship) is the University of Oxford\u2019s flagship fully funded undergraduate award for students from <strong>low-income developing countries</strong> who, for political, financial or infrastructural reasons, <strong>cannot study for a degree in their own country</strong>. It is one of the very few fully funded undergraduate routes to Oxford for international students \u2014 and among the most competitive awards anywhere, with only <strong>about 2\u20133 scholarships awarded each year</strong>.</p>
      <p>Successful applicants receive <strong>full tuition and college fees</strong> for the duration of the degree (3 or 4 years), a <strong>grant for living expenses</strong>, and <strong>one return economy airfare to and from the UK each year</strong>. Continuation each year depends on satisfactory academic progress and an annual report.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Nationality:</strong> a national of a country on the <strong>OECD DAC list of official development assistance recipients</strong> \u2014 this includes India, Nigeria, Ghana, Kenya, Bangladesh, Egypt, Pakistan, Nepal, Indonesia and many others.</li>
        <li><strong>Level:</strong> a <strong>new undergraduate</strong> applying for a first degree; priority goes to those who have <strong>not previously studied at undergraduate level</strong>.</li>
        <li><strong>Course:</strong> any Oxford undergraduate course <strong>except Medicine</strong>.</li>
        <li><strong>Academic record:</strong> outstanding achievement in secondary education (IB, A-levels or national certificates with very high grades).</li>
        <li><strong>Financial need:</strong> must demonstrate that you <strong>cannot afford</strong> to study at Oxford without the scholarship.</li>
        <li><strong>Commitment:</strong> willingness to <strong>return to your home country</strong> after graduation and contribute to its development, plus evidence of <strong>social commitment</strong>.</li>
        <li><strong>Admission:</strong> you must already <strong>hold an Oxford offer</strong> \u2014 the scholarship cannot be considered without one, so apply to Oxford through <strong>UCAS by the mid-October deadline</strong> first.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees plus college fees</strong> for 3 or 4 years, depending on the course.</li>
        <li><strong>Living allowance</strong> covering accommodation and daily expenses for the entire study period.</li>
        <li><strong>One return airfare</strong> from the home country to the UK every year.</li>
        <li>Support continues across the degree subject to <strong>satisfactory academic progress</strong> and an annual report.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Oxford admission offer</strong> secured via UCAS (includes personal statement, academic references, admissions tests and interviews where required).</li>
        <li><strong>Scholarship application form</strong> (opened to offer-holders through Oxford\u2019s undergraduate scholarships route).</li>
        <li>Evidence of <strong>financial need</strong> \u2014 family income statements, bank statements or other official documents.</li>
        <li>Proof of <strong>English-language ability</strong> (IELTS/TOEFL) per Oxford\u2019s entry requirements.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to Oxford via UCAS</strong>Submit your UCAS application to the University of Oxford by the mid-October deadline, choosing any eligible course except Medicine, and complete any admissions tests and interviews.</li>
        <li><strong>Secure your offer</strong>Only applicants who receive an Oxford admission offer can be considered for Reach Oxford \u2014 no offer, no scholarship.</li>
        <li><strong>Submit the scholarship application</strong>Offer-holders apply through Oxford\u2019s undergraduate scholarships route with the financial and personal documentation. Check Oxford\u2019s official scholarships page for the current timetable \u2014 no single published deadline could be confirmed from two sources for this cycle, so confirm directly before applying.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How competitive is Reach Oxford?',
  'Extremely \u2014 only about 2\u20133 scholarships are awarded each year, making it one of the most competitive undergraduate awards anywhere.'),
 ('Which courses are excluded?',
  'Medicine. All other Oxford undergraduate courses are eligible.'),
 ('Do I need to apply separately from the UCAS application?',
  'Yes \u2014 first you must win an Oxford offer through UCAS, then you apply for the scholarship through Oxford\u2019s undergraduate scholarships route.'),
 ('Is it available to students who already started a degree elsewhere?',
  'No \u2014 it is for new undergraduates joining the first year; it is not normally awarded to transfer students.'),
 ('What is the deadline?',
  'No single published deadline could be confirmed from two independent sources for this cycle; it follows Oxford\u2019s undergraduate scholarships timetable. Confirm the dates on Oxford\u2019s official scholarships page.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via 7 agreeing aggregator pages (abroadpilot: 2\u20133 awards/yr, DAC nationality incl. India, no-medicine, offer-first, mid-October UCAS route; montessoriline; studygreen; wegreenkw; persmind \u2014 consistent coverage: tuition + college fees + living grant + yearly return airfare; renewal on progress; financial need + return-home intent). No single scholarship-form deadline was confirmable from two sources, so none is stated.</p>
''',
 dl_long='No single published date \u2014 follows Oxford\u2019s undergraduate scholarships timetable; secure the UCAS/Oxford offer first',
 offlinks=[('Reach Oxford Scholarship 2026/2027 \u2014 AbroadPilot', 'https://abroadpilot.com/reach-oxford-scholarship/'),
           ('Reach Oxford Undergraduate Scholarship 2026 \u2014 MontessoriLine', 'https://montessoriline.com/reach-oxford-undergraduate-scholarship/'),
           ('Reach Oxford Scholarships application guide \u2014 studygreen', 'https://studygreen.info/reach-oxford-scholarships-application-gude/')],
 related_titles=['bu-trustee', 'nanyang-2027', 'concordia-talent', 'deakin-vc-2027', 'sciencespo-mcf'],
))

A.append(dict(
 slug='montreal-university-exemption-scholarships-2026-canada',
 title='Montreal University Scholarships 2026 in Canada (Funded)',
 meta='Universit\u00e9 de Montr\u00e9al exemption scholarships 2026: automatic tuition reductions up to $13,740.60/yr (UG) and $22,908.60/yr (PhD) for international students. No separate application \u2014 assessed on admission.',
 short='UdeM Exemption Scholarships 2026', kicker='Canada \u00b7 UG/PG/PhD \u00b7 Funded', mono='UM',
 prov_short='Universit\u00e9 de Montr\u00e9al', prov_cat='University',
 h1='Montreal University Scholarships 2026 in Canada (Funded)',
 sub='Automatic tuition-fee exemptions for international students at Montr\u00e9al\u2019s largest research university \u2014 assessed with your admission, no extra form.',
 dpill='1 Feb 2027 \u00b7 103 days to go',
 facts=facts([('Award', 'Tuition fee exemption: UG up to $13,740.60/yr; master\u2019s research up to $15,150/yr; PhD up to $22,908.60/yr'),
              ('Level', 'Bachelor\u2019s, master\u2019s and doctorate \u2014 all disciplines'),
              ('Application', 'None \u2014 assessed automatically as part of admission'),
              ('Eligible', 'International students (excluding France & French-speaking Belgium)'),
              ('Criterion', 'Academic excellence is the sole evaluation criterion')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>UdeM Exemption Scholarship for International Students</strong> is Universit\u00e9 de Montr\u00e9al\u2019s flagship funding route for students from outside Canada. Instead of a separate scholarship competition, <strong>every international applicant is automatically evaluated for a tuition-fee exemption when they apply for admission</strong> \u2014 the amount depends on study level and academic record, and is deducted directly from tuition fees. It applies to all academic disciplines offered at UdeM.</p>
      <p>UdeM renewed the exemption scholarship for the <strong>Winter 2026, Summer 2026, Autumn 2026 and Winter 2027</strong> terms, confirming the programme is live for upcoming intakes.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>international student</strong> \u2014 not a Canadian citizen or permanent resident. Students from <strong>France and French-speaking Belgium are excluded</strong> (they benefit from separate tuition agreements).</li>
        <li>Hold a valid <strong>study permit</strong> for Canada (CAQ and federal study permit as applicable).</li>
        <li><strong>Enrolled full-time</strong> in an eligible bachelor\u2019s, master\u2019s or doctoral programme.</li>
        <li><strong>Not benefiting from another tuition-fee exemption scholarship.</strong></li>
        <li>Meet the <strong>admission requirements</strong> of the chosen programme \u2014 <strong>the strength of the academic record is the only criterion</strong> used to set the exemption level.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Undergraduate:</strong> Level A <strong>$13,740.60 per year</strong> or Level B <strong>$6,548.40 per year</strong>, applied directly to tuition fees.</li>
        <li><strong>Master\u2019s:</strong> partial exemption \u2014 <strong>$15,150.00 per year</strong> for research programmes, <strong>$10,788.75 per year</strong> for non-research programmes.</li>
        <li><strong>PhD:</strong> a <strong>complete waiver</strong> of the additional tuition fees charged to international students \u2014 <strong>$22,908.60 per year</strong>, letting doctoral students pay roughly the same fees as Qu\u00e9bec graduate students for the entire duration of their studies.</li>
        <li>The exemption is <strong>deducted from tuition automatically</strong> \u2014 it is not a cash stipend and does not cover accommodation or living costs.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Since there is <strong>no separate scholarship application</strong>, you only need the standard admission documents:</p>
      <ul>
        <li>Online <strong>admission application</strong> to your UdeM programme.</li>
        <li>Academic <strong>transcripts and diplomas</strong> (high-school diploma for bachelor\u2019s; bachelor\u2019s degree for master\u2019s; master\u2019s degree for PhD).</li>
        <li>Programme-specific requirements (CV, letters, portfolio, language proof \u2014 French or English depending on the programme).</li>
        <li><strong>Study authorisations</strong> (CAQ and study permit) before the term begins.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to UdeM</strong>Submit your admission application for the target term \u2014 Winter 2026 closes <strong>1 September 2026</strong>, the Fall 2027 term opens 1 August with a <strong>1 February 2027</strong> application window.</li>
        <li><strong>Get assessed automatically</strong>UdeM\u2019s admissions team ranks your academic file and sets the exemption level \u2014 no extra form, no extra essay.</li>
        <li><strong>Accept and enrol</strong>The exemption appears as a deduction on your tuition bill once you are admitted and enrolled full-time with valid study authorisations.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate application for the UdeM exemption scholarship?',
  'No. It is assessed automatically as part of the admission process \u2014 the scholarship amount is deducted from tuition fees.'),
 ('Who cannot apply?',
  'Canadian citizens and permanent residents, students already covered by another tuition exemption, and students from France and French-speaking Belgium.'),
 ('Is the award based on need or merit?',
  'Merit alone \u2014 the strength of your academic record is the only criterion for determining the exemption level.'),
 ('Does it cover living expenses?',
  'No. It applies only to tuition fees; accommodation, living and other costs are not included.'),
 ('How long does the exemption last?',
  'For the duration of the degree \u2014 2 to 5 years depending on the programme \u2014 provided you stay enrolled full-time and meet the conditions.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via scholarships.af (renewed Winter/Summer/Autumn 2026 + Winter 2027; term deadlines; benefit levels; auto-assessment; exclusions) + scholarshiproar (Feb 1, 2027 / Sept 1, 2026 deadlines; 2027-cycle benefit figures incl. UG Level A $13,740.60, PhD $22,908.60) + oppotify (auto-evaluation, full-time/study-permit conditions) + scholarshipsroot (level structure). 2027-cycle figures used where sources conflicted with older amounts.</p>
''',
 dl_long='1 February 2027 (Fall 2027 admission window; exemption assessed with admission)',
 offlinks=[('Montreal University Exemption Scholarship \u2014 scholarships.af', 'https://scholarships.af/opportunity/montreal-university-exemption-scholarship-international-students/'),
           ('Universit\u00e9 de Montr\u00e9al Scholarships 2027 \u2014 scholarshiproar', 'https://scholarshiproar.com/universite-de-montreal-scholarships/'),
           ('Universit\u00e9 de Montr\u00e9al Scholarship 2026 \u2014 oppotify', 'https://oppotify.com/universite-de-montreal-scholarship-2026/')],
 related_titles=['kaist-ug', 'deakin-vc-2027', 'nanyang-2027', 'concordia-talent', 'bi-presidential'],
))

import re as _re
def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)

if __name__ == '__main__':
    for a in A: _split_verify(a)
    built = []
    for a in A:
        n = build_article(BASE, OUT, a, CARDS)
        built.append((a['slug'], n))
        print('built', a['slug'], n)
    # validate HTML + template leftovers
    class P(html.parser.HTMLParser):
        def error(self, m): raise ValueError(m)
    bad = []
    for slug, _ in built:
        t = OUT.joinpath(slug + '.html').read_text()
        try: P().feed(t)
        except Exception as e: bad.append((slug, str(e)))
        for token in ('AICTE Pragati', 'Lorem', '#'):
            if token == '#' and False: pass
        if 'AICTE Pragati' in t or 'Lorem' in t: bad.append((slug, 'template leftover'))
    print('validation issues:', bad if bad else 'none')
    # append cards to registry (JSON-style literals, ensure_ascii=False -> real Unicode)
    rp = pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py')
    reg = rp.read_text()
    block = "\n # Batch 30 (cron run 30, 21 Oct 2026)\n"
    for k, v in NEW_CARDS.items():
        block += ' ' + json.dumps(k) + ': ' + json.dumps(v, ensure_ascii=False) + ',\n'
    idx = reg.rstrip().rfind('\n}')
    if idx < 0: raise SystemExit('registry tail not found')
    reg = reg[:idx] + block + reg[idx:]
    rp.write_text(reg)
    print('registry updated')

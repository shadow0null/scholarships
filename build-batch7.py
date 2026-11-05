#!/usr/bin/env python3
"""Batch 7: 5 verified articles. Verified 16 Oct 2026. Skipped: Sree Community Youth Fellowship (unverifiable)."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'umbrella-tripura': dict(mono='NSP', title='Umbrella Scheme Post-Matric Scholarship for ST Students, Tripura 2026-27', href='umbrella-scheme-post-matric-st-tripura-2026-27.html',
              dpill='15 days to go', award='Up to Rs 1,200/month', elig='ST; Tripura domicile; Class 11+; income < Rs 2.5 lakh.',
              tags=[('ST','blue'),('Tripura','teal')]),
 'prematric-st-goa': dict(mono='NSP', title='Pre-Matric Scholarship for ST Students (Class 9 & 10), Goa 2026-27', href='nsp-pre-matric-st-goa-2026-27.html',
              dpill='15 days to go', award='Up to Rs 5,250/year', elig='ST; Goa domicile; Class 9–10; income < Rs 2.5 lakh.',
              tags=[('ST','blue'),('Goa','teal')]),
 'sakal-cds': dict(mono='SIF', title='Sakal India Foundation Career Development Scholarship 2026', href='sakal-india-foundation-career-development-scholarship-2026.html',
              dpill='15 days to go', award='Rs 5,000–10,000', elig='Indian resident; 85%+ in previous class; Class 11–PG; income proof.',
              tags=[('Merit','blue'),('Private','teal')]),
 'super50-aayam': dict(mono='A', title='Super 50 by AAYAM 2026-27 (NEET/JEE)', href='super-50-by-aayam-neet-jee-2026-27.html',
              dpill='20 days to go', award='Free coaching + hostel + up to Rs 3L/yr', elig='MP domicile; Class 10–12; NEET/JEE aspirants; income < Rs 12L.',
              tags=[('Coaching','blue'),('Madhya Pradesh','teal')]),
 'swiss-phd': dict(mono='CH', title='Swiss Government Excellence PhD Scholarships 2027-28', href='swiss-government-excellence-phd-scholarships-2027-28.html',
              dpill='25 days to go', award='CHF 2,450/month', elig='Master’s holders; research/PhD in Switzerland; born after 1991.',
              tags=[('PhD','blue'),('International','teal')]),
}

ARTICLES = [
dict(
 slug='umbrella-scheme-post-matric-st-tripura-2026-27',
 title='Umbrella Scheme Post-Matric Scholarship for ST Students, Tripura 2026-27 | StudyDesk',
 meta='Umbrella Scheme Post-Matric Scholarship for ST Students, Tripura 2026-27: maintenance up to Rs 1,200/month + fee reimbursement. Eligibility, deadline 31 Oct 2026.',
 short='Umbrella Post-Matric ST, Tripura', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via NSP)',
 h1='Umbrella Scheme Post-Matric Scholarship for ST Students, Tripura 2026–27',
 sub='Monthly maintenance up to Rs 1,200 plus fee reimbursement — for ST students of Tripura from Class 11 up.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 1,200 / month<small>+ fees, study tour, thesis grants</small>'),
              ('Who can apply','ST students<small>Tripura domicile; Class 11+</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Account','Aadhaar-linked bank<small>+ mobile number required</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Umbrella Scheme for Education of ST Children — Post-Matric Scholarship for ST Students, Tripura 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, gives financial assistance to <strong>Scheduled Tribe students of Tripura studying in Class 11 and above</strong> in recognised institutions. It is applied for on the National Scholarship Portal, and the Tripura Tribal Welfare Department implements it in the state.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of India</strong> and <strong>domicile of Tripura</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> category.</li>
        <li>Passed <strong>Class 10/12 or higher secondary</strong> from a recognised board/university; studying in <strong>Class 11 or above</strong>.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
        <li>Hold a <strong>bank account in a scheduled bank linked to Aadhaar</strong>, with a mobile number.</li>
        <li><strong>Not receiving any other scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly maintenance allowance up to Rs 1,200</strong> (hostellers; Rs 550 day scholars).</li>
        <li><strong>Reimbursement of compulsory non-refundable fees.</strong></li>
        <li><strong>Study tour charges</strong> up to Rs 1,600/year; <strong>thesis typing/printing</strong> up to Rs 1,600.</li>
        <li><strong>Annual book allowance</strong> Rs 1,200 for correspondence-course students.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Student photograph</li><li>ST category certificate</li><li>Income certificate (DDO/SDM as applicable)</li>
        <li>Last exam marksheet</li><li><strong>Affidavit of annual family income</strong> (submitted at the institute)</li>
      </ol>
      <div class="honest-note"><strong>Two copies:</strong> after applying on NSP, institutes ask for two printed copies of the form plus photocopies of the uploaded documents — keep them ready.</div>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Tripura + Umbrella Post-Matric ST scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
        <li><strong>Submit printouts at your institute</strong>Two copies with document photocopies.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Below Rs 2,50,000 per year of family income."),
 ("Can I apply if I get another scholarship?","No — you must not be receiving any other scholarship."),
 ("What documents are special here?","An affidavit of annual family income submitted at the institute, plus the standard certificates."),
 ("How is the money paid?","Through the NSP/DBT system to the Aadhaar-linked bank account."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Tripura listing (31 Oct 2026; up to Rs 1,200/month; ST; Tripura domicile; income < Rs 2.5L; Aadhaar-linked account), the Tripura Tribal Welfare Department official page (scheme components), and Techno College Agartala (documents + income affidavit).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['manipur-st','sikkim-sc','prematric-st-goa'],
),

dict(
 slug='nsp-pre-matric-st-goa-2026-27',
 title='Pre-Matric Scholarship for ST Students (Class 9 & 10), Goa 2026-27 | StudyDesk Scholarships',
 meta='Pre-Matric Scholarship for ST Students, Goa 2026-27: up to Rs 5,250/year + books grant. Eligibility, deadline 31 Oct 2026.',
 short='Pre-Matric ST, Goa', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via NSP)',
 h1='Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Goa 2026–27',
 sub='Up to Rs 5,250 a year plus a books grant — for ST students of Goa in Classes 9 and 10.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 5,250 / year<small>+ Rs 750–1,000 books grant</small>'),
              ('Who can apply','ST students<small>Goa domicile; Class 9–10</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Direct to bank account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Scheme of Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Goa 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, supports <strong>Scheduled Tribe students of Goa in Classes 9 and 10</strong> — cutting dropout in the move from elementary to secondary school. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domicile of Goa</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> community.</li>
        <li><strong>Regular full-time student in Class 9 or 10</strong> in a government school or a school recognised by the government / Central-State Board.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
        <li><strong>Not receiving any other centrally-funded pre-matric scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Scholarship for 10 months:</strong> Rs 2,250/year (day scholars) / Rs 5,250/year (hostellers).</li>
        <li><strong>Books and ad-hoc grant:</strong> Rs 750/year (day) / Rs 1,000/year (hostellers).</li>
        <li>Paid by <strong>DBT</strong> directly to the student's bank account.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Goa)</li><li>ST certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank details</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Goa + Pre-Matric ST scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Two scholarships?</strong> If awarded two simultaneously, choose one and communicate your choice through your institution's head.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much will I get?","Rs 2,250 per year as a day scholar or Rs 5,250 as a hosteller, plus the books grant."),
 ("What is the income limit?","Below Rs 2,50,000 per year of family income."),
 ("Which classes are covered?","Class 9 and Class 10."),
 ("Can I hold another pre-matric scholarship?","Not another centrally-funded one."),
]),
 verify='Verified 16 Oct 2026 via the Buddy4Study 2026-27 Goa listing (31 Oct 2026; Rs 2,250 day / 5,250 hostel per annum; Rs 750/1,000 books grant; ST; Goa domicile; income < Rs 2.5L).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['manipur-st','umbrella-tripura','sikkim-sc'],
),

dict(
 slug='sakal-india-foundation-career-development-scholarship-2026',
 title='Sakal India Foundation Career Development Scholarship 2026 | StudyDesk Scholarships',
 meta='Sakal India Foundation Career Development Scholarship 2026: Rs 5,000–10,000 for Class 11 to PG students with 85%+. Eligibility, deadline 31 Oct 2026.',
 short='Sakal India Foundation CDS', kicker='Private Foundation · Merit',
 mono='SIF', prov_short='Sakal India Foundation', prov_long='Sakal India Foundation, Pune',
 h1='Sakal India Foundation Career Development Scholarship 2026',
 sub='Rs 5,000 to Rs 10,000 a year — for brilliant students who can’t fully meet their education expenses.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 5,000 – 10,000 / year<small>By class level</small>'),
              ('Who can apply','85%+ scorers<small>Class 11 to PG; Indian resident</small>'),
              ('Need','Lower income group<small>Family income proof required</small>'),
              ('Deadline','31 Oct 2026<small>Fresh applications</small>'),
              ('Renewal','Till PG level<small>Yearly renewal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Career Development Scholarship (CDS)</strong> of the <strong>Sakal India Foundation, Pune</strong>, supports brilliant students who cannot fully meet their education expenses. It covers students from <strong>Class 11 through post-graduation</strong> — and once awarded, it can be <strong>renewed every year till PG level</strong>. Beyond money, scholars get mentorship and career guidance through the Foundation's network.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Resident of India</strong>, studying in India.</li>
        <li>Completed <strong>Class 10 or above</strong>; currently in <strong>Class 11, 12, diploma, UG or PG</strong> with a <strong>valid admission letter</strong>.</li>
        <li><strong>Minimum 85% aggregate</strong> in the previous class (10th/12th).</li>
        <li>Good record in <strong>co-curricular and extracurricular</strong> activities.</li>
        <li>From a <strong>lower family income group</strong> — family income proof required.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th>Level</th><th>Award</th></tr>
      <tr><td>Class 11</td><td>Rs 5,000</td></tr>
      <tr><td>Class 12</td><td>Rs 5,000</td></tr>
      <tr><td>Graduation</td><td>Rs 8,000</td></tr>
      <tr><td>Post-graduation</td><td>Rs 10,000</td></tr></table>
      <ul>
        <li><strong>Renewable every year</strong> till completion of post-graduation.</li>
        <li><strong>Mentorship and career guidance</strong> through the Foundation's professional network.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar card</li><li>Academic transcripts and certificates</li>
        <li><strong>Statement of Purpose</strong></li><li><strong>Letter(s) of recommendation</strong></li>
        <li>Family income proof</li><li>Co-curricular/extracurricular certificates</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Sakal India Foundation website</strong>sakalindiafoundation.com — Career Development Scholarship page.</li>
        <li><strong>Fill the online application</strong>With academic, income and activity details.</li>
        <li><strong>Upload documents</strong>Including SOP and recommendation letter(s).</li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Deadline note:</strong> 31 Oct 2026 is the fresh-application cycle date per the 2026 listing; the Foundation lists 31 March 2027 for renewals. Apply early.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I scored 84%. Can I apply?","No — the minimum is 85% aggregate in the previous class."),
 ("Is it only for Maharashtra students?","No — any Indian resident studying in India can apply."),
 ("Can I renew it?","Yes — every year till you complete post-graduation."),
 ("What is the award used for?","Tuition fees, books, study materials or other academic expenses."),
]),
 verify='Verified 16 Oct 2026 against the official Sakal India Foundation CDS page (85%+, Class 11–PG, Indian resident, income proof, co-curricular record) and the B4S 2026 listing (31 Oct 2026; Rs 5,000/5,000/8,000/10,000 by level; SOP + recommendation letters).',
 offlinks=[('Sakal India Foundation — CDS (official)','https://www.sakalindiafoundation.com/career-development-scholarship/')],
 related_titles=['isi-stipend','super50-aayam','icar-jrf'],
),

dict(
 slug='super-50-by-aayam-neet-jee-2026-27',
 title='Super 50 by AAYAM 2026-27: Free NEET/JEE Coaching Scholarship | StudyDesk',
 meta='Super 50 by AAYAM 2026-27: free NEET/JEE coaching + free hostel + up to Rs 3 lakh/year college scholarship for 50 MP students. Eligibility, exam dates.',
 short='Super 50 by AAYAM', kicker='Coaching Scholarship · Madhya Pradesh',
 mono='A', prov_short='AAYAM Career Institute', prov_long='AAYAM Career Institute, Indore',
 h1='Super 50 by AAYAM 2026–27',
 sub='Free NEET/JEE coaching, free hostel, and up to Rs 3 lakh a year for college — for 50 students of Madhya Pradesh.',
 dpill='20 days to go', dl_long='5 Nov 2026',
 facts=facts([('Award','Free coaching + hostel<small>+ up to Rs 3L/yr college</small>'),
              ('Who can apply','MP students<small>Class 10–12; NEET/JEE aspirants</small>'),
              ('Income limit','Rs 12 lakh / year<small>Family income</small>'),
              ('Register by','5 Nov 2026<small>Rs 50 registration fee</small>'),
              ('Exam','Phase 1: 22 Nov 2026<small>OMR; Hindi + English</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>MP Super 50 by AAYAM 2026–27</strong> is a scholarship-cum-coaching programme by <strong>AAYAM Career Institute, Indore</strong>, for NEET/JEE aspirants of Madhya Pradesh. The final <strong>50 students</strong> get <strong>coaching, school and hostel at zero cost</strong>, plus a scholarship of <strong>up to Rs 3 lakh per year</strong> for college.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Domicile of Madhya Pradesh.</strong></li>
        <li>Studying in <strong>Class 10, 11 or 12</strong>.</li>
        <li><strong>Aspiring for NEET or JEE.</strong></li>
        <li>Annual <strong>family income below Rs 12 lakh</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Free NEET/JEE coaching</strong> at AAYAM, Indore.</li>
        <li><strong>Free hostel</strong> for the final 50.</li>
        <li>Scholarship of <strong>up to Rs 3 lakh per year</strong> for college.</li>
        <li>Top 2,000 in Phase 1 qualify for the final round.</li>
      </ul>
      <h2 id="exam-pattern">Exam pattern</h2>
      <table><tr><th></th><th>Phase 1</th><th>Phase 2 (final)</th></tr>
      <tr><td>Date</td><td>22 Nov 2026</td><td>27 Mar 2027, Indore</td></tr>
      <tr><td>Level</td><td>District / city</td><td>State</td></tr>
      <tr><td>Questions</td><td>80</td><td>90</td></tr>
      <tr><td>Marks</td><td>320</td><td>360</td></tr>
      <tr><td>Duration</td><td>2:30 hours</td><td>3 hours</td></tr></table>
      <p><strong>Mode:</strong> OMR-based, in <strong>Hindi + English</strong>. Marking: <strong>+4 correct, −1 incorrect</strong>.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to mpsuper50.com</strong>The official Super 50 page.</li>
        <li><strong>Register for Rs 50</strong>Before <strong>5 November 2026</strong>.</li>
        <li><strong>Appear for Phase 1</strong>22 November 2026 at your district/city centre.</li>
        <li><strong>Final round</strong>Top 2,000 go to Indore on 27 March 2027; final 50 selected.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it only for MP students?","Yes — Madhya Pradesh domicile is required."),
 ("What does the final 50 get?","Free coaching, school and hostel, plus up to Rs 3 lakh per year for college."),
 ("What is the registration fee?","Rs 50 only."),
 ("What is the exam pattern?","OMR-based, Hindi + English, +4/−1 marking; Phase 1 has 80 questions (320 marks)."),
]),
 verify='Verified 16 Oct 2026 against the official mpsuper50.com (final 50 get free coaching/school/hostel + up to Rs 3L/yr; MP domicile; Class 10–12; income < Rs 12L; Rs 50 registration; Phase 1 on 22 Nov 2026; Phase 2 on 27 Mar 2027 in Indore) and aayamcareerinstitute.com (register till 5 Nov).',
 offlinks=[('MP Super 50 official page','https://www.mpsuper50.com/')],
 related_titles=['sakal-cds','isi-stipend','icar-jrf'],
),

dict(
 slug='swiss-government-excellence-phd-scholarships-2027-28',
 title='Swiss Government Excellence PhD Scholarships 2027-28 | StudyDesk Scholarships',
 meta='Swiss Government Excellence Scholarships 2027-28: CHF 2,450/month for PhD and research stays in Switzerland. Eligibility for Indians, deadline 10 Nov 2026.',
 short='Swiss Excellence Scholarships', kicker='Switzerland · PhD/Research',
 mono='CH', prov_short='Swiss Confederation', prov_long='Federal Commission for Scholarships (FCS/ESKAS), Switzerland',
 h1='Swiss Government Excellence Scholarships 2027–28',
 sub='CHF 2,450 a month to do your PhD or research in Switzerland — one of the world’s most generous government scholarships.',
 dpill='25 days to go', dl_long='10 Nov 2026',
 facts=facts([('Award','CHF 2,450 / month<small>+ housing, insurance, flights</small>'),
              ('Who can apply','Master’s holders<small>Research/PhD; born after 1991</small>'),
              ('Start','1 Sept 2027<small>12 months, extendable</small>'),
              ('Deadline','10 Nov 2026<small>India; 11:59 PM Swiss time</small>'),
              ('Note','No postdoc track<small>Discontinued for 2027–28</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Swiss Government Excellence Scholarships 2027–28</strong>, administered by the <strong>Federal Commission for Scholarships for Foreign Students (FCS/ESKAS)</strong>, fund <strong>PhD studies and research stays</strong> at Swiss public universities, federal institutes of technology (ETH Zurich, EPFL), universities of applied sciences and research institutes. For India, two categories are open: <strong>research fellowships and PhD scholarships</strong>. Applications opened 20 August 2026.</p>
      <div class="honest-note"><strong>2027–28 change:</strong> the postdoctoral scholarship track has been <strong>discontinued</strong> — only research fellowships and PhD scholarships are offered now (art scholarships remain for selected countries, not India).</div>
      <h2 id="eligibility">Eligibility (India)</h2>
      <ul>
        <li>Hold a <strong>Master's degree or equivalent</strong> (completed by 31 July 2027; 30 June 2027 for ETH Zurich).</li>
        <li><strong>Born after 31 December 1991.</strong></li>
        <li>For the <strong>research fellowship</strong>: a defined research project under a <strong>Swiss academic supervisor</strong> (6–12 months, non-renewable).</li>
        <li>For the <strong>PhD scholarship</strong>: full doctoral studies in Switzerland (12 months, extendable).</li>
        <li>Not already holding a Master's at scholarship start (art track rules); check the India country fact sheet.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CHF 2,450 per month</strong> living stipend.</li>
        <li><strong>One-time CHF 600 housing allowance.</strong></li>
        <li><strong>Health and accident insurance.</strong></li>
        <li><strong>Half-fare public transport card.</strong></li>
        <li><strong>Return flight allowance</strong> for non-EU/EFTA scholars.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>CV with education, awards and experience</li><li>Letter of motivation (max 2 pages)</li>
        <li>Research proposal / study plan</li><li>Supervisor confirmation from the Swiss host</li>
        <li>Two professors' email addresses (references)</li><li>Certificates, transcripts, passport copy</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find a Swiss supervisor</strong>Contact professors at your target university first.</li>
        <li><strong>Register on the ESKAS portal</strong>The Swiss government's online application system.</li>
        <li><strong>Submit before 10 November 2026</strong>11:59 PM Swiss local time (India deadline).</li>
        <li><strong>Decisions by end of May 2027</strong>Scholarship starts 1 September 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the India deadline?","10 November 2026, 11:59 PM Swiss local time."),
 ("Is the postdoc track available?","No — discontinued for 2027–28; only research fellowships and PhD scholarships."),
 ("Do I need a supervisor before applying?","Yes — identify and get approval from a Swiss academic supervisor first."),
 ("What does it cover?","CHF 2,450/month plus housing allowance, insurance, half-fare travel card and return flights."),
]),
 verify='Verified 16 Oct 2026 via EducationPost (India deadline 10 Nov 2026; CHF 2,450/month; research + PhD categories; opened 20 Aug 2026; FCS/ESKAS) and CareerAidHub (10 Nov 2026 11:59 PM Swiss time; postdoc discontinued; 12-month duration).',
 offlinks=[('EducationPost report','https://educationpost.in/news/education/scholarship/swiss-government-excellence-scholarships-open-for-202728')],
 related_titles=['nasa-hubble','bloomberg-harvard','icar-jrf'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')

import cards_registry
cards_registry.CARDS.update(CARDINFO)
pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').write_text(
    '"""Shared related-card registry for all scholarship articles. Append new batches here."""\n\nCARDS = ' + repr(cards_registry.CARDS) + '\n')

p = json.load(open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json'))
p['done'] += ['Umbrella Scheme Post-Matric Scholarships for ST Students, Tripura 2024-25',
 'Centrally Sponsored Scheme of Pre-Matric Scholarship for ST Students (Class 9 & 10), Goa 2026-27',
 'Sakal India Foundation Career Development Scholarship 2026',
 'Super 50 by AAYAM 2026-27', 'Swiss Government Excellence PhD Scholarships 2027-28']
p['skipped'] += [{'title': 'Sree Community Youth Fellowship 2026–27',
                  'reason': 'unverifiable — no trace of such a fellowship in search results'}]
p['runs'] = 7
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 7 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 31 | umbrella-scheme-post-matric-st-tripura-2026-27 | Umbrella Post-Matric ST, Tripura | 31 Oct 2026 | Yes — B4S/Tripura TWD |
| 32 | nsp-pre-matric-st-goa-2026-27 | Pre-Matric ST, Goa | 31 Oct 2026 | Yes — B4S |
| 33 | sakal-india-foundation-career-development-scholarship-2026 | Sakal India Foundation CDS | 31 Oct 2026 | Yes — SIF official/B4S |
| 34 | super-50-by-aayam-neet-jee-2026-27 | Super 50 by AAYAM | 5 Nov 2026 | Yes — mpsuper50.com official |
| 35 | swiss-government-excellence-phd-scholarships-2027-28 | Swiss Excellence PhD 2027-28 | 10 Nov 2026 | Yes — EducationPost/CareerAidHub |

Skipped: Sree Community Youth Fellowship (unverifiable).

**Completed: 35 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

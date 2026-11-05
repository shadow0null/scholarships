import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'navgurukul-prog-sarjapur': {'mono': 'NG', 'title': 'Navgurukul School of Programming Residential Programme (Sarjapur)',
   'href': 'navgurukul-school-of-programming-residential-programme-sarjapur.html',
   'dpill': 'Applications open (rolling)',
   'award': 'Fully funded residential programming course (stay, food, learning materials) with placement assistance.',
   'elig': 'Youth above 16 from low-income families; no prior education required on the current official page (older listings mention Class 10 and age 17).',
   'tags': [('Residential', 'purple'), ('Karnataka', 'teal')]},
 'nshm-asha': {'mono': 'NS', 'title': 'NSHM Knowledge Campus Asha Jyoti Scholarship 2025',
   'href': 'nshm-knowledge-campus-asha-jyoti-scholarship-2025.html',
   'dpill': 'Admission-linked (no separate deadline published)',
   'award': '25% to 100% fee waiver for UG and PG programmes, by merit, means or special category.',
   'elig': 'NSHM applicants: UG/PG marks tiers; means tier needs family income below Rs 2.5 lakh a year.',
   'tags': [('Merit-cum-Means', 'blue'), ('West Bengal', 'teal')]},
 'pmss-police': {'mono': 'PM', 'title': "NSP Prime Minister's Scholarship Scheme for Wards of States/UTs Police Personnel 2026-27",
   'href': 'nsp-prime-ministers-scholarship-scheme-for-wards-of-states-uts-police-personnel-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 2,500 a month for boys and Rs 3,000 a month for girls, paid annually; 500 scholarships a year.',
   'elig': 'Dependent wards of State/UT police personnel martyred in terror or Naxal attacks; 60%+ in the qualifying exam; first professional degree.',
   'tags': [('Police families', 'blue'), ('Central Govt', 'teal')]},
 'topclass-disab': {'mono': 'TC', 'title': 'NSP Scholarships for Top Class Education for Students with Disabilities 2026-27',
   'href': 'nsp-scholarships-for-top-class-education-for-students-with-disabilities-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Tuition reimbursement up to Rs 1.9 lakh a year + Rs 3,000 a month maintenance for hostellers (Rs 1,500 for day scholars).',
   'elig': 'Benchmark disability of 40% or more; graduate, postgraduate or diploma course at a notified Institute of Excellence; family income up to Rs 8 lakh.',
   'tags': [('Disability', 'blue'), ('Central Govt', 'teal')]},
 'nurtr-50': {'mono': 'N', 'title': 'nurtr Nurturing Minds with Chess Program (50% fee waiver)',
   'href': 'nurtr-nurturing-minds-with-chess-program-50-fee-waiver-2025-26.html',
   'dpill': 'No fixed deadline published',
   'award': '50% fee waiver: the nurtr Neo chess course for Rs 4,999 (family income Rs 8–15 lakh a year); a 90% tier at Rs 1,000 covers incomes below Rs 8 lakh.',
   'elig': 'Indian school or college students aged 5 to 25.',
   'tags': [('Chess', 'purple'), ('Skill course', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. NavGurukul School of Programming, Sarjapur
ARTICLES.append({
 'slug': 'navgurukul-school-of-programming-residential-programme-sarjapur',
 'title': 'Navgurukul School of Programming Residential Programme (Sarjapur)',
 'meta': 'NavGurukul School of Programming Residential Programme at Sarjapur: a fully funded residential programming course with stay, food and placement assistance. Admissions are rolling; the current official page asks only for age above 16 and no prior education.',
 'short': 'Navgurukul School of Programming Residential Programme (Sarjapur)',
 'kicker': 'Karnataka · Residential Programme',
 'mono': 'NG',
 'prov_short': 'NavGurukul',
 'prov_cat': 'Non-profit · India',
 'h1': 'Navgurukul School of Programming Residential Programme (Sarjapur)',
 'sub': 'NavGurukul’s School of Programming at Sarjapur, Karnataka, is the programming track of its residential programme: a fully funded, live-on-campus course that teaches software engineering to young people from low-income families and then helps them into jobs. It is not a cash scholarship and it is not a college degree — it is a place to live, learn to code, and leave with work. Admissions run on a rolling basis rather than a fixed annual deadline, and the current official criteria are simpler than older listings suggest, so both versions are stated openly below.',
 'dpill': 'Applications open (rolling)',
 'facts': facts([
   ('Provider', 'NavGurukul, a non-profit founded in 2016 that runs fully funded residential campuses for learners from underserved communities'),
   ('Award', 'A fully funded residential programming course: accommodation, meals and learning materials are covered, with placement assistance into software jobs on completion'),
   ('Duration', 'One year in the older programme listings; the current official residential-programmes page describes its residential programmes as lasting 1 to 2 years'),
   ('Deadline', 'No single deadline published — admissions happen on a rolling basis, with a new student enrolled as a placed student leaves'),
   ('Eligibility', 'Youth above 16 years of age from underprivileged or low-income families who cannot afford expensive college education; no prior education is required on the current official page (older listings describe Class 10 completion and age 17 — see the note below)'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>NavGurukul is a non-profit founded in 2016 whose stated mission is to give students from marginalised communities access to aspirational careers. Its flagship offering is a residential programme: students live on campus, learn in a self-paced, peer-learning style, and take part in running the campus through elected student bodies. The Sarjapur campus in Karnataka is one of those residential centres, and its programming track is the course this article covers. It is distinct from the School of Business track that also runs at Sarjapur, which teaches business and digital-marketing skills instead of programming.</p>
      <p>Older programme listings describe Sarjapur as one of the girls’ campuses, alongside Pune and Bangalore, with Dharamshala as the boys’ campus. The current official residential-programmes page does not label individual campuses by gender, so this article does not assert the Sarjapur campus’s present gender composition — check the official page or the application form before applying. What the current page does state is the scale of the operation: nine campuses with a combined capacity of around 1,100 students, and more than 1,500 students placed into jobs.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A fully funded residential course: the programme covers accommodation, meals and learning materials, so the student does not pay tuition or living costs while studying.</li>
        <li>Programming training aimed at employment, with English and personality-development training alongside the technical curriculum in the older programme descriptions.</li>
        <li>Placement assistance on completion: the organisation’s placement material reports 1,500+ students placed, at salaries reported between Rs 2.4 lakh and Rs 8.5 lakh a year, with 120+ hiring partners.</li>
        <li>A self-governed campus community: students manage campus responsibilities through a student council system, which the organisation presents as part of the learning itself.</li>
      </ul>
      <p>One honest clarification: older programme material promises a guaranteed job, and one older description promises a minimum salary of Rs 20,000 a month. The current official material speaks of placement assistance and reports a salary range rather than a guarantee. Treat the outcome as strong placement support, not a contractual job guarantee.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are above 16 years of age. This is the age rule on the current official residential-programmes page, and it is the rule this article follows.</li>
        <li>You come from an underprivileged or low-income family and cannot afford expensive college education. The organisation’s mission pages describe its learners as students from marginalised communities.</li>
        <li>No prior education is required on the current official page: its students have included school and college dropouts, Class 10 and Class 12 pass students, and degree holders who could not get jobs.</li>
        <li>You can live residentially at the Sarjapur campus for the programme’s duration and take part in its self-governed community life. This is a full-time, on-campus commitment, not a remote or part-time course.</li>
      </ul>
      <p>A note on the older criteria, because they still circulate widely. Older listings for this programme say it is open to students who have finished Class 10 and are 17 years of age, and older profiles put the family-income bar at below Rs 10,000 a month (one older profile says below Rs 8,000). Those figures come from earlier years of the programme. The current official page’s criteria — above 16, no prior education needed — are less restrictive, and this article follows the current page. If you are below 17 or have not finished Class 10, the current criteria still leave you eligible; confirm on the application form, since that form governs admission.</p>
      <h2 id="admission">Admission process</h2>
      <p>Admissions happen on a rolling basis: the organisation’s placement material states that as soon as a student gets placed, a new student is enrolled. There is no published annual closing date. The admission experience described by a student account runs in rounds: an online application, followed by an algebra round, an English round, and a culture-fit round in which the applicant submits a short video introducing themselves and explaining why they want to join. The organisation’s school pages for the related tracks describe the same shape — a screening test, an academic interview and a culture-fit round — ending in an offer letter sent by email. Expect a test-and-interview process rather than a marks-based selection, and expect to be assessed on willingness to work hard and learn, which the older programme posters state explicitly.</p>
      <h2 id="documents">Documents required</h2>
      <p>No document checklist for the Sarjapur programming programme is published on the official NavGurukul pages checked, so none is invented here. The admission process is test- and interview-based rather than document-based. Keep an identity proof, proof of your family-income situation and your previous education records (if any) ready, and follow whatever the application form asks for, since that form governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official NavGurukul residential-programmes page in full, including the Sarjapur campus listing and the residential commitment, and decide honestly whether living on campus fits your life.</li>
        <li>Start the enrolment process through the official NavGurukul page and choose the School of Programming at Sarjapur.</li>
        <li>Complete the screening and interview rounds described above, including the culture-fit round.</li>
        <li>If you pass, you receive an offer letter confirming selection for the residential course, sent by email.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a scholarship that pays money?', 'No. It is a fully funded residential programme: stay, food and learning materials are covered, and you receive placement assistance. No cash award is paid to the student.'),
   ('Do I need to have passed Class 10?', 'Not on the current official criteria, which require only age above 16 and no prior education. Older listings mention Class 10 and age 17; the current page is less restrictive and is the one this article follows.'),
   ('Is there a deadline for the Sarjapur campus?', 'No single deadline is published. Admissions are rolling, so check the official page for the next Sarjapur cohort.'),
   ('Is Sarjapur a girls-only campus?', 'Older programme listings describe Sarjapur as one of the girls’ campuses. The current official page does not label campuses by gender, so confirm the position on the application form before applying.'),
   ('How is this different from the School of Business at Sarjapur?', 'The School of Programming teaches software engineering; the School of Business teaches Google Suite, CRM and Salesforce, digital marketing and data analytics. Both are fully funded residential programmes at the same campus.'),
   ('Is a job guaranteed?', 'Older material promised a guaranteed job, but current official material reports placement assistance with 1,500+ students placed. Treat it as strong placement support, not a guarantee.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the NavGurukul placement deck (Sarjapur listed among residential campuses; rolling admissions as placed students leave; 9 campuses, around 1,100 capacity; 1,500+ placed at Rs 2.4–8.5 lakh a year), the Smart Village Movement programme page (Sarjapur as a girls’ campus in older listings; free one-year programme including food, hostel and travel; guaranteed-job wording in older material), a student admission-experience account (algebra, English and culture-fit rounds), and the official residential-programmes page criteria used in the previous batch (above 16, no prior education required, fully funded 1–2 years). Gender labelling and the older Class 10/age 17 criteria are flagged as older-versus-current differences, not hidden.',
 'dl_long': 'Applications open on a rolling basis — no single deadline published on the official pages',
 'offlinks': [('NavGurukul — Residential Programs (official)', 'https://www.navgurukul.org/residentialprograms'), ('Buddy4Study — Navgurukul School of Programming Residential Programme (Sarjapur)', 'https://www.buddy4study.com/scholarship/navgurukul-school-of-programming-residential-programme-sarjapur'), ('Smart Village Movement — NavGurukul Meraki programme page', 'https://smartvillagemovement.org/meraki-from-navgurukul/')],
 'related_titles': ['navgurukul-pune', 'navgurukul-business-sarjapur', 'balmiki-2026', 'nsp-pg-2026'],
})

# 2. NSHM Asha Jyoti Scholarship 2025
ARTICLES.append({
 'slug': 'nshm-knowledge-campus-asha-jyoti-scholarship-2025',
 'title': 'NSHM Knowledge Campus Asha Jyoti Scholarship 2025',
 'meta': 'NSHM Knowledge Campus Asha Jyoti Scholarship 2025: a 25% to 100% fee waiver for UG and PG students at NSHM, by merit, means or special category. Apply through the NSHM admission form; keep a 6.75 CGPA and 75% attendance to retain it.',
 'short': 'NSHM Knowledge Campus Asha Jyoti Scholarship 2025',
 'kicker': 'West Bengal · Institute Scholarship',
 'mono': 'NS',
 'prov_short': 'NSHM Knowledge Campus',
 'prov_cat': 'Private Institute · West Bengal',
 'h1': 'NSHM Knowledge Campus Asha Jyoti Scholarship 2025',
 'sub': 'The Asha Jyoti Scholarship is NSHM Knowledge Campus’s own fee-waiver scheme for students joining its undergraduate and postgraduate programmes in Kolkata and Durgapur. It is not a government scholarship and it is not applied for separately: you claim it through the NSHM admission form, and the waiver — between a quarter and the whole fee — depends on which of its three categories you fit. There is no separate published deadline, because the scholarship rides on the admission cycle itself.',
 'dpill': 'Admission-linked (no separate deadline published)',
 'facts': facts([
   ('Provider', 'NSHM Knowledge Campus (Kolkata and Durgapur campuses), West Bengal'),
   ('Award', 'A fee waiver ranging from 25% to 100% of fees, depending on category and academic record, for undergraduate and postgraduate programmes'),
   ('Categories', 'Asha Jyoti Merit Scholarship, Asha Jyoti Means Scholarship and Asha Jyoti Special Category Scholarship, plus the Asha Jyoti Unnati route for NSHM undergraduates moving to a postgraduate programme'),
   ('Deadline', 'No separate deadline published — apply through the NSHM admission form and select the Asha Jyoti category you are eligible for'),
   ('Eligibility', 'UG and PG applicants meeting the marks tiers below; the means tier needs a yearly family income below Rs 2.5 lakh; the special category covers differently abled students, state-level sportspersons and wards of teachers, defence personnel or single mothers'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>NSHM Knowledge Campus is a private institute group with campuses in Kolkata and Durgapur, West Bengal. Its Asha Jyoti Scholarship Scheme is the institute’s own fee-waiver programme, introduced to mark a decade of scholarship awards at NSHM and expanded into four categories. Unlike a government scheme on the National Scholarship Portal, it is claimed at admission: the scholarship field on the NSHM application form is where you select the Asha Jyoti category you are eligible for. The waiver applies to the institute’s fee, and the institute’s own scholarship pages are the governing source for the current year’s terms.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A fee waiver from 25% to 100%, based on past academic performance, for undergraduate and postgraduate programmes at NSHM.</li>
        <li>Four routes within the scheme: merit, means, special category, and Asha Jyoti Unnati for existing NSHM students upgrading from an undergraduate to a postgraduate programme.</li>
        <li>The waiver is a fee concession at NSHM, not a cash payment: it reduces what you owe the institute rather than paying money into your account.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <p>The eligibility tables published for NSHM Kolkata’s Asha Jyoti categories work in tiers. The marks quoted are the previous qualifying examination’s marks, and the three rows below are the three published tiers, not three separate scholarships:</p>
      <ul>
        <li>Top tier: 70% for undergraduate programmes and 60% for postgraduate programmes, with no additional condition stated for the merit category.</li>
        <li>Middle tier: 60% for undergraduate programmes and 50% for postgraduate programmes, combined with a yearly family income below Rs 2.5 lakh for the means category.</li>
        <li>Entry tier: 50% for undergraduate programmes and 45% for postgraduate programmes, for the special category — differently abled students, sports students holding state-level medals, certificates or trophies, and wards of teachers, defence professionals or single mothers.</li>
      </ul>
      <p>For master’s degree courses the scholarship is calculated on overall graduation marks, for lateral-entry courses on overall diploma marks, and for Class 12 marks on the best of five subjects across all boards. Existing NSHM students upgrading from an undergraduate to a postgraduate programme apply under Asha Jyoti Unnati.</p>
      <h2 id="conditions">Keeping the scholarship</h2>
      <ul>
        <li>Maintain a CGPA of 6.75 or above along with 75% attendance in every semester. This is the Asha Jyoti maintenance rule published for NSHM; a different NSHM academic scholarship uses a 7 CGPA bar, so do not confuse the two.</li>
        <li>Keep a clean academic record with no backlogs, and do not receive any letter for disciplinary action.</li>
        <li>Clear college or university fees on or before the due dates.</li>
        <li>Do not conceal or misstate any fact in the application.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Original transcripts of Class X and Class XII are mandatory for undergraduate applicants, and original undergraduate transcripts for postgraduate applicants. Where the means category applies, a family income certificate obtained from an A1 gazetted officer is required. Defence-personnel wards need the parent’s valid government photo identity card or dependent card plus proof of relation. Follow the document list shown on the NSHM admission form, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the NSHM admissions and scholarships pages and confirm the Asha Jyoti categories open for the programme you want.</li>
        <li>Fill in the NSHM admission form for your chosen undergraduate or postgraduate programme.</li>
        <li>In the scholarship field on the form, select the Asha Jyoti category you are eligible for — merit, means, special category or Unnati.</li>
        <li>Upload or present the transcripts and, where applicable, the income or category certificates listed above, and complete admission within the institute’s admission cycle.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much of the fee is waived?', 'Between 25% and 100%, depending on your category and academic record. The exact waiver for your marks is decided by NSHM at admission.'),
   ('Is there a separate application or deadline?', 'No separate deadline is published. You apply through the NSHM admission form and select the Asha Jyoti category there, so the institute’s admission cycle is the effective deadline.'),
   ('What marks do I need?', 'The published tiers are 70%/60%/50% for undergraduate programmes and 60%/50%/45% for postgraduate programmes, with the middle tier tied to family income below Rs 2.5 lakh a year and the entry tier tied to the special categories.'),
   ('What do I need to keep the waiver?', 'A CGPA of 6.75 or above with 75% attendance every semester, no backlogs, no disciplinary letter, and fees paid on time.'),
   ('Is this a government scholarship?', 'No. It is NSHM Knowledge Campus’s own institute scholarship, claimed at admission. It is not applied for on the National Scholarship Portal.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Careers360 NSHM Knowledge Campus Kolkata page (Asha Jyoti merit, means and special-category eligibility tables: UG 70/60/50%, PG 60/50/45%, family income below Rs 2.5 lakh, differently abled, state-level sportspersons, wards of teachers/defence professionals/single mothers) and the Shiksha NSHM Durgapur scholarship listing (25% to 100% fee waiver; 6.75 CGPA plus 75% attendance to maintain Asha Jyoti; original Class X and XII transcripts mandatory; income certificate from an A1 gazetted officer; best-of-five Class 12 calculation; Asha Jyoti Unnati for UG-to-PG upgrades; official page nshm.com/admissions/scholarships). No separate deadline is published in the sources checked and none is stated.',
 'dl_long': 'No separate deadline published — apply through the NSHM admission form and select the Asha Jyoti category',
 'offlinks': [('NSHM — Admissions and Scholarships (official)', 'https://www.nshm.com/admissions/scholarships/'), ('Buddy4Study — NSHM Knowledge Campus Asha Jyoti Scholarship 2025', 'https://www.buddy4study.com/scholarship/nshm-knowledge-campus-asha-jyoti-scholarship'), ('Careers360 — NSHM Knowledge Campus Kolkata scholarships', 'https://www.careers360.com/colleges/nshm-knowledge-campus-kolkata')],
 'related_titles': ['infocepts', 'muskaan', 'concentrix', 'satya'],
})

# 3. PMSS for Wards of States/UTs Police Personnel 2026-27
ARTICLES.append({
 'slug': 'nsp-prime-ministers-scholarship-scheme-for-wards-of-states-uts-police-personnel-2026-27',
 'title': "NSP Prime Minister's Scholarship Scheme for Wards of States/UTs Police Personnel 2026-27",
 'meta': "PMSS for wards of States/UTs police personnel 2026-27: Rs 2,500 a month for boys and Rs 3,000 a month for girls, for dependent wards of police personnel martyred in terror or Naxal attacks. Apply on NSP by 31 October 2026 — today.",
 'short': "NSP Prime Minister's Scholarship Scheme for Wards of States/UTs Police Personnel 2026-27",
 'kicker': 'Central Government · Police Families · NSP',
 'mono': 'PM',
 'prov_short': 'Ministry of Home Affairs',
 'prov_cat': 'Central Government · NSP',
 'h1': "NSP Prime Minister's Scholarship Scheme for Wards of States/UTs Police Personnel 2026-27",
 'sub': 'The Prime Minister’s Scholarship Scheme for wards of States and Union Territories police personnel is a small, sharply targeted scheme: 500 scholarships a year for the dependent children of state and UT police personnel who lost their lives in terror or Naxal attacks, paying a monthly allowance through a first professional degree. It runs on the National Scholarship Portal and its 2026-27 window closes today, 31 October 2026 — so an eligible student should submit today, not tomorrow.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Ministry of Home Affairs, Government of India, under the National Defence Fund, applied for through the National Scholarship Portal (NSP)'),
   ('Award', 'Rs 2,500 a month for boys and Rs 3,000 a month for girls — Rs 30,000 and Rs 36,000 a year respectively — paid annually for the duration of the first professional degree course'),
   ('Scholarships', '500 a year for this category: 250 for boys and 250 for girls'),
   ('Deadline', '31 October 2026 (NSP window for 2026-27: 1 June to 31 October 2026; institute verification by 15 November 2026 and district/state verification by 30 November 2026)'),
   ('Eligibility', 'Dependent ward of a State or UT police personnel martyred in a terror or Naxal attack; at least 60% marks in the minimum entry qualification (Class 12, diploma or graduation); enrolled in a first professional degree course at a recognised institution'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The Prime Minister’s Scholarship Scheme was launched under the National Defence Fund to encourage technical and professional education among the wards and widows of uniformed personnel. It has several tracks — ex-servicemen, Central Armed Police Forces and Assam Rifles, Railway Protection Force, and the track this article covers: wards of States and Union Territories police personnel. This track is the narrowest of them: it covers only the dependent children of state or UT police personnel who were martyred in terror or Naxal attacks, and it awards 500 scholarships a year, split equally between boys and girls. The Railway Protection Force track, which runs to 31 December 2026, is a different scheme with a different deadline and is not covered here.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Rs 2,500 a month for boys and Rs 3,000 a month for girls, credited annually — Rs 30,000 and Rs 36,000 a year respectively.</li>
        <li>Payment for the duration of the first professional degree course, subject to renewal conditions.</li>
        <li>Payment by Direct Benefit Transfer into the student’s Aadhaar-linked bank account, through the National Scholarship Portal system.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a dependent ward of a State or Union Territory police personnel martyred in a terror or Naxal attack, and you can produce a certificate confirming the martyrdom issued by the state government.</li>
        <li>You have secured at least 60% marks in your minimum entry qualification — Class 12, diploma or graduation, whichever qualifies you for the course.</li>
        <li>You are enrolled in a first professional degree course recognised by the relevant regulator (AICTE, UGC, medical or other councils): engineering, medicine, dental, veterinary science, BBA, BCA, B.Pharma, B.Sc Nursing or agriculture, MBA or MCA as a first professional course, and similar programmes listed in the scheme guidelines.</li>
        <li>Your course is full-time and on campus. Correspondence and distance-learning courses are not eligible, and neither are courses that do not lead to a degree.</li>
        <li>Wards of civilian employees of state police personnel are not eligible.</li>
        <li>Renewal applicants must pass each academic year with at least 50% marks.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The scheme’s official FAQ lists: a service certificate (Annexure-A) for serving personnel, the pension payment order, discharge, death, disability or gallantry award certificate as applicable, a bonafide certificate from the institution, a self-attested mark sheet of the minimum entry qualification, and — for this track specifically — a certificate confirming martyrdom in a terror or Naxal attack issued by the state government. An Aadhaar-linked bank account is required for payment. Follow the document list shown on the NSP application itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the full PMSS guidelines on the National Scholarship Portal before applying.</li>
        <li>Complete One Time Registration (OTR) on NSP at scholarships.gov.in, if you have not already done so.</li>
        <li>Open the Prime Minister’s Scholarship Scheme for Wards of States/UTs Police Personnel for 2026-27 and fill in your personal, family and course details.</li>
        <li>Upload the documents listed above — above all the state-government certificate confirming martyrdom in a terror or Naxal attack — and submit before 31 October 2026. This article is written on the last day of the window.</li>
        <li>Have your institute verify the application: institute verification closes on 15 November 2026 and district/state verification on 30 November 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much does it pay?', 'Rs 2,500 a month for boys and Rs 3,000 a month for girls, paid annually — Rs 30,000 and Rs 36,000 a year.'),
   ('Who exactly is eligible?', 'Dependent wards of State or UT police personnel martyred in terror or Naxal attacks, with at least 60% in the qualifying examination and admission to a first professional degree course.'),
   ('What is the deadline for 2026-27?', '31 October 2026 on the National Scholarship Portal. This article is written on that day — apply immediately.'),
   ('Which courses count?', 'First professional degree courses recognised by AICTE, UGC or the relevant council — engineering, medicine, dental, veterinary, BBA, BCA, pharmacy, nursing, agriculture, and MBA/MCA as a first professional course. Distance and correspondence courses do not count.'),
   ('What is the one document that matters most?', 'The state-government certificate confirming that the police personnel was martyred in a terror or Naxal attack. Without it, the application does not fit this track.'),
   ('Is the RPF track the same scheme?', 'No. The RPF/RPSF track is a separate PMSS track with its own deadline of 31 December 2026. Do not confuse the two dates.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the official NSP Prime Minister’s Scholarship Scheme FAQ (scholarships.gov.in: 500 scholarships for the States/UTs Police category, 60% minimum entry qualification, 50% renewal rule, first professional degree courses only, state-government martyrdom certificate, NSP application route), the Buddy4Study scheme page for wards of States/UTs police personnel (window 1 June to 31 October 2026; Rs 2,500/3,000 a month; 500 scholarships; verification dates 15 and 30 November 2026; civilian-employee wards and distance courses excluded) and the Buddy4Study PMSS overview (RPF/RPSF deadline 31 December 2026, distinct from this track).',
 'dl_long': '31 October 2026 (National Scholarship Portal; window 1 June to 31 October 2026)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('NSP — PMSS Frequently Asked Questions (official)', 'https://scholarships.gov.in/public/FAQ/FAQonPMSSS.pdf'), ('Buddy4Study — PMSS for Wards of States/UTs Police Personnel 2026', 'https://www.buddy4study.com/article/pmss-for-wards-of-states-uts-police-personnel'), ('Buddy4Study — PMSS for Wards of States/UTs Police Personnel (queue page)', 'https://www.buddy4study.com/scholarship/nsp-prime-ministers-scholarship-scheme-for-wards-of-states-uts-police-personnel')],
 'related_titles': ['pmss-railways', 'topclass-sc', 'nsp-pg-2026', 'balmiki-2026'],
})

# 4. Top Class Education for Students with Disabilities 2026-27
ARTICLES.append({
 'slug': 'nsp-scholarships-for-top-class-education-for-students-with-disabilities-2026-27',
 'title': 'NSP Scholarships for Top Class Education for Students with Disabilities 2026-27',
 'meta': 'NSP Top Class Education Scholarship for Students with Disabilities 2026-27: tuition reimbursement up to Rs 1.9 lakh a year plus Rs 3,000 a month maintenance for hostellers, for students with benchmark disability at notified Institutes of Excellence. Apply on NSP by 31 October 2026 — today.',
 'short': 'NSP Scholarships for Top Class Education for Students with Disabilities 2026-27',
 'kicker': 'Central Government · Disability Support · NSP',
 'mono': 'TC',
 'prov_short': 'DEPwD',
 'prov_cat': 'Central Government · NSP',
 'h1': 'NSP Scholarships for Top Class Education for Students with Disabilities 2026-27',
 'sub': 'The Scholarship for Top Class Education for Students with Disabilities is the Department of Empowerment of Persons with Disabilities’ route for students with a benchmark disability who reach a notified Institute of Excellence: it reimburses tuition, pays a monthly maintenance allowance, and adds allowances for readers, escorts and study material. It runs on the National Scholarship Portal and its 2026-27 window closes today, 31 October 2026 — so an eligible student should submit today, not tomorrow.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Department of Empowerment of Persons with Disabilities (DEPwD), Ministry of Social Justice and Empowerment, Government of India, applied for through the National Scholarship Portal (NSP)'),
   ('Award', 'Reimbursement of tuition fees and non-refundable charges up to Rs 1.9 lakh a year; maintenance allowance of Rs 3,000 a month for hostellers and Rs 1,500 a month for day scholars; a special allowance of Rs 2,000 a month for reader, escort or helper needs; and a fixed book and equipment allowance of Rs 5,000 a year'),
   ('Scholarships', '300 slots a year, including renewal cases'),
   ('Deadline', '31 October 2026 (NSP window for 2026-27: 1 June to 31 October 2026; defective-application verification by 15 November 2026 and district/state verification by 30 November 2026)'),
   ('Eligibility', 'Benchmark disability of 40% or more with a valid disability certificate or UDID card; graduate, postgraduate or diploma course at an Institute of Excellence notified by DEPwD; annual family income not exceeding Rs 8 lakh; the scholarship is awarded only once'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>This scheme sits inside the National Scholarship Portal’s family of central schemes, but it is run by a specific department: the Department of Empowerment of Persons with Disabilities, under the Ministry of Social Justice and Empowerment. Its purpose is to remove the cost barrier for students with disabilities who win places at the country’s notified Institutes of Excellence — the IITs, NITs, IIMs, AIIMS, NLUs and similar institutions on the department’s list — for graduate, postgraduate or diploma study. It is a top-class scheme in the literal sense: it only applies at notified institutions, and it pays at a higher level than the ordinary pre-matric and post-matric disability schemes.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Reimbursement of tuition fees and non-refundable charges, capped at Rs 1.9 lakh a year in the detailed 2026-27 listing checked. One guide gives the cap as Rs 2,00,000 a year; the detailed listing’s Rs 1.9 lakh figure is used here, and the difference is flagged rather than hidden — confirm the cap in force on the NSP scheme page.</li>
        <li>Maintenance allowance of Rs 3,000 a month for hostellers and Rs 1,500 a month for day scholars.</li>
        <li>A special allowance of Rs 2,000 a month for students who need a reader, escort or helper.</li>
        <li>A fixed book and equipment allowance of Rs 5,000 a year.</li>
        <li>Payment by Direct Benefit Transfer into the student’s Aadhaar-linked bank account, through the Public Financial Management System.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You have a benchmark disability of 40% or more, as defined under the Rights of Persons with Disabilities Act, 2016, with a valid disability certificate from a competent authority or a UDID card or enrolment number.</li>
        <li>You are pursuing a graduate, postgraduate or diploma course at an Institute of Excellence notified by the Department of Empowerment of Persons with Disabilities. Courses at institutions outside the notified list are not covered.</li>
        <li>Your parents’ or guardians’ annual income from all sources does not exceed Rs 8 lakh.</li>
        <li>You have not received this scholarship before: it is admissible only once, and is not given for a repeat course or a second award.</li>
        <li>You are an Indian student applying through the National Scholarship Portal with One Time Registration completed.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: your disability certificate or UDID card, an income certificate showing family income up to Rs 8 lakh a year, proof of admission to a notified Institute of Excellence, your Aadhaar card and Aadhaar-linked bank account details, and your previous academic records. The NSP application itself lists the documents it requires for your course and category, and that list governs the application — follow it rather than any shorter summary.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete One Time Registration (OTR) on the National Scholarship Portal at scholarships.gov.in, if you have not already done so.</li>
        <li>Find the Scholarship for Top Class Education for Students with Disabilities under the Department of Empowerment of Persons with Disabilities and open the 2026-27 application.</li>
        <li>Fill in your disability, income and admission details, upload the documents listed above, and submit before 31 October 2026. This article is written on the last day of the window.</li>
        <li>Have your institute verify the application: defective-application verification closes on 15 November 2026 and district/state verification on 30 November 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much does it pay?', 'Tuition reimbursement up to Rs 1.9 lakh a year, plus Rs 3,000 a month maintenance for hostellers (Rs 1,500 for day scholars), Rs 2,000 a month special allowance where a reader, escort or helper is needed, and Rs 5,000 a year for books and equipment.'),
   ('Who counts as having a benchmark disability?', 'A disability of 40% or more under the Rights of Persons with Disabilities Act, 2016, backed by a valid disability certificate or a UDID card.'),
   ('Does my college need to be on a list?', 'Yes. The course must be at an Institute of Excellence notified by the Department of Empowerment of Persons with Disabilities. Courses elsewhere are not covered.'),
   ('What is the deadline for 2026-27?', '31 October 2026 on the National Scholarship Portal. This article is written on that day — apply immediately.'),
   ('Can I get it twice, for two courses?', 'No. The scholarship is awarded only once and is not admissible for a repeat course or a second award.'),
   ('Is there an income limit?', 'Yes: annual family income from all sources must not exceed Rs 8 lakh.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study scheme page (window 1 June to 31 October 2026; defective verification 15 November 2026; district/state verification 30 November 2026; benchmark disability 40% or more; notified Institutes of Excellence; income up to Rs 8 lakh; one-time award; PFMS payment), the detailed 2026-27 listing (tuition reimbursement up to Rs 1.9 lakh a year; maintenance Rs 3,000 hosteller and Rs 1,500 day scholar a month; Rs 2,000 a month special allowance; Rs 5,000 a year book allowance; deadline 31 October 2026) and a second 2026-27 guide (300 slots including renewals; 40%+ disability; Rs 8 lakh income limit; 31 October 2026 deadline). A separate guide’s Rs 2,00,000 tuition cap is carried openly as a disagreement.',
 'dl_long': '31 October 2026 (National Scholarship Portal; window 1 June to 31 October 2026)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('Buddy4Study — Scholarships for Top Class Education for Students with Disabilities', 'https://www.buddy4study.com/article/scholarships-for-top-class-education-for-students-with-disabilities'), ('Buddy4Study — NSP Scholarships for Top Class Education for Students with Disabilities (queue page)', 'https://www.buddy4study.com/scholarship/nsp-scholarships-for-top-class-education-for-students-with-disabilities')],
 'related_titles': ['banishree', 'topclass-sc', 'pmss-railways', 'nsp-pg-2026'],
})

# 5. nurtr Nurturing Minds with Chess Program (50% fee waiver)
ARTICLES.append({
 'slug': 'nurtr-nurturing-minds-with-chess-program-50-fee-waiver-2025-26',
 'title': 'nurtr Nurturing Minds with Chess Program (50% fee waiver)',
 'meta': 'nurtr Nurturing Minds with Chess Program: grandmaster-led online chess coaching for school and college students aged 5 to 25, with income-based fee waivers — Rs 4,999 at 50% for family incomes of Rs 8–15 lakh, and Rs 1,000 at 90% for incomes below Rs 8 lakh.',
 'short': 'nurtr Nurturing Minds with Chess Program (50% fee waiver)',
 'kicker': 'India · Skill Course · Chess',
 'mono': 'N',
 'prov_short': 'nurtr',
 'prov_cat': 'Private · Chess Academy',
 'h1': 'nurtr Nurturing Minds with Chess Program (50% fee waiver)',
 'sub': 'The Nurturing Minds with Chess programme is a partnership between nurtr, an online chess academy founded in 2018, and Buddy4Study: it sells access to grandmaster-led online chess coaching at a price set by family income, so that the same course costs Rs 1,000 for the lowest-income families and Rs 9,999 at full price. This article covers the whole programme and leads with its middle tier — the 50% fee waiver at Rs 4,999 — because the programme’s three price points are one scheme, not three scholarships, and they belong in one article.',
 'dpill': 'No fixed deadline published',
 'facts': facts([
   ('Provider', 'nurtr, an online chess academy founded in 2018, in partnership with Buddy4Study'),
   ('Award', 'A fee waiver on the nurtr Neo online chess course: 50% waiver for this tier, meaning the course costs Rs 4,999 instead of Rs 9,999'),
   ('All three tiers', 'Family income below Rs 8 lakh a year: Rs 1,000 (90% waiver). Family income Rs 8–15 lakh a year: Rs 4,999 (50% waiver). Family income above Rs 15 lakh a year: Rs 9,999 (actual cost, no waiver)'),
   ('Deadline', 'No fixed deadline is published on the current programme page — applications are taken through Buddy4Study while the programme page is live'),
   ('Eligibility', 'Indian resident, currently enrolled as a school or college student, aged between 5 and 25 years'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>nurtr is an online chess academy that offers course content and coaching from titled chess trainers, and its Neo course is the programme’s flagship online offering. The Nurturing Minds with Chess programme exists to put that coaching within reach of families who could not pay the full fee: rather than a single flat discount, it scales the price to family income, with the largest subsidy going to the families who need it most. The coaching itself is the same across tiers — the tiers differ only in what the family pays.</p>
      <p>Be clear about what this is and is not. It is a subsidised course purchase, not a cash scholarship: you pay the reduced fee, your documents are verified, and the course is then activated. If verification finds you ineligible for the tier you chose, the amount you paid is refunded in full, as the programme page states. The full-cost tier exists for families who would rather skip income verification altogether.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Grandmaster-led online chess coaching through the nurtr Neo course, with structured learning material and access to tournaments, as described on the programme pages.</li>
        <li>Income-based pricing: Rs 1,000 for family incomes below Rs 8 lakh a year (90% waiver), Rs 4,999 for incomes between Rs 8 lakh and Rs 15 lakh a year (50% waiver), and Rs 9,999 at actual cost for incomes above Rs 15 lakh a year.</li>
        <li>A refund if document verification finds you ineligible for the tier you applied under.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a resident of India.</li>
        <li>You are currently enrolled as a school or college student.</li>
        <li>You are between 5 and 25 years of age.</li>
        <li>Your tier is decided by annual family income: below Rs 8 lakh for the 90% waiver, Rs 8–15 lakh for the 50% waiver, and above Rs 15 lakh for the actual-cost option.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>A student identity proof issued by your school or college, and family income proof — a salary slip, Form 16, income certificate, income tax return or similar document. Applicants in the above-Rs 8 lakh brackets also submit a self-declaration about family income, as the programme page specifies. Follow the document list shown on the application form, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the nurtr Nurturing Minds with Chess programme page on Buddy4Study.</li>
        <li>Choose your tier — the 90% waiver, the 50% waiver, or the actual-cost option — according to your family income.</li>
        <li>Click Apply Now, log in to your Buddy4Study account or register with an email address, mobile number or Google account.</li>
        <li>Fill in your details, upload the student identity and income documents, and submit.</li>
        <li>Pay the applicable fee through Buddy4Study’s payment gateway. Your course access is activated once your documents clear verification; if you are found ineligible, the amount is refunded.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a cash scholarship?', 'No. It is a subsidised course: you pay a reduced fee for the nurtr Neo chess course, and the course is activated after document verification.'),
   ('What do I pay at each income level?', 'Below Rs 8 lakh a year: Rs 1,000 (90% waiver). Rs 8–15 lakh a year: Rs 4,999 (50% waiver). Above Rs 15 lakh a year: Rs 9,999 at actual cost.'),
   ('Who can apply?', 'Indian school or college students aged 5 to 25.'),
   ('What if my documents do not match the tier I chose?', 'The programme page states that the amount paid is fully refunded if you are found ineligible on verification.'),
   ('Is there a deadline?', 'No fixed deadline is published on the current programme page. An older cycle listing gave 31 March 2026 for the 2025-26 cycle, but the programme page is live with applications open now, so this article states no deadline rather than repeating the old one.'),
   ('Are the 90% and actual-cost versions separate scholarships?', 'No. They are the same programme’s other price tiers, and they are covered in this one article rather than written up separately.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the live Buddy4Study nurtr programme page (three tiers: below Rs 8 lakh Rs 1,000 at 90% waiver; Rs 8–15 lakh Rs 4,999 at 50% waiver; above Rs 15 lakh Rs 9,999 at actual cost; eligibility Indian resident, school/college student, age 5–25; documents student ID and income proof plus self-declaration; payment through Buddy4Study gateway with refund on failed verification) and the Buddy4Study programme article (same tiers and eligibility). An older 2025-26 cycle listing gave a 31 March 2026 deadline, but the programme page is live with applications open, so no deadline is stated.',
 'dl_long': 'No fixed deadline published on the current programme page — applications taken through Buddy4Study',
 'offlinks': [('Buddy4Study — nurtr Nurturing Minds with Chess Program (programme page)', 'https://www.buddy4study.com/nurtneo'), ('Buddy4Study — nurtr Nurturing Minds with Chess Program (article)', 'https://www.buddy4study.com/article/nurtr-nurturing-minds-with-chess-program'), ('Buddy4Study — nurtr Nurturing Minds with Chess Program (50% fee waiver)', 'https://www.buddy4study.com/scholarship/nurtr-nurturing-minds-with-chess-program-50-fee-waiver-2025-26')],
 'related_titles': ['infocepts', 'muskaan', 'satya', 'navgurukul-pune'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

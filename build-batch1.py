#!/usr/bin/env python3
"""Build batch 1 of verified scholarship articles."""
import pathlib, html

TPL = pathlib.Path('/home/hatch/workspace/scholarships-17k/template/article-shell.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')
OUT.mkdir(parents=True, exist_ok=True)

def facts(items):
    return ''.join(f'<div class="fact"><small>{k}</small><strong>{v}</strong></div>' for k, v in items)

def faqs(pairs):
    return ''.join(f'<div class="faq"><strong>{q}</strong><p>{a}</p></div>' for q, a in pairs)

ARTICLES = []

# ---------------- 1. SDEF India Scholarship ----------------
ARTICLES.append(dict(
    slug='sdef-india-scholarship-2026-27',
    title='SDEF India Scholarship 2026-27: Up to Rs 50,000/Year for First-Year Professional Students',
    meta='SDEF India Scholarship 2026-27 offers up to Rs 50,000 per year to first-year B.Tech, MBBS, BDS and B.Arch students. Check eligibility, award slabs, documents and deadline.',
    mono='SDEF', short='SDEF India Scholarship', h1='SDEF India Scholarship 2026-27',
    provider='Swami Dayanand Education Foundation (SDEF)',
    deadline_pill='Closes 31 Oct 2026', status='Applications open', checked='16 Oct 2026',
    facts=facts([
        ('Award', 'Up to Rs 50,000 / year'),
        ('Who', '1st-year professional UG students'),
        ('Income limit', 'Rs 12 lakh / year'),
        ('Deadline', '31 Oct 2026'),
        ('Apply', 'Online only'),
    ]),
    body=f"""
<section><h2>About the scholarship</h2>
<p>The SDEF India Scholarship 2026-27 is run by the Swami Dayanand Education Foundation, a registered non-profit. It supports first-year students beginning full-time professional undergraduate degrees in India — engineering, medicine, dentistry, nursing, pharmacy, architecture and veterinary science.</p>
<p>Between 100 and 150 scholarships are awarded across India every year. The award is renewable for up to four years, subject to annual review of academic progress and continued eligibility.</p></section>
<section><h2>Eligibility</h2>
<p>You must meet <strong>all</strong> of the following conditions:</p>
<ul>
<li>Enrolling as a <strong>first-year, full-time undergraduate student</strong> in an eligible professional degree programme in India for 2026-27.</li>
<li><strong>Minimum 80% marks</strong> (or equivalent CGPA) in the Class 12 board examination.</li>
<li>Meet the <strong>entrance exam cutoff</strong> for your programme: JEE Main AIR 50,000 or below; JEE Advanced AIR 40,000 or below; NEET UG AIR 50,000 or below; NATA minimum 100 marks.</li>
<li>Total annual <strong>family income of Rs 12,00,000 or less</strong>, from all sources.</li>
<li><strong>No drop or gap year</strong> after Class 12 — this is a hard rule, including for JEE/NEET repeaters.</li>
</ul>
<h3>Eligible programmes</h3>
<ul><li>B.Tech / B.E. (JEE Main / Advanced)</li><li>MBBS, BDS (NEET UG)</li><li>B.Sc. Nursing, B.Pharm / Pharm.D, BVSc &amp; AH (as applicable)</li><li>B.Arch (NATA)</li></ul>
<p>Students admitted through management quota or state counselling may apply, but the published entrance cutoff for the programme must still be met where one applies.</p></section>
<section><h2>Benefits: the award slab</h2>
<p>Rs 50,000 is the <strong>maximum, not the standard award</strong>. Your yearly amount (Rs 20,000–50,000) is decided by your entrance rank band and your average of Class 10 and 12 marks:</p>
<table><tr><th>Avg. of Class 10 &amp; 12</th><th>Rank under 5,000</th><th>Under 10,000</th><th>Under 20,000</th><th>Under 30,000</th><th>Under 40,000</th></tr>
<tr><td>Above 80%</td><td>Rs 35,000</td><td>Rs 30,000</td><td>Rs 25,000</td><td>Rs 20,000</td><td>Rs 20,000</td></tr>
<tr><td>Above 85%</td><td>Rs 40,000</td><td>Rs 35,000</td><td>Rs 30,000</td><td>Rs 25,000</td><td>Rs 20,000</td></tr>
<tr><td>Above 90%</td><td>Rs 45,000</td><td>Rs 40,000</td><td>Rs 35,000</td><td>Rs 30,000</td><td>Rs 25,000</td></tr>
<tr><td>Above 95%</td><td>Rs 50,000</td><td>Rs 45,000</td><td>Rs 40,000</td><td>Rs 35,000</td><td>Rs 30,000</td></tr></table>
<p>Important: funds are <strong>disbursed once a year directly to your college or university</strong> toward approved educational expenses — not into personal bank accounts. Preference may be given to first-generation college students, meritorious female students from disadvantaged backgrounds, and students from agricultural families (30% of awards are reserved for talented women under the girls' initiative).</p></section>
<section><h2>Documents required</h2>
<p>The form asks for twelve uploads — scan everything <em>before</em> you start:</p>
<ol><li>Recent passport-size photograph</li><li>Aadhaar Card</li><li>Class 10 marksheet</li><li>Class 12 marksheet</li><li>JEE / NEET / NATA (or relevant) entrance scorecard</li><li>Admission letter</li><li>College ID card</li><li>Latest college fee receipt</li><li>Family income proof</li><li>Utility bill (electricity/water/gas, not older than 3 months)</li><li>Three photographs of your residence (inside and outside)</li><li>Signed SDEF Scholar Pledge form (download, print, sign, re-scan)</li></ol>
<p>Depending on circumstances, agricultural land documents, education loan papers, ITR, salary slips or pension proof may also be asked for.</p></section>
<section><h2>How to apply</h2>
<ol><li>Go to the official page: <strong>swamidayanand.org/india-scholarships-2026-27</strong></li>
<li>Download the SDEF Scholar Pledge, print, sign and scan it first.</li><li>Scan all twelve documents; check each is clear and within size limits.</li>
<li>Click <strong>Apply — Fresh Applicants</strong> and complete the nine sections (personal, college, academics, family, income, documents, declaration).</li>
<li>Save progress as you go; submit well before 31 October 2026. Applications are online only; no application fee is listed.</li></ol>
<h3>Selection process</h3>
<ol><li>Application review</li><li>Document verification</li><li>Online assessment (laptop/desktop + internet needed)</li><li>Personal interview, if shortlisted</li></ol>
<p>Results are expected mid-November 2026; funding begins January 2027. Renewal each year needs full-time enrolment, no backlogs, and a renewal form.</p></section>
<section><h2>FAQs</h2>
{faqs([
("Can I apply if I took a drop year for JEE/NEET?", "No. A drop or gap year after Class 12 makes you ineligible, regardless of rank."),
("Is BCA or general B.Sc. eligible?", "The published list covers engineering, MBBS, BDS, nursing, pharmacy, architecture and veterinary science. Students in other professional courses should write to SDEF to confirm before applying."),
("Does everyone get Rs 50,000?", "No. The award is slab-based (Rs 20,000–50,000) on rank band and Class 10/12 average. Only rank under 5,000 with above-95% average gets the full Rs 50,000."),
("Where does the money go?", "Directly to your college/university account once a year — not to your personal bank account."),
("Can I submit two applications?", "No. One application per applicant; multiple submissions can lead to disqualification."),
])}</section>""",
    vnote="Facts verified 16 Oct 2026 against the SDEF applicant handbook as reported by AglaSem News and Sakshi Education. Deadline: AglaSem and Sakshi report 31 Oct 2026; one Buddy4Study listing shows 30 Nov 2026 — verify on swamidayanand.org before applying. Award slabs, cutoffs and document list per the official handbook.",
))

# ---------------- 2. Vidyadhan Mathura Women in STEM ----------------
ARTICLES.append(dict(
    slug='vidyadhan-mathura-women-stem-scholarship-2026',
    title='Vidyadhan Mathura Scholarship for Women in STEM 2026: Rs 15,000–75,000/Year',
    meta='Shrimati Sadhana Khaitan Vidyadhan Scholarship for Women in STEM supports girl students from Mathura district pursuing MBBS, engineering and BSc. Eligibility, amount, deadline.',
    mono='V', short='Vidyadhan Mathura Women in STEM', h1='Vidyadhan Mathura Scholarship for Women in STEM 2026',
    provider='Vidyadhan (Shibulal Family philanthropic initiative)',
    deadline_pill='Closes 25 Oct 2026', status='Applications open', checked='16 Oct 2026',
    facts=facts([
        ('Award', 'Rs 15,000–75,000 / year'),
        ('Who', 'Girls from Mathura district, STEM courses'),
        ('Income limit', 'Under Rs 3 lakh / year'),
        ('Deadline', '25 Oct 2026'),
        ('Extra', 'Mentoring included'),
    ]),
    body=f"""
<section><h2>About the scholarship</h2>
<p>The <strong>Shrimati Sadhana Khaitan Vidyadhan Scholarship for Women in STEM</strong> supports talented young women from low-income families in <strong>Mathura district, Uttar Pradesh</strong>, who aspire to careers in science, technology, engineering and healthcare. It was instituted in memory of Smt. Sadhana Khaitan by her family, as a philanthropic initiative of the Shibulal Family under Vidyadhan — a higher-education programme supporting over 14,000 students across India.</p>
<p>Beyond money, scholars receive <strong>training and mentoring support</strong> to help them succeed in their chosen fields. The award continues till course completion, subject to satisfactory academic performance.</p></section>
<section><h2>Eligibility</h2>
<ul>
<li><strong>Female student</strong> from Mathura district, Uttar Pradesh.</li>
<li>Pursuing a <strong>STEM course</strong> — MBBS, Engineering, BSc or other STEM programmes.</li>
<li>Admitted to the <strong>first year</strong> of a degree or professional programme in academic year 2026-27.</li>
<li><strong>Minimum 70% marks in Class 12</strong> (60% for students with disabilities).</li>
<li>Completed Class 12 from a <strong>school in Mathura district</strong>, OR currently studying at an institution located in Mathura district.</li>
<li>Annual <strong>family income less than Rs 3 lakh</strong>.</li>
</ul></section>
<section><h2>Benefits</h2>
<p>Selected students receive <strong>Rs 15,000 to Rs 75,000 per year</strong>, depending on the course, till completion of the course — plus training and mentoring support.</p>
<h3>Selection process</h3>
<ol><li>Application screening</li><li>Written test</li><li>Interview (scheduled mid-to-late November 2026 for shortlisted candidates)</li></ol></section>
<section><h2>Documents required</h2>
<p>Scanned copies are required at application stage, including your <strong>Class 12 marksheet</strong>. Keep ID proof, income proof and admission proof ready as per the official application form.</p></section>
<section><h2>How to apply</h2>
<ol><li>Go to the official Vidyadhan application portal and find the Mathura Women in STEM programme.</li>
<li>Fill the application with personal, academic and family income details.</li><li>Upload scanned documents including your Class 12 marksheet.</li>
<li>Submit before <strong>25 October 2026</strong>; shortlisted candidates are called for test and interview.</li></ol></section>
<section><h2>FAQs</h2>
{faqs([
("I studied Class 12 outside Mathura but now study in a Mathura college. Am I eligible?", "Yes — eligibility covers students who completed Class 12 from a Mathura district school OR are currently studying at an institution located in Mathura district."),
("What is the minimum marks requirement?", "70% in Class 12; 60% for students with disabilities."),
("Is the scholarship only for engineering and MBBS?", "No — BSc and other STEM programmes are also eligible."),
("Does it renew automatically?", "It continues till course completion subject to satisfactory academic performance."),
])}</section>""",
    vnote="Facts verified 16 Oct 2026 via ScholarshipsInIndia and AimIndia reporting on the official Vidyadhan announcement. Deadline: 25 Oct 2026 per the most recent sources and Buddy4Study listing; one older report mentioned 25 Sept 2026 — verify on the official Vidyadhan portal before applying.",
))

# ---------------- 3. SML Mahindra Scholarship (Saarthi Abhiyaan) ----------------
ARTICLES.append(dict(
    slug='sml-mahindra-scholarship-saarthi-2026-27',
    title='SML Mahindra Scholarship 2026-27 (Saarthi Abhiyaan): Rs 10,000–30,000 for Daughters of Drivers',
    meta='SML Mahindra Scholarship 2026-27 under Saarthi Abhiyaan: Rs 10,000 for Class 11-12 girls and Rs 30,000 for UG/diploma STEM students who are daughters of commercial vehicle drivers.',
    mono='M', short='SML Mahindra Saarthi Scholarship', h1='SML Mahindra Scholarship Program 2026-27 (Saarthi Abhiyaan)',
    provider='SML Mahindra Limited (CSR initiative)',
    deadline_pill='Closes 21 Oct 2026', status='Applications open', checked='16 Oct 2026',
    facts=facts([
        ('Award', 'Rs 10,000 – 30,000 (one-time)'),
        ('Who', 'Daughters of commercial vehicle drivers'),
        ('Income limit', 'Rs 6 lakh / year'),
        ('Deadline', '21 Oct 2026'),
        ('Apply', 'Online'),
    ]),
    body=f"""
<section><h2>About the scholarship</h2>
<p>The <strong>SML Mahindra Scholarship Program 2026-27</strong>, run under the Saarthi Abhiyaan CSR initiative, supports the education of <strong>girl students who are daughters of drivers</strong> of heavy/light commercial goods vehicles and large passenger vehicles like buses. It runs in two categories:</p>
<ul><li><strong>SML Saarthi:</strong> Rs 10,000 — girl students in Class 11 or 12 (any stream).</li>
<li><strong>SML Unnati:</strong> Rs 30,000 — students pursuing UG, diploma or polytechnic in STEM and core engineering fields (any year).</li></ul>
<p>Children of SML Mahindra or Buddy4Study employees are not eligible. Preference may be given to applicants from Delhi-NCR, Punjab, Chandigarh, Haryana, UP, Uttarakhand, Himachal Pradesh and aspirational districts, as well as PwD students, single-parent families and orphaned students.</p></section>
<section><h2>Eligibility</h2>
<ul>
<li><strong>Girl student</strong> (for Saarthi; Unnati is open per category rules).</li>
<li><strong>Daughter of a driver</strong> operating a heavy or light commercial goods vehicle, or a large passenger vehicle such as a bus — a valid commercial driving licence of the parent/guardian is required as proof.</li>
<li>Saarthi: studying in <strong>Class 11 or 12</strong> in any stream at a recognised school; Unnati: UG/diploma/polytechnic in STEM or core engineering.</li>
<li><strong>Minimum 60% marks</strong> (or equivalent CGPA/grade) in the previous academic year.</li>
<li>Annual <strong>family income not exceeding Rs 6 lakh</strong> from all sources.</li>
</ul></section>
<section><h2>Benefits</h2>
<p>One-time scholarship: <strong>Rs 10,000</strong> (Saarthi, Class 11-12) or <strong>Rs 30,000</strong> (Unnati, UG/diploma STEM), to help cover tuition, books, study material and related academic expenses.</p></section>
<section><h2>Documents required</h2>
<ol><li>Recent passport-size photograph</li><li>Student identity proof (Aadhaar etc.)</li><li>Proof of current admission (admission letter / institute ID)</li><li>Class 10 marksheet</li><li>Previous year's marksheet</li><li>Fee receipts, where applicable</li><li><strong>Parent/guardian's valid commercial driving licence</strong></li><li>Student bank account details (passbook / cancelled cheque)</li><li>Address proof</li></ol></section>
<section><h2>How to apply</h2>
<ol><li>Open the scholarship application page on the Buddy4Study portal (the programme's application partner).</li>
<li>Register and enter the student's educational details.</li><li>Add the commercial vehicle driver's details and licence information.</li>
<li>Upload the required documents and the student's bank account information.</li>
<li>Review carefully and submit before <strong>21 October 2026</strong>. Application is free.</li></ol></section>
<section><h2>FAQs</h2>
{faqs([
("My father drives a taxi/auto. Are we eligible?", "The programme specifies drivers of heavy/light commercial goods vehicles and large passenger vehicles like buses — check the official eligibility page for your exact vehicle category."),
("Is there an income limit?", "Yes — Rs 6 lakh per year from all sources."),
("Can boys apply?", "The Saarthi category is for girl students; check the Unnati category rules on the official page."),
("Is there any application fee?", "No — the application is completely free."),
])}</section>""",
    vnote="Facts verified 16 Oct 2026 via CareerStar, OBC Rights and Buddy4Study listing data (The Hans India). Two categories (Saarthi Rs 10,000 / Unnati Rs 30,000), 60% marks, Rs 6 lakh income limit and 21 Oct 2026 deadline corroborated across sources. The classic 'Mahindra Saarthi Abhiyaan' (Rs 10,000 for daughters of truck drivers) is the predecessor/related CSR initiative — verify the current edition's name on the application portal.",
))

# ---------------- 4. Ujjivan Transgender Scholarship ----------------
ARTICLES.append(dict(
    slug='ujjivan-transgender-scholarship-2026-27',
    title='Ujjivan Small Finance Bank Transgender Scholarship 2026-27: Up to Rs 40,000',
    meta='Ujjivan Small Finance Bank Transgender Scholarship 2026-27 offers a one-time Rs 40,000 to transgender students in Classes 9-12, UG and PG. Eligibility and deadline.',
    mono='U', short='Ujjivan Transgender Scholarship', h1='Ujjivan Small Finance Bank Transgender Scholarship Program 2026-27',
    provider='Ujjivan Small Finance Bank Limited (CSR, via Buddy4Study)',
    deadline_pill='Closes 30 Oct 2026', status='Applications open', checked='16 Oct 2026',
    facts=facts([
        ('Award', 'Up to Rs 40,000 (one-time)'),
        ('Who', 'Transgender students, pan-India'),
        ('Income limit', 'Rs 10 lakh / year'),
        ('Deadline', '30 Oct 2026'),
        ('Apply', 'Online'),
    ]),
    body=f"""
<section><h2>About the scholarship</h2>
<p>The <strong>Ujjivan Small Finance Bank Transgender Scholarship Program 2026-27</strong> is a CSR initiative of Ujjivan Small Finance Bank Limited, implemented through Buddy4Study. It aims to empower talented and deserving <strong>transgender students across India</strong> by reducing financial barriers to education.</p>
<p>Selected candidates receive a <strong>one-time scholarship of up to Rs 40,000</strong>, usable for academic expenses such as examination fees, admission fees and tuition fees.</p></section>
<section><h2>Eligibility</h2>
<ul>
<li><strong>Transgender student</strong>, anywhere in India (pan-India).</li>
<li>Pursuing <strong>secondary (Class 9-10), senior secondary (Class 11-12), undergraduate or postgraduate</strong> studies.</li>
<li>Enrolled through a recognised <strong>government or private open school, or open university</strong>.</li>
<li>Minimum <strong>35% marks in Class 10 and/or Class 12</strong>.</li>
<li>Total annual <strong>household income not exceeding Rs 10,00,000</strong> from all sources.</li>
<li>Children of employees of Ujjivan Small Finance Bank or Buddy4Study are <strong>not eligible</strong>.</li>
</ul></section>
<section><h2>Benefits</h2>
<p>One-time financial assistance of <strong>up to Rs 40,000</strong> for academic-related expenses — exam fees, admission fees, tuition fees and similar costs.</p></section>
<section><h2>Documents required</h2>
<p>As listed on the official application form. Keep your ID proof, marksheets, income proof and bank account details ready before you begin.</p></section>
<section><h2>How to apply</h2>
<ol><li>Open the scholarship application page on the Buddy4Study portal (the programme's implementation partner).</li>
<li>Register and fill in personal, academic and income details.</li><li>Upload the required documents.</li>
<li>Submit online before <strong>30 October 2026</strong>. No application fee.</li></ol></section>
<section><h2>FAQs</h2>
{faqs([
("Who can apply?", "Transgender students across India in Classes 9-12, UG or PG through recognised open schools/open universities."),
("What is the minimum marks requirement?", "35% in Class 10 and/or Class 12."),
("Is the amount paid every year?", "No — it is a one-time scholarship of up to Rs 40,000."),
("Is there an income limit?", "Yes — Rs 10 lakh per year of total household income from all sources."),
])}</section>""",
    vnote="Facts verified 16 Oct 2026 via Sakshi Education, ScholarshipsInIndia, The Hindu (10 Oct 2026 education roundup) and DT Next — all agree on Rs 40,000 one-time award, 35% marks, Rs 10 lakh income limit and 30 Oct 2026 deadline. Older DT Next pieces mention earlier 2026 deadlines from previous cycles — the 2026-27 deadline is 30 Oct 2026.",
))

# ---------------- 5. Concentrix Scholarship ----------------
ARTICLES.append(dict(
    slug='concentrix-scholarship-2026-27',
    title='Concentrix Scholarship 2026-27: Up to Rs 65,000/Year for Female MBBS Students',
    meta='Concentrix Scholarship 2026-27 offers up to Rs 65,000 per year to female first-year MBBS students at government medical colleges. Eligibility, benefits, deadline.',
    mono='C', short='Concentrix Scholarship', h1='Concentrix Scholarship Program 2026-27',
    provider='Concentrix Daksh Services India Private Limited',
    deadline_pill='Closes 30 Oct 2026', status='Applications open', checked='16 Oct 2026',
    facts=facts([
        ('Award', 'Up to Rs 65,000 / year'),
        ('Who', 'Female 1st-year MBBS students, govt. colleges'),
        ('Income limit', 'Rs 5 lakh / year'),
        ('Deadline', '30 Oct 2026'),
        ('Apply', 'Online'),
    ]),
    body=f"""
<section><h2>About the scholarship</h2>
<p>The <strong>Concentrix Scholarship Program 2026-27</strong>, by Concentrix Daksh Services India Private Limited, supports young women entering medical education. It is open to <strong>female students enrolled in the first year of MBBS at a government medical college</strong> anywhere in India.</p>
<p>Selected scholars receive <strong>up to Rs 65,000 per year for the duration of the MBBS course</strong>, covering institution fees, examination fees, books, stationery, equipment and other academic costs. Applications opened 28 September 2026.</p></section>
<section><h2>Eligibility</h2>
<ul>
<li><strong>Female student</strong>, anywhere in India.</li>
<li>Enrolled in the <strong>first year of MBBS</strong> at a <strong>government medical college</strong>.</li>
<li>Successfully completed the <strong>Class 12</strong> board examination.</li>
<li>Annual <strong>parental income not exceeding Rs 5,00,000</strong> from all sources.</li>
<li>Children of employees of Concentrix or Buddy4Study India Foundation are <strong>not eligible</strong>.</li>
</ul>
<p><strong>Preference</strong> may be given to: children from single-parent families or orphans; students from aspirational districts; students with disabilities.</p></section>
<section><h2>Benefits</h2>
<p>Financial assistance of <strong>up to Rs 65,000 per year throughout the MBBS course</strong> — for institutional fees, exam fees, books, stationery, equipment and other academic costs.</p></section>
<section><h2>Documents required</h2>
<p>As listed on the official application form. Typically keep ready: Class 12 marksheet, government-issued ID, MBBS admission/enrolment proof, fee details, income certificate, and bank account details.</p></section>
<section><h2>How to apply</h2>
<ol><li>Open the scholarship application page on the Buddy4Study portal.</li>
<li>Register and fill in personal, academic and family income details.</li><li>Upload the required documents.</li>
<li>Submit online before <strong>30 October 2026</strong>. No application fee.</li></ol></section>
<section><h2>FAQs</h2>
{faqs([
("I am in second-year MBBS. Can I apply?", "No — only first-year MBBS students at government medical colleges are eligible."),
("Does it cover private medical colleges?", "No — government medical colleges only."),
("What is the income limit?", "Rs 5 lakh per year of parental income from all sources."),
("For how long is the support given?", "Up to Rs 65,000 per year for the duration of the MBBS course, subject to the programme's conditions."),
])}</section>""",
    vnote="Facts verified 16 Oct 2026 via Buddy4Study's official programme page, The Hindustan Gazette, CareerStar and EduAdvice — all agree on Rs 65,000/year, first-year MBBS at government colleges, Rs 5 lakh income limit and 30 Oct 2026 deadline. One YouTube video mentioned 30 Sept 2026, which appears outdated; the programme page confirms 30 Oct 2026.",
))

for a in ARTICLES:
    page = TPL
    page = page.replace('{{TITLE}}', html.escape(a['title']))
    page = page.replace('{{META}}', html.escape(a['meta']))
    page = page.replace('{{MONO}}', a['mono'])
    page = page.replace('{{SHORT}}', html.escape(a['short']))
    page = page.replace('{{H1}}', html.escape(a['h1']))
    page = page.replace('{{PROVIDER}}', html.escape(a['provider']))
    page = page.replace('{{DEADLINE_PILL}}', a['deadline_pill'])
    page = page.replace('{{STATUS}}', a['status'])
    page = page.replace('{{CHECKED}}', a['checked'])
    page = page.replace('{{FACTS}}', a['facts'])
    page = page.replace('{{BODY}}', a['body'])
    page = page.replace('{{VNOTE}}', a['vnote'])
    assert '{{' not in page, f"placeholder left in {a['slug']}"
    (OUT / (a['slug'] + '.html')).write_text(page)
    print('wrote', a['slug'], len(page), 'bytes')

# progress tracker
tracker = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md')
tracker.write_text("""# 17k Scholarship Articles — Progress Tracker

## Batch 1 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 1 | sdef-india-scholarship-2026-27 | SDEF India Scholarship | 31 Oct 2026 | Yes — handbook via AglaSem/Sakshi |
| 2 | vidyadhan-mathura-women-stem-scholarship-2026 | Vidyadhan Mathura Women in STEM | 25 Oct 2026 | Yes — ScholarshipsInIndia/AimIndia |
| 3 | sml-mahindra-scholarship-saarthi-2026-27 | SML Mahindra (Saarthi Abhiyaan) | 21 Oct 2026 | Yes — CareerStar/OBC Rights/B4S |
| 4 | ujjivan-transgender-scholarship-2026-27 | Ujjivan Transgender Scholarship | 30 Oct 2026 | Yes — Sakshi/The Hindu/DT Next |
| 5 | concentrix-scholarship-2026-27 | Concentrix Scholarship | 30 Oct 2026 | Yes — B4S programme page et al |

**Completed: 5 / ~17,000**
""")
print('tracker written')

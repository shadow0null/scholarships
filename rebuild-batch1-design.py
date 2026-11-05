#!/usr/bin/env python3
"""Rebuild batch-1 articles in the Pragati article design system."""
import re, pathlib, html as htmllib

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

TROPHY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4h10v5a5 5 0 0 1-10 0V4z"/><path d="M7 5.5H4.5a3 3 0 0 0 3.2 4.8M17 5.5h2.5a3 3 0 0 1-3.2 4.8M12 14v3.5M8.5 21h7M9.5 17.5h5"/></svg>'
PERSON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.8 20a7.2 7.2 0 0 1 14.4 0"/></svg>'

def scard(mono, title, href, dpill, award, elig, tags):
    taghtml = ''.join(f'<span class="tag {c}">{t}</span>' for t, c in tags)
    return f'''<article class="scard rv">
        <div class="scard-top">
          <span class="plogo monogram">{mono}</span>
          <span class="dpill ">{dpill}</span>
        </div>
        <h3><a href="{href}">{title}</a></h3>
        <div class="spec">
          <div class="spec-row"><span class="spec-ic" aria-hidden="true">{TROPHY}</span><div><strong>Award</strong><p>{award}</p></div></div>
          <div class="spec-row"><span class="spec-ic" aria-hidden="true">{PERSON}</span><div><strong>Eligibility</strong><p>{elig}</p></div></div>
        </div>
        <div class="tags">{taghtml}</div>
        <div class="scard-foot">
          <a class="view" href="{href}">View details →</a>
          <small><span class="verified">✓ Verified</span> · 16 Oct 2026</small>
        </div>
      </article>'''

def facts(items):
    return ''.join(
        f'<div class="fact"><div class="k">{k}</div><div class="v">{v}</div></div>'
        for k, v in items)

def faqs(pairs):
    return ''.join(
        f'<div class="faq"><div class="q">{q}</div><p>{a}</p></div>'
        for q, a in pairs)

# ---------- article data (verified 16 Oct 2026) ----------
ARTICLES = [
dict(
 slug='sdef-india-scholarship-2026-27',
 title='SDEF India Scholarship 2026–27: Up to Rs 50,000/Year | StudyDesk Scholarships',
 meta='SDEF India Scholarship 2026-27 offers up to Rs 50,000 per year to first-year B.Tech, MBBS, BDS and B.Arch students. Eligibility, award slabs, documents, deadline 31 Oct 2026.',
 short='SDEF India Scholarship 2026–27', kicker='Private · Merit-cum-Means',
 mono='SD', prov_short='SDEF', prov_long='Swami Dayanand Education Foundation',
 h1='SDEF India Scholarship 2026–27',
 sub='Up to Rs 50,000 a year for first-year professional students — B.Tech, MBBS, BDS, nursing, pharmacy, architecture and veterinary science.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 50,000 / year<small>Slab-based; max Rs 2 lakh over 4 yrs</small>'),
              ('Who can apply','First-year professional UG students<small>80%+ in Class 12; entrance cutoffs apply</small>'),
              ('Income limit','Rs 12 lakh / year<small>From all sources</small>'),
              ('Deadline','31 Oct 2026<small>Online only; no extension stated</small>'),
              ('Official site','swamidayanand.org<small>Apply only here</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The SDEF India Scholarship 2026–27 is run by the Swami Dayanand Education Foundation, a registered non-profit. It supports first-year students beginning full-time professional undergraduate degrees in India — engineering, medicine, dentistry, nursing, pharmacy, architecture and veterinary science.</p>
      <p>Between 100 and 150 scholarships are awarded across India every year. The award is renewable for up to four years, subject to annual review of academic progress and continued eligibility.</p>
      <h2 id="eligibility">Eligibility</h2>
      <p>You must meet <strong>all</strong> of the following conditions:</p>
      <ul>
        <li>Enrolling as a <strong>first-year, full-time undergraduate student</strong> in an eligible professional degree programme in India for 2026–27.</li>
        <li><strong>Minimum 80% marks</strong> (or equivalent CGPA) in the Class 12 board examination.</li>
        <li>Meet the <strong>entrance exam cutoff</strong>: JEE Main AIR 50,000 or below; JEE Advanced AIR 40,000 or below; NEET UG AIR 50,000 or below; NATA minimum 100 marks.</li>
        <li>Total annual <strong>family income of Rs 12,00,000 or less</strong>, from all sources.</li>
        <li><strong>No drop or gap year</strong> after Class 12 — a hard rule, including for JEE/NEET repeaters.</li>
      </ul>
      <h3>Eligible programmes</h3>
      <ul><li>B.Tech / B.E. (JEE Main / Advanced)</li><li>MBBS, BDS (NEET UG)</li><li>B.Sc. Nursing, B.Pharm / Pharm.D, BVSc &amp; AH (as applicable)</li><li>B.Arch (NATA)</li></ul>
      <div class="honest-note"><strong>Not the full Rs 50,000 for everyone:</strong> the award is slab-based (Rs 20,000–50,000) on your rank band and Class 10/12 average. Only rank under 5,000 with above-95% average gets the maximum.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 20,000 to Rs 50,000 per year</strong>, decided by entrance rank band and average of Class 10 and 12 marks — up to Rs 2,00,000 over four years.</li>
        <li>Funds are <strong>disbursed once a year directly to your college or university</strong> toward approved educational expenses — not into personal bank accounts.</li>
        <li>Renewable yearly after review: full-time enrolment, no backlogs, renewal form each year.</li>
        <li>Preference may be given to first-generation college students, meritorious female students from disadvantaged backgrounds, and agricultural families (30% of awards reserved for talented women).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Twelve uploads — scan everything <em>before</em> you start:</p>
      <ol>
        <li>Recent passport-size photograph</li><li>Aadhaar Card</li><li>Class 10 marksheet</li><li>Class 12 marksheet</li>
        <li>JEE / NEET / NATA (or relevant) entrance scorecard</li><li>Admission letter</li><li>College ID card</li><li>Latest college fee receipt</li>
        <li>Family income proof</li><li>Utility bill (electricity/water/gas, not older than 3 months)</li>
        <li>Three photographs of your residence (inside and outside)</li><li>Signed SDEF Scholar Pledge form (download, print, sign, re-scan)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the official page</strong>swamidayanand.org/india-scholarships-2026-27</li>
        <li><strong>Download the Scholar Pledge first</strong>Print, sign and scan it — required from every applicant.</li>
        <li><strong>Scan all twelve documents</strong>Check each is clear, complete and within the size limit.</li>
        <li><strong>Click Apply — Fresh Applicants</strong>Complete the nine sections: personal, college, academics, family, income, documents, declaration.</li>
        <li><strong>Submit before 31 October 2026</strong>Save progress as you go; applications are online only and no fee is listed.</li>
      </ol>
      <h3>Selection process</h3>
      <ol><li>Application review</li><li>Document verification</li><li>Online assessment (laptop/desktop + internet needed)</li><li>Personal interview, if shortlisted</li></ol>
      <p>Results expected mid-November 2026; funding begins January 2027.</p>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I apply if I took a drop year for JEE/NEET?","No. A drop or gap year after Class 12 makes you ineligible, regardless of rank."),
 ("Does everyone get Rs 50,000?","No. The award is slab-based (Rs 20,000–50,000) on rank band and Class 10/12 average."),
 ("Where does the money go?","Directly to your college/university account once a year — not to your personal bank account."),
 ("Can I submit two applications?","No. One application per applicant; multiple submissions can lead to disqualification."),
]),
 verify='Award slabs, cutoffs, eligibility and the 12-document list verified 16 Oct 2026 against the official SDEF applicant handbook (via AglaSem News) and Sakshi Education. Deadline: AglaSem and Sakshi report 31 Oct 2026; one Buddy4Study listing shows 30 Nov 2026 — confirm on swamidayanand.org before applying.',
 offlinks=[('SDEF official page','https://www.swamidayanand.org/india-scholarships-2026-27')],
 related_titles=['vidyadhan','sml','concentrix'],
),

dict(
 slug='vidyadhan-mathura-women-stem-scholarship-2026',
 title='Vidyadhan Mathura Scholarship for Women in STEM 2026 | StudyDesk Scholarships',
 meta='Shrimati Sadhana Khaitan Vidyadhan Scholarship for Women in STEM: Rs 15,000–75,000/year for girl students from Mathura district in MBBS, engineering, BSc. Deadline 25 Oct 2026.',
 short='Vidyadhan Mathura Women in STEM', kicker='Private · Girls · STEM',
 mono='V', prov_short='Vidyadhan', prov_long='Vidyadhan (Shibulal Family initiative)',
 h1='Vidyadhan Mathura Scholarship for Women in STEM 2026',
 sub='Rs 15,000 to Rs 75,000 a year — plus mentoring — for girl students from Mathura district pursuing STEM degrees.',
 dpill='9 days to go', dl_long='25 Oct 2026',
 facts=facts([('Award','Rs 15,000–75,000 / year<small>Till course completion</small>'),
              ('Who can apply','Girls from Mathura district<small>STEM courses: MBBS, engineering, BSc</small>'),
              ('Income limit','Under Rs 3 lakh / year<small>Family income</small>'),
              ('Deadline','25 Oct 2026<small>Test + interview after</small>'),
              ('Extra','Mentoring included<small>Training support for scholars</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Shrimati Sadhana Khaitan Vidyadhan Scholarship for Women in STEM</strong> supports talented young women from low-income families in <strong>Mathura district, Uttar Pradesh</strong>, who aspire to careers in science, technology, engineering and healthcare. Instituted in memory of Smt. Sadhana Khaitan by her family, it is a philanthropic initiative of the Shibulal Family under Vidyadhan — a higher-education programme supporting over 14,000 students across India.</p>
      <p>Beyond money, scholars receive <strong>training and mentoring support</strong>. The award continues till course completion, subject to satisfactory academic performance.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Female student</strong> from Mathura district, Uttar Pradesh.</li>
        <li>Pursuing a <strong>STEM course</strong> — MBBS, engineering, BSc or other STEM programmes.</li>
        <li>Admitted to the <strong>first year</strong> of a degree or professional programme in 2026–27.</li>
        <li><strong>Minimum 70% marks in Class 12</strong> (60% for students with disabilities).</li>
        <li>Completed Class 12 from a <strong>school in Mathura district</strong>, OR currently studying at an institution located in Mathura district.</li>
        <li>Annual <strong>family income less than Rs 3 lakh</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 15,000 to Rs 75,000 per year</strong>, depending on the course, till completion of the course.</li>
        <li><strong>Training and mentoring support</strong> alongside the financial award.</li>
      </ul>
      <h3>Selection process</h3>
      <ol><li>Application screening</li><li>Written test</li><li>Interview (mid-to-late November 2026 for shortlisted candidates)</li></ol>
      <h2 id="documents">Documents required</h2>
      <p>Scanned copies are required at application stage, including your <strong>Class 12 marksheet</strong>. Keep ID proof, income proof and admission proof ready as per the official application form.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the official Vidyadhan portal</strong>Find the Mathura Women in STEM programme for 2026.</li>
        <li><strong>Fill the application</strong>Personal, academic and family income details.</li>
        <li><strong>Upload scanned documents</strong>Including your Class 12 marksheet.</li>
        <li><strong>Submit before 25 October 2026</strong>Shortlisted candidates are called for test and interview.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I studied Class 12 outside Mathura but now study in a Mathura college. Am I eligible?","Yes — eligibility covers students who completed Class 12 from a Mathura district school OR are currently studying at an institution in Mathura district."),
 ("What is the minimum marks requirement?","70% in Class 12; 60% for students with disabilities."),
 ("Is it only for engineering and MBBS?","No — BSc and other STEM programmes are also eligible."),
 ("Does it renew automatically?","It continues till course completion subject to satisfactory academic performance."),
]),
 verify='Verified 16 Oct 2026 via ScholarshipsInIndia and AimIndia reporting on the official Vidyadhan announcement. Deadline: 25 Oct 2026 per the most recent sources and the Buddy4Study listing; one older report mentioned 25 Sept 2026 — confirm on the official Vidyadhan portal before applying.',
 offlinks=[('Vidyadhan official portal','https://www.vidyadhan.org/')],
 related_titles=['sdef','concentrix','ujjivan'],
),

dict(
 slug='sml-mahindra-scholarship-saarthi-2026-27',
 title='SML Mahindra Scholarship 2026–27 (Saarthi Abhiyaan) | StudyDesk Scholarships',
 meta='SML Mahindra Scholarship 2026-27 under Saarthi Abhiyaan: Rs 10,000 for Class 11-12 girls and Rs 30,000 for UG/diploma STEM students who are daughters of commercial vehicle drivers. Deadline 21 Oct 2026.',
 short='SML Mahindra Saarthi Scholarship', kicker='CSR · Girls',
 mono='M', prov_short='SML Mahindra', prov_long='SML Mahindra Limited (CSR initiative)',
 h1='SML Mahindra Scholarship Program 2026–27 (Saarthi Abhiyaan)',
 sub='Rs 10,000 for Class 11–12 girls and Rs 30,000 for UG/diploma STEM students — for daughters of commercial vehicle drivers.',
 dpill='5 days to go', dl_long='21 Oct 2026',
 facts=facts([('Award','Rs 10,000 – 30,000<small>One-time; by category</small>'),
              ('Who can apply','Daughters of commercial vehicle drivers<small>Girls; 60%+ in previous year</small>'),
              ('Income limit','Rs 6 lakh / year<small>From all sources</small>'),
              ('Deadline','21 Oct 2026<small>Online; free application</small>'),
              ('Categories','Saarthi + Unnati<small>Class 11–12 · UG/diploma STEM</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>SML Mahindra Scholarship Program 2026–27</strong>, run under the Saarthi Abhiyaan CSR initiative, supports the education of <strong>girl students who are daughters of drivers</strong> of heavy/light commercial goods vehicles and large passenger vehicles like buses. Two categories:</p>
      <ul><li><strong>SML Saarthi — Rs 10,000:</strong> girl students in Class 11 or 12 (any stream).</li>
      <li><strong>SML Unnati — Rs 30,000:</strong> students pursuing UG, diploma or polytechnic in STEM and core engineering fields (any year).</li></ul>
      <p>Children of SML Mahindra or Buddy4Study employees are not eligible. Preference may be given to applicants from Delhi-NCR, Punjab, Chandigarh, Haryana, UP, Uttarakhand, Himachal Pradesh and aspirational districts, plus PwD students, single-parent families and orphaned students.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Daughter of a driver</strong> operating a heavy or light commercial goods vehicle, or a large passenger vehicle such as a bus — a valid commercial driving licence of the parent/guardian is required as proof.</li>
        <li>Saarthi: studying in <strong>Class 11 or 12</strong> (any stream) at a recognised school; Unnati: UG/diploma/polytechnic in STEM or core engineering.</li>
        <li><strong>Minimum 60% marks</strong> (or equivalent CGPA/grade) in the previous academic year.</li>
        <li>Annual <strong>family income not exceeding Rs 6 lakh</strong> from all sources.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 10,000</strong> one-time (Saarthi, Class 11–12) or <strong>Rs 30,000</strong> one-time (Unnati, UG/diploma STEM).</li>
        <li>Usable for tuition, books, study material and related academic expenses.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Recent passport-size photograph</li><li>Student identity proof (Aadhaar etc.)</li>
        <li>Proof of current admission (admission letter / institute ID)</li><li>Class 10 marksheet</li>
        <li>Previous year's marksheet</li><li>Fee receipts, where applicable</li>
        <li><strong>Parent/guardian's valid commercial driving licence</strong></li>
        <li>Student bank account details (passbook / cancelled cheque)</li><li>Address proof</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal (the programme's application partner).</li>
        <li><strong>Register and enter details</strong>Student's educational information first.</li>
        <li><strong>Add the driver's details</strong>Commercial vehicle driver's details and licence information.</li>
        <li><strong>Upload documents and bank details</strong>Review carefully and submit before <strong>21 October 2026</strong>. Free.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("My father drives a taxi/auto. Are we eligible?","The programme specifies drivers of heavy/light commercial goods vehicles and large passenger vehicles like buses — check the official eligibility page for your exact vehicle category."),
 ("Is there an income limit?","Yes — Rs 6 lakh per year from all sources."),
 ("Is there any application fee?","No — the application is completely free."),
 ("Which edition is this?","The 2026 edition was announced as the 12th edition of the Saarthi initiative."),
]),
 verify='Verified 16 Oct 2026 via CareerStar, OBC Rights and Buddy4Study listing data (The Hans India). Two categories (Saarthi Rs 10,000 / Unnati Rs 30,000), 60% marks, Rs 6 lakh income limit and 21 Oct 2026 deadline corroborated across sources. Applications run on the Buddy4Study portal.',
 offlinks=[('Buddy4Study portal (application partner)','https://www.buddy4study.com/')],
 related_titles=['ujjivan','sdef','vidyadhan'],
),

dict(
 slug='ujjivan-transgender-scholarship-2026-27',
 title='Ujjivan Transgender Scholarship 2026–27: Up to Rs 40,000 | StudyDesk Scholarships',
 meta='Ujjivan Small Finance Bank Transgender Scholarship 2026-27: one-time Rs 40,000 for transgender students in Classes 9-12, UG and PG. Eligibility, deadline 30 Oct 2026.',
 short='Ujjivan Transgender Scholarship', kicker='CSR · Transgender Students',
 mono='U', prov_short='Ujjivan SFB', prov_long='Ujjivan Small Finance Bank Limited (CSR, via Buddy4Study)',
 h1='Ujjivan Small Finance Bank Transgender Scholarship Program 2026–27',
 sub='A one-time scholarship of up to Rs 40,000 for transgender students across India — Classes 9–12, UG and PG.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 40,000<small>One-time</small>'),
              ('Who can apply','Transgender students, pan-India<small>Classes 9–12, UG, PG via open school/university</small>'),
              ('Income limit','Rs 10 lakh / year<small>Household income</small>'),
              ('Deadline','30 Oct 2026<small>Online only</small>'),
              ('Use','Academic expenses<small>Exam, admission, tuition fees</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Ujjivan Small Finance Bank Transgender Scholarship Program 2026–27</strong> is a CSR initiative of Ujjivan Small Finance Bank Limited, implemented through Buddy4Study. It aims to empower talented and deserving <strong>transgender students across India</strong> by reducing financial barriers to education.</p>
      <p>Selected candidates receive a <strong>one-time scholarship of up to Rs 40,000</strong>, usable for academic expenses such as examination fees, admission fees and tuition fees.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Transgender student</strong>, anywhere in India (pan-India).</li>
        <li>Pursuing <strong>secondary (Class 9–10), senior secondary (Class 11–12), undergraduate or postgraduate</strong> studies.</li>
        <li>Enrolled through a recognised <strong>government or private open school, or open university</strong>.</li>
        <li>Minimum <strong>35% marks in Class 10 and/or Class 12</strong>.</li>
        <li>Total annual <strong>household income not exceeding Rs 10,00,000</strong> from all sources.</li>
        <li>Children of employees of Ujjivan Small Finance Bank or Buddy4Study are <strong>not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>One-time financial assistance of <strong>up to Rs 40,000</strong>.</li>
        <li>Covers academic-related expenses — exam fees, admission fees, tuition fees and similar costs.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your ID proof, marksheets, income proof and bank account details ready before you begin.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal (the programme's implementation partner).</li>
        <li><strong>Register and fill details</strong>Personal, academic and income details.</li>
        <li><strong>Upload documents</strong>As required by the form.</li>
        <li><strong>Submit before 30 October 2026</strong>Online only; no application fee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who can apply?","Transgender students across India in Classes 9–12, UG or PG through recognised open schools/open universities."),
 ("What is the minimum marks requirement?","35% in Class 10 and/or Class 12."),
 ("Is the amount paid every year?","No — it is a one-time scholarship of up to Rs 40,000."),
 ("Is there an income limit?","Yes — Rs 10 lakh per year of total household income from all sources."),
]),
 verify='Verified 16 Oct 2026 via Sakshi Education, ScholarshipsInIndia, The Hindu (10 Oct 2026 education roundup) and DT Next — all agree on Rs 40,000 one-time award, 35% marks, Rs 10 lakh income limit and 30 Oct 2026 deadline. Older DT Next pieces mention earlier 2026 deadlines from previous cycles; the 2026–27 deadline is 30 Oct 2026.',
 offlinks=[('Buddy4Study portal (application partner)','https://www.buddy4study.com/')],
 related_titles=['sml','concentrix','sdef'],
),

dict(
 slug='concentrix-scholarship-2026-27',
 title='Concentrix Scholarship 2026–27: Rs 65,000/Year for Female MBBS Students | StudyDesk Scholarships',
 meta='Concentrix Scholarship 2026-27 offers up to Rs 65,000 per year to female first-year MBBS students at government medical colleges. Eligibility, benefits, deadline 30 Oct 2026.',
 short='Concentrix Scholarship', kicker='CSR · Girls · Medical',
 mono='C', prov_short='Concentrix', prov_long='Concentrix Daksh Services India Private Limited',
 h1='Concentrix Scholarship Program 2026–27',
 sub='Up to Rs 65,000 a year, for the full MBBS course — for female first-year students at government medical colleges.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 65,000 / year<small>For the MBBS course duration</small>'),
              ('Who can apply','Female 1st-year MBBS students<small>Government medical colleges, pan-India</small>'),
              ('Income limit','Rs 5 lakh / year<small>Parental income</small>'),
              ('Deadline','30 Oct 2026<small>Online only</small>'),
              ('Covers','Fees, books, equipment<small>+ exam & academic costs</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Concentrix Scholarship Program 2026–27</strong>, by Concentrix Daksh Services India Private Limited, supports young women entering medical education. It is open to <strong>female students enrolled in the first year of MBBS at a government medical college</strong> anywhere in India.</p>
      <p>Selected scholars receive <strong>up to Rs 65,000 per year for the duration of the MBBS course</strong>, covering institution fees, examination fees, books, stationery, equipment and other academic costs. Applications opened 28 September 2026.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Female student</strong>, anywhere in India.</li>
        <li>Enrolled in the <strong>first year of MBBS</strong> at a <strong>government medical college</strong>.</li>
        <li>Successfully completed the <strong>Class 12</strong> board examination.</li>
        <li>Annual <strong>parental income not exceeding Rs 5,00,000</strong> from all sources.</li>
        <li>Children of employees of Concentrix or Buddy4Study India Foundation are <strong>not eligible</strong>.</li>
      </ul>
      <div class="honest-note"><strong>Preference may be given to:</strong> children from single-parent families or orphans; students from aspirational districts; students with disabilities.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Financial assistance of <strong>up to Rs 65,000 per year throughout the MBBS course</strong>.</li>
        <li>Covers institutional fees, exam fees, books, stationery, equipment and other academic costs.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Typically keep ready: Class 12 marksheet, government-issued ID, MBBS admission/enrolment proof, fee details, income certificate, and bank account details.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal.</li>
        <li><strong>Register and fill details</strong>Personal, academic and family income details.</li>
        <li><strong>Upload documents</strong>As required by the form.</li>
        <li><strong>Submit before 30 October 2026</strong>Online only; no application fee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am in second-year MBBS. Can I apply?","No — only first-year MBBS students at government medical colleges are eligible."),
 ("Does it cover private medical colleges?","No — government medical colleges only."),
 ("What is the income limit?","Rs 5 lakh per year of parental income from all sources."),
 ("For how long is the support given?","Up to Rs 65,000 per year for the duration of the MBBS course, subject to the programme's conditions."),
]),
 verify="Verified 16 Oct 2026 via Buddy4Study's official programme page, The Hindustan Gazette, CareerStar and EduAdvice — all agree on Rs 65,000/year, first-year MBBS at government colleges, Rs 5 lakh income limit and 30 Oct 2026 deadline. One YouTube video mentioned 30 Sept 2026, which appears outdated; the programme page confirms 30 Oct 2026.",
 offlinks=[('Concentrix programme page (Buddy4Study)','https://www.buddy4study.com/article/concentrix-scholarship')],
 related_titles=['sdef','vidyadhan','ujjivan'],
),
]

# related-card content lookup
CARDINFO = {
 'sdef': dict(mono='SD', title='SDEF India Scholarship 2026–27', href='sdef-india-scholarship-2026-27.html',
              dpill='15 days to go', award='Up to Rs 50,000/year, slab-based', elig='First-year professional UG; 80%+ in Class 12; income ≤ Rs 12 lakh.',
              tags=[('Merit-cum-Means','blue'),('Private','teal')]),
 'vidyadhan': dict(mono='V', title='Vidyadhan Mathura Scholarship for Women in STEM 2026', href='vidyadhan-mathura-women-stem-scholarship-2026.html',
              dpill='9 days to go', award='Rs 15,000–75,000/year + mentoring', elig='Girls from Mathura district in STEM; 70%+ in Class 12; income < Rs 3 lakh.',
              tags=[('Girls','blue'),('STEM','teal')]),
 'sml': dict(mono='M', title='SML Mahindra Scholarship 2026–27 (Saarthi Abhiyaan)', href='sml-mahindra-scholarship-saarthi-2026-27.html',
              dpill='5 days to go', award='Rs 10,000–30,000 one-time', elig='Daughters of commercial vehicle drivers; 60%+; income ≤ Rs 6 lakh.',
              tags=[('Girls','blue'),('CSR','teal')]),
 'ujjivan': dict(mono='U', title='Ujjivan Transgender Scholarship 2026–27', href='ujjivan-transgender-scholarship-2026-27.html',
              dpill='14 days to go', award='Up to Rs 40,000 one-time', elig='Transgender students pan-India; 35%+; income ≤ Rs 10 lakh.',
              tags=[('Transgender','blue'),('CSR','teal')]),
 'concentrix': dict(mono='C', title='Concentrix Scholarship 2026–27', href='concentrix-scholarship-2026-27.html',
              dpill='14 days to go', award='Up to Rs 65,000/year for MBBS', elig='Female 1st-year MBBS, govt. college; income ≤ Rs 5 lakh.',
              tags=[('Girls','blue'),('Medical','teal')]),
}

MONO_CSS = ('.plogo.monogram{background:linear-gradient(135deg,#1a2145,#2e4a8f);color:#fff;'
            'font-weight:800;font-size:15px;letter-spacing:.02em;padding:0;border:0}'
            '.plogo.monogram.lg{font-size:20px}')

for a in ARTICLES:
    page = BASE
    # 1. title + meta
    page = re.sub(r'<title>.*?</title>', f"<title>{htmllib.escape(a['title'])}</title>", page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content=".*?">',
                  f'<meta name="description" content="{htmllib.escape(a["meta"])}">', page, count=1)
    # 2. monogram CSS (once)
    page = page.replace('</style>', MONO_CSS + '\n</style>', 1)
    # 3. crumbs
    page = re.sub(r'(<p class="crumbs">.*?<span>/</span>)AICTE Pragati Scholarship 2026–27</p>',
                  r'\g<1>' + htmllib.escape(a['short']) + '</p>', page, count=1, flags=re.S)
    # 4. kicker
    page = re.sub(r'<p class="kicker">.*?</p>', f'<p class="kicker">{a["kicker"]}</p>', page, count=1, flags=re.S)
    # 5. logo -> monogram (first plogo lg only)
    page = re.sub(r'<span class="plogo lg"><img src="data:image/[^"]*"[^>]*></span>',
                  f'<span class="plogo lg monogram">{a["mono"]}</span>', page, count=1)
    # 6. provider name spans in prov-row
    page = re.sub(r'(<div class="prov-row">.*?</span>\s*<div>\s*<span>).*?(</span>)',
                  r'\g<1>' + htmllib.escape(a['prov_short']) + r'\g<2>', page, count=1, flags=re.S)
    # 7. h1 + sub
    page = re.sub(r'<h1>.*?</h1>', f"<h1>{htmllib.escape(a['h1'])}</h1>", page, count=1, flags=re.S)
    page = re.sub(r'<p class="sub">.*?</p>', f'<p class="sub">{a["sub"]}</p>', page, count=1, flags=re.S)
    # 8. meta-row
    newmeta = (f'<div class="meta-row">\n      <span class="dline">{a["dpill"]}</span>\n'
               f'      <span class="status">Open</span>\n      <span>Updated 16 Oct 2026</span>\n'
               f'      <span>By {htmllib.escape(a["prov_short"])}</span>\n    </div>')
    page = re.sub(r'<div class="meta-row">.*?</div>', newmeta, page, count=1, flags=re.S)
    # 9. facts
    page = re.sub(r'<div class="facts rv">.*?</div>\s*(?=<div class="alayout">)',
                  f'<div class="facts rv">\n{a["facts"]}\n    </div>\n    ', page, count=1, flags=re.S)
    # 10. article body
    start = page.find('<article class="abody">')
    end = page.find('</article>', start)
    newbody = '<article class="abody">\n' + a['body'] + '\n      <p class="verify">' + a['verify'] + '</p>\n    '
    page = page[:start] + newbody + page[end:]
    # 11. alert card deadline
    page = re.sub(r'(<div class="acard alert-card rv"[^>]*>\s*<h3>)Deadline: .*?(</h3>)',
                  r'\g<1>Deadline: ' + a['dl_long'] + r'\g<2>', page, count=1, flags=re.S)
    # 12. offcard links
    links = ''.join(
        f'<a class="offlink" href="{u}" rel="noopener"><span>{htmllib.escape(t)}</span><span>→</span></a>'
        for t, u in a['offlinks'])
    page = re.sub(r'(<div class="acard offcard rv">.*?<p>Always confirm details on the official portal before applying\.</p>).*?(</div>\s*</aside>)',
                  r'\g<1>\n        ' + links + r'\n      \g<2>', page, count=1, flags=re.S)
    # 13. related cards
    cards = '\n'.join(scard(**CARDINFO[k]) for k in a['related_titles'])
    page = re.sub(r'(<section class="related">.*?<div class="cards">).*?(</div>\s*</section>)',
                  r'\g<1>\n' + cards + r'\n    \g<2>', page, count=1, flags=re.S)
    # sanity
    page = page.replace('<a class="wa-float" href="#"',
                        '<a class="wa-float" href="https://wa.me/919905166009"', 1)
    assert 'AICTE Pragati' not in page and 'pragati' not in page.lower().replace('pragati-scholarship',''), a['slug']
    assert 'data:image' not in page, a['slug'] + ' still has embedded images'
    assert '{{' not in page
    OUT.joinpath(a['slug'] + '.html').write_text(page)
    print('rebuilt', a['slug'], len(page), 'bytes')

print('done')

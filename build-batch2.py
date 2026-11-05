#!/usr/bin/env python3
"""Batch 2: 5 verified articles. All facts verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'wings': dict(mono='W', title='WINGS — Women INspiring Growth in STEM Scholarship (IIT Bombay)', href='wings-women-stem-iit-bombay-2027-28.html',
              dpill='15 days to go', award='Rs 2 lakh/year tuition fees', elig='Girls planning UG STEM at IIT Bombay (2027-28); 6.0 CPI to renew.',
              tags=[('Girls','blue'),('STEM','teal')]),
 'infocepts': dict(mono='I', title='Infocepts Innovate for Impact Scholarship 2026-27', href='infocepts-innovate-impact-scholarship-2026-27.html',
              dpill='14 days to go', award='Up to Rs 50,000/year for 4 years', elig='UG CS/IT/AI/ML/Data Science; 60%+ in 10th & 12th; income ≤ Rs 6 lakh; Nagpur/Pune/Chennai/Bengaluru.',
              tags=[('Engineering','blue'),('CSR','teal')]),
 'abcapital': dict(mono='AB', title='Aditya Birla Capital Scholarship 2026-27', href='aditya-birla-capital-scholarship-2026-27.html',
              dpill='14 days to go', award='Rs 25,000–60,000 one-time', elig='Girl students Class 9–PG at government institutions; 60%+; income ≤ Rs 6 lakh.',
              tags=[('Girls','blue'),('CSR','teal')]),
 'satya': dict(mono='S', title='Satya Scholarship Program 2026', href='satya-scholarship-program-2026.html',
              dpill='15 days to go', award='100% course fee + hostel & meals', elig='1st-year MBBS/BDS/nursing via Punjab route; 60%+ in Class 12; income ≤ Rs 8 lakh.',
              tags=[('Medical','blue'),('Punjab','teal')]),
 'muskaan': dict(mono='M', title='Muskaan Scholarship Program 2.0 (2026-27)', href='muskaan-scholarship-2-2026-27.html',
              dpill='14 days to go', award='Up to Rs 12,000 + mentoring', elig='Class 9–12; children of drivers/mechanics/EWS; 18 states; 60%+ in previous class.',
              tags=[('School','blue'),('CSR','teal')]),
}

ARTICLES = [
dict(
 slug='wings-women-stem-iit-bombay-2027-28',
 title='WINGS Scholarship (IIT Bombay): Rs 2 Lakh/Year for Women in STEM | StudyDesk Scholarships',
 meta='WINGS — Women INspiring Growth in STEM Scholarship: Rs 2 lakh per year tuition support for female students pursuing UG STEM at IIT Bombay (2027-28). Eligibility, deadline 31 Oct 2026.',
 short='WINGS Scholarship (IIT Bombay)', kicker='IIT Bombay · Girls · STEM',
 mono='W', prov_short='IIT Bombay', prov_long='IIT Bombay (funded by Bharat Desai & Neerja Sethi)',
 h1='WINGS — Women INspiring Growth in STEM Scholarship Program',
 sub='Rs 2 lakh a year toward tuition fees for women pursuing undergraduate STEM at IIT Bombay — applications for the 2027–28 session close 31 October 2026.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 2,00,000 / year<small>Tuition fee support</small>'),
              ('Who can apply','Female students<small>Planning UG STEM at IIT Bombay, 2027–28</small>'),
              ('Renewal','CPI 6.0+<small>Maintain every year</small>'),
              ('Deadline','31 Oct 2026<small>Online only</small>'),
              ('Funded by','Bharat Desai & Neerja Sethi<small>IIT Bombay alumni</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>WINGS — Women INspiring Growth in STEM</strong> is an initiative at IIT Bombay launched by alumnus Bharat Desai and his wife Neerja Sethi. It aims to break financial barriers for women in science, technology, engineering and mathematics, and to increase female representation in STEM nationwide.</p>
      <p>The scholarship covers <strong>tuition fees of Rs 2 lakh per annum</strong> for eligible women students. It particularly encourages applicants from rural and underprivileged backgrounds.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Female student</strong> planning to pursue an <strong>undergraduate STEM course at IIT Bombay</strong> in the <strong>2027–28 academic session</strong>.</li>
        <li><strong>Not availing any other government tuition grant or scholarship.</strong></li>
        <li>To continue receiving the scholarship, the student must maintain a <strong>CPI of 6.0 or higher</strong>.</li>
      </ul>
      <div class="honest-note"><strong>Note the timing:</strong> this round of applications (closing 31 Oct 2026) is for students <em>planning</em> to join IIT Bombay's UG STEM programmes in the 2027–28 session — apply before you have the admission offer in hand.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 2,00,000 per year</strong> toward tuition fees.</li>
        <li>Continues through the degree subject to maintaining <strong>6.0 CPI</strong> and meeting the programme's conditions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your ID proof, academic records and any income documents ready before you begin.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal (application partner for this edition).</li>
        <li><strong>Fill the interest/application form</strong>Personal and academic details, plus your planned IIT Bombay UG STEM course.</li>
        <li><strong>Submit before 31 October 2026</strong>Online only.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need an IIT Bombay admission offer to apply?","No — this round is for students planning to pursue UG STEM at IIT Bombay in 2027–28. Check the official page for how admission-stage verification works."),
 ("Can I hold another scholarship alongside WINGS?","No — applicants must not be availing any other government tuition grant or scholarship."),
 ("What happens if my CPI drops below 6.0?","The scholarship continues only for students maintaining a 6.0 CPI or higher."),
 ("Who funds WINGS?","IIT Bombay alumnus Bharat Desai and his wife Neerja Sethi."),
]),
 verify='Verified 16 Oct 2026 via Sakshi Education, The Hans India (Buddy4Study listing), The Hindustan Gazette and Campuzine — all agree on Rs 2 lakh/year tuition support, female UG STEM aspirants for IIT Bombay 2027–28, no other government tuition grant, 6.0 CPI renewal rule, and 31 Oct 2026 deadline. An older Sakshi page (April 2026 deadline) refers to a previous cycle.',
 offlinks=[('Buddy4Study portal (application partner)','https://www.buddy4study.com/')],
 related_titles=['infocepts','abcapital','satya'],
),

dict(
 slug='infocepts-innovate-impact-scholarship-2026-27',
 title='Infocepts Innovate for Impact Scholarship 2026-27: Rs 50,000/Year | StudyDesk Scholarships',
 meta='Infocepts Innovate for Impact Scholarship 2026-27: up to Rs 50,000 per year for 4 years for UG students in CS, IT, AI, ML, Data Science. Eligibility, deadline 30 Oct 2026.',
 short='Infocepts Innovate for Impact', kicker='CSR · Engineering',
 mono='I', prov_short='Infocepts Foundation', prov_long='Infocepts Foundation (CSR initiative)',
 h1='Infocepts Innovate for Impact Scholarship 2026–27',
 sub='Up to Rs 50,000 a year for up to four years — for UG students in Computer Engineering, IT, AI, ML and Data Science.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 50,000 / year<small>Maximum 4 years</small>'),
              ('Who can apply','UG CS / IT / AI / ML / Data Science<small>Any year of study</small>'),
              ('Income limit','Rs 6 lakh / year<small>Family income</small>'),
              ('Deadline','30 Oct 2026<small>Online only</small>'),
              ('Where','Nagpur · Pune · Chennai · Bengaluru<small>Study or domicile</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Infocepts Innovate for Impact Scholarship 2026–27</strong> is a CSR initiative of the <strong>Infocepts Foundation</strong>. It supports talented engineering students from financially weaker backgrounds pursuing technology degrees, helping them complete their education and build careers in technology-driven fields.</p>
      <p>Selected students receive <strong>up to Rs 50,000 per academic year for up to four years</strong>, subject to annual renewal conditions.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Pursuing an <strong>undergraduate degree</strong> in <strong>Computer Engineering, Information Technology, Artificial Intelligence, Machine Learning, or Data Science</strong> — students from <strong>any year</strong> of UG study can apply.</li>
        <li><strong>Minimum 60% marks in Class 10 and Class 12.</strong></li>
        <li>Annual <strong>family income up to Rs 6 lakh</strong>.</li>
        <li>Must be <strong>studying in or domiciled in Nagpur, Pune, Chennai or Bengaluru</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Financial assistance of <strong>up to Rs 50,000 per academic year</strong>.</li>
        <li>Support available for a <strong>maximum of four years</strong>.</li>
        <li>Renewal each year depends on meeting the required eligibility conditions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your Class 10 and 12 marksheets, ID proof, income proof, domicile/study proof and bank details ready.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal.</li>
        <li><strong>Register / log in</strong>With email ID and mobile number.</li>
        <li><strong>Select the scholarship and fill the form</strong>Personal, academic and family income details; upload documents.</li>
        <li><strong>Submit before 30 October 2026</strong>Online only.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am in 3rd year of B.Tech CSE. Can I apply?","Yes — students from any year of the eligible UG programmes can apply."),
 ("Which cities are covered?","You must be studying in or domiciled in Nagpur, Pune, Chennai or Bengaluru."),
 ("Is it renewable?","Yes, up to four years, subject to meeting the renewal conditions each year."),
 ("What is the income limit?","Rs 6 lakh per year of family income."),
]),
 verify='Verified 16 Oct 2026 via Sakshi Education, The Hindustan Gazette, BongJobs, The Hindu (10 Oct 2026 roundup) and EduAdvice — all agree on up to Rs 50,000/year for 4 years, eligible branches, 60% in 10th & 12th, Rs 6 lakh income limit, the four cities, and 30 Oct 2026 deadline. Applications run on the Buddy4Study portal.',
 offlinks=[('Buddy4Study portal (application partner)','https://www.buddy4study.com/')],
 related_titles=['wings','abcapital','muskaan'],
),

dict(
 slug='aditya-birla-capital-scholarship-2026-27',
 title='Aditya Birla Capital Scholarship 2026-27: Rs 25,000–60,000 for Girls | StudyDesk Scholarships',
 meta='Aditya Birla Capital Scholarship 2026-27 for girl students in Class 9 to PG at government institutions: Rs 25,000 to Rs 60,000 one-time. Eligibility, deadline 30 Oct 2026.',
 short='Aditya Birla Capital Scholarship', kicker='CSR · Girls',
 mono='AB', prov_short='Aditya Birla Capital Foundation', prov_long='Aditya Birla Capital Foundation (CSR)',
 h1='Aditya Birla Capital Scholarship Program 2026–27',
 sub='Rs 25,000 to Rs 60,000 one-time support for meritorious girl students — from Class 9 to post-graduation.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Rs 25,000 – 60,000<small>One-time, by education level</small>'),
              ('Who can apply','Girl students<small>Class 9 to PG, government institutions</small>'),
              ('Income limit','Rs 6 lakh / year<small>Family income</small>'),
              ('Deadline','30 Oct 2026<small>Online via Buddy4Study</small>'),
              ('Marks','60%+<small>In most recent academic year</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Aditya Birla Capital Scholarship Program 2026–27</strong>, by the Aditya Birla Capital Foundation (the CSR arm of Aditya Birla Capital), supports <strong>meritorious girl students from underprivileged backgrounds</strong> across India, helping them continue their education with confidence.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Girl student</strong> — the programme is open exclusively to girls.</li>
        <li>Currently enrolled in <strong>Classes 9 to 12, a Polytechnic Diploma, or an undergraduate or postgraduate course</strong>.</li>
        <li>Studying at a <strong>recognised government school, college or institution</strong> in India.</li>
        <li><strong>Minimum 60% marks</strong> in the most recent academic year.</li>
        <li>Annual <strong>family income not exceeding Rs 6,00,000</strong>.</li>
        <li>Children of employees of Aditya Birla Capital (including subsidiaries/JVs) and Buddy4Study are <strong>not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <p>One-time financial assistance for one year, by education level:</p>
      <ul>
        <li><strong>Class 9–12 and Polytechnic Diploma:</strong> Rs 25,000</li>
        <li><strong>Undergraduate:</strong> up to Rs 45,000</li>
        <li><strong>Postgraduate:</strong> Rs 60,000</li>
      </ul>
      <p>Covers academic expenses (tuition, admission, exam fees, books) and living expenses (hostel/mess charges, uniforms and allied necessities). <strong>Not renewable</strong> — plan finances accordingly.</p>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your marksheet, ID proof, income proof, admission proof and bank details ready; missing documents can lead to rejection.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the programme page</strong>On the Buddy4Study portal.</li>
        <li><strong>Check eligibility and register</strong>Confirm every criterion before starting the form.</li>
        <li><strong>Fill and upload</strong>Personal, academic and financial details with all required documents.</li>
        <li><strong>Submit before 30 October 2026</strong>Online only; selection involves screening and document verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this the same as the Aditya Birla Scholarship?","No — this is the Aditya Birla <em>Capital</em> Scholarship by the Aditya Birla Capital Foundation, a separate CSR programme for girl students."),
 ("Can private-school students apply?","No — applicants must study at recognised government schools, colleges or institutions."),
 ("Is the scholarship renewed every year?","No — it is a one-time fixed grant for one year."),
 ("Can boys apply?","No — this programme is exclusively for girl students."),
]),
 verify="Verified 16 Oct 2026 via Buddy4Study's official programme page, The Hindustan Gazette, The Hans India, AssamTopper and Cigmapedia — all agree on the girl-student criterion, Class 9–PG range at government institutions, 60% marks, Rs 6 lakh income limit, the three award slabs, one-time nature, and 30 Oct 2026 deadline.",
 offlinks=[('Aditya Birla Capital programme page (Buddy4Study)','https://www.buddy4study.com/article/aditya-birla-capital-scholarship')],
 related_titles=['infocepts','wings','satya'],
),

dict(
 slug='satya-scholarship-program-2026',
 title='Satya Scholarship 2026: 100% Medical Course Fee + Hostel | StudyDesk Scholarships',
 meta='Satya Scholarship Program 2026 by Nehru Sidhant Kender Trust: 100% annual course fee plus hostel & meal support for first-year MBBS, BDS, nursing students from Punjab. Deadline 31 Oct 2026.',
 short='Satya Scholarship Program 2026', kicker='Trust · Medical · Punjab',
 mono='S', prov_short='Nehru Sidhant Kender Trust', prov_long='Nehru Sidhant Kender Trust',
 h1='Satya Scholarship Program 2026',
 sub='100% annual course fee coverage plus hostel and meal support — for first-year medical and health-sciences students on the Punjab route.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','100% course fee<small>+ hostel & meal support, full course</small>'),
              ('Who can apply','1st-year MBBS/BDS/nursing etc.<small>Punjab-route eligibility</small>'),
              ('Income limit','Rs 8 lakh / year<small>Parental income</small>'),
              ('Deadline','31 Oct 2026<small>Online only</small>'),
              ('Courses','MBBS · BDS · BPT · Nursing<small>3–5 yr UG / integrated masters</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Satya Scholarship Program 2026</strong>, an initiative of the <strong>Nehru Sidhant Kender Trust</strong>, provides <strong>100% annual course fee coverage along with hostel/accommodation and meal support</strong> to eligible students pursuing 3–5-year undergraduate or integrated master's programmes in Medical &amp; Health Sciences.</p>
      <p>Two routes qualify: students <strong>from Punjab</strong> admitted to eligible courses at <strong>12 selected institutes in Ludhiana district</strong>, and students <strong>from Ludhiana district</strong> admitted to eligible courses at <strong>selected top NIRF-ranked medical institutions across India</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>First-year student</strong> in a 3–5-year UG or integrated master's programme: <strong>MBBS, BDS, BPT, B.Sc. Nursing, B.Sc. Allied &amp; Healthcare</strong>.</li>
        <li>Passed Class 12 from a <strong>recognised board in Punjab</strong> with at least <strong>60% aggregate</strong>.</li>
        <li><strong>Route A:</strong> student from Punjab with admission to an eligible course at one of the <strong>12 selected institutes in Ludhiana district</strong>.</li>
        <li><strong>Route B:</strong> student from <strong>Ludhiana district</strong> with admission to an eligible course at a <strong>selected top NIRF-ranked medical institution</strong> anywhere in India.</li>
        <li>Annual <strong>parental income not exceeding Rs 8 lakh</strong> (separate guardian income provisions for orphans).</li>
        <li><strong>Indian citizen</strong>; not receiving any other educational scholarship.</li>
      </ul>
      <div class="honest-note"><strong>Preference may be given to:</strong> girl students, sportspersons, persons with disabilities (PwD), orphans, and children of single parents.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% annual course fee coverage for the entire course duration.</strong></li>
        <li>Additional support for <strong>hostel, accommodation and meals</strong>, as per programme guidelines.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your Class 12 marksheet (Punjab board), admission proof, ID proof, income proof and bank details ready.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the application page</strong>On the Buddy4Study portal.</li>
        <li><strong>Confirm your route</strong>Punjab → Ludhiana institutes, or Ludhiana district → top NIRF medical institutions.</li>
        <li><strong>Fill and upload</strong>Personal, academic and income details with documents.</li>
        <li><strong>Submit before 31 October 2026</strong>Online only.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am from Amritsar, studying MBBS in Ludhiana. Am I eligible?","Yes — Route A covers students from Punjab admitted to eligible courses at the 12 selected Ludhiana institutes."),
 ("I am from Ludhiana, studying MBBS in Delhi. Am I eligible?","Yes — Route B covers Ludhiana-district students at selected top NIRF-ranked medical institutions across India."),
 ("Does it cover hostel and food?","Yes — alongside 100% course fee, the programme supports hostel/accommodation and meals per its guidelines."),
 ("Can I hold another scholarship with it?","No — recipients of any other educational scholarship are not eligible."),
]),
 verify='Verified 16 Oct 2026 via Sakshi Education, The Hindustan Gazette, The Hans India (Buddy4Study listing), NavJeevan Express and AgriJob — all agree on 100% course fee + hostel/meal support, the two Punjab/Ludhiana routes, eligible courses, 60% in Class 12 (Punjab board), Rs 8 lakh income limit, and 31 Oct 2026 deadline. Applications run on the Buddy4Study portal.',
 offlinks=[('Buddy4Study portal (application partner)','https://www.buddy4study.com/')],
 related_titles=['abcapital','wings','muskaan'],
),

dict(
 slug='muskaan-scholarship-2-2026-27',
 title='Muskaan Scholarship 2.0 (2026-27): Rs 12,000 for Class 9–12 | StudyDesk Scholarships',
 meta='Muskaan Scholarship Program 2.0 by Valvoline Cummins: up to Rs 12,000 for Class 9-12 students — children of drivers, mechanics and EWS families. Eligibility, deadline 30 Oct 2026.',
 short='Muskaan Scholarship 2.0', kicker='CSR · School Students',
 mono='M', prov_short='Valvoline Cummins', prov_long='Valvoline Cummins Private Limited (via Buddy4Study)',
 h1='Muskaan Scholarship Program 2.0 (2026–27)',
 sub='Up to Rs 12,000 plus mentoring — for Class 9–12 students who are children of commercial drivers, mechanics, or from EWS families.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 12,000<small>Based on actual expenses + mentoring</small>'),
              ('Who can apply','Class 9–12 students<small>Drivers\'/mechanics\' children, EWS</small>'),
              ('Income limit','Rs 8 lakh / year<small>Family income</small>'),
              ('Deadline','30 Oct 2026<small>Online via Buddy4Study</small>'),
              ('Where','18 states / UTs<small>South, east & northeast India</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Muskaan Scholarship Program 2.0 (2026–27)</strong> is a CSR initiative of <strong>Valvoline Cummins Private Limited (VCPL)</strong>, implemented through Buddy4Study. It helps schoolchildren from eligible family backgrounds continue their studies by reducing the financial burden of education.</p>
      <p>Alongside money, the programme provides <strong>mentorship support, including a session on road safety</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Studying in <strong>Class 9, 10, 11 or 12</strong> in 2026–27, in one of the <strong>18 eligible states/UTs</strong>: Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Jharkhand, Karnataka, Kerala, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Tripura, Puducherry, Sikkim, Tamil Nadu, Telangana and West Bengal.</li>
        <li>Belong to one of: <strong>children of commercial drivers</strong> (LMV/HMV licence holders), <strong>children of mechanics</strong>, or <strong>EWS category</strong> students.</li>
        <li><strong>Minimum 60% marks</strong> in the previous class.</li>
        <li>Total annual <strong>family income not exceeding Rs 8 lakh</strong> from all sources.</li>
        <li>Children of VCPL or Buddy4Study employees are <strong>not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Financial grant of <strong>up to Rs 12,000</strong>, disbursed <strong>based on actual verified educational expenses</strong> (tuition, books, uniforms, stationery — keep every receipt).</li>
        <li><strong>Mentorship support</strong>, including a dedicated road-safety session.</li>
      </ul>
      <div class="honest-note"><strong>Reimbursement-based:</strong> if your documented expenses are less than Rs 12,000, you receive only the receipt-backed amount. Collect fee receipts, book bills and uniform receipts through the year.</div>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the official application form. Keep your previous class marksheet, ID proof, parent's occupation proof (driving licence / mechanic declaration), income proof, expense receipts and bank details ready.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the programme page</strong>On the Buddy4Study portal.</li>
        <li><strong>Check state + category eligibility</strong>Confirm your state is among the 18 and your category fits.</li>
        <li><strong>Fill and upload</strong>Personal, academic, occupation and income details with documents.</li>
        <li><strong>Submit before 30 October 2026</strong>Online only.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("My father is an auto-rickshaw driver. Are we eligible?","The programme specifies commercial LMV/HMV licence holders — check the official page for how your licence category is treated."),
 ("Is it only for drivers' children?","No — children of mechanics and EWS-category students are also eligible."),
 ("Which states are covered?","18 states/UTs across southern, eastern and northeastern India (list in Eligibility above)."),
 ("How is the Rs 12,000 paid?","Based on actual verified expenses via direct bank transfer — keep all receipts."),
]),
 verify="Verified 16 Oct 2026 via Buddy4Study's official programme page, Education Post, The Hindustan Gazette and AimIndia. Deadline: the official Buddy4Study programme page (most recent, 16 days ago) shows 30 Oct 2026; older pieces (Sakshi, AgriJob) mentioned 30 Sept 2026 — confirm on the application portal before applying. Eligibility, 18-state list, Rs 12,000 reimbursement model and Rs 8 lakh income limit corroborated across sources.",
 offlinks=[('Muskaan programme page (Buddy4Study)','https://www.buddy4study.com/article/muskaan-scholarship')],
 related_titles=['infocepts','satya','abcapital'],
),
]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

# update tracker
t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 2 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 6 | wings-women-stem-iit-bombay-2027-28 | WINGS Women in STEM (IIT Bombay) | 31 Oct 2026 | Yes — Sakshi/Hans/Gazette/Campuzine |
| 7 | infocepts-innovate-impact-scholarship-2026-27 | Infocepts Innovate for Impact | 30 Oct 2026 | Yes — Sakshi/Gazette/Hindu/EduAdvice |
| 8 | aditya-birla-capital-scholarship-2026-27 | Aditya Birla Capital Scholarship | 30 Oct 2026 | Yes — B4S page/Gazette/Hans |
| 9 | satya-scholarship-program-2026 | Satya Scholarship (Nehru Sidhant Kender) | 31 Oct 2026 | Yes — Sakshi/Gazette/Hans |
| 10 | muskaan-scholarship-2-2026-27 | Muskaan Scholarship 2.0 (Valvoline Cummins) | 30 Oct 2026 | Yes — B4S page/EduPost/Gazette |

**Completed: 10 / ~17,000 (target under revision — sitemap sampling suggests a few thousand unique topics, not 17k)**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker updated')

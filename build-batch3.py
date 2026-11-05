#!/usr/bin/env python3
"""Batch 3: 5 verified articles (govt schemes, 25-31 Oct deadlines). Verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'pathani': dict(mono='P', title='Pathani Samanta Mathematics Talent Scholarship 2026-27', href='pathani-samanta-maths-talent-scholarship-2026-27.html',
              dpill='9 days to go', award='Rs 5,000/year (1,000 students)', elig='Class 11-12, Odia-medium CHSE schools; Odisha domicile; no income limit.',
              tags=[('Merit','blue'),('Odisha','teal')]),
 'icar-nts': dict(mono='ICAR', title='ICAR National Talent Scholarship (UG) 2026', href='icar-nts-ug-scholarship-2026.html',
              dpill='15 days to go', award='Rs 3,000/month', elig='UG agriculture outside home state via AIEEA; full-time study.',
              tags=[('Merit','blue'),('Central Govt','teal')]),
 'ambedkar-hp': dict(mono='A', title='Dr. Ambedkar Medhavi Chatravriti Yojana, HP 2026-27', href='ambedkar-medhavi-chatravriti-himachal-2026-27.html',
              dpill='15 days to go', award='Rs 10,000–12,000/year × 2 yrs', elig='SC/OBC HP domicile; top HPBOSE matric merit; Class 11/professional course.',
              tags=[('SC/OBC','blue'),('Himachal','teal')]),
 'nirman': dict(mono='N', title='Nirman Shramik Kalyan Yojana Scholarship 2026-27', href='nirman-shramik-kalyan-yojana-odisha-2026-27.html',
              dpill='15 days to go', award='Rs 2,000–40,000/year', elig='Children of registered construction workers; Class 6+; Odisha domicile.',
              tags=[('Workers’ children','blue'),('Odisha','teal')]),
 'megh-sc': dict(mono='NSP', title='NSP Post-Matric Scholarship for SC Students, Meghalaya 2026-27', href='nsp-post-matric-sc-meghalaya-2026-27.html',
              dpill='14 days to go', award='Up to Rs 13,500 + maintenance', elig='SC students, Meghalaya domicile, Class 11–PhD; income ≤ Rs 2.5 lakh.',
              tags=[('SC','blue'),('Meghalaya','teal')]),
}

ARTICLES = [
dict(
 slug='pathani-samanta-maths-talent-scholarship-2026-27',
 title='Pathani Samanta Mathematics Talent Scholarship 2026-27: Rs 5,000/Year | StudyDesk',
 meta='Pathani Samanta Mathematics Talent Scholarship 2026-27: Rs 5,000/year for 1,000 Class 11-12 students in Odia-medium schools. Eligibility, deadline 25 Oct 2026.',
 short='Pathani Samanta Scholarship 2026–27', kicker='Odisha Government · Merit',
 mono='P', prov_short='Govt. of Odisha', prov_long='School & Mass Education Dept., Government of Odisha',
 h1='Pathani Samanta Mathematics Talent Scholarship 2026–27',
 sub='Rs 5,000 a year for 1,000 meritorious Class 11–12 students with talent in Mathematics — Odisha’s own maths scholarship.',
 dpill='9 days to go', dl_long='25 Oct 2026',
 facts=facts([('Award','Rs 5,000 / year<small>Rs 500 × 10 months; 1,000 students</small>'),
              ('Who can apply','Class 11–12 students<small>Odia-medium CHSE schools; maths talent</small>'),
              ('Income limit','None<small>No income criterion</small>'),
              ('Deadline','25 Oct 2026<small>Odisha scholarship portal</small>'),
              ('Selection','HSC + Maths marks<small>Top 2,088 HSC 2026 passers eligible</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pathani Samanta Mathematics Talent Scholarship (PSMTS) 2026–27</strong>, run by the School &amp; Mass Education Department, Government of Odisha, rewards Higher Secondary students with proficiency in Mathematics. Named after the legendary Odia astronomer-mathematician Pathani Samanta, it selects <strong>1,000 students every year</strong>.</p>
      <p>For fresh selection in 2026–27, the eligible pool is the <strong>top 2,088 students who passed the HSC Examination 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Domicile of Odisha.</strong></li>
        <li>Studying in <strong>Class 11 or Class 12</strong> in an <strong>Odia-medium Higher Secondary School affiliated to CHSE Odisha</strong>.</li>
        <li>Belong to <strong>General, SC, ST, OBC or SEBC</strong> category.</li>
        <li>Demonstrated proficiency in Mathematics (selection is on HSC aggregate + Mathematics marks, with SCP marks as tiebreaker).</li>
        <li><strong>No income criterion</strong> — the 2026–27 guidelines prescribe none.</li>
      </ul>
      <div class="honest-note"><strong>Can be held with other scholarships:</strong> the guidelines state a student may enjoy more than one scholarship at a time, including this one.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 5,000 per year</strong> (Rs 500 per month for 10 months).</li>
        <li>Paid via <strong>Direct Benefit Transfer (DBT)</strong> to the student's bank account.</li>
        <li><strong>Renewable</strong> in Class 12 for Class 11 recipients, subject to promotion and conditions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>HSC marksheet and certificate</li><li>Aadhaar Card</li>
        <li>Bank account details (account number + IFSC)</li>
        <li>College ID Card — or admission receipt, library card, or letter of undertaking from the college authority</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Odisha State Scholarship Portal</strong>scholarship.odisha.gov.in</li>
        <li><strong>Register / log in</strong>With Aadhaar-linked details.</li>
        <li><strong>Select Pathani Samanta Mathematics Talent Scholarship</strong>Fill academic and bank details; upload documents.</li>
        <li><strong>Submit before 25 October 2026</strong>Applications opened 20 August 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there an income limit?","No — the 2026–27 guidelines do not prescribe any income criterion."),
 ("How are students selected?","On aggregate HSC marks plus Mathematics marks as provided by BSE Odisha, with SCP marks as tiebreaker."),
 ("Can I hold it with another scholarship?","Yes — the guidelines allow it alongside other scholarships."),
 ("How is the money paid?","By DBT directly to the beneficiary's bank account."),
]),
 verify='Verified 16 Oct 2026 via GovtSchemes.in, ScholarshipsX and SarkariYojana reporting on the official Odisha guidelines: Rs 5,000/year, 1,000 students, Class 11–12 Odia-medium CHSE schools, no income limit, selection on HSC+Maths marks, 25 Oct 2026 deadline on the Odisha State Scholarship Portal.',
 offlinks=[('Odisha State Scholarship Portal','https://scholarship.odisha.gov.in/')],
 related_titles=['nirman','ambedkar-hp','megh-sc'],
),

dict(
 slug='icar-nts-ug-scholarship-2026',
 title='ICAR National Talent Scholarship (UG) 2026: Rs 3,000/Month | StudyDesk Scholarships',
 meta='ICAR National Talent Scholarship (Undergraduate) 2026: Rs 3,000/month for UG agriculture students studying outside their home state. Eligibility, deadline 31 Oct 2026.',
 short='ICAR NTS (UG) 2026', kicker='Central Government · ICAR',
 mono='ICAR', prov_short='ICAR', prov_long='Indian Council of Agricultural Research',
 h1='ICAR National Talent Scholarship (Undergraduate) 2026',
 sub='Rs 3,000 a month for UG agriculture students admitted through the All India entrance — studying outside their home state.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 3,000 / month<small>Renewable for the degree duration</small>'),
              ('Who can apply','UG agriculture students<small>Outside home state via AIEEA</small>'),
              ('Study','Full-time<small>Good conduct; no employment</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Scheme','Strengthening Higher Agri-Education<small>ICAR Education Division</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>ICAR National Talent Scholarship (Undergraduate)</strong> is awarded by the Indian Council of Agricultural Research under its Education Division scheme for strengthening higher agricultural education. It supports Bachelor's students in agriculture and allied disciplines who secured admission through the All India Entrance Examination and study <strong>outside their state of domicile</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Pursuing a <strong>Bachelor's degree in agriculture or allied disciplines</strong> at an <strong>ICAR-recognised agricultural university located outside your state of domicile</strong>.</li>
        <li>Admission secured through the <strong>All India Entrance Examination (AIEEA)</strong>.</li>
        <li>University funded under ICAR's scheme for strengthening higher agricultural education.</li>
        <li>Maintain <strong>good academic performance and conduct</strong>; pursue studies <strong>full-time</strong>; <strong>no employment</strong> alongside.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 3,000 per month.</strong></li>
        <li>Awarded initially for <strong>one year from admission</strong>; renewed for the remaining degree duration subject to performance and conduct.</li>
      </ul>
      <div class="honest-note"><strong>Amount note:</strong> older guides quote Rs 2,000 or Rs 1,000 per month — the current 2026 figure reported by The Hindu's scholarship roundup is Rs 3,000/month. Confirm on the NSP listing before applying.</div>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the NSP application form. Keep your AIEEA/admission proof, ID proof, marksheets and bank details ready.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — find the ICAR NTS (UG) listing.</li>
        <li><strong>Register / log in</strong>Fresh or renewal as applicable.</li>
        <li><strong>Fill and upload</strong>Academic, admission and bank details with documents.</li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I study agriculture in my home state. Am I eligible?","No — the university must be outside your state of domicile."),
 ("How much is the scholarship?","Rs 3,000 per month as per the latest 2026 reporting."),
 ("Is it renewed automatically?","It is awarded for one year initially and renewed for the degree duration subject to good performance and conduct."),
 ("Can I do a part-time job alongside?","No — full-time study is required and employment is not permitted."),
]),
 verify='Verified 16 Oct 2026 via The Hindu (19 Sept 2026 scholarship roundup: Rs 3,000/month, 31 Oct deadline) and an ICAR scheme knowledge base (eligibility: AIEEA admission, outside-domicile study, full-time, good conduct). Older sources quote Rs 2,000/1,000 per month — treated as outdated.',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['pathani','nirman','megh-sc'],
),

dict(
 slug='ambedkar-medhavi-chatravriti-himachal-2026-27',
 title='Dr. Ambedkar Medhavi Chatravriti Yojana HP 2026-27 | StudyDesk Scholarships',
 meta='Dr. Ambedkar Medhavi Chatravriti Yojana Himachal Pradesh 2026-27: Rs 12,000/year (SC) and Rs 10,000/year (OBC) for top HPBOSE matric merit students. Deadline 31 Oct 2026.',
 short='Ambedkar Medhavi Chatravriti HP', kicker='Himachal Pradesh · SC/OBC',
 mono='A', prov_short='Govt. of Himachal Pradesh', prov_long='Government of Himachal Pradesh (via NSP)',
 h1='Dr. Ambedkar Medhavi Chatravriti Yojana, Himachal Pradesh 2026–27',
 sub='Rs 12,000 a year for top SC students and Rs 10,000 a year for top OBC students in the HPBOSE matric merit list — for two years.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 10,000–12,000 / year<small>For 2 successive years</small>'),
              ('Who can apply','SC/OBC HP domicile<small>Top HPBOSE matric merit list</small>'),
              ('Study','Class 11 or professional course<small>Recognised institution, in/out of state</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Seats','1,250 SC + 1,000 OBC<small>Merit list based</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Dr. Ambedkar Medhavi Chatravriti Yojana</strong>, Government of Himachal Pradesh, rewards the most meritorious SC and OBC students of the state's matric examination. The <strong>top 1,250 SC students</strong> and <strong>top 1,000 OBC students</strong> in the HPBOSE Dharamshala matric merit list receive the scholarship for <strong>two successive years</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Domicile (bonafide resident) of Himachal Pradesh.</strong></li>
        <li>Belong to the <strong>SC or OBC</strong> category as declared by the HP Government.</li>
        <li><strong>Passed Class 10</strong> (HPBOSE matric examination).</li>
        <li>Figure in the <strong>top 1,250 (SC) or top 1,000 (OBC)</strong> of the HPBOSE merit list.</li>
        <li>Taken admission in <strong>Class 11 or any professional/technical course</strong> after Class 10, at a recognised institution <strong>within or outside the state</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>SC students: Rs 12,000 per year.</strong></li>
        <li><strong>OBC students: Rs 10,000 per year.</strong></li>
        <li>For <strong>two successive years</strong>; renewal subject to satisfactory performance in the first year / Class 11.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar Card</li><li>Passport-size photograph</li><li>Caste certificate (SC/OBC)</li>
        <li>Class 10 marksheet and certificate</li><li>Bank account details</li>
        <li>Income certificate, domicile proof, mobile number &amp; email ID (as asked on the form)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>New registration / login</strong>Under the applicant corner.</li>
        <li><strong>Select the scheme</strong>Dr. Ambedkar Medhavi Chatravriti Yojana (Himachal Pradesh).</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>. No application fee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am OBC but not in the top 1,000. Can I apply?","No — selection is strictly from the HPBOSE matric merit list (top 1,250 SC / top 1,000 OBC)."),
 ("Can I study outside Himachal?","Yes — admission in a recognised institution within or outside the state is allowed."),
 ("For how long is it paid?","Two successive years, with renewal linked to first-year performance."),
 ("Is there an application fee?","No."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (31 Oct 2026 deadline; Rs 12,000 SC / Rs 10,000 OBC; top 1,250 SC + 1,000 OBC merit lists) and Notopedia/govtschemes (eligibility, documents). One Notopedia page mentioned 31 May 2026 — appears to be a previous cycle; the 2026–27 deadline is 31 Oct 2026.',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['megh-sc','pathani','nirman'],
),

dict(
 slug='nirman-shramik-kalyan-yojana-odisha-2026-27',
 title='Nirman Shramik Kalyan Yojana Scholarship Odisha 2026-27 | StudyDesk',
 meta='Nirman Shramik Kalyan Yojana 2026-27: Rs 2,000–40,000/year for children of registered construction workers in Odisha (Class 6+). Eligibility, deadline 31 Oct 2026.',
 short='Nirman Shramik Kalyan Yojana', kicker='Odisha Government · Workers’ Children',
 mono='N', prov_short='Govt. of Odisha', prov_long='Labour & ESI Department, Government of Odisha',
 h1='Nirman Shramik Kalyan Yojana Scholarship 2026–27',
 sub='Rs 2,000 to Rs 40,000 a year — educational assistance for children of registered building and construction workers in Odisha.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 2,000 – 40,000 / year<small>By class; +20% for girls from Class 8</small>'),
              ('Who can apply','Children of construction workers<small>Registered with OB&OCWW Board 1+ yr</small>'),
              ('Study','Class 6 and above<small>Passed previous exam; 50% attendance</small>'),
              ('Deadline','31 Oct 2026<small>Odisha scholarship portal</small>'),
              ('Family cap','2 children max<small>Per family</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Nirman Shramik Kalyan Yojana Scholarship 2026–27</strong>, run by the Labour &amp; ESI Department, Government of Odisha, gives educational assistance to <strong>children of building and construction workers</strong> registered with the Odisha Building and Other Construction Workers' Welfare (OB&amp;OCWW) Board. Amounts rise with the class level — up to <strong>Rs 40,000 a year</strong> for professional courses in government colleges.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Indian citizen and <strong>domicile of Odisha</strong>.</li>
        <li>Studying in <strong>Class 6 or above</strong> in a recognised school/institution/university (<strong>Classes 6–7: girl children only</strong>; Class 8 onward: both).</li>
        <li><strong>Passed the previous examination</strong> with <strong>50% attendance</strong> in the current session.</li>
        <li>Parent must be a <strong>registered construction worker</strong> with the OB&amp;OCWW Board for <strong>at least one year</strong>, with <strong>up-to-date contributions</strong> (renew the Nirman Shramik Card first if lapsed).</li>
        <li>Maximum <strong>two children per family</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th>Level</th><th>Per year</th></tr>
      <tr><td>Class 6–7 (girls only)</td><td>Rs 2,000</td></tr>
      <tr><td>Class 8</td><td>Rs 2,000</td></tr>
      <tr><td>Class 9</td><td>Rs 3,000</td></tr>
      <tr><td>Class 10</td><td>Rs 4,000</td></tr>
      <tr><td>Class 11–12</td><td>Rs 5,000</td></tr>
      <tr><td>B.A./B.Sc./B.Com./PG</td><td>Rs 7,000</td></tr>
      <tr><td>Professional courses in govt. colleges (B.Tech, medical, etc.)</td><td>Rs 40,000</td></tr>
      <tr><td>B.Ed/CT/Nursing (govt. colleges)</td><td>Rs 10,000</td></tr></table>
      <ul>
        <li><strong>Girl students get 20% extra</strong> from Class 8 onward (up to Rs 48,000 for professional courses).</li>
        <li><strong>Rs 10,000 one-time cash award</strong> for scoring 90% or above in Class 10.</li>
        <li>Paid by <strong>DBT</strong> to the student's Aadhaar-linked bank account.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Student's Aadhaar card</li><li>Odisha domicile certificate</li>
        <li>Parent's Aadhaar + <strong>BOC ID / Nirman Shramik Card</strong></li>
        <li>Bank passbook copy (account number + IFSC)</li>
        <li>School/college ID card</li><li>Qualifying exam marksheet</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Odisha State Scholarship Portal</strong>scholarship.odisha.gov.in — register (new) or log in.</li>
        <li><strong>Fill the form</strong>Personal, academic, eligibility and bank details.</li>
        <li><strong>Upload documents and submit</strong>The form is verified by the District Labour Officer.</li>
        <li><strong>Deadline: 31 October 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Check the worker card first:</strong> if your parent's Board registration has lapsed or contributions are pending, renew at nirmanshramik.odisha.gov.in <em>before</em> applying — otherwise the application is rejected.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can both my brother and I apply?","Yes — up to two children per family can receive it."),
 ("My father's worker card expired. What now?","Renew it first at nirmanshramik.odisha.gov.in; lapsed registration means rejection."),
 ("Do girls get more?","Yes — 20% additional assistance from Class 8 onward."),
 ("Is there a reward for Class 10 toppers?","A one-time Rs 10,000 cash award for scoring 90% or above in Class 10."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (award table, 31 Oct 2026 deadline), SarkariYojana (documents, steps), ProjectSarthi and Bajaj Finserv guides (eligibility, 1-year registration rule, 2-children cap, 20% girls bonus). Worker registration/renewal at nirmanshramik.odisha.gov.in.',
 offlinks=[('Odisha State Scholarship Portal','https://scholarship.odisha.gov.in/')],
 related_titles=['pathani','icar-nts','ambedkar-hp'],
),

dict(
 slug='nsp-post-matric-sc-meghalaya-2026-27',
 title='NSP Post-Matric Scholarship for SC Students, Meghalaya 2026-27 | StudyDesk',
 meta='NSP Post-Matric Scholarship for SC Students, Meghalaya 2026-27: academic allowance up to Rs 13,500 plus maintenance. Eligibility, deadline 30 Oct 2026.',
 short='NSP Post-Matric SC, Meghalaya', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='NSP Post-Matric Scholarship for SC Students, Meghalaya 2026–27',
 sub='Annual academic allowance up to Rs 13,500 plus monthly maintenance — for SC students of Meghalaya from Class 11 to PhD.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 13,500 / year<small>+ Rs 230–1,350/month maintenance</small>'),
              ('Who can apply','SC students<small>Meghalaya domicile; Class 11–PhD</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Oct 2026<small>Via NSP; institute verifies by 20 Nov</small>'),
              ('Fees','Full reimbursement<small>Compulsory non-refundable fees</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Scheme of Post-Matric Scholarship for SC Students, Meghalaya 2026–27</strong>, offered by the <strong>Ministry of Social Justice and Empowerment</strong> and implemented through the National Scholarship Portal, helps SC students from low-income families continue higher education. Meghalaya's Directorate of Higher and Technical Education issued the 2026–27 advertisement on 3 July 2026.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domicile of Meghalaya</strong>.</li>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Completed <strong>Class 10</strong> (or higher secondary) with a passing grade; pursuing <strong>Class 11 to PhD</strong>.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong> in the previous financial year.</li>
        <li><strong>Cannot hold another scholarship/stipend</strong> simultaneously — if awarded another, choose the more beneficial one and inform the authority.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Annual academic allowance up to Rs 13,500</strong> plus other benefits.</li>
        <li><strong>Monthly maintenance allowance</strong> by course group: Group I (professional degrees) Rs 1,350 hosteller / Rs 550 day scholar; Group II Rs 950/530; Group III Rs 750/300; Group IV (Class 11–12, ITI) Rs 400/230.</li>
        <li><strong>Full reimbursement of compulsory non-refundable fees.</strong></li>
        <li>Paid by <strong>DBT to the Aadhaar-seeded bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar Card (+ Aadhaar-linked mobile)</li><li>OTR (One Time Registration) ID on NSP</li>
        <li>SC certificate</li><li>Income certificate from competent authority</li>
        <li>Previous year marksheet / passing certificate</li><li>Admission receipt / bonafide certificate</li>
        <li>Passport-size photograph</li><li>Aadhaar-seeded bank passbook + IFSC</li>
      </ol>
      <div class="honest-note"><strong>Aadhaar seeding is mandatory</strong> — link Aadhaar to your active bank account before applying, or the DBT payment cannot go through.</div>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — New Registration (fresh) or Login (renewal).</li>
        <li><strong>Select Meghalaya + Post-Matric SC scheme</strong>Fill academic, income and bank details; upload documents.</li>
        <li><strong>Submit before 30 October 2026</strong>Take a printout for institutional verification (last date 20 Nov 2026).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh per year of family income from all sources."),
 ("Can I apply if I already get another scholarship?","No — you cannot hold two scholarships at once; choose the more beneficial one."),
 ("I study via distance/correspondence. Am I eligible?","Yes, for Central/State university distance programmes — but no academic allowance for such courses."),
 ("When does the institute verify?","By 20 November 2026."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (30 Oct 2026 deadline; up to Rs 13,500 academic allowance; eligibility rules) and Meghalaya Portal (Directorate of Higher & Technical Education advertisement dated 3 July 2026: applications from 15 June 2026, institute verification by 20 Nov 2026, Rs 2.5 lakh income limit, Aadhaar seeding mandatory).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['ambedkar-hp','pathani','icar-nts'],
),
]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 3 (16 Oct 2026) — 5 articles, all verified (govt schemes)
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 11 | pathani-samanta-maths-talent-scholarship-2026-27 | Pathani Samanta Maths Talent (Odisha) | 25 Oct 2026 | Yes — GovtSchemes/ScholarshipsX |
| 12 | icar-nts-ug-scholarship-2026 | ICAR National Talent Scholarship (UG) | 31 Oct 2026 | Yes — The Hindu/ICAR KB |
| 13 | ambedkar-medhavi-chatravriti-himachal-2026-27 | Dr. Ambedkar Medhavi Chatravriti (HP) | 31 Oct 2026 | Yes — B4S/Notopedia |
| 14 | nirman-shramik-kalyan-yojana-odisha-2026-27 | Nirman Shramik Kalyan Yojana (Odisha) | 31 Oct 2026 | Yes — B4S/SarkariYojana |
| 15 | nsp-post-matric-sc-meghalaya-2026-27 | NSP Post-Matric SC, Meghalaya | 30 Oct 2026 | Yes — B4S/Meghalaya Portal |

**Completed: 15 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker updated')

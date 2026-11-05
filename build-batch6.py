#!/usr/bin/env python3
"""Batch 6: 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'pmss-railways': dict(mono='PMSS', title="PM's Scholarship Scheme for Ministry of Railways 2026-27", href='pm-scholarship-scheme-ministry-railways-2026-27.html',
              dpill='15 days to go', award='Rs 2,500–3,000/month', elig='Wards/widows of RPF/RPSF; 60%+; professional degree; first year.',
              tags=[('Defence/RPF','blue'),('Central Govt','teal')]),
 'isi-stipend': dict(mono='ISI', title='ISI Kolkata Stipend Scheme for UG/PG Studies 2026-27', href='isi-kolkata-stipend-scheme-ug-pg-2026-27.html',
              dpill='15 days to go', award='Rs 5,000–12,400/month', elig='ISI students via admission test; 60% to continue.',
              tags=[('Merit','blue'),('Institute','teal')]),
 'yasasvi-pre-sikkim': dict(mono='Y', title='PM Yasasvi Pre-Matric Scholarship for OBC/EBC/DNT, Sikkim 2026-27', href='pm-yasasvi-pre-matric-obc-sikkim-2026-27.html',
              dpill='15 days to go', award='Rs 4,000/year', elig='OBC/EBC/DNT; Sikkim; Class 9–10 govt schools; income ≤ Rs 2.5 lakh.',
              tags=[('OBC/EBC/DNT','blue'),('Sikkim','teal')]),
 'prematric-sc-sikkim': dict(mono='NSP', title='NSP Pre-Matric Scholarship for SC Students (Class 9 & 10), Sikkim 2026-27', href='nsp-pre-matric-sc-sikkim-2026-27.html',
              dpill='15 days to go', award='Rs 3,500–7,000/year', elig='SC; Sikkim domicile; Class 9–10; income < Rs 2.5 lakh.',
              tags=[('SC','blue'),('Sikkim','teal')]),
 'yasasvi-post-andaman': dict(mono='Y', title='PM Yasasvi Post-Matric Scholarship for OBC Students, Andaman & Nicobar 2026-27', href='pm-yasasvi-post-matric-obc-andaman-2026-27.html',
              dpill='15 days to go', award='Up to Rs 10,000/year', elig='OBC; A&N domicile; post-matric; income ≤ Rs 2.5 lakh.',
              tags=[('OBC','blue'),('Andaman & Nicobar','teal')]),
}

ARTICLES = [
dict(
 slug='pm-scholarship-scheme-ministry-railways-2026-27',
 title="Prime Minister's Scholarship Scheme for Ministry of Railways 2026-27 | StudyDesk",
 meta="PM's Scholarship Scheme for Ministry of Railways 2026-27: Rs 3,000/month (girls), Rs 2,500/month (boys) for wards of RPF/RPSF personnel. Eligibility, deadline 31 Oct 2026.",
 short="PMSS Ministry of Railways", kicker='Central Government · RPF/RPSF Wards',
 mono='PMSS', prov_short='Ministry of Railways', prov_long='Security Directorate, Railway Board (via NSP)',
 h1="Prime Minister's Scholarship Scheme for Ministry of Railways 2026–27",
 sub='Rs 3,000 a month for girls and Rs 2,500 for boys — for the wards and widows of RPF/RPSF personnel.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 2,500 – 3,000 / month<small>150 scholarships; 75 girls</small>'),
              ('Who can apply','RPF/RPSF wards & widows<small>Below gazetted rank</small>'),
              ('Marks','60%+ in qualifying exam<small>First-year professional degree</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Renewal','50% marks yearly<small>Reapply on NSP each year</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Prime Minister's Scholarship Scheme (PMSS) for the Ministry of Railways 2026–27</strong>, run by the Security Directorate, Railway Board, gives financial aid to <strong>dependent wards and widows of serving, retired or deceased RPF/RPSF personnel</strong> for recognised professional and technical courses. <strong>150 scholarships</strong> are awarded every year — 75 for girls, 75 for boys — through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Dependent ward (child) or widow</strong> of ex-serving or serving <strong>RPF/RPSF personnel below the rank of Gazetted Officer</strong>.</li>
        <li><strong>At least 60% marks</strong> in the Minimum Entry Qualification (Class 12, diploma or graduation).</li>
        <li><strong>Regular first-year admission in 2026–27</strong> to a professional degree course (BE/B.Tech, MBBS, BDS, BCA, MCA, B.Pharma, B.Ed, LLB, MBA, etc.) recognised by AICTE/UGC/MCI/NCTE.</li>
        <li>Only <strong>two wards per family</strong>.</li>
        <li><strong>Not eligible:</strong> Master's courses (except MBA/MCA), distance learning, or a second course.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Girls: Rs 3,000/month. Boys: Rs 2,500/month</strong> — paid annually via DBT.</li>
        <li>Continues for the <strong>full course duration</strong> on yearly renewal.</li>
        <li><strong>Priority order:</strong> wards/widows of personnel killed in action → died in service → retired → serving.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the NSP form — including service proof of the RPF/RPSF personnel, MEQ marksheet, admission proof, Aadhaar and bank details.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select the PMSS Railways scheme.</li>
        <li><strong>Fill and upload</strong>Service, academic and bank details with documents.</li>
        <li><strong>Submit before 31 October 2026</strong>Renew yearly on NSP with 50%+ marks.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How many scholarships are there?","150 per year — 75 for girls, 75 for boys."),
 ("I am in second year. Can I apply fresh?","No — fresh applications are only for first-year admissions in the current academic year."),
 ("What marks do I need to renew?","At least 50% in the previous year's exams, passing all subjects in the first attempt."),
 ("Is there an income limit?","No income limit is prescribed for this route."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (150 scholarships; Rs 3,000/2,500; 60% MEQ; 31 Oct 2026; 2 wards/family) and Shiksha PMSS guide (four PMSS routes; Railways = 150 seats via NSP; renewal rules).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['topclass-sc','yasasvi-sikkim','sikkim-sc'],
),

dict(
 slug='isi-kolkata-stipend-scheme-ug-pg-2026-27',
 title='ISI Kolkata Stipend Scheme for UG/PG Studies 2026-27 | StudyDesk Scholarships',
 meta='ISI Kolkata stipend 2026-27: Rs 5,000/month (UG), Rs 8,000/month (PG), Rs 12,400/month (MTech) + contingency. Eligibility and how to get it.',
 short='ISI Kolkata Stipend', kicker='Institute · Merit',
 mono='ISI', prov_short='ISI Kolkata', prov_long='Indian Statistical Institute',
 h1='Stipend Scheme for Undergraduate and Postgraduate Studies, ISI Kolkata 2026–27',
 sub='Rs 5,000 to Rs 12,400 a month plus contingency — every ISI student gets a stipend, not just a few.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 5,000 – 12,400 / month<small>By programme + contingency</small>'),
              ('Who can apply','ISI students<small>Via ISI admission test</small>'),
              ('Continue','60% performance<small>Required to keep stipend</small>'),
              ('Deadline','31 Oct 2026<small>Scholarship listing cycle</small>'),
              ('Fees','No tuition for many<small>SC/ST/PwD waivers</small>')]),
 body='''
      <h2 id="about">About the stipend</h2>
      <p>The <strong>Indian Statistical Institute</strong> pays a <strong>monthly stipend to every student</strong> in its degree programmes — one of the most generous institute-level supports in India. Amounts for 2026–27 rise with the programme level, and a yearly <strong>contingency grant</strong> (Rs 5,000 for UG, Rs 8,000 for PG) is added.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Admission to an ISI programme through the <strong>ISI Admission Test</strong> (B.Stat/B.Math via test + interview; BSDS via JEE Main/CUET).</li>
        <li>Maintain <strong>minimum 60% academic performance</strong> to continue the stipend.</li>
        <li>Students opting for <strong>KVPY/INSPIRE/JBNSTS</strong> may not be eligible for the institute stipend simultaneously.</li>
      </ul>
      <h2 id="benefits">Benefits (2026–27)</h2>
      <table><tr><th>Programme</th><th>Monthly stipend</th></tr>
      <tr><td>B Stat (Hons) / B Math (Hons)</td><td>Rs 5,000</td></tr>
      <tr><td>M Stat / M Math / MS (QE, QMBA, LIS)</td><td>Rs 8,000</td></tr>
      <tr><td>M Tech (CS, CrS, QROR)</td><td>Rs 12,400</td></tr></table>
      <ul>
        <li><strong>Contingency grant:</strong> Rs 5,000/year (UG), Rs 8,000/year (PG).</li>
        <li><strong>Fee waivers:</strong> full tuition waiver for SC/ST/PwD; income-based waivers for others.</li>
      </ul>
      <div class="honest-note"><strong>Amount note:</strong> older guides quote Rs 3,000/month for B Stat — the 2026–27 admission reporting (Mathrubhumi/Collegedunia) puts it at Rs 5,000. Confirm on the ISI admission portal.</div>
      <h2 id="documents">Documents required</h2>
      <p>As per the ISI admission portal for the programme applied to.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for ISI admission</strong>admission.isical.ac.in — via the ISI Admission Test.</li>
        <li><strong>Secure admission</strong>The stipend applies automatically to enrolled students.</li>
        <li><strong>Maintain 60%</strong>To keep receiving it each year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Does every ISI student get the stipend?","Yes — it applies to enrolled students in the degree programmes, linked to admission, not a separate application."),
 ("Can I take KVPY and the ISI stipend together?","No — students opting for KVPY/INSPIRE/JBNSTS may not be eligible for the institute stipend."),
 ("What if my marks drop below 60%?","The stipend requires minimum 60% academic performance to continue."),
 ("Is there a separate scholarship application?","No — it comes with admission; the 31 Oct date is the scholarship-listing cycle."),
]),
 verify='Verified 16 Oct 2026 via Mathrubhumi (2026-27 admissions: B Stat/B Math Rs 5,000; M Stat etc Rs 8,000; M Tech Rs 12,400) and Collegedunia (contingency Rs 5,000 UG / 8,000 PG; 60% continuation rule; KVPY exclusion).',
 offlinks=[('ISI admission portal','https://admission.isical.ac.in/')],
 related_titles=['icar-jrf','icar-ntspg','icar-nts'],
),

dict(
 slug='pm-yasasvi-pre-matric-obc-sikkim-2026-27',
 title='PM Yasasvi Pre-Matric Scholarship for OBC/EBC/DNT, Sikkim 2026-27 | StudyDesk',
 meta='PM Yasasvi Pre-Matric Scholarship for OBC, EBC and DNT students, Sikkim 2026-27: Rs 4,000/year academic allowance. Eligibility, deadline 31 Oct 2026.',
 short='PM Yasasvi Pre-Matric, Sikkim', kicker='Central Government · OBC/EBC/DNT',
 mono='Y', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='PM Yasasvi Pre-Matric Scholarship for OBC, EBC and DNT Students, Sikkim 2026–27',
 sub='Rs 4,000 a year academic allowance — for OBC, EBC and DNT students in Classes 9 and 10.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 4,000 / year<small>Academic allowance</small>'),
              ('Who can apply','OBC/EBC/DNT students<small>Sikkim; Class 9–10 govt schools</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Note','Same for day/hostel<small>Both get Rs 4,000</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>PM Yasasvi Pre-Matric Scholarship for OBC, EBC and DNT Students, Sikkim 2026–27</strong>, from the <strong>Ministry of Social Justice and Empowerment</strong>, supports <strong>Other Backward Classes, Economically Backward Classes and Denotified/Nomadic Tribe</strong> students in <strong>Classes 9 and 10 of government schools</strong> in Sikkim. Selected students receive an <strong>academic allowance of Rs 4,000 per year</strong> — the same for day scholars and hostellers.</p>
      <div class="honest-note"><strong>Don't confuse the tracks:</strong> the flagship PM YASASVI merit scheme pays Rs 75,000 (Class 9) and Rs 1,25,000 (Class 11) in Top Class Schools — this article covers the <strong>pre-matric OBC/EBC/DNT allowance of Rs 4,000/year</strong>, which is what most Class 9–10 applicants qualify for.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Resident of Sikkim.</strong></li>
        <li>Belong to <strong>OBC, EBC or DNT</strong> community.</li>
        <li>Studying in <strong>Class 9 or 10</strong> in a <strong>government school</strong>.</li>
        <li>Annual <strong>family income up to Rs 2,50,000</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 4,000 per year</strong> academic allowance.</li>
        <li>Same amount for <strong>day scholars and hostellers</strong>.</li>
        <li>Paid via <strong>DBT</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Passport-size photograph</li><li>Attested academic transcripts/certificates</li>
        <li><strong>Caste certificate</strong> signed by a Revenue Officer (Tehsildar rank or above)</li>
        <li><strong>Income certificate</strong> of parent(s)/guardian(s)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select the PM Yasasvi Pre-Matric scheme (Sikkim).</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much do hostellers get?","The same Rs 4,000 per year — the pre-matric allowance does not differ for hostellers."),
 ("What is the income limit?","Rs 2.5 lakh per year of family income from all sources."),
 ("I study in a private school. Can I apply?","No — this Sikkim pre-matric track is for government schools only."),
 ("Is this the Rs 75,000 YASASVI?","No — that is the flagship merit track for Top Class Schools; this is the Rs 4,000 pre-matric allowance."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Sikkim listing (Rs 4,000/yr; 31 Oct 2026; OBC/EBC/DNT; Class 9–10 govt schools; income ≤ Rs 2.5L) and Shiksha (Rs 4,000/yr pre-matric allowance, same for day/hostel).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['yasasvi-sikkim','prematric-sc-sikkim','sikkim-sc'],
),

dict(
 slug='nsp-pre-matric-sc-sikkim-2026-27',
 title='NSP Pre-Matric Scholarship for SC Students (Class 9 & 10), Sikkim 2026-27 | StudyDesk',
 meta='Pre-Matric Scholarship for SC Students, Sikkim 2026-27: consolidated allowance Rs 3,500 (day) / Rs 7,000 (hostel) per year. Eligibility, deadline 31 Oct 2026.',
 short='Pre-Matric SC, Sikkim', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='Pre-Matric Scholarship for SC Students (Class 9 &amp; 10), Sikkim 2026–27',
 sub='Rs 3,500 a year for day scholars, Rs 7,000 for hostellers — keeping SC students in school through Classes 9 and 10.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 3,500 – 7,000 / year<small>Day scholar / hosteller</small>'),
              ('Who can apply','SC students<small>Sikkim domicile; Class 9–10</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Extra','Disabled students<small>Additional allowance</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pre-Matric Scholarship for SC Students (Class 9 &amp; 10), Sikkim 2026–27</strong>, from the <strong>Ministry of Social Justice &amp; Empowerment</strong>, gives financial assistance to <strong>Scheduled Caste students of Sikkim in Classes 9 and 10</strong> — aimed at cutting dropout in the transition from elementary to secondary school. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian citizen</strong> and <strong>domicile of Sikkim</strong>.</li>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li><strong>Full-time student in Class 9 or 10</strong> at a recognised institution.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Consolidated academic allowance per year:</strong> Rs 3,500 (day scholars) / Rs 7,000 (hostellers).</li>
        <li><strong>Extra allowance for students with disabilities.</strong></li>
        <li>Paid by <strong>DBT</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Sikkim)</li><li>SC certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank details</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Sikkim + Pre-Matric SC scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much do I get?","Rs 3,500 per year as a day scholar, Rs 7,000 as a hosteller, plus an extra allowance if you have a disability."),
 ("What is the income limit?","Below Rs 2,50,000 per year of family income."),
 ("Which classes are covered?","Class 9 and Class 10."),
 ("Where do I apply?","On the National Scholarship Portal, scholarships.gov.in."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Sikkim listing (Rs 3,500 day / 7,000 hostel per annum; 31 Oct 2026; SC; Sikkim domicile; income < Rs 2.5L).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['yasasvi-pre-sikkim','sikkim-sc','yasasvi-sikkim'],
),

dict(
 slug='pm-yasasvi-post-matric-obc-andaman-2026-27',
 title='PM Yasasvi Post-Matric Scholarship for OBC Students, Andaman & Nicobar 2026-27 | StudyDesk',
 meta='PM Yasasvi Post-Matric Scholarship for OBC students, Andaman & Nicobar 2026-27: up to Rs 10,000/year. Eligibility, deadline 31 Oct 2026.',
 short='PM Yasasvi Post-Matric, A&N', kicker='Central Government · OBC',
 mono='Y', prov_short='Dept. of Social Justice', prov_long='Department of Social Justice & Empowerment, Govt. of India',
 h1='PM Yasasvi Post-Matric Scholarship for OBC Students, Andaman &amp; Nicobar Islands 2026–27',
 sub='Up to Rs 10,000 a year — for OBC students of the Andaman & Nicobar Islands in post-matric courses.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 10,000 / year<small>Allowance + fees</small>'),
              ('Who can apply','OBC students<small>A&N domicile; post-matric</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Aadhaar-seeded account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>PM Yasasvi Post-Matric Scholarship for OBC Students, Andaman &amp; Nicobar Islands 2026–27</strong>, offered by the <strong>Department of Social Justice &amp; Empowerment, Government of India</strong>, supports <strong>Other Backward Classes students of the islands</strong> pursuing post-matriculation courses. Selected candidates receive financial assistance of <strong>up to Rs 10,000 per year</strong> covering the academic allowance and fees.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domiciled in Andaman &amp; Nicobar Islands</strong>.</li>
        <li>Belong to the <strong>OBC</strong> community of the UT.</li>
        <li>Studying a <strong>post-matriculation or post-secondary course</strong> in a recognised institution.</li>
        <li>Passed <strong>matriculation or higher</strong> from a recognised board/university.</li>
        <li>Annual <strong>parent/guardian income ≤ Rs 2,50,000</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to Rs 10,000 per year</strong> — academic allowance plus tuition fees.</li>
        <li>Paid by <strong>DBT into the Aadhaar-seeded bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar Card</li><li>OBC caste certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank passbook copy</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select the PM Yasasvi Post-Matric OBC scheme (Andaman &amp; Nicobar).</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much will I receive?","Up to Rs 10,000 per year, covering the academic allowance and fees."),
 ("What is the income limit?","Rs 2.5 lakh per year of parent/guardian income from all sources."),
 ("Which courses are covered?","Recognised post-matriculation or post-secondary courses."),
 ("Where do I apply?","On the National Scholarship Portal, scholarships.gov.in."),
]),
 verify='Verified 16 Oct 2026 via the Buddy4Study 2026-27 Andaman & Nicobar listing (up to Rs 10,000/yr; 31 Oct 2026) and the PM Yasasvi scheme structure confirmed across the Sikkim post-matric listing and CollegeDunia guide (OBC; income ≤ Rs 2.5L; NSP).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['yasasvi-sikkim','oasis-obc','sikkim-sc'],
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
p['done'] += ["Prime Minister's Scholarship Scheme For Ministry of Railways 2026-27",
 'Stipend Scheme for Undergraduate and Postgraduate Studies ISI Kolkata 2026-27',
 'PM Yasasvi Pre-Matric Scholarship For OBC, EBC, and DNT Students, Sikkim 2026-27',
 'NSP Pre-Matric Scholarship for SC Students (Class 9 & 10), Sikkim 2026-27',
 'PM Yasasvi Post-Matric Scholarship for OBC Students, Andaman and Nicobar 2026-27']
p['runs'] = 6
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 6 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 26 | pm-scholarship-scheme-ministry-railways-2026-27 | PMSS Ministry of Railways | 31 Oct 2026 | Yes — B4S/Shiksha |
| 27 | isi-kolkata-stipend-scheme-ug-pg-2026-27 | ISI Kolkata Stipend UG/PG | 31 Oct 2026 | Yes — Mathrubhumi/Collegedunia |
| 28 | pm-yasasvi-pre-matric-obc-sikkim-2026-27 | PM Yasasvi Pre-Matric, Sikkim | 31 Oct 2026 | Yes — B4S/Shiksha |
| 29 | nsp-pre-matric-sc-sikkim-2026-27 | NSP Pre-Matric SC, Sikkim | 31 Oct 2026 | Yes — B4S |
| 30 | pm-yasasvi-post-matric-obc-andaman-2026-27 | PM Yasasvi Post-Matric OBC, A&N | 31 Oct 2026 | Yes — B4S/scheme structure |

**Completed: 30 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

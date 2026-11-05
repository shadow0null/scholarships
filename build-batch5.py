#!/usr/bin/env python3
"""Batch 5: 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'yasasvi-sikkim': dict(mono='Y', title='PM Yasasvi Post-Matric Scholarship for OBC/EBC/DNT, Sikkim 2026-27', href='pm-yasasvi-post-matric-obc-sikkim-2026-27.html',
              dpill='15 days to go', award='Up to Rs 20,000/year', elig='OBC/EBC/DNT; Sikkim domicile; post-matric; income ≤ Rs 2.5 lakh.',
              tags=[('OBC/EBC/DNT','blue'),('Sikkim','teal')]),
 'oasis-obc': dict(mono='WB', title='Oasis Post-Matric Scholarship for OBC Students, WB 2026-27', href='oasis-post-matric-obc-west-bengal-2026-27.html',
              dpill='15 days to go', award='Up to Rs 20,000/year', elig='OBC; West Bengal domicile; Class 11+; income ≤ Rs 1 lakh.',
              tags=[('OBC','blue'),('West Bengal','teal')]),
 'sikkim-sc': dict(mono='NSP', title='NSP Post-Matric Scholarship for SC Students, Sikkim 2026-27', href='nsp-post-matric-sc-sikkim-2026-27.html',
              dpill='15 days to go', award='Up to Rs 13,500 + maintenance', elig='SC; Sikkim domicile; Class 11–PhD; income ≤ Rs 2.5 lakh.',
              tags=[('SC','blue'),('Sikkim','teal')]),
 'manipur-st': dict(mono='NSP', title='NSP Pre-Matric Scholarship for ST Students (Class 9 & 10), Manipur 2026-27', href='nsp-pre-matric-st-manipur-2026-27.html',
              dpill='14 days to go', award='Up to Rs 350/month × 10', elig='ST; Manipur domicile; Class 9–10; income ≤ Rs 2 lakh.',
              tags=[('ST','blue'),('Manipur','teal')]),
 'icar-jrf': dict(mono='ICAR', title='ICAR Junior Research Fellowship (PGS) 2026', href='icar-junior-research-fellowship-pgs-2026.html',
              dpill='15 days to go', award='Rs 8,640–12,000/month', elig='Bachelor’s in agriculture; 60%/55%; age 19+; via All India exam.',
              tags=[('Fellowship','blue'),('Central Govt','teal')]),
}

ARTICLES = [
dict(
 slug='pm-yasasvi-post-matric-obc-sikkim-2026-27',
 title='PM Yasasvi Post-Matric Scholarship for OBC/EBC/DNT, Sikkim 2026-27 | StudyDesk',
 meta='PM Yasasvi Post-Matric Scholarship for OBC, EBC and DNT students, Sikkim 2026-27: academic allowance + tuition up to Rs 20,000. Eligibility, deadline 31 Oct 2026.',
 short='PM Yasasvi Post-Matric, Sikkim', kicker='Central Government · OBC/EBC/DNT',
 mono='Y', prov_short='Dept. of Social Justice', prov_long='Department of Social Justice & Empowerment, Govt. of India',
 h1='PM Yasasvi Post-Matric Scholarship for OBC, EBC and DNT Students, Sikkim 2026–27',
 sub='Academic allowance plus tuition fees up to Rs 20,000 a year — for OBC, EBC and DNT students of Sikkim.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 20,000 / year<small>Allowance + tuition fees</small>'),
              ('Who can apply','OBC/EBC/DNT students<small>Sikkim domicile; post-matric</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Aadhaar-seeded account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>PM Yasasvi Post-Matric Scholarship for OBC, EBC and DNT Students, Sikkim 2026–27</strong>, offered by the <strong>Department of Social Justice &amp; Empowerment, Government of India</strong>, gives financial assistance to students of the OBC, EBC and Denotified/Nomadic/Semi-Nomadic Tribe communities of Sikkim studying at the post-matric level. Selected candidates receive an <strong>annual academic allowance plus tuition fees of up to Rs 20,000</strong>.</p>
      <div class="honest-note"><strong>Two Yasasvi tracks:</strong> the flagship PM YASASVI school scheme (Rs 75,000 for Class 9, Rs 1,25,000 for Class 11, merit-based, Top Class Schools) is separate — this article covers the <strong>state post-matric component for Sikkim</strong> applied for on NSP.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domiciled in Sikkim</strong>.</li>
        <li>Belong to <strong>OBC, EBC or DNT</strong> communities of the state.</li>
        <li>Studying a <strong>post-matriculation or post-secondary course</strong> in a recognised institution/college/university.</li>
        <li>Passed <strong>matriculation / higher secondary or higher</strong> from a recognised board/university.</li>
        <li>Annual <strong>parent/guardian income ≤ Rs 2,50,000</strong>.</li>
        <li>Not repeating the same stage of education in a different subject; correspondence/distance courses eligible only via Central/State universities.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Annual academic allowance + tuition fees up to Rs 20,000.</strong></li>
        <li>Maintenance stipend and course fees as per scheme terms.</li>
        <li>Paid by <strong>DBT into the Aadhaar-seeded bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar Card</li><li>Caste certificate (OBC/EBC/DNT)</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank passbook copy</li><li>Passport-size photograph</li>
        <li>Mobile number &amp; email ID</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Fresh or renewal.</li>
        <li><strong>Select the scheme</strong>PM Yasasvi Post-Matric for OBC/EBC/DNT (Sikkim).</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh per year of parent/guardian income from all sources."),
 ("I study via correspondence. Can I apply?","Yes, for Central/State university distance programmes."),
 ("Is this the same as the Rs 1.25 lakh YASASVI?","No — that is the flagship school scheme; this is the state post-matric component (up to Rs 20,000)."),
 ("Can I hold another scholarship with it?","If awarded two scholarships, you must choose one and inform the authority through your institution's head."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Sikkim listing (up to Rs 20,000; 31 Oct 2026; OBC/EBC/DNT; Sikkim domicile; income ≤ Rs 2.5L) and CollegeDunia PM YASASVI guide (scheme structure, flagship amounts).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['sikkim-sc','oasis-obc','manipur-st'],
),

dict(
 slug='oasis-post-matric-obc-west-bengal-2026-27',
 title='Oasis Post-Matric Scholarship for OBC Students, West Bengal 2026-27 | StudyDesk',
 meta='Oasis Post-Matric Scholarship for OBC students, West Bengal 2026-27: up to Rs 20,000/year for hostellers. Eligibility, income limit, deadline 31 Oct 2026.',
 short='Oasis Post-Matric OBC, WB', kicker='West Bengal · OBC',
 mono='WB', prov_short='Govt. of West Bengal', prov_long='Backward Classes Welfare Dept., Government of West Bengal',
 h1='Oasis Post-Matric Scholarship for OBC Students, West Bengal 2026–27',
 sub='Up to Rs 20,000 a year for hostellers — West Bengal’s Oasis track for OBC post-matric students.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 20,000 / year<small>Hostellers; by course group</small>'),
              ('Who can apply','OBC students<small>WB domicile; Class 11+</small>'),
              ('Income limit','Rs 1 lakh / year<small>OBC-specific limit</small>'),
              ('Deadline','31 Oct 2026<small>oasis.gov.in</small>'),
              ('Mode','DBT<small>Aadhaar-linked account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Oasis Post-Matric Scholarship for OBC Students 2026–27</strong> is West Bengal's dedicated track — run by the <strong>Backward Classes Welfare Department</strong> — for <strong>Other Backward Classes</strong> students from Class 11 through postgraduate level. Applications run on the official <strong>Oasis portal (oasis.gov.in)</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Permanent resident (domicile) of West Bengal.</strong></li>
        <li>Belong to the <strong>OBC</strong> category with a valid caste certificate.</li>
        <li>Studying in <strong>Class 11 or above</strong> — ITI, diploma, degree, PG — at an institution <strong>inside India</strong>.</li>
        <li>Annual <strong>family income up to Rs 1,00,000</strong> (the OBC-specific limit; SC/ST limit is Rs 2.5 lakh).</li>
        <li>Passed the previous year's examination.</li>
        <li>Active bank account in the student's own name, <strong>linked with Aadhaar</strong>.</li>
        <li><strong>Not taking any other scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to Rs 20,000 per year</strong> for OBC hostellers (amount varies by course group and level).</li>
        <li>Maintenance allowance plus <strong>reimbursement of compulsory non-refundable fees</strong>.</li>
        <li>Paid by <strong>DBT</strong> to the Aadhaar-linked bank account.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar details</li><li>OBC caste certificate</li><li>Income certificate</li>
        <li>Previous exam marksheet</li><li>Bank details (Aadhaar-linked)</li>
        <li>Photograph + institution details</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Oasis portal</strong>oasis.gov.in</li>
        <li><strong>Register / log in</strong>New applicants register; renewals log in.</li>
        <li><strong>Fill the form and upload documents</strong></li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Income limit differs by category:</strong> OBC applicants face a Rs 1 lakh ceiling, while SC/ST applicants get Rs 2.5 lakh. Check the correct track before applying.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit for OBC?","Rs 1,00,000 per year of family income."),
 ("How much can I get?","Up to Rs 20,000 per year for hostellers, varying by course group."),
 ("Can I apply if I study outside West Bengal?","Yes — the institution must be inside India; West Bengal domicile is what matters."),
 ("Where do I apply?","On the official Oasis portal, oasis.gov.in — not on NSP."),
]),
 verify='Verified 16 Oct 2026 via Shiksha (WB domicile, OBC track, income ≤ Rs 1L for OBC, OTR, no other scholarship), the B4S 2026-27 listing (up to Rs 20,000; 31 Oct 2026), and oasisscholarship.in amount table.',
 offlinks=[('Oasis portal (official)','https://oasis.gov.in/')],
 related_titles=['oasis-scst','yasasvi-sikkim','sikkim-sc'],
),

dict(
 slug='nsp-post-matric-sc-sikkim-2026-27',
 title='NSP Post-Matric Scholarship for SC Students, Sikkim 2026-27 | StudyDesk Scholarships',
 meta='NSP Post-Matric Scholarship for SC Students, Sikkim 2026-27: academic allowance up to Rs 13,500 plus maintenance. Eligibility, deadline 31 Oct 2026.',
 short='NSP Post-Matric SC, Sikkim', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='NSP Post-Matric Scholarship for SC Students, Sikkim 2026–27',
 sub='Annual academic allowance up to Rs 13,500 plus monthly maintenance — for SC students of Sikkim.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 13,500 / year<small>+ Rs 230–1,200/month maintenance</small>'),
              ('Who can apply','SC students<small>Sikkim domicile; Class 11–PhD</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Fees','Full reimbursement<small>Compulsory non-refundable fees</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Scheme of Post-Matric Scholarship for SC Students, Sikkim 2026–27</strong>, offered by the <strong>Ministry of Social Justice and Empowerment</strong> and administered by the <strong>Department of Social Welfare, Government of Sikkim</strong>, supports SC students of the state from <strong>Class 11 to postgraduate level</strong>. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Domiciled in Sikkim</strong> and belonging to the <strong>Scheduled Caste</strong> category of the state.</li>
        <li>Studying a <strong>post-matriculation or post-secondary course</strong> in a recognised institution/college/university.</li>
        <li>Passed <strong>matriculation / higher secondary or higher</strong> from a recognised board/university.</li>
        <li>Annual <strong>parent/guardian income ≤ Rs 2,50,000</strong>.</li>
        <li>Not repeating the same educational stage in a different subject.</li>
        <li>Distance/continuing-education students eligible only for Central/State university courses.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Annual academic allowance up to Rs 13,500</strong> plus other benefits.</li>
        <li><strong>Monthly maintenance allowance Rs 230–1,200</strong> by course group and hosteller/day-scholar status.</li>
        <li><strong>Full reimbursement of compulsory non-refundable fees.</strong></li>
        <li>Paid by <strong>DBT to the Aadhaar-linked bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Sikkim)</li><li>Caste certificate (SC)</li><li>Income certificate</li>
        <li>Previous year's marksheet</li><li>Bank passbook (Aadhaar-linked)</li><li>Passport-size photograph</li>
        <li>Aadhaar details for OTR</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — complete OTR if fresh.</li>
        <li><strong>Select Sikkim + Post-Matric SC scheme</strong>Fill details; upload documents.</li>
        <li><strong>Submit before 31 October 2026</strong>Institute verification follows.</li>
      </ol>
      <div class="honest-note"><strong>Two scholarships?</strong> If you are awarded two simultaneously, you may choose one — communicate your choice through your institution's head.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh per year of parent/guardian income from all sources."),
 ("Which classes are covered?","Class 11 through postgraduate level, including ITI, diploma, UG, PG, technical and professional courses."),
 ("Is OTR compulsory?","Yes — fresh applicants must complete One Time Registration on NSP before applying."),
 ("Is there an application fee?","No — applying on NSP is completely free."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Sikkim listing (up to Rs 13,500; 31 Oct 2026; Sikkim domicile; income ≤ Rs 2.5L) cross-checked with AssamJobApply and SchemesInIndia (NSP dates, maintenance Rs 230–1,200, OTR requirement).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['yasasvi-sikkim','megh-sc','oasis-obc'],
),

dict(
 slug='nsp-pre-matric-st-manipur-2026-27',
 title='NSP Pre-Matric Scholarship for ST Students (Class 9 & 10), Manipur 2026-27 | StudyDesk',
 meta='Pre-Matric Scholarship for ST Students, Manipur 2026-27: up to Rs 350/month for 10 months plus books grant. Eligibility, deadline 30 Oct 2026.',
 short='Pre-Matric ST, Manipur', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via NSP)',
 h1='Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Manipur 2026–27',
 sub='Up to Rs 350 a month for 10 months plus a books grant — keeping ST students in school through Classes 9 and 10.',
 dpill='14 days to go', dl_long='30 Oct 2026',
 facts=facts([('Award','Up to Rs 350 / month × 10<small>+ Rs 750–1,000 books grant</small>'),
              ('Who can apply','ST students<small>Manipur domicile; Class 9–10</small>'),
              ('Income limit','Rs 2 lakh / year<small>Family income</small>'),
              ('Deadline','30 Oct 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Direct to bank account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Manipur 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, gives financial assistance to <strong>Scheduled Tribe students of Manipur in Classes 9 and 10</strong> — aimed at cutting dropout in the transition from elementary to secondary school. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of India</strong> and <strong>domicile of Manipur</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribes (ST)</strong> category.</li>
        <li>Studying in <strong>Class 9 or 10</strong> in a government school, or a school recognised by the government / Central-State Board.</li>
        <li>Annual <strong>parent/guardian income ≤ Rs 2,00,000</strong>.</li>
        <li><strong>Not availing any other centrally-funded pre-matric scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly scholarship for 10 months:</strong> Rs 150 (day scholars) / Rs 350 (hostellers).</li>
        <li><strong>Books and ad-hoc grant per year:</strong> Rs 750 (day scholars) / Rs 1,000 (hostellers).</li>
        <li>Additional allowances for ST students with disabilities in private unaided schools, per the notification.</li>
        <li>Paid by <strong>DBT</strong> directly to the student's bank account.</li>
      </ul>
      <div class="honest-note"><strong>Rates follow the state notification:</strong> the Ministry's standard pre-matric ST rates are Rs 225/525 per month — the Manipur listing shows Rs 150/350. Confirm the applicable rate on the NSP listing before applying.</div>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Manipur)</li><li>ST certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank details</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Manipur + Pre-Matric ST scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>30 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2,00,000 per year of parent/guardian income."),
 ("Can I apply if I get another pre-matric scholarship?","No — not if it is centrally funded; if awarded two, choose one and inform through your institution's head."),
 ("How is the money paid?","By DBT directly to the student's bank account."),
 ("Which classes are covered?","Class 9 and Class 10."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Manipur listing (30 Oct 2026; Rs 150/350 per month × 10; Rs 750/1,000 books grant; income ≤ Rs 2L) cross-checked with EdexLive on the Ministry of Tribal Affairs scheme (standard rates Rs 225/525 noted as differing — flagged in article).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['yasasvi-sikkim','sikkim-sc','oasis-obc'],
),

dict(
 slug='icar-junior-research-fellowship-pgs-2026',
 title='ICAR Junior Research Fellowship (PGS) 2026 | StudyDesk Scholarships',
 meta='ICAR Junior Research Fellowship for Postgraduate Studies 2026: Rs 8,640–12,000/month + contingency. Eligibility, deadline 31 Oct 2026.',
 short='ICAR JRF (PGS) 2026', kicker='Central Government · ICAR · Fellowship',
 mono='ICAR', prov_short='ICAR', prov_long='Indian Council of Agricultural Research',
 h1='ICAR Junior Research Fellowship for Postgraduate Studies 2026',
 sub='Rs 8,640 to Rs 12,000 a month plus contingency — ICAR’s fellowship for Master’s students in agricultural sciences.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 8,640 – 12,000 / month<small>+ Rs 6,000/yr contingency</small>'),
              ('Who can apply','Agriculture graduates<small>60%/55%; age 19+</small>'),
              ('Duration','2 years<small>Via All India exam merit</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Fields','All agri disciplines<small>Vet sciences paid higher</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>ICAR Junior Research Fellowship for Postgraduate Studies (PGS)</strong> is awarded by the Indian Council of Agricultural Research to meritorious graduates pursuing <strong>Master's degree programmes in agricultural sciences</strong>. It is awarded on <strong>merit in the All India Competitive Entrance Examination</strong>, with concurrent admission to a Master's programme at a State Agricultural University or Deemed University. It runs for <strong>two years</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>Bachelor's degree</strong> in agriculture/allied sciences (or be appearing in the final examination).</li>
        <li><strong>60% marks or 6.60/10 OGPA</strong> for General/OBC/UPS; <strong>55% or 5.50/10</strong> for SC/ST/PH.</li>
        <li><strong>Minimum age 19 years</strong> at the time of the examination (reservations per Government of India rules).</li>
        <li>Secure admission to a Master's programme alongside the fellowship award.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Veterinary sciences: Rs 12,000/month</strong> + Rs 6,000/year contingency.</li>
        <li><strong>All other disciplines: Rs 8,640/month</strong> + Rs 6,000/year contingency.</li>
        <li>Duration: <strong>2 years.</strong></li>
      </ul>
      <div class="honest-note"><strong>Rates are per the scheme listing</strong> and subject to periodic revision by the Council — confirm the current rates on the NSP listing before applying.</div>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the NSP application form — including photograph, signature and thumb impression (left for males, right for females) for the online application.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — find the ICAR JRF (PGS) listing.</li>
        <li><strong>Register / log in</strong></li>
        <li><strong>Fill and upload</strong>Academic and bank details with documents.</li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the monthly amount?","Rs 8,640 for most disciplines and Rs 12,000 for veterinary sciences, plus Rs 6,000 per year contingency."),
 ("How is it awarded?","On merit in the All India Competitive Entrance Examination, with concurrent Master's admission."),
 ("What are the marks requirements?","60% (Gen/OBC) or 55% (SC/ST/PH) in the Bachelor's degree."),
 ("How long does it last?","Two years."),
]),
 verify='Verified 16 Oct 2026 via Oliveboard ICAR-JRF guide (Rs 8,640 non-vet / Rs 12,000 vet + Rs 6,000/yr contingency; 2 years; 60%/55%; age 19+; All India exam merit) and the B4S 2026-27 NSP listing (31 Oct 2026 deadline).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['icar-ntspg','icar-nts','topclass-sc'],
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
p['done'] += ['PM Yasasvi Post-Matric Scholarship For OBC, EBC, and DNT Students, Sikkim',
 'Oasis Post Matric Scholarships for OBC Students 2026-27',
 'NSP Centrally Sponsored Post-Matric Scholarship to SC Students, Sikkim',
 'NSP Pre-Matric Scholarship For ST Students (Class 9 & 10), Manipur 2026',
 'NSP ICAR Junior Research Fellowship (PGS) 2026']
p['runs'] = 5
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 5 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 21 | pm-yasasvi-post-matric-obc-sikkim-2026-27 | PM Yasasvi Post-Matric OBC/EBC/DNT, Sikkim | 31 Oct 2026 | Yes — B4S/CollegeDunia |
| 22 | oasis-post-matric-obc-west-bengal-2026-27 | Oasis Post-Matric OBC, West Bengal | 31 Oct 2026 | Yes — Shiksha/B4S |
| 23 | nsp-post-matric-sc-sikkim-2026-27 | NSP Post-Matric SC, Sikkim | 31 Oct 2026 | Yes — B4S/SchemesInIndia |
| 24 | nsp-pre-matric-st-manipur-2026-27 | NSP Pre-Matric ST, Manipur | 30 Oct 2026 | Yes — B4S/EdexLive |
| 25 | icar-junior-research-fellowship-pgs-2026 | ICAR Junior Research Fellowship (PGS) | 31 Oct 2026 | Yes — Oliveboard/B4S |

**Completed: 25 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

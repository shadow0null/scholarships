#!/usr/bin/env python3
"""Batch 9: 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'nirankari-rajmata': dict(mono='SN', title='Nirankari Rajmata Scholarship Scheme 2026-27', href='nirankari-rajmata-scholarship-scheme-2026-27.html',
              dpill='45 days to go', award='Up to Rs 75,000/year', elig='90%+ in Class 12; professional courses; income < Rs 5L.',
              tags=[('Merit-cum-means','blue'),('Private','teal')]),
 'goa-sc': dict(mono='NSP', title='NSP Post-Matric Scholarship for SC, Goa 2026-27', href='nsp-post-matric-sc-goa-2026-27.html',
              dpill='45 days to go', award='Up to Rs 13,500 + maintenance', elig='SC; Goa domicile; Class 11+; income ≤ Rs 2.5 lakh.',
              tags=[('SC','blue'),('Goa','teal')]),
 'banishree': dict(mono='OD', title='Odisha Banishree Scholarship 2026', href='odisha-banishree-scholarship-2026.html',
              dpill='45 days to go', award='Rs 400–700/month', elig='Students with disabilities; Odisha domicile; UDID card.',
              tags=[('Disability','blue'),('Odisha','teal')]),
 'umbrella-megh': dict(mono='NSP', title='Umbrella Scheme Post-Matric Scholarship for ST Students, Meghalaya 2026-27', href='umbrella-scheme-post-matric-st-meghalaya-2026-27.html',
              dpill='45 days to go', award='Up to Rs 1,200/month', elig='ST; Meghalaya domicile; Class 11+; income < Rs 2.5 lakh.',
              tags=[('ST','blue'),('Meghalaya','teal')]),
 'nfsc': dict(mono='NSP', title='National Fellowship Scheme for SC Students (NFSC) 2026', href='national-fellowship-sc-students-nfsc-2026.html',
              dpill='65 days to go', award='Rs 37,000–42,000/month', elig='SC; M.Phil/Ph.D; NET-JRF/GATE qualified.',
              tags=[('SC','blue'),('PhD','teal')]),
}

ARTICLES = [
dict(
 slug='nirankari-rajmata-scholarship-scheme-2026-27',
 title='Nirankari Rajmata Scholarship Scheme 2026-27 | StudyDesk Scholarships',
 meta='Nirankari Rajmata Scholarship Scheme 2026-27: full tuition fee waiver up to Rs 75,000/year for 90%+ scorers in professional courses. Deadline 30 Nov 2026.',
 short='Nirankari Rajmata Scholarship', kicker='Merit-cum-means · Private Foundation',
 mono='SN', prov_short='Sant Nirankari Charitable Foundation', prov_long='Sant Nirankari Charitable Foundation, Delhi',
 h1='Nirankari Rajmata Scholarship Scheme 2026–27',
 sub='Full tuition fee waiver up to Rs 75,000 a year — for meritorious students in professional courses.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Up to Rs 75,000 / year<small>Tuition fee waiver</small>'),
              ('Who can apply','90%+ in Class 12<small>Professional/technical courses</small>'),
              ('Income limit','Rs 5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Nov 2026<small>Offline application</small>'),
              ('Girls','50% reserved<small>For female students</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Nirankari Rajmata Scholarship Scheme 2026–27</strong>, offered by the <strong>Sant Nirankari Charitable Foundation</strong> (introduced 2014–15), gives <strong>full tuition fee waivers of up to Rs 75,000 per year</strong> to meritorious students who need financial aid for <strong>professional and technical courses at UG and PG level</strong>. It is a merit-cum-means scheme, assessed by the Foundation's Education Committee.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Regular student</strong> of a <strong>Central/State government-recognised institution/university</strong>.</li>
        <li>Admission secured through a <strong>competitive written test</strong> (not management/convenor quota).</li>
        <li>Admission offer in an eligible discipline: <strong>Engineering, Medicine (Allopathic/Ayurvedic/Homeopathic), MBA/PGDM, Architecture, CA (after CPT), CFA (after Foundation), LLB, Journalism &amp; Mass Communication</strong>.</li>
        <li><strong>90% or above in Class 12.</strong></li>
        <li>Annual <strong>family income below Rs 5,00,000</strong>.</li>
        <li><strong>Not receiving any other scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee waiver up to Rs 75,000 per year</strong> (tuition fees only).</li>
        <li><strong>50% reserved for girl students</strong> (unused quota goes to eligible boys).</li>
        <li><strong>Renewal:</strong> minimum <strong>75% marks every year</strong>; final instalment after final-year marksheet + feedback form.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed application form with passport-size photo</li>
        <li>Income certificate (SDM/BDO/Tehsildar) or latest payslip + IT return of earning members</li>
        <li>Admission slip/letter from the institution</li><li>Marksheets from Class 10 onwards; Class 10 &amp; 12 certificates</li>
        <li>Certificate from institution: no other scholarship, not quota admission</li>
        <li>Bank passbook/cheque; proof of residence</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Download the application form</strong>From the Foundation's website or via the scholarship listing.</li>
        <li><strong>Fill and attach documents</strong>Self-attested copies as above.</li>
        <li><strong>Send by speed post / email</strong>Member Education, Sant Nirankari Charitable Foundation, 80-A, Avtar Marg, Sant Nirankari Colony, Delhi-110009 — before <strong>30 November 2026</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Offline only:</strong> this is a postal/email application — there is no online portal. Send early so it arrives before the deadline.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much do I get?","Up to Rs 75,000 per year as a tuition fee waiver — the exact amount depends on your fee and the committee's assessment."),
 ("I got 89% in Class 12. Can I apply?","No — 90% or above is required."),
 ("Is there a girls' quota?","Yes — 50% of the scholarship amount is reserved for girls."),
 ("How do I renew it?","Secure at least 75% marks every year."),
]),
 verify='Verified 16 Oct 2026 via The Hindu (27 Sep 2026: SNCF; competitive-test admission; eligible courses; 90%+; income < Rs 5L; up to Rs 75,000/yr; 30 Nov; offline to 80-A Avtar Marg Delhi), B4S listing (same + 50% girls quota + 75% renewal) and DT Next (offline application).',
 offlinks=[('Sant Nirankari Charitable Foundation (official)','https://www.nirankari.org/')],
 related_titles=['sakal-cds','pmss-railways','isi-stipend'],
),

dict(
 slug='nsp-post-matric-sc-goa-2026-27',
 title='NSP Post-Matric Scholarship for SC, Goa 2026-27 | StudyDesk Scholarships',
 meta='NSP Post-Matric Scholarship for SC, Goa 2026-27: academic allowance up to Rs 13,500 + maintenance. Eligibility, deadline 30 Nov 2026.',
 short='NSP Post-Matric SC, Goa', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='NSP Post-Matric Scholarship for SC, Goa 2026–27',
 sub='Annual academic allowance up to Rs 13,500 plus maintenance — for SC students of Goa.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Up to Rs 13,500 / year<small>+ Rs 230–1,200/month maintenance</small>'),
              ('Who can apply','SC students<small>Goa domicile; Class 11–PhD</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Nov 2026<small>Via NSP</small>'),
              ('Fees','Full reimbursement<small>Compulsory non-refundable fees</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Scheme of Post-Matric Scholarship for SC Students, Goa 2026–27</strong>, from the <strong>Ministry of Social Justice and Empowerment</strong>, supports <strong>Scheduled Caste students of Goa</strong> studying at the <strong>post-matriculation or post-secondary level</strong>. Selected students receive an <strong>academic allowance of up to Rs 13,500 per year</strong> plus maintenance. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domiciled in Goa</strong>.</li>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Pursuing a <strong>post-matriculation or post-secondary course</strong> in a recognised institution/college/university.</li>
        <li>Annual <strong>family income ≤ Rs 2,50,000</strong>.</li>
        <li>Not repeating the same stage of education in a different subject.</li>
        <li>Correspondence students eligible only for Central/State university courses.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Academic allowance up to Rs 13,500 per year.</strong></li>
        <li><strong>Monthly maintenance Rs 230–1,200</strong> by course group and hosteller/day-scholar status.</li>
        <li><strong>Compulsory non-refundable fees</strong> (including tuition as fixed by the state fee committee).</li>
        <li>Paid by <strong>DBT to the Aadhaar-linked bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Goa)</li><li>SC certificate</li><li>Income certificate</li>
        <li>Previous year's marksheet</li><li>Bank passbook (Aadhaar-linked)</li><li>Passport-size photograph</li>
        <li>Aadhaar details for OTR</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — complete OTR if fresh.</li>
        <li><strong>Select Goa + Post-Matric SC scheme</strong>Fill details; upload documents.</li>
        <li><strong>Submit before 30 November 2026</strong>Institute verification follows.</li>
      </ol>
      <div class="honest-note"><strong>Two scholarships?</strong> If awarded two simultaneously, choose one and communicate your choice through your institution's head.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh per year of family income from all sources."),
 ("Which classes are covered?","Class 11 through PhD, including ITI, diploma, UG, PG, technical and professional courses."),
 ("Is OTR compulsory?","Yes — fresh applicants must complete One Time Registration on NSP."),
 ("Is there an application fee?","No — applying on NSP is completely free."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Goa listing (30 Nov 2026; up to Rs 13,500; SC; Goa domicile; income ≤ Rs 2.5L) cross-checked with SchemesInIndia and AssamJobApply (maintenance table Rs 230–1,200; OTR requirement).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['sikkim-sc','megh-sc','prematric-st-goa'],
),

dict(
 slug='odisha-banishree-scholarship-2026',
 title='Odisha Banishree Scholarship 2026 | StudyDesk Scholarships',
 meta='Odisha Banishree Scholarship 2026: Rs 400–700/month for students with disabilities. UDID, eligibility, deadline 30 Nov 2026.',
 short='Banishree Scholarship, Odisha', kicker='Odisha · Disability',
 mono='OD', prov_short='Govt. of Odisha (SSEPD)', prov_long='Dept. of Social Security & Empowerment of Persons with Disabilities, Odisha',
 h1='Odisha Banishree Scholarship 2026',
 sub='Rs 400 to Rs 700 a month — Odisha’s revamped scholarship for students with disabilities.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Rs 400 – 700 / month<small>By education level</small>'),
              ('Who can apply','Students with disabilities<small>40%+; UDID card; Odisha domicile</small>'),
              ('Extra','Reader’s + transport allowance<small>For eligible needs</small>'),
              ('Deadline','30 Nov 2026<small>State scholarship portal</small>'),
              ('Stackable','Yes<small>Can combine with other scholarships</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Banishree Scholarship 2026</strong>, run by Odisha's <strong>Department of Social Security and Empowerment of Persons with Disabilities (SSEPD)</strong>, supports students with disabilities from <strong>Class 1 to postgraduate and technical/vocational courses</strong>. The revamped scheme covers all <strong>21 disability categories</strong> under the RPwD Act 2016 and runs on the <strong>State Common Scholarship Application portal</strong> — and unlike most schemes, it can be <strong>availed over and above other scholarships</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Bonafide resident of Odisha.</strong></li>
        <li><strong>Benchmark disability of 40% or more</strong> with a valid <strong>UDID card</strong>.</li>
        <li>Regular student of a <strong>recognised institution</strong> (special schools and recognised distance education also eligible).</li>
        <li><strong>At least one parent must not be an income-tax payee</strong> (neither parent an income taxpayer per the listing).</li>
        <li>Maintain <strong>75% attendance</strong> to continue.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th>Level</th><th>Per month</th></tr>
      <tr><td>Primary (Class 1–5)</td><td>Rs 400</td></tr>
      <tr><td>Middle &amp; high school (Class 6–12)</td><td>Rs 500–600</td></tr>
      <tr><td>UG / PG / technical &amp; vocational</td><td>Rs 600–700</td></tr></table>
      <ul>
        <li><strong>Reader's allowance</strong> (visually impaired): Rs 200–400/month by level.</li>
        <li><strong>Transport allowance:</strong> Rs 200/month for 75%+ locomotor disability needing special transport.</li>
        <li><strong>Stackable:</strong> can be taken with other state/central scholarships.</li>
        <li>Paid by <strong>DBT</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>UDID card / disability certificate</li><li>Domicile proof (Odisha)</li><li>Income proof</li>
        <li>Previous class marksheet</li><li>Bank details (joint account with parent if below 18)</li>
        <li>Aadhaar + mobile number</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Odisha State Scholarship Portal</strong>Select the Banishree scheme.</li>
        <li><strong>Register with Aadhaar + mobile</strong></li>
        <li><strong>Fill details and upload documents</strong></li>
        <li><strong>Submit before 30 November 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What disability percentage is needed?","Benchmark disability of 40% or more with a valid UDID card."),
 ("Can I take it with another scholarship?","Yes — Banishree can be availed over and above other scholarships you are eligible for."),
 ("Is there extra help for visually impaired students?","Yes — a reader's allowance of Rs 200–400 per month by level."),
 ("Where do I apply?","On the Odisha State Scholarship Portal (Common Application portal)."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026 listing (30 Nov 2026; Rs 400–700/month by level; UDID; Odisha domicile; parents not income taxpayers; stackable) and Times of India (revamped scheme: 21 disability categories; 40%+ benchmark; 75% attendance; reader/transport allowances; common portal).',
 offlinks=[('Odisha State Scholarship Portal','https://scholarship.odisha.gov.in/')],
 related_titles=['nirman','pathani','nirankari-rajmata'],
),

dict(
 slug='umbrella-scheme-post-matric-st-meghalaya-2026-27',
 title='Umbrella Scheme Post-Matric Scholarship for ST Students, Meghalaya 2026-27 | StudyDesk',
 meta='Umbrella Scheme Post-Matric Scholarship for ST Students, Meghalaya 2026-27: maintenance up to Rs 1,200/month + fees. Deadline 30 Nov 2026.',
 short='Umbrella Post-Matric ST, Meghalaya', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via NSP)',
 h1='Umbrella Scheme Post-Matric Scholarship for ST Students, Meghalaya 2026–27',
 sub='Monthly maintenance up to Rs 1,200 plus fee reimbursement — for ST students of Meghalaya from Class 11 up.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Up to Rs 1,200 / month<small>+ fees, study tour, thesis grants</small>'),
              ('Who can apply','ST students<small>Meghalaya domicile; Class 11–PG</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Nov 2026<small>Via NSP</small>'),
              ('Verify by','21 Dec 2026<small>Institute verification</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Umbrella Scheme for Education of ST Children — Post-Matric Scholarship for ST Students, Meghalaya 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, supports <strong>Scheduled Tribe students of Meghalaya from Class 11 to post-graduation</strong> in recognised institutions. Applications opened <strong>3 July 2026</strong> and run only on the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of India</strong> and <strong>permanent resident (domicile) of Meghalaya</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> category.</li>
        <li>Passed <strong>Class 10/12 or higher secondary</strong>; studying in <strong>Class 11 or above</strong> (up to PG).</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
        <li>Institution's <strong>Institute Nodal Officer registered on NSP 2.0</strong>.</li>
        <li><strong>Aadhaar-linked bank account.</strong></li>
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
        <li>Domicile certificate (Meghalaya)</li><li>ST certificate</li><li>Income certificate</li>
        <li>Previous exam marksheet</li><li>Aadhaar-linked bank details</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Meghalaya + Umbrella Post-Matric ST scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>30 November 2026</strong>.</li>
        <li><strong>Institute verifies by 21 December 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Below Rs 2,50,000 per year of family income from all sources."),
 ("Which classes are covered?","Class 11 through post-graduation."),
 ("When did applications open?","3 July 2026; they close 30 November 2026."),
 ("Does my college need to do anything?","Yes — its Institute Nodal Officer must be registered on NSP 2.0, and verification closes 21 December 2026."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Meghalaya listing (30 Nov 2026; up to Rs 1,200/month; ST; Meghalaya domicile; income < Rs 2.5L; Aadhaar-linked account) and MeghalayaPortal/MeghalayaJobPortal (opened 3 Jul 2026; closes 30 Nov 2026; institute verification by 21 Dec 2026).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['umbrella-tripura','megh-sc','manipur-st'],
),

dict(
 slug='national-fellowship-sc-students-nfsc-2026',
 title='National Fellowship Scheme for SC Students (NFSC) 2026 | StudyDesk Scholarships',
 meta='NFSC 2026: Rs 37,000–42,000/month for SC students pursuing M.Phil/Ph.D. 2,000 fellowships. Eligibility, deadline 20 Dec 2026.',
 short='NFSC 2026', kicker='Central Government · PhD · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment / UGC',
 h1='National Fellowship Scheme for Scheduled Caste Students (NFSC) 2026',
 sub='Rs 37,000 to Rs 42,000 a month — 2,000 fellowships for SC research scholars.',
 dpill='65 days to go', dl_long='20 Dec 2026',
 facts=facts([('Award','Rs 37,000 – 42,000 / month<small>JRF → SRF + HRA + contingency</small>'),
              ('Who can apply','SC research scholars<small>M.Phil/Ph.D; NET-JRF/GATE</small>'),
              ('Fellowships','2,000 per year<small>1,500 Humanities + 500 Science</small>'),
              ('Deadline','20 Dec 2026<small>Via merit selection</small>'),
              ('Tenure','Up to 5 years<small>Performance-based continuation</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>National Fellowship Scheme for Scheduled Caste Students (NFSC) 2026</strong>, from the <strong>Ministry of Social Justice and Empowerment</strong>, gives fellowships to <strong>SC students pursuing full-time M.Phil. or Ph.D.</strong> in Science, Humanities or Social Sciences at <strong>UGC-recognised universities/institutions</strong>. <strong>2,000 new fellowships</strong> are awarded every year — 1,500 for Humanities/Social Sciences and 500 for Science — over and above the normal UGC reservation intake.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Enrolled in a <strong>regular, full-time M.Phil./Ph.D.</strong> at a UGC-recognised university/research institution.</li>
        <li>Qualified in <strong>UGC-NET-JRF / UGC-CSIR NET-JRF</strong> (or GATE, per the listing).</li>
        <li>Already-admitted NET-qualified candidates get <strong>priority</strong>; must join within 3 months of the JRF award letter.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>JRF: Rs 37,000/month</strong> (first 2 years) → <strong>SRF: Rs 42,000/month</strong>.</li>
        <li><strong>HRA</strong> as per university norms; <strong>contingency</strong> Rs 10,000–25,000/year by stream.</li>
        <li><strong>Tenure up to 5 years</strong>, continued on satisfactory performance.</li>
        <li>Paid by <strong>DBT</strong> after university verification.</li>
      </ul>
      <div class="honest-note"><strong>Amount note:</strong> older explainers quote Rs 31,000/35,000 — the current UGC-aligned rates (Mizoram University's official fellowship table) are <strong>Rs 37,000 JRF / Rs 42,000 SRF</strong>. The scheme is under periodic revision by the Ministry.</div>
      <h2 id="documents">Documents required</h2>
      <p>As per the UGC/ministry notification — including SC certificate, NET-JRF/GATE scorecard, PG degree, enrolment proof.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Qualify UGC-NET-JRF / CSIR-NET-JRF</strong>Selection is merit-based on the NET roll-number merit list.</li>
        <li><strong>Watch the ministry/UGC notification</strong>Applications close <strong>20 December 2026</strong>.</li>
        <li><strong>University verifies enrolment</strong>Half-yearly progress reports continue the fellowship.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How many fellowships are there?","2,000 per year — 1,500 in Humanities/Social Sciences, 500 in Science."),
 ("Do I need NET?","Yes — selection is via the UGC-NET-JRF / CSIR-NET-JRF merit list (GATE also listed)."),
 ("What is the monthly amount?","Rs 37,000 as JRF, rising to Rs 42,000 as SRF, plus HRA and contingency."),
 ("How long does it last?","Up to 5 years, continued yearly on satisfactory performance."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026 listing (20 Dec 2026; up to Rs 42,000; 2,000 fellowships; NET-JRF/GATE; full-time M.Phil/Ph.D) and Mizoram University official fellowship table (JRF 37,000 / SRF 42,000 + contingency + 9% HRA).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['icar-jrf','topclass-sc','isi-stipend'],
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
p['done'] += ['Nirankari Rajmata Scholarship Scheme 2026-27',
 'NSP Post-Matric Scholarship for SC, Goa 2026-27',
 'Odisha Banishree Scholarship 2026',
 'Umbrella Scheme Post-Matric Scholarship for ST Students, Meghalaya 2026-27',
 'National Fellowship Scheme for Scheduled Caste Students (NFSC) 2026']
p['runs'] = 9
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 9 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 41 | nirankari-rajmata-scholarship-scheme-2026-27 | Nirankari Rajmata Scholarship | 30 Nov 2026 | Yes — The Hindu/B4S |
| 42 | nsp-post-matric-sc-goa-2026-27 | NSP Post-Matric SC, Goa | 30 Nov 2026 | Yes — B4S/SchemesInIndia |
| 43 | odisha-banishree-scholarship-2026 | Odisha Banishree Scholarship | 30 Nov 2026 | Yes — B4S/TOI |
| 44 | umbrella-scheme-post-matric-st-meghalaya-2026-27 | Umbrella Post-Matric ST, Meghalaya | 30 Nov 2026 | Yes — B4S/MeghalayaPortal |
| 45 | national-fellowship-sc-students-nfsc-2026 | NFSC 2026 | 20 Dec 2026 | Yes — B4S/MZU official |

**Completed: 45 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

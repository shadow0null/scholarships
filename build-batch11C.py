#!/usr/bin/env python3
"""Batch 11C (Group C): 10 verified articles. Verified 16 Oct 2026.
Writes ONLY article HTML files. Registry/progress/tracker merge is done by parent.
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'nsp-clean-tripura': dict(mono='NSP', title='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2025-26', href='nsp-pre-matric-sc-cleaning-health-hazard-tripura-2025-26.html',
              dpill='86 days to go', award='Up to Rs 700/month', elig='SC; Tripura; Class 1–10; child of manual scavenger / waste picker.',
              tags=[('SC','blue'),('Tripura','teal')]),
 'nsp-prematric-tripura': dict(mono='NSP', title='Pre-Matric SC Scholarship Class 9 and 10, Tripura 2025', href='nsp-pre-matric-sc-tripura-2025-26.html',
              dpill='86 days to go', award='Up to Rs 525/month', elig='SC; Tripura domicile; Class 9–10.',
              tags=[('SC','blue'),('Tripura','teal')]),
 'dundee-ge': dict(mono='UD', title='University of Dundee Global Excellence Scholarship 2027', href='dundee-global-excellence-scholarship-2027.html',
              dpill='105 days to go', award='£8,000 tuition discount', elig='International; UK 1st-class degree; Jan 2027 taught Master\u2019s.',
              tags=[('Master\u2019s','blue'),('UK','teal')]),
 'ka-dme-nursing': dict(mono='KA', title='DME Scholarships and Incentives for Medical Students, Karnataka 2026-27', href='karnataka-ssp-dme-nursing-scholarship-2026-27.html',
              dpill='107 days to go', award='Financial assistance', elig='Diploma in Nursing; DME-specified college; promoted.',
              tags=[('Nursing','blue'),('Karnataka','teal')]),
 'ka-prathibha': dict(mono='KA', title='DTE Prathibha Puraskara (Free Fee) Scheme, Karnataka 2026-27', href='karnataka-ssp-dte-prathibha-puraskara-2026-27.html',
              dpill='107 days to go', award='Fee support', elig='BE/B.Tech/B.Arch; KEA admission; 80%+ in PUC (Govt/Aided).',
              tags=[('Engineering','blue'),('Karnataka','teal')]),
 'ka-dme-st': dict(mono='KA', title='Karnataka SSP DME Post-Matric Scholarship for ST Students 2026-27', href='karnataka-ssp-dme-post-matric-st-2026-27.html',
              dpill='107 days to go', award='Financial assistance', elig='ST; MBBS/BDS/MDS/MD/MS; income Rs 2.5–10L.',
              tags=[('ST','blue'),('Karnataka','teal')]),
 'ka-dmw': dict(mono='KA', title='Karnataka SSP DMW Fee Reimbursement Scheme for Minorities 2026–27', href='karnataka-ssp-dmw-minority-fee-reimbursement-2026-27.html',
              dpill='107 days to go', award='Fee reimbursement', elig='Minority; income \u2264 Rs 2.5L (MCM) / 2L (post-matric).',
              tags=[('Minority','blue'),('Karnataka','teal')]),
 'ka-dte-spl': dict(mono='KA', title='Karnataka SSP DTE Scholarship for Special Category Students 2026-27', href='karnataka-ssp-dte-special-category-2026-27.html',
              dpill='107 days to go', award='Financial assistance', elig='Any caste; Diploma/BE/B.Tech/B.Arch; promoted.',
              tags=[('Engineering','blue'),('Karnataka','teal')]),
 'ka-hosteller': dict(mono='KA', title='Karnataka SSP Hosteller Maintenance Scheme (SWD), 2026-27', href='karnataka-ssp-hosteller-maintenance-swd-2026-27.html',
              dpill='107 days to go', award='Maintenance support', elig='SC; income \u2264 Rs 2.5L; technical/medical; hosteller.',
              tags=[('SC','blue'),('Karnataka','teal')]),
 'ka-vidyasiri': dict(mono='KA', title='Karnataka SSP Vidyasiri Scheme for Minorities 2026–27', href='karnataka-ssp-vidyasiri-minorities-2026-27.html',
              dpill='107 days to go', award='Financial assistance', elig='Minority; income \u2264 Rs 2.5L; no minority-hostel seat allotted.',
              tags=[('Minority','blue'),('Karnataka','teal')]),
}

SSP = 'https://ssp.postmatric.karnataka.gov.in/'

ARTICLES = [
dict(
 slug='nsp-pre-matric-sc-cleaning-health-hazard-tripura-2025-26',
 title='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2025-26 | StudyDesk Scholarships',
 meta='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2025-26: up to Rs 700/month for SC students of Tripura whose parents do hazardous cleaning work. Deadline 10 Jan 2027.',
 short='Cleaning & Health Hazard Scholarship, Tripura', kicker='Tripura · SC · Class 1–10',
 mono='NSP', prov_short='Ministry of Social Justice and Empowerment', prov_long='Ministry of Social Justice and Empowerment, Government of India',
 h1='Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2025–26',
 sub='Up to Rs 700 a month — for SC schoolchildren of Tripura whose parents work in manual scavenging, flaying, waste picking or other hazardous occupations.',
 dpill='86 days to go', dl_long='10 Jan 2027',
 facts=facts([('Award','Up to Rs 700 / month<small>Hostellers, Class 3–10; 10 months</small>'),
              ('Day scholars','Rs 225 / month<small>Class 1–10; 10 months</small>'),
              ('Ad-hoc grant','Rs 750–1,000 / year<small>Day scholar / hosteller</small>'),
              ('Who can apply','SC students<small>Tripura domicile; Class 1–10</small>'),
              ('Deadline','10 Jan 2027<small>Apply on NSP</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pre-Matric SC Cleaning and Health Hazard Scholarship, Tripura 2025–26</strong> is a centrally sponsored scheme of the <strong>Ministry of Social Justice and Empowerment</strong> for Scheduled Caste students of Tripura in <strong>Class 1 to 10</strong> whose parent or guardian works in <strong>manual scavenging, flaying, waste picking or another hazardous health occupation</strong> as defined under the Manual Scavengers Act, 2013. Applications are made on the <strong>National Scholarship Portal (NSP)</strong> and close <strong>10 January 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Caste</strong> community.</li>
        <li><strong>Domiciled in Tripura</strong> and an Indian national.</li>
        <li>Enrolled in <strong>Class 1 to 10</strong> in a recognised institution.</li>
        <li>Be the <strong>child or ward of a person engaged in manual scavenging, flaying, waste picking or a hazardous health occupation</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Hostellers (Class 3–10):</strong> Rs 700 per month for 10 months.</li>
        <li><strong>Day scholars (Class 1–10):</strong> Rs 225 per month for 10 months.</li>
        <li><strong>Ad-hoc grant:</strong> Rs 750 per annum (day scholars) / Rs 1,000 per annum (hostellers).</li>
        <li>Paid through <strong>Direct Benefit Transfer</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar card</li><li>Caste certificate (SC)</li><li>Domicile certificate of Tripura</li>
        <li>Proof of parent's occupation (hazardous cleaning work)</li><li>Previous year marksheet</li>
        <li>Bonafide certificate from the school</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on NSP</strong>Visit scholarships.gov.in and complete One-Time Registration.</li>
        <li><strong>Select the scheme</strong>Choose the Pre-Matric SC Cleaning and Health Hazard Scholarship for Tripura.</li>
        <li><strong>Upload documents</strong>Attach caste, domicile, occupation proof and school records.</li>
        <li><strong>Submit before 10 January 2027</strong>Track verification status on the NSP dashboard.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who exactly counts as a hazardous-occupation worker?","A parent or guardian engaged in manual scavenging, flaying, waste picking or a hazardous health occupation as defined in Section 2(I) of the Manual Scavengers Act, 2013."),
 ("Which classes are covered?","Class 1 to 10 for day scholars; the hosteller rate applies from Class 3 to 10."),
 ("How much is the ad-hoc grant?","Rs 750 per year for day scholars and Rs 1,000 per year for hostellers."),
 ("Where do I apply?","On the National Scholarship Portal (scholarships.gov.in) before 10 January 2027."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Tripura listing (10 Jan 2027; Rs 700/month hosteller, Rs 225/month day scholar; Rs 750/1,000 ad-hoc grant; SC; Tripura domicile; Class 1–10; Manual Scavengers Act 2013 occupations; NSP).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['nsp-prematric-tripura','prematric-sc-sikkim','umbrella-tripura'],
),

dict(
 slug='nsp-pre-matric-sc-tripura-2025-26',
 title='Pre-Matric SC Scholarship Class 9 and 10, Tripura 2025 | StudyDesk Scholarships',
 meta='Pre-Matric SC Scholarship Class 9 and 10, Tripura 2025: up to Rs 525/month for SC students of Tripura in Class 9–10. Deadline 10 Jan 2027.',
 short='Pre-Matric SC Scholarship, Tripura', kicker='Tripura · SC · Class 9–10',
 mono='NSP', prov_short='Ministry of Social Justice and Empowerment', prov_long='Ministry of Social Justice and Empowerment, Government of India',
 h1='Pre-Matric SC Scholarship Class 9 and 10, Tripura 2025',
 sub='Up to Rs 525 a month — pre-matric support for Scheduled Caste students of Tripura in Class 9 and 10.',
 dpill='86 days to go', dl_long='10 Jan 2027',
 facts=facts([('Award','Up to Rs 525 / month<small>For 10 months, plus other grants</small>'),
              ('Who can apply','SC students<small>Tripura; Class 9–10</small>'),
              ('Mode','Online only<small>National Scholarship Portal</small>'),
              ('Deadline','10 Jan 2027<small>NSP application</small>'),
              ('Payment','DBT<small>Direct to bank account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pre-Matric SC Scholarship for Class 9 and 10, Tripura 2025</strong> is a centrally sponsored scheme of the <strong>Ministry of Social Justice and Empowerment</strong> that supports <strong>Scheduled Caste students of Tripura studying in Class 9 and 10</strong>. Selected students receive up to <strong>Rs 525 per month for 10 months</strong> along with other grants. Applications run on the <strong>National Scholarship Portal (NSP)</strong> and close <strong>10 January 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Caste</strong> community.</li>
        <li><strong>Domiciled in Tripura</strong>.</li>
        <li>Studying in <strong>Class 9 or 10</strong> in a recognised school.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly scholarship:</strong> up to Rs 525 per month for 10 months.</li>
        <li><strong>Other grants</strong> as per the scheme guidelines.</li>
        <li>Paid through <strong>Direct Benefit Transfer</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar card</li><li>Caste certificate (SC)</li><li>Domicile certificate of Tripura</li>
        <li>Previous year marksheet</li><li>Bonafide certificate</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on NSP</strong>Visit scholarships.gov.in and complete One-Time Registration.</li>
        <li><strong>Choose the scheme</strong>Select the Pre-Matric SC Scholarship for Tripura (Class 9–10).</li>
        <li><strong>Fill and submit</strong>Upload documents and submit before 10 January 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who can apply?","Scheduled Caste students domiciled in Tripura who are studying in Class 9 or 10."),
 ("What is the award amount?","Up to Rs 525 per month for 10 months, plus other grants under the scheme."),
 ("What is the deadline?","10 January 2027 for the current cycle."),
 ("Where do I apply?","On the National Scholarship Portal (scholarships.gov.in)."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Tripura listing (10 Jan 2027; up to Rs 525/month for 10 months; SC; Tripura; Class 9–10; NSP).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['nsp-clean-tripura','prematric-sc-sikkim','prematric-st-goa'],
),

dict(
 slug='dundee-global-excellence-scholarship-2027',
 title='University of Dundee Global Excellence Scholarship 2027 (UK) | StudyDesk Scholarships',
 meta='University of Dundee Global Excellence Scholarship 2027: £8,000 tuition discount for international taught Master\u2019s students starting January 2027. Deadline 29 Jan 2027.',
 short='Dundee Global Excellence Scholarship', kicker='UK · Master\u2019s · International',
 mono='UD', prov_short='University of Dundee', prov_long='University of Dundee, Scotland, United Kingdom',
 h1='University of Dundee Global Excellence Scholarship 2027',
 sub='£8,000 off tuition — for outstanding international students starting a taught Master\u2019s at Dundee in January 2027.',
 dpill='105 days to go', dl_long='29 Jan 2027',
 facts=facts([('Award','£8,000 tuition discount<small>Fee reduction, not cash</small>'),
              ('Who can apply','International Master\u2019s<small>UK 1st-class degree or equivalent</small>'),
              ('Start','11 Jan 2027<small>Full-time, on-campus</small>'),
              ('Deadline','29 Jan 2027<small>23:59 UK time</small>'),
              ('Application','Automatic<small>No separate form</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Dundee Global Excellence Scholarship</strong> rewards outstanding international students beginning a <strong>full-time, on-campus taught Master\u2019s programme in January 2027</strong> with an <strong>£8,000 reduction in tuition fees</strong>. It is a <strong>partial award — a fee discount, not a fully funded scholarship</strong>: it does not cover living costs, travel, visa fees or the Immigration Health Surcharge. There is <strong>no separate application</strong>; the admissions team assesses every eligible course applicant automatically.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold an offer for a <strong>full-time, on-campus taught Master\u2019s programme</strong> starting January 2027, in any academic school.</li>
        <li>Programme tuition fee of <strong>£22,250 or above</strong>.</li>
        <li>Hold a <strong>UK first-class honours degree or a Dundee-approved equivalent</strong>.</li>
        <li>Be classified as an <strong>international fee-paying student</strong>, as confirmed in the offer letter.</li>
        <li>Awards are not made on <strong>predicted grades</strong> — final qualifications must be submitted.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>£8,000 tuition-fee discount</strong> for the postgraduate taught programme.</li>
        <li>Applied in <strong>every year of study</strong> where the programme exceeds 12 months and a full eligible fee is charged each year.</li>
        <li><strong>No separate form</strong> — considered automatically with the course application.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>University admission application with supporting documents</li><li>Final degree certificate and transcripts</li>
        <li>English-language evidence (per course requirement)</li><li>Passport / fee-status documents</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose an eligible Master\u2019s programme</strong>Check the course page for the £22,250 fee threshold and January 2027 start.</li>
        <li><strong>Apply for admission</strong>Submit the university application with all supporting documents.</li>
        <li><strong>Meet the conditions</strong>Secure the offer, meet academic and English conditions, and upload final qualifications.</li>
        <li><strong>Automatic assessment</strong>The admissions team reviews eligible applicants — no scholarship form needed. Deadline: 29 January 2027, 23:59 UK time.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this a fully funded scholarship?","No — it is an £8,000 tuition-fee discount. Living costs, travel, visa and health surcharge are not covered."),
 ("Do I need a separate application?","No. You are assessed automatically from your course application once final qualifications are submitted."),
 ("What grades do I need?","A UK first-class honours degree or an equivalent approved by Dundee; predicted grades alone are not enough."),
 ("Which programmes qualify?","Full-time, on-campus taught Master\u2019s programmes starting January 2027 with fees of £22,250 or more."),
]),
 verify='Verified 16 Oct 2026 via University of Dundee key-facts page (£8,000 PG / £7,500 UG tuition discount; UK 1st-class; fee ≥ £22,250; international status; auto-assessment) and DAADScholarships, AfterSchoolAfrica and Mastersportal listings (Jan 2027 intake; deadline 29 Jan 2027, 23:59 UK time; start 11 Jan 2027).',
 offlinks=[('University of Dundee — scholarships','https://www.dundee.ac.uk/scholarships/')],
 related_titles=['griffith-vc','hanns-seidel','swiss-phd'],
),

dict(
 slug='karnataka-ssp-dme-nursing-scholarship-2026-27',
 title='DME Scholarships and Incentives for Medical Students, Karnataka 2026-27 | StudyDesk Scholarships',
 meta='DME Scholarships and Incentives for Medical Students, Karnataka 2026-27: financial assistance for Diploma in Nursing students. Apply on the SSP portal — confirm the 2026-27 deadline on the official notice board.',
 short='DME Nursing Scholarship, Karnataka', kicker='Karnataka · Nursing · SSP',
 mono='KA', prov_short='Dept. of Medical Education, Karnataka', prov_long='Department of Medical Education, Government of Karnataka',
 h1='DME Scholarships and Incentives for Medical Students, Karnataka 2026–27',
 sub='Financial assistance — for Diploma in Nursing students at colleges specified by Karnataka\u2019s Department of Medical Education.',
 dpill='To be announced', dl_long='To be announced',
 facts=facts([('Award','Financial assistance<small>Amount per department norms</small>'),
              ('Who can apply','Nursing diploma students<small>DME-specified colleges</small>'),
              ('Seat','Any seat category<small>Promoted to current year</small>'),
              ('Deadline','To be announced<small>Check SSP portal</small>'),
              ('Mode','Online<small>ssp.postmatric.karnataka.gov.in</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DME Scholarship and Incentive for Medical Students, Karnataka 2026–27</strong> is offered by the <strong>Department of Medical Education, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It supports students pursuing a <strong>Diploma in Nursing</strong> at colleges specified by the department. Selected students receive <strong>financial assistance</strong> (the exact amount is not published in the listing). The department has not announced the 2026-27 deadline — check the <strong>SSP portal</strong> notice board.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Pursuing a <strong>Diploma in Nursing</strong>.</li>
        <li>Enrolled in a <strong>college specified by the Department of Medical Education</strong>.</li>
        <li>Admitted under <strong>any college seat category</strong>.</li>
        <li><strong>Promoted to the present academic year</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Financial assistance</strong> for eligible nursing diploma students.</li>
        <li>Disbursed through the <strong>SSP portal</strong> per department norms.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Admission / fee receipt</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Log in and select the scheme</strong>Choose the DME Scholarship and Incentive for the post-matric 2026–27 cycle.</li>
        <li><strong>Submit before the announced deadline</strong>Fill details, upload documents and track verification on the portal.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Which course is covered?","The Diploma in Nursing at colleges specified by the Department of Medical Education."),
 ("Is there an income limit published?","The listing does not publish an income or caste criterion — check the SSP portal for the current cycle\u2019s conditions."),
 ("Where do I apply?","On the Karnataka State Scholarship Portal (ssp.postmatric.karnataka.gov.in) — the department deadline is to be announced; confirm on the portal."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka listing (31 Jan 2027 shown on Buddy4Study; corrected 16 Oct 2026 — department deadline not confirmed on SSP portal, TBA; Diploma in Nursing; DME-specified college; any seat; promoted; financial assistance; SSP portal) and Entri SSP overview (SSP portal process; department-wise awards).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-dme-st','ka-hosteller','ka-dte-spl'],
),

dict(
 slug='karnataka-ssp-dte-prathibha-puraskara-2026-27',
 title='DTE Prathibha Puraskara (Free Fee) Scheme, Karnataka 2026-27 | StudyDesk Scholarships',
 meta='DTE Prathibha Puraskara (Free Fee) Scheme, Karnataka 2026-27: fee support for BE/B.Tech/B.Arch students admitted via KEA. Apply on the SSP portal — confirm the 2026-27 deadline on the official notice board.',
 short='Prathibha Puraskara Scheme, Karnataka', kicker='Karnataka · Engineering · SSP',
 mono='KA', prov_short='Dept. of Technical Education, Karnataka', prov_long='Department of Technical Education, Government of Karnataka',
 h1='DTE Prathibha Puraskara (Free Fee) Scheme, Karnataka 2026–27',
 sub='Fee support — for meritorious BE, B.Tech and B.Arch students admitted through KEA in Karnataka.',
 dpill='To be announced', dl_long='To be announced',
 facts=facts([('Award','Fee support<small>Free-fee / reimbursement structure</small>'),
              ('Who can apply','BE / B.Tech / B.Arch<small>KEA admission; any caste</small>'),
              ('Merit bar','80%+ in PUC<small>From Govt/Aided college</small>'),
              ('Deadline','To be announced<small>Check SSP portal</small>'),
              ('Promotion','Required<small>Promoted to present year</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Prathibha Puraskara (Free Fee) Scheme 2026–27</strong> is run by the <strong>Department of Technical Education (DTE), Government of Karnataka</strong> and disbursed through the <strong>State Scholarship Portal (SSP)</strong>. It rewards <strong>meritorious students pursuing B.E., B.Tech or B.Arch</strong> with fee support. The department has not announced the 2026–27 application deadline — check the <strong>SSP portal</strong> notice board.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>any caste category</strong>.</li>
        <li>Pursuing <strong>B.E., B.Tech or B.Arch</strong>.</li>
        <li><strong>Admitted through KEA</strong> (Karnataka Examinations Authority).</li>
        <li><strong>Promoted to the present academic year</strong>.</li>
        <li>Completed <strong>PUC in a Government or Aided college with at least 80% marks</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Fee support</strong> under the free-fee / reimbursement structure for eligible technical students.</li>
        <li>Disbursed via the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet (PUC and current year)</li><li>Aadhaar card</li><li>KEA admission order / allotment letter</li>
        <li>Fee receipt</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the Prathibha Puraskara (Free Fee) Scheme for 2026–27.</li>
        <li><strong>Submit before the announced deadline</strong>Upload the KEA allotment and marksheets, then track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a caste restriction?","No — the scheme is open to students of any caste category."),
 ("What is the merit requirement?","At least 80% in PUC completed from a Government or Aided college."),
 ("Must admission be through KEA?","Yes — admission through the Karnataka Examinations Authority is required."),
 ("What is the deadline?","To be announced — the department has not confirmed the 2026-27 deadline; check the SSP portal notice board."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (31 Jan 2027 shown on Buddy4Study; corrected 16 Oct 2026 — department deadline not confirmed on SSP portal, TBA; BE/B.Tech/B.Arch; KEA admission; promoted) and scholarships.net.in SSP listing (DTE; any caste; 80%+ in PUC from Govt/Aided college; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-dte-spl','ka-dme-nursing','ka-dme-st'],
),

dict(
 slug='karnataka-ssp-dme-post-matric-st-2026-27',
 title='Karnataka SSP DME Post-Matric Scholarship for ST Students 2026-27 | StudyDesk Scholarships',
 meta='Karnataka SSP DME Post-Matric Scholarship for ST Students 2026-27: financial assistance for ST students in MBBS/BDS/MD/MS. Apply on the SSP portal — confirm the 2026-27 deadline on the official notice board.',
 short='DME Post-Matric Scholarship for ST, Karnataka', kicker='Karnataka · ST · Medical',
 mono='KA', prov_short='Dept. of Medical Education, Karnataka', prov_long='Department of Medical Education, Government of Karnataka',
 h1='Karnataka SSP DME Post-Matric Scholarship for ST Students 2026–27',
 sub='Financial assistance — for Scheduled Tribe students pursuing MBBS, BDS, MDS, MD or MS in Karnataka.',
 dpill='To be announced', dl_long='To be announced',
 facts=facts([('Award','Financial assistance<small>Amount per department norms</small>'),
              ('Who can apply','ST students<small>MBBS / BDS / MDS / MD / MS</small>'),
              ('Income','Rs 2.5L – Rs 10L<small>Annual family income</small>'),
              ('Seat','Any except management quota<small>Promoted to current year</small>'),
              ('Deadline','To be announced<small>Check SSP portal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Karnataka SSP DME Post-Matric Scholarship for ST Students 2026–27</strong> is offered by the <strong>Department of Medical Education, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It supports <strong>Scheduled Tribe students pursuing medical education</strong> — MBBS, BDS, MDS, MD and MS — with financial assistance. The department has not announced the 2026-27 deadline — check the <strong>SSP portal</strong> notice board.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> category.</li>
        <li>Annual family income between <strong>Rs 2.5 lakh and Rs 10 lakh</strong>.</li>
        <li>Pursuing <strong>MBBS, BDS, MDS, MD or MS</strong>.</li>
        <li>Studying at <strong>any college</strong>, admitted under <strong>any seat category except the management quota</strong>.</li>
        <li><strong>Promoted to the current academic year</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Financial assistance</strong> for eligible ST medical students (amount per department norms).</li>
        <li>Disbursed through the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Caste certificate (ST)</li>
        <li>Parent\u2019s salary / income certificate</li><li>Non-practising certificate (for PG students, if applicable)</li>
        <li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the DME Post-Matric Scholarship for ST Students, 2026–27.</li>
        <li><strong>Submit before the announced deadline</strong>Upload income and caste proofs and track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Which courses are covered?","MBBS, BDS, MDS, MD and MS."),
 ("What is the income range?","Annual family income between Rs 2.5 lakh and Rs 10 lakh."),
 ("Are management-quota seats eligible?","No — admission under any seat category except the management quota."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka listing (31 Jan 2027 shown on Buddy4Study; corrected 16 Oct 2026 — department deadline not confirmed on SSP portal, TBA; ST; income Rs 2.5–10L; MBBS/BDS/MDS/MD/MS; any college except management quota; promoted; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-dme-nursing','ka-hosteller','ka-dte-spl'],
),

dict(
 slug='karnataka-ssp-dmw-minority-fee-reimbursement-2026-27',
 title='Karnataka SSP DMW Fee Reimbursement Scheme for Minorities 2026–27 | StudyDesk Scholarships',
 meta='Karnataka SSP DMW Fee Reimbursement Scheme for Minorities 2026–27: fee reimbursement for minority students. Income up to Rs 2.5L. Minorities track closed 30 Sep 2026.',
 short='DMW Fee Reimbursement for Minorities, Karnataka', kicker='Karnataka · Minority · SSP',
 mono='KA', prov_short='Directorate of Minorities, Karnataka', prov_long='Directorate of Minorities, Government of Karnataka',
 h1='Karnataka SSP DMW Fee Reimbursement Scheme for Minorities 2026–27',
 sub='Fee reimbursement — for minority-community students of Karnataka under the Directorate of Minorities.',
 dpill='Closed 30 Sep 2026', dl_long='30 Sep 2026 (closed)',
 facts=facts([('Award','Fee reimbursement<small>Amount per department norms</small>'),
              ('Who can apply','Minority students<small>Recognised minority community</small>'),
              ('Income','\u2264 Rs 2.5L (MCM)<small>\u2264 Rs 2L for post-matric</small>'),
              ('Exclusions','No KSOU / residential<small>Internships excluded</small>'),
              ('Deadline','Closed 30 Sep 2026<small>Minorities track</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DMW Fee Reimbursement Scheme for Minorities 2026–27</strong> is run by the <strong>Directorate of Minorities, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It reimburses fees for students of <strong>recognised minority communities</strong> enrolled in eligible courses. The minorities-track application window closed on <strong>30 September 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to a <strong>recognised minority community</strong>.</li>
        <li>Annual family income of <strong>Rs 2.5 lakh or less</strong> for MCM (Merit-cum-Means) courses, or <strong>Rs 2 lakh or less</strong> under the post-matric category.</li>
        <li>Enrolled in an <strong>eligible course</strong> (internship courses excluded).</li>
        <li>Studying at an <strong>eligible college or institution</strong> — Karnataka State Open University (KSOU) and residential colleges are excluded.</li>
        <li><strong>Promoted to the present academic year</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Fee reimbursement</strong> for eligible minority students (amount per department norms).</li>
        <li>Disbursed through the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Minority certificate</li>
        <li>Category certificate issued by the Tahsildar (current/valid)</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the DMW Fee Reimbursement Scheme for Minorities, 2026–27.</li>
        <li><strong>Minorities window closed 30 Sep 2026</strong>Upload minority and income proofs and track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh or less for MCM courses; Rs 2 lakh or less under the post-matric category."),
 ("Are KSOU students eligible?","No — Karnataka State Open University and residential colleges are excluded."),
 ("Which documents prove minority status?","A minority certificate plus a category certificate issued by the Tahsildar."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka listing (31 Jan 2027 shown on Buddy4Study listing; corrected 16 Oct 2026 — Minorities Welfare Dept closed 30 Sep 2026 per multiple trackers; recognised minority; income ≤ Rs 2.5L MCM / ≤ Rs 2L post-matric; eligible course excl. internships; excl. KSOU and residential colleges; promoted; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-vidyasiri','ka-hosteller','ka-dte-spl'],
),

dict(
 slug='karnataka-ssp-dte-special-category-2026-27',
 title='Karnataka SSP DTE Scholarship for Special Category Students 2026-27 | StudyDesk Scholarships',
 meta='Karnataka SSP DTE Scholarship for Special Category Students 2026-27: financial assistance for Diploma/BE/B.Tech/B.Arch students of any caste. Apply on the SSP portal — confirm the 2026-27 deadline on the official notice board.',
 short='DTE Special Category Scholarship, Karnataka', kicker='Karnataka · Technical · SSP',
 mono='KA', prov_short='Dept. of Technical Education, Karnataka', prov_long='Department of Technical Education, Government of Karnataka',
 h1='Karnataka SSP DTE Scholarship for Special Category Students 2026–27',
 sub='Financial assistance — for Diploma, BE, B.Tech and B.Arch students of any caste under Karnataka\u2019s technical education department.',
 dpill='To be announced', dl_long='To be announced',
 facts=facts([('Award','Financial assistance<small>Amount per department norms</small>'),
              ('Who can apply','Any caste category<small>Technical students</small>'),
              ('Courses','Diploma / BE / B.Tech / B.Arch<small>Any college and seat type</small>'),
              ('Promotion','Required<small>Promoted to present year</small>'),
              ('Deadline','To be announced<small>Check SSP portal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DTE Scholarship for Special Category Students 2026–27</strong> is offered by the <strong>Department of Technical Education, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It provides <strong>financial assistance to students of any caste category</strong> pursuing technical courses. The department has not announced the 2026-27 deadline — check the <strong>SSP portal</strong> notice board.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to <strong>any caste category</strong>.</li>
        <li>Pursuing <strong>Diploma in Polytechnic, B.E., B.Tech or B.Arch</strong>.</li>
        <li>Enrolled in <strong>any type of college</strong>.</li>
        <li>Admitted under <strong>any college seat category</strong>.</li>
        <li><strong>Promoted to the present academic year</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Financial assistance</strong> for eligible technical students (amount per department norms).</li>
        <li>Disbursed through the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Admission / fee receipt</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the DTE Scholarship for Special Category Students, 2026–27.</li>
        <li><strong>Submit before the announced deadline</strong>Fill details, upload documents and track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a caste restriction?","No — students of any caste category can apply."),
 ("Which courses are covered?","Diploma in Polytechnic, B.E., B.Tech and B.Arch."),
 ("Does the seat type matter?","No — any college type and any seat category are eligible, provided the student is promoted."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka listing (31 Jan 2027 shown on Buddy4Study; corrected 16 Oct 2026 — department deadline not confirmed on SSP portal, TBA; any caste; Diploma/BE/B.Tech/B.Arch; any college and seat type; promoted; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-prathibha','ka-dme-nursing','ka-dme-st'],
),

dict(
 slug='karnataka-ssp-hosteller-maintenance-swd-2026-27',
 title='Karnataka SSP Hosteller Maintenance Scheme (SWD), 2026-27 | StudyDesk Scholarships',
 meta='Karnataka SSP Hosteller Maintenance Scheme (SWD) 2026-27: maintenance support for SC hostellers in technical/medical courses. Income up to Rs 2.5L. Apply by 31 Jan 2027.',
 short='Hosteller Maintenance Scheme (SWD), Karnataka', kicker='Karnataka · SC · Hosteller',
 mono='KA', prov_short='Social Welfare Department, Karnataka', prov_long='Social Welfare Department, Government of Karnataka',
 h1='Karnataka SSP Hosteller Maintenance Scheme (SWD), 2026–27',
 sub='Maintenance support — for SC students staying in college hostels while pursuing technical or medical courses.',
 dpill='107 days to go', dl_long='31 Jan 2027',
 facts=facts([('Award','Maintenance support<small>Amount per department norms</small>'),
              ('Who can apply','SC hostellers<small>Technical / medical courses</small>'),
              ('Income','\u2264 Rs 2.5L<small>Annual family income</small>'),
              ('Hostel','College/university-run<small>Detained students ineligible</small>'),
              ('Deadline','31 Jan 2027<small>SSP portal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Hosteller Maintenance Scheme (SWD) 2026–27</strong> is run by the <strong>Social Welfare Department, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It provides <strong>maintenance support to Scheduled Caste students</strong> who stay in <strong>college or university-run hostels</strong> while pursuing <strong>technical or medical courses</strong>. Applications close <strong>31 January 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Annual family income of <strong>Rs 2.5 lakh or less</strong>.</li>
        <li>Admitted to a <strong>technical or medical course</strong>.</li>
        <li>Studying in a <strong>college offering technical or medical courses</strong>.</li>
        <li>A <strong>hosteller staying in a college/university-run hostel</strong>.</li>
        <li><strong>Promoted to the current academic year</strong> — detained or discontinued students are not eligible.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Maintenance support</strong> for eligible SC hostellers (amount per department norms).</li>
        <li>Disbursed through the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Caste certificate issued by the Tahsildar (current/valid)</li>
        <li>Hostel certificate</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the Hosteller Maintenance Scheme (SWD), 2026–27.</li>
        <li><strong>Submit before 31 January 2027</strong>Upload caste, income and hostel proofs and track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who is this scheme for?","SC students with family income up to Rs 2.5 lakh who stay in college/university hostels while studying technical or medical courses."),
 ("Are day scholars eligible?","No — the applicant must be a hosteller in a college or university-run hostel."),
 ("Are detained students eligible?","No — detained or discontinued students are explicitly excluded."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka listing (31 Jan 2027; SC; income ≤ Rs 2.5L; technical/medical course; college/university-run hostel; promoted; detained ineligible; SWD; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-dme-st','ka-dmw','ka-dme-nursing'],
),

dict(
 slug='karnataka-ssp-vidyasiri-minorities-2026-27',
 title='Karnataka SSP Vidyasiri Scheme for Minorities 2026–27 | StudyDesk Scholarships',
 meta='Karnataka SSP Vidyasiri Scheme for Minorities 2026–27: food and accommodation support for minority students without a hostel seat. Minorities track closed 30 Sep 2026.',
 short='Vidyasiri Scheme for Minorities, Karnataka', kicker='Karnataka · Minority · SSP',
 mono='KA', prov_short='Directorate of Minorities, Karnataka', prov_long='Directorate of Minorities, Government of Karnataka',
 h1='Karnataka SSP Vidyasiri Scheme for Minorities 2026–27',
 sub='Food and accommodation support — for minority students who applied for a minority hostel seat but were not allotted one.',
 dpill='Closed 30 Sep 2026', dl_long='30 Sep 2026 (closed)',
 facts=facts([('Award','Financial assistance<small>Food & accommodation support</small>'),
              ('Who can apply','Minority students<small>No minority-hostel seat allotted</small>'),
              ('Income','\u2264 Rs 2.5L<small>Annual family income</small>'),
              ('Exclusions','No KSOU<small>Promoted to present year</small>'),
              ('Deadline','Closed 30 Sep 2026<small>Minorities track</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Vidyasiri Scheme for Minorities 2026–27</strong> is run by the <strong>Directorate of Minorities, Government of Karnataka</strong> through the <strong>State Scholarship Portal (SSP)</strong>. It supports <strong>minority-community students</strong> with food and accommodation assistance when they <strong>applied for a seat in a minority hostel but were not allotted one</strong>. The minorities-track application window closed on <strong>30 September 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to a <strong>recognised minority community</strong>.</li>
        <li>Annual family income of <strong>Rs 2.5 lakh or less</strong>.</li>
        <li>Enrolled in an <strong>eligible course</strong>.</li>
        <li>Studying at an <strong>eligible college or institution</strong> — Karnataka State Open University (KSOU) is excluded.</li>
        <li><strong>Promoted to the present academic year</strong>.</li>
        <li><strong>Applied for a hostel seat in a minority hostel but was not allotted one</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Financial assistance</strong> towards food and accommodation (the exact amount for this track is not published in the listing).</li>
        <li>Disbursed through the <strong>SSP portal</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic marksheet</li><li>Aadhaar card</li><li>Minority certificate</li>
        <li>Category certificate issued by the Tahsildar (current/valid)</li><li>Bank account details (Aadhaar-seeded)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on SSP</strong>Complete Aadhaar-based one-time registration at ssp.postmatric.karnataka.gov.in.</li>
        <li><strong>Select the scheme</strong>Choose the Vidyasiri Scheme for Minorities, 2026–27.</li>
        <li><strong>Minorities window closed 30 Sep 2026</strong>Upload minority, income and hostel-application proofs and track verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who is this Vidyasiri track for?","Minority-community students who applied for a minority hostel seat but were not allotted one — run by the Directorate of Minorities."),
 ("How is it different from the main Vidyasiri scheme?","The main Vidyasiri (Backward Classes Welfare) track serves OBC students; this track is specifically for minority students via the Directorate of Minorities."),
 ("What is the income limit?","Annual family income of Rs 2.5 lakh or less."),
 ("Are KSOU students eligible?","No — Karnataka State Open University is excluded."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Karnataka minorities listing (31 Jan 2027 shown on Buddy4Study; corrected 16 Oct 2026 — Minorities Welfare Dept closed 30 Sep 2026 per multiple trackers; recognised minority; income ≤ Rs 2.5L; eligible course; excl. KSOU; promoted; applied for minority hostel, not allotted; Directorate of Minorities; SSP portal). General Vidyasiri context cross-checked via Buddy4Study article, scholarshipsx and karnatakacareers (Rs 1,500/month × 10 for the BCWD OBC track; SSP portal).',
 offlinks=[('Karnataka SSP Portal',SSP)],
 related_titles=['ka-dmw','ka-hosteller','ka-dme-st'],
),
]

written = []
for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    written.append((a['slug'], n))
    print('wrote', a['slug'], n, 'bytes')

print('TOTAL:', len(written))

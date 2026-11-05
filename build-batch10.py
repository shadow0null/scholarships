#!/usr/bin/env python3
"""Batch 10: 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'hanns-seidel': dict(mono='HS', title='Hanns Seidel Scholarships 2027 in Germany', href='hanns-seidel-scholarships-2027-germany.html',
              dpill='91 days to go', award='Up to €1,650/month', elig='International Master’s/PhD; B2 German; volunteer record.',
              tags=[('PhD','blue'),('International','teal')]),
 'cg-postmatric': dict(mono='CG', title='Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026-27', href='post-matric-scholarship-sc-st-obc-chhattisgarh-2026-27.html',
              dpill='75 days to go', award='Up to Rs 3,800/year', elig='SC/ST/OBC; CG domicile; Class 11+; 50%+ marks.',
              tags=[('SC/ST/OBC','blue'),('Chhattisgarh','teal')]),
 'chandigarh-sc': dict(mono='NSP', title='Centrally Sponsored Post-Matric Scholarship for SC Students, Chandigarh 2026-27', href='post-matric-sc-chandigarh-2026-27.html',
              dpill='45 days to go', award='Up to Rs 1,200/month', elig='SC; Chandigarh domicile; Class 11–PhD; income < Rs 2.5 lakh.',
              tags=[('SC','blue'),('Chandigarh','teal')]),
 'griffith-vc': dict(mono='G', title="Griffith University Vice Chancellor's International Scholarship 2027", href='griffith-vc-international-scholarship-2027.html',
              dpill='43 days to go', award='50% tuition waiver', elig='International; GPA 6.0/7; offer received; full-time.',
              tags=[('UG/PG','blue'),('Australia','teal')]),
 'umbrella-pre-megh': dict(mono='NSP', title='Umbrella Scheme Pre-Matric Scholarship for ST Students (Class 9 & 10), Meghalaya 2026-27', href='umbrella-pre-matric-st-meghalaya-2026-27.html',
              dpill='45 days to go', award='Up to Rs 5,250/year', elig='ST; Meghalaya domicile; Class 9–10; income < Rs 2.5 lakh.',
              tags=[('ST','blue'),('Meghalaya','teal')]),
}

ARTICLES = [
dict(
 slug='hanns-seidel-scholarships-2027-germany',
 title='Hanns Seidel Scholarships 2027 in Germany | StudyDesk Scholarships',
 meta='Hanns Seidel Scholarships 2027: up to €1,650/month for international Master’s and PhD students in Germany. B2 German required. Apply by 15 Jan 2027.',
 short='Hanns Seidel Scholarships 2027', kicker='Germany · Master’s/PhD · International',
 mono='HS', prov_short='Hanns Seidel Foundation', prov_long='Hanns-Seidel-Stiftung, Munich',
 h1='Hanns Seidel Scholarships 2027 in Germany',
 sub='Up to €1,650 a month — for international Master’s and PhD students committed to Germany and to society.',
 dpill='91 days to go', dl_long='15 Jan 2027',
 facts=facts([('Award','Up to €1,650 / month<small>+ €300 allowance + insurance</small>'),
              ('Who can apply','International Master’s/PhD<small>Admitted in Germany; B2 German</small>'),
              ('Need','Volunteer record<small>Social commitment required</small>'),
              ('Deadline','15 Jan 2027<small>Winter cycle</small>'),
              ('Tracks','Study / Doctoral / Journalism<small>Non-repayable grants</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Hanns Seidel Foundation (Hanns-Seidel-Stiftung)</strong> scholarship programme — one of Germany's six major political foundations' talent schemes — funds <strong>highly qualified international Master's and doctoral students</strong> in Germany. Beyond money, scholars get <strong>mentoring, seminars and a lifelong alumni network</strong>. All scholarships are <strong>non-repayable grants</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>International student planning or pursuing <strong>Master's or doctoral studies in Germany</strong>.</li>
        <li><strong>Excellent academic record</strong> with a clear study/career plan.</li>
        <li><strong>German at B2 level minimum</strong> at application (C1 after the first year) — applications without proof are rejected.</li>
        <li><strong>Proven volunteer / civic engagement</strong> record.</li>
        <li>Doctoral applicants: completed dissertation plan/exposé, academic references, supervisor approval.</li>
        <li>Journalism track: relevant work samples (up to five).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend:</strong> up to €992 (Master's) / €1,300–1,650 (PhD).</li>
        <li><strong>Study allowance</strong> €300/month; <strong>health insurance subsidy</strong> up to €102/month.</li>
        <li><strong>One-time travel reimbursement.</strong></li>
        <li><strong>Mentoring, seminars, workshops</strong> and alumni network.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Application form</li><li>Degree certificate + transcripts</li><li>Passport</li>
        <li>CV (tabular + narrative)</li><li>Personal statement / study goals</li>
        <li>Volunteer certificates; recommendation letter(s)</li><li>German B2 proof</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Hanns Seidel Foundation portal</strong>hss.de — scholarship section.</li>
        <li><strong>Upload all documents</strong>Incomplete applications cannot be submitted.</li>
        <li><strong>Submit in the winter cycle</strong><strong>15 December 2026 – 15 January 2027</strong> (summer cycle: 15 Jun – 15 Jul 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need German?","Yes — B2 at application is mandatory; applications without proof are rejected."),
 ("Is volunteering really required?","Yes — a proven record of social/voluntary commitment is a core criterion."),
 ("How much is the stipend?","Up to €992/month for Master's, €1,300–1,650 for PhD, plus allowances."),
 ("When will I hear back?","About four weeks after the deadline."),
]),
 verify='Verified 16 Oct 2026 via Bright Scholarship (€992 Master’s / €1,650 PhD + €300 allowance + €102 insurance; B2 German; volunteer record; window 15 Dec 2026–15 Jan 2027), OpForAll and AfterSchoolAfrica (same window; document lists).',
 offlinks=[('Hanns Seidel Foundation (official)','https://www.hss.de/en/scholarships/')],
 related_titles=['swiss-phd','zonta-ae','epfl-summer'],
),

dict(
 slug='post-matric-scholarship-sc-st-obc-chhattisgarh-2026-27',
 title='Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026-27 | StudyDesk Scholarships',
 meta='Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026-27: up to Rs 3,800/year. Eligibility, deadline 30 Dec 2026.',
 short='CG Post-Matric Scholarship', kicker='Chhattisgarh · SC/ST/OBC',
 mono='CG', prov_short='Govt. of Chhattisgarh', prov_long='Dept. of Tribal and Scheduled Caste, Government of Chhattisgarh',
 h1='Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026–27',
 sub='Up to Rs 3,800 a year — Chhattisgarh’s post-matric support for SC, ST and OBC students.',
 dpill='75 days to go', dl_long='30 Dec 2026',
 facts=facts([('Award','Up to Rs 3,800 / year<small>SC/ST hostellers</small>'),
              ('Who can apply','SC/ST/OBC students<small>CG domicile; Class 11+; 50%+</small>'),
              ('Income limit','Rs 2.5L (SC/ST) · Rs 1L (OBC)<small>Family income</small>'),
              ('Deadline','30 Dec 2026<small>State portal</small>'),
              ('e-KYC','Aadhaar e-KYC mandatory<small>+ NSP OTR for college</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026–27</strong>, run by the <strong>Department of Tribal and Scheduled Caste, Government of Chhattisgarh</strong>, supports SC, ST and OBC students of the state in <strong>Class 11 and above</strong>. Fresh applications opened 1 August 2026; both fresh and renewal applications close <strong>30 December 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Permanent resident of Chhattisgarh</strong> (domicile certificate).</li>
        <li>Belong to <strong>SC, ST or OBC</strong> with a permanent caste certificate.</li>
        <li><strong>Minimum 50% marks</strong> in the previous examination.</li>
        <li>Studying in <strong>Class 11 or above</strong> in a recognised institution.</li>
        <li>Annual family income: <strong>SC/ST ≤ Rs 2,50,000; OBC ≤ Rs 1,00,000</strong>.</li>
        <li><strong>Aadhaar e-KYC mandatory</strong>; college applicants need <strong>NSP OTR</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th>Category</th><th>Hosteller</th><th>Day scholar</th></tr>
      <tr><td>SC/ST</td><td>Rs 3,800/yr</td><td>Rs 2,250/yr</td></tr>
      <tr><td>OBC (Class 11)</td><td>Rs 1,000/yr</td><td>Rs 600/yr</td></tr>
      <tr><td>OBC (Class 12)</td><td>Rs 1,100/yr</td><td>Rs 700/yr</td></tr></table>
      <p>College students additionally get <strong>tuition fee support + maintenance allowance</strong> by course. Paid by <strong>DBT</strong>.</p>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate</li><li>Caste certificate</li><li>Birth certificate</li>
        <li>Income certificate</li><li>Previous year's marksheet</li><li>Passport-size photograph</li>
        <li>Aadhaar (e-KYC + OTR for college)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your portal</strong>Class 11–12: schoolscholarship.cg.nic.in · After Class 12: postmatric-scholarship.cg.nic.in (e-Medha).</li>
        <li><strong>Register under Students Corner</strong>Complete Aadhaar e-KYC.</li>
        <li><strong>Fill, upload, submit</strong>Before <strong>30 December 2026</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Studying outside Chhattisgarh?</strong> CG-domicile students in other states can apply on the e-Medha portal with their CG domicile and caste certificates.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 2.5 lakh for SC/ST, Rs 1 lakh for OBC."),
 ("Is there a minimum marks requirement?","Yes — 50% in the previous examination."),
 ("Which portal do I use?","Class 11–12: schoolscholarship.cg.nic.in; after Class 12: postmatric-scholarship.cg.nic.in (e-Medha)."),
 ("Is Aadhaar e-KYC needed?","Yes — mandatory; the application is incomplete without it."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (30 Dec 2026; Rs 3,800/2,250 SC-ST; OBC 600–1,100; 50% marks; income limits) and Shiksha (portals; e-KYC mandatory; NSP OTR for college; outside-state route).',
 offlinks=[('CG Post-Matric portal (official)','https://postmatric-scholarship.cg.nic.in/')],
 related_titles=['goa-sc','chandigarh-sc','sikkim-sc'],
),

dict(
 slug='post-matric-sc-chandigarh-2026-27',
 title='Centrally Sponsored Post-Matric Scholarship for SC Students, Chandigarh 2026-27 | StudyDesk',
 meta='Post-Matric Scholarship for SC Students, Chandigarh 2026-27: maintenance up to Rs 1,200/month. Eligibility, deadline 30 Nov 2026.',
 short='Post-Matric SC, Chandigarh', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='Centrally Sponsored Post-Matric Scholarship for SC Students, Chandigarh 2026–27',
 sub='Monthly maintenance up to Rs 1,200 — for SC students of Chandigarh from Class 11 to PhD.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Up to Rs 1,200 / month<small>+ other benefits</small>'),
              ('Who can apply','SC students<small>Chandigarh domicile; Class 11–PhD</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Nov 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Aadhaar-linked account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Post-Matric Scholarship for SC Students, Chandigarh 2026–27</strong>, from the <strong>Ministry of Social Justice and Empowerment</strong> and implemented by the <strong>Government of Chandigarh</strong>, gives financial assistance to <strong>SC students of the UT from Class 11 to PhD level</strong>. Applications go through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domicile of Chandigarh</strong>.</li>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Studying at <strong>post-matric level (Class 11 and above)</strong> at a recognised institution / Central-State Board.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
        <li><strong>Not receiving any other centrally-funded pre-matric scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly maintenance allowance up to Rs 1,200</strong> plus other benefits (fee reimbursement by course group).</li>
        <li>Paid by <strong>DBT to the Aadhaar-linked bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Chandigarh)</li><li>SC certificate</li><li>Income certificate</li>
        <li>Previous year's marksheet</li><li>Bank passbook (Aadhaar-linked)</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Chandigarh + Post-Matric SC scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>30 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Below Rs 2,50,000 per year of family income from all sources."),
 ("Which classes are covered?","Class 11 through PhD level."),
 ("Where do I apply?","On the National Scholarship Portal, scholarships.gov.in."),
 ("Can I hold another scholarship with it?","Not another centrally-funded pre-matric scholarship."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Chandigarh listing (30 Nov 2026; up to Rs 1,200/month; SC; Chandigarh domicile; Class 11–PhD; income < Rs 2.5L) and the B4S Chandigarh scholarships guide (NSP route).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['goa-sc','sikkim-sc','megh-sc'],
),

dict(
 slug='griffith-vc-international-scholarship-2027',
 title="Griffith University Vice Chancellor's International Scholarship 2027 | StudyDesk Scholarships",
 meta="Griffith University Vice Chancellor's International Scholarship 2027: 50% tuition waiver for the whole degree. Eligibility, deadline 28 Nov 2026.",
 short="Griffith VC Scholarship", kicker='Australia · UG/PG · International',
 mono='G', prov_short='Griffith University', prov_long='Griffith University, Australia',
 h1="Griffith University Vice Chancellor's International Scholarship 2027",
 sub='50% off tuition for your whole degree — for exceptional international students at Griffith.',
 dpill='43 days to go', dl_long='28 Nov 2026',
 facts=facts([('Award','50% tuition waiver<small>Valid for the whole degree</small>'),
              ('Who can apply','International students<small>GPA 6.0/7; offer received</small>'),
              ('Level','UG + PG coursework<small>Full-time; 2026/2027 start</small>'),
              ('Deadline','28 Nov 2026<small>Trimester 1, 2027 intake</small>'),
              ('Note','Not automatic<small>Separate application needed</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Vice Chancellor's International Scholarship</strong> rewards exceptional international students commencing <strong>undergraduate or postgraduate coursework</strong> at <strong>Griffith University, Australia</strong>. It covers <strong>50% of tuition fees for the entire degree</strong> — one of Australia's most generous university awards.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of a country other than Australia or New Zealand.</strong></li>
        <li><strong>New, commencing international student</strong> (full-time).</li>
        <li><strong>Received an offer</strong> to study at Griffith by the scholarship closing date.</li>
        <li><strong>Minimum GPA 6.0 on a 7-point scale</strong> (approx. 85%+ in Class 12 for Indian UG applicants).</li>
        <li>Meet all <strong>academic and English language</strong> entry requirements.</li>
      </ul>
      <div class="honest-note"><strong>Not automatic:</strong> unlike Griffith's 20–25% awards (applied automatically on offer), the 50% VC scholarship needs a <strong>separate application with a personal statement</strong> after you accept your offer.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>50% tuition fee reduction</strong>, valid for the <strong>whole degree</strong> (subject to ongoing eligibility).</li>
        <li>Recognition as a <strong>Vice Chancellor's International Scholar</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Griffith Letter of Offer</li><li>Academic transcripts and certificates</li>
        <li><strong>Personal statement (250–500 words)</strong> — why Griffith, your goals, achievements</li>
        <li>English proficiency proof (if required)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to study at Griffith</strong>Get your Letter of Offer first.</li>
        <li><strong>Apply for the scholarship</strong>On the Griffith scholarships page — attach records + personal statement.</li>
        <li><strong>Submit before 28 November 2026</strong>For the Trimester 1, 2027 intake.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is it worth?","50% of tuition fees for the entire degree."),
 ("What GPA do I need?","6.0 on a 7-point scale — roughly 85%+ in Class 12 for Indian applicants."),
 ("Is it automatic?","No — you must apply separately after receiving your offer."),
 ("Does it cover living costs?","No — tuition only; plan separately for accommodation, living and visa costs."),
]),
 verify='Verified 16 Oct 2026 against the official Griffith University scholarship page (50% tuition; whole degree; non-Australia/NZ; GPA 6.0/7; offer required; separate application with personal statement) and the B4S 2027 listing (28 Nov 2026 deadline).',
 offlinks=[("Griffith VC Scholarship (official)",'https://www.griffith.edu.au/international/scholarships-finance/scholarships/vice-chancellors-international-scholarship')],
 related_titles=['swiss-phd','hanns-seidel','zonta-ae'],
),

dict(
 slug='umbrella-pre-matric-st-meghalaya-2026-27',
 title='Umbrella Scheme Pre-Matric Scholarship for ST Students (Class 9 & 10), Meghalaya 2026-27 | StudyDesk',
 meta='Umbrella Pre-Matric Scholarship for ST Students, Meghalaya 2026-27: up to Rs 5,250/year + books grant. Deadline 30 Nov 2026.',
 short='Umbrella Pre-Matric ST, Meghalaya', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via NSP)',
 h1='Umbrella Scheme Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Meghalaya 2026–27',
 sub='Up to Rs 5,250 a year plus a books grant — for ST students of Meghalaya in Classes 9 and 10.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Up to Rs 5,250 / year<small>+ Rs 750–1,000 books grant</small>'),
              ('Who can apply','ST students<small>Meghalaya domicile; Class 9–10</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','30 Nov 2026<small>Via NSP</small>'),
              ('Verify by','21 Dec 2026<small>Institute verification</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Umbrella Scheme Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Meghalaya 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, supports <strong>Scheduled Tribe students of Meghalaya in Classes 9 and 10</strong> — cutting dropout in the move to secondary school. Applications opened <strong>3 July 2026</strong> on the National Scholarship Portal; the state released ~Rs 93 crore to 96,000+ ST students under the Umbrella Scheme in August 2026.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domicile of Meghalaya</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> community.</li>
        <li><strong>Regular full-time student in Class 9 or 10</strong> in a government school or a recognised school / Central-State Board.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>.</li>
        <li>School's <strong>Institute Nodal Officer registered on NSP 2.0</strong>.</li>
        <li><strong>Not receiving any other centrally-funded pre-matric scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Scholarship for 10 months:</strong> Rs 2,250/year (day scholars) / Rs 5,250/year (hostellers).</li>
        <li><strong>Books and ad-hoc grant:</strong> Rs 750/year (day) / Rs 1,000/year (hostellers).</li>
        <li>Paid by <strong>DBT</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Meghalaya)</li><li>ST certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank details (Aadhaar-linked)</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Select Meghalaya + Umbrella Pre-Matric ST scheme.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>30 November 2026</strong>.</li>
        <li><strong>Institute verifies by 21 December 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Two scholarships?</strong> If awarded two simultaneously, choose one and communicate your choice through your institution's head.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much will I get?","Rs 2,250 per year as a day scholar or Rs 5,250 as a hosteller, plus the books grant."),
 ("What is the income limit?","Below Rs 2,50,000 per year of family income from all sources."),
 ("Which classes are covered?","Class 9 and Class 10."),
 ("When did applications open?","3 July 2026; they close 30 November 2026."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 Meghalaya listing (30 Nov 2026; Rs 2,250 day / 5,250 hostel per annum; Rs 750/1,000 books grant; ST; Meghalaya domicile; income < Rs 2.5L) and MeghalayaPortal (dates; INO registration; verification by 21 Dec 2026).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['umbrella-megh','manipur-st','prematric-st-goa'],
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
p['done'] += ['Hanns Seidel Scholarships 2027 in Germany (Funded)',
 'Post-Matric Scholarship for SC/ST/OBC, Chhattisgarh 2026-27',
 "Centrally Sponsored Post-Matric Scholarship for SC Students, Chandigarh 2026-27",
 "Griffith University Vice Chancellor's International Scholarship 2027",
 'Umbrella Scheme Pre-Matric Scholarship For ST Students (Classes 9 & 10), Meghalaya 2026-27']
p['runs'] = 10
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 10 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 46 | hanns-seidel-scholarships-2027-germany | Hanns Seidel Scholarships 2027 | 15 Jan 2027 | Yes — Bright/OpForAll |
| 47 | post-matric-scholarship-sc-st-obc-chhattisgarh-2026-27 | CG Post-Matric SC/ST/OBC | 30 Dec 2026 | Yes — B4S/Shiksha |
| 48 | post-matric-sc-chandigarh-2026-27 | Post-Matric SC, Chandigarh | 30 Nov 2026 | Yes — B4S |
| 49 | griffith-vc-international-scholarship-2027 | Griffith VC Scholarship 2027 | 28 Nov 2026 | Yes — Griffith official/B4S |
| 50 | umbrella-pre-matric-st-meghalaya-2026-27 | Umbrella Pre-Matric ST, Meghalaya | 30 Nov 2026 | Yes — B4S/MeghalayaPortal |

**Completed: 50 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

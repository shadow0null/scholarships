#!/usr/bin/env python3
"""Batch 4: 5 verified articles. Verified 16 Oct 2026. Skipped: Vylor Agritech (unverifiable), ICAR SRF (ambiguous listing)."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'icar-ntspg': dict(mono='ICAR', title='ICAR National Talent Scholarship (PG) 2026', href='icar-nts-pg-scholarship-2026.html',
              dpill='15 days to go', award='Rs 5,000/month', elig='PG agriculture outside home state; full-time; good conduct.',
              tags=[('Merit','blue'),('Central Govt','teal')]),
 'topclass-sc': dict(mono='NSP', title='NSP Top Class Education Scholarship for SC Students 2026-27', href='nsp-top-class-education-sc-2026-27.html',
              dpill='15 days to go', award='Full tuition + Rs 86,000', elig='SC; 60%+ in Class 12; full-time UG/PG; income < Rs 8 lakh.',
              tags=[('SC','blue'),('Central Govt','teal')]),
 'nasa-hubble': dict(mono='NASA', title='NASA Hubble Fellowship Program 2027', href='nasa-hubble-fellowship-program-2027.html',
              dpill='12 days to go', award='Salary + benefits, 3 yrs', elig='PhD (2023+) in astronomy/physics; any nationality; U.S. host.',
              tags=[('Fellowship','blue'),('International','teal')]),
 'bloomberg-harvard': dict(mono='H', title='Bloomberg Harvard Visiting Scholars Program 2027', href='bloomberg-harvard-visiting-scholars-2027.html',
              dpill='12 days to go', award='Residency + housing + support', elig='Researchers with doctoral degree; urban research focus.',
              tags=[('Fellowship','blue'),('International','teal')]),
 'oasis-scst': dict(mono='WB', title='Oasis Post-Matric Scholarship for SC/ST Students, WB 2026-27', href='oasis-post-matric-sc-st-west-bengal-2026-27.html',
              dpill='15 days to go', award='Up to Rs 13,500 + maintenance', elig='SC/ST; West Bengal domicile; Class 11+; income ≤ Rs 2.5 lakh.',
              tags=[('SC/ST','blue'),('West Bengal','teal')]),
 # carried from batch 3 for related cards
 'icar-nts': dict(mono='ICAR', title='ICAR National Talent Scholarship (UG) 2026', href='icar-nts-ug-scholarship-2026.html',
              dpill='15 days to go', award='Rs 3,000/month', elig='UG agriculture outside home state via AIEEA; full-time study.',
              tags=[('Merit','blue'),('Central Govt','teal')]),
 'megh-sc': dict(mono='NSP', title='NSP Post-Matric Scholarship for SC Students, Meghalaya 2026-27', href='nsp-post-matric-sc-meghalaya-2026-27.html',
              dpill='14 days to go', award='Up to Rs 13,500 + maintenance', elig='SC students, Meghalaya domicile, Class 11–PhD; income ≤ Rs 2.5 lakh.',
              tags=[('SC','blue'),('Meghalaya','teal')]),
 'ambedkar-hp': dict(mono='A', title='Dr. Ambedkar Medhavi Chatravriti Yojana, HP 2026-27', href='ambedkar-medhavi-chatravriti-himachal-2026-27.html',
              dpill='15 days to go', award='Rs 10,000–12,000/year × 2 yrs', elig='SC/OBC HP domicile; top HPBOSE matric merit; Class 11/professional course.',
              tags=[('SC/OBC','blue'),('Himachal','teal')]),
}

ARTICLES = [
dict(
 slug='icar-nts-pg-scholarship-2026',
 title='ICAR National Talent Scholarship (PG) 2026: Rs 5,000/Month | StudyDesk Scholarships',
 meta='ICAR National Talent Scholarship (Postgraduate) 2026: Rs 5,000/month for PG agriculture students studying outside their home state. Eligibility, deadline 31 Oct 2026.',
 short='ICAR NTS (PG) 2026', kicker='Central Government · ICAR',
 mono='ICAR', prov_short='ICAR', prov_long='Indian Council of Agricultural Research',
 h1='ICAR National Talent Scholarship (Postgraduate) 2026',
 sub='Rs 5,000 a month for Master’s agriculture students who joined a university outside their home state.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Rs 5,000 / month<small>Via NSP; DBT</small>'),
              ('Who can apply','PG agriculture students<small>Outside home state</small>'),
              ('Study','Full-time<small>Good conduct; no other scholarship</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Note','ICAR-PG Scholarship separate<small>Rs 12,640/mo for merit ranks</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>ICAR National Talent Scholarship (Postgraduate)</strong> is awarded by the Indian Council of Agricultural Research to Master's students in agriculture and allied disciplines who are studying at an agricultural university <strong>outside their state of domicile</strong>. It is disbursed through the National Scholarship Portal (NSP).</p>
      <div class="honest-note"><strong>Don't confuse the two ICAR PG awards:</strong> the <strong>ICAR-PG Scholarship</strong> (Rs 12,640/month + Rs 6,000/year contingency) goes to merit-ranked candidates admitted through the ICAR AIEEA-PG exam; the <strong>NTS-PG</strong> (Rs 5,000/month) supports students who joined an agricultural university outside their home state but are not in the ICAR-PG scholarship bracket.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Pursuing a <strong>Master's degree in agriculture or allied disciplines</strong> at an <strong>ICAR-recognised agricultural university outside your state of domicile</strong>.</li>
        <li>Maintain <strong>good academic performance and conduct</strong>.</li>
        <li><strong>Full-time study</strong>; no employment; <strong>no other scholarship</strong> simultaneously.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 5,000 per month.</strong></li>
        <li>Disbursed via the <strong>National Scholarship Portal</strong> to the student's bank account.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the NSP application form — keep admission proof, ID proof, marksheets and bank details ready.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in — find the ICAR NTS (PG) listing.</li>
        <li><strong>Register / log in</strong>Fresh or renewal as applicable.</li>
        <li><strong>Fill and upload</strong>Academic, admission and bank details with documents.</li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the difference between ICAR-PG Scholarship and NTS-PG?","The ICAR-PG Scholarship (Rs 12,640/month) is for merit-ranked AIEEA-PG candidates; NTS-PG (Rs 5,000/month) is for students at an out-of-state agricultural university who are not in that bracket."),
 ("I study agriculture in my home state. Am I eligible?","No — the university must be outside your state of domicile."),
 ("Can I hold another scholarship with it?","No — no other financial assistance is permitted during the course."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (Rs 5,000/month, 31 Oct 2026, NSP) and AgriJob ICAR guide (Sept 2026: NTS-PG Rs 5,000/month for out-of-state AU students vs ICAR-PG Scholarship Rs 12,640/month for merit ranks). Older guides quoting Rs 3,000 treated as outdated.',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['icar-nts','topclass-sc','oasis-scst'],
),

dict(
 slug='nsp-top-class-education-sc-2026-27',
 title='NSP Top Class Education Scholarship for SC Students 2026-27 | StudyDesk Scholarships',
 meta='Top Class Education Scholarship for SC Students 2026-27: full tuition up to Rs 2 lakh/year + Rs 86,000 academic allowance. Eligibility, deadline 31 Oct 2026.',
 short='Top Class Education SC', kicker='Central Government · NSP · SC',
 mono='NSP', prov_short='Ministry of Social Justice', prov_long='Ministry of Social Justice & Empowerment (via NSP)',
 h1='Central Sector Scholarship of Top Class Education for SC Students 2026–27',
 sub='Full tuition plus Rs 86,000 in the first year — for SC students in India’s top institutions.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Full tuition + Rs 86,000<small>1st year; Rs 41,000 after</small>'),
              ('Who can apply','SC students<small>60%+ in Class 12; full-time UG/PG</small>'),
              ('Income limit','Rs 8 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>Via NSP</small>'),
              ('Girls quota','30% of slots<small>Per institution</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Central Sector Scholarship of Top Class Education for SC Students 2026–27</strong>, run by the <strong>Ministry of Social Justice and Empowerment</strong>, recognises and promotes quality education beyond Class 12 among Scheduled Caste students admitted to <strong>notified premier institutions</strong> (IITs, NITs, IIMs, AIIMS and other listed institutions). It is applied for through the National Scholarship Portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Caste (SC)</strong> category.</li>
        <li>Passed <strong>Class 12 with at least 60% marks</strong>.</li>
        <li>Secured admission to a <strong>notified institution</strong> for a <strong>full-time undergraduate or postgraduate</strong> degree.</li>
        <li>Annual <strong>family income below Rs 8,00,000</strong> (income certificate from a revenue officer not below Tehsildar rank).</li>
        <li>Maximum <strong>two siblings per family</strong> can benefit.</li>
        <li><strong>Cannot hold any other Central/State scholarship</strong> simultaneously.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee and non-refundable charges</strong> — ceiling of <strong>Rs 2,00,000 per year</strong> for private institutions.</li>
        <li><strong>Academic allowance: Rs 86,000 in the first year</strong>, <strong>Rs 41,000 per year</strong> after — for living expenses, books, stationery and a computer/laptop with accessories.</li>
        <li><strong>30% of slots per institution reserved for SC girl students</strong> (unfilled slots go to boys on merit).</li>
        <li>Paid by <strong>DBT</strong>; payable once admission is secured and classes begin.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Caste certificate (SC)</li><li>Income certificate (revenue officer, Tehsildar rank or above)</li>
        <li>Class 12 marksheet</li><li>Admission proof</li><li>Aadhaar + bank details</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Register / log in</strong>Complete OTR if needed.</li>
        <li><strong>Select the scheme</strong>Central Sector Scholarship of Top Class Education for SC Students.</li>
        <li><strong>Upload documents and submit</strong>Before <strong>31 October 2026</strong>. No fee.</li>
      </ol>
      <div class="honest-note"><strong>Staying eligible:</strong> the scholarship can be discontinued if you fail to get promoted to the next class/semester, and changing institutions after selection ends the benefit.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the income limit?","Rs 8 lakh per year of family income from all sources."),
 ("Is there a quota for girls?","Yes — 30% of each institution's slots are reserved for SC girl students."),
 ("Can two siblings both get it?","Yes — up to two siblings per family."),
 ("What if I change college later?","Further benefits stop if you change the institution after selection."),
]),
 verify='Verified 16 Oct 2026 via Buddy4Study 2026-27 listing (31 Oct 2026; full tuition up to Rs 2L/yr private; Rs 86,000/41,000 allowance; 60% Class 12; income < Rs 8L; 30% girls) and GovtSchemes.in FAQ (NSP schedule, documents, sibling cap).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['megh-sc','icar-ntspg','ambedkar-hp'],
),

dict(
 slug='nasa-hubble-fellowship-program-2027',
 title='NASA Hubble Fellowship Program 2027: Fully Funded Postdoc | StudyDesk Scholarships',
 meta='NASA Hubble Fellowship Program 2027: salary + benefits for up to 3 years for postdoctoral astrophysicists. Eligibility, deadline 28 Oct 2026.',
 short='NASA Hubble Fellowship 2027', kicker='NASA · Postdoctoral Fellowship',
 mono='NASA', prov_short='NASA', prov_long='NASA Astrophysics Division (administered by STScI)',
 h1='NASA Hubble Fellowship Program 2027',
 sub='Salary, benefits and research funding for up to three years — for postdoctoral scientists in NASA Astrophysics.',
 dpill='12 days to go', dl_long='28 Oct 2026',
 facts=facts([('Award','Salary + benefits<small>Up to 3 years</small>'),
              ('Who can apply','Recent postdocs<small>PhD 2023+ in astronomy/physics</small>'),
              ('Nationality','All nationalities<small>U.S. host institution required</small>'),
              ('Deadline','28 Oct 2026<small>Letters by 4 Nov</small>'),
              ('Fellowships','Up to 24<small>Einstein / Hubble / Sagan tracks</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>NASA Hubble Fellowship Program (NHFP) 2027</strong>, announced by the NASA Astrophysics Division and administered by the Space Telescope Science Institute (STScI) with JPL, NExScI and the Chandra X-ray Center, supports postdoctoral scientists doing <strong>independent research contributing to NASA Astrophysics</strong> — theoretical, observational and/or instrumental. Fellows become <strong>NHFP Einstein, Hubble or Sagan Fellows</strong> depending on their research area, continuing the legacy of those three prize fellowships.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Completed (or will complete) all doctoral requirements <strong>on or after 1 January 2023</strong> in <strong>astronomy, physics or related disciplines</strong>.</li>
        <li><strong>Open to applicants of any nationality.</strong></li>
        <li>Propose <strong>independent research</strong> relevant to NASA Astrophysics.</li>
        <li>Secure a <strong>U.S. host institution</strong> (max two new fellows per institution per year; host must comply with the NHFP employment policy).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Salary support</strong> comparable to other prize fellowships, paid via the host institution.</li>
        <li><strong>Benefits</strong> including health insurance (per host-institution rules).</li>
        <li><strong>Research allowance</strong> for travel, computing, publications and direct research costs.</li>
        <li>Duration <strong>up to three years</strong> (initial one-year appointment + two annual renewals, subject to performance and NASA funding).</li>
        <li>Up to <strong>24 fellowships</strong> expected this year.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Application form (NHFP portal)</li><li>Research proposal tailored to NHFP priorities</li>
        <li>CV</li><li><strong>Three letters of reference</strong> (due 4 Nov 2026)</li>
        <li>Host institution confirmation</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the Announcement of Opportunity</strong>On the NHFP program page (science.nasa.gov).</li>
        <li><strong>Apply on the NHFP portal</strong>cosmos.ipac.caltech.edu/nhfp/application.php — open since 8 Sept 2026.</li>
        <li><strong>Submit by 28 October 2026</strong>7:00 PM EDT.</li>
        <li><strong>Referees submit by 4 November 2026</strong>Awards expected February 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am not a U.S. citizen. Can I apply?","Yes — the program is open to applicants of any nationality, but you must secure a U.S. host institution."),
 ("How long is the fellowship?","Up to three years: one initial year plus two annual renewals."),
 ("What are the Einstein/Hubble/Sagan tracks?","Fellows are designated by research area: Einstein (How does the universe work?), Hubble (How did we get here?), Sagan (Are we alone?)."),
 ("When are results announced?","Award offers are expected in February 2027, with public announcement in March 2027."),
]),
 verify='Verified 16 Oct 2026 against the official NASA announcement (science.nasa.gov, 14 Sept 2026): up to 24 fellowships, PhD on/after 1 Jan 2023, any nationality, up to 3 years, U.S. host institution, deadline 28 Oct 2026, reference letters by 4 Nov 2026. Cross-checked with fundsforNGOs and ScholarshipUnion.',
 offlinks=[('NASA NHFP announcement (official)','https://science.nasa.gov/astrophysics/programs/physics-of-the-cosmos/community/applications-for-the-2027-nasa-hubble-fellowship-program/')],
 related_titles=['bloomberg-harvard','icar-ntspg','topclass-sc'],
),

dict(
 slug='bloomberg-harvard-visiting-scholars-2027',
 title='Bloomberg Harvard Visiting Scholars Program 2027 | StudyDesk Scholarships',
 meta='Bloomberg Harvard Visiting Scholars Program 2027: funded research residency at Harvard for doctoral researchers in urban problem-solving. Deadline 28 Oct 2026.',
 short='Bloomberg Harvard Visiting Scholars', kicker='Harvard · Research Fellowship',
 mono='H', prov_short='Harvard University', prov_long='Bloomberg Center for Cities, Harvard University',
 h1='Bloomberg Harvard Visiting Scholars Program 2027',
 sub='A funded semester or year at Harvard — for researchers working on how cities solve problems.',
 dpill='12 days to go', dl_long='28 Oct 2026',
 facts=facts([('Award','Residency + housing<small>+ financial assistance</small>'),
              ('Who can apply','Doctoral researchers<small>Urban research focus</small>'),
              ('Duration','1 semester or 1 year<small>In residence at Harvard</small>'),
              ('Deadline','28 Oct 2026<small>Inaugural cohort</small>'),
              ('Location','Cambridge, Massachusetts<small>Harvard University</small>')]),
 body='''
      <h2 id="about">About the program</h2>
      <p>The <strong>Bloomberg Harvard Visiting Scholars Program 2027</strong> is the <strong>inaugural</strong> residential research program of the <strong>Bloomberg Center for Cities at Harvard University</strong>. It supports rigorous, policy-relevant research on <strong>urban problem-solving and city leadership</strong>, building a collaborative community of researchers whose work strengthens both scholarship and real-world city governance.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>doctoral degree or comparable terminal research degree</strong>.</li>
        <li>Currently hold a <strong>faculty or research appointment</strong> at a degree-granting university or recognised research institution.</li>
        <li>Research must align with the Center's mission: <strong>urban problem-solving, city leadership, public-sector innovation</strong> — e.g. mayoral leadership, evidence-based policymaking, data/AI in governance, high-performing public teams.</li>
        <li>Researchers from <strong>any discipline and career stage</strong> may apply.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>One semester or one full academic year</strong> in residence at the Bloomberg Center for Cities, Harvard University.</li>
        <li><strong>Housing near Harvard University.</strong></li>
        <li><strong>Financial assistance</strong> enabling dedicated research time (may support course buyout or stepping back from regular obligations).</li>
        <li>Access to Harvard's intellectual community — faculty, students, practitioners.</li>
        <li>Possible <strong>visa sponsorship</strong>, subject to circumstances and institutional policies.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>As listed on the program application page — including a <strong>clearly defined research proposal</strong> (questions, methodology, significance, expected outcomes).</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Prepare your research proposal</strong>Addressing an important urban problem.</li>
        <li><strong>Apply via the Bloomberg Center for Cities</strong>Applications opened 16 September 2026.</li>
        <li><strong>Submit before 28 October 2026</strong>Selection notifications expected in February.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this the first year of the program?","Yes — 2027 is the inaugural cohort."),
 ("How long is the residency?","One semester or one full academic year, at Harvard in Cambridge, Massachusetts."),
 ("I don't work on cities directly. Can I apply?","Researchers from any discipline may apply if their work clearly relates to urban problem-solving and city leadership."),
 ("Is housing included?","Yes — housing near Harvard University plus financial assistance for the research residency."),
]),
 verify='Verified 16 Oct 2026 via OpportunityDesk, OYA Opportunities and YouthOp (deadline 28 Oct 2026; doctoral degree required; semester/year residency; housing + financial assistance; inaugural cohort; applications opened 16 Sept 2026).',
 offlinks=[('OpportunityDesk listing','https://opportunitydesk.org/2026/09/22/bloomberg-harvard-visiting-scholars-program-2027/')],
 related_titles=['nasa-hubble','topclass-sc','icar-ntspg'],
),

dict(
 slug='oasis-post-matric-sc-st-west-bengal-2026-27',
 title='Oasis Post-Matric Scholarship for SC/ST Students, West Bengal 2026-27 | StudyDesk',
 meta='Oasis Post-Matric Scholarship West Bengal 2026-27: academic allowance up to Rs 13,500 + monthly maintenance for SC/ST students. Eligibility, deadline 31 Oct 2026.',
 short='Oasis Post-Matric SC/ST, WB', kicker='West Bengal · SC/ST',
 mono='WB', prov_short='Govt. of West Bengal', prov_long='Backward Classes Welfare Dept., Government of West Bengal',
 h1='Oasis Post-Matric Scholarship for SC/ST Students, West Bengal 2026–27',
 sub='Up to Rs 13,500 a year plus monthly maintenance — West Bengal’s own portal for SC/ST post-matric students.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Up to Rs 13,500 / year<small>+ Rs 230–1,200/month maintenance</small>'),
              ('Who can apply','SC/ST students<small>WB domicile; Class 11+</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Oct 2026<small>oasis.gov.in</small>'),
              ('Fees','Full reimbursement<small>Compulsory non-refundable fees</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Oasis Post-Matric Scholarship 2026–27</strong> is West Bengal's dedicated platform — run by the <strong>Backward Classes Welfare Department and Tribal Development Department</strong> — for <strong>SC, ST and OBC</strong> students from Class 9 through postgraduate level. Applications run on the official <strong>Oasis portal (oasis.gov.in)</strong>, separate from the NSP.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Permanent resident (domicile) of West Bengal.</strong></li>
        <li>Belong to the <strong>SC or ST</strong> category (OBC has a separate Oasis track).</li>
        <li>Studying in <strong>Class 11 or above</strong> — ITI, diploma, degree, PG, MPhil, PhD — at an institution <strong>inside India</strong>.</li>
        <li>Annual <strong>family income up to Rs 2,50,000</strong>.</li>
        <li>Passed the previous year's examination.</li>
        <li>Active bank account in the student's own name, <strong>linked with Aadhaar</strong> (name/spelling/DOB/gender must match Aadhaar exactly).</li>
        <li><strong>Not taking any other scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Academic allowance up to Rs 13,500 per year</strong>.</li>
        <li><strong>Monthly maintenance allowance</strong> by course group: Group I (Medicine/Engineering/MBA/PhD) Rs 1,200 hosteller / Rs 550 day scholar; Group II Rs 820/530; Group III Rs 570/300; Group IV (Class 11–12, ITI) Rs 380/230.</li>
        <li><strong>Reimbursement of compulsory non-refundable fees.</strong></li>
        <li>Paid by <strong>DBT</strong> to the Aadhaar-linked bank account (SC students: 40% first, 60% later).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Aadhaar details</li><li>Caste certificate (SC/ST)</li><li>Income certificate</li>
        <li>Previous exam marksheet</li><li>Bank details (Aadhaar-linked)</li>
        <li>Photograph + institution details</li>
        <li><strong>OTR number</strong> (mandatory for ST students; via NSP e-KYC)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Oasis portal</strong>oasis.gov.in</li>
        <li><strong>Register / log in</strong>New applicants register; renewals log in.</li>
        <li><strong>Fill the form and upload documents</strong>Track via "Track an Application" with your district + tracking ID.</li>
        <li><strong>Submit before 31 October 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Deadline note:</strong> the 2026–27 portal is open and the B4S listing shows 31 Oct 2026; some guides call the date "expected". Apply early rather than waiting for a confirmed extension notice on oasis.gov.in.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I apply if I study outside West Bengal?","Yes — the institution must be inside India; West Bengal domicile is what matters."),
 ("Is OTR mandatory?","OTR on NSP is mandatory for ST students; the Oasis form asks for the OTR number."),
 ("How is the money paid?","By DBT to your Aadhaar-linked bank account, usually within 3–4 months of approval."),
 ("What is the income limit?","Rs 2,50,000 per year of family income."),
]),
 verify='Verified 16 Oct 2026 via Shiksha (eligibility table: WB domicile, income ≤ Rs 2.5L, OTR, no other scholarship), AIM India (amounts: academic allowance up to Rs 13,500; maintenance by group), and the B4S 2026-27 listing (31 Oct 2026). Deadline treated as 31 Oct with an early-application note.',
 offlinks=[('Oasis portal (official)','https://oasis.gov.in/')],
 related_titles=['topclass-sc','megh-sc','icar-ntspg'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')

# persist new cards to the shared registry for future batches
import cards_registry
cards_registry.CARDS.update(CARDINFO)
pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').write_text(
    '"""Shared related-card registry for all scholarship articles. Append new batches here."""\n\nCARDS = ' + repr(cards_registry.CARDS) + '\n')

# mark done + skipped in progress
p = json.load(open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json'))
p['done'] += ['ICAR Postgraduate National Talent Scholarship (NTS-PG) 2026',
 'Central Sector Scholarship of Top Class Education for SC Students',
 'NASA Hubble Postdoctoral Fellowships 2027', 'Bloomberg Harvard Visiting Scholars Program 2027',
 'Oasis Post Matric Scholarships for SC/ST Students 2026-27']
p['skipped'] += [{'title': 'Vylor Agritech Scholarship Program for Postgraduate Students FY 26-27',
                  'reason': 'unverifiable — no trace of such a scholarship; Vylor is a seed company (Corteva spin-off) with no scholarship program found'},
                 {'title': 'NSP ICAR Senior Research Fellowship (PGS) 2026',
                  'reason': 'ambiguous — could not verify as a distinct NSP scholarship scheme; SRF results were project-based contractual posts'}]
p['runs'] = 4
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 4 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 16 | icar-nts-pg-scholarship-2026 | ICAR National Talent Scholarship (PG) | 31 Oct 2026 | Yes — B4S/AgriJob |
| 17 | nsp-top-class-education-sc-2026-27 | NSP Top Class Education for SC | 31 Oct 2026 | Yes — B4S/GovtSchemes |
| 18 | nasa-hubble-fellowship-program-2027 | NASA Hubble Fellowship Program 2027 | 28 Oct 2026 | Yes — NASA official |
| 19 | bloomberg-harvard-visiting-scholars-2027 | Bloomberg Harvard Visiting Scholars 2027 | 28 Oct 2026 | Yes — OpportunityDesk/OYA |
| 20 | oasis-post-matric-sc-st-west-bengal-2026-27 | Oasis Post-Matric SC/ST, West Bengal | 31 Oct 2026 | Yes — Shiksha/AIM India |

Skipped this batch: Vylor Agritech Scholarship (unverifiable — no such program exists); ICAR Senior Research Fellowship PGS (ambiguous listing).

**Completed: 20 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

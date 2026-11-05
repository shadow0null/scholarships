#!/usr/bin/env python3
"""Batch 11B (subagent): 8 verified articles. Verified 16 Oct 2026.
SKIPPED: Swiss Government Excellence PhD 2027-28 (duplicate of existing article),
         10 US Colleges 100% Financial Aid (listicle, not a scholarship)."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'mea': dict(mono='MEA', title="Malayalee Engineers' Association Scholarship 2026", href='malayalee-engineers-mea-scholarship-2026.html',
              dpill='16 days to go', award='$600 / year (4–5 yrs)', elig='Kerala; 1st-yr B.Tech/B.Arch; KEAM top 7000; 85%+ in X & XII.',
              tags=[('Engineering','blue'),('Kerala','teal')]),
 'an-prematric': dict(mono='NSP', title='Centrally Sponsored Pre-Matric Scholarship for ST Students (Class 9 & 10), Andaman and Nicobar 2026-27', href='centrally-sponsored-pre-matric-st-andaman-nicobar-2026-27.html',
              dpill='76 days to go', award='Rs 225–525 / month', elig='ST; A&N domicile; Class 9–10; income < Rs 2.5 lakh.',
              tags=[('ST','blue'),('Andaman & Nicobar','teal')]),
 'an-addl': dict(mono='TW', title='Grant of Additional Scholarship to ST Students for Higher Studies, Andaman and Nicobar 2026-27', href='additional-scholarship-st-higher-studies-andaman-nicobar-2026-27.html',
              dpill='76 days to go', award='Rs 1,000 / month', elig='ST; A&N domicile; Class 12+; full-time higher studies.',
              tags=[('ST','blue'),('Andaman & Nicobar','teal')]),
 'iiser-pdrf': dict(mono='IISER', title='IISER Berhampur Post-Doctoral Research Fellowship (PDRF) 2025-26', href='iiser-berhampur-pdrf-2025-26.html',
              dpill='76 days to go', award='Up to Rs 67,000 / month', elig='PhD holders; below 35; Indian or foreign nationals.',
              tags=[('PhD','blue'),('Fellowship','teal')]),
 'malabar': dict(mono='MCT', title='Malabar Charitable Trust Scholarship 2026', href='malabar-charitable-trust-scholarship-2026.html',
              dpill='76 days to go', award='Up to Rs 10,000 (one-time)', elig='Girls; 50%+ in Class 10; higher secondary in govt. schools.',
              tags=[('Girls','blue'),('Class 11–12','teal')]),
 'ramanujan': dict(mono='ANRF', title='Ramanujan Fellowship 2025', href='ramanujan-fellowship-2025-anrf.html',
              dpill='76 days to go', award='Rs 1.35 lakh / month', elig='Indian-origin scientists abroad; below 40; nomination-based.',
              tags=[('Fellowship','blue'),('Research','teal')]),
 'sof-dsas': dict(mono='SOF', title='SOF Defence Services Academic Excellence Scholarship (DSAS) 2026-27', href='sof-dsas-defence-services-scholarship-2026-27.html',
              dpill='76 days to go', award='Rs 5,000 (one-time)', elig='Classes 1–10; defence / internal security families; school-nominated.',
              tags=[('School','blue'),('Defence families','teal')]),
 'aalto': dict(mono='A', title='Aalto University Scholarships 2027 in Finland', href='aalto-university-scholarships-2027-finland.html',
              dpill='81 days to go', award='100% tuition waiver', elig='Non-EU/EEA; merit-based; via admission application.',
              tags=[('Masters','blue'),('Finland','teal')]),
}

ARTICLES = [
dict(
 slug='malayalee-engineers-mea-scholarship-2026',
 title="Malayalee Engineers' Association Scholarship 2026 | StudyDesk Scholarships",
 meta="MEA Scholarship 2026: $600/year for 4–5 years for first-year engineering students of Kerala origin. KEAM top 7000, 85%+ in X & XII. Deadline 1 Nov 2026.",
 short="MEA Scholarship 2026", kicker='MEA Houston · Engineering · Kerala',
 mono='MEA', prov_short="Malayalee Engineers' Association", prov_long="Malayalee Engineers' Association (MEA), Houston, Texas, USA",
 h1="Malayalee Engineers' Association (MEA) Scholarship 2026",
 sub='$600 a year for up to five years — for first-year engineering students of Kerala origin with top KEAM ranks.',
 dpill='16 days to go', dl_long='1 Nov 2026',
 facts=facts([('Award','$600 / year<small>4–5 years + mentorship</small>'),
              ('Who can apply','1st-year B.E./B.Tech/B.Arch<small>Kerala origin; KEAM route</small>'),
              ('Academics','KEAM top 7000<small>85%+ in Class X & XII</small>'),
              ('Deadline','1 Nov 2026<small>Via meahouston.org</small>'),
              ('Need','Financial hardship<small>Income certificate required</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Malayalee Engineers' Association (MEA) Scholarship 2026</strong>, run by the <strong>Malayalee Engineers' Association of Houston, Texas, USA</strong> — an association of Malayalee engineers in the Greater Houston area — has awarded scholarships <strong>every year since 2000</strong>. It supports <strong>financially needy first-year engineering students of Kerala origin</strong> with a <strong>$600-per-year scholarship, renewable for four to five years</strong> subject to satisfactory academic performance, plus <strong>active mentorship</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>First-year student</strong> enrolled in an accredited engineering college or university in India, in a <strong>4-year (8-semester)</strong> course — or a <strong>5-year (10-semester) B.Arch</strong> course — leading to a Bachelor's degree in <strong>Engineering, Technology, Computer Science, Architecture or Naval Architecture</strong>.</li>
        <li>Must have taken the <strong>Kerala state-level engineering entrance examination (KEAM)</strong> and be <strong>ranked within the top 7000</strong>. B.Arch applicants are assessed on <strong>NATA score above 110</strong>.</li>
        <li><strong>Above 85% marks in both Class X and Class XII</strong> examinations.</li>
        <li><strong>Financial hardship:</strong> the award is based on academic merit and financial need. Published listings cite <strong>annual family income below Rs 1,50,000</strong>; an <strong>income certificate from the Tahsildar / Village Officer</strong> is mandatory.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$600 per year</strong> (about Rs 52,900) for <strong>four years</strong> — five for B.Arch — subject to satisfactory performance each year.</li>
        <li><strong>Active mentorship</strong> from MEA members.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Self-attested <strong>mark lists of Class X and Class XII</strong></li>
        <li><strong>KEAM rank sheet</strong> (or <strong>NATA score card</strong> for B.Arch)</li>
        <li><strong>Income certificate</strong> (all sources) issued by the Tahsildar / Village Officer — plus a statement of occupation if parents are daily-wage workers, labourers or in agriculture/trade/business</li>
        <li><strong>Recommendation letter</strong></li>
        <li>Details of <strong>awards and honours</strong> for extracurricular activities</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Download "Information for Applicants"</strong>On meahouston.org — read the eligibility and renewal rules carefully.</li>
        <li><strong>Complete the online application form</strong>On the MEA website. If you don't meet the academic and financial criteria, do not proceed — you won't qualify.</li>
        <li><strong>Email supporting documents</strong>To MeaHouston.scholarship@gmail.com with your name in the subject line, before <strong>1 November 2026</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Apply only if you clear all three criteria</strong> (income, KEAM rank, 85%+ marks) — MEA asks ineligible students not to apply.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the scholarship worth?","$600 per year for four years (five for B.Arch), renewable on satisfactory performance, plus mentorship."),
 ("What KEAM rank do I need?","Within the top 7000 in the Kerala engineering entrance; B.Arch applicants need a NATA score above 110."),
 ("Is there an income limit?","The scheme targets financially needy students; published listings cite below Rs 1,50,000/year, and an income certificate from the Tahsildar/Village Officer is mandatory."),
 ("How do I apply?","Fill the online form on meahouston.org and email your documents to MeaHouston.scholarship@gmail.com by 1 November 2026."),
]),
 verify='Verified 16 Oct 2026 via the official meahouston.org scholarship page ($600/year for 4–5 years + mentorship; 1 Nov 2026 deadline; KEAM top 7000 / NATA 110; 85%+ in X & XII; income certificate mandatory) and Mathrubhumi English (same criteria).',
 offlinks=[('MEA Houston — Apply for Scholarship (official)','https://meahouston.org/apply-for-scholarship/')],
 related_titles=['concentrix','sdef','infocepts'],
),

dict(
 slug='centrally-sponsored-pre-matric-st-andaman-nicobar-2026-27',
 title='Centrally Sponsored Pre-Matric Scholarship for ST Students (Class 9 & 10), Andaman and Nicobar 2026-27 | StudyDesk',
 meta='Pre-Matric Scholarship for ST Students, Andaman and Nicobar 2026-27: Rs 225–525/month for 10 months. Eligibility, deadline 31 Dec 2026.',
 short='Pre-Matric ST, Andaman & Nicobar', kicker='Central Government · NSP · ST',
 mono='NSP', prov_short='Ministry of Tribal Affairs', prov_long='Ministry of Tribal Affairs, Govt. of India (via A&N Administration)',
 h1='Centrally Sponsored Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Andaman and Nicobar 2026–27',
 sub='Rs 225–525 a month for ten months — keeping ST students of the islands in school through Classes 9 and 10.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Rs 225–525 / month<small>10 months; day/hosteller</small>'),
              ('Who can apply','ST students<small>A&N domicile; Class 9–10</small>'),
              ('Income limit','Rs 2.5 lakh / year<small>Family income</small>'),
              ('Deadline','31 Dec 2026<small>Via NSP</small>'),
              ('Mode','DBT<small>Direct to bank account</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Centrally Sponsored Pre-Matric Scholarship for ST Students (Class 9 &amp; 10), Andaman and Nicobar 2026–27</strong>, from the <strong>Ministry of Tribal Affairs, Government of India</strong>, supports <strong>Scheduled Tribe students of the Andaman and Nicobar Islands in Classes 9 and 10</strong> — cutting dropout in the move to secondary school. The A&amp;N scholarship application portal went live on <strong>3 July 2026</strong> for the 2026–27 session.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian national</strong> and <strong>domicile of the Andaman and Nicobar Islands</strong>.</li>
        <li>Belong to the <strong>Scheduled Tribe (ST)</strong> community as notified for the UT.</li>
        <li><strong>Regular full-time student in Class 9 or 10</strong> in a government school or a recognised school / Central-State Board.</li>
        <li>Annual <strong>family income below Rs 2,50,000</strong>, as per the scheme guidelines.</li>
        <li><strong>Not receiving any other centrally-funded pre-matric scholarship.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Day scholars:</strong> Rs 225 per month × 10 months = <strong>Rs 2,250 per year</strong>.</li>
        <li><strong>Hostellers:</strong> Rs 525 per month × 10 months = <strong>Rs 5,250 per year</strong>.</li>
        <li>Paid by <strong>DBT directly to the student's bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Andaman and Nicobar Islands)</li><li>ST certificate</li><li>Income certificate</li>
        <li>Previous class marksheet</li><li>Bank details (Aadhaar-linked)</li><li>Passport-size photograph</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Complete One-Time Registration (OTR)</strong>With Aadhaar-based eKYC.</li>
        <li><strong>Select the scheme and submit</strong>Before <strong>31 December 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much will I get?","Rs 225/month as a day scholar or Rs 525/month as a hosteller, for 10 months of the academic year."),
 ("What is the income limit?","Below Rs 2,50,000 per year of family income from all sources, per the scheme guidelines."),
 ("Which classes are covered?","Class 9 and Class 10."),
 ("Where do I apply?","On the National Scholarship Portal, scholarships.gov.in."),
]),
 verify='Verified 16 Oct 2026 via the B4S 2026-27 A&N listing (31 Dec 2026; Rs 225 day / Rs 525 hostel per month; ST; A&N domicile; Class 9–10; portal live 3 Jul 2026) and EdexLive on the Ministry scheme (same monthly rates for 10 months; DBT; NSP route).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['manipur-st','prematric-st-goa','umbrella-pre-megh'],
),

dict(
 slug='additional-scholarship-st-higher-studies-andaman-nicobar-2026-27',
 title='Grant of Additional Scholarship to ST Students for Higher Studies, Andaman and Nicobar 2026-27 | StudyDesk',
 meta='Additional Scholarship for ST Students, Andaman and Nicobar 2026-27: Rs 1,000/month for graduation and above. Eligibility, deadline 31 Dec 2026.',
 short='Additional Scholarship ST, A&N', kicker='A&N Administration · ST · Higher studies',
 mono='TW', prov_short='Directorate of Tribal Welfare', prov_long='Directorate of Tribal Welfare, Andaman and Nicobar Administration',
 h1='Grant of Additional Scholarship to ST Students for Higher Studies, Andaman and Nicobar 2026–27',
 sub='Rs 1,000 a month on top of other support — for ST students of the islands pursuing graduation and above, anywhere in India.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Rs 1,000 / month<small>10 months per session</small>'),
              ('Who can apply','ST students<small>A&N domicile; Class 12+</small>'),
              ('Level','Graduation and above<small>Any recognised institution in India</small>'),
              ('Deadline','31 Dec 2026<small>Via NSP</small>'),
              ('Tenure','Till course completion<small>Subject to conduct & attendance</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Grant of Additional Scholarship to ST Students for Higher Studies, Andaman and Nicobar 2026–27</strong>, implemented by the <strong>Directorate of Tribal Welfare, Andaman and Nicobar Administration</strong> under the UT Plan, gives <strong>additional financial assistance of Rs 1,000 per month</strong> to <strong>ST students of the islands pursuing higher education after Class 12</strong> — in colleges and universities <strong>anywhere in India</strong> — as an incentive to supplement the cost of their education.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Belong to the <strong>Scheduled Tribes as notified for the Andaman and Nicobar Islands</strong> and be a <strong>domicile of the islands</strong>.</li>
        <li>Have passed <strong>Senior Secondary (10+2)</strong> from a recognised board, and be a <strong>full-time student pursuing higher studies</strong> at a government-recognised institution (AICTE/UGC-approved or equivalent) — graduate degrees, postgraduate courses, CA/CS/ICWA, M.Phil, PhD, postdoctoral programmes, professional courses in medicine, engineering, management, law, pharmacy, nursing and more.</li>
        <li><strong>Class 11–12 students are not eligible</strong> (this is a post-matric scheme) — though professional/technical courses taken after Class 10 count as post-matric.</li>
        <li><strong>PG medicine students are eligible</strong> provided they are not allowed to practise during the course.</li>
        <li>Not eligible: students repeating the <strong>same stage of education in a different subject</strong> (e.g. B.Sc. after B.A.), or pursuing a second professional course after completing one.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 1,000 per month</strong>, payable for <strong>ten months in an academic session</strong>.</li>
        <li>Released <strong>directly to the beneficiary's bank account</strong> by the Directorate of Tribal Welfare.</li>
        <li><strong>Tenable till course completion</strong>, subject to good conduct and regular attendance certified by the head of the institution.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Domicile certificate (Andaman and Nicobar Islands)</li><li>ST (caste) certificate</li>
        <li>Income certificate</li><li>Self-attested copies of Class 10 / 12 / degree certificates</li>
        <li>Front page of savings bank account passbook</li><li>Passport-size photograph with signature</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the National Scholarship Portal</strong>scholarships.gov.in</li>
        <li><strong>Complete One-Time Registration (OTR)</strong>With mobile OTP and Aadhaar eKYC.</li>
        <li><strong>Fill and submit the application</strong>Fill details carefully — no changes after submission; multiple applications lead to disqualification. Before <strong>31 December 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the scholarship?","Rs 1,000 per month, paid for ten months in an academic session, directly to your bank account."),
 ("Who can apply?","ST students domiciled in the Andaman and Nicobar Islands who have passed Class 12 and are pursuing full-time higher studies at a recognised institution anywhere in India."),
 ("Can I apply if I'm in Class 11 or 12?","No — this scheme is for post-matric/higher studies only."),
 ("Is it renewable?","Yes — tenable till course completion, subject to good conduct, regular attendance and passing each year."),
]),
 verify='Verified 16 Oct 2026 via the B4S 2026-27 A&N listing (31 Dec 2026; Rs 1,000/month for 10 months; ST; A&N domicile; Class 12+; full-time; NSP/OTR route; direct release by Directorate of Tribal Welfare) and the myScheme scheme data (same amount; Directorate of Tribal Welfare, A&N Administration; eligibility terms).',
 offlinks=[('National Scholarship Portal','https://scholarships.gov.in/')],
 related_titles=['umbrella-tripura','umbrella-megh','nfsc'],
),

dict(
 slug='iiser-berhampur-pdrf-2025-26',
 title='IISER Berhampur Post-Doctoral Research Fellowship (PDRF) 2025-26 | StudyDesk Scholarships',
 meta='IISER Berhampur PDRF 2025-26: up to Rs 67,000/month + HRA for PhD holders. Departments: Biological, Chemical, Mathematical, Physical, Earth & CS. Deadline 31 Dec 2026.',
 short='IISER Berhampur PDRF', kicker='IISER Berhampur · PhD · Fellowship',
 mono='IISER', prov_short='IISER Berhampur', prov_long='Indian Institute of Science Education and Research, Berhampur (Odisha)',
 h1='IISER Berhampur Post-Doctoral Research Fellowship (PDRF) 2025–26',
 sub='Up to Rs 67,000 a month plus HRA — post-doctoral research across six science departments at IISER Berhampur.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Up to Rs 67,000 / month<small>+ HRA</small>'),
              ('Who can apply','PhD holders<small>Indian or foreign nationals; below 35</small>'),
              ('Departments','6 science departments<small>Bio, Chem, Maths, Physics, Earth, CS</small>'),
              ('Deadline','31 Dec 2026<small>Institute scheme</small>'),
              ('Tenure','1 year<small>Extendable to 3 on review</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>IISER Berhampur Post-Doctoral Research Fellowship (PDRF) 2025–26</strong>, from the <strong>Indian Institute of Science Education and Research, Berhampur</strong> — an Institute of National Importance — funds <strong>post-doctoral research</strong> in the Departments of <strong>Biological Sciences, Chemical Sciences, Mathematical Sciences, Physical Sciences, Earth &amp; Environmental Sciences and Computer Science</strong>. The initial award is for <strong>one year</strong>, extendable to a <strong>maximum of three years</strong> after annual performance review.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian or foreign national.</strong></li>
        <li><strong>Below 35 years</strong> of age on the date of application.</li>
        <li>Hold a <strong>PhD degree in the respective field</strong>, with a <strong>good academic record</strong>.</li>
        <li><strong>Research experience after the PhD</strong> as per the institute's prevailing guidelines (published listings cite five years of post-PhD experience for PDRF; thesis-submitted candidates may apply as <strong>Research Associates</strong>).</li>
      </ul>
      <div class="honest-note"><strong>Project-specific ads differ:</strong> IISER Berhampur also advertises PDRF positions tied to individual funded projects (with their own PIs and deadlines). This listing covers the <strong>institute's general PDRF scheme</strong> — check the official jobs page for the current advertisement.</div>
      <h2 id="benefits">Benefits</h2>
      <table><tr><th>Category</th><th>Fellowship</th></tr>
      <tr><td>Research Associate (thesis submitted, PhD awaited)</td><td>Rs 42,000/month + HRA</td></tr>
      <tr><td>PDRF (up to 1 year post-PhD experience)</td><td>Rs 58,000/month + HRA</td></tr>
      <tr><td>PDRF (1–2 years experience)</td><td>Rs 61,000/month + HRA</td></tr>
      <tr><td>PDRF (over 2 years experience)</td><td>Rs 67,000/month + HRA</td></tr></table>
      <ul>
        <li><strong>Campus accommodation</strong> as per institute rules (HRA if unavailable).</li>
        <li><strong>30 days annual leave</strong> plus on-duty leave for conferences/workshops; <strong>15 days medical leave</strong> per year.</li>
        <li><strong>OPD medical consultation</strong> as per institute norms (medical insurance of at least Rs 1,00,000 required).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Detailed <strong>CV</strong></li><li><strong>Research statement</strong> (background and motivation)</li>
        <li><strong>Marksheet</strong> of the last examination</li><li><strong>Resident proof</strong></li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the official advertisement</strong>On iiserbpr.ac.in (jobs / fellowship section) for the current PDRF call.</li>
        <li><strong>Prepare your application</strong>CV plus research statement, in the format the advertisement asks for.</li>
        <li><strong>Submit before 31 December 2026</strong>Shortlisted candidates are notified by email; interviews are held periodically through the year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the fellowship?","Rs 42,000/month as a Research Associate up to Rs 67,000/month as a PDRF with over two years' experience, plus HRA."),
 ("Can foreign nationals apply?","Yes — the fellowship is open to Indian and foreign nationals."),
 ("What is the age limit?","Preferably below 35 years on the date of application."),
 ("How long is the tenure?","One year initially, extendable up to three years on annual performance review."),
]),
 verify='Verified 16 Oct 2026 via the B4S 2025-26 listing (31 Dec 2026; Rs 42,000–67,000/month + HRA by category; below 35; PhD; 6 departments; 1-year tenure extendable to 3) and Scholarlify (same structure), against the official iiserbpr.ac.in PDRF advertisement (HRA rules; age below 35; accommodation; leave and medical terms).',
 offlinks=[('IISER Berhampur (official)','https://www.iiserbpr.ac.in/')],
 related_titles=['nasa-hubble','icar-jrf','nfsc'],
),

dict(
 slug='malabar-charitable-trust-scholarship-2026',
 title='Malabar Charitable Trust Scholarship 2026 | StudyDesk Scholarships',
 meta='Malabar Charitable Trust Scholarship 2026: up to Rs 10,000 one-time for girl students in higher secondary at government schools. Deadline 31 Dec 2026.',
 short='Malabar Charitable Trust Scholarship', kicker='Malabar Charitable Trust · Girls · Class 11–12',
 mono='MCT', prov_short='Malabar Charitable Trust', prov_long='Malabar Charitable Trust (Malabar Group)',
 h1='Malabar Charitable Trust Scholarship 2026',
 sub='Up to Rs 10,000 one-time — for girl students in higher secondary at government schools, running since 2007.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Up to Rs 10,000<small>One-time; score-based</small>'),
              ('Who can apply','Girl students<small>50%+ in Class 10; govt. schools</small>'),
              ('Level','Higher secondary<small>Full-time; not distance learning</small>'),
              ('Deadline','31 Dec 2026<small>Check current cycle</small>'),
              ('Since','2007<small>1.45 lakh+ girls supported</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Malabar Charitable Trust Scholarship 2026</strong> — the trust's <strong>"Empowering Education: Empowering Womenhood"</strong> scheme, running since <strong>2007</strong> — supports <strong>girl students from government schools</strong> to reduce dropouts and keep them studying through higher secondary. The trust reports <strong>over 1.45 lakh girl students supported across 18 states and 3 UTs</strong>, with more than Rs 103 crore disbursed to date.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Female student.</strong></li>
        <li><strong>Minimum 50% marks in the Class 10 examination.</strong></li>
        <li><strong>Pursuing higher secondary studies</strong> in a <strong>government school</strong> (aided schools in selected states) — <strong>full-time, regular programme</strong>. Distance learning and correspondence students are not eligible.</li>
        <li><strong>Preference</strong> to students with the <strong>highest marks and the lowest family income</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>One-time financial assistance up to Rs 10,000</strong>, graded on the selection score: <strong>60–100 marks → Rs 10,000; 40–55 → Rs 8,000; 25–35 → Rs 6,000</strong>.</li>
        <li>Scoring is on <strong>qualifying-exam marks, family income, parental support, disability and chronic illness</strong> in the family.</li>
        <li>Disbursed by <strong>RTGS directly to the student's bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Class 10 certificate and marksheet (Class 11 marksheet for Class 12 students)</li>
        <li>Applicant's photograph</li><li>Bank passbook</li>
        <li>Declaration form / bonafide certificate</li><li>Proof of family income</li>
        <li>Disability certificate / death certificate (if applicable)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check eligibility online</strong>Use the eligibility checker on the trust's official website.</li>
        <li><strong>Register and fill the online form</strong>Upload scanned documents.</li>
        <li><strong>Submit hard copies</strong>To the nearest Malabar Gold &amp; Diamonds showroom <strong>within 3 days</strong> of online submission.</li>
        <li><strong>Await verification and selection</strong>Results are notified by SMS; the amount is disbursed by RTGS.</li>
      </ol>
      <div class="honest-note"><strong>Cycle dates vary:</strong> different listings cite different deadlines for this scheme's cycles. Confirm the <strong>current cycle's last date on the official Malabar Charitable Trust website</strong> before applying.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much will I receive?","Up to Rs 10,000 one-time, graded by your selection score (Rs 6,000–10,000)."),
 ("Who can apply?","Girl students with 50%+ in Class 10, studying higher secondary full-time in government schools."),
 ("Can distance-learning students apply?","No — only full-time, regular programmes."),
 ("How is the money paid?","By RTGS directly to the selected student's bank account."),
]),
 verify='Verified 16 Oct 2026 via the B4S 2026 listing (31 Dec 2026; up to Rs 10,000 one-time; girls; 50%+ in Class 10; higher secondary in government schools; score-based amounts) and Careers360 (same scheme, selection criteria and amount slabs) — with an honest note that cycle deadlines vary across listings.',
 offlinks=[('Malabar Group (official)','https://www.malabargroup.com/')],
 related_titles=['vidyadhan','muskaan','wings'],
),

dict(
 slug='ramanujan-fellowship-2025-anrf',
 title='Ramanujan Fellowship 2025 | StudyDesk Scholarships',
 meta='Ramanujan Fellowship 2025 (ANRF): Rs 1.35 lakh/month + Rs 7 lakh/year research grant for Indian-origin scientists abroad returning to India. 5 years. Deadline 31 Dec 2026.',
 short='Ramanujan Fellowship 2025', kicker='ANRF · Fellowship · Research',
 mono='ANRF', prov_short='Anusandhan National Research Foundation', prov_long='Anusandhan National Research Foundation (ANRF), Govt. of India',
 h1='Ramanujan Fellowship 2025',
 sub='Rs 1.35 lakh a month plus a Rs 7 lakh yearly research grant — for brilliant Indian-origin scientists abroad returning to India.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Rs 1.35 lakh / month<small>+ Rs 7L/yr research grant</small>'),
              ('Who can apply','Indian-origin scientists abroad<small>Below 40; nomination-based</small>'),
              ('Duration','5 years<small>Non-extendable</small>'),
              ('Deadline','31 Dec 2026<small>Nominations via ANRF portal</small>'),
              ('Host','Any Indian institution<small>Not the PhD institution</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Ramanujan Fellowship 2025</strong>, from the <strong>Anusandhan National Research Foundation (ANRF), Government of India</strong>, is a prestigious, <strong>scientist-specific fellowship</strong> meant to attract <strong>brilliant Indian and Indian-origin scientists and engineers working abroad</strong> to return to India for cutting-edge research. Fellows can work at <strong>any scientific institution or university in India</strong> and remain eligible for regular extramural research grants. It is <strong>highly selective</strong> and aimed at reversing brain drain.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian citizen or person of Indian origin</strong>, working <strong>abroad</strong> at the time of nomination.</li>
        <li><strong>Below 40 years</strong> of age.</li>
        <li><strong>Higher degree or equivalent</strong>: PhD in Science or Engineering, Master's in Engineering/Technology, or MD in Medicine — with <strong>adequate professional experience</strong> and a <strong>proven, outstanding research track record</strong> (publications and recognition).</li>
        <li><strong>Not holding any permanent, tenure-track or contractual position</strong> in any Indian institute/university.</li>
        <li>Must be <strong>nominated and hosted by an eligible Indian institution</strong> — the host <strong>cannot be the institute where the nominee earned the PhD</strong>, and PhD guides cannot nominate.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Consolidated fellowship of Rs 1,35,000 per month</strong> (inclusive of HRA).</li>
        <li><strong>Research grant of Rs 7,00,000 per year</strong> (consumables, travel, research personnel, contingencies).</li>
        <li><strong>Rs 60,000 per year</strong> as overhead charges to the host institution.</li>
        <li><strong>Five years, non-extendable.</strong></li>
        <li>Eligible for <strong>regular extramural research grants</strong> from S&amp;T agencies of the Government of India.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Nomination letter</strong> (on official letterhead, duly signed and stamped)</li>
        <li><strong>Curriculum Vitae</strong> of the nominee</li>
        <li><strong>Research proposal</strong> in the prescribed format</li>
        <li>Plagiarism undertaking (as per prescribed format)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on the ANRF online portal</strong>anrfonline.in — complete your profile.</li>
        <li><strong>Select "Ramanujan Fellowship"</strong>Fill the nomination form and upload the research proposal.</li>
        <li><strong>Submit to your nominator</strong>The nominator reviews and forwards the nomination to ANRF. This is a <strong>nomination-based</strong> fellowship — you cannot apply directly without a nominator.</li>
      </ol>
      <div class="honest-note"><strong>Nomination, not application:</strong> you need an eligible Indian institution to nominate and host you. Start the conversation with your prospective host department well before the deadline.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the fellowship?","Rs 1,35,000/month consolidated (including HRA), plus Rs 7 lakh/year research grant and Rs 60,000/year institutional overhead — for 5 years."),
 ("Who can be nominated?","Indian/Indian-origin scientists and engineers working abroad, below 40, with an outstanding research record, holding no position in India."),
 ("Can I apply directly?","No — nominations go through the ANRF portal via an eligible nominating institution."),
 ("How long does it last?","Five years, non-extendable."),
]),
 verify='Verified 16 Oct 2026 via the B4S 2025 listing (31 Dec 2026; Rs 1,35,000/month incl. HRA; Rs 7L/yr grant; Rs 60K overhead; below 40; abroad; nomination-based) and the India Science & Technology (ISTI) portal (same amounts; 5 years; 31 Dec 2026 last date).',
 offlinks=[('ANRF Ramanujan Fellowship (official)','https://anrfonline.in/ANRF/Ramanujan_fellowship?HomePage=New')],
 related_titles=['nasa-hubble','wb-gaf','icar-jrf'],
),

dict(
 slug='sof-dsas-defence-services-scholarship-2026-27',
 title='SOF Defence Services Academic Excellence Scholarship (DSAS) 2026-27 | StudyDesk Scholarships',
 meta='SOF DSAS 2026-27: Rs 5,000 + certificate for 260 students of defence/internal security families in Classes 1–10. School-nominated. Deadline 31 Dec 2026.',
 short='SOF DSAS 2026-27', kicker='SOF · School · Defence families',
 mono='SOF', prov_short='Science Olympiad Foundation', prov_long='Science Olympiad Foundation (SOF), Gurugram',
 h1='SOF Defence Services Academic Excellence Scholarship (DSAS) 2026–27',
 sub='Rs 5,000 and a certificate — for 260 academically brilliant students from defence and internal security families.',
 dpill='76 days to go', dl_long='31 Dec 2026',
 facts=facts([('Award','Rs 5,000<small>One-time + certificate</small>'),
              ('Who can apply','Classes 1–10<small>Defence / internal security families</small>'),
              ('Seats','260 students<small>School-nominated</small>'),
              ('Deadline','31 Dec 2026<small>Offline via school</small>'),
              ('Mode','Offline<small>Schools send nominations</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>SOF Defence Services Academic Excellence Scholarship (DSAS) 2026–27</strong>, from the <strong>Science Olympiad Foundation (SOF)</strong>, recognises the academic achievements of students from <strong>Defence Services and Internal Security families</strong> — families SOF notes make monumental contributions to India's safety and security. <strong>Up to 260 academically brilliant students</strong> receive a <strong>cash award of Rs 5,000 each plus a certificate</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Resident of India.</strong></li>
        <li>Studying in <strong>Classes 1 to 10</strong> in a recognised school/institution.</li>
        <li>Belong to a <strong>serving or retired Defence Services / Internal Security Services family</strong>.</li>
        <li><strong>Nominated by the school</strong> — the selection committee evaluates applications sent by schools; winners are informed individually through their schools.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>One-time cash award of Rs 5,000</strong> per selected student.</li>
        <li><strong>Certificate</strong> of academic excellence.</li>
        <li>Amount deposited in the <strong>student's bank account</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Report card of the previous year</strong>, duly certified by the Principal</li>
        <li><strong>Recommendation letter</strong> signed by the headmaster/headmistress/principal (in the specified format)</li>
        <li><strong>Academic transcripts</strong>, including marksheets and certificates</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Contact your school</strong>Students cannot apply directly — ask your school to nominate you.</li>
        <li><strong>School downloads the nomination form</strong>From the official SOF website (sofworld.org).</li>
        <li><strong>School sends the signed recommendation</strong>To: Science Olympiad Foundation, 1st Floor, Plot No. 99, Sector 44, Gurugram, Haryana 122003 — before <strong>31 December 2026</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Students can't apply directly.</strong> Talk to your principal or class teacher early — your school must send the nomination.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the award?","Rs 5,000 one-time cash plus a certificate, for 260 students."),
 ("Who is eligible?","Indian residents in Classes 1–10 from serving or retired Defence Services / Internal Security Services families."),
 ("Can students apply directly?","No — schools send nominations; students should contact their school."),
 ("What is the deadline?","31 December 2026; the amount is released to winners' bank accounts."),
]),
 verify='Verified 16 Oct 2026 via the official sofworld.org DSAS page (2026-27 launch; 260 students; Rs 5,000 + certificate; school nominations) and the B4S 2026-27 listing (31 Dec 2026; Classes 1–10; defence/internal security families; offline via school; Gurugram address).',
 offlinks=[('SOF DSAS (official)','https://sofworld.org/sof-defence-services-academician-scholarship-dsas')],
 related_titles=['pathani','muskaan','satya'],
),

dict(
 slug='aalto-university-scholarships-2027-finland',
 title='Aalto University Scholarships 2027 in Finland | StudyDesk Scholarships',
 meta='Aalto University Scholarships 2027: up to 100% tuition fee waiver for non-EU/EEA Master’s and Bachelor’s students. Apply 7 Dec 2026 – 5 Jan 2027.',
 short='Aalto University Scholarships 2027', kicker='Finland · UG/PG · International',
 mono='A', prov_short='Aalto University', prov_long='Aalto University, Espoo, Finland',
 h1='Aalto University Scholarships 2027 in Finland',
 sub='Up to 100% tuition fee waiver — merit scholarships for non-EU/EEA students, awarded automatically with admission.',
 dpill='81 days to go', dl_long='5 Jan 2027',
 facts=facts([('Award','100% tuition waiver<small>Or 50%; living costs excluded</small>'),
              ('Who can apply','Non-EU/EEA students<small>Merit-based; fee-paying</small>'),
              ('Level',"Bachelor's + Master's<small>English-taught programmes</small>"),
              ('Deadline','5 Jan 2027<small>Master\u2019s; 3 PM Finnish time</small>'),
              ('Application','No separate form<small>Awarded via admission application</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Aalto University</strong> — Finland's leading university for technology, business, art and design, based in Espoo near Helsinki — offers the <strong>Aalto University Excellence Scholarship</strong> to top applicants liable for tuition fees. It is a <strong>tuition fee waiver of up to 100%</strong> (some awards are 50%), valid for the <strong>normal length of the degree</strong> — two years for a Master's, three for a Bachelor's. There is <strong>no separate scholarship application</strong>: you are considered automatically when you apply for admission.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Citizen of a country <strong>outside the EU/EEA</strong> (or Switzerland) — i.e. <strong>liable to pay tuition fees</strong>.</li>
        <li>Applying to an <strong>English-taught Bachelor's or Master's programme</strong> at Aalto for the <strong>autumn 2027 intake</strong>.</li>
        <li>Hold a <strong>Bachelor's degree equivalent to 180 ECTS credits</strong> (three years of full-time study), or be completing it by <strong>31 July 2027</strong>.</li>
        <li><strong>Strong academic record</strong> — the scholarship is merit-based, awarded to top applicants.</li>
        <li>Meet the programme's <strong>English language proficiency</strong> requirements (test scores such as IELTS/TOEFL or GMAT/GRE where the programme requires).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to 100% tuition fee waiver</strong> for the full normal duration of the programme. Tuition without the waiver is about <strong>€12,000–20,000 per year</strong> depending on the programme.</li>
        <li><strong>Not covered: living costs.</strong> For the Finnish residence permit you must show you can support yourself.</li>
        <li>Continuation requires <strong>full-time study and steady progress</strong>, checked each spring.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Passport</li><li>Bachelor's degree certificate and <strong>academic transcripts</strong></li>
        <li><strong>Proof of English proficiency</strong></li><li>CV</li><li><strong>Motivation letter</strong></li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to Aalto</strong>Through the university's online application — the scholarship needs no separate form.</li>
        <li><strong>Master's programmes: apply 7 December 2026 – 5 January 2027</strong> (by 15:00 Finnish time); supporting documents due <strong>12 January 2027</strong>. Bachelor's programmes: <strong>7–22 January 2027</strong>.</li>
        <li><strong>Scholarship decisions arrive with admission results</strong></li>
      </ol>
      <div class="honest-note"><strong>Tuition only.</strong> The waiver never covers living costs — budget for accommodation, food, travel and the residence-permit funds requirement before you apply.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the waiver?","Up to 100% of tuition (some awards are 50%), for the normal length of the degree."),
 ("Do I apply separately for the scholarship?","No — you are automatically considered when you apply for admission."),
 ("What are the deadlines?","Master's: 7 Dec 2026 – 5 Jan 2027 (documents by 12 Jan 2027). Bachelor's: 7–22 Jan 2027."),
 ("Does it cover living expenses?","No — living costs and the residence-permit funds requirement are on you."),
]),
 verify='Verified 16 Oct 2026 via Scholar Fahad, AfterSchoolAfrica and Pontly Africa 2027 listings (up to 100% tuition waiver; non-EU/EEA fee-paying; merit-based; no separate application; Master\u2019s window 7 Dec 2026 – 5 Jan 2027, documents by 12 Jan 2027; Bachelor\u2019s 7–22 Jan 2027; tuition \u20ac12–20K/year; living costs excluded).',
 offlinks=[('Aalto University admissions (official)','https://www.aalto.fi/en/admission-services')],
 related_titles=['griffith-vc','hanns-seidel','epfl-summer'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')

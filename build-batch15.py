#!/usr/bin/env python3
"""Batch 15 (cron run 15): 5 verified international articles. Verified 17 Oct 2026.

Notes:
- BCDI 2030: real programme, funded by Global Affairs Canada (Government of
  Canada), co-administered by Colleges and Institutes Canada (CICan) and
  Universities Canada. Fully funded (tuition, monthly living allowance,
  return airfare, health insurance, books/materials). NO single program-wide
  deadline - each approved project sets its own; students apply through their
  home/partner institution's project call, not a central portal. 26 partner
  countries (mostly francophone Africa); must return home; must never have
  held a Canadian-government-funded scholarship or applied for Canadian PR.
- MSU out-of-state: MISSISSIPPI State University (Starkville, MS) - NOT
  Michigan State. Automatically awarded on admission to first-time freshmen
  on 9th-11th grade GPA + ACT/SAT (superscores accepted, tests through the
  Feb date of senior year). Official 2026-27 figures used; no separate
  scholarship deadline. Additional scholarships need the General Scholarship
  Application (priority 1 Dec). 34+ ACT gets a one-year housing award.
- Said Foundation 2027: fully funded one-year master's at partner UK
  universities for Syrian/Jordanian/Lebanese/Palestinian nationals resident
  in those countries (displaced Syrians excepted). Deadline 30 Oct 2026,
  5:00 PM UK time (opened 1 Sep 2026). Covers tuition, full living costs,
  arrival allowance, visa fees, IHS, one return flight; ~20-30 awards/yr.
  Official partner page (Imperial) used as anchor source.
- UM Bright 2027: real UM scheme - PhD by research only; RM3,500/month x 42
  months + full tuition waiver for 7 semesters; age <=30; Bachelor CGPA >3.70
  AND Master's (research or mixed-mode) CGPA >=3.70/4.00; IELTS 6.5+/TOEFL
  73-93/CEFR B2 (2-yr validity); deadline varies by thrust area / rolling;
  apply by emailing the compiled PDF to brightscholar@um.edu.my (address as
  published in the official call documents).
- NTU 2027: Master's & PhD at National Taiwan University, Taipei. Round 1:
  5 Nov 2026; Round 2: 19 Jan 2027. No separate scholarship form - tick the
  box in the NTU admission portal. Headline graduate package reported across
  trackers: tuition waiver up to TWD 65,000/semester + TWD 30,000/month
  stipend + one return air ticket (benefits vary by tier - stated as such).
SKIPPED this run (3): YSEALI Academic Fellowship 2027 (deadline 12 Oct 2026
  - deadline passed); World Bank Treasury Summer Internship 2027 (September
  2026 deadline - deadline passed); 'Scholarship Opportunities 2027 | Fully
  Funded Scholarships' (not a real scheme - generic junk topic, unverifiable).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'bcdi2030': dict(mono='BCDI', title='Canadian International Development Scholarships 2030 (BCDI 2030) (Funded)', href='canadian-international-development-scholarships-bcdi-2030.html',
              dpill='No fixed deadline', award='Full tuition + living allowance + return airfare', elig='Nationals of 26 partner countries; nominated through home/partner institution projects; must return home.',
              tags=[("All levels",'blue'),('Canada','teal')]),
 'msu-oos': dict(mono='MSU', title='Mississippi State University Out-of-State Resident Scholarship 2027 (USA)', href='msu-out-of-state-resident-scholarship-2027-usa.html',
              dpill='Automatic on admission', award='$12,000–$24,000/year, renewable 8 semesters', elig='First-time freshmen, non-resident; 9th–11th grade GPA 3.30+; ACT/SAT scores.',
              tags=[('Undergraduate','blue'),('USA','teal')]),
 'said': dict(mono='SF', title='Saïd Foundation Scholarship 2027 in UK (Fully Funded)', href='said-foundation-scholarship-2027-uk.html',
              dpill='13 days to go', award='Full tuition + living costs + flight (one-year master’s)', elig='Syrian, Jordanian, Lebanese or Palestinian nationals resident in those countries; UK 2:1 equivalent.',
              tags=[("Master's",'blue'),('UK','teal')]),
 'um-bright': dict(mono='UM', title='University of Malaya Bright Scholarship 2027 in Malaysia (Fully Funded)', href='university-of-malaya-bright-scholarship-2027-malaysia.html',
              dpill='Rolling deadline', award='RM3,500/month × 42 months + full tuition waiver', elig='PhD by research; age ≤30; Bachelor’s CGPA >3.70; Master’s CGPA ≥3.70; IELTS 6.5+/TOEFL 73–93.',
              tags=[('PhD','blue'),('Malaysia','teal')]),
 'ntu': dict(mono='NTU', title='National Taiwan University Scholarship 2027 in Taiwan (Fully Funded)', href='national-taiwan-university-scholarship-2027-taiwan.html',
              dpill='19 days to go', award='Tuition waiver up to TWD 65,000/sem + TWD 30,000/month', elig='International Master’s/PhD applicants via NTU portal; language requirements apply.',
              tags=[("Master's/PhD",'blue'),('Taiwan','teal')]),
})

ARTICLES = [

# ---------------------------------------------------------------- 1. BCDI 2030
dict(
 slug='canadian-international-development-scholarships-bcdi-2030',
 title='Canadian International Development Scholarships 2030 (BCDI 2030) | StudyDesk Scholarships',
 meta='BCDI 2030: Global Affairs Canada funds fully funded study and training in Canada for students from 26 partner countries. No single deadline — each project sets its own. Eligibility, benefits and how to apply.',
 short='BCDI 2030 Scholarships', kicker='Canada · All levels · Funded by Global Affairs Canada',
 mono='BCDI', prov_short='Global Affairs Canada',
 h1='Canadian International Development Scholarships 2030 (BCDI 2030)',
 sub='BCDI 2030 is Canada’s flagship education-for-development programme: an eight-year, fully funded initiative by Global Affairs Canada that brings students and professionals from 26 partner countries to study and train at Canadian colleges and universities. There is no single application form and no single deadline — awards flow through approved projects run by partner institutions, so you apply through your own university, not a central portal.',
 dpill='No fixed deadline', dl_long='Varies by project (no central program-wide deadline)',
 facts=facts([('Award','Fully funded<small>Full tuition, monthly living allowance, return airfare, health insurance, books and study materials, local transport</small>'),
              ('Who','26 partner countries<small>Benin, Burkina Faso, Cameroon, CAR, Chad, Congo, DR Congo, Egypt, Gabon, Ghana, Guinea-Bissau, Haiti, Ivory Coast, Kenya, Madagascar, Mali, Mauritania, Morocco, Niger, Rwanda, São Tomé and Príncipe, Senegal, South Africa, Tanzania, Togo, Tunisia</small>'),
              ('Levels','Vocational to PhD<small>Short training, undergraduate, master’s, PhD and fellowships — aligned with development priorities like health, climate, agriculture and governance</small>'),
              ('Scale','~600 scholars<small>At least 51% of awards are reserved for women; program runs 2022–2030</small>'),
              ('How to apply','Through your institution<small>Find an approved BCDI 2030 project at your home or a partner university and follow that project’s own call — there is no central student application</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Canadian International Development Scholarships 2030 (BCDI 2030)</strong> is a Canadian government programme designed to use higher education as a lever for development. It is funded by <strong>Global Affairs Canada</strong> and co-administered by <strong>Colleges and Institutes Canada (CICan)</strong> and <strong>Universities Canada (UnivCan)</strong> — the two national bodies representing Canadian colleges and universities. The programme supports students, researchers and professionals from <strong>26 eligible partner countries</strong> across Africa, Latin America, the Caribbean and small island states, funding study and training at Canadian institutions in fields tied to sustainable development: STEM, health sciences, agriculture and food security, climate action, governance, education and more.</p>
      <p><strong>The defining feature of BCDI 2030 is that it has no central application.</strong> Canadian institutions design projects with partners in eligible countries, each approved project publishes its own call, and candidates are nominated by their institutions. Around <strong>600 scholars</strong> will benefit over the programme’s life, with at least <strong>51% of awards reserved for women</strong>. Application fees do not exist anywhere in the process — any request for payment is a sign of fraud.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Nationality:</strong> be a citizen of one of the 26 eligible partner countries (Benin, Burkina Faso, Cameroon, Central African Republic, Chad, Congo, DR Congo, Egypt, Gabon, Ghana, Guinea-Bissau, Haiti, Ivory Coast, Kenya, Madagascar, Mali, Mauritania, Morocco, Niger, Rwanda, São Tomé and Príncipe, Senegal, South Africa, Tanzania, Togo, Tunisia).</li>
        <li><strong>Institutional affiliation:</strong> be affiliated — as a student, teaching/research staff or administrator — with a higher-education institution that is eligible for, or part of, an approved BCDI 2030 project; candidates can also be recruited externally through a project’s own selection.</li>
        <li><strong>Intent to return:</strong> your primary objective must be to study or train in Canada and then <strong>return to your home country</strong> — the programme is explicitly about building change-makers at home, not immigration.</li>
        <li><strong>Clean slate with Canadian funding:</strong> you must not have previously participated in a Canadian-government-funded scholarship programme, must not already be enrolled at a Canadian higher-education institution, and must never have applied for Canadian permanent residence or citizenship.</li>
        <li><strong>Project-specific rules:</strong> eligible levels, fields and academic requirements vary by individual project — always check the specific call.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for the duration of the programme at the participating Canadian institution.</li>
        <li><strong>Monthly living allowance</strong> covering accommodation, meals and daily expenses.</li>
        <li><strong>Round-trip economy airfare</strong> between your home country and Canada.</li>
        <li><strong>Health insurance</strong> for the duration of the stay, plus immigration and medical-examination fees.</li>
        <li><strong>Study costs:</strong> mandatory books, installation and clothing allowances, and local transportation.</li>
        <li>Access to labs, libraries, mentorship and professional-development activities, depending on the project.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>No program-wide document list is published — “not published in the official notification”. Each project call publishes its own requirements. Trackers consistently report that candidates should have recommendation letters, proof of achievements or project work, and academic records ready; English test requirements vary by project (several calls do not require IELTS).</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find an active project:</strong> check the official BCDI 2030 project listings and the announcements at universities in your country — for example, the University of Limpopo’s call for a January 2027 research stay at Toronto Metropolitan University.</li>
        <li><strong>Contact your institution:</strong> apply through your home or the partner university running the project, following that call’s own process and deadlines.</li>
        <li><strong>Prepare a strong file:</strong> academic record, recommendation letters, evidence of community involvement or development work — selection weighs academic merit and project relevance.</li>
        <li><strong>Selection and nomination:</strong> your institution’s selection committee nominates candidates, reviewed jointly with the Canadian partner. There is no fee at any stage.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there one deadline for BCDI 2030?","No. There is no single program-wide application deadline or timezone. Each approved scholarship project sets its own application period and deadline, so you must watch the individual project calls."),
 ("Can I apply directly to the Canadian government?","No. Students do not apply centrally — you apply through the home or partner institution that is running an approved BCDI 2030 project, and institutions nominate their selected candidates."),
 ("Is IELTS required?","Not necessarily. Language requirements vary by project, and several published calls do not require IELTS. Check the specific project call rather than assuming a test is mandatory."),
 ("Do I have to pay anything to apply?","No. There is no application fee, and candidates are never asked to pay to apply, receive the scholarship, or access support. Payment requests are a fraud signal."),
 ("Which countries are eligible?","26 partner countries: Benin, Burkina Faso, Cameroon, Central African Republic, Chad, Congo, DR Congo, Egypt, Gabon, Ghana, Guinea-Bissau, Haiti, Ivory Coast, Kenya, Madagascar, Mali, Mauritania, Morocco, Niger, Rwanda, São Tomé and Príncipe, Senegal, South Africa, Tanzania, Togo and Tunisia."),
]),
 offlinks=[('BCDI 2030 — McMaster Global (programme overview, funder and co-administrators)','https://global.mcmaster.ca/canadian-international-development-scholarships-2030-bcdi-2030/'),
           ('BCDI 2030 at University of Alberta — eligibility and benefits','https://www.9scholarships.com/2025/12/bcdi-2030-scholarship-at-university-of-alberta-canada/'),
           ('BCDI 2030 overview — eligible countries and funding type','https://edugist.org/canadian-international-development-scholarships-bcdi-2030/')],
 related_titles=['oise-toronto','nasa-hubble','bloomberg-harvard'],
 verify='Verified 17 Oct 2026 via McMaster University’s official Global page (funded by Global Affairs Canada; co-administered by CICan and Universities Canada; 2026 Egypt partnership call deadline 30 Oct 2026), University of Limpopo’s official BCDI 2030 research-stay call (funded, benefits list), and 9scholarships/edugist/scholarshipwire trackers (26-country list, ~600 scholars with ≥51% women, no single program-wide deadline, affiliation and return-home rules). Document lists are project-specific and not stated program-wide.'),

# ---------------------------------------------------------------- 2. MSU out-of-state
dict(
 slug='msu-out-of-state-resident-scholarship-2027-usa',
 title='Mississippi State University Out-of-State Resident Scholarship 2027 (USA) | StudyDesk Scholarships',
 meta='MSU out-of-state resident scholarships: automatically awarded on admission — $12,000 to $24,000/year based on GPA and ACT/SAT, renewable for 8 semesters. No separate application. Eligibility and figures.',
 short='MSU Out-of-State Scholarship', kicker='USA · Undergraduate · Automatic on admission',
 mono='MSU', prov_short='Mississippi State University',
 h1='Mississippi State University Out-of-State Resident Scholarship 2027 in USA',
 sub='Mississippi State University hands its out-of-state academic scholarships to freshmen automatically — no separate form, no essay. If your 9th–11th grade GPA and ACT/SAT scores clear the published bands, the award (worth $12,000 to $24,000 a year for the 2026–27 cycle) lands with your admission, and it renews for up to eight semesters as long as your MSU GPA holds up.',
 dpill='Automatic on admission', dl_long='No separate scholarship deadline — automatic with admission',
 facts=facts([('Award','$12,000–$24,000/year (2026–27)<small>3.30–3.59 GPA: $12,000 ($17,000 with 31 ACT/1390 SAT+); 3.60–4.09: $16,000 ($21,000); 4.10+: $19,000 ($24,000). Amounts combine institutional and private aid</small>'),
              ('Who','Entering first-time freshmen<small>Classified as non-residents for tuition purposes; awarded on 9th–11th grade GPA and official ACT/SAT scores (superscoring accepted)</small>'),
              ('Renewal','Up to 8 semesters<small>Renewed each fall and spring based on overall MSU GPA; combined awards cannot exceed the non-resident portion of tuition</small>'),
              ('Bonus','Housing award<small>Students with a 34+ ACT (or SAT equivalent) also receive a one-year, on-campus housing scholarship</small>'),
              ('How to apply','No separate form<small>Apply for admission to MSU — the scholarship is automatic. For additional scholarships, file the General Scholarship Application (priority: 1 December)</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Mississippi State University (MSU)</strong> in Starkville, Mississippi — not to be confused with Michigan State, which shares the initials — awards its <strong>Out-of-State Resident Scholarships</strong> to entering first-time freshmen <strong>automatically on admission</strong>. There is no separate scholarship application, no essay and no interview: the university reads your high-school GPA (grades 9–11) and your official ACT/SAT scores and slots you into a published award band. The published figures for the 2026–27 cycle run from <strong>$12,000 a year</strong> (GPA 3.30–3.59) to <strong>$24,000 a year</strong> (GPA 4.10+ with a 31 ACT/1390 SAT or above). The award renews each fall and spring for <strong>up to eight semesters</strong> based on your overall MSU GPA.</p>
      <p>The university also layers extra value on top: students scoring <strong>34+ on the ACT</strong> (or the SAT equivalent) receive a <strong>one-year, on-campus housing scholarship</strong>, and a separate <strong>Alumni Non-Resident Tuition Scholarship</strong> (up to $5,000/year) exists for non-resident children of MSU alumni. The figures are subject to change — always check the current official schedule before planning.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Entering first-time freshman</strong> at Mississippi State University, classified as a <strong>non-resident</strong> for tuition purposes.</li>
        <li><strong>Minimum 3.30 GPA</strong> on the 9th–11th grade high-school record (4.0 scale).</li>
        <li><strong>Official ACT/SAT scores</strong> sent directly to MSU — <strong>superscoring is accepted</strong>, and the university accepts scores taken through the <strong>February test date</strong> of your senior year.</li>
        <li>Higher bands: 31 ACT/1390 SAT and above unlock the top column of each GPA band.</li>
        <li>Enrol as a full-time student in the semester the award is received; renewal depends on maintaining continuous full-time enrolment and the required MSU GPA.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$12,000–$24,000 per year</strong> (2026–27 figures) applied against out-of-state tuition — renewable for up to 8 semesters.</li>
        <li><strong>One-year on-campus housing scholarship</strong> for 34+ ACT (or SAT-equivalent) scorers, covering the student’s share of a double-occupancy room.</li>
        <li>Can be combined with some other MSU scholarships and aid, subject to the cap on the non-resident tuition portion.</li>
        <li><strong>Alumni track:</strong> non-resident children of MSU alumni can receive up to $5,000/year through the Alumni Non-Resident Tuition Scholarship.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>No separate scholarship documents — the award is automatic. You only need what MSU admission itself requires: official high-school transcripts and official ACT/SAT score reports sent directly to the university. For the alumni track, parent alumni status must be verified by the MSU Office of the Registrar.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission</strong> to Mississippi State University as a first-time freshman — this single step automatically puts you in the scholarship pool.</li>
        <li><strong>Send official test scores</strong> directly to MSU (scores through the February date of your senior year count; superscores accepted).</li>
        <li><strong>For extra awards:</strong> submit the <strong>General Scholarship Application</strong> at my.msstate.edu — the priority date for maximum consideration was <strong>1 December</strong> for the 2026 cycle, so check the current date early.</li>
        <li><strong>Alumni families:</strong> have your parent’s MSU alumni status verified through the Office of the Registrar for the alumni non-resident award.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate scholarship application?","No. The Freshman Academic Scholarships for non-residents are automatically awarded on admission based on your GPA and test scores. Only the additional (departmental, leadership, private) scholarships need the General Scholarship Application."),
 ("Which MSU is this — Michigan or Mississippi?","Mississippi State University in Starkville, Mississippi. Michigan State University is a different institution with its own scholarship pages — make sure you are reading msstate.edu sources."),
 ("How long does the scholarship last?","It renews each fall and spring for up to eight semesters, as long as you maintain continuous full-time enrolment and the required overall MSU GPA."),
 ("What test scores count?","MSU accepts the ACT/SAT through the February test date of your senior year, and superscoring is accepted. A 31 ACT/1390 SAT or above moves you into the higher column of your GPA band; 34+ ACT adds a one-year housing award."),
 ("Can international students get it?","The award is for students classified as non-residents for tuition purposes — that includes out-of-state US students. International applicants should confirm their tuition classification with MSU Undergraduate Admissions, since the official schedule is written around domestic non-resident tuition."),
]),
 offlinks=[('Out-of-State Resident Scholarships 2026–27 (official PDF, MSU Admissions)','https://admissions.msstate.edu/sites/www.admissions.msstate.edu/files/2026-05/Mississippi%20State%20University%202025-2026%20OOS%20Scholarships.pdf'),
           ('Out-of-State Freshman Scholarships — MSU Student Financial Aid','https://www.sfa.msstate.edu/scholarships/out-state-freshman-scholarships')],
 related_titles=['ursinus','mcneill','bloomberg-harvard'],
 verify='Verified 17 Oct 2026 via MSU Admissions’ official 2026–27 out-of-state scholarship PDF (award bands $12,000–$24,000 by GPA × test score; automatic on admission; superscoring; February test-date cutoff; 8-semester renewal; 34+ ACT housing award) and the official sfa.msstate.edu out-of-state freshman page (alumni non-resident award, non-resident tuition waiver, General Scholarship Application priority 1 Dec 2025). Confirmed Mississippi State (msstate.edu), not Michigan State.'),

# ---------------------------------------------------------------- 3. Said Foundation
dict(
 slug='said-foundation-scholarship-2027-uk',
 title='Saïd Foundation Scholarship 2027 in UK (Fully Funded) | StudyDesk Scholarships',
 meta='Saïd Foundation Scholarship 2027: fully funded one-year master’s in the UK for Syrian, Jordanian, Lebanese and Palestinian nationals. Deadline 30 Oct 2026. Eligibility, benefits and how to apply.',
 short='Saïd Foundation Scholarship 2027', kicker='UK · Master’s · Fully funded by the Saïd Foundation',
 mono='SF', prov_short='Saïd Foundation',
 h1='Saïd Foundation Scholarship 2027 in UK (Fully Funded)',
 sub='The Saïd Foundation Scholarship is one of the most mission-driven awards in the UK: a fully funded one-year master’s at a partner university, reserved for talented nationals of Syria, Jordan, Lebanon and Palestine who plan to take their degree home. Around 20 to 30 scholarships are awarded each year, and the 2027/28 window closes at 5:00 PM UK time on 30 October 2026 — you apply to the Foundation and to your chosen universities in parallel.',
 dpill='13 days to go', dl_long='30 Oct 2026, 5:00 PM UK time',
 facts=facts([('Award','Fully funded one-year master’s<small>Tuition fees, full living costs, arrival allowance, visa fees, Immigration Health Surcharge, one economy return flight — ~20–30 awards per year</small>'),
              ('Who','4 nationalities<small>Syrian, Jordanian, Lebanese or Palestinian nationals permanently resident in those countries (Syrians displaced elsewhere considered); UK 2:1-equivalent degree; relevant work/voluntary experience; leadership potential</small>'),
              ('Where','Partner UK universities<small>Defined partner list including Oxford, Cambridge, UCL, King’s College London, Imperial, York, Sussex, Southampton, Nottingham — several partners co-fund tuition</small>'),
              ('English','IELTS 6.0 overall (6.0 each band)<small>TOEFL iBT and Duolingo also accepted under the Foundation’s published conditions</small>'),
              ('Timeline','Now open → 30 Oct 2026<small>Applications opened 1 Sep 2026; university-application evidence due 29 Jan 2027; interviews Mar 2027; final decisions May/Jun 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Saïd Foundation</strong> awards up to <strong>thirty scholarships a year</strong> for one-year master’s degrees at its <strong>partner universities across the UK</strong> — a list that includes Oxford, Cambridge, UCL, King’s College London, Imperial, York, Sussex, Southampton and Nottingham. Unlike broad global awards, this one is deliberately regional: it exists to develop people who will <strong>return to Syria, Jordan, Lebanon or Palestine</strong> and apply what they learned there. The award is genuinely fully funded — tuition, full living costs for the course duration, an arrival allowance, visa and Immigration Health Surcharge fees, and one economy return flight — with several partner universities co-funding part of the tuition themselves (King’s College London, for example, covers 25 per cent). There is no fixed subject requirement; what matters is leadership potential, professional objectives and a credible plan to return home.</p>
      <p><strong>The application runs through the Foundation’s own website, not the universities</strong> — but you must apply to the universities separately at the same time, and you can list up to three courses at partner universities in order of preference.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Nationality and residence:</strong> hold Syrian, Jordanian, Lebanese or Palestinian nationality <strong>and</strong> be permanently resident in one of those countries. The Foundation considers Syrians living elsewhere because of conditions in the country.</li>
        <li><strong>Academics:</strong> an undergraduate degree equivalent to a <strong>UK 2:1 or above</strong>; final-year undergraduates may also apply.</li>
        <li><strong>Experience:</strong> relevant work and/or voluntary experience in your field of study, with a clear career path on completing the degree and returning to your home country or region.</li>
        <li><strong>Leadership:</strong> demonstrable leadership potential in your chosen field or sector.</li>
        <li><strong>English:</strong> meet the Foundation’s English-language requirement — currently <strong>IELTS 6.0 overall with at least 6.0 in each band</strong>; TOEFL iBT and Duolingo accepted under published conditions.</li>
        <li><strong>Course:</strong> have applied for an eligible one-year postgraduate taught or research master’s at a partner university. MBA programmes, joint courses with other institutions and online/distance degrees are not eligible.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> at the partner university (several partners co-fund a share of the fee).</li>
        <li><strong>Full living/maintenance costs</strong> for the duration of the one-year course.</li>
        <li><strong>Arrival allowance</strong>, plus <strong>visa fees and the Immigration Health Surcharge</strong>.</li>
        <li><strong>One economy return flight</strong> between home and the UK.</li>
        <li>Professional network and alumni community of scholars working across the region. Note: the Foundation states plainly that it cannot financially support spouses or children.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed <strong>online Foundation application</strong>.</li>
        <li><strong>Three reference letters</strong> — one academic, one professional and one voluntary.</li>
        <li>University <strong>transcripts and graduation certificate</strong>; high-school certificate copy.</li>
        <li><strong>Passport or national ID</strong> copy; recent passport-sized photographs.</li>
        <li><strong>English-language certificate</strong> (test dated after 1 October 2025, per the published requirements).</li>
        <li><strong>Evidence of university applications</strong> — offer letters or proof of application to your preferred courses (official evidence due by 29 January 2027).</li>
        <li>Medical certificate and any other supporting documents.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check eligibility</strong> on the Foundation’s requirements page and shortlist up to three eligible one-year master’s courses at partner universities.</li>
        <li><strong>Apply to the universities directly</strong> — you do not need an offer before the Foundation deadline, but you should have applied if the course applications are open.</li>
        <li><strong>Complete the Foundation’s online application</strong> with your three proposed courses in order of preference, and upload all documents and references.</li>
        <li><strong>Submit by 5:00 PM UK time on 30 October 2026.</strong> Incomplete applications are not considered.</li>
        <li><strong>After the deadline:</strong> upload evidence of your university applications by 29 January 2027; shortlisted candidates are interviewed in March 2027, and final selections are notified by early June 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who can apply for the Saïd Foundation Scholarship?","Citizens of Syria, Jordan, Lebanon or Palestine who are permanently resident in those countries (with an exception for Syrians displaced elsewhere). It is not open to other nationalities."),
 ("Is there an age limit?","No — the Foundation states there is no age limit for applicants."),
 ("Do I need a university offer before applying?","No. You apply to the Foundation and to your chosen universities in parallel; you need to have applied to the university course if applications are open, but an offer is not required at the Foundation deadline."),
 ("What does 'fully funded' cover?","Tuition fees, full living costs, an arrival allowance, visa fees, the Immigration Health Surcharge and one economy return flight. Spouses and children are not supported."),
 ("Can I study any subject?","There is no fixed subject requirement, but your course must be an eligible one-year master’s (taught or by research) at one of the Foundation’s partner universities — MBAs, joint courses and online degrees are excluded."),
 ("Is work experience really required?","Yes — you should have previous work or voluntary experience relevant to your subject of study, plus a clear plan to apply your degree back home."),
]),
 offlinks=[('Saïd Foundation Scholarship — Imperial College London (official partner page: deadlines, eligibility)','https://www.imperial.ac.uk/study/fees-and-funding/postgraduate-taught/grants-scholarships/said-foundation-scholarship/'),
           ('Saïd Foundation Scholarships 2027 — key dates and procedure','https://europescholarships.com/scholarships/said-foundation-scholarships-uk-2027')],
 related_titles=['mcneill','eiffel','keio-adb'],
 verify='Verified 17 Oct 2026 via Imperial College London’s official Saïd Foundation partner page (applications open 1 Sep 2026, close 30 Oct 2026 5:00 PM UK time; nationality/residence rules; 2:1-equivalent degree; experience, leadership and English requirements; eligible one-year master’s), corroborated by europescholarships, scholarpositions and scholarshipsads (full benefits breakdown incl. arrival allowance, visa fees and IHS; 29 Jan 2027 evidence deadline; Mar 2027 interviews; May/Jun 2027 decisions; ~20–30 awards).'),

# ---------------------------------------------------------------- 4. UM Bright
dict(
 slug='university-of-malaya-bright-scholarship-2027-malaysia',
 title='University of Malaya Bright Scholarship 2027 in Malaysia (Fully Funded) | StudyDesk Scholarships',
 meta='UM Bright Scholarship 2027: RM3,500/month for 42 months plus a full tuition waiver for 7 semesters for PhD by research at Universiti Malaya. Age ≤30, CGPA 3.70+. Eligibility, documents and how to apply.',
 short='UM Bright Scholarship 2027', kicker='Malaysia · PhD by research · Fully funded by Universiti Malaya',
 mono='UM', prov_short='University of Malaya',
 h1='University of Malaya Bright Scholarship 2027 in Malaysia (Fully Funded)',
 sub='The Universiti Malaya (UM) Bright Scholarship is built for one audience: outstanding researchers, Malaysian or international, ready to do a full-time PhD by research in Kuala Lumpur. The package is RM3,500 a month for 42 months plus a full tuition-fee waiver for seven semesters. The bar is high — a 3.70 CGPA at both bachelor’s and master’s level and age 30 or under — and applications roll throughout the year with deadlines that vary by research field.',
 dpill='Rolling deadline', dl_long='Varies by research field (applications accepted throughout the year)',
 facts=facts([('Award','RM3,500/month × 42 months<small>Plus a full tuition-fee waiver for 7 semesters. Insurance, visa, flights, medical exams and accommodation are NOT covered</small>'),
              ('Who','PhD by research candidates<small>Malaysian citizens and international students; age not exceeding 30 in the year of application; must not hold any other sponsorship or scholarship</small>'),
              ('Grades','CGPA 3.70+<small>Bachelor’s degree with CGPA above 3.70 AND a Master’s by research or mixed mode (coursework + dissertation) with CGPA ≥3.70/4.00</small>'),
              ('English','IELTS 6.5+ / TOEFL 73–93 / CEFR B2<small>Non-citizens must submit a valid English qualification (valid within 2 years of the exam date)</small>'),
              ('Fields','10 UM thrust areas<small>Nuclear energy, semiconductors, nanotechnology/quantum, AI & robotics, space science, food security, medical & health, rare earths, defence & security, social-science advancement</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>UM Bright Scholarship</strong> is Universiti Malaya’s flagship award for doctoral talent — a fully funded route into a <strong>full-time PhD by research</strong> at Malaysia’s top-ranked university in Kuala Lumpur. It is open to <strong>both Malaysian citizens and international students</strong>, and it is explicitly designed to attract strong minds into UM’s <strong>10 strategic research thrust areas</strong>: nuclear and new energy transition, semiconductors and chips, nanotechnology and quantum exploration, AI and digital robotics, space science and engineering, food sustainability and security, medical and health excellence, rare earths and critical minerals, defence and security innovation, and social-science advancement (economics, finance, law, geopolitics).</p>
      <p>The support is straightforward and generous where it counts: a <strong>monthly stipend of RM3,500 for 42 months</strong> and a <strong>full tuition-fee waiver for seven semesters</strong>. The university is equally clear about what it does <strong>not</strong> pay: passport preparation, insurance, visas, flight tickets, medical examinations and accommodation are all on the scholar.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Age:</strong> must not exceed <strong>30 years</strong> in the year of application.</li>
        <li><strong>Bachelor’s degree</strong> with a CGPA <strong>above 3.70</strong> (or a recognised equivalent).</li>
        <li><strong>Master’s degree</strong> by research, or through mixed mode (coursework plus dissertation), with a CGPA of at least <strong>3.70/4.00</strong>.</li>
        <li><strong>English proficiency (non-citizens):</strong> IELTS Academic 6.5 or above, TOEFL 73–93, or CEFR B2 — the qualification must be valid within the two years before application.</li>
        <li><strong>No double funding:</strong> you must not already be receiving any sponsorship or scholarship from any other organisation.</li>
        <li>Research area must fall within the 10 UM thrust areas; the university reserves the right to assign the appropriate field based on your merits.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>RM3,500 per month</strong> for 42 months — over RM147,000 in direct stipend support.</li>
        <li><strong>Full tuition-fee waiver</strong> throughout seven semesters of the PhD.</li>
        <li>Supervision and research facilities at one of Southeast Asia’s leading research universities.</li>
        <li><strong>Not covered:</strong> insurance, visa fees, flight tickets, medical examinations and accommodation.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Passport-sized photograph.</li>
        <li>Completed <strong>UMES application form</strong>.</li>
        <li><strong>Publication proof</strong> (first page) and evidence of conference participation, where applicable.</li>
        <li>Copy of <strong>identity card / passport</strong>.</li>
        <li><strong>Bachelor’s and Master’s degree certificates and transcripts.</strong></li>
        <li><strong>Valid English-proficiency certificate.</strong></li>
        <li>Proposed PhD research area and preferred supervisor (asked for in the official application form).</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Complete the UM application form</strong> (the UMES form published with the official call).</li>
        <li><strong>Compile every document as a PDF</strong> and label the file in the official format: <strong>“&lt;your name&gt;*UMBrightS*&lt;date dd-mm-yy&gt;”</strong>.</li>
        <li><strong>Email the package to brightscholar@um.edu.my</strong> — the application address published in the official call documents.</li>
        <li><strong>Watch your field’s deadline:</strong> there is no single closing date — the last date varies by field of research, and applications are accepted throughout the year. Apply well ahead of your intended intake.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the UM Bright Scholarship open to international students?","Yes — both Malaysian citizens and international (non-citizen) students are eligible, provided they meet the academic, age and English requirements."),
 ("What CGPA do I actually need?","A Bachelor’s with CGPA above 3.70 and a Master’s (by research or mixed mode) with CGPA of at least 3.70/4.00. Both thresholds apply."),
 ("Does it cover accommodation and flights?","No. Insurance, visas, flight tickets, medical examinations and accommodation are explicitly not borne by Universiti Malaya under this scheme."),
 ("Is there a single deadline?","No — the closing date varies by field of research, and the scheme accepts applications throughout the year. Check the call for your thrust area."),
 ("Can I hold another scholarship at the same time?","No — applicants must not be recipients of any sponsorship or scholarship from any other organisation or party."),
]),
 offlinks=[('UM Bright Scholarship 2027 — benefits, eligibility, documents','https://medjouel.com/jobs/um-bright-scholarship-2027-in-malaysia-fully-funded/'),
           ('UM Bright Scholarship — official criteria, thrust areas, deadlines','https://opportunityportal.info/university-malaya-um-bright-scholarship/')],
 related_titles=['keio-adb','honjo','mcneill'],
 verify='Verified 17 Oct 2026 via medjouel and opportunityportal.info trackers (RM3,500/month × 42 months; full tuition waiver 7 semesters; age ≤30; Bachelor CGPA >3.70; research/mixed-mode Master CGPA ≥3.70/4.00; IELTS 6.5+/TOEFL 73–93/CEFR B2 valid 2 years; no other sponsorship; brightscholar@um.edu.my application email; deadline varies by field), corroborated by scholarshipsedge and aktravelsltd (official document excerpts: 10 thrust areas, exclusions list, research-only PhD mode).'),

# ---------------------------------------------------------------- 5. NTU
dict(
 slug='national-taiwan-university-scholarship-2027-taiwan',
 title='National Taiwan University Scholarship 2027 in Taiwan (Fully Funded) | StudyDesk Scholarships',
 meta='National Taiwan University Scholarship 2027: tuition waiver up to TWD 65,000/semester, TWD 30,000/month stipend and return airfare for international Master’s and PhD students. Round 1 deadline 5 Nov 2026.',
 short='NTU Scholarship 2027', kicker='Taiwan · Master’s/PhD · Fully funded by NTU',
 mono='NTU', prov_short='National Taiwan University',
 h1='National Taiwan University Scholarship 2027 in Taiwan (Fully Funded)',
 sub='National Taiwan University in Taipei — Taiwan’s most comprehensive research university — funds international master’s and PhD students through scholarships considered automatically inside the admission application. The headline graduate package reported across trackers runs to a tuition waiver of up to TWD 65,000 a semester, a TWD 30,000 monthly stipend and one return air ticket. Round 1 closes 5 November 2026, with a second round on 19 January 2027.',
 dpill='19 days to go', dl_long='Round 1: 5 Nov 2026 · Round 2: 19 Jan 2027',
 facts=facts([('Award','Tuition waiver + TWD 30,000/month<small>Tuition waiver up to TWD 65,000 per semester (headline graduate package), monthly stipend around TWD 30,000 (~USD 1,000), one economy-class return ticket; exact tier depends on the award — benefits vary by scheme</small>'),
              ('Who','International Master’s & PhD applicants<small>Foreign nationals holding a bachelor’s (for master’s) or master’s (for PhD); must never have held Overseas Chinese status</small>'),
              ('Deadlines','Two rounds<small>Round 1: 5 Nov 2026 (portal opened 29 Sep 2026); Round 2: 19 Jan 2027 — for September 2027 entry</small>'),
              ('No separate form','Tick the box<small>No separate scholarship application in most cases — select scholarship consideration inside the NTU online admission portal and you are evaluated automatically</small>'),
              ('Language','TOEFL iBT 72 / IELTS 5.5 / TOEIC 785<small>English-taught programmes: CEFR B2 or equivalent (MOI certificate accepted in place of a test); Chinese-taught: TOCFL Band A Level 2 or HSK 4</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>National Taiwan University (NTU)</strong> in Taipei — operating since 1928, with 11 colleges, 56 departments and 133 graduate institutes — invites international students from all countries to apply for its <strong>2027 scholarships for Master’s and PhD programmes</strong>. The convenient part: <strong>admission and scholarship consideration happen through the same process</strong>. There is no separate scholarship form in most cases — you tick the scholarship-consideration box inside the NTU online application portal, and the selection committee evaluates you automatically.</p>
      <p>Benefits are tiered, but the headline graduate package reported across trackers is strong: a <strong>tuition waiver of up to TWD 65,000 per semester</strong> (up to TWD 40,000 in the first semester in some reports), a <strong>monthly stipend of TWD 30,000</strong> (about USD 1,000) for living costs, and <strong>one economy-class return ticket</strong> between your home country and Taiwan. Funding duration is matched to the degree — roughly two years for a master’s and three for a doctorate.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Nationality:</strong> international (foreign-national) students; applicants must never have held Overseas Chinese status.</li>
        <li><strong>Academics:</strong> a bachelor’s degree (or equivalent) for master’s entry; a master’s degree (or equivalent) for PhD entry.</li>
        <li><strong>Language — English-taught programmes:</strong> CEFR B2 or above, e.g. <strong>TOEFL iBT 72, IELTS Academic 5.5, TOEIC 785</strong>, or an official Medium of Instruction certificate from your previous university confirming English-medium study.</li>
        <li><strong>Language — Chinese-taught programmes:</strong> CEFR A2 or above, e.g. <strong>TOCFL Band A Level 2 or HSK Level 4</strong>.</li>
        <li>Renewal is GPA-based where stipends continue — the undergraduate scheme, for reference, requires GPA 3.0/3.2/3.33 across the first three years.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition waiver:</strong> up to TWD 65,000 per semester under the headline international scheme (figures vary by tier — some reports quote up to TWD 40,000 in the first semester, rising thereafter).</li>
        <li><strong>Monthly living stipend:</strong> up to TWD 30,000 (~USD 1,000) for graduate scholars.</li>
        <li><strong>One economy-class return air ticket</strong> (home country ⇄ Taiwan).</li>
        <li>Duration matched to the degree: about two years for a master’s, three for a doctorate.</li>
        <li>Administrative fees, thesis-advisor fees, insurance, accommodation, internet and credit fees are excluded — you pay those.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>The full per-programme document list is published inside the NTU online application portal — “not published in the official notification” as a single list. Trackers consistently report: degree certificates and transcripts, language-proficiency proof (or MOI certificate), passport copy, two academic referees (contact details entered in the portal for automated recommendation requests), and the NTD 2,000 application fee. Individual departments may ask for more.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on the NTU online application portal</strong> (the Round 1 portal opened 29 September 2026).</li>
        <li><strong>Select up to five target departments or graduate institutes</strong> in order of preference.</li>
        <li><strong>Complete the form and tick the scholarship-consideration box</strong> — this registers you for scholarship review automatically.</li>
        <li><strong>Upload documents</strong> within the portal’s file limits and <strong>enter two referees’ details</strong> for automated recommendation requests.</li>
        <li><strong>Pay the NTD 2,000 application fee</strong> (reported; non-refundable) and submit before <strong>5 November 2026 (Round 1)</strong> or <strong>19 January 2027 (Round 2)</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate scholarship application?","In most cases, no. You tick the scholarship-consideration box in the NTU online admission portal, and the selection committee evaluates your profile automatically."),
 ("What are the 2027 deadlines?","Round 1 closes 5 November 2026 and Round 2 closes 19 January 2027, both for September 2027 entry. Results come out around mid-January (Round 1) and mid-April (Round 2)."),
 ("Can I apply without IELTS?","Yes, if you submit an official Medium of Instruction certificate from your previous university confirming your degree was taught in English. Otherwise TOEFL iBT 72, IELTS 5.5 or TOEIC 785 meet the English-taught requirement."),
 ("Is the scholarship fully funded?","The headline graduate package covers tuition (up to TWD 65,000/semester), a TWD 30,000 monthly stipend and one return air ticket. Tiers vary, and admin fees, insurance, accommodation and credit fees are excluded."),
 ("Do undergraduates get the same package?","No — the undergraduate international scheme is a separate tier (up to TWD 65,000/semester tuition subsidy plus a TWD 8,000 monthly stipend). This article covers the Master’s/PhD 2027 intake."),
]),
 offlinks=[('NTU Scholarship 2027 — deadlines, benefits, application steps','https://scholarpositions.com/national-taiwan-university-scholarship-2027/'),
           ('NTU Scholarships 2027 — two rounds, funding details','https://scholarshipforphd.com/ntu-scholarship/')],
 related_titles=['keio-adb','honjo','mcneill'],
 verify='Verified 17 Oct 2026 via scholarpositions and scholarshipforphd (Round 1: 5 Nov 2026; Round 2: 19 Jan 2027; Master’s/PhD; tuition waiver up to TWD 65,000/semester; TWD 30,000/month stipend; one return ticket; no separate form), corroborated by greatyop and scholarships.af (eligibility: foreign nationals, degree requirements, language thresholds TOEFL 72/IELTS 5.5/TOCFL A2, NTD 2,000 fee, two referees). Benefits vary by tier — presented as the headline graduate package, not a guaranteed uniform award.'),

]

if __name__ == '__main__':
    ok = 0
    for a in ARTICLES:
        assert a['slug'] not in [x['slug'] for x in ARTICLES[:ok]], a['slug'] + ' duplicated'
        sz = build_article(BASE, OUT, a, CARDINFO)
        ok += 1
        print('built', a['slug'], sz, 'bytes')
    import html.parser as hp
    for a in ARTICLES:
        path = OUT / (a['slug'] + '.html')
        src = path.read_text()
        p = hp.HTMLParser(); p.feed(src)
        for bad in ('AICTE Pragati', 'Lorem'):
            if bad in src:
                raise AssertionError((a['slug'], 'leftover', bad))
        print('validated', a['slug'])

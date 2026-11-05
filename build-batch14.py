#!/usr/bin/env python3
"""Batch 14 (cron run 14): 5 verified international articles. Verified 17 Oct 2026.

Notes:
- Erfurt doctoral 2027: official August 2026 call PDF is the authority. EUR1,400/mo,
  3 yrs + 1 yr extension, funding starts 1 Apr 2027, apply as ONE PDF <=5MB by
  24 Nov 2026 11:59 p.m. CET; recommendation letter goes by separate email from
  the reviewer. No separate international-eligibility caveat: the official PDF's
  equal-opportunities clause covers all origins.
- McNeill 2027: offered once every TWO years (current cycle 2026, deadline still
  31 Oct 2026); NOT fully funded in the tuition-waiver sense; no separate form -
  automatic consideration via the myApp graduate-research application; only ONE
  award. Aggregate breakdown figures (relocation/research splits) are NOT on the
  official page - not stated.
- TU/e Excellence 2027: EXPLICITLY partial (EUR7,500/yr x 2 yrs, ~35 awards) -
  not fully funded despite aggregator claims of full tuition + stipend.
  Non-EEA awards partly funded via the national NL Scholarship - no separate
  NL application allowed. Results by end of March 2027.
- Tilburg Research Master Scholarship 2027: tuition-fee waiver ONLY (2 yrs, max
  3 per cohort), no living stipend; detailed official page covers the Research
  Master in Communication, Cognition and Digital Culture; do NOT merge the
  separate CentER Economics scholarship into it.
- ANZ Summer Internship 2027: PAID EMPLOYMENT internship, not a scholarship;
  currently Expression of Interest only (no deadline published; formal apps
  expected June/July 2027; internships start Nov 2027); AU/NZ citizenship or PR
  required - not open to international students in general.
- 1PAX Graduate Fellowship 2026 (France): SKIPPED - deadline passed 30 Sep 2026.
- KCL Chevening 2027: SKIPPED - Chevening 2027/28 round closed 6 Oct 2026.
- NOMIS Senior Fellowship 2027: SKIPPED - 2027 nominations closed 30 Sep 2026;
  next deadline 30 Sep 2027 for the 2028-29 term.
- International Graduate Scholarship 2027 in Japan: SKIPPED as duplicate - same
  scheme already published as Science Tokyo MEXT Scholarship 2027 (22 Nov 2026).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'erfurt-phd': dict(mono='UE', title='University of Erfurt Doctoral Scholarships 2027 in Germany', href='university-erfurt-doctoral-scholarships-2027-germany.html',
              dpill='38 days to go', award='€1,400/month × 3 years (+1 yr extension)', elig='Doctoral candidates at Erfurt / Max-Weber-Kolleg; above-average results; matriculation by funding start.',
              tags=[("PhD",'blue'),('Germany','teal')]),
 'mcneill': dict(mono='SJ', title='Sir James McNeill Postgraduate Research Scholarship 2027 (Australia)', href='sir-james-mcneill-postgraduate-research-scholarship-2027-australia.html',
              dpill='14 days to go', award='$53,608 p.a. living + research + relocation (2026 rate)', elig='Monash HDR applicants; domestic + international; eligible faculties incl. Engineering, Science.',
              tags=[("Postgraduate research",'blue'),('Australia','teal')]),
 'tue-excellence': dict(mono='TU/e', title='TU/e Scholarship for Excellence 2027 in Netherlands (Partial)', href='tu-eindhoven-excellence-scholarship-2027-netherlands.html',
              dpill='76 days to go', award='€7,500/year × 2 years (partial; ~35 awards)', elig='Non-Dutch diploma; GPA ≥7.5/10; eligible TU/e MSc, Sep 2027 start.',
              tags=[("Master's",'blue'),('Netherlands','teal')]),
 'tilburg-rm': dict(mono='T', title='Tilburg University Research Master Scholarship 2027 in Netherlands', href='tilburg-university-research-master-scholarship-2027-netherlands.html',
              dpill='166 days to go', award='Full 2-year tuition-fee waiver (max 3 per cohort)', elig='Research Master in Communication, Cognition and Digital Culture; outstanding non-EEA first-master students; Sep start.',
              tags=[("Master's",'blue'),('Netherlands','teal')]),
 'anz-summer': dict(mono='ANZ', title='ANZ Summer Internship Program 2027 in Australia (Paid)', href='anz-summer-internship-program-2027-australia.html',
              dpill='EOI open now', award='Paid 8–10 week internship, starts Nov 2027', elig='AU/NZ citizens or PR; penultimate-year students; any degree background.',
              tags=[("Internship",'blue'),('Australia','teal')]),
})

ARTICLES = [

# ---------------------------------------------------------------- 1. Erfurt
dict(
 slug='university-erfurt-doctoral-scholarships-2027-germany',
 title='University of Erfurt Doctoral Scholarships 2027 in Germany (€1,400/Month) | StudyDesk Scholarships',
 meta="University of Erfurt doctoral scholarships 2027: €1,400/month for 3 years under Thuringia's state graduate scheme. Deadline 24 Nov 2026. Eligibility, documents and how to apply.",
 short='Erfurt Doctoral Scholarships 2027', kicker='Germany · PhD · State-funded doctoral scholarships',
 mono='UE', prov_short='University of Erfurt',
 h1='University of Erfurt Doctoral Scholarships 2027 in Germany',
 sub='The University of Erfurt is funding up to four doctoral scholarships through Thuringia’s state graduate scheme: €1,400 a month for three years (extendable by a fourth), plus family and research allowances. The application is a single email — but every document has to land in the right order, and the referee’s letter travels separately.',
 dpill='38 days to go', dl_long='24 Nov 2026, 11:59 p.m. CET',
 facts=facts([('Award','€1,400/month basic scholarship<small>Standard period 3 years, extendable by one additional year on request; up to 4 scholarships awarded</small>'),
              ('Extras','Family + research allowances<small>€300/month for the first dependent child, €150/month for each additional child; up to €600/year for research-related material and travel</small>'),
              ('Who','Doctoral candidates at Erfurt<small>Accepted by an Erfurt faculty or the Max-Weber-Kolleg, and matriculated, by funding start at the latest</small>'),
              ('How to apply','Single PDF by email<small>One PDF (≤5 MB, official document order, with a table of contents) to graduiertenfoerderung@uni-erfurt.de</small>'),
              ('Funding starts','1 April 2027<small>No later than 1 July 2027; decisions expected end of February 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Erfurt</strong> is awarding doctoral scholarships under the <strong>Thuringian State Graduate Support</strong> (<em>Thüringer Graduiertenförderung</em>) — the state of Thuringia’s scheme for funding doctoral researchers. Up to <strong>four scholarships</strong> are on offer in this call. The core award is a <strong>basic scholarship of €1,400 per month</strong> with a <strong>standard funding period of three years</strong>, which can be <strong>extended by one additional year on request</strong>. On top of the basic amount there are family allowances and an annual research budget, and funded researchers join the university’s structured doctoral training programme (the Erfurt Doctoral and Postdoctoral Programme, EPPP), with academic-skills courses, networking and science-communication platforms. Funding starts on <strong>1 April 2027</strong> (no later than 1 July 2027).</p>
      <p><strong>The application mechanics matter more than the money:</strong> the entire dossier goes as <strong>one PDF, no larger than 5 MB</strong>, in the university’s official document order with a table of contents, emailed to the graduate services office. The <strong>letter of recommendation is NOT part of that PDF</strong> — your reviewer sends it separately, on the university’s prescribed form, directly by email. You do not need to be formally accepted as a doctoral candidate when you apply; proof that you have contacted a Graduate Centre or the Max-Weber-Kolleg is enough — but formal acceptance, full Graduate Centre membership and matriculation must all be in place by the funding start.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Above-average academic achievements:</strong> your examination results must show clear aptitude for academic research.</li>
        <li><strong>Doctoral acceptance by funding start:</strong> you must be accepted as a doctoral candidate by one of the University of Erfurt’s faculties or the Max-Weber-Kolleg <strong>by the start of funding at the latest</strong>, and maintain that status throughout. You do not need this at application time — documented contact with a Graduate Centre or the Max-Weber-Kolleg suffices.</li>
        <li><strong>Matriculation:</strong> you must be matriculated at the University of Erfurt by the start of funding.</li>
        <li><strong>Graduate Centre membership:</strong> full membership in a certified Graduate Centre or the Max-Weber-Kolleg by the start of funding.</li>
        <li><strong>Health insurance:</strong> current proof of health insurance by the start of funding.</li>
        <li><strong>No double funding:</strong> no parallel public funding for the same period and purpose.</li>
        <li><strong>Employment limits:</strong> up to 12 hours/week of research/teaching work at a higher-education or research institution, or up to 5 hours/week of other employment; teaching no more than 2 hours/week on average per academic year.</li>
        <li><strong>Open to all origins:</strong> the official call’s equal-opportunities clause welcomes applications regardless of origin. Your doctoral project must sit within the Erfurt Doctoral and Postdoctoral Programme — for example a certified Graduate Centre, the Max-Weber-Kolleg, or CEREB (economics/behavioural sciences).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€1,400 per month</strong> basic scholarship for three years, extendable by one further year on request.</li>
        <li><strong>Family allowance:</strong> €300 per month for the first dependent child and €150 per month for each additional child.</li>
        <li><strong>Research budget:</strong> up to €600 per funding year for research-related material and travel costs (subject to available funds).</li>
        <li><strong>Structured doctoral training:</strong> integration into the EPPP, with at least six Academic Skills courses, networking and science-communication opportunities.</li>
        <li>Evaluation takes about <strong>10 weeks</strong>; decisions are expected by the <strong>end of February 2027</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>Confirmed from the official August 2026 call (PDF). Assemble Part 1 in the official order, with a table of contents, into one PDF of ≤5 MB.</em></p>
      <ol>
        <li><strong>Cover letter</strong> (max 2 pages): name the Graduate Centre or Max-Weber-Kolleg, explain why you are applying, state your project’s progress, and add any voluntary personal circumstances.</li>
        <li><strong>Tabular CV</strong> plus the university’s CV supplement form.</li>
        <li><strong>Exposé:</strong> project outline of 6–8 pages (excluding cover page and bibliography) plus a three-year work and time schedule.</li>
        <li><strong>Contact form:</strong> official form confirming contact established with a Graduate Centre or the Max-Weber-Kolleg (or the admission form if you are already a full member).</li>
        <li><strong>Faculty/Max-Weber-Kolleg confirmation</strong> of doctoral acceptance, if already available.</li>
        <li><strong>List of academic publications and presentations</strong>, if applicable.</li>
        <li><strong>Degree certificates</strong> (Diploma/Magister or Bachelor’s + Master’s) — certified German/English translation if the originals are in another language.</li>
        <li><strong>Complete copy of your final thesis</strong> (Diploma/Magister/Master’s) — include a 2-page German/English summary if the original is not in either language.</li>
        <li><strong>Signed consent</strong> to the processing of personal data.</li>
        <li><strong>Letter of recommendation</strong> on the university’s prescribed form, written by a professor/university teacher (University of Erfurt or another higher-education institution) — <strong>submitted SEPARATELY by the reviewer by email, NOT inside your PDF</strong>.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the official call and document checklist</strong> on the university’s announcements page, and <strong>establish contact with a Graduate Centre or the Max-Weber-Kolleg early</strong> — that contact is a hard requirement at application time.</li>
        <li><strong>Assemble the dossier</strong> in the official order with a table of contents into <strong>one PDF of ≤5 MB</strong>. Do not include the checklist itself in the application.</li>
        <li><strong>Email it to graduiertenfoerderung@uni-erfurt.de</strong> with the subject line <strong>“Application for the State Graduate Scholarship 2026 – surname, first name”</strong> (use your own surname and first name) by <strong>24 November 2026, 11:59 p.m. CET</strong>.</li>
        <li><strong>Arrange the recommendation letter separately:</strong> your reviewer emails it directly — on the prescribed form, and on time — to the same address.</li>
        <li><strong>Contact for queries:</strong> Ms Xiaolei Dong, Research and Graduate Services, +49 (0)361 737-5042. Decisions are expected by the end of February 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need to be accepted as a doctoral candidate before I apply?","No. At application time, proof that you have established contact with a Graduate Centre or the Max-Weber-Kolleg is enough. Formal acceptance, full membership and matriculation are required only by the funding start (1 April 2027 at the earliest)."),
 ("How long does the funding last?","Three years as standard, with the possibility of a one-year extension on request. The family allowance is €300/month for the first dependent child and €150/month for each further child."),
 ("Where does the recommendation letter go?","Not in your PDF. Your reviewer sends it separately, on the university’s prescribed form, by email to graduiertenfoerderung@uni-erfurt.de — and it must arrive by the deadline too."),
 ("Can international students apply?","Yes. The official call’s equal-opportunities clause welcomes applications regardless of origin, and the underlying state scheme applies to all doctoral candidates at the university."),
 ("When will I hear back?","The evaluation takes about 10 weeks, and decisions are expected by the end of February 2027."),
]),
 offlinks=[('Official call — doctoral scholarships (PDF, University of Erfurt, August 2026)','https://www.uni-erfurt.de/fileadmin/fakultaet/max-weber-kolleg/00_Neue_Struktur/03_Ausschreibungen/02_Universitaet/Promotionsstipendien/Ausschreibung_Promotionsstipendien_Landesgraduiertenfoerderung_2026_EN.pdf')],
 related_titles=['hanns-seidel','daad','swiss-phd'],
 verify='Verified 17 Oct 2026 via the official University of Erfurt announcement (August 2026 PDF: deadline 24 Nov 2026 11:59 p.m. CET; €1,400/month × 3 years, extendable by 1 year; €300/€150 family allowances; ≤€600/yr research costs; full 10-item document list with the separate-email recommendation rule; subject-line format; Ms Xiaolei Dong contact), corroborated by globalsouthopportunities, researchersjob, truescho and Bright Scholarship trackers. Funding starts 1 April 2027; decisions expected end of February 2027; up to 4 scholarships.'),

# ---------------------------------------------------------------- 2. McNeill
dict(
 slug='sir-james-mcneill-postgraduate-research-scholarship-2027-australia',
 title='Sir James McNeill Postgraduate Research Scholarship 2027 (Australia) | StudyDesk Scholarships',
 meta="Sir James McNeill Postgraduate Research Scholarship 2027 at Monash University: $53,608 p.a. living allowance for research degrees in eligible faculties. Closes 31 Oct 2026. Eligibility and application guide.",
 short='McNeill Scholarship 2027', kicker='Australia · Postgraduate research · Monash University',
 mono='SJ', prov_short='Monash University',
 h1='Sir James McNeill Postgraduate Research Scholarship 2027 in Australia',
 sub='Monash University’s Sir James McNeill Postgraduate Research Scholarship is a rare one: a single $53,608-a-year living allowance for a research degree whose work is both environmentally responsible and socially beneficial. There is no separate scholarship form — you are considered automatically when you apply for a graduate research degree. And the clock is short: it closes 31 October.',
 dpill='14 days to go', dl_long='31 Oct 2026 (closes 31 October each year; awarded in the 31 October round)',
 facts=facts([('Award','$53,608 p.a. (2026 rate)<small>Living allowance + research allowance + relocation allowance (if eligible); only ONE scholarship offered</small>'),
              ('Cycle','Offered once every two years<small>The current cycle is 2026, with the 31 October round as the awarding round — this is the one to target</small>'),
              ('Who','Monash graduate-research applicants<small>Australian/NZ citizens, permanent residents, humanitarian visa holders AND international students</small>'),
              ('Eligible faculties','Arts, Engineering, Medicine/Nursing/Health Sciences, Science<small>Arts: School of Music only; research must be environmentally responsible AND socially beneficial</small>'),
              ('How to apply','No separate form<small>Apply for your graduate research degree via Monash’s myApp Portal; eligible applicants are automatically considered</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Sir James McNeill Postgraduate Research Scholarship</strong> is funded by a private trust in memory of <strong>Sir James McNeill</strong> and administered by <strong>Monash University</strong> in Melbourne, Australia. It is one of Monash’s most competitive research awards: <strong>only one scholarship is offered</strong>, carrying a <strong>living allowance of $53,608 per year (2026 rate)</strong>, plus a research allowance and a relocation allowance for those who qualify. It is awarded <strong>once every two years from R4/2024 onwards</strong> — the current cycle is 2026, decided in the <strong>31 October round</strong>.</p>
      <p><strong>What makes it unusual:</strong> the scholarship is not for any strong research topic — your research must be <strong>both environmentally responsible and socially beneficial</strong>, and it is open only within <strong>eligible faculties</strong>: Arts (School of Music only), Engineering, Medicine/Nursing/Health Sciences, and Science. Joint research awards qualify if Monash is the home institution. And unlike most big scholarships, <strong>there is no separate application form</strong>: eligible graduate-research applicants are <strong>automatically considered</strong>, with faculties nominating their candidates from Rounds 1–4 of the offering year. Note the official page does not mention tuition coverage — this is a <strong>living/research/relocation award, not a “full tuition + everything” package</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Residency:</strong> Australian citizens, New Zealand citizens, Australian permanent residents, Australian humanitarian visa holders, <strong>or international students</strong>.</li>
        <li><strong>Research direction:</strong> your research must be <strong>both environmentally responsible and socially beneficial</strong>.</li>
        <li><strong>Faculty:</strong> eligible faculties are <strong>Arts (School of Music only)</strong>, <strong>Engineering</strong>, <strong>Medicine/Nursing/Health Sciences</strong>, and <strong>Science</strong>. Joint research awards are eligible if Monash is the home institution.</li>
        <li><strong>Timing:</strong> you must have <strong>submitted a scholarship application in the year the scholarship is offered</strong> (the current cycle is 2026).</li>
        <li><strong>Competitive standing:</strong> you must meet <strong>Monash’s competitive scholarship selection requirements</strong> and the university’s <strong>English-language proficiency requirements</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$53,608 per year living allowance</strong> (2026 rate) for the research degree.</li>
        <li><strong>Research allowance</strong> attached to the award.</li>
        <li><strong>Relocation allowance</strong> for those who qualify (e.g. moving to Melbourne for the degree).</li>
        <li><strong>Only one award is made</strong> — this is a flagship single scholarship, not a cohort scheme.</li>
        <li>Applicants are <strong>automatically considered for all Monash graduate-research scholarships</strong> alongside this one.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>The official Monash page publishes no scholarship-specific document list — applications go through the standard graduate-research (HDR) application, so Monash does not spell out a separate checklist here. Typical HDR application materials (CV, transcripts, research proposal, English-language evidence) are listed by aggregators only and are not confirmed on the official page.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for your graduate research degree at Monash</strong> — scholarship applications are submitted <strong>at the same time as the course application</strong> via Monash’s <strong>myApp Portal</strong> (or as a current student if you are already enrolled).</li>
        <li><strong>There is no separate scholarship form to fill.</strong> Eligible applicants are <strong>automatically considered</strong> for all graduate-research scholarships, including the Sir James McNeill award.</li>
        <li><strong>Your faculty nominates you:</strong> eligible applicants from <strong>Rounds 1–4 of the offering year</strong> are automatically nominated by their faculty for the McNeill award — the scholarship itself is <strong>awarded in the 31 October round only</strong>.</li>
        <li><strong>Meet the 31 October deadline.</strong> The official page states the scholarship <strong>closes 31 October each year</strong>; for this cycle that is <strong>31 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this scholarship fully funded?","Not in the tuition-waiver sense. The official Monash page lists a living allowance, a research allowance and a relocation allowance — it does not mention tuition coverage. Read it as a generous living-cost award for a research degree, not a package covering every cost."),
 ("Is there a separate application form?","No. Graduate-research scholarship applications are submitted with the course application via Monash’s myApp Portal, and eligible applicants are automatically considered. Your faculty nominates you from the year’s rounds 1–4."),
 ("How often is it offered?","Once every two years from R4/2024 onwards — so the current offering cycle is 2026, decided in the 31 October 2026 round. Only one scholarship is offered per cycle."),
 ("Can international students apply?","Yes. International students are explicitly eligible alongside Australian citizens, NZ citizens, permanent residents and humanitarian visa holders."),
 ("Which faculties count?","Arts (School of Music only), Engineering, Medicine/Nursing/Health Sciences, and Science. Your research must be both environmentally responsible and socially beneficial."),
]),
 offlinks=[('Sir James McNeill Postgraduate Research Scholarship — Monash University (official)','https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/sir-james-mcneill-postgraduate-research-scholarship')],
 related_titles=['swiss-phd','zonta-ae','nasa-hubble'],
 verify='Verified 17 Oct 2026 via the official Monash University scholarships page ($53,608 p.a. 2026 rate — living + research + relocation; closes 31 October each year; offered once every two years from R4/2024; no separate scholarship form — automatic consideration via the myApp graduate-research application; eligible faculties Arts (Music only)/Engineering/Medicine-Nursing-Health/Science; research must be environmentally responsible and socially beneficial; international students eligible), corroborated by Mastersportal, PhDportal and Bright Scholarship. Aggregate breakdown figures are not published on the official page and are not stated here.'),

# ---------------------------------------------------------------- 3. TU/e Excellence
dict(
 slug='tu-eindhoven-excellence-scholarship-2027-netherlands',
 title='TU/e Scholarship for Excellence 2027 in Netherlands (€7,500/Year, Partial) | StudyDesk Scholarships',
 meta="TU/e Scholarship for Excellence 2027 at Eindhoven University of Technology: €7,500/year for 2 years for top Master's students in physics, engineering, maths and computing. Deadline 1 Jan 2027. Guide to eligibility and application.",
 short='TU/e Excellence Scholarship 2027', kicker='Netherlands · Master’s · Partial scholarship',
 mono='TU/e', prov_short='Eindhoven University of Technology',
 h1='TU/e Scholarship for Excellence 2027 in the Netherlands',
 sub='Eindhoven University of Technology offers about 35 Excellence scholarships a year to outstanding international Master’s students in physics, electrical and mechanical engineering, and mathematics and computer science. It pays €7,500 a year for up to two years — explicitly a partial award, so this is a boost toward your costs, not a full ride. The window closes 1 January 2027.',
 dpill='76 days to go', dl_long='1 Jan 2027, 23:59 CET',
 facts=facts([('Award','€7,500 per academic year<small>Up to two years (total €15,000), paid in monthly instalments to a Dutch or SEPA bank account; approx. 35 awards (20 EEA, 15 non-EEA)</small>'),
              ('Explicitly partial','Does NOT cover full costs<small>Full tuition and living costs are not covered — recipients must fund the rest; non-EEA recipients must still prove sufficient funds for the Dutch visa/residence permit</small>'),
              ('Who','Top international Master’s applicants<small>Eligible TU/e Master’s tracks in applied physics, electrical/mechanical engineering, maths & computer science; GPA ≥7.5/10; non-Dutch diploma</small>'),
              ('How to apply','Inside the MSc application<small>Apply for an eligible Master’s for Sep 2027; confirm scholarship interest with a brief motivation statement — no separate form</small>'),
              ('Results','By end of March 2027<small>Scholarship Selection Committee ranks applicants; second-year payment needs ≥45 ECTS in year 1</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>TU/e Scholarship for Excellence</strong> is <strong>Eindhoven University of Technology’s</strong> flagship award for outstanding new Master’s students, tied to the university’s microchip-innovation agenda and funded through the Dutch government’s national <strong>Beethoven Program</strong>. For the <strong>2027–2028 academic year</strong>, roughly <strong>35 awards</strong> are expected: <strong>20 for EEA students and 15 for non-EEA students</strong>. Each award is <strong>€7,500 per academic year for up to two years</strong> (total €15,000), paid in <strong>monthly instalments</strong> to a Dutch or SEPA bank account. For non-EEA recipients, part of the first year’s funding comes through the national <strong>NL Scholarship</strong> (formerly the Holland Scholarship) — you do <strong>not</strong> apply to that separately, and applying to it yourself is not allowed.</p>
      <p><strong>Be clear-eyed about what it is:</strong> this is <strong>explicitly a partial scholarship</strong>. It does not cover full tuition or living costs — recipients are expected to fund the remainder themselves, and non-EEA recipients must still demonstrate <strong>sufficient funds for the Dutch entry visa/residence permit</strong>. Some aggregator blogs falsely describe it as full tuition plus a monthly living stipend; the official TU/e page contradicts that. The second year’s payment is conditional: you need <strong>at least 45 ECTS in the first year</strong> and must graduate within 36 months. Selection results come <strong>by the end of March 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Applied for an eligible full-time TU/e Master’s program</strong> starting <strong>1 September 2027</strong> in: Applied Physics; Electrical Engineering; Mechanical Engineering; or Mathematics &amp; Computer Science — including the eligible tracks (Applied Physics; Artificial Intelligence and Engineering Systems; Automotive Technology; Computer Science and Engineering incl. Cybersecurity and Systems/AI tracks; Data Science and AI; Embedded Systems; Industrial and Applied Mathematics incl. Quantum Science &amp; Technology and AI Fundamentals tracks; Mechanical Engineering incl. Aerospace Systems Engineering track; Science and Technology of Nuclear Fusion; Sustainable Energy Technology; Systems and Control).</li>
        <li><strong>Meet the specific admission requirements</strong> of that Master’s program.</li>
        <li><strong>Hold or be completing a non-Dutch high school diploma and/or university bachelor’s degree</strong> (exchange programmes in the Netherlands are allowed; completed Dutch higher education is not).</li>
        <li><strong>Latest transcript GPA of at least 7.5/10.</strong></li>
        <li><strong>Meet Dutch entry visa/residence permit requirements</strong> — including proof of sufficient funds despite the award.</li>
        <li><strong>Not</strong> applying for the joint Master’s with Tilburg University (JADS) or a European Double Degree program.</li>
        <li><strong>Not</strong> relying on an admission decision from a previous intake.</li>
        <li><strong>Very competitive:</strong> TU/e states only about 2% of applicants receive it; selection outcomes cannot be appealed, and awards cannot be deferred.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€7,500 per academic year</strong>, for up to two years (total <strong>€15,000</strong>).</li>
        <li>Paid in <strong>monthly instalments</strong> to a Dutch or SEPA bank account.</li>
        <li>Roughly <strong>35 awards</strong> per year (20 EEA / 15 non-EEA).</li>
        <li>First year of non-EEA awards includes <strong>NL Scholarship</strong> funding — no separate application needed or allowed.</li>
        <li>Second-year payment requires <strong>≥45 ECTS in year 1</strong> and graduation within 36 months.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>There is no separate scholarship document list — you are considered inside the standard Master’s application. Candidates must submit the <strong>complete Master’s program application</strong> via the TU/e application system (Studielink/OSIRIS) <strong>with a brief motivation statement confirming scholarship interest</strong>. Program-standard documents (transcripts, degree certificate, CV, passport, English-language proof per your chosen program’s admission requirements) are listed by aggregators only and are not confirmed on the official scholarship page.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for an eligible full-time Master’s program/track</strong> at TU/e for the 2027–2028 intake (start 1 September 2027).</li>
        <li><strong>Submit the complete application by 1 January 2027, 23:59 CET.</strong></li>
        <li><strong>Within the application, confirm you wish to be considered for the scholarship</strong> and include a <strong>brief motivation statement</strong> on why you are a strong candidate.</li>
        <li><strong>Wait for the selection process:</strong> the TU/e International Office checks eligibility after the deadline, the Scholarship Selection Committee ranks applications, and selected candidates are informed <strong>by the end of March 2027</strong> and sign a scholarship agreement.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the TU/e Excellence scholarship fully funded?","No — and this matters. The official page describes it explicitly as a partial award: €7,500 per year for two years, which does not cover full tuition or living costs. Blogs claiming full tuition coverage plus a monthly living stipend contradict the university’s own page."),
 ("Do I need to apply separately for the NL Scholarship?","No. For non-EEA recipients, part of the first year’s award is funded through the national NL Scholarship (formerly Holland Scholarship) automatically — do not file a separate NL Scholarship application."),
 ("What GPA do I need?","A latest transcript GPA of at least 7.5/10, plus a non-Dutch high school diploma and/or bachelor’s degree. Only about 2% of applicants receive the award."),
 ("When will I hear the result?","Selected candidates are informed by the end of March 2027 and sign a scholarship agreement. Decisions cannot be appealed and the award cannot be deferred."),
 ("Does the award continue into the second year?","Yes, provided you earn at least 45 ECTS in the first year and graduate within 36 months."),
]),
 offlinks=[('TU/e Scholarship for Excellence — Eindhoven University of Technology (official)','https://www.tue.nl/en/education/become-a-tue-student/scholarships-and-grants/tue-scholarship-for-excellence-shaping-the-future-of-microchip-innovation')],
 related_titles=['each','hanns-seidel','keio-adb'],
 verify='Verified 17 Oct 2026 via the official TU/e scholarship page (deadline 1 Jan 2027 23:59 CET; €7,500/academic year × up to 2 years; ~35 awards, 20 EEA/15 non-EEA; explicitly partial; GPA ≥7.5/10; non-Dutch diploma; eligible MSc tracks; second-year ≥45 ECTS rule; NL Scholarship first-year mechanism; results by end of March 2027), corroborated by youthexpat, scholarshipunion, afterschoolafrica and daadscholarship trackers. Aggregator claims of full tuition coverage + monthly living stipend are false per the official page and are not repeated here.'),

# ---------------------------------------------------------------- 4. Tilburg
dict(
 slug='tilburg-university-research-master-scholarship-2027-netherlands',
 title='Tilburg University Research Master Scholarship 2027 in Netherlands (Tuition Waiver) | StudyDesk Scholarships',
 meta="Tilburg University Research Master Scholarship 2027: full 2-year tuition-fee waiver for the Research Master in Communication, Cognition and Digital Culture. Deadline 1 Apr 2027. Eligibility and application guide.",
 short='Tilburg Research Master Scholarship 2027', kicker='Netherlands · Master’s · Tuition-fee waiver',
 mono='T', prov_short='Tilburg University',
 h1='Tilburg University Research Master Scholarship 2027 in the Netherlands',
 sub='Tilburg University offers up to three Research Master Scholarships per cohort: a tuition-fee waiver covering the full two years of the research master — a serious award with no living stipend attached. It is aimed at outstanding non-EEA students starting their first Dutch master’s, plus exceptional students with a prior Dutch master’s degree. The complete program application must be in before 1 April 2027.',
 dpill='166 days to go', dl_long='1 Apr 2027, 23:59 CET (complete program application)',
 facts=facts([('Award','Tuition-fee waiver, 2 years<small>Covers the full two-year duration of the Research Master; the waiver is lost if study is delayed beyond 2 years; maximum 3 waivers per cohort</small>'),
              ('No living stipend','Tuition only<small>No living-expense allowance is advertised — plan your own funding for living costs; exact euro reduction figures are not published on the official page</small>'),
              ('Program','Research Master in Communication, Cognition and Digital Culture<small>The detailed official page names this program; September start only — February starters are ineligible</small>'),
              ('Who','Outstanding students<small>Non-EEA students pursuing their first master’s in the Netherlands, or exceptional students (any citizenship) with a previous master’s from the Netherlands</small>'),
              ('Timeline','Apply by 1 Apr 2027<small>Qualifying candidates are interviewed online in May/June; notified in the third week of June; award letter must be signed and returned by 1 July</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Tilburg University</strong> in the Netherlands awards the <strong>Research Master Scholarship</strong>: a <strong>tuition-fee waiver covering the full two-year duration of the Research Master</strong>, with a <strong>maximum of three waivers per cohort</strong>. The detailed official page describes the scheme for the <strong>Research Master in Communication, Cognition and Digital Culture</strong>, for the <strong>2027 intake</strong> (listed on the university’s 2027–2028 scholarships &amp; waivers overview). It is a pure tuition award: <strong>no living stipend is advertised</strong>, so you will need to fund your own living costs in Tilburg. The waiver is lost if your study is delayed beyond the two years.</p>
      <p><strong>Read the scope carefully:</strong> some aggregator sites describe this as “fully funded” and imply it covers every research master and all nationalities. The official detailed page is narrower — it names the Communication, Cognition and Digital Culture program and sets two specific student categories (see eligibility). There is also a <strong>separate CentER Scholarship</strong> (€10,800/year, February deadline) for the Research Master in Economics — a different award that is not part of this scheme and must not be confused with it. Exact euro figures for the fee reduction circulate on aggregator sites only and are <strong>not published on the official page</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Program:</strong> the Research Master in <strong>Communication, Cognition and Digital Culture</strong> at Tilburg University (per the detailed official page).</li>
        <li><strong>Two applicant categories:</strong> (1) <strong>outstanding non-EEA students</strong> pursuing their <strong>first master’s degree in the Netherlands</strong>; (2) <strong>exceptional students with a previous master’s degree from the Netherlands</strong> (Dutch, EEA and non-EEA citizens).</li>
        <li><strong>September start only:</strong> February starters are <strong>ineligible</strong>.</li>
        <li><strong>Program admission:</strong> you must meet the program’s admission requirements (prior education and English-language proficiency).</li>
        <li><strong>Selection criteria:</strong> general eligibility, academic quality and potential, fit with the program, and your motivation letter.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition-fee waiver</strong> for the entire two-year Research Master.</li>
        <li><strong>Maximum three waivers</strong> awarded per cohort — a very small intake.</li>
        <li>Waiver <strong>lost if study is delayed beyond two years</strong>.</li>
        <li><strong>No living stipend</strong> is part of the award — budget living costs separately.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>No separate scholarship document list is published — the official page requires you to meet the admission requirements and submit a <strong>complete program application including the motivation letter</strong> before the deadline. The full document list lives on the per-program admission page.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to the eligible Research Master program</strong> at Tilburg University (aggregators note Studielink registration, then OSIRIS Aanmeld; the official page links through to the program’s own application and admission website).</li>
        <li><strong>Submit the complete program application before 1 April, 23:59 CET.</strong> Note that admission processing can take <strong>at least 6 weeks</strong> — do not start at the end of March.</li>
        <li><strong>Qualifying candidates are interviewed online in May/June</strong> and <strong>notified by email in the third week of June</strong>.</li>
        <li><strong>Sign and return the award letter by 1 July.</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Does the scholarship cover living expenses?","No. It is a tuition-fee waiver only — there is no living stipend in the official description. Sites calling it “fully funded” are overstating it."),
 ("How much is the tuition reduction in euros?","The official pages give no euro figures, so none is stated here. Aggregator figures are not from the university — treat them with caution."),
 ("Which programs does it cover?","The detailed official page names the Research Master in Communication, Cognition and Digital Culture. It does not cover the separate CentER Economics scholarship, which is a different award."),
 ("Can February-start students apply?","No — September start only."),
 ("How many scholarships are given?","A maximum of three waivers per cohort."),
]),
 offlinks=[('Research Master Scholarship — Tilburg University (official)','https://www.tilburguniversity.edu/education/masters-programmes/tuition-fees-scholarships/research-master-scholarship')],
 related_titles=['each','ursinus','hanns-seidel'],
 verify='Verified 17 Oct 2026 via the official Tilburg University Research Master Scholarship page (deadline 1 Apr, 23:59 CET; 2027 intake on the 2027–28 scholarships overview; tuition-fee waiver for the full 2-year Research Master, max 3 per cohort; no living stipend; non-EEA first-master / exceptional Dutch-master categories; September start only; interviews May/June, notified third week of June, award letter by 1 July), corroborated by 3 aggregator trackers. Exact fee-reduction euro figures are not published on the official page and are not stated here; the separate CentER Economics scholarship is not merged into this scheme.'),

# ---------------------------------------------------------------- 5. ANZ
dict(
 slug='anz-summer-internship-program-2027-australia',
 title='ANZ Summer Internship Program 2027 in Australia (Paid) | StudyDesk Scholarships',
 meta="ANZ Summer Internship Program 2027/28: paid 8–10 week summer internships in Melbourne, Sydney and Brisbane starting Nov 2027. EOI open now; formal applications expected June/July 2027. Eligibility and process.",
 short='ANZ Summer Internship 2027', kicker='Australia · Paid internship · ANZ',
 mono='ANZ', prov_short='Australia and New Zealand Banking Group (ANZ)',
 h1='ANZ Summer Internship Program 2027 in Australia',
 sub='ANZ runs one of Australia’s big bank internships: an 8–10 week paid summer program across Melbourne, Sydney and Brisbane, with a graduate buddy, professional development, and a possible early offer into the ANZ Graduate Program. Right now it is at the Expression of Interest stage — there is no application deadline yet, and formal applications are expected around June/July 2027.',
 dpill='EOI open now', dl_long='Not published — Expression of Interest open now (formal applications expected June/July 2027; internships start Nov 2027)',
 facts=facts([('What it is','Paid summer internship, 8–10 weeks<small>Professional development + a graduate buddy + potential early offer into the ANZ Graduate Program; accommodation/airfare support not mentioned</small>'),
              ('Stage','Expression of Interest open<small>No deadline published for the EOI; ANZ contacts registrants when formal applications open (expected June/July 2027)</small>'),
              ('Who','AU/NZ citizens or permanent residents<small>Penultimate (second-last) year of a bachelor’s or postgraduate degree; digitally savvy and data literate; no banking background required</small>'),
              ('Locations','Melbourne, Sydney, Brisbane<small>Streams: Agribusiness, Australia Retail Banking, Business & Private Bank, Institutional, Technology, Finance</small>'),
              ('Start','November 2027<small>The 2027/28 summer intake commences November 2027</small>')]),
 body='''
      <h2 id="about">About the program</h2>
      <p>The <strong>ANZ Summer Internship Program</strong> is the <strong>Australia and New Zealand Banking Group’s</strong> flagship summer intake: a <strong>paid internship of 8–10 weeks</strong> in the <strong>2027/28 cycle, commencing November 2027</strong>, across <strong>Melbourne, Sydney and Brisbane</strong>. Interns get <strong>professional development, a graduate buddy</strong>, and a real shot at an <strong>early offer into the ANZ Graduate Program</strong>. Available <strong>streams</strong> include Agribusiness, Australia Retail Banking, Business &amp; Private Bank, Institutional, Technology and Finance. Note the framing: this is <strong>paid employment, not a scholarship award</strong> — it is a proper paid internship, and accommodation, airfare or living-expense support are <strong>not mentioned anywhere</strong>, so they must not be assumed.</p>
      <p><strong>Where it stands right now:</strong> the 2027/28 Australian intake is at the <strong>Expression of Interest (EOI) stage</strong>, not formal application — so <strong>no application deadline has been published</strong>. ANZ will contact registrants when formal applications open, which is <strong>expected around June/July 2027</strong> (an expected opening, not a confirmed deadline). Some aggregator sites describe it as open to “international students” — that is misleading: ANZ requires <strong>Australian or New Zealand citizenship, or permanent residency</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizenship/residency:</strong> citizen of, or permanent resident in, <strong>Australia or New Zealand</strong>. Other international students should check work rights carefully — ANZ’s requirement is AU/NZ citizenship or PR.</li>
        <li><strong>Year of study:</strong> in your <strong>penultimate (second-last) year</strong> of a bachelor’s or postgraduate degree.</li>
        <li><strong>Attributes:</strong> digitally savvy, data literate, and able to learn from challenges and setbacks.</li>
        <li><strong>No banking background required:</strong> there is no requirement to have studied banking or finance — diverse academic backgrounds are welcome.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Paid internship</strong> for 8–10 weeks (specific salary not published on the official page).</li>
        <li><strong>Professional development</strong> and a <strong>graduate buddy</strong>.</li>
        <li><strong>Potential early offer</strong> into the ANZ Graduate Program.</li>
        <li>Exposure across real banking streams — Agribusiness, Retail, Business &amp; Private Bank, Institutional, Technology, Finance.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>No document list has been released for the Expression of Interest stage — “not published in the official notification”. Prepare the usual graduate-recruitment basics (CV, academic transcript) for when formal applications open.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Submit an Expression of Interest now</strong> via the official ANZ careers page (the 2027/28 AU Summer Intern Program listings appear on gradconnection and the ANZ careers site).</li>
        <li><strong>ANZ contacts registrants</strong> when formal applications open — expected <strong>June/July 2027</strong>.</li>
        <li><strong>Formal recruitment</strong> (per ANZ’s official process): quick online application → digital interview and game-based assessment → personality questionnaire → interview preparation → face-to-face interview.</li>
        <li>Internships <strong>commence November 2027</strong> in Melbourne, Sydney or Brisbane.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this a scholarship?","No — it is a paid employment internship. It should not be framed as a scholarship award; the value is paid work experience, development and a possible fast-track into ANZ’s graduate program."),
 ("Is there a deadline right now?","No. The intake is at the Expression of Interest stage with no published closing date. Formal applications are expected to open around June/July 2027."),
 ("Can international students apply?","ANZ requires Australian or New Zealand citizenship, or permanent residency in Australia or New Zealand. Sites presenting it as broadly open to international students are misleading."),
 ("Which degree backgrounds does ANZ want?","All of them — there is no requirement to have studied banking or finance. You need to be in your penultimate year, digitally savvy and data literate."),
 ("Where are the internships based?","Melbourne, Sydney and Brisbane, across streams including Technology, Finance, Institutional, Agribusiness, Australia Retail Banking and Business & Private Bank."),
]),
 offlinks=[('ANZ Summer Internship Program — ANZ careers (official)','https://www.anz.com.au/careers/career-programs/summer-internship/')],
 related_titles=['epfl-summer','wb-gaf','zonta-ae'],
 verify='Verified 17 Oct 2026 via ANZ’s official careers page and ANZ’s official LinkedIn post on the 2027 intake EOI (paid 8–10 week program; EOI stage with no published deadline; formal applications expected June/July 2027; internships start Nov 2027; AU/NZ citizenship or PR required; penultimate-year students; Melbourne/Sydney/Brisbane; six streams; game-based assessment recruitment flow), corroborated by gradconnection and multiple independent trackers. It is a paid employment internship, not a scholarship; salary, accommodation and airfare figures are not published and are not stated here.'),

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

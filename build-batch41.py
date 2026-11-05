#!/usr/bin/env python3
"""Batch 41 (cron run 41, 23 Oct 2026): 5 new verified articles.

Queue scan: the 5 stale bright topics batch 40 meant to skip (GOIIES 2026 closed
12 Mar 2026; Commonwealth Split-site 2025-26 closed 16 Dec 2024; Obama Scholars
2025-26 closed 16 Dec 2024; SUSI 2025 closed 11 Nov 2024; Google STEP 2025 closed
25 Oct 2024) resurfaced as pending — batch 40 recorded them in tracker prose but
never persisted them to queue-progress.json's skipped list. Re-verified closed
this run and skipped with EXACT queue titles, then continued in queue order.

WRITES (queue titles were stale 2023-24/2024-25 editions; articles written for
the live 2026-27/2027 cycles and state the cycle explicitly, batch-39 precedent):
1. Pierre Elliott Trudeau Scholarship 2027 in Canada (Fully Funded) — 2027
   competition; eligibility screening closed 2 Oct 2026, complete applications
   due 6 Nov 2026 4pm ET; up to $50k/yr + $20k/yr research allowance x3 yrs.
2. HDFC Bank Parivartan ECSS Programme 2026-27 in India (up to Rs.75,000) —
   deadline 31 Oct 2026; Rs.15,000-75,000 by level; 55%+, income <= Rs.2.5L.
3. UN Young Professionals Programme (YPP) 2026 — Development and Sustainability
   exam; applications 16 Oct - 30 Nov 2026; <=32 yrs, bachelor's, EN/FR fluent.
4. Florida Bright Futures Scholarship 2026-27 in USA (Funded) — FFAA window
   1 Oct 2026 - 31 Aug 2027 for 2026-27 graduates; FAS 100% / FMS 75% tuition.
5. UP Scholarship 2026-27 Online Apply — Dashmottar fresh till 31 Oct 2026,
   renewal till 15 Oct 2026 (Classes 9-12 windows closed); scholarship.up.gov.in.

SKIPS this run (40): the 5 re-verified stale topics above + Oxford PLC 2025
(2025 edition concluded) + MENA 2025 (deadline passed 6 May 2025) + HSE 2025
(deadline passed 5 Nov 2024) + Australia Awards Fellowship 2025 (Round 21 closed
16 Jan 2026) + YSEALI PFP 2025 (deadline passed 17 Oct 2024) + Global UGRAD 2025
(deadline passed 15 Dec 2024; 2026-27 cycle not yet announced) + NSTC IIPP 2025
(2026 cycle closed 15 Jul 2026) + British Council Scotland EARTH 2025 (deadline
passed 1 Nov 2024) + both Vanier entries (programme discontinued after fall
2024; replaced by CGRS-D) + Universal Youth Leadership Summit 2024 (event
concluded) + 8th Arab European Youth Forum 2024 (event concluded) + Turkish
Government Success Scholarship 2024 (2024 edition concluded; current Basari
Burs cycle not announced) + Hurford Youth Fellowship 2025 (2026 cycle closed
31 Jul 2026) + Jumeirah Group Trainee Program 2024 (2024 intake concluded) +
Asia Foundation Development Fellowship 2025 (2026 cycle closed 10 Nov 2025) +
KAIST Electrical Engineering Camp 2024 (2024 edition concluded) + Berlin
Summer Courses 2024 (2024 edition concluded) + HIT China Link Scholarship
2024-25 (Link Scholarship 2025 closed Apr 2025) + Arqus Talent Scholarship
2024-25 (scheme funding ended 30 Sep 2026) + Fulbright Tampere 2024 (2024 cycle
concluded) + Edinburgh Global Masters 2024-25 (2026-27 cycle closed Jun 2026)
+ Sheffield GREAT Egyptians 2024 (2024 edition concluded) + Nurse Corps
2024-25 (2024-25 cycle concluded) + Awaji Youth Federation Fellowship 2024
(AYF 2026 cycle closed 31 Dec 2025) + Google Lime Scholarship 2024-25 (2024-25
cycle concluded) + Top 10 Nursing Scholarships 2024 (listicle, not a scheme) +
Dali University CSC Scholarship 2024-25 (CSC 2025 cycle closed) + List of Top
MBBS Scholarships 2024-25 (listicle, not a scheme) + McDonald Fellowship 2024
(2024 cycle concluded) + Alberta MBA Scholarships 2024 (2024 cycle concluded) +
IU International ad (not a scholarship - promotional content).

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re

def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'trudeau-2027': {'mono': 'PET', 'title': 'Pierre Elliott Trudeau Scholarship 2027 in Canada (Fully Funded)',
   'href': 'pierre-elliott-trudeau-scholarship-2027-canada.html',
   'dpill': 'Deadline 6 Nov 2026 \u00b7 14 days left',
   'award': 'Up to $50,000/yr stipend + up to $20,000/yr research, travel and networking allowance for 3 years (up to $210,000 total) + a 3-year leadership program with mentors and fellows.',
   'elig': '1st/2nd-year doctoral students in humanities and social sciences; Canadian citizens (any university worldwide) or international students enrolled at a Canadian university; research aligned with one of the Foundation\u2019s four themes.',
   'tags': [('PhD', 'purple'), ('Canada', 'teal')]},
 'hdfc-ecss-2026-27': {'mono': 'HDFC', 'title': 'HDFC Bank Parivartan ECSS Programme 2026-27 in India (Scholarship up to \u20b975,000)',
   'href': 'hdfc-bank-parivartan-ecss-programme-2026-27-india.html',
   'dpill': 'Deadline 31 Oct 2026 \u00b7 8 days left',
   'award': '\u20b915,000 (Class 1\u20136) / \u20b918,000 (Class 7\u201312, diploma, ITI, polytechnic) / \u20b930,000 (UG general) / \u20b950,000 (UG professional) / \u20b935,000 (PG general) / \u20b975,000 (PG professional).',
   'elig': 'Indian nationals from Class 1 to PG with 55%+ marks and annual family income up to \u20b92.5 lakh; preference for students hit by a family or personal crisis in the last 3 years.',
   'tags': [('All levels', 'blue'), ('India', 'teal')]},
 'un-ypp-2026': {'mono': 'UN', 'title': 'UN Young Professionals Programme (YPP) 2026 (Careers)',
   'href': 'un-young-professionals-programme-ypp-2026.html',
   'dpill': 'Deadline 30 Nov 2026 \u00b7 38 days left',
   'award': 'A pathway into the UN Secretariat: successful candidates join a 3-year roster for entry-level P-1/P-2 professional posts (normally a 2-year initial contract) after a competitive written exam and interview.',
   'elig': 'Nationals of the 47 participating member states; 32 or younger in 2026 (born on/after 1 Jan 1994); a bachelor\u2019s degree in a relevant field; fluent English or French. No work experience required.',
   'tags': [('Careers', 'purple'), ('Global', 'teal')]},
 'florida-bf-2026-27': {'mono': 'BF', 'title': 'Florida Bright Futures Scholarship 2026-27 in USA (Funded)',
   'href': 'florida-bright-futures-scholarship-2026-27-usa.html',
   'dpill': 'FFAA open 1 Oct 2026 \u2013 31 Aug 2027',
   'award': 'Florida Academic Scholars (FAS): 100% tuition and fees at Florida public institutions. Florida Medallion Scholars (FMS): 75% tuition. A statutory entitlement \u2014 meet the checklist and the award follows.',
   'elig': 'Florida residents (US citizens/eligible noncitizens) graduating from a Florida high school in 2026-27 with the required GPA, test scores and service hours; enrolment at an eligible Florida institution.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'up-scholarship-2026-27': {'mono': 'UP', 'title': 'UP Scholarship 2026-27 Online Apply | Scholarship UP Online',
   'href': 'up-scholarship-2026-27-online-apply.html',
   'dpill': 'Fresh: 31 Oct 2026 \u00b7 8 days left',
   'award': 'Post-matric assistance of roughly \u20b9230\u2013\u20b91,200 per month and pre-matric \u20b93,000\u2013\u20b97,000 per year (category-dependent), paid by Direct Benefit Transfer to an Aadhaar-seeded bank account.',
   'elig': 'UP-domicile students (General, OBC, SC, ST, minority) enrolled in eligible institutions; family income up to \u20b92 lakh (General/OBC) or \u20b92.5 lakh (SC/ST).',
   'tags': [('All levels', 'blue'), ('India', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Trudeau
A.append(dict(
 slug='pierre-elliott-trudeau-scholarship-2027-canada',
 title='Pierre Elliott Trudeau Scholarship 2027 in Canada (Fully Funded)',
 meta='Pierre Elliott Trudeau Scholarship 2027: up to $50,000/year plus $20,000/year research allowance for 3 years for doctoral students in Canada. Complete applications due 6 November 2026 — eligibility, themes, documents and how to apply.',
 short='Trudeau Scholarship 2027', kicker='Canada \u00b7 PhD \u00b7 Fully Funded', mono='PET',
 prov_short='Pierre Elliott Trudeau Foundation', prov_cat='Foundation \u00b7 Canada',
 h1='Pierre Elliott Trudeau Scholarship 2027 in Canada (Fully Funded)',
 sub='A three-year leadership program plus generous doctoral funding: the Pierre Elliott Trudeau Foundation supports outstanding PhD researchers in the humanities and social sciences with up to $50,000 a year for living costs and up to $20,000 a year for research, travel and networking.',
 dpill='Deadline 6 Nov 2026 \u00b7 14 days left',
 facts=facts([('Award', 'Up to $50,000 per year for three years for tuition and living expenses, plus up to $20,000 per year for three years for research travel, networking, Foundation events and official-language training — a total package of up to $210,000. Scholars also join a three-year leadership program with mentors, fellows and an alumni community. Even scholars holding other funding keep at least $25,000 of the stipend plus the full $20,000 allowance.'),
              ('Eligible', 'Doctoral students in their first or second year at the time of application, working in the humanities and social sciences broadly (including business, public-health and law research that fits the themes). Canadian citizens and permanent residents may study at any university worldwide; international students must be enrolled at a Canadian university. Research must relate to at least one of the Foundation\u2019s four themes: Human Rights and Dignity; Responsible Citizenship; Canada and the World; People and their Natural Environment. Applications may be written in English or French.'),
              ('How', 'New two-step process for 2027: first complete the online eligibility-verification form (this step closed 2 October 2026); confirmed candidates then attend a mandatory information session and submit the full application directly to the Foundation — no university nomination is required. You need three referees: your PhD supervisor, one additional academic referee, and one referee from outside academia. References are due 30 October 2026 at 9:00 a.m. ET.'),
              ('Deadline', 'Complete applications: 6 November 2026 at 4:00 p.m. ET. References: 30 October 2026 at 9:00 a.m. ET. The Foundation\u2019s own page frames the 2027 application window as 1 September to 23 October 2026, so confirm the current status on trudeaufoundation.ca before relying on the later date.'),
              ('Fine print', 'About fifteen scholars are selected each year through group and individual interviews. If you did not complete the eligibility-verification step by 2 October 2026, you cannot enter the 2027 competition — treat this page as your briefing for the 2028 cycle instead.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Pierre Elliott Trudeau Foundation Scholarship</strong> is one of Canada\u2019s most generous doctoral awards — and deliberately more than a cheque. Since 2001 the Foundation has built a community of scholars, fellows and mentors around a single idea: train engaged leaders who can turn research into action for their communities, Canada and the world. Each year a small cohort of doctoral researchers is selected for a <strong>three-year program</strong> that combines substantial funding with leadership institutes, exchanges, networking events and one-to-one mentorship.</p>
      <p>The money is structured in two parts. The <strong>stipend of up to $50,000 per year</strong> covers tuition and living expenses during doctoral research, while a separate <strong>allowance of up to $20,000 per year</strong> pays for research travel, networking, participation in Foundation events and improving knowledge of Canada\u2019s official languages. Over three years the package can reach <strong>$210,000</strong>. Importantly, the Foundation adjusts rather than cancels: scholars who hold other funding still receive at least $25,000 of the stipend plus the full $20,000 allowance.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be in the <strong>first or second year of a doctoral program</strong> at the time of application.</li>
        <li>Work in the <strong>humanities and social sciences</strong>, broadly understood — candidates from business schools, public-health schools and law faculties are welcome where the research fits the themes.</li>
        <li>Be a <strong>Canadian citizen or permanent resident</strong> studying at any university in the world, <strong>or</strong> an <strong>international student enrolled in a doctoral program at a Canadian university</strong>. International students at non-Canadian universities are not eligible.</li>
        <li>Have research related to <strong>at least one</strong> of the Foundation\u2019s four themes: <strong>Human Rights and Dignity; Responsible Citizenship; Canada and the World; People and their Natural Environment</strong>.</li>
        <li>Be able to communicate effectively in <strong>English or French</strong> (the application is completed in one language throughout).</li>
        <li>There is <strong>no age limit</strong>, and dual nationals are assessed under the standard citizenship rules published by the Foundation.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to $50,000 per year for three years</strong> for tuition and living expenses.</li>
        <li><strong>Up to $20,000 per year for three years</strong> for research travel, networking, Foundation events and official-language training.</li>
        <li>A <strong>three-year leadership program</strong>: institutes, exchanges and events with the Foundation\u2019s fellows and mentors.</li>
        <li><strong>Mentorship</strong> from accomplished professionals outside academia.</li>
        <li>Lifelong access to an <strong>alumni community</strong> of close to 600 scholars, fellows and mentors.</li>
        <li>Funding floor: scholars with other awards still keep <strong>at least $25,000 of the stipend plus the full $20,000 allowance</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed eligibility-verification form</strong> (step one of the 2027 process).</li>
        <li><strong>Full online application</strong> to the Foundation, in English or French.</li>
        <li><strong>Three references</strong>: your PhD supervisor, one additional academic referee, and one referee from outside academia. Referees may write in English or French and may live outside Canada.</li>
        <li><strong>Transcripts</strong> for all post-secondary education (you are responsible for ensuring the complete package reaches the Foundation).</li>
        <li><strong>Doctoral project description</strong>, essay responses on leadership and communication style, education and achievements record, and language-skills declaration.</li>
        <li>Confirmation that you have read the Foundation\u2019s <strong>key policies</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the 2027 two-step process</strong>The 2027 competition starts with an eligibility-verification form; only confirmed candidates can open the full application. That screening step closed on <strong>2 October 2026</strong>.</li>
        <li><strong>Attend the mandatory information session</strong>Eligible applicants are required to join an information session during the weeks of <strong>5 and 12 October 2026</strong>.</li>
        <li><strong>Line up three referees early</strong>Ask your supervisor, an academic referee and a non-academic referee well ahead of time — all references must arrive by <strong>30 October 2026 at 9:00 a.m. ET</strong>, and letters are submitted through the portal, not by email.</li>
        <li><strong>Complete the full application</strong>Fill in the Foundation\u2019s online form in one language (English or French), upload transcripts and project materials, and submit by <strong>6 November 2026 at 4:00 p.m. ET</strong>.</li>
        <li><strong>Apply directly to the Foundation</strong>Since the 2020 competition there is no department or university nomination stage — every eligible applicant applies directly, and universities may later be asked to confirm academic standing.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('The eligibility screening closed on 2 October 2026. Can I still apply for 2027?',
  'Almost certainly not. The 2027 competition uses a two-step process and only candidates whose eligibility was confirmed can access the full application. If you missed the screening, use this page to prepare for the 2028 competition instead.'),
 ('I am an international student. Can I apply?',
  'Yes, if you are enrolled in a doctoral program at a Canadian university. International students at universities outside Canada are not eligible; Canadian citizens and permanent residents may study anywhere.'),
 ('Does the scholarship cover my tuition fees?',
  'The stipend of up to $50,000 per year is meant to cover tuition and living expenses together; the separate $20,000 annual allowance covers research, travel and networking costs.'),
 ('Which fields count as humanities and social sciences?',
  'The Foundation interprets the fields broadly — candidates from business, public health and law are considered where their research clearly fits one of the four themes.'),
 ('Do I need to be bilingual in English and French?',
  'No. You need to communicate effectively in either English or French, and you complete the whole application in one of the two languages.'),
 ('How many scholars are selected?',
  'About fifteen scholars are selected each year through group interviews followed by individual interviews with the selection committee.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: trudeaufoundation.ca (official, crawled 23 Oct 2026) — 2027 application window 1 Sep to 23 Oct 2026, direct application, no university nomination quota; gradstudents.carleton.ca (43 days ago) — stipend up to $50,000/yr + up to $20,000/yr research allowance, references and full-application deadlines; opportunitiesforyouth.org (Sep 2026) — two-step process, eligibility verification deadline 2 Oct 2026, references 30 Oct 2026 9:00 a.m. ET, complete application 6 Nov 2026 4:00 p.m. ET, three referees (supervisor, academic, non-academic); greatyop.com — $25,000 stipend floor with other funding, Canadian/international enrolment rules, four themes; yorku.ca + enews.sgs.utoronto.ca — up to $210,000 total, ~15 scholars/yr. Queue title "Pierre Elliott Trudeau Scholarship 2025" retitled to the live 2027 competition; the 2025 and 2026 editions are closed.</p>
''',
 dl_long='November 6, 2026 (4:00 p.m. ET) — complete application; eligibility screening closed October 2, 2026',
 offlinks=[('Pierre Elliott Trudeau Foundation — official site', 'https://www.trudeaufoundation.ca/'),
           ('Carleton University — 2027 competition details', 'https://gradstudents.carleton.ca/pierre-elliott-trudeau-scholarship/')],
 related_titles=['ucalgary-2027', 'gates-cam-2027', 'nias-safehaven', 'monash-rtp'],
))

# ---------------------------------------------------------------- 2. HDFC ECSS
A.append(dict(
 slug='hdfc-bank-parivartan-ecss-programme-2026-27-india',
 title='HDFC Bank Parivartan ECSS Programme 2026-27 in India (Scholarship up to \u20b975,000)',
 meta='HDFC Bank Parivartan ECSS Programme 2026-27: merit-cum-need scholarship of Rs.15,000 to Rs.75,000 for Indian students from Class 1 to PG. Last date 31 October 2026 — eligibility, amounts, documents and how to apply.',
 short='HDFC Parivartan ECSS 2026-27', kicker='India \u00b7 All levels \u00b7 Up to \u20b975,000', mono='HDFC',
 prov_short='HDFC Bank', prov_cat='CSR \u00b7 India',
 h1='HDFC Bank Parivartan ECSS Programme 2026-27 in India (Scholarship up to \u20b975,000)',
 sub='HDFC Bank\u2019s Parivartan CSR initiative supports students who might otherwise drop out for financial reasons: a merit-cum-need scholarship paying Rs.15,000 to Rs.75,000 a year to Indian students from Class 1 all the way through postgraduate studies. Applications for 2026-27 close 31 October 2026.',
 dpill='Deadline 31 Oct 2026 \u00b7 8 days left',
 facts=facts([('Award', 'Class 1 to 6: Rs.15,000. Class 7 to 12, diploma, ITI and polytechnic: Rs.18,000. Undergraduate (general courses): Rs.30,000. Undergraduate (professional courses): Rs.50,000. Postgraduate (general): Rs.35,000. Postgraduate (professional): Rs.75,000. The money can be used for tuition and examination fees, books, stationery, travel and other study costs; selected students may receive support in later years of the same course if they keep meeting the eligibility rules. 6,553 scholars were selected in 2025-26.'),
              ('Eligible', 'Indian nationals currently enrolled in Class 1 to 12, diploma, ITI, polytechnic, undergraduate or postgraduate courses at recognised private, government or government-aided institutions. Minimum 55% marks in the most recent qualifying examination. Annual family income from all sources not above Rs.2.5 lakh. Preference is given to students who faced a personal or family crisis in the last three years that hurt their ability to pay for education. Diploma applicants must have joined the diploma after completing Class 12.'),
              ('How', 'Apply online only, through the Buddy4Study portal (parivartanecss.com). Fill the online form with academic, personal and family-income details, upload scanned documents, preview carefully and submit. Selection is multi-stage: shortlisting on eligibility, document verification, and a personal interview for shortlisted candidates.'),
              ('Deadline', '31 October 2026. Applications for the 2026-27 session opened on 6 August 2026. There is no application fee.'),
              ('Fine print', 'Three separate application tracks exist — school, undergraduate and postgraduate — each with its own form and award slabs; apply under exactly one, matching your current level of study.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Parivartan ECSS (Educational Crisis Scholarship Support) Programme</strong> is HDFC Bank\u2019s flagship scholarship under its <strong>Parivartan</strong> corporate social responsibility initiative. It rests on one conviction: no student should have to abandon school or college because of a financial crisis at home. It is a <strong>merit-cum-need</strong> scholarship — academic performance opens the door, financial need decides who walks through it — and it is unusually wide in scope, covering students from <strong>Class 1 through postgraduate level</strong>, including diploma, ITI, polytechnic, and both general and professional degree courses.</p>
      <p>The programme is administered through <strong>Buddy4Study</strong> and applications are submitted entirely online. Since its launch it has supported thousands of students every year — <strong>6,553 scholars in 2025-26</strong>, 6,262 in 2024-25 and 7,684 in 2023-24 — making it one of India\u2019s largest private scholarships aimed at financially vulnerable students.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>Indian national</strong>.</li>
        <li>Be currently enrolled in <strong>Class 1 to 12</strong>, a <strong>diploma, ITI or polytechnic</strong> course, or a <strong>full-time undergraduate or postgraduate</strong> programme (general or professional) at a recognised institution in India. Private, government and government-aided institutions are all covered.</li>
        <li>Have secured at least <strong>55% marks</strong> in the most recent qualifying examination.</li>
        <li>Have an annual family income from all sources <strong>not above Rs.2.5 lakh</strong>.</li>
        <li><strong>Preference</strong> is given to applicants who faced a personal or family crisis in the last three years — such as a death, illness, or job loss in the family — that significantly affected their ability to continue studying.</li>
        <li>Diploma applicants must have enrolled in the diploma <strong>after completing Class 12</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Class 1 to 6:</strong> Rs.15,000 per year.</li>
        <li><strong>Class 7 to 12, diploma, ITI, polytechnic:</strong> Rs.18,000 per year.</li>
        <li><strong>Undergraduate (general — B.Com, B.Sc, B.A. etc.):</strong> Rs.30,000 per year.</li>
        <li><strong>Undergraduate (professional — B.Tech, MBBS, LLB, B.Arch, Nursing etc.):</strong> Rs.50,000 per year.</li>
        <li><strong>Postgraduate (general — M.Com, M.A. etc.):</strong> Rs.35,000 per year.</li>
        <li><strong>Postgraduate (professional — M.Tech, MBA etc.):</strong> Rs.75,000 per year.</li>
        <li>Funds may be used for <strong>tuition and examination fees, books, stationery, travel and other study costs</strong>.</li>
        <li>Support can <strong>continue into later years</strong> of the same course if eligibility is maintained.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Passport-size photograph.</strong></li>
        <li><strong>Previous year\u2019s marksheet</strong> (proof of the 55% requirement).</li>
        <li><strong>Identity proof</strong> — Aadhaar card, voter ID or driving licence.</li>
        <li><strong>Current-year admission proof</strong> — fee receipt, admission letter, institution ID card or bonafide certificate.</li>
        <li><strong>Family income proof</strong> — issued by the Gram Panchayat, Ward Counsellor, Sarpanch, SDM/DM/Tehsildar, or an affidavit.</li>
        <li><strong>Bank account details</strong> — cancelled cheque or passbook copy.</li>
        <li><strong>Proof of crisis, if applicable</strong> — medical records, death certificate, or job-loss documents.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick the right track</strong>The programme runs three separate applications — school, undergraduate and postgraduate. Choose the one matching your current level of study; you may apply under only one.</li>
        <li><strong>Register on the Buddy4Study portal</strong>Applications are submitted online at <strong>parivartanecss.com</strong> (the application link circulated for 2026-27 is <strong>www.b4s.in/yeks/HDFC63</strong>). Registration is free.</li>
        <li><strong>Fill the form carefully</strong>Enter academic, personal and family-income details exactly as they appear on your documents.</li>
        <li><strong>Upload scanned documents</strong>Attach clear scans of every document listed above, including income proof and crisis proof where relevant.</li>
        <li><strong>Preview and submit before 31 October 2026</strong>Check every field on the preview screen, accept the terms and submit. Take a printout of the submitted form for your records.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the last date for the HDFC Parivartan ECSS Programme 2026-27?',
  '31 October 2026. Applications for the 2026-27 session opened on 6 August 2026 and there is no application fee.'),
 ('How much money will I actually get?',
  'It depends on your level: Rs.15,000 for Classes 1 to 6; Rs.18,000 for Classes 7 to 12, diploma, ITI and polytechnic; Rs.30,000 for general UG; Rs.50,000 for professional UG; Rs.35,000 for general PG; and Rs.75,000 for professional PG courses.'),
 ('I scored 54%. Can I apply?',
  'No — 55% in the most recent qualifying examination is a hard eligibility line across all three tracks.'),
 ('My family income is Rs.3 lakh. Am I eligible?',
  'No. Annual family income from all sources must not exceed Rs.2.5 lakh.'),
 ('What counts as a family crisis?',
  'Events in the last three years such as the death or serious illness of an earning member, or a job loss, that significantly affected your ability to pay for education. Such applicants get preference, and you should attach supporting proof.'),
 ('Is there an interview?',
  'Yes, for shortlisted candidates: the selection process runs through eligibility shortlisting, document verification and a personal interview.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: coursejoiner.com (8 days ago) — 2026-27 session, deadline 31 Oct 2026, full amount slabs, 55% marks, Rs.2.5L income cap, Buddy4Study mode; shiksha.com (43 days ago) — three tracks with separate forms, full slab table, session 2026-27; agrijob.in (29 and 39 days ago) — applications opened 6 Aug 2026, parivartanecss.com portal, 6,553 scholars in 2025-26, income and marks rules; education.sakshi.com (8 days ago) — crisis preference (last 3 years), application link www.b4s.in/yeks/HDFC63, deadline 31 Oct 2026; assamtopper.com — school-track details, diploma-after-Class-12 rule. Queue title "HDFC Bank Parivartan ECSS Program 2024-25" retitled to the live 2026-27 programme.</p>
''',
 dl_long='October 31, 2026',
 offlinks=[('Shiksha — HDFC Scholarship 2026-27 guide', 'https://www.shiksha.com/college/articles/hdfc-scholarship-2026-27-eligibility-amount-last-date-and-how-to-apply-online-blogId-241309'),
           ('Sakshi Education — ECSS 2026-27 notification', 'https://education.sakshi.com/en/scholarships/education-news/hdfc-bank-parivartan-ecss-programme-2026-27-201288'),
           ('CourseJoiner — ECSS 2026-27 details', 'https://coursejoiner.com/scholarship/hdfc-parivartan-scholarship-2026/')],
 related_titles=['sdef', 'vidyadhan', 'dakshana', 'abcapital'],
))

# ---------------------------------------------------------------- 3. UN YPP
A.append(dict(
 slug='un-young-professionals-programme-ypp-2026',
 title='UN Young Professionals Programme (YPP) 2026 (Careers)',
 meta='UN Young Professionals Programme 2026: the Development and Sustainability exam is open 16 October to 30 November 2026. Eligibility (32 or younger, bachelor\u2019s degree, English/French), participating countries and how to apply via Inspira.',
 short='UN YPP 2026', kicker='Global \u00b7 Careers \u00b7 UN Secretariat', mono='UN',
 prov_short='United Nations', prov_cat='UN \u00b7 Worldwide',
 h1='UN Young Professionals Programme (YPP) 2026 (Careers)',
 sub='The United Nations\u2019 main entry route for young graduates is open: the 2026 Young Professionals Programme examines candidates in Development and Sustainability, and successful applicants join a roster for entry-level professional posts across the UN Secretariat. Applications close 30 November 2026.',
 dpill='Deadline 30 Nov 2026 \u00b7 38 days left',
 facts=facts([('Award', 'Not a scholarship for study — a competitive recruitment programme. Successful candidates are placed on a three-year roster and may be selected for entry-level Professional posts (P-1/P-2) across UN Secretariat duty stations (New York, Geneva, Vienna, Nairobi, Bangkok, Beirut, Santiago, Addis Ababa and others). The initial appointment is normally a two-year contract. There is no application fee.'),
              ('Eligible', 'Nationals of the 47 participating member states in 2026 (the country list changes every year to improve geographical representation — check the official YPP page for your country; India, Nigeria, Ghana, Kenya and South Africa are not on the 2026 list). 32 years old or younger in the examination year — born on or after 1 January 1994. A first-level university degree (bachelor\u2019s or equivalent three-year qualification) in a field relevant to the examination area. Fluency in English or French. No work experience is required.'),
              ('How', 'Apply online through the UN Inspira recruitment system against the 2026 Development and Sustainability job opening (ID 285586). The process runs: application screening, an online written examination, then interviews for those who pass. Only nationals of participating states can apply in a given year.'),
              ('Deadline', '30 November 2026. The application window opened on 16 October 2026.'),
              ('Fine print', 'The YPP is the UN Secretariat\u2019s programme — it does not cover specialised agencies, funds or programmes, which run their own young-professional schemes. Meeting the eligibility checklist does not guarantee an invitation to the written exam; applications are screened competitively.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>United Nations Young Professionals Programme (YPP)</strong> is the UN Secretariat\u2019s flagship route for bringing talented young graduates into international civil service. Each year the UN holds a <strong>competitive examination in one subject area</strong>, chosen according to the Secretariat\u2019s staffing needs. For <strong>2026 the examination area is Development and Sustainability</strong> — covering economic and social development, environmental protection, population affairs and sustainable development.</p>
      <p>This is a <strong>career opportunity, not a study scholarship</strong>: there is no tuition funding and no degree attached. Instead, candidates who clear the written examination and interview are placed on a <strong>roster</strong> that the UN uses when entry-level Professional vacancies arise. It is the closest thing the UN system has to a graduate scheme, and for many young professionals it is the first rung of a career across the Secretariat\u2019s duty stations worldwide.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>national of a participating member state</strong> for the 2026 cycle. Only 47 countries take part this year, and the list is built from states under-represented among UN staff — it changes annually. <strong>India, Nigeria, Ghana, Kenya and South Africa are not on the 2026 list</strong>; in Africa only Angola, Equatorial Guinea, Liberia, Libya and S\u00e3o Tom\u00e9 and Pr\u00edncipe can apply this year. Always confirm your country on the official YPP page.</li>
        <li>Be <strong>32 years old or younger</strong> in the examination year — born on or after <strong>1 January 1994</strong>.</li>
        <li>Hold at least a <strong>first-level university degree</strong> (a bachelor\u2019s degree or equivalent three-year qualification) in a field relevant to Development and Sustainability — such as economics, statistics, social sciences, environmental studies or sustainable development.</li>
        <li>Be <strong>fluent in English or French</strong>, the two working languages of the programme.</li>
        <li><strong>No work experience is required</strong> — the programme is designed for recent graduates.</li>
      </ul>
      <h2 id="benefits">What successful candidates get</h2>
      <ul>
        <li>A place on the <strong>YPP roster for three years</strong>, from which the UN selects for entry-level vacancies.</li>
        <li>Eligibility for <strong>P-1 and P-2 Professional posts</strong> across Secretariat duty stations worldwide.</li>
        <li>A <strong>normally two-year initial contract</strong> on recruitment, with the UN\u2019s professional development framework.</li>
        <li>A structured path into <strong>international civil service</strong> — the YPP exists precisely to improve the geographical representation of member states, so rostered candidates from participating countries are genuinely in demand.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>UN Inspira personal history profile</strong> — the UN\u2019s standard online application, completed in full.</li>
        <li><strong>Degree certificate(s)</strong> proving a first-level university degree in a relevant field.</li>
        <li>Evidence supporting <strong>nationality</strong> of a participating member state.</li>
        <li>Any documents the specific <strong>job opening (ID 285586)</strong> requests — read the vacancy notice on Inspira before you start.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm your country participates in 2026</strong>Check the official YPP examination information at <strong>careers.un.org/ypp</strong>. If your nationality is not on the 2026 list, you cannot apply this year.</li>
        <li><strong>Read the 2026 vacancy notice</strong>Open job opening <strong>285586</strong> (Development and Sustainability) and check the exact list of accepted degree subjects and any additional instructions.</li>
        <li><strong>Create or update your Inspira profile</strong>Complete the UN\u2019s Personal History Profile carefully — this is the application itself, and incomplete profiles are screened out.</li>
        <li><strong>Submit before 30 November 2026</strong>Applications are free. Apply well before the deadline; late submissions are not accepted.</li>
        <li><strong>Prepare for the written examination</strong>Screened candidates sit an online written assessment, followed by interviews for those who pass. Read the YPP exam guide materials while you wait.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the UN YPP a scholarship?',
  'No. It does not fund any degree. It is a competitive recruitment programme that can lead to paid entry-level Professional employment with the UN Secretariat.'),
 ('Can I apply if my country is not participating in 2026?',
  'No. Only nationals of the participating member states can apply in a given cycle, and the list changes every year. India, Nigeria, Ghana, Kenya and South Africa are not on the 2026 list.'),
 ('Do I need work experience?',
  'No. The YPP is designed for young graduates; a relevant bachelor\u2019s degree, the right age and nationality, and fluency in English or French are the core requirements.'),
 ('What happens after I pass the exam?',
  'You are placed on a three-year roster. When suitable P-1/P-2 vacancies arise, rostered candidates may be selected — the initial appointment is normally a two-year contract.'),
 ('Which duty stations could I be posted to?',
  'The 2026 job opening lists duty stations including New York, Geneva, Vienna, Nairobi, Bangkok, Beirut, Santiago and Addis Ababa, among others.'),
 ('Is there an application fee?',
  'No. Applying through Inspira is free, and the UN never charges fees at any stage of recruitment.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: thepeninsulaqatar.com (16 Oct 2026) + menafn.com — 2026 YPP exam in Development and Sustainability, application window October\u2013November 2026, age/nationality/degree/language rules; UN Information Centre for the Caribbean (LinkedIn, 17 Oct 2026) — applications open, deadline 30 November 2026, careers.un.org/ypp; pathfinderly.com — job opening 285586, opened 16 Oct 2026, deadline 30 Nov 2026, P-1/P-2 roster, 2-year initial contract; opportunitylab.net — 47 participating countries, India/Nigeria/Ghana/Kenya/South Africa not on 2026 list; opportunitiesforyouth.org (17 Oct 2026) — exam guide with full eligibility; globalsouthconnections.co.ke — yearly-changing country list. Queue title "UN Young Professionals Program 2024 UN YPP Careers" retitled to the live 2026 cycle.</p>
''',
 dl_long='November 30, 2026',
 offlinks=[('UN Careers — Young Professionals Programme (official)', 'https://careers.un.org/ypp'),
           ('Pathfinderly — UN YPP 2026 details (job opening 285586)', 'https://pathfinderly.com/united-nations-young-professionals-programme/'),
           ('OpportunityLab — UN YPP 2026 eligible countries and exam area', 'https://opportunitylab.net/un-young-professionals-programme-ypp-2026/')],
 related_titles=['oecd', 'unicef-2026', 'unu-junior-fellows-2027'],
))

# ---------------------------------------------------------------- 4. Florida BF
A.append(dict(
 slug='florida-bright-futures-scholarship-2026-27-usa',
 title='Florida Bright Futures Scholarship 2026-27 in USA (Funded)',
 meta='Florida Bright Futures Scholarship 2026-27: FAS covers 100% tuition, FMS 75% for Florida high-school graduates. FFAA window 1 Oct 2026 to 31 Aug 2027 — GPA, test-score and service-hour requirements and how to apply.',
 short='Florida Bright Futures 2026-27', kicker='USA \u00b7 Undergraduate \u00b7 Funded', mono='BF',
 prov_short='Florida Dept. of Education (OSFA)', prov_cat='Government \u00b7 USA (Florida)',
 h1='Florida Bright Futures Scholarship 2026-27 in USA (Funded)',
 sub='Florida\u2019s best-known student award is not a competition you win — it is a statutory entitlement you claim: meet the GPA, test-score and service checklist, file the Florida Financial Aid Application, and the state pays 100% or 75% of your tuition. For students graduating in 2026-27, the application window runs 1 October 2026 to 31 August 2027.',
 dpill='FFAA open 1 Oct 2026 \u2013 31 Aug 2027',
 facts=facts([('Award', 'Florida Academic Scholars (FAS): 100% of tuition and applicable fees at Florida public colleges and universities (plus partial support at eligible private institutions). Florida Medallion Scholars (FMS): 75% of tuition. Funded by the Florida Lottery through the Office of Student Financial Assistance (OSFA). Renewable each year on continued academic performance.'),
              ('Eligible', 'Florida residents who are US citizens or eligible noncitizens, graduating from a Florida public high school, a Florida Department of Education-registered private high school, or a completed home-education program in 2026-27. Must complete 16 college-preparatory credits, meet the award-level GPA and test-score cutoffs, complete the required service or paid-work hours, and enrol at an eligible Florida postsecondary institution for at least 6 credit hours per term.'),
              ('How', 'Submit the Florida Financial Aid Application (FFAA) online during your senior year — for 2026-27 graduates the window is 1 October 2026 to 31 August 2027 (mid-year graduates have an earlier January deadline). Your district evaluates your coursework, GPA, test scores and service hours against the award checklist; there is no separate scholarship essay or committee.'),
              ('Deadline', '31 August 2027 for 2026-27 graduates (FFAA submission). Qualifying ACT, SAT or CLT scores must also be earned by 31 August of the graduation year.'),
              ('Fine print', 'Requirements are pegged to your graduating class: for 2026-27 graduates FAS needs a recalculated 3.50 weighted GPA with SAT 1330 / ACT 29 / CLT 95 and 100 service hours (paid work counts with district approval); FMS needs 3.00 with SAT 1190 / ACT 24 / CLT 82 and 75 hours. The $300/semester book allowance has not been funded since 2021.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Florida Bright Futures Scholarship Program</strong>, run by the state\u2019s <strong>Office of Student Financial Assistance (OSFA)</strong> and funded by the <strong>Florida Lottery</strong>, is one of the most valuable state scholarships in the United States. Its unusual feature is that it is <strong>not competitive</strong>: it is a statutory entitlement. If you meet the published checklist for your graduating class and file the application on time, the award follows — no committee, no essay contest, no limited number of winners.</p>
      <p>There are three award levels. <strong>Florida Academic Scholars (FAS)</strong> — the top tier — covers <strong>100% of tuition and applicable fees</strong> at Florida public institutions. <strong>Florida Medallion Scholars (FMS)</strong> covers <strong>75%</strong>. A third tier, the <strong>Gold Seal</strong> awards, supports career and technical education pathways. Because the requirements are fixed in state law and tied to your graduating class, the single most important thing is to check the <strong>2026-27 figures</strong>, not last year\u2019s.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>Florida resident</strong> and a <strong>US citizen or eligible noncitizen</strong>.</li>
        <li>Graduate in <strong>2026-27</strong> with a standard diploma from a <strong>Florida public high school</strong>, a Florida Department of Education-registered <strong>private high school</strong>, or a completed <strong>home-education program</strong>. (A narrow exception covers out-of-state diplomas for children of Florida-resident military or qualifying public-service personnel stationed away.)</li>
        <li>Complete the <strong>16 college-preparatory credits</strong> required for state-university admission.</li>
        <li><strong>FAS:</strong> recalculated weighted <strong>3.50 GPA</strong> across those 16 credits, plus <strong>SAT 1330 / ACT 29 / CLT 95</strong> and <strong>100 hours</strong> of volunteer service, paid work, or a combination.</li>
        <li><strong>FMS:</strong> recalculated weighted <strong>3.00 GPA</strong>, plus <strong>SAT 1190 / ACT 24 / CLT 82</strong> and <strong>75 hours</strong> of service/work.</li>
        <li>Enrol in a <strong>degree- or certificate-seeking program</strong> at an eligible Florida public or independent postsecondary institution, taking at least <strong>6 credit hours</strong> per term.</li>
        <li>Submit the <strong>Florida Financial Aid Application (FFAA)</strong> no later than <strong>31 August</strong> after graduation.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>FAS: 100% of tuition and applicable fees</strong> at Florida public colleges and universities; set per-credit amounts at eligible private institutions.</li>
        <li><strong>FMS: 75% of tuition</strong> at Florida public institutions.</li>
        <li><strong>Renewable funding</strong> for subsequent years on satisfactory academic performance — it is not a one-year award.</li>
        <li><strong>No separate competition</strong> — meet the checklist, file the FFAA, and the award follows by statute.</li>
        <li>Applies at <strong>Florida\u2019s public universities and colleges</strong> and eligible independent institutions across the state.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Florida Financial Aid Application (FFAA)</strong> — the single application, completed online; it takes only a few minutes.</li>
        <li>Your high school\u2019s <strong>evaluation report</strong> (districts must give every 11th and 12th grader an annual report showing credits, GPA per award level and unmet requirements).</li>
        <li><strong>Test scores</strong> (SAT, ACT or CLT) earned by 31 August of the graduation year.</li>
        <li><strong>Signed documentation</strong> of service hours or paid work hours, approved by the district.</li>
        <li>Standard <strong>residency and citizenship</strong> records as required by the institution.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Track your checklist from 11th grade</strong>Your district\u2019s annual evaluation report shows exactly where you stand on credits, the recalculated GPA per award level, test scores and hours — read it, because transcript GPA alone does not decide FAS.</li>
        <li><strong>Finish test scores and hours early</strong>Qualifying SAT, ACT or CLT scores must be earned by <strong>31 August</strong> of your graduation year; service or paid-work hours need district sign-off, so do not leave them for the summer.</li>
        <li><strong>File the FFAA in senior year</strong>Complete the Florida Financial Aid Application online between <strong>1 October 2026 and 31 August 2027</strong>. Even if you are unsure about attending a Florida college, filing keeps the award available if you later enrol in-state.</li>
        <li><strong>Enrol at an eligible Florida institution</strong>Take at least 6 credit hours per term in a degree- or certificate-seeking program; the institution certifies your award level.</li>
        <li><strong>Keep it renewable</strong>Maintain the required college GPA and credit completion so the funding continues beyond the first year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is Bright Futures competitive? Will I be ranked against other students?',
  'No. It is a statutory entitlement: every student who meets the checklist for their graduating class and files the FFAA on time receives the award. There is no quota of winners.'),
 ('I am not a Florida resident. Can I apply?',
  'No. Florida residency (plus US citizenship or eligible-noncitizen status) is a hard requirement, with only a narrow exception for children of Florida-resident military or qualifying public-service personnel stationed out of state.'),
 ('What is the difference between FAS and FMS?',
  'Florida Academic Scholars (FAS) is the top tier: 3.50 recalculated GPA, higher test scores, 100 service hours, and 100% tuition coverage. Florida Medallion Scholars (FMS) needs 3.00, lower scores, 75 hours, and covers 75% of tuition.'),
 ('Do paid work hours count toward the service requirement?',
  'Yes. 100 hours of paid work (with district approval and signed documentation) can substitute for volunteer hours at any award level — or combine both to reach the total.'),
 ('What if I do not plan to attend a Florida college right away?',
  'File the FFAA anyway. Applying keeps the scholarship available if you later enrol at an eligible Florida institution, and the application takes only minutes.'),
 ('Does the award cover books?',
  'The $300-per-semester book allowance exists in statute but has not actually been funded since 2021 — do not budget for it.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: beyondhorizons.lagosmove.com.ng (3 days ago) — FFAA window 1 Oct 2026 to 31 Aug 2027 for 2026-27 graduates, residency/citizenship/school rules, 6-credit enrolment; floridacourtrules.com (31 days ago) — statutory entitlement (not competitive), class-pegged requirements, FAS 3.50 recalculated GPA, SAT/ACT/CLT cutoffs that move by year, paid-work substitution, book allowance unfunded since 2021; collegereadyparent.org (2026-2027 cheat sheet) — FFAA opens Oct 1 of senior year, closes Aug 31 after graduation, mid-year graduates January; thrillshare.com (official 2026-27 FAS/FMS requirements PDF) — 2026-27 cutoffs: FAS 3.50 + 29/95/1330 + 100 hrs, FMS 3.00 + 24/82/1190 + 75 hrs; encolro.com + internationalcollegecounselors.com — 100%/75% tuition coverage, FFAA procedure. Queue title "Florida Bright Futures Scholarship 2024-25" retitled to the live 2026-27 cycle.</p>
''',
 dl_long='August 31, 2027 (FFAA submission for 2026-27 graduates; window opened October 1, 2026)',
 offlinks=[('Florida Court Rules — Bright Futures 2026-27 requirements', 'https://floridacourtrules.com/florida-bright-futures/'),
           ('Encolro — Florida Bright Futures Scholarship Program', 'https://encolro.com/2026/05/11/florida-bright-futures-scholarship-program-usa/'),
           ('International College Counselors — Bright Futures guide', 'https://internationalcollegecounselors.com/florida-bright-futures-scholarship-4/')],
 related_titles=['richmond-2027', 'minnesota-ges', 'ursinus'],
))

# ---------------------------------------------------------------- 5. UP Scholarship
A.append(dict(
 slug='up-scholarship-2026-27-online-apply',
 title='UP Scholarship 2026-27 Online Apply | Scholarship UP Online',
 meta='UP Scholarship 2026-27: Dashmottar applications open till 31 October 2026 (fresh) at scholarship.up.gov.in. Eligibility, income limits, documents, category-wise dates and how to apply online.',
 short='UP Scholarship 2026-27', kicker='India \u00b7 Uttar Pradesh \u00b7 All levels', mono='UP',
 prov_short='Government of Uttar Pradesh', prov_cat='State Government \u00b7 Uttar Pradesh',
 h1='UP Scholarship 2026-27 Online Apply | Scholarship UP Online',
 sub='The Uttar Pradesh Scholarship and Fee Reimbursement Online System is accepting 2026-27 applications: students in graduation, postgraduation, diploma, ITI and other Dashmottar courses can apply fresh until 31 October 2026 on the official portal scholarship.up.gov.in, with the money reaching Aadhaar-seeded bank accounts by Direct Benefit Transfer.',
 dpill='Fresh: 31 Oct 2026 \u00b7 8 days left',
 facts=facts([('Award', 'Post-matric scholarships of roughly Rs.230 to Rs.1,200 per month (course- and category-dependent) and pre-matric assistance of Rs.3,000 to Rs.7,000 per year. The state recently transferred over Rs.148 crore in scholarship and fee-reimbursement funds to more than 4.60 lakh students. Payment is by Direct Benefit Transfer after institute and district verification.'),
              ('Eligible', 'Students who fulfil Uttar Pradesh domicile requirements and are enrolled in eligible schools, colleges, universities, diploma or ITI institutions. Open to General, OBC, SC, ST and minority students, each with its own conditions: family income up to Rs.2 lakh per year for General and OBC candidates, and up to Rs.2.5 lakh for SC and ST candidates. Students need a bank account in their own name seeded with Aadhaar.'),
              ('How', 'Apply online at the official portal scholarship.up.gov.in: complete the One-Time Registration where applicable, choose the correct category (Pre-Matric, Post-Matric Intermediate, or Post-Matric Other Than Intermediate/Dashmottar), select Fresh or Renewal, fill details carefully, upload documents, submit, print the form and submit the hard copy to the institution where required.'),
              ('Deadline', 'Dashmottar (UG, PG, diploma, ITI and other courses): fresh applications till 31 October 2026; renewal till 15 October 2026. The Class 9 to 12 windows for 2026-27 have already closed (fresh till 21 September, renewal till 25 August 2026).'),
              ('Fine print', 'The application window opened on 15 September 2026 for Dashmottar. Choosing the wrong category or the wrong Fresh/Renewal option is the most common reason forms get rejected — match the option to your situation before submitting.')]),
 body='''
      <h2 id="about">About the scheme</h2>
      <p>The <strong>UP Scholarship</strong> — formally the Uttar Pradesh Scholarship and Fee Reimbursement Online System — is the state government\u2019s umbrella program for student financial aid, run on the official portal <strong>scholarship.up.gov.in</strong>. It covers <strong>pre-matric and post-matric</strong> students across General, SC, ST, OBC and minority categories, from Class 9 upward through graduation, postgraduation, diploma, ITI and other courses. For the 2026-27 session the state has already moved more than <strong>Rs.148 crore</strong> to over <strong>4.60 lakh students</strong> under the scheme.</p>
      <p>Applications are organised into three broad categories: <strong>Pre-Matric</strong> (Classes 9 and 10), <strong>Post-Matric Intermediate</strong> (Classes 11 and 12), and <strong>Post-Matric Other Than Intermediate</strong> — better known as <strong>Dashmottar</strong> — covering graduation, postgraduation, diploma, ITI and other qualifying courses. Each category has its own window, and <strong>fresh and renewal applicants have different deadlines</strong>, so the first job is to identify exactly which box you fall into.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li> fulfil the <strong>Uttar Pradesh domicile requirements</strong> applicable to the scholarship category (students studying at eligible institutions outside UP may be covered under specific provisions — check the portal instructions).</li>
        <li>Be enrolled in an <strong>eligible school, college, university, diploma, ITI or other recognised institution</strong> for the 2026-27 session.</li>
        <li>Belong to one of the covered groups: <strong>General, OBC, SC, ST or minority</strong> communities, meeting the conditions prescribed for that group.</li>
        <li>Meet the <strong>family income ceiling</strong>: up to <strong>Rs.2 lakh per year</strong> for General and OBC candidates, and up to <strong>Rs.2.5 lakh per year</strong> for SC and ST candidates.</li>
        <li>Hold a <strong>bank account in your own name, seeded with your Aadhaar number</strong> — the scholarship is paid by Direct Benefit Transfer.</li>
        <li>Pre-Matric covers Classes 9\u201310; Post-Matric Intermediate covers Classes 11\u201312; <strong>Dashmottar</strong> covers UG, PG, diploma, ITI and other qualifying courses.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Post-matric:</strong> roughly <strong>Rs.230 to Rs.1,200 per month</strong>, varying by course and category.</li>
        <li><strong>Pre-matric:</strong> roughly <strong>Rs.3,000 to Rs.7,000 per year</strong> (for example, around Rs.3,500 for SC day scholars and Rs.7,000 for residential candidates; around Rs.3,000 per year for General category).</li>
        <li><strong>Fee reimbursement</strong> provisions for eligible categories, alongside the scholarship itself.</li>
        <li>Payment by <strong>Direct Benefit Transfer (DBT)</strong> straight to the student\u2019s Aadhaar-seeded bank account, after institute and district verification.</li>
        <li>Applications, uploads and <strong>status tracking</strong> are all handled on the single official portal — no agents or intermediaries are needed.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Aadhaar card</strong> (and Aadhaar-seeded bank account details).</li>
        <li><strong>Previous year\u2019s marksheet</strong> / academic records.</li>
        <li><strong>Income certificate</strong> proving the family income ceiling for your category.</li>
        <li><strong>Caste certificate</strong> (for SC/ST/OBC applicants) or minority declaration, as applicable.</li>
        <li><strong>Domicile certificate</strong> of Uttar Pradesh.</li>
        <li><strong>Admission proof</strong> — fee receipt, admission letter or bonafide certificate for 2026-27.</li>
        <li><strong>Registration/OTR details</strong> — keep your registration number safe for login and status checks.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Identify your category and type</strong>Are you Pre-Matric (9\u201310), Post-Matric Intermediate (11\u201312) or Dashmottar (UG/PG/diploma/ITI)? And are you a <strong>fresh</strong> applicant or a <strong>renewal</strong>? The deadlines differ — Dashmottar fresh closes <strong>31 October 2026</strong>, renewal closed <strong>15 October 2026</strong>.</li>
        <li><strong>Open the official portal</strong>Go to <strong>scholarship.up.gov.in</strong> — the only genuine site. Ignore lookalike domains and anyone asking for money to apply.</li>
        <li><strong>Complete One-Time Registration</strong>Finish the OTR process where applicable and keep the registration number and login details safe.</li>
        <li><strong>Choose the right options</strong>Select your scholarship category, then the Fresh or Renewal option, exactly matching your situation.</li>
        <li><strong>Fill, upload and submit</strong>Enter personal and academic details carefully, upload the required documents, submit the form, and <strong>take a printout</strong>.</li>
        <li><strong>Submit the hard copy to your institution</strong>Wherever required, hand the printed form to your school or college so institute-level verification can proceed, then track the status online.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the last date for UP Scholarship 2026-27?',
  'For Dashmottar (UG, PG, diploma, ITI and other courses): 31 October 2026 for fresh applicants; renewal closed on 15 October 2026. The Class 9 to 12 windows are already closed for 2026-27.'),
 ('Where do I apply? Is there any fee?',
  'Only on the official portal scholarship.up.gov.in. The application is free — the scheme needs no agents, and nobody can charge you for it.'),
 ('What is the income limit?',
  'Up to Rs.2 lakh per year for General and OBC candidates, and up to Rs.2.5 lakh per year for SC and ST candidates.'),
 ('How much money will I get?',
  'Roughly Rs.230 to Rs.1,200 per month for post-matric students and Rs.3,000 to Rs.7,000 per year for pre-matric students, depending on course and category, plus fee-reimbursement provisions where applicable.'),
 ('How is the money paid?',
  'By Direct Benefit Transfer into your own Aadhaar-seeded bank account, after your institute and the district verify the application.'),
 ('I missed the renewal deadline of 15 October. Can I still apply as fresh?',
  'No — fresh and renewal are distinct tracks with separate eligibility. Applying under the wrong option is one of the most common reasons forms are rejected.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: jagranjosh.com (14\u201316 days ago, three articles) — Dashmottar window opened 15 Sep 2026, fresh till 31 Oct 2026, renewal till 15 Oct 2026; Classes 9\u201312 windows closed (fresh 21 Sep, renewal 25 Aug 2026); post-matric Rs.230\u20131,200/month, pre-matric Rs.3,000\u20137,000/year; business-standard.com (16 days ago) — official portal accepting Dashmottar applications, OTR process, category selection, hard-copy submission; educationtimes.com (17 days ago) — Rs.148 crore transferred to 4.60+ lakh students, General/OBC/SC/ST/minority coverage; dainiknewslive.in (17 days ago) — income ceilings (Rs.2L General/OBC, Rs.2.5L SC/ST), Aadhaar-seeded DBT. Queue title "UP Scholarship 2023-24 Online Apply | Scholarship UP Online" retitled to the live 2026-27 session.</p>
''',
 dl_long='October 31, 2026 (fresh Dashmottar applications; renewal closed October 15, 2026)',
 offlinks=[('Jagran Josh — UP Scholarship 2026-27 applications open', 'https://www.jagranjosh.com/news/up-scholarship-2026-27-applications-open-for-ug-pg-diploma-students-at-scholarship-up-gov-in-188197'),
           ('Business Standard — who can apply, deadlines, how to register', 'https://www.business-standard.com/education/news/up-scholarship-2026-27-who-can-apply-deadlines-and-how-to-register-online-nc-126100700289_1.html'),
           ('Education Times — complete details and last date', 'https://www.educationtimes.com/news/up-scholarship-2026-27-check-complete-details-eligibility-last-date-and-how-to-apply/articleshow/134733578.cms')],
 related_titles=['oasis-scst', 'ambedkar-hp', 'banishree'],
))

sizes = {}
for a in A: _split_verify(a)
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)

# HTML parse validation + leftover template text check
class P(html.parser.HTMLParser):
    def error(self, message): raise AssertionError(message)
for a in A:
    pth = OUT / (a['slug'] + '.html')
    assert pth.exists(), a['slug']
    P().feed(pth.read_text())
    txt = pth.read_text()
    assert 'AICTE Pragati' not in txt, a['slug']
    assert 'Lorem' not in txt, a['slug']
    assert 'wa.me/919905166009' in txt, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

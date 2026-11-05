#!/usr/bin/env python3
"""Batch 42 (cron run 42, 23 Oct 2026): 5 new verified articles.

Queue scan: the 112 stale-titled topics at the head of the queue (2020-2024
cycles: Nurse Corps 2024-25, IST 2024, Bath Global Leaders 2024, IU 2023
admissions notices, VCDNP 2024, OKP 2023-24, ... through to International
Excellence Masters 2020) were each verified by 3 parallel research workers
with 1-2 searches each; ALL were skipped with evidence-backed reasons
(dead cycles, employer internships, non-scholarship promos, discontinued
programs, listicles). Per batch-39/41 precedent, had any shown an open
current cycle it would have been written retitled to the live cycle — none
did. Scanning continued in queue order into the fresh-titled block:

WRITES (verified by researcher D with 2-3 searches each, 23 Oct 2026):
1. LawAI Summer Research Fellowship 2027 in USA (Fully Funded) — deadline
   29 Jan 2027 11:59pm ET; 10-week paid summer (Jun 14-Aug 20, 2027),
   $2,000/week subsidy + $10,000 relocation/housing stipend for DC movers;
   Convening Week Jun 21-25, 2027 in Washington, DC.
2. Swinburne University Scholarships 2027 in Australia (Funded) — no
   separate deadline; automatic merit assessment with the 2027 course
   application: 20% International, 30% George Swinburne Excellence,
   30% Women in Engineering Leadership, ELICOS+ up to 10 weeks refund.
3. University of Hawaii EWC Graduate Fellowship 2027 in United States
   (Fully Funded) — deadline 1 Dec 2026 11:59pm HST; docs by 10 Jan 2027;
   full UH Manoa tuition+fees, EWC housing, stipend, books allowance,
   health-insurance subsidy (~$22,000/yr package).
4. University of Hawaii ADB-JSP Scholarship 2027 in USA (Fully Funded) —
   biennial intake (next opens Fall 2029); deadline 1 Dec 2026 (refs by
   15 Dec 2026); full tuition, housing, monthly stipend, airfare,
   insurance, J-1 sponsorship; ADB developing member countries, <=35,
   2+ yrs work experience.
5. INPEX Scholarship Program 2027 in Japan (Fully Funded) — deadline
   31 Oct 2026 23:59 JST; full tuition/fees, JPY 160,000/month,
   JPY 60,000 settling-in, round-trip airfare; Indonesia/Australia/UAE
   citizens only, <30, mandatory LOA from a Japanese professor.

SKIPS also recorded this run (17 from researcher's fresh-block scan):
Cagliari PhD 2027 (Cycle 42 closed), HEC Commonwealth 2027 (cycle closed),
Devin AI Ambassador (not a scholarship — dev advocacy promo), Wilson Center
2027-28 (closed), UNOPS 2026 (employer internship), Barclays 2027 (employer
pipeline), Silicon Valley Space Week 2026 (closed), Loughborough CSC 2027
(cycle closed), Uni Porto 2027 (aggregator, not one scheme), College Students
2027 (generic listicle), Goldman Sachs 2027 (employer pipeline), UNIDIR 2026
(employer posting), GCF Internship 2027 (employer pipeline), NASA JPL 2027
(employer listing), TU Berlin Winter 2027 (unverifiable), Commonwealth Grad
2027 (cycle closed), KAU 2027 (window not verifiably open).

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
 'lawai-2027': {'mono': 'LA', 'title': 'LawAI Summer Research Fellowship 2027 in USA (Fully Funded)',
   'href': 'lawai-summer-research-fellowship-2027-usa.html',
   'dpill': 'Deadline 29 Jan 2027 · 98 days left',
   'award': '$2,000/week subsidy + $10,000 relocation/housing stipend for DC movers; 10-week paid summer.',
   'elig': 'Law students (JD/LLM incl. incoming 1L), PhD candidates, postdocs, professionals, legal academics; strong grasp of US legal principles applied to AI.',
   'tags': [('Fellowship', 'purple'), ('USA', 'teal')]},
 'swinburne-2027': {'mono': 'SW', 'title': 'Swinburne University Scholarships 2027 in Australia (Funded)',
   'href': 'swinburne-university-scholarships-2027-australia.html',
   'dpill': 'No deadline — auto-assessed with course application',
   'award': '20% or 30% tuition-fee reduction; 30% Women in Engineering; ELICOS+ up to 10 weeks English-fee refund.',
   'elig': 'International students commencing an eligible 2027 course at Hawthorn campus; merit-based, no separate form.',
   'tags': [('UG/PG', 'blue'), ('Australia', 'teal')]},
 'hawaii-ewc': {'mono': 'EWC', 'title': 'University of Hawaii EWC Graduate Fellowship 2027 in United States (Fully Funded)',
   'href': 'hawaii-ewc-graduate-fellowship-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · 39 days left',
   'award': 'Full UH Manoa tuition+fees, EWC housing, living stipend, books allowance, health-insurance subsidy (~$22,000/yr).',
   'elig': 'US citizens/PRs or eligible Asia-Pacific citizens; 3.0+ GPA; graduate study at UH Manoa from Aug 2027.',
   'tags': [('Masters/PhD', 'blue'), ('USA', 'teal')]},
 'hawaii-adb': {'mono': 'ADB', 'title': 'University of Hawaii ADB-JSP Scholarship 2027 in USA (Fully Funded)',
   'href': 'hawaii-adb-jsp-scholarship-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · 39 days left',
   'award': 'Full tuition+fees, housing, monthly stipend, round-trip airfare, insurance, J-1 sponsorship; biennial intake.',
   'elig': 'ADB developing member country citizens resident at home; ≤35; bachelor’s + 2 yrs work experience; approved master’s at UHM.',
   'tags': [('Masters', 'blue'), ('USA', 'teal')]},
 'inpex-2027': {'mono': 'IN', 'title': 'INPEX Scholarship Program 2027 in Japan (Fully Funded)',
   'href': 'inpex-scholarship-program-2027-japan.html',
   'dpill': 'Deadline 31 Oct 2026 · 8 days left',
   'award': 'Full tuition/exam/entrance fees + JPY 160,000/month + JPY 60,000 settling-in + round-trip airfare.',
   'elig': 'Citizens of Indonesia, Australia or UAE only; <30; GPA ≥3.0/4.0; mandatory LOA from a Japanese professor.',
   'tags': [('Masters', 'blue'), ('Japan', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. LawAI
A.append(dict(
 slug='lawai-summer-research-fellowship-2027-usa',
 title='LawAI Summer Research Fellowship 2027 in USA (Fully Funded)',
 meta='LawAI Summer Research Fellowship 2027: a 10-week paid summer fellowship (14 Jun – 20 Aug 2027) at the leading edge of AI law and policy. $2,000/week subsidy plus $10,000 relocation and housing stipend for fellows moving to Washington, DC. Deadline 29 January 2027 — eligibility, benefits, application steps and FAQs.',
 short='LawAI Summer Fellowship 2027', kicker='USA \u00b7 Fellowship \u00b7 Paid', mono='LA',
 prov_short='Institute for Law & AI (LawAI)', prov_cat='Institute \u00b7 USA',
 h1='LawAI Summer Research Fellowship 2027 in USA (Fully Funded)',
 sub='Ten weeks at the centre of the AI-governance debate: the LawAI Summer Research Fellowship 2027 pays you $2,000 a week to do original research on AI law and policy, adds a $10,000 relocation and housing stipend if you move to Washington, DC, and brings the whole cohort together for a Convening Week in the US capital. Applications close 29 January 2027.',
 dpill='Deadline 29 Jan 2027 \u00b7 98 days left',
 facts=facts([('Award', 'A fellowship subsidy of $2,000 per week (higher amounts are possible for exceptional candidates) for the 10-week program, plus a $10,000 relocation and housing stipend for fellows who move to Washington, DC for the summer. Travel, accommodation and meals for the Convening Week in Washington, DC (21\u201325 June 2027) are covered for eligible fellows. There is no application fee.'),
              ('Eligible', 'Law students (JD or LLM, including incoming 1Ls), PhD candidates, postdoctoral researchers, professionals and legal academics. You need a strong grasp of the legal principles that govern AI regulation under US law and policy, genuine interest in AI law and policy, and the ability to apply legal research skills to real questions. Prior AI-specific research experience is not required. In-person participation in Washington, DC is strongly encouraged and is a selection factor for law students; remote arrangements are considered only case by case. You must be able to participate full-time from 14 June to 20 August 2027 and attend the Convening Week.'),
              ('How', 'Submit the online application form by 11:59 pm ET on 29 January 2027 (about 20 minutes; late applications are not assessed). Shortlisted candidates complete an asynchronous exploratory interview of about 20 minutes on perspectives about AI development, law and society, then a project interview of about 45 minutes with a LawAI research staff member on interests, goals and fit. Decisions are aimed for mid-March; if you have an earlier decision deadline, note it on the application form. Questions or disability-accommodation requests go to programs@law-ai.org.'),
              ('Deadline', '29 January 2027, 11:59 pm Eastern Time.'),
              ('Fine print', 'You must hold valid visa or immigration permissions for the place of participation; LawAI offers best-effort visa sponsorship support to offer holders. Outputs are set with your mentor — some fellows produce one extended piece such as a report or law review article, others support several advisory or research projects, all connected to AI safety, security and the rule of law.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Summer Research Fellowship</strong> is the flagship talent program of the <strong>Institute for Law &amp; AI (LawAI)</strong>, the research institute working on the legal foundations of AI safety and governance. For ten weeks each summer it gathers a cohort of lawyers, researchers and policy-minded professionals to do real, publishable research at the point where law meets frontier AI: liability for autonomous systems, the legal architecture of AI governance, safety regulation, and the rule-of-law questions raised by powerful AI.</p>
      <p>The 2027 fellowship runs <strong>14 June to 20 August 2027</strong>. Fellows work with a mentor on a project matched to their experience and interests, join Q&amp;A sessions with leading experts, build a US law-and-policy network, and get career-planning support. The whole cohort comes together for a <strong>Convening Week in Washington, DC from 21 to 25 June 2027</strong>, with flights, accommodation and meals covered. For strong collaborators, the fellowship also opens doors afterwards: follow-on grant funding, event invitations and possible openings at LawAI itself.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>law student</strong> (JD or LLM, including incoming 1Ls), a <strong>PhD candidate</strong>, a <strong>postdoctoral researcher</strong>, a <strong>professional</strong>, or a <strong>legal academic</strong>.</li>
        <li>Have a <strong>strong grasp of US legal principles as applied to AI regulation</strong> — from formal legal study or comparable professional experience. Prior AI-specific research is welcome but not required.</li>
        <li>Show <strong>genuine interest in AI law and policy</strong> and readiness to apply legal research skills to open questions.</li>
        <li>Be able to participate <strong>full-time from 14 June to 20 August 2027</strong> and attend the Convening Week in Washington, DC (21\u201325 June 2027).</li>
        <li>Hold <strong>valid visa or immigration permissions</strong> for the place of participation; LawAI gives best-effort visa sponsorship support to offer holders.</li>
        <li>Expect to participate <strong>in person in Washington, DC</strong> — this is the default, and for law students it is a selection factor. Remote arrangements are considered only for candidates with compelling reasons, case by case.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$2,000 per week</strong> fellowship subsidy for the 10-week program (higher for exceptional candidates).</li>
        <li><strong>$10,000 relocation and housing stipend</strong> for fellows who move to Washington, DC for the summer.</li>
        <li><strong>Convening Week in Washington, DC (21\u201325 June 2027)</strong> with eligible travel, accommodation and meals covered.</li>
        <li><strong>Close mentorship</strong> from LawAI research staff and affiliates, matched to your interests.</li>
        <li>Q&amp;A sessions with <strong>leading experts</strong>, US law-and-policy <strong>networking</strong>, and <strong>career-planning</strong> resources.</li>
        <li><strong>Pathways after the fellowship</strong>: follow-on grant funding, event invitations and possible openings at LawAI.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The official 2027 notification does <strong>not publish a document list</strong> — the application is an online form that takes about 20 minutes. (The previous cycle asked for an academic CV in PDF and the most recent transcript in PDF, with a LinkedIn profile and a writing sample in English from the past two years as optional extras, per third-party guides — confirm against the live form before applying.)</li>
        <li>If you are selected, expect follow-up paperwork around <strong>visa/immigration permissions</strong> and any decision deadline you noted on the form.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check you can attend the full summer</strong>The fellowship runs 14 June to 20 August 2027 with a mandatory Convening Week in Washington, DC from 21 to 25 June. If you cannot be in DC, weigh whether your case for remote participation is genuinely compelling.</li>
        <li><strong>Submit the online application by 29 January 2027, 11:59 pm ET</strong>The form takes about 20 minutes. Late applications are not assessed, so do not rely on a deadline extension.</li>
        <li><strong>Complete the asynchronous exploratory interview</strong>Shortlisted candidates record about 20 minutes on their perspectives about AI development, law and society — on their own schedule.</li>
        <li><strong>Attend the project interview</strong>A roughly 45-minute conversation with a member of LawAI research staff on your interests, goals and fit with available projects.</li>
        <li><strong>Watch for the decision by mid-March</strong>Decisions are aimed for mid-March 2027. If you need an answer earlier for another commitment, note that deadline on the application form so the team can try to accommodate it.</li>
        <li><strong>Ask for help if you need it</strong>Questions and disability-accommodation requests go to <strong>programs@law-ai.org</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Who is the fellowship aimed at?',
  'It is designed for law students, professionals and academics who want to work on AI governance. Past cohorts have included JD and LLM students, PhD candidates, postdocs, mid-career professionals moving into AI-focused roles, and legal academics.'),
 ('Do I need prior AI research experience?',
  'No. You need a solid understanding of the legal principles that govern AI regulation in US law and policy, which can come from formal legal study or comparable professional experience. Curiosity and research ability matter more than an AI publication record.'),
 ('Is the program remote or in person?',
  'The default is in person in Washington, DC for the summer, and fellows who relocate there receive the $10,000 relocation and housing stipend. Remote participation is possible only for candidates with compelling reasons, assessed case by case.'),
 ('What does a fellow actually do day to day?',
  'You work with a mentor to develop and run a project matched to your experience and interests. Some fellows produce one extended piece such as a report or law review article; others support several advisory or research projects. Outputs are chosen with your mentor and should connect to AI safety, security and the rule of law.'),
 ('What happens after the fellowship?',
  'Alumni have moved into law and policy roles at the US Department of Commerce, leading AI companies, universities and think tanks, including LawAI itself. The fellowship advertises follow-on grants, event invitations and possible job openings for strong collaborators.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: law-ai.org/summer-fellowship-us (official, crawled 23 Oct 2026) — 2027 program dates 14 Jun\u201320 Aug 2027, Convening Week 21\u201325 Jun 2027 in Washington DC, $2,000/week subsidy, $10,000 relocation/housing stipend, deadline 29 Jan 2027 11:59 pm ET, ~20-min form, async exploratory interview + 45-min project interview, decisions aimed mid-March, programs@law-ai.org, best-effort visa sponsorship; opportunities247.org + scholarshipbob.com (previous cycle) — CV and transcript PDFs previously required, LinkedIn and English writing sample optional. Document list for 2027 not published in the official notification.</p>
''',
 dl_long='January 29, 2027 (11:59 pm ET)',
 offlinks=[('LawAI — Summer Fellowship (US), official page', 'https://law-ai.org/summer-fellowship-us/')],
 related_titles=['unu-junior-fellows-2027', 'nyt-fellowship', 'auc-fellow-2027', 'nasa-hubble'],
))

# ---------------------------------------------------------------- 2. Swinburne
A.append(dict(
 slug='swinburne-university-scholarships-2027-australia',
 title='Swinburne University Scholarships 2027 in Australia (Funded)',
 meta='Swinburne University Scholarships 2027: 20% or 30% tuition-fee reductions for international students commencing in 2027 — automatic merit assessment with your course application, no separate form. 30% Women in Engineering Leadership and ELICOS+ English refund. Eligibility, excluded courses and FAQs.',
 short='Swinburne Scholarships 2027', kicker='Australia \u00b7 UG/PG \u00b7 Up to 30% fees', mono='SW',
 prov_short='Swinburne University of Technology', prov_cat='University \u00b7 Australia',
 h1='Swinburne University Scholarships 2027 in Australia (Funded)',
 sub='No essays, no separate application: Swinburne automatically checks every international applicant commencing an eligible course in 2027 for tuition-fee scholarships worth 20% to 30% off — plus a 30% Women in Engineering Leadership award and an English-course fee refund through ELICOS+. The outcome arrives inside your letter of offer.',
 dpill='No deadline \u2014 auto-assessed with course application',
 facts=facts([('Award', 'Swinburne International Scholarship: a 20% reduction of tuition fees for the standard duration of the course. George Swinburne International Excellence Scholarship: a 30% tuition-fee reduction for high academic achievers. Women in Engineering Leadership Scholarship: a 30% tuition-fee reduction for women entering selected engineering and construction courses, plus professional-development and mentorship activities. ELICOS+ Scholarship: a refund equal to up to 10 weeks of English-course (ELICOS) tuition, deducted from tuition across the first three semesters of the principal degree. Awards cover tuition fees only.'),
              ('Eligible', 'International students commencing an eligible course for the first time in 2027 at Swinburne\u2019s Hawthorn campus — undergraduate, postgraduate coursework and pathway courses (Foundation, UniLink diploma, Postgraduate Qualifying Program). Awards are merit-based on previous academic results; stronger results are considered for the 30% Excellence award. Excluded: Bachelor of Aviation and Piloting (and its double degrees) and Bachelor of Nursing at undergraduate level; Master of Physiotherapy, Master of Occupational Therapy, master\u2019s by research and doctorates at postgraduate level. The Women in Engineering Leadership award targets female international applicants entering selected engineering/construction courses such as the Bachelor of Engineering (Honours) or Master of Professional Engineering. ELICOS+ is for packaged English-course students who do not yet meet the English entry requirement of their principal course.'),
              ('How', 'There is no separate scholarship application. Apply for an eligible Swinburne course commencing in 2027 through the university\u2019s normal course-application process; the university automatically assesses your previous academic results, and any scholarship you receive is stated in the same letter of offer as your admission. ELICOS+ students receive the refund after completing the English course and starting the principal degree, applied across the first three semesters.'),
              ('Deadline', 'No separate deadline. Because assessment is automatic with the course application, your effective deadline is the course-application deadline for your chosen 2027 intake.'),
              ('Fine print', 'Scholarships reduce tuition fees only — Overseas Student Health Cover, accommodation, living expenses, practicum costs and other non-tuition fees remain your responsibility. Verify the exact eligible courses on the official page before applying.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>Swinburne University of Technology, based in Melbourne, bundles its international-student support into a simple proposition: <strong>apply for your course, and the university does the rest</strong>. Instead of a separate scholarship form with essays and references, every international applicant who commences an eligible course for the first time in 2027 is <strong>automatically assessed on previous academic results</strong>, and any award is written into the same letter of offer as the admission itself.</p>
      <p>The 2027 package has four parts. The standard <strong>Swinburne International Scholarship</strong> cuts <strong>20% off tuition fees</strong> for the standard course duration. The <strong>George Swinburne International Excellence Scholarship</strong> lifts that to <strong>30%</strong> for applicants with particularly strong previous results. The <strong>Women in Engineering Leadership Scholarship</strong> gives women entering selected engineering and construction courses <strong>30%</strong> off plus mentoring and professional-development activities. And the <strong>ELICOS+ Scholarship</strong> refunds up to <strong>10 weeks of English-course fees</strong> for students who need English preparation before their degree.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> commencing an eligible course for the first time in <strong>2027</strong> at Swinburne\u2019s <strong>Hawthorn campus</strong>.</li>
        <li>Apply for an <strong>undergraduate</strong>, <strong>postgraduate coursework</strong> or <strong>pathway</strong> course (Foundation, UniLink diploma, Postgraduate Qualifying Program).</li>
        <li>Be assessed on <strong>previous academic results</strong> — merit decides the award; higher achievers are considered for the 30% Excellence award.</li>
        <li><strong>Women in Engineering Leadership:</strong> female international applicants entering selected engineering/construction courses (e.g. Bachelor of Engineering (Honours), Master of Professional Engineering).</li>
        <li><strong>ELICOS+:</strong> packaged English-course students who do not yet meet the English entry requirement of their principal course.</li>
        <li><strong>Excluded courses for 2027:</strong> Bachelor of Aviation and Piloting (including double degrees) and Bachelor of Nursing at undergraduate level; Master of Physiotherapy, Master of Occupational Therapy, master\u2019s by research and doctorates at postgraduate level.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Automatic merit assessment</strong> — no separate scholarship application; the outcome appears in your course offer letter.</li>
        <li><strong>20% or 30% reduction of tuition fees</strong> for the standard duration of the course.</li>
        <li><strong>Women in Engineering:</strong> 30% tuition reduction plus professional-development and mentorship activities.</li>
        <li><strong>ELICOS+ refund</strong> of up to 10 weeks of English-course fees, deducted from tuition across the first three semesters of the main degree.</li>
        <li>Covers <strong>tuition fees only</strong> — Overseas Student Health Cover, practicum costs and other non-tuition fees are not included.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>No separate scholarship document list is published — assessment is <strong>automatic from the documents you submit with your course application</strong> for the chosen degree (academic transcripts and certificates, English evidence, passport and the standard admission paperwork).</li>
        <li>ELICOS+ students need the <strong>packaged English-course offer</strong> to trigger the refund mechanism.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick an eligible course for 2027</strong>Check the official scholarships page against your course — some courses are excluded, so confirm before you apply.</li>
        <li><strong>Apply for the course through the normal channel</strong>Submit your Swinburne course application for first-time commencement in 2027 at the Hawthorn campus, with academic transcripts, English evidence and passport.</li>
        <li><strong>Wait for automatic assessment</strong>The university checks your previous results against the available scholarships — there is nothing extra to fill in.</li>
        <li><strong>Read your letter of offer</strong>Any scholarship you receive, and its exact percentage, is stated in the same offer letter as your admission.</li>
        <li><strong>ELICOS+ only</strong>Complete the English course, start your principal degree, and the refund of up to 10 weeks of ELICOS fees is deducted from tuition across your first three semesters.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need to file a separate scholarship application?',
  'No. When you apply for an eligible course for first-time commencement in 2027, Swinburne automatically checks your academic record for the available international scholarships and tells you in the letter of offer.'),
 ('What is the difference between the 20% and 30% awards?',
  'The 20% Swinburne International Scholarship is the standard merit award for eligible commencing international students; the 30% George Swinburne International Excellence Scholarship recognizes applicants with particularly strong previous results. There is also a 30% Women in Engineering Leadership Scholarship for women entering selected engineering and construction programs.'),
 ('Which courses are excluded?',
  'For 2027 the university excludes the Bachelor of Aviation and Piloting (including double degrees) and Bachelor of Nursing, plus Master of Physiotherapy, Master of Occupational Therapy, master\u2019s degrees by research and doctorates.'),
 ('How does the ELICOS+ Scholarship work?',
  'If you need English preparation before your degree, you can receive a refund equal to up to 10 weeks of ELICOS fees once you finish the English course and begin your principal degree; the amount is deducted from tuition across the first three semesters.'),
 ('Does the scholarship cover living or health costs?',
  'No. It is a tuition-fee reduction only. Overseas Student Health Cover, accommodation, living expenses and other non-tuition fees remain your responsibility.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: swinburne.edu.au/courses/scholarships/international-scholarships (official, crawled 23 Oct 2026) — 2027 international awards: 20% Swinburne International Scholarship, 30% George Swinburne International Excellence, 30% Women in Engineering Leadership (+mentoring/PD), ELICOS+ refund of up to 10 weeks ELICOS fees across first three semesters; automatic assessment with 2027 course application, stated in the letter of offer; Hawthorn campus, first-time commencement 2027; excluded courses (Aviation & Piloting, Nursing, Physiotherapy, OT, research masters, doctorates); tuition-fee-only coverage. No separate scholarship deadline published in the official notification.</p>
''',
 dl_long='No separate deadline \u2014 automatic assessment with your 2027 course application',
 offlinks=[('Swinburne \u2014 International scholarships (official)', 'https://www.swinburne.edu.au/courses/scholarships/international-scholarships/')],
 related_titles=['griffith-vc', 'deakin-vc-2027', 'monash-rtp', 'adelaide2027'],
))

# ---------------------------------------------------------------- 3. Hawaii EWC
A.append(dict(
 slug='hawaii-ewc-graduate-fellowship-2027-usa',
 title='University of Hawaii EWC Graduate Fellowship 2027 in United States (Fully Funded)',
 meta='University of Hawaii East-West Center Graduate Fellowship 2027: full UH Manoa tuition and fees, EWC housing, living stipend, books allowance and health-insurance subsidy (~$22,000/year package). Deadline 1 December 2026 — eligibility, documents, how to apply and FAQs.',
 short='Hawaii EWC Fellowship 2027', kicker='USA \u00b7 Masters/PhD \u00b7 Fully Funded', mono='EWC',
 prov_short='East-West Center', prov_cat='Research Institute \u00b7 USA',
 h1='University of Hawaii EWC Graduate Fellowship 2027 in United States (Fully Funded)',
 sub='Study for your master\u2019s or doctorate at the University of Hawai\u02bbi at M\u0101noa while living in one of America\u2019s most international residential communities: the East-West Center Graduate Fellowship covers full-time graduate tuition and fees, a room in an EWC residence hall, a living stipend and a health-insurance subsidy — a package the Center values at about $22,000 a year. Applications close 1 December 2026.',
 dpill='Deadline 1 Dec 2026 \u00b7 39 days left',
 facts=facts([('Award', 'Full-time graduate tuition and fees at the University of Hawai\u02bbi at M\u0101noa rate; single-occupancy housing in an East-West Center residence hall for the academic year; a stipend toward food and daily expenses; a books and materials allowance; and a subsidy toward health insurance. The Center values the total package at about $22,000 per year. Fellows also get automatic consideration for EWC Alumni and Foundation scholarships and can compete for travel grants for field study and conference presentations, subject to funding.'),
              ('Eligible', 'Citizens or permanent residents of the United States, or citizens of eligible Asia-Pacific countries (not open to all nationalities \u2014 the list includes countries such as India, Pakistan, Bangladesh, Nepal, China and Indonesia). You must be applying to, admitted to, or enrolled in a graduate degree program at the University of Hawai\u02bbi at M\u0101noa for the following fall, in a field relevant to East-West Center goals — and you must complete the UH admission application separately. Minimum GPA of 3.0 on a 4.0 scale in the last four semesters/six quarters of undergraduate work and in all post-baccalaureate work. Preference is given to master\u2019s-degree applicants. Fellows must be willing to live in the EWC residential community and take part in its leadership, cultural-exchange and community-service programs.'),
              ('How', 'First read the official Application Handbook and FAQ on the East-West Center site and download the two letter-of-reference forms. Apply online to the East-West Center by 11:59 pm Hawaii Standard Time on 1 December 2026. Separately submit the graduate admission application to the University of Hawai\u02bbi at M\u0101noa (its system opens each August 1). Have official transcripts and English test scores reach both offices by 10 January 2027, regardless of any later UH departmental deadline. Ask three referees to submit their letters online through the links they receive once you apply \u2014 late documents may disqualify the application.'),
              ('Deadline', 'Fellowship application: 1 December 2026, 11:59 pm HST. Supporting documents (transcripts, test scores) complete by 10 January 2027. Results are expected around April 2027 for study beginning August 2027.'),
              ('Fine print', 'New awardees must attend the Community Building Institute starting in early-to-mid August, and fellows are required to devote 90 hours to community service during the award period (45 hours for one-year awards). Single fellows live in EWC residence halls; those with minor dependent children must live off-campus.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>East-West Center (EWC)</strong>, based in Honolulu next to the University of Hawai\u02bbi at M\u0101noa, has run one of America\u2019s most distinctive graduate fellowships since the 1960s. The <strong>Graduate Degree Fellowship</strong> funds master\u2019s and doctoral study at UH M\u0101noa for students from the United States and across the Asia-Pacific — but it is deliberately more than a fee waiver. Fellows live together in the Center\u2019s <strong>international residential community</strong> and join a structured program of leadership development, cultural exchange, community service and educational enrichment.</p>
      <p>The funding is comprehensive: <strong>full-time graduate tuition and fees</strong> at the UH rate, <strong>single-occupancy housing</strong> in an EWC residence hall for the academic year, a <strong>stipend toward food and daily expenses</strong>, a <strong>books/materials allowance</strong>, and a <strong>subsidy toward health insurance</strong> — a package the Center values at about <strong>$22,000 per year</strong>. Fellows also receive automatic consideration for EWC Alumni and Foundation scholarships and can compete for travel grants for field study and conferences.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen or permanent resident of the United States</strong>, or a <strong>citizen of an eligible Asia-Pacific country</strong> (not open to all nationalities — the eligible list includes countries such as India, Pakistan, Bangladesh, Nepal, China and Indonesia; check the official list for yours).</li>
        <li>Be <strong>applying to, admitted to, or enrolled in</strong> a graduate degree program at the <strong>University of Hawai\u02bbi at M\u0101noa</strong> for the following fall, in a field relevant to East-West Center goals. The UH admission application must also be completed.</li>
        <li>Hold a <strong>minimum GPA of 3.0 on a 4.0 scale</strong> in the last four semesters/six quarters of undergraduate work and in all post-baccalaureate work.</li>
        <li>Be willing to <strong>live in the EWC residential community</strong> and take part in its leadership, cultural-exchange and community-service programs.</li>
        <li><strong>Preference is given to master\u2019s-degree applicants</strong>, though doctoral applicants are eligible.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full-time graduate tuition and fees</strong> covered toward master\u2019s or doctoral study at UH M\u0101noa.</li>
        <li><strong>Housing</strong> in an East-West Center residence hall, based on single occupancy.</li>
        <li><strong>Stipend</strong> partially covering food and incidental expenses.</li>
        <li><strong>Allowance for books, materials and supplies</strong>, plus a <strong>subsidy toward health insurance</strong>.</li>
        <li><strong>Automatic consideration</strong> for EWC Alumni and Foundation scholarships.</li>
        <li><strong>Competitive travel grants</strong> for field study and conference presentations, subject to funding.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Submit by 1 December 2026:</strong> CV or r\u00e9sum\u00e9; the University of Hawai\u02bbi application acknowledgment (screenshot or PDF of the confirmation); passport biodata page for international applicants.</li>
        <li><strong>Submit by 10 January 2027:</strong> official transcripts from each institution attended; official IELTS, Duolingo or TOEFL scores sent by the testing agency where English proficiency must be shown; three recommendation letters (two on academic/professional ability, one on community service/civic engagement) via the links referees receive after you apply.</li>
        <li>The University of Hawai\u02bbi <strong>statement of objectives</strong> and any additional documents your chosen graduate program requires.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the handbook first</strong>Download the official Application Handbook and FAQ from the East-West Center site and get the academic and civic-engagement letter-of-reference forms — referees use these specific forms.</li>
        <li><strong>Apply online to the East-West Center by 1 December 2026</strong>Submit the EWC fellowship application by <strong>11:59 pm Hawaii Standard Time on 1 December 2026</strong>.</li>
        <li><strong>Apply separately to the University of Hawai\u02bbi</strong>Submit the UH M\u0101noa graduate admission application as well (launched each August 1 for the following year\u2019s admission). The two tracks can run concurrently, but the fellowship cannot start without UH admission.</li>
        <li><strong>Get documents in by 10 January 2027</strong>Official transcripts and English test scores must reach both offices by 10 January 2027 — even if your UH departmental deadline is later.</li>
        <li><strong>Line up three referees early</strong>Referees submit online through links they receive after you apply. Late documents may disqualify the application, so brief your referees well ahead of December.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need UH admission before applying to the EWC?',
  'No. Applications to the East-West Center and the University of Hawai\u02bbi can be done concurrently, but both must be submitted; the fellowship cannot start without UH admission to a graduate program.'),
 ('Which countries can apply?',
  'Citizens or permanent residents of the United States and citizens of many Asian and Pacific countries, including Pakistan, India, Bangladesh, Nepal, China and Indonesia. The award is not open to all nationalities — check the official eligibility list for your country.'),
 ('What are the key dates?',
  'The fellowship application closes at 11:59 pm Hawaii Standard Time on 1 December 2026, and all supporting documents for both UH and the EWC must be complete by 10 January 2027. Results are expected around April 2027 for study beginning August 2027.'),
 ('Is there a separate track for ADB-JSP applicants?',
  'Yes. The ADB-Japan Scholarship Program is administered through the same office and has its own supplementary application and deadlines, alongside the Graduate Degree Fellowship.'),
 ('What do fellows do besides their degree?',
  'Fellows live together in the EWC international residential community and take part in leadership development projects, internships, cultural exchange, educational enrichment events and community service — the residential and community dimension is central to the fellowship. New awardees attend the Community Building Institute starting in early-to-mid August.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: eastwestcenter.org (official, crawled 23 Oct 2026) — Graduate Degree Fellowship apply page: 2026-2027 competition opened 15 Aug, closes 1 Dec (11:59 pm HST), UH application via manoa.hawaii.edu/graduate (opens Aug 1), documents complete by 10 Jan regardless of departmental deadlines, two reference forms; award-details page: full-time UH M\u0101noa tuition+fees, EWC housing (single occupancy), food/incidentals stipend, CBI required early-to-mid August, 90 hrs community service; student-life page: EWC residential community required; gksscholarships.com + insurab.com + scholarshipsedge.com — ~$22,000/yr package value, 3.0 GPA, US + Asia-Pacific countries (incl. India, Pakistan, Bangladesh, Nepal, China, Indonesia), preference for master\u2019s, 3 referees (2 academic, 1 civic engagement).</p>
''',
 dl_long='December 1, 2026 (11:59 pm HST) \u2014 documents complete by January 10, 2027',
 offlinks=[('East-West Center \u2014 Graduate Degree Fellowship: apply now (official)', 'https://www.eastwestcenter.org/apply/east-west-center-graduate-degree-fellowship-apply-now'),
           ('East-West Center \u2014 award details (official)', 'https://www.eastwestcenter.org/education/ewc-graduate-degree-fellowship/gdf-award-details')],
 related_titles=['hawaii-adb', 'apu-adb', 'keio-adb', 'u-tokyo-mext'],
))

# ---------------------------------------------------------------- 4. Hawaii ADB-JSP
A.append(dict(
 slug='hawaii-adb-jsp-scholarship-2027-usa',
 title='University of Hawaii ADB-JSP Scholarship 2027 in USA (Fully Funded)',
 meta='University of Hawaii ADB-JSP Scholarship 2027: fully funded master\u2019s at UH Manoa for professionals from ADB developing member countries — tuition, housing, monthly stipend, airfare, insurance, J-1 sponsorship. Biennial intake: deadline 1 December 2026, references by 15 December 2026.',
 short='Hawaii ADB-JSP 2027', kicker='USA \u00b7 Masters \u00b7 Fully Funded', mono='ADB',
 prov_short='Asian Development Bank / East-West Center', prov_cat='Multilateral \u00b7 USA',
 h1='University of Hawaii ADB-JSP Scholarship 2027 in USA (Fully Funded)',
 sub='A rare fully funded American master\u2019s for development professionals: the ADB-Japan Scholarship Program, financed by the Government of Japan and run through the East-West Center, pays full tuition at the University of Hawai\u02bbi at M\u0101noa plus housing, a monthly stipend, round-trip airfare and insurance. This Fall 2027 intake is biennial — miss it and the next cycle opens for Fall 2029. Deadline: 1 December 2026.',
 dpill='Deadline 1 Dec 2026 \u00b7 39 days left',
 facts=facts([('Award', 'Full tuition and fees at the University of Hawai\u02bbi at M\u0101noa; monthly subsistence allowance including housing (accommodation in East-West Center residential facilities); economy round-trip airfare between the home country and Honolulu; books and instructional materials; medical and health insurance; a thesis-preparation grant for eligible research; and J-1 Exchange Visitor visa sponsorship through the East-West Center track.'),
              ('Eligible', 'Citizen and current resident of an eligible ADB developing member country \u2014 applicants living or working in a country other than their home country are ineligible. Aged 35 or younger at the time of application. Hold a four-year bachelor\u2019s degree or equivalent with a strong academic record. Have at least two years of full-time professional work experience after completing the university degree. Have not previously studied abroad (outside ADB developing member countries) and are not seeking a second master\u2019s degree. Be admitted to an approved ADB-JSP master\u2019s program in a development-related field (e.g. Economics, Public Administration, Urban and Regional Planning, Global MBA), meet the program\u2019s English-language requirements, be in good health, and intend to return home after study.'),
              ('How', 'First confirm your target field is on the ADB-JSP approved list \u2014 not every UHM graduate program qualifies. Apply for admission to the chosen master\u2019s program at the University of Hawai\u02bbi at M\u0101noa (Graduate Division, or the Shidler Global MBA portal for the Global MBA). In parallel, prepare and submit the ADB-JSP scholarship application to the East-West Center by 1 December 2026 \u2014 do not wait for the admission decision. Arrange for three referees to submit their reference letters directly to EWC by 15 December 2026. Have official English test scores sent directly from the testing service. Note this intake is biennial: after this cycle, the next ADB-JSP application at EWC opens for Fall 2029.'),
              ('Deadline', 'ADB-JSP application to the East-West Center: 1 December 2026 (opened 18 August 2026). Reference letters: 15 December 2026.'),
              ('Fine print', 'Scholars are expected to return to their home countries after completing their studies and use their knowledge to promote socioeconomic development \u2014 this is not designed as a pathway to staying in the US. The application includes four required essay questions.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Asian Development Bank\u2013Japan Scholarship Program (ADB-JSP)</strong> was established in April 1988 with financing from the <strong>Government of Japan</strong> to strengthen human-resource capacity in ADB\u2019s developing member countries. Most ADB-JSP awards send scholars to universities across Asia — the <strong>University of Hawai\u02bbi at M\u0101noa</strong> track, administered by the <strong>East-West Center (EWC)</strong>, is the program\u2019s American outpost, pairing a funded master\u2019s degree with the Center\u2019s residential, educational and leadership-development programs in Honolulu.</p>
      <p>The package is genuinely comprehensive: <strong>full tuition and fees</strong>, <strong>housing</strong> in EWC residential facilities, a <strong>monthly living stipend</strong>, <strong>round-trip airfare</strong> between home and Honolulu, <strong>books</strong>, <strong>health insurance</strong>, and <strong>J-1 Exchange Visitor visa sponsorship</strong> — the last of which removes a real layer of complexity for applicants navigating US immigration on their own. One structural warning matters more here than for annual scholarships: the East-West Center opens ADB-JSP applications <strong>every other year</strong>, so the Fall 2027 cycle (open August\u2013December 2026) is followed by nothing until <strong>Fall 2029</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen and current resident of an eligible ADB developing member country</strong>. Applicants living or working in a country other than their home country are ineligible.</li>
        <li>Be <strong>35 years old or younger</strong> at the time of application.</li>
        <li>Hold a <strong>four-year bachelor\u2019s degree or equivalent</strong> with a strong academic record.</li>
        <li>Have at least <strong>2 years of full-time professional work experience</strong> after completing the university degree.</li>
        <li><strong>Not have previously studied abroad</strong> (in a country outside ADB developing member countries) and <strong>not be seeking a second master\u2019s degree</strong>.</li>
        <li>Be admitted to an <strong>approved ADB-JSP master\u2019s program</strong> in a development-related field — e.g. Economics, Public Administration, Urban and Regional Planning, Global MBA, Geography, Natural Resources and Environmental Management, Oceanography, Pacific Islands Studies, Sociology, Tropical Plant and Soil Sciences. Check the approved list: not every UHM program qualifies.</li>
        <li>Meet the program\u2019s <strong>English-language requirements</strong>, be in <strong>good health</strong>, and <strong>intend to return home</strong> after study.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and additional fees</strong> for the master\u2019s degree.</li>
        <li><strong>Monthly subsistence allowance</strong> covering living costs, plus <strong>housing</strong> in EWC residential facilities.</li>
        <li><strong>Economy round-trip airfare</strong> between the home country and Honolulu.</li>
        <li><strong>Books and instructional materials</strong> allowance.</li>
        <li><strong>Medical and health insurance</strong>.</li>
        <li><strong>Thesis or research support</strong> where applicable, and <strong>J-1 visa sponsorship</strong>.</li>
        <li>Participation in the East-West Center\u2019s <strong>residential, educational and leadership development</strong> programs.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed ADB-JSP online application</strong> including <strong>four required essay questions</strong>.</li>
        <li><strong>Curriculum vitae or r\u00e9sum\u00e9.</strong></li>
        <li><strong>Transcripts and degree/graduation certificates</strong> from every higher-education institution attended.</li>
        <li><strong>Official TOEFL/IELTS results</strong> sent directly by the testing service.</li>
        <li><strong>Three letters of reference</strong> submitted directly by the referees to EWC (due 15 December 2026).</li>
        <li><strong>Proof of the University of Hawai\u02bbi application submission</strong>, plus the UH admission documents (statement of objectives, test scores, application fee — the fee is reimbursed for one program if the scholarship is awarded).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm your field is approved</strong>Check the ADB-JSP approved-fields list on the East-West Center page first — applying to a non-approved UHM program wastes the whole effort.</li>
        <li><strong>Apply to the University of Hawai\u02bbi in parallel</strong>Submit the UHM graduate admission application for your approved master\u2019s program (Graduate Division, or the Shidler portal for the Global MBA). Do not wait for the admission decision before starting the scholarship application.</li>
        <li><strong>Submit the ADB-JSP application to EWC by 1 December 2026</strong>Complete the East-West Center ADB-JSP application, including the four essay questions, by the closing date.</li>
        <li><strong>Lock in your referees early</strong>Three reference letters must reach EWC directly from your referees by <strong>15 December 2026</strong> — two weeks after the main deadline, and a classic point of failure.</li>
        <li><strong>Send test scores officially</strong>Have TOEFL/IELTS results sent directly by the testing service; screenshots or applicant-forwarded copies do not count.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the ADB-JSP at Hawaii?',
  'The Asian Development Bank\u2013Japan Scholarship Program, financed by the Government of Japan and administered at this site by the East-West Center, funds master\u2019s study at the University of Hawai\u02bbi at M\u0101noa for professionals from ADB\u2019s developing member countries. It is offered every other year — this is the Fall 2027 intake.'),
 ('What is the exact deadline?',
  'The EWC opened applications on 18 August 2026 and closes the ADB-JSP application on 1 December 2026. Reference letters are due 15 December 2026.'),
 ('Can I apply while my UH admission is pending?',
  'Yes. The two tracks run in parallel and you should not wait for the admission decision, since both timelines are tight. But you must complete the UH admission application separately.'),
 ('Do I have to return home after the degree?',
  'Yes. Scholars are expected to return to their home countries after completing their studies and apply their new knowledge to promote socioeconomic development.'),
 ('Which fields are approved?',
  'Development-related master\u2019s programs such as Business Administration (Global MBA), Economics, Geography, Natural Resources and Environmental Management, Ocean and Resources Engineering, Oceanography, Pacific Islands Studies, Public Administration, Sociology, Tropical Plant and Soil Sciences, and Urban and Regional Planning.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: eastwestcenter.org/apply/asian-development-bank-japan-scholarship-program (official, crawled 23 Oct 2026) — opening 18 Aug 2026, closing 1 Dec 2026, biennial cycle (next Fall 2029), established Apr 1988 with Government of Japan financing, approved fields, return-home expectation; insurab.com + gksscholarships.com + scholarships365.biz + scholarpositions.com — 1 Dec 2026 deadline, refs 15 Dec 2026, full tuition+fees, housing, monthly stipend, round-trip airfare, books, insurance, J-1 sponsorship, thesis grant; eligibility: ADB developing member country citizen resident at home, \u226435, 4-yr bachelor\u2019s, 2+ yrs work experience, no prior study abroad, no second master\u2019s, good health.</p>
''',
 dl_long='December 1, 2026 \u2014 reference letters due December 15, 2026',
 offlinks=[('East-West Center \u2014 ADB-Japan Scholarship Program (official)', 'https://www.eastwestcenter.org/apply/asian-development-bank-japan-scholarship-program')],
 related_titles=['hawaii-ewc', 'apu-adb', 'keio-adb', 'nus-adb-2027'],
))

# ---------------------------------------------------------------- 5. INPEX
A.append(dict(
 slug='inpex-scholarship-program-2027-japan',
 title='INPEX Scholarship Program 2027 in Japan (Fully Funded)',
 meta='INPEX Scholarship Program 2027: fully funded master\u2019s in Japan for citizens of Indonesia, Australia and the UAE — full tuition, JPY 160,000/month, JPY 60,000 settling-in grant, round-trip airfare. A Letter of Acceptance from a Japanese professor is mandatory. Deadline 31 October 2026.',
 short='INPEX Scholarship 2027', kicker='Japan \u00b7 Masters \u00b7 Fully Funded', mono='IN',
 prov_short='INPEX Scholarship Foundation', prov_cat='Foundation \u00b7 Japan',
 h1='INPEX Scholarship Program 2027 in Japan (Fully Funded)',
 sub='Full funding before you ever leave home: the INPEX Scholarship Foundation recruits master\u2019s students from Indonesia, Australia and the UAE while they are still overseas, paying full tuition plus JPY 160,000 a month, a JPY 60,000 settling-in grant and round-trip airfare. The catch is the mandatory Letter of Acceptance from a Japanese professor. Applications close 31 October 2026.',
 dpill='Deadline 31 Oct 2026 \u00b7 8 days left',
 facts=facts([('Award', 'Full coverage of examination, entrance and tuition fees; a monthly living stipend of JPY 160,000; a one-time settling-in allowance of JPY 60,000 on arrival; economy round-trip airfare between the home country and Japan; and pre-departure Japanese-language training support. Support runs for up to 2 years and 8 months.'),
              ('Eligible', 'Citizens of Indonesia, Australia or the United Arab Emirates only \u2014 no other nationalities are eligible. Under 30 years of age at the time of application. Hold a bachelor\u2019s degree with a GPA of at least 3.0/4.0 (Australian applicants: 3.0/4.0 or 5.25/7.0) from a major recognized university. Indonesian applicants: degree and proposed master\u2019s must be in Natural Sciences (STEM); Australian and UAE applicants may study any field (Natural Sciences, Social Sciences or Humanities; clinical medical degrees excluded). A Letter of Acceptance from a prospective Japanese graduate school or professor is compulsory at submission.'),
              ('How', 'Download the 2027 Scholarship Application Guidelines and the country-specific application form from the INPEX Scholarship Foundation website. Choose a suitable Japanese graduate school and master\u2019s program and identify a professor whose research matches your proposed study. Contact the professor directly with your CV and research proposal and secure the Letter of Acceptance \u2014 start this well before the deadline, as it is the most demanding step. Prepare the remaining documents per your country\u2019s 2027 guidelines (type everything in English; maximum 20 MB per email; cloud-storage links are not permitted). Submit the complete package according to your country\u2019s instructions by 31 October 2026 (23:59 Tokyo time). Contact the Foundation if you do not receive an acknowledgment email.'),
              ('Deadline', '31 October 2026, 23:59 Tokyo time. The 2027 guidelines were released 1 July 2026; the window ran 1 August to 31 October 2026.'),
              ('Fine print', 'The Foundation also runs a separate outbound track for Japanese citizens wishing to study or research in Indonesia, Australia or the UAE. Final recipients are typically notified by the end of March 2027, ahead of Japan\u2019s April academic-year start.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>INPEX Scholarship Foundation</strong>, the philanthropic arm of the Japanese energy company INPEX, funds master\u2019s study in Japan for students from just three countries — <strong>Indonesia, Australia and the United Arab Emirates</strong> — reflecting the company\u2019s operating footprint. What makes the program unusual is its <strong>pre-departure recruitment model</strong>: unlike most Japan scholarships that target students already enrolled in Japan, INPEX selects scholars while they are still overseas, so you have full funding certainty before you ever leave home.</p>
      <p>The support is fully funded in the real sense: <strong>examination, entrance and tuition fees paid in full</strong>, a <strong>JPY 160,000 monthly living stipend</strong>, a <strong>JPY 60,000 settling-in grant</strong> on arrival, <strong>economy round-trip airfare</strong>, and financial help for <strong>pre-departure Japanese-language preparation</strong> — for up to 2 years and 8 months. You may study at any accredited Japanese public or private graduate university, including the top national institutions.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of Indonesia, Australia or the United Arab Emirates</strong> — no other nationalities are eligible, regardless of academic qualifications.</li>
        <li>Be <strong>under 30 years of age</strong> at the time of application.</li>
        <li>Hold a <strong>bachelor\u2019s degree</strong> with a <strong>GPA of at least 3.0/4.0</strong> (Australian applicants: 3.0/4.0 or 5.25/7.0) from a major recognized university.</li>
        <li><strong>Indonesian applicants:</strong> degree and proposed master\u2019s must be in <strong>Natural Sciences (STEM)</strong>. <strong>Australian and UAE applicants:</strong> any field across Natural Sciences, Social Sciences or Humanities — clinical medical degrees excluded.</li>
        <li>Hold a <strong>Letter of Acceptance (LOA)</strong> from a prospective Japanese graduate school or professor <strong>at the time of application</strong> — this is mandatory, not something gathered later.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Complete tuition, entrance and examination fees</strong> paid.</li>
        <li><strong>JPY 160,000 per month</strong> for living expenses.</li>
        <li><strong>JPY 60,000 settling-in grant</strong> disbursed on arrival in Japan.</li>
        <li><strong>Round-trip economy airfare</strong> between the scholar\u2019s home country and Japan.</li>
        <li><strong>Financial assistance</strong> for pre-departure Japanese-language preparation.</li>
        <li>Study at <strong>any accredited Japanese public or private graduate university</strong>.</li>
        <li><strong>Pre-arrival recruitment model</strong> — scholars plan the move with full funding certainty before departing.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed country-specific 2027 application form</strong> — typed in English; handwritten forms are not accepted.</li>
        <li><strong>Degree certificate</strong> and <strong>official academic transcript</strong>.</li>
        <li><strong>Valid passport</strong> copy.</li>
        <li><strong>CV or r\u00e9sum\u00e9.</strong></li>
        <li><strong>Letter of Acceptance (LOA)</strong> from the prospective Japanese professor — compulsory at submission.</li>
        <li><strong>Other supporting documents</strong> specified in the country-specific 2027 guidelines (e.g. recommendation letters, study plan, English test scores for Indonesian and UAE applicants, ID photo).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start with the professor, not the paperwork</strong>The LOA is the real bottleneck. Research Japanese graduate schools and faculty pages, and email professors whose published research overlaps with your proposed study — a short, specific message with your CV and research proposal. Generic requests rarely get replies. Begin months before the window, not weeks.</li>
        <li><strong>Download your country\u2019s 2027 guidelines and form</strong>Get the 2027 Scholarship Application Guidelines and the application form for Indonesia, Australia or the UAE from the INPEX Scholarship Foundation website.</li>
        <li><strong>Secure the Letter of Acceptance</strong>Confirm a specific prospective supervisor agrees to accept you if the university admits you. Some professors want a video call before agreeing — budget time for this.</li>
        <li><strong>Prepare the remaining documents</strong>Type everything in English (with simple English translations/outlines for documents in other languages), and keep attachments under <strong>20 MB per email</strong> — split across multiple emails if needed. Cloud-storage links such as Google Drive or OneDrive are <strong>not permitted</strong>.</li>
        <li><strong>Submit by 31 October 2026, 23:59 Tokyo time</strong>Send the complete package by email to the Foundation (subject line \u201c2027 Scholarship Application (Name)\u201d) or per your country\u2019s instructions. If no acknowledgment email arrives, contact the Foundation to confirm receipt.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Who can apply?',
  'Only citizens of Indonesia, Australia and the UAE. If you do not hold one of those nationalities, the program is not available to you regardless of academic qualifications.'),
 ('What is the Letter of Acceptance?',
  'It is a written statement from a specific prospective supervisor at your target Japanese university confirming they will accept you if the university admits you. You must secure this yourself through direct outreach before you can submit — it is the compulsory first step, not a supporting document collected along the way.'),
 ('Which fields can I study?',
  'Indonesian applicants must propose a master\u2019s in a Natural Science (STEM) field. Australian and UAE applicants may choose any field across Natural Sciences, Social Sciences and Humanities. Clinical medical degrees are excluded.'),
 ('What is the timeline?',
  'The 2027 guidelines were released on 1 July 2026 and the application window ran 1 August to 31 October 2026. Because the LOA depends on professor outreach, successful applicants typically started contacting supervisors in July or August. Final recipients are notified by the end of March 2027.'),
 ('How is INPEX different from other Japan scholarships?',
  'Unlike most Japan scholarships that target students already enrolled in Japan, INPEX recruits overseas residents before departure, so you have full funding certainty before you ever leave home. There is also a separate outbound track for Japanese citizens wishing to study or research in Indonesia, Australia or the UAE.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: inpex-s.com (official Foundation site; 2027 application form PDF at inpex-s.com/pdf/APPLICATION_FORM_FOR_SCHOLARSHIPS_EN_2027.pdf) — 2027 guidelines, country-specific forms, LOA mandatory, typed-in-English rule, 20 MB/email cap, no cloud links; daadscholarship.com + scholarpositions.com + gradualin.com + opportunityportal.info — deadline 31 Oct 2026 (23:59 JST), window 1 Aug\u201331 Oct 2026, guidelines released 1 Jul 2026, JPY 160,000/month, JPY 60,000 settling-in, full fees, round-trip airfare, up to 2 yrs 8 months, Indonesia/Australia/UAE only, <30, GPA \u22653.0/4.0 (5.25/7.0 AU), Indonesian STEM-only, email isf-foundation@inpex.com with subject \u201c2027 Scholarship Application (Name)\u201d, decisions by end Mar 2027.</p>
''',
 dl_long='October 31, 2026 (23:59 Tokyo time)',
 offlinks=[('INPEX Scholarship Foundation \u2014 official site', 'https://www.inpex-s.com/'),
           ('2027 application form (PDF, official)', 'https://www.inpex-s.com/pdf/APPLICATION_FORM_FOR_SCHOLARSHIPS_EN_2027.pdf')],
 related_titles=['u-tokyo-mext', 'science-tokyo', 'hawaii-adb', 'hawaii-ewc'],
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
    # write checkpoints as we go
    json.dump(sizes, open('/tmp/batch42_built.json','w'))

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
    assert '#' not in a['slug']
    assert 'wa.me/919905166009' in txt, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

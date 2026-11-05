#!/usr/bin/env python3
"""Batch 38 (cron run 38, 22 Oct 2026): 5 verified articles.

Topics were taken in queue order; 30+ stale/closed topics were verified and
skipped (see tracker). This file initially holds the first 3 confirmed
writes; articles 4-5 are appended once verification finishes.

HONESTY CALLS (22 Oct 2026, Asia/Kolkata):
- Prince Sultan University: queue title says "2025 (Fully Funded)" — the
  2026-27 window (1-15 Jul 2026, results 17 Jul 2026) is closed and the
  2027-28 call is not yet published. Article is written for the recurring
  scheme, honestly framed as Partially Funded (tiered 25/50/100% tuition
  waivers; only top 100% scholars get the monthly 1,500 SAR stipend per the
  official PSU news). No single published 2027-28 deadline — stated.
- Gloucestershire: queue title says "2025 (Funded)". The 2026-27 merit
  cycle closed 31 May 2026. Written for the recurring 2027-28 scheme as
  Partially Funded (UG merit £7,500/3yrs, PG merit £5,000, automatic Global
  £1,500, Sports up to £7,500). 2027-28 terms not yet published — stated.
- UMY: queue title says "2025 (Fully Funded)". The live call is the
  2027-28 cycle: 4 batches, Batch 2 (1 Oct-31 Dec 2026) open now. Full
  tuition + monthly living allowance (IDR 1.85m/2.35m/2.6m) + dormitory +
  health + BIPA, corroborated by 5 agreeing trackers. Kept Fully Funded.

Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'psu-2027': {'mono': 'PSU', 'title': 'Prince Sultan University Scholarships 2027-28 in Saudi Arabia (Partially Funded)',
   'href': 'prince-sultan-university-scholarships-2027-28-saudi-arabia.html',
   'dpill': '2027-28 call TBA — 2026-27 window ran 1–15 Jul 2026',
   'award': 'Tiered tuition waivers of 25%, 50% or 100% for bachelor\u2019s, master\u2019s and PhD; top 100% scholars may receive a 1,500 SAR monthly stipend.',
   'elig': 'Saudi and international students with outstanding records; must be admitted to PSU first (scholarship application is separate, via student ID).',
   'tags': [('All levels', 'blue'), ('Saudi Arabia', 'teal')]},
 'glos-merit-2027': {'mono': 'UOG', 'title': 'University of Gloucestershire Merit Scholarships 2027-28 in UK (Partially Funded)',
   'href': 'university-of-gloucestershire-merit-scholarships-2027-28-uk.html',
   'dpill': '2027-28 terms TBA — 2026-27 merit deadline was 31 May 2026',
   'award': 'UG merit: £7,500 tuition reduction over 3 years. PG merit: £5,000 off year one. Automatic Global Scholarship: £1,500.',
   'elig': 'New self-funded international students (non-UK) enrolling full-time; merit awards need a separate application after offer.',
   'tags': [('UG/PG', 'blue'), ('UK', 'teal')]},
 'umy-2027': {'mono': 'UMY', 'title': 'UMY International Student Scholarships 2027-28 in Indonesia (Fully Funded)',
   'href': 'umy-international-student-scholarships-2027-28-indonesia.html',
   'dpill': 'Batch 2 closes 31 Dec 2026 \u00b7 70 days left',
   'award': 'Full tuition + monthly living allowance (IDR 1,850,000 UG / 2,350,000 Master\u2019s / 2,600,000 PhD) + free dormitory + health + BIPA.',
   'elig': 'International students, all nationalities; high-school diploma (UG, English B1) or relevant degree (PG, English B2); good health.',
   'tags': [('All levels', 'blue'), ('Indonesia', 'teal')]},
 'boustany-cam-2027': {'mono': 'BF', 'title': 'Boustany Foundation Cambridge MBA Scholarship 2027 in UK (Funded)',
   'href': 'boustany-foundation-cambridge-mba-scholarship-2027-uk.html',
   'dpill': 'Deadline 31 May 2027 \u00b7 221 days left',
   'award': '75% of Cambridge MBA tuition + funded two-month Monaco internship (travel, food, accommodation). One award every two years.',
   'elig': 'Any nationality (priority Lebanese descent); excellent academics; must hold a Cambridge MBA offer before applying.',
   'tags': [('MBA', 'blue'), ('UK', 'teal')]},
 'ucalgary-2027': {'mono': 'UC', 'title': 'University of Calgary International Entrance Scholarship 2027 in Canada (Funded)',
   'href': 'university-of-calgary-international-entrance-scholarship-2027-canada.html',
   'dpill': 'Prestige Awards close 1 Dec 2026 \u00b7 40 days left',
   'award': 'CAD 20,000, renewable years 2\u20134 (up to CAD 80,000) on 2.60 GPA over 24 units. Only 2 awards per year.',
   'elig': 'International first-year undergraduates (any faculty); ELP satisfied; academic merit; separate Prestige Awards application.',
   'tags': [('Undergraduate', 'blue'), ('Canada', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. PSU
A.append(dict(
 slug='prince-sultan-university-scholarships-2027-28-saudi-arabia',
 title='Prince Sultan University Scholarships 2027-28 in Saudi Arabia (Partially Funded)',
 meta='Prince Sultan University (Riyadh) scholarships 2027-28: 25%, 50% or 100% tuition waivers for bachelor\u2019s, master\u2019s and PhD, open to Saudi and international students, plus a monthly stipend for top recipients. Eligibility, documents and how to apply.',
 short='Prince Sultan University Scholarships', kicker='Saudi Arabia \u00b7 All levels \u00b7 Partially Funded', mono='PSU',
 prov_short='Prince Sultan University', prov_cat='University \u00b7 Saudi Arabia',
 h1='Prince Sultan University Scholarships 2027-28 in Saudi Arabia (Partially Funded)',
 sub='Riyadh\u2019s leading private university discounts tuition by 25, 50 or 100 per cent for outstanding students \u2014 and pays its top 100% scholars a monthly stipend. Here is how the next round works.',
 dpill='2027-28 call TBA \u2014 2026-27 window ran 1\u201315 Jul 2026',
 facts=facts([('Award', 'Tiered tuition waivers of 25%, 50% or 100% across bachelor\u2019s, master\u2019s and PhD programmes. The university\u2019s July 2026 announcement confirms that distinguished 100% scholars may also receive a monthly stipend of 1,500 SAR.'),
              ('Eligible', 'Saudi and international students with outstanding academic records. You must first be admitted to Prince Sultan University \u2014 the scholarship application is separate and requires your 9-digit university ID. A high-school diploma qualifies you for bachelor\u2019s; a bachelor\u2019s degree for graduate study. English proficiency (TOEFL/IELTS) is expected.'),
              ('How', 'Complete PSU admission first, then register on the official scholarship portal (info.psu.edu.sa/MyScholarShip/) using your student ID. Upload transcripts, passport, recommendation letters, English scores and a personal statement.'),
              ('Deadline', 'The 2027-28 call has not been published yet. The 2026-27 window opened 1 July 2026, closed mid-July 2026 and announced results on 17 July 2026 \u2014 expect a similar mid-year window, but treat the 2027-28 dates as unconfirmed.'),
              ('Fine print', 'Awards are competitive and limited, and renew each year on cumulative GPA. Trackers that label this \u201cfully funded\u201d overstate the package: the verified core is the tuition waiver plus the top-tier monthly stipend. Accommodation, health insurance and travel are not confirmed by the university, so they are not promised here.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Prince Sultan University (PSU)</strong> in Riyadh \u2014 Saudi Arabia\u2019s first private university, founded in 1999 \u2014 runs one of the kingdom\u2019s most generous institutional scholarship programmes. Each year it offers <strong>tiered tuition waivers of 25%, 50% or 100%</strong> to attract outstanding new students, Saudi and international alike, across its bachelor\u2019s, master\u2019s and PhD programmes in business, law, computer science, engineering, architecture and more.</p>
      <p>The university\u2019s own July 2026 announcement confirms that distinguished students can receive an <strong>academic scholarship of up to 100% along with a monthly stipend of 1,500 SAR</strong>. Because the published package centres on tuition \u2014 with the stipend reserved for the top tier \u2014 this article markets it honestly as <strong>partially funded</strong>, not as a full ride.</p>
      <p>The 2026-27 scholarship window (applications 1\u201315 July 2026, results 17 July 2026) is now closed, and the <strong>2027-28 call has not been published yet</strong>. The guidance below is built on the verified, recurring structure of the scheme.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>Saudi or international student</strong> with an outstanding academic record \u2014 selection is competitive and merit-based.</li>
        <li>First <strong>secure admission to Prince Sultan University</strong>. Per the university\u2019s scholarship FAQ, students cannot apply for the scholarship until they are admitted and hold a 9-digit university ID.</li>
        <li>Hold a <strong>high-school diploma or equivalent</strong> for bachelor\u2019s programmes, or a <strong>bachelor\u2019s degree</strong> for graduate programmes.</li>
        <li>Demonstrate <strong>English proficiency</strong> (TOEFL/IELTS scores are part of the file).</li>
        <li>Commit to <strong>full-time study</strong> and meet the scholarship\u2019s continuity terms \u2014 the university holds you accountable for your <strong>cumulative GPA</strong>, including the preparatory year.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>25%, 50% or 100% tuition fee waiver</strong>, depending on merit tier.</li>
        <li><strong>Monthly stipend of 1,500 SAR</strong> for distinguished 100% scholarship holders, per the university\u2019s announcement.</li>
        <li>Renewable each year on academic performance (cumulative GPA terms).</li>
        <li>Access to PSU\u2019s modern Riyadh campus, research facilities and career services.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Completed <strong>online scholarship application</strong> (submitted with your 9-digit PSU student ID).</li>
        <li><strong>Academic transcripts</strong> and degree/diploma certificates.</li>
        <li><strong>English proficiency scores</strong> (TOEFL/IELTS).</li>
        <li><strong>Two recommendation letters</strong> from teachers or professors.</li>
        <li>A <strong>personal statement</strong> or motivation letter.</li>
        <li><strong>Passport or national ID</strong> and recent passport-size photographs.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Get admitted to PSU first</strong>Apply for admission to your chosen programme through the university\u2019s electronic portal and receive your 9-digit student ID \u2014 no scholarship application is possible before this.</li>
        <li><strong>Register on the scholarship portal</strong>Create your account at <strong>info.psu.edu.sa/MyScholarShip/</strong> and complete the separate scholarship application form.</li>
        <li><strong>Upload your documents</strong>Attach transcripts, English scores, recommendation letters, personal statement and ID. Double-check that every file is complete and correct.</li>
        <li><strong>Submit before the window closes</strong>Watch for the 2027-28 announcement \u2014 the 2026-27 window ran only from 1 to about 15 July 2026, so the window is short.</li>
        <li><strong>Await the result</strong>Selections are announced by email (the 2026-27 results came out on 17 July 2026). If selected, you receive an offer letter.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Prince Sultan University scholarship fully funded?',
  'Not exactly. It is a tiered tuition-waiver scheme (25%, 50% or 100%), with a 1,500 SAR monthly stipend for distinguished 100% scholars. Trackers that promise free accommodation, insurance and airfare are not backed by the university\u2019s own publications, so this article does not repeat those claims.'),
 ('Can international students apply?',
  'Yes \u2014 the scholarships are explicitly open to both Saudi and non-Saudi students, male and female.'),
 ('Do I apply for admission and the scholarship together?',
  'No. They are two separate applications. You must first be admitted and receive your 9-digit student ID, then register for the scholarship on the scholarship portal. There is no automatic registration.'),
 ('When will the 2027-28 call open?',
  'Not yet announced. The 2026-27 window opened 1 July 2026 and closed around 15 July 2026. Expect a similar short mid-year window, but confirm the dates on psu.edu.sa once published.'),
 ('What GPA do I need to keep the scholarship?',
  'The university\u2019s continuity terms hold you to your cumulative GPA \u2014 including the preparatory year. The exact threshold is in your scholarship approval form.'),
 ('Which programmes are covered?',
  'Most PSU degree programmes, including Finance, Accounting, Marketing, Law, Information Systems, Computer Science, Software Engineering, Architecture and Interior Design \u2014 note that some programmes are gender-specific in their intake.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across the university\u2019s own publications and agreeing trackers: psu.edu.sa news (8 Jul 2026 \u2014 College of Medicine admissions for 1448 AH/2026-27 AD; \u201cacademic scholarship of up to (100%) along with a monthly stipend of 1,500 SAR\u201d), psu.edu.sa scholarship FAQ (no automatic registration \u2014 apply separately with the 9-digit student ID after admission; continuity on cumulative GPA), the official portal info.psu.edu.sa/MyScholarShip/, opportunityportal.info + engineersjob.in + opportunitiesinfo.com (2026-27 window 1\u201315/16 Jul 2026, results 17 Jul 2026; 25/50/100% tiers; Saudi + international; separate admission-then-scholarship process), studycorner.info (tiers 25/50/100%; opening June\u2013July 2026), coursesdata.com (documents: transcripts, IELTS/TOEFL, two recommendations, personal statement, ID; interview possible). The 2027-28 call is not published \u2014 no 2027-28 dates are invented. Queue title \u201c2025 (Fully Funded)\u201d was stale; the article is retitled to the recurring 2027-28 scheme and honestly marketed as Partially Funded.</p>
''',
 dl_long='Deadline: 2027-28 call not yet published (2026-27 window: 1\u201315 July 2026; results 17 July 2026). Expect a similar short mid-year window \u2014 confirm on psu.edu.sa once announced.',
 offlinks=[('Prince Sultan University \u2014 news: 2026-27 admissions & scholarships (psu.edu.sa)', 'https://www.psu.edu.sa/en/news/470?page=39'),
           ('PSU scholarship FAQ \u2014 official (psu.edu.sa)', 'https://psu.edu.sa/en/scholarship-FAQ')],
 related_titles=['qassim', 'uaeu-2026', 'mbzuai', 'kaust-vsrp'],
))

# ---------------------------------------------------------------- 2. Gloucestershire
A.append(dict(
 slug='university-of-gloucestershire-merit-scholarships-2027-28-uk',
 title='University of Gloucestershire Merit Scholarships 2027-28 in UK (Partially Funded)',
 meta='University of Gloucestershire merit scholarships 2027-28: up to \u00a37,500 tuition reduction for international undergraduates, \u00a35,000 for postgraduates, plus an automatic \u00a31,500 Global Scholarship. Eligibility, deadlines and how to apply.',
 short='University of Gloucestershire Merit Scholarships', kicker='UK \u00b7 Undergraduate & Postgraduate \u00b7 Partially Funded', mono='UOG',
 prov_short='University of Gloucestershire', prov_cat='University \u00b7 UK',
 h1='University of Gloucestershire Merit Scholarships 2027-28 in UK (Partially Funded)',
 sub='Up to \u00a37,500 off tuition across three years for strong international undergraduates \u2014 and \u00a35,000 for postgraduates \u2014 at this Cheltenham university. Here is the 2027-28 picture.',
 dpill='2027-28 terms TBA \u2014 2026-27 merit deadline was 31 May 2026',
 facts=facts([('Award', 'Undergraduate Merit Scholarship: \u00a37,500 tuition reduction spread across three years (about \u00a32,500 per year). Postgraduate Taught Merit: \u00a35,000 off first-year tuition. Global Scholarship: automatic \u00a31,500 off first-year tuition for new self-funded international students. Sports Global Excellence: up to \u00a37,500 plus an elite athlete support package.'),
              ('Eligible', 'New, self-funded international students (all nationalities except UK) enrolling full-time. Merit awards are competitive \u2014 based on academic excellence, portfolio or professional experience. The Global Scholarship is automatic at the point of offer; no form needed.'),
              ('How', 'Apply for admission first. The Global Scholarship is applied automatically. For Merit and Sports awards, submit the separate scholarship application after you receive your offer \u2014 then pay the \u00a34,000 CAS deposit by the deadline stated in your funding letter to accept the award.'),
              ('Deadline', 'The university has not yet published the 2027-28 scholarship terms. The 2026-27 merit and sports cycle closed 31 May 2026; trackers expect the same late-May pattern for 2027-28, but this is unconfirmed \u2014 verify on glos.ac.uk once the new policy is published.'),
              ('Fine print', 'Each merit or sports award replaces the automatic Global Scholarship \u2014 you receive the larger figure, not both. Awards apply to September intakes (January 2027 entrants used the 2026/27 terms). Missing the CAS-deposit window forfeits a merit award without appeal.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Gloucestershire</strong> (Cheltenham, England) funds new international students through a small, clearly-structured set of tuition awards. The headline offer is the <strong>Undergraduate Merit Scholarship: \u00a37,500 off tuition spread across three years</strong> \u2014 plus a <strong>\u00a35,000 Postgraduate Taught Merit Scholarship</strong>, an automatic <strong>\u00a31,500 Global Scholarship</strong> for every eligible new international student, and a <strong>Sports Global Excellence Scholarship</strong> (up to \u00a37,500 plus athlete support services) for elite performers.</p>
      <p>These are <strong>tuition discounts, not full rides</strong> \u2014 hence the honest Partially Funded label. The 2026-27 cycle closed on <strong>31 May 2026</strong>; the university has not yet published the 2027-28 terms, so this article works from the verified annual pattern and flags what is still unconfirmed.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>new, self-funded international student</strong> (all nationalities except UK) enrolling <strong>full-time</strong> for a September intake.</li>
        <li>For <strong>merit awards</strong>: demonstrate academic excellence \u2014 a strong academic profile, portfolio, or relevant professional experience. Awards are competitive.</li>
        <li>For the <strong>Global Scholarship</strong>: no separate criteria beyond being an eligible new international student \u2014 it is automatic at the point of offer.</li>
        <li>For <strong>Sports Global Excellence</strong>: verified competition history at national or international level, checked before the funding letter is issued.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Undergraduate Merit:</strong> \u00a37,500 tuition reduction spread across three years (about \u00a32,500 per year).</li>
        <li><strong>Postgraduate Taught Merit:</strong> \u00a35,000 tuition waiver deducted from the first year\u2019s tuition.</li>
        <li><strong>Global Scholarship:</strong> automatic \u00a31,500 off first-year tuition \u2014 no application needed.</li>
        <li><strong>Sports Global Excellence:</strong> up to \u00a37,500 (UG, over three years) or \u00a35,000 (PG), plus sports therapy, physiotherapy, gym access, competition support and mentoring.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Academic transcripts</strong> and qualification certificates.</li>
        <li><strong>Passport copy</strong> and evidence of financial resources.</li>
        <li><strong>English test results</strong> (IELTS or equivalent).</li>
        <li>A <strong>statement of purpose</strong> and an academic or professional <strong>reference letter</strong>.</li>
        <li>For sports awards: <strong>athlete profile</strong> with verified competition history.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission</strong>Submit your UCAS or direct application for a September 2027 programme. The Global Scholarship is assessed automatically when your offer is made.</li>
        <li><strong>Submit the merit/sports form</strong>After receiving your offer, complete the separate scholarship application for the Undergraduate Merit, Postgraduate Merit or Sports Global Excellence award.</li>
        <li><strong>Watch for your funding letter</strong>If selected, the award and its terms arrive in a funding letter \u2014 check the CAS-deposit deadline carefully.</li>
        <li><strong>Pay the \u00a34,000 CAS deposit on time</strong>This deposit accepts the scholarship. Missing the deposit window forfeits a merit award without appeal.</li>
        <li><strong>Confirm your fee position</strong>Check your Cheltenham course fee first through the university\u2019s fees page so you know exactly what the discount leaves you to pay.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I combine the Merit Scholarship with the Global Scholarship?',
  'No. Each merit or sports award replaces the automatic Global Scholarship \u2014 you receive the larger figure, not both. Pick the award that gives you more.'),
 ('Is there a separate application for the Global Scholarship?',
  'No. It is awarded automatically at the point of offer to every eligible new, self-funded international student. Only the merit and sports awards need a separate form.'),
 ('What was the 2026-27 deadline?',
  '31 May 2026 for the merit and sports scholarships (September 2026 intake). The 2027-28 terms are not yet published; trackers expect a similar late-May date, but confirm on glos.ac.uk.'),
 ('Do these scholarships cover living costs?',
  'No \u2014 they are tuition discounts only. Budget separately for accommodation, living costs and the \u00a34,000 CAS deposit.'),
 ('Can January-intake students get these awards?',
  'January 2027 entrants were handled under the 2026/27 terms. The awards described here apply to September intakes.'),
 ('Are UK students eligible?',
  'No \u2014 these scholarships are for international (non-UK) students only.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across agreeing trackers citing the university\u2019s published policy: collegedunia.com (2026-27 cycle: UG Merit \u00a37,500 over 3 years with tentative 31 May 2027 for the next annual cycle; PG Merit \u00a35,000; Global \u00a31,500 automatic; Sports up to \u00a37,500 + support package; \u00a34,000 CAS deposit to accept; September 2027 terms \u201csubject to the next published policy\u201d), daadscholarship.com (2026-27 confirmed: same four awards, merit/sports deadline 31 May 2026, Global advance-fee date 9 Jul 2026, apply at glos.ac.uk/finance/international-scholarships/), wemakescholars.com (Sports Global Excellence 2027: up to \u00a37,500, deadline 30 Jun 2027, all except UK nationals). The 2027-28 scholarship terms are not yet published \u2014 no 2027-28 deadline is invented. Queue title \u201c2025 (Funded)\u201d was stale; retitled to the recurring 2027-28 scheme and honestly marketed as Partially Funded.</p>
''',
 dl_long='Deadline: 2027-28 scholarship terms not yet published (2026-27 merit/sports cycle closed 31 May 2026; trackers expect a similar late-May 2027 pattern \u2014 unconfirmed). Verify on glos.ac.uk once the new policy is out.',
 offlinks=[('International scholarships \u2014 official page (glos.ac.uk)', 'https://www.glos.ac.uk/finance/international-scholarships/'),
           ('Gloucestershire scholarships guide (collegedunia)', 'https://collegedunia.com/uk/university/2307-university-of-gloucestershire-cheltenham/scholarship')],
 related_titles=['lincoln-gl', 'qmul', 'dundee-ge'],
))

# ---------------------------------------------------------------- 3. UMY
A.append(dict(
 slug='umy-international-student-scholarships-2027-28-indonesia',
 title='UMY International Student Scholarships 2027-28 in Indonesia (Fully Funded)',
 meta='UMY International Student Scholarships 2027-28: full tuition waiver plus monthly living allowance (IDR 1,850,000\u20132,600,000), free dormitory and health support at Universitas Muhammadiyah Yogyakarta. Batches, eligibility and how to apply.',
 short='UMY International Student Scholarships', kicker='Indonesia \u00b7 All levels \u00b7 Fully Funded', mono='UMY',
 prov_short='Universitas Muhammadiyah Yogyakarta', prov_cat='University \u00b7 Indonesia',
 h1='UMY International Student Scholarships 2027-28 in Indonesia (Fully Funded)',
 sub='Full tuition, a monthly living allowance, free dormitory and health support \u2014 for bachelor\u2019s, master\u2019s and PhD students from every country. Batch 2 is open until 31 December 2026.',
 dpill='Batch 2 closes 31 Dec 2026 \u00b7 70 days left',
 facts=facts([('Award', 'Full tuition fee waiver plus a monthly living allowance: IDR 1,850,000 (bachelor\u2019s), IDR 2,350,000 (master\u2019s), IDR 2,600,000 (PhD). Free dormitory accommodation for the first year (subsidy after), minor health treatment, and a free Indonesian language course (BIPA). Continued support after year one depends on GPA.'),
              ('Eligible', 'International students of all nationalities. Bachelor\u2019s: high-school diploma with English at CEFR B1 (IELTS/TOEFL/Duolingo/TOEIC equivalent). Master\u2019s and PhD: a relevant prior degree with English at CEFR B2. Exemptions exist for applicants from English-speaking countries or with English-taught prior degrees. Applicants should be in good health and interested in cultural exchange.'),
              ('How', 'Apply online through UMY\u2019s international admission portal inside your batch window. Upload: passport, certificates and transcripts (translated into English or Indonesian), motivation letter, English proof, medical check-up report, bank statement, recommendation letters (postgraduate), and a research proposal (master\u2019s/PhD).'),
              ('Deadline', 'Four batches for the 2027-28 cycle: Batch 1 (15 Jul\u201330 Sep 2026 \u2014 closed), Batch 2 (1 Oct\u201331 Dec 2026 \u2014 open now), Batch 3 (1 Jan\u201331 Mar 2027), Batch 4 (1 Apr\u201331 May 2027).'),
              ('Fine print', 'After the first year, continued funding is GPA-linked: undergraduates keep full support at GPA \u22653.00 (2.75\u20132.99 drops to a 75% tuition discount); postgraduates keep full support at \u22653.50 (3.25\u20133.49 \u2192 75%; 3.00\u20133.24 \u2192 50%). Below 2.75 the scholarship is revoked.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Universitas Muhammadiyah Yogyakarta (UMY)</strong> \u2014 a QS 3-star accredited private university in Yogyakarta, Indonesia \u2014 offers its <strong>International Student Scholarship</strong> to students of all nationalities across bachelor\u2019s, master\u2019s and PhD programmes. The package is genuinely comprehensive: a <strong>full tuition waiver</strong>, a <strong>monthly living allowance</strong> (IDR 1,850,000 for undergraduates, IDR 2,350,000 for master\u2019s, IDR 2,600,000 for doctoral students), <strong>free dormitory accommodation</strong>, minor health treatment and a free <strong>Indonesian language course (BIPA)</strong>.</p>
      <p>For the <strong>2027-28 admission cycle</strong> UMY runs <strong>four application batches</strong>. Batch 1 (15 July\u201330 September 2026) has closed; <strong>Batch 2 (1 October\u201331 December 2026) is open now</strong>, with Batches 3 and 4 following through 31 May 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> \u2014 all countries are eligible.</li>
        <li>For <strong>bachelor\u2019s</strong>: hold a high-school diploma with transcript, and English at <strong>CEFR B1</strong> (IELTS/TOEFL/Duolingo/TOEIC equivalent).</li>
        <li>For <strong>master\u2019s</strong>: hold a bachelor\u2019s degree (16 years of education); for <strong>PhD</strong>: a master\u2019s degree \u2014 with English at <strong>CEFR B2</strong>.</li>
        <li><strong>English exemptions</strong> apply if you come from an English-speaking country or your previous degree was taught in English (proof required).</li>
        <li>Be in <strong>good physical and medical health</strong> and show a genuine interest in international cultural exchange.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee waiver</strong> for the normal duration of the degree.</li>
        <li><strong>Monthly living allowance:</strong> IDR 1,850,000 (bachelor\u2019s), IDR 2,350,000 (master\u2019s), IDR 2,600,000 (PhD).</li>
        <li><strong>Free dormitory accommodation</strong> for the first year (a monthly subsidy applies afterwards).</li>
        <li><strong>Minor health treatment</strong> support.</li>
        <li><strong>Free Indonesian language course (BIPA)</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Completed <strong>online application form</strong>.</li>
        <li><strong>Passport copy</strong> (valid).</li>
        <li><strong>High-school certificate / degree certificates and transcripts</strong>, translated into English or Indonesian.</li>
        <li><strong>Motivation letter</strong> and <strong>CV/resume</strong>.</li>
        <li><strong>English proficiency certificate</strong> (or waiver letter, if exempt).</li>
        <li><strong>Medical check-up report</strong> and a <strong>bank statement</strong> covering at least 3 months.</li>
        <li><strong>Two recommendation letters</strong> (master\u2019s and PhD) and a <strong>research proposal</strong> (master\u2019s/PhD).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick your batch</strong>Batch 2 (1 Oct\u201331 Dec 2026) is open now. If your documents are ready, apply early \u2014 don\u2019t wait for Batch 4 by default.</li>
        <li><strong>Prepare translations</strong>Get non-English/Indonesian documents officially translated, and line up your referees early.</li>
        <li><strong>Submit online</strong>Complete UMY\u2019s international admission form inside the batch window and upload every document in the correct format.</li>
        <li><strong>Follow the batch schedule</strong>Announcement, interview, document validation and visa stages follow each batch\u2019s own timetable.</li>
        <li><strong>Protect your GPA</strong>Remember the renewal thresholds \u2014 full support continues only above the GPA cut-offs stated above.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the UMY scholarship really fully funded?',
  'For the first year, yes in the meaningful sense: full tuition plus a monthly living allowance, free dormitory, minor health treatment and a free Indonesian course. From year two, the level of support depends on your GPA \u2014 fall below the thresholds and the discount shrinks or the award is revoked.'),
 ('Which batch should I apply in?',
  'The one whose window matches your readiness. Batch 2 runs 1 Oct\u201331 Dec 2026; Batch 3, 1 Jan\u201331 Mar 2027; Batch 4, 1 Apr\u201331 May 2027. If your English proof or research proposal needs work, a later batch beats a rushed file.'),
 ('Do I need IELTS?',
  'You need English at CEFR B1 (undergraduate) or B2 (postgraduate) via IELTS, TOEFL, Duolingo or TOEIC \u2014 unless you qualify for the exemption (English-speaking country or English-taught prior degree, with proof).'),
 ('What happens if my GPA drops?',
  'Undergraduates: GPA 2.75\u20132.99 drops you to a 75% tuition discount. Postgraduates: 3.25\u20133.49 \u2192 75%, 3.00\u20133.24 \u2192 50%. Below 2.75 at any level, the scholarship is revoked.'),
 ('Which programmes can I choose?',
  'All three levels across UMY\u2019s faculties \u2014 from Accounting, Law and International Relations to Engineering, Nursing and Islamic Studies at undergraduate level, and Management, Law, Civil Engineering and more at postgraduate level.'),
 ('Is there an application fee?',
  'The trackers describe the application process as free of a scholarship-specific fee; confirm any admission-portal charges on UMY\u2019s official site before submitting.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across five agreeing trackers: kabulscholarship.com (2027/2028 cycle: Batch 1, 15 Jul\u201330 Sep 2026; Batch 2, 1 Oct\u201331 Dec 2026; Batch 3, 1 Jan\u201331 Mar 2027; Batch 4, 1 Apr\u201331 May 2027; UG/PG/PhD; all nationalities), daadscholarship.com (same four batches; announcement/interview/validation/visa per batch), fully-fundedscholarships.com (same batches), scholarshipsads.com (same batches + documents: passport, transcripts, graduation certificate, English proof, recommendations, motivation/personal statement, research proposal, translations), scholarshiproar.com (same batches; benefits: full tuition + IDR 1,850,000/2,350,000/2,600,000 monthly + dormitory + minor health + BIPA), coursmooc.com (same batches; first-year dormitory free + IDR 750,000/month subsidy after; documents incl. bank statement + medical report). Benefits package corroborated by scholarshipunion.com, opportunitiespedia.com (GPA renewal thresholds), careerliftglobal.com and universityyat.com (CEFR B1/B2, exemptions). Queue title \u201c2025 (Fully Funded)\u201d was stale \u2014 the live cycle is 2027-28 and the article is written for it.</p>
''',
 dl_long='Deadline: Batch 2 closes 31 December 2026 (70 days from 22 Oct 2026). Batch 3: 1 Jan\u201331 Mar 2027. Batch 4: 1 Apr\u201331 May 2027. Batch 1 (15 Jul\u201330 Sep 2026) has closed.',
 offlinks=[('UMY International Student Scholarship 2027-28 \u2014 batches & guide (kabulscholarship)', 'https://kabulscholarship.com/opportunity/umy-international-student-scholarship/'),
           ('UMY Scholarships 2027-28 \u2014 detailed guide (daadscholarship)', 'https://daadscholarship.com/universitas-muhammadiyah-yogyakarta-international-scholarships-2027-to-study-for-free-in-indonesia/')],
 related_titles=['uiii', 'dcse-gts', 'um-bright'],
))

# ---------------------------------------------------------------- 4. Boustany Cambridge MBA
A.append(dict(
 slug='boustany-foundation-cambridge-mba-scholarship-2027-uk',
 title='Boustany Foundation Cambridge MBA Scholarship 2027 in UK (Funded)',
 meta='Boustany Foundation Cambridge MBA Scholarship 2027: 75% of Cambridge MBA tuition plus a funded two-month Monaco internship, awarded every two years to one exceptional candidate. Deadline 31 May 2027. Eligibility and how to apply.',
 short='Boustany Cambridge MBA Scholarship', kicker='UK \u00b7 MBA \u00b7 Funded', mono='BF',
 prov_short='Boustany Foundation', prov_cat='Foundation \u00b7 UK',
 h1='Boustany Foundation Cambridge MBA Scholarship 2027 in UK (Funded)',
 sub='75% of Cambridge MBA tuition covered, plus a two-month internship in Monaco with travel and accommodation paid \u2014 awarded to one exceptional candidate every two years.',
 dpill='Deadline 31 May 2027 \u00b7 221 days left',
 facts=facts([('Award', '75% of the Cambridge MBA tuition fees, plus travel and accommodation expenses for a compulsory two-month internship at the Boustany Foundation\u2019s office in Monaco (food also covered). One award, granted every two years. Scholars become members of Pembroke College.'),
              ('Eligible', 'Outstanding candidates of any nationality \u2014 priority is given to candidates of Lebanese descent \u2014 with an excellent academic background and considerable promise. You may apply only after receiving an offer of admission from the Cambridge MBA programme.'),
              ('How', 'Email your CV (with photograph), GMAT scores and your Cambridge MBA acceptance letter to admissions@boustany-foundation.org. Shortlisted candidates are interviewed by the Foundation; one scholar is chosen.'),
              ('Deadline', '31 May 2027 for submission of candidacy; the scholarship is awarded in June 2027, for the MBA class beginning in autumn 2027.'),
              ('Fine print', 'The Cambridge MBA itself runs five admission rounds (24 Aug 2026 to 4 May 2027) \u2014 secure your Judge Business School offer well before the 31 May scholarship deadline. The Monaco internship is unpaid, but all related travel, food and accommodation expenses are covered by the Foundation.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Boustany Foundation</strong> awards its <strong>Cambridge University MBA Scholarship</strong> once every two years to a single outstanding candidate admitted to the one-year MBA at <strong>Cambridge Judge Business School</strong>. The award covers <strong>75% of the MBA tuition fees</strong> and funds a <strong>two-month internship at the Foundation\u2019s office in Monaco</strong> over the summer \u2014 with travel, food and accommodation expenses paid.</p>
      <p>This is a genuine flagship award, confirmed on both the Foundation\u2019s official site and Cambridge Judge\u2019s own scholarships page: <strong>one award, deadline 31 May 2027, decided in June 2027</strong> for the class beginning in autumn 2027. Because it covers most \u2014 but not all \u2014 of the cost, it is marketed here as <strong>Funded</strong>, not fully funded.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold an <strong>offer of admission from the Cambridge MBA programme</strong> \u2014 you cannot apply for the scholarship before this.</li>
        <li>Show an <strong>excellent academic background</strong> and considerable promise: the Foundation looks for high intellectual potential, leadership, ambition and strong ethics.</li>
        <li>Be of <strong>any nationality</strong> \u2014 though priority is given to candidates of <strong>Lebanese descent</strong>.</li>
        <li>Be ready to complete the <strong>two-month Monaco internship</strong>; its exact dates are agreed case by case between you and the Foundation.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>75% of Cambridge MBA tuition fees</strong> covered.</li>
        <li><strong>Two-month internship in Monaco</strong> at the Boustany Foundation office \u2014 travel, food and accommodation expenses covered.</li>
        <li>Work on real Foundation projects: raising awareness, designing new scholarships, or initiatives that advance the Foundation\u2019s vision \u2014 the scope is shaped around your interests from day one.</li>
        <li><strong>Membership of Pembroke College</strong>, one of Cambridge\u2019s oldest colleges.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Curriculum vitae with a photograph</strong>.</li>
        <li><strong>GMAT scores</strong>.</li>
        <li><strong>Acceptance letter</strong> from the Cambridge MBA programme.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Win your Cambridge MBA offer first</strong>Apply to Cambridge Judge through one of the five MBA rounds (24 Aug 2026, 5 Oct 2026, 4 Jan 2027, 22 Mar 2027, 4 May 2027). Apply early \u2014 the scholarship deadline is fixed.</li>
        <li><strong>Email the Foundation</strong>Send your CV with photograph, GMAT scores and acceptance letter to <strong>admissions@boustany-foundation.org</strong> by <strong>31 May 2027</strong>.</li>
        <li><strong>Interview if shortlisted</strong>You may be invited to one or more interviews with the Foundation.</li>
        <li><strong>Await the June decision</strong>The single scholar is chosen and awarded during June 2027.</li>
        <li><strong>Plan the Monaco internship</strong>Agree the two-month summer window with the Foundation; your travel, food and accommodation are covered.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this scholarship fully funded?',
  'No \u2014 it covers 75% of tuition plus the funded Monaco internship (travel, food, accommodation). You remain responsible for the remaining 25% of tuition and your living costs in Cambridge, so it is honestly labelled Funded.'),
 ('Can I apply before I have the Cambridge MBA offer?',
  'No. The Foundation states clearly that candidates may apply only after receiving an offer of admission from the Cambridge MBA programme.'),
 ('Does my nationality matter?',
  'The scholarship is open to all nationalities, but priority is given to candidates of Lebanese descent.'),
 ('How often is it awarded?',
  'Once every two years, to a single candidate \u2014 which makes it one of the most competitive MBA awards in the UK.'),
 ('What does the Monaco internship involve?',
  'A two-month, unpaid internship at the Foundation\u2019s Monaco office working on awareness, new-scholarship design or other mission projects. It is unpaid, but the Foundation covers your travel, food and accommodation.'),
 ('Which college will I join?',
  'Scholars become members of Pembroke College.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 on the two official sources: boustany-foundation.org (Cambridge University MBA Scholarship page \u2014 deadline for candidacy 31 May 2027; awarded June 2027; 75% of tuition; two-month unpaid Monaco internship with travel, food and accommodation covered; CV with photograph + GMAT scores + acceptance letter to admissions@boustany-foundation.org; shortlisted candidates interviewed; one award every two years; all nationalities, priority to Lebanese descent; apply only after MBA offer) and jbs.cam.ac.uk (Boustany Foundation scholarship listing \u2014 external scholarship; value up to 75% of tuition + accommodation; 1 award; deadline 31 May 2027; Pembroke College membership). Corroborated by leverageedu.com (75%, biennial, separate application). Queue title \u201cCambridge University MBA Scholarship 2026 (Funded)\u201d was stale \u2014 retitled to the live 2027 Boustany round.</p>
''',
 dl_long='Deadline: 31 May 2027 (221 days from 22 Oct 2026). Awarded June 2027, for the MBA class beginning autumn 2027. Secure your Cambridge Judge offer first \u2014 MBA rounds run 24 Aug 2026 to 4 May 2027.',
 offlinks=[('Cambridge University MBA Scholarship \u2014 official (boustany-foundation.org)', 'https://boustany-foundation.org/scholarships/programs/cambridge-university-mba-scholarship/'),
           ('Boustany Foundation Scholarship \u2014 Cambridge Judge listing (jbs.cam.ac.uk)', 'https://www.jbs.cam.ac.uk/scholarships-loans/boustany-foundation-scholarship/')],
 related_titles=['imperial-mba-2027', 'clarendon', 'qmul'],
))

# ---------------------------------------------------------------- 5. Calgary
A.append(dict(
 slug='university-of-calgary-international-entrance-scholarship-2027-canada',
 title='University of Calgary International Entrance Scholarship 2027 in Canada (Funded)',
 meta='University of Calgary International Entrance Scholarship 2027: CAD 20,000, renewable for up to four years, for international undergraduates entering first year. Apply through the High School Prestige Awards by 1 Dec 2026.',
 short='UCalgary International Entrance Scholarship', kicker='Canada \u00b7 Undergraduate \u00b7 Funded', mono='UC',
 prov_short='University of Calgary', prov_cat='University \u00b7 Canada',
 h1='University of Calgary International Entrance Scholarship 2027 in Canada (Funded)',
 sub='CAD 20,000 for international students entering first year of any undergraduate degree \u2014 renewable for up to four years on a 2.60 GPA.',
 dpill='Prestige Awards close 1 Dec 2026 \u00b7 40 days left',
 facts=facts([('Award', 'CAD 20,000, renewable in the second, third and fourth year (up to CAD 80,000 across four years) provided you achieve a GPA of 2.60 or more over at least 24.00 units in the previous fall and winter terms and continue to pay international tuition fees. Only 2 awards are offered each year.'),
              ('Eligible', 'International undergraduate students \u2014 not Canadian citizens or permanent residents \u2014 entering first year of any undergraduate degree in the upcoming fall term, who have satisfied the university\u2019s English Language Proficiency requirement. Awarded on academic merit.'),
              ('How', 'A separate application is required: apply through the My UCalgary Portal under \u201cHigh School Prestige Awards\u201d. First submit your undergraduate admission application, then complete the Prestige Awards application inside the portal.'),
              ('Deadline', '1 December 2026 for the High School Prestige Awards application (for fall 2027 entry); admission documents must be submitted by 15 December 2026. Notifications go out in March/April.'),
              ('Fine print', 'Do not confuse this with the President\u2019s Admission Scholarship \u2014 a different, automatic award (CAD 5,000, non-renewable, 95%+ average, no application). The old registrar awards listing page no longer exists; the live award page is the authoritative source. Third-party trackers that quote CAD 15,000 one-time are outdated \u2014 the official figure is CAD 20,000 renewable.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Calgary International Entrance Scholarship</strong> is the university\u2019s flagship entrance award for international undergraduates: <strong>CAD 20,000</strong>, offered to just <strong>2 students each year</strong> entering first year of any undergraduate degree. It is <strong>renewable in years two, three and four</strong> \u2014 worth up to <strong>CAD 80,000 in total</strong> \u2014 as long as you keep a <strong>2.60 GPA over at least 24.00 units</strong> in the previous fall and winter terms and remain an international fee-paying student.</p>
      <p>Unlike many automatic entrance awards, this one needs a <strong>separate application</strong> through UCalgary\u2019s <strong>High School Prestige Awards</strong> competition \u2014 and that competition\u2019s deadline is <strong>1 December 2026</strong> for fall 2027 entry. With only two awards on offer, apply early and treat the Prestige Awards form as seriously as your admission application.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> \u2014 not a Canadian citizen or permanent resident \u2014 required to pay international tuition fees.</li>
        <li>Be entering <strong>first year of any undergraduate degree</strong> at the University of Calgary in the upcoming fall term (fall 2027).</li>
        <li>Have satisfied the university\u2019s <strong>English Language Proficiency</strong> requirement.</li>
        <li>Show strong <strong>academic merit</strong> \u2014 the official award page states merit as the criterion, with no fixed admission-average cutoff published.</li>
        <li>To renew: a <strong>GPA of 2.60+</strong> over at least <strong>24.00 units</strong> in the previous fall and winter terms, remaining enrolled and paying international fees.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CAD 20,000</strong> in the first year.</li>
        <li><strong>Renewable for years 2\u20134</strong> (up to CAD 80,000 total) on a 2.60 GPA over 24.00 units per year.</li>
        <li>Open to <strong>any undergraduate faculty</strong> \u2014 business, engineering, science, arts and more.</li>
        <li>Study at one of Canada\u2019s leading research universities in Calgary, Alberta.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Undergraduate admission application</strong> with official high-school transcripts and certificates.</li>
        <li><strong>Prestige Awards application</strong> completed in the My UCalgary Portal (essay/personal-statement responses on leadership and goals, as prompted).</li>
        <li><strong>English proficiency proof</strong> (IELTS/TOEFL or equivalent) if required for your admission stream.</li>
        <li>All <strong>admission documents</strong> uploaded by <strong>15 December 2026</strong> (check your Applicant Portal to-do list).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for undergraduate admission</strong>Submit your UCalgary undergraduate application and create your eID.</li>
        <li><strong>Wait 24\u201348 hours</strong>Your My UCalgary Portal (Student Centre) access activates after admission submission.</li>
        <li><strong>Open the Prestige Awards form</strong>Log in, go to \u201cMy Financials\u201d, and click \u201cApply for Undergraduate Awards\u201d \u2014 select the <strong>High School Prestige Awards</strong> application (enable browser pop-ups).</li>
        <li><strong>Submit by 1 December 2026</strong>Complete every section \u2014 the deadline is strict.</li>
        <li><strong>Upload documents by 15 December 2026</strong>Clear every item on your Applicant Portal to-do list.</li>
        <li><strong>Await March/April notification</strong>Award decisions are communicated in March/April.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the CAD 20,000 per year or one-time?',
  'It is CAD 20,000 for the first year and renewable in years two, three and four \u2014 up to CAD 80,000 total \u2014 provided you keep a 2.60 GPA over at least 24.00 units each year and remain an international fee-paying student.'),
 ('Do I need a separate application?',
  'Yes. Admission alone is not enough \u2014 you must complete the High School Prestige Awards application in the My UCalgary Portal by 1 December 2026.'),
 ('How many awards are available?',
  'Only 2 per year, which makes this one of UCalgary\u2019s most competitive international awards.'),
 ('Is there a fixed grade cutoff?',
  'The official award page states \u201cacademic merit\u201d without publishing a numeric admission average. Apply with the strongest grades you have.'),
 ('What is the difference from the President\u2019s Admission Scholarship?',
  'That is a separate, automatic award: CAD 5,000, non-renewable, based on a 95%+ final admission average, with no application. This International Entrance Scholarship is larger, renewable, competitive (2 awards), and needs the Prestige Awards application.'),
 ('When will I hear back?',
  'Notifications go out in March/April, after the December deadlines.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 on the official UCalgary award page (ucalgary.ca/registrar/awards/university-calgary-international-entrance-scholarship \u2014 CAD 20,000 renewable; 2 awards; separate application via My UCalgary Portal High School Prestige Awards; international first-year undergraduates, any faculty; ELP required; academic merit; renewal at 2.60 GPA over 24.00 units) and the official Awards calendar (Prestige Awards: applications open 1 Oct, close 1 Dec, documents by 15 Dec, notification March/April). The old registrar awards listing URL now 404s; the live award page was found via UCalgary site search. Corroborated by scholarshipsads.com and fundeddegree.com (CAD 20,000 renewable, March 2027 notification window). Queue title \u201cUniversity of Calgary Bachelors Scholarship 2025 (Funded)\u201d was stale \u2014 retitled to the live 2027 International Entrance Scholarship.</p>
''',
 dl_long='Deadline: 1 December 2026 (40 days from 22 Oct 2026) for the High School Prestige Awards application; admission documents by 15 December 2026. Notifications March/April 2027.',
 offlinks=[('University of Calgary International Entrance Scholarship \u2014 official award page', 'https://www.ucalgary.ca/registrar/awards/university-calgary-international-entrance-scholarship'),
           ('UCalgary Awards Calendar \u2014 Prestige Awards dates', 'https://www.ucalgary.ca/registrar/finances/awards/calendar')],
 related_titles=['trent-2027', 'udem-exempt', 'canada-noielts'],
))

import re as _re
def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)

if __name__ == '__main__':
    for a in A: _split_verify(a)
    built = []
    for a in A:
        n = build_article(BASE, OUT, a, CARDS)
        built.append((a['slug'], n))
    class P(html.parser.HTMLParser):
        def error(self, m): raise ValueError(m)
        def __init__(self):
            super().__init__(); self.errs = []
    bad = []
    for slug, _ in built:
        t = OUT.joinpath(slug + '.html').read_text()
        for token in ('AICTE Pragati', 'Lorem', '{{', 'data:image'):
            if token in t: bad.append((slug, 'template leftover / forbidden token: ' + token))
        for mm in re.finditer(r'href=["\']#["\']', t):
            bad.append((slug, 'suspicious placeholder: ' + mm.group(0)))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

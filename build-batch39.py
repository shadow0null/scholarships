#!/usr/bin/env python3
"""Batch 39 (cron run 39, 23 Oct 2026): 4 new verified articles + 1 bookkeeping done.

Queue scan (deadline order) examined entries until the batch was filled:
- WRITES: Copenhagen Danish Govt 2026-27, KAIST 2027 (dedicated queue title),
  Hasselt Master Mind 2027, Guangxi Normal CSC 2027.
- SINGA: the queue title 'Singapore International Graduate Award 2025...' was
  found to already have a published 2027 article
  (articles/singapore-international-graduate-award-singa-2027.html, written
  22 Oct, card 'singa2027' in registry) but was never marked done. Marked done
  here as bookkeeping; no duplicate written.
- Flinders RTP: REJECTED as a write. The 2026 international round closed
  18 Jun 2026 (official flinders.edu.au); the 2027 round is not announced.
  Marked skipped.
- 36 topics skipped with reasons (29 pre-compaction confirmations + Nairobi,
  Flinders, PSU, Lanzhou, World Bank, DREAM, CERN resolutions).
- Guangxi chosen over CERN for the 4th new write: CERN Summer Student 2027
  open-status is contradictory across sources (leapkite/careeraidhub say open
  vs freshscholarships: no active call on the official page) -> skipped.

HONESTY CALLS (23 Oct 2026, Asia/Kolkata):
- Copenhagen: queue said "2025-26 (Funded)". Live cycle is 2026-27: deadline
  15 Jan 2027 = the master's admission deadline for Sept 2027 starts; no
  separate scholarship application (automatic consideration). Full OR partial
  tuition waiver; some awards add a living-costs grant (taxable in Denmark).
- KAIST: queue had "Graduate Scholarships 2025" (stale) AND a dedicated
  "KAIST University Scholarship 2027" title. Written for Fall 2027 graduate
  admission (window 7 Jan - 5 Feb 2027, official admission.kaist.ac.kr); the
  2027 title is marked done, the 2025 title skipped as superseded. Benefits per
  the official KAIST Scholarship page: full tuition, national health insurance,
  monthly stipend (varies by college/research involvement); KGPS top tier
  1,000,000 KRW/month x 4 semesters; 94% of international students funded.
- Hasselt: queue said "2025 (Funded)". Live 2027 Master Mind: EUR 10,225/yr
  grant + tuition waiver (60 ECTS), admin fee only. Deadline 15 Mar 2027 is
  the annual-pattern expectation (2026 was 15 Mar 2026) - NOT yet published;
  the article flags confirmation on uhasselt.be. GPA 3.5/4.0, IELTS 7.0.
- Guangxi: queue said "2025-26 (Fully Funded)". Live 2027 CSC call: deadline
  31 Jan 2027, agency 10602 Type B, full tuition + accommodation + stipend
  (3,000 RMB master's / 3,500 RMB doctoral) + medical insurance, no fee.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'ucph-2027': {'mono': 'UCPH', 'title': 'University of Copenhagen Danish Government Scholarship 2026-27 in Denmark (Funded)',
   'href': 'university-of-copenhagen-danish-government-scholarship-2026-27.html',
   'dpill': 'Deadline 15 Jan 2027 \u00b7 84 days left',
   'award': 'Full or partial tuition fee waiver for the master\u2019s programme; some awards add a grant covering basic living costs. Funded by the Danish state.',
   'elig': 'Non-EU/EEA/Swiss citizens admitted to a full-time master\u2019s at UCPH and liable for tuition fees. Awarded on academic merit only.',
   'tags': [('Master\u2019s', 'blue'), ('Denmark', 'teal')]},
 'kaist-grad-2027': {'mono': 'KAIST', 'title': 'KAIST University Scholarship 2027 in South Korea (Fully Funded)',
   'href': 'kaist-university-scholarship-2027-south-korea.html',
   'dpill': 'Fall 2027: 7 Jan \u2013 5 Feb 2027 \u00b7 opens in 76 days',
   'award': 'Full tuition + national health insurance + monthly stipend (varies by college/research involvement); KGPS top tier 1,000,000 KRW/month. 94% of international students funded.',
   'elig': 'International applicants to KAIST graduate programmes (Master\u2019s, Master\u2019s-PhD Integrated, PhD); select \u201cKAIST Scholarship\u201d in the admission application.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('South Korea', 'teal')]},
 'hasselt-mm-2027': {'mono': 'UH', 'title': 'Hasselt University Master Mind Scholarship 2027 in Belgium (Funded)',
   'href': 'hasselt-university-master-mind-scholarship-2027-belgium.html',
   'dpill': 'Deadline 15 Mar 2027 \u00b7 143 days left (confirm on uhasselt.be)',
   'award': '\u20ac10,225 annual grant + full tuition fee waiver per academic year (60 ECTS); holders pay only an administrative enrolment fee.',
   'elig': 'GPA 3.5/4.0; IELTS 7.0 / TOEFL 94 / CAE C1; degree from outside Flanders; not enrolled at a Flemish HEI; nominated by Hasselt.',
   'tags': [('Master\u2019s', 'blue'), ('Belgium', 'teal')]},
 'gxnu-csc-2027': {'mono': 'GXNU', 'title': 'Guangxi Normal University CSC Scholarship 2027 in China (Fully Funded)',
   'href': 'guangxi-normal-university-csc-scholarship-2027-china.html',
   'dpill': 'Deadline 31 Jan 2027 \u00b7 100 days left',
   'award': 'Full tuition + accommodation + monthly stipend (3,000 RMB master\u2019s / 3,500 RMB doctoral) + comprehensive medical insurance. No application fee.',
   'elig': 'Non-Chinese citizens; bachelor\u2019s for master\u2019s, master\u2019s for PhD; under 35 (master\u2019s) / under 40 (PhD); HSK 4 or IELTS 5.5+.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('China', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Copenhagen
A.append(dict(
 slug='university-of-copenhagen-danish-government-scholarship-2026-27',
 title='University of Copenhagen Danish Government Scholarship 2026-27 in Denmark (Funded)',
 meta='University of Copenhagen Danish Government Scholarship 2026-27: full or partial tuition waivers for non-EU/EEA master\u2019s students, awarded on merit with automatic consideration. Deadline 15 January 2027, eligibility, benefits and how to apply.',
 short='UCPH Danish Government Scholarship', kicker='Denmark \u00b7 Master\u2019s \u00b7 Funded', mono='UCPH',
 prov_short='University of Copenhagen', prov_cat='University \u00b7 Denmark',
 h1='University of Copenhagen Danish Government Scholarship 2026-27 in Denmark (Funded)',
 sub='Denmark\u2019s oldest university waives tuition \u2014 in full or in part \u2014 for outstanding non-EU/EEA master\u2019s students. There is no separate application: your admission file is your scholarship application.',
 dpill='Deadline 15 Jan 2027 \u00b7 84 days left',
 facts=facts([('Award', 'Full or partial tuition fee waiver for the standard duration of the master\u2019s programme (typically two years), depending on the faculty\u2019s award. A limited number of awards also include a grant covering basic living costs. Funded by the Danish Ministry of Higher Education and Science.'),
              ('Eligible', 'Citizens of countries outside the EU, EEA and Switzerland who are admitted to a full-time master\u2019s (MA/MSc) programme at the University of Copenhagen and are liable for tuition fees. Awarded solely on academic excellence \u2014 financial need is not considered.'),
              ('How', 'Apply for admission to a UCPH master\u2019s programme starting September 2027 by 15 January 2027 through the university\u2019s official admissions portal. Every eligible non-EU/EEA applicant is automatically considered \u2014 no scholarship form exists.'),
              ('Deadline', '15 January 2027 for most master\u2019s programmes starting September 2027. A few programmes set different deadlines, so check your programme\u2019s page.'),
              ('Fine print', 'The number of awards is limited and varies by faculty. A partial waiver leaves you to fund the remainder yourself. Living-cost grants are subject to Danish tax legislation. UCPH contacts nominees by email \u2014 you must accept or decline by the stated deadline or the offer passes to another applicant.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Copenhagen (UCPH)</strong> \u2014 founded in 1479, Denmark\u2019s oldest and largest university, with 119 master\u2019s programmes across six faculties \u2014 offers the <strong>Danish Government Scholarship</strong> to a limited number of exceptionally talented students from outside the EU/EEA and Switzerland. Funded by the <strong>Danish Ministry of Higher Education and Science</strong>, the scheme exists to attract outstanding international talent into Danish research universities.</p>
      <p>The defining feature of this award is its simplicity: <strong>there is no separate scholarship application</strong>. Every eligible non-EU/EEA applicant to a UCPH master\u2019s programme is automatically evaluated for the scholarship as part of the admission process, and awards are made <strong>purely on academic merit</strong>. Depending on the faculty, the scholarship is granted as a <strong>full or partial tuition fee waiver</strong>, and in some cases as <strong>an amount covering basic living costs</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of a country outside the EU, EEA and Switzerland</strong>.</li>
        <li>Be <strong>admitted to a full-time master\u2019s degree programme</strong> at the University of Copenhagen.</li>
        <li>Be <strong>liable for tuition fees</strong> \u2014 students with a legal claim to Danish citizens\u2019 rights, or who are eligible for the Danish State Educational Grant (SU), are excluded.</li>
        <li>Hold (or be able to obtain) a <strong>time-limited Danish residence permit</strong> for the purpose of study.</li>
        <li>Show an <strong>outstanding academic record</strong> \u2014 selection is competitive and based on excellence alone.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full or partial tuition fee waiver</strong> for the standard duration of the master\u2019s programme (typically two years), depending on the faculty\u2019s award.</li>
        <li>Selected recipients also receive <strong>a grant covering basic living costs</strong> \u2014 note these grants are subject to Danish tax legislation.</li>
        <li><strong>Automatic consideration</strong> \u2014 no separate form, no extra fee, no additional documents beyond your admission file.</li>
        <li>Study at one of Europe\u2019s leading research universities, a member of the League of European Research Universities (LERU).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Your <strong>master\u2019s admission application</strong> \u2014 the scholarship requires nothing beyond this file.</li>
        <li><strong>Bachelor\u2019s degree certificate</strong> (or proof of expected graduation) and <strong>official academic transcripts</strong>.</li>
        <li><strong>Proof of English language proficiency</strong> (e.g. IELTS/TOEFL, where the programme requires it).</li>
        <li><strong>CV</strong> and a <strong>motivation letter</strong> where the programme asks for them.</li>
        <li><strong>Passport copy</strong> and any programme-specific supporting documents \u2014 requirements vary, so check your programme\u2019s admission page.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your programme</strong>Browse UCPH\u2019s 119 master\u2019s programmes and select one starting in <strong>September 2027</strong> that matches your academic background.</li>
        <li><strong>Apply for admission by 15 January 2027</strong>Submit your application through the university\u2019s official admissions portal (studies.ku.dk) before the deadline.</li>
        <li><strong>Upload the complete document file</strong>Degree certificate, transcripts, English proof, CV, motivation letter and passport \u2014 everything the programme requires.</li>
        <li><strong>Do nothing extra for the scholarship</strong>Every eligible non-EU/EEA applicant is automatically evaluated; no scholarship form exists.</li>
        <li><strong>Watch your email</strong>UCPH contacts nominees directly at the address in their admission application \u2014 check your spam folder too. You must <strong>accept or decline by the deadline in the email</strong>, or the offer is revoked and passed to another applicant.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate scholarship application?',
  'No. All eligible non-EU/EEA applicants to UCPH master\u2019s programmes are automatically considered for the Danish Government Scholarship as part of the admission process.'),
 ('I am an EU citizen. Can I apply?',
  'No \u2014 EU/EEA and Swiss citizens do not pay tuition fees in Denmark, so the scholarship does not apply to them.'),
 ('Is it fully funded?',
  'It can be. Awards are granted as a full tuition waiver, a partial tuition waiver, or an amount covering basic living costs, depending on the faculty. Check your award letter for exactly what your scholarship covers.'),
 ('When will I know if I got it?',
  'UCPH contacts scholarship nominees directly by email after admission decisions. Because you must accept or decline by a stated deadline, check your inbox \u2014 and spam folder \u2014 regularly.'),
 ('Can I combine it with another scholarship?',
  'The published terms do not promise combinability. Check your award letter and ask the university before accepting a second award.'),
 ('Which programmes are covered?',
  'Full-time master\u2019s (MA/MSc) programmes starting September 2027. Most share the 15 January 2027 deadline, but a few programmes differ \u2014 confirm on your programme\u2019s page.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: aktravelsltd.com (9 Jul 2026) \u2014 15 Jan 2027 deadline for most September-2027 master\u2019s programmes, no separate application, full/partial tuition waiver or living stipend, merit only, funded by the Danish Ministry of Higher Education and Science; scholarshiptab.com \u2014 automatic consideration via the official admissions portal (studies.ku.dk), email nomination with an accept/decline deadline, eligibility exclusions (SU eligibility, Danish-citizen rights); educatewithguide.com (8 Aug 2026) \u2014 full/partial waiver and/or living-costs grant depending on faculty, living grants subject to Danish tax, UCPH founded 1479 with 119 master\u2019s programmes. Queue title \u201cUniversity of Copenhagen Danish Government Scholarships 2025-26 (Funded)\u201d was stale \u2014 retitled to the live 2026-27 cycle.</p>
''',
 dl_long='Deadline: 15 January 2027 for most master\u2019s programmes starting September 2027. There is no separate scholarship application \u2014 every eligible non-EU/EEA applicant is automatically considered with their admission file.',
 offlinks=[('Danish Government Scholarship at UCPH \u2014 trackers summary (scholarshiptab.com)', 'https://www.scholarshiptab.com/scholarships/danish-government-international-awards-at-the-university-of-copenhagen-denmark-for-master&via=ScholarshipTab&via=ScholarshipTab'),
           ('UCPH Danish Government Scholarships 2027 \u2014 deadline & terms (aktravelsltd.com)', 'https://aktravelsltd.com/2026/07/09/university-of-copenhagen-danish-government-scholarships-2027/')],
 related_titles=['fulbright-dk', 'stockholm-2027', 'radboud-2027'],
))

# ---------------------------------------------------------------- 2. KAIST
A.append(dict(
 slug='kaist-university-scholarship-2027-south-korea',
 title='KAIST University Scholarship 2027 in South Korea (Fully Funded)',
 meta='KAIST University Scholarship 2027: full tuition, monthly stipend and health insurance for international Master\u2019s and PhD students, awarded automatically with admission. Fall 2027 window: 7 Jan \u2013 5 Feb 2027. Eligibility, benefits and how to apply.',
 short='KAIST University Scholarship', kicker='South Korea \u00b7 Master\u2019s & PhD \u00b7 Fully Funded', mono='KAIST',
 prov_short='KAIST', prov_cat='University \u00b7 South Korea',
 h1='KAIST University Scholarship 2027 in South Korea (Fully Funded)',
 sub='Korea\u2019s top science university funds 94% of its international students \u2014 full tuition, a monthly stipend and health insurance \u2014 with no separate scholarship form to fill in.',
 dpill='Fall 2027: 7 Jan \u2013 5 Feb 2027 \u00b7 opens in 76 days',
 facts=facts([('Award', 'Full tuition coverage, national health insurance, and a monthly stipend (the amount depends on research involvement and varies by college). The university states that 94% of international students benefit. The strongest candidates are automatically elevated to higher tiers such as the KAIST Global Presidential Scholarship (KGPS): full tuition plus 1,000,000 KRW per month for four regular semesters.'),
              ('Eligible', 'International applicants to KAIST graduate programmes \u2014 Master\u2019s, Master\u2019s-PhD Integrated, or PhD \u2014 across all departments except the Global Technology Innovation Program (GDI-GTIP track). You must select \u201cKAIST Scholarship\u201d as your financial resource inside the admission application.'),
              ('How', 'Apply online for Fall 2027 graduate admission at admission.kaist.ac.kr between 7 January and 5 February 2027, tick the KAIST Scholarship option in the financial-resources section, and upload the full document file. There is no separate scholarship application \u2014 admission and funding decisions arrive together.'),
              ('Deadline', '5 February 2027 (Fall 2027 graduate admission window: 7 January \u2013 5 February 2027, per the official admissions site).'),
              ('Fine print', 'The stipend amount is not a single published figure \u2014 it varies by college and research involvement, so confirm the figure for your department. KGPS/KPS tiers are awarded automatically to eligible candidates; you cannot apply for them directly.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>KAIST</strong> \u2014 the Korea Advanced Institute of Science and Technology in Daejeon, founded in 1971 and widely regarded as South Korea\u2019s premier research university for science and technology \u2014 funds its international graduate students through its <strong>own institutional scholarship</strong>, not a government scheme. The KAIST Scholarship is not a separate competition: it is a funding option you select inside your graduate admission application.</p>
      <p>The university\u2019s own admissions site describes the programme as simple yet generous: <strong>full tuition fees, national health insurance, and a monthly stipend</strong>, benefiting <strong>94% of the international student body</strong>. Research involvement often tops the support up further, letting most students reach financial self-sufficiency. Candidates admitted to Master\u2019s or Master\u2019s-PhD Integrated programmes are additionally considered \u2014 automatically \u2014 for the prestigious <strong>KAIST Global Presidential Scholarship (KGPS)</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international applicant</strong> to a KAIST graduate programme \u2014 <strong>Master\u2019s, Master\u2019s-PhD Integrated, or PhD</strong>.</li>
        <li>Apply to any department <strong>except the Global Technology Innovation Program (GDI-GTIP track)</strong>.</li>
        <li>Select <strong>\u201cKAIST Scholarship\u201d as your financial resource</strong> in the admission application \u2014 this is what triggers funding consideration.</li>
        <li>Meet KAIST\u2019s graduate <strong>admission requirements</strong>, including the academic background and English proficiency for your programme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition coverage</strong> for the standard duration of the programme.</li>
        <li><strong>National health insurance</strong> throughout your studies.</li>
        <li><strong>Monthly stipend</strong> \u2014 the amount depends on research involvement and varies by college, so confirm the figure for your department.</li>
        <li><strong>KGPS top tier</strong> (Master\u2019s / Integrated programmes): full tuition plus <strong>1,000,000 KRW per month for four regular semesters</strong>.</li>
        <li><strong>No separate scholarship application</strong> and no extra fee \u2014 funding follows admission automatically.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Completed <strong>online graduate admission application</strong> (with \u201cKAIST Scholarship\u201d selected as the financial resource).</li>
        <li><strong>Academic transcripts</strong> and <strong>degree certificates</strong>.</li>
        <li><strong>Proof of English proficiency</strong> (e.g. TOEFL/IELTS).</li>
        <li><strong>Statement of purpose / study plan</strong>.</li>
        <li><strong>Recommendation letters</strong> and a <strong>passport copy</strong>.</li>
        <li>These are the typical graduate-admission documents \u2014 always confirm against the <strong>official checklist</strong> for your programme and intake.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Note the Fall 2027 window</strong>Graduate applications for Fall 2027 run from <strong>7 January to 5 February 2027</strong>, per the official admissions site.</li>
        <li><strong>Start the online application</strong>Apply at <strong>admission.kaist.ac.kr</strong> and choose your department and degree programme.</li>
        <li><strong>Tick \u201cKAIST Scholarship\u201d</strong>In the financial-resources section, select the KAIST Scholarship option \u2014 this single tick is the entire scholarship application.</li>
        <li><strong>Upload the full file before 5 February 2027</strong>Transcripts, certificates, English scores, statement of purpose and recommendations.</li>
        <li><strong>Await the joint decision</strong>Admission and scholarship outcomes arrive together; admitted students who selected the option are funded automatically, with the strongest considered for KGPS/KPS tiers.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate scholarship application form?',
  'No. You select \u201cKAIST Scholarship\u201d as your financial resource inside the graduate admission application. That selection is the whole application \u2014 there is nothing else to fill in.'),
 ('Does this cover undergraduate degrees?',
  'No. This is the graduate scholarship (Master\u2019s, Integrated Master\u2019s-PhD, PhD). The undergraduate KAIST Scholarship is a separate scheme on a different calendar.'),
 ('How much is the monthly stipend?',
  'It varies by college and by your research involvement \u2014 the university does not publish a single figure. The published top tier (KGPS) is 1,000,000 KRW per month for four semesters.'),
 ('What does \u201c94% of international students\u201d mean?',
  'It is the university\u2019s own figure for the share of international students receiving scholarship support. Admission itself remains competitive.'),
 ('How is this different from the Global Korea Scholarship (GKS)?',
  'The KAIST Scholarship is institutional and automatic with admission. GKS is a Korean government award run via NIIED and Korean embassies \u2014 a separate application with its own timeline.'),
 ('Which departments are covered?',
  'All departments except the Global Technology Innovation Program (GDI-GTIP track).'),
]) + '''
      <p class="verify">Verified 23 Oct 2026 on the official admissions site admission.kaist.ac.kr (KAIST Scholarship page: full tuition, national health insurance, monthly stipend varying by research involvement/college, 94% of international students funded, automatic KGPS/KPS consideration for eligible candidates, all departments except GDI-GTIP, select the KAIST Scholarship option in the admission application; KGPS: full tuition + 1,000,000 KRW/month for 4 regular semesters) and the official graduate admissions schedule (Fall 2027 window 7 January \u2013 5 February 2027). Corroborated by leapscholar.com and scholarshipshive.com on the automatic-award mechanism. Queue title \u201cKAIST University Graduate Scholarships 2025 in South Korea (Fully Funded)\u201d was stale \u2014 the article is written for the live 2027 graduate cycle and the dedicated queue title \u201cKAIST University Scholarship 2027 in South Korea (Fully Funded)\u201d is marked done.</p>
''',
 dl_long='Deadline: 5 February 2027 (Fall 2027 graduate admission window: 7 January \u2013 5 February 2027, per the official admissions site). Select \u201cKAIST Scholarship\u201d as your funding source inside the admission application \u2014 there is no separate scholarship deadline.',
 offlinks=[('KAIST Scholarship \u2014 official admissions page (admission.kaist.ac.kr)', 'https://admission.kaist.ac.kr/intl-graduate/FinancialSupport/Scholarship/KAISTScholarship')],
 related_titles=['kaist-ug', 'gks2027', 'saitama-mext-2027'],
))

# ---------------------------------------------------------------- 3. Hasselt
A.append(dict(
 slug='hasselt-university-master-mind-scholarship-2027-belgium',
 title='Hasselt University Master Mind Scholarship 2027 in Belgium (Funded)',
 meta='Hasselt University Master Mind Scholarship 2027: \u20ac10,225 annual grant plus full tuition waiver for outstanding international master\u2019s students. Deadline 15 March 2027, GPA 3.5/4.0, IELTS 7.0. Eligibility and how to apply.',
 short='Hasselt Master Mind Scholarship', kicker='Belgium \u00b7 Master\u2019s \u00b7 Funded', mono='UH',
 prov_short='Hasselt University', prov_cat='University \u00b7 Belgium',
 h1='Hasselt University Master Mind Scholarship 2027 in Belgium (Funded)',
 sub='Flanders pays its best international master\u2019s students \u20ac10,225 a year and waives their tuition. At Hasselt the 2027 deadline is expected on 15 March \u2014 confirm it on uhasselt.be.',
 dpill='Deadline 15 Mar 2027 \u00b7 143 days left (confirm on uhasselt.be)',
 facts=facts([('Award', '\u20ac10,225 grant per academic year plus a full tuition fee waiver per academic year (60 ECTS). Recipients pay only a small administrative enrolment fee. The grant is paid in instalments and covers accommodation, insurance and a significant share of living expenses. Funded by the Flemish Ministry of Education and Training.'),
              ('Eligible', 'GPA of 3.5 out of 4.0 on the last obtained degree; English at IELTS 7.0 overall / TOEFL 94 / CAE C1 (online tests accepted); previous degree from a higher education institution outside Flanders; not currently enrolled at a Flemish HEI. All nationalities except Russian nationals.'),
              ('How', 'Apply for an eligible master\u2019s programme at Hasselt University \u2014 the university nominates its strongest candidates to the Flemish Master Mind programme. You cannot apply to the Flemish government directly.'),
              ('Deadline', '15 March 2027 (expected). Hasselt\u2019s Master Mind deadline for the 2026 intake was 15 March 2026; the 2027 date follows the annual pattern but is NOT yet published \u2014 verify on uhasselt.be before you apply.'),
              ('Fine print', 'Hasselt\u2019s allocation is small and competition is intense. The scholarship cannot be combined with another Flemish government scholarship or an Erasmus Mundus scholarship. One-year (60 ECTS) and two-year (120 ECTS) master\u2019s programmes are covered.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Master Mind Scholarship</strong> is the Flemish Government\u2019s flagship award for international master\u2019s students, funded by the <strong>Flemish Ministry of Education and Training</strong> and administered through participating universities in Flanders and Brussels. At <strong>Hasselt University</strong>, it targets academically outstanding students from outside Flanders: a grant of <strong>\u20ac10,225 per academic year</strong> plus a <strong>full tuition fee waiver</strong> \u2014 recipients pay only a small administrative enrolment fee.</p>
      <p>Master Mind is strictly <strong>merit-based</strong> and nomination-driven. Students cannot apply to the Flemish authorities directly; each participating institution \u2014 Hasselt included \u2014 selects and nominates its own candidates from its master\u2019s applicant pool.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>GPA of 3.5 out of 4.0</strong> on the last obtained degree \u2014 a high standard of academic performance is required.</li>
        <li>Sufficient English: <strong>IELTS 7.0 overall, TOEFL 94, or CAE C1</strong> (or a similar result in another official test; online IELTS/TOEFL accepted).</li>
        <li><strong>Not currently enrolled</strong> at a Flemish higher education institution \u2014 the exception is international students in a preparatory programme leading to a master\u2019s starting in September.</li>
        <li>Previous degree obtained from a <strong>higher education institution outside Flanders</strong>.</li>
        <li><strong>All nationalities except Russian nationals</strong> may apply.</li>
        <li>Students enrolling only for a preparatory, bridging or distance-learning programme are <strong>not eligible</strong>.</li>
        <li>Cannot be combined with <strong>another Flemish government scholarship or an Erasmus Mundus scholarship</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac10,225 grant per academic year</strong>, paid in instalments \u2014 covers accommodation, insurance and a significant share of living expenses.</li>
        <li><strong>Full tuition fee waiver</strong> per academic year (60 ECTS); you pay only the administrative enrolment fee.</li>
        <li>Available for <strong>one-year (60 ECTS) and two-year (120 ECTS)</strong> master\u2019s programmes.</li>
        <li>Study at Hasselt University, with access to Flanders\u2019 academic networks and research environment.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Your <strong>Hasselt master\u2019s admission application</strong> \u2014 the nomination is handled internally by the university from its applicant pool.</li>
        <li><strong>Degree certificate</strong> and <strong>academic transcripts</strong> (showing the 3.5/4.0 GPA).</li>
        <li><strong>English test score</strong> (IELTS/TOEFL/CAE).</li>
        <li><strong>Passport copy</strong>, <strong>motivation letter</strong> and <strong>CV</strong>, plus any programme-specific requirements.</li>
        <li>Confirm the internal nomination procedure and document list with <strong>Hasselt\u2019s international office</strong>, since each institution runs its own process.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for a Hasselt master\u2019s</strong>Submit your application for an eligible master\u2019s programme at Hasselt University.</li>
        <li><strong>Follow the internal nomination procedure</strong>Each institution sets its own internal deadline and process \u2014 for the 2026 intake Hasselt\u2019s was <strong>15 March 2026</strong>. Check the international office\u2019s instructions for 2027.</li>
        <li><strong>Get nominated</strong>The university selects its strongest candidates and nominates them to the Flemish Master Mind programme. There is no direct application to the Flemish government.</li>
        <li><strong>Await the Flemish selection</strong>The final decision comes from the programme; if selected, the grant and tuition waiver apply from the start of your master\u2019s.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I apply for the Master Mind Scholarship directly?',
  'No. Students cannot apply independently \u2014 the host institution nominates its candidates. Your route in is a strong master\u2019s application at Hasselt.'),
 ('Why does the article say 15 March 2027 if it is not confirmed?',
  'Because Hasselt\u2019s Master Mind deadline was 15 March 2026 and the scheme runs on an annual cycle. The 2027 date is the honest expectation, not a published fact \u2014 the article tells you to verify it on uhasselt.be before relying on it.'),
 ('How many Master Mind awards does Hasselt get?',
  'Very few \u2014 Mastersportal\u2019s 2027 listing for Hasselt shows a single award, so treat this as one of Belgium\u2019s most competitive master\u2019s scholarships.'),
 ('Can I combine it with an Erasmus Mundus scholarship?',
  'No. The programme rules forbid combining Master Mind with another Flemish government scholarship or an Erasmus Mundus scholarship.'),
 ('I already study in Flanders. Am I eligible?',
  'No \u2014 unless you are an international student in a preparatory programme leading to a master\u2019s starting in September.'),
 ('How is the \u20ac10,225 paid?',
  'In instalments across the academic year, intended to cover accommodation, insurance and a significant part of your living expenses.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: mastersportal.com 2027 listing (\u20ac10,225 grant + tuition waiver per academic year/60 ECTS; administrative enrolment fee only; paid in instalments; GPA 3.5/4.0; IELTS 7.0 / TOEFL 94 / CAE C1; not enrolled at a Flemish HEI; previous degree from outside Flanders; all nationalities except Russian; cannot combine with Flemish government or Erasmus Mundus awards); daadscholarship.com (Hasselt\u2019s 2026 Master Mind deadline was 15 March 2026 \u2014 the 15 Mar 2027 date is the annual-pattern expectation and is NOT yet published); careerliftglobal.com (\u20ac10,225/yr + waiver; nomination by the host institution; students cannot apply independently). The article flags the 2027 deadline for confirmation on uhasselt.be. Queue title \u201cHasselt University Master Mind Scholarships 2025 in Belgium (Funded)\u201d was stale \u2014 retitled to the 2027 cycle.</p>
''',
 dl_long='Deadline: 15 March 2027 (Hasselt\u2019s Master Mind deadline for the 2026 intake was 15 March 2026; the 2027 date follows the annual pattern but is not yet published \u2014 verify on uhasselt.be before you apply).',
 offlinks=[('Mastermind Scholarship 2027 \u2014 Hasselt University listing (mastersportal.com)', 'https://www.mastersportal.com/scholarships/3582/mastermind-scholarship.html')],
 related_titles=['radboud-2027', 'maastricht', 'leiden-mandela'],
))

# ---------------------------------------------------------------- 4. Guangxi
A.append(dict(
 slug='guangxi-normal-university-csc-scholarship-2027-china',
 title='Guangxi Normal University CSC Scholarship 2027 in China (Fully Funded)',
 meta='Guangxi Normal University CSC Scholarship 2027: full tuition, accommodation, 3,000\u20133,500 RMB monthly stipend and medical insurance for Master\u2019s and PhD. Deadline 31 Jan 2027, agency number 10602 (Type B). Eligibility, documents and how to apply.',
 short='GXNU CSC Scholarship', kicker='China \u00b7 Master\u2019s & PhD \u00b7 Fully Funded', mono='GXNU',
 prov_short='Guangxi Normal University', prov_cat='University \u00b7 China',
 h1='Guangxi Normal University CSC Scholarship 2027 in China (Fully Funded)',
 sub='Guilin\u2019s teacher-training powerhouse offers the Chinese Government Scholarship for 2027: tuition, a dormitory bed, a monthly stipend and insurance \u2014 with no application fee and no hard copies.',
 dpill='Deadline 31 Jan 2027 \u00b7 100 days left',
 facts=facts([('Award', 'Full tuition fee, on-campus accommodation, monthly stipend (3,000 RMB for master\u2019s students, 3,500 RMB for doctoral students) and comprehensive medical insurance. This is the Chinese Government Scholarship (CSC) Type B channel through the university \u2014 agency number 10602.'),
              ('Eligible', 'Non-Chinese citizens in good health: a bachelor\u2019s degree for master\u2019s programmes, a master\u2019s degree for doctoral programmes. Under 35 for postgraduate applicants, under 40 for doctoral applicants. Language: HSK 4 (score 210+) for Chinese-taught programmes; IELTS 5.5+ or TOEFL 80+ for English-taught programmes.'),
              ('How', 'Complete the CSC online application (Program Category Type B, agency number 10602 for GXNU) AND the GXNU online application, uploading all documents. No application fee; no hard copies. Submit by 31 January 2027 \u2014 early applications are encouraged.'),
              ('Deadline', '31 January 2027. The university reviews files and issues pre-admission notices to recommended candidates before forwarding them to the China Scholarship Council.'),
              ('Fine print', 'An acceptance letter from a GXNU supervisor is optional but strengthens the file. The 2027 call described here covers master\u2019s and doctoral study \u2014 bachelor\u2019s applicants should confirm availability with the admission office.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Guangxi Normal University (GXNU)</strong> in Guilin, China \u2014 a comprehensive university with a long teacher-training tradition and a major role in education and research in southern China \u2014 participates in the <strong>Chinese Government Scholarship (CSC)</strong> scheme. For 2027, international students can apply for full CSC funding for <strong>master\u2019s and doctoral</strong> study through the university\u2019s <strong>Type B</strong> channel (agency number <strong>10602</strong>): tuition, accommodation, a monthly stipend and medical insurance.</p>
      <p>The process is entirely online and refreshingly simple: <strong>no application fee, no hard copies</strong>. You file on the CSC system, file on the university portal, and GXNU\u2019s departments review your documents before the university forwards recommended candidates to the China Scholarship Council.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Chinese citizen</strong> in good health.</li>
        <li>Hold a <strong>bachelor\u2019s degree</strong> for master\u2019s programmes, or a <strong>master\u2019s degree</strong> for doctoral programmes.</li>
        <li>Be <strong>under 35</strong> for postgraduate (master\u2019s) applicants, <strong>under 40</strong> for doctoral applicants.</li>
        <li>Meet the language requirement: <strong>HSK 4 (score 210+, valid two years)</strong> for Chinese-taught programmes; <strong>IELTS 5.5+ or TOEFL 80+</strong> for English-taught programmes \u2014 confirm the exact threshold for your programme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee</strong> for the duration of the programme.</li>
        <li><strong>On-campus accommodation</strong> provided.</li>
        <li><strong>Monthly stipend: 3,000 RMB</strong> for master\u2019s students, <strong>3,500 RMB</strong> for doctoral students.</li>
        <li><strong>Comprehensive medical insurance</strong> for the entire study period.</li>
        <li><strong>No application fee</strong> and <strong>no hard-copy documents</strong> \u2014 the whole process is online.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CSC online application form</strong> \u2014 Program Category <strong>Type B</strong>, agency number <strong>10602</strong>.</li>
        <li><strong>GXNU online application form</strong> with all documents uploaded.</li>
        <li><strong>Notarized highest degree certificate</strong> (or proof of expected graduation; the original is checked at registration).</li>
        <li><strong>Notarized academic transcripts</strong>.</li>
        <li><strong>Study plan or research proposal</strong>.</li>
        <li><strong>Two recommendation letters</strong> from professors or associate professors.</li>
        <li><strong>Passport copy</strong> (photo page) and a <strong>passport-size photo</strong>.</li>
        <li><strong>Foreigner Physical Examination Form</strong> (completed and valid).</li>
        <li><strong>No-criminal-record certificate</strong> (police clearance).</li>
        <li><strong>Language proficiency certificate</strong>.</li>
        <li><strong>Acceptance letter</strong> from a GXNU supervisor \u2014 optional, but it significantly improves your chances.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>File on the CSC system</strong>Register on the Chinese Government Scholarship Information System, choose <strong>Program Category Type B</strong>, and enter agency number <strong>10602</strong> for Guangxi Normal University.</li>
        <li><strong>File on the GXNU portal</strong>Complete the university\u2019s online application and upload every document. Double-check names, dates and scans.</li>
        <li><strong>Email a copy of the set</strong>Guides advise sending your documents to <strong>admission@gxnu.edu.cn</strong> \u2014 confirm the current instruction on the university\u2019s notice page before you send.</li>
        <li><strong>GXNU review</strong>The relevant department reviews your file; recommended candidates receive a <strong>pre-admission notice</strong> and their files go to the CSC.</li>
        <li><strong>Submit by 31 January 2027</strong>Early submission is strongly encouraged so the review is not rushed.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is an acceptance letter required?',
  'No \u2014 it is optional. But it is not a throwaway line: the university\u2019s own guidance says an acceptance letter significantly improves your chances, so contacting a supervisor early is worth it.'),
 ('Is there an application fee?',
  'No. There is no application fee for the GXNU CSC route.'),
 ('Do I need to mail hard copies?',
  'No. The application is fully online \u2014 just submit through the CSC system and the GXNU portal.'),
 ('Can bachelor\u2019s students apply?',
  'The 2027 CSC call at GXNU described here covers master\u2019s and doctoral study. Bachelor\u2019s applicants should confirm availability directly with the admission office.'),
 ('What does \u201cType B\u201d mean?',
  'It is the CSC program category for applications submitted directly through the university itself (agency number 10602), as opposed to embassy or dispatching-authority routes.'),
 ('Is IELTS mandatory?',
  'A language proficiency certificate is required, but IELTS specifically is not mandatory \u2014 the university accepts equivalent proof. For English-taught programmes the published bar is IELTS 5.5+ or TOEFL 80+.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: opforall.com (published 2 Sep 2026) \u2014 2027 call, deadline 31 Jan 2027, agency number 10602 Type B, full tuition + accommodation + monthly stipend (3,000 RMB master\u2019s / 3,500 RMB doctoral) + comprehensive medical insurance, age limits 35/40, HSK 4 (210+) for Chinese-taught and IELTS 5.5+/TOEFL 80+ for English-taught programmes, full document list, admission@gxnu.edu.cn; chinesescholarshipcouncil.com \u2014 eligibility, two-step online application, no application fee, no hard copies. Queue title \u201cGuangxi Normal University CSC Scholarship 2025-26 in China (Fully Funded)\u201d was stale \u2014 retitled to the live 2027 cycle.</p>
''',
 dl_long='Deadline: 31 January 2027 (agency number 10602, Program Category Type B). Apply early \u2014 the university reviews files before forwarding them to the China Scholarship Council.',
 offlinks=[('GXNU CSC Scholarship 2027 \u2014 call details & documents (opforall.com)', 'https://opforall.com/guangxi-normal-university-chinese-government-scholarship/'),
           ('Guangxi Normal University CSC Scholarship \u2014 eligibility & steps (chinesescholarshipcouncil.com)', 'https://www.chinesescholarshipcouncil.com/guangxi-normal-university.html')],
 related_titles=['xiamen-csc-2027', 'hust-csc-2027', 'nju-csc-2027'],
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

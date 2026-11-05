#!/usr/bin/env python3
"""Batch 37 (manual recovery run, 22 Oct 2026): 5 verified articles.

The 14:52 IST cron run (batch 37) stalled with no blocker named; this run
executes the same pipeline manually so the corpus does not lose a batch.

Topics (queue order): Chang Gung (#2), Wageningen (#7), NIAS Safe Haven (#22),
WA Premier's (#26), Stockholm Scheme (#28).

HONESTY CALLS (22 Oct 2026, Asia/Kolkata):
- Chang Gung: queue title said 2026; the live cycle is Fall 2027 admission.
  Round 1 (25 Sep-17 Nov 2026) is OPEN NOW per the official cgu.edu.tw
  2027-28 guidelines page. Scholarship package (tuition waiver + TWD 8,000/mo
  MSc / TWD 12,000 + NT$29,000/mo PhD + advisor assistantships) from three
  agreeing trackers; official page confirms rounds, portal, fee, contact.
  TWD 1,600 application fee is NOT waivable (official).
- Wageningen: queue title said 2026; the live cycle is September 2027 MSc
  intake, deadline 1 Dec 2026 (complete application incl. diploma + English).
  Excellence Programme = tuition waiver ONLY (living excluded) -> marketed as
  Partially Funded. ASP (Africa) = full package. No separate scholarship form;
  invitation-based; lottery selection; offers ~7 Apr 2027.
- NIAS Safe Haven: queue title said 2026; the live call is first semester
  2027-28, applications 21 Jul-14 Dec 2026 12:00h (official nias.knaw.nl).
  EUR 3,500/month x 5 months + Amsterdam accommodation/travel/office.
  Scholarly track needs PhD + 3 yrs postdoc; creative tracks need bachelor's
  + 7 yrs experience. Humanities/social sciences only.
- WA Premier's: queue title said 2026; the 2027 round opens 16 Nov 2026,
  closes 19 Mar 2027 (official uwa.edu.au, "Opening Soon"). AUD 50,000
  one-time tuition grant (NOT a full ride) -> marketed as Funded. UWA
  instance: onshore international postgrads, 2+ yr course, Semester 1 2027
  start, 21 eligible countries incl. India; separate application with
  500-1000 word statement + community service + achievement evidence.
- Stockholm Scheme: queue title said 2025; the live round is autumn 2027,
  first admission round deadline 15 Jan 2027. Full tuition waiver
  (SEK 90k-140k/yr); living costs excluded -> Partially Funded. Merit-based,
  SU as first choice. SI Scholarship (separate, Feb 2027, needs 3,000h work
  experience) mentioned as an alternative, not conflated.

SKIPPED (queue order; reasons):
- Taiwan Tech ASUS Scholarship 2026: 2027 call deadline 5 Sep 2026 passed
  (kaistscholarship.com); only the 2022 launch + stale 2026-intake tracker
  posts verifiable; no current open call.
- BYD Internship Program 2025 Thailand: employer internship, not a
  scholarship; 2025 cycle closed.
- OIST Visiting Program 2026: FY2027 full-consideration deadline 15 Sep 2026
  passed (official oist.jp); no new cycle announced.
- ASU MasterCard Scholarship 2026: 2027-28 call deadline 27 Sep 2026 passed
  per two trackers; one tracker claims 2 Nov 2026 - conflict unresolvable,
  no official open call confirmed.
- Switzerland TaDA Residence Program 2026: 2027 call deadline 12 Aug 2026
  passed (official TaDA call PDF); 2026 applications closed.
- EERC Internship Program 2025 Nigeria: employer internship, not a
  scholarship; 2025 cycle closed.
- Global South Study Week 2025 Lebanon: 2025 event, closed.
- 65000 FIFA Volunteer Program 2026: volunteer programme, not a scholarship.
- UNESCO Granada Literature Residency 2025: 2025 residency, closed.
- CUAS TECH Scholarship 2026: 2026 call closed 15 May 2026 (official
  studyinaustria.at); Europe/South America/Mexico only - wrong audience.
- UWC Mastercard Foundation Scholarship 2026: official uwc.ac.za says "not
  accepting applications until further notice"; 2026 call closed.
- SEARCA Scholarship 2026: 2026-27 call closed 30 Sep 2025 (official
  searca.org); 2027-28 call not published.
- Turkish Language and Culture Program 2025 (KatipAta): duplicate of the
  skipped KATIP 2026 topic; 2025 cycle closed.
- Egyptian MOHE Scholarships 2026: no single verifiable deadline or unified
  terms; awards run via bilateral/Wafedeen channels that vary by country.
- Aspire Leadership Program 2025: 2025 cohort closed.
- Cambridge AI Research Internship 2026: generic aggregator topic; no unified
  official programme found.
- Utah Fulbright US Student Program 2026: US-citizens-only - wrong audience.
- Mary Washington Scholarships 2026: aggregator construct; flagship
  full-rides are US-state-based (Washington Scholars = VA residents, Alvey =
  out-of-state US); no clean verifiable 2027 programme.
- HKH Arctic Leadership Forum 2025: 2025 event, closed.
- HIIA Future Leadership Program 2025: 2025 programme, closed.
- Brighton International Fellowship 2025: 2025 fellowship, closed.
- Apple Trainee Program 2026: employer trainee programme, not a scholarship.
- UNS Scholarship 2026: August 2026 intake call closed (official uns.ac.id);
  no 2027 call published.
- Google Generation Scholarship 2026: no active call verifiable
  (freshscholarships checked 22 Sep 2026: "no active call announced").
- London Delfina Foundation 2026: 2026 residency cycle closed (Oct 2026); no
  2027 call verified.
- Curtin RTP Scholarship 2026: official curtin.edu.au - 2027 intake closed;
  2028 opens July 2027.
- Kader Asmal Fellowship 2026: South Africa only - wrong audience.
- International Local Authorities Internship 2025 Turkey: 2025 internship,
  closed.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'cgu-2027': {'mono': 'CGU', 'title': 'Chang Gung University Scholarships 2027 in Taiwan (Fully Funded)',
   'href': 'chang-gung-university-scholarships-2027-taiwan.html',
   'dpill': 'Round 1 closes 17 Nov 2026 · 26 days left',
   'award': 'Full tuition waiver; Master\u2019s: TWD 8,000/month + advisor assistantship. PhD: TWD 12,000/month + NT$29,000/month stipend.',
   'elig': 'Non-Taiwanese international students; bachelor\u2019s for Master\u2019s, master\u2019s for PhD; no concurrent scholarship; one department per application.',
   'tags': [('Master\u2019s', 'blue'), ('PhD', 'purple'), ('Taiwan', 'teal')]},
 'wageningen-2027': {'mono': 'WUR', 'title': 'Wageningen University Scholarships 2027 in Netherlands (Partially Funded)',
   'href': 'wageningen-university-scholarships-2027-netherlands.html',
   'dpill': 'Deadline 1 Dec 2026 · 40 days left',
   'award': 'Excellence: 24-month tuition waiver (living excluded). Africa Scholarship: full package (tuition + living + travel + visa + insurance).',
   'elig': 'Non-EU/EFTA citizens with a complete September-2027 MSc application before 1 Dec 2026; 80%+ GPA/First Class honours; invitation-based.',
   'tags': [('Master\u2019s', 'blue'), ('Netherlands', 'teal')]},
 'nias-safehaven': {'mono': 'NIAS', 'title': 'NIAS Safe Haven Fellowship 2027-28 in Netherlands (Fully Funded)',
   'href': 'nias-safe-haven-fellowship-2027-28-netherlands.html',
   'dpill': 'Deadline 14 Dec 2026 · 53 days left',
   'award': '\u20ac3,500/month for 5 months in Amsterdam + subsidised accommodation, office, research facilities, return travel.',
   'elig': 'Scholars, journalists, writers, artists at risk; PhD + 3 yrs postdoc (scholarly) or bachelor\u2019s + 7 yrs experience (creative); humanities/social sciences.',
   'tags': [('Fellowship', 'purple'), ('Netherlands', 'teal')]},
 'wa-premier-2027': {'mono': 'WA', 'title': "Western Australian Premier\u2019s University Scholarship 2027 in Australia (Funded)",
   'href': 'western-australian-premier-university-scholarship-2027-australia.html',
   'dpill': 'Opens 16 Nov 2026 · closes 19 Mar 2027',
   'award': 'One-time AUD $50,000 tuition grant for high-achieving onshore international postgraduates starting Semester 1, 2027.',
   'elig': 'UWA postgraduate offer (2+ yr full-time course); onshore international; Semester 1, 2027 start; citizen of 21 listed countries incl. India; no prior WA study.',
   'tags': [('Master\u2019s', 'blue'), ('Australia', 'teal')]},
 'stockholm-2027': {'mono': 'SU', 'title': 'Stockholm University Scholarship Scheme 2027 in Sweden (Partially Funded)',
   'href': 'stockholm-university-scholarship-scheme-2027-sweden.html',
   'dpill': 'Deadline 15 Jan 2027 · 85 days left',
   'award': 'Full tuition waiver (SEK 90,000\u2013140,000/yr); living costs not covered. Merit-based, decided from the first-round admission application.',
   'elig': 'Non-EU/EEA/Switzerland tuition-fee-paying students admitted to an SU master\u2019s; first (international) admission round; SU as first choice.',
   'tags': [('Master\u2019s', 'blue'), ('Sweden', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Chang Gung
A.append(dict(
 slug='chang-gung-university-scholarships-2027-taiwan',
 title='Chang Gung University Scholarships 2027 in Taiwan (Fully Funded)',
 meta='Chang Gung University Scholarships 2027: fully funded Master\u2019s and PhD scholarships in Taiwan \u2014 full tuition waiver plus TWD 8,000/month (Master\u2019s) or TWD 12,000 + NT$29,000/month (PhD). Fall 2027 Round 1 closes 17 November 2026. Eligibility, documents and how to apply.',
 short='Chang Gung University Scholarships', kicker='Taiwan · Master\u2019s & PhD · Fully Funded', mono='CGU',
 prov_short='Chang Gung University', prov_cat='University · Taiwan',
 h1='Chang Gung University Scholarships 2027 in Taiwan (Fully Funded)',
 sub='Full tuition plus a monthly living package at one of Taiwan\u2019s leading private research universities \u2014 for international Master\u2019s and PhD students starting in fall 2027.',
 dpill='Round 1 closes 17 Nov 2026 · 26 days left',
 facts=facts([('Award', 'Full tuition waiver. Master\u2019s students receive TWD 8,000 per month plus a research assistantship with their advisor; PhD students receive TWD 12,000 per month living allowance plus an NT$29,000 per month stipend (about US$966), plus an advisor research assistantship.'),
              ('Eligible', 'Non-Taiwanese international students: a bachelor\u2019s degree for Master\u2019s applicants, a master\u2019s degree for PhD applicants. Good physical and mental health. You may not hold another scholarship at the same time, and you may apply to one department only.'),
              ('How', 'Apply online through the CGU international admissions portal (recruit-intl.cgu.edu.tw) before the round deadline. Pay the TWD 1,600 (US$50) application fee \u2014 it is non-refundable and cannot be waived, even for scholarship applicants. Admission is by written document review, with a phone or video interview if the department needs one.'),
              ('Deadline', 'Fall 2027 Round 1: 25 September \u2013 17 November 2026 (26 days from 22 Oct 2026). Round 2: 29 December 2026 \u2013 20 February 2027. The 2027 spring round (Master\u2019s/PhD only) closed 25 September 2026.'),
              ('Fine print', 'CGU contacts applicants by email only \u2014 use an address you check daily. No IELTS is required if your previous education was in English. Documents not in Chinese or English need a notarised translation.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Chang Gung University (CGU)</strong> in Taoyuan, Taiwan, runs its own scholarship for international students alongside its degree admissions: a <strong>full tuition waiver plus a monthly living package</strong> for Master\u2019s and PhD students. It is one of the more generous university-funded awards in Taiwan because the PhD tier stacks three separate payments \u2014 a living allowance, a monthly stipend, and an advisor research assistantship.</p>
      <p>The university has published its <strong>2027\u20132028 international admission guidelines</strong> (posted 4 September 2026) with two fall rounds. <strong>Round 1 is open now and closes 17 November 2026</strong> \u2014 26 days from today (22 October 2026). A second round follows from 29 December 2026 to 20 February 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Taiwanese international student</strong> (all nationalities except Taiwan).</li>
        <li>Hold a <strong>bachelor\u2019s degree</strong> for Master\u2019s programmes, or a <strong>master\u2019s degree</strong> for PhD programmes.</li>
        <li>Be in <strong>good physical and mental health</strong>.</li>
        <li><strong>Not hold any other scholarship</strong> at the same time.</li>
        <li>Apply to <strong>one department only</strong> \u2014 multiple simultaneous applications are not processed.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee waiver</strong> for both Master\u2019s and PhD students.</li>
        <li>Master\u2019s: <strong>TWD 8,000 per month</strong> living allowance.</li>
        <li>PhD: <strong>TWD 12,000 per month</strong> living allowance <strong>plus NT$29,000 per month</strong> (about US$966) as a stipend.</li>
        <li><strong>Research assistantships</strong> with the student\u2019s advisor, for both levels.</li>
        <li>Programmes start in the <strong>fall semester (early September)</strong>; spring entry (mid-February) exists for Master\u2019s/PhD but its 2027 round has closed.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>online application form</strong> on the CGU international admissions portal.</li>
        <li><strong>Highest degree certificate</strong> (officially stamped) and <strong>academic transcripts</strong>.</li>
        <li><strong>Two letters of recommendation</strong>.</li>
        <li>A <strong>valid passport</strong> (bio page).</li>
        <li>A <strong>study plan</strong> in English or Chinese.</li>
        <li>An <strong>English proficiency statement</strong> if applicable (no IELTS needed if your previous education was in English).</li>
        <li>PhD applicants: <strong>academic thesis or publications</strong>.</li>
        <li><strong>Payment receipt</strong> for the TWD 1,600 application fee \u2014 unpaid applications are not processed, and cash is not accepted.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on the portal</strong>Create an account at recruit-intl.cgu.edu.tw, confirm it through the email link, log in, and select your programme \u2014 remember, one department only.</li>
        <li><strong>Complete the form step by step</strong>Fill in every section online and upload all required documents before the round deadline.</li>
        <li><strong>Pay the application fee</strong>Transfer TWD 1,600 (US$50) and upload the payment receipt to the portal. The fee is non-refundable and cannot be waived for any reason, including scholarship applicants.</li>
        <li><strong>Submit before the round closes</strong>Round 1 closes <strong>17 November 2026</strong>; Round 2 runs 29 December 2026 \u2013 20 February 2027. Late submissions are not accepted.</li>
        <li><strong>Watch your email</strong>CGU contacts applicants solely by email. Review is by written documents, with a phone or video interview only if the department requests one.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is IELTS required for the CGU scholarship?',
  'No \u2014 if your previous education was in English, you do not need IELTS. An English proficiency statement is only asked for where applicable.'),
 ('Can I apply to two departments to improve my chances?',
  'No. CGU states clearly that you may apply for one department only; applications that ignore this are not processed.'),
 ('Is the application fee waived for scholarship applicants?',
  'No. The TWD 1,600 (US$50) fee is mandatory, non-refundable, and explicitly cannot be waived for any reason \u2014 including when applying for the CGU scholarship.'),
 ('When do classes start?',
  'Fall semester classes begin in early September 2027. The spring semester (mid-February start) is Master\u2019s/PhD only, and its 2027 round has already closed.'),
 ('Can I hold another scholarship alongside the CGU one?',
  'No. Candidates cannot hold more than one scholarship at the same time.'),
 ('How will I know the result?',
  'By email \u2014 CGU contacts applicants solely by email, so use a valid address you check frequently.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026: official cgu.edu.tw \u201cApplication Guidelines for International Students 2027\u20132028 Academic Year\u201d page (posted 4 Sep 2026) \u2014 Fall 2027 Round 1: 25 Sep\u201317 Nov 2026; Round 2: 29 Dec 2026\u201320 Feb 2027; 2027 spring round (Master\u2019s/PhD only, 3 Aug\u201325 Sep 2026) now closed; apply at recruit-intl.cgu.edu.tw; contact cgu_fs@mail.cgu.edu.tw, +886-3-2118800 ext 3064. Official CGU application procedures page: TWD 1,600 (US$50) fee, non-refundable and not waivable; one department per application; email-only contact; written review with possible phone/video interview. Scholarship package (full tuition waiver; Master\u2019s TWD 8,000/month + advisor assistantship; PhD TWD 12,000/month + NT$29,000/month stipend + advisor assistantship) corroborated by three agreeing trackers (opportunitiesinfo.com, bloompakistan.com, montessoriline.com); the scholarshipforphd.com 2027 guide agrees on rounds, documents and the no-IELTS-if-English-educated rule. No invented GPA or test thresholds are stated.</p>
''',
 dl_long='Deadline: 17 November 2026 (Fall 2027 Round 1 \u2014 26 days from 22 Oct 2026). Round 2: 29 December 2026 \u2013 20 February 2027.',
 offlinks=[('2027\u201328 international admission guidelines \u2014 official (cgu.edu.tw)', 'https://www.cgu.edu.tw/recruit_intl/Subject/Detail/83973?nodeId=15120'),
           ('CGU international admissions portal', 'https://recruit-intl.cgu.edu.tw/'),
           ('CGU application procedures \u2014 official (cgu.edu.tw)', 'https://www.cgu.edu.tw/recruit_intl/Contents?nodeId=15181')],
 related_titles=['ntu', 'taiwanicdf-2027', 'tigp-2027', 'daad', 'minnesota-ges'],
))

# ---------------------------------------------------------------- 2. Wageningen
A.append(dict(
 slug='wageningen-university-scholarships-2027-netherlands',
 title='Wageningen University Scholarships 2027 in Netherlands (Partially Funded)',
 meta='Wageningen University Scholarships 2027: Excellence Programme tuition waiver, Africa Scholarship Programme full package, and Anne van den Ban Fund for the September 2027 MSc intake in the Netherlands. Deadline 1 December 2026. Eligibility, documents and how to apply.',
 short='Wageningen University Scholarships', kicker='Netherlands · Master\u2019s · Partially Funded', mono='WUR',
 prov_short='Wageningen University & Research', prov_cat='University · Netherlands',
 h1='Wageningen University Scholarships 2027 in Netherlands (Partially Funded)',
 sub='One application, three funding tracks: a tuition waiver for top non-EU master\u2019s applicants, a full package for African students, and a developing-country fund \u2014 all decided from your MSc application before 1 December 2026.',
 dpill='Deadline 1 Dec 2026 · 40 days left',
 facts=facts([('Award', 'Excellence Programme: tuition-fee waiver for the full 24-month MSc (living costs NOT included). Africa Scholarship Programme: tuition + living expenses + travel + visa costs + health insurance. Anne van den Ban Fund: partial or full support for selected students from developing/low-income countries \u2014 no direct application.'),
              ('Eligible', 'Citizens of countries outside the EU/EFTA, admitted to a Wageningen MSc starting September 2027. Excellence track: complete MSc application before 1 December 2026, unconditional admission, First Class honours bachelor\u2019s (or 80%+ GPA), bachelor\u2019s completed before the deadline, English requirements met before the deadline. Only prospective students \u2014 current WUR students cannot apply.'),
              ('How', 'There is NO separate scholarship form. Apply for the MSc programme normally and submit a complete application \u2014 diploma and official English test results uploaded \u2014 before 1 December 2026. Shortlisted candidates are invited to the final selection around March\u2013April 2027; recipients are chosen by lottery, with offers around 7 April 2027.'),
              ('Deadline', '1 December 2026 \u2014 40 days from 22 Oct 2026. Only complete applications submitted before this date are assessed by the scholarship committee at all.'),
              ('Fine print', 'Scholarships apply to the September intake only (the NL Scholarship is the exception, with a February intake too). English test results take weeks \u2014 plan ahead, because there is no extension for a late score. A final-year student still mid-thesis on 1 December does not qualify. For ASP, preference goes to applicants who do not already hold a master\u2019s degree.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Wageningen University & Research (WUR)</strong> \u2014 the Netherlands\u2019 specialist university for food, agriculture, environment and life sciences \u2014 funds international master\u2019s students through three tracks, all decided from the <strong>same MSc application</strong>. There is no separate scholarship form to hunt down: the strength of your programme application <em>is</em> your scholarship application.</p>
      <p>The headline track, the <strong>Excellence Programme</strong>, waives tuition for the full 24-month MSc for outstanding non-EU/EFTA students. Be clear-eyed about what it is: a <strong>tuition waiver, not a full ride</strong> \u2014 living costs are yours, which is why this article is honestly labelled partially funded. The <strong>Africa Scholarship Programme (ASP)</strong> is the genuinely full package (tuition, living, travel, visa, insurance) for African applicants, and the <strong>Anne van den Ban Fund</strong> supports selected students from developing countries without a direct application route.</p>
      <p>Everything hinges on one date: a <strong>complete MSc application before 1 December 2026</strong> \u2014 40 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of a country outside the EU and EFTA</strong>.</li>
        <li>Apply for a <strong>Wageningen MSc programme starting September 2027</strong> and receive <strong>unconditional admission</strong>.</li>
        <li>Hold a <strong>First Class honours bachelor\u2019s degree or equivalent (80%+ GPA)</strong> \u2014 and have <strong>completed the degree before 1 December 2026</strong>.</li>
        <li>Meet the university\u2019s <strong>English-language requirements before the deadline</strong> (official test results uploaded \u2014 no extensions for late scores).</li>
        <li>Be a <strong>prospective student</strong>: students already enrolled at WUR cannot apply for these scholarships.</li>
        <li>ASP additionally targets <strong>African applicants</strong>; preference goes to those without a previous master\u2019s degree.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Excellence Programme:</strong> full <strong>tuition-fee waiver for 24 months</strong>.</li>
        <li><strong>Africa Scholarship Programme:</strong> tuition fees, <strong>living expenses, travel, visa costs and health insurance</strong>.</li>
        <li><strong>Anne van den Ban Fund:</strong> partial or full support for selected students from developing/low-income countries (invitation/nomination \u2014 you cannot apply directly).</li>
        <li>Finalists not selected in the lottery go on a <strong>waiting list</strong> rather than being rejected outright \u2014 places can still open up.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>complete MSc application</strong> via the university\u2019s admissions portal \u2014 this doubles as the scholarship application.</li>
        <li><strong>Bachelor\u2019s diploma</strong> (degree must be completed before 1 December 2026), uploaded with the application.</li>
        <li><strong>Official English-language test results</strong> (e.g. IELTS/TOEFL per programme requirements) \u2014 available and uploaded before the deadline.</li>
        <li><strong>Academic transcripts</strong> and all programme-specific supporting documents.</li>
        <li>Shortlisted candidates are later <strong>invited</strong> to the ASP/Excellence selection process \u2014 no extra form to find yourself.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your MSc programme early</strong>Pick from Wageningen\u2019s English-taught master\u2019s programmes for the September 2027 intake and check its specific admission requirements.</li>
        <li><strong>Book your English test now</strong>Results take weeks to arrive, and they must be uploaded before 1 December 2026 \u2014 a late score disqualifies the whole application.</li>
        <li><strong>Submit a complete MSc application</strong>File everything \u2014 diploma, transcripts, English results, supporting documents \u2014 <strong>before 1 December 2026</strong>. Incomplete applications are not assessed by the scholarship committee at all.</li>
        <li><strong>Wait for the invitation</strong>Around March\u2013April 2027, shortlisted candidates are invited to the final selection stage.</li>
        <li><strong>Lottery and offers</strong>Recipients are chosen by lottery from the shortlist, with scholarship offers going out around <strong>7 April 2027</strong>. Unselected finalists join a waiting list.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate scholarship application form?',
  'No. You apply for the MSc programme the normal way; a complete, strong application before 1 December 2026 is what puts you in front of the scholarship committee.'),
 ('Does the Excellence Programme cover living costs?',
  'No \u2014 it is a tuition-fee waiver for 24 months. Living expenses, insurance and travel are yours, which is why this article is labelled partially funded rather than fully funded.'),
 ('I am an African applicant \u2014 which track is for me?',
  'The Africa Scholarship Programme: the same 1 December 2026 MSc deadline applies, and qualifying applicants are invited into its selection process for the full package (tuition + living + travel + visa + insurance).'),
 ('Can current WUR students apply?',
  'No. All three tracks are for prospective students only \u2014 you must not already be enrolled at Wageningen.'),
 ('What if my English test results arrive after 1 December?',
  'Then the application is incomplete and will not be assessed for scholarships \u2014 there is no extension for late scores. Book the test now.'),
 ('I finish my bachelor\u2019s in December 2026. Am I eligible?',
  'No. The degree must be fully completed \u2014 diploma uploaded \u2014 before 1 December 2026.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across five agreeing sources: youthexpat.com (Excellence Programme \u2014 deadline 1 Dec 2026, non-EU/EFTA, complete MSc application, unconditional admission, 80%+ GPA / First Class honours, English + diploma before the deadline, invitation-based); worldwide-scholarships.com (ASP \u2014 no separate form, invitation after a complete MSc application, shortlist Mar\u2013Apr 2027, lottery selection, offers 7 Apr 2027, preference for first-time master\u2019s holders); opportunitiesforyouth.org (Excellence = 24-month tuition waiver; ASP/ABF = tuition + living + travel + visa + insurance); globalsouthopportunities.com (September 2027 intake; ASP/Excellence timelines and lottery); collegedunia.com (admissions timeline: September 2027 primary intake with the 1 Dec 2026 scholarship cut-off; February 2027 limited to five programmes). No invented award amounts are stated beyond the published tuition-waiver and ASP package descriptions.</p>
''',
 dl_long='Deadline: 1 December 2026 (complete MSc application, including diploma and English test \u2014 40 days from 22 Oct 2026). Selection invitations Mar\u2013Apr 2027; offers around 7 Apr 2027.',
 offlinks=[('Wageningen Excellence Programme \u2014 guide (youthexpat)', 'https://youthexpat.com/2026/08/10/wageningen-university-excellence-scholarship-programme-scholarship/'),
           ('Wageningen Africa Scholarship Programme \u2014 guide', 'https://worldwide-scholarships.com/scholarships/wageningen-university-africa-scholarship-programme-asp/'),
           ('WUR admissions timeline (collegedunia)', 'https://collegedunia.com/netherlands/college/757-wageningen-university--research-wageningen/admission')],
 related_titles=['tue-excellence', 'tudelft-excellence-2027', 'radboud-2027', 'leiden-mandela', 'uva-merit-2027'],
))

# ---------------------------------------------------------------- 3. NIAS Safe Haven
A.append(dict(
 slug='nias-safe-haven-fellowship-2027-28-netherlands',
 title='NIAS Safe Haven Fellowship 2027-28 in Netherlands (Fully Funded)',
 meta='NIAS Safe Haven Fellowship 2027-28: five-month fully funded fellowship in Amsterdam (\u20ac3,500/month) for scholars, journalists, writers and artists at risk. Applications open until 14 December 2026. Eligibility, documents and how to apply.',
 short='NIAS Safe Haven Fellowship', kicker='Netherlands · Fellowship · Fully Funded', mono='NIAS',
 prov_short='NIAS-KNAW', prov_cat='Netherlands Institute for Advanced Study',
 h1='NIAS Safe Haven Fellowship 2027-28 in Netherlands (Fully Funded)',
 sub='Five months in Amsterdam \u2014 \u20ac3,500 a month, a desk, and a safe place to keep working \u2014 for researchers, journalists, writers and artists whose work is under threat.',
 dpill='Deadline 14 Dec 2026 · 53 days left',
 facts=facts([('Award', '\u20ac3,500 per month for 5 months. Subsidised accommodation in Amsterdam or commuting expenses; a private office, research facilities and library access; communal lunches and the NIAS fellows community; outward and return travel reimbursed.'),
              ('Eligible', 'Scholars, journalists, writers and artists unable to work safely in their current location due to conflict, war, or severe restrictions on academic or creative freedom. Scholarly track: PhD plus at least 3 years of postdoctoral research. Journalistic/literary/artistic track: bachelor\u2019s degree plus at least 7 years of professional experience. The project must fall within the humanities or social sciences; full English proficiency is required; no affiliation with institutions boycotted by the Dutch state.'),
              ('How', 'Online application form ONLY \u2014 applications sent by email are not considered. Prepare a research proposal, CV, motivation statement and risk statement, all in English and in line with the regulations. After submitting, confirm your registration within 48 hours of the automated email, or the application expires. NIAS runs two selection rounds a year (June and December deadlines); eligible applications go to two external referees, then the Fellowship Advisory Committee.'),
              ('Deadline', '14 December 2026, 12:00h \u2014 first semester 2027\u201328 call; applications have been open since 21 July 2026 (53 days from 22 Oct 2026).'),
              ('Fine print', 'This is a temporary refuge, not a degree programme. About ten scholarly and ten literary/journalistic/artistic fellowships are awarded per round. Incomplete applications are ineligible and cannot be changed once submitted \u2014 and the programme makes no exceptions to the requirements.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>NIAS Safe Haven Fellowship</strong>, run by the <strong>Netherlands Institute for Advanced Study (NIAS-KNAW)</strong> in Amsterdam, exists for one purpose: to give <strong>scholars, journalists, writers and artists at risk</strong> a safe place to continue their work. If conflict, war, or state or non-state obstruction makes it impossible to work where you are, this fellowship offers <strong>five months of protected time</strong> in one of Europe\u2019s leading institutes for advanced study.</p>
      <p>The current call covers the <strong>first semester of the 2027\u20132028 academic year</strong>. Applications opened 21 July 2026 and close <strong>14 December 2026 at 12:00h</strong> \u2014 53 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>scholar, journalist, writer or artist unable to carry out your work safely</strong> in your current location or circumstances \u2014 due to conflict, war, or severe infringements on academic/creative freedom.</li>
        <li><strong>Scholarly track:</strong> hold a <strong>PhD</strong> and have at least <strong>3 years of postdoctoral research experience</strong> at the time of application.</li>
        <li><strong>Journalistic, literary or artistic track:</strong> hold at least a <strong>bachelor\u2019s degree</strong> and have a minimum of <strong>7 years of professional experience</strong> in your field.</li>
        <li>Propose a project within the <strong>humanities or social sciences</strong>.</li>
        <li>Have <strong>full proficiency in English</strong> \u2014 it is the working language at NIAS.</li>
        <li><strong>Not be affiliated</strong> with institutions boycotted by the Dutch state.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A stipend of <strong>\u20ac3,500 per month</strong> for five months.</li>
        <li><strong>Subsidised accommodation in Amsterdam</strong> or commuting travel expenses.</li>
        <li>A <strong>private office, research facilities and library access</strong>, plus communal lunches and full participation in the NIAS fellows community.</li>
        <li><strong>Reimbursement of outward and return travel</strong>.</li>
        <li>Partnership backing from the <strong>University of Amsterdam, Maastricht University and the Royal Netherlands Academy of Arts and Sciences (KNAW)</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>A <strong>research proposal</strong> describing the project you will pursue during the fellowship.</li>
        <li>A <strong>curriculum vitae</strong> evidencing your experience (publications for scholarly applicants; professional record for creative tracks).</li>
        <li>A <strong>motivation statement</strong>.</li>
        <li>A <strong>risk statement</strong> explaining why you cannot work safely in your current circumstances.</li>
        <li>All documents in <strong>English</strong> and in line with the official regulations \u2014 read them first, because incomplete applications are ineligible.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the regulations</strong>On the official NIAS Safe Haven Fellowship page, read the formal requirements carefully \u2014 the programme makes no exceptions.</li>
        <li><strong>Prepare the four documents</strong>Write your research proposal, CV, motivation statement and risk statement in English, following the regulations exactly.</li>
        <li><strong>Complete the online form</strong>Submit through the official online application form only. Applications sent by email are not considered.</li>
        <li><strong>Confirm within 48 hours</strong>After submitting, confirm your registration within 48 hours of receiving the automated email \u2014 otherwise the application expires.</li>
        <li><strong>Selection</strong>Eligible applications are sent to two external referees; the ten highest-scoring scholarly and ten highest-scoring literary/journalistic/artistic applications go to the Fellowship Advisory Committee, which advises the NIAS Director\u2019s final decision. Apply by <strong>14 December 2026, 12:00h</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Who is the Safe Haven Fellowship for?',
  'Established scholars, journalists, writers and artists who cannot carry out their work safely where they are \u2014 because of conflict, war, or obstruction by state or non-state actors. It is a temporary academic refuge, not a degree programme.'),
 ('Do I need a PhD to apply?',
  'Only for the scholarly track (PhD + 3 years postdoctoral experience). Journalistic, literary and artistic applicants need a bachelor\u2019s degree plus at least 7 years of professional experience instead.'),
 ('What fields are covered?',
  'The humanities and the social sciences. Your proposed project must fall within those areas.'),
 ('Can I apply by email?',
  'No. Applications are accepted only through the official online application form; email applications are not considered.'),
 ('How long is the fellowship, and when does it run?',
  'Five months. This call is for the first semester of the 2027\u20132028 academic year (the September\u2013January semester pattern).'),
 ('How many fellowships are awarded?',
  'About ten scholarly and ten literary/journalistic/artistic fellowships per selection round; NIAS runs two rounds a year with June and December deadlines.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026: official nias.knaw.nl application page \u2014 \u201cThe call is currently accepting applications for Safe Haven Fellowships in the first semester of the 2027\u20132028 academic year. Applications for this period can be submitted from 21 July 2026 until 14 December 2026 at 12:00h.\u201d Official NIAS Safe Haven Fellowship page: online-only application; research proposal + CV + motivation statement + risk statement in English; 48-hour registration confirmation; two selection rounds a year; ten scholarly + ten literary/journalistic/artistic fellowships per round via external referees and the Fellowship Advisory Committee. Package (\u20ac3,500/month, subsidised Amsterdam accommodation or commuting, office and facilities, travel reimbursement) and eligibility (PhD + 3 yrs postdoc for scholarly; bachelor\u2019s + 7 yrs experience for creative tracks; humanities/social sciences; full English) corroborated by i79media.com (2027\u201328 session, deadline 14 Dec 2026) and agreeing trackers (scholarshipbob.com x2, ilmkidunya.com, scholarshipunion.com, burseline.com).</p>
''',
 dl_long='Deadline: 14 December 2026, 12:00h (first semester 2027\u201328 \u2014 53 days from 22 Oct 2026). NIAS runs two selection rounds per year (June and December deadlines).',
 offlinks=[('Safe Haven Fellowship \u2014 application (official, nias.knaw.nl)', 'https://nias.knaw.nl/application-form-safe-haven-fellowship/'),
           ('Safe Haven Fellowship \u2014 about (official, nias.knaw.nl)', 'https://nias.knaw.nl/fellowships/safe-haven-fellowship-for-scholars-at-risk/')],
 related_titles=['maastricht', 'leiden-mandela', 'hanns-seidel', 'swiss-phd', 'tue-excellence'],
))

# ---------------------------------------------------------------- 4. WA Premier's
A.append(dict(
 slug='western-australian-premier-university-scholarship-2027-australia',
 title='Western Australian Premier\u2019s University Scholarship 2027 in Australia (Funded)',
 meta='Western Australian Premier\u2019s University Scholarship 2027: AUD $50,000 for high-achieving international postgraduates at the University of Western Australia. Applications open 16 November 2026, close 19 March 2027. Eligibility and how to apply.',
 short='WA Premier\u2019s University Scholarship', kicker='Australia · Postgraduate · Funded', mono='WA',
 prov_short='University of Western Australia', prov_cat='University · Australia',
 h1='Western Australian Premier\u2019s University Scholarship 2027 in Australia (Funded)',
 sub='AUD $50,000 toward your postgraduate tuition in Perth \u2014 the WA Government\u2019s flagship award for high achievers from 21 countries, opening 16 November 2026.',
 dpill='Opens 16 Nov 2026 · closes 19 Mar 2027',
 facts=facts([('Award', 'A one-time AUD $50,000 grant applied directly to tuition fees (one award at UWA). It is a major contribution, not a full ride \u2014 budget separately for remaining tuition, living costs, health insurance and flights.'),
              ('Eligible', 'Onshore international students with an offer from UWA for a full-time postgraduate course of at least two years, commencing Semester 1, 2027, who meet visa criteria and have not previously studied in Western Australia or entered via a packaged, foundation or English-language pathway. Citizens of 21 listed countries including India, Bangladesh, Nepal, Sri Lanka, Indonesia, Vietnam, Kenya, Malaysia, Singapore and the Philippines. One-year law courses, 1.5-year arts courses and courses with 24 points of admission credit are excluded.'),
              ('How', 'Apply through UWA\u2019s scholarship form between 16 November 2026 and 19 March 2027 (3:00pm). Prepare: a 500\u20131000 word written statement on why the scholarship would benefit you and how a UWA postgraduate degree fits your future; evidence of community service; and evidence of recognition awarded for academic, community or sporting achievement.'),
              ('Deadline', 'Applications open 16 November 2026 and close 19 March 2027 (3:00pm). Outcomes are notified in May 2027.'),
              ('Fine print', 'The WA Government funds this award across five WA universities, but each university sets its own terms \u2014 this article covers UWA\u2019s instance (postgraduate, onshore, direct application). Do not confuse it with UWA\u2019s automatic Global Excellence Scholarship, which needs no separate application.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Western Australian Premier\u2019s University Scholarship</strong> is the Government of Western Australia\u2019s flagship award for attracting high-achieving international students to the state\u2019s universities. At the <strong>University of Western Australia (UWA)</strong> in Perth, it takes the form of a <strong>one-time AUD $50,000 grant applied directly to tuition fees</strong> for a commencing postgraduate student.</p>
      <p>UWA\u2019s official listing currently shows the status as <strong>\u201cOpening Soon\u201d</strong>: applications open <strong>16 November 2026</strong> and close <strong>19 March 2027 (3:00pm)</strong>, with outcomes notified in <strong>May 2027</strong>. An honest note first: $50,000 is a serious contribution, but it is <strong>not a full ride</strong> \u2014 plan for remaining tuition, accommodation, food, transport, health insurance, visa costs and flights.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Have <strong>applied and received an offer</strong> from UWA for a <strong>postgraduate course</strong> as an <strong>onshore international student</strong>, studying <strong>full time for at least two years</strong>.</li>
        <li>Be <strong>commencing studies onshore for Semester 1, 2027</strong>.</li>
        <li>Meet the criteria for an <strong>Australian international student visa</strong>.</li>
        <li><strong>Not</strong> have commenced or completed previous studies in Western Australia, and <strong>not</strong> be entering on a packaged, foundation or English-language pathway.</li>
        <li>Be a <strong>citizen of one of the 21 listed countries</strong>, including India, Bangladesh, Bhutan, Nepal, Sri Lanka, Indonesia, Malaysia, Singapore, the Philippines, Vietnam, Kenya, China, Japan, South Korea, Hong Kong, the UAE, Saudi Arabia, Oman, Brazil, Colombia and the UK.</li>
        <li>Excluded at UWA: one-year law courses, 1.5-year arts courses, and business/science courses carrying 24 points of admission credit (these finish in 1.5 years).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>one-time AUD $50,000 payment</strong> applied directly against tuition fees.</li>
        <li>The prestige of a <strong>government-funded flagship award</strong>, nominated through the university.</li>
        <li>Study at <strong>UWA in Perth</strong>, one of Australia\u2019s leading research universities.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>completed UWA scholarship application form</strong> (opens 16 November 2026).</li>
        <li>A <strong>written statement of 500\u20131000 words</strong> outlining why the scholarship would benefit you and how a UWA postgraduate degree fits into your future plans.</li>
        <li><strong>Evidence of community service</strong>.</li>
        <li><strong>Evidence of recognition</strong> awarded for academic, community or sporting achievement.</li>
        <li>Your <strong>UWA offer for the postgraduate course</strong> (you must hold the offer to apply).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure your UWA offer first</strong>Apply for an eligible 2+ year full-time postgraduate course at UWA for Semester 1, 2027, and receive your offer \u2014 you cannot apply for the scholarship without it.</li>
        <li><strong>Wait for the form to open</strong>The scholarship application form opens on <strong>16 November 2026</strong>. Use the waiting time to draft your statement and gather evidence.</li>
        <li><strong>Write the statement</strong>Prepare 500\u20131000 words on why this scholarship would benefit you and how the UWA degree fits your future \u2014 plus concrete evidence of community service and recognised achievement.</li>
        <li><strong>Submit before 19 March 2027 (3:00pm)</strong>File the complete application through UWA\u2019s scholarship listing before the deadline.</li>
        <li><strong>Await the May 2027 outcome</strong>UWA notifies applicants of the outcome in May 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the WA Premier\u2019s Scholarship fully funded?',
  'No. It is a one-time AUD $50,000 grant applied to tuition \u2014 a major contribution, but you must budget separately for remaining tuition, living costs, insurance, visa and flights. That is why this article is labelled Funded, not Fully Funded.'),
 ('I am offshore. Can I apply at UWA?',
  'UWA\u2019s instance requires onshore commencement for Semester 1, 2027. The other four WA universities run their own Premier\u2019s scholarships with their own terms \u2014 check each university\u2019s page.'),
 ('Is it for undergraduates too?',
  'The WA Government program generally covers undergraduate and postgraduate study, but UWA\u2019s instance in this round is postgraduate. Check Curtin, Murdoch, ECU and Notre Dame for their own eligibility.'),
 ('Do I need a separate application?',
  'Yes \u2014 unlike UWA\u2019s automatic Global Excellence Scholarship, the Premier\u2019s Scholarship needs its own application with the written statement and evidence.'),
 ('When will I hear back?',
  'UWA notifies applicants of the outcome in May 2027.'),
 ('Which countries are eligible?',
  '21 listed countries at UWA, including India, Bangladesh, Nepal, Sri Lanka, Indonesia, Malaysia, Singapore, the Philippines, Vietnam, Kenya, China, Japan, South Korea, Hong Kong, the UAE, Saudi Arabia, Oman, Brazil, Colombia and the UK.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026: official uwa.edu.au scholarship listing \u2014 status \u201cOpening Soon\u201d; applications open 16 Nov 2026, close 19 Mar 2027 (3:00pm); value AUD $50,000; one offered; postgraduate; onshore international students with a UWA offer for a 2+ year full-time course commencing Semester 1, 2027; no prior WA study; not via packaged/foundation/English pathways; 21 eligible countries including India, Bangladesh, Nepal, Sri Lanka, Indonesia and Vietnam; requires a 500\u20131000 word statement plus evidence of community service and of academic/community/sporting recognition; outcomes notified May 2027. Corroborated by worldwidestudies.info (value $50,000; opens 16 Nov 2026; closes 19 Mar 2027; Semester 1, 2027 start; separate application required) and wsscholar4u.com (WA Government-funded flagship; one-time $50,000 tuition grant; run through WA\u2019s five universities). This article covers UWA\u2019s instance; terms at Curtin, Murdoch, ECU and Notre Dame Australia may differ \u2014 check each university\u2019s page.</p>
''',
 dl_long='Deadline: 19 March 2027, 3:00pm (applications open 16 November 2026; outcomes notified May 2027).',
 offlinks=[('Premier\u2019s University Scholarship \u2014 official (uwa.edu.au)', 'https://www.uwa.edu.au/study/scholarship-listing/westernaustralianpremiersuniversityscholarshipf234681'),
           ('WA Premier\u2019s University Scholarship \u2014 program overview', 'https://globalscholarships.com/external/western-australian-premiers-university-scholarship/')],
 related_titles=['griffith-vc', 'deakin-vc-2027', 'melbourne2027', 'adelaide2027', 'monash-rtp'],
))

# ---------------------------------------------------------------- 5. Stockholm
A.append(dict(
 slug='stockholm-university-scholarship-scheme-2027-sweden',
 title='Stockholm University Scholarship Scheme 2027 in Sweden (Partially Funded)',
 meta='Stockholm University Scholarship Scheme 2027: full tuition-fee waiver for non-EU/EEA master\u2019s students in Sweden. Apply in the first admission round by 15 January 2027. Eligibility, documents and how to apply.',
 short='Stockholm University Scholarship Scheme', kicker='Sweden · Master\u2019s · Partially Funded', mono='SU',
 prov_short='Stockholm University', prov_cat='University · Sweden',
 h1='Stockholm University Scholarship Scheme 2027 in Sweden (Partially Funded)',
 sub='Full tuition covered, living costs on you: Stockholm University\u2019s merit scholarship for non-EU master\u2019s students, decided from your first-round admission application.',
 dpill='Deadline 15 Jan 2027 · 85 days left',
 facts=facts([('Award', 'Full tuition-fee waiver \u2014 typically SEK 90,000\u2013140,000 per year depending on the programme. Living expenses are NOT covered, so budget around SEK 10,584 per month for the residence-permit funds proof.'),
              ('Eligible', 'Citizens of countries outside the EU/EEA/Switzerland who are required to pay tuition fees; admitted to a Stockholm University master\u2019s programme; applied in the first (international) admission round with Stockholm University as first choice; strong academic record; eligible for a Swedish residence permit for studies.'),
              ('How', 'Apply to your master\u2019s programme(s) via UniversityAdmissions.se in the autumn 2027 first round (deadline 15 January 2027). The scholarship is awarded on academic merit from the admission application \u2014 complete the scholarship motivation section in the same window. There is no separate fee.'),
              ('Deadline', '15 January 2027 \u2014 the first international admission round for autumn 2027 (85 days from 22 Oct 2026). Supporting documents are due 1 February 2027.'),
              ('Fine print', 'Highly competitive: only a small share of admitted non-EU students receive it each year, so budget the full tuition as your plan and treat the scholarship as a bonus. This scheme is separate from the Swedish Institute Scholarship for Global Professionals (full tuition + SEK 12,000/month stipend + travel grant), which needs 3,000 hours of work experience and applies in February 2027 \u2014 consider both.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Stockholm University Scholarship Scheme</strong> is the university\u2019s own merit award for <strong>non-EU/EEA master\u2019s students</strong>: a <strong>full waiver of tuition fees</strong> \u2014 typically SEK 90,000 to 140,000 per year depending on the programme. It is awarded on <strong>academic merit</strong> to students admitted in the <strong>first (international) admission round</strong> for the autumn intake.</p>
      <p>An honest framing first: this is a <strong>tuition waiver, not a full ride</strong>. Living costs in Stockholm are yours \u2014 the Swedish Migration Agency wants to see about <strong>SEK 10,584 per month</strong> in funds for the residence permit \u2014 which is why this article is labelled partially funded. Only a small share of admitted non-EU students receive the award each year, so apply for it but <strong>budget the full tuition as your plan</strong>.</p>
      <p>The autumn 2027 first round is <strong>open now</strong>; the programme application deadline is <strong>15 January 2027</strong> \u2014 85 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of a country outside the EU/EEA/Switzerland</strong> and required to pay tuition fees.</li>
        <li>Be <strong>admitted to a Stockholm University master\u2019s programme</strong> (full-time).</li>
        <li>Have applied in the <strong>first (international) admission round</strong>, with <strong>Stockholm University as first choice</strong> on the UniversityAdmissions portal.</li>
        <li>Show a <strong>strong academic record</strong> \u2014 selection is merit-based.</li>
        <li>Be <strong>eligible for a Swedish residence permit</strong> for studies and not already residing in Sweden.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% tuition-fee waiver</strong> for the master\u2019s programme (renewable with the programme, subject to academic progress).</li>
        <li><strong>No separate application fee</strong> for the scholarship itself.</li>
        <li>Combines with <strong>external awards</strong>: you can also apply for the Swedish Institute Scholarship for Global Professionals (full tuition + SEK 12,000/month stipend + one-time travel grant) in February 2027 if you have 3,000 hours of work experience.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>UniversityAdmissions.se programme application</strong> (up to four programmes, ranked) \u2014 this doubles as the scholarship application.</li>
        <li><strong>Academic transcripts and degree certificates</strong> (attested; allow 4\u20136 weeks from Indian universities).</li>
        <li><strong>English proficiency proof</strong> (e.g. IELTS) \u2014 the score must be available before the <strong>1 February 2027</strong> document deadline.</li>
        <li>A <strong>motivation letter tailored per programme</strong> \u2014 generic reused letters are the top reason strong applicants land on the reserve list.</li>
        <li>A <strong>valid passport</strong>; do not send documents to SU directly \u2014 everything goes to University Admissions in Sweden.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Rank SU first</strong>On UniversityAdmissions.se, list your Stockholm University master\u2019s programme as your <strong>first choice</strong> \u2014 the scholarship requires it.</li>
        <li><strong>Complete the scholarship motivation section</strong>In the same application window, complete the university\u2019s scholarship motivation section with a programme-specific letter.</li>
        <li><strong>Submit by 15 January 2027</strong>File the programme application (and pay the UniversityAdmissions application fee) before the first-round deadline.</li>
        <li><strong>Upload documents by 1 February 2027</strong>Transcripts, degree certificates and the English test score must reach University Admissions by this date \u2014 start transcripts 8 weeks early.</li>
        <li><strong>Await admission and award decisions</strong>Admission results arrive in late March; scholarship decisions follow. Have the first tuition instalment ready by April 2027 in case the award goes elsewhere \u2014 the residence permit process cannot start until the fee clears.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Does the Stockholm University Scholarship cover living costs?',
  'No \u2014 it is a full tuition-fee waiver only. Budget around SEK 10,584 per month for living costs and the residence-permit funds proof. That is why this article is labelled partially funded.'),
 ('Can bachelor\u2019s students apply?',
  'No. The Scholarship Scheme targets master\u2019s applicants only.'),
 ('Is there a separate scholarship application?',
  'Not a separate portal: you apply through the UniversityAdmissions.se programme application in the first round and complete the scholarship motivation section in the same window.'),
 ('What happens if I apply in a later round?',
  'You are not eligible \u2014 the scheme requires application in the first (international) admission round with SU as first choice.'),
 ('What is the difference from the Swedish Institute Scholarship?',
  'The SI Scholarship for Global Professionals is a Swedish government award: full tuition plus SEK 12,000/month stipend plus a travel grant, but it requires a bachelor\u2019s degree, 3,000 hours of work experience and a February 2027 application. The SU Scheme is the university\u2019s own merit tuition waiver. Eligible applicants should consider both.'),
 ('How competitive is it?',
  'Very \u2014 only a small share of admitted non-EU students receive it each year. Treat it as a bonus and budget the full tuition (SEK 180,000\u2013280,000 for a two-year programme) as your plan.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across four agreeing sources: collegedunia.com (Stockholm University Scholarships 2027 table \u2014 Scheme: full tuition SEK 90,000\u2013140,000/yr for non-EU/EEA master\u2019s admits in the first round, expected 15 Jan 2027; SI Scholarship: full tuition + SEK 12,000/month, mid-Feb 2027; source cited as the Stockholm University scholarships page), collegedunia.com admissions guide (autumn 2027 Round 1: scholarship motivation section in the same window, documents by 1 Feb 2027, SEK 10,584/month funds proof, first tuition instalment by April 2027), daadscholarship.com (Scheme: full tuition for non-EU/EEA/Switzerland tuition-fee-paying students admitted to an SU master\u2019s, first-round application, academic merit, SU as first choice; official page su.se/english/education/how-to-apply/costs-fees-and-scholarships/scholarships), coursesdata.com (100% tuition waiver, non-EU/EEA, full-time master\u2019s, merit-based, living costs excluded, separate from SI scholarships). No invented award counts or recipient numbers are stated.</p>
''',
 dl_long='Deadline: 15 January 2027 (first international admission round, autumn 2027 \u2014 85 days from 22 Oct 2026). Supporting documents due 1 February 2027.',
 offlinks=[('Stockholm University scholarships \u2014 official (su.se)', 'https://www.su.se/english/education/how-to-apply/costs-fees-and-scholarships/scholarships'),
           ('Sweden admissions timeline 2027 (collegedunia)', 'https://collegedunia.com/sweden/university/778-stockholm-university-stockholm/admission')],
 related_titles=['daad', 'erfurt-phd', 'kassel-expose', 'leiden-mandela', 'cga-phd'],
))

import re as _re
def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)

if __name__ == '__main__':
    # fail fast if any related link target is missing from the registry
    for a in A:
        for t in a['related_titles']:
            if t not in CARDS:
                raise SystemExit('related_titles key missing from registry: ' + t)
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

#!/usr/bin/env python3
"""Batch 57 (cron run 57, 27 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. KPMG Global Internship Program 2026 - VERIFIED (rolling, no fixed
   deadline; fully funded 4-week rotation on top of a home-country KPMG
   internship: visa, return airfare, lodging, placement allowance).
2. Brandtech Group AI Good Scholarships 2026 - SKIPPED: deadline passed
   2 Aug 2026 (One Young World portal; Summit 3-6 Nov 2026, Cape Town).
3. UCLouvain Postdoctoral Fellowships 2027 - SKIPPED: deadline passed
   23 Sep 2026 09:00 (FSR call, 15 fellowships; queue's "European
   Commission / MSCA COFUND" framing is wrong - MOVE-IN Louvain ended).
4. University Of Idaho Scholarships 2027 - VERIFIED as a family of
   tuition-reduction awards: Invitation to Idaho ~$16,000/yr (tuition
   $29,016 -> $13,294), #YouAreWelcomeHere 50% tuition, graduate
   assistantships departmental. Rolling, no single deadline.
5. HPI Scholarship Programs 2026 - SKIPPED: deadline passed
   15 Jul 2026 (EUR 500/month, first-year bachelor/master tracks).
6. EMBL European ARISE2 Postdoctoral Fellowships 2026 - SKIPPED:
   deadline passed 30 Sep 2026 23:59 CEST (17 fellowships, MSCA COFUND).
7. Cape Breton University Scholarships 2027 - VERIFIED as a family of
   partial entrance awards: Chancellor's $30,000, President's $20,000,
   Fitzgerald $20,000, Schwartz $14,000, W.M. Reid $11,500, Deans'
   $10,000 over 4 years; deadline 1 Mar 2027 (official page says
   "March 1st" without the year; 2027 per secondary sources).
8. Erasmus Mundus MARIHE Scholarship 2027 - SKIPPED: deadline passed
   21 Sep 2026 10:00 CEST (official marihe.eu: "closed"; next intake
   Sep 2028).
9. University of Warsaw Scholarships 2027 - SKIPPED: listicle, not a
   single scheme (10+ distinct schemes, deadline "Varies").
10. RMIT University Scholarships 2027 - SKIPPED: deadline passed
    (international EOI 30 Aug 2026, full application 30 Sep 2026);
    also a listicle of six distinct awards.
11. Erasmus Mundus Scholarships 2027 in Space, Physics and Material
    Engineering - SKIPPED: listicle (5 separate EMJM programmes).
12. SIDS Fellowship Programs 2027 in Ireland - SKIPPED: deadline
    passed (Stage 1 closed 26 Jul 2026; Stage 2 21 Sep-18 Oct 2026).
13. Griffith University Research Scholarships 2027 - SKIPPED:
    deadline passed 12 Oct 2026 (queue date; official page lists
    1 Sep 2026 / 5 Feb 2027 commencement closings instead).
14. IceLab Postdoc Scholarships 2027 - SKIPPED: deadline passed
    17 Sep 2026 21:59 UTC (SEK 720,000 over 2 years).
15. IEEE USA Government Fellowship Program 2027 - VERIFIED: deadline
    1 Jan 2027 (official IEEE-USA page, updated 13 Oct 2026); US
    citizens only; ~$100,000 total is aggregator-reported, not
    officially published.
16. Seoul National University President Fellowship 2027 - SKIPPED:
    deadline passed 9 Jul 2026 (Spring 2027 intake, 6-9 Jul 2026
    window); no verified Fall 2027 call.
17. University Technology Malaysia Scholarships 2027 - SKIPPED:
    deadline passed 31 Jul 2026 (international PG); research-mode
    admission window to 31 Oct 2026 is admission, not a scholarship.
18. KOICA Scholarship Program 2027 - SKIPPED: deadline passed
    31 Jul 2026 (some sources 29 Jun 2026).
19. Ultimate Guide to Fully Funded Scholarships 2027 - SKIPPED:
    listicle/guide, not a single scheme.
20. Helwan University Scholarships 2026 - SKIPPED: deadline passed
    15 Sep 2026 (Bright's 2026 date is a rollover of the official
    2025/26 call, 15 Sep 2025).
21. Australian Government Research Scholarship 2026-27 - VERIFIED as
    the Research Training Program (RTP): no central deadline, varies
    by university; next round Sydney 18 Dec 2026; official stipend
    range 2026 AUD 34,315-53,608 / 2027 base AUD 35,550.
22. University of Genova Scholarships 2027 - SKIPPED: deadline passed
    28 Aug 2026 (also a bundle of unrelated funding streams).
23. Two Fully Funded PhD Positions in HUGO Lab at the University of
    South Carolina - VERIFIED as a spare (Fall 2027: 1 May 2027
    international / 15 May 2027 domestic; fully funded, stipend
    amount not published; no official sc.edu page found - two
    aggregators agree exactly). NOT written this run; stays in the
    queue for the next run.
24. Lund University Postdoctoral Fellowship - SKIPPED: deadline
    passed 28 Jun 2026 (single named vacancy, ref PA2026/1959).

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 27)
def dl_left(ymd):
    y, m, d = map(int, ymd.split('-'))
    return (date(y, m, d) - TODAY).days

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
 'kpmg-gip-2026': {'mono': 'KP', 'title': 'KPMG Global Internship Program 2026 (Fully Funded)',
   'href': 'kpmg-global-internship-program-2026.html',
   'dpill': 'No fixed deadline · Rolling',
   'award': 'Fully funded 4-week international rotation: visa, return airfare, lodging and a placement allowance, plus a performance manager, a mentor and KPMG training. You must already hold a KPMG internship in your home country.',
   'elig': 'Undergraduate or recent graduate students who already hold a KPMG internship offer in their home country; prior practical experience is expected and valued.',
   'tags': [('Internship', 'blue'), ('Global', 'teal')]},
 'idaho-2027': {'mono': 'UI', 'title': 'University Of Idaho Scholarships 2027 in USA (Funded)',
   'href': 'university-of-idaho-scholarships-2027-usa.html',
   'dpill': 'Rolling · No single deadline',
   'award': 'Invitation to Idaho cuts international tuition from $29,016 to $13,294 a year (about $16,000 a year); #YouAreWelcomeHere covers 50% of tuition. Graduate assistantships add a waiver plus a stipend.',
   'elig': 'New international undergraduates with GPA 3.0+ (Invitation to Idaho, automatic on admission); first-year internationals for #YouAreWelcomeHere (essay or video).',
   'tags': [('Undergraduate to PhD', 'blue'), ('USA', 'teal')]},
 'cbu-2027': {'mono': 'CB', 'title': 'Cape Breton University Scholarships 2027 in Canada (Funded)',
   'href': 'cape-breton-university-scholarships-2027-canada.html',
   'dpill': 'Deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
   'award': 'Partial entrance awards: Chancellor’s $30,000, President’s $20,000 and Fitzgerald $20,000 over four years, plus awards of $500–$5,000 a year. Not fully funded.',
   'elig': 'Canadian and international students entering a full-time undergraduate programme with a high academic average and no failures in Grade 11/12 courses.',
   'tags': [('Undergraduate', 'blue'), ('Canada', 'teal')]},
 'ieee-gov-2027': {'mono': 'IE', 'title': 'IEEE USA Government Fellowship Program 2027 (Funding $100,000)',
   'href': 'ieee-usa-government-fellowship-program-2027.html',
   'dpill': 'Deadline 1 Jan 2027 · %d days left' % dl_left('2027-01-01'),
   'award': 'About $100,000 in total (aggregator-reported: ~$95,000 stipend + $5,000 relocation) for a year in Washington, D.C. — Capitol Hill, the State Department, or the Electric Grid Policy track.',
   'elig': 'U.S. citizens only, active IEEE members in good standing; PhD, or a Master’s plus 5+ years of relevant experience.',
   'tags': [('Fellowship', 'blue'), ('USA', 'teal')]},
 'rtp-2027': {'mono': 'AU', 'title': 'Australian Government Research Training Program (RTP) Scholarships 2027',
   'href': 'australian-government-research-training-program-rtp-2027.html',
   'dpill': 'Next round 18 Dec 2026 · %d days left' % dl_left('2026-12-18'),
   'award': 'Full tuition via the RTP Fees Offset plus a stipend: official 2026 range AUD 34,315–53,608; 2027 base AUD 35,550. Universities set the rate within that range.',
   'elig': 'Domestic or international students in a Master’s by Research or PhD at a participating Australian university, with an outstanding academic record and research experience.',
   'tags': [('Masters & PhD', 'blue'), ('Australia', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. KPMG Global Internship Program
A.append(dict(
 slug='kpmg-global-internship-program-2026',
 title='KPMG Global Internship Program 2026 (Fully Funded)',
 meta='KPMG Global Internship Program 2026: a fully funded 4-week international rotation for students who already hold a KPMG internship at home — visa, return airfare, lodging and a placement allowance covered. No fixed deadline; applications run per country.',
 short='KPMG Global Internship Program 2026', kicker='Global · Internship · Fully Funded', mono='KP',
 prov_short='KPMG', prov_cat='Professional Services · Global',
 h1='KPMG Global Internship Program 2026 (Fully Funded)',
 sub='Read this first, because the KPMG Global Internship Program is not a standalone internship you apply to from scratch — it is a four-week international rotation on top of a local KPMG internship you already hold. If you have accepted an internship with KPMG in your home country, the Global Internship Program can send you to another KPMG office abroad for four weeks, fully funded: visa expenses, return airfare, lodging and a placement allowance are covered, and you get a performance manager, a mentor and access to KPMG training. There is no fixed global deadline — each country runs its own timeline, so once you hold a local offer, check your local KPMG office and apply as soon as possible.',
 dpill='No fixed deadline · Rolling',
 facts=facts([('Award', 'Fully funded 4-week international rotation: visa expenses, return airfare, lodging/accommodation and a placement/mobility allowance are covered, plus a performance manager, a mentor and access to KPMG training. No cash stipend figure is published — do not expect a stated salary.'),
              ('Eligible', 'You must already have accepted/secured an internship offer with KPMG in your home country — the GIP is a rotation on top of that local internship. Undergraduate or recent graduate students; prior practical work experience is expected/valued (sources differ on whether it is required). Placements are in tax, audit and advisory; selection is competitive and interview-based.'),
              ('How', '1) Secure/accept a local KPMG internship in your home country. 2) Open the official KPMG Global Internship Program page and select your country. 3) Follow that country’s application process and contact the local KPMG recruiter if needed. 4) Submit the supporting documents your local office asks for.'),
              ('Deadline', 'No fixed global deadline — applications are accepted throughout the year and the timeline varies by country and region. Apply as soon as possible once you hold a local offer; check your local KPMG office for its dates.'),
              ('Fine print', 'The 14-country list circulating on aggregators (China, Canada, Germany, India, Italy, Ireland, Japan, Luxembourg, Norway, Sweden, South Africa, Singapore, USA, Vietnam) is an aggregator claim, not officially corroborated — the official page only requires a home-country KPMG internship. No IELTS/TOEFL requirement is published on the official page.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p><strong>KPMG</strong>, one of the world’s largest professional-services networks, runs the <strong>Global Internship Program (GIP)</strong> as a short international rotation for students who are already interning at a KPMG firm in their home country. It is not a way into KPMG — it is a way to spend <strong>four weeks</strong> working at a KPMG office in another country, in <strong>tax, audit or advisory</strong>, while keeping the internship you already have. That distinction matters: every credible source, including KPMG’s own page, says you must already hold a home-country internship before the GIP is even an option.</p>
      <p>The package is genuinely <strong>fully funded</strong> for those four weeks: <strong>visa expenses, return airfare, lodging/accommodation and a placement/mobility allowance</strong> are covered. You also get a <strong>performance manager and a mentor</strong>, plus access to KPMG training. What the programme does not publish is a cash stipend figure — no source states a monthly salary, so do not plan around one. Selection is <strong>competitive and interview-based</strong>, and the whole point of the rotation is the cross-border experience: working with a different team, in a different market, on real client work.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>You must already have <strong>accepted/secured an internship offer with KPMG in your home country</strong> — the GIP is a rotation on top of that local internship, confirmed by the official KPMG page and multiple aggregators.</li>
        <li>Be an <strong>undergraduate or recent graduate student</strong>.</li>
        <li>Have <strong>prior practical work experience</strong> — sources differ slightly on whether it is required or simply an advantage; treat it as expected and valued.</li>
        <li>Be open to a placement in <strong>tax, audit or advisory</strong>, and to a competitive, interview-based selection.</li>
        <li>Be able to travel internationally for <strong>four weeks</strong> on the rotation.</li>
        <li>Note: the 14-country list on some aggregators (China, Canada, Germany, India, Italy, Ireland, Japan, Luxembourg, Norway, Sweden, South Africa, Singapore, USA, Vietnam) is an <strong>aggregator claim, not officially corroborated</strong> — the official requirement is simply a home-country KPMG internship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Visa expenses</strong> covered.</li>
        <li><strong>Return airfare</strong> covered.</li>
        <li><strong>Lodging/accommodation</strong> covered.</li>
        <li><strong>Placement/mobility allowance</strong> covered.</li>
        <li>A <strong>performance manager and a mentor</strong> for the rotation.</li>
        <li>Access to <strong>KPMG training</strong> during the programme.</li>
        <li>Four weeks of <strong>international work experience</strong> in tax, audit or advisory at another KPMG office.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>valid passport</strong>.</li>
        <li>Your <strong>CV</strong>.</li>
        <li>A <strong>motivation letter/essay</strong>.</li>
        <li><strong>Reference/recommendation letter(s)</strong>.</li>
        <li>A <strong>photograph</strong>.</li>
        <li>Note: this document list comes from aggregators (edu-live, OpportunitiesCircle, OpportunitiesInfo agree) — it is <strong>not published on the official KPMG page</strong>. Your local KPMG office will confirm exactly what it wants.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Secure/accept a local KPMG internship</strong> in your home country first — without it, the GIP is not open to you.</li>
        <li>Visit the <strong>official KPMG Global Internship Program page</strong> and select your country.</li>
        <li>Follow that <strong>country’s application process</strong> — it varies by office; contact the local KPMG recruiter if you need guidance.</li>
        <li>Submit the <strong>supporting documents</strong> your local office asks for.</li>
        <li>Complete the <strong>interview/selection process</strong> — selection is competitive.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the KPMG Global Internship Program?',
  'A fully funded four-week international rotation for students who already hold a KPMG internship in their home country. You work for four weeks at a KPMG office abroad, in tax, audit or advisory, with visa, return airfare, lodging and a placement allowance covered.'),
 ('Do I need a KPMG internship first?',
  'Yes — this is the key requirement. The official KPMG page and multiple aggregators confirm you must already have accepted/secured an internship offer with KPMG in your home country. The GIP is a rotation on top of that local internship, not a standalone application.'),
 ('What is the deadline for the KPMG Global Internship Program 2026?',
  'There is no fixed global deadline. Applications are accepted throughout the year and the timeline varies by country and region — check your local KPMG office and apply as soon as possible once you hold a local offer.'),
 ('Is the KPMG Global Internship Program fully funded?',
  'Yes — visa expenses, return airfare, lodging/accommodation and a placement/mobility allowance are covered, plus a performance manager, a mentor and access to KPMG training. No cash stipend figure is published.'),
 ('Which countries can apply for the KPMG Global Internship Program?',
  'The official requirement is simply that you hold a home-country KPMG internship. A 14-country list (China, Canada, Germany, India, Italy, Ireland, Japan, Luxembourg, Norway, Sweden, South Africa, Singapore, USA, Vietnam) circulates on aggregators, but it is not officially corroborated — do not treat it as the official list.'),
 ('Is work experience required for the KPMG Global Internship Program?',
  'Sources differ: some say prior practical work experience is required, others that it is an advantage but not mandatory. Treat it as expected and valued — having it will strengthen your application.'),
 ('Is there an IELTS or TOEFL requirement?',
  'No IELTS/TOEFL requirement is published on the official KPMG page. Some aggregators state there is none, but that is aggregator-only — confirm with your local KPMG office.')]) + '''
      <p class="verify">Verified 27 Oct 2026: kpmg.com/eg/en/home/careers/graduates/global-internship-program.html (official KPMG GIP page, Egypt) and home.kpmg/xx/en/home/careers/graduates/global-internship-program.html (global GIP page) — the GIP is a 4-week international rotation on top of a home-country KPMG internship; applicants must already hold a local internship offer. Bright Scholarship (queue URL), OpportunitiesInfo, OpportunitiesPedia — no fixed global deadline ("no last date to apply; apply as soon as possible"; "applications accepted throughout the year"; "deadline varies by country and region"); fully funded (visa, return airfare, lodging, placement/mobility allowance, performance manager, mentor, KPMG training); placements in tax, audit and advisory; competitive, interview-based selection. Documents (valid passport, CV, motivation letter/essay, reference letter(s), photograph) are aggregator-sourced (edu-live, OpportunitiesCircle, OpportunitiesInfo) and not published on the official page. CONFLICTS: "work experience required" (Bright Scholarship/edu-live) vs "advantage but not mandatory" (OpportunitiesPedia) — unresolved; the article says experience is expected/valued. The 14-country list (edu-live) is an aggregator claim, not officially corroborated. No cash stipend amount is published anywhere — none is stated.</p>''',
 dl_long='No fixed deadline — rolling, varies by country and region',
 offlinks=[('KPMG — Global Internship Program (official)', 'https://kpmg.com/eg/en/home/careers/graduates/global-internship-program.html'),
           ('KPMG — Global Internship Program, global page (official)', 'https://home.kpmg/xx/en/home/careers/graduates/global-internship-program.html'),
           ('Bright Scholarship — KPMG Global Internship Program 2026', 'https://brightscholarship.com/kpmg-global-internship-program-2026/')],
 related_titles=['wto-internship-2027', 'un-ypp-2026', 'kaust-vsrp', 'gem-usa-2027'])),

# ---------------------------------------------------------------- 2. University of Idaho
A.append(dict(
 slug='university-of-idaho-scholarships-2027-usa',
 title='University Of Idaho Scholarships 2027 in USA (Funded)',
 meta='University of Idaho Scholarships 2027: Invitation to Idaho cuts international tuition from $29,016 to $13,294 a year (about $16,000 a year), and #YouAreWelcomeHere covers 50% of tuition. Both are rolling — no single deadline.',
 short='University of Idaho Scholarships 2027', kicker='USA · Undergraduate to PhD · Funded', mono='UI',
 prov_short='University of Idaho', prov_cat='University · USA',
 h1='University Of Idaho Scholarships 2027 in USA (Funded)',
 sub='Read this first, because “University of Idaho Scholarships 2027” is not one scholarship — it is a small family of tuition-reduction awards, and the two that matter most for international undergraduates are automatic or essay-based, with no single deadline. Invitation to Idaho is the big one: it cuts annual international tuition from $29,016 to $13,294 — worth almost $16,000 a year, about $64,000 over four years — and it is automatic on admission, with no separate form. The #YouAreWelcomeHere Scholarship covers 50% of tuition for first-year international undergraduates, through a separate essay or video application. Graduate students are funded differently again, through departmental teaching and research assistantships. None of these is a full ride — and any aggregator that calls the package “fully funded” is overstating it.',
 dpill='Rolling · No single deadline',
 facts=facts([('Award', 'Invitation to Idaho: worth almost $16,000 a year (about $64,000 over four years) — cuts annual international tuition from $29,016 to $13,294. Non-disbursable tuition reduction, renewable up to four years at a 2.5 cumulative U of I GPA. #YouAreWelcomeHere Scholarship: 50% of tuition, renewable up to four years, for first-year international undergraduates. Graduate assistantships (TA/RA): tuition waiver plus stipend — amounts vary by department and are not published centrally.'),
              ('Eligible', 'Invitation to Idaho: new undergraduate admitted as a first-year or first-time transfer, pursuing a first bachelor’s degree, enrolled 12–18 credits a semester full-time, incoming GPA 3.0 or higher, resident of a non-WUE state or an international student. #YouAreWelcomeHere: first-year international applicant to an undergraduate programme who attended/graduated from a secondary school outside the USA, with an interest in intercultural learning and exchange. Graduate funding: admitted graduate students; assistantships are awarded at department level.'),
              ('How', 'Apply for admission to the University of Idaho — Invitation to Idaho is automatic on admission, with no separate form. For #YouAreWelcomeHere, submit the separate 500–1,000-word essay or 2–5-minute video application through the International Programs Office. For graduate funding, apply to the department and ask about TA/RA openings.'),
              ('Deadline', 'Rolling — no single 2027 deadline is published. Invitation to Idaho has no separate application or deadline. Graduate admission priority deadline for Fall is 15 January (international); international applications for Fall admission must reach Graduate Admissions by 1 May. #YouAreWelcomeHere has priority deadlines per term, but no exact 2027 date was found — treat as not published.'),
              ('Fine print', 'Invitation to Idaho cannot be combined with #YouAreWelcomeHere or WUE. Aggregator claims of a “partial to fully funded” package with a monthly stipend of USD 800–1,500, accommodation, airfare, health insurance and visa-fee reimbursement are not corroborated by uidaho.edu — these awards are tuition reductions, not full funding. The “Global Vandal Scholarship” appears only on Collegedunia, not on uidaho.edu pages checked. Collegedunia’s “1 February 2027” graduate date is the SFS cybersecurity programme only, not a general graduate deadline.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of Idaho</strong> in Moscow, Idaho, funds international students through <strong>tuition reductions</strong>, not cash scholarships — and that is the most important thing to understand before applying. The headline award is <strong>Invitation to Idaho</strong>: a non-disbursable tuition reduction worth almost <strong>$16,000 a year</strong> (about <strong>$64,000 over four years</strong>), which cuts annual international tuition from <strong>$29,016 to $13,294</strong>. It is renewable for up to four years if you keep a <strong>2.5 cumulative U of I GPA</strong>, and — crucially — it is <strong>automatic on admission</strong>: there is no separate application and no separate deadline.</p>
      <p>The second award is the <strong>#YouAreWelcomeHere Scholarship</strong>: <strong>50% of tuition</strong>, renewable up to four years, for first-year international undergraduates. Unlike Invitation to Idaho, it needs a separate application — a <strong>500–1,000-word essay or a 2–5-minute video</strong> on leadership and promoting intercultural learning, submitted through the International Programs Office. You cannot combine the two: Invitation to Idaho cannot be held with #YouAreWelcomeHere or with WUE. Graduate students are funded through a different route entirely — <strong>departmental teaching and research assistantships</strong> that carry a tuition waiver plus a stipend, with amounts set by each department and not published centrally.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>For <strong>Invitation to Idaho</strong>: be a <strong>new undergraduate</strong> admitted as a first-year or first-time transfer, pursuing your <strong>first bachelor’s degree</strong>, enrolled <strong>12–18 credits a semester</strong> full-time, with an <strong>incoming GPA of 3.0 or higher</strong>, and be a resident of a non-WUE state or an international student.</li>
        <li>For <strong>#YouAreWelcomeHere</strong>: be a <strong>first-year international applicant</strong> to an undergraduate programme who <strong>attended/graduated from a secondary school outside the USA</strong>, with an interest in intercultural learning and exchange.</li>
        <li>For <strong>graduate funding</strong>: be an <strong>admitted graduate student</strong>; assistantships are administered at department level, not as a central scholarship.</li>
        <li>Keep a <strong>2.5 cumulative U of I GPA</strong> to renew Invitation to Idaho for up to four years.</li>
        <li>Note: Invitation to Idaho <strong>cannot be combined</strong> with #YouAreWelcomeHere or WUE — pick the award that fits you.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Invitation to Idaho:</strong> almost <strong>$16,000 a year</strong> (about $64,000 over four years) — international tuition falls from <strong>$29,016 to $13,294 a year</strong>. Non-disbursable tuition reduction, renewable up to four years at a 2.5 GPA.</li>
        <li><strong>#YouAreWelcomeHere Scholarship:</strong> <strong>50% of tuition</strong>, renewable up to four years, for first-year international undergraduates.</li>
        <li><strong>Graduate assistantships (TA/RA):</strong> a <strong>tuition waiver plus a stipend</strong>, awarded by departments — amounts vary and are not published centrally.</li>
        <li><strong>No separate scholarship form</strong> for Invitation to Idaho — it is automatic on admission.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>For <strong>Invitation to Idaho</strong>: nothing beyond the <strong>admission application</strong> — no separate documents.</li>
        <li>For <strong>#YouAreWelcomeHere</strong>: a <strong>500–1,000-word essay OR a 2–5-minute video</strong> on leadership and promoting intercultural learning.</li>
        <li>For <strong>graduate funding</strong>: the <strong>admission application</strong> plus department requirements; transcripts and recommendation letters per Bright only (not independently confirmed — check the department page).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to the University of Idaho — Invitation to Idaho is automatic on admission, with no separate form.</li>
        <li>For <strong>#YouAreWelcomeHere</strong>, submit the separate <strong>essay or video application</strong> through the International Programs Office.</li>
        <li>For <strong>graduate funding</strong>, apply to the department and ask about <strong>TA/RA openings</strong> — assistantships are awarded at department level.</li>
        <li>Watch the graduate deadlines: the <strong>Fall priority deadline is 15 January</strong> (international), and international applications for Fall admission must reach Graduate Admissions by <strong>1 May</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for University of Idaho Scholarships 2027?',
  'There is no single deadline — the awards are rolling. Invitation to Idaho has no separate application or deadline at all. For graduate admission, the Fall priority deadline is 15 January (international) and international applications must reach Graduate Admissions by 1 May.'),
 ('Is the University of Idaho scholarship fully funded?',
  'No. These are tuition reductions, not full funding. Invitation to Idaho cuts tuition from $29,016 to $13,294 a year, and #YouAreWelcomeHere covers 50% of tuition. Aggregator claims of a monthly stipend of USD 800–1,500, accommodation, airfare and health insurance are not corroborated by uidaho.edu.'),
 ('How much is the Invitation to Idaho scholarship worth?',
  'Almost $16,000 a year — about $64,000 over four years. It is a non-disbursable tuition reduction, renewable up to four years if you keep a 2.5 cumulative U of I GPA.'),
 ('Do I need a separate application for University of Idaho scholarships?',
  'Not for Invitation to Idaho — it is automatic on admission. #YouAreWelcomeHere needs a separate essay (500–1,000 words) or video (2–5 minutes) through the International Programs Office. Graduate assistantships are applied for through the department.'),
 ('Can I combine Invitation to Idaho with other scholarships?',
  'No — Invitation to Idaho cannot be combined with #YouAreWelcomeHere or WUE.'),
 ('What is the #YouAreWelcomeHere Scholarship at the University of Idaho?',
  'A 50%-of-tuition scholarship, renewable up to four years, for first-year international undergraduates who attended or graduated from a secondary school outside the USA and have an interest in intercultural learning and exchange.'),
 ('What GPA do I need for University of Idaho scholarships?',
  'Invitation to Idaho requires an incoming GPA of 3.0 or higher, and a 2.5 cumulative U of I GPA to renew it.')]) + '''
      <p class="verify">Verified 27 Oct 2026: uidaho.edu/financial-aid/scholarships/international-scholarship (official) and uidaho.edu/financial-aid/scholarships/out-of-state-scholarship (official) — Invitation to Idaho worth almost $16,000/year (~$64,000 over 4 years), cuts annual international tuition from $29,016 to $13,294, non-disbursable tuition reduction renewable up to 4 years at 2.5 cumulative U of I GPA, cannot combine with #YouAreWelcomeHere or WUE; incoming GPA 3.0+, new undergraduate first-year/first-time transfer, first bachelor's degree, 12-18 credits/semester full-time, non-WUE resident or international. catalog.uidaho.edu/student-services/admission/ (official) — graduate admission priority deadline for Fall 15 January (international); international applications for Fall admission must reach Graduate Admissions by 1 May. IDP #YouAreWelcomeHere page — 50% of tuition, renewable up to 4 years, first-year international undergraduates, secondary school outside the USA, intercultural learning interest. Bright Scholarship (queue URL), AfroCareer, IDP — #YouAreWelcomeHere essay 500-1,000 words or video 2-5 minutes on leadership and intercultural learning. CONFLICTS: Bright/abgram claim "partial to fully funded", monthly stipend USD 800-1,500, accommodation, return airfare, health insurance, visa-fee reimbursement — none corroborated by uidaho.edu; the article presents the awards as tuition reductions. Collegedunia's "apply by 1 February 2027" is the SFS cybersecurity programme only, not a general graduate deadline. "Global Vandal Scholarship" appears only on Collegedunia — not on uidaho.edu pages checked, omitted. #YouAreWelcomeHere has priority deadlines per term but no exact 2027 date was found on any source — stated as not published.</p>''',
 dl_long='Rolling — no single deadline (graduate Fall priority 15 January; international graduate applications by 1 May)',
 offlinks=[('University of Idaho — International Scholarships (official)', 'https://www.uidaho.edu/financial-aid/scholarships/international-scholarship'),
           ('University of Idaho — Out-of-State Scholarships, Invitation to Idaho (official)', 'https://www.uidaho.edu/financial-aid/scholarships/out-of-state-scholarship'),
           ('University of Idaho — Graduate Admission Deadlines (official catalogue)', 'https://catalog.uidaho.edu/student-services/admission/'),
           ('Bright Scholarship — University of Idaho Scholarships 2027', 'https://brightscholarship.com/the-university-of-idaho-scholarships-2027/')],
 related_titles=['fsu-2027', 'alabama-2027', 'msu-oos', 'dayton-merit'])),

# ---------------------------------------------------------------- 3. Cape Breton University
A.append(dict(
 slug='cape-breton-university-scholarships-2027-canada',
 title='Cape Breton University Scholarships 2027 in Canada (Funded)',
 meta='Cape Breton University Scholarships 2027: partial entrance awards from $500 to $30,000 over four years — Chancellor’s $30,000, President’s $20,000 and Fitzgerald $20,000 lead the list. Accepted students can apply until 1 March 2027.',
 short='Cape Breton University Scholarships 2027', kicker='Canada · Undergraduate · Funded', mono='CB',
 prov_short='Cape Breton University', prov_cat='University · Canada',
 h1='Cape Breton University Scholarships 2027 in Canada (Funded)',
 sub='Read this first, because the Cape Breton University Scholarships 2027 are partial entrance awards, not a full ride — and the official page says so plainly. The biggest award, the Chancellor’s Scholarship, is $30,000 over four years ($7,500 a year), and even that covers roughly a third of CBU’s international tuition, which averages about CAD 23,794 a year. What the awards do offer is real money for strong school results: the Chancellor’s ($30,000), President’s ($20,000) and Fitzgerald ($20,000) lead a ladder of entrance scholarships down to $500 a year, for Canadian and international students entering a full-time undergraduate programme. Accepted students can apply for entrance scholarships until 1 March 2027.',
 dpill='Deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
 facts=facts([('Award', 'Partial entrance scholarships only — NOT fully funded. Major awards (CAD, total over four years): Chancellor’s $30,000 ($7,500 a year); President’s $20,000 ($5,000 a year); Fitzgerald $20,000 ($5,000 a year); Schwartz $14,000 ($3,500 a year); W.M. Reid $11,500; Deans’ $10,000 ($2,500 a year). Other entrance awards run $500–$5,000 a year. For scale, CBU international tuition averages about CAD 23,794 a year, so even the Chancellor’s covers roughly a third of tuition.'),
              ('Eligible', 'Canadian and international students entering a full-time undergraduate programme. A high academic average with no failures in Grade 11/12 courses; the average is based on Grade 11 courses and completed Grade 12 courses, and CBU determines the average for international students entering directly from high school. ESL conditional-offer students must attend a CBU English language partner school for the award to stand. Articulation/transfer students are also eligible.'),
              ('How', '1) Apply for admission to a full-time undergraduate programme through a CBU Future Student account. 2) Submit the official transcript with the admission application. 3) Accepted students can apply for entrance scholarships until 1 March. 4) Bursary applicants additionally complete the Entrance Bursary Form (available January, closes March) with income-tax documentation.'),
              ('Deadline', '1 March 2027 for the September 2027 intake. The official CBU page states “Accepted students can apply for Entrance Scholarships until March 1st” without naming the year; 1 March 2027 is the date given by Collegedunia and Sagblog. Bright Scholarship’s “no deadline” claim is wrong.'),
              ('Fine print', 'The widely quoted 80% minimum average appears in several aggregators but is not stated on CBU’s own page — do not treat it as an official cut-off. The Orpha Thayer-Scott Scholarship ($10,000) appears in some aggregator tables but not in the major-awards table on the official page. Direct-entry applicants are described by Collegedunia as automatically ranked with no separate form — that is an aggregator-only claim; the official page says the transcript must be submitted in addition to an admission application.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Cape Breton University (CBU)</strong> in Sydney, Nova Scotia, awards its entrance scholarships on <strong>academic merit</strong> to students entering a full-time undergraduate programme — Canadian and international alike. The awards are <strong>partial</strong>: they reduce tuition, they do not cover it. The ladder is led by the <strong>Chancellor’s Scholarship ($30,000 over four years, $7,500 a year)</strong>, followed by the <strong>President’s ($20,000)</strong> and <strong>Fitzgerald ($20,000)</strong> scholarships, then the <strong>Schwartz ($14,000)</strong>, <strong>W.M. Reid ($11,500)</strong> and <strong>Deans’ ($10,000)</strong> awards, with other entrance awards running <strong>$500–$5,000 a year</strong>. Against CBU international tuition of about <strong>CAD 23,794 a year</strong>, even the Chancellor’s covers roughly a third of tuition — so treat these as meaningful help, not a full ride.</p>
      <p>The official CBU page is the authority here, and it is careful about what it does and does not say. It states the awards, the <strong>March 1st</strong> deadline for accepted students, and the eligibility rules — but it does <strong>not</strong> name the year, and it does <strong>not</strong> state a percentage cut-off. The “1 March 2027” date and the “80% minimum average” you will see on aggregator pages are secondary claims: the date is consistent and corroborated, the 80% figure is not on the official page at all. This article uses the official page wherever the two disagree.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>Canadian or international student</strong> entering a <strong>full-time undergraduate programme</strong> at CBU.</li>
        <li>Have a <strong>high academic average</strong>, with <strong>no failures in Grade 11/12 courses</strong>.</li>
        <li>Your average is based on <strong>Grade 11 courses and completed Grade 12 courses</strong>; CBU determines the average for international students entering directly from high school.</li>
        <li>If you hold an <strong>ESL conditional offer</strong>, you must attend a <strong>CBU English language partner school</strong> for the award to stand.</li>
        <li><strong>Articulation/transfer students</strong> are also eligible.</li>
        <li>Note: the widely quoted <strong>80% minimum average</strong> is aggregator-only — it is <strong>not stated on CBU’s own page</strong> and is not presented here as an official cut-off.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Chancellor’s Scholarship:</strong> <strong>$30,000</strong> over four years ($7,500 a year).</li>
        <li><strong>President’s Scholarship:</strong> <strong>$20,000</strong> over four years ($5,000 a year).</li>
        <li><strong>Fitzgerald Scholarship:</strong> <strong>$20,000</strong> over four years ($5,000 a year).</li>
        <li><strong>Schwartz Scholarship:</strong> <strong>$14,000</strong> over four years ($3,500 a year).</li>
        <li><strong>W.M. Reid Scholarship:</strong> <strong>$11,500</strong>.</li>
        <li><strong>Deans’ Scholarship:</strong> <strong>$10,000</strong> over four years ($2,500 a year).</li>
        <li><strong>Other entrance awards:</strong> <strong>$500–$5,000 a year</strong>.</li>
        <li><strong>Bursaries</strong> are available separately for students with demonstrated financial need (Entrance Bursary Form, January–March).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>official transcript</strong> — submitted with the admission application (scholarship-specific, per the official page).</li>
        <li>For <strong>bursary applicants only</strong>: the <strong>Entrance Bursary Form</strong> plus <strong>income-tax documentation</strong>.</li>
        <li>A <strong>personal statement, CV, passport copy and English-proficiency proof</strong> are admission documents per aggregators — they are <strong>not confirmed as separate scholarship requirements</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to a full-time undergraduate programme through a <strong>CBU Future Student account</strong> (online).</li>
        <li>Submit your <strong>official transcript</strong> with the admission application.</li>
        <li>Once accepted, apply for <strong>entrance scholarships until 1 March</strong>.</li>
        <li>For <strong>bursaries</strong>, additionally complete the <strong>Entrance Bursary Form</strong> (available January, closes March) with income-tax documentation.</li>
        <li>Questions: contact the awards office at <strong>awards@cbu.ca</strong> (listed on the official page).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for Cape Breton University Scholarships 2027?',
  '1 March 2027 for the September 2027 intake. The official CBU page states “Accepted students can apply for Entrance Scholarships until March 1st” without naming the year; 1 March 2027 is the date given by Collegedunia and Sagblog.'),
 ('Are Cape Breton University scholarships fully funded?',
  'No — they are partial entrance awards. The largest, the Chancellor’s Scholarship, is $30,000 over four years, against international tuition of about CAD 23,794 a year. The “(Funded)” label in the queue title overstates this.'),
 ('How much is the Cape Breton University Chancellor’s Scholarship?',
  '$30,000 in total over four years ($7,500 a year). The President’s and Fitzgerald scholarships are $20,000 each over four years; Schwartz is $14,000; W.M. Reid is $11,500; Deans’ is $10,000.'),
 ('Do I need an 80% average for CBU scholarships?',
  'The 80% figure appears in several aggregators but is not stated on CBU’s own page, so it is not presented here as an official cut-off. The official requirement is a high academic average with no failures in Grade 11/12 courses.'),
 ('Do international students get Cape Breton University scholarships?',
  'Yes — Canadian and international students entering a full-time undergraduate programme are eligible. CBU determines the average for international students entering directly from high school.'),
 ('Is there a separate application for CBU entrance scholarships?',
  'Collegedunia states direct-entry applicants are automatically ranked with no separate form, but that is an aggregator-only claim. The official page says the transcript must be submitted in addition to an admission application, and accepted students can apply for entrance scholarships until 1 March.'),
 ('Does CBU offer bursaries as well as scholarships?',
  'Yes — bursary applicants complete the Entrance Bursary Form (available January, closes March) with income-tax documentation, in addition to the admission application.')]) + '''
      <p class="verify">Verified 27 Oct 2026: cbu.ca/future-students/scholarships-bursaries/ (official CBU page) — entrance scholarships for Canadian and international students entering a full-time undergraduate programme; major awards (CAD, total over 4 years) Chancellor's $30,000, President's $20,000, Fitzgerald $20,000, Schwartz $14,000, W.M. Reid $11,500, Deans' $10,000, plus other entrance awards $500-$5,000/year; "Accepted students can apply for Entrance Scholarships until March 1st" (year not stated on the page); high academic average, no failures in Grade 11/12 courses, average based on Grade 11 courses and completed Grade 12 courses, CBU determines the average for international students entering directly from high school; ESL conditional-offer students must attend a CBU English language partner school; official transcript submitted with the admission application; Entrance Bursary Form available January, closes March, with income-tax documentation; contact awards@cbu.ca. Collegedunia and Sagblog (checked against the official page 17 Oct 2026) give 1 March 2027 for the September 2027 intake. CBU international tuition averages ~CAD 23,794/year (aggregators). CONFLICTS: Bright Scholarship and several clones say "No deadline / No Fixed Deadline" — wrong; the official March 1st date wins. The widely quoted 80% minimum average appears in aggregators (ehsaskafaalat, grabscholarships, myexamportal) but is not on the official page — not published as an official cut-off. The Orpha Thayer-Scott Scholarship ($10,000) appears in some aggregator tables but not in the major-awards table on the official page — not listed as a major award. Collegedunia's "automatically ranked, no separate form" is aggregator-only. The queue title's "(Funded)" overstates partial awards.</p>''',
 dl_long='1 March 2027 (September 2027 intake; official page states “March 1st” without the year)',
 offlinks=[('Cape Breton University — Scholarships & Bursaries (official)', 'https://www.cbu.ca/future-students/scholarships-bursaries/'),
           ('Bright Scholarship — Cape Breton University Scholarships 2027', 'https://brightscholarship.com/cape-breton-university-scholarships-2027/')],
 related_titles=['canada-noielts', 'ucalgary-2027', 'ubc-2027', 'trent-2027'])),

# ---------------------------------------------------------------- 4. IEEE-USA Government Fellowship
A.append(dict(
 slug='ieee-usa-government-fellowship-program-2027',
 title='IEEE USA Government Fellowship Program 2027 (Funding $100,000)',
 meta='IEEE-USA Government Fellowship Program 2027: a year in Washington, D.C. on Capitol Hill or at the State Department for U.S.-citizen IEEE members. Deadline 1 January 2027; finalists are interviewed in person 9–10 February 2027.',
 short='IEEE-USA Government Fellowship 2027', kicker='USA · Fellowship · $100,000', mono='IE',
 prov_short='IEEE-USA', prov_cat='Professional Association · USA',
 h1='IEEE USA Government Fellowship Program 2027 (Funding $100,000)',
 sub='The IEEE-USA Government Fellowship Program puts engineers and technologists inside American government for a year — on Capitol Hill, at the U.S. Department of State, or on the Electric Grid Policy track — and the 2027–28 cycle is open now, with applications closing 1 January 2027. Two things to get straight before you apply. First, this fellowship is for U.S. citizens only: the official IEEE-USA page states that explicitly, and aggregator pages calling it “for international students” are wrong. Second, the $100,000 figure in the title is aggregator-reported — roughly a $95,000 stipend plus a $5,000 relocation allowance — and is not confirmed on the official IEEE-USA page, so treat it as reported, not officially published. The fellowship year runs 1 September 2027 to 31 August 2028, and finalists are interviewed in person in Washington, D.C. on 9–10 February 2027.',
 dpill='Deadline 1 Jan 2027 · %d days left' % dl_left('2027-01-01'),
 facts=facts([('Award', 'About $100,000 in total, per aggregators — roughly a $95,000 stipend plus a $5,000 relocation allowance. This figure is NOT confirmed on the official IEEE-USA page, so treat it as aggregator-reported. Three tracks: Congressional Fellowship (Capitol Hill), Engineering & Diplomacy Fellowship (U.S. Department of State) and Congressional Electric Grid Policy Fellowship. Fellowship year: 1 September 2027 – 31 August 2028.'),
              ('Eligible', 'U.S. citizen — mandatory, stated explicitly on the official page. Active IEEE member in good standing (graduate student members are eligible); the Electric Grid Policy track does not require membership at the application stage but requires joining if selected. A PhD, or a Master’s degree plus at least five years of full-time relevant professional experience (aggregator-sourced). Strong science, engineering or technology background, excellent written and verbal communication, demonstrated interest in public policy. Must be able to relocate to Washington, D.C. for the full year.'),
              ('How', 'Apply directly to IEEE-USA through the “Apply Online” links on the official fellowships page — do not apply via AAAS. Finalists are interviewed in person in Washington, D.C. on 9–10 February 2027 (interviews cannot be rescheduled).'),
              ('Deadline', '1 January 2027 for the 2027–28 Congressional Fellowships (official IEEE-USA page, updated 13 October 2026). Two aggregators give 8 January 2027 — use the official 1 January date. One aggregator page listing 31 July 2026 is stale and wrong.'),
              ('Fine print', 'Bright Scholarship’s description of this fellowship as “for international students” with “deadline not specified” is wrong on both counts — the official page restricts it to U.S. citizens and states the deadline. The $100,000 figure is aggregator-reported, not officially published.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p><strong>IEEE-USA</strong>, the U.S. arm of the world’s largest technical professional organisation, runs its <strong>Government Fellowship Program</strong> to place engineers and technologists inside the federal government for a year. There are three tracks: the <strong>Congressional Fellowship</strong>, working on Capitol Hill; the <strong>Engineering &amp; Diplomacy Fellowship</strong>, at the U.S. Department of State; and the <strong>Congressional Electric Grid Policy Fellowship</strong>, focused on grid policy. Fellows spend the year advising on legislation and policy, bringing a technical perspective to decisions that are usually made without one — and the experience routinely shapes careers in public policy, industry and academia.</p>
      <p>The <strong>2027–28 fellowship year runs 1 September 2027 to 31 August 2028</strong>, and the application deadline is <strong>1 January 2027</strong>, per the official IEEE-USA page (updated 13 October 2026). The award is reported by aggregators at about <strong>$100,000 in total</strong> — roughly a $95,000 stipend plus a $5,000 relocation allowance — but that figure does <strong>not</strong> appear on the official IEEE-USA page, so this article presents it as aggregator-reported. Finalists are interviewed <strong>in person in Washington, D.C. on 9–10 February 2027</strong>, and those dates cannot be rescheduled.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>U.S. citizen</strong> — mandatory, stated explicitly on the official page. This fellowship is <strong>not</strong> open to international applicants.</li>
        <li>Be an <strong>active IEEE member in good standing</strong> (graduate student members are eligible). The <strong>Electric Grid Policy track</strong> does not require membership at the application stage but requires joining if selected.</li>
        <li>Hold a <strong>PhD</strong>, or a <strong>Master’s degree plus at least five years of full-time relevant professional experience</strong> (aggregator-sourced; not stated on the official page section read).</li>
        <li>Have a <strong>strong science, engineering or technology background</strong>, excellent written and verbal communication, and a demonstrated interest in public policy.</li>
        <li>Be able to <strong>relocate to Washington, D.C. for the full year</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>About <strong>$100,000 in total</strong> (aggregator-reported: ~$95,000 stipend + $5,000 relocation allowance) — not confirmed on the official page.</li>
        <li>A year working on <strong>Capitol Hill</strong> (Congressional Fellowship), at the <strong>U.S. Department of State</strong> (Engineering &amp; Diplomacy Fellowship), or on <strong>Electric Grid Policy</strong>.</li>
        <li>Direct experience of <strong>legislation and policy-making</strong> from inside government.</li>
        <li>Fellowship year: <strong>1 September 2027 – 31 August 2028</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>letter of intent</strong>.</li>
        <li>A <strong>personal/technical resume</strong>.</li>
        <li><strong>Three letters of reference</strong>.</li>
        <li>Note: this document list is aggregator-sourced — confirm the exact requirements on the official fellowships page when you apply.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the <strong>official IEEE-USA fellowships page</strong> and choose your track (Congressional, Engineering &amp; Diplomacy, or Electric Grid Policy).</li>
        <li>Apply directly to IEEE-USA through the <strong>“Apply Online” links</strong> on that page — <strong>do not apply via AAAS</strong>.</li>
        <li>Submit your <strong>letter of intent, resume and three letters of reference</strong> by <strong>1 January 2027</strong>.</li>
        <li>If selected as a finalist, attend the <strong>in-person interview in Washington, D.C. on 9–10 February 2027</strong> — interviews cannot be rescheduled.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the IEEE-USA Government Fellowship 2027?',
  '1 January 2027 for the 2027–28 fellowships, per the official IEEE-USA page (updated 13 October 2026). Two aggregators give 8 January 2027 — use the official 1 January date.'),
 ('How much is the IEEE-USA Government Fellowship worth?',
  'About $100,000 in total — roughly a $95,000 stipend plus a $5,000 relocation allowance — according to aggregators. The figure is not confirmed on the official IEEE-USA page, so treat it as aggregator-reported.'),
 ('Can international students apply for the IEEE-USA Government Fellowship?',
  'No. U.S. citizenship is mandatory and is stated explicitly on the official page. Aggregator pages calling it “for international students” are wrong.'),
 ('Do I need to be an IEEE member to apply?',
  'Yes — you must be an active IEEE member in good standing (graduate student members are eligible). The Electric Grid Policy track is the exception: it does not require membership at the application stage, but you must join if selected.'),
 ('What are the three IEEE-USA Government Fellowship tracks?',
  'The Congressional Fellowship (Capitol Hill), the Engineering & Diplomacy Fellowship (U.S. Department of State), and the Congressional Electric Grid Policy Fellowship.'),
 ('How do I apply for the IEEE-USA Government Fellowship?',
  'Apply directly to IEEE-USA through the “Apply Online” links on the official fellowships page — do not apply via AAAS. Finalists are interviewed in person in Washington, D.C. on 9–10 February 2027.'),
 ('When does the IEEE-USA Government Fellowship year run?',
  '1 September 2027 to 31 August 2028.')]) + '''
      <p class="verify">Verified 27 Oct 2026: ieeeusa.org/public-policy/government-fellowships/ (official IEEE-USA page, updated 13 Oct 2026) — "The Deadline for 2027-2028 Congressional Fellowships is 1 January 2027"; U.S. citizenship mandatory, stated explicitly; active IEEE member in good standing; three tracks (Congressional Fellowship, Engineering &amp; Diplomacy Fellowship, Congressional Electric Grid Policy Fellowship); apply directly to IEEE-USA via the "Apply Online" links (do NOT apply via AAAS); finalists interviewed in person in Washington, D.C. on 9-10 February 2027 (interviews cannot be rescheduled); fellowship year 1 September 2027 - 31 August 2028. Aggregators (kaistscholarship.com, Bright Scholarship) — ~$95,000 stipend + $5,000 relocation allowance (~$100,000 total); PhD, or Master's plus at least 5 years of full-time relevant professional experience; letter of intent, personal/technical resume, three letters of reference; Electric Grid Policy track does not require membership at application stage but requires joining if selected. CONFLICTS: official page says 1 January 2027; gradualin.com and engineersjob.in say 8 January 2027 (12:00 PM ET) — the official date is used. One engineersjob.in page lists "31 July 2026" — stale/wrong, contradicted by the official page. Bright Scholarship says the fellowship is "for international students" and "deadline not specified" — both wrong. The $100,000 figure is NOT on the official page and is presented as aggregator-reported.</p>''',
 dl_long='1 January 2027 (2027–28 fellowships; interviews 9–10 February 2027)',
 offlinks=[('IEEE-USA — Government Fellowships (official)', 'https://ieeeusa.org/public-policy/government-fellowships/'),
           ('Bright Scholarship — IEEE USA Government Fellowship Program 2027', 'https://brightscholarship.com/ieee-usa-government-fellowship-program-2027/')],
 related_titles=['gem-usa-2027', 'nyt-fellowship', 'faspe-2027', 'jefferson-2027'])),

# ---------------------------------------------------------------- 5. Australian Government RTP
A.append(dict(
 slug='australian-government-research-training-program-rtp-2027',
 title='Australian Government Research Training Program (RTP) Scholarships 2027',
 meta='Australian Government Research Training Program (RTP) 2027: a federal block grant that pays full tuition plus a stipend of AUD 34,315–53,608 (2026 rates; 2027 base AUD 35,550). There is no central deadline — each university runs its own round; the next is Sydney, 18 December 2026.',
 short='Australian Government RTP Scholarships 2027', kicker='Australia · Masters & PhD · Fully Funded', mono='AU',
 prov_short='Australian Government', prov_cat='Government · Australia',
 h1='Australian Government Research Training Program (RTP) Scholarships 2027',
 sub='First, the name: the scheme in the queue is called the “Australian Government Research Scholarship”, but that is not its real name. The real scheme is the Research Training Program (RTP) — a federal block grant that the Australian Government pays to universities, which then award it to research students as a full tuition offset plus a living stipend. Second, there is no single RTP deadline and no central application: you apply to a university, not to the government, and each university runs its own round on its own dates. The official stipend range for 2026 is AUD 34,315 to AUD 53,608 (2027 base: AUD 35,550), with universities setting the rate inside that range — Sydney pays AUD 42,754 a year (2026), ANU AUD 39,069. The next open round is the University of Sydney’s, closing 18 December 2026.',
 dpill='Next round 18 Dec 2026 · %d days left' % dl_left('2026-12-18'),
 facts=facts([('Award', 'RTP Fees Offset covers full tuition, plus a stipend and allowances (relocation, thesis; Overseas Student Health Cover for internationals). Official stipend range: 2026 base AUD 34,315 / maximum AUD 53,608; 2027 base AUD 35,550 / maximum AUD 55,537 — universities set the rate within that range. Sydney pays AUD 42,754 a year (2026) / AUD 44,293 (2027); ANU AUD 39,069 a year. Duration: Master’s by research up to 2 years, PhD up to 4 years.'),
              ('Eligible', 'Domestic or international student enrolled in or commencing a Higher Degree by Research (Master’s by Research or PhD) at a participating Australian university. An outstanding academic record and previous research experience; the equivalent of an Australian Honours degree; meets the university’s English-language requirements.'),
              ('How', '1) Choose a participating university and secure/identify a supervisor (required at some universities). 2) Apply for HDR admission through that university’s portal. 3) Submit that university’s scholarship/RTP form by its own deadline (Sydney: separate RTP form; ANU: tick the scholarship in the admission application — no separate form). 4) No application goes to the Department of Education — there is no central portal.'),
              ('Deadline', 'No central deadline — it varies by university. Next open rounds: University of Sydney Research Periods 3 & 4, 2027 — 18 December 2026; Southern Cross University — 31 October 2026; Central Queensland University — 31 December 2026; ANU Round 2 — 15 April 2027. Already closed: Sydney RP 1 & 2, 2027 (11 September 2026) and ANU Round 1.'),
              ('Fine print', 'The queue title’s “Australian Government Research Scholarship” is not the scheme’s real name — the real name is the Research Training Program (RTP). One aggregator’s flat “AUD 52,352 stipend” is the official 2025 maximum rate mislabelled as the standard stipend — do not use it. Bright’s “AUD 1,000 travel from home country to/from Adelaide” is Adelaide-specific, not a general RTP benefit. The Sydney 18 December 2026 date is aggregator-corroborated; the official Sydney page’s timeline table did not render in the fetch.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Research Training Program (RTP)</strong> is how the Australian Government funds research degrees. It is not a scholarship you apply to directly: the Government gives <strong>block grants to universities</strong>, and each university awards RTP places to its own research students. An RTP award has two parts — an <strong>RTP Fees Offset</strong>, which covers full tuition, and an <strong>RTP Stipend</strong>, a living allowance paid while you study. Some universities also add allowances for relocation, thesis costs and, for international students, Overseas Student Health Cover. A Master’s by research is funded for up to <strong>2 years</strong>; a PhD for up to <strong>4 years</strong>.</p>
      <p>How much you actually receive depends on your university, because the Government publishes a <strong>range</strong>, not a single figure: for 2026 the base rate is <strong>AUD 34,315</strong> and the maximum is <strong>AUD 53,608</strong>; for 2027 the base is <strong>AUD 35,550</strong> and the maximum <strong>AUD 55,537</strong>. The University of Sydney pays <strong>AUD 42,754 a year</strong> (2026 rate, AUD 44,293 in 2027); ANU pays <strong>AUD 39,069 a year</strong>. Any page quoting one flat “RTP stipend” for the whole country is simplifying — and one aggregator’s flat “AUD 52,352” is simply the official 2025 maximum rate, mislabelled as the standard stipend.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>domestic or international student</strong> enrolled in, or commencing, a <strong>Higher Degree by Research</strong> — a Master’s by Research or a PhD — at a participating Australian university.</li>
        <li>Have an <strong>outstanding academic record</strong> and <strong>previous research experience</strong>.</li>
        <li>Hold the equivalent of an <strong>Australian Honours degree</strong> (per Bright; university-specific).</li>
        <li>Meet the university’s <strong>English-language requirements</strong>.</li>
        <li>Do not hold a concurrent RTP at another institution (aggregator-only).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>RTP Fees Offset:</strong> full tuition covered.</li>
        <li><strong>RTP Stipend:</strong> a living allowance — official 2026 range <strong>AUD 34,315–53,608</strong>; 2027 base <strong>AUD 35,550</strong> (maximum AUD 55,537).</li>
        <li><strong>Allowances:</strong> relocation and thesis allowances (Sydney: up to AUD 1,485 each way for relocation, AUD 420 Master’s / AUD 840 Doctoral for thesis), plus <strong>Overseas Student Health Cover</strong> for internationals.</li>
        <li><strong>Duration:</strong> Master’s by research up to 2 years; PhD up to 4 years.</li>
        <li>Example rates: <strong>Sydney AUD 42,754 a year</strong> (2026) / AUD 44,293 (2027); <strong>ANU AUD 39,069 a year</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>HDR admission application</strong> for your chosen university.</li>
        <li><strong>Academic transcripts</strong> plus grading-system information.</li>
        <li>A <strong>research proposal</strong>.</li>
        <li>Your <strong>CV/résumé</strong>.</li>
        <li><strong>Academic references</strong>.</li>
        <li><strong>English-proficiency evidence</strong> (IELTS/TOEFL).</li>
        <li><strong>Proof of citizenship/residency</strong>; a Student ID is issued after the admission application (Sydney FAQ).</li>
        <li>Note: the exact list varies by university — there is <strong>no single published central checklist</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Choose a participating university</strong> and secure or identify a supervisor (required at some universities, e.g. SCU, CQU).</li>
        <li><strong>Apply for HDR admission</strong> through that university’s portal (e.g. Sydney Courses).</li>
        <li>Submit that university’s <strong>scholarship/RTP form by its own deadline</strong> — Sydney has a separate RTP form; at ANU you tick the scholarship in the admission application and there is no separate form.</li>
        <li><strong>Do not apply to the Department of Education</strong> — RTP applications cannot be made through the Department; there is no central portal.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Australian Government RTP Scholarship 2027?',
  'There is no central deadline — it varies by university. The next open rounds are the University of Sydney (Research Periods 3 & 4, 2027) on 18 December 2026, Southern Cross University on 31 October 2026, Central Queensland University on 31 December 2026, and ANU Round 2 on 15 April 2027.'),
 ('How much is the RTP stipend?',
  'The official range for 2026 is AUD 34,315 (base) to AUD 53,608 (maximum); for 2027 the base is AUD 35,550 and the maximum AUD 55,537. Universities set the rate within that range — Sydney pays AUD 42,754 a year (2026), ANU AUD 39,069.'),
 ('Is the RTP fully funded?',
  'Yes, in the usual sense: the RTP Fees Offset covers full tuition, and the stipend covers living costs, with relocation, thesis and health-cover allowances on top. Duration is up to 2 years for a Master’s by research and up to 4 years for a PhD.'),
 ('How do I apply for the Australian Government RTP?',
  'Apply to a university, not to the government. Choose a participating university, secure a supervisor, apply for HDR admission through that university’s portal, and submit that university’s RTP form by its own deadline. There is no central portal.'),
 ('What is the real name of the Australian Government Research Scholarship?',
  'The Research Training Program (RTP). “Australian Government Research Scholarship” is the aggregator’s name for it, not the scheme’s official name.'),
 ('Can international students get the RTP?',
  'Yes — the RTP is open to domestic and international students enrolled in or commencing a Higher Degree by Research at a participating Australian university.'),
 ('Which university deadlines are still open for RTP 2027?',
  'Sydney Research Periods 3 & 4, 2027 (18 December 2026), Southern Cross University (31 October 2026), Central Queensland University (31 December 2026) and ANU Round 2 (15 April 2027). Sydney RP 1 & 2, 2027 and ANU Round 1 are already closed.')]) + '''
      <p class="verify">Verified 27 Oct 2026: education.gov.au/research-block-grants/research-training-program (official) — RTP is a federal block grant administered by individual higher education providers; "RTP scholarship applications cannot be made through the Department of Education"; official stipend rates 2026 base AUD 34,315 / max AUD 53,608, 2027 base AUD 35,550 / max AUD 55,537; coverage RTP Fees Offset (full tuition), stipend, allowances (relocation, thesis), OSHC for internationals; duration Master's by research up to 2 years, PhD up to 4 years. education.gov.au RTP FAQ for students (official). sydney.edu.au/scholarships/australian-government-research-training-program.html (official) — process confirmed; its timeline table did not render in the fetch, so the Sydney 18 Dec 2026 date for Research Periods 3 &amp; 4, 2027 is aggregator-corroborated (scholarships.af, Gradualin, ScholarshipsAds, YouthExpat), not direct-official. study.anu.edu.au/scholarships/find-scholarship/australian-government-research-training-program-rtp-stipend (official ANU page) — Round 2 15 April 2027; Round 1 international closed 31 Aug 2026, domestic 26 Oct 2026. Southern Cross University 31 Oct 2026 (AfterSchoolAfrica) and Central Queensland University 31 Dec 2026 (ScholarPositions) are aggregator-only. Sydney stipend AUD 42,754/yr (2026) / AUD 44,293/yr (2027) and ANU AUD 39,069/yr are aggregator/ANU-page figures; Sydney relocation up to AUD 1,485 each way, thesis AUD 420 Master's / AUD 840 Doctoral (aggregator). CONFLICTS: one aggregator (ehsaskafaalat) quotes a flat "AUD 52,352 stipend" — that is the official 2025 maximum rate, mislabelled as the standard stipend; not used. Bright's "AUD 1,000 travel from home country to/from Adelaide" is Adelaide-specific, not a general RTP benefit. The queue title's "Australian Government Research Scholarship" is not the scheme's real name — the real name is Research Training Program (RTP). Already closed: Sydney RP 1 &amp; 2, 2027 (11 Sep 2026); ANU Round 1.</p>''',
 dl_long='Varies by university — next round: University of Sydney, 18 December 2026 (ANU Round 2: 15 April 2027)',
 offlinks=[('Australian Government — Research Training Program (official)', 'https://www.education.gov.au/research-block-grants/research-training-program'),
           ('Australian Government — RTP FAQs for students (official)', 'https://www.education.gov.au/research-block-grants/research-training-program/research-training-program-frequently-asked-questions-students'),
           ('University of Sydney — RTP (official)', 'https://www.sydney.edu.au/scholarships/australian-government-research-training-program.html'),
           ('ANU — RTP Stipend (official)', 'https://study.anu.edu.au/scholarships/find-scholarship/australian-government-research-training-program-rtp-stipend'),
           ('Bright Scholarship — Australian Government Research Scholarship 2026-27', 'https://brightscholarship.com/australian-government-research-scholarship-2026-27/')],
 related_titles=['monash-rtp', 'melbourne2027', 'uq-arc-ft27', 'deakin-vc-2027'])),

# ---------------------------------------------------------------- build + validate
for a in A:
    _split_verify(a)
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']

sizes = {}
for a in A:
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch57_built.json','w'))

class _P(html.parser.HTMLParser):
    def error(self, msg): raise ValueError(msg)

for a in A:
    p = OUT / (a['slug'] + '.html')
    assert p.exists(), a['slug']
    _P().feed(p.read_text())
    t = p.read_text()
    assert 'AICTE Pragati' not in t, a['slug']
    assert 'Lorem' not in t, a['slug']
    assert '#' not in a['slug']
    assert 'wa.me/919905166009' in t, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

# write new cards into the registry for the next run
reg = pathlib.Path('cards_registry.py').read_text()
assert reg.rstrip().endswith('}')
add = ''
for k, v in NEW_CARDS.items():
    add += " '%s': %s,\n" % (k, repr(v))
reg = reg.rstrip()[:-1] + add + '}\n'
pathlib.Path('cards_registry.py').write_text(reg)
print('registry updated, now', len(CARDS), 'cards')

#!/usr/bin/env python3
"""Batch 43 (cron run 43, 24 Oct 2026): 5 new verified articles.

Queue scan order (next 5 not in done/skipped):
1. British Academy Elevate Leadership Program 2027 (Funded) — VERIFIED:
   official British Academy Elevate Programme "Leadership Stream" key-information
   page; applications 1 Sep - 28 Oct 2026 for the March-June 2027 cohort;
   deadline 28 Oct 2026 (closing time of day not published). Funded professional
   development (no fee), three-year pilot backed by a GBP 5m Wellcome investment.
   NOT a cash award. For ECRs in SHAPE disciplines; ECRN members / Wellcome-funded
   researchers; 62 per year; UK-based attend ~10 in-person sessions, non-UK join online.
2. Dartmouth Neukom Postdoctoral Fellowship 2027 in USA (Stipend $70,000) — VERIFIED:
   official neukom.dartmouth.edu page; application site live 1 Aug 2026;
   deadline 1 Dec 2026 (recommendation letters due 8 Dec 2026; no time zone stated);
   $70,000 salary for 2027-2028, two-year appointment with option to request a third
   year, plus funds for equipment/travel/research materials; $5,000 research stipend
   per Dartmouth's Chronicle job listing. PhD (any discipline)/DMA/MFA expected by
   1 Sep 2027; research intersecting computation; no citizenship restriction published;
   teach one seminar course per year. A passport is NOT on the official document list.
3. University of Tokyo ADB Scholarship 2027 in Japan (Fully Funded) — VERIFIED:
   official UTokyo Graduate School of Frontier Sciences ADB-JSP page (guidelines
   updated Sep 2026); deadline 10 Dec 2026 for the Autumn 2027 intake (GSFS-specific;
   other UTokyo schools run separate routes). Full tuition, monthly subsistence
   (housing included; exact amount not published on the official page), books,
   medical insurance, travel; scholar only. ADB borrowing member country nationals,
   35 or under, bachelor's + 2 yrs professional work experience, GSFS master's only.
4. "Industrial Future Fellowships Australia 2027 for International Researchers" —
   SKIPPED (duplicate): the aggregator-invented title refers to the ARC Future
   Fellowships 2027 (FT27) round, which is already covered by the published article
   arc-future-fellowships-2027-australia.html (batch 33, same deadline 6 Nov 2026).
   Marked skipped with reason "duplicate of published FT27 2027 article".
   REPLACEMENT: Hong Kong PhD Fellowship Scheme (HKPFS) 2027 (Fully Funded) —
   (verifier dossier pending at script authoring time; article appended below on receipt).
5. European Space Agency International Internship 2027 (Funded) — VERIFIED:
   official esa.int Student Internships page + FAQ + cosmos.esa.int. The 2027 call
   is NOT yet open (jobs.esa.int shows no internship vacancies); opens each November
   for about a month (expected Nov 2026 - ~30 Nov 2026, earliest starts Feb 2027).
   ESA calls internships "unpaid" but grants a monthly allowance: EUR 800 for
   non-residents, EUR 500 for residents; 3-6 months, on site. Master's students in
   final/penultimate year; citizens of ESA Member/Associate/Cooperating States or
   Canada only (NOT all nationalities); one ESA internship per person; max 2
   applications per call. CV + motivation letter via the ESA recruitment site.

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
 'elevate-2027': {'mono': 'BA', 'title': 'British Academy Elevate Leadership Program 2027 (Funded)',
   'href': 'british-academy-elevate-leadership-program-2027.html',
   'dpill': 'Deadline 28 Oct 2026 \u00b7 4 days left',
   'award': 'Funded professional development (no fee to participate); three-year pilot backed by a \u00a35m Wellcome investment.',
   'elig': 'Early-career researchers in SHAPE disciplines; British Academy ECR Network members / Wellcome-funded researchers; UK-based in-person, online for others.',
   'tags': [('Fellowship', 'purple'), ('UK', 'teal')]},
 'neukom-2027': {'mono': 'NE', 'title': 'Dartmouth Neukom Postdoctoral Fellowship 2027 in USA (Stipend $70,000)',
   'href': 'dartmouth-neukom-postdoctoral-fellowship-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 \u00b7 38 days left',
   'award': '$70,000/yr salary, 2-year appointment (+ possible 3rd year), $5,000 research stipend, equipment/travel/research funds.',
   'elig': 'PhD (any discipline)/DMA/MFA by 1 Sep 2027; research intersecting computation; teach 1 seminar/yr; no citizenship restriction published.',
   'tags': [('Fellowship', 'purple'), ('USA', 'teal')]},
 'utokyo-adb-2027': {'mono': 'UT', 'title': 'University of Tokyo ADB Scholarship 2027 in Japan (Fully Funded)',
   'href': 'university-of-tokyo-adb-scholarship-2027-japan.html',
   'dpill': 'Deadline 10 Dec 2026 \u00b7 47 days left',
   'award': 'Full tuition + monthly subsistence (housing) + books + medical insurance + travel; covers the scholar only.',
   'elig': 'ADB borrowing member country nationals, 35 or under; bachelor\u2019s + 2 yrs work experience; English; GSFS master\u2019s only.',
   'tags': [('Master\u2019s', 'blue'), ('Japan', 'teal')]},
 'esa-2027': {'mono': 'ESA', 'title': 'European Space Agency International Internship 2027 (Funded)',
   'href': 'european-space-agency-internship-2027.html',
   'dpill': 'Call expected Nov 2026 \u00b7 dates not yet published',
   'award': '\u20ac800/month (non-resident) / \u20ac500/month (resident) allowance; 3\u20136 months on site; own insurance, travel, accommodation.',
   'elig': 'Master\u2019s students (final/penultimate year); ESA member/cooperating states + Canada; one internship per person; max 2 applications/call.',
   'tags': [('Internship', 'blue'), ('Europe', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Elevate
A.append(dict(
 slug='british-academy-elevate-leadership-program-2027',
 title='British Academy Elevate Leadership Program 2027 (Funded)',
 meta='British Academy Elevate Leadership Program 2027: funded professional development for early-career researchers in the humanities and social sciences. Free of charge, backed by a \u00a35m Wellcome investment. Applications for the March\u2013June 2027 cohort close 28 October 2026 \u2014 eligibility, structure, how to apply and FAQs.',
 short='Elevate Leadership Program 2027', kicker='UK \u00b7 Fellowship \u00b7 Funded', mono='BA',
 prov_short='British Academy', prov_cat='Academy \u00b7 UK',
 h1='British Academy Elevate Leadership Program 2027 (Funded)',
 sub='Not a cash prize \u2014 something rarer: the British Academy\u2019s Elevate Leadership Program 2027 gives early-career researchers in the humanities and social sciences a funded, year-structured development journey into academic leadership, free of charge and backed by a \u00a35 million Wellcome investment. Applications for the March\u2013June 2027 cohort close on 28 October 2026.',
 dpill='Deadline 28 Oct 2026 \u00b7 4 days left',
 facts=facts([('Award', 'This is a funded professional-development programme, not a cash award. All courses are free of charge and participants do not pay to take part. Elevate is a three-year pilot backed by a \u00a35 million investment from Wellcome. Within nine months of completing the programme, participants organise an event for the Network (funded by the British Academy) and mentor the next cohort.'),
              ('Eligible', 'Early-career researchers (ECRs) in SHAPE disciplines \u2014 Social Sciences, Humanities and the Arts for People and the Economy \u2014 who are members of the British Academy Early Career Researcher Network (ECRN) or Wellcome-funded researchers. The programme adapts to early, mid and late early-career stages, and each year takes a selective cohort of 62 participants. UK-based participants attend about ten in-person sessions of one to two days in different UK locations (travel is expected); participants based outside the UK join online.'),
              ('How', 'Applications are open from 1 September to 28 October 2026 for the March\u2013June 2027 cohort. Apply through the official Leadership Stream key-information page on the British Academy website (\u201cHow to apply\u201d), where the British Academy\u2019s own channels direct ECRN members to apply directly.'),
              ('Deadline', '28 October 2026. A closing time of day is not published in the official notification, so do not assume a midnight cut-off.'),
              ('Fine print', 'The \u201c2027\u201d label refers to the March\u2013June 2027 delivery cohort; applications are made in autumn 2026. Completion carries obligations: a Network event to organise and a cohort to mentor within nine months, funded and supported by the British Academy.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>British Academy Elevate Programme</strong> is the Academy\u2019s flagship development offer for early-career researchers in <strong>SHAPE</strong> \u2014 the Social Sciences, Humanities and the Arts for People and the Economy. The <strong>Leadership Stream</strong> is its leadership-development strand: a structured programme that builds the skills, networks and confidence researchers need to lead in academic and public life, from running research teams and influencing policy to shaping the future of their disciplines.</p>
      <p>Elevate runs as a <strong>three-year pilot backed by a \u00a35 million investment from Wellcome</strong>, and participation is <strong>free of charge</strong> \u2014 participants do not pay to take part. Each year a selective cohort of <strong>62 participants</strong> is drawn from members of the British Academy <strong>Early Career Researcher Network (ECRN)</strong> and Wellcome-funded researchers, and the programme is designed to work across early, mid and late early-career stages. Delivery mixes roughly ten in-person sessions of one to two days at locations across the UK (for UK-based participants, who are expected to travel) with online provision for those based outside the UK.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>early-career researcher</strong> in a <strong>SHAPE discipline</strong> \u2014 Social Sciences, Humanities and the Arts for People and the Economy.</li>
        <li>Be a member of the <strong>British Academy Early Career Researcher Network (ECRN)</strong> or a <strong>Wellcome-funded researcher</strong>.</li>
        <li>Fit anywhere in the <strong>early, mid or late early-career stage</strong> \u2014 the programme adapts to the stage you are at.</li>
        <li>If based in the <strong>UK</strong>, be ready to attend about <strong>ten in-person sessions</strong> of one to two days each in different UK locations.</li>
        <li>If based <strong>outside the UK</strong>, join via the <strong>online delivery</strong> route.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Free of charge</strong> \u2014 all courses are free; you do not pay to participate.</li>
        <li>A structured <strong>leadership-development journey</strong> designed for SHAPE researchers, spanning early, mid and late early-career stages.</li>
        <li>A <strong>national cohort of 62 peers</strong> \u2014 a built-in network across the humanities and social sciences.</li>
        <li><strong>In-person sessions across the UK</strong> (for UK-based participants) with online delivery for those based elsewhere.</li>
        <li><strong>Post-programme support</strong>: within nine months of completing, you organise a Network event funded by the British Academy and mentor the next cohort \u2014 leadership practice, not just leadership theory.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The official notification does <strong>not publish a document list</strong> \u2014 application requirements sit inside the official Elevate application material, so read the \u201cHow to apply\u201d section of the Leadership Stream page before starting.</li>
        <li>Expect the application to establish your <strong>ECR status, SHAPE discipline, and ECRN membership or Wellcome funding</strong> \u2014 have your researcher profile and career details ready.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check your route in</strong>Confirm you are an early-career researcher in a SHAPE discipline and that you are a member of the British Academy ECR Network or a Wellcome-funded researcher.</li>
        <li><strong>Decide your delivery mode</strong>UK-based participants attend roughly ten in-person sessions around the country; those based outside the UK join online. Be sure you can commit to the format for your location.</li>
        <li><strong>Open the official Leadership Stream page</strong>The key-information page on the British Academy website carries the \u201cHow to apply\u201d section and the application route for the March\u2013June 2027 cohort.</li>
        <li><strong>Submit by 28 October 2026</strong>The application window runs 1 September to 28 October 2026. No closing time of day is published \u2014 do not leave it to the final evening.</li>
        <li><strong>Plan for the post-programme year</strong>If selected, you will organise a Network event (British Academy-funded) and mentor the next cohort within nine months of completing the programme \u2014 build that into your plans.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is Elevate a cash award?',
  'No. Elevate is a funded professional-development programme, not a grant or prize. Participation is free of charge \u2014 the funding (a \u00a35 million Wellcome investment in the three-year pilot) goes into running the programme, not into payments to participants.'),
 ('Who can apply?',
  'Early-career researchers in SHAPE disciplines \u2014 Social Sciences, Humanities and the Arts for People and the Economy \u2014 who are members of the British Academy Early Career Researcher Network or Wellcome-funded researchers. The programme works across early, mid and late early-career stages.'),
 ('Can I take part from outside the UK?',
  'Yes. UK-based participants attend about ten in-person sessions around the country, but online delivery is available specifically for participants based outside the UK.'),
 ('What happens after the programme ends?',
  'Within nine months of completing, participants organise an event for the Network \u2014 funded by the British Academy \u2014 and mentor the next cohort. It is a built-in leadership exercise, not optional extras.'),
 ('When does the 2027 cohort run?',
  'The \u201c2027\u201d cohort runs from March to June 2027. Applications for it are made in autumn 2026, closing 28 October 2026.'),
]) + '''
      <p class="verify">Verified 24 Oct 2026: thebritishacademy.ac.uk/early-career-researcher-network/british-academy-elevate-programme/leadership-stream-key-information/ (official) \u2014 applications 1 Sep\u201328 Oct 2026, March\u2013June 2027 cohort, 62 participants/year, free of charge, Wellcome three-year pilot; thebritishacademy.ac.uk/early-career-researcher-network/british-academy-elevate-programme/ (official) \u2014 \u201call courses are free of charge / you will not need to pay to participate\u201d; British Academy LinkedIn (official) \u2014 \u201cApplication window open until 28 October\u201d, ECRN members apply directly; bafa.ac.uk/about/ecr-support.html \u2014 window dates; official Wellcome-investment news release \u2014 \u00a35m pilot. Closing time of day and document list not published in the official notification.</p>
''',
 dl_long='October 28, 2026 (closing time of day not published in the official notification)',
 offlinks=[('British Academy \u2014 Elevate Programme, Leadership Stream (official)', 'https://www.thebritishacademy.ac.uk/early-career-researcher-network/british-academy-elevate-programme/leadership-stream-key-information/')],
 related_titles=['un-ypp-2026', 'lawai-2027', 'boustany-cam-2027', 'gates-cam-2027'],
))

# ---------------------------------------------------------------- 2. Dartmouth Neukom
A.append(dict(
 slug='dartmouth-neukom-postdoctoral-fellowship-2027-usa',
 title='Dartmouth Neukom Postdoctoral Fellowship 2027 in USA (Stipend $70,000)',
 meta='Dartmouth Neukom Postdoctoral Fellowship 2027: $70,000 salary for 2027\u20132028, a two-year appointment (possible third year) plus research funds at Dartmouth College. For PhDs in any discipline whose research intersects computation. Deadline 1 December 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Neukom Postdoctoral Fellowship 2027', kicker='USA \u00b7 Fellowship \u00b7 $70,000', mono='NE',
 prov_short='Neukom Institute, Dartmouth College', prov_cat='Institute \u00b7 USA',
 h1='Dartmouth Neukom Postdoctoral Fellowship 2027 in USA (Stipend $70,000)',
 sub='Computation meets every discipline: the Neukom Fellows program at Dartmouth College funds postdoctoral researchers with a $70,000 salary for 2027\u20132028, a two-year appointment (with the option to request a third), plus dedicated money for equipment, travel and research \u2014 open to PhDs in any field whose work strongly intersects computation. Applications close 1 December 2026.',
 dpill='Deadline 1 Dec 2026 \u00b7 38 days left',
 facts=facts([('Award', 'A salary of $70,000 for 2027\u20132028 on a two-year appointment, with the option to request a third year. Additional funds are available for equipment, travel and research materials, and Dartmouth\u2019s own job listing adds an annual $5,000 research stipend plus eligibility for certain benefits. Fellows teach one seminar course per year.'),
              ('Eligible', 'PhD in any discipline \u2014 or a DMA or MFA \u2014 expected by 1 September 2027, with research interests that strongly intersect the theme of computation. You should show a demonstrated interest in multidisciplinary research, evidence of thinking outside traditional paradigms, a history of collaborative work across disciplines, and independence and initiative. Postdocs and fellows currently at Dartmouth may also apply. No citizenship restriction is published on the official page.'),
              ('Documents', 'Curriculum vitae; a publications list; a statement of research interests of at most two pages, including a description of the proposed Neukom Fellow research; a description of which Dartmouth departments and faculty you want to work with and why cross-department engagement would enhance the work; three referees (letters are uploaded via an emailed link, and referees have seven days after the position closes). Optional: one paper in English (or comparable creative work), an optional teaching statement, and an optional cover letter. A passport is not on the official application materials list.'),
              ('How', 'Apply online through Interfolio (linked from the official Neukom page); the application site has been live since 1 August 2026. You are strongly encouraged to contact prospective Dartmouth mentors before applying \u2014 successful applications usually include a faculty agreement to mentor. Submit by 1 December 2026; referees have until seven days after closing (recommendation letters due by 8 December 2026).'),
              ('Deadline', '1 December 2026 \u2014 application review begins on this date; recommendation letters are due no later than 8 December 2026. No time zone is stated on the official page. Applications continue to be reviewed until positions are filled.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Neukom Institute for Computational Science</strong> at <strong>Dartmouth College</strong> runs the <strong>Neukom Fellows</strong> program \u2014 postdoctoral fellowships for researchers whose work sits at the intersection of <strong>computation and any other discipline</strong>. Fellows pursue their own interdisciplinary research while embedded in Dartmouth\u2019s academic community, with the freedom to work across departments rather than inside a single one.</p>
      <p>The 2027\u20132029 competition offers a <strong>$70,000 salary for 2027\u20132028</strong> on a <strong>two-year appointment</strong>, with the option to request a third year. Beyond salary, the Institute makes <strong>additional funds available for equipment, travel and research materials</strong>, and Dartmouth\u2019s own job listing adds an <strong>annual $5,000 research stipend</strong> plus eligibility for certain benefits. Fellows teach <strong>one seminar course per year</strong> \u2014 a light teaching load that keeps the focus on research while building an academic profile.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold (or expect by <strong>1 September 2027</strong>) a <strong>PhD in any discipline</strong>, or a <strong>DMA or MFA</strong>.</li>
        <li>Have research interests that <strong>strongly intersect the theme of computation</strong>.</li>
        <li>Show <strong>demonstrated interest in multidisciplinary research</strong> and evidence of thinking outside traditional paradigms.</li>
        <li>Bring a <strong>history of collaborative work across disciplines</strong> together with evidence of <strong>independence and initiative</strong>.</li>
        <li>Be ready to <strong>teach one seminar course per year</strong>.</li>
        <li><strong>Current Dartmouth postdocs and fellows</strong> are also eligible to apply; no citizenship restriction is published on the official page.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$70,000 salary</strong> for 2027\u20132028.</li>
        <li><strong>Two-year appointment</strong> with the option to request a <strong>third year</strong>.</li>
        <li><strong>Additional funds for equipment, travel and research materials</strong>, plus an annual <strong>$5,000 research stipend</strong> per Dartmouth\u2019s job listing.</li>
        <li>Eligibility for <strong>certain benefits</strong> (per Dartmouth\u2019s posting).</li>
        <li>A <strong>light teaching load</strong> \u2014 one seminar course per year \u2014 inside a strongly interdisciplinary research community.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Curriculum vitae</strong> and a <strong>publications list</strong>.</li>
        <li><strong>Statement of research interests</strong> (maximum two pages), including a description of the research you propose as a Neukom Fellow.</li>
        <li><strong>Description of the Dartmouth departments and faculty</strong> you want to work with, and why engagement across departments would enhance your work.</li>
        <li><strong>Three referees</strong> \u2014 letters are uploaded via a link emailed to them; referees have <strong>seven days after the position closes</strong>.</li>
        <li>Optional extras: <strong>one paper in English</strong> (or comparable creative work), a <strong>teaching statement</strong>, and a <strong>cover letter</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Line up a mentor early</strong>Contact prospective Dartmouth faculty before applying \u2014 successful applications usually include a faculty agreement to mentor you.</li>
        <li><strong>Draft the core documents</strong>Prepare your CV, publications list, two-page research-interest statement (including your proposed Neukom research), and the statement on which departments and faculty you want to work with and why.</li>
        <li><strong>Apply online via Interfolio</strong>The application site (linked from the official Neukom page) has been live since 1 August 2026 \u2014 submit your full application by 1 December 2026.</li>
        <li><strong>Brief your referees</strong>Three referees receive an upload link by email; they have seven days after the position closes, so recommendation letters are due by 8 December 2026.</li>
        <li><strong>Note the rolling tail</strong>Application review begins on 1 December 2026 and continues until positions are filled \u2014 but the deadline itself is firm, so apply on time.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Which disciplines can apply?',
  'Any. The fellowship is defined by the intersection with computation, not by department \u2014 PhDs from the sciences, humanities, social sciences and arts have all held Neukom fellowships, provided their research strongly engages computational questions.'),
 ('Do I need the PhD in hand when I apply?',
  'The doctorate (PhD, DMA or MFA) must be expected by 1 September 2027. You can apply while finishing, as long as the degree will be complete by then.'),
 ('Is there a citizenship or residency restriction?',
  'None is published on the official page \u2014 international researchers are welcome to apply.'),
 ('How much teaching is involved?',
  'Fellows teach one seminar course per year \u2014 a light load designed to build an academic profile without crowding out research.'),
 ('Should I contact a Dartmouth mentor before applying?',
  'Strongly encouraged. The Institute notes that successful applications usually include a faculty agreement to mentor, so start that conversation well before the 1 December deadline.'),
]) + '''
      <p class="verify">Verified 24 Oct 2026: neukom.dartmouth.edu/funding/faculty/postdoctoral-fellows (official) \u2014 application site live 1 Aug 2026, deadline 1 Dec 2026, referee letters due 7 days after closing, $70,000 salary for 2027\u20132028, two-year appointment with option to request a third year, additional funds for equipment/travel/research materials, PhD (any discipline)/DMA/MFA expected by 1 Sep 2027, computation-intersecting research, one seminar course per year, current Dartmouth postdocs eligible, review continues until filled; jobs.chronicle.com posting (Dartmouth) \u2014 $70,000, 2+1 years, $5,000 research stipend, benefits; globalsouthopportunities.com \u2014 dates corroborated (opens 1 Aug 2026, letters 8 Dec 2026, start 1 Sep 2027). No time zone and no passport requirement published in the official notification.</p>
''',
 dl_long='December 1, 2026 (recommendation letters due by December 8, 2026; no time zone published)',
 offlinks=[('Neukom Institute \u2014 Postdoctoral Fellows, official page', 'https://neukom.dartmouth.edu/funding/faculty/postdoctoral-fellows')],
 related_titles=['lawai-2027', 'hawaii-ewc', 'trudeau-2027', 'un-ypp-2026'],
))

# ---------------------------------------------------------------- 3. UTokyo ADB
A.append(dict(
 slug='university-of-tokyo-adb-scholarship-2027-japan',
 title='University of Tokyo ADB Scholarship 2027 in Japan (Fully Funded)',
 meta='University of Tokyo ADB Scholarship 2027 (ADB-JSP): fully funded master\u2019s at UTokyo\u2019s Graduate School of Frontier Sciences \u2014 full tuition, monthly subsistence, books, medical insurance and travel. Deadline 10 December 2026 for the Autumn 2027 intake \u2014 eligibility, documents, how to apply and FAQs.',
 short='UTokyo ADB Scholarship 2027', kicker='Japan \u00b7 Master\u2019s \u00b7 Fully Funded', mono='UT',
 prov_short='University of Tokyo', prov_cat='University \u00b7 Japan',
 h1='University of Tokyo ADB Scholarship 2027 in Japan (Fully Funded)',
 sub='A fully funded master\u2019s in Tokyo: the Asian Development Bank\u2013Japan Scholarship Program at the University of Tokyo\u2019s Graduate School of Frontier Sciences covers full tuition, a monthly subsistence allowance, books, medical insurance and travel for the Autumn 2027 intake. Applications close 10 December 2026.',
 dpill='Deadline 10 Dec 2026 \u00b7 47 days left',
 facts=facts([('Award', 'Fully funded: full tuition fees; a monthly subsistence allowance that includes housing (the exact amount is not published on the official GSFS page); an allowance for books and instructional materials; medical insurance; and travel expenses. Thesis-preparation research grants and, in special cases, preparatory language or computer courses may also be covered. The scholarship covers the scholar only, not dependents.'),
              ('Eligible', 'Nationals of an ADB borrowing member country that is eligible for Japanese ODA; 35 years old or younger at the time of application (GSFS states explicitly it cannot nominate anyone over 35); a bachelor\u2019s degree or equivalent with a superior academic record; at least two years of full-time professional work experience gained after the degree and related to the field of study; proficiency in oral and written English; good health; agreement to return to and work in the home country for at least two years after completing the programme; no master\u2019s degree already held; not a dual citizen of a developed country; not ADB staff or consultants or their close relatives; not staff of a designated institution; not living or working outside the home country; not already enrolled in a graduate degree programme. You must also meet the admission requirements of your chosen GSFS department and pass the university\u2019s preliminary screening. GSFS offers the master\u2019s course only \u2014 there is no doctoral track under this route.'),
              ('Documents', 'The official GSFS ADB-JSP page does not publish a full document checklist \u2014 applicants are directed to their department\u2019s application guidelines. The ADB standard application set, per corroborating sources, comprises the completed ADB-JSP information/application sheet, academic transcripts and degree certificates, a CV, a research plan, recommendation letters, a passport copy, income/family-income certifications, proof of work experience, and English-proficiency evidence. Confirm the exact per-department checklist in the GSFS guidelines documents.'),
              ('How', 'Never apply directly to ADB \u2014 candidates are nominated by the university. (1) Check your ADB-JSP eligibility at adb.org. (2) Identify a prospective faculty supervisor in the target GSFS department and complete the department\u2019s application procedures by 10 December 2026. (3) Preliminary-screening results are announced in mid-February 2027. (4) Those who pass are told the ADB-JSP application procedure. (5) UTokyo nominates candidates to ADB in mid-March 2027. (6) ADB runs its own screening, with results around May 2027. (7) Confirmed scholars complete Autumn 2027 enrolment and enter Japan by the end of September 2027 \u2014 the Autumn semester begins 1 October 2027.'),
              ('Deadline', '10 December 2026 \u2014 for the Graduate School of Frontier Sciences, Autumn 2027 intake. Other UTokyo graduate schools (e.g. GraSPP) run separate ADB-JSP routes with their own deadlines, so do not mix them up.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Asian Development Bank\u2013Japan Scholarship Program (ADB-JSP)</strong>, funded by the Government of Japan and administered by the ADB, sends outstanding students from developing Asia and the Pacific to designated institutions across the region. At the <strong>University of Tokyo</strong>, one of those designated institutions, the scholarship is administered school by school \u2014 and the <strong>Graduate School of Frontier Sciences (GSFS)</strong> runs the route covered here, with its <strong>Autumn 2027 intake</strong> guidelines updated in September 2026.</p>
      <p>The award is <strong>fully funded</strong>: full tuition fees, a <strong>monthly subsistence allowance including housing</strong>, a books and instructional-materials allowance, <strong>medical insurance</strong> and <strong>travel expenses</strong>, with thesis-preparation research grants and (in special cases) preparatory courses also possible. ADB-JSP scholars join GSFS departments spanning environmental studies, ocean technology and policy, environment systems, human and engineered environmental studies, socio-cultural environment studies, international studies, and the Graduate Program in Sustainability Science.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>national of an ADB borrowing member country</strong> eligible for Japanese ODA.</li>
        <li>Be <strong>35 or younger</strong> at the time of application (GSFS states it cannot nominate anyone over 35).</li>
        <li>Hold a <strong>bachelor\u2019s degree or equivalent</strong> with a superior academic record.</li>
        <li>Have at least <strong>two years of full-time professional work experience</strong> gained after the degree and related to the field of study (undergraduate research-assistant work does not count).</li>
        <li>Be <strong>proficient in oral and written English</strong> and in <strong>good health</strong>.</li>
        <li><strong>Agree to return to and work in the home country</strong> for at least two years after completing the programme.</li>
        <li><strong>Not already hold a master\u2019s degree</strong>; not hold dual citizenship of a developed country; not be ADB staff/consultants or their close relatives; not be staff of a designated institution; not be living or working outside the home country; not already be enrolled in a graduate degree programme.</li>
        <li>Meet the <strong>admission requirements of the chosen GSFS department</strong> and pass the university\u2019s preliminary screening (GSFS master\u2019s course only \u2014 no doctoral track).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> covered.</li>
        <li><strong>Monthly subsistence allowance including housing</strong> (exact amount not published on the official GSFS page).</li>
        <li><strong>Books and instructional-materials allowance</strong>, plus <strong>medical insurance</strong> and <strong>travel expenses</strong>.</li>
        <li>Possible <strong>thesis-preparation research grants</strong> and, in special cases, <strong>preparatory language or computer courses</strong>.</li>
        <li>Study at one of the world\u2019s top-ranked research universities, across GSFS\u2019s environment-focused departments.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The official GSFS ADB-JSP page does <strong>not publish a full checklist</strong> \u2014 the exact documents live in each department\u2019s application guidelines, which you must read.</li>
        <li>The ADB standard set (per corroborating sources): completed <strong>ADB-JSP application sheet</strong>, <strong>academic transcripts and degree certificates</strong>, <strong>CV</strong>, <strong>research plan</strong>, <strong>recommendation letters</strong>, <strong>passport copy</strong>, <strong>income/family-income certifications</strong>, <strong>proof of work experience</strong>, and <strong>English-proficiency evidence</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm ADB-JSP eligibility</strong>Read the program criteria at adb.org first \u2014 nationality, age, work experience and return-home conditions knock many applicants out early.</li>
        <li><strong>Find a prospective supervisor</strong>Identify a faculty member in your target GSFS department whose research matches yours and make contact \u2014 the departmental application is the real gateway.</li>
        <li><strong>Complete the departmental application by 10 December 2026</strong>Follow your department\u2019s procedures exactly; this is the deadline that matters for the GSFS Autumn 2027 route.</li>
        <li><strong>Wait for preliminary screening</strong>Results are announced in mid-February 2027. If you pass, the university tells you the ADB-JSP application procedure.</li>
        <li><strong>University nomination and ADB screening</strong>UTokyo nominates candidates to ADB in mid-March 2027; ADB conducts its own screening and announces results around May 2027.</li>
        <li><strong>Enrol for Autumn 2027</strong>Confirmed scholars complete enrolment procedures and enter Japan by the end of September 2027 \u2014 the Autumn semester begins 1 October 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I apply directly to the ADB?',
  'No. ADB-JSP applications go only through the designated institution \u2014 in this case the University of Tokyo. You apply through the GSFS departmental process; the university nominates candidates to ADB.'),
 ('Is there a PhD track at GSFS under ADB-JSP?',
  'No. GSFS offers the master\u2019s course only under this route, and the school states explicitly it cannot nominate anyone over 35 or anyone who already holds a master\u2019s degree.'),
 ('Does the scholarship cover my family?',
  'No. The ADB-JSP covers the scholar only \u2014 dependents are not included, so plan accordingly.'),
 ('Which UTokyo schools run ADB-JSP?',
  'Several, each with its own route and deadline. This article covers the Graduate School of Frontier Sciences (deadline 10 December 2026 for Autumn 2027). Other schools \u2014 such as the Graduate School of Public Policy \u2014 run separate routes; always confirm against that school\u2019s own page.'),
 ('Do I need a supervisor before applying?',
  'The GSFS process expects you to identify a prospective faculty supervisor in the target department as part of the departmental application \u2014 start that outreach early, not in December.'),
]) + '''
      <p class="verify">Verified 24 Oct 2026: k.u-tokyo.ac.jp/en/exam/master/foreign_research_students/adb_jsp/ (official UTokyo GSFS page; 2027 Autumn guidelines updated Sep 2026) \u2014 deadline 10 Dec 2026, GSFS master\u2019s only, 35-or-under rule, full tuition + monthly subsistence incl. housing + books + medical + travel, scholar-only coverage, nomination route (no direct ADB applications), preliminary screening mid-Feb 2027, UTokyo nomination mid-Mar 2027, ADB results ~May 2027, enter Japan by end Sep 2027 (semester starts 1 Oct 2027), eligible departments list; leapscholar.com + educatenepal.com \u2014 benefits/eligibility corroboration (monthly allowance ~JPY 147,000 per secondary sources, not on the official page). Document checklist and monthly amount not published in full on the official JSP page.</p>
''',
 dl_long='December 10, 2026 (Graduate School of Frontier Sciences, Autumn 2027 intake)',
 offlinks=[('University of Tokyo GSFS \u2014 ADB-JSP, official page', 'https://www.k.u-tokyo.ac.jp/en/exam/master/foreign_research_students/adb_jsp/')],
 related_titles=['inpex-2027', 'hawaii-adb', 'kaist-grad-2027', 'gxnu-csc-2027'],
))

# ---------------------------------------------------------------- 4. ESA
A.append(dict(
 slug='european-space-agency-internship-2027',
 title='European Space Agency International Internship 2027 (Funded)',
 meta='European Space Agency Internship 2027: ESA\u2019s annual student internship programme \u2014 a monthly allowance of \u20ac800 (non-resident) or \u20ac500 (resident) for 3\u20136 months on site at ESA establishments. The 2027 call opens in November 2026 \u2014 eligibility, allowance, how to apply and FAQs.',
 short='ESA Internship 2027', kicker='Europe \u00b7 Internship \u00b7 Funded', mono='ESA',
 prov_short='European Space Agency', prov_cat='Agency \u00b7 Europe',
 h1='European Space Agency International Internship 2027 (Funded)',
 sub='Work inside Europe\u2019s space program: the European Space Agency\u2019s annual Student Internship programme places master\u2019s-level students at ESA establishments for three to six months, with a monthly allowance of \u20ac800 for non-residents and \u20ac500 for residents. The 2027 call opens in November 2026 \u2014 here is everything to have ready.',
 dpill='Call expected Nov 2026 \u00b7 dates not yet published',
 facts=facts([('Award', 'ESA officially calls its internships \u201cunpaid\u201d, but grants a monthly allowance: \u20ac800 for non-resident interns (those living more than 50 km from the ESA establishment \u2014 also granted to students with special needs regardless of residency) and \u20ac500 for residents. Internships last three to six months and are on site. Interns cover their own health insurance, accident insurance, travel expenses and accommodation.'),
              ('Eligible', 'You must be a student \u2014 preferably in the final or second-to-last year of a university course at master\u2019s level \u2014 and you must hold student status and be enrolled at university for the entire duration of the internship. PhD students are told not to apply; they should use the Research Fellowship programme instead. You must be a citizen of an ESA Member State, an Associate Member, a European Cooperating State, or Canada as a Cooperating State \u2014 it is not open to all nationalities. Only one ESA internship may be undertaken per person, and a maximum of two internship applications per person per call (more than two means all are disregarded).'),
              ('Documents', 'A CV and a motivation letter \u2014 both are required to create the candidate profile on the ESA recruitment site \u2014 plus your answers to the application-form questions. No other required documents are published in the official notification.'),
              ('How', 'Internship opportunities are published each November on ESA\u2019s recruiting site, jobs.esa.int. Browse the openings, register, create a candidate profile with your CV and motivation letter, and submit \u2014 a maximum of two applications per call. You can set up a job alert on the ESA site to be notified when the opportunities go live. Contact: ESA.Student.Internships@esa.int. As of 24 October 2026 the 2027 call is not yet published (the portal shows no open internship vacancies).'),
              ('Deadline', 'Not published in the official notification: the 2027 call had not opened as of 24 October 2026. ESA opens the call in November each year for about one month \u2014 the annual pattern points to a window from early November to around 30 November 2026, with the earliest internship starts in February 2027. Treat the window as expected, not official, and set the job alert now.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>European Space Agency (ESA)</strong> runs an <strong>annual Student Internship programme</strong> that places university students inside real ESA teams \u2014 engineering, science, Earth observation, telecommunications, operations, and the corporate functions that keep a space agency flying. Internships run <strong>three to six months</strong> and are <strong>on site</strong> at ESA establishments, so this is a genuine placement inside Europe\u2019s space program, not a remote project.</p>
      <p>On money, the wording matters: ESA officially describes the internships as <strong>\u201cunpaid\u201d</strong>, but every intern receives a <strong>monthly allowance</strong> \u2014 <strong>\u20ac800 for non-residents</strong> (students living more than 50 km from the establishment, plus students with special needs regardless of where they live) and <strong>\u20ac500 for residents</strong>. Interns arrange and pay for their own <strong>health insurance, accident insurance, travel and accommodation</strong>, so budget the allowance against the cost of living near the establishment.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>student</strong>, preferably in the <strong>final or second-to-last year of a master\u2019s-level</strong> university course.</li>
        <li>Hold <strong>student status and stay enrolled</strong> at your university for the entire duration of the internship.</li>
        <li>Be a <strong>citizen of an ESA Member State, an Associate Member, a European Cooperating State, or Canada</strong> as a Cooperating State \u2014 the programme is <strong>not open to all nationalities</strong>.</li>
        <li><strong>PhD students should not apply</strong> \u2014 ESA directs them to the Research Fellowship programme instead.</li>
        <li>Respect the limits: <strong>one ESA internship per person, ever</strong>, and a <strong>maximum of two applications per call</strong> \u2014 submit more than two and all of them are disregarded.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac800/month allowance</strong> for non-residents (over 50 km from the establishment; also students with special needs) or <strong>\u20ac500/month</strong> for residents.</li>
        <li><strong>Three to six months on site</strong> at an ESA establishment, working inside a real mission or corporate team.</li>
        <li>A placement inside <strong>Europe\u2019s space program</strong> \u2014 engineering, science, Earth observation, operations and more.</li>
        <li>Note the intern\u2019s own costs: <strong>health insurance, accident insurance, travel and accommodation are on you</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV</strong> and <strong>motivation letter</strong> \u2014 both required to create your candidate profile on the ESA recruitment site.</li>
        <li>Your <strong>answers to the application-form questions</strong> for each opportunity you apply to.</li>
        <li>No other required documents are published in the official notification.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Set a job alert now</strong>The 2027 call is not yet open \u2014 register on jobs.esa.int and set an alert so you are notified the day internship opportunities go live in November.</li>
        <li><strong>Prepare your CV and motivation letter early</strong>Both are mandatory for the candidate profile; have them polished before the one-month window opens.</li>
        <li><strong>Pick at most two opportunities</strong>When the call opens, browse the listings and choose carefully \u2014 the limit is two applications per call, and a third gets all of them thrown out.</li>
        <li><strong>Submit within the window</strong>The call runs about a month (the annual pattern suggests early-to-late November 2026) \u2014 do not assume it will be extended.</li>
        <li><strong>Ask ESA directly if unsure</strong>Internship questions go to <strong>ESA.Student.Internships@esa.int</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the internship open to all nationalities?',
  'No. You must be a citizen of an ESA Member State, an Associate Member, a European Cooperating State, or Canada as a Cooperating State. Some aggregator sites wrongly claim \u201call nationalities\u201d \u2014 the official FAQ restricts eligibility.'),
 ('Is it really unpaid?',
  'ESA uses the word \u201cunpaid\u201d, but every intern receives a monthly allowance: \u20ac800 for non-residents (\u2014 or students with special needs) and \u20ac500 for residents. Health insurance, accident insurance, travel and accommodation are your own costs.'),
 ('Can PhD students apply?',
  'No. ESA tells PhD students not to apply for internships and points them to the Research Fellowship programme instead. The internships target master\u2019s-level students, preferably in their final or penultimate year.'),
 ('How many applications can I submit?',
  'Two per call \u2014 and ESA is strict: more than two means all your applications are disregarded. Across your lifetime, you may only ever do one ESA internship.'),
 ('When does the 2027 call open?',
  'Not yet published. ESA opens the call each November for about a month; the annual pattern points to November 2026 with earliest starts in February 2027. Set a job alert on jobs.esa.int rather than guessing the date.'),
]) + '''
      <p class="verify">Verified 24 Oct 2026: esa.int/About_Us/Careers_at_ESA/Student_Internships2 (official) + Student internships FAQ (official) \u2014 annual call each November for ~1 month, on-site 3\u20136 months, \u201cunpaid\u201d with monthly allowance, master\u2019s final/penultimate year, student status for full duration, PhD students excluded, ESA Member/Associate/Cooperating States + Canada only, 1 internship per person, max 2 applications per call, job alerts, ESA.Student.Internships@esa.int; cosmos.esa.int/web/science-internships (official ESA science site) \u2014 \u20ac800 non-resident / \u20ac500 resident allowance figures; jobs.esa.int (official portal) \u2014 no open internship vacancies as of 24 Oct 2026, confirming the 2027 call is not yet published; scholarshipbob.com \u2014 corroborating summary (3\u20136 months, allowance model, starts from Feb 2027). Exact 2027 call dates not published in the official notification; the Nov\u2013~30 Nov 2026 window is the annual pattern. The separate EAC school internship (deadline 30 Sep 2026) is a different programme.</p>
''',
 dl_long='2027 call not yet open as of 24 October 2026 \u2014 expected November 2026 (exact dates not published in the official notification)',
 offlinks=[('ESA \u2014 Student Internships, official page', 'https://www.esa.int/About_Us/Careers_at_ESA/Student_Internships2'),
           ('ESA recruitment portal \u2014 internship vacancies', 'https://jobs.esa.int/')],
 related_titles=['salzburg-int-2027', 'un-ypp-2026', 'lawai-2027', 'swinburne-2027'],
))

# ---------------------------------------------------------------- 5. HKPFS
A.append(dict(
 slug='hong-kong-phd-fellowship-scheme-2027',
 title='Hong Kong PhD Fellowship Scheme (HKPFS) 2027 (Fully Funded)',
 meta='Hong Kong PhD Fellowship Scheme 2027/28: HK$344,400 annual stipend (~US$44,150) + HK$14,400 travel allowance for three years at one of Hong Kong\u2019s eight UGC-funded universities. 400 fellowships, open to all nationalities. Deadline 1 December 2026 (noon HKT) \u2014 eligibility, the two-step application, and FAQs.',
 short='HKPFS 2027', kicker='Hong Kong \u00b7 PhD \u00b7 Fully Funded', mono='HK',
 prov_short='Research Grants Council (RGC), Hong Kong', prov_cat='Research Council \u00b7 Hong Kong',
 h1='Hong Kong PhD Fellowship Scheme (HKPFS) 2027 (Fully Funded)',
 sub='One of the world\u2019s most generous PhD awards: the Hong Kong PhD Fellowship Scheme pays HK$344,400 a year (about US$44,150) plus a HK$14,400 annual travel allowance for three years of full-time doctoral study at one of Hong Kong\u2019s eight publicly funded universities \u2014 with 400 fellowships for 2027/28 and no nationality restriction. The initial RGC application closes 1 December 2026 at noon Hong Kong Time.',
 dpill='Deadline 1 Dec 2026 \u00b7 38 days left',
 facts=facts([('Award', 'An annual stipend of HK$344,400 (about US$44,150) plus a conference and research-related travel allowance of HK$14,400 per year (about US$1,840), for a period of three years. 400 fellowships will be awarded for the 2027/28 academic year. Tuition is not part of the RGC award itself \u2014 most host universities cover it separately, so verify tuition arrangements with your chosen university. (Older pages may show the 2026/27 figures of HK$340,800/HK$14,200 \u2014 the 2027/28 call letter raises them to HK$344,400/HK$14,400.)'),
              ('Eligible', 'You must be seeking admission as a new full-time PhD student at a UGC-funded Hong Kong university \u2014 the eight participating institutions are HKU, CUHK, HKUST, CityUHK, PolyU, HKBU, Lingnan and EdUHK. The scheme is open irrespective of country of origin, prior work experience or ethnic background: there is no nationality restriction. Applicants are expected to demonstrate outstanding academic performance, research ability and potential, communication and interpersonal skills, and leadership abilities \u2014 and must still meet the chosen university\u2019s own admission requirements.'),
              ('Documents', 'Not listed in the official RGC call letter. Documents are handled at the university full-application stage, which \u2014 per university pages \u2014 covers transcripts and degree certificates, a CV, a research proposal or statement of purpose, reference letters and English test scores. Confirm the exact list against your chosen university\u2019s HKPFS page.'),
              ('How', 'Two steps. Step 1: submit the initial application through the RGC\u2019s HKPFS Electronic System (HKPFSES) during the call window \u2014 you may select up to two programmes in one or two universities \u2014 and on submission you receive an HKPFS Reference Number. Step 2: submit the full PhD admission application directly to your chosen university or universities, quoting that reference number, before their stated deadlines. Enquiries: HKPF@ugc.edu.hk.'),
              ('Deadline', 'Initial application: 1 December 2026, 12:00 noon Hong Kong Time, via the RGC electronic system. The full PhD admission applications to the universities carry their own deadlines (e.g. Lingnan\u2019s cutoff is 1 December 2026, 11:59 pm HKT \u2014 a per-university time, not the RGC\u2019s), so check each chosen university\u2019s page.')]),
 body='''
      <h2 id="about">About the scheme</h2>
      <p>Established by the <strong>Research Grants Council (RGC)</strong> of Hong Kong, the <strong>Hong Kong PhD Fellowship Scheme (HKPFS)</strong> was created to attract the world\u2019s best doctoral students to the city\u2019s universities. For the <strong>2027/28 academic year, 400 fellowships</strong> are on offer \u2014 each paying an annual stipend of <strong>HK$344,400 (about US$44,150)</strong> plus a <strong>HK$14,400 yearly travel allowance</strong> for three years of full-time PhD study.</p>
      <p>Eight <strong>UGC-funded universities</strong> take part \u2014 HKU, CUHK, HKUST, CityUHK, PolyU, HKBU, Lingnan and EdUHK \u2014 and the scheme is deliberately <strong>open to all nationalities</strong>, irrespective of country of origin, prior work experience or ethnic background. Selection looks for <strong>outstanding academic performance, research ability and potential, communication and interpersonal skills, and leadership abilities</strong>, on top of each university\u2019s own admission bar.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be seeking admission as a <strong>new full-time PhD student</strong> at one of the eight <strong>UGC-funded Hong Kong universities</strong> (HKU, CUHK, HKUST, CityUHK, PolyU, HKBU, Lingnan, EdUHK).</li>
        <li>Open <strong>irrespective of country of origin, prior work experience or ethnic background</strong> \u2014 no nationality restriction.</li>
        <li>Demonstrate <strong>outstanding academic performance</strong> and <strong>research ability/potential</strong>.</li>
        <li>Show strong <strong>communication and interpersonal skills</strong> plus <strong>leadership abilities</strong>.</li>
        <li>Meet the <strong>admission requirements of the chosen university</strong> \u2014 the fellowship does not waive them.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>HK$344,400 per year</strong> stipend (about US$44,150) \u2014 among the most generous PhD stipends in Asia.</li>
        <li><strong>HK$14,400 per year</strong> conference and research-related travel allowance.</li>
        <li><strong>Three years</strong> of support; universities may provide extra support if the PhD extends beyond that.</li>
        <li><strong>400 fellowships</strong> for the 2027/28 academic year \u2014 a large intake by global standards.</li>
        <li>Study at one of <strong>Hong Kong\u2019s eight publicly funded universities</strong>, with most covering tuition separately.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The official RGC call letter does <strong>not publish a document list</strong> \u2014 documents are handled at the university full-application stage.</li>
        <li>Per university HKPFS pages, expect: <strong>academic transcripts and degree certificates</strong>, <strong>CV</strong>, <strong>research proposal or statement of purpose</strong>, <strong>reference letters</strong>, and <strong>English test scores</strong> \u2014 confirm the exact list against each chosen university\u2019s page.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Shortlist up to two programmes</strong>Pick up to two PhD programmes at one or two of the eight participating universities and check you meet each university\u2019s admission requirements.</li>
        <li><strong>Step 1 \u2014 the RGC initial application</strong>Submit through the RGC\u2019s HKPFS Electronic System during the call window (1 September \u2013 1 December 2026). On submission you receive your <strong>HKPFS Reference Number</strong> \u2014 keep it safe.</li>
        <li><strong>Step 2 \u2014 the university full application</strong>Apply directly to each chosen university for PhD admission, <strong>quoting your HKPFS Reference Number</strong>, before that university\u2019s own deadline.</li>
        <li><strong>Watch both clocks</strong>The RGC initial application closes <strong>1 December 2026 at 12:00 noon HKT</strong>; university full-application deadlines are separate (e.g. Lingnan: 1 December 2026, 11:59 pm HKT).</li>
        <li><strong>Ask early if unsure</strong>Enquiries go to <strong>HKPF@ugc.edu.hk</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How many fellowships are available?',
  '400 for the 2027/28 academic year \u2014 one of the largest single PhD fellowship intakes anywhere, and the reason the scheme is a realistic target for strong applicants.'),
 ('Does the award cover tuition fees?',
  'Not as part of the RGC award itself. Most host universities cover tuition separately, but this varies \u2014 verify the tuition arrangement with each university you apply to.'),
 ('Can I apply to more than one programme?',
  'Yes \u2014 up to two programmes at one or two universities, in a single initial application through the RGC electronic system.'),
 ('Is there a nationality restriction?',
  'No. The scheme is explicitly open irrespective of country of origin, prior work experience or ethnic background.'),
 ('Which deadline matters \u2014 the RGC\u2019s or the university\u2019s?',
  'Both. The RGC initial application closes 1 December 2026 at 12:00 noon HKT, and each university sets its own full-application deadline. Miss either and the application is incomplete.'),
]) + '''
      <p class="verify">Verified 24 Oct 2026: ugc.edu.hk/eng/rgc/funding_opport/hkpfs/call_letter.html (official 2027/28 call letter) \u2014 call window 1 Sep\u20131 Dec 2026, initial application deadline 1 Dec 2026 12:00 noon HKT, HK$344,400/yr stipend (~US$44,150) + HK$14,400/yr travel allowance for 3 years, 400 fellowships, 8 UGC-funded universities, no nationality restriction, two-step process (HKPFSES initial application + university full application with HKPFS Reference Number), up to 2 programmes, HKPF@ugc.edu.hk; ln.edu.hk (Lingnan) \u2014 university full-application cutoff 1 Dec 2026 11:59 pm HKT; opportunitiesforyouth.org + Harvard FAS careers page \u2014 corroboration. Document list not published in the official RGC call letter; tuition not part of the RGC award.</p>
''',
 dl_long='December 1, 2026, 12:00 noon Hong Kong Time (initial application via the RGC electronic system)',
 offlinks=[('RGC \u2014 HKPFS 2027/28 call letter (official)', 'https://www.ugc.edu.hk/eng/rgc/funding_opport/hkpfs/call_letter.html'),
           ('HKPFS scheme home (official)', 'http://www.rgc.edu.hk/hkphd')],
 related_titles=['kaist-grad-2027', 'trudeau-2027', 'gxnu-csc-2027', 'swinburne-2027'],
))

# ---------------------------------------------------------------- build + validate
NEW_CARDS['hkpfs-2027'] = {'mono': 'HK', 'title': 'Hong Kong PhD Fellowship Scheme (HKPFS) 2027 (Fully Funded)',
   'href': 'hong-kong-phd-fellowship-scheme-2027.html',
   'dpill': 'Deadline 1 Dec 2026 \u00b7 38 days left',
   'award': 'HK$344,400/yr stipend (~US$44,150) + HK$14,400/yr travel allowance, 3 years; 400 fellowships.',
   'elig': 'New full-time PhD at one of 8 UGC-funded HK universities; all nationalities; outstanding academics + research potential.',
   'tags': [('PhD', 'purple'), ('Hong Kong', 'teal')]}
CARDS.update(NEW_CARDS)

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
    json.dump(sizes, open('/tmp/batch43_built.json','w'))

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

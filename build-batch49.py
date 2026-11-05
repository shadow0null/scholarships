#!/usr/bin/env python3
"""Batch 49 (cron run 49, 25 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Digital Humanism Fellowship 2027 — SKIPPED: deadline passed
   (21 Sep 2026, 23:59 CEST per IWM; the queue's 14 Sep date is wrong).
2. Google Student Offer 2026 — SKIPPED: not a scholarship — a student
   product offer (12 months free Google AI Pro/Plus); not written as a
   scholarship article.
3. OIST Research Internship 2027 — SKIPPED: Spring 2027 round closed
   15 Oct 2026, 23:59 JST; Fall 2027 round (15 Apr 2027) not yet open.
4. IST Research Scholarship 2027 — SKIPPED: call closed 2 Sep 2026;
   also an aggregator composite, not one scheme.
5. Taipei Medical University Scholarships 2027 — SKIPPED: deadline
   passed (31 Aug 2026, 17:00 Taiwan time).
6. Gulbenkian Institute Fellowship 2027 — SKIPPED: deadline passed
   (15 Oct 2026, 15:00 Lisbon time).
7. Durham University Early Career Fellowships 2027 — SKIPPED: deadline
   passed (2 Sep 2026); a specific Business School vacancy, not a
   university-wide scheme.
8. University of Turin Scholarship 2027 — SKIPPED: bundled schemes all
   closed (Talents 4 UniTO 29 Jan 2026; EDISU 8 Sep 2026); composite.
9. Marshall Scholarship 2027 — SKIPPED: deadline passed (29 Sep 2026;
   institutional submission 1 Oct 2026).
10. University of Alabama Presidential Scholarship 2027 — VERIFIED:
    deadline 4 Dec 2026 (NOT 15 Dec as the queue says); USD 28,000/year
    for up to 4 years; NOT fully funded (out-of-state tuition is higher).
    CORRECTION carried into the article: the "Fully Funded" label in
    the listing title is wrong; the sub, Award fact, Fine print and an
    FAQ all say so plainly. Presidential Elite (4.0 GPA + SAT 1600/ACT
    36) covers tuition + first-year housing + USD 1,500/year + one-time
    USD 2,000.
11. Western Balkans Meet Exchange Program 2027 — SKIPPED: deadline
    passed (31 Aug 2026, 23:59 CET).
12. KUT Special Scholarship Program 2027 — VERIFIED: next open deadline
    9 Apr 2027 (October 2027 enrolment, second deadline; the 16 Oct
    2026 deadline has passed). Fully funded 3-year PhD: full fee
    exemption, JPY 150,000/month stipend, one-off JPY 150,000 allowance.
13. King Abdullah University Scholarship 2027 — VERIFIED: Fall 2027
    deadline 3 Jan 2027. KAUST Fellowship, automatic for every admitted
    student; full tuition + living allowance + housing + medical +
    relocation + annual flight home.
14. Guggenheim Fellowship 2027 — SKIPPED: deadline passed (15 Sep 2026).
15. Czech Government Scholarship 2027 — SKIPPED: deadline passed
    (30 Sep 2026).
16. BS MS PhD Scholarships 2027 in Malaysia — SKIPPED: aggregator
    listicle, not a single scheme (bundles MIS, MTCP and others).
17. Oxford OCEMR DPhil Studentships 2027 — SKIPPED: deadline passed
    (22 Sep 2026, 12:00 noon UK time).
18. World Bank GovTech AI Bootcamp 2026 — SKIPPED: deadline passed
    (2 Oct 2026); also an institutional bootcamp, not a scholarship.
19. World Trade Organization Internship 2027 — VERIFIED: current
    requisition closes 31 Dec 2026, 11:59 p.m. Geneva time; CHF 60/day;
    3-6 months in Geneva. CORRECTION: "Without IELTS" is aggregator
    framing — WTO asks for no language test, but the article does not
    promise it as a feature.
20. Notre Dame Kellogg Postdoctoral Fellowship 2027 — SKIPPED: deadline
    passed (1 Oct 2026).
21. University of Konstanz Postdoc Fellowship 2027 — SKIPPED: deadline
    passed (12 Oct 2026, 11:00 AM CET).
22. INEGI Portugal PhD Scholarship 2026 — SKIPPED: deadline passed
    (31 Aug 2026); also an aggregator construct (FCT stipend figure,
    no single INEGI call).
23. Fully Funded Scholarships in USA 2027 — SKIPPED: listicle, not a
    single scheme.
24. Khalifa University Graduate Scholarship 2027 — SKIPPED: Spring 2027
    window passed (31 Aug 2026); Fall 2027 not yet open, no deadline
    published.
25. British Academy Mid Career Fellowship 2027 — SKIPPED: deadline
    passed (26 Aug 2026, 17:00 BST).
26. ERA Winter Fellowship 2027 — SKIPPED: deadline passed (13 Sep 2026).
27. KAUST Global Fellowship 2027 — SKIPPED: Stage 1 closed 1 Oct 2026;
    Stage 2 (15 Nov 2026-15 Jan 2027) is invitation-only.
28. Google Student Researcher Program 2027 — VERIFIED: open, but no
    single global deadline — deadlines are per regional posting. The
    queue's "November 2026" matches the 27 Nov 2026 posting; the EMEA
    posting closes 13 Dec 2026 and the US PhD Winter-Summer 2027 posting
    has an anticipated 16 Jul 2027 deadline. Paid placement (~12 weeks);
    the USD 118,000-157,000 figure on the US posting is an annualised
    salary range, not a stipend.
29. Eni MiNDS Master's Scholarship 2027 — SKIPPED: deadline passed
    (1 Oct 2026, 2:00 PM Italian time).
30. MSCA Postdoctoral Fellowships 2027 — SKIPPED: 2027 call not yet open
    (opens 7 Apr 2027, closes 8 Sep 2027, both TBC).

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 25)
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
 'alabama-2027': {'mono': 'AL', 'title': 'University of Alabama Presidential Scholarship 2027 in USA (Fully Funded)',
   'href': 'university-of-alabama-presidential-scholarship-2027-usa.html',
   'dpill': 'Deadline 4 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-04'),
   'award': 'USD 28,000 a year for up to four years for out-of-state and international first-time freshmen \u2014 a partial merit award, not full funding; the Presidential Elite tier covers tuition in full.',
   'elig': 'Out-of-state or international first-time freshmen with a GPA of 3.50 and SAT 1420\u20131600 or ACT 32\u201336 from a single test date.',
   'tags': [('Bachelor\u2019s', 'blue'), ('USA', 'teal')]},
 'kut-ssp-2027': {'mono': 'KU', 'title': 'KUT Special Scholarship Program 2027 in Japan (Fully Funded)',
   'href': 'kut-special-scholarship-program-2027-japan.html',
   'dpill': 'Deadline 9 Apr 2027 \u00b7 %d days left' % dl_left('2027-04-09'),
   'award': 'A fully funded three-year English-taught PhD in Engineering at Kochi University of Technology: full fee exemption, a \u00a5150,000 monthly stipend and a one-off \u00a5150,000 travel allowance.',
   'elig': 'International students of all nationalities holding a Master\u2019s degree, who select a project from the official SSP list and secure supervisor approval before applying.',
   'tags': [('PhD', 'purple'), ('Japan', 'teal')]},
 'kaust-2027': {'mono': 'KA', 'title': 'King Abdullah University Scholarship 2027 in Saudi Arabia (Fully Funded)',
   'href': 'king-abdullah-university-scholarship-2027-saudi-arabia.html',
   'dpill': 'Deadline 3 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-03'),
   'award': 'The KAUST Fellowship, awarded automatically to every admitted student: full tuition, a living allowance, free on-campus housing, medical cover, relocation support and an annual flight home.',
   'elig': 'All nationalities with a Bachelor\u2019s in a relevant STEM field (MS) or a Master\u2019s (PhD), a GPA of 3.0/4.0 and IELTS 6.5 or TOEFL iBT 79\u201381.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Saudi Arabia', 'teal')]},
 'wto-internship-2027': {'mono': 'WT', 'title': 'World Trade Organization Internship 2027 in Switzerland (Without IELTS)',
   'href': 'world-trade-organization-internship-2027-switzerland.html',
   'dpill': 'Deadline 31 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-31'),
   'award': 'A 3\u20136 month full-time internship at WTO headquarters in Geneva with a daily allowance of CHF 60, open to nationals of WTO members and acceding countries.',
   'elig': 'Nationals of WTO members or acceding countries, aged 21\u201330, with a relevant undergraduate degree and at least one year of a Master\u2019s completed.',
   'tags': [('Internship', 'blue'), ('Switzerland', 'teal')]},
 'google-srp-2027': {'mono': 'GS', 'title': 'Google Student Researcher Program 2027 (Funded)',
   'href': 'google-student-researcher-program-2027.html',
   'dpill': 'Deadline 27 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-27'),
   'award': 'A paid research placement of about 12 weeks with Google Research, DeepMind or Google Cloud teams; deadlines are set per regional posting, not globally.',
   'elig': 'PhD students for the US Winter\u2013Summer 2027 posting; Bachelor\u2019s, Master\u2019s or PhD students for the EMEA posting, in computer science or a related field.',
   'tags': [('Research placement', 'purple'), ('USA & EMEA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Alabama
A.append(dict(
 slug='university-of-alabama-presidential-scholarship-2027-usa',
 title='University of Alabama Presidential Scholarship 2027 in USA (Fully Funded)',
 meta='University of Alabama Presidential Scholarship 2027: USD 28,000 a year for up to four years for out-of-state and international first-time freshmen. Deadline 4 December 2026 \u2014 eligibility, scores, how to apply and FAQs. Note: this is a partial merit award, not full funding.',
 short='University of Alabama Presidential Scholarship 2027', kicker='USA \u00b7 Bachelor\u2019s \u00b7 Merit scholarship', mono='AL',
 prov_short='University of Alabama', prov_cat='University \u00b7 United States',
 h1='University of Alabama Presidential Scholarship 2027 in USA (Fully Funded)',
 sub='The University of Alabama Presidential Scholarship 2027 gives out-of-state and international first-time freshmen USD 28,000 a year for up to four years, awarded automatically on admission with no separate scholarship application. Read the title with care: despite the \u201cfully funded\u201d label on the listing, this is a partial merit award \u2014 out-of-state tuition at Alabama is higher than USD 28,000 a year, so the award leaves a balance to cover. The only route in this programme that covers tuition in full is the Presidential Elite tier, which needs a 4.0 GPA and a perfect test score. The priority deadline is 4 December 2026.',
 dpill='Deadline 4 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-04'),
 facts=facts([('Award', 'USD 28,000 a year, renewable for up to four years, for out-of-state and international first-time freshmen. This is a partial merit award, not full funding: out-of-state tuition at the University of Alabama is higher than USD 28,000 a year, so the scholarship leaves tuition, fees, housing and living costs partly uncovered. The higher Presidential Elite tier covers tuition for up to four years (eight semesters), plus first-year on-campus housing at the regular room rate, a USD 1,500-a-year supplemental scholarship for four years and a one-time USD 2,000 allowance for research or international study.'),
              ('Eligible', 'Out-of-state and international students entering the University of Alabama as first-time freshmen in Summer or Fall 2027, with a minimum GPA of 3.50 and an SAT score of 1420\u20131600 or an ACT score of 32\u201336. Scores must be official and from a single test date \u2014 superscores are not used for automatic scholarships. Alabama residents have a separate award table with different thresholds. Admission to the university is test-optional, but test scores are required for automatic merit consideration.'),
              ('How', 'There is no separate scholarship application. Apply for undergraduate admission to the University of Alabama by 4 December 2026 and submit official ACT or SAT scores; eligible students are considered automatically and notified with their admission decision. A USD 50 application fee applies to international and out-of-state applicants.'),
              ('Deadline', '4 December 2026 \u2014 the Summer/Fall 2027 priority deadline. Some listings give 15 December 2026; the university\u2019s scholarship pages and the 2027-cycle guides give 4 December 2026, which is the date this article uses. The Spring 2027 deadline was 2 November 2026.'),
              ('Fine print', 'The Presidential Scholarship is renewable for up to four years, subject to the university\u2019s renewal conditions \u2014 check the renewal GPA and credit requirements on afford.ua.edu before relying on four years of funding. It is a tuition award: it does not cover housing, meals, books, travel or visa costs. The Presidential Elite tier is the only route in this programme that covers tuition in full, and it requires a 4.0 GPA alongside a perfect SAT 1600 or ACT 36.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Alabama</strong>, in Tuscaloosa, is a large public research university, and its <strong>Presidential Scholarship</strong> is the top tier of its automatic merit awards for students from outside the state. The idea is simple: strong school results and strong test scores earn a fixed annual award, with no essay, no interview and no separate scholarship form. If you are admitted and your scores clear the bar, the award follows automatically.</p>
      <p>That simplicity is also why the fine print matters. The award is <strong>USD 28,000 a year</strong>, and out-of-state tuition at Alabama runs higher than that, so the scholarship is a substantial discount rather than a free ride. Budget for the remaining tuition, plus housing, meals, books, travel and visa costs, before you apply. The exception is the <strong>Presidential Elite</strong> tier, which does cover tuition in full \u2014 but it asks for a perfect record: a 4.0 GPA and a perfect SAT 1600 or ACT 36, with housing and extra allowances on top.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>out-of-state or international student</strong> entering the University of Alabama as a <strong>first-time freshman</strong> in Summer or Fall 2027.</li>
        <li>Hold a minimum <strong>GPA of 3.50</strong>.</li>
        <li>Score <strong>SAT 1420\u20131600 or ACT 32\u201336</strong>, with official scores from a <strong>single test date</strong> \u2014 superscores are not used for automatic scholarships.</li>
        <li>Note that admission to the university is <strong>test-optional</strong>, but test scores are <strong>required</strong> for automatic merit consideration \u2014 an application without scores cannot earn this award.</li>
        <li>For the <strong>Presidential Elite</strong> tier: a <strong>4.0 GPA</strong> and a perfect <strong>SAT 1600 or ACT 36</strong>.</li>
        <li>Alabama residents are assessed under a <strong>separate award table</strong> with different thresholds.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>USD 28,000 a year</strong> towards tuition, renewable for up to <strong>four years</strong> (Presidential Scholarship).</li>
        <li><strong>Presidential Elite:</strong> tuition for up to four years (eight semesters), <strong>first-year on-campus housing</strong> at the regular room rate, a <strong>USD 1,500-a-year</strong> supplemental scholarship for four years, and a <strong>one-time USD 2,000</strong> allowance for research or international study.</li>
        <li><strong>No separate application</strong> \u2014 the award is considered automatically with the admission application.</li>
        <li>Notification with the <strong>admission decision</strong>, so you know the award before you commit.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>undergraduate admission application</strong> to the University of Alabama \u2014 this is the only application the scholarship needs.</li>
        <li><strong>Official ACT or SAT scores</strong>, sent from the testing agency, from a single test date.</li>
        <li>Your <strong>school transcripts</strong> as required by the admission application.</li>
        <li>The <strong>USD 50 application fee</strong> for international and out-of-state applicants.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check the automatic merit table on <strong>afford.ua.edu</strong> and confirm your GPA and test scores meet the Presidential tier.</li>
        <li>Submit your <strong>undergraduate admission application</strong> to the University of Alabama.</li>
        <li>Arrange for <strong>official ACT or SAT scores</strong> from a single test date to reach the university \u2014 do not rely on a superscore.</li>
        <li>Pay the <strong>USD 50 application fee</strong> and complete any remaining admission requirements.</li>
        <li>Watch for the <strong>admission decision</strong>, which carries the scholarship notification for eligible students.</li>
        <li>Apply by <strong>4 December 2026</strong>, the Summer/Fall 2027 priority deadline \u2014 do not use the 15 December date some listings give.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Alabama Presidential Scholarship fully funded?',
  'No. It pays USD 28,000 a year, which is less than out-of-state tuition at the University of Alabama, so it is a partial merit award. Only the Presidential Elite tier covers tuition in full, and that requires a 4.0 GPA and a perfect SAT 1600 or ACT 36.'),
 ('What scores do I need for the Presidential Scholarship?',
  'A GPA of 3.50 and an SAT score of 1420\u20131600 or an ACT score of 32\u201336, from a single test date. Superscores are not used for automatic scholarships.'),
 ('Do I need a separate scholarship application?',
  'No. Apply for undergraduate admission and submit official test scores; eligible students are considered automatically and notified with their admission decision.'),
 ('Can I use my superscore?',
  'No. The University of Alabama uses scores from a single test date for its automatic scholarships, and superscores are explicitly not used.'),
 ('What is the Presidential Elite tier?',
  'The top tier of the same programme: a 4.0 GPA and a perfect SAT 1600 or ACT 36 earns tuition for up to four years, first-year on-campus housing at the regular room rate, a USD 1,500-a-year supplemental scholarship for four years and a one-time USD 2,000 allowance for research or international study.'),
 ('What is the application deadline?',
  '4 December 2026, the Summer/Fall 2027 priority deadline. Some listings give 15 December 2026, but the university\u2019s scholarship pages and the 2027-cycle guides give 4 December 2026.')]) + '''
      <p class="verify">Verified 25 Oct 2026: afford.ua.edu (official, University of Alabama scholarships pages) \u2014 USD 28,000 a year, GPA 3.50, SAT 1420\u20131600 / ACT 32\u201336, single test date, superscores not used, no separate application, USD 50 application fee; vhtc.org, scholarshipsedge.com, nextdeadlines.com \u2014 priority deadline 4 December 2026 (not 15 December), Presidential Elite terms (4.0 GPA + SAT 1600/ACT 36, tuition for four years, first-year housing, USD 1,500 a year, one-time USD 2,000 allowance), Spring 2027 deadline 2 November 2026.</p>''',
 dl_long='4 December 2026 (Summer/Fall 2027 priority deadline)',
 offlinks=[('University of Alabama \u2014 Scholarships (official)', 'https://afford.ua.edu/'),
           ('Bright Scholarship \u2014 University of Alabama Presidential Scholarship 2027', 'https://brightscholarship.com/university-of-alabama-presidential-scholarship/')],
 related_titles=['richmond-2027', 'ursinus', 'msu-oos', 'dayton-merit'])),

# ---------------------------------------------------------------- 2. KUT SSP
A.append(dict(
 slug='kut-special-scholarship-program-2027-japan',
 title='KUT Special Scholarship Program 2027 in Japan (Fully Funded)',
 meta='KUT Special Scholarship Program 2027: a fully funded three-year English-taught PhD in Engineering at Kochi University of Technology \u2014 full fee exemption, JPY 150,000 monthly stipend and a one-off JPY 150,000 travel allowance. Next deadline 9 April 2027 \u2014 eligibility, projects, how to apply and FAQs.',
 short='KUT Special Scholarship Program 2027', kicker='Japan \u00b7 PhD \u00b7 Fully funded', mono='KU',
 prov_short='Kochi University of Technology', prov_cat='University \u00b7 Japan',
 h1='KUT Special Scholarship Program 2027 in Japan (Fully Funded)',
 sub='The KUT Special Scholarship Program 2027 funds a three-year English-taught PhD in Engineering at Kochi University of Technology, with every fee waived, a monthly stipend of JPY 150,000 and a one-off JPY 150,000 travel and settlement allowance. The first deadline for October 2027 enrolment (16 October 2026) has already passed; the still-open route is the second deadline, 9 April 2027. Before you apply, you must choose a project from the official SSP research project list and get the supervisor\u2019s approval \u2014 that step is part of the application, not an optional extra.',
 dpill='Deadline 9 Apr 2027 \u00b7 %d days left' % dl_left('2027-04-09'),
 facts=facts([('Award', 'A fully funded three-year English-taught PhD in Engineering at Kochi University of Technology. The scholarship waives the entrance examination fee (JPY 15,000), the enrolment fee (JPY 300,000) and tuition (JPY 535,800 a year) in full, pays a monthly stipend of JPY 150,000, and gives a one-off JPY 150,000 travel and settlement allowance to applicants coming from outside Japan.'),
              ('Eligible', 'International students of all nationalities holding a Master\u2019s degree (or equivalent) for doctoral study. Applicants must select a research project from the official SSP Research Project List and obtain the supervisor\u2019s approval before applying; KUT encourages the pre-application request at least eight weeks before the deadline. No Japanese language ability is required \u2014 the doctorate is taught in English.'),
              ('How', 'Submit the pre-application through KUT\u2019s online form, with your chosen project and supervisor approval, then send the formal application documents to KUT so they arrive by the deadline. The formal application pack follows the official SSP guidelines published on kut.ac.jp \u2014 check the current guidelines rather than any aggregator\u2019s document list.'),
              ('Deadline', '9 April 2027 \u2014 the second deadline for October 2027 enrolment. The earlier deadline, 16 October 2026 (for April 2027 intake and the first October 2027 window), has passed.'),
              ('Fine print', 'The stipend and allowances are tied to the SSP and the October 2027 intake; the project you choose determines your supervisor and research group, so a project without supervisor approval cannot proceed. Travel and settlement support is a one-off payment of JPY 150,000 for applicants outside Japan, not a recurring allowance.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Kochi University of Technology (KUT)</strong>, on the island of Shikoku, runs one of Japan\u2019s most generous doctoral scholarships for international students. The <strong>Special Scholarship Program (SSP)</strong> is built around a simple idea: the university publishes a list of research projects, each with a named supervisor, and international Master\u2019s graduates apply to work on one of them. The doctorate is taught entirely in English, and the funding covers everything a student needs to live and study \u2014 fees, a monthly stipend and a travel allowance.</p>
      <p>The funding is genuinely full: the entrance examination fee, the enrolment fee and three years of tuition are all waived, the stipend is <strong>JPY 150,000 a month</strong>, and applicants from outside Japan receive a <strong>one-off JPY 150,000</strong> for travel and settling in. The catch is the structure \u2014 you do not apply to KUT in general, you apply to a specific project with a specific supervisor, and that supervisor must approve you before the formal application goes in. Start that conversation early: KUT itself suggests the pre-application request at least eight weeks before the deadline.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> of any nationality.</li>
        <li>Hold a <strong>Master\u2019s degree (or equivalent)</strong> for doctoral study.</li>
        <li>Select a research project from the <strong>official SSP Research Project List</strong> and obtain the <strong>supervisor\u2019s approval</strong> before applying.</li>
        <li>Submit the <strong>pre-application request</strong> \u2014 KUT encourages this at least <strong>eight weeks before the deadline</strong>.</li>
        <li><strong>No Japanese is required</strong> \u2014 the PhD is taught in English.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Full exemption from the <strong>entrance examination fee (JPY 15,000)</strong>.</li>
        <li>Full exemption from the <strong>enrolment fee (JPY 300,000)</strong>.</li>
        <li>Full exemption from <strong>tuition (JPY 535,800 a year)</strong> for three years.</li>
        <li>A <strong>monthly stipend of JPY 150,000</strong>.</li>
        <li>A <strong>one-off JPY 150,000 travel and settlement allowance</strong> for applicants from outside Japan.</li>
        <li>A <strong>three-year English-taught PhD in Engineering</strong> with a named supervisor and research group.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your chosen project from the <strong>official SSP Research Project List</strong>, with the <strong>supervisor\u2019s approval</strong>.</li>
        <li>The <strong>pre-application</strong> submitted through KUT\u2019s online form.</li>
        <li>The <strong>formal application documents</strong> as set out in the official SSP guidelines on kut.ac.jp \u2014 use the current guidelines, not an aggregator\u2019s list, and make sure the pack reaches KUT by the deadline.</li>
        <li>Proof of your <strong>Master\u2019s degree (or equivalent)</strong> as required by the guidelines.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the <strong>official SSP pages on kut.ac.jp</strong> and open the current <strong>SSP Research Project List</strong>.</li>
        <li>Choose a project that matches your background and <strong>contact the supervisor</strong> \u2014 you need their approval before you can apply. Do this at least eight weeks before the deadline.</li>
        <li>Submit the <strong>pre-application</strong> through KUT\u2019s online form.</li>
        <li>Prepare the <strong>formal application documents</strong> exactly as the official SSP guidelines specify.</li>
        <li>Send the formal application so it <strong>reaches KUT by 9 April 2027</strong> for the October 2027 intake.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the KUT Special Scholarship Program fully funded?',
  'Yes. It waives the entrance examination fee, the enrolment fee and three years of tuition, pays a monthly stipend of JPY 150,000, and gives a one-off JPY 150,000 travel and settlement allowance to applicants from outside Japan.'),
 ('What is the deadline for the KUT SSP 2027?',
  '9 April 2027, the second deadline for October 2027 enrolment. The earlier deadline, 16 October 2026, has already passed.'),
 ('Do I need to know Japanese?',
  'No. The SSP doctorate is taught in English and no Japanese language ability is required.'),
 ('Do I need a supervisor before I apply?',
  'Yes. You must select a project from the official SSP Research Project List and obtain the supervisor\u2019s approval before applying. KUT encourages the pre-application request at least eight weeks before the deadline.'),
 ('How long is the PhD and what does the stipend cover?',
  'Three years. The JPY 150,000 monthly stipend is for living costs, and the one-off JPY 150,000 allowance covers travel to Japan and settling in.')]) + '''
      <p class="verify">Verified 25 Oct 2026: kut.ac.jp (official, KUT SSP pages) \u2014 programme structure, project list and supervisor approval; ResearchersJob, Global Scholarship Point, Fully Scholarships \u2014 admission schedule (16 October 2026 and 9 April 2027 deadlines), fee figures (JPY 15,000 / JPY 300,000 / JPY 535,800 a year), JPY 150,000 monthly stipend, one-off JPY 150,000 travel allowance, eight-week pre-application guidance. The formal document list is stated per the official SSP guidelines only, as aggregator lists were not fully confirmed.</p>''',
 dl_long='9 April 2027 (second deadline, October 2027 enrolment)',
 offlinks=[('Kochi University of Technology \u2014 Special Scholarship Program (official)', 'https://www.kut.ac.jp/'),
           ('Bright Scholarship \u2014 KUT Special Scholarship Program 2027', 'https://brightscholarship.com/kut-special-scholarship-program-2027-japan/')],
 related_titles=['saitama-mext-2027', 'u-tokyo-mext', 'nims2026', 'tigp-2027'])),

# ---------------------------------------------------------------- 3. KAUST
A.append(dict(
 slug='king-abdullah-university-scholarship-2027-saudi-arabia',
 title='King Abdullah University Scholarship 2027 in Saudi Arabia (Fully Funded)',
 meta='King Abdullah University Scholarship 2027: the KAUST Fellowship for MS, MS/PhD and PhD study \u2014 full tuition, living allowance, free housing, medical cover, relocation support and an annual flight home. Fall 2027 deadline 3 January 2027 \u2014 eligibility, documents, how to apply and FAQs.',
 short='King Abdullah University Scholarship 2027', kicker='Saudi Arabia \u00b7 Master\u2019s & PhD \u00b7 Fully funded', mono='KA',
 prov_short='King Abdullah University of Science and Technology', prov_cat='University \u00b7 Saudi Arabia',
 h1='King Abdullah University Scholarship 2027 in Saudi Arabia (Fully Funded)',
 sub='The King Abdullah University Scholarship 2027 is the KAUST Fellowship, and it works differently from most scholarships on this site: there is no separate scholarship application. Every student admitted to a KAUST Master\u2019s or PhD programme receives the fellowship automatically, covering full tuition, a living allowance, free on-campus housing, medical and dental cover, relocation support and an annual return flight home. The Fall 2027 deadline is 3 January 2027 \u2014 the Spring 2027 PhD-only deadline (27 September 2026) has already passed.',
 dpill='Deadline 3 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-03'),
 facts=facts([('Award', 'The KAUST Fellowship, awarded automatically to every admitted student \u2014 no separate scholarship application. It covers full tuition and bench fees (up to about USD 35,000 a year), a living allowance of about USD 20,000 a year for MS students and USD 25,000\u201330,000 a year for PhD students, free on-campus housing, medical and dental cover, relocation support and an annual return flight home. Scholarship guides put the total package at roughly USD 70,000\u201380,000 a year.'),
              ('Eligible', 'All nationalities. A Bachelor\u2019s degree in a relevant STEM field is required for MS entry; a Master\u2019s degree (or a Bachelor\u2019s for the MS/PhD track) for PhD entry. Applicants need a minimum GPA of 3.0/4.0 and English proficiency of IELTS 6.5 or TOEFL iBT 79\u201381, with exemptions where applicable. Applicants must be at least 18 at entry. The GRE is not required but is encouraged.'),
              ('How', 'Apply online through the official KAUST admissions portal (admissions.kaust.edu.sa) by 3 January 2027 for Fall 2027 entry. Scholarship consideration is automatic with the admission application \u2014 there is no separate fellowship form to fill in.'),
              ('Deadline', '3 January 2027 for Fall 2027 entry (MS, MS/PhD and PhD). The Spring 2027 PhD-only deadline, 27 September 2026, has passed. The Fall 2027 semester begins on 29 August 2027.'),
              ('Fine print', 'The fellowship is tied to admission: only admitted students receive it, and it is assessed as part of the admission decision. The living allowance differs by level \u2014 about USD 20,000 a year for MS students and USD 25,000\u201330,000 a year for PhD students \u2014 so check the level you are applying for. English test exemptions apply in some cases; confirm your position on the official admissions pages.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>King Abdullah University of Science and Technology (KAUST)</strong>, on the Red Sea coast of Saudi Arabia, is a graduate-only research university, and its scholarship model is unusually simple: there is no scholarship competition to enter. The <strong>KAUST Fellowship</strong> is awarded automatically to every student admitted to an MS, MS/PhD or PhD programme, which means the real contest is the admission decision itself. Apply well, and the funding follows.</p>
      <p>The package is comprehensive. Beyond full tuition and bench fees, it pays a <strong>living allowance</strong> (about USD 20,000 a year for MS students and USD 25,000\u201330,000 a year for PhD students), provides <strong>free on-campus housing</strong>, covers <strong>medical and dental care</strong>, and adds <strong>relocation support</strong> and an <strong>annual return flight home</strong>. Scholarship guides value the whole package at roughly USD 70,000\u201380,000 a year. Because the fellowship is automatic, the application effort goes entirely into the admission file \u2014 transcripts, test scores, references and a statement of purpose.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>all nationalities</strong>.</li>
        <li>For <strong>MS entry</strong>: a Bachelor\u2019s degree in a relevant STEM field.</li>
        <li>For <strong>PhD entry</strong>: a Master\u2019s degree, or a Bachelor\u2019s degree for the MS/PhD track.</li>
        <li>A minimum <strong>GPA of 3.0/4.0</strong>.</li>
        <li>English proficiency of <strong>IELTS 6.5 or TOEFL iBT 79\u201381</strong>, with exemptions where applicable.</li>
        <li>Applicants must be at least <strong>18 years old</strong> at entry.</li>
        <li>The <strong>GRE is not required</strong> but is encouraged.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and bench fees</strong> (up to about USD 35,000 a year).</li>
        <li>A <strong>living allowance</strong> of about USD 20,000 a year (MS) or USD 25,000\u201330,000 a year (PhD).</li>
        <li><strong>Free on-campus housing</strong>.</li>
        <li><strong>Medical and dental cover</strong>.</li>
        <li><strong>Relocation support</strong> and an <strong>annual return flight home</strong>.</li>
        <li><strong>No separate scholarship application</strong> \u2014 the fellowship is automatic for admitted students.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Transcripts</strong> from previous degrees.</li>
        <li>An up-to-date <strong>CV</strong>.</li>
        <li>A <strong>statement of purpose</strong>.</li>
        <li>Contact details for <strong>three referees</strong>.</li>
        <li>An <strong>English test score</strong> (IELTS 6.5 or TOEFL iBT 79\u201381), unless exempt.</li>
        <li>A <strong>passport or national ID</strong>.</li>
        <li>GRE scores, if you have them \u2014 encouraged but not required.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check the <strong>official KAUST admissions pages</strong> (admissions.kaust.edu.sa) for the programme and entry requirements of your chosen degree.</li>
        <li>Prepare your <strong>transcripts, CV, statement of purpose</strong> and <strong>three referee contacts</strong>, and take the English test if you need one.</li>
        <li>Submit your application through the <strong>official KAUST admissions portal</strong>.</li>
        <li>Remember there is <strong>no separate scholarship form</strong> \u2014 the KAUST Fellowship is considered automatically with your admission application.</li>
        <li>Apply by <strong>3 January 2027</strong> for Fall 2027 entry; the semester begins on 29 August 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a separate application for the KAUST Fellowship?',
  'No. The KAUST Fellowship is awarded automatically to every admitted student. You apply for admission to KAUST, and the fellowship follows the admission decision.'),
 ('What does the KAUST Fellowship cover?',
  'Full tuition and bench fees, a living allowance (about USD 20,000 a year for MS students and USD 25,000\u201330,000 a year for PhD students), free on-campus housing, medical and dental cover, relocation support and an annual return flight home.'),
 ('What is the deadline for Fall 2027 entry?',
  '3 January 2027 for MS, MS/PhD and PhD programmes. The Spring 2027 PhD-only deadline, 27 September 2026, has already passed.'),
 ('What GPA and English scores does KAUST require?',
  'A minimum GPA of 3.0/4.0 and English proficiency of IELTS 6.5 or TOEFL iBT 79\u201381, with exemptions where applicable. The GRE is not required but is encouraged.'),
 ('Who can apply?',
  'Students of all nationalities with a Bachelor\u2019s degree in a relevant STEM field (MS) or a Master\u2019s degree (PhD), who are at least 18 at entry.')]) + '''
      <p class="verify">Verified 25 Oct 2026: admissions.kaust.edu.sa (official KAUST admissions portal) \u2014 MS, MS/PhD and PhD entry, fellowship automatic for admitted students; Opportunities Nexus, EduTimes Africa, Opportunities for Youth \u2014 Fall 2027 deadline 3 January 2027 (Spring 2027 PhD-only deadline 27 September 2026 passed), fellowship value breakdown (tuition and bench fees up to about USD 35,000 a year, living allowance about USD 20,000 a year MS / USD 25,000\u201330,000 a year PhD, housing, medical and dental cover, relocation, annual flight home), GPA 3.0/4.0, IELTS 6.5 / TOEFL iBT 79\u201381, documents list, semester begins 29 August 2027.</p>''',
 dl_long='3 January 2027 (Fall 2027 entry)',
 offlinks=[('KAUST \u2014 Admissions (official)', 'https://admissions.kaust.edu.sa/'),
           ('Bright Scholarship \u2014 King Abdullah University Scholarship 2027', 'https://brightscholarship.com/king-abdullah-university-scholarship/')],
 related_titles=['kaust-vsrp', 'qassim', 'mbzuai', 'auc-fellow-2027'])),

# ---------------------------------------------------------------- 4. WTO
A.append(dict(
 slug='world-trade-organization-internship-2027-switzerland',
 title='World Trade Organization Internship 2027 in Switzerland (Without IELTS)',
 meta='World Trade Organization Internship 2027: a 3\u20136 month full-time internship at WTO headquarters in Geneva with a daily allowance of CHF 60. Current requisition closes 31 December 2026 \u2014 eligibility, tracks, how to apply and FAQs.',
 short='World Trade Organization Internship 2027', kicker='Switzerland \u00b7 Internship \u00b7 Paid', mono='WT',
 prov_short='World Trade Organization', prov_cat='International Organisation \u00b7 Switzerland',
 h1='World Trade Organization Internship 2027 in Switzerland (Without IELTS)',
 sub='The World Trade Organization Internship 2027 is a three- to six-month, full-time placement at WTO headquarters in Geneva, paying a daily allowance of CHF 60. The current general-programme requisition closes on 31 December 2026 at 11:59 p.m. Geneva time, and the programme runs on a rolling roster after that. A note on the title: WTO asks for no IELTS or TOEFL score as part of its application \u2014 language ability is assessed through the application itself \u2014 but \u201cwithout IELTS\u201d is an aggregator\u2019s phrase, not a WTO promise, and this article does not present it as a special feature.',
 dpill='Deadline 31 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-31'),
 facts=facts([('Award', 'A daily allowance of CHF 60 under the general programme, including weekends and holidays, for a full-time internship of three to six months at WTO headquarters in Geneva. Two specialist tracks pay more: the China\u2019s LDCs and Accessions Programme pays CHF 90 a day plus a return airfare and a CHF 100-a-month health-insurance contribution, and runs for up to ten months; the doctoral support programme also covers travel. Travel to and from Geneva is not covered under the general programme, and interns arrange their own health and accident insurance.'),
              ('Eligible', 'Nationals of a WTO member country or of a country or customs territory negotiating accession. Applicants must be at least 21 at the start of the internship and no older than 30, and must hold a relevant undergraduate degree plus at least one completed year of a Master\u2019s programme, or have completed a Master\u2019s and be enrolled in higher postgraduate study, or have completed a Master\u2019s or PhD within two years of selection.'),
              ('How', 'Apply online through the WTO external jobs platform (wto.wd3.myworkdayjobs.com/External). The general programme runs on a rolling roster: suitable candidates join a one-year roster, and the current requisition (JR103985) closes on 31 December 2026 at 11:59 p.m. Geneva time. Programme details are published at wto.org/english/thewto_e/vacan_e/iypp_e.htm.'),
              ('Deadline', '31 December 2026, 11:59 p.m. Geneva time \u2014 the cut-off for the current general-programme requisition (JR103985). The programme itself is rolling, with suitable candidates held on a one-year roster.'),
              ('Fine print', 'This is a paid internship, not a scholarship or a degree programme, and it does not lead to WTO employment. Under the general programme, the CHF 60 daily allowance is the only payment \u2014 there is no airfare, and interns must arrange their own health and accident insurance and their own travel to Geneva. WTO does not require an IELTS or TOEFL score.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>World Trade Organization (WTO)</strong>, based in Geneva, runs its internship programme for students and recent graduates who want to work inside the organisation that sets the rules of world trade. Interns join a division for <strong>three to six months</strong> of full-time work, supporting the WTO\u2019s work on trade policy, dispute settlement, accessions or development \u2014 and the experience carries weight well beyond the placement itself, because WTO internships are one of the few routes into the trade-policy world for early-career professionals from member countries.</p>
      <p>The programme is paid, but modestly: the general track pays <strong>CHF 60 a day</strong>, including weekends and holidays, and does not cover travel to Geneva or health insurance. Two specialist tracks are more generous \u2014 the China\u2019s LDCs and Accessions Programme pays <strong>CHF 90 a day plus a return airfare</strong> and runs for up to ten months, and the doctoral support programme also covers travel. Applications run on a <strong>rolling roster</strong>, so the 31 December 2026 date is the cut-off for the current requisition rather than the end of the programme.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a national of a <strong>WTO member country</strong> or of a country or customs territory <strong>negotiating accession</strong> to the WTO.</li>
        <li>Be at least <strong>21 years old</strong> at the start of the internship and <strong>no older than 30</strong>.</li>
        <li>Hold a relevant <strong>undergraduate degree</strong> and have completed at least <strong>one year of a Master\u2019s programme</strong>; or have completed a Master\u2019s and be enrolled in <strong>higher postgraduate study</strong>; or have completed a Master\u2019s or PhD <strong>within two years</strong> of selection.</li>
        <li>Be available for a <strong>full-time</strong> placement in Geneva of three to six months (up to ten months on the China\u2019s LDCs and Accessions track).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>daily allowance of CHF 60</strong> under the general programme, including weekends and holidays.</li>
        <li><strong>CHF 90 a day plus a return airfare</strong> and a <strong>CHF 100-a-month health-insurance contribution</strong> under the China\u2019s LDCs and Accessions Programme (up to ten months).</li>
        <li><strong>Travel cover</strong> under the doctoral support programme.</li>
        <li>A <strong>full-time placement at WTO headquarters in Geneva</strong>, working inside the organisation that governs world trade.</li>
        <li>Experience that counts towards a career in <strong>trade policy, international law or development</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An <strong>online application</strong> through the WTO external jobs platform.</li>
        <li>A current <strong>CV</strong>.</li>
        <li>A <strong>motivation letter</strong> for the specific track you apply to.</li>
        <li>Proof of your <strong>degree and enrolment status</strong> as set out in the requisition instructions \u2014 check the exact list on the posting you apply to, as it varies by track.</li>
        <li>No <strong>IELTS or TOEFL score</strong> is required by WTO.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the programme information on the <strong>WTO website</strong> (wto.org/english/thewto_e/vacan_e/iypp_e.htm) and decide which track fits you \u2014 general, China\u2019s LDCs and Accessions, or doctoral support.</li>
        <li>Open the <strong>WTO external jobs platform</strong> (wto.wd3.myworkdayjobs.com/External) and find the current internship requisition.</li>
        <li>Prepare your <strong>CV and motivation letter</strong>, tailored to the track and the division you want to join.</li>
        <li>Submit the <strong>online application</strong> before the requisition closes.</li>
        <li>Apply by <strong>31 December 2026 at 11:59 p.m. Geneva time</strong> for the current general-programme requisition (JR103985) \u2014 suitable candidates are held on a one-year roster.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How much does the WTO internship pay?',
  'CHF 60 a day under the general programme, including weekends and holidays. The China\u2019s LDCs and Accessions Programme pays CHF 90 a day plus a return airfare and a CHF 100-a-month health-insurance contribution, and runs for up to ten months.'),
 ('What is the deadline for the WTO Internship 2027?',
  '31 December 2026 at 11:59 p.m. Geneva time, for the current general-programme requisition (JR103985). The programme itself is rolling, with suitable candidates held on a one-year roster.'),
 ('Do I need IELTS for the WTO internship?',
  'No. WTO does not require an IELTS or TOEFL score as part of its application. Language ability is assessed through the application itself.'),
 ('Who can apply?',
  'Nationals of WTO member countries or of countries or customs territories negotiating accession, aged 21 to 30, with a relevant undergraduate degree and at least one year of a Master\u2019s completed, or an equivalent postgraduate position.'),
 ('Does the WTO internship cover travel to Geneva?',
  'Not under the general programme \u2014 interns arrange and pay for their own travel and their own health and accident insurance. The China\u2019s LDCs and Accessions Programme covers the return airfare, and the doctoral support programme also covers travel.')]) + '''
      <p class="verify">Verified 25 Oct 2026: wto.org (official, WTO internship programme page) \u2014 programme structure and tracks; Opportunities Home, Scholarships.af, Opportunities Feed \u2014 current requisition JR103985, deadline 31 December 2026 at 11:59 p.m. Geneva time, CHF 60 a day (general) and CHF 90 a day plus airfare and CHF 100 a month health-insurance contribution (China\u2019s LDCs and Accessions), 3\u20136 months general programme (up to 10 months LDCs track), rolling one-year roster, age 21\u201330, degree and enrolment requirements. "Without IELTS" is aggregator framing, not a WTO term; WTO requires no language test.</p>''',
 dl_long='31 December 2026, 11:59 p.m. Geneva time (current requisition JR103985)',
 offlinks=[('World Trade Organization \u2014 Internship Programme (official)', 'https://www.wto.org/english/thewto_e/vacan_e/iypp_e.htm'),
           ('WTO \u2014 External Jobs Platform (official)', 'https://wto.wd3.myworkdayjobs.com/External'),
           ('Bright Scholarship \u2014 World Trade Organization Internship 2027', 'https://brightscholarship.com/world-trade-organization-internship-2027/')],
 related_titles=['oecd', 'unicef-2026', 'un-ypp-2026', 'lawai-2027'])),

# ---------------------------------------------------------------- 5. Google SRP
A.append(dict(
 slug='google-student-researcher-program-2027',
 title='Google Student Researcher Program 2027 (Funded)',
 meta='Google Student Researcher Program 2027: a paid research placement of about 12 weeks with Google Research, DeepMind or Google Cloud teams. Deadlines are per regional posting \u2014 the November 2026 posting closes 27 November 2026 \u2014 eligibility, how to apply and FAQs.',
 short='Google Student Researcher Program 2027', kicker='USA & EMEA \u00b7 Research placement \u00b7 Paid', mono='GS',
 prov_short='Google', prov_cat='Company \u00b7 United States',
 h1='Google Student Researcher Program 2027 (Funded)',
 sub='The Google Student Researcher Program 2027 is a paid research placement of about twelve weeks, working with Google Research, DeepMind or Google Cloud teams on a live research project. There is one thing to understand before anything else: there is no single global deadline. Deadlines are set per regional posting \u2014 the posting that matches this listing\u2019s November 2026 date closes on 27 November 2026, the EMEA posting closes on 13 December 2026, and the US PhD Winter\u2013Summer 2027 posting has an anticipated deadline of 16 July 2027. Apply to the posting for your region and use its date, not the headline date.',
 dpill='Deadline 27 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-27'),
 facts=facts([('Award', 'A paid research placement of about 12 weeks with Google Research, DeepMind or Google Cloud teams, with flexible duration, hours and working arrangements. The US posting lists a base salary range of USD 118,000\u2013157,000 a year \u2014 that is an annualised salary figure for the role as posted, not a lump-sum stipend, and it should not be read as the amount a student researcher is paid for twelve weeks.'),
              ('Eligible', 'Eligibility varies by posting. The US Winter\u2013Summer 2027 posting is for PhD students only. The EMEA posting is open to Bachelor\u2019s, Master\u2019s or PhD students enrolled in accredited programmes in Europe, the Middle East and Africa. Other postings ask for a PhD or Master\u2019s in computer science or a related field, with experience in at least one area such as machine learning, AI, natural language processing, computer vision, quantum computing or data science, prior research experience and programming skills (Python, Java, JavaScript, C or C++).'),
              ('How', 'Apply online through Google Careers, on the Student Researcher posting for your region. Applications are reviewed on a rolling basis and postings can close early if projects fill, so apply as soon as your file is ready rather than waiting for the deadline.'),
              ('Deadline', 'There is no single deadline. The November 2026 posting closes on 27 November 2026; the EMEA posting closes on 13 December 2026; the US posting \u201cStudent Researcher, PhD, Winter\u2013Summer 2027\u201d has an anticipated deadline of 16 July 2027, with start dates from January to August 2027. Check the deadline printed on the specific posting you apply to.'),
              ('Fine print', 'This is a paid work placement, not a conventional scholarship: you are hired into a research team for about twelve weeks, and the terms \u2014 duration, hours, location and pay \u2014 are set by the posting. The USD 118,000\u2013157,000 figure is an annualised salary range on the US posting, not a stipend. Postings are reviewed on a rolling basis and may close early.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Google Student Researcher Program</strong> places students inside Google\u2019s research organisation for about <strong>twelve weeks</strong>, working on a real project with a Google Research, DeepMind or Google Cloud team. It is not a scholarship in the usual sense \u2014 it is a paid research placement, closer to a research internship, and it is judged the way a research job is judged: on your prior research, your technical skills and the fit between your background and the project.</p>
      <p>The programme is organised as separate <strong>regional postings</strong>, and that is the detail that matters most. The US posting for PhD students (Winter\u2013Summer 2027) has start dates from January to August 2027 and an anticipated deadline of <strong>16 July 2027</strong>; the EMEA posting closes on <strong>13 December 2026</strong>; and the posting behind this listing\u2019s November date closes on <strong>27 November 2026</strong>. Because applications are reviewed on a <strong>rolling basis</strong> and postings can close early when projects fill, the practical deadline is sooner than the printed one \u2014 apply as soon as your file is ready.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be enrolled as a student in a relevant field \u2014 the exact level depends on the posting: the <strong>US Winter\u2013Summer 2027 posting is for PhD students only</strong>, while the <strong>EMEA posting</strong> is open to <strong>Bachelor\u2019s, Master\u2019s or PhD students</strong> in accredited programmes in Europe, the Middle East and Africa.</li>
        <li>Study <strong>computer science or a related field</strong>, with experience in at least one area such as machine learning, AI, natural language processing, computer vision, quantum computing or data science.</li>
        <li>Have <strong>prior research experience</strong> and <strong>programming skills</strong> (Python, Java, JavaScript, C or C++).</li>
        <li>Be able to commit to a placement of about <strong>twelve weeks</strong>, with the flexible duration, hours and working arrangements the posting allows.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>paid research placement of about 12 weeks</strong> with Google Research, DeepMind or Google Cloud teams.</li>
        <li>Work on a <strong>live research project</strong> alongside Google researchers, with flexible duration, hours and working arrangements.</li>
        <li>The US posting lists a <strong>base salary range of USD 118,000\u2013157,000 a year</strong> \u2014 an annualised figure for the role as posted, not a lump-sum stipend.</li>
        <li>Experience inside one of the world\u2019s largest research organisations, which carries weight for a research career or a PhD application.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A current <strong>CV</strong> setting out your research experience and technical skills.</li>
        <li>A current or recent <strong>academic transcript in English</strong>.</li>
        <li>Note: the CV and transcript requirement is as given in the posting guides \u2014 confirm the exact document list on the Google Careers posting you apply to, as it can vary by region.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open <strong>Google Careers</strong> and find the <strong>Student Researcher</strong> posting for your region \u2014 US (PhD, Winter\u2013Summer 2027) or EMEA, or the current November 2026 posting.</li>
        <li>Read the posting carefully: the <strong>deadline, eligibility level and start dates</strong> are set per posting, and they differ.</li>
        <li>Prepare your <strong>CV and academic transcript</strong>, and make sure your research experience and programming skills are easy to see.</li>
        <li>Submit the <strong>online application</strong> through Google Careers.</li>
        <li>Apply early \u2014 applications are reviewed on a <strong>rolling basis</strong> and postings can close before the printed deadline if projects fill. The November 2026 posting closes on <strong>27 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Google Student Researcher Program a scholarship?',
  'Not in the usual sense. It is a paid research placement of about twelve weeks with Google Research, DeepMind or Google Cloud teams, judged on your prior research and technical skills.'),
 ('What is the deadline?',
  'There is no single deadline. The November 2026 posting closes on 27 November 2026, the EMEA posting on 13 December 2026, and the US PhD Winter\u2013Summer 2027 posting has an anticipated deadline of 16 July 2027. Use the deadline on the posting you apply to.'),
 ('Who can apply?',
  'It depends on the posting. The US Winter\u2013Summer 2027 posting is for PhD students only; the EMEA posting is open to Bachelor\u2019s, Master\u2019s or PhD students in accredited programmes in Europe, the Middle East and Africa. All postings ask for computer science or a related field, prior research experience and programming skills.'),
 ('How much does it pay?',
  'The US posting lists a base salary range of USD 118,000\u2013157,000 a year. That is an annualised salary figure for the role as posted, not a lump-sum stipend for twelve weeks.'),
 ('Do I need a PhD to apply?',
  'Not for every posting. The EMEA posting accepts Bachelor\u2019s and Master\u2019s students as well as PhD students; the US Winter\u2013Summer 2027 posting is PhD-only.')]) + '''
      <p class="verify">Verified 25 Oct 2026: careers.google.com (official Google Careers postings) \u2014 Student Researcher, PhD, Winter\u2013Summer 2027 and Student Researcher, 2027 (EMEA) postings exist for 2027; Global South Opportunities / CareerGlobalConnect \u2014 US posting anticipated deadline 16 July 2027, rolling review, January\u2013August 2027 starts, USD 118,000\u2013157,000 annualised salary range; Opportunities for Youth / LinkedIn \u2014 EMEA deadline 13 December 2026, Bachelor\u2019s/Master\u2019s/PhD eligibility, rolling review; November 2026 posting deadline 27 November 2026. The CV and transcript requirement is per posting guides and was not confirmed from the official page snippet.</p>''',
 dl_long='27 November 2026 (November 2026 posting; other regional postings close 13 December 2026 and 16 July 2027)',
 offlinks=[('Google Careers \u2014 Student Researcher, PhD, Winter\u2013Summer 2027 (official)', 'https://careers.google.com/jobs/results/134313315235963590'),
           ('Google Careers \u2014 Student Researcher, 2027 (official)', 'https://careers.google.com/jobs/results/86733690079453894'),
           ('Bright Scholarship \u2014 Google Student Researcher Program 2027', 'https://brightscholarship.com/google-student-researcher-program-2027/')],
 related_titles=['nvidia-amri-2027', 'nvidia-2027', 'lawai-2027', 'kaist-grad-2027'])),

for a in A: _split_verify(a)
sizes = {}
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch49_built.json','w'))

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

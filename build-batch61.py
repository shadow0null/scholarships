#!/usr/bin/env python3
"""Batch 61 (cron run 61, 28 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Rowland Fellowships 2027 at Harvard - SKIPPED: deadline passed
   1 Aug 2026, 11:59 PM EDT (letters due 15 Aug 2026).
2. Osaka University MEXT Scholarship 2026 - SKIPPED: deadline passed
   1 Sep 2026 (LoA request deadline via AAD for AY2027).
3. Embassy of Japan Scholarships 2026 - SKIPPED: listicle (9+ schemes,
   "Last date: Different"); underlying MEXT 2026 embassy cycle closed
   (India deadline 13 May 2026).
4. Netflix Internship Program 2026 - SKIPPED: 2026 cycle closed
   (internships ran May-Aug 2026); rolling listings, no single deadline
   or confirmed 2027 call.
5. Bank of America Summer Internships 2026 - SKIPPED: deadline passed
   (EMEA 2026 cycle closed 11 Oct 2026; US window closed Mar 2026).
6. Chulabhorn Graduate Institute Scholarship 2027 - SKIPPED: deadline
   passed 31 Aug 2026 (official CGI page).
7. 5000 Scholarships in Turkey Without IELTS 2026 - SKIPPED: listicle.
8. Leipzig University DAAD EPOS SEPT Scholarship 2027 - SKIPPED:
   deadline passed 1 Oct 2026 (official Leipzig page).
9. Abroad Studies Scholarship 2026 - SKIPPED: listicle (9 schemes).
10. McGill University Scholarships 2026 - SKIPPED: family/umbrella label,
    no single fully funded scheme (closest single scheme: McGill Major
    Entrance Scholarships, deadline 21 Jan 2027, partial award CAD
    3,000-12,000/year - kept as spare for a future run).
11. Deakin University Scholarship 2027 - SKIPPED: deadline passed
    (international round 23 Aug 2026; domestic round 25 Oct 2026).
12. FBI Honors Internships 2027 - VERIFIED (deadline 2 Nov 2026,
    11:59 PM ET; official fbijobs.gov page).
13. 10 Best Scholarships in Greece 2026 - SKIPPED: listicle.
14. King Saud University Scholarship 2026 - SKIPPED: deadline passed
    (21 May 2026); other tracks conflict, no single current deadline.
15. Hubei Provincial Scholarships 2026 - SKIPPED: new-student deadline
    passed 30 Jun 2026; no official source; UG award conflicts
    (5,000 vs 10,000 RMB/year).
16. Eric Bleumink Fellowship 2027 - SKIPPED: DUPLICATE of the already
    published Eric Bleumink Scholarship 2027 article (same scheme,
    written in an earlier batch; queue carries both titles). A draft
    article was built and then DELETED, its registry card and INFO
    entry removed, and the original 'bleumink-2027' card restored.
    NOTE: the wave-3 fact sheet claimed no cash figure is published;
    the earlier batch verified the official Ubbo Emmius Fund figure
    of a EUR 15,000 grant - the wave-3 claim is wrong, do not reuse.
17. University Of Florence Scholarships 2026 - SKIPPED: family/umbrella
    label, no single scheme.
18. University of Glasgow Global Leadership Scholarships 2026 -
    VERIFIED as the 2027/28 cycle (retitled; 350 awards, GBP 10,000
    tuition waiver; rolling; official gla.ac.uk page).
19. 600 Graduate Research Scholarships 2027 - VERIFIED as the
    University of Melbourne Graduate Research Scholarships (retitled;
    deadline 31 Oct 2026; AUD 41,100/year 2027 stipend; official
    scholarships.unimelb.edu.au page).
20. NASA OSTEM Internship Program 2026 - SKIPPED: 2026 cycle closed
    (Summer 27 Feb 2026; Fall 22 May 2026); next open session Summer
    2027, deadline 1 Mar 2027 - kept as spare for a 2027 retitle.
21. RIFS Fellowship Program 2027 - SKIPPED: deadline passed
    21 Jun 2026, 23:59 CET (official RIFS call page).
22. Hokkaido University MEXT Scholarships 2027 - VERIFIED (three
    tracks: e3 Engineering 20-29 Oct 2026; IGP Life Science supervisor
    contact by 10 Nov 2026; IGC-DHS Science 1 Oct-15 Nov 2026;
    official Hokkaido pages).
23. Study in Singapore Without IELTS 2026 - SKIPPED: listicle.
24. Interpol Internships 2026 - VERIFIED as a rolling programme
    (EUR 700/month; per-vacancy deadlines; official interpol.int
    page) - kept as spare; not written this run.
25. Abdulhadi H Taher Endowed Scholarships 2026 - SKIPPED: deadline
    passed 1 Jun 2026 (AUC Fall 2026 admission deadline).
Wave 4 (replacement for the Bleumink duplicate):
26. Malta Government Endeavour Scholarship 2026-27 - SKIPPED: deadline
    passed 5 Jun 2026, 12:00 noon Malta time (Endeavour II, 5th Call).
27. Atlantic Dialogues Emerging Leaders Program 2026 - SKIPPED:
    deadline passed 14 Jun 2026 (programme 6-10 Dec 2026, Rabat).
28. Bond University Transformer Scholarship 2026 - SKIPPED: deadline
    passed 31 Aug 2026, 11:59 PM AEST.
29. Boston University Presidential Scholarship 2026 - VERIFIED as the
    Fall 2027 entering class (retitled to 2027; half tuition per year;
    December 1 deadline; no separate application; official BU page).
30. Westlake University Summer Camp 2026 - SKIPPED: deadline passed
    17 May 2026, 24:00 Beijing Time.
31. DBA Scholarships in USA 2026-27 - SKIPPED: listicle.
32. Khazar University International Scholarship 2026-27 - SKIPPED:
    deadline passed 30 Jun 2026.
33. University of Adelaide RTP Scholarship 2026 - SKIPPED: deadline
    passed (2026 round closed 7 Jun 2026).
34. White House Internship Program 2026 - SKIPPED: 2026 sessions closed
    (Summer 5 Jan 2026; Fall 6 Apr 2026); next session Summer 2027,
    deadline 4 Jan 2027, UNPAID - kept as spare for a 2027 retitle.
35. UAL International Masters Scholarship 2026 - VERIFIED as the UAL
    International Postgraduate GBP 10,000 Scholarship, but 2026 rounds
    closed (27 Mar / 26 Jun 2026); live official cycle is 2027/28
    (23 Mar / 18 May 2027) - kept as spare for a 2027/28 retitle.
Spares verified this run but NOT written (stay in queue for the next
run): McGill Major Entrance Scholarships (deadline 21 Jan 2027,
partial CAD 3,000-12,000/year); NASA OSTEM Summer 2027 (deadline
1 Mar 2027); Interpol Internships (rolling, EUR 700/month);
White House Internship Summer 2027 (deadline 4 Jan 2027, unpaid);
UAL International Postgraduate 2027/28 (deadlines 23 Mar / 18 May 2027).
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 28)
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
 'fbi-honors-2027': {'mono': 'FBI', 'title': 'FBI Honors Internships 2027 in USA (Paid)',
   'href': 'fbi-honors-internships-2027-usa.html',
   'dpill': 'Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
   'award': 'Full-time paid 10-week internship, June–August 2027, at FBI Headquarters, one of 56 field offices, or a satellite campus; paid at federal GS-4 or GS-5 level depending on education. Exact dollar amount not published.',
   'elig': 'US citizens only; full-time students at a US-accredited college or university (undergraduate, graduate or post-doctoral); minimum 3.0 GPA; aged 18+; must pass a Top Secret background investigation.',
   'tags': [('Internship', 'blue'), ('USA', 'teal')]},
 'glasgow-leadership-2027': {'mono': 'UG', 'title': 'University of Glasgow Global Leadership Scholarships 2027 in UK (Funded)',
   'href': 'university-of-glasgow-global-leadership-scholarships-2027-uk.html',
   'dpill': 'Rolling · no fixed deadline',
   'award': '£10,000 tuition fee waiver for one year; 350 scholarships for the 2027/28 session. Partial funding — tuition only, not living costs.',
   'elig': 'Hold an offer for a full-time, one-year, in-person taught Master’s starting September 2027; International or EU fee status; results equivalent to a UK First-Class Honours degree.',
   'tags': [('Master’s', 'blue'), ('United Kingdom', 'teal')]},
 'melbourne-grs-2027': {'mono': 'UM', 'title': 'University of Melbourne Graduate Research Scholarships 2027 in Australia (Fully Funded)',
   'href': 'university-of-melbourne-graduate-research-scholarships-2027-australia.html',
   'dpill': 'Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': 'Around 600 awards a year: full tuition fee remission, a living allowance of AUD $41,100 a year (2027 rate), a relocation grant of up to AUD $3,000 and OSHC for international students. Total package up to AUD $135,000.',
   'elig': 'Domestic and international students applying for, or enrolled in, a Master’s by Research or PhD at the University of Melbourne; awarded on academic merit and research potential.',
   'tags': [('Master’s & PhD', 'blue'), ('Australia', 'teal')]},
 'hokkaido-mext-2027': {'mono': 'HU', 'title': 'Hokkaido University MEXT Scholarships 2027 in Japan (Fully Funded)',
   'href': 'hokkaido-university-mext-scholarships-2027-japan.html',
   'dpill': 'Deadline 29 Oct 2026 (e3) · %d day left' % dl_left('2026-10-29'),
   'award': 'Fully funded MEXT award: full tuition waiver, monthly stipend (MEXT standard rates as reported: ¥144,000 Master’s / ¥145,000 PhD), admission and application fee exemption and round-trip airfare.',
   'elig': 'International (non-Japanese) students residing outside Japan; bachelor’s degree for a Master’s, master’s degree for a PhD; strong academic record; English or Japanese proficiency.',
   'tags': [('Master’s & PhD', 'blue'), ('Japan', 'teal')]},
 'bu-presidential-2027': {'mono': 'BU', 'title': 'Boston University Presidential Scholarship 2027 in USA (Funded)',
   'href': 'boston-university-presidential-scholarship-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': 'Half of undergraduate tuition per year for incoming first-year students; no separate scholarship application — all applicants who apply by December 1 are automatically considered. Not fully funded.',
   'elig': 'Incoming first-year undergraduates at Boston University; US citizens, permanent residents and international students; exceptional academic achievement plus leadership, talent and initiative.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. FBI Honors Internships 2027
A.append(dict(
 slug='fbi-honors-internships-2027-usa',
 title='FBI Honors Internships 2027 in USA (Paid)',
 meta='FBI Honors Internships 2027: paid 10-week summer internships at the FBI, June–August 2027, at Headquarters, 56 field offices or satellite campuses. US citizens, full-time students, 3.0+ GPA. Deadline 2 November 2026, 11:59 PM ET.',
 short='FBI Honors Internships 2027', kicker='USA · Internship · Paid', mono='FBI',
 prov_short='Federal Bureau of Investigation (FBI)', prov_cat='Federal Agency · USA',
 h1='FBI Honors Internships 2027 in USA (Paid)',
 sub='Read this first, because the FBI Honors Internship Program has two different deadlines floating around online, and only one of them is live. FBI press releases from February 2026 listed 5 March 2026 — that was the first application window for the summer 2027 cycle. The FBI Jobs page now shows the cycle open until 2 November 2026 at 11:59 PM ET. This is a full-time, paid, 10-week internship running June to August 2027, open to full-time students at US-accredited colleges and universities — undergraduate, graduate or post-doctoral — who are US citizens with a minimum 3.0 GPA and who can pass a Top Secret background investigation. You rank up to three preferred locations, from FBI Headquarters to any of the 56 field offices.',
 dpill='Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
 facts=facts([('Award', 'A full-time paid internship for 10 weeks, June–August 2027 (one source gives 1 June – 6 August 2027). Interns are paid at federal GS-4 or GS-5 level depending on their education level, as reported by a secondary source citing FBI Jobs information; the exact dollar amount is not published in the official notification. Placements are at FBI Headquarters divisions, one of 56 field offices, or satellite campuses in Huntsville, Quantico and Pocatello.'),
              ('Eligible', 'US citizens only. Full-time students at a US-accredited college or university — undergraduate, graduate or post-doctoral. A minimum 3.0 cumulative GPA, maintained through the application and the internship. At least 18 years old. You must not graduate before the programme start date (1 June 2027), unless you are continuing your education in the following semester. You must pass all FBI employment background-investigation requirements and be able to receive a Top Secret clearance (including a drug test, fingerprinting and a polygraph), and you must be in the continental US, Hawaii or San Juan for parts of the background investigation.'),
              ('How', '1) Go to the FBI Jobs Students and Graduates page and open the Honors Internship Program posting (apply.fbijobs.gov / USAJOBS listing). 2) Rank up to three preferred locations. 3) Complete the application and upload the unofficial transcript(s) and the Program Terms Acknowledgement Form by 2 November 2026, 11:59 PM ET. 4) Shortlisted applicants go through qualification evaluation, interviews and the Top Secret background investigation.'),
              ('Deadline', '2 November 2026, 11:59 PM ET (per the official FBI Jobs page, checked 28 October 2026). The internship runs June–August 2027.'),
              ('Fine print', 'The February 2026 FBI releases that cite a 5 March 2026 deadline were the first application window for this same summer 2027 cycle — the live date is 2 November 2026. The USAJOBS posting still carries the older 5 March 2026 date; use the fbijobs.gov page for the current date. A résumé built with the USAJOBS Resume Builder is required — uploaded résumés are not reviewed. No letters of recommendation are listed as required.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>FBI Honors Internship Program</strong> is the Federal Bureau of Investigation’s flagship student programme: a <strong>full-time, paid, 10-week internship</strong> running <strong>June to August 2027</strong> (one source gives 1 June to 6 August 2027). Interns work inside real FBI teams — the programme is open to a <strong>wide range of academic backgrounds</strong>, including STEM, intelligence, forensic science, business, languages and law — at <strong>FBI Headquarters divisions, one of the 56 field offices, or satellite campuses in Huntsville, Quantico and Pocatello</strong>. You rank up to <strong>three preferred locations</strong> when you apply.</p>
      <p>Pay is at <strong>federal GS-4 or GS-5 level depending on your education level</strong>, as reported by a secondary source citing FBI Jobs information; the FBI’s own pages do not publish an exact dollar amount. What the FBI does publish, and what matters most for planning, is the clearance: every intern must pass the FBI’s <strong>Top Secret background investigation</strong>, which includes a drug test, fingerprinting and a polygraph, and you must be in the continental US, Hawaii or San Juan for parts of that investigation.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>US citizen.</strong></li>
        <li>A <strong>full-time student</strong> at a <strong>US-accredited college or university</strong> — undergraduate, graduate or post-doctoral.</li>
        <li>A minimum <strong>3.0 cumulative GPA</strong>, maintained through the application and the internship.</li>
        <li>At least <strong>18 years old</strong>.</li>
        <li>You must <strong>not graduate before the programme start date (1 June 2027)</strong>, unless you are continuing your education in the following semester.</li>
        <li>You must pass all <strong>FBI employment background-investigation requirements</strong> and be able to receive a <strong>Top Secret clearance</strong> (drug test, fingerprinting, polygraph).</li>
        <li>You must be in the <strong>continental US, Hawaii or San Juan</strong> for parts of the background investigation.</li>
        <li>Open to a <strong>wide range of academic backgrounds</strong> — STEM, intelligence, forensic science, business, languages, law and more.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full-time paid internship</strong> for <strong>10 weeks, June–August 2027</strong>, paid at federal <strong>GS-4 or GS-5 level</strong> depending on education (exact dollar amount not published in the official notification).</li>
        <li>Real work inside FBI teams at <strong>Headquarters, 56 field offices, or satellite campuses</strong> in Huntsville, Quantico and Pocatello.</li>
        <li>You choose up to <strong>three preferred locations</strong> when you apply.</li>
        <li>Experience inside a federal law-enforcement and intelligence agency, with the clearance process itself as part of the programme.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A résumé built with the <strong>USAJOBS Resume Builder</strong> — uploaded résumés are <strong>not reviewed</strong>, so build it in the tool.</li>
        <li><strong>Unofficial college transcript(s)</strong> — plus a high-school transcript for first-semester freshmen with no GPA; transfer and graduate students need transcripts from previous and current schools.</li>
        <li>The <strong>Program Terms Acknowledgement Form</strong> (required attachment).</li>
        <li>A <strong>School Certification Form / Enrollment Verification Certificate</strong> — optional but highly recommended.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the <strong>FBI Jobs Students and Graduates page</strong> and open the <strong>Honors Internship Program</strong> posting (apply.fbijobs.gov / USAJOBS listing).</li>
        <li><strong>Rank up to three preferred locations</strong> — HQ divisions, 56 field offices, or satellite campuses in Huntsville, Quantico or Pocatello.</li>
        <li>Complete the application and upload the <strong>unofficial transcript(s)</strong> and the <strong>Program Terms Acknowledgement Form</strong> by <strong>2 November 2026, 11:59 PM ET</strong>.</li>
        <li>Shortlisted applicants then go through <strong>qualification evaluation, interviews</strong>, and the <strong>Top Secret background investigation</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the FBI Honors Internships 2027?',
  '2 November 2026 at 11:59 PM ET, per the official FBI Jobs page checked on 28 October 2026. FBI press releases from February 2026 listed 5 March 2026 — that was the first application window for the same summer 2027 cycle, and the USAJOBS posting still carries that older date. Use the fbijobs.gov date.'),
 ('How much do FBI Honors Interns get paid?',
  'Interns are paid at federal GS-4 or GS-5 level depending on their education level, as reported by a secondary source citing FBI Jobs information. The exact dollar amount is not published in the official notification.'),
 ('Who can apply for the FBI Honors Internship?',
  'US citizens who are full-time students at a US-accredited college or university (undergraduate, graduate or post-doctoral), with a minimum 3.0 cumulative GPA, aged 18 or older, who have not graduated before 1 June 2027 (unless continuing education the following semester), and who can pass a Top Secret background investigation.'),
 ('Where are FBI Honors Interns placed?',
  'At FBI Headquarters divisions, one of the 56 field offices, or satellite campuses in Huntsville, Quantico and Pocatello. You rank up to three preferred locations in your application.'),
 ('Do I need a security clearance for the FBI Honors Internship?',
  'Yes. You must pass all FBI employment background-investigation requirements and be able to receive a Top Secret clearance, which includes a drug test, fingerprinting and a polygraph. You must be in the continental US, Hawaii or San Juan for parts of the investigation.'),
 ('What documents do I need for the FBI Honors Internship application?',
  'A résumé built with the USAJOBS Resume Builder (uploaded résumés are not reviewed), unofficial college transcript(s), and the Program Terms Acknowledgement Form. A School Certification Form / Enrollment Verification Certificate is optional but highly recommended.'),
 ('Can international students apply for the FBI Honors Internship?',
  'No. The Honors Internship Program is open to US citizens only.'),
 ('How long is the FBI Honors Internship?',
  '10 weeks, running June to August 2027 (one source gives 1 June to 6 August 2027).')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the FBI's own sites — fbijobs.gov/students-and-graduates and fbijobs.gov/students-and-graduates/featured-skills-and-locations (checked live 28 Oct 2026; the 2027 cycle "is open and closes on November 2, 2026") and the FBI announcement at fbi.gov (Philadelphia field office) — plus corroboration from Bright Scholarship and aggregator reports: deadline 2 November 2026, 11:59 PM ET; internship June-August 2027, 10 weeks; paid at federal GS-4 or GS-5 level depending on education level (per a secondary aggregator citing FBI Jobs information — exact dollar amount not published in the official notification); US citizen; full-time student at a US-accredited college or university (undergraduate, graduate or post-doctoral); minimum 3.0 cumulative GPA; aged 18+; must not graduate before 1 June 2027 unless continuing education the following semester; must pass a Top Secret background investigation (drug test, fingerprinting, polygraph); must be in the continental US, Hawaii or San Juan for parts of the investigation; rank up to three preferred locations (HQ divisions, 56 field offices, Huntsville, Quantico, Pocatello); documents — USAJOBS Resume Builder resume (uploaded resumes not reviewed), unofficial college transcript(s), Program Terms Acknowledgement Form (required), School Certification Form / Enrollment Verification Certificate (optional but highly recommended). CONFLICTS: (1) February 2026 FBI press releases listed a 5 March 2026 deadline — that was the first application window for this same summer 2027 cycle; the current fbijobs.gov page shows the cycle open until 2 November 2026, and the article uses that date. (2) The USAJOBS posting (job 857040400) still carries the older 5 March 2026 deadline and is not used for the date. The 1 June - 6 August 2027 dates come from one secondary source and are presented as such.</p>''',
 dl_long='2 November 2026, 11:59 PM ET (internship June–August 2027)',
 offlinks=[('FBI Jobs — Students and Graduates (official)', 'https://www.fbijobs.gov/students-and-graduates'),
           ('FBI Jobs — Featured Skills and Locations (official, current deadline)', 'https://www.fbijobs.gov/students-and-graduates/featured-skills-and-locations'),
           ('FBI — Honors Internship Program Open for Applications, Summer 2027 (official)', 'https://www.fbi.gov/contact-us/field-offices/philadelphia/news/fbi-honors-internship-program-open-for-applications-for-summer-2027'),
           ('Bright Scholarship — FBI Honors Internships 2027', 'https://brightscholarship.com/fbi-honors-internships-2027-in-usa-paid/')],
 related_titles=['ista-internships-2027', 'adidas-internships-2027', 'nsp-slovakia-2027', 'claude-corps-2027'])),

# ---------------------------------------------------------------- 3. Glasgow Global Leadership Scholarships 2027
A.append(dict(
 slug='university-of-glasgow-global-leadership-scholarships-2027-uk',
 title='University of Glasgow Global Leadership Scholarships 2027 in UK (Funded)',
 meta='University of Glasgow Global Leadership Scholarships 2027: 350 awards of a £10,000 tuition fee waiver for one-year taught Master’s programmes starting September 2027. Rolling applications; decisions within 6 weeks.',
 short='Glasgow Global Leadership Scholarships 2027', kicker='UK · Master’s · Funded', mono='UG',
 prov_short='University of Glasgow', prov_cat='University · United Kingdom',
 h1='University of Glasgow Global Leadership Scholarships 2027 in UK (Funded)',
 sub='Read this first, because the title most listings still carry — "2026" — is out of date. The University of Glasgow’s own page, checked on 28 October 2026, now describes the 2027/2028 session for September 2027 entry, with 350 scholarships of a £10,000 tuition fee waiver. The 2026/27 cycle is closed. The award runs on a rolling basis with no exact published deadline — decisions come within 6 weeks of your programme offer or scholarship application, whichever is later — and the closing date is confirmed in due course, usually in late August. It is a partial award: £10,000 off tuition for one year, not living costs, and it cannot be combined with other university or external discounts (except the Alumni Discount).',
 dpill='Rolling · no fixed deadline',
 facts=facts([('Award', 'A £10,000 tuition fee waiver for one year only, confirmed on the official page. 350 scholarships for the 2027/28 session. Partial funding only: it covers tuition, not living costs, and cannot be combined with other university or external discounts (except the Alumni Discount). The 2026/27 cycle had 281 awards — use the figure matching the cycle written about.'),
              ('Eligible', 'You must hold an offer for a full-time, one-year, in-person taught Master’s programme starting in September 2027. You must have International or EU fee status, and show academic results equivalent to a UK First-Class Honours degree. The award is open to a long published list of eligible countries/regions, including India, Pakistan, Bangladesh, Nepal, Nigeria, Ghana, Brazil and many others. Diplomas and certificates are not eligible; only one-year full-time in-person Master’s programmes qualify (with a first-year-only exception for the Book and Paper Conservation and Textile Conservation MPhils).'),
              ('How', '1) Apply for an eligible taught Master’s programme through the university’s postgraduate portal and secure an offer. 2) Apply for the scholarship through the university’s online scholarship portal — the 2027/28 round "will open shortly" and the university invites applicants to register interest for a notification; the portal asks for the student ID and application number issued with the offer. 3) Successful applicants are notified within about six weeks of the offer or scholarship submission, whichever is later.'),
              ('Deadline', 'No exact date is published. The official page states the award runs on a rolling basis, decisions come within 6 weeks of the programme offer or scholarship application (whichever is later), and the closing date "will be confirmed in due course, usually in late August". Third-party summaries of the 2026/27 cycle also reported no fixed deadline.'),
              ('Fine print', 'Some third-party pages describe the award as automatic on offer, while others — and the existence of the university’s own scholarship portal — describe a separate application; this article follows the portal-based route. The queue title "2026" is the listing year — the live cycle is 2027/28, September 2027 entry, and the article is retitled accordingly.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Glasgow Global Leadership Scholarship</strong> is a <strong>£10,000 tuition fee waiver for one year</strong>, offered to international students starting a <strong>one-year taught Master’s programme in September 2027</strong>. For the <strong>2027/28 session there are 350 scholarships</strong>, confirmed on the university’s own page. It is a <strong>partial award</strong>: it covers tuition only, not living costs, and it cannot be combined with other university or external discounts — the one exception is the Alumni Discount.</p>
      <p>There is <strong>no fixed deadline</strong>. The award runs on a <strong>rolling basis</strong>: decisions come within <strong>6 weeks of your programme offer or scholarship application, whichever is later</strong>, and the closing date is confirmed in due course, usually in late August. That means the useful deadline is your own: get the Master’s offer first, then apply for the scholarship promptly, because the award is made while places remain.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold an offer for a <strong>full-time, one-year, in-person taught Master’s programme</strong> starting in <strong>September 2027</strong>.</li>
        <li><strong>International or EU fee status.</strong></li>
        <li>Academic results equivalent to a <strong>UK First-Class Honours degree</strong>.</li>
        <li>Be from a country or region on the university’s <strong>published eligible list</strong> — a long list that includes India, Pakistan, Bangladesh, Nepal, Nigeria, Ghana, Brazil and many others.</li>
        <li><strong>Diplomas and certificates are not eligible</strong> — only one-year full-time in-person Master’s programmes qualify, with a first-year-only exception for the <strong>Book and Paper Conservation and Textile Conservation MPhils</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>£10,000 tuition fee waiver</strong> for one year.</li>
        <li><strong>350 scholarships</strong> for the 2027/28 session.</li>
        <li>Decisions within <strong>6 weeks</strong> of your programme offer or scholarship application, whichever is later.</li>
        <li>Can be held alongside the <strong>Alumni Discount</strong> (the only combinable discount).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The official page lists <strong>no separate document checklist</strong> for the scholarship itself — it is <strong>not published in the official notification</strong>.</li>
        <li>The <strong>Master’s programme application</strong> (a precondition) requires the usual items per third-party sources: degree certificate and transcripts, English-language test proof, CV, personal statement and references. Treat these as programme-application documents, not scholarship documents.</li>
        <li>The scholarship portal asks for the <strong>student ID and application number</strong> issued with your offer.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>First apply for an <strong>eligible taught Master’s programme</strong> through the university’s postgraduate portal and secure an offer.</li>
        <li>Then apply for the scholarship through the university’s <strong>online scholarship portal</strong> — the official page says the 2027/28 round "will open shortly" and invites applicants to <strong>register interest for a notification</strong>. The portal asks for the student ID and application number issued with the offer.</li>
        <li>Successful applicants are <strong>notified within about six weeks</strong> of the offer or scholarship submission, whichever is later.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Glasgow Global Leadership Scholarship 2027?',
  'No exact date is published. The award runs on a rolling basis, decisions come within 6 weeks of your programme offer or scholarship application (whichever is later), and the closing date is confirmed in due course, usually in late August. Apply as soon as you hold an offer.'),
 ('How much is the Glasgow Global Leadership Scholarship worth?',
  '£10,000 as a tuition fee waiver for one year only. It is partial funding — it covers tuition, not living costs — and it cannot be combined with other university or external discounts, except the Alumni Discount.'),
 ('How many Global Leadership Scholarships are available?',
  '350 for the 2027/28 session, per the university’s own page. The 2026/27 cycle had 281 awards — use the figure matching the cycle you are applying for.'),
 ('Who can apply for the Glasgow Global Leadership Scholarship?',
  'Students who hold an offer for a full-time, one-year, in-person taught Master’s programme starting in September 2027, with International or EU fee status, academic results equivalent to a UK First-Class Honours degree, and nationality from a country or region on the university’s published eligible list (including India, Pakistan, Bangladesh, Nepal, Nigeria, Ghana and Brazil).'),
 ('Is the Glasgow Global Leadership Scholarship automatic on offer?',
  'Not according to the university’s own pages. Some third-party pages describe it as automatic, but the university runs an online scholarship portal and the 2027/28 round opens shortly — this article follows the portal-based route: secure the Master’s offer first, then apply through the scholarship portal.'),
 ('Which programmes qualify for the Glasgow Global Leadership Scholarship?',
  'Full-time, one-year, in-person taught Master’s programmes starting in September 2027. Diplomas and certificates do not qualify. The only exception is the first year of the Book and Paper Conservation and Textile Conservation MPhils.'),
 ('Can the Glasgow Global Leadership Scholarship be combined with other discounts?',
  'No — it cannot be combined with other university or external discounts. The only exception is the Alumni Discount.'),
 ('Is the 2026 cycle of the Glasgow Global Leadership Scholarship still open?',
  'No. The 2026/27 cycle is closed and the university’s page now describes the 2027/2028 session for September 2027 entry, which is why this article is titled for 2027.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the University of Glasgow's own scholarship page (gla.ac.uk/scholarships/globalleadershipscholarship/, checked live 28 Oct 2026 — now describes the 2027/2028 session, September 2027 entry) and corroborated by Bright Scholarship plus multiple third-party summaries agreeing on GBP 10,000, rolling basis and the First-Class-equivalent requirement: award GBP 10,000 tuition fee waiver for one year only; 350 scholarships for the 2027/28 session (281 for 2026/27 — use the cycle-matched figure); partial funding, tuition only, not living costs, cannot be combined with other university or external discounts except the Alumni Discount; eligibility — hold an offer for a full-time, one-year, in-person taught Master's starting September 2027, International or EU fee status, academic results equivalent to a UK First-Class Honours degree, nationality on the published eligible-country list (including India, Pakistan, Bangladesh, Nepal, Nigeria, Ghana, Brazil); diplomas and certificates not eligible; only one-year full-time in-person Master's qualify, with a first-year-only exception for the Book and Paper Conservation and Textile Conservation MPhils; deadline — no exact date published, rolling, decisions within 6 weeks of the programme offer or scholarship application (whichever is later), closing date "confirmed in due course, usually in late August"; process — apply for an eligible taught Master's through the postgraduate portal, secure an offer, then apply through the university's online scholarship portal (2027/28 round "will open shortly"; register interest for a notification; portal asks for student ID and application number); documents — no separate scholarship document checklist is published in the official notification; the Master's application requires degree certificate/transcripts, English test proof, CV, personal statement and references per third-party sources. CONFLICTS: (1) The queue title "2026" is stale — the 2026/27 cycle is closed and the official page has moved to 2027/28, so the article is retitled to 2027. (2) Some third-party pages describe the award as automatic on offer; the university's own scholarship portal indicates a separate application, and the article follows the portal-based route. (3) Third-party summaries of the 2026/27 cycle also reported no fixed deadline, consistent with the rolling basis.</p>''',
 dl_long='Rolling — no fixed date published (closing usually in late August; decisions within 6 weeks)',
 offlinks=[('University of Glasgow — Global Leadership Scholarship (official)', 'https://www.gla.ac.uk/scholarships/globalleadershipscholarship/'),
           ('University of Glasgow — Postgraduate Taught Programmes (official)', 'https://www.gla.ac.uk/postgraduate/taught/'),
           ('Bright Scholarship — University of Glasgow Global Leadership Scholarships 2026', 'https://brightscholarship.com/university-of-glasgow-global-leadership-scholarships-2026/')],
 related_titles=['york-pise-2027', 'miami-stamps-2027', 'ucl-impact-2027', 'alqasimi-foundation-2026'])),

# ---------------------------------------------------------------- 4. Melbourne Graduate Research Scholarships 2027
A.append(dict(
 slug='university-of-melbourne-graduate-research-scholarships-2027-australia',
 title='University of Melbourne Graduate Research Scholarships 2027 in Australia (Fully Funded)',
 meta='University of Melbourne Graduate Research Scholarships 2027: around 600 fully funded awards a year — full tuition fee remission, AUD $41,100 a year living allowance (2027 rate), relocation grant and OSHC. Automatic consideration; deadline 31 October 2026.',
 short='Melbourne Graduate Research Scholarships 2027', kicker='Australia · Master’s & PhD · Fully Funded', mono='UM',
 prov_short='University of Melbourne', prov_cat='University · Australia',
 h1='University of Melbourne Graduate Research Scholarships 2027 in Australia (Fully Funded)',
 sub='Read this first, because the "600 Graduate Research Scholarships" in the listing title is not a separate award — it is the University of Melbourne’s Graduate Research Scholarships, the umbrella for the Melbourne Research Scholarship and the Research Training Program Scholarship, with around 600 awards a year. The package is genuinely fully funded: 100% fee remission, a living allowance of AUD $41,100 a year at the 2027 rate, a relocation grant and single Overseas Student Health Cover for international students who need a visa — a total package the university values at up to AUD $135,000. And there is no separate scholarship application for most new applicants: you apply for a graduate research course by its closing date — widely reported as 31 October 2026 for the Round 1, February 2027 start — and you are automatically considered.',
 dpill='Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'Around 600 awards a year. 100% fee remission — full tuition fee offset, up to 2 years for a Master’s by Research and up to 4 years for a PhD. Living allowance AUD $41,100 a year (2027 full-time rate, per the official University of Melbourne page; indexed annually; includes limited paid sick, maternity and parenting leave) — up to 2 years (Master’s) or 3.5 years (PhD). Relocation grant: AUD $2,000 (from other Australian states/territories) or AUD $3,000 (from outside Australia). OSHC Single Membership for international students who need a student visa. Total package value up to AUD $135,000 (official figure).'),
              ('Eligible', 'Open to domestic and international students of all nationalities. You must have applied for, and meet the entry requirements of, a graduate research degree (Master’s by Research or PhD) at the University of Melbourne, or be currently enrolled in one. Awards are based on academic merit and research potential, ranked by selection panels. All domestic students offered admission to a Master’s by Research or PhD automatically receive an RTP Fee Offset scholarship. The typical entry bar (secondary sources): a four-year bachelor’s degree or equivalent, with a research project worth at least 25% of final-year coursework.'),
              ('How', '1) New applicants: apply for a graduate research course at the University of Melbourne by the course closing date — you are automatically considered for the scholarship; no separate scholarship application and no application fee. A scholarship application is added to your record within 10 business days of the course application. 2) Currently enrolled or deferred students: apply or reapply through the scholarship application process, which varies by enrolling Faculty (see the university’s Graduate Research Scholarship Applications page). 3) Domestic students receive the RTP Fee Offset offer with their course offer; stipend scholarship offers come separately, around the same time.'),
              ('Deadline', '31 October 2026 — the widely reported Round 1 closing date for a February 2027 start, corroborated by many independent sources. The official University of Melbourne page itself does not print a single date; it says new applicants must apply for their course "by the application closing date for that course". Current and deferred students must submit the scholarship form by the same date.'),
              ('Fine print', 'Several secondary sites quote AUD $39,500 (the 2026 rate) or $38,500/$31,200 (outdated) — the official page’s 2027 rate is $41,100, and this article uses that. The official page publishes no standalone scholarship document list, so no definitive document checklist is stated here; the course application requires academic transcripts and a CV plus other supporting documents, per secondary sources only.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Melbourne Graduate Research Scholarships</strong> — the <strong>Melbourne Research Scholarship</strong> and the <strong>Research Training Program (RTP) Scholarship</strong> — are the university’s flagship research awards, with <strong>around 600 awards a year</strong>. The package is <strong>fully funded</strong>: a <strong>100% fee remission</strong> (full tuition fee offset for up to 2 years for a Master’s by Research, up to 4 years for a PhD), a <strong>living allowance of AUD $41,100 a year</strong> at the 2027 full-time rate, a <strong>relocation grant</strong> of AUD $2,000 from other Australian states or territories and AUD $3,000 from outside Australia, and <strong>single Overseas Student Health Cover</strong> for international students who need a student visa. The university values the total package at up to <strong>AUD $135,000</strong>.</p>
      <p>The best part of the process is how little of it there is. For most new applicants there is <strong>no separate scholarship application and no application fee</strong>: you apply for a graduate research course by its closing date, and you are <strong>automatically considered</strong>. A scholarship application is added to your record within 10 business days of the course application. Currently enrolled or deferred students use a separate scholarship process that varies by Faculty.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>domestic and international students</strong> of all nationalities.</li>
        <li>You must have applied for, and meet the entry requirements of, a <strong>graduate research degree (Master’s by Research or PhD)</strong> at the University of Melbourne, or be <strong>currently enrolled</strong> in one.</li>
        <li>Awards are based on <strong>academic merit and research potential</strong>, ranked by selection panels.</li>
        <li>All domestic students offered admission to a Master’s by Research or PhD <strong>automatically receive an RTP Fee Offset scholarship</strong>.</li>
        <li>The typical entry bar (secondary sources): a <strong>four-year bachelor’s degree or equivalent</strong>, with a research project worth at least <strong>25% of final-year coursework</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% fee remission</strong> — full tuition fee offset, up to 2 years (Master’s by Research) or 4 years (PhD).</li>
        <li><strong>Living allowance AUD $41,100 a year</strong> (2027 full-time rate; indexed annually; includes limited paid sick, maternity and parenting leave) — up to 2 years (Master’s) or 3.5 years (PhD).</li>
        <li><strong>Relocation grant:</strong> AUD $2,000 (from other Australian states/territories) or AUD $3,000 (from outside Australia).</li>
        <li><strong>OSHC Single Membership</strong> for international students who need a student visa.</li>
        <li><strong>Total package value up to AUD $135,000</strong> (official figure).</li>
        <li><strong>No separate scholarship application</strong> for most new applicants — automatic consideration on the course application.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The official page publishes <strong>no standalone scholarship document list</strong> — a definitive scholarship-specific checklist is <strong>not published in the official notification</strong>, so none is stated here.</li>
        <li>Secondary sources report that the <strong>course application</strong> requires <strong>academic transcripts and a CV</strong> plus other supporting documents — treat these as secondary-source only, not officially confirmed.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>New applicants:</strong> apply for a graduate research course at the University of Melbourne by the <strong>course closing date</strong> — you are <strong>automatically considered</strong> for the scholarship; no separate scholarship application and no application fee. A scholarship application is added to your record within <strong>10 business days</strong> of the course application.</li>
        <li><strong>Currently enrolled or deferred students:</strong> apply or reapply via the scholarship application process, which <strong>varies by enrolling Faculty</strong> (see the university’s Graduate Research Scholarship Applications page).</li>
        <li>Domestic students receive the <strong>RTP Fee Offset offer with their course offer</strong>; stipend scholarship offers come separately, around the same time.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Melbourne Graduate Research Scholarships 2027?',
  '31 October 2026 — the widely reported Round 1 closing date for a February 2027 start, corroborated by many independent sources. The official University of Melbourne page itself does not print a single date; it says new applicants must apply for their course "by the application closing date for that course".'),
 ('How much is the Melbourne Graduate Research Scholarship worth?',
  'A living allowance of AUD $41,100 a year at the 2027 full-time rate, plus 100% fee remission, a relocation grant of AUD $2,000–$3,000 and single OSHC for international students who need a visa — a total package the university values at up to AUD $135,000.'),
 ('How many Graduate Research Scholarships does the University of Melbourne offer?',
  'Around 600 awards a year, covering the Melbourne Research Scholarship and the Research Training Program Scholarship.'),
 ('Do I need a separate application for the Melbourne Graduate Research Scholarship?',
  'No, for most new applicants. You apply for a graduate research course by its closing date and are automatically considered — no separate scholarship application and no application fee. Currently enrolled or deferred students use a separate scholarship process that varies by Faculty.'),
 ('Who can apply for the Melbourne Graduate Research Scholarships?',
  'Domestic and international students of all nationalities who have applied for, and meet the entry requirements of, a Master’s by Research or PhD at the University of Melbourne, or who are currently enrolled in one. Awards are based on academic merit and research potential.'),
 ('What is the stipend for the Melbourne Graduate Research Scholarship in 2027?',
  'AUD $41,100 a year (2027 full-time rate, per the official University of Melbourne page; indexed annually). Several secondary sites quote $39,500 — that is the 2026 rate — or older figures, which are outdated.'),
 ('Does the Melbourne Graduate Research Scholarship cover tuition fees?',
  'Yes — 100% fee remission, a full tuition fee offset for up to 2 years (Master’s by Research) or 4 years (PhD). All domestic students offered admission to a Master’s by Research or PhD automatically receive an RTP Fee Offset scholarship.'),
 ('What documents do I need for the Melbourne Graduate Research Scholarship?',
  'The official page publishes no standalone scholarship document list, so no definitive checklist is stated here. Secondary sources report that the course application requires academic transcripts and a CV plus other supporting documents.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the University of Melbourne's own scholarships page (scholarships.unimelb.edu.au/awards/graduate-research-scholarships, checked live 28 Oct 2026 — confirms quantity 600, AUD 135,000 total package value, AUD 41,100 stipend, eligibility, automatic consideration) and corroborated by FullScholarships, StudyCalcTools, Collegedunia and other independent sources: around 600 awards a year (Melbourne Research Scholarship + Research Training Program Scholarship); 100% fee remission — full tuition fee offset up to 2 years (Master's by Research) / 4 years (PhD); living allowance AUD 41,100/year (2027 full-time rate, official; indexed annually; includes limited paid sick, maternity and parenting leave) up to 2 years (Master's) / 3.5 years (PhD); relocation grant AUD 2,000 (from other Australian states/territories) / AUD 3,000 (from outside Australia); OSHC Single Membership for international students who need a student visa; total package up to AUD 135,000; eligibility — domestic and international students of all nationalities, applied for and meeting entry requirements of a graduate research degree (Master's by Research or PhD) or currently enrolled, awards based on academic merit and research potential ranked by selection panels, all domestic students offered admission automatically receive an RTP Fee Offset; process — new applicants apply for a graduate research course by the course closing date and are automatically considered (no separate scholarship application, no application fee; scholarship application added to the record within 10 business days); currently enrolled or deferred students apply via the scholarship process varying by Faculty; domestic students receive the RTP Fee Offset offer with their course offer, stipend offers separately around the same time. CONFLICTS: (1) Deadline — the official page does not print a single date ("by the application closing date for that course"); 31 October 2026 is the widely reported Round 1 closing date for a February 2027 start, corroborated by many independent sources, and the article presents it as such. (2) Several secondary sites quote AUD 39,500 (the 2026 rate) or 38,500/31,200 (outdated) — the official 2027 rate is AUD 41,100 and the article uses that. (3) The typical entry bar (four-year bachelor's or equivalent, research project worth at least 25% of final-year coursework) and the course-application document list (transcripts, CV) come from secondary sources only — the article says so and does not present a definitive scholarship-specific document checklist, since the official page publishes none.</p>''',
 dl_long='31 October 2026 (Round 1 closing date for a February 2027 start, as widely reported)',
 offlinks=[('University of Melbourne — Graduate Research Scholarships (official)', 'https://scholarships.unimelb.edu.au/awards/graduate-research-scholarships'),
           ('Bright Scholarship — 600 Graduate Research Scholarships 2027', 'https://brightscholarship.com/600-graduate-research-scholarships-2027/')],
 related_titles=['tsukuba-mext-2027', 'jsps-2027', 'hugo-lab-2027', 'rtp-2027'])),

# ---------------------------------------------------------------- 5. Hokkaido University MEXT Scholarships 2027
A.append(dict(
 slug='hokkaido-university-mext-scholarships-2027-japan',
 title='Hokkaido University MEXT Scholarships 2027 in Japan (Fully Funded)',
 meta='Hokkaido University MEXT Scholarships 2027: fully funded Japanese Government (MEXT) awards for October 2027 intake — full tuition waiver, monthly stipend, airfare. Three tracks: e3 Engineering (closes 29 Oct 2026), IGP Life Science and IGC-DHS Science.',
 short='Hokkaido University MEXT Scholarships 2027', kicker='Japan · Master’s & PhD · Fully Funded', mono='HU',
 prov_short='Hokkaido University', prov_cat='University · Japan',
 h1='Hokkaido University MEXT Scholarships 2027 in Japan (Fully Funded)',
 sub='Read this first, because "Hokkaido University MEXT Scholarships 2027" is not one scheme with one deadline — it is several distinct MEXT tracks for the October 2027 intake, each with its own deadline, and the one that matters most closes tomorrow. The Graduate School of Engineering’s e3 programme (University Recommendation) takes online applications from 20 to 29 October 2026 and the system closes at 23:59:59 JST on 29 October 2026. The Life Science IGP Special Quota needs you to contact a prospective supervisor by 10 November 2026, and the Science IGC-DHS special programme takes first-stage documents from 1 October to 15 November 2026. The Embassy Recommendation track runs separately through the Japanese embassy in your home country. All tracks are fully funded MEXT awards: full tuition waiver, monthly stipend, and round-trip airfare.',
 dpill='Deadline 29 Oct 2026 (e3) · %d day left' % dl_left('2026-10-29'),
 facts=facts([('Award', 'Fully funded MEXT award: full tuition waiver, admission and application fee exemption, and round-trip airfare to Japan plus return airfare after completion. Monthly stipend at the MEXT standard rates as reported across multiple secondary sources — ¥144,000 a month for a Master’s and ¥145,000 a month for a PhD (¥147,000 / ¥148,000 from November to March) — not stated on the official Hokkaido pages fetched, so the article attributes them as reported rather than as Hokkaido-published. Duration: Master’s 2 years, PhD 3 years; intake October 2027.'),
              ('Eligible', 'International (non-Japanese) students residing outside Japan, of all nationalities. A bachelor’s degree (or expected completion before October 2027) for a Master’s; a master’s degree for a PhD. A strong academic record — the exact GPA threshold is programme-dependent and not confirmed on the official pages fetched, so only "academically excellent / strong record" is stated. Age: born on or after 2 April 1991 (under 35) per secondary sources, with the same caveat. English or Japanese proficiency is required, and study is full-time. Ineligible per the official IGP page: past MEXT recipients, active military personnel, dual citizens unable to renounce Japanese citizenship, applicants holding another government scholarship during the period, and those who cannot arrive in Japan by the designated date.'),
              ('How', 'e3 Engineering: create an account on the e3 online submission system during the application window only, upload all documents and submit before 29 October 2026; shortlisted candidates are interviewed by a prospective supervisor, then by a nomination committee. Scholarship application and admission screening are separate procedures. IGP Life Science: pick a laboratory, contact the prospective supervisor directly (IGP First Step Form), obtain permission to enrol, and hand the document package to the supervisor, who forwards it to the IGP office by 10 December 2026. IGC-DHS Science: after supervisor agreement, email the first-stage PDF package to the Graduate School of Science international-support office between 1 October and 15 November 2026. Embassy track: apply through the Japanese embassy in your home country, then obtain an acceptance letter from Hokkaido separately.'),
              ('Deadline', 'Track by track: e3 Engineering (University Recommendation) — online applications 20–29 October 2026, system closes 23:59:59 JST on 29 October 2026; first-screening results 24 December 2026. IGP Life Science Special Quota — contact a prospective supervisor by 10 November 2026; supervisor submits documents to the IGP office by 10 December 2026; recommendation to MEXT in March 2027. IGC-DHS Science special programme — first-stage documents 1 October – 15 November 2026 (5 places: 4 doctoral, 1 master’s). Embassy Recommendation — separate route via the Japanese embassy in your home country; timelines differ by country and no single date applies.'),
              ('Fine print', 'Do not use Bright Scholarship’s vague "November 2026" as the headline deadline — it is wrong for the e3 track, which closes 29 October 2026. Stipend figures and the age/GPA thresholds are MEXT-standard figures repeated across secondary sources but were not visible on the official pages fetched — they are attributed accordingly, not presented as Hokkaido-published.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Hokkaido University MEXT Scholarships 2027</strong> are <strong>Japanese Government (MEXT) awards</strong> for the <strong>October 2027 intake</strong>, run through Hokkaido University’s graduate schools. They are <strong>fully funded</strong>: a <strong>full tuition waiver</strong>, exemption from <strong>admission and application fees</strong>, a <strong>monthly stipend</strong>, and <strong>round-trip airfare</strong> to Japan plus return airfare after completion. A Master’s runs for <strong>2 years</strong> and a PhD for <strong>3 years</strong>.</p>
      <p>The essential thing to understand is that there are <strong>several distinct MEXT tracks</strong>, each with its own deadline and its own application route. The <strong>Graduate School of Engineering’s e3 programme</strong> (University Recommendation) closes <strong>29 October 2026</strong>. The <strong>Graduate School of Life Science IGP Special Quota</strong> needs supervisor contact by <strong>10 November 2026</strong>. The <strong>Graduate School of Science IGC-DHS special programme</strong> takes first-stage documents until <strong>15 November 2026</strong>. And the <strong>Embassy Recommendation track</strong> runs separately through the Japanese embassy in your home country, with timelines that differ by country.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International (non-Japanese) students</strong> residing outside Japan, of <strong>all nationalities</strong>.</li>
        <li>A <strong>bachelor’s degree</strong> (or expected completion before October 2027) for a Master’s; a <strong>master’s degree</strong> for a PhD.</li>
        <li>A <strong>strong academic record</strong> — the exact GPA threshold is programme-dependent and not confirmed on the official pages fetched, so no single figure is stated.</li>
        <li>Age: born on or after <strong>2 April 1991 (under 35)</strong> per secondary sources — same caveat; not confirmed on the official pages fetched.</li>
        <li><strong>English or Japanese proficiency</strong> is required; study is <strong>full-time</strong>.</li>
        <li><strong>Ineligible</strong> per the official IGP page: past MEXT recipients, active military personnel, dual citizens unable to renounce Japanese citizenship, applicants holding another government scholarship during the period, and those who cannot arrive in Japan by the designated date.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver</strong>, plus <strong>admission and application fee exemption</strong>.</li>
        <li><strong>Monthly stipend</strong> at the MEXT standard rates as reported: <strong>¥144,000 a month for a Master’s, ¥145,000 a month for a PhD</strong> (¥147,000 / ¥148,000 from November to March) — not stated on the official Hokkaido pages fetched, so attributed as reported.</li>
        <li><strong>Round-trip airfare</strong> to Japan, and <strong>return airfare</strong> after completion.</li>
        <li>Duration: <strong>Master’s 2 years, PhD 3 years</strong>; intake <strong>October 2027</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>MEXT scholarship application form</strong> and <strong>Field of Study and Study Program</strong>.</li>
        <li><strong>Motivation to Apply and Research Plan</strong> (e3 format, maximum 2 pages).</li>
        <li><strong>Abstracts of your graduation thesis</strong> (and of publications, if any).</li>
        <li><strong>Official academic transcripts</strong> and <strong>graduation / expected graduation certificates</strong>.</li>
        <li>A <strong>recommendation letter</strong> and <strong>evidence of academic excellence</strong>.</li>
        <li><strong>Proof of English proficiency</strong> (for example IELTS/TOEFL, or a medium-of-instruction certificate).</li>
        <li>A <strong>photocopy of your valid passport</strong>, and a <strong>summary of your master’s thesis or undergraduate research</strong> (IGP).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>e3 Engineering (University Recommendation):</strong> create an account on the e3 online submission system during the application window only, upload all documents, and click submit before <strong>29 October 2026</strong>. Shortlisted candidates are interviewed by a prospective supervisor, then by a nomination committee. Scholarship application and admission screening are separate procedures.</li>
        <li><strong>IGP Life Science (Special Quota):</strong> pick a laboratory, contact the prospective supervisor directly (IGP First Step Form), obtain permission to enrol, and hand the document package to the supervisor, who forwards it to the IGP office by <strong>10 December 2026</strong>. Contact the supervisor by <strong>10 November 2026</strong>.</li>
        <li><strong>IGC-DHS Science (special programme):</strong> after supervisor agreement, email the first-stage PDF package to the Graduate School of Science international-support office between <strong>1 October and 15 November 2026</strong> (5 places: 4 doctoral, 1 master’s).</li>
        <li><strong>Embassy Recommendation track:</strong> apply through the Japanese embassy in your home country, then obtain an acceptance letter from Hokkaido separately.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Hokkaido University MEXT Scholarships 2027?',
  'There is no single deadline — Hokkaido runs several MEXT tracks. The e3 Engineering track closes 29 October 2026 at 23:59:59 JST. The IGP Life Science track needs supervisor contact by 10 November 2026 (supervisor submits by 10 December 2026). The IGC-DHS Science track takes first-stage documents from 1 October to 15 November 2026. The Embassy Recommendation track follows your home country’s embassy timeline.'),
 ('How much is the Hokkaido University MEXT Scholarship worth?',
  'It is fully funded: full tuition waiver, admission and application fee exemption, round-trip airfare, and a monthly stipend at the MEXT standard rates as reported — ¥144,000 a month for a Master’s and ¥145,000 a month for a PhD (¥147,000 / ¥148,000 from November to March). Those stipend figures were not stated on the official Hokkaido pages fetched, so they are attributed as reported.'),
 ('Who can apply for the Hokkaido University MEXT Scholarships?',
  'International (non-Japanese) students residing outside Japan, of all nationalities, with a bachelor’s degree (or expected completion before October 2027) for a Master’s or a master’s degree for a PhD, a strong academic record, and English or Japanese proficiency. Past MEXT recipients, active military personnel and holders of another government scholarship during the period are ineligible.'),
 ('What is the e3 programme at Hokkaido University?',
  'The e3 programme is the Graduate School of Engineering’s English-language programme for the MEXT University Recommendation track. Applications run 20–29 October 2026 online; shortlisted candidates are interviewed by a prospective supervisor and then by a nomination committee; first-screening results come on 24 December 2026.'),
 ('Do I need a supervisor before applying for the Hokkaido MEXT Scholarship?',
  'It depends on the track. For the IGP Life Science Special Quota you must contact a prospective supervisor directly (by 10 November 2026) and obtain permission to enrol. For the IGC-DHS Science programme you also need supervisor agreement before emailing your first-stage documents. For e3 Engineering, shortlisted candidates are interviewed by a prospective supervisor after submission.'),
 ('Can I apply through the Japanese embassy for Hokkaido University MEXT?',
  'Yes — the Embassy Recommendation track is a separate route. You apply through the Japanese embassy in your home country, then obtain an acceptance letter from Hokkaido separately. Timelines differ by country, so there is no single embassy-track date.'),
 ('How many places are there on the Hokkaido IGC-DHS MEXT programme?',
  '5 places: 4 doctoral and 1 master’s, for the October 2027 intake. First-stage documents are accepted from 1 October to 15 November 2026.'),
 ('When does the Hokkaido University MEXT Scholarship start?',
  'October 2027 intake. A Master’s runs for 2 years and a PhD for 3 years.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against Hokkaido University's own pages — e3 Engineering, University Recommendation (eprogram.eng.hokudai.ac.jp/e3/scholarships/mext: deadlines, documents, schedule), IGP Special Quota (altair.sci.hokudai.ac.jp/grad/igpoverview/special-quota.php: deadlines, documents, ineligibility) and IGC-DHS special programme (www2.sci.hokudai.ac.jp/gs/en/news/5419: deadlines, documents, 5 places) — plus corroboration from Bright Scholarship (documents/eligibility broadly match, but its "November 2026" deadline is too vague and wrong for the e3 track): deadlines track-by-track — e3 Engineering online applications 20-29 October 2026, system closes 23:59:59 JST on 29 October 2026, first-screening results 24 December 2026; IGP Life Science Special Quota — contact prospective supervisor by 10 November 2026, supervisor submits documents to the IGP office by 10 December 2026, recommendation to MEXT in March 2027; IGC-DHS Science — first-stage documents 1 October-15 November 2026, 5 places (4 doctoral, 1 master's); Embassy Recommendation — separate route via the Japanese embassy in the applicant's home country, timelines differ by country; award — full tuition waiver, admission and application fee exemption, round-trip airfare to Japan and return airfare after completion, duration Master's 2 years / PhD 3 years, intake October 2027; eligibility — international (non-Japanese) students residing outside Japan, all nationalities, bachelor's degree (or expected completion before October 2027) for a Master's, master's degree for a PhD, strong academic record, English or Japanese proficiency, full-time study; ineligible per the official IGP page — past MEXT recipients, active military personnel, dual citizens unable to renounce Japanese citizenship, applicants holding another government scholarship during the period, those who cannot arrive by the designated date; documents from the official e3 and IGP pages — MEXT application form, Field of Study and Study Program, Motivation to Apply and Research Plan (e3, max 2 pages), abstracts of graduation thesis (and publications if any), official transcripts, graduation/expected graduation certificates, recommendation letter, evidence of academic excellence, proof of English proficiency (IELTS/TOEFL or medium-of-instruction certificate), passport photocopy, summary of master's thesis or undergraduate research (IGP). CONFLICTS: (1) Bright Scholarship's "November 2026" headline deadline is not used — it is wrong for the e3 track, which closes 29 October 2026. (2) Stipend figures (JPY 144,000/month Master's, JPY 145,000/month PhD; JPY 147,000/148,000 November-March) and the age/GPA thresholds (born on/after 2 April 1991, under 35; GPA 2.30/3.00 or CGPA 3.0/4.0 or 80%) are MEXT-standard figures repeated across secondary sources but were not visible on the official pages fetched — the article attributes them as reported and states only "strong academic record" as confirmed.</p>''',
 dl_long='e3 track: 29 October 2026 (other tracks to 10 December 2026)',
 offlinks=[('Hokkaido University — e3 Engineering, MEXT Scholarship (official)', 'https://eprogram.eng.hokudai.ac.jp/e3/scholarships/mext'),
           ('Hokkaido University — IGP Special Quota, Life Science (official)', 'https://altair.sci.hokudai.ac.jp/grad/igpoverview/special-quota.php'),
           ('Hokkaido University — IGC-DHS Special Programme, Science (official)', 'https://www2.sci.hokudai.ac.jp/gs/en/news/5419'),
           ('Bright Scholarship — Hokkaido University MEXT Scholarships 2027', 'https://brightscholarship.com/hokkaido-university-mext-scholarships-2027/')],
 related_titles=['tsukuba-mext-2027', 'jsps-2027', 'gottingen-daad-2027', 'hugo-lab-2027'])),

# ---------------------------------------------------------------- 5. Boston University Presidential Scholarship 2027
A.append(dict(
 slug='boston-university-presidential-scholarship-2027-usa',
 title='Boston University Presidential Scholarship 2027 in USA (Funded)',
 meta='Boston University Presidential Scholarship 2027: half of undergraduate tuition per year for incoming first-year students, US and international. No separate application — apply for admission by December 1 and you are automatically considered.',
 short='BU Presidential Scholarship 2027', kicker='USA · Undergraduate · Funded', mono='BU',
 prov_short='Boston University', prov_cat='University · USA',
 h1='Boston University Presidential Scholarship 2027 in USA (Funded)',
 sub='Read this first, because two things about this scholarship are routinely stated wrong online: the amount and the year. The award is half of undergraduate tuition per year — the "$25,000 a year" figure repeated by Bright Scholarship and other aggregators is the pre-Fall 2026 value and is superseded by Boston University’s current half-tuition figure. And the deadline Boston University itself publishes is simply "December 1", with no year attached: for Fall 2026 entry that deadline was 1 December 2025, already passed, so the live deadline is 1 December 2026, for the Fall 2027 entering class. There is no separate scholarship application, essay or form — every first-year applicant who applies by December 1 is automatically considered, and winners are notified with their admission decision.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'Half of undergraduate tuition per year for incoming first-year students, effective for students entering Fall 2026 per Boston University’s official merit-scholarships page (the same half-tuition terms apply to the next entering class). Renewable for up to four years of undergraduate study, per third-party sources; Boston University’s page does not state duration explicitly. Not fully funded — it does not cover housing, meals or other costs. The "$25,000 per academic year" figure repeated by aggregators is the pre-Fall 2026 value and is superseded — do not use it.'),
              ('Eligible', 'Incoming first-year undergraduate students at Boston University. Open to US citizens, US permanent residents, and international students (all nationalities). Exceptional academic achievement, plus leadership, talent, initiative and creativity beyond the classroom and impact in school and community. Third-party sites report typical profiles of the top 5% of the high-school class and SAT above 1500 / ACT above 33 — these are not published by Boston University as requirements, so they are presented only as reported typical profiles, not cut-offs; Boston University states test scores are not required.'),
              ('How', '1) Apply for first-year undergraduate admission to Boston University via the Common Application (or Coalition Application). 2) Submit the complete admission application and all supporting credentials by December 1. 3) No separate scholarship application, essay or form is required — all applicants who apply by December 1 are automatically considered. 4) Successful applicants are notified of the award with their admission decision.'),
              ('Deadline', 'December 1 — Boston University publishes only "December 1", with no year attached. Third-party pages list 1 December 2026, which corresponds to Fall 2027 entry; for Fall 2026 entry the deadline was 1 December 2025 (already passed). This article frames the deadline as 1 December 2026 for the Fall 2027 entering class.'),
              ('Fine print', 'The award is Boston University’s flagship first-year merit scholarship, but it is partial: half tuition, not full funding. There is no separate application — the admission application is the scholarship application. Standardised test scores (SAT/ACT) are optional at Boston University; do not treat reported typical scores as cut-offs.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Boston University Presidential Scholarship</strong> is the university’s flagship merit award for <strong>incoming first-year undergraduates</strong>: <strong>half of undergraduate tuition per year</strong>. It is open to <strong>US citizens, US permanent residents and international students</strong> of all nationalities, and it is awarded on <strong>exceptional academic achievement plus leadership, talent, initiative and creativity</strong> beyond the classroom, and impact in school and community. It is a <strong>partial award</strong> — it does not cover housing, meals or other costs — and it is renewable for up to <strong>four years</strong> of undergraduate study, per third-party sources (Boston University’s page does not state duration explicitly).</p>
      <p>The process could hardly be simpler: there is <strong>no separate scholarship application, essay or form</strong>. You apply for first-year admission to Boston University, submit the complete application and all supporting credentials by <strong>December 1</strong>, and you are <strong>automatically considered</strong>. Successful applicants are notified of the award with their admission decision.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Incoming first-year undergraduate students</strong> at Boston University.</li>
        <li>Open to <strong>US citizens, US permanent residents, and international students</strong> (all nationalities).</li>
        <li><strong>Exceptional academic achievement</strong>, plus <strong>leadership, talent, initiative and creativity</strong> beyond the classroom and impact in school and community.</li>
        <li>Third-party sites report typical profiles of the <strong>top 5% of the high-school class</strong> and <strong>SAT above 1500 / ACT above 33</strong> — these are <strong>not</strong> published by Boston University as requirements, so treat them only as reported typical profiles, not cut-offs; Boston University states <strong>test scores are not required</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Half of undergraduate tuition per year</strong> for incoming first-year students.</li>
        <li>Renewable for up to <strong>four years</strong> of undergraduate study (per third-party sources; Boston University’s page does not state duration explicitly).</li>
        <li><strong>No separate scholarship application</strong> — automatic consideration on the admission application.</li>
        <li>Open to <strong>US and international students</strong> alike.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>These are the <strong>first-year admission application documents</strong>; no separate scholarship form exists.</li>
        <li>The <strong>Common Application</strong> (or Coalition Application).</li>
        <li><strong>Secondary school records/transcripts</strong> and senior-year grades.</li>
        <li>A <strong>counsellor recommendation and School Report Form</strong>, and a <strong>teacher evaluation/recommendation</strong>.</li>
        <li><strong>English proficiency test results</strong> (TOEFL/IELTS) where required.</li>
        <li>For international applicants: a <strong>copy of the passport data page</strong> and <strong>documentation of financial support</strong>.</li>
        <li><strong>Standardised test scores (SAT/ACT) if submitted — optional.</strong></li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for <strong>first-year undergraduate admission</strong> to Boston University via the <strong>Common Application</strong> (or Coalition Application).</li>
        <li>Submit the <strong>complete admission application and all supporting credentials by December 1</strong>.</li>
        <li><strong>No separate scholarship application, essay or form</strong> is required — all applicants who apply by December 1 are <strong>automatically considered</strong>.</li>
        <li>Successful applicants are <strong>notified of the award with their admission decision</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Boston University Presidential Scholarship?',
  'December 1 — Boston University publishes only "December 1", with no year attached. Third-party pages list 1 December 2026, which corresponds to Fall 2027 entry; for Fall 2026 entry the deadline was 1 December 2025 and has passed. This article frames the deadline as 1 December 2026 for the Fall 2027 entering class.'),
 ('How much is the Boston University Presidential Scholarship worth?',
  'Half of undergraduate tuition per year. The "$25,000 per academic year" figure repeated by Bright Scholarship and other aggregators is the pre-Fall 2026 value and is superseded by Boston University’s current half-tuition figure. It is renewable for up to four years of undergraduate study, per third-party sources.'),
 ('Is the Boston University Presidential Scholarship fully funded?',
  'No. It covers half of undergraduate tuition only — it does not cover housing, meals or other costs.'),
 ('Do I need a separate application for the Boston University Presidential Scholarship?',
  'No. There is no separate scholarship application, essay or form. You apply for first-year undergraduate admission by December 1 and are automatically considered; winners are notified with their admission decision.'),
 ('Who can apply for the Boston University Presidential Scholarship?',
  'Incoming first-year undergraduate students at Boston University — US citizens, US permanent residents and international students of all nationalities — with exceptional academic achievement plus leadership, talent, initiative and creativity beyond the classroom.'),
 ('What SAT or ACT score do I need for the Boston University Presidential Scholarship?',
  'Boston University publishes no score cut-off and states test scores are not required. Third-party sites report typical profiles of SAT above 1500 / ACT above 33 and the top 5% of the high-school class — treat those only as reported typical profiles, not requirements.'),
 ('When will I know if I won the Boston University Presidential Scholarship?',
  'Successful applicants are notified of the award with their admission decision.'),
 ('Can international students win the Boston University Presidential Scholarship?',
  'Yes. The scholarship is open to US citizens, US permanent residents and international students of all nationalities.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against Boston University's own merit-scholarships page (bu.edu/admissions/tuition-aid/scholarships-financial-aid/first-year-merit/, verified by direct fetch 28 Oct 2026 — confirms half tuition, December 1 deadline, eligibility, no separate application) and corroborated by Bright Scholarship (confirms the Dec 1 date and document list, but its USD 25,000 award figure is outdated): award — half of undergraduate tuition per year for incoming first-year students, effective for students entering Fall 2026 per BU's official page; renewable for up to four years of undergraduate study per third-party sources (BU's page does not state duration explicitly); not fully funded — does not cover housing, meals or other costs; eligibility — incoming first-year undergraduates, open to US citizens, US permanent residents and international students (all nationalities), exceptional academic achievement plus leadership, talent, initiative and creativity beyond the classroom and impact in school/community; documents are the first-year admission application documents (Common Application or Coalition Application, secondary school records/transcripts and senior-year grades, counsellor recommendation and School Report Form, teacher evaluation/recommendation, English proficiency test results where required, passport data page copy and documentation of financial support for international applicants, standardised test scores if submitted — optional); process — apply for first-year admission, submit the complete application and all supporting credentials by December 1, no separate scholarship application/essay/form, all applicants who apply by December 1 are automatically considered, winners notified with their admission decision. CONFLICTS: (1) The USD 25,000 per academic year figure repeated by Bright Scholarship and other aggregators is the pre-Fall 2026 value and is superseded by BU's current half-tuition figure — the article uses half tuition only. (2) Deadline year — BU publishes only "December 1" with no year attached; for Fall 2026 entry the deadline was 1 December 2025 (passed), so the article frames the live deadline as 1 December 2026 for the Fall 2027 entering class, with the caveat stated. (3) Typical profiles reported by third-party sites (top 5% of high-school class, SAT above 1500 / ACT above 33) are NOT published by BU as requirements — the article presents them only as reported typical profiles, and notes BU states test scores are not required.</p>''',
 dl_long='1 December 2026 (BU publishes "December 1"; Fall 2027 entry)',
 offlinks=[('Boston University — First-Year Merit Scholarships (official)', 'https://www.bu.edu/admissions/tuition-aid/scholarships-financial-aid/first-year-merit/'),
           ('Bright Scholarship — Boston University Presidential Scholarship 2026', 'https://brightscholarship.com/boston-university-presidential-scholarship-2026/')],
 related_titles=['york-pise-2027', 'duke-karsh-2026', 'miami-stamps-2027', 'ucl-impact-2027'])),

# ---------------------------------------------------------------- build + validate
class _P(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.errs = []
    def error(self, m): self.errs.append(m)

for a in A:
    _split_verify(a)
    n = build_article(BASE, OUT, a, CARDS)
    p = OUT / (a['slug'] + '.html')
    assert p.exists(), a['slug']
    t = p.read_text()
    for bad in ('AICTE Pragati', 'Lorem'):
        assert bad not in t, (a['slug'], bad)
    assert '#' not in a['slug'], a['slug']
    assert '919905166009' in t, a['slug'] + ' missing WhatsApp'
    pr = _P(); pr.feed(t)
    assert not pr.errs, (a['slug'], pr.errs)
    print('OK', a['slug'], n, 'chars')
print('built', len(A), 'articles')

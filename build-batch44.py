#!/usr/bin/env python3
"""Batch 44 (cron run 44, 24 Oct 2026): 5 new verified articles.

Queue scan order (next 5 not in done/skipped, all dl=None so none time-skipped):
1. Franz Werfel Scholarship Program 2027 in Austria (Funded) — VERIFIED: OeAD
   programme on behalf of Austria's Federal Ministry of Women, Science and
   Research; EUR 2,500/month for 4-9 month research stays (extendable to 18),
   for postgraduates/postdocs/researchers/lecturers with a strong Austrian
   literature focus; deadlines 1 March and 15 September each year — next is
   1 March 2027; travel subsidy up to EUR 1,200; follow-up support (Werfel
   conference, research grant, habilitation grant, publication allowance) after
   12 scholarship months. NOT a degree scholarship. Sources: aau.at (official
   OeAD listing), opportunityinside.com, daadscholarship.com, scholarshipunion.com.
2. ASEA-UNINET Ernst Mach Scholarship 2027 in Austria (Funded) — VERIFIED:
   OeAD + ASEA-UNINET for citizens of Indonesia, Malaysia, the Philippines,
   Thailand and Vietnam only; EUR 1,300/month all routes (+EUR 300/month mobility
   on the 36-month full PhD = EUR 1,600 effective; travel subsidy up to EUR
   1,200); postdoc 4-9 months; music practice 9 months at mdw/Mozarteum/KUG;
   deadline 1 March 2027; max age 35 (postdocs 45); strong English and/or German;
   ASEA-UNINET affiliation required only for the postdoc route. Supplemental
   grant, not "fully funded". Sources: oead.at official music-grant announcement
   PDF, hust.edu.vn official 2026/27 call PDF, inter.chula.ac.th official call page,
   scholarshipshive.com 2027 piece.
3. Cardiff University Vice-Chancellor's Scholarship 2027 in UK (Funded) — VERIFIED:
   postgraduate taught January 2027 intake; tuition-fee discount GBP 4,000
   (GBP 6,000 for Egypt/Kazakhstan/Kenya/Mexico/Pakistan/South Korea/Taiwan/USA/
   Vietnam; GBP 10,000 for Bangladesh/Nigeria); automatic consideration, no
   separate application; course application deadline 4 Dec 2026; Mainland China
   and Turkiye excluded; self-funded international-fee only; cannot defer.
   Sources: cardiff.ac.uk official January 2027 T&C document + official UG
   scholarship page, daadscholarship.com, ukscholarships.uk.
4. NCTU International Student Scholarships 2027 in Taiwan (Fully Funded) — VERIFIED:
   NCTU merged into National Yang Ming Chiao Tung University (NYCU) in Feb 2021;
   NYCU International Student Scholarship: stipend NT$7,000-25,000/month plus
   tuition waiver (official plans A-E); published 2027 figures: master's full
   tuition waiver + NT$22,000/month, PhD + NT$29,000/month, bachelor's up to
   NT$21,000/month; Fall 2027 applications open 20 Dec 2026, close 15 Mar 2027
   (11:59 AM GMT+8); Spring 2027 round closed 30 Sep 2026. Non-Taiwanese of all
   nationalities; no other scholarship. Sources: phil.nycu.edu.tw/en/admission
   (official), opportunitiesinfo.com, opportunityportal.info, bb-education.com,
   scholarshipbob.com.
5. University of Stirling Vice Chancellor Scholarship 2027 in UK (Funded) — VERIFIED:
   Vice Chancellor's Postgraduate International Scholarship: GBP 7,000 tuition-fee
   waiver for first year of an eligible taught master's (Sept 2027 or Jan 2028
   intake); separate scholarship application (2027-28 form); offer required;
   GBP 1,000 deposit secures it; batched rounds — round 1 closes 15 Dec 2026;
   online/MRes/MPhil/INTO pre-masters excluded; cannot combine with other
   Stirling awards. Sources: stir.ac.uk official scholarship page,
   scholarshipforphd.com, scholarshipunion.com, scholarshiproar.com.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 24)
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
 'franz-werfel-2027': {'mono': 'FW', 'title': 'Franz Werfel Scholarship Program 2027 in Austria (Funded)',
   'href': 'franz-werfel-scholarship-program-2027-austria.html',
   'dpill': 'Deadline 1 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-01'),
   'award': '\u20ac2,500/month for 4\u20139-month research stays (extendable to 18); travel subsidy up to \u20ac1,200; follow-up support after 12 scholarship months.',
   'elig': 'Postgraduates, postdocs, researchers and university lecturers with above-average qualifications and a strong Austrian-literature research focus; non-Austrians.',
   'tags': [('Postdoc & research', 'purple'), ('Austria', 'teal')]},
 'asea-uninet-2027': {'mono': 'AU', 'title': 'ASEA-UNINET Ernst Mach Scholarship 2027 in Austria (Funded)',
   'href': 'asea-uninet-ernst-mach-scholarship-2027-austria.html',
   'dpill': 'Deadline 1 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-01'),
   'award': '\u20ac1,300/month (+ \u20ac300/month mobility on the full PhD; travel up to \u20ac1,200): 36-month full PhD, 4\u20139-month postdoc, 9-month music practice.',
   'elig': 'Citizens of Indonesia, Malaysia, the Philippines, Thailand or Vietnam; under 35 (postdocs 45); strong English and/or German.',
   'tags': [("Master\u2019s & PhD", 'blue'), ('Austria', 'teal')]},
 'cardiff-vc-2027': {'mono': 'CU', 'title': "Cardiff University Vice-Chancellor's Scholarship 2027 in UK (Funded)",
   'href': 'cardiff-university-vice-chancellors-scholarship-2027-uk.html',
   'dpill': 'Apply by 4 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-04'),
   'award': 'Tuition-fee discount \u00a34,000 (\u00a36,000 for 9 listed countries; \u00a310,000 for Bangladesh/Nigeria). Automatic consideration, January 2027 intake.',
   'elig': 'International-fee, self-funded applicants to eligible full-time taught master\u2019s; meet published entry and English requirements.',
   'tags': [("Master\u2019s", 'blue'), ('UK', 'teal')]},
 'nctu-2027': {'mono': 'NYCU', 'title': 'NCTU International Student Scholarships 2027 in Taiwan (Fully Funded)',
   'href': 'nctu-international-student-scholarships-2027-taiwan.html',
   'dpill': 'Fall 2027: opens 20 Dec 2026 \u00b7 deadline 15 Mar 2027',
   'award': 'Tuition waiver + monthly stipend (published 2027 figures: NT$22,000 master\u2019s / NT$29,000 PhD; official plans range NT$7,000\u201325,000).',
   'elig': 'Non-Taiwanese international students; high-school diploma (UG) / bachelor\u2019s (master\u2019s) / master\u2019s (PhD); not holding another scholarship.',
   'tags': [('UG/PG/PhD', 'blue'), ('Taiwan', 'teal')]},
 'stirling-vc-2027': {'mono': 'US', 'title': 'University of Stirling Vice Chancellor Scholarship 2027 in UK (Funded)',
   'href': 'university-of-stirling-vice-chancellor-scholarship-2027-uk.html',
   'dpill': 'Round 1: 15 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-15'),
   'award': '\u00a37,000 tuition-fee waiver for the first year of an eligible taught master\u2019s. Separate application; \u00a31,000 deposit secures the award.',
   'elig': 'New international-fee, self-funded students with an offer for full-time on-campus taught PG study starting Sept 2027/Jan 2028.',
   'tags': [("Master\u2019s", 'blue'), ('UK', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Franz Werfel
A.append(dict(
 slug='franz-werfel-scholarship-program-2027-austria',
 title='Franz Werfel Scholarship Program 2027 in Austria (Funded)',
 meta='Franz Werfel Scholarship Program 2027: OeAD\u2019s \u20ac2,500/month research grant for Austrian-literature scholars, postdocs and university lecturers. 4\u20139 month stays in Austria, deadlines 1 March and 15 September each year \u2014 eligibility, benefits, documents, how to apply and FAQs.',
 short='Franz Werfel Scholarship Program 2027', kicker='Austria \u00b7 Fellowship \u00b7 Funded', mono='FW',
 prov_short='OeAD', prov_cat='Agency \u00b7 Austria',
 h1='Franz Werfel Scholarship Program 2027 in Austria (Funded)',
 sub='The Franz Werfel Scholarship Program 2027 pays \u20ac2,500 a month to postgraduates, postdocs, researchers and university lecturers whose work is centred on Austrian literature \u2014 funding a 4\u20139 month research stay in Austria, administered by the OeAD. The next deadline is 1 March 2027.',
 dpill='Deadline 1 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-01'),
 facts=facts([('Award', '\u20ac2,500 per month for a funded research stay of 4\u20139 months, with possible extensions taking total support up to 18 months. A travel-cost subsidy of up to \u20ac1,200 applies. After 12 scholarship months, follow-up support opens up: an annual Werfel conference invitation, a one-month research grant every three years (bundlable to three months), a habilitation grant, and a publication allowance.'),
              ('Eligible', 'Postgraduates, postdocs, researchers and university lecturers with above-average qualifications \u2014 preferably already teaching and employed at a university \u2014 whose research focuses substantially on Austrian literature. Applicants must not be Austrian citizens, must not have lived or worked in Austria in the six months before applying, must not be permanently resident in Austria, and must not have completed most of their academic education in Austria.'),
              ('How', 'Apply through the OeAD\u2019s scholarships.at application portal; the full call details are published in the OeAD grants database (grants.at). Two rounds close each year: 1 March and 15 September.'),
              ('Deadline', '1 March and 15 September every year. The 15 September 2026 round has closed; the next deadline is 1 March 2027.'),
              ('Fine print', 'This is a research-stay grant, not a degree scholarship: you come to Austria as a visiting researcher at a university department, using libraries, archives and research institutes. It does not fund a taught master\u2019s enrolment.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Franz Werfel Scholarship Program</strong> is one of Austria\u2019s most established funding routes for scholars of <strong>Austrian literature</strong>. Administered by the <strong>OeAD</strong> \u2014 Austria\u2019s Agency for Education and Internationalisation \u2014 on behalf of the Federal Ministry of Women, Science and Research, it supports visiting researchers, postdocs, PhD candidates and university lecturers who want to spend several months working in Austria\u2019s libraries, archives and university departments in cities like Vienna, Graz, Innsbruck and Salzburg.</p>
      <p>It is worth understanding what the grant is <em>not</em>: it is not a general humanities scholarship, not a degree programme, and not a route into a taught master\u2019s. It exists for researchers with a clear, demonstrable academic connection to Austrian literature \u2014 preferably with teaching experience and an established university profile \u2014 who will use the stay to advance real research.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>postgraduate, postdoc, researcher or university lecturer</strong> with above-average qualifications \u2014 preferably already teaching and employed at a university.</li>
        <li>Have research that <strong>focuses substantially on Austrian literature</strong> (the OeAD frames it as support for research and teaching in the field, strengthening an international network of Germanists).</li>
        <li>Come from <strong>any country of origin</strong> \u2014 Austrian citizens are excluded.</li>
        <li>Have <strong>not lived or worked in Austria</strong> in the six months before the scholarship application.</li>
        <li>Not be permanently resident in Austria and not have completed most of your academic education there.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac2,500 per month</strong> for a research stay of <strong>4\u20139 months</strong>, extendable to <strong>18 months</strong> in total.</li>
        <li><strong>Travel subsidy of up to \u20ac1,200</strong>.</li>
        <li>Placement as a visiting researcher at an Austrian university department, with access to libraries, archives and research institutes.</li>
        <li><strong>Follow-up support</strong> after at least 12 scholarship months: annual invitation to the Werfel conference, a one-month research grant every three years, a habilitation grant, and a publication allowance.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Academic CV and proof of qualifications and any teaching experience.</li>
        <li>A <strong>research proposal</strong> with a clear connection to Austrian literature and a work plan for the stay.</li>
        <li>Confirmation of a host contact at an Austrian university department, where the programme requires it.</li>
        <li>Passport and academic transcripts/degree certificates.</li>
        <li>The exact checklist for the current round is published in the official call entry \u2014 confirm it there before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the current call entry in the OeAD grants database (<strong>grants.at</strong>), which carries the full terms and documents.</li>
        <li>Submit your application through the OeAD application portal (<strong>scholarships.at</strong>) before the round closes.</li>
        <li>Aim for the <strong>1 March or 15 September</strong> round \u2014 15 September 2026 has passed, so the live target is <strong>1 March 2027</strong>.</li>
        <li>Do not confuse this track with the discontinued Richard Plaschka history grant \u2014 Werfel is the literature track that remains advertised.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Who can apply for the Franz Werfel Scholarship?',
  'Postgraduate students, PhD candidates, postdocs, researchers and university lecturers with above-average qualifications whose research focuses on Austrian literature. The OeAD prefers applicants with teaching experience and an established university profile. All countries of origin are eligible except Austria.'),
 ('How much is the Franz Werfel grant worth?',
  '\u20ac2,500 per month for 4\u20139 months, with possible extensions to 18 months, plus a travel subsidy of up to \u20ac1,200. A nine-month stay alone can exceed \u20ac22,500.'),
 ('When is the deadline?',
  'Twice a year: 1 March and 15 September. The 15 September 2026 round is closed, so the next deadline is 1 March 2027.'),
 ('Can it fund a master\u2019s degree in Austria?',
  'No. This is a funded research stay for visiting researchers, not a taught-degree scholarship and not a route into master\u2019s enrolment.'),
 ('What is the follow-up support after the grant?',
  'After completing at least 12 scholarship months, fellows can access an annual invitation to the Werfel conference, a one-month research grant every three years (bundlable up to three months), a habilitation grant and a publication allowance.')]) + '''
      <p class="verify">Verified 24 Oct 2026: aau.at/en/doctoral-programme/grants-scholarships/ (official University of Klagenfurt listing of the OeAD programme) \u2014 \u20ac2,500/month, 4\u20139 months, 1 March/15 September annual deadlines, early-career researchers with teaching experience and university position, 6-months-prior non-residence rule; opportunityinside.com/fellowships/franz-werfel-grant-austria-2027.html \u2014 two annual dates, 15 Sept 2026 closed, next 1 Mar 2027, applications via scholarships.at, follow-up benefits; daadscholarship.com/austrian-franz-werfel-scholarship-2027-new-application-method-discussed/ + scholarshipunion.com/franz-werfel-scholarship-2027-austria/ \u2014 \u20ac2,500/month, 4\u20139 months extendable to 18, OeAD on behalf of the Federal Ministry of Women, Science and Research. Exact document checklist not extracted from the official call entry.</p>''',
 dl_long='March 1, 2027 (annual rounds on 1 March and 15 September; the 15 September 2026 round has closed)',
 offlinks=[('University of Klagenfurt \u2014 OeAD Franz Werfel Scholarship (official listing)', 'https://www.aau.at/en/doctoral-programme/grants-scholarships/'),
           ('Bright Scholarship \u2014 Franz Werfel Scholarship Program 2027', 'https://brightscholarship.com/franz-werfel-scholarship-program-in-austria/')],
 related_titles=['neukom-2027', 'trudeau-2027', 'hkpfs-2027', 'lawai-2027'])),

# ---------------------------------------------------------------- 2. ASEA-UNINET Ernst Mach
A.append(dict(
 slug='asea-uninet-ernst-mach-scholarship-2027-austria',
 title='ASEA-UNINET Ernst Mach Scholarship 2027 in Austria (Funded)',
 meta='ASEA-UNINET Ernst Mach Scholarship 2027: OeAD\u2019s \u20ac1,300/month grant for PhD, postdoc and music-practice routes in Austria \u2014 citizens of Indonesia, Malaysia, the Philippines, Thailand and Vietnam. Deadline 1 March 2027. Eligibility, benefits, documents, how to apply and FAQs.',
 short='ASEA-UNINET Ernst Mach Scholarship 2027', kicker='Austria \u00b7 PhD/Postdoc/Music \u00b7 Funded', mono='AU',
 prov_short='OeAD / ASEA-UNINET', prov_cat='Agency \u00b7 Austria',
 h1='ASEA-UNINET Ernst Mach Scholarship 2027 in Austria (Funded)',
 sub='The ASEA-UNINET Ernst Mach Scholarship 2027 is Austria\u2019s OeAD grant for a narrowly defined group: citizens of Indonesia, Malaysia, the Philippines, Thailand and Vietnam. It funds a full 36-month PhD, a postdoc research stay, or nine months of music practice \u2014 with \u20ac1,300 a month, deadline 1 March 2027.',
 dpill='Deadline 1 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-01'),
 facts=facts([('Award', 'A monthly grant of \u20ac1,300 on every route. The full PhD route adds a \u20ac300/month mobility subsidy (\u20ac1,600/month effective) over 36 months. A travel-cost subsidy of up to \u20ac1,200 applies. This is a supplemental grant \u2014 it is not labelled \u201cfully funded\u201d: scholars cover their own housing and health insurance (roughly \u20ac55\u2013200/month), and tuition at Austrian public universities may be waived on request but is not automatic; private-university fees are not covered.'),
              ('Eligible', 'Citizenship of Indonesia, Malaysia, the Philippines, Thailand or Vietnam (citizenship, not just residence). Full PhD: postgraduates who meet admission requirements and completed their studies outside Austria. Postdoc: postdocs involved in teaching and research at an ASEA-UNINET member university (ASEA-UNINET affiliation is required only for this route). Music Practice: undergraduates or higher in instrumental/vocal performance, composition or conducting. Maximum age 35 (postdocs 45); very good English and/or German; all fields of study. Not lived, studied or worked in Austria in the six months before the grant; not permanently resident there.'),
              ('How', 'Apply through the OeAD grants portal (grants.at) before the call closes; the official call announcements are published there and through ASEA-UNINET member universities\u2019 international offices.'),
              ('Deadline', '1 March 2027 for the full PhD and postdoc routes. The Music Practice Grant runs on its own calendar \u2014 its 2026/27 round closed on 15 December 2025 with auditions in February 2026; next-round dates were not published in the official notification checked.'),
              ('Fine print', 'Applicants must provide their own supplementary funding \u2014 the OeAD is explicit that this is a supplemental award. The music-practice auditions are held by video interview for shortlisted candidates.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Ernst Mach Grant \u2013 ASEA-UNINET</strong> is offered by the Austrian Federal Ministry of Women, Science and Research through the <strong>OeAD</strong> in cooperation with <strong>ASEA-UNINET</strong>, the university network linking Europe and Southeast Asia. It exists to move knowledge \u2014 and people \u2014 between Austrian universities and the five eligible Southeast Asian countries. Unlike the worldwide Ernst Mach routes, this one is <strong>restricted by citizenship</strong>: it only works if you hold a passport from one of the five countries, and no amount of academic strength changes that.</p>
      <p>Three routes share the grant name: a <strong>full PhD</strong> (the strongest option \u2014 a genuine 36-month funded doctorate), a <strong>postdoc research stay</strong>, and a <strong>music practice grant</strong> for performers, composers and conductors at the University of Music and Performing Arts Vienna, the Mozarteum Salzburg, or the University of Music and Performing Arts Graz. All fields of study are covered on the PhD and postdoc routes.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold <strong>citizenship of Indonesia, Malaysia, the Philippines, Thailand or Vietnam</strong> \u2014 only these five nationalities can apply.</li>
        <li><strong>Full PhD:</strong> be a postgraduate wanting to carry out a complete doctorate in Austria, fulfilling the admission requirements and having completed your studies at a university outside Austria.</li>
        <li><strong>Postdoc:</strong> be a postdoc involved in teaching and research at an <strong>ASEA-UNINET member university</strong> (affiliation is only required for this route; other routes are open to alumni of non-member institutions too).</li>
        <li><strong>Music practice:</strong> be an undergraduate or above in instrumental or vocal performance, composition or conducting.</li>
        <li>Be under <strong>35</strong> (undergraduates, graduates, postgraduates) or under <strong>45</strong> (postdocs).</li>
        <li>Have <strong>very good English and/or German</strong>, matching the requirements of the chosen programme.</li>
        <li>Have <strong>not lived, studied or worked in Austria</strong> in the six months before the grant, and not be permanently resident there.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac1,300 per month</strong> on all three routes.</li>
        <li><strong>Full PhD:</strong> an extra \u20ac300/month mobility subsidy (\u20ac1,600/month effective) over <strong>36 months</strong>.</li>
        <li><strong>Postdoc:</strong> 4\u20139 months at \u20ac1,300/month (confirm the current duration in the live call entry \u2014 some 2027 summaries describe this route as 4\u20136 months).</li>
        <li><strong>Music practice:</strong> 9 months at \u20ac1,300/month, with travel-cost subsidy.</li>
        <li><strong>Travel subsidy of up to \u20ac1,200</strong> against verified receipts.</li>
        <li>Be honest about the gaps: housing and health insurance are on you (insurance typically \u20ac55\u2013200/month); tuition at Austrian public universities may be waived on request but is not automatic, and private-university fees are excluded.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Online application through the OeAD grants portal with academic records and CV.</li>
        <li>Study or research proposal for the PhD/postdoc route; proof that you meet admission requirements for a full doctorate.</li>
        <li>Proof of citizenship of one of the five eligible countries.</li>
        <li>Evidence of language proficiency (English and/or German).</li>
        <li>For music practice: performance records and audition-ready material, per the route\u2019s announcement.</li>
        <li>Confirm the exact document checklist in the current call entry on grants.at before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the official call entry on the OeAD grants portal (<strong>grants.at</strong>) for your route \u2014 or the call page published by an ASEA-UNINET member university\u2019s international office.</li>
        <li>Submit the full application online by <strong>1 March 2027</strong> (full PhD and postdoc routes).</li>
        <li>Music-practice applicants: the 2026/27 round is closed (deadline 15 December 2025, auditions February 2026); watch for the next round\u2019s announcement separately.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Which nationalities can apply?',
  'Only citizens of Indonesia, Malaysia, the Philippines, Thailand and Vietnam. Citizenship is the eligibility test \u2014 residence elsewhere does not qualify.'),
 ('What does the full PhD route pay?',
  '\u20ac1,300/month plus a \u20ac300/month mobility subsidy (\u20ac1,600 effective) for 36 months, plus a travel subsidy of up to \u20ac1,200. It is a supplemental award \u2014 housing, health insurance and living costs beyond the grant are your own.'),
 ('Is ASEA-UNINET affiliation required?',
  'Only for the postdoc route, where you must be teaching and researching at an ASEA-UNINET member university. Full PhD and music-practice applicants can also be students or alumni of non-member institutions.'),
 ('What is the deadline?',
  '1 March 2027 for the full PhD and postdoc routes. The Music Practice Grant runs on a separate calendar whose next-round dates were not published in the official notification checked.'),
 ('Is this \u201cfully funded\u201d?',
  'No \u2014 the OeAD describes it as a supplemental grant. Treat it as a substantial government stipend that still needs personal budgeting for housing, insurance and any tuition not waived.')]) + '''
      <p class="verify">Verified 24 Oct 2026: oead.at/fileadmin/Dokumente/oead.at/OeAD_Hauptmenueseiten/Studieren_Forschen_Lehren/ASEA-UNINET/Music_Practice_Grant_Announcement__Call_2026_27.pdf (official OeAD announcement) \u2014 9-month music grant, 5 countries, \u20ac1,300/month, travel subsidy up to \u20ac1,200, deadline 15 Dec 2025, Feb 2026 Zoom auditions; hust.edu.vn official 2026/27 call PDF \u2014 full PhD 36 months at \u20ac1,300 + \u20ac300 mobility + \u20ac1,200 travel, postdoc 4\u20139 months, music 9 months, citizenship rule, age 35/45, all fields; inter.chula.ac.th/funding-opportunity/28490/ (official call page) \u2014 \u20ac1,600 effective for full PhD, affiliation only required for postdoc route; scholarshipshive.com/austrias-ernst-mach-grant-asea-uninet-strong-funding-restricted-to-five-countries/ \u2014 deadline 1 March 2027, 2027-route structure. Next music-practice round dates not published in the official notification.</p>''',
 dl_long='March 1, 2027 (full PhD and postdoc routes; Music Practice Grant runs on a separate calendar)',
 offlinks=[('Hanoi University of Science and Technology \u2014 Ernst Mach ASEA-UNINET call 2026/27 (official call PDF)', 'https://hust.edu.vn/uploads/sys/hop-tac-doi-ngoai/2025_12/info-ernst-mach-grant-asea-uninet-call-2026_27.pdf'),
           ('Chulalongkorn University \u2014 Ernst Mach Grant ASEA-UNINET call page (official)', 'https://www.inter.chula.ac.th/funding-opportunity/28490/'),
           ('Bright Scholarship \u2014 ASEA-UNINET Ernst Mach Scholarship 2027', 'https://brightscholarship.com/asea-uninet-ernst-mach-scholarship/')],
 related_titles=['kaist-grad-2027', 'gxnu-csc-2027', 'hkpfs-2027', 'swinburne-2027'])),
# ---------------------------------------------------------------- 3. Cardiff VC
A.append(dict(
 slug='cardiff-university-vice-chancellors-scholarship-2027-uk',
 title="Cardiff University Vice-Chancellor's Scholarship 2027 in UK (Funded)",
 meta="Cardiff University Vice-Chancellor\u2019s Scholarship 2027: \u00a34,000\u2013\u00a310,000 tuition-fee discount for international taught master\u2019s students (January 2027 intake). Automatic consideration, no separate application \u2014 eligibility, award tiers by domicile, deadlines and FAQs.",
 short="Cardiff University Vice-Chancellor's Scholarship 2027", kicker="UK \u00b7 Master's \u00b7 Tuition discount", mono='CU',
 prov_short='Cardiff University', prov_cat='University \u00b7 United Kingdom',
 h1="Cardiff University Vice-Chancellor's Scholarship 2027 in UK (Funded)",
 sub='Cardiff University\u2019s Vice-Chancellor\u2019s Scholarship 2027 cuts up to \u00a310,000 off tuition for international students starting a taught master\u2019s in January 2027 \u2014 \u00a34,000 as standard, \u00a36,000 or \u00a310,000 depending on where you are domiciled. There is no separate application: meet the conditions and Cardiff considers you automatically.',
 dpill='Apply by 4 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-04'),
 facts=facts([('Award', 'A tuition-fee discount only: \u00a34,000 as standard; \u00a36,000 for students domiciled in Egypt, Kazakhstan, Kenya, Mexico, Pakistan, South Korea, Taiwan, the USA or Vietnam; \u00a310,000 for students domiciled in Bangladesh or Nigeria. There is no cash alternative, no living stipend, and it cannot be used in place of any required admission deposit. Students domiciled in Mainland China or T\u00fcrkiye are not eligible for this scheme (alternative Cardiff schemes may apply).'),
              ('Eligible', 'Classed as an international student for fee purposes and domiciled in an eligible country (domicile means ordinarily resident for three years or more before the course starts, not counting time spent studying elsewhere). Entering an eligible full-time, Cardiff campus-based taught postgraduate programme in the January 2027 intake; meet the published academic entry requirements and English-language conditions; be self-funded. No separate scholarship application \u2014 eligible offer-holders are considered automatically. The award cannot be deferred to a later entry year.'),
              ('How', 'Apply for an eligible postgraduate taught programme through Cardiff\u2019s normal admissions route by the course-application deadline; meet your offer conditions and accept the offer. If you meet the scholarship criteria in the official terms, the award is applied automatically.'),
              ('Deadline', 'Course applications for the January 2027 intake close on 4 December 2026, with offer acceptance and deposit by 11 December 2026 (per the published scholarship cycle \u2014 confirm the current dates on cardiff.ac.uk). Eligibility queries must be raised by 30 March 2027.'),
              ('Fine print', 'The January 2027 scheme is distinct from Cardiff\u2019s undergraduate Vice-Chancellor\u2019s scholarship (\u00a33,500/\u00a35,000 for September 2027 entry). This article covers the postgraduate January 2027 route only.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>Cardiff University runs a family of Vice-Chancellor\u2019s scholarships across undergraduate and postgraduate entry. The <strong>Vice-Chancellor\u2019s Postgraduate International Scholarship 2027</strong> is the master\u2019s route: a <strong>tuition-fee discount of \u00a34,000 to \u00a310,000</strong> for international students entering an eligible taught postgraduate programme in the <strong>January 2027 intake</strong>. Cardiff\u2019s model is unusually simple \u2014 there is no scholarship essay, no second portal, no nomination: if you hold an offer for an eligible programme and meet the published criteria, the university considers you <strong>automatically</strong>.</p>
      <p>Be clear about what it is: a partial tuition discount, not a fully funded scholarship. It trims the first-year tuition bill and leaves living costs, visa finances and the deposit entirely to you. The award tier depends on <strong>domicile</strong> \u2014 where you have ordinarily lived for the past three years \u2014 not simply on passport nationality.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be classified as an <strong>international student for fee-paying purposes</strong>.</li>
        <li>Be <strong>domiciled in an eligible country</strong>: ordinarily resident for three years or longer before the course starts (time spent studying elsewhere does not count). Mainland China and T\u00fcrkiye are <strong>excluded</strong> from this scheme.</li>
        <li>Enter an <strong>eligible full-time, Cardiff campus-based taught postgraduate programme</strong> in the <strong>January 2027</strong> intake \u2014 the award applies to year 1 only and cannot be deferred.</li>
        <li>Meet the <strong>published academic entry requirements</strong> of your chosen course exactly as stated at application time, plus the <strong>English-language conditions</strong> in your offer.</li>
        <li>Be a <strong>self-funded student</strong>.</li>
        <li>There is <strong>no separate scholarship application</strong> \u2014 eligible offer-holders are considered automatically.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u00a34,000 tuition-fee discount</strong> for most eligible international students.</li>
        <li><strong>\u00a36,000</strong> for students domiciled in <strong>Egypt, Kazakhstan, Kenya, Mexico, Pakistan, South Korea, Taiwan, the USA or Vietnam</strong>.</li>
        <li><strong>\u00a310,000</strong> for students domiciled in <strong>Bangladesh or Nigeria</strong>.</li>
        <li>Applied against tuition \u2014 <strong>no cash alternative</strong>, and it cannot substitute for the required admission deposit.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>programme application</strong> with academic transcripts and degree certificates.</li>
        <li>Evidence meeting the published <strong>entry requirements</strong> for your course.</li>
        <li><strong>English-language evidence</strong> satisfying your offer conditions.</li>
        <li>Any documents proving domicile where Cardiff asks for them \u2014 confirm current requirements on the official terms.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for an <strong>eligible taught master\u2019s programme</strong> at Cardiff University by the course-application deadline (<strong>4 December 2026</strong> for the January 2027 intake).</li>
        <li><strong>Accept your offer and pay the required deposit</strong> by the acceptance deadline (<strong>11 December 2026</strong> per the published cycle).</li>
        <li>Meet all offer conditions, including English-language requirements.</li>
        <li>There is <strong>nothing further to submit</strong> \u2014 Cardiff assesses scholarship eligibility automatically on enrolment.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a separate scholarship application?',
  'No. The Vice-Chancellor\u2019s Postgraduate International Scholarship is awarded automatically to eligible offer-holders \u2014 there is no scholarship form or essay.'),
 ('How much is the award for my country?',
  '\u00a34,000 is standard. Students domiciled in Egypt, Kazakhstan, Kenya, Mexico, Pakistan, South Korea, Taiwan, the USA or Vietnam receive \u00a36,000; those domiciled in Bangladesh or Nigeria receive \u00a310,000. Students domiciled in Mainland China or T\u00fcrkiye are not eligible for this scheme.'),
 ('Is it fully funded?',
  'No. It is a partial tuition-fee discount for the first year \u2014 no living stipend, no cash alternative, and it cannot be used in place of the admission deposit. You must still satisfy UKVI financial requirements independently.'),
 ('What does domicile mean here?',
  'Where you have been ordinarily resident for a three-year period or longer before the course starts. Time you spent living somewhere else purely for study does not count.'),
 ('Can I defer the scholarship?',
  'No. The award is for January 2027 entry only and cannot be transferred to a later entry year; deferred entrants must re-apply for whatever scheme covers 2027/28 entry.')]) + '''
      <p class="verify">Verified 24 Oct 2026: cardiff.ac.uk/documents/2873088-vice-chancellors-international-scholarship-terms-and-conditions-for-january-2026-entry (official January 2027 entry T&C) \u2014 \u00a34,000/\u00a36,000/\u00a310,000 tiers by domicile, Mainland China and T\u00fcrkiye excluded, automatic consideration, tuition-discount only, January 2027 entry only, non-deferrable, self-funded, full-time campus-based, domicile definition, queries by 30 Mar 2027; cardiff.ac.uk/study/international/funding-and-fees/international-scholarships/vice-chancellors-international-scholarship-ug (official) \u2014 confirms the separate UG scheme (\u00a33,500/\u00a35,000, apply by 30 Jun 2027); daadscholarship.com/cardiff-university-vice-chancellors-scholarship-2027-for-masters-admissions-process/ \u2014 4 Dec 2026 application and 11 Dec 2026 acceptance/deposit dates, country tiers; ukscholarships.uk/scholarships/cardiff-university-vice-chancellor-scholarship-uk-2027 \u2014 eligibility corroboration. Deadline dates 4/11 Dec 2026 come from the secondary source \u2014 confirm on the official page before applying.</p>''',
 dl_long='December 4, 2026 (course application; offer acceptance and deposit by December 11, 2026 \u2014 per the published scholarship cycle; confirm on cardiff.ac.uk)',
 offlinks=[('Cardiff University \u2014 Vice-Chancellor\u2019s International Scholarship T&C, January 2027 entry (official)', 'https://www.cardiff.ac.uk/documents/2873088-vice-chancellors-international-scholarship-terms-and-conditions-for-january-2026-entry'),
           ('Cardiff University \u2014 Vice-Chancellor\u2019s International Scholarship, UG (official)', 'https://www.cardiff.ac.uk/study/international/funding-and-fees/international-scholarships/vice-chancellors-international-scholarship-ug'),
           ('Bright Scholarship \u2014 Cardiff University Vice-Chancellor\u2019s Scholarship 2027', 'https://brightscholarship.com/cardiff-university-vice-chancellors-scholarship/')],
 related_titles=['boustany-cam-2027', 'glos-merit-2027', 'gates-cam-2027', 'swinburne-2027'])),

# ---------------------------------------------------------------- 4. NCTU/NYCU
A.append(dict(
 slug='nctu-international-student-scholarships-2027-taiwan',
 title='NCTU International Student Scholarships 2027 in Taiwan (Fully Funded)',
 meta='NCTU/NYCU International Student Scholarships 2027: National Yang Ming Chiao Tung University\u2019s tuition-waiver + monthly-stipend awards for international bachelor\u2019s, master\u2019s and PhD students. Fall 2027 deadline 15 March 2027 \u2014 eligibility, benefits, documents, how to apply and FAQs.',
 short='NCTU International Student Scholarships 2027', kicker='Taiwan \u00b7 Master\u2019s \u00b7 Tuition + stipend', mono='NYCU',
 prov_short='NYCU (formerly NCTU)', prov_cat='University \u00b7 Taiwan',
 h1='NCTU International Student Scholarships 2027 in Taiwan (Fully Funded)',
 sub='The NCTU International Student Scholarships 2027 are awarded by National Yang Ming Chiao Tung University (NYCU) \u2014 the university NCTU became after its 2021 merger. International master\u2019s and PhD students can receive a full tuition waiver plus a monthly stipend; the Fall 2027 intake opens 20 December 2026 and closes 15 March 2027.',
 dpill='Fall 2027: opens 20 Dec 2026 \u00b7 deadline 15 Mar 2027',
 facts=facts([('Award', 'The NYCU International Student Scholarship combines a monthly stipend and a tuition award. Official award plans: Plan A \u2014 monthly stipend NT$7,000\u201325,000 + full waiver of tuition and credit fees; Plan B \u2014 stipend + tuition at local-student rates; Plan C \u2014 stipend only; Plan D \u2014 local-rate tuition only. Published 2027 figures: master\u2019s students a full tuition waiver + NT$22,000/month stipend; doctoral students a tuition waiver + NT$29,000/month; bachelor\u2019s up to NT$21,000/month. Awards run for one year and are renewable on academic performance.'),
              ('Eligible', 'Non-Taiwanese international applicants of all nationalities. A high-school diploma for undergraduate, a bachelor\u2019s degree for master\u2019s, a master\u2019s degree for doctoral programmes; good physical and mental health; applicants must not be receiving any other scholarship.'),
              ('How', 'Apply through NYCU\u2019s online admission system by the intake deadline, selecting the scholarship option (\u201cNCTU Scholarship\u201d in the admission application) for scholarship consideration. No IELTS is required where an official letter confirms your previous degree was taught in English.'),
              ('Deadline', 'Fall 2027: the online system opens 20 December 2026 and closes at 11:59 AM on 15 March 2027 (GMT+8); results around mid-May 2027; admitted students reply by late May 2027; classes begin early September 2027. The Spring 2027 round (graduate programmes only) closed on 30 September 2026.'),
              ('Fine print', '\u201cNCTU\u201d is the pre-2021 name \u2014 the awarding university is now NYCU (National Yang Ming Chiao Tung University), formed by the February 2021 merger of NCTU and National Yang Ming University. Graduate scholarship renewal typically requires a 3.5 GPA (3.0 for undergraduates) plus Mandarin course enrolment, per published programme rules.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>One point of housekeeping first: <strong>NCTU no longer exists under that name</strong>. In February 2021, National Chiao Tung University merged with National Yang Ming University to form <strong>National Yang Ming Chiao Tung University (NYCU)</strong> \u2014 one of Taiwan\u2019s leading research universities. Scholarship aggregators (including the one this topic came from) still call it \u201cNCTU\u201d, and the admission system may still show an \u201cNCTU Scholarship\u201d option, but the institution awarding the money is NYCU.</p>
      <p>The <strong>NYCU International Student Scholarship</strong> is the university\u2019s own award for incoming international students across undergraduate, master\u2019s and doctoral programmes. It is structured in two parts: a <strong>monthly stipend</strong> (funded partly by the Office of International Affairs, sometimes topped up by your college, department or advisor) and a <strong>tuition award</strong> (a full waiver of tuition and credit fees, or tuition at local Taiwanese-student rates). You can receive one or both parts, and the award runs for one year at a time.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Taiwanese international applicant</strong> of any nationality.</li>
        <li>Hold a <strong>high-school diploma</strong> (undergraduate), a <strong>bachelor\u2019s degree</strong> (master\u2019s), or a <strong>master\u2019s degree</strong> (doctoral).</li>
        <li>Be in <strong>good physical and mental health</strong>.</li>
        <li><strong>Not be a recipient of any other scholarship</strong> at the time of application.</li>
        <li>Fill the application form correctly, honestly and completely, with all required materials.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Master\u2019s:</strong> full tuition waiver + <strong>NT$22,000/month</strong> stipend; research assistantship from an advisor.</li>
        <li><strong>Doctoral:</strong> tuition waiver + <strong>NT$29,000/month</strong> stipend; research assistantship from an advisor.</li>
        <li><strong>Bachelor\u2019s:</strong> up to <strong>NT$21,000/month</strong> and/or tuition waiver.</li>
        <li>The university\u2019s official admission page frames the award as plans A\u2013E: stipend of <strong>NT$7,000\u201325,000/month</strong> combined with either a full tuition waiver, local-rate tuition, or no tuition component.</li>
        <li>Awards are granted for <strong>one year</strong> and renewable \u2014 published programme rules require a minimum GPA of <strong>3.5 for graduate students</strong> (3.0 for undergraduates) plus Mandarin course enrolment for renewal.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Completed <strong>online application form</strong>.</li>
        <li><strong>Highest-degree diploma</strong> verified with official stamps, and the <strong>highest-degree transcript</strong>.</li>
        <li><strong>Two recommendation/reference letters</strong> (from a teacher, advisor or employer).</li>
        <li>Copy of a valid <strong>passport</strong>.</li>
        <li><strong>Study plan</strong> written in English or Chinese.</li>
        <li><strong>English proficiency evidence</strong> \u2014 or an official letter confirming your previous degree was taught in English (no IELTS required in that case).</li>
        <li><strong>Academic thesis or relevant publications</strong> (PhD applicants).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check the NYCU admission pages for your programme and its requirements.</li>
        <li>Submit the <strong>online application</strong> through the university\u2019s admission system before the intake deadline.</li>
        <li>Select the <strong>\u201cNCTU Scholarship\u201d option</strong> in the admission application to be considered for the award.</li>
        <li>Upload all documents \u2014 diploma, transcripts, recommendation letters, passport, study plan, language evidence \u2014 by the deadline.</li>
        <li>Wait for results (around mid-May 2027 for the Fall intake) and reply by the admitted-students deadline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is NCTU the same as NYCU?',
  'NCTU (National Chiao Tung University) merged with National Yang Ming University in February 2021 to form National Yang Ming Chiao Tung University (NYCU). Scholarship sites still write \u201cNCTU\u201d, but the awarding university \u2014 and the name to look for on the official site \u2014 is NYCU.'),
 ('What are the 2027 deadlines?',
  'Fall 2027: applications open 20 December 2026 and close at 11:59 AM on 15 March 2027 (Taiwan time). Results come around mid-May 2027 and classes start in early September 2027. The Spring 2027 round closed on 30 September 2026.'),
 ('How much money does it actually pay?',
  'Published 2027 figures: NT$22,000/month for master\u2019s, NT$29,000/month for PhD, up to NT$21,000/month for bachelor\u2019s \u2014 with tuition waivers. The university\u2019s official plans show stipends of NT$7,000\u201325,000/month combined with full or local-rate tuition, so the exact package depends on the award plan you receive.'),
 ('Is IELTS required?',
  'Not necessarily \u2014 if your previous degree was taught in English, an official letter from your previous institution confirming that can stand in for a test score.'),
 ('Can I hold another scholarship at the same time?',
  'No. Recipients of any other scholarship are not eligible for the NYCU International Student Scholarship.')]) + '''
      <p class="verify">Verified 24 Oct 2026: phil.nycu.edu.tw/en/admission/ (official NYCU admission page) \u2014 NYCU International Student Scholarship (1 year), Plans A\u2013E with monthly stipend NT$7,000\u201325,000 and tuition waiver/local-rate options; opportunitiesinfo.com/nycu-nctu-international-scholarships-2026/ + opportunityportal.info/nctu-international-student-scholarship/ \u2014 Fall 2027 dates (system opens 20 Dec 2026, deadline 15 Mar 2027 11:59 AM GMT+8, results mid-May 2027, classes early Sep 2027) and Spring 2027 dates (opened 10 Aug 2026, closed 30 Sep 2026); bb-education.com/nctu-scholarship-2027-in-taiwan-fully-funded/ + scholarshipbob.com/scholarship/national-chiao-tung-university-nctu-scholarship-2027-fully-funded \u2014 NCTU\u2192NYCU merger, NT$21,000/22,000/29,000 figures, document list, \u201cselect NCTU Scholarship\u201d application step. Stipend payment-date and GPA/Mandarin renewal rules from a single secondary source each.</p>''',
 dl_long='March 15, 2027, 11:59 AM Taiwan time (Fall 2027; the online system opens December 20, 2026)',
 offlinks=[('NYCU \u2014 Admission, scholarship information for international students (official)', 'https://phil.nycu.edu.tw/en/admission/'),
           ('Bright Scholarship \u2014 NCTU International Student Scholarships 2027', 'https://brightscholarship.com/nctu-international-student-scholarships/')],
 related_titles=['kaist-grad-2027', 'gxnu-csc-2027', 'hawaii-ewc', 'swinburne-2027'])),
# ---------------------------------------------------------------- 5. Stirling VC
A.append(dict(
 slug='university-of-stirling-vice-chancellor-scholarship-2027-uk',
 title='University of Stirling Vice Chancellor Scholarship 2027 in UK (Funded)',
 meta='University of Stirling Vice Chancellor Scholarship 2027: \u00a37,000 tuition-fee waiver for international taught master\u2019s students (Sept 2027 / Jan 2028 intake). Separate scholarship application; \u00a31,000 deposit secures it; first round closes 15 December 2026 \u2014 eligibility, benefits, rounds, FAQs.',
 short='University of Stirling Vice Chancellor Scholarship 2027', kicker="Scotland \u00b7 Master's \u00b7 Tuition waiver", mono='US',
 prov_short='University of Stirling', prov_cat='University \u00b7 United Kingdom',
 h1='University of Stirling Vice Chancellor Scholarship 2027 in UK (Funded)',
 sub='The University of Stirling Vice Chancellor Scholarship 2027 is a \u00a37,000 tuition-fee waiver for new international students on a full-time taught master\u2019s \u2014 for September 2027 or January 2028 entry. It needs a separate scholarship application on top of your course application, and the first application round closes on 15 December 2026.',
 dpill='Round 1: 15 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-15'),
 facts=facts([('Award', '\u00a37,000 tuition-fee waiver for the first year of an eligible master\u2019s degree \u2014 applied against fees, not paid as cash. It is not a fully funded scholarship: living costs, accommodation, visa fees and travel are yours. It cannot be combined with any other University of Stirling scholarship or award; if you qualify for more than one, the highest-value award is applied.'),
              ('Eligible', 'New students starting in September 2027 or January 2028; classed as international for tuition-fee purposes; self-funded (external sponsorship or other scholarships disqualify you); holding a conditional or unconditional offer for an eligible full-time postgraduate taught course delivered at the Stirling campus \u2014 applications without a valid offer are not assessed. Online degrees, MRes and MPhil are not eligible; students progressing from an INTO pre-master\u2019s course are not eligible (INTO progression awards may apply instead). Read the terms and conditions before applying.'),
              ('How', 'Submit the separate \u201cVice Chancellor\u2019s Scholarship Application 2027-28\u201d form after securing your course offer. Applications are assessed and added to a wait list as scholarship funding becomes available; if you are offered a scholarship, pay the \u00a31,000 deposit by the deadline in your offer letter to secure it. Stirling aims to inform all applicants of the outcome by 15 July.'),
              ('Deadline', 'Applications are assessed in rounds. Round 1 runs 1 September \u2013 15 December 2026 (decisions by 21 December 2026; deposit by 1 February 2027); further rounds run through June 2027, and a January-2028 round runs 16 June \u2013 30 October 2027. Round dates come from published scholarship summaries \u2014 confirm the live round dates on stir.ac.uk before applying.'),
              ('Fine print', 'The \u00a31,000 deposit is required to secure the award and is separate from any course deposit. The university\u2019s automatic International Undergraduate Scholarship (\u00a32,500/year) is a different scheme and does not apply here.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Vice Chancellor\u2019s Postgraduate International Scholarship</strong> is the University of Stirling\u2019s flagship master\u2019s award for international students. It cuts <strong>\u00a37,000 off first-year tuition</strong> for new, self-funded international students on eligible full-time taught master\u2019s programmes starting in <strong>September 2027 or January 2028</strong>. Unlike Stirling\u2019s undergraduate scholarship \u2014 which is automatic \u2014 this one needs a <strong>separate scholarship application</strong> once you hold a course offer, and awards are allocated from a wait list as funding becomes available.</p>
      <p>Two things to get right early: you must be self-funded (any external sponsorship or another scholarship takes you out of the running), and the award is a fee waiver, not cash \u2014 it trims \u00a37,000 from your tuition bill and nothing from your living costs.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be classed as an <strong>international student for tuition-fee purposes</strong>.</li>
        <li>Be a <strong>new student</strong> starting at the university in <strong>September 2027 or January 2028</strong>.</li>
        <li>Hold a <strong>conditional or unconditional offer</strong> for an eligible postgraduate taught course \u2014 applications without a valid offer are not assessed.</li>
        <li>Be entering a <strong>full-time postgraduate degree</strong> delivered at the university\u2019s <strong>Stirling campus</strong>.</li>
        <li>Be <strong>self-funded</strong> \u2014 those receiving external sponsorship or other scholarships are not eligible.</li>
        <li><strong>Not</strong> be on an online degree, an MRes or an MPhil.</li>
        <li><strong>Not</strong> be progressing from an INTO pre-master\u2019s course (INTO progression scholarships may apply instead).</li>
        <li>Be prepared to pay the <strong>\u00a31,000 scholarship deposit</strong> by the deadline on your scholarship offer letter to secure the award.</li>
        <li>Read the <strong>terms and conditions</strong> before submitting.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u00a37,000 tuition-fee waiver</strong> for the first year of an eligible master\u2019s degree.</li>
        <li>Applied directly against tuition \u2014 <strong>no cash payment</strong>.</li>
        <li>Can be combined with Stirling\u2019s <strong>Sports Scholarship</strong> only; if you qualify for another Stirling award, the <strong>highest-value award</strong> is applied instead of stacking.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Completed <strong>University of Stirling admission application</strong> (the course offer comes first).</li>
        <li>Separate <strong>Vice Chancellor\u2019s Scholarship Application 2027-28</strong>.</li>
        <li><strong>Degree certificate and academic transcripts</strong>.</li>
        <li>Valid <strong>passport</strong>.</li>
        <li><strong>CV or r\u00e9sum\u00e9</strong>.</li>
        <li><strong>English-language evidence</strong> where required.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for an <strong>eligible taught master\u2019s</strong> at the University of Stirling and receive a <strong>conditional or unconditional offer</strong>.</li>
        <li>Submit the separate <strong>Vice Chancellor\u2019s Scholarship Application 2027-28</strong> form within the round window for your intake.</li>
        <li>Join the <strong>assessment wait list</strong> \u2014 applications are assessed as funding becomes available, and Stirling aims to notify everyone of the outcome by <strong>15 July</strong>.</li>
        <li>If offered the scholarship, pay the <strong>\u00a31,000 deposit</strong> by the deadline stated in your scholarship offer letter to secure it.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Stirling Vice Chancellor Scholarship fully funded?',
  'No. It is a \u00a37,000 tuition-fee waiver for the first year \u2014 living costs, accommodation, visa fees and travel are not covered. It is a fee reduction, not cash.'),
 ('Do I need a separate application?',
  'Yes \u2014 unlike Stirling\u2019s automatic undergraduate scholarship, this one needs the separate \u201cVice Chancellor\u2019s Scholarship Application 2027-28\u201d form after you hold a course offer. Applications without a valid offer are not assessed.'),
 ('What are the deadlines?',
  'Applications are assessed in rounds: Round 1 runs 1 September\u201315 December 2026 (decisions by 21 December 2026, deposit by 1 February 2027), with further rounds through 30 October 2027 covering the September 2027 and January 2028 intakes. Confirm the live round dates on stir.ac.uk before applying.'),
 ('Can I combine it with other Stirling scholarships?',
  'No. It cannot be combined with any other University of Stirling scholarship or award (the Sports Scholarship is the exception); if you qualify for more than one, the highest-value award is applied.'),
 ('Who is excluded?',
  'Online degrees, MRes and MPhil programmes are not eligible; students progressing from an INTO pre-master\u2019s course are excluded from this scheme; externally sponsored students are not eligible \u2014 you must be self-funded.')]) + '''
      <p class="verify">Verified 24 Oct 2026: stir.ac.uk/scholarships/general/postgraduate/vice-chancellors-postgraduate-international-scholarship/ (official) \u2014 \u00a37,000 tuition-fee waiver, first year of master\u2019s, offer required before assessment, \u00a31,000 deposit to secure, Sept 2027/Jan 2028 intake, international fee status, self-funded only, full-time on-campus, online/MRes/MPhil and INTO pre-master\u2019s excluded, not combinable, separate 2027-28 application form, wait-list assessment, outcomes aimed by 15 July; scholarshipforphd.com/stir-chancellor-scholarship/ + scholarshipunion.com/stirling-vice-chancellor-scholarship-2027/ \u2014 five application rounds with submission windows, decision and deposit dates; scholarshiproar.com/university-of-stirling-scholarships/ \u2014 corroboration (\u00a37,000, separate application, not fully funded). Round-by-round dates come from secondary sources \u2014 confirm on the official page.</p>''',
 dl_long='Round 1 closes December 15, 2026 (further rounds run through October 30, 2027; round dates from published summaries \u2014 confirm on stir.ac.uk)',
 offlinks=[('University of Stirling \u2014 Vice Chancellor\u2019s Postgraduate International Scholarship (official)', 'https://www.stir.ac.uk/scholarships/general/postgraduate/vice-chancellors-postgraduate-international-scholarship/'),
           ('Bright Scholarship \u2014 University of Stirling Vice Chancellor Scholarship 2027', 'https://brightscholarship.com/university-of-stirling-vice-chancellor-scholarship/')],
 related_titles=['glos-merit-2027', 'boustany-cam-2027', 'swinburne-2027', 'gates-cam-2027'])),

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
    json.dump(sizes, open('/tmp/batch44_built.json','w'))

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

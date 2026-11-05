#!/usr/bin/env python3
"""Batch 54 (cron run 54, 26 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. ETH Pioneer Fellowship 2027 - SKIPPED: deadline passed 1 Sep 2026
   (17:00 Swiss time; interviews 29 Oct 2026; spring round has no
   confirmed date). Amounts CHF 120,000/12mo, CHF 180,000/18mo
   (Deep-Tech), CHF 150,000/18mo (Global Development).
2. Ireland Masters Fellows Programme 2027 - SKIPPED: deadline passed
   26 Jul 2026 (Ireland Fellows Programme 2027/28, applications
   29 Jun - 26 Jul 2026). Bright's "programme begins August 2026"
   is wrong - it begins August 2027.
3. CEEPUS Scholarship Program 2027 - VERIFIED: summer-semester
   Network Mobility deadline 31 Dec 2026; Freemover summer
   30 Nov 2026. HUF 170,000/month stipend in Hungary (most
   sources; one Hungarian university page lists HUF 190,000 -
   conflict noted), full tuition exemption, 1-10 months.
4. Stuttgart University Scholarships 2027 - VERIFIED (honest
   composite): no single fully funded award. Real routes are the
   joint international funding windows (31 Jan / 30 Jun / 31 Oct),
   Deutschlandstipendium EUR 300/month, DAAD STIBET EUR 250-500/
   month, Baden-Wuerttemberg-STIPENDIUM EUR 600-1,300/month.
   Next window 31 Oct 2026. "Fully funded" label is wrong.
5. Slovakia Scholarship for Talented Students 2026 - SKIPPED:
   deadline passed 8 Sep 2026 (extended; originally 31 Jul 2026).
   EUR 500/month x 10 months/year, up to EUR 15,000; SAT 1100+.
6. Harvard Academy Scholars Program 2027 - SKIPPED: deadline
   passed 18 Sep 2026 (letters 28 Sep 2026). $80,000/year +
   $6,000 research support, 2 years, 5-6 scholars.
7. GEM Fellowship Program 2027 - VERIFIED: deadline 13 Nov 2026,
   11:59 pm ET (official GEM site + ASU + Penn State). US citizens
   / permanent residents only. MS: full tuition + $4,000/semester
   (up to $16,000 total) + up to 2 paid summer internships. PhD:
   full tuition + $16,000 first year + at least 1 paid internship.
   Associate Fellows: full tuition + at least $8,000/year (Penn
   State) - Bright's $16,000/year is not corroborated.
8. Toyohashi University of Technology MEXT Scholarship 2027 -
   SKIPPED: deadline passed 1 Sep 2026 (TUT post-screening
   submission; embassy track closed earlier).
9. KMU University Scholarships 2026 - SKIPPED: deadline passed
   12 Oct 2026 (Spring 2027 intake, 17:00 Taiwan time).
10. Asia in the World Fellowship Program 2027 - SKIPPED: deadline
    passed 10 Sep 2026 (IIAS, 1 Jul - 10 Sep 2026). EUR 1,250/
    month + EUR 1,200/month housing, 9 months, Category A only.
11. Hanjo Foundation Scholarship 2027 - SKIPPED: duplicate -
    already published as "Honjo International Scholarship 2027 in
    Japan (Fully Funded)" (honjo-international-scholarship-2027-
    japan.html, verified 16 Oct 2026). "Hanjo" is Bright's
    misspelling of Honjo.
12. University of Milan DSU Scholarship 2027 - SKIPPED: deadline
    passed 30 Sep 2026 (2026/27 call, 10 Jul - 30 Sep 2026).
13. Sir Edward Youde Memorial Scholarships 2027 - SKIPPED:
    deadline passed 4 Sep 2026 (official SEYM Fund Council).
    Up to HK$280,000/year (scholarships) / HK$300,000/year
    (fellowships), Hong Kong permanent residents only.
14. World Bank Group Pioneers Internship 2026 - SKIPPED:
    deadline passed 12 Aug 2026 (Fall/Winter cycle; Spring cycle
    closed 17 Feb 2026).
15. University of British Columbia Fellowships 2027 - VERIFIED
    (honest family): flagship is the Four Year Doctoral Fellowship
    (4YF) - CAD 24,000/year + full tuition, up to 4 years,
    automatic consideration on PhD admission (official grad.ubc.ca
    page). 4YF deadline set by each programme; commonly cited
    admission deadlines 15 Nov 2026 (Jan 2027 start), 15 Mar 2027,
    1 Jun 2027. Affiliated Fellowships doctoral deadline passed
    15 Sep 2026. IDF $30,000/year + tuition; ITA up to $3,200/year.
16. Lincoln University Scholarships 2027 - VERIFIED (honest
    family): five international merit awards, all tuition-fee
    credits only (NZ$2,500 Pathway, NZ$3,000 Undergraduate,
    NZ$5,000 Vice-Chancellor's, NZ$10,000 School Leavers,
    NZ$10,000-15,000 Taught Master's Merit), mostly automatic on
    admission (official lincoln.ac.nz pages). Scholarship forms
    due 31 Jan 2027 (Semester 1); study application 1 Dec 2026.
    "Fully funded" label is wrong. Manaaki is a separate NZ
    government award, not a Lincoln award.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 26)
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
 'ceepus-2027': {'mono': 'CE', 'title': 'CEEPUS Scholarship Program 2027 in Hungary (Fully Funded)',
   'href': 'ceepus-scholarship-program-2027-hungary.html',
   'dpill': 'Deadline 31 Dec 2026 · %d days left' % dl_left('2026-12-31'),
   'award': 'A monthly stipend of HUF 170,000 for students in Hungary plus a full tuition-fee exemption, for 1–10 months of exchange mobility. Travel costs are reported as covered by the home country’s National CEEPUS Office; dormitory or housing support is reported by aggregators, not confirmed officially.',
   'elig': 'Students and teachers enrolled or employed at an accredited institution in one of the 16 CEEPUS member countries; students must have completed at least two semesters; no application in your home country and no double funding.',
   'tags': [('Bachelor’s/Master’s/PhD', 'blue'), ('Hungary', 'teal')]},
 'stuttgart-2027': {'mono': 'US', 'title': 'University of Stuttgart Scholarships 2027 in Germany (Funded)',
   'href': 'university-of-stuttgart-scholarships-2027-germany.html',
   'dpill': 'Next window 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': 'No single fully funded award. Real routes: joint international funding windows (31 Jan / 30 Jun / 31 Oct), Deutschlandstipendium €300 a month, DAAD STIBET €250–€500 a month, and Baden-Württemberg-STIPENDIUM €600–€1,300 a month for exchange semesters.',
   'elig': 'Enrolled international students at the University of Stuttgart for most routes; Deutschlandstipendium is open to any nationality once enrolled; Baden-Württemberg-STIPENDIUM is for non-EU exchange students at partner institutions.',
   'tags': [('Bachelor’s/Master’s/PhD', 'blue'), ('Germany', 'teal')]},
 'gem-usa-2027': {'mono': 'GM', 'title': 'GEM Fellowship Program 2027 in USA (Fully Funded)',
   'href': 'gem-fellowship-program-2027-usa.html',
   'dpill': 'Deadline 13 Nov 2026 · %d days left' % dl_left('2026-11-13'),
   'award': 'Full tuition and fees plus a stipend and paid summer internships: Master’s fellows get $4,000 a semester (up to $16,000 in total) and up to two paid internships; PhD fellows get $16,000 in the first academic year and at least one paid internship; Associate Fellows get full tuition plus at least $8,000 a year.',
   'elig': 'US citizens or US permanent residents only, from under-represented groups in science and engineering; Master’s applicants need GPA 2.8/4.0, PhD applicants 3.0/4.0; must apply to at least 3 GEM Member Universities and complete the required summer internships.',
   'tags': [('Master’s & PhD', 'blue'), ('USA', 'teal')]},
 'ubc-2027': {'mono': 'UBC', 'title': 'University of British Columbia Fellowships 2027 in Canada (Funded)',
   'href': 'university-of-british-columbia-fellowships-2027-canada.html',
   'dpill': 'Apply by 15 Nov 2026 for January 2027 start · %d days left' % dl_left('2026-11-15'),
   'award': 'Flagship: the Four Year Doctoral Fellowship — CAD 24,000 a year plus full tuition for up to 4 years, automatically considered on PhD admission. Also the International Doctoral Fellowship ($30,000 a year plus tuition) and the International Tuition Award (up to $3,200 a year).',
   'elig': 'PhD, DMA and MD/PhD students, domestic and international; the 4YF mainly targets students starting their first year of full-time doctoral study; selection is by academic excellence and each graduate programme nominates its strongest candidates.',
   'tags': [('PhD', 'blue'), ('Canada', 'teal')]},
 'lincoln-nz-2027': {'mono': 'LN', 'title': 'Lincoln University Scholarships 2027 in New Zealand (Funded)',
   'href': 'lincoln-university-scholarships-2027-new-zealand.html',
   'dpill': 'Deadline 31 Jan 2027 · %d days left' % dl_left('2027-01-31'),
   'award': 'Five international merit awards, all as tuition-fee credits: NZ$2,500 (Pathway), NZ$3,000 (Undergraduate), NZ$5,000 (Vice-Chancellor’s), NZ$10,000 (School Leavers) and NZ$10,000–NZ$15,000 (Taught Master’s Merit). No living costs, airfare or full funding.',
   'elig': 'New international students who have not previously studied at Lincoln University, meeting the academic and English requirements for their programme and holding no other scholarship; Taught Master’s Merit needs at least a B average in the final year of a bachelor’s degree.',
   'tags': [('Undergraduate & Taught Master’s', 'blue'), ('New Zealand', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. CEEPUS
A.append(dict(
 slug='ceepus-scholarship-program-2027-hungary',
 title='CEEPUS Scholarship Program 2027 in Hungary (Fully Funded)',
 meta='CEEPUS Scholarship Program 2027 in Hungary: a monthly stipend of HUF 170,000 plus a full tuition-fee exemption for 1–10 months of exchange mobility. Summer-semester Network Mobility deadline 31 December 2026 — eligibility, documents, how to apply and FAQs.',
 short='CEEPUS Scholarship Program 2027', kicker='Hungary · Bachelor’s/Master’s/PhD · Fully Funded', mono='CE',
 prov_short='CEEPUS', prov_cat='Exchange Programme · Central Europe',
 h1='CEEPUS Scholarship Program 2027 in Hungary (Fully Funded)',
 sub='CEEPUS — the Central European Exchange Program for University Studies — is an exchange-mobility scheme, not a degree scholarship: it funds students and teachers from 16 Central European and Western Balkan countries to spend 1 to 10 months at a partner university, with a monthly stipend and a full tuition-fee exemption at the host institution. For Hungary the summer-semester Network Mobility deadline is 31 December 2026, and Freemover applications for the summer semester close on 30 November 2026. Two honest warnings before you apply: the stipend figure is reported differently across sources, and “fully funded” is aggregator language — this is a mobility grant, and some costs (notably travel and housing) are only partly covered or reported, not guaranteed.',
 dpill='Deadline 31 Dec 2026 · %d days left' % dl_left('2026-12-31'),
 facts=facts([('Award', 'A monthly stipend — HUF 170,000 a month for students in Hungary, according to most sources; one Hungarian university page lists HUF 190,000 a month for students, so the exact figure should be confirmed on ceepus.info. A full tuition-fee exemption at the host institution. Duration: student mobility 3–5 months, short-term student mobility 1–2 months, teacher mobility from 5 working days; the overall CEEPUS stay can run 1–10 months. Travel costs are reported by aggregators as reimbursed or covered by the National CEEPUS Office of the home country; dormitory placement or a housing allowance is reported by aggregators and is not confirmed on an official page retrieved.'),
              ('Eligible', 'Enrolled or employed at an accredited institution in a CEEPUS member country: Albania, Austria, Bosnia and Herzegovina, Bulgaria, Croatia, the Czech Republic, Hungary, Kosovo, Moldova, Montenegro, North Macedonia, Poland, Romania, Serbia, Slovakia and Slovenia. Students must have completed at least two semesters of studies. You must not apply for a scholarship in your home country (citizenship or residence), must not receive double funding for the same mobility, and citizens of member countries studying in non-member countries are not eligible.'),
              ('How', 'Register on the central CEEPUS application interface at ceepus.info (“My CEEPUS”), use the Mobility Wizard to guide the application, select a host institution through a CEEPUS network or as a Freemover (a Letter of Acceptance from the Hungarian host university is required for Freemovers), upload the required documents and submit.'),
              ('Deadline', 'Network Mobility, summer semester: 31 December 2026. Freemover, summer semester: 30 November 2026. The winter-semester deadlines (Network Mobility 31 August 2026; Freemover from 1 July, rolling) have passed. Deadlines repeat annually on the same dates, so plan ahead.'),
              ('Fine print', 'The “2027” label refers to mobilities in the 2026/27 academic year, not a 2027 degree intake. The stipend figure conflicts across sources (HUF 170,000 vs HUF 190,000 a month for students in Hungary) — neither figure is confirmed on the official CEEPUS page retrieved, so confirm it before budgeting. “Fully funded” is aggregator language: the grant is a tuition exemption plus a monthly stipend for an exchange stay, not a full degree package, and airfare and housing are only reported as covered, not guaranteed. The CEEPUS member list above is consistent across sources.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>CEEPUS</strong> — the <strong>Central European Exchange Program for University Studies</strong> — is a regional exchange scheme run by <strong>16 member countries</strong> in Central Europe and the Western Balkans. It funds <strong>students and teachers</strong> to spend time at a partner university in another member country: <strong>3–5 months</strong> for regular student mobility, <strong>1–2 months</strong> for short-term thesis or research mobility, and from <strong>5 working days</strong> for teachers. Hungary is one of the most popular host countries in the network, and this article covers the Hungarian route.</p>
      <p>The funding is a <strong>monthly stipend</strong> — <strong>HUF 170,000 a month for students in Hungary</strong>, according to most sources — plus a <strong>full tuition-fee exemption</strong> at the host university. One Hungarian university page lists <strong>HUF 190,000 a month for students</strong> instead, so the exact figure should be confirmed on ceepus.info before you budget. Travel and housing are the grey areas: aggregators report that travel is reimbursed or covered by your home country’s National CEEPUS Office and that dormitory placement or a housing allowance is available, but neither is confirmed on an official page retrieved — treat them as reported, not guaranteed. And be clear about what this is: an <strong>exchange-mobility grant</strong>, not a full degree scholarship. You stay enrolled at your home university and earn credits abroad.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be <strong>enrolled or employed at an accredited institution</strong> in a CEEPUS member country: <strong>Albania, Austria, Bosnia and Herzegovina, Bulgaria, Croatia, the Czech Republic, Hungary, Kosovo, Moldova, Montenegro, North Macedonia, Poland, Romania, Serbia, Slovakia and Slovenia</strong>.</li>
        <li>Students must have <strong>completed at least two semesters</strong> of studies.</li>
        <li>Short-term student mobility is for <strong>final-year Bachelor’s/Master’s students working on a thesis</strong> and <strong>PhD students</strong>.</li>
        <li><strong>Do not apply for a scholarship in your home country</strong> (citizenship or residence).</li>
        <li><strong>No double funding</strong> for the same mobility.</li>
        <li><strong>Citizens of member countries studying in non-member countries are not eligible</strong>.</li>
        <li>Freemover applicants (whose home university is not in a CEEPUS network) need a <strong>Letter of Acceptance from the Hungarian host university</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly stipend of HUF 170,000</strong> for students in Hungary (most sources; one Hungarian university page lists HUF 190,000 — confirm on ceepus.info).</li>
        <li><strong>Full tuition-fee exemption</strong> at the host institution.</li>
        <li><strong>Transferable academic credits</strong> towards your degree.</li>
        <li>Support for <strong>thesis research, laboratory work and internships</strong> during the stay.</li>
        <li><strong>Travel costs</strong> reported as reimbursed or covered by the home country’s National CEEPUS Office — reported by aggregators, not confirmed officially.</li>
        <li><strong>Dormitory placement or a housing allowance</strong> reported by aggregators — not confirmed officially.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The completed <strong>online application form</strong> on ceepus.info.</li>
        <li>A <strong>motivation letter</strong> outlining your study or research plans.</li>
        <li>A <strong>Letter of Acceptance</strong> from the Hungarian host university (Freemover applicants only).</li>
        <li><strong>Academic transcripts</strong> (for students).</li>
        <li><strong>Proof of enrolment or employment</strong> at your home institution.</li>
        <li>A <strong>CV</strong> (recommended).</li>
        <li>A <strong>language certificate</strong> if applicable.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the official website, <strong>ceepus.info</strong>, and <strong>register / log in</strong> under “My CEEPUS”.</li>
        <li>Use the <strong>Mobility Wizard</strong> to guide your application.</li>
        <li>Select a <strong>host institution</strong> — through a CEEPUS network, or as a <strong>Freemover</strong> with a Letter of Acceptance.</li>
        <li>Upload the required <strong>documents</strong> (motivation letter, transcripts, proof of enrolment/employment, CV, language certificate if applicable).</li>
        <li><strong>Submit</strong> before the deadline for your mobility type and semester.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the CEEPUS Scholarship 2027 in Hungary?',
  'For the summer semester: Network Mobility closes 31 December 2026 and Freemover closes 30 November 2026. The winter-semester deadlines (31 August 2026 for Network Mobility) have passed. Deadlines repeat annually on the same dates.'),
 ('How much is the CEEPUS stipend in Hungary?',
  'HUF 170,000 a month for students, according to most sources — but one Hungarian university page lists HUF 190,000 a month for students. The exact figure should be confirmed on ceepus.info before you budget.'),
 ('Is CEEPUS fully funded?',
  'In the aggregator sense only. It pays a monthly stipend and exempts you from tuition at the host university for an exchange stay of 1–10 months. It is a mobility grant, not a full degree scholarship, and travel and housing coverage is reported rather than guaranteed.'),
 ('Who can apply for CEEPUS?',
  'Students and teachers enrolled or employed at an accredited institution in one of the 16 CEEPUS member countries, who have completed at least two semesters (students). You cannot apply in your home country, cannot receive double funding for the same mobility, and citizens of member countries studying in non-member countries are not eligible.'),
 ('What is a Freemover application?',
  'An application for students whose home university is not part of a CEEPUS network. Freemovers need a Letter of Acceptance from the Hungarian host university and apply through the same ceepus.info portal.'),
 ('Which countries are CEEPUS members?',
  'Albania, Austria, Bosnia and Herzegovina, Bulgaria, Croatia, the Czech Republic, Hungary, Kosovo, Moldova, Montenegro, North Macedonia, Poland, Romania, Serbia, Slovakia and Slovenia.')]) + '''
      <p class="verify">Verified 26 Oct 2026: ceepus.info (official central application interface, via FellowshipGuide / Elvoyager / ScholarshipUnion application guides) — Network Mobility summer semester 31 December 2026, winter semester 31 August 2026, Freemover summer semester 30 November 2026, Freemover winter from 1 July (rolling); ppke.hu (Pázmány Péter Catholic University, official Hungarian host page) — 2026/27 freemover deadlines and scholarship amounts (students HUF 190,000/month); FellowshipGuide, Elvoyager, OpportunitiesPedia, ScholarshipUnion — corroboration, including HUF 170,000/month for students in Hungary, full tuition exemption, 16 member countries, eligibility (two semesters completed, no home-country application, no double funding), mobility types and documents. CONFLICT: the monthly stipend in Hungary is HUF 170,000 (most aggregators) vs HUF 190,000 (PPKE page) — neither is confirmed on the official CEEPUS page retrieved, so the article states the majority figure and flags the conflict. NOT CONFIRMED officially: dormitory placement / housing allowance and travel reimbursement (aggregator-reported only). The "2027" label refers to 2026/27 academic-year mobilities.</p>''',
 dl_long='31 December 2026 (Network Mobility, Summer Semester) — Freemover Summer Semester: 30 November 2026',
 offlinks=[('CEEPUS — Official website', 'https://www.ceepus.info/'),
           ('Bright Scholarship — CEEPUS Scholarship Program 2027', 'https://brightscholarship.com/ceepus-scholarship-program-2027-in-hungary/')],
 related_titles=['ceu-hungary', 'anhalt-stibet-2027', 'daad-reinvitation-2027', 'hanns-seidel'])),

# ---------------------------------------------------------------- 2. University of Stuttgart
A.append(dict(
 slug='university-of-stuttgart-scholarships-2027-germany',
 title='University of Stuttgart Scholarships 2027 in Germany (Funded)',
 meta='University of Stuttgart Scholarships 2027: there is no single fully funded award — the real routes are the joint international funding windows (next: 31 October 2026), the Deutschlandstipendium (€300 a month), DAAD STIBET (€250–€500 a month) and the Baden-Württemberg-STIPENDIUM (€600–€1,300 a month). Eligibility, documents, how to apply and FAQs.',
 short='University of Stuttgart Scholarships 2027', kicker='Germany · Bachelor’s/Master’s/PhD · Funded', mono='US',
 prov_short='University of Stuttgart', prov_cat='University · Germany',
 h1='University of Stuttgart Scholarships 2027 in Germany (Funded)',
 sub='Read this first, because the listings get it wrong: the University of Stuttgart does not have one fully funded scholarship with one annual deadline for all international students. What it has is a funding system — joint international funding windows that close on 31 January, 30 June and 31 October, the Deutschlandstipendium, DAAD STIBET grants for enrolled students, and the Baden-Württemberg-STIPENDIUM for exchange semesters — each with its own amount, rules and deadline. The next joint window closes on 31 October 2026. Most of these routes are for students who are already enrolled at Stuttgart, so if you are applying from abroad, your best funding is usually DAAD or a home-country scholarship applied for before you arrive — and the university’s own International Office says it plainly: “Do not rely on receiving an aid or scholarship!”',
 dpill='Next window 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'No single fully funded award. The real routes, all partial: the Deutschlandstipendium — €300 a month for 12 months for enrolled students with top-quartile academics. DAAD STIBET — €250–€500 a month (sources differ: €250–€400 for final-stage students, €250–€300 for commitment, one source says €300–€500) for international students in their final Master’s phase or near graduation. The Baden-Württemberg-STIPENDIUM — €600–€1,300 a month for non-EU students on exchange semesters at partner institutions. German foundation scholarships (StipendiumPlus, 13 foundations) have their own amounts and deadlines and usually expect good German.'),
              ('Eligible', 'Most routes are for students already enrolled at the University of Stuttgart, usually from the second or third semester. Deutschlandstipendium: enrolled students of any nationality with top-quartile academics (need optional). STIBET: international students in their final phase — Bachelor’s from the 6th semester, Master’s from the 4th semester, PhD in the final 12 months — or students active in the international community. Baden-Württemberg-STIPENDIUM: non-EU students for exchange semesters at partner institutions, applied for via the International Office. Foundation scholarships: international Master’s and PhD students, usually with good German.'),
              ('How', 'For the joint international funding windows, contact the International Office first and submit the combined application by the window deadline. For the Deutschlandstipendium, apply in the annual window that opens in mid-January 2027 for funding from April 2027. For STIBET, watch the International Office’s internal calls each semester. For the Baden-Württemberg-STIPENDIUM, apply via the International Office, typically by January for the following academic year. For foundation scholarships, apply directly to the individual foundation (StipendiumPlus portal).'),
              ('Deadline', 'Next joint international funding window: 31 October 2026 (only if funds remain). The other annual windows are 31 January and 30 June. The Deutschlandstipendium window opens in mid-January 2027. STIBET calls run each semester through the International Office. Foundation deadlines vary by foundation.'),
              ('Fine print', 'The “fully funded” label on aggregator pages is wrong — none of these routes covers full tuition plus living costs. Non-EU students pay €1,500 a semester in tuition in Baden-Württemberg, and DAAD scholarships do not cover that fee. One aggregator lists the Deutschlandstipendium as opening in “October 2027 after enrolment” — that conflicts with the mid-January 2027 window reported by other sources and is not used. The STIBET amounts differ across sources (€250–€400 vs €300–€500), so the article gives the range. Most funding here is for students already enrolled — new applicants from abroad should apply for DAAD or home-country funding first, before arrival.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of Stuttgart</strong> is one of Germany’s leading technical universities, and its funding for international students is a <strong>system of separate routes</strong>, not a single scholarship. The university’s own financing page runs <strong>joint international funding windows</strong> that close on <strong>31 January, 30 June and 31 October</strong> each year, and the <strong>International Office</strong> administers the main grants. On top of that sit the <strong>Deutschlandstipendium</strong> (€300 a month), <strong>DAAD STIBET</strong> grants for enrolled international students, the <strong>Baden-Württemberg-STIPENDIUM</strong> for exchange semesters, and Germany’s <strong>foundation scholarships</strong> (StipendiumPlus).</p>
      <p>Two things matter most. First, the money is <strong>partial</strong>: €250–€500 a month from STIBET, €300 a month from the Deutschlandstipendium, €600–€1,300 a month from the Baden-Württemberg-STIPENDIUM — helpful, but none of it is a full ride, and non-EU students still owe <strong>€1,500 a semester in tuition</strong> in Baden-Württemberg, which DAAD scholarships do not cover. Second, most of these routes are for <strong>students already enrolled</strong> at Stuttgart, usually from the second or third semester. If you are applying from abroad, the realistic path is to secure <strong>DAAD or home-country funding first</strong>, then use Stuttgart’s grants as a top-up once you are there.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Deutschlandstipendium:</strong> enrolled students of any nationality with <strong>top-quartile academics</strong>; financial need is optional.</li>
        <li><strong>DAAD STIBET Final Stage:</strong> international students near graduation — <strong>Bachelor’s from the 6th semester, Master’s from the 4th semester, PhD in the final 12 months</strong>.</li>
        <li><strong>DAAD STIBET Commitment:</strong> international students <strong>active in the international community</strong>.</li>
        <li><strong>DAAD STIBET Equal Opportunities:</strong> students facing extra challenges such as <strong>disability, illness, parenthood or refugee status</strong>.</li>
        <li><strong>Baden-Württemberg-STIPENDIUM:</strong> <strong>non-EU students</strong> for <strong>exchange semesters at partner institutions</strong>.</li>
        <li><strong>Foundation scholarships (StipendiumPlus):</strong> international <strong>Master’s and PhD</strong> students, based on grades, social commitment and personality — <strong>good German is usually expected</strong>.</li>
        <li>Most routes require you to be <strong>already enrolled at the University of Stuttgart</strong>, usually from the second or third semester.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Deutschlandstipendium:</strong> <strong>€300 a month for 12 months</strong>.</li>
        <li><strong>DAAD STIBET:</strong> <strong>€250–€500 a month</strong> (sources differ: €250–€400 for final-stage students, €250–€300 for commitment awards).</li>
        <li><strong>Baden-Württemberg-STIPENDIUM:</strong> <strong>€600–€1,300 a month</strong> for exchange semesters at partner institutions.</li>
        <li><strong>Foundation scholarships:</strong> amounts vary by foundation (StipendiumPlus).</li>
        <li><strong>Emergency help:</strong> the <strong>Beihilfe</strong> and the <strong>Bürkert emergency fund</strong> give short-term help in a financial emergency.</li>
        <li>Note that none of these routes is <strong>fully funded</strong>, and <strong>non-EU tuition of €1,500 a semester is not covered by DAAD scholarships</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An updated <strong>CV / résumé</strong>.</li>
        <li><strong>Academic transcripts</strong> and degree certificates.</li>
        <li>A <strong>motivation letter</strong> (one aggregator caps it at 2 pages).</li>
        <li>A valid <strong>passport</strong>.</li>
        <li><strong>Recommendation letter(s)</strong> where the route requires them.</li>
        <li>Note that no single official document list exists for “Stuttgart scholarships” as a whole — each route sets its own list, so <strong>check the International Office or the foundation’s page</strong> for the route you choose.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Contact the International Office first</strong> — it runs the joint funding windows and the STIBET calls, and it can tell you which routes you qualify for.</li>
        <li>For the <strong>joint international funding windows</strong>, submit the combined application by <strong>31 October 2026</strong> (next window), <strong>31 January</strong> or <strong>30 June</strong>.</li>
        <li>For the <strong>Deutschlandstipendium</strong>, apply in the annual window opening in <strong>mid-January 2027</strong> for funding from <strong>April 2027</strong>.</li>
        <li>For <strong>STIBET</strong>, watch the International Office’s <strong>internal calls each semester</strong>.</li>
        <li>For the <strong>Baden-Württemberg-STIPENDIUM</strong>, apply via the International Office, typically by <strong>January</strong> for the following academic year.</li>
        <li>For <strong>foundation scholarships</strong>, apply <strong>directly to the individual foundation</strong> via the StipendiumPlus portal.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the University of Stuttgart scholarship fully funded?',
  'No. There is no single fully funded scholarship at the University of Stuttgart. The real routes are partial: Deutschlandstipendium €300 a month, DAAD STIBET €250–€500 a month, Baden-Württemberg-STIPENDIUM €600–€1,300 a month, plus foundation scholarships with their own amounts.'),
 ('What is the deadline for University of Stuttgart scholarships 2027?',
  'The joint international funding windows close on 31 January, 30 June and 31 October — the next one is 31 October 2026, if funds remain. The Deutschlandstipendium window opens in mid-January 2027. STIBET calls run each semester, and foundation deadlines vary.'),
 ('Can I apply before I am enrolled at Stuttgart?',
  'Most routes are for students already enrolled, usually from the second or third semester. If you are applying from abroad, apply for DAAD or a home-country scholarship first, before you arrive.'),
 ('Does the scholarship cover the €1,500 tuition fee for non-EU students?',
  'No. Non-EU students pay €1,500 a semester in tuition in Baden-Württemberg, and DAAD scholarships do not cover that fee.'),
 ('What is the Deutschlandstipendium worth?',
  '€300 a month for 12 months, for enrolled students of any nationality with top-quartile academics. The annual application window opens in mid-January 2027 for funding from April 2027.'),
 ('What does the International Office advise?',
  '“Do not rely on receiving an aid or scholarship!” — the university’s own advice to international students. Treat Stuttgart’s grants as a top-up, not as your funding plan.')]) + '''
      <p class="verify">Verified 26 Oct 2026: uni-stuttgart.de/en/study/service-and-info/scholarships (official University of Stuttgart financing and scholarships portal, via CollegeDunia source line and ScholarFahad) — joint international funding windows 31 January, 30 June and 31 October; Deutschlandstipendium €300/month; DAAD STIBET for enrolled international students; Baden-Württemberg-STIPENDIUM €600–€1,300/month for non-EU exchange semesters; International Office advice "Do not rely on receiving an aid or scholarship!"; ScholarFahad (University of Stuttgart Scholarships 2027 guide) — STIBET €250–€400/month final stage, €250–€300 commitment, Deutschlandstipendium window mid-January 2027 for April 2027 funding, non-EU tuition €1,500/semester not covered by DAAD; CollegeDunia — Deutschlandstipendium €300/month, STIBET €300–€500/month, BW-STIPENDIUM €600–€1,300/month; TechMLA / DAADScholarship.org — 31 October 2026 deadline. CORRECTION: the "Fully Funded" label on aggregator pages is wrong — no single fully funded award exists; this article covers the real funding system instead. NOT USED: CollegeDunia's "Deutschlandstipendium opens October 2027 after enrolment" (conflicts with the mid-January 2027 window); the STIBET amounts differ across sources (€250–€400 vs €300–€500), so the article gives the range. No single official document list exists for the system as a whole — each route sets its own list.</p>''',
 dl_long='31 October 2026 (next joint international funding window; also 31 January and 30 June)',
 offlinks=[('University of Stuttgart — Scholarships & Financing (official)', 'https://www.uni-stuttgart.de/en/study/service-and-info/scholarships'),
           ('Bright Scholarship — Stuttgart University Scholarships 2027', 'https://brightscholarship.com/stuttgart-university-scholarships-2027/')],
 related_titles=['anhalt-stibet-2027', 'daad-reinvitation-2027', 'hanns-seidel', 'wiko-2027'])),

# ---------------------------------------------------------------- 3. GEM Fellowship
A.append(dict(
 slug='gem-fellowship-program-2027-usa',
 title='GEM Fellowship Program 2027 in USA (Fully Funded)',
 meta='GEM Fellowship Program 2027: full tuition and fees plus a stipend and paid summer internships for Master’s and PhD study in engineering and science in the USA — but only for US citizens and permanent residents. Deadline 13 November 2026 — eligibility, documents, how to apply and FAQs.',
 short='GEM Fellowship Program 2027', kicker='USA · Master’s/PhD · Fully Funded', mono='GM',
 prov_short='National GEM Consortium', prov_cat='Consortium · United States',
 h1='GEM Fellowship Program 2027 in USA (Fully Funded)',
 sub='The GEM Fellowship is one of the most distinctive routes into a Master’s or PhD in engineering or science in the United States: full tuition and fees, a stipend, and paid summer internships with a major employer — plus a formal pipeline from graduate school into the STEM workforce. But it comes with two hard limits that catch applicants off guard. First, it is only for US citizens and US permanent residents; international students without that status cannot apply. Second, the internship is contractual, not optional — you agree to intern with a GEM employer, and refusing an internship offer can cancel the fellowship. And there are two applications, not one: the fellowship through GEM’s eGEM portal by 13 November 2026, and admission to at least three GEM Member Universities by 15 January 2027 or the department deadline, whichever is earlier.',
 dpill='Deadline 13 Nov 2026 · %d days left' % dl_left('2026-11-13'),
 facts=facts([('Award', 'Full tuition and fees provided by a GEM Member University, plus a stipend and paid summer internships. Master’s (MS) fellows: a $4,000 living stipend per full-time semester for up to 4 semesters ($16,000 in total) plus up to two paid summer internships with a GEM Employer Member. PhD fellows: a $16,000 stipend in the first academic year, a living stipend from the member university up to the 5th year of the PhD, and at least one paid summer internship. Associate Fellows: full tuition and fees plus at least $8,000 a year from the member university (Penn State page). The minimum GEM stipend is $8,000 a year (Scholarships.com, citing GEM).'),
              ('Eligible', 'US citizens or US permanent residents at the time of application — international students without that status are not eligible. Targeted at under-represented groups in science and engineering: American Indian / Native, African American / Black, and Hispanic / Latino. Master’s: a senior, or a graduate of an accredited engineering or computer science programme, minimum GPA 2.8/4.0, and a contractual agreement to intern for two summers with a sponsoring GEM Employer. PhD: a senior, Master’s student or graduate of an accredited engineering or applied science programme, minimum GPA 3.0/4.0, and a contractual agreement to intern with a GEM Employer the summer immediately after sponsorship. GRE is strongly encouraged (not required by GEM, but individual programmes may require it). Must apply to at least 3 GEM Member Universities. GEM does not fund online programmes.'),
              ('How', 'Register on the eGEM online application system at gemfellowship.org, complete the application (resume, unofficial transcripts, statement of purpose, three recommenders, GRE test dates/scores if taken), and submit by 13 November 2026. Then apply directly to at least 3 GEM Member Universities for admission to a STEM graduate programme by 15 January 2027 or the department’s own deadline, whichever is earlier. Employer interviews and sponsorship selections run December 2026 – June 2027.'),
              ('Deadline', '13 November 2026, 11:59 pm Eastern Time — the second Friday in November each year. The application cycle opened 1 July 2026; the early-consideration period ended 1 October 2026. Graduate university applications are due by 15 January 2027 or the university’s own STEM deadline if earlier.'),
              ('Fine print', 'Bright Scholarship’s $16,000 a year figure for Associate Fellows is not corroborated — the Penn State GEM page says at least $8,000 a year for Associate Fellows, and ASU’s official GEM page gives $4,000 a semester for MS fellows and $16,000 in the first academic year for PhD fellows, which is what this article uses. The internship is contractual: fellows must accept the GEM summer internship, and failure to accept an offer can result in cancellation of the fellowship. This is not the Erasmus Mundus GEM scholarship — that is a different, European programme. The “fully funded” label applies to the fellowship package (tuition + stipend + internships), but the exact stipend depends on the fellowship type.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>GEM Fellowship</strong>, run by the <strong>National GEM Consortium</strong>, is a graduate fellowship for <strong>Master’s and PhD study in engineering, computer science and applied science</strong> in the United States. It is designed to increase the number of <strong>under-represented minority students</strong> — American Indian / Native, African American / Black, and Hispanic / Latino students — who earn advanced STEM degrees, and it does that by combining <strong>graduate funding with paid industry experience</strong>: full tuition and fees, a stipend, and <strong>paid summer internships</strong> with a GEM Employer Member.</p>
      <p>The money is real, but the structure is what makes GEM different from an ordinary scholarship. You are not just funded; you are <strong>contractually committed</strong> to intern with a GEM employer — two summers for Master’s fellows, the summer immediately after sponsorship for PhD fellows — and <strong>refusing an internship offer can cancel the fellowship</strong>. You also apply twice: once to GEM through its <strong>eGEM portal</strong>, and separately to <strong>at least three GEM Member Universities</strong> for admission. And the eligibility line is absolute: <strong>US citizens and US permanent residents only</strong>. If you do not hold that status, GEM is not available to you, however strong your record is.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>US citizen or US permanent resident</strong> at the time of application.</li>
        <li>Be a member of an <strong>under-represented group</strong> in science and engineering: <strong>American Indian / Native, African American / Black, or Hispanic / Latino</strong>.</li>
        <li>For a <strong>Master’s</strong>: be a <strong>senior, or a graduate of an accredited engineering or computer science programme</strong>, with a minimum cumulative GPA of <strong>2.8/4.0</strong>.</li>
        <li>For a <strong>PhD</strong>: be a <strong>senior, Master’s student, or graduate of an accredited engineering or applied science programme</strong>, with a minimum cumulative GPA of <strong>3.0/4.0</strong>.</li>
        <li><strong>Contractually agree to intern</strong> with a sponsoring GEM Employer — <strong>two summers</strong> for Master’s fellows, the <strong>summer immediately after sponsorship</strong> for PhD fellows.</li>
        <li><strong>Apply to at least 3 GEM Member Universities</strong> for admission to a STEM graduate programme.</li>
        <li>The <strong>GRE is strongly encouraged</strong> (GEM does not require it, but individual graduate programmes may).</li>
        <li><strong>GEM does not fund online programmes</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and fees</strong> provided by a GEM Member University.</li>
        <li><strong>Master’s fellows:</strong> a <strong>$4,000 living stipend per full-time semester</strong> for up to 4 semesters (<strong>$16,000 in total</strong>), plus <strong>up to two paid summer internships</strong>.</li>
        <li><strong>PhD fellows:</strong> a <strong>$16,000 stipend in the first academic year</strong>, a living stipend from the member university <strong>up to the 5th year</strong> of the PhD, and <strong>at least one paid summer internship</strong>.</li>
        <li><strong>Associate Fellows:</strong> full tuition and fees plus <strong>at least $8,000 a year</strong> from the member university.</li>
        <li><strong>Paid summer internships</strong> with GEM Employer Members, plus access to the <strong>GEM alumni and industry network</strong> and weekly GEM Fellowship meetings.</li>
        <li>Note that the <strong>minimum GEM stipend is $8,000 a year</strong>, and the exact stipend depends on the fellowship type.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A current <strong>resume</strong>.</li>
        <li><strong>Unofficial college transcripts</strong>.</li>
        <li>A <strong>statement of purpose</strong> of at least one page.</li>
        <li>Contact information for <strong>three recommenders</strong> — at least two recommendations must be submitted through the application system by the deadline.</li>
        <li><strong>GRE test dates and/or scores</strong> if taken (self-reported; the official score report is not required by the deadline).</li>
        <li>Personal, educational, employment and research information for the eGEM questionnaire.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Register on the eGEM portal</strong> at gemfellowship.org and begin the application.</li>
        <li>Complete the application: <strong>resume, unofficial transcripts, statement of purpose, three recommenders, GRE information</strong>.</li>
        <li>Submit the GEM application by <strong>13 November 2026, 11:59 pm Eastern Time</strong>.</li>
        <li>Apply directly to <strong>at least 3 GEM Member Universities</strong> for admission to a STEM graduate programme, by <strong>15 January 2027</strong> or the department’s own deadline, whichever is earlier.</li>
        <li>Take part in <strong>employer interviews and sponsorship selections</strong> (December 2026 – June 2027) and confirm your university admission and fellowship agreement by March–June 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the GEM Fellowship 2027?',
  '13 November 2026, 11:59 pm Eastern Time — the second Friday in November each year. The cycle opened 1 July 2026 and the early-consideration period ended 1 October 2026.'),
 ('Can international students apply for the GEM Fellowship?',
  'No. Only US citizens and US permanent residents are eligible. International students who do not hold either status cannot apply.'),
 ('How much does the GEM Fellowship pay?',
  'Full tuition and fees plus a stipend and paid internships. Master’s fellows get $4,000 a semester (up to $16,000 in total); PhD fellows get $16,000 in the first academic year plus a university living stipend through the 5th year; Associate Fellows get at least $8,000 a year. The minimum GEM stipend is $8,000 a year.'),
 ('Is the internship mandatory?',
  'Yes, contractually. Master’s fellows agree to intern for two summers with a sponsoring GEM Employer; PhD fellows agree to intern the summer immediately after sponsorship. Failure to accept a GEM summer internship offer can result in cancellation of the fellowship.'),
 ('How many universities must I apply to?',
  'At least three GEM Member Universities, directly to the relevant STEM department, by 15 January 2027 or the department’s own deadline, whichever is earlier. The requirement is waived only if you are already matriculating at a GEM Member University that confirms in writing it will support you as a GEM Fellow.'),
 ('Is the GRE required?',
  'Not by GEM — but GEM strongly encourages taking it, and individual graduate programmes may require or consider it. Check the policies of every university and department on your list.')]) + '''
      <p class="verify">Verified 26 Oct 2026: gemfellowship.org/gem-fellowship-program/ and gemfellowship.org/application-process/ (official National GEM Consortium pages, opened and read) — eGEM portal, at least 3 GEM Member Universities required, 15 January 2027 university deadline, GEM does not fund online programmes, GRE questions required in the application; onsa.asu.edu (Arizona State University, official GEM page) — MS fellows $4,000/semester up to 4 semesters, PhD fellows $16,000 first academic year plus university living stipend to 5th year, at least one paid summer internship, full tuition and fees, US citizens / permanent residents only; engr.psu.edu (Penn State Engineering, official) — Associate Fellows full tuition and fees plus at least $8,000 stipend per year; Bright Scholarship, ScholarPositions, ScholarshipsAds, Scholarshub — corroboration, including the 13 November 2026, 11:59 pm ET deadline and the 1 July 2026 opening. CORRECTION: Bright's "$16,000 per year" for Associate Fellows is not corroborated — Penn State says at least $8,000 a year, which is used here. The internship is contractual and refusing an offer can cancel the fellowship. This is not the Erasmus Mundus GEM scholarship (a different, European programme).</p>''',
 dl_long='13 November 2026, 11:59 pm Eastern Time',
 offlinks=[('National GEM Consortium — GEM Fellowship Program (official)', 'https://www.gemfellowship.org/gem-fellowship-program/'),
           ('Bright Scholarship — GEM Fellowship Program 2027', 'https://brightscholarship.com/gem-fellowship-program-2027-in-usa/')],
 related_titles=['dayton-merit', 'alabama-2027', 'au-egls-2027', 'jefferson-2027'])),

# ---------------------------------------------------------------- 4. University of British Columbia
A.append(dict(
 slug='university-of-british-columbia-fellowships-2027-canada',
 title='University of British Columbia Fellowships 2027 in Canada (Funded)',
 meta='University of British Columbia Fellowships 2027: the flagship is the Four Year Doctoral Fellowship — CAD 24,000 a year plus full tuition for up to 4 years, automatically considered on PhD admission. Apply by 15 November 2026 for a January 2027 start — eligibility, how to apply and FAQs.',
 short='University of British Columbia Fellowships 2027', kicker='Canada · PhD · Funded', mono='UBC',
 prov_short='University of British Columbia', prov_cat='University · Canada',
 h1='University of British Columbia Fellowships 2027 in Canada (Funded)',
 sub='“UBC Fellowships” is not one scholarship — it is a family of doctoral funding at the University of British Columbia, and the flagship is the Four Year Doctoral Fellowship (4YF): CAD 24,000 a year plus full tuition for up to four years, for domestic and international PhD students alike. The part that surprises applicants is that there is no separate fellowship application: every admitted PhD, DMA or MD/PhD applicant is automatically considered, and each graduate programme nominates its strongest candidates. So the real deadline is the admission deadline — commonly cited as 15 November 2026 for a January 2027 start, 15 March 2027 for May and 1 June 2027 for September — while the official 4YF deadline is set by each graduate programme. Alongside the 4YF sit the International Doctoral Fellowship, the International Tuition Award and the Affiliated Fellowships, each with its own rules — and one of them, the Affiliated Fellowships doctoral competition, already closed on 15 September 2026.',
 dpill='Apply by 15 Nov 2026 for January 2027 start · %d days left' % dl_left('2026-11-15'),
 facts=facts([('Award', 'Four Year Doctoral Fellowship (4YF): $24,000 in stipend funding plus tuition per year, for up to four years of doctoral study (effective September 2026 — up from $18,200). The tuition is a tuition award applied against charges, not a waiver, and the combined total of external scholarship funding and the 4YF tuition award may not exceed $35,000. International Doctoral Fellowship (IDF): $30,000 stipend plus tuition for 4 years, plus a minimum $18,000 package in year 5. International Tuition Award (ITA): up to $3,200 a year toward international tuition fees. Affiliated Fellowships: approximately 50 awards a year, $175–$40,000 (most around $16,000), including the Killam Doctoral Scholarships for top candidates. Schmidt Science Fellowship (postdoctoral, UBC-nominated): $110,000 a year for at least one year.'),
              ('Eligible', 'PhD, DMA and MD/PhD students, domestic and international — there is no nationality restriction for the 4YF. The 4YF is mainly aimed at students beginning their first year of full-time doctoral study, although continuing students can sometimes receive an award. Selection is by academic excellence; each UBC graduate programme receives a limited allocation and nominates its strongest incoming and continuing doctoral students, with incoming students generally receiving priority. The Schmidt Science Fellowship is for PhD graduates in computer science, engineering or the natural sciences, nominated by UBC.'),
              ('How', 'Apply for admission to the relevant UBC graduate programme — there is normally no separate 4YF application. All admitted PhD, DMA and MD/PhD applicants are automatically considered for 4YF funding, and the graduate programme reviews its candidates and nominates selected students. For the Schmidt Science Fellowship, UBC nominates PhD graduates; you cannot apply directly to Schmidt.'),
              ('Deadline', 'The 4YF deadline is set by each UBC graduate programme. Commonly cited admission deadlines by start term: 15 November 2026 (January 2027 start), 15 March 2027 (May 2027 start), 1 June 2027 (September 2027 start). Affiliated Fellowships (Master’s): 1 December 2026 before 5:00 pm PT (official UBC award list). The Affiliated Fellowships doctoral competition closed 15 September 2026. The Schmidt Science Fellowship deadline is expected in April 2027, subject to official announcement.'),
              ('Fine print', '“UBC Fellowships 2027” is not a single scheme with one deadline — it is a family of awards, and this article leads with the 4YF because it is the flagship doctoral award with an open admission route. The Affiliated Fellowships doctoral deadline (15 September 2026) has already passed, so do not plan around it for 2027/28. The $110,000 Schmidt figure is a postdoctoral fellowship, not a doctoral award. The 4YF tuition component is an award applied against tuition charges, not a waiver, and it is reduced if your external funding plus the tuition award would exceed $35,000. The widely quoted “January 2027 start deadline 15 November 2026” comes from aggregators — the official 4YF page says the deadline is set by each graduate programme, so confirm your programme’s date.')]),
 body='''
      <h2 id="about">About the fellowships</h2>
      <p>The <strong>University of British Columbia (UBC)</strong> funds its doctoral students through a <strong>family of fellowships</strong>, not a single award, and the flagship is the <strong>Four Year Doctoral Fellowship (4YF)</strong>. From September 2026 it provides <strong>$24,000 in stipend funding plus tuition per year, for up to four years</strong> — up from $18,200 — to outstanding domestic and international doctoral students. It is UBC’s base-level funding: stable, four-year support that lets the university attract strong PhD candidates in every discipline.</p>
      <p>The unusual part is the application: <strong>there is normally no separate 4YF application</strong>. You apply for <strong>admission to a UBC graduate programme</strong>, and every admitted <strong>PhD, DMA or MD/PhD applicant is automatically considered</strong>. Each programme gets a limited allocation and nominates its strongest candidates, with incoming students generally receiving priority — so the admission application is doing double duty, and the real deadline is your programme’s admission deadline. Around the 4YF sit the <strong>International Doctoral Fellowship</strong> ($30,000 a year plus tuition), the <strong>International Tuition Award</strong> (up to $3,200 a year), the <strong>Affiliated Fellowships</strong> (about 50 awards a year, most around $16,000, including the Killam Doctoral Scholarships) and the postdoctoral <strong>Schmidt Science Fellowship</strong> ($110,000 a year, UBC-nominated).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>PhD, DMA or MD/PhD student</strong> at UBC — domestic or international; there is <strong>no nationality restriction</strong> for the 4YF.</li>
        <li>The 4YF is mainly aimed at students beginning their <strong>first year of full-time doctoral study</strong>, although <strong>continuing students can sometimes receive an award</strong>.</li>
        <li>Selection is by <strong>academic excellence</strong> — academic record, research preparation, proposed project, references and fit with the graduate programme.</li>
        <li>Each graduate programme receives a <strong>limited allocation</strong> and nominates its strongest candidates; <strong>incoming students generally receive priority</strong>.</li>
        <li>For the <strong>Schmidt Science Fellowship</strong>: hold or be nearing completion of a <strong>PhD in computer science, engineering or the natural sciences</strong>, and be <strong>nominated by UBC</strong>.</li>
        <li>For the <strong>Affiliated Fellowships</strong>: meet the eligibility requirements of the <strong>Canada Graduate Scholarships – Doctoral (CGS-D) competition</strong>; priority goes to candidates without significant scholarship funding (at least $16,000) for 2027/28.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Four Year Doctoral Fellowship:</strong> <strong>$24,000 a year in stipend plus tuition</strong>, for up to <strong>4 years</strong>.</li>
        <li><strong>International Doctoral Fellowship:</strong> <strong>$30,000 stipend plus tuition for 4 years</strong>, plus a <strong>minimum $18,000 package in year 5</strong>.</li>
        <li><strong>International Tuition Award:</strong> up to <strong>$3,200 a year</strong> toward international tuition fees.</li>
        <li><strong>Affiliated Fellowships:</strong> about <strong>50 awards a year</strong>, <strong>$175–$40,000</strong> (most around $16,000), including the <strong>Killam Doctoral Scholarships</strong> for top candidates.</li>
        <li><strong>Schmidt Science Fellowship (postdoctoral):</strong> <strong>$110,000 a year</strong> for at least one year, plus residential meetings and leadership training.</li>
        <li>Note that the 4YF tuition component is a <strong>tuition award applied against charges, not a waiver</strong>, and it is reduced if external funding plus the tuition award would exceed <strong>$35,000</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>UBC graduate programme admission application</strong> — this is the fellowship application too, for the 4YF.</li>
        <li><strong>Academic transcripts</strong> and degree certificates.</li>
        <li><strong>References</strong> and a <strong>research proposal</strong>, as required by your programme.</li>
        <li>Note that there is <strong>normally no separate 4YF form</strong> — the programme’s admission documents are what the fellowship decision is made on.</li>
        <li>For the <strong>Schmidt Science Fellowship</strong>, UBC nominates candidates — check with your department about the internal nomination process.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>UBC graduate programme</strong> and check its <strong>admission requirements and deadline</strong> — the 4YF deadline is set by each programme.</li>
        <li>Apply for <strong>admission to the programme</strong> (commonly cited deadlines: <strong>15 November 2026</strong> for a January 2027 start, <strong>15 March 2027</strong> for May 2027, <strong>1 June 2027</strong> for September 2027).</li>
        <li>You are <strong>automatically considered for 4YF funding</strong> — no separate fellowship form is normally needed.</li>
        <li>Your programme <strong>nominates its strongest candidates</strong> to the Faculty of Graduate and Postdoctoral Studies.</li>
        <li>For the <strong>Schmidt Science Fellowship</strong>, ask your department about <strong>UBC’s internal nomination</strong> — the expected deadline is <strong>April 2027</strong>, subject to official announcement.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate application for the UBC Four Year Doctoral Fellowship?',
  'Normally, no. You apply for admission to the relevant UBC graduate programme, and all admitted PhD, DMA and MD/PhD applicants are automatically considered for 4YF funding. The programme nominates selected students.'),
 ('What is the deadline for UBC Fellowships 2027?',
  'The 4YF deadline is set by each UBC graduate programme. Commonly cited admission deadlines are 15 November 2026 (January 2027 start), 15 March 2027 (May 2027 start) and 1 June 2027 (September 2027 start). The Affiliated Fellowships (Master’s) deadline is 1 December 2026.'),
 ('How much is the UBC 4YF worth?',
  'From September 2026, $24,000 a year in stipend funding plus tuition, for up to four years. It was $18,200 a year before the increase.'),
 ('Can international students get the 4YF?',
  'Yes. There is no nationality restriction — international applicants are eligible on the same footing as domestic candidates.'),
 ('What is the International Doctoral Fellowship?',
  'A separate UBC award: $30,000 a year in stipend plus tuition for 4 years, plus a minimum $18,000 package in year 5.'),
 ('Is the Schmidt Science Fellowship the same as the 4YF?',
  'No. The Schmidt Science Fellowship is a postdoctoral fellowship ($110,000 a year for at least one year) for PhD graduates in computer science, engineering or the natural sciences, and UBC nominates candidates for it. The 4YF is a doctoral award.')]) + '''
      <p class="verify">Verified 26 Oct 2026: grad.ubc.ca/awards/four-year-doctoral-fellowship-4yf (official UBC Graduate School page, opened and read) — $24,000 stipend plus full tuition per year, up to 4 years, effective September 2026, deadline set by each UBC graduate programme, Canadian / permanent resident / international citizenship, doctoral level; grad.ubc.ca award opportunities list — Affiliated Fellowships Master's 1 December 2026 before 5:00 pm PT, approximately 50 awards a year; DAADScholarship.com — 4YF admission deadlines 15 November 2026 (January 2027 start), 15 March 2027 (May 2027), 1 June 2027 (September 2027), automatic consideration on admission; ScholarshipForPhD / Universities.NSPScholarships — Schmidt Science Fellowship $110,000/year, deadline April 2027; AfterSchoolAfrica — Affiliated Fellowships doctoral deadline 15 September 2026 (passed), $175–$40,000, most around $16,000, Killam Doctoral Scholarships through the same competition. CORRECTION: "UBC Fellowships 2027" is not a single scheme with one deadline — it is a family of awards, and this article leads with the 4YF. NOT USED as open: the Affiliated Fellowships doctoral deadline (15 September 2026, passed). The 15 November 2026 / 15 March 2027 / 1 June 2027 dates are aggregator-cited admission deadlines — the official 4YF page says the deadline is set by each graduate programme, so readers are told to confirm their programme's date.</p>''',
 dl_long='15 November 2026 (January 2027 start admission deadline; the 4YF deadline itself is set by each graduate programme)',
 offlinks=[('UBC Graduate School — Four Year Doctoral Fellowship (official)', 'https://www.grad.ubc.ca/awards/four-year-doctoral-fellowship-4yf'),
           ('Bright Scholarship — University of British Columbia Fellowships 2027', 'https://brightscholarship.com/university-of-british-columbia-fellowships-2027/')],
 related_titles=['ogs-2027', 'bcdi2030', 'leeds-2027', 'bleumink-2027'])),

# ---------------------------------------------------------------- 5. Lincoln University (NZ)
A.append(dict(
 slug='lincoln-university-scholarships-2027-new-zealand',
 title='Lincoln University Scholarships 2027 in New Zealand (Funded)',
 meta='Lincoln University Scholarships 2027 in New Zealand: five international merit awards as tuition-fee credits — NZ$2,500 to NZ$15,000 — mostly automatic on admission. Scholarship forms due 31 January 2027 (Semester 1); study application 1 December 2026 — eligibility, how to apply and FAQs.',
 short='Lincoln University Scholarships 2027', kicker='New Zealand · Undergraduate & Taught Master’s · Funded', mono='LN',
 prov_short='Lincoln University', prov_cat='University · New Zealand',
 h1='Lincoln University Scholarships 2027 in New Zealand (Funded)',
 sub='Lincoln University — New Zealand’s specialist land-based university in Canterbury, near Christchurch — offers five international merit awards for 2027, worth NZ$2,500 to NZ$15,000 each. Read the fine print first: every one of them is a credit to your Lincoln tuition-fees account, not cash, and none of them is fully funded — the remaining tuition can still be large. The good news is that most of them are automatic: the Taught Master’s Merit Scholarship needs no separate form at all, and the others are assessed on your admission application. The dates that matter are 1 December 2026 for your Semester 1 study application (offshore students) and 31 January 2027 for the scholarship forms. And do not mix these up with the Manaaki New Zealand Scholarships — that is a separate New Zealand government award, not a Lincoln award.',
 dpill='Deadline 31 Jan 2027 · %d days left' % dl_left('2027-01-31'),
 facts=facts([('Award', 'Five international merit awards, all as credits to your Lincoln University Tuition Fees account on confirmed enrolment — not cash, and no living costs or airfare: International Pathway Merit Scholarship NZ$2,500 (Pathway Certificate or First Year Pathway Diploma); International Undergraduate Scholarship NZ$3,000 (undergraduate programmes); Undergraduate Vice-Chancellor’s Scholarship NZ$5,000 (Bachelor’s programmes, tenable for two consecutive semesters); International School Leavers Scholarship NZ$10,000 (first-year Bachelor’s); Taught Master’s Merit Scholarship NZ$10,000 (B average in the final year of a Bachelor’s) or NZ$15,000 (A average, selected programmes).'),
              ('Eligible', 'New international students who have not previously studied in an academic programme at Lincoln University, meeting the academic and English language requirements for their programme and the immigration requirements to study in New Zealand, and not holding any other scholarship. School Leavers: a school leaver from a New Zealand high school or an overseas high school, entering first-year Bachelor’s study. Taught Master’s Merit: a full taught Master’s programme, with at least a B average in the final year of a Bachelor’s degree (A average for the NZ$15,000 tier).'),
              ('How', 'Apply for admission to Lincoln University through the MyLinc online portal. The Taught Master’s Merit Scholarship is automatic — no separate application is required; Lincoln assesses and offers it to qualifying students. The other four awards use scholarship forms submitted by the closing dates below. The English for Further Study Award gives a tuition-fee rebate (capped at up to 12 weeks of EAP fees) to students who complete at least 12 weeks of English for Academic Purposes and then enrol in their next programme.'),
              ('Deadline', 'Scholarship forms: 31 January 2027 for Semester 1, 30 June 2027 for Semester 2. Study application for offshore students: 1 December 2026 for Semester 1. The Summer School closing date (31 October 2026) has passed. Applications for the International Undergraduate Scholarship must be received before the semester commencement date (the first day of semester).'),
              ('Fine print', 'The “fully funded” label on aggregator pages is wrong — these are partial tuition credits only, and one aggregator’s “NZD 2,500 to NZD 32,000 per annum + full tuition coverage” mixes Lincoln’s own awards with other funding and is not used. The NZ$7,000 taught-master’s tier quoted by one aggregator is not on the official page — the official tiers are NZ$10,000 (B average) and NZ$15,000 (A average, selected programmes). The Manaaki New Zealand Scholarships are a separate New Zealand government award that Lincoln highlights as a flagship route — they are not Lincoln University awards and are not covered here. One aggregator’s deadline table is garbled (it lists “Semester 2, 2026: 31 May 2027”) and is not used.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Lincoln University</strong>, in Lincoln, Canterbury — near Christchurch — is New Zealand’s specialist <strong>land-based university</strong>, founded in 1878, with strengths in <strong>agriculture, environment, business and science</strong>. For international students it offers <strong>five merit awards</strong> for 2027, and the structure is simple: they are all <strong>tuition-fee credits</strong>, paid into your Lincoln tuition-fees account once your enrolment is confirmed. The amounts run from <strong>NZ$2,500</strong> for pathway study to <strong>NZ$15,000</strong> for a taught Master’s with an A average.</p>
      <p>That is useful money, but it is a <strong>discount, not a grant</strong>: the balance of your tuition is still yours to pay, and no living costs, airfare or accommodation are covered. The awards are also deliberately easy to enter — the <strong>Taught Master’s Merit Scholarship is automatic</strong> (no separate form; Lincoln assesses you when you apply for admission), and the other four are assessed on your admission application and scholarship form. The two dates to hold are <strong>1 December 2026</strong> for your Semester 1 study application if you are applying from outside New Zealand, and <strong>31 January 2027</strong> for the scholarship forms.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>new international student</strong> who has <strong>not previously studied</strong> in an academic programme at Lincoln University.</li>
        <li>Meet the <strong>academic and English language requirements</strong> for admission to your chosen programme.</li>
        <li>Meet all <strong>immigration requirements</strong> to study in New Zealand.</li>
        <li><strong>Not hold any other scholarship</strong> at the time of application.</li>
        <li><strong>School Leavers Scholarship:</strong> be a <strong>school leaver from a New Zealand high school or an overseas high school</strong>, entering <strong>first-year Bachelor’s</strong> study.</li>
        <li><strong>Taught Master’s Merit Scholarship:</strong> enrol in a <strong>full taught Master’s programme</strong>, with at least a <strong>B average in the final year of a Bachelor’s degree</strong> (an <strong>A average</strong> qualifies for the NZ$15,000 tier on selected programmes).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>International Pathway Merit Scholarship:</strong> <strong>NZ$2,500</strong> — Pathway Certificate (Foundation) or First Year Pathway Diploma.</li>
        <li><strong>International Undergraduate Scholarship:</strong> <strong>NZ$3,000</strong> — undergraduate programmes.</li>
        <li><strong>Undergraduate Vice-Chancellor’s Scholarship:</strong> <strong>NZ$5,000</strong> — Bachelor’s programmes, for <strong>two consecutive semesters</strong>.</li>
        <li><strong>International School Leavers Scholarship:</strong> <strong>NZ$10,000</strong> — first-year Bachelor’s programmes.</li>
        <li><strong>Taught Master’s Merit Scholarship:</strong> <strong>NZ$10,000</strong> (B average) or <strong>NZ$15,000</strong> (A average, selected programmes) — full taught Master’s programmes.</li>
        <li><strong>English for Further Study Award:</strong> a <strong>tuition-fee rebate</strong> (capped at up to 12 weeks of EAP fees) for students who complete at least <strong>12 weeks of English for Academic Purposes</strong> and enrol in their next programme.</li>
        <li>Note that all awards are <strong>tuition-fee credits, not cash</strong>, and <strong>no living costs or airfare</strong> are covered.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>Lincoln University admission application</strong> through the MyLinc portal.</li>
        <li><strong>Academic transcripts and certificates</strong>.</li>
        <li><strong>English language proficiency</strong> test scores (IELTS / TOEFL) or a <strong>medium-of-instruction certificate</strong> where accepted.</li>
        <li>A <strong>CV</strong>.</li>
        <li>A <strong>personal statement</strong>.</li>
        <li><strong>Two letters of recommendation</strong>.</li>
        <li>A <strong>passport copy</strong>.</li>
        <li>Note that this document list is the typical set reported by aggregators — the <strong>official Lincoln pages list the scholarship form and the admission requirements</strong>, not a single universal document list, so check your programme’s page.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for <strong>admission to Lincoln University</strong> through the <strong>MyLinc online portal</strong> — offshore students must apply by <strong>1 December 2026</strong> for Semester 1, 2027.</li>
        <li>For the <strong>Taught Master’s Merit Scholarship</strong>, do nothing extra — it is <strong>automatic</strong>; Lincoln assesses and offers it to qualifying international students.</li>
        <li>For the other four awards, submit the <strong>scholarship form</strong> by <strong>31 January 2027</strong> (Semester 1) or <strong>30 June 2027</strong> (Semester 2).</li>
        <li>For the <strong>International Undergraduate Scholarship</strong>, make sure your application is received <strong>before the semester commencement date</strong>.</li>
        <li>Confirm your <strong>enrolment</strong> — the award is credited to your <strong>Lincoln tuition-fees account</strong> once enrolment is confirmed.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for Lincoln University Scholarships 2027?',
  'Scholarship forms are due 31 January 2027 for Semester 1 and 30 June 2027 for Semester 2. Your study application as an offshore student is due 1 December 2026 for Semester 1. The Summer School closing date (31 October 2026) has passed.'),
 ('Are Lincoln University scholarships fully funded?',
  'No. They are partial tuition-fee credits of NZ$2,500 to NZ$15,000, paid into your Lincoln tuition-fees account. No living costs, airfare or accommodation are covered, and the remaining tuition can still be large.'),
 ('Do I need a separate application for the Taught Master’s Merit Scholarship?',
  'No. It is automatic — Lincoln assesses and offers it to qualifying international students enrolling in a full taught Master’s programme. You need at least a B average in the final year of your Bachelor’s degree (A average for the NZ$15,000 tier on selected programmes).'),
 ('How much is the Taught Master’s Merit Scholarship?',
  'NZ$10,000 for a B average in the final year of a Bachelor’s degree, or NZ$15,000 for an A average on selected programmes.'),
 ('Who can apply?',
  'New international students who have not previously studied at Lincoln University, who meet the academic and English requirements for their programme and the immigration requirements to study in New Zealand, and who hold no other scholarship.'),
 ('Are the Manaaki New Zealand Scholarships the same as Lincoln scholarships?',
  'No. The Manaaki New Zealand Scholarships are a separate New Zealand government award that Lincoln highlights as a flagship route. They are not Lincoln University awards and are not covered in this article.')]) + '''
      <p class="verify">Verified 26 Oct 2026: lincoln.ac.nz/study/scholarships/international-scholarships/ (official Lincoln University international scholarships page, opened and read) — five flagship awards (Pathway Merit NZ$2,500; International Undergraduate NZ$3,000; Undergraduate Vice-Chancellor's NZ$5,000; School Leavers NZ$10,000; Taught Master's Merit automatic, no separate form) and the English for Further Study Award; lincoln.ac.nz individual scholarship pages — Taught Master's Merit NZ$15,000 (A average, selected programmes) / NZ$10,000 (B average), GPA of at least a B average required; Pathway Merit NZ$2,500, closing dates 31 January (Semester 1), 30 June (Semester 2), 31 October (Summer School); International Undergraduate NZ$3,000, applications before semester commencement; School Leavers NZ$10,000; Vice-Chancellor's NZ$5,000; StudyAbroadWithArbaz, ScholarHunter, CollegeDunia — corroboration, including the 1 December 2026 study-application deadline and 31 January 2027 scholarship-form deadline. CORRECTION: the "fully funded" label is wrong — all five awards are tuition-fee credits only. NOT USED: one aggregator's "NZD 2,500 to NZD 32,000 per annum + full tuition coverage" (mixes Lincoln awards with other funding); the NZ$7,000 taught-master's tier on one aggregator (official tiers are NZ$10,000/NZ$15,000); one aggregator's garbled deadline table ("Semester 2, 2026: 31 May 2027"). The Manaaki New Zealand Scholarships are a separate government award and are not covered here. The document list is the typical aggregator set — the official pages list the scholarship form and admission requirements, not a single universal list.</p>''',
 dl_long='31 January 2027 (scholarship forms, Semester 1; study application due 1 December 2026)',
 offlinks=[('Lincoln University — International Scholarships (official)', 'https://www.lincoln.ac.nz/study/scholarships/international-scholarships/'),
           ('Bright Scholarship — Lincoln University Scholarships 2027', 'https://brightscholarship.com/lincoln-university-scholarships-2027/')],
 related_titles=['griffith-vc', 'deakin-vc-2027', 'dalarna-2027', 'ecu-2027'])),

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
    json.dump(sizes, open('/tmp/batch54_built.json','w'))

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

#!/usr/bin/env python3
"""Batch 75 — 1 Nov 2026. FINAL batch: the last queue entry is AICTE Yashasvi.
Only one article this run because only one queue entry remains; after this
run the queue is empty and the operation is complete."""
import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'aicte-yashasvi-2024': {'mono': 'AICTE', 'title': "AICTE Yashasvi (Young Achievers' Scholarship & Holistic Academic Skills Venture Initiative) Scheme 2024",
   'href': 'aicte-yashasvi-scholarship-scheme-2024.html',
   'dpill': 'Portal open — apply well before 31 Jan 2027',
   'award': 'Rs 50,000 a year for degree students (up to 4 years) and Rs 30,000 a year for diploma students (up to 3 years), paid by DBT.',
   'elig': 'First-year degree or diploma students, or second-year lateral-entry students, in core engineering branches at AICTE-approved institutions; family income up to Rs 8 lakh a year.',
   'tags': [('Engineering', 'blue'), ('Central Govt', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

ARTICLES.append({
 'slug': 'aicte-yashasvi-scholarship-scheme-2024',
 'title': "AICTE Yashasvi (Young Achievers' Scholarship & Holistic Academic Skills Venture Initiative) Scheme 2024",
 'meta': "AICTE Yashasvi Scholarship Scheme: Rs 50,000 a year for degree students and Rs 30,000 a year for diploma students in core engineering branches at AICTE-approved institutions — 5,200 awards a year, family income up to Rs 8 lakh. The 2026-27 portal opened 15 October 2026; institute verification closes 31 January 2027 and the portal closes 28 February 2027.",
 'short': "AICTE Yashasvi Scholarship Scheme 2024",
 'kicker': 'Scholarship · Core Engineering',
 'mono': 'AICTE',
 'prov_short': 'AICTE',
 'prov_cat': 'Central Government · AICTE',
 'h1': "AICTE Yashasvi (Young Achievers' Scholarship & Holistic Academic Skills Venture Initiative) Scheme 2024",
 'sub': 'A national scholarship for meritorious students who choose core engineering rather than the newer, more fashionable branches: Rs 50,000 a year for degree students and Rs 30,000 a year for diploma students, across 5,200 awards a year. This page keeps the queue\u2019s 2024 title — the year the scheme began — but the cycle that is open right now is 2026-27, and its dates are the ones in the deadline card.',
 'dpill': 'Portal open — apply well before 31 Jan 2027',
 'facts': facts([
   ('Provider', 'All India Council for Technical Education (AICTE)'),
   ('Award', 'Rs 50,000 a year for degree students (up to 4 years; 3 years for lateral entry) and Rs 30,000 a year for diploma students (up to 3 years; 2 years for lateral entry), paid annually by Direct Benefit Transfer'),
   ('Scholarships', '5,200 a year — 2,593 for degree courses and 2,607 for diploma courses, distributed state-wise'),
   ('Eligibility', 'First-year degree or diploma students, or second-year lateral-entry students, in core engineering branches at AICTE-approved institutions; Indian citizen; family income not exceeding Rs 8 lakh a year from all sources'),
   ('Core branches', 'Civil, Chemical, Electrical, Electronics and Communication, Mechanical, Agricultural Engineering and Textile Technology'),
   ('Portal', 'yashasvi.aicte.gov.in — separate from the National Scholarship Portal'),
   ('Deadline (2026-27 cycle)', 'Portal opened 15 October 2026; institute (level 1) verification by 31 January 2027; State Nodal Officer (level 2) verification by 15 February 2027; portal closes 28 February 2027; no separate student deadline is published'),
   ('Title note', 'The scheme commenced in academic year 2024-25. The 2024 title is kept here, but the live cycle at the time of writing is 2026-27'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>YASHASVI — the Young Achievers\u2019 Scholarship and Holistic Academic Skills Venture Initiative — is AICTE\u2019s own scholarship for students entering the core branches of engineering. It was introduced for academic year 2024-25, in step with the National Education Policy 2020, with a deliberate purpose: to draw able students towards the branches that underpin manufacturing and infrastructure — civil, chemical, electrical, electronics and communication, mechanical, agricultural engineering and textile technology — rather than leaving those seats to fill by default. The scheme runs on AICTE\u2019s own portal, not on the National Scholarship Portal, and it is administered by AICTE itself.</p>
      <p>A warning about a lookalike name, because the two schemes are constantly confused online. PM-YASASVI — the Pradhan Mantri Young Achievers Scholarship Award Scheme for Vibrant India — is a different programme run by the Ministry of Social Justice and Empowerment for OBC, EBC and DNT school students in Classes 9 to 12, applied for through the National Scholarship Portal, with school-level amounts of up to Rs 75,000 and Rs 1,25,000 a year. Nothing on that scheme applies here. This article is about AICTE\u2019s engineering scholarship only, and its portal is yashasvi.aicte.gov.in.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be an Indian citizen admitted to the first year of a degree or diploma course in a core engineering branch at an AICTE-approved institution, or admitted to the second year through lateral entry.</li>
        <li>Be studying one of the core branches: Civil, Chemical, Electrical, Electronics and Communication, Mechanical, Agricultural Engineering or Textile Technology.</li>
        <li>Have an annual family income from all sources of no more than Rs 8 lakh, supported by an income certificate issued by the State or Union Territory government.</li>
        <li>Have no more than a two-year gap between passing the qualifying examination and joining the course.</li>
      </ul>
      <p>Selection is on merit in the qualifying examination: Class 12 marks for degree students, Class 10 marks for diploma students, and the average consolidated percentage across all six semesters of the diploma for lateral-entry students. Lateral-entry awards are limited to 10% of the total seats allocated in the respective state. Reservations apply as per Government of India norms.</p>
      <h2 id="benefits">What you get</h2>
      <p>Degree students receive Rs 50,000 a year for every year of study, up to four years for first-year entrants and three years for lateral entrants. Diploma students receive Rs 30,000 a year, up to three years for first-year entrants and two years for lateral entrants. Payment is made annually through Direct Benefit Transfer. A total of 5,200 scholarships are earmarked each year — 2,593 for degree courses and 2,607 for diploma courses — distributed among States and Union Territories in proportion to their share of degree and diploma seats in AICTE-approved institutions.</p>
      <p>Two conditions carry real consequences and are worth stating plainly. First, a student who receives any other scholarship, emolument, salary, stipend or financial assistance from another source during the course risks discontinuation of this scholarship and must refund the amount to AICTE. Second, a student who shifts from a specified core branch to another branch in a subsequent year becomes ineligible for further scholarship and must refund the entire amount. A student who fails to be promoted to the next class or level forfeits the scholarship.</p>
      <h2 id="amount-note">An amount conflict you should know about</h2>
      <p>Older summaries of this scheme — including the queue entry this article was written from — quote Rs 18,000 a year for degree students and Rs 12,000 a year for diploma students, with 5,000 awards for each level. Those figures do not match the scheme guidelines of 2024, which state Rs 50,000 and Rs 30,000 and a total of 5,200 awards, and the 2026-27 cycle reporting agrees with the guidelines figures. This article therefore follows the guidelines figures and treats the Rs 18,000 and Rs 12,000 figures as outdated. Applicants should still confirm the amount on the official portal before relying on it, since one current guide notes that the lower figures may reflect a subsequent revision somewhere in the chain — but no official revision notice stating them was found in this run\u2019s searches.</p>
      <h2 id="documents">Documents needed</h2>
      <p>No single published document checklist was found in the sources checked. The items the scheme\u2019s own process descriptions require applicants to have in hand are:</p>
      <ul>
        <li>Income certificate issued by the State or Union Territory government, showing family income of no more than Rs 8 lakh a year.</li>
        <li>Academic transcripts or marksheets of the qualifying examination (Class 12 for degree applicants, Class 10 for diploma applicants, diploma semester marks for lateral entry).</li>
        <li>Admission letter from the AICTE-approved institution.</li>
        <li>APAAR ID, which scheme guides list as mandatory for applicants to this scheme.</li>
        <li>An Aadhaar-seeded bank account in the student\u2019s own name, for Direct Benefit Transfer payment.</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Go to the AICTE Yashasvi portal at yashasvi.aicte.gov.in and register as a new applicant.</li>
        <li>Confirm the email verification link sent after registration (check the spam folder if it does not arrive).</li>
        <li>Fill in the application with your qualifying marks, branch, institution and family income details, and upload the income certificate, transcripts and admission letter.</li>
        <li>Submit well before your institute\u2019s verification deadline — see the timeline below — because an unverified application cannot proceed.</li>
        <li>Track the application on the same portal through the institute and State Nodal Officer verification stages, and fix any discrepancy when the portal reopens for corrections.</li>
      </ol>
      <h2 id="deadline-note">The 2026-27 timeline, and why there is no single student deadline</h2>
      <p>The 2026-27 notifications for Yashasvi (and for the companion Saraswati scholarship for girls in BBA, BCA and BMS) were issued on 21 October 2026, and the portals opened on 15 October 2026 for fresh applicants admitted in 2026-27 and for renewal students in their second and third year. AICTE has not printed a separate last date for students. Instead, the published dates are the verification dates: the institute must verify by 31 January 2027, the State Nodal Officer by 15 February 2027, the portal then reopens for students to fix discrepancies, and the portal closes on 28 February 2027. The practical consequence is simple: apply well before 31 January 2027, because your college has to verify your form by then. Older schedules found in search results — for example a 15 September 2026 student deadline with portal closure on 30 September 2026 — belong to an earlier round and are superseded by the 2026-27 notification; do not use them.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this the same as PM-YASASVI?', 'No. PM-YASASVI is a Ministry of Social Justice and Empowerment scheme for OBC, EBC and DNT school students in Classes 9 to 12, applied for through the National Scholarship Portal. AICTE Yashasvi is for first-year degree and diploma students in core engineering branches, applied for on yashasvi.aicte.gov.in.'),
   ('How much do I get?', 'Rs 50,000 a year for degree courses (up to 4 years, or 3 for lateral entry) and Rs 30,000 a year for diploma courses (up to 3 years, or 2 for lateral entry), under the scheme guidelines. Older listings quoting Rs 18,000 and Rs 12,000 are treated here as outdated — see the amount note above.'),
   ('Which branches count as core?', 'Civil, Chemical, Electrical, Electronics and Communication, Mechanical, Agricultural Engineering and Textile Technology. Students in other branches are not eligible, and shifting out of a core branch ends the scholarship.'),
   ('Is there an income limit?', 'Yes: family income from all sources must not exceed Rs 8 lakh a year, supported by a State or Union Territory government income certificate.'),
   ('Can I hold another scholarship at the same time?', 'No. The guidelines state that a student must not receive any other scholarship, emolument, salary, stipend or financial assistance from another source during the course; if they do, the scholarship may be discontinued and the amount must be refunded.'),
   ('What is the last date for students?', 'No separate student deadline is published for 2026-27. The institute verification deadline is 31 January 2027 and the portal closes 28 February 2027, so apply well before 31 January 2027.'),
   ('Where do I apply?', 'On the AICTE Yashasvi portal, yashasvi.aicte.gov.in — not on the National Scholarship Portal. The scheme helpdesk email published in scheme guides is yashasvi@aicte-india.org.'),
  ]),
 'verify': 'Verified 1 Nov 2026 against the CareerBox report on the 2026-27 opening (notifications issued 21 October 2026; portals opened 15 October 2026 for fresh 2026-27 applicants and second- and third-year renewals; institute verification by 31 January 2027; State Nodal Officer verification by 15 February 2027; discrepancy-correction reopening; portal closes 28 February 2027; no separate student last date published; core branches Civil, Chemical, Electrical, Electronics and Communication, Mechanical, Agricultural Engineering and Textile Technology; income up to Rs 8 lakh a year; Rs 50,000 a year degree for up to 4 years and Rs 30,000 a year diploma for up to 3 years by DBT; 5,200 awards a year, 2,593 degree and 2,607 diploma), the AICTE YASHASVI Scheme Guidelines 2024 as hosted on the BCREC site (commencement academic year 2024-25; 5,200 scholarships, 2,593 degree and 2,607 diploma; Rs 50,000 a year degree for a maximum of 4 years and Rs 30,000 a year diploma for a maximum of 3 years; DBT annually; merit of qualifying examination; lateral-entry selection on the six-semester diploma average, limited to 10% of state allocation; no more than a two-year gap between qualifying examination and admission; no other financial assistance during the course; branch shift ends eligibility and requires refund; forfeiture on failure to be promoted), and scheme guides on govtschemes.in and collegesearch.in (income certificate from the State or UT government; academic transcripts and admission letter; APAAR ID mandatory; helpdesk yashasvi@aicte-india.org). The queue amount of up to Rs 18,000 a year and older summaries quoting Rs 18,000 degree and Rs 12,000 diploma with 5,000 awards per level conflict with the guidelines figures and are flagged in the article as outdated. Older 15 September 2026 schedule dates on govtschemes.in belong to an earlier round and are superseded by the 2026-27 notification.',
 'dl_long': '31 January 2027 — last date for institute (level 1) verification; portal closes 28 February 2027. No separate student deadline is published, so apply well before 31 January 2027',
 'offlinks': [('AICTE Yashasvi portal (apply)', 'https://yashasvi.aicte.gov.in/'), ('Buddy4Study — AICTE Yashasvi Scheme', 'https://www.buddy4study.com/scholarship/aicte-yashasvi-young-achievers-scholarship-holistic-academic-skills-venture-initiative-scheme'), ('AICTE YASHASVI Scheme Guidelines 2024 (PDF)', 'https://mail.bcrec.ac.in/public/storage/notice_file/1737609975.pdf')],
 'related_titles': ['aicte-saksham-2024', 'swanath-2026', 'aicte-apf-2026', 'aicte-pdf-2024'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

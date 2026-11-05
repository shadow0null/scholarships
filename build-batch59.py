#!/usr/bin/env python3
"""Batch 59 (cron run 59, 28 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Al Qasimi Foundation Scholarships 2026 - VERIFIED (overseas open to
   29 Dec 2026; domestic closed 30 Jun 2026; RAK nationals only; official
   alqasimifoundation.com page read in full).
2. York University Scholarships 2026 - VERIFIED as the President's
   International Scholarship of Excellence, Fall 2027 entry (deadline
   27 Jan 2027; $45,000 CAD/year; official York Future Students pages).
3. IUSS Pavia PhD Scholarship 2027 - SKIPPED: deadline passed
   16 Jun 2026 (42nd cycle, official IUSS page); no later 2027 call.
4. Seoul University Scholarship 2026 - SKIPPED: aggregator umbrella
   label, not a single SNU scheme; last date 9 Jul 2026 passed; no
   verifiable current open call.
5. KAPSARC Graduate Development Program 2026 - SKIPPED: 2026 cohort
   closed (assessments Jul 2026, programme started Oct 2026); no 2027
   call announced; no exact closing date ever published.
6. University of Tsukuba MEXT Scholarship 2027 - VERIFIED WITH
   CORRECTION (official Tsukuba MEXT page, Sep 2026: General Program
   expected discontinued from 2027; only Special Program continues;
   no single deadline; embassy route largely closed for 2027).
7. GovAI Winter Fellowship 2027 - SKIPPED: real deadline was
   12 Jul 2026 (official posting); queue's "January 2027" is wrong.
8. List of Top Scholarships in Germany 2026 - SKIPPED: listicle.
9. University of Bergamo Scholarship 2026 - SKIPPED: deadline passed
   10 Jul 2026 (Top International Student Grants); no follow-up call.
10. University of Agder Scholarships 2027 - SKIPPED: deadline passed
    1 Oct 2026 (five NOK 15,000 thesis grants); UiA offers no
    scholarships for 2027/28.
11. UK Embassy Paid Internships 2026 - SKIPPED: rolling family of
    vacancies, no single scheme or deadline.
12. Rosa Luxemburg Stiftung Scholarships 2027 - SKIPPED: deadline
    passed 1 Oct 2026 (funding from Apr 2027); next round 1 Oct 2027.
13. Norway Mobility Scholarships 2027 - SKIPPED: no official source
    or deadline verifiable (aggregator-only label for HK-dir Mobility
    Grant; deadline "not specified").
14. Sapienza University Scholarships 2026 - SKIPPED: umbrella label,
    every scheme with a published 2026 deadline already closed
    (admissions 15 May / 31 Jul 2026; #100ragazzeSTEM 17 Apr 2026).
15. Laval University Excellence Scholarships 2027 - SKIPPED: deadline
    passed 17 Jun 2026 (PBEEE pre-selection); no new call found.
16. Matsumae International Research Fellowship 2027 - SKIPPED:
    deadline passed 30 Jun 2026 (official MIF page: applications
    closed); no 2028 call published.
17. EPFL CYD Fellowship 2027 - VERIFIED as the 15th call (opens
    3 Dec 2026; Stage 1 deadline 25 Feb 2027, 17:00 CET; Master
    Thesis rolling; official EPFL pages).
18. South Korea KDI Scholarships 2027 - SKIPPED: deadline passed
    31 Jul 2026 (WIPO-KDI MIPD, Spring 2027 intake); no new call.
19. Duke University Karsh Scholarship 2026 - VERIFIED (Early Decision
    2 Nov 2026; Regular Decision 4 Jan 2027; no separate application;
    official Duke pages).

Run from /home/hatch/workspace/scholarships-17k/.
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
 'alqasimi-foundation-2026': {'mono': 'AQ', 'title': 'Al Qasimi Foundation Scholarships 2026 in UAE (Tuition Fee, Stipend)',
   'href': 'al-qasimi-foundation-scholarships-2026-uae.html',
   'dpill': 'Deadline 29 Dec 2026 · %d days left' % dl_left('2026-12-29'),
   'award': 'Overseas Masters: 100% tuition plus AED 12,000–15,000 a month, an annual round-trip ticket and annual health insurance. Overseas Bachelor: AED 3,000 a month. Domestic Bachelor: 100% tuition at private universities or AED 3,000 a month at federal universities; Domestic Masters: 50% tuition.',
   'elig': 'Emirati nationals of Ras Al Khaimah holding a RAK Family Book. Bachelor: 95% high-school average. Masters: a Bachelor’s degree with GPA 3.0–3.5+. IELTS 6.0–6.5.',
   'tags': [('Undergraduate & Master’s', 'blue'), ('UAE', 'teal')]},
 'york-pise-2027': {'mono': 'YU', 'title': 'President’s International Scholarship of Excellence 2027 at York University in Canada ($45,000 per Year)',
   'href': 'york-university-presidents-international-scholarship-excellence-2027-canada.html',
   'dpill': 'Deadline 27 Jan 2027 · %d days left' % dl_left('2027-01-27'),
   'award': '$45,000 CAD per year for up to four years ($180,000 CAD in total), renewable subject to good academic standing. A substantial partial scholarship — it does not cover the full cost of study.',
   'elig': 'International high-school applicants entering the first year of a four-year undergraduate degree at York in Fall 2027; minimum 80% (A) admission average; leadership and community involvement; nominated by a school official.',
   'tags': [('Undergraduate', 'blue'), ('Canada', 'teal')]},
 'tsukuba-mext-2027': {'mono': 'UT', 'title': 'University of Tsukuba MEXT Scholarship 2027 in Japan (Fully Funded)',
   'href': 'university-of-tsukuba-mext-scholarship-2027-japan.html',
   'dpill': 'Deadlines vary by programme — check the programme page',
   'award': 'Full tuition exemption, round-trip airfare and a monthly stipend of about ¥117,000 (undergraduate), ¥144,000 (Master’s) or ¥145,000 (doctoral) — the standard MEXT rates as reported; the University of Tsukuba page does not state figures.',
   'elig': 'Nationals of countries with diplomatic relations with Japan; GPA 2.30/3.00+; under 35 for the graduate route; JLPT N2 or English CEFR B2. University Recommendation now runs only through individual Special Programs.',
   'tags': [('Master’s & PhD', 'blue'), ('Japan', 'teal')]},
 'duke-karsh-2026': {'mono': 'DU', 'title': 'Duke University Karsh Scholarship 2026 in USA (Fully Funded)',
   'href': 'duke-university-karsh-scholarship-2026-usa.html',
   'dpill': 'Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
   'award': 'Fully funded for four years: full tuition, room and board, mandatory fees, demonstrated financial need beyond those costs, and funding for three summers of research or internships. No separate Karsh application — apply to Duke and request financial aid.',
   'elig': 'International applicants who are not US citizens or dual US citizens, applying as incoming first-year undergraduates with demonstrated financial need; must not already hold a BA or BS degree.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'epfl-cyd-2027': {'mono': 'CY', 'title': 'EPFL CYD Fellowship 2027 in Switzerland (Fully Funded)',
   'href': 'epfl-cyd-fellowship-2027-switzerland.html',
   'dpill': 'Deadline 25 Feb 2027 · %d days left' % dl_left('2027-02-25'),
   'award': 'Doctoral: salary contribution for 4 years (possible 1-year extension) plus up to CHF 3,000 a year for research and CHF 5,000 a year for conferences. Distinguished Postdoctoral: same, for up to 2 years. Master Thesis: CHF 2,500 a month for up to 6 months plus up to CHF 1,500 for research.',
   'elig': 'Any nationality, no age limit. Master Thesis: enrolled in a Master’s at a Swiss higher education institution. Doctoral: enrolled in a PhD at a Swiss higher education institution. Postdoctoral: endorsed by a professor at a Swiss higher education institution.',
   'tags': [('Master’s, PhD & Postdoc', 'blue'), ('Switzerland', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Al Qasimi Foundation Scholarships
A.append(dict(
 slug='al-qasimi-foundation-scholarships-2026-uae',
 title='Al Qasimi Foundation Scholarships 2026 in UAE (Tuition Fee, Stipend)',
 meta='Al Qasimi Foundation Scholarships 2026: overseas Bachelor and Masters awards for Emirati nationals of Ras Al Khaimah, open to 29 December 2026. Up to 100% tuition plus AED 12,000–15,000 a month for overseas Masters. Domestic applications closed 30 June 2026.',
 short='Al Qasimi Foundation Scholarships 2026', kicker='UAE · Undergraduate & Master’s · Funded', mono='AQ',
 prov_short='Al Qasimi Foundation', prov_cat='Foundation · United Arab Emirates',
 h1='Al Qasimi Foundation Scholarships 2026 in UAE (Tuition Fee, Stipend)',
 sub='Read this first, because the Al Qasimi Foundation Scholarships are two different things at once: a domestic programme that has already closed, and an overseas programme that is still open. The Sheikh Saud bin Saqr Al Qasimi Foundation for Policy Research runs four scholarship categories for Emirati nationals of Ras Al Khaimah — domestic Bachelor and Masters, and overseas Bachelor and Masters. Domestic applications for the 2026 cycle closed on 30 June 2026. Overseas applications remain open from 2 January to 29 December 2026, so if you are a Ras Al Khaimah national planning to study abroad, this is still live. The other thing to know before you read further: these scholarships are not open to international applicants, whatever the aggregator sites say — the official page states repeatedly that applicants must be Emirati nationals from Ras Al Khaimah holding a RAK Family Book.',
 dpill='Deadline 29 Dec 2026 · %d days left' % dl_left('2026-12-29'),
 facts=facts([('Award', 'Overseas Masters (Al Qasimi Scholarship): 100% tuition plus AED 12,000–15,000 a month, an annual round-trip ticket and annual health insurance. MoHESR-sponsored overseas Masters recipients receive AED 5,000 a month instead. Overseas Bachelor: AED 3,000 a month (for Ministry-sponsored or self-funded students). Domestic Bachelor: 100% tuition at private universities, or AED 3,000 a month at federal universities. Domestic Masters: 50% tuition fee coverage.'),
              ('Eligible', 'Emirati nationals from Ras Al Khaimah holding a RAK Family Book. Also open to Grade 12 graduates within the past two years, Ras Al Khaimah Government employees and Emirati professionals from Ras Al Khaimah. Bachelor: minimum 95% high-school average, including 95% in all scientific subjects; continuing students need a cumulative GPA of 3.0–3.5 or higher. Masters: a Bachelor’s degree, with a cumulative GPA of 3.0–3.5 or higher. IELTS 6.0 (Domestic Bachelor), 6.0–6.5 (Overseas Bachelor), 6.5 (Masters); IELTS 7.0 for Doctor of Medicine where applicable. Overseas study must be at a university in the Top 200 of the QS or Times Higher Education rankings, or accredited by the UAE Ministry of Higher Education, with unconditional admission.'),
              ('How', 'Apply online only through the scholarship portal linked from the official scholarships page. Review the eligibility criteria for the relevant category, create a portal account (or log in), select the category, complete the form in English and upload all required documents, then submit before the deadline — late applications are not considered. A confirmation email is sent on successful submission; if none arrives, check spam or contact scholarships@alqasimifoundation.rak.ae.'),
              ('Deadline', 'Overseas (Bachelor and Masters): 29 December 2026 — application period 2 January to 29 December 2026. Domestic (Bachelor and Masters): 30 June 2026 — CLOSED. Application period was 1 April to 30 June 2026.'),
              ('Fine print', 'Not open to international applicants — the "all nationalities" claim on aggregator sites is wrong; the Foundation’s separate Doctoral Research Grants are the programme open to PhD students of any nationality, and the two must not be confused. The exact document checklist is not published on the official scholarships page — the commonly listed documents below come from aggregators, so confirm the checklist in the portal. Do not confuse this with Al Qasimia University in Sharjah, a different institution.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Sheikh Saud bin Saqr Al Qasimi Foundation for Policy Research</strong>, based in Ras Al Khaimah, runs a scholarship programme for <strong>Emirati nationals of Ras Al Khaimah</strong> through its Scholarship Office. There are <strong>four categories</strong>: domestic Bachelor, domestic Masters, overseas Bachelor and overseas Masters. The award is not one flat package — it changes sharply by category, from <strong>50% tuition</strong> for a domestic Masters to <strong>100% tuition plus AED 12,000–15,000 a month</strong>, an annual round-trip ticket and annual health insurance for an overseas Masters on the Al Qasimi Scholarship.</p>
      <p>The timing is split too. The <strong>domestic</strong> categories for the 2026 cycle ran from <strong>1 April to 30 June 2026</strong> and are closed. The <strong>overseas</strong> categories run from <strong>2 January to 29 December 2026</strong> and are still open. So the live opportunity in this article is the overseas one: a Ras Al Khaimah national heading to a university in the <strong>Top 200 of the QS or Times Higher Education rankings</strong>, or accredited by the UAE Ministry of Higher Education, with unconditional admission. Priority goes to disciplines aligned with Ras Al Khaimah’s strategic goals and workforce needs.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Emirati nationals from Ras Al Khaimah holding a RAK Family Book</strong>. Also open to Grade 12 graduates within the past two years, Ras Al Khaimah Government employees and Emirati professionals from Ras Al Khaimah. <strong>Not open to international applicants</strong> — aggregator sites claiming "all nationalities" are wrong.</li>
        <li>For a <strong>Bachelor</strong>: a minimum <strong>95% high-school average</strong>, including <strong>95% minimum in all scientific subjects</strong>; continuing students need a cumulative <strong>GPA of 3.0–3.5 or higher</strong>.</li>
        <li>For a <strong>Masters</strong>: a <strong>Bachelor’s degree</strong> (or continuing-student status for overseas), with a cumulative <strong>GPA of 3.0–3.5 or higher</strong>.</li>
        <li>English: <strong>IELTS 6.0</strong> (Domestic Bachelor), <strong>6.0–6.5</strong> (Overseas Bachelor), <strong>6.5</strong> (Masters); <strong>IELTS 7.0</strong> for Doctor of Medicine where applicable.</li>
        <li>Overseas study must be at a university in the <strong>Top 200 of the QS or Times Higher Education rankings</strong>, or accredited by the <strong>UAE Ministry of Higher Education</strong>, with <strong>unconditional admission</strong>.</li>
        <li>Domestic study must be at one of the <strong>approved universities/programmes</strong> listed by the Scholarship Office (13 universities, 214 programmes on the official page).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Overseas Masters (Al Qasimi Scholarship):</strong> <strong>100% tuition</strong> plus <strong>AED 12,000–15,000 a month</strong>, an <strong>annual round-trip ticket</strong> and <strong>annual health insurance</strong>. MoHESR-sponsored recipients receive <strong>AED 5,000 a month</strong> instead.</li>
        <li><strong>Overseas Bachelor:</strong> <strong>AED 3,000 a month</strong> (for Ministry-sponsored or self-funded students).</li>
        <li><strong>Domestic Bachelor:</strong> <strong>100% tuition at private universities</strong>, or <strong>AED 3,000 a month at federal universities</strong>.</li>
        <li><strong>Domestic Masters:</strong> <strong>50% tuition fee coverage</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>exact document checklist is not published on the official scholarships page</strong> — the page links to expandable "View full requirements" sections and to the application portal, but no checklist appeared in the page text. Confirm the exact checklist in the portal before submitting.</li>
        <li>The documents <strong>commonly listed</strong> by aggregators, consistently across several sites, are: the completed <strong>online application form</strong>, <strong>degree certificate</strong>, <strong>academic transcript</strong>, <strong>passport or national ID</strong>, <strong>medical certificate</strong> and an updated <strong>CV/resume</strong>. Other sites add an IELTS certificate, an admission letter and recommendation letters — the lists conflict, so treat them as a guide, not as the official requirement.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the <strong>online scholarship portal</strong> linked from the official scholarships page (alqasimifoundation.com/scholarships).</li>
        <li>Review the <strong>eligibility criteria</strong> for the relevant Domestic or Overseas category.</li>
        <li><strong>Create a portal account</strong> (new users) or log in.</li>
        <li>Select the appropriate <strong>scholarship category</strong>.</li>
        <li>Complete the application form in <strong>English</strong> and upload all required documents, then submit before the stated deadline — <strong>late applications are not considered</strong>.</li>
        <li>Applications are <strong>online only</strong>; in-person submissions are not accepted. A <strong>confirmation email</strong> is sent on successful submission; if none arrives, check spam or contact <strong>scholarships@alqasimifoundation.rak.ae</strong> — the only contact published on the official page.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Al Qasimi Foundation Scholarships 2026?',
  'Overseas Bachelor and Masters applications are open from 2 January to 29 December 2026. Domestic Bachelor and Masters applications for the 2026 cycle closed on 30 June 2026.'),
 ('Are the Al Qasimi Foundation Scholarships open to international students?',
  'No. They are for Emirati nationals from Ras Al Khaimah holding a RAK Family Book (plus Grade 12 graduates within the past two years, RAK Government employees and Emirati professionals from Ras Al Khaimah). Aggregator sites claiming "all nationalities" are wrong — they appear to confuse these scholarships with the Foundation’s separate Doctoral Research Grants, which are open to PhD students of any nationality.'),
 ('How much is the Al Qasimi Foundation Scholarship worth?',
  'It depends on the category. Overseas Masters on the Al Qasimi Scholarship: 100% tuition plus AED 12,000–15,000 a month, an annual round-trip ticket and annual health insurance (MoHESR-sponsored recipients get AED 5,000 a month instead). Overseas Bachelor: AED 3,000 a month. Domestic Bachelor: 100% tuition at private universities or AED 3,000 a month at federal universities. Domestic Masters: 50% tuition.'),
 ('What grades do I need for the Al Qasimi Foundation Scholarship?',
  'For a Bachelor: a minimum 95% high-school average, including 95% in all scientific subjects; continuing students need a cumulative GPA of 3.0–3.5 or higher. For a Masters: a Bachelor’s degree with a cumulative GPA of 3.0–3.5 or higher.'),
 ('What IELTS score do I need for the Al Qasimi Foundation Scholarship?',
  'IELTS 6.0 for Domestic Bachelor, 6.0–6.5 for Overseas Bachelor and 6.5 for Masters; IELTS 7.0 for Doctor of Medicine where applicable.'),
 ('Where can I study on the overseas scholarship?',
  'At a university in the Top 200 of the QS or Times Higher Education rankings, or accredited by the UAE Ministry of Higher Education, with unconditional admission. Priority goes to disciplines aligned with Ras Al Khaimah’s strategic goals and workforce needs.'),
 ('What documents do I need for the Al Qasimi Foundation Scholarship?',
  'The exact checklist is not published on the official scholarships page, so confirm it in the application portal. Aggregators consistently list the online application form, degree certificate, academic transcript, passport or national ID, medical certificate and an updated CV/resume.'),
 ('How do I apply for the Al Qasimi Foundation Scholarship?',
  'Online only, through the portal linked from alqasimifoundation.com/scholarships. Create an account, select your category, complete the form in English, upload your documents and submit before the deadline. Contact the Scholarship Office at scholarships@alqasimifoundation.rak.ae if you do not receive a confirmation email.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the Al Qasimi Foundation's official scholarships page (alqasimifoundation.com/scholarships, read in full), corroborated by CoursMooc, AfroCareer and GlobalScholarshipsHub — four categories for Emirati nationals of Ras Al Khaimah (RAK Family Book): domestic Bachelor and Masters, overseas Bachelor and Masters. Domestic 2026 cycle closed 30 June 2026 (application period 1 April – 30 June 2026); overseas open 2 January – 29 December 2026. Awards per the official page: Domestic Bachelor 100% tuition at private universities or AED 3,000/month at federal universities; Domestic Masters 50% tuition; Overseas Bachelor AED 3,000/month (Ministry-sponsored or self-funded); Overseas Masters 100% tuition plus AED 12,000–15,000/month, annual round-trip ticket and annual health insurance (MoHESR-sponsored recipients AED 5,000/month instead). Eligibility: RAK nationals (also Grade 12 graduates within the past two years, RAK Government employees, Emirati professionals from RAK); Bachelor 95% high-school average incl. 95% in all scientific subjects, continuing students GPA 3.0–3.5+; Masters Bachelor's degree, GPA 3.0–3.5+; IELTS 6.0 (Domestic Bachelor), 6.0–6.5 (Overseas Bachelor), 6.5 (Masters), 7.0 for Doctor of Medicine where applicable; overseas at Top 200 QS/THE or MoHESR-accredited universities with unconditional admission; domestic at approved universities/programmes (13 universities, 214 programmes). CONFLICTS: (1) "all nationalities eligible" on Bright Scholarship, EngineersJob, Jehlum, ScholarshipUnion and Ehsaas Kafaalat is WRONG — official page requires RAK nationals; the error likely comes from merging these scholarships with the Foundation's separate Doctoral Research Grants, open to PhD students of any nationality. (2) CoursMooc alone claims Overseas Bachelor gets "100% tuition + AED 3,000 stipend" — official page lists only the AED 3,000/month stipend for Overseas Bachelor; 100% tuition applies to Domestic Bachelor and Overseas Masters only. (3) GlobalScholarshipsHub's "50% master tuition support" without a category matches Domestic Masters only; Overseas Masters is 100%. (4) Al Qasimia University, Sharjah is a different institution and is not mixed in here. Documents: exact checklist NOT published on the official page — the commonly listed documents (application form, degree certificate, transcript, passport/national ID, medical certificate, CV) are aggregator-sourced and lists conflict, so the article flags them as unconfirmed. Apply online only via the portal linked from the official page; confirmation email on submission; contact scholarships@alqasimifoundation.rak.ae (only contact published). The direct portal URL was not captured in the fetched page text, so the article links to the official scholarships page rather than inventing a portal link.</p>''',
 dl_long='Overseas: 29 December 2026 (domestic closed 30 June 2026)',
 offlinks=[('Al Qasimi Foundation — Scholarships (official)', 'https://www.alqasimifoundation.com/scholarships'),
           ('Bright Scholarship — Al Qasimi Foundation Scholarships 2026', 'https://brightscholarship.com/al-qasimi-foundation-scholarships-2026/'),
           ('CoursMooc — Al Qasimi Foundation Overseas Bachelor Scholarship 2026', 'https://coursmooc.com/scholarships/al-qasimi-foundation-overseas-bachelor-scholarship-2026/')],
 related_titles=['mbzuai', 'uaeu-2026', 'doha-2027', 'qatar-gov-2027'])),

# ---------------------------------------------------------------- 2. York University — President's International Scholarship of Excellence
A.append(dict(
 slug='york-university-presidents-international-scholarship-excellence-2027-canada',
 title='President’s International Scholarship of Excellence 2027 at York University in Canada ($45,000 per Year)',
 meta='President’s International Scholarship of Excellence 2027 at York University: $45,000 CAD per year for up to four years ($180,000 CAD) for international high-school applicants entering Fall 2027. Student deadline 27 January 2027; nominator deadline 4 February 2027.',
 short='President’s International Scholarship of Excellence 2027', kicker='Canada · Undergraduate · $45,000 per Year', mono='YU',
 prov_short='York University', prov_cat='University · Canada',
 h1='President’s International Scholarship of Excellence 2027 at York University in Canada ($45,000 per Year)',
 sub='Read this first, because the queue title behind this article — "York University Scholarships 2026" — is misleading in two ways. The award it points to is not a general 2026 scholarship: it is one named award, the President’s International Scholarship of Excellence, for students entering York in Fall 2027. And it is not fully funded: it pays $45,000 CAD a year for up to four years, which is a very large partial scholarship, but York itself warns that international scholarships are limited and applicants should be prepared to support themselves throughout their studies. What it does offer is rare: a renewable $180,000 CAD over four years, awarded on academic strength plus leadership and community involvement, with no offer of admission needed before you apply for the award.',
 dpill='Deadline 27 Jan 2027 · %d days left' % dl_left('2027-01-27'),
 facts=facts([('Award', '$45,000 CAD per year, up to $180,000 CAD over four years. Renewable for a further three years of full-time undergraduate study if the recipient maintains good academic standing each year. The number of recipients is not published in the official notification — York says only "a select number". This is a substantial partial scholarship, not full funding of all study costs.'),
              ('Eligible', 'International high-school applicants entering the first year of a four-year undergraduate degree at York in Fall 2027. Holds international student status and pays international tuition fees. Minimum final admission average of 80% (A) or equivalent. Strong academic performance, plus leadership skills and active involvement in volunteer work and extracurricular activities. Officially nominated by a guidance counsellor, principal or senior school official — a maximum of two nominations per school per year. Under York’s definition of a high-school applicant: under 21 by 31 December of the admission year, out of full-time high-school study for less than two years since graduation, and no studies attempted at an accredited college or university.'),
              ('How', '1) Apply for admission to an undergraduate programme at York for Fall 2027. 2) Receive the 9-digit York reference number (within about 5 business days of the admission application). 3) When the scholarship application opens on 1 November 2026, log in with that reference number and complete the International Student Scholarship & Award Application. 4) Submit by 27 January 2027, 11:59 PM EST — no offer of admission is needed before applying for the entrance award. 5) York emails the nominator a link to confirm the nomination and submit the reference letter, to be completed by 4 February 2027, 11:59 PM EST.'),
              ('Deadline', 'Student application: 27 January 2027, 11:59 PM EST. Nominator confirmation and reference letter: 4 February 2027, 11:59 PM EST. Application opens 1 November 2026. Apply for admission well ahead of 27 January, since the scholarship form needs the York reference number issued after the admission application.'),
              ('Fine print', 'The 27 January date is confirmed by York’s dedicated PISE guide and the header of its general incoming-scholarships page; one table row on that same page says 26 January alongside an obvious typo, and is not used. A "20 awards per year" figure on secondary sites is not confirmed on York’s official pages and is not stated here. A Canadian study permit is mentioned by secondary sources but was not stated in the official PISE guide checked, so it is not presented as a PISE condition. A CV, transcripts or an English-proficiency certificate do not appear in the official PISE guide — they relate to admission generally, not to the PISE application.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>York University</strong> in Toronto, Canada, offers the <strong>President’s International Scholarship of Excellence (PISE)</strong> to international high-school applicants entering the <strong>first year of a four-year undergraduate degree in Fall 2027</strong>. Each award is worth <strong>$45,000 CAD per year</strong> — up to <strong>$180,000 CAD over four years</strong> — renewable for a further three years of full-time study if the recipient maintains <strong>good academic standing</strong> each year. Recipients are drawn from a variety of regions and are called <strong>President’s International Scholars</strong>.</p>
      <p>Two things set this award apart. First, it is awarded on more than grades: you need a <strong>minimum 80% (A) final admission average</strong>, but also <strong>leadership skills and active involvement in volunteer work and extracurricular activities</strong>, and you must be <strong>officially nominated</strong> by a guidance counsellor, principal or senior school official — a maximum of two nominations per school per year. Second, the timing is forgiving in one respect and strict in another: <strong>no offer of admission is needed</strong> before you apply for the entrance award, but the scholarship form requires a <strong>9-digit York reference number</strong> issued after your admission application, so you must apply for admission well ahead of the <strong>27 January 2027</strong> scholarship deadline. And be clear about the money: $45,000 a year is a very large award, but it is a <strong>partial scholarship</strong>, not full funding — York states plainly that international scholarships are limited.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>international high-school applicant</strong> entering the <strong>first year of a four-year undergraduate degree</strong> at York in <strong>Fall 2027</strong>.</li>
        <li>Holds <strong>international student status</strong> and pays <strong>international tuition fees</strong>.</li>
        <li>Minimum final admission average of <strong>80% (A) or equivalent</strong>.</li>
        <li>Strong academic performance, plus <strong>leadership skills</strong> and active involvement in <strong>volunteer work and extracurricular activities</strong>.</li>
        <li><strong>Officially nominated</strong> by a guidance counsellor, principal or senior school official; a <strong>maximum of two nominations per school per year</strong>.</li>
        <li>Under York’s definition of a high-school applicant: <strong>under 21 by 31 December</strong> of the admission year, out of full-time high-school study for <strong>less than two years</strong> since graduation, and <strong>no studies attempted at an accredited college or university</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$45,000 CAD per year</strong>, up to <strong>$180,000 CAD over four years</strong>.</li>
        <li><strong>Renewable</strong> for a further three years of full-time undergraduate study, subject to <strong>good academic standing</strong> each year.</li>
        <li>Recipients are named <strong>President’s International Scholars</strong> and drawn from a variety of regions.</li>
        <li>No offer of admission is needed before applying for the entrance award.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>York University reference number</strong> (9 digits), obtained by first applying for undergraduate admission — it takes about <strong>5 business days</strong> to arrive.</li>
        <li>A <strong>personal statement, maximum 500 words</strong>, covering personal and professional goals, leadership, and volunteer/extracurricular commitment.</li>
        <li>A list of <strong>extracurricular activities and community involvement</strong> (maximum 3 entries).</li>
        <li>A list of <strong>previous awards</strong> (maximum 3 entries).</li>
        <li><strong>Contact details for the nominating guidance counsellor, principal or senior school official</strong>.</li>
        <li>An <strong>optional additional reference letter</strong> highlighting community involvement.</li>
        <li>A <strong>financial profile</strong> showing the estimated total funding available to support study over the next three to four years.</li>
        <li>From the nominator: <strong>confirmation of the nomination plus a reference letter</strong>, signed and on the school’s official letterhead, covering academic achievement and extracurricular/community contributions.</li>
        <li>Note: a CV, transcripts or an English-proficiency certificate are listed by some aggregator sites for a generic "York University Scholarship", but they <strong>do not appear in the official PISE guide</strong> — they relate to admission generally and should not be presented as PISE application documents.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to an undergraduate programme at York University for <strong>Fall 2027</strong>.</li>
        <li>Receive your <strong>9-digit York reference number</strong> (within about 5 business days of the admission application).</li>
        <li>When the scholarship application <strong>opens on 1 November 2026</strong>, log in with that reference number and complete the <strong>International Student Scholarship &amp; Award Application</strong>, including the personal statement, activity and award lists, nominator contact details, optional extra reference letter and financial profile.</li>
        <li>Submit by <strong>27 January 2027, 11:59 PM EST</strong>. No offer of admission is needed before applying for the entrance award.</li>
        <li>York emails the nominator a link to <strong>confirm the nomination and submit the reference letter</strong>, to be completed by <strong>4 February 2027, 11:59 PM EST</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the President’s International Scholarship of Excellence 2027?',
  'The student application is due 27 January 2027 at 11:59 PM EST, and the nominator’s confirmation and reference letter are due 4 February 2027 at 11:59 PM EST. Applications open 1 November 2026. Apply for admission well ahead of 27 January, since the scholarship form needs the York reference number issued after the admission application.'),
 ('How much is the President’s International Scholarship of Excellence worth?',
  '$45,000 CAD per year for up to four years — $180,000 CAD in total — renewable subject to good academic standing. It is a substantial partial scholarship, not full funding of all study costs.'),
 ('Who can apply for the President’s International Scholarship of Excellence?',
  'International high-school applicants entering the first year of a four-year undergraduate degree at York in Fall 2027, with a minimum 80% (A) final admission average, leadership skills and volunteer/extracurricular involvement, and nomination by a guidance counsellor, principal or senior school official (maximum two nominations per school per year).'),
 ('Do I need an offer of admission before applying for the PISE?',
  'No. No offer of admission is needed before applying for the entrance award. You do need the 9-digit York reference number, which is issued within about 5 business days of your admission application.'),
 ('What should the personal statement cover?',
  'A maximum of 500 words on your personal and professional goals, leadership, and volunteer/extracurricular commitment.'),
 ('How are PISE winners chosen?',
  'On academic strength (minimum 80% average), leadership and community involvement, and the nomination. Recipients are drawn from a variety of regions and are called President’s International Scholars.'),
 ('How many President’s International Scholarships are awarded each year?',
  'Not published in the official notification — York’s official pages say only "a select number". Secondary sites report 20 awards a year, but that figure was not confirmed on the official pages checked.'),
 ('What documents do I need for the PISE application?',
  'Your York reference number, a 500-word personal statement, lists of up to 3 extracurricular activities and up to 3 previous awards, your nominator’s contact details, an optional additional reference letter, and a financial profile. The nominator submits a confirmation and a reference letter on school letterhead. A CV, transcripts or an English-proficiency certificate do not appear in the official PISE guide.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against York University's official Future Students pages (futurestudents.yorku.ca — President's International Scholarship of Excellence application guides, and Scholarships, Awards and Bursaries for Incoming Students): President's International Scholarship of Excellence, Fall 2027 entry — $45,000 CAD per year, up to $180,000 CAD over four years, renewable subject to good academic standing; international high-school applicants entering the first year of a four-year undergraduate degree in Fall 2027; international student status, pays international tuition fees; minimum 80% (A) final admission average; leadership and volunteer/extracurricular involvement; nomination by a guidance counsellor, principal or senior school official (max two nominations per school per year); high-school applicant definition — under 21 by 31 December of the admission year, out of full-time high-school study less than two years since graduation, no studies attempted at an accredited college or university; application opens 1 November 2026; student deadline 27 January 2027, 11:59 PM EST; nominator confirmation and reference letter due 4 February 2027, 11:59 PM EST; 9-digit York reference number issued within about 5 business days of the admission application; no offer of admission needed before applying for the entrance award; personal statement max 500 words (goals, leadership, volunteer/extracurricular commitment), up to 3 extracurricular activities, up to 3 previous awards, nominator contact details, optional extra reference letter, financial profile; nominator reference letter signed and on school letterhead. CONFLICTS: (1) 27 Jan vs 26 Jan 2027 — the dedicated PISE guide and the page header say 27 January 2027; one table row on the general page says 26 January alongside an obvious typo ("January 26, 2026" in its note). Resolved for 27 January 2027, also given by Collegedunia, 9Scholarships and Shiksha. (2) A 1 April 2027 deadline on ScholarshipRoar describes a different York continuing-student award, not PISE. (3) A 1 October 2026 deadline on one secondary site is inconsistent with the official 2027 cycle (opens 1 November 2026). (4) 24 March 2027 (GlobalScholarships) is an admission deadline, not the PISE deadline. (5) "20 awards per year" on secondary sites is NOT confirmed on the official pages — not stated. (6) Renewal: official pages say only "good academic standing each year" — a secondary source's 24 credits / 6.0 GPA condition is not confirmed officially. (7) "Fully funded" is rejected — $45,000/year against international tuition and living costs, and York warns international scholarships are limited. (8) A Canadian study permit is mentioned by secondary sources but was not stated in the official PISE guide checked — not presented as a PISE condition. (9) CV, transcripts and English-proficiency certificate do not appear in the official PISE guide — they relate to admission generally, not the PISE application.</p>''',
 dl_long='27 January 2027, 11:59 PM EST (nominator deadline 4 February 2027; applications open 1 November 2026)',
 offlinks=[('York University — President’s International Scholarship of Excellence, application guides (official)', 'https://futurestudents.yorku.ca/presidents-international-scholarship-excellence-application-guides'),
           ('York University — Scholarships, Awards and Bursaries for Incoming Students (official)', 'https://futurestudents.yorku.ca/scholarships-incoming-students'),
           ('Bright Scholarship — York University Scholarships 2026 in Canada', 'https://brightscholarship.com/york-university-scholarships-2026-in-canada/')],
 related_titles=['ucalgary-2027', 'trent-2027', 'cbu-2027', 'ogs-2027'])),

# ---------------------------------------------------------------- 3. University of Tsukuba MEXT Scholarship
A.append(dict(
 slug='university-of-tsukuba-mext-scholarship-2027-japan',
 title='University of Tsukuba MEXT Scholarship 2027 in Japan (Fully Funded)',
 meta='University of Tsukuba MEXT Scholarship 2027: full tuition exemption, round-trip airfare and a monthly stipend for study at the University of Tsukuba. The University Recommendation General Program is expected to be discontinued from 2027 — only Special Programs continue, each with its own deadline.',
 short='University of Tsukuba MEXT Scholarship 2027', kicker='Japan · Master’s & PhD · Fully Funded', mono='UT',
 prov_short='University of Tsukuba', prov_cat='University · Japan',
 h1='University of Tsukuba MEXT Scholarship 2027 in Japan (Fully Funded)',
 sub='Read this first, because this scholarship has changed since most of the listings about it were written — and the change decides whether you can apply at all. The University of Tsukuba MEXT Scholarship is real, funded by Japan’s Ministry of Education (MEXT), and it covers full tuition, round-trip airfare and a monthly stipend. But the route most older listings describe — the University Recommendation General Program, with a November–December application window — is expected to be discontinued from the 2027 academic year, according to the university’s own MEXT page, updated in September 2026. Only the Special Program route continues, programme by programme, each with its own deadline. The embassy route, meanwhile, has largely closed for 2027 entry. So there is no single deadline for this award any more — this article explains the routes that are actually open and the ones that are not.',
 dpill='Deadlines vary by programme — check the programme page',
 facts=facts([('Award', 'Full tuition exemption, round-trip airfare to and from Japan, and a monthly stipend of approximately ¥117,000 for undergraduates, ¥144,000 for Master’s students and ¥145,000 for doctoral students (a preparatory/research rate of about ¥143,000 is also reported). Accommodation and living support and medical/health coverage are also reported. These are the standard MEXT rates as reported by several independent sources, including the Embassy of Japan in India’s published 2027 terms — the University of Tsukuba’s own MEXT page does not state stipend figures, and the 2027 MEXT guidelines had not yet been published at the time of checking (expected around December 2026), so amounts remain subject to confirmation.'),
              ('Eligible', 'Nationality of a country that has diplomatic relations with Japan; in principle, holders of Japanese nationality at the time of application are not eligible (dual nationals living outside Japan may qualify if they choose the foreign nationality and give up Japanese nationality before arrival). Strong academic record: a grade point average of at least 2.30 on a 3.00 scale at the previous school, to be maintained during the scholarship period. Age (graduate route): born on or after 2 April 1992 — under 35 — with only narrow MEXT-recognised exceptions (such as military service or loss of study opportunities due to war). For a Master’s: a Bachelor’s degree (16 years of education) completed or expected by March 2027. For a doctorate: a Master’s degree or equivalent completed or expected by March 2027. Language: Japanese at JLPT N2 level or higher, or English at CEFR B2 level or higher (all four skills), by the time of enrolment; or completion of a prior degree taught in the relevant language. Physically and mentally fit to study at a university in Japan; applicants must commit to enrolling at the University of Tsukuba if accepted, and are subject to the university’s security export-control screening.'),
              ('How', 'Embassy Recommendation route: apply through the Japanese embassy or consulate in your own country and pass its first screening; then request a Letter of Provisional Acceptance from the University of Tsukuba, submit it to the embassy, and await MEXT’s second screening and final result. For 2027 entry this route is now closed in most countries. University Recommendation, Special Program route (the route that continues for 2027): identify an eligible Special Program, read that programme’s own guideline, contact a prospective academic supervisor in advance and obtain their consent, pass the programme’s entrance examination, and submit the MEXT scholarship documents by the programme’s stated deadline. MEXT makes the final decision (expected around early March 2027 for the Materials Innovation programme); enrolment is in April 2027 (Materials Innovation) or October 2027 (some other programmes). The General Program route is expected to be discontinued for 2027 — do not present it as available.'),
              ('Deadline', 'No single published deadline. Embassy Recommendation: deadlines are set separately by each Japanese embassy or consulate and have largely already passed for 2027 entry (for example, the Embassy of Japan in India set 15 May 2026 for research students and 25 May 2026 for undergraduates; the University of Tsukuba’s deadline to request a Letter of Provisional Acceptance was 1 September 2026). University Recommendation, Special Program: deadlines are set programme by programme — for example, the Materials Innovation special entrance examination closed for applications on 3 September 2026 at 5:00 p.m. JST, with its scholarship-document deadline for recommended candidates in early December 2026 (exact date to be announced). The 2027 MEXT guidelines were still to be published at the time of checking.'),
              ('Fine print', 'The General Program November–December window shown in older listings (published June 2026) should not be relied on — the university’s official MEXT page, updated September 2026, says General Program recruitment is expected to be discontinued from the 2027 academic year and only the Special Program will continue. Undergraduate entry exists only through selected Special Programs, not generally. The widely repeated "under 25 for undergraduates" age limit was not confirmed in the official Tsukuba documents opened, so it is not stated here. Stipend figures are standard MEXT rates as reported, not figures published by the University of Tsukuba.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Tsukuba MEXT Scholarship</strong> is a Japanese Government (MEXT) scholarship for study at the <strong>University of Tsukuba</strong>, funded by Japan’s Ministry of Education, Culture, Sports, Science and Technology. The award is <strong>fully funded</strong> in the usual MEXT sense: <strong>full tuition exemption</strong>, <strong>round-trip airfare</strong> to and from Japan, and a <strong>monthly stipend</strong> of approximately <strong>¥117,000 for undergraduates, ¥144,000 for Master’s students and ¥145,000 for doctoral students</strong>, with accommodation and living support and medical/health coverage also reported. One caveat on the numbers: the University of Tsukuba’s own MEXT page does not state stipend figures — these are the standard MEXT rates as reported by several independent sources, including the Embassy of Japan in India’s published 2027 terms, and the 2027 MEXT guidelines had not yet been published at the time of checking.</p>
      <p>The important change is the route. MEXT scholarships at Tsukuba run through two channels: <strong>Embassy Recommendation</strong> (apply through the Japanese embassy in your own country) and <strong>University Recommendation</strong>. For 2027 entry the embassy route has <strong>largely closed</strong> — embassy deadlines vary by country and most have passed, and Tsukuba’s deadline to request a Letter of Provisional Acceptance was <strong>1 September 2026</strong>. On the university side, the <strong>General Program</strong> — the route older listings describe, with a November–December window — is <strong>expected to be discontinued from the 2027 academic year</strong>, per the university’s official MEXT page updated in September 2026. What continues is the <strong>Special Program</strong> route: individual programmes such as Materials Innovation and Multimodal Biomedicine run their own entrance examinations and their own timetables. There is therefore <strong>no single deadline</strong> for this award — you must check the specific programme page.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Nationality of a <strong>country that has diplomatic relations with Japan</strong>; in principle, holders of <strong>Japanese nationality</strong> at the time of application are not eligible (dual nationals living outside Japan may qualify if they choose the foreign nationality and give up Japanese nationality before arrival).</li>
        <li>Strong academic record: a grade point average of at least <strong>2.30 on a 3.00 scale</strong> at the previous school, to be maintained during the scholarship period.</li>
        <li>Age (graduate route): born on or after <strong>2 April 1992</strong> — under 35 — with only narrow MEXT-recognised exceptions (such as military service or loss of study opportunities due to war).</li>
        <li>For a <strong>Master’s</strong>: a <strong>Bachelor’s degree (16 years of education)</strong> completed or expected by <strong>March 2027</strong>. For a <strong>doctorate</strong>: a <strong>Master’s degree or equivalent</strong> completed or expected by <strong>March 2027</strong>.</li>
        <li>Language: <strong>Japanese at JLPT N2 level or higher</strong>, or <strong>English at CEFR B2 level or higher (all four skills)</strong>, by the time of enrolment; or completion of a prior degree taught in the relevant language.</li>
        <li><strong>Physically and mentally fit</strong> to study at a university in Japan; applicants must <strong>commit to enrolling at the University of Tsukuba</strong> if accepted, and are subject to the university’s <strong>security export-control screening</strong>.</li>
        <li>Note: undergraduate entry exists <strong>only through selected Special Programs</strong>, not generally — and the widely repeated "under 25 for undergraduates" age limit was not confirmed in the official Tsukuba documents opened, so it is not stated here.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition exemption</strong>.</li>
        <li><strong>Round-trip airfare</strong> to and from Japan.</li>
        <li>A <strong>monthly stipend</strong> of approximately <strong>¥117,000 (undergraduate), ¥144,000 (Master’s) or ¥145,000 (doctoral)</strong> — the standard MEXT rates as reported; the University of Tsukuba page does not state figures, and the 2027 guidelines were still to be published at the time of checking.</li>
        <li><strong>Accommodation and living support</strong> and <strong>medical/health coverage</strong> are also reported.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>For the University Recommendation, Special Program route (Materials Innovation guideline): the <strong>application form on the prescribed form</strong>, plus an <strong>application checklist</strong>.</li>
        <li><strong>Academic transcript</strong> for each year of the last university attended, with an official document explaining the grading system if it is not shown on the transcript.</li>
        <li><strong>Graduation/degree certificate</strong> (or certificate of expected graduation).</li>
        <li>A <strong>summary of research and future research plans</strong>, in English on the designated form.</li>
        <li><strong>Language proficiency evidence</strong> (JLPT N2 certificate, or a four-skill English test score at CEFR B2 or higher).</li>
        <li>An <strong>examination admission slip</strong> with a recent photograph (4.5 × 3.5 cm, taken within the last six months).</li>
        <li>A <strong>letter of approval</strong> from the head of your current university/department (or employer) if currently enrolled or employed.</li>
        <li>For the general MEXT application, secondary sources consistently also list: the <strong>MEXT application form</strong>, <strong>passport or national ID</strong>, <strong>letters of recommendation</strong> (the dean or president of your university, addressed to the President of the University of Tsukuba), a <strong>field-of-study/research plan</strong>, a <strong>medical certificate</strong>, a <strong>CV</strong>, and a <strong>thesis abstract</strong> where applicable. These general-list items were not all confirmed in the official documents opened, so the article presents the programme-specific list above as confirmed and the wider MEXT list as the usual requirement.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Embassy Recommendation route (now closed for most countries for 2027):</strong> apply through the Japanese embassy or consulate in your own country and pass its first screening; then request a <strong>Letter of Provisional Acceptance</strong> from the University of Tsukuba, submit it to the embassy, and await MEXT’s second screening and final result.</li>
        <li><strong>University Recommendation, Special Program route (the route that continues for 2027):</strong> identify an <strong>eligible Special Program</strong> at the University of Tsukuba and read that programme’s own guideline.</li>
        <li>Contact a <strong>prospective academic supervisor</strong> in advance and obtain their consent to the application.</li>
        <li>Pass that programme’s <strong>entrance examination</strong> (for example, document screening plus an oral examination).</li>
        <li>Candidates who pass and are selected for recommendation submit the <strong>MEXT scholarship documents</strong> by the programme’s stated deadline (early December 2026, exact date to be announced, in the Materials Innovation case).</li>
        <li>MEXT makes the <strong>final decision</strong> (expected around early March 2027 for that programme); enrolment is in <strong>April 2027</strong> (Materials Innovation) or <strong>October 2027</strong> (some other programmes).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Tsukuba MEXT Scholarship 2027?',
  'There is no single published deadline. Embassy-route deadlines vary by country and have largely passed for 2027 entry (for example, the Embassy of Japan in India set 15 May 2026 for research students; Tsukuba’s deadline to request a Letter of Provisional Acceptance was 1 September 2026). University Recommendation now runs only through individual Special Programs, each with its own timetable — for example, the Materials Innovation entrance examination closed on 3 September 2026, with its scholarship-document deadline in early December 2026. Check the specific programme page.'),
 ('Is the University of Tsukuba MEXT Scholarship General Program still open?',
  'No — or rather, it should not be treated as open. The university’s official MEXT page, updated in September 2026, says General Program recruitment is expected to be discontinued from the 2027 academic year, with only the Special Program continuing. Older listings showing a November–December 2026 window are out of date.'),
 ('How much is the University of Tsukuba MEXT Scholarship worth?',
  'Full tuition exemption, round-trip airfare and a monthly stipend of about ¥117,000 (undergraduate), ¥144,000 (Master’s) or ¥145,000 (doctoral). These are the standard MEXT rates as reported by several independent sources; the University of Tsukuba page does not state figures, and the 2027 MEXT guidelines had not yet been published at the time of checking.'),
 ('Who can apply for the University of Tsukuba MEXT Scholarship?',
  'Nationals of countries with diplomatic relations with Japan, with a GPA of at least 2.30 on a 3.00 scale, under 35 for the graduate route (born on or after 2 April 1992), a Bachelor’s degree for a Master’s or a Master’s degree for a doctorate (completed or expected by March 2027), and Japanese at JLPT N2 or English at CEFR B2 (all four skills) by enrolment.'),
 ('How do I apply for the University of Tsukuba MEXT Scholarship?',
  'Through the Embassy Recommendation route (apply via the Japanese embassy in your country — now largely closed for 2027) or the University Recommendation Special Program route: pick an eligible Special Program, read its guideline, contact a prospective supervisor, pass the programme’s entrance examination, and submit the MEXT documents by the programme’s deadline.'),
 ('Can undergraduates apply for the University of Tsukuba MEXT Scholarship?',
  'Only through selected Special Programs — undergraduate entry is not generally available. The widely repeated "under 25" age limit for undergraduates was not confirmed in the official Tsukuba documents opened.'),
 ('What documents do I need for the University of Tsukuba MEXT Scholarship?',
  'For the Special Program route: the prescribed application form and checklist, transcripts with a grading-system explanation, graduation or expected-graduation certificate, a research summary and future plans, language-proficiency evidence, an examination admission slip with a recent photo, and a letter of approval from your current university or employer. The wider MEXT list (MEXT form, passport, recommendation letters, research plan, medical certificate, CV, thesis abstract) is the usual requirement.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the University of Tsukuba's official MEXT scholarship page (tsukuba.ac.jp/en/admissions/financial-scholarships/mext/, updated September 2026) and its published 2027 programme guidelines (Materials Innovation special entrance examination; Multimodal Biomedicine), with award figures cross-checked against several independent sources including the Embassy of Japan in India's published 2027 terms. There is no single published deadline: embassy-route deadlines vary by country and have largely passed for 2027 entry (Embassy of Japan in India: 15 May 2026 research students, 25 May 2026 undergraduates; Tsukuba's Letter of Provisional Acceptance request deadline 1 September 2026), while the university route now runs only through individual Special Programs, each with its own timetable (Materials Innovation entrance applications closed 3 September 2026 at 5:00 p.m. JST; oral examinations 8 and 13-15 October 2026; results 30 October 2026; scholarship-document deadline for recommended candidates early December 2026, exact date to be announced; MEXT final decision expected around early March 2027; enrolment April 2027, or October 2027 for some programmes). MATERIAL CORRECTION: the university announced in September 2026 that the University Recommendation General Program is expected to be discontinued from the 2027 academic year, with only the Special Program continuing — the November-December window shown in older listings (Bright Scholarship and others, published June 2026) should not be relied on, and the 2027 MEXT guidelines were still to be published at the time of checking (expected around December 2026). CONFLICTS: (1) General Program November-December window vs discontinuation — resolved in favour of the official university page, the newer primary source. (2) Undergraduate availability — aggregators describe the award as open to bachelor's, master's and PhD generally; the official material is narrower — bachelor's places exist only through selected Special Programs. (3) Stipend figures (¥117,000 / ¥144,000 / ¥145,000, preparatory/research rate about ¥143,000) are consistent across multiple independent secondary sources and match the Embassy of Japan in India's published 2027 terms, but do not appear on the University of Tsukuba's MEXT page — treated as confirmed by multiple secondary sources with the attribution caveat. (4) A DAAD Scholarships page mixing this award with unrelated Tsukuba scholarships and other deadlines was disregarded. (5) Programme-specific vs general deadlines: the Materials Innovation deadline (3 September 2026, already passed) does not contradict the general November-December window claimed by aggregators — they describe different routes; the article keeps the routes separate and never presents one programme's date as the scholarship's deadline. Eligibility confirmed in the official 2027 programme guidelines: nationality of a country with diplomatic relations with Japan (Japanese nationals in principle not eligible; dual nationals living outside Japan may qualify if they choose the foreign nationality and give up Japanese nationality before arrival); GPA at least 2.30/3.00; age under 35 for the graduate route (born on or after 2 April 1992, narrow MEXT-recognised exceptions); Master's needs a Bachelor's (16 years of education) completed or expected by March 2027, doctorate needs a Master's by March 2027; JLPT N2 or English CEFR B2 (all four skills) by enrolment, or a prior degree taught in the relevant language; physically and mentally fit; commit to enrolling at Tsukuba; security export-control screening. The "under 25 for undergraduates" age limit was not confirmed in the official documents opened and is not stated.</p>''',
 dl_long='No single deadline — embassy route largely closed for 2027; Special Program deadlines vary by programme (check the programme page)',
 offlinks=[('University of Tsukuba — Japanese Government (MEXT) Scholarship (official)', 'https://www.tsukuba.ac.jp/en/admissions/financial-scholarships/mext/'),
           ('University of Tsukuba — 2027 Application Guidelines, Materials Innovation (official PDF)', 'https://grad.pas.tsukuba.ac.jp/content/uploads/sites/8/2026/06/Application-Guidelines.pdf'),
           ('University of Tsukuba — 2027 Application Guideline, MEXT Scholarship, Multimodal Biomedicine (official PDF)', 'https://www.md.tsukuba.ac.jp/FrontierSite/data/examination/01_Application_Guideline_MEXT_SCHOLARSHIP_PROGRAM_2027.pdf'),
           ('Bright Scholarship — University of Tsukuba MEXT Scholarship 2027', 'https://brightscholarship.com/university-of-tsukuba-mext-scholarship-2027/')],
 related_titles=['saitama-mext-2027', 'u-tokyo-mext', 'apu-mext-2027', 'science-tokyo'])),

# ---------------------------------------------------------------- 4. Duke University Karsh Scholarship
A.append(dict(
 slug='duke-university-karsh-scholarship-2026-usa',
 title='Duke University Karsh Scholarship 2026 in USA (Fully Funded)',
 meta='Duke University Karsh Scholarship 2026: fully funded undergraduate study at Duke for international students with demonstrated financial need — tuition, room and board, fees and three funded summers. Early Decision deadline 2 November 2026; Regular Decision 4 January 2027.',
 short='Duke University Karsh Scholarship 2026', kicker='USA · Undergraduate · Fully Funded', mono='DU',
 prov_short='Duke University', prov_cat='University · USA',
 h1='Duke University Karsh Scholarship 2026 in USA (Fully Funded)',
 sub='Read this first, because the Karsh Scholarship works differently from most scholarships on this site — and the difference decides how you apply. There is no separate Karsh application. You apply to Duke University for undergraduate admission through the Common Application and request financial aid in that same first-year application; eligible applicants are then considered automatically for Karsh during the admissions process. The other thing to get right is the deadline: this is the 2026–27 admissions cycle for entry in autumn 2027 (Duke’s Class of 2031), and there are two routes — Early Decision, closing 2 November 2026, and Regular Decision, closing 4 January 2027. The "1 November" date on many aggregator sites is carried over from an earlier cycle and is not Duke’s current date.',
 dpill='Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
 facts=facts([('Award', 'Fully funded for up to four years of full-time undergraduate study: full tuition, room and board, mandatory university fees, demonstrated financial need beyond those costs, and funding for three summers, for research, unpaid internships and other opportunities that advance the scholar’s academic career. Duke publishes no single cash figure, so none is stated here — a laptop, a living allowance, travel costs or a total dollar value are not confirmed by Duke and are not claimed.'),
              ('Eligible', 'International applicants who are citizens of a country outside the United States; not a US citizen and not a dual US / other-country citizen. Applying as an incoming first-year undergraduate at Duke. Must not already hold a BA or BS degree before enrolling. Strong academic preparation and demonstrated financial need, with a financial-aid application submitted to Duke. Open to students in any academic field or major.'),
              ('How', 'There is no separate Karsh application. Apply to Duke for undergraduate admission through the Common Application (QuestBridge is also named as a route where eligible) and request financial aid in that original first-year application, completing the required financial-aid forms. Eligible applicants are then considered automatically for Karsh during the admissions process.'),
              ('Deadline', 'Early Decision: 2 November 2026 — application, Early Decision Agreement, transcript, first-quarter grades, Secondary School Report with counsellor recommendation, two teacher recommendations, and financial-aid applications (CSS Profile and FAFSA) all due 2 November; additional financial-aid documents by 15 November; decisions mid-December. Regular Decision: 4 January 2027 — application and supporting documents due 4 January; decisions late March / early April 2027. As of 28 October 2026 the Early Decision route closes in five days.'),
              ('Fine print', 'The widely repeated "1 November 2026" date on aggregator sites (including the queue’s source page) is not supported by Duke’s own current admissions page — Duke gives 2 November for Early Decision, corroborated by 2026–27 cycle guides. A "4 November 2026" date on one site is the Round 1 deadline for a Duke Fuqua graduate programme, not undergraduate admission. The number of awards is not published by Duke — secondary estimates of roughly 18–25 a year circulate, but one figure belongs to the separate Robertson programme, so no number is stated. One aggregator page contradicts itself on the BA/BS rule; Duke’s rule (no prior BA/BS) stands.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Karsh International Scholars Program</strong> at <strong>Duke University</strong> is a fully funded undergraduate scholarship for <strong>international students with demonstrated financial need</strong>. It covers <strong>full tuition for up to four years</strong> of full-time undergraduate study, <strong>room and board</strong>, <strong>mandatory university fees</strong>, <strong>demonstrated financial need beyond those costs</strong>, and <strong>funding for three summers</strong> — for research, unpaid internships and other opportunities that advance the scholar’s academic career. It is open to students in <strong>any academic field or major</strong>.</p>
      <p>The key fact about Karsh is that there is <strong>no separate application</strong>. You apply to Duke for undergraduate admission through the <strong>Common Application</strong> and request financial aid in that same first-year application; eligible applicants are then considered automatically for Karsh during the admissions process. That means the Karsh "deadline" is really Duke’s admissions deadline, and there are two of them: <strong>Early Decision on 2 November 2026</strong> and <strong>Regular Decision on 4 January 2027</strong>. This is the <strong>2026–27 admissions cycle for entry in autumn 2027</strong> (Duke’s Class of 2031), which is why several current sources label the same award "2027" — the "2026" in the queue title refers to the application year, not the entry year. If you are reading this close to 2 November, do not leave it to the last day: older listings still show 1 November, and Duke’s current date is the 2nd.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>international applicant</strong> who is a <strong>citizen of a country outside the United States</strong>.</li>
        <li><strong>Not a US citizen</strong> and <strong>not a dual US / other-country citizen</strong>.</li>
        <li>Applying as an <strong>incoming first-year undergraduate</strong> at Duke.</li>
        <li>Must <strong>not already hold a BA or BS degree</strong> before enrolling.</li>
        <li><strong>Strong academic preparation</strong>.</li>
        <li><strong>Demonstrated financial need</strong>, with a financial-aid application submitted to Duke.</li>
        <li>Open to students in <strong>any academic field / major</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition</strong> for up to four years of full-time undergraduate study.</li>
        <li><strong>Room and board</strong>.</li>
        <li><strong>Mandatory university fees</strong>.</li>
        <li><strong>Demonstrated financial need beyond those costs</strong>.</li>
        <li><strong>Funding for three summers</strong>, for research, unpaid internships and other opportunities that advance the scholar’s academic career.</li>
        <li>No separate Karsh application — consideration is automatic once you apply to Duke and request financial aid.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>Common Application</strong>, including the personal essay and Duke short responses.</li>
        <li>An <strong>official high-school transcript</strong>.</li>
        <li>The <strong>Secondary School Report with counsellor recommendation</strong>.</li>
        <li><strong>Two teacher recommendations</strong> from major academic subjects.</li>
        <li><strong>First-quarter grades</strong> (Early Decision applicants).</li>
        <li>A <strong>midyear grade report</strong> when available.</li>
        <li>The <strong>US$85 application fee</strong>, or an approved fee-waiver request.</li>
        <li>The <strong>CSS Profile</strong> for international applicants requesting financial aid (Duke’s Early Decision list also names FAFSA under financial-aid applications; the CSS Profile is the form international applicants use to evidence need).</li>
        <li><strong>Tax, income or other financial documents</strong> if Duke or the College Board requests them.</li>
        <li>Translated transcripts must be submitted with <strong>both the original and an English translation</strong>, where translation is needed.</li>
        <li>Note: <strong>SAT / ACT scores are optional</strong> for the 2026–27 cycle. An English-proficiency test is <strong>recommended but not required</strong> for non-native speakers or students not studying in an English-medium curriculum.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply to Duke</strong> for undergraduate admission through the <strong>Common Application</strong> (QuestBridge is also named as a route where eligible).</li>
        <li><strong>Request financial aid</strong> in that original first-year application, completing the required financial-aid forms (CSS Profile and, per Duke’s list, FAFSA).</li>
        <li>There is <strong>no separate Karsh application</strong> — eligible applicants are considered <strong>automatically</strong> for Karsh during the admissions process.</li>
        <li>Meet the deadline for your route: <strong>Early Decision, 2 November 2026</strong> (additional financial-aid documents by 15 November; decisions mid-December) or <strong>Regular Decision, 4 January 2027</strong> (decisions late March / early April 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Duke Karsh Scholarship 2026?',
  'Early Decision: 2 November 2026. Regular Decision: 4 January 2027. The widely repeated 1 November 2026 date on aggregator sites is carried over from an earlier cycle and is not Duke’s current date — use 2 November.'),
 ('Is there a separate application for the Karsh Scholarship?',
  'No. You apply to Duke for undergraduate admission through the Common Application and request financial aid in that same first-year application. Eligible applicants are then considered automatically for Karsh during the admissions process.'),
 ('What does the Karsh Scholarship cover?',
  'Full tuition for up to four years, room and board, mandatory university fees, demonstrated financial need beyond those costs, and funding for three summers of research or internships. Duke publishes no single cash figure, and a laptop, living allowance or travel costs are not confirmed by Duke.'),
 ('Who can apply for the Karsh Scholarship?',
  'International applicants who are citizens of a country outside the United States, are not US citizens or dual US citizens, are applying as incoming first-year undergraduates, do not already hold a BA or BS degree, have strong academic preparation and demonstrated financial need. Any major.'),
 ('Is the Karsh Scholarship for 2026 or 2027 entry?',
  'This is the 2026–27 admissions cycle for entry in autumn 2027 (Duke’s Class of 2031). The "2026" in the title refers to the application year, not the entry year.'),
 ('Do I need SAT or ACT scores for Duke Karsh?',
  'No — SAT / ACT scores are optional for the 2026–27 cycle. An English-proficiency test is recommended but not required for non-native speakers or students not studying in an English-medium curriculum.'),
 ('How many Karsh Scholarships are awarded each year?',
  'Not published by Duke. Secondary estimates of roughly 18–25 a year circulate, but one figure belongs to the separate Robertson programme, so no number is stated here.'),
 ('What documents do I need for Duke Karsh?',
  'The Common Application with personal essay and Duke short responses, official high-school transcript, Secondary School Report with counsellor recommendation, two teacher recommendations, first-quarter grades (Early Decision), a midyear grade report when available, the US$85 application fee or a fee waiver, and the CSS Profile for financial aid, plus tax/income documents if requested.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against Duke University's own pages: the Karsh International Scholars Program page (Office of University Scholars and Fellows, ousf.duke.edu) confirms the award is for international first-year undergraduates with demonstrated financial need, covers tuition, room and board, mandatory fees, need beyond those costs and three summers of funded research or internship experience, and requires no separate application beyond applying to Duke and requesting financial aid; Duke Undergraduate Admissions (admissions.duke.edu/apply/) confirms the 2026-27 cycle deadlines of 2 November 2026 for Early Decision and 4 January 2027 for Regular Decision (Early Decision: application, Early Decision Agreement, transcript, first-quarter grades, Secondary School Report with counsellor recommendation, two teacher recommendations, financial-aid applications — CSS Profile and FAFSA — all due 2 November; additional financial-aid documents by 15 November; decisions mid-December. Regular Decision: application and supporting documents due 4 January; decisions late March / early April 2027). Eligibility: international applicant, citizen of a country outside the US, not a US citizen and not a dual US / other-country citizen, incoming first-year undergraduate, must not already hold a BA or BS degree, strong academic preparation, demonstrated financial need with a financial-aid application submitted to Duke, open to any major. Documents per Duke Undergraduate Admissions for first-year applicants 2026-27: Common Application with personal essay and Duke short responses, official high-school transcript, Secondary School Report with counsellor recommendation, two teacher recommendations from major academic subjects, first-quarter grades (Early Decision), midyear grade report when available, US$85 application fee or approved fee waiver, CSS Profile for international applicants requesting financial aid, tax/income or other financial documents if requested, translated transcripts with original and English translation. SAT/ACT optional for 2026-27; English-proficiency test recommended but not required for non-native speakers or students not studying in an English-medium curriculum. CONFLICTS: (1) 1 November vs 2 November 2026 — Bright Scholarship, Eduspur, EngineersJob and other aggregators give 1 November; Duke's own admissions page for the 2026-27 cycle gives 2 November for Early Decision, corroborated by IvyWise, College Confidential's Class of 2031 thread and other 2026-27 cycle guides. Resolved in favour of Duke: 2 November 2026 (Early Decision). The 1 November figure looks carried over from an earlier cycle. (2) 4 November 2026 (GlobalScholarships) — no other source corroborates this for undergraduate admission; 4 November 2026 is the Round 1 deadline for a Duke Fuqua graduate programme, so this appears to be a mix-up. Discarded. (3) Bright Scholarship contradicts itself on the BA/BS rule — its eligibility list correctly says applicants "cannot have a BA or BSc degree already", then a later line says eligible students are "those who already hold a B.A. or B.S. degree". Discarded as a copy error; Duke's rule (no prior BA/BS) stands. (4) Number of awards — secondary estimates of roughly 18-25 a year circulate, but one figure belongs to the Robertson programme and the other is an estimate of need-met international enrolments, not a Karsh quota. Duke publishes no number — stated as not published. (5) Laptop / living allowance / total value — claimed by some aggregators, absent from Duke's Karsh page, which lists only tuition, room and board, mandatory fees, demonstrated need beyond those costs, and three summers of funding. Not confirmed — omitted. One aggregator claims a figure above $350,000 over four years — single-source, not Duke-published, and on a page that confuses Karsh with the separate Robertson programme; omitted.</p>''',
 dl_long='Early Decision: 2 November 2026 · Regular Decision: 4 January 2027',
 offlinks=[('Duke University — Karsh International Scholars Program (official)', 'https://ousf.duke.edu/merit-scholarships/karsh-international-scholars-program/'),
           ('Duke Undergraduate Admissions — Apply (official)', 'https://admissions.duke.edu/apply/'),
           ('Bright Scholarship — Duke University Karsh Scholarship 2026', 'https://brightscholarship.com/duke-university-karsh-scholarship-2026/')],
 related_titles=['york-pise-2027', 'ucalgary-2027', 'trent-2027', 'nyt-fellowship'])),

# ---------------------------------------------------------------- 5. EPFL CYD Fellowship
A.append(dict(
 slug='epfl-cyd-fellowship-2027-switzerland',
 title='EPFL CYD Fellowship 2027 in Switzerland (Fully Funded)',
 meta='EPFL CYD Fellowship 2027: the 15th call for Doctoral and Distinguished Postdoctoral fellowships opens 3 December 2026, Stage 1 deadline 25 February 2027. Master Thesis fellowships run on a rolling call. Any nationality, no age limit.',
 short='EPFL CYD Fellowship 2027', kicker='Switzerland · Master’s, PhD & Postdoc · Fully Funded', mono='CY',
 prov_short='EPFL / CYD Campus', prov_cat='University · Switzerland',
 h1='EPFL CYD Fellowship 2027 in Switzerland (Fully Funded)',
 sub='Read this first, because the deadline most listings show for this fellowship is already gone — and the real one has not opened yet. The queue’s "August 2026" deadline was the now-closed 14th call of the EPFL CYD Fellowships. The official EPFL pages state that the 15th call for Doctoral and Distinguished Postdoctoral fellowships opens on 3 December 2026, with a Stage 1 deadline of 25 February 2027 at 17:00 CET. The Master Thesis strand is different again: it runs on a rolling call with no fixed deadline. This article is about the 15th call — the live opportunity — and it uses only the dates and figures on the official EPFL pages, because the aggregator totals floating around for this fellowship are not published by EPFL.',
 dpill='Deadline 25 Feb 2027 · %d days left' % dl_left('2027-02-25'),
 facts=facts([('Award', 'Master Thesis: a living allowance of CHF 2,500 per month for a maximum of 6 months, plus up to CHF 1,500 for research costs. Doctoral: a salary contribution (including social security benefits, set by the host institution’s salary scale — no fixed figure is published) plus up to CHF 3,000 per year for research costs and up to CHF 5,000 per year for conference costs, for 4 years with a possible one-year extension. Distinguished Postdoctoral: a salary contribution on the same basis, plus the same CHF 3,000/year research and CHF 5,000/year conference caps, for up to 2 years. No single lump-sum total is published by EPFL for the doctoral/postdoctoral strands, and the salary figure itself is not published — only the scale basis. The research/conference caps apply to specific equipment and conference costs only, not general IT material.'),
              ('Eligible', 'Citizens of any nationality may apply; no age restrictions apply. Excellence is the primary selection criterion, judged on academic records and professional accomplishments; strong grade transcripts are expected. Master Thesis: must be enrolled in a Master’s programme at a Swiss higher education institution (university or school of applied sciences) and have the endorsement of a professor/supervisor employed there. Doctoral: must be enrolled in a doctoral programme at a Swiss higher education institution and have a supervising professor’s endorsement by the Stage 2 application. Applicants endorsed by a professor at a school of applied sciences must also provide written confirmation at Stage 2 of simultaneous enrolment in a doctoral programme at a Swiss university. Preference is given to applicants who have not yet started, or are at the beginning of, their PhD. Funding for less than four years may be requested if that matches the thesis completion date. Distinguished Postdoctoral: must have the endorsement of a professor employed at a Swiss higher education institution by the Stage 2 application, and the funded postdoctoral research must be carried out in a different laboratory from the applicant’s doctoral laboratory and any current postdoctoral laboratory. Research must engage with cyber-defence themes: protection of confidentiality, integrity and availability of cyber and cyber-physical systems; information sharing, data fusion and crowdsourcing; data science and AI methods for cyber-relevant data; and security, privacy and digital trust technologies. Applicants must show their project can significantly influence security/data-science research and Swiss cyber-defence, and that it brings together CYD Campus researchers and at least one Swiss higher education institution.'),
              ('How', '1) Read the official call guidelines and the application toolkit on the EPFL CYD Fellowships page (15th-call versions from 3 December 2026). 2) Check the list of prioritised topics in the call guidelines and align the proposal with them; Master Thesis applicants may pick a listed CYD Campus topic or propose their own. 3) Secure hosting/endorsement from a professor at a Swiss higher education institution (needed by Stage 2 for doctoral/postdoctoral applicants). 4) Prepare and submit all documents in English through the official online submission platform before the Stage 1 deadline. 5) Selection runs in two stages: Stage 1 screening by a CYD Campus internal committee, after which shortlisted applicants are assigned a prospective CYD Campus mentor who interviews them and must endorse them for Stage 2; Stage 2 requires a full research proposal, with final decisions by a committee chaired by the Director of the CYD Campus.'),
              ('Deadline', 'Doctoral and Distinguished Postdoctoral (15th call): 25 February 2027, 17:00 CET (Stage 1). The call opens 3 December 2026. Master Thesis: rolling call — no fixed deadline; applications may be submitted throughout the year. The 14th call is closed; as of 28 October 2026 the 15th call is not yet open.'),
              ('Fine print', 'The exact document checklist is not published in detail on the EPFL pages checked — the official pages state only that all required documents must be submitted in English via the online submission platform, and direct applicants to read the call guidelines and the application toolkit. The toolkit currently linked is for the 14th call; EPFL states the updated documents for the 15th call will be available when it opens on 3 December 2026. No itemised document checklist should be printed as fact — the exact document list is in the official toolkit/guidelines. One secondary source suggests some projects may carry nationality restrictions; this does not appear on the official EPFL pages, which state any nationality may apply, so it is not confirmed and is not stated as a rule.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>CYD Fellowships</strong>, run by <strong>EPFL</strong> with the <strong>CYD Campus</strong>, fund research in cyber-defence at a Swiss higher education institution. There are <strong>three strands</strong>: <strong>Master Thesis</strong>, <strong>Doctoral</strong> and <strong>Distinguished Postdoctoral</strong>. The Master Thesis strand pays a <strong>living allowance of CHF 2,500 per month for up to 6 months</strong>, plus up to <strong>CHF 1,500 for research costs</strong>. The Doctoral strand pays a <strong>salary contribution</strong> (including social security benefits, set by the host institution’s salary scale) plus up to <strong>CHF 3,000 a year for research costs</strong> and up to <strong>CHF 5,000 a year for conference costs</strong>, for <strong>4 years with a possible one-year extension</strong>. The Distinguished Postdoctoral strand pays a salary contribution on the same basis, plus the same research and conference caps, for <strong>up to 2 years</strong>. EPFL publishes <strong>no fixed salary figure</strong> and <strong>no lump-sum total</strong> for the doctoral and postdoctoral strands — only the scale basis and the caps — so this article states the components and nothing more.</p>
      <p>The timing is the part that needs care. The <strong>14th call is closed</strong>. The <strong>15th call</strong> for Doctoral and Distinguished Postdoctoral fellowships <strong>opens on 3 December 2026</strong>, with a <strong>Stage 1 deadline of 25 February 2027 at 17:00 CET</strong>. The Master Thesis strand runs on a <strong>rolling call with no fixed deadline</strong> — applications may be submitted throughout the year. If you see "19 August 2026" on a listing, that was the 14th call and it is over. The research itself must engage with <strong>cyber-defence themes</strong> — protecting the confidentiality, integrity and availability of cyber and cyber-physical systems; information sharing, data fusion and crowdsourcing; data science and AI methods for cyber-relevant data; and security, privacy and digital trust technologies — and must bring together CYD Campus researchers and at least one Swiss higher education institution.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizens of any nationality</strong> may apply; <strong>no age restrictions</strong> apply.</li>
        <li><strong>Excellence is the primary selection criterion</strong>, judged on academic records and professional accomplishments; strong grade transcripts are expected.</li>
        <li><strong>Master Thesis:</strong> must be <strong>enrolled in a Master’s programme at a Swiss higher education institution</strong> (university or school of applied sciences) and have the <strong>endorsement of a professor/supervisor</strong> employed there.</li>
        <li><strong>Doctoral:</strong> must be <strong>enrolled in a doctoral programme at a Swiss higher education institution</strong> and have a <strong>supervising professor’s endorsement</strong> by the Stage 2 application. Applicants endorsed by a professor at a school of applied sciences must also provide written confirmation at Stage 2 of simultaneous enrolment in a doctoral programme at a Swiss university. <strong>Preference</strong> is given to applicants who have <strong>not yet started, or are at the beginning of, their PhD</strong>. Funding for less than four years may be requested if that matches the thesis completion date.</li>
        <li><strong>Distinguished Postdoctoral:</strong> must have the <strong>endorsement of a professor</strong> employed at a Swiss higher education institution by the Stage 2 application, and the funded postdoctoral research must be carried out in a <strong>different laboratory</strong> from the applicant’s doctoral laboratory and any current postdoctoral laboratory.</li>
        <li>Research must engage with <strong>cyber-defence themes</strong>: protection of confidentiality, integrity and availability of cyber and cyber-physical systems; information sharing, data fusion and crowdsourcing; data science and AI methods for cyber-relevant data; and security, privacy and digital trust technologies. Applicants must show their project can <strong>significantly influence security/data-science research and Swiss cyber-defence</strong>, and that it brings together <strong>CYD Campus researchers and at least one Swiss higher education institution</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Master Thesis:</strong> a <strong>living allowance of CHF 2,500 per month</strong> for a maximum of 6 months, plus up to <strong>CHF 1,500 for research costs</strong>.</li>
        <li><strong>Doctoral:</strong> a <strong>salary contribution</strong> (including social security benefits, set by the host institution’s salary scale) plus up to <strong>CHF 3,000 per year for research costs</strong> and up to <strong>CHF 5,000 per year for conference costs</strong>, for <strong>4 years</strong> with a possible <strong>one-year extension</strong>.</li>
        <li><strong>Distinguished Postdoctoral:</strong> a <strong>salary contribution</strong> on the same basis, plus the same <strong>CHF 3,000/year research</strong> and <strong>CHF 5,000/year conference</strong> caps, for <strong>up to 2 years</strong>.</li>
        <li>A <strong>CYD Campus mentor</strong> for shortlisted applicants, and research hosted by a Swiss higher education institution with CYD Campus researchers.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>exact document checklist is not published in detail</strong> on the EPFL pages checked. The official pages state only that all required documents must be <strong>submitted in English via the online submission platform</strong>, and direct applicants to read the <strong>call guidelines and the application toolkit</strong>.</li>
        <li>The toolkit currently linked is for the <strong>14th call</strong>; EPFL states the <strong>updated documents for the 15th call will be available when it opens on 3 December 2026</strong>. No itemised document checklist (for example CV, transcripts, proposal) could be confirmed from two sources, so no such list is printed here as fact — the exact document list is in the official toolkit/guidelines.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official <strong>call guidelines and application toolkit</strong> on the EPFL CYD Fellowships page (15th-call versions from <strong>3 December 2026</strong>).</li>
        <li>Check the list of <strong>prioritised topics</strong> in the call guidelines and align your proposal with them; Master Thesis applicants may pick a listed CYD Campus topic or propose their own.</li>
        <li>Secure <strong>hosting/endorsement from a professor at a Swiss higher education institution</strong> (needed by Stage 2 for doctoral/postdoctoral applicants).</li>
        <li>Prepare and submit all documents in <strong>English</strong> through the official <strong>online submission platform</strong> before the Stage 1 deadline.</li>
        <li><strong>Selection runs in two stages:</strong> Stage 1 screening by a CYD Campus internal committee, after which shortlisted applicants are assigned a <strong>prospective CYD Campus mentor</strong> who interviews them and must endorse them for Stage 2; Stage 2 requires a <strong>full research proposal</strong>, with final decisions by a committee chaired by the <strong>Director of the CYD Campus</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the EPFL CYD Fellowship 2027?',
  'For the Doctoral and Distinguished Postdoctoral strands (15th call): 25 February 2027 at 17:00 CET (Stage 1). The call opens 3 December 2026. The Master Thesis strand runs on a rolling call with no fixed deadline. The August 2026 date on older listings was the closed 14th call.'),
 ('How much is the EPFL CYD Fellowship worth?',
  'Master Thesis: CHF 2,500 a month for up to 6 months, plus up to CHF 1,500 for research. Doctoral: a salary contribution for 4 years (possible 1-year extension) plus up to CHF 3,000 a year for research and CHF 5,000 a year for conferences. Distinguished Postdoctoral: the same, for up to 2 years. EPFL publishes no fixed salary figure and no lump-sum total for the doctoral/postdoctoral strands.'),
 ('Who can apply for the EPFL CYD Fellowship?',
  'Citizens of any nationality, with no age limit. Master Thesis applicants must be enrolled in a Master’s at a Swiss higher education institution with a professor’s endorsement. Doctoral applicants must be enrolled in a PhD at a Swiss higher education institution with a supervising professor’s endorsement by Stage 2. Postdoctoral applicants need a professor’s endorsement by Stage 2 and must work in a different laboratory from their doctoral and any current postdoctoral laboratory.'),
 ('What research does the CYD Fellowship fund?',
  'Cyber-defence research: protection of confidentiality, integrity and availability of cyber and cyber-physical systems; information sharing, data fusion and crowdsourcing; data science and AI methods for cyber-relevant data; and security, privacy and digital trust technologies. The project must bring together CYD Campus researchers and at least one Swiss higher education institution.'),
 ('What documents do I need for the CYD Fellowship?',
  'The exact checklist is not published on the EPFL pages — it is in the official call guidelines and application toolkit, with 15th-call documents available when the call opens on 3 December 2026. All documents are submitted in English via the online submission platform.'),
 ('How does CYD Fellowship selection work?',
  'In two stages. Stage 1 screening by a CYD Campus internal committee, after which shortlisted applicants are assigned a prospective CYD Campus mentor who interviews them and must endorse them for Stage 2. Stage 2 requires a full research proposal, with final decisions by a committee chaired by the Director of the CYD Campus.'),
 ('When does the 15th CYD call open?',
  '3 December 2026, for Doctoral and Distinguished Postdoctoral fellowships. The Master Thesis strand is rolling.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the official EPFL CYD Fellowships pages (overview, Master Thesis, Doctoral and Distinguished Postdoctoral pages, epfl.ch/research/funding/epfl-programmes/cyd/), which state that the 14th call is closed, the 15th call for Doctoral and Distinguished Postdoctoral fellowships opens on 3 December 2026 with a Stage 1 deadline of 25 February 2027 at 17:00 CET, and that the Master Thesis fellowship runs on a rolling call with no fixed deadline. Award components: Master Thesis living allowance CHF 2,500/month for a maximum of 6 months plus up to CHF 1,500 for research costs; Doctoral salary contribution (including social security benefits, set by the host institution's salary scale — no fixed figure published) plus up to CHF 3,000/year for research costs and up to CHF 5,000/year for conference costs, for 4 years with a possible one-year extension; Distinguished Postdoctoral salary contribution on the same basis plus the same caps, for up to 2 years. No lump-sum total is published by EPFL for the doctoral/postdoctoral strands. Eligibility: citizens of any nationality, no age restrictions; excellence the primary criterion (academic records and professional accomplishments; strong transcripts expected); Master Thesis — enrolled in a Master's at a Swiss higher education institution with a professor/supervisor's endorsement; Doctoral — enrolled in a doctoral programme at a Swiss higher education institution with a supervising professor's endorsement by Stage 2 (applicants endorsed by a professor at a school of applied sciences must also provide written confirmation at Stage 2 of simultaneous enrolment in a doctoral programme at a Swiss university; preference to applicants who have not yet started, or are at the beginning of, their PhD; funding for less than four years may be requested if that matches the thesis completion date); Distinguished Postdoctoral — endorsement of a professor at a Swiss higher education institution by Stage 2, funded research in a different laboratory from the doctoral laboratory and any current postdoctoral laboratory; research must engage with cyber-defence themes and bring together CYD Campus researchers and at least one Swiss higher education institution. Selection: two stages — Stage 1 screening by a CYD Campus internal committee, shortlisted applicants assigned a prospective CYD Campus mentor who interviews them and must endorse them for Stage 2; Stage 2 full research proposal, final decisions by a committee chaired by the Director of the CYD Campus. CONFLICTS: (1) August 2026 vs February 2027 — the queue and several aggregator sites still list 19 August 2026; the official EPFL pages state the 14th call is closed and the 15th call opens 3 December 2026 with a 25 February 2027 Stage 1 deadline. Resolved in favour of the official EPFL pages; the August 2026 date belongs to the closed 14th call. (2) "Fully funded" lump sums on aggregator sites — only the component figures above are confirmed by EPFL; no lump-sum total for doctoral/postdoctoral funding is published. (3) Possible nationality limits on sensitive projects — one secondary source suggests some projects may carry nationality restrictions; this does not appear on the official EPFL pages, which state any nationality may apply, so it is not confirmed and is not stated as a rule. Documents: exact checklist NOT published in detail on the EPFL pages checked — the official pages state only that all required documents must be submitted in English via the online submission platform (epflresearchfunds.gomovein.com), and direct applicants to the call guidelines and application toolkit; the toolkit currently linked is for the 14th call, with 15th-call documents available when the call opens on 3 December 2026.</p>''',
 dl_long='25 February 2027, 17:00 CET — Stage 1 (15th call opens 3 December 2026; Master Thesis rolling)',
 offlinks=[('EPFL — CYD Fellowships overview (official)', 'https://www.epfl.ch/research/funding/epfl-programmes/cyd/'),
           ('EPFL — CYD Doctoral Fellowships (official)', 'https://www.epfl.ch/research/funding/epfl-programmes/cyd/cyd-phd/'),
           ('EPFL — CYD Distinguished Postdoctoral Fellowships (official)', 'https://www.epfl.ch/research/funding/epfl-programmes/cyd/cyd-postdoc/'),
           ('EPFL — CYD Master Thesis Fellowship (official)', 'https://www.epfl.ch/research/funding/epfl-programmes/cyd/cyd-master/'),
           ('Bright Scholarship — EPFL CYD Fellowships 2027', 'https://brightscholarship.com/epfl-cyd-fellowships-2027-in-switzerland/')],
 related_titles=['sges-2027', 'daad-reinvitation-2027', 'sbw-berlin-2027', 'emhrpp-2027'])),

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
    json.dump(sizes, open('/tmp/batch59_built.json','w'))

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

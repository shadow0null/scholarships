#!/usr/bin/env python3
"""Batch 52 (cron run 52, 26 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. AIM ADB-Japan Scholarship 2027 - SKIPPED: deadline passed 15 Sep 2026
   (January 2027 MDM intake; Buddy4Study's 31 Dec 2026 is the programme-wide
   date, not the AIM intake date).
2. Harvard Law School Fellowship 2027 - SKIPPED: deadline passed 1 Oct 2026
   (Reginald F. Lewis Fellowship for Law Teaching, $60,000 stipend).
3. VFD Future Leaders Graduate Trainee Programme 2026 - SKIPPED: deadline
   passed 31 Aug 2026 (Bright); "Rolling" counter-claim uncorroborated and
   the official VFD page could not be checked - unresolved.
4. Westminster Postgraduate Scholarships 2027 - VERIFIED (scope corrected):
   International Postgraduate Excellence Award - January 2027. Deadline
   30 Nov 2026. GBP 3,000 (1-yr Master's) / GBP 5,000 (2-yr with Integrated
   Professional Year). Partial tuition reduction only - NOT fully funded.
5. British Chevening Scholarship 2027 - SKIPPED: deadline passed 6 Oct 2026,
   11:00 UTC (2027/28 cycle closed; 2028/29 not yet announced).
6. America's Future Development Fellowship 2026 - SKIPPED: deadline passed
   7 Sep 2026 (official page: Fall 2026 cohort closed).
7. WIPO Fellowship Program 2026 - SKIPPED: deadline passed 7 Aug 2026.
8. Texas State Molecular Parasitology PhD 2027 - SKIPPED: deadline passed
   (review began 15 Aug 2026); single-lab vacancy, not a scholarship.
9. Asia Pacific University MEXT Scholarship 2027 - VERIFIED: deadline
   5 Nov 2026 (September 2027 enrolment only, MEXT University
   Recommendation). JPY 144,000/month + full tuition + airfare. Graduate
   only (Master's/PhD). CORRECTION: Bright says Bachelor's/Master's/PhD
   and calls APU "Asia Pacific University of Technology and Innovation"
   (a Malaysian university) - both wrong; APU founded 2000.
10. DAAD Re-Invitation Programme 2027 - VERIFIED: next open deadline
    23 Feb 2027 (funding from Oct 2027); 1 Oct 2026 round closed.
    EUR 2,000/month (assistant teachers/lecturers) / EUR 2,150 (professors),
    1-3 months. Former DAAD holders only; country-restricted.
11. TU Berlin DAAD EPOS Scholarship 2027 - SKIPPED: deadline passed
    31 Aug 2026 (M.Sc. Urban Management, Oct 2027 intake).
12. Best Portugal Scholarships Without IELTS 2027 - SKIPPED: listicle.
13. GovAI Research Fellows Program 2026 - SKIPPED: deadline passed
    16 Aug 2026 (official page: applications closed).
14. ASEF LinkUp Programme 2026 - SKIPPED: deadline passed 27 Aug 2026.
15. Top 25 American Scholarships Without IELTS 2027 - SKIPPED: listicle.
16. Erasmus Mundus Scholarship Program 2027 - SKIPPED: aggregator composite
    (EMJM framework, no single scheme/deadline).
17. DDSA Visit Grant Scholarships 2027 - SKIPPED: deadline passed 1 Sep 2026;
    2026 call closed for exhausted funds, no 2027 call announced.
18. Ontario Graduate Scholarship 2027 - VERIFIED (framing corrected): no
    single deadline - varies by university (Carleton 16 Nov 2026, Ontario
    Tech 1 Dec 2026, Laurentian 31 Jan 2027). CAD 5,000/term (max
    CAD 15,000). Partial, not fully funded. International students only if
    already studying in Ontario on a study permit.
19. Carleton University Scholarships 2027 - SKIPPED: aggregator composite
    (many separate awards under one "Varies" deadline; the Prestige
    Scholarships reframe - deadline 1 Mar 2027 - is noted for a future
    single-scheme queue entry, not written here).
20. Eric Bleumink Scholarship 2027 - VERIFIED: deadline 1 Dec 2026.
    Official grant EUR 15,000 (Ubbo Emmius Fund). "Fully funded" label
    flagged: secondary sources describe tuition/travel/subsistence/books/
    insurance coverage; no monthly stipend figure is official.

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
 'westminster-2027': {'mono': 'UW', 'title': 'University of Westminster International Postgraduate Excellence Award 2027 in UK (Partially Funded)',
   'href': 'westminster-international-postgraduate-excellence-award-2027-uk.html',
   'dpill': 'Deadline 30 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-30'),
   'award': 'A partial tuition-fee reduction of \u00a33,000 for a one-year full-time Master\u2019s, or \u00a35,000 for the two-year Master\u2019s with Integrated Professional Year Experience. Not full funding: no living costs, travel, visa or CAS-deposit support.',
   'elig': 'International students with overseas fee status holding an offer for a full-time Master\u2019s starting January 2027, with at least a UK equivalent Good 2.1 Honours degree.',
   'tags': [('Master\u2019s', 'blue'), ('UK', 'teal')]},
 'apu-mext-2027': {'mono': 'AP', 'title': 'Asia Pacific University MEXT Scholarship 2027 in Japan (Fully Funded)',
   'href': 'asia-pacific-university-mext-scholarship-2027-japan.html',
   'dpill': 'Deadline 5 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-05'),
   'award': 'Fully funded MEXT University Recommendation award for graduate study at Ritsumeikan APU: full admission fee and tuition, a \u00a5144,000 monthly stipend and economy round-trip airfare, for the full programme.',
   'elig': 'Master\u2019s and PhD applicants only, citizens of a MEXT-designated country, born on or after 2 April 1992, with a GPA of at least 2.30 on a 3.00 scale and English at B2 level (TOEFL iBT 72+ or IELTS 5.5+).',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Japan', 'teal')]},
 'daad-reinvitation-2027': {'mono': 'DA', 'title': 'DAAD Re-Invitation Programme 2027 in Germany (Funded)',
   'href': 'daad-re-invitation-programme-2027-germany.html',
   'dpill': 'Deadline 23 Feb 2027 \u00b7 %d days left' % dl_left('2027-02-23'),
   'award': '\u20ac2,000 a month for assistant teachers, assistant professors and lecturers (\u20ac2,150 for professors), plus a travel allowance and health insurance, for a 1\u20133 month research stay in Germany. Former DAAD scholarship holders only.',
   'elig': 'Former DAAD research-grant or study-scholarship holders funded for more than 6 months, who have not lived in Germany for at least the last 3 years, with a project coordinated with a German cooperation partner.',
   'tags': [('Research stay', 'purple'), ('Germany', 'teal')]},
 'bleumink-2027': {'mono': 'EB', 'title': 'Eric Bleumink Scholarship 2027 in Netherlands (Fully Funded)',
   'href': 'eric-bleumink-scholarship-2027-netherlands.html',
   'dpill': 'Deadline 1 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-01'),
   'award': 'An individual grant of \u20ac15,000 per student (official Ubbo Emmius Fund figure) for a 1- or 2-year Master\u2019s at the University of Groningen, starting September 2027. Secondary sources describe tuition, travel, subsistence, books and insurance coverage.',
   'elig': 'Students from eligible non-Western / developing countries with outstanding undergraduate grades, admitted to a Groningen Master\u2019s before February 2027, with no other means of financing their studies.',
   'tags': [('Master\u2019s', 'blue'), ('Netherlands', 'teal')]},
 'ogs-2027': {'mono': 'OG', 'title': 'Ontario Graduate Scholarship 2027 in Canada (Funded)',
   'href': 'ontario-graduate-scholarship-2027-canada.html',
   'dpill': 'Deadline varies by university \u00b7 earliest 16 Nov 2026',
   'award': 'CAD $5,000 per term, $10,000 for two consecutive terms or $15,000 for three, for Master\u2019s or PhD study at a participating Ontario university. Partial funding, jointly paid by the Ontario government and the host university.',
   'elig': 'Master\u2019s or PhD students at a participating Ontario university with a minimum A\u2212 average in the last two years of full-time study. International students only if already studying in Ontario on a valid study permit.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Canada', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Westminster
A.append(dict(
 slug='westminster-international-postgraduate-excellence-award-2027-uk',
 title='University of Westminster International Postgraduate Excellence Award 2027 in UK (Partially Funded)',
 meta='University of Westminster International Postgraduate Excellence Award 2027: a \u00a33,000 tuition-fee reduction for a one-year full-time Master\u2019s (\u00a35,000 for the two-year Master\u2019s with Integrated Professional Year Experience) starting January 2027. Deadline 30 November 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Westminster International Postgraduate Excellence Award 2027', kicker='UK \u00b7 Master\u2019s \u00b7 Partially Funded', mono='UW',
 prov_short='University of Westminster', prov_cat='University \u00b7 United Kingdom',
 h1='University of Westminster International Postgraduate Excellence Award 2027 in UK (Partially Funded)',
 sub='The University of Westminster International Postgraduate Excellence Award 2027 is a partial tuition-fee reduction for international students starting a full-time Master\u2019s in January 2027: \u00a33,000 off a one-year Master\u2019s, or \u00a35,000 off the two-year Master\u2019s with Integrated Professional Year Experience. Read the word "partial" carefully, because most listings do not: this award does not cover living costs, travel, a visa, or the \u00a35,500 CAS deposit, and it is not the fully funded scholarship the queue title suggests. The deadline is 30 November 2026.',
 dpill='Deadline 30 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-30'),
 facts=facts([('Award', '\u00a33,000 towards tuition fees for a one-year full-time Master\u2019s, or \u00a35,000 for the two-year Master\u2019s with Integrated Professional Year Experience. The award is applied as a tuition-fee reduction only \u2014 it cannot be used towards the \u00a35,500 CAS deposit, and it does not cover living costs, travel or visa costs. The number of awards is variable, per the official page. This is a partial award, not full funding.'),
              ('Eligible', 'Classified as overseas fee status; hold an offer for a full-time Master\u2019s starting January 2027; hold a minimum UK equivalent Good 2.1 Honours degree. Selection is principally on academic excellence. Not eligible: professional courses (for example RIBA Part III), doctoral programmes, online or distance learning, Postgraduate Certificates or Diplomas, or anyone eligible for another tuition discount such as an alumni or partner discount. Nationality is open \u2014 the requirement is overseas fee status, not a particular country.'),
              ('How', 'Apply for an eligible full-time Master\u2019s starting January 2027 and secure an offer, then submit the scholarship application through the "Apply now" link on the official award page before 30 November 2026. A separate scholarship application is required \u2014 the award is not automatic on offer, whatever some listings claim.'),
              ('Deadline', '30 November 2026. The exact time of day on 30 November is not published on the official page.'),
              ('Fine print', 'Do not confuse this award with two separate January 2027 awards on the same official site. The Postgraduate Sanctuary Scholarship is genuinely fully funded \u2014 a full tuition waiver plus \u00a31,000 a month for up to 12 months, 2 awards \u2014 but only for asylum seekers resident in the UK, with a deadline of 2 November 2026, 5pm. The Home Postgraduate Part Fee Scholarship is \u00a32,000 for Home fee students only, also closing 2 November 2026, 5pm. Neither is the award this article covers. No taught-postgraduate Vice-Chancellor\u2019s Scholarship was found on Westminster\u2019s site, so none is presented here. One listing claims applicants "will be informed of the outcome by 21 November 2026" \u2014 impossible, since that precedes the 30 November deadline, and it is not used here.')]),
 body='''
      <h2 id="about">About the award</h2>
      <p>The <strong>International Postgraduate Excellence Award \u2013 January 2027</strong> is the University of Westminster\u2019s main partial scholarship for international students starting a taught Master\u2019s in January 2027. It is awarded on <strong>academic excellence</strong>: the university selects the strongest applicants from those who hold an offer for an eligible full-time Master\u2019s and apply for the award before the deadline.</p>
      <p>What it pays is straightforward and modest: <strong>\u00a33,000 off tuition</strong> for a one-year full-time Master\u2019s, or <strong>\u00a35,000</strong> for the two-year Master\u2019s with Integrated Professional Year Experience. It is a <strong>tuition-fee reduction only</strong> \u2014 it cannot be put towards the <strong>\u00a35,500 CAS deposit</strong>, and it pays nothing towards living costs, travel or a visa. If you are budgeting for a year in London, treat this as a discount on the fee, not as funding for the year.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be classified as <strong>overseas fee status</strong>.</li>
        <li>Hold an offer for a <strong>full-time Master\u2019s starting January 2027</strong>.</li>
        <li>Hold a minimum <strong>UK equivalent Good 2.1 Honours degree</strong>.</li>
        <li>Be selected principally on <strong>academic excellence</strong>.</li>
        <li><strong>Not eligible:</strong> professional courses (for example RIBA Part III), doctoral programmes, online or distance learning, Postgraduate Certificates or Diplomas, or anyone eligible for another tuition discount such as an alumni or partner discount.</li>
        <li>Nationality is <strong>open</strong> \u2014 the requirement is overseas fee status, not a particular country.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u00a33,000</strong> towards tuition fees for a one-year full-time Master\u2019s.</li>
        <li><strong>\u00a35,000</strong> towards tuition fees for the two-year Master\u2019s with Integrated Professional Year Experience.</li>
        <li>Applied as a <strong>tuition-fee reduction</strong>.</li>
        <li>Note that the award <strong>cannot</strong> go towards the <strong>\u00a35,500 CAS deposit</strong>, and covers <strong>no living costs, travel or visa costs</strong>.</li>
        <li>The number of awards is <strong>variable</strong>, per the official page.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>scholarship application</strong> itself, submitted through the "Apply now" link on the official award page.</li>
        <li>Proof of your <strong>course offer</strong> for a full-time Master\u2019s starting January 2027.</li>
        <li><strong>Transcripts</strong> showing the equivalent of a Good 2.1 Honours degree (the official page works from the course application and its country-equivalency chart).</li>
        <li>Note that the official page does <strong>not publish a full document checklist</strong> beyond the application form, the offer and the transcripts. Lists on aggregator sites (passport, motivation letter, CV, cover letter, degree certificates, language proficiency) were not confirmed on the official page and are not presented here as official requirements.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for an <strong>eligible full-time Master\u2019s starting January 2027</strong> at the University of Westminster and secure an offer.</li>
        <li>Open the <strong>official award page</strong> and submit the scholarship application through its "Apply now" link.</li>
        <li>Make sure your <strong>offer is in place in time</strong> to meet the scholarship deadline.</li>
        <li>Submit the scholarship application by <strong>30 November 2026</strong>.</li>
        <li>Note that a <strong>separate scholarship application is required</strong> \u2014 the award is not automatic on offer, whatever some listings claim.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Westminster International Postgraduate Excellence Award fully funded?',
  'No. It is a partial tuition-fee reduction of \u00a33,000 (one-year Master\u2019s) or \u00a35,000 (two-year Master\u2019s with Integrated Professional Year Experience). It does not cover living costs, travel, visa costs or the \u00a35,500 CAS deposit.'),
 ('What is the deadline for the Westminster Excellence Award 2027?',
  '30 November 2026. The exact time of day on 30 November is not published on the official page.'),
 ('Do I need to apply separately for the scholarship?',
  'Yes. A separate scholarship application is required through the "Apply now" link on the official award page. The award is not automatic on offer, whatever some listings claim.'),
 ('Can the award be used for the CAS deposit?',
  'No. The award is applied as a tuition-fee reduction only and cannot go towards the \u00a35,500 CAS deposit.'),
 ('What is the Postgraduate Sanctuary Scholarship?',
  'A separate, genuinely fully funded award at Westminster: a full tuition waiver plus \u00a31,000 a month for up to 12 months, with 2 awards. It is only for asylum seekers resident in the UK, and its deadline was 2 November 2026, 5pm. It is not the award this article covers.'),
 ('Who is not eligible?',
  'Students on professional courses (for example RIBA Part III), doctoral programmes, online or distance learning, and Postgraduate Certificates or Diplomas; and anyone eligible for another tuition discount such as an alumni or partner discount.')]) + '''
      <p class="verify">Verified 26 Oct 2026: westminster.ac.uk (official International Postgraduate Excellence Award \u2013 January 2027 page, opened and read in full) \u2014 \u00a33,000 (one-year Master\u2019s) / \u00a35,000 (two-year with Integrated Professional Year Experience), tuition-fee reduction only, cannot go towards the \u00a35,500 CAS deposit, overseas fee status, offer for a full-time Master\u2019s starting January 2027, minimum UK equivalent Good 2.1 Honours, deadline 30 November 2026; AfterSchoolAfrica, Bright Scholarship, ScholarshipsAds, Fully-FundedScholarships \u2014 corroboration. CORRECTION: the queue title\u2019s "(Funded)" framing is misleading \u2014 this is a partial award, not full funding, and the article is scoped to the Excellence Award only. The Postgraduate Sanctuary Scholarship (full tuition waiver + \u00a31,000/month up to 12 months, 2 awards, asylum seekers resident in the UK only, deadline 2 November 2026, 5pm) and the Home Postgraduate Part Fee Scholarship (\u00a32,000, Home fee students only, deadline 2 November 2026, 5pm) are separate awards. No taught-postgraduate Vice-Chancellor\u2019s Scholarship was found on Westminster\u2019s site. CollegeDunia\u2019s "automatic on offer" claim is contradicted by the official page\u2019s "Apply now" link. One listing\u2019s outcome date of 21 November 2026 precedes the deadline and is not used. The exact time of day on 30 November and the full document checklist are not published on the official page.</p>''',
 dl_long='30 November 2026',
 offlinks=[('University of Westminster \u2014 International Postgraduate Excellence Award, January 2027 (official)', 'https://www.westminster.ac.uk/study/fees-and-funding/scholarships/international-postgraduate-excellence-award-january-2027'),
           ('Bright Scholarship \u2014 Westminster Postgraduate Scholarships 2027', 'https://brightscholarship.com/westminster-postgraduate-scholarships-2027/')],
 related_titles=['southampton-2027', 'leeds-2027', 'pershing-2027', 'st-andrews-pg-2027'])),

# ---------------------------------------------------------------- 2. APU MEXT
A.append(dict(
 slug='asia-pacific-university-mext-scholarship-2027-japan',
 title='Asia Pacific University MEXT Scholarship 2027 in Japan (Fully Funded)',
 meta='Asia Pacific University MEXT Scholarship 2027: a fully funded MEXT University Recommendation award for graduate study at Ritsumeikan APU \u2014 full tuition, a \u00a5144,000 monthly stipend and economy round-trip airfare. Deadline 5 November 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Asia Pacific University MEXT Scholarship 2027', kicker='Japan \u00b7 Master\u2019s & PhD \u00b7 Fully Funded', mono='AP',
 prov_short='Ritsumeikan Asia Pacific University', prov_cat='University \u00b7 Japan',
 h1='Asia Pacific University MEXT Scholarship 2027 in Japan (Fully Funded)',
 sub='The Asia Pacific University MEXT Scholarship 2027 is a fully funded MEXT University Recommendation award for graduate study at Ritsumeikan Asia Pacific University (APU) in Beppu, Japan: full tuition, a \u00a5144,000 monthly stipend and economy round-trip airfare, for the full length of your Master\u2019s or PhD. Two things to get right before you apply. First, this route is for graduate study only \u2014 there is no undergraduate MEXT route at APU, whatever some listings say. Second, it is for September 2027 enrolment only, and the deadline is 5 November 2026 \u2014 ten days away.',
 dpill='Deadline 5 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-05'),
 facts=facts([('Award', 'Fully funded under the MEXT University Recommendation route: full admission fee, 100% of tuition (through the APU Tuition Reduction Scholarship), a monthly stipend of \u00a5144,000 (including housing; the amount is subject to change), and economy-class round-trip airfare between your home country and APU at the start and end of the programme. The award lasts for the full length of the enrolled graduate programme. The number of awards is not published \u2014 it varies annually with MEXT allocations.'),
              ('Eligible', 'Master\u2019s and PhD applicants only (Graduate School of Asia Pacific Studies; Graduate School of Management / MBA). Be a citizen of a MEXT-designated country (a country with diplomatic relations with Japan); not a Japanese national, including dual nationality. Intend to study in Japan from overseas and hold, or be eligible for, a Student visa. Be born on or after 2 April 1992. Hold a GPA of at least 2.30 on a 3.00 scale at your most recent university. Show English at B2 CEFR level or above \u2014 TOEFL iBT 72 or above, or IELTS 5.5 or above, or an English-medium-of-instruction certificate from your previous university; only English tests taken on or after 15 March 2025 count. Excluded: active military personnel and civilian military staff, previous MEXT recipients (with limited exceptions), and holders of another unapproved concurrent scholarship.'),
              ('How', 'Apply for admission to an APU graduate programme through APU\u2019s online application system (apply.admissions.apu.ac.jp) by 5 November 2026, and pay the \u00a511,250 screening fee (bank transfer only, non-refundable). APU reviews applications and selects candidates to recommend to MEXT; recommended candidates are notified with their APU admission result, and MEXT makes the final scholarship decision by the end of June 2027. Do NOT apply directly to MEXT for this route \u2014 there is no separate MEXT application.'),
              ('Deadline', '5 November 2026, for September 2027 enrolment only (MEXT University Recommendation route). The application period opened on 1 September 2026. There is no April 2027 round for the MEXT University Recommendation route at APU \u2014 an April intake mentioned by one aggregator is generic APU admission, not this route.'),
              ('Fine print', 'Bright Scholarship says this award covers Bachelor\u2019s, Master\u2019s and PhD \u2014 wrong: the MEXT University Recommendation route at APU is for graduate applicants only, and APU\u2019s own MEXT page sits under /graduate/. Bright also calls APU "Asia Pacific University of Technology and Innovation" \u2014 that is a Malaysian university, not APU \u2014 and says APU was founded in 1993; APU was founded in 2000. Bright\u2019s headline "no IELTS/TOEFL needed" is misleading \u2014 English proficiency evidence IS required (test scores or an English-medium certificate). One source gives the age cut-off as born on or after 2 April 1986; six sources give 2 April 1992, which is used here. APU\u2019s admissions site is currently restricted after a critical PHP vulnerability was identified, so the full document list below is assembled from secondary sources \u2014 check the 2027 Graduate Application Handbook on the APU admissions site once it is restored.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>MEXT Scholarship (University Recommendation)</strong> at <strong>Ritsumeikan Asia Pacific University (APU)</strong> is Japan\u2019s government scholarship, administered by the Ministry of Education, Culture, Sports, Science and Technology (MEXT), with APU selecting and recommending candidates. APU, in Beppu, Oita Prefecture, is one of Japan\u2019s most international universities \u2014 around half its students come from outside Japan \u2014 and its graduate schools run English-taught Master\u2019s and PhD programmes in Asia Pacific Studies and Management.</p>
      <p>The funding is genuinely full: <strong>full admission fee and tuition</strong>, a <strong>\u00a5144,000 monthly stipend</strong> (including housing) and <strong>economy round-trip airfare</strong>, for the full length of the programme. But the route is narrow in two ways that listings keep getting wrong. It is <strong>graduate study only</strong> \u2014 there is no undergraduate MEXT route at APU \u2014 and it is for <strong>September 2027 enrolment only</strong>. If you are applying for an April start, or for a Bachelor\u2019s, this is not your route.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Apply for a <strong>Master\u2019s or PhD</strong> at APU (Graduate School of Asia Pacific Studies; Graduate School of Management / MBA). <strong>Undergraduate applicants are not eligible</strong> for this route.</li>
        <li>Be a citizen of a <strong>MEXT-designated country</strong> (a country with diplomatic relations with Japan); <strong>not</strong> a Japanese national, including dual nationality.</li>
        <li>Intend to study in Japan <strong>from overseas</strong> and hold, or be eligible for, a <strong>Student visa</strong>.</li>
        <li>Be <strong>born on or after 2 April 1992</strong>.</li>
        <li>Hold a <strong>GPA of at least 2.30 on a 3.00 scale</strong> at your most recent university.</li>
        <li>Show English at <strong>B2 CEFR level or above</strong> \u2014 TOEFL iBT 72 or above, or IELTS 5.5 or above, or an English-medium-of-instruction certificate from your previous university. Only English tests taken <strong>on or after 15 March 2025</strong> count.</li>
        <li><strong>Excluded:</strong> active military personnel and civilian military staff; previous MEXT recipients (with limited exceptions); holders of another unapproved concurrent scholarship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full admission fee</strong> and <strong>100% of tuition</strong> (through the APU Tuition Reduction Scholarship).</li>
        <li>A monthly stipend of <strong>\u00a5144,000</strong> (including housing; the amount is subject to change).</li>
        <li><strong>Economy-class round-trip airfare</strong> between your home country and APU at the start and end of the programme.</li>
        <li>Funding for the <strong>full length</strong> of the enrolled graduate programme.</li>
        <li>Note that the <strong>number of awards is not published</strong> \u2014 it varies annually with MEXT allocations.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application</strong> through APU\u2019s application system.</li>
        <li><strong>Academic transcripts</strong> (plus a grade scale sheet).</li>
        <li>A <strong>graduation or enrolment certificate</strong>.</li>
        <li>A valid <strong>passport copy</strong>.</li>
        <li><strong>English proficiency evidence</strong> (TOEFL iBT 72+, IELTS 5.5+, or an English-medium-of-instruction certificate).</li>
        <li>A <strong>statement of purpose / research plan</strong>.</li>
        <li><strong>Recommendation documents</strong>.</li>
        <li>The <strong>screening fee of \u00a511,250</strong> (bank transfer only, non-refundable).</li>
        <li>Note that this list is assembled from secondary sources: APU\u2019s admissions site is currently restricted after a critical PHP vulnerability was identified, so check the <strong>2027 Graduate Application Handbook</strong> on the APU admissions site once it is restored.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose an <strong>APU graduate programme</strong> (Graduate School of Asia Pacific Studies, or Graduate School of Management / MBA).</li>
        <li>Apply for admission through APU\u2019s <strong>online application system</strong> (apply.admissions.apu.ac.jp) by <strong>5 November 2026</strong>.</li>
        <li>Pay the <strong>\u00a511,250 screening fee</strong> by bank transfer.</li>
        <li>APU reviews applications and <strong>selects candidates to recommend to MEXT</strong>.</li>
        <li>Recommended candidates are notified with their <strong>APU admission result</strong>.</li>
        <li>MEXT makes the <strong>final scholarship decision by the end of June 2027</strong>.</li>
        <li>Do <strong>NOT apply directly to MEXT</strong> for this route \u2014 there is no separate MEXT application.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the APU MEXT Scholarship 2027?',
  '5 November 2026, for September 2027 enrolment only (MEXT University Recommendation route). The application period opened on 1 September 2026. There is no April 2027 round for this route.'),
 ('Is the APU MEXT Scholarship fully funded?',
  'Yes. It covers the full admission fee and 100% of tuition, a \u00a5144,000 monthly stipend (including housing) and economy round-trip airfare, for the full length of the graduate programme.'),
 ('Can undergraduates apply for the APU MEXT Scholarship?',
  'No. The MEXT University Recommendation route at APU is for Master\u2019s and PhD applicants only. Listings that say Bachelor\u2019s are wrong.'),
 ('Do I need IELTS or TOEFL?',
  'Yes, unless you can show an English-medium-of-instruction certificate from your previous university. You need TOEFL iBT 72 or above, or IELTS 5.5 or above, at B2 CEFR level \u2014 and only tests taken on or after 15 March 2025 count.'),
 ('What is the age limit?',
  'You must be born on or after 2 April 1992. One source gives 2 April 1986; six sources give 2 April 1992, which is used here.'),
 ('How much is the screening fee?',
  '\u00a511,250, paid by bank transfer only, non-refundable.'),
 ('When will I know the final result?',
  'MEXT makes the final scholarship decision by the end of June 2027. APU notifies recommended candidates with their admission result first.')]) + '''
      <p class="verify">Verified 26 Oct 2026: APU\u2019s own MEXT University Recommendation page (admissions.apu.ac.jp/graduate/how_to_apply/external_scholarship/u_recommendation/) as quoted by Academia Magazine, AfterSchoolAfrica and Bright Scholarship \u2014 deadline 5 November 2026, September 2027 enrolment only, \u00a5144,000 monthly stipend, full admission fee and tuition, economy round-trip airfare, born on or after 2 April 1992, GPA 2.30 on a 3.00 scale, TOEFL iBT 72+ / IELTS 5.5+ (tests on or after 15 March 2025), final MEXT decision by end June 2027; allpakalerts.com, o4af.com, scholarshipforphd.com, educatewithguide.com, career.mystudypals.com \u2014 corroboration. CORRECTION: Bright Scholarship says this award covers Bachelor\u2019s, Master\u2019s and PhD \u2014 wrong, it is graduate-only; Bright also calls APU "Asia Pacific University of Technology and Innovation" (a Malaysian university) and says APU was founded in 1993 \u2014 both wrong (APU was founded in 2000). Bright\u2019s "no IELTS/TOEFL needed" headline is misleading \u2014 English proficiency evidence is required. One source gives the age cut-off as 2 April 1986; six sources give 2 April 1992. APU\u2019s admissions site is currently restricted after a critical PHP vulnerability was identified (a stripped-down temporary site is live at sub-buildman.ssl-lolipop.jp/apu/en/), so the full document list is assembled from secondary sources and readers should check the 2027 Graduate Application Handbook. The number of awards is not published.</p>''',
 dl_long='5 November 2026',
 offlinks=[('Academia Magazine \u2014 APU MEXT Scholarship 2027 in Japan', 'https://academiamag.com/scholarships/apu-mext-scholarship-2027-in-japan/'),
           ('Bright Scholarship \u2014 Asia Pacific University MEXT Scholarship 2027', 'https://brightscholarship.com/asia-pacific-university-mext-scholarship-2027/')],
 related_titles=['kut-ssp-2027', 'sophia-2027', 'science-tokyo', 'u-tokyo-mext'])),

# ---------------------------------------------------------------- 3. DAAD Re-Invitation
A.append(dict(
 slug='daad-re-invitation-programme-2027-germany',
 title='DAAD Re-Invitation Programme 2027 in Germany (Funded)',
 meta='DAAD Re-Invitation Programme 2027: \u20ac2,000 a month for assistant teachers, assistant professors and lecturers (\u20ac2,150 for professors), plus a travel allowance and health insurance, for a 1\u20133 month research stay in Germany. Next deadline 23 February 2027 \u2014 eligibility, documents, how to apply and FAQs.',
 short='DAAD Re-Invitation Programme 2027', kicker='Germany \u00b7 Research Stay \u00b7 Funded', mono='DA',
 prov_short='German Academic Exchange Service (DAAD)', prov_cat='Exchange Service \u00b7 Germany',
 h1='DAAD Re-Invitation Programme 2027 in Germany (Funded)',
 sub='The DAAD Re-Invitation Programme 2027 invites former DAAD scholarship holders back to Germany for a short research or working stay: \u20ac2,000 a month for assistant teachers, assistant professors and lecturers (\u20ac2,150 for professors), plus a travel allowance and health insurance, for one to three months. Read the eligibility first, because this programme is not open to everyone: you must be a former DAAD scholarship holder who has not lived in Germany for at least the last three years. The next open deadline is 23 February 2027 \u2014 the 1 October 2026 round has already closed.',
 dpill='Deadline 23 Feb 2027 \u00b7 %d days left' % dl_left('2027-02-23'),
 facts=facts([('Award', 'Monthly payments of \u20ac2,000 for assistant teachers, assistant professors and lecturers, and \u20ac2,150 for professors. For applicants outside the science sector, the rate is calculated on qualifications. A travel allowance is paid unless it is covered by your home country or another funder. Health insurance is provided through DAAD if you are not otherwise insured \u2014 the cost is deducted from the payment. A disability or chronic-illness subsidy is available on application, case by case. Duration: 1\u20133 months, funding must begin in 2027, non-renewable, and claimable only once within three years. Do not call this simply "fully funded": state the exact payments instead.'),
              ('Eligible', 'Former holder of a DAAD research grant or study scholarship, funded for more than 6 months by the Federal Foreign Office or a co-financed programme; or an East German (GDR) scholarship holder who studied in Germany for at least 1 year. You must not have lived in Germany for at least the last 3 years. Your research or working project must be coordinated with a cooperation partner in Germany. Open to graduates, postdoctoral researchers and faculty, in all disciplines. Working stays in business, administration, culture or media are possible for non-science-sector alumni. Country-restricted \u2014 the DAAD database says "Country: Only specified", so do not repeat the "All Nationalities" claim; third-country applicants and Germans living abroad should contact the responsible DAAD branch or section before applying.'),
              ('How', 'Online only, through the DAAD portal (linked at the bottom of the official programme page): register in the portal, download and complete the form, upload your documents as PDFs, and submit. The portal opens at least 6 weeks before each deadline and closes at 24:00 CET/CEST on the last day; it is unavailable outside the application period. Technical help: portal@daad.de; hotline +49 (0) 228 882-8888, weekdays 09:00\u201312:00 and 14:00\u201316:00 CET/CEST.'),
              ('Deadline', '23 February 2027 (next open round; selection June/July 2027, funding starts October 2027). The 1 October 2026 round has closed (selection February 2027, funding from April 2027).'),
              ('Fine print', 'This article covers the main Re-Invitation Programme only. The separate EPOS re-invitation programme \u2014 for former holders of Development-Related Postgraduate Courses scholarships \u2014 has different deadlines and eligibility and is not covered here; do not mix the two. No application fee is mentioned on the official page, so none is claimed here. The exact list of eligible countries depends on the applicant\u2019s country filter in the DAAD database and cannot be stated as a fixed list.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>DAAD Re-Invitation Programme</strong> is the German Academic Exchange Service\u2019s way of keeping its alumni connected: if you once held a DAAD research grant or study scholarship, DAAD will fund you to come back to Germany for a <strong>short research or working stay of one to three months</strong>, to work on a project with a German cooperation partner. It is funded by the <strong>German Federal Foreign Office</strong>.</p>
      <p>The money is specific, not a blank cheque: <strong>\u20ac2,000 a month</strong> for assistant teachers, assistant professors and lecturers, <strong>\u20ac2,150 a month</strong> for professors, plus a <strong>travel allowance</strong> and <strong>health insurance</strong> if you are not otherwise insured. The stay must begin in 2027, cannot be renewed, and can be claimed only <strong>once within three years</strong>. And the door is narrow by design: you must be a <strong>former DAAD holder</strong> who has <strong>not lived in Germany for at least the last three years</strong>. If you have never held a DAAD scholarship, this programme is not for you.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>former holder of a DAAD research grant or study scholarship</strong>, funded for <strong>more than 6 months</strong> by the Federal Foreign Office or a co-financed programme; <strong>or</strong> an East German (GDR) scholarship holder who studied in Germany for <strong>at least 1 year</strong>.</li>
        <li>Have <strong>not lived in Germany for at least the last 3 years</strong>.</li>
        <li>Have a <strong>research or working project coordinated with a cooperation partner in Germany</strong>.</li>
        <li>Be a <strong>graduate, postdoctoral researcher or faculty member</strong>, in any discipline (languages and cultural studies; law, economics and social sciences; maths and natural sciences; medicine; veterinary, agricultural, forest, nutritional sciences and ecology; engineering; art, music and sport).</li>
        <li>Working stays in <strong>business, administration, culture or media</strong> are possible for non-science-sector alumni.</li>
        <li><strong>Country-restricted</strong> \u2014 the DAAD database says "Country: Only specified". Third-country applicants and Germans living abroad should <strong>contact the responsible DAAD branch or section</strong> before applying.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac2,000 a month</strong> for assistant teachers, assistant professors and lecturers; <strong>\u20ac2,150 a month</strong> for professors. For non-science-sector applicants, the rate is calculated on qualifications.</li>
        <li>A <strong>travel allowance</strong>, unless it is covered by your home country or another funder.</li>
        <li><strong>Health insurance</strong> through DAAD if you are not otherwise insured \u2014 the cost is deducted from the payment.</li>
        <li>A <strong>disability or chronic-illness subsidy</strong> on application, case by case.</li>
        <li>A <strong>1\u20133 month</strong> research or working stay in Germany, beginning in 2027.</li>
        <li>Note that the stay is <strong>non-renewable</strong> and can be claimed only <strong>once within three years</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application form</strong> (downloaded from the DAAD portal).</li>
        <li>A <strong>full tabular CV</strong> (maximum 3 pages).</li>
        <li>A <strong>list of publications</strong>, if applicable.</li>
        <li>A <strong>comprehensive project statement</strong> (maximum 10 pages, uploaded under "research project").</li>
        <li>A <strong>time schedule and itinerary</strong> of the visit.</li>
        <li><strong>Confirmation from the German academic host</strong>, referring to the project and guaranteeing a workplace.</li>
        <li><strong>German or English translations</strong> of any documents in a national language.</li>
        <li>All uploads as <strong>PDF only</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm you are a <strong>former DAAD scholarship holder</strong> who has not lived in Germany for at least the last 3 years.</li>
        <li>Agree your <strong>project with a cooperation partner in Germany</strong> and get their written confirmation.</li>
        <li>Wait for the <strong>DAAD portal to open</strong> \u2014 at least 6 weeks before the deadline.</li>
        <li><strong>Register in the DAAD portal</strong>, download and complete the application form, and upload your documents as PDFs.</li>
        <li>Submit by <strong>23 February 2027</strong> (the portal closes at 24:00 CET/CEST on the last day).</li>
        <li>For technical help: <strong>portal@daad.de</strong>, or the hotline <strong>+49 (0) 228 882-8888</strong>, weekdays 09:00\u201312:00 and 14:00\u201316:00 CET/CEST.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the DAAD Re-Invitation Programme 2027?',
  '23 February 2027 for the next open round (selection June/July 2027, funding from October 2027). The 1 October 2026 round has closed.'),
 ('Who can apply for the DAAD Re-Invitation Programme?',
  'Former DAAD research-grant or study-scholarship holders funded for more than 6 months, or East German (GDR) scholarship holders who studied in Germany for at least 1 year, who have not lived in Germany for at least the last 3 years. If you have never held a DAAD scholarship, you are not eligible.'),
 ('How much does the programme pay?',
  '\u20ac2,000 a month for assistant teachers, assistant professors and lecturers, and \u20ac2,150 a month for professors, plus a travel allowance and health insurance if you are not otherwise insured. The stay lasts 1\u20133 months.'),
 ('Is the programme open to all nationalities?',
  'No \u2014 it is country-restricted. The DAAD database says "Country: Only specified". Third-country applicants and Germans living abroad should contact the responsible DAAD branch or section before applying.'),
 ('Can I renew the stay?',
  'No. The stay is non-renewable and can be claimed only once within three years.'),
 ('What is the difference from the EPOS re-invitation programme?',
  'The EPOS re-invitation programme is a separate scheme for former holders of Development-Related Postgraduate Courses scholarships, with different deadlines and eligibility. It is not covered in this article.')]) + '''
      <p class="verify">Verified 26 Oct 2026: daad.de (official DAAD scholarship database, detail 50015492, opened live) \u2014 next deadline 23 February 2027, 1 October 2026 round closed, \u20ac2,000/\u20ac2,150 monthly rates, 1\u20133 months, once within three years, former DAAD holders funded more than 6 months, not lived in Germany for at least 3 years, country-restricted, documents (CV max 3 pages, project statement max 10 pages, host confirmation), DAAD portal procedure; europescholarships.com, myguide.de \u2014 corroboration. CORRECTION: Bright Scholarship says the deadline is "not specified" / "Open Now" and claims "All Nationalities" \u2014 both wrong against the official page; the 1 October 2026 round has passed and the next open deadline is 23 February 2027. Date pairs seen in search snippets (31.07.2026 / 16.11.2026; 17.08.2026 / 16.11.2026) belong to the separate EPOS re-invitation programme, which is not covered here. No application fee is mentioned on the official page, so none is claimed. The exact list of eligible countries depends on the applicant\u2019s country filter in the DAAD database and cannot be stated as a fixed list.</p>''',
 dl_long='23 February 2027',
 offlinks=[('DAAD \u2014 Re-Invitation Programme (official scholarship database)', 'https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?origin=41&status=2&subjectGrps=&daad=&q=&page=4&detail=50015492'),
           ('Bright Scholarship \u2014 DAAD Re-Invitation Programme 2027', 'https://brightscholarship.com/daad-re-invitation-programme-2027-in-germany/')],
 related_titles=['anhalt-stibet-2027', 'vechta-phd-2027', 'wiko-2027', 'leiden-lexs-2027'])),

# ---------------------------------------------------------------- 4. Eric Bleumink
A.append(dict(
 slug='eric-bleumink-scholarship-2027-netherlands',
 title='Eric Bleumink Scholarship 2027 in Netherlands (Fully Funded)',
 meta='Eric Bleumink Scholarship 2027: an individual grant of \u20ac15,000 for a 1- or 2-year Master\u2019s at the University of Groningen, starting September 2027. Deadline 1 December 2026 \u2014 eligibility, how to apply and FAQs.',
 short='Eric Bleumink Scholarship 2027', kicker='Netherlands \u00b7 Master\u2019s \u00b7 Fully Funded', mono='EB',
 prov_short='University of Groningen', prov_cat='University \u00b7 Netherlands',
 h1='Eric Bleumink Scholarship 2027 in Netherlands (Fully Funded)',
 sub='The Eric Bleumink Scholarship 2027 funds a Master\u2019s at the University of Groningen for students from developing countries: an individual grant of \u20ac15,000 per student, awarded by the Ubbo Emmius Fund. Read the number before the label, because the official source states exactly one figure \u2014 \u20ac15,000 \u2014 and the "fully funded" description comes from secondary sources, not from the fund itself. There is no separate scholarship application: you apply for admission to a Groningen Master\u2019s by 1 December 2026, and the university nominates the best admitted candidates. The deadline is 1 December 2026.',
 dpill='Deadline 1 Dec 2026 \u00b7 %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'An individual grant of \u20ac15,000 per student, per the official Ubbo Emmius Fund page \u2014 the only amount the official source states. Secondary sources describe the award as covering tuition fees, international travel, subsistence and living costs, books and study materials, and health insurance, for the full 1- or 2-year programme. A limited number of awards is made each year; the scheme is highly competitive (around 100 students from 30 countries have received it since 2000). Whether the \u20ac15,000 grant is per year or for the whole programme is not stated on the official page, so neither is asserted here.'),
              ('Eligible', 'A national of an eligible non-Western / developing / low-income country \u2014 more than 60 countries on the fund\u2019s list ("Appendix 1"); examples include India, Nepal, Bangladesh, Nigeria, Ghana, Kenya, Ethiopia and Vietnam. Not "all nationalities". Excellent academic performance and outstanding undergraduate grades, supported by recommendation letters; no specific GPA threshold is published. Provisional or unconditional admission to a Groningen Master\u2019s (MSc, MA, LL.M; all programmes eligible) before February 2027. English proficiency per the chosen programme\u2019s requirements; available for the full programme duration; in good health (for Dutch health insurance); with no other means of financing the studies.'),
              ('How', 'There is no scholarship application. Apply for admission to a Master\u2019s programme at the University of Groningen by 1 December 2026, through the university\u2019s admission portal. The Admission Office, with the faculty admission boards, nominates suitable admitted candidates; a selection committee makes the final choice, and selected candidates are notified directly.'),
              ('Deadline', '1 December 2026 \u2014 the Master\u2019s programme application deadline to be considered for nomination. Admission (provisional or unconditional) must be in place before February 2027. The programme starts in September 2027 only.'),
              ('Fine print', 'Do not use the \u20ac1,100\u2013\u20ac1,300 a month stipend and \u20ac350\u2013\u20ac500 book allowance figures found on some sites \u2014 they are uncorroborated by the official source and look invented. One site\u2019s "\u20ac1500 stipend" headline is almost certainly a typo for \u20ac15,000. Bright Scholarship is wrong on two points: it says "All Nationalities" (the official list is non-Western / developing countries only) and "admission letter by February 2026" (it should be February 2027). The full eligible-country list ("Appendix 1") was not retrieved from an official source \u2014 example countries only are given here, and readers should check the official page for the list. Contact on the official page: Frederika Cazemier, f.cazemier@rug.nl.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Eric Bleumink Scholarship</strong> is awarded by the <strong>Ubbo Emmius Fund</strong> at the <strong>University of Groningen</strong>, for talented students from developing countries to take a Master\u2019s degree in the Netherlands. The fund is named after Eric Bleumink, a former Rector Magnificus of the university, and it has supported around <strong>100 students from 30 countries since 2000</strong>.</p>
      <p>The award is a single figure: an <strong>individual grant of \u20ac15,000 per student</strong>, per the official Ubbo Emmius Fund page. Secondary sources describe it as covering <strong>tuition fees, international travel, subsistence and living costs, books and study materials, and health insurance</strong> for the full one- or two-year programme. The honest way to read those two statements together is this: the official source guarantees \u20ac15,000, and the broader coverage is what trackers report, not what the fund publishes. There is also no separate scholarship form \u2014 the university finds its candidates among admitted Master\u2019s applicants, so the real deadline is the <strong>Master\u2019s application deadline of 1 December 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a national of an <strong>eligible non-Western / developing / low-income country</strong> \u2014 more than 60 countries on the fund\u2019s list ("Appendix 1"); examples include India, Nepal, Bangladesh, Nigeria, Ghana, Kenya, Ethiopia and Vietnam. <strong>Not "all nationalities".</strong></li>
        <li>Show <strong>excellent academic performance</strong> and outstanding undergraduate grades, supported by recommendation letters. <strong>No specific GPA threshold is published.</strong></li>
        <li>Hold <strong>provisional or unconditional admission</strong> to a Groningen Master\u2019s (MSc, MA, LL.M; all programmes eligible) <strong>before February 2027</strong>.</li>
        <li>Meet the <strong>English proficiency</strong> requirements of the chosen programme.</li>
        <li>Be <strong>available for the full programme duration</strong> and in <strong>good health</strong> (for Dutch health insurance).</li>
        <li>Have <strong>no other means of financing</strong> the studies.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>An <strong>individual grant of \u20ac15,000 per student</strong> (official Ubbo Emmius Fund figure).</li>
        <li>Secondary sources describe coverage of <strong>tuition fees, international travel, subsistence and living costs, books and study materials, and health insurance</strong> for the full 1- or 2-year programme.</li>
        <li>A <strong>limited number of awards</strong> each year; highly competitive.</li>
        <li>Note that whether the \u20ac15,000 grant is per year or for the whole programme is <strong>not stated on the official page</strong>, so neither is asserted here.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>There is <strong>no separate scholarship application or document set</strong>. The documents are those of the Master\u2019s admission application:</li>
        <li><strong>Academic transcripts and degree certificates.</strong></li>
        <li>Proof of <strong>English proficiency</strong> (IELTS/TOEFL).</li>
        <li>An updated <strong>CV</strong>.</li>
        <li><strong>Recommendation letters</strong>.</li>
        <li>A <strong>motivation / personal statement</strong>.</li>
        <li>A valid <strong>passport or ID</strong>.</li>
        <li>Any <strong>programme-specific requirements</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>Master\u2019s programme</strong> at the University of Groningen (MSc, MA, LL.M; all programmes are eligible).</li>
        <li>Apply for <strong>admission</strong> through the university\u2019s admission portal by <strong>1 December 2026</strong>.</li>
        <li>Secure <strong>provisional or unconditional admission before February 2027</strong>.</li>
        <li>The <strong>Admission Office, with the faculty admission boards, nominates</strong> suitable admitted candidates; a <strong>selection committee</strong> makes the final choice.</li>
        <li><strong>Selected candidates are notified directly.</strong></li>
        <li>There is <strong>no separate scholarship application</strong> to submit.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Eric Bleumink Scholarship fully funded?',
  'The official Ubbo Emmius Fund page states a single figure: an individual grant of \u20ac15,000 per student. Secondary sources describe it as covering tuition, travel, subsistence, books and insurance for the full programme. This article states the official \u20ac15,000 figure and reports the broader coverage as secondary-source description, not as an official promise.'),
 ('What is the deadline for the Eric Bleumink Scholarship 2027?',
  '1 December 2026 \u2014 the Master\u2019s programme application deadline to be considered for nomination. Admission must be in place before February 2027, and the programme starts in September 2027.'),
 ('Do I need to apply separately for the scholarship?',
  'No. There is no scholarship application. You apply for admission to a Groningen Master\u2019s, and the Admission Office nominates suitable admitted candidates.'),
 ('Who can apply?',
  'Students from eligible non-Western / developing countries (more than 60 countries on the fund\u2019s list) with outstanding undergraduate grades, admitted to a Groningen Master\u2019s, with no other means of financing their studies. It is not open to all nationalities.'),
 ('How much is the grant?',
  '\u20ac15,000 per student, per the official Ubbo Emmius Fund page. Whether that is per year or for the whole programme is not stated on the official page. Monthly stipend figures quoted on some sites (\u20ac1,100\u2013\u20ac1,300 a month) are uncorroborated and are not used here.'),
 ('Which programmes are eligible?',
  'All Master\u2019s programmes at the University of Groningen (MSc, MA, LL.M), for 1 or 2 years, starting September 2027.')]) + '''
      <p class="verify">Verified 26 Oct 2026: uef.nl/projecten/ebf (official Ubbo Emmius Fund page, opened and read in full) \u2014 "an individual grant of \u20ac15,000" per student, contact Frederika Cazemier, f.cazemier@rug.nl; rug.nl FAQ and fellowship-students pages; afterschoolafrica.com, edugist.org, europescholarships.com, daadscholarship.com, opportunitiesforyouth.org \u2014 deadline 1 December 2026, admission before February 2027, September 2027 start, 1- or 2-year Master\u2019s, developing-country eligibility, no separate application, nomination by the Admission Office. CORRECTION: Bright Scholarship says "All Nationalities" (official: non-Western / developing countries only) and "admission letter by February 2026" (should be February 2027) \u2014 neither is used. The \u20ac1,100\u2013\u20ac1,300 a month stipend and \u20ac350\u2013\u20ac500 book allowance figures on some sites are uncorroborated and are not used; one site\u2019s "\u20ac1500 stipend" headline is almost certainly a typo for \u20ac15,000. Whether the \u20ac15,000 grant is per year or for the whole programme is not stated on the official page and is not asserted. The full eligible-country list ("Appendix 1") was not retrieved from an official source \u2014 example countries only are given, and readers should check the official page for the list. The exact Master\u2019s application portal link (Studielink) was not verified in this pass.</p>''',
 dl_long='1 December 2026',
 offlinks=[('Ubbo Emmius Fund \u2014 Eric Bleumink Fund (official)', 'https://uef.nl/projecten/ebf'),
           ('Bright Scholarship \u2014 Eric Bleumink Scholarship 2027', 'https://brightscholarship.com/eric-bleumink-scholarship-2027-netherlands/')],
 related_titles=['leiden-lexs-2027', 'dalarna-2027', 'st-andrews-pg-2027', 'southampton-2027'])),

# ---------------------------------------------------------------- 5. Ontario Graduate Scholarship
A.append(dict(
 slug='ontario-graduate-scholarship-2027-canada',
 title='Ontario Graduate Scholarship 2027 in Canada (Funded)',
 meta='Ontario Graduate Scholarship 2027: CAD $5,000 per term (up to $15,000) for Master\u2019s or PhD study at a participating Ontario university, jointly funded by the Ontario government and the host university. Deadlines vary by university \u2014 earliest confirmed 16 November 2026 (Carleton) \u2014 eligibility, documents, how to apply and FAQs.',
 short='Ontario Graduate Scholarship 2027', kicker='Canada \u00b7 Master\u2019s & PhD \u00b7 Partially Funded', mono='OG',
 prov_short='Government of Ontario', prov_cat='Government \u00b7 Canada',
 h1='Ontario Graduate Scholarship 2027 in Canada (Funded)',
 sub='The Ontario Graduate Scholarship 2027 (OGS) is the Government of Ontario\u2019s merit scholarship for Master\u2019s and PhD students at participating Ontario universities: CAD $5,000 a term, up to $15,000 for three consecutive terms, jointly paid by the province and your university. Two things to understand before you apply. First, there is no single deadline \u2014 each university runs its own competition, and the earliest confirmed deadline is 16 November 2026 at Carleton University. Second, this is partial funding, not full funding, and international students can apply only if they are already studying in Ontario on a valid study permit.',
 dpill='Deadline varies by university \u00b7 earliest 16 Nov 2026',
 facts=facts([('Award', 'CAD $5,000 per term; $10,000 for two consecutive terms; $15,000 for three consecutive terms (maximum one year; minimum two consecutive terms). Jointly funded: the Ontario government pays two-thirds and the host university one-third. This is partial funding \u2014 it does not automatically cover full tuition, accommodation, travel, health insurance or living costs. Support limits: a Master\u2019s student may hold OGS for at most 2 academic years, a doctoral student for at most 4 years, and no student may receive more than 6 years of government-funded graduate awards in a lifetime.'),
              ('Eligible', 'Master\u2019s or PhD study, in all disciplines, at a participating Ontario university (19 universities, including Toronto, Waterloo, McMaster, Queen\u2019s, Ottawa, Western and York). Be a Canadian citizen, Permanent Resident, or Protected Person at the application deadline; international students only if already studying in Ontario on a valid study permit (allotted international awards) \u2014 students living abroad cannot apply directly. Hold a minimum GPA of 10.0 (A\u2212) in each of the last two years of full-time study (Carleton scale; students in the 3rd year or later of graduate study need 10.0 overall on graduate courses). Be enrolled, or intend to enrol, full-time in 2027\u201328 (part-time only for students with a documented disability). Excluded: students in an extension term; students in default on a Canadian government-sponsored student loan; students holding OGS concurrently with SSHRC, NSERC, CIHR, Vanier, QEII-GSST or another OGS.'),
              ('How', 'Through your chosen university \u2014 there is no central provincial application. At Carleton: online through Carleton Central (MC1 credentials) under Awards and Financial Assistance, or a PDF application package submitted to the department\u2019s Graduate Administrator for external applicants. Each university runs its own competition, forms and deadline. Results are notified in April each year.'),
              ('Deadline', 'Varies by university. Confirmed for the 2027\u201328 cycle: Carleton University \u2014 16 November 2026, 11:59 PM EST (applications opened 26 August 2026; referee deadline 2 December 2026); Ontario Tech University \u2014 1 December 2026; Laurentian University \u2014 31 January 2027; University of Toronto Scarborough (Psychology, domestic) \u2014 23 April 2027. Per-university deadlines beyond these four were not individually verified \u2014 check your university\u2019s graduate awards page.'),
              ('Fine print', 'Bright Scholarship is unreliable on the details and was not copied: it claims two letters of recommendation and a health certificate (the official Carleton page says one reference and no health certificate), and it says "All Nationalities" (misleading \u2014 international applicants must already be studying in Ontario on a study permit). A dedicated ontario.ca OGS information page was not located \u2014 the official sources linked below are Carleton\u2019s OGS page and Ontario Regulation 400/00, the legal basis for the award. No ministry-level change to the 2027\u201328 cycle was confirmed, so none is stated.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Ontario Graduate Scholarship (OGS)</strong> is the Government of Ontario\u2019s merit-based scholarship for graduate students, running since the 1970s under <strong>Ontario Regulation 400/00</strong>. It is not a single national competition: each <strong>participating Ontario university</strong> runs its own OGS competition, sets its own deadline, and selects its own recipients, within the province\u2019s rules. The province pays <strong>two-thirds</strong> of each award and the host university pays <strong>one-third</strong>.</p>
      <p>The award is <strong>CAD $5,000 a term</strong> \u2014 $10,000 for two consecutive terms, $15,000 for three \u2014 for a maximum of one year at a time. That is real money towards a graduate degree, but it is <strong>partial funding</strong>: it does not automatically cover full tuition, accommodation, travel, health insurance or living costs. And the deadline you must meet is your university\u2019s, not the province\u2019s \u2014 the earliest confirmed for 2027\u201328 is <strong>16 November 2026 at Carleton University</strong>, and other universities close later, some as late as April 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be enrolled, or intend to enrol, in a <strong>Master\u2019s or PhD</strong> programme, in any discipline, at a <strong>participating Ontario university</strong>.</li>
        <li>Be a <strong>Canadian citizen, Permanent Resident, or Protected Person</strong> at the application deadline; <strong>international students only if already studying in Ontario on a valid study permit</strong> (allotted international awards). Students living abroad <strong>cannot apply directly</strong>.</li>
        <li>Hold a minimum <strong>GPA of 10.0 (A\u2212) in each of the last two years of full-time study</strong> (Carleton scale; students in the 3rd year or later of graduate study need 10.0 overall on graduate courses).</li>
        <li>Be enrolled, or intend to enrol, <strong>full-time in 2027\u201328</strong> (part-time only for students with a documented disability).</li>
        <li><strong>Excluded:</strong> students in an extension term; students in default on a Canadian government-sponsored student loan; students holding OGS concurrently with SSHRC, NSERC, CIHR, Vanier, QEII-GSST or another OGS.</li>
        <li>Support limits: a Master\u2019s student may hold OGS for at most <strong>2 academic years</strong>, a doctoral student for at most <strong>4 years</strong>, and no student may receive more than <strong>6 years</strong> of government-funded graduate awards in a lifetime.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CAD $5,000 per term</strong>; <strong>$10,000</strong> for two consecutive terms; <strong>$15,000</strong> for three consecutive terms (maximum one year; minimum two consecutive terms).</li>
        <li><strong>Jointly funded:</strong> the Ontario government pays two-thirds, the host university one-third.</li>
        <li>Available at <strong>participating Ontario universities</strong> (19 universities, including Toronto, Waterloo, McMaster, Queen\u2019s, Ottawa, Western and York).</li>
        <li>Note that this is <strong>partial funding</strong> \u2014 it does not automatically cover full tuition, accommodation, travel, health insurance or living costs.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Official transcripts</strong> from all undergraduate and graduate studies, up to date (including the fall term of the application year); a <strong>certified translation</strong> if they are not in English or French.</li>
        <li>A <strong>citizenship document</strong> (birth certificate, passport or PR card) <strong>or</strong> a Canadian <strong>study permit</strong> for international applicants.</li>
        <li>The <strong>OGS application form</strong>, <strong>application checklist</strong> and <strong>research / program statement</strong>.</li>
        <li><strong>One academic reference / assessment</strong>, submitted directly by the referee (Carleton referee deadline 2 December 2026).</li>
        <li>Optional: an <strong>awards page</strong> and a <strong>publications page</strong>.</li>
        <li>Note that this list is from the <strong>official Carleton page</strong>. Bright Scholarship\u2019s claim of two letters of recommendation and a health certificate is wrong \u2014 one reference, no health certificate.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>participating Ontario university</strong> and check its OGS deadline \u2014 there is <strong>no central provincial application</strong>.</li>
        <li>At Carleton: apply online through <strong>Carleton Central</strong> (MC1 credentials) under Awards and Financial Assistance, or submit a <strong>PDF application package</strong> to the department\u2019s Graduate Administrator (for external applicants).</li>
        <li>Ask your <strong>referee to submit their assessment directly</strong> (Carleton referee deadline 2 December 2026).</li>
        <li>Submit by <strong>your university\u2019s deadline</strong> \u2014 the earliest confirmed is <strong>16 November 2026, 11:59 PM EST (Carleton)</strong>.</li>
        <li>Results are notified in <strong>April</strong> each year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Ontario Graduate Scholarship 2027?',
  'There is no single deadline \u2014 each university sets its own. Confirmed for 2027\u201328: Carleton University 16 November 2026, 11:59 PM EST; Ontario Tech University 1 December 2026; Laurentian University 31 January 2027; University of Toronto Scarborough (Psychology, domestic) 23 April 2027. Check your university\u2019s graduate awards page.'),
 ('Is the Ontario Graduate Scholarship fully funded?',
  'No. It pays CAD $5,000 a term, up to $15,000 for three consecutive terms, jointly funded by the Ontario government and the host university. It does not automatically cover full tuition, accommodation, travel, health insurance or living costs.'),
 ('Can international students apply for OGS?',
  'Only if they are already studying in Ontario on a valid study permit, under the allotted international awards. Students living abroad cannot apply directly.'),
 ('How much is the OGS worth?',
  'CAD $5,000 per term, $10,000 for two consecutive terms, or $15,000 for three consecutive terms, for a maximum of one year at a time.'),
 ('What GPA do I need?',
  'A minimum of 10.0 (A\u2212) in each of the last two years of full-time study on the Carleton scale. Students in the 3rd year or later of graduate study need 10.0 overall on graduate courses.'),
 ('How do I apply?',
  'Through your chosen university \u2014 there is no central provincial application. At Carleton, apply online through Carleton Central or submit a PDF package to the department\u2019s Graduate Administrator.')]) + '''
      <p class="verify">Verified 26 Oct 2026: gradstudents.carleton.ca/ogs/ (official Carleton OGS page, opened and read in full) \u2014 2027\u201328 cycle, applications opened 26 August 2026, deadline 16 November 2026, 11:59 PM EST, referee deadline 2 December 2026, CAD $5,000 per term ($10,000 / $15,000), one reference, transcripts, citizenship document or study permit, results notified in April; ontario.ca/laws/regulation/r00400 (Ontario Regulation 400/00, opened and read) \u2014 award amounts and legal basis; 9Scholarships, Laurentian University, utsc.utoronto.ca \u2014 Ontario Tech 1 December 2026, Laurentian 31 January 2027, U of T Scarborough Psychology (domestic) 23 April 2027. CORRECTION: Bright Scholarship is unreliable on the details and was not copied \u2014 it claims two letters of recommendation and a health certificate (official: one reference, no health certificate) and says "All Nationalities" (misleading \u2014 international applicants must already be studying in Ontario on a study permit). Per-university deadlines beyond the four cited were not individually verified. A dedicated ontario.ca OGS information page was not located; the official sources are Carleton\u2019s OGS page and Ontario Regulation 400/00. No ministry-level change to the 2027\u201328 cycle was confirmed, so none is stated.</p>''',
 dl_long='16 November 2026 (Carleton University; varies by university)',
 offlinks=[('Carleton University \u2014 Ontario Graduate Scholarship (official)', 'https://gradstudents.carleton.ca/ogs/'),
           ('Ontario Regulation 400/00 \u2014 Graduate Scholarship Awards (official)', 'https://www.ontario.ca/laws/regulation/r00400')],
 related_titles=['manitoba-2026', 'alabama-2027', 'loyola-merit-2027', 'au-egls-2027'])),

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
    json.dump(sizes, open('/tmp/batch52_built.json','w'))

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

#!/usr/bin/env python3
"""Batch 53 (cron run 53, 26 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. UCLouvain Postdoctoral Fellowship 2027 - SKIPPED: deadline passed
   23 Sep 2026, 09:00 Brussels time (official UCLouvain call page).
2. Erasmus Mundus EMHRPP Scholarship 2027 - VERIFIED: real programme,
   deadline TBC (applications opening October 2026; no exact date
   published). EUR 1,000/month + participation costs, 24 months.
   Partner-list conflicts noted; EUR 1,400/month figure belongs to
   other Erasmus Mundus programmes, not EMHRPP.
3. Frontier AI Security Residency 2026 - SKIPPED: deadline passed
   2 Aug 2026; residency itself runs 12 Oct - 4 Dec 2026.
4. Cyprus International University Scholarships 2027 - VERIFIED: open,
   no fixed deadline. Tuition-fee reductions only (50% for all
   international undergraduates; merit 50-100%; graduate CGPA 3.50+).
   CORRECTION: campus is in Nicosia, Northern Cyprus - Bright's
   "Turkey" is shorthand, not the location.
5. Young Leaders Union 2026 - SKIPPED: deadline passed (Bright says
   1 Sep 2026, official page 3 Oct 2026, others 30 Sep 2026 - all
   before today); also charges a GBP 18.75 application fee despite
   the "fully funded" label.
6. Taiwan Government Scholarship 2027 - VERIFIED (MOE Taiwan
   Scholarship): deadline 31 Mar 2027 (1 Feb - 31 Mar window; local
   TECO may close earlier). CORRECTION: Bright's 31 Oct 2026 date,
   TWD 6,000/month, "2,000 awards" and "no acceptance letter needed"
   all contradict the official MOE directions - official figures used.
7. University of Virginia Jefferson Scholarship 2027 - VERIFIED:
   deadline 1 Dec 2026. Fully funded 4-year undergraduate award;
   school nomination is mandatory, students cannot apply directly.
8. Gotoh Tokyu Group Scholarship 2027 - SKIPPED: deadline passed
   25 Sep 2026; Bright's "Turkey" is wrong - it is Tokyo City
   University, Japan.
[wave 2 entries 9-16]
9. European Commission Blue Book Traineeship 2027 - SKIPPED: deadline
   passed 4 Sep 2026, 10:00 Brussels time (March 2027 session); the
   October 2027 session has no confirmed opening date.
10. Murdoch University RTP Scholarships 2027 - SKIPPED: deadline passed
    30 Sep 2026 (round opened 1 Jul 2026).
11. List of Scholarships in Chile Universities 2027 - SKIPPED: listicle
    composite (ANID PhD/Master's, universities, Fulbright/OAS/DAAD,
    private awards - no single scheme, deadline or amount).
12. TU Berlin Scholarships 2027 - SKIPPED: aggregator composite (BAfoeG,
    STIBET, Deutschlandstipendium, DAAD awards, Hilde Domin, DAAD
    Prize and more; "Last date: Varies").
13. UNICEF Traineeship 2027 - VERIFIED: open, rolling - no fixed
    deadline; each vacancy sets its own closing date. Paid internship:
    monthly stipend (amount varies by posting - UNICEF publishes no
    single figure), possible travel/visa contribution, 6-26 weeks.
    "Fully funded" is an overstatement - housing and health insurance
    are not confirmed as covered.
14. Top 10 Slovenia Scholarships without IELTS 2027 - SKIPPED: listicle
    composite (10 unrelated awards, "varies by scholarship").
15. University of Pavia Scholarships 2027 - SKIPPED: aggregator
    composite (EDiSU, Invest Your Talent in Italy, Italian Government
    Scholarships, mobility grants; "Last date: Varies"); its main
    named sub-scheme CICOPS closed 10 Jun 2026.
16. University of Tasmania Research Scholarships 2027 - SKIPPED:
    deadline passed 1 Oct 2026, 11:59 pm AEST.

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
 'ciu-2027': {'mono': 'CIU', 'title': 'Cyprus International University Scholarships 2027 in Northern Cyprus (Funded)',
   'href': 'cyprus-international-university-scholarships-2027.html',
   'dpill': 'No fixed deadline · apply early',
   'award': 'Tuition-fee reductions only: 50% off tuition for all international undergraduates, merit awards of 50–100% off tuition, athletic awards, and graduate awards for CGPA 3.50+. No monthly stipend is officially published.',
   'elig': 'All nationalities; high-school diploma for undergraduate entry, bachelor’s degree for postgraduate entry, CGPA 3.50+ for the graduate scholarship.',
   'tags': [('Undergraduate & Postgraduate', 'blue'), ('Northern Cyprus', 'teal')]},
 'taiwan-moe-2027': {'mono': 'TW', 'title': 'Taiwan Government Scholarship (MOE) 2027 for International Students (Fully Funded)',
   'href': 'taiwan-government-scholarship-2027.html',
   'dpill': 'Deadline 31 Mar 2027 · %d days left' % dl_left('2027-03-31'),
   'award': 'Tuition and miscellaneous fees up to NT$40,000 per semester plus a monthly living allowance of NT$15,000 (Bachelor’s) or NT$20,000 (Master’s/PhD), for up to 4 years (Bachelor’s), 2 years (Master’s) or 4 years (PhD).',
   'elig': 'Foreign nationals only (not ROC citizens, overseas Chinese, or nationals of mainland China, Hong Kong or Macao); excellent academic record; not already receiving a Taiwan government scholarship.',
   'tags': [('Bachelor’s/Master’s/PhD', 'blue'), ('Taiwan', 'teal')]},
 'jefferson-2027': {'mono': 'UVA', 'title': 'University of Virginia Jefferson Scholarship 2027 in USA (Fully Funded)',
   'href': 'university-of-virginia-jefferson-scholarship-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': 'Fully funded 4-year undergraduate award: full tuition and fees, on-campus housing, meals and living costs, books and supplies, plus leadership, research, travel and internship support. Widely reported total value over $405,000 for non-Virginia students.',
   'elig': 'Final-year secondary-school students; school nomination is mandatory — students cannot apply directly or self-nominate; must separately gain admission to UVA.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'emhrpp-2027': {'mono': 'EM', 'title': 'Erasmus Mundus EMHRPP Scholarship 2027 in Europe (Fully Funded)',
   'href': 'erasmus-mundus-emhrpp-scholarship-2027-europe.html',
   'dpill': 'Deadline to be announced',
   'award': 'Fully funded 24-month joint Master’s: €1,000 a month living allowance (€24,000 total) plus full participation costs (€9,000 programme-country / €18,000 partner-country students), travel, visa and relocation support and full health insurance.',
   'elig': 'Bachelor’s degree of at least 180 ECTS in any field plus at least 2 years of practitioner experience in human rights; English at B/6 upper-secondary level or equivalent.',
   'tags': [('Master’s', 'blue'), ('Europe', 'teal')]},
 'unicef-2027': {'mono': 'UN', 'title': 'UNICEF Traineeship 2027 | UNICEF Summer Internship (Paid Internship)',
   'href': 'unicef-traineeship-summer-internship-2027.html',
   'dpill': 'Rolling · no fixed deadline',
   'award': 'Paid internship, 6–26 weeks at UNICEF offices worldwide or remote: a monthly stipend (amount varies by posting — UNICEF publishes no single figure) plus a possible one-off travel/visa contribution where funding allows.',
   'elig': 'Aged 18+; enrolled in an undergraduate, graduate or PhD programme, or graduated within the past 2 years; fluent in English, French or Spanish; no immediate relatives at UNICEF.',
   'tags': [('Internship', 'blue'), ('Worldwide', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Cyprus International University
A.append(dict(
 slug='cyprus-international-university-scholarships-2027',
 title='Cyprus International University Scholarships 2027 in Northern Cyprus (Funded)',
 meta='Cyprus International University Scholarships 2027: a 50% tuition scholarship for all international undergraduates, merit awards of 50–100% off tuition, athletic awards and graduate awards for CGPA 3.50+. No fixed deadline published — eligibility, documents, how to apply and FAQs.',
 short='Cyprus International University Scholarships 2027', kicker='Northern Cyprus · Undergraduate & Postgraduate · Funded', mono='CIU',
 prov_short='Cyprus International University', prov_cat='University · Northern Cyprus',
 h1='Cyprus International University Scholarships 2027 in Northern Cyprus (Funded)',
 sub='Cyprus International University (CIU) in Nicosia offers tuition-fee reductions to international students at every level: every international undergraduate gets 50% off tuition, strong students can earn merit awards of 50–100%, and graduate students with a CGPA of 3.50 or above can qualify for a graduate scholarship. There is no fixed deadline published, so applications stay open — but read the funding honestly first: these are tuition discounts, not a full ride, and no monthly stipend, free housing or airfare is officially published. One more correction before you apply: the campus is in Northern Cyprus, not Turkey as some listings say.',
 dpill='No fixed deadline · apply early',
 facts=facts([('Award', 'Tuition-fee reductions only, per the official CIU fees-and-scholarships page. All international undergraduate students receive a 50% tuition scholarship. Merit-based academic scholarships give 50–100% off tuition. Athletic scholarships are available for national-level and league players. Graduate (Master’s/PhD) scholarships are available to holders of a bachelor’s degree with a CGPA of 3.50 or above. No monthly stipend is officially published.'),
              ('Eligible', 'All nationalities. Undergraduate applicants need a high-school diploma or equivalent. Postgraduate applicants need a bachelor’s degree and transcripts; the graduate scholarship additionally needs a CGPA of 3.50 or above. Athletic scholarship applicants need to be national-level or league players.'),
              ('How', 'Choose a programme on the CIU website, check the admission and scholarship requirements, complete the online application form, upload the required documents and submit through the university portal, then monitor your email and the portal for the decision.'),
              ('Deadline', 'No fixed deadline is published on the official CIU page, and intake dates vary by programme. Apply early, because places and scholarship funds are allocated as applications arrive.'),
              ('Fine print', 'Bright Scholarship places this university in "Turkey" — that is shorthand, not the campus location. CIU’s official address is 99258 Nicosia, North Cyprus, Mersin 10, Türkiye. Monthly stipends (for example 3,000–6,000 TRY), free accommodation, annual airfare, health insurance and book allowances claimed by some aggregators are NOT confirmed on the official page and are not used here. The English requirement is also conflicting across sources — one says no IELTS/TOEFL is needed at first application, another says TOEFL 65 iBT or IELTS 5.5, or a CIU exam on arrival — so it is marked not confirmed and you should check the official page.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Cyprus International University (CIU)</strong> is a private university in <strong>Nicosia, Northern Cyprus</strong>, and its scholarship system is built around tuition-fee reductions rather than cash awards. The headline offer is simple: <strong>every international undergraduate student receives a 50% tuition scholarship</strong>, automatically, on admission. On top of that, the university runs <strong>merit-based academic scholarships of 50–100% off tuition</strong>, <strong>athletic scholarships</strong> for national-level and league players, and <strong>graduate scholarships</strong> for students with a strong undergraduate record.</p>
      <p>That is a real discount, but it is not a full ride. The official page publishes <strong>no monthly stipend, no free accommodation and no airfare</strong>, so you should budget for living costs in Nicosia yourself and treat any aggregator promising stipends or free housing as unconfirmed. There is also <strong>no fixed deadline published</strong>, which makes this a genuinely open application — but also means you should apply early rather than assume the offer will wait.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to students of <strong>all nationalities</strong>.</li>
        <li>For <strong>undergraduate</strong> entry: a <strong>high-school diploma or equivalent</strong>.</li>
        <li>For <strong>postgraduate</strong> entry: a <strong>bachelor’s degree and transcripts</strong>.</li>
        <li>For the <strong>graduate scholarship</strong>: a bachelor’s degree with a <strong>CGPA of 3.50 or above</strong>.</li>
        <li>For the <strong>athletic scholarship</strong>: be a <strong>national-level or league player</strong>.</li>
        <li>The <strong>50% undergraduate tuition scholarship</strong> applies to all international undergraduates on admission.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>50% off tuition</strong> for all international undergraduate students.</li>
        <li><strong>Merit-based academic scholarships of 50–100% off tuition</strong>.</li>
        <li><strong>Athletic scholarships</strong> for national-level and league players.</li>
        <li><strong>Graduate scholarships</strong> for bachelor’s holders with a <strong>CGPA of 3.50 or above</strong>.</li>
        <li>Note that the award is a <strong>tuition-fee reduction only</strong> — no monthly stipend, free accommodation or airfare is officially published.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application form</strong> on the CIU website.</li>
        <li><strong>Academic transcripts</strong> and your <strong>degree certificate</strong> as applicable.</li>
        <li>A <strong>personal statement</strong> and a <strong>CV</strong>.</li>
        <li>A valid <strong>passport or national ID</strong>.</li>
        <li>The signed <strong>CIU Rules and Regulations</strong> documents.</li>
        <li>Any <strong>extra documents CIU requests</strong> for your programme.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>programme on the CIU website</strong> and check its admission and scholarship requirements.</li>
        <li>Complete the <strong>online application form</strong>.</li>
        <li>Upload the required <strong>documents</strong> (transcripts, degree certificate, personal statement, CV, passport or ID, signed Rules and Regulations).</li>
        <li>Submit the application through the <strong>university portal</strong>.</li>
        <li>Monitor your <strong>email and the portal</strong> for the admission and scholarship decision.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Cyprus International University scholarship fully funded?',
  'No. It is a tuition-fee reduction: 50% off tuition for all international undergraduates, merit awards of 50–100% off tuition, athletic awards, and graduate awards for CGPA 3.50+. No monthly stipend, free accommodation or airfare is officially published.'),
 ('What is the deadline for CIU scholarships 2027?',
  'No fixed deadline is published on the official CIU page, and intake dates vary by programme. Apply early, because places and scholarship funds are allocated as applications arrive.'),
 ('Where is Cyprus International University located?',
  'In Nicosia, Northern Cyprus (official address: 99258 Nicosia, North Cyprus, Mersin 10, Türkiye). Listings that say "Turkey" are using shorthand, not the campus location.'),
 ('Do I need IELTS or TOEFL to apply?',
  'Not confirmed. Sources conflict: one says no IELTS/TOEFL is needed at first application, another says TOEFL 65 iBT or IELTS 5.5, or a CIU exam on arrival. Check the official page before you apply.'),
 ('What CGPA do I need for the graduate scholarship?',
  'A bachelor’s degree with a CGPA of 3.50 or above.'),
 ('Does the scholarship cover living costs?',
  'No. The awards are tuition-fee reductions only. Monthly stipends, free accommodation, annual airfare, health insurance and book allowances claimed by some aggregators are not confirmed on the official page.')]) + '''
      <p class="verify">Verified 26 Oct 2026: ciu.edu.tr/en/become-student/international/fees-and-scholarships (official CIU fees-and-scholarships page, opened and read) — 50% tuition scholarship for all international undergraduates, merit-based academic scholarships of 50–100% off tuition, athletic scholarships for national-level / league players, graduate scholarships for bachelor’s holders with CGPA 3.50+, no deadline published; Bright Scholarship and ScholarshipsAds — corroboration. CORRECTION: Bright places CIU in "Turkey" — the campus is in Nicosia, Northern Cyprus (official address 99258 Nicosia, North Cyprus, Mersin 10, Türkiye). NOT USED: monthly stipends (3,000–6,000 TRY), free accommodation, annual airfare, health insurance and book allowances claimed by some aggregators — none is confirmed on the official page. The English requirement is conflicting across sources (no IELTS/TOEFL at first application vs TOEFL 65 iBT / IELTS 5.5 or a CIU exam on arrival) and is marked not confirmed.</p>''',
 dl_long='No fixed deadline published',
 offlinks=[('Cyprus International University — Fees and Scholarships (official)', 'https://ciu.edu.tr/en/become-student/international/fees-and-scholarships'),
           ('Bright Scholarship — Cyprus International University Scholarships 2027', 'https://brightscholarship.com/cyprus-international-university-scholarships-2027/')],
 related_titles=['aalto', 'dundee-ge', 'griffith-vc', 'lincoln-gl'])),

# ---------------------------------------------------------------- 2. Taiwan Government Scholarship (MOE)
A.append(dict(
 slug='taiwan-government-scholarship-2027',
 title='Taiwan Government Scholarship (MOE) 2027 for International Students (Fully Funded)',
 meta='Taiwan Government Scholarship (MOE) 2027: tuition and miscellaneous fees up to NT$40,000 per semester plus NT$15,000 a month (Bachelor’s) or NT$20,000 a month (Master’s/PhD). Deadline 31 March 2027 — eligibility, documents, how to apply and FAQs.',
 short='Taiwan Government Scholarship (MOE) 2027', kicker='Taiwan · Bachelor’s/Master’s/PhD · Fully Funded', mono='TW',
 prov_short='Ministry of Education, Taiwan', prov_cat='Government · Taiwan',
 h1='Taiwan Government Scholarship (MOE) 2027 for International Students (Fully Funded)',
 sub='The Taiwan Government Scholarship — the Ministry of Education (MOE) Taiwan Scholarship — is Taiwan’s main government award for international students: tuition and miscellaneous fees up to NT$40,000 a semester, plus NT$15,000 a month for a Bachelor’s or NT$20,000 a month for a Master’s or PhD, for up to four years. The deadline is 31 March 2027, but your local Taiwan representative office may close earlier, so check it first. And a warning about the listings: several aggregators get this scholarship badly wrong — the wrong deadline, the wrong stipend and the wrong award count — so this article uses only the official MOE directions.',
 dpill='Deadline 31 Mar 2027 · %d days left' % dl_left('2027-03-31'),
 facts=facts([('Award', 'Tuition and miscellaneous fees up to NT$40,000 per semester — the student pays any amount above that. A monthly living allowance of NT$15,000 for Bachelor’s students or NT$20,000 for Master’s and PhD students. Duration: up to 4 years for a Bachelor’s, 2 years for a Master’s, 4 years for a PhD, with a maximum of 5 years in total. Scholarship results are announced by 31 May, and the admission letter is due by 30 June.'),
              ('Eligible', 'Foreign nationals only — not ROC (Taiwan) citizens, not overseas Chinese, and not nationals of mainland China, Hong Kong or Macao. An excellent academic record and good moral character. Not currently enrolled at a Taiwan university (exception: final-year students applying for the next level). Not receiving another Taiwan government scholarship, and not having received one in the last 5 years. For Chinese-taught programmes, TOCFL Level 3 or higher; an English certificate is accepted for English-taught programmes.'),
              ('How', 'Two separate applications are required. (1) Apply to a Taiwan university directly for admission. (2) Apply for the scholarship at the local Taiwan representative office (TECO / ROC mission) in the country of your citizenship. Winning the scholarship does not guarantee university admission — the two decisions are independent.'),
              ('Deadline', '31 March 2027, in principle — the application window runs from 1 February to 31 March 2027. Each local Taiwan representative office (TECO) may set an earlier closing date, so applicants must check their local office.'),
              ('Fine print', 'Bright Scholarship’s page for this award is misleading and was not used for the facts above: it gives a 31 October 2026 deadline, a TWD 6,000 monthly stipend, "2,000 awards" and "no acceptance letter needed" — all four contradict the official MOE directions, which are used here. Bright’s 31 October date appears to come from individual universities’ Spring 2027 admission deadlines, many of which have already passed. Note also that the TaiwanICDF scholarship is a different, separate award (1 December 2026 – 15 March 2027, partner countries only, full tuition plus dormitory and airfare) — do not mix its terms into the MOE award.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Taiwan Government Scholarship</strong>, formally the <strong>MOE Taiwan Scholarship</strong>, is the Ministry of Education’s award for international students who want a degree in Taiwan. It pays <strong>tuition and miscellaneous fees up to NT$40,000 per semester</strong> — you cover any amount above that — plus a <strong>monthly living allowance of NT$15,000 for a Bachelor’s or NT$20,000 for a Master’s or PhD</strong>. The award runs for the length of the degree, up to <strong>4 years for a Bachelor’s, 2 years for a Master’s and 4 years for a PhD</strong>, with a 5-year overall maximum.</p>
      <p>The part that trips applicants up is that there are <strong>two separate applications</strong>: one to a Taiwan university for admission, and one to your local Taiwan representative office for the scholarship. Winning the scholarship does <strong>not</strong> guarantee university admission, and admission does not guarantee the scholarship. And the deadline needs care: the window is <strong>1 February to 31 March 2027</strong>, but your local office (TECO) may close earlier than 31 March, so its date is the one that matters.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>foreign national</strong> — not an ROC (Taiwan) citizen, not an overseas Chinese national, and not a national of <strong>mainland China, Hong Kong or Macao</strong>.</li>
        <li>Have an <strong>excellent academic record</strong> and <strong>good moral character</strong>.</li>
        <li><strong>Not currently enrolled</strong> at a Taiwan university (exception: <strong>final-year students</strong> applying for the next level).</li>
        <li><strong>Not receiving another Taiwan government scholarship</strong>, and not having received one in the <strong>last 5 years</strong>.</li>
        <li>For <strong>Chinese-taught programmes</strong>: <strong>TOCFL Level 3 or higher</strong>. For <strong>English-taught programmes</strong>: an <strong>English certificate</strong> is accepted.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition and miscellaneous fees up to NT$40,000 per semester</strong> (the student pays any excess).</li>
        <li>A monthly living allowance of <strong>NT$15,000 (Bachelor’s)</strong> or <strong>NT$20,000 (Master’s/PhD)</strong>.</li>
        <li>Duration: up to <strong>4 years (Bachelor’s)</strong>, <strong>2 years (Master’s)</strong> or <strong>4 years (PhD)</strong>, maximum <strong>5 years</strong> in total.</li>
        <li>Results are announced by <strong>31 May</strong>, and the admission letter is due by <strong>30 June</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Official transcripts</strong> from your previous studies.</li>
        <li>A <strong>language certificate</strong> (TOCFL or equivalent for Chinese-taught programmes; English certificate for English-taught programmes).</li>
        <li><strong>Two recommendation letters</strong>.</li>
        <li>A <strong>study plan</strong>.</li>
        <li><strong>Proof of application to a Taiwan university</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply to a <strong>Taiwan university directly</strong> for admission.</li>
        <li>Apply for the <strong>scholarship at your local Taiwan representative office (TECO / ROC mission)</strong> in the country of your citizenship.</li>
        <li>Check your <strong>local office’s closing date</strong> — it may be earlier than 31 March 2027.</li>
        <li>Submit both applications within the <strong>1 February – 31 March 2027</strong> window.</li>
        <li>Note that <strong>winning the scholarship does not guarantee university admission</strong> — the two decisions are independent.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Taiwan Government Scholarship 2027?',
  '31 March 2027, in principle — the window runs 1 February to 31 March 2027. Each local Taiwan representative office (TECO) may set an earlier closing date, so check your local office. Do not use the 31 October 2026 date on some aggregator pages; it contradicts the official MOE directions.'),
 ('How much does the Taiwan Government Scholarship pay?',
  'Tuition and miscellaneous fees up to NT$40,000 per semester (you pay any excess), plus NT$15,000 a month for a Bachelor’s or NT$20,000 a month for a Master’s or PhD.'),
 ('Can I apply without an acceptance letter from a Taiwan university?',
  'No — you must apply to a Taiwan university for admission as well as applying for the scholarship at your local representative office. One aggregator’s "no acceptance letter needed" claim contradicts the official directions.'),
 ('Who cannot apply?',
  'ROC (Taiwan) citizens, overseas Chinese, and nationals of mainland China, Hong Kong or Macao; students currently enrolled at a Taiwan university (except final-year students applying for the next level); and anyone already receiving a Taiwan government scholarship or who received one in the last 5 years.'),
 ('Is the TaiwanICDF scholarship the same as this one?',
  'No. TaiwanICDF is a different, separate award (1 December 2026 – 15 March 2027, partner countries only, full tuition plus dormitory and airfare). Do not mix its terms into the MOE award.'),
 ('Do I need TOCFL?',
  'For Chinese-taught programmes, TOCFL Level 3 or higher. For English-taught programmes, an English certificate is accepted.')]) + '''
      <p class="verify">Verified 26 Oct 2026: MOE Taiwan Scholarship Program Directions (official, hosted by National Taiwan Ocean University) — tuition and miscellaneous fees up to NT$40,000 per semester, NT$15,000/month (Bachelor’s) / NT$20,000/month (Master’s/PhD), durations up to 4 / 2 / 4 years (max 5 years), 1 February – 31 March 2027 window with 31 March 2027 deadline, local TECO may close earlier, results by 31 May, admission letter due 30 June, foreign nationals only, TOCFL Level 3 for Chinese-taught programmes; European Funding Guide — 1 February–31 March window; ScholarshipUnion guides — corroboration. CORRECTION: Bright Scholarship’s page is misleading and was not used for the facts — its 31 October 2026 deadline, TWD 6,000/month stipend, "2,000 awards" and "no acceptance letter needed" all contradict the official MOE directions. Bright’s 31 October date appears to come from individual universities’ Spring 2027 admission deadlines, many already passed. TaiwanICDF is a separate scholarship and its terms are not mixed in here.</p>''',
 dl_long='31 March 2027',
 offlinks=[('MOE Taiwan Scholarship Program Directions (official)', 'https://oia.ntou.edu.tw/var/file/22/1022/img/1030/IS-04-MOETaiwanScholarshipGuidelines(2016).pdf'),
           ('Bright Scholarship — Taiwan Government Scholarship 2027', 'https://brightscholarship.com/taiwan-government-scholarship-2027/')],
 related_titles=['swiss-phd', 'jispa-phd', 'jj-wbgsp', 'ubd-grad'])),

# ---------------------------------------------------------------- 3. University of Virginia Jefferson Scholarship
A.append(dict(
 slug='university-of-virginia-jefferson-scholarship-2027-usa',
 title='University of Virginia Jefferson Scholarship 2027 in USA (Fully Funded)',
 meta='University of Virginia Jefferson Scholarship 2027: a fully funded 4-year undergraduate award — full tuition and fees, housing, meals, living costs, books, plus leadership, research and travel support. School nomination is mandatory. Deadline 1 December 2026 — eligibility, how to apply and FAQs.',
 short='University of Virginia Jefferson Scholarship 2027', kicker='USA · Undergraduate · Fully Funded', mono='UVA',
 prov_short='Jefferson Scholars Foundation', prov_cat='Foundation · United States',
 h1='University of Virginia Jefferson Scholarship 2027 in USA (Fully Funded)',
 sub='The Jefferson Scholarship is the University of Virginia’s flagship undergraduate award: four years fully funded — tuition and fees, housing, meals, living costs and books — plus leadership programmes, research support and international travel. It is also one of the hardest awards to enter, because you cannot apply for it yourself. Your school must nominate you, and you must separately win admission to UVA. Counsellor and nominee materials are due by 1 December 2026, and your school may set an earlier internal deadline, so the first step is a conversation with your counsellor — not a form.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'Fully funded for 4 years (8 semesters): full tuition and fees, on-campus housing, meals and living costs, books and supplies, plus leadership and citizenship programmes, undergraduate research support, international travel, internships and conferences, and career and alumni networking. The total value is widely reported as more than $405,000 for non-Virginia / international students (about $83,000 a year) — that figure is corroborated by several aggregators but was not stated on the official FAQ page retrieved, so it is presented as the widely reported figure, not as an official quote.'),
              ('Eligible', 'Final-year secondary-school students in their graduating class, with outstanding academics plus leadership and community engagement. School nomination is mandatory — students cannot apply directly or self-nominate. You must separately apply for and gain admission to UVA: nomination does not guarantee admission, and admission does not guarantee the scholarship. All nationalities. No minimum GPA is published. SAT/ACT scores are not considered for the scholarship. There is no IELTS requirement for the scholarship itself, but UVA’s English-language requirements still apply.'),
              ('How', 'Ask your school counsellor or principal whether your school participates and seek nomination — schools may set earlier internal deadlines. If nominated, complete the Foundation’s counsellor and nominee materials. Separately apply to UVA for admission. If shortlisted, attend regional and final interviews (final interviews are in late February 2027, per one source).'),
              ('Deadline', '1 December 2026 — counsellor and nominee materials are due that date, per the official Jefferson Scholars Foundation FAQ. Your school may set an earlier internal deadline.'),
              ('Fine print', 'The separate Walentas Scholarship is for first-generation students and is US-schools only for nomination — it is not this award. No specific official document list was found: Bright lists a generic form / transcripts / CV / personal-statement set, but the official process speaks of counsellor and nominee materials supplied by the Foundation after nomination, so Bright’s generic list is not presented as the official document list.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Jefferson Scholarship</strong>, run by the <strong>Jefferson Scholars Foundation</strong>, is the University of Virginia’s most prestigious undergraduate award — a <strong>fully funded four-year</strong> package covering <strong>tuition and fees, on-campus housing, meals and living costs, and books and supplies</strong>, with <strong>leadership and citizenship programmes, undergraduate research support, international travel, internships, conferences and career and alumni networking</strong> on top. The total value is widely reported at <strong>more than $405,000 for non-Virginia students</strong> over four years — a figure corroborated by several aggregators, though not stated on the official FAQ page retrieved, so it is presented here as the widely reported figure rather than an official quote.</p>
      <p>What makes this award different from most scholarships is the entry route: <strong>you cannot apply for it yourself</strong>. Your school must nominate you, and nomination alone is not enough — you must also win <strong>admission to the University of Virginia</strong> through the normal admissions process. The two decisions are independent. That means the real deadline is not just 1 December 2026 for the Foundation’s materials; it is also whatever <strong>internal deadline your school sets</strong> for choosing its nominees.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>final-year secondary-school student</strong> in your graduating class.</li>
        <li>Show <strong>outstanding academics</strong> plus <strong>leadership and community engagement</strong>.</li>
        <li>Be <strong>nominated by your school</strong> — nomination is mandatory; students <strong>cannot apply directly or self-nominate</strong>.</li>
        <li>Separately <strong>apply for and gain admission to the University of Virginia</strong> — nomination does not guarantee admission, and admission does not guarantee the scholarship.</li>
        <li>Open to <strong>all nationalities</strong>.</li>
        <li><strong>No minimum GPA</strong> is published. <strong>SAT/ACT scores are not considered</strong> for the scholarship.</li>
        <li>There is <strong>no IELTS requirement for the scholarship itself</strong>, but UVA’s <strong>English-language requirements</strong> still apply.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and fees</strong> for 4 years (8 semesters).</li>
        <li><strong>On-campus housing, meals and living costs</strong>, plus <strong>books and supplies</strong>.</li>
        <li><strong>Leadership and citizenship programmes</strong>.</li>
        <li><strong>Undergraduate research support</strong> and <strong>international travel</strong>.</li>
        <li><strong>Internships, conferences</strong> and <strong>career and alumni networking</strong>.</li>
        <li>Note that the widely reported total value of <strong>more than $405,000</strong> for non-Virginia students was <strong>not</strong> stated on the official FAQ page retrieved.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Counsellor and nominee materials</strong> supplied by the Jefferson Scholars Foundation after nomination — these are the official materials, and they are due by <strong>1 December 2026</strong>.</li>
        <li>Your <strong>UVA admission application</strong>, submitted separately.</li>
        <li>Note that no specific official document list was found: Bright’s generic list (form, transcripts, CV, personal statement) is <strong>not</strong> presented here as the official list.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Ask your <strong>school counsellor or principal</strong> whether your school participates, and <strong>seek nomination</strong>.</li>
        <li>Note that your school may set an <strong>earlier internal deadline</strong> for choosing nominees.</li>
        <li>If nominated, complete the Foundation’s <strong>counsellor and nominee materials</strong> by <strong>1 December 2026</strong>.</li>
        <li>Separately <strong>apply to UVA for admission</strong>.</li>
        <li>If shortlisted, attend <strong>regional and final interviews</strong> (final interviews are in late February 2027, per one source).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I apply for the Jefferson Scholarship myself?',
  'No. School nomination is mandatory — students cannot apply directly or self-nominate. Ask your school counsellor or principal whether your school participates.'),
 ('What is the deadline for the Jefferson Scholarship 2027?',
  '1 December 2026 — counsellor and nominee materials are due that date, per the official Jefferson Scholars Foundation FAQ. Your school may set an earlier internal deadline.'),
 ('Is the Jefferson Scholarship fully funded?',
  'Yes. It covers full tuition and fees, on-campus housing, meals and living costs, books and supplies for 4 years, plus leadership, research, travel and internship support. The widely reported total value of more than $405,000 for non-Virginia students was not stated on the official FAQ page retrieved.'),
 ('Does nomination guarantee admission to UVA?',
  'No. You must separately apply for and gain admission to UVA. Nomination does not guarantee admission, and admission does not guarantee the scholarship.'),
 ('Is there a minimum GPA or SAT/ACT requirement?',
  'No minimum GPA is published, and SAT/ACT scores are not considered for the scholarship. There is no IELTS requirement for the scholarship itself, but UVA’s English-language requirements still apply.'),
 ('What is the Walentas Scholarship?',
  'A separate Jefferson Scholars Foundation award for first-generation students, with nomination limited to US schools. It is not the Jefferson Scholarship covered in this article.')]) + '''
      <p class="verify">Verified 26 Oct 2026: jeffersonscholars.org/scholarships/walentas-faqs (official Jefferson Scholars Foundation FAQ, opened and read) — counsellor and nominee materials due 1 December 2026, school nomination mandatory, students cannot apply directly, separate UVA admission required, final-year students, leadership and community engagement, no minimum GPA published, SAT/ACT not considered; Bright Scholarship and ScholarshipUnion — corroboration, including the widely reported total value of more than $405,000 for non-Virginia students (about $83,000 a year), which was NOT stated on the official FAQ page retrieved and is presented as the widely reported figure, not an official quote. NOT USED: Bright’s generic document list (form, transcripts, CV, personal statement) — the official process speaks of counsellor and nominee materials supplied by the Foundation after nomination. Final interviews in late February 2027 are from one source only.</p>''',
 dl_long='1 December 2026',
 offlinks=[('Jefferson Scholars Foundation — Scholarships FAQ (official)', 'https://www.jeffersonscholars.org/scholarships/walentas-faqs'),
           ('Bright Scholarship — University of Virginia Jefferson Scholarship', 'https://brightscholarship.com/university-of-virginia-jefferson-scholarship/')],
 related_titles=['dayton-merit', 'alabama-2027', 'loyola-merit-2027', 'manitoba-2026'])),

# ---------------------------------------------------------------- 4. Erasmus Mundus EMHRPP
A.append(dict(
 slug='erasmus-mundus-emhrpp-scholarship-2027-europe',
 title='Erasmus Mundus EMHRPP Scholarship 2027 in Europe (Fully Funded)',
 meta='Erasmus Mundus EMHRPP Scholarship 2027 (Human Rights Policy and Practice): a fully funded 24-month joint Master’s — €1,000 a month plus full participation costs, travel and insurance. Deadline to be announced; applications opening October 2026 — eligibility, documents, how to apply and FAQs.',
 short='Erasmus Mundus EMHRPP Scholarship 2027', kicker='Europe · Master’s · Fully Funded', mono='EM',
 prov_short='University of Gothenburg', prov_cat='University · Sweden (Erasmus Mundus consortium)',
 h1='Erasmus Mundus EMHRPP Scholarship 2027 in Europe (Fully Funded)',
 sub='The Erasmus Mundus Master’s in Human Rights Policy and Practice (EMHRPP) is a fully funded 24-month joint Master’s for people who already work in human rights: €1,000 a month, full participation costs, travel and relocation support and health insurance. It is not a scholarship for fresh graduates with only academic interest — you need at least two years of practitioner experience. And one honest warning before you plan around it: no exact deadline has been published yet. Applications are expected to open in October 2026, but the closing date is still to be announced, so this article gives you everything else and tells you where to watch for the date.',
 dpill='Deadline to be announced',
 facts=facts([('Award', 'Fully funded for 24 months: a €1,000 a month living allowance (€24,000 in total) plus full participation costs — €9,000 for EU / programme-country students and €18,000 for partner-country / international students — travel, visa and relocation support in two instalments, and full health insurance. These figures are corroborated by Bright Scholarship and a second aggregator but were NOT confirmed on the official Gothenburg programme page retrieved — do not treat them as an official quote.'),
              ('Eligible', 'A bachelor’s degree of at least 180 ECTS in any field. At least 2 years of practitioner experience in human rights — paid work, an internship or volunteering. English at B/6 upper-secondary level or an equivalent test. Open to third-country and EU/EEA students. Fresh graduates with only academic interest are not the target group.'),
              ('How', 'Apply through the Swedish University Admissions portal (universityadmissions.se) for the Gothenburg-led programme, and submit the separate Erasmus Mundus scholarship form from the Costs and Scholarships page with the programme application. Assessment is by the Gothenburg Joint Admission Committee.'),
              ('Deadline', 'To be announced. Bright says "Open Now" and that applications "will be started in October 2026" with no date; a second source says the next call opens in October 2026 at the earliest and exact dates will be announced when it opens; a third says applications open 16 October 2026, with the deadline TBC. The programme starts in August 2027. No exact deadline is printed here because none has been published.'),
              ('Fine print', 'The partner list conflicts across sources: some list Gothenburg, Pablo de Olavide (Spain), Roehampton (UK) and NTNU (Norway); another lists Deusto (Spain) and the Arctic University of Norway instead — no definitive partner list is stated here. Do not use the €1,400 a month figure seen for other Erasmus Mundus programmes; that is not the EMHRPP figure. The official Gothenburg programme page confirms the programme and the joint degree, but the official Costs and Scholarships page and the 2027 deadline could not be located on it in this search.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Erasmus Mundus Master’s in Human Rights Policy and Practice (EMHRPP)</strong> is a two-year joint Master’s run by a consortium of European universities and led by the <strong>University of Gothenburg</strong> in Sweden. It is designed for people who already work in human rights — practitioners, not fresh graduates — and it combines study at the partner universities with a practice-based approach to human rights policy.</p>
      <p>The funding, as reported by two aggregators, is genuinely full: a <strong>€1,000 a month living allowance</strong>, <strong>full participation costs</strong> (€9,000 for EU / programme-country students, €18,000 for partner-country / international students), <strong>travel, visa and relocation support</strong> and <strong>full health insurance</strong> for 24 months. Those figures were not confirmed on the official Gothenburg page retrieved, so they are presented as reported, not as an official quote. What is certain is the shape of the programme — and the fact that the <strong>deadline has not been published yet</strong>. Applications are expected to open in October 2026, with the programme starting in August 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>bachelor’s degree of at least 180 ECTS</strong> in any field.</li>
        <li>Have at least <strong>2 years of practitioner experience in human rights</strong> — paid work, an internship or volunteering.</li>
        <li>Show English at <strong>B/6 upper-secondary level</strong> or an equivalent test.</li>
        <li>Open to <strong>third-country and EU/EEA students</strong>.</li>
        <li>Note that <strong>fresh graduates with only academic interest are not the target group</strong> — practitioner experience is required.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>€1,000 a month living allowance</strong> (€24,000 over 24 months).</li>
        <li><strong>Full participation costs</strong>: €9,000 (EU / programme-country students) or €18,000 (partner-country / international students).</li>
        <li><strong>Travel, visa and relocation support</strong> in two instalments.</li>
        <li><strong>Full health insurance</strong>.</li>
        <li>Note that these figures are corroborated by two aggregators but were <strong>not confirmed on the official Gothenburg page</strong> retrieved.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application</strong> via the Swedish University Admissions portal.</li>
        <li><strong>Transcripts</strong> and your <strong>degree certificate</strong>.</li>
        <li>A <strong>CV</strong>.</li>
        <li>A <strong>motivation letter on the official template</strong>.</li>
        <li><strong>Two recommendation letters</strong>.</li>
        <li><strong>Proof of work experience</strong> and <strong>proof of residence</strong>.</li>
        <li>An <strong>English certificate</strong>.</li>
        <li>The separate <strong>Erasmus Mundus scholarship form</strong> from the Costs and Scholarships page.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply through <strong>universityadmissions.se</strong> for the Gothenburg-led programme.</li>
        <li>Submit the separate <strong>Erasmus Mundus scholarship form</strong> from the Costs and Scholarships page with the programme application.</li>
        <li>Watch the <strong>official Gothenburg programme page</strong> for the call opening and the deadline, which have not been published yet.</li>
        <li>Assessment is by the <strong>Gothenburg Joint Admission Committee</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the EMHRPP Scholarship 2027?',
  'To be announced. Applications are expected to open in October 2026, with the programme starting in August 2027, but no exact deadline has been published. Watch the official Gothenburg programme page for the announcement.'),
 ('Is the EMHRPP Scholarship fully funded?',
  'Yes, as reported by two aggregators: €1,000 a month living allowance, full participation costs, travel, visa and relocation support and full health insurance for 24 months. These figures were not confirmed on the official Gothenburg page retrieved.'),
 ('Can fresh graduates apply?',
  'Not as the target group. You need at least 2 years of practitioner experience in human rights — paid work, an internship or volunteering — on top of a bachelor’s degree.'),
 ('Which universities are in the EMHRPP consortium?',
  'Not stated definitively here: sources conflict. Some list Gothenburg, Pablo de Olavide (Spain), Roehampton (UK) and NTNU (Norway); another lists Deusto (Spain) and the Arctic University of Norway instead. Check the official page.'),
 ('How do I apply?',
  'Through the Swedish University Admissions portal (universityadmissions.se) for the Gothenburg-led programme, with the separate Erasmus Mundus scholarship form submitted alongside the programme application.'),
 ('Is the stipend €1,400 a month?',
  'No. The €1,400 a month figure belongs to other Erasmus Mundus programmes, not EMHRPP. The EMHRPP living allowance reported by two aggregators is €1,000 a month.')]) + '''
      <p class="verify">Verified 26 Oct 2026: studentportal.gu.se/en/programme/erasmus-mundus-masters-programme-in-human-rights-policy-and-practice (official University of Gothenburg programme page, opened and read) — confirms the programme and the joint degree; Bright Scholarship and ScholarshipUnion / Scholarships.af — €1,000/month living allowance (€24,000 total), participation costs €9,000 (programme-country) / €18,000 (partner-country), travel/visa/relocation in two instalments, full health insurance, bachelor’s of at least 180 ECTS, 2 years of practitioner experience, English B/6, applications opening October 2026, deadline TBC, programme starting August 2027. NOT CONFIRMED on the official page retrieved: the award figures and the official Costs and Scholarships page and 2027 deadline could not be located on it in this search — the figures are presented as reported by two aggregators, not as an official quote. NOT USED: the €1,400/month figure (other Erasmus Mundus programmes, not EMHRPP). Partner list conflicts across sources (Gothenburg / Pablo de Olavide / Roehampton / NTNU vs Deusto / Arctic University of Norway) — no definitive list is stated.</p>''',
 dl_long='To be announced',
 offlinks=[('University of Gothenburg — EMHRPP programme (official)', 'https://studentportal.gu.se/en/programme/erasmus-mundus-masters-programme-in-human-rights-policy-and-practice'),
           ('Bright Scholarship — Erasmus Mundus EMHRPP Scholarship 2027', 'https://brightscholarship.com/erasmus-mundus-emhrpp-scholarship-2027/')],
 related_titles=['jj-wbgsp', 'swiss-phd', 'hanns-seidel', 'ieg-mainz'])),

# ---------------------------------------------------------------- 5. UNICEF Traineeship
A.append(dict(
 slug='unicef-traineeship-summer-internship-2027',
 title='UNICEF Traineeship 2027 | UNICEF Summer Internship (Paid Internship)',
 meta='UNICEF Traineeship 2027: a paid internship at UNICEF offices worldwide or remote — monthly stipend (amount varies by posting), 6–26 weeks, open throughout the year with each vacancy setting its own closing date. Eligibility, documents, how to apply and FAQs.',
 short='UNICEF Traineeship 2027', kicker='Worldwide · Internship · Paid', mono='UN',
 prov_short='UNICEF', prov_cat='United Nations · Worldwide',
 h1='UNICEF Traineeship 2027 | UNICEF Summer Internship (Paid Internship)',
 sub='The UNICEF Traineeship — the UNICEF internship programme — is a paid internship at UNICEF offices around the world, or remote for some roles, lasting 6 to 26 weeks. It is open throughout the year: there is no single deadline, because every vacancy sets its own closing date and new posts appear continuously. Two things to get straight before you apply. First, the stipend is real but its amount varies by posting — UNICEF publishes no single universal figure, so any listing quoting a flat monthly amount is wrong. Second, "fully funded" is an overstatement: housing and health insurance are not confirmed as covered, so budget for them yourself.',
 dpill='Rolling · no fixed deadline',
 facts=facts([('Award', 'Paid internship: a monthly stipend — the amount varies by vacancy, because UNICEF does not publish a single universal figure; one source wrongly cites a flat US$1,000 a month, which is not used here — plus a possible one-off contribution towards travel and visa costs where funding allows, and visa supporting documents where required. Duration is normally 6–26 weeks, full-time or part-time, at UNICEF offices worldwide or remote / hybrid for some roles. Housing and health insurance are not confirmed as covered.'),
              ('Eligible', 'Aged at least 18. Currently enrolled in an undergraduate, graduate or PhD programme, or graduated within the past two years. A strong academic record. Fluent in at least one UNICEF working language (English, French or Spanish), plus the working language of the host office where required. No immediate relatives working at UNICEF or in the applicant’s reporting line. Relevant work or volunteer experience is an advantage. Individual vacancies may add degree or skill requirements.'),
              ('How', 'Go to the official UNICEF careers / internships page, browse open internship vacancies by field or region, pick a role matching your background, register or log in on the UNICEF recruitment portal, upload your documents and submit for that specific vacancy. Only shortlisted candidates are contacted.'),
              ('Deadline', 'No fixed deadline — open throughout the year. Each individual vacancy sets its own closing date, and new posts appear continuously, so check the official internships page for the vacancy you want.'),
              ('Fine print', 'Do not use the flat US$1,000 a month figure quoted by one source — UNICEF publishes no single universal stipend amount; the amount varies by posting. "Fully funded" in the aggregator sense is an overstatement: housing and health insurance are not confirmed as covered, and the travel/visa contribution is a possible one-off where funding allows, not a guarantee. The "Summer Internship" label is seasonal branding for one intake window — the programme itself runs year-round.')]),
 body='''
      <h2 id="about">About the traineeship</h2>
      <p>The <strong>UNICEF Traineeship</strong> — UNICEF’s <strong>internship programme</strong> — places students and recent graduates in <strong>UNICEF offices worldwide</strong>, with some roles <strong>remote or hybrid</strong>. Internships normally last <strong>6 to 26 weeks</strong>, full-time or part-time, and cover UNICEF’s whole range of work, from health and education to data, communications, supply and emergency response.</p>
      <p>It is a <strong>paid</strong> internship: you receive a <strong>monthly stipend</strong>, and there may be a one-off contribution towards <strong>travel and visa costs</strong> where funding allows. But the amount is not fixed — UNICEF publishes <strong>no single universal figure</strong>, and it varies by posting, so do not plan around a number from an aggregator. The programme is also <strong>open throughout the year</strong>: there is no single deadline, because each vacancy sets its own closing date and new posts appear continuously. The vacancy you want is the one whose date matters.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be aged <strong>at least 18</strong>.</li>
        <li>Be currently <strong>enrolled in an undergraduate, graduate or PhD programme</strong>, or have <strong>graduated within the past two years</strong>.</li>
        <li>Have a <strong>strong academic record</strong>.</li>
        <li>Be <strong>fluent in at least one UNICEF working language</strong> (English, French or Spanish), plus the <strong>working language of the host office</strong> where required.</li>
        <li>Have <strong>no immediate relatives working at UNICEF</strong> or in your reporting line.</li>
        <li><strong>Relevant work or volunteer experience</strong> is an advantage.</li>
        <li>Note that <strong>individual vacancies may add degree or skill requirements</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly stipend</strong> — the amount varies by posting; UNICEF publishes no single universal figure.</li>
        <li>A possible <strong>one-off contribution towards travel and visa costs</strong> where funding allows.</li>
        <li><strong>Visa supporting documents</strong> where required.</li>
        <li>Work at a <strong>UNICEF office worldwide</strong>, or <strong>remote / hybrid</strong> for some roles.</li>
        <li>Duration normally <strong>6–26 weeks</strong>, full-time or part-time.</li>
        <li>Note that <strong>housing and health insurance are not confirmed as covered</strong> — "fully funded" is an overstatement.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An updated <strong>CV / résumé</strong>.</li>
        <li>A <strong>cover letter or personal statement</strong>.</li>
        <li>An <strong>academic transcript</strong> or proof of enrolment / graduation.</li>
        <li><strong>Recommendation letters</strong> where requested.</li>
        <li>A valid <strong>ID / passport</strong> where requested.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the official <strong>UNICEF careers / internships page</strong>.</li>
        <li>Browse open <strong>internship vacancies</strong> by field or region.</li>
        <li>Pick a role matching your <strong>background</strong>.</li>
        <li><strong>Register or log in</strong> on the UNICEF recruitment portal.</li>
        <li>Upload your <strong>documents</strong> and submit for that <strong>specific vacancy</strong>.</li>
        <li>Note that <strong>only shortlisted candidates are contacted</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the UNICEF Traineeship 2027?',
  'There is no fixed deadline — the programme is open throughout the year. Each individual vacancy sets its own closing date, and new posts appear continuously, so check the official internships page for the vacancy you want.'),
 ('Is the UNICEF internship paid?',
  'Yes. It pays a monthly stipend, plus a possible one-off contribution towards travel and visa costs where funding allows. The stipend amount varies by posting — UNICEF publishes no single universal figure.'),
 ('How much is the UNICEF internship stipend?',
  'Not published as a single figure. UNICEF does not publish a universal stipend amount; it varies by vacancy. One source’s flat US$1,000 a month figure is wrong and is not used here.'),
 ('Is the UNICEF Traineeship fully funded?',
  'Not in the full sense. It pays a monthly stipend and may contribute to travel and visa costs, but housing and health insurance are not confirmed as covered.'),
 ('Who can apply?',
  'Anyone aged at least 18 who is currently enrolled in an undergraduate, graduate or PhD programme, or who graduated within the past two years, with a strong academic record and fluency in at least one UNICEF working language (English, French or Spanish). No immediate relatives working at UNICEF or in your reporting line.'),
 ('Is it only a summer internship?',
  'No. "Summer Internship" is seasonal branding for one intake window — the programme itself runs year-round, with vacancies appearing continuously.')]) + '''
      <p class="verify">Verified 26 Oct 2026: unicef.org/careers/internships (official UNICEF internships page) — paid internships, 6–26 weeks, open throughout the year, each vacancy with its own closing date, vacancies at jobs.unicef.org; Bright Scholarship, NDTV Education, SightsInPlus — corroboration, including eligibility (18+, enrolled or graduated within 2 years, strong academic record, English/French/Spanish, no immediate relatives at UNICEF) and the application route via the UNICEF recruitment portal. NOT USED: the flat US$1,000 a month stipend figure quoted by one source — UNICEF publishes no single universal amount; the amount varies by posting. "Fully funded" is an overstatement — housing and health insurance are not confirmed as covered, and the travel/visa contribution is a possible one-off where funding allows, not a guarantee.</p>''',
 dl_long='Rolling — no fixed deadline',
 offlinks=[('UNICEF — Internships (official)', 'https://www.unicef.org/careers/internships'),
           ('Bright Scholarship — UNICEF Traineeship 2027', 'https://brightscholarship.com/unicef-traineeship-summer-internship-2027/')],
 related_titles=['swiss-phd', 'epfl-summer', 'hanns-seidel', 'jj-wbgsp'])),

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
    json.dump(sizes, open('/tmp/batch53_built.json','w'))

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

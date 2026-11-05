#!/usr/bin/env python3
"""Batch 56 (cron run 56, 27 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Florida State University Scholarships 2027 - VERIFIED (family of
   awards; operative deadline 1 Dec 2026; Presidential $42,000 + waiver;
   Vires $16,000; IB Diploma $8,000; Stamps full-ride x5; Benacquisto
   is Florida-resident only per official FSU page).
2. KWI Institute Fellowship 2027 - SKIPPED: deadline passed 17 Aug 2026
   (6-month fellowship 1 Apr-30 Sep 2027; EUR 3,000/month).
3. List of Universities to Study in Ireland Without IELTS 2027 -
   SKIPPED: listicle, not a single scheme.
4. Merck International Research Scholarship 2026 - SKIPPED: deadline
   passed 31 Aug 2026 (Merck Research Grants, up to EUR 500,000/yr).
5. Top 40 Europe Scholarships for 2027 Without IELTS - SKIPPED:
   listicle, not a single scheme.
6. Shenzhen University Graduate Research Opportunities 2026 -
   VERIFIED as the live March 2027 PhD intake: 10 Oct-30 Nov 2026;
   Liyuan tuition waiver + CNY 4,000-6,000/month; supervisor
   recommendation letter required before applying.
7. Bond University HDR Scholarship 2027 - SKIPPED: deadline passed
   30 Sep 2026 (BUPRS window 1 Aug-30 Sep 2026).
8. Zayed University Merit Scholarship 2026 - SKIPPED: 2026 cycle
   closed; no open application window verified (deadline "not
   specified" on every source; one roundup lists June 2026).
9. US Fulbright Student Program 2027 - SKIPPED: deadline passed
   6 Oct 2026 (national deadline; 2027-28 cycle for grant year
   2028-29 not yet open).
10. PSU Research Internship at CABI-SEA 2026 - SKIPPED: deadline
    passed 20 Jul 2026.
11. University of Florence PEGASO Scholarships 2026 - SKIPPED:
    deadline passed 6 Aug 2026 (42nd cycle, EUR 16,243/yr).
12. Discover Canada Winter Edition 2026 - SKIPPED: deadline passed
    30 Aug 2026.
13. Malaysian International Scholarship MIS 2026 - SKIPPED: deadline
    passed 3 Apr 2026; official MOHE page confirms 2026/27 closed.
14. Ireland Kader Asmal Fellowships 2027 - SKIPPED: deadline passed
    27 Jul 2026 (Stage 1).
15. Max Planck Doucet Scholarship 2027 - SKIPPED: deadline passed
    15 Sep 2026 (3-month stay, EUR 1,365/month).
16. Jiangxi Province Government Scholarship 2027 - SKIPPED: deadline
    passed 20 Aug 2026 (RMB 25,000/20,000/6,000 by class).
17. Climate Tech Fellowship 2026 - SKIPPED: deadline passed 1 Aug
    2026 (NY Climate Exchange, USD 10,000 stipend).
18. IKEA Internship Program 2026 - SKIPPED: no single verified
    scheme; Bengaluru posting closed 14 Oct 2026; IKEA India states
    it offers no internships.
19. University of Silesia Scholarship 2026-27 - SKIPPED: deadline
    passed 30 Sep 2026.
20. International Student Festival 2027 in Norway (ISFiT) - SKIPPED:
    deadline passed 2 Aug 2026.
21. Charles Darwin University RTP Scholarship 2027 - SKIPPED:
    international deadline passed 30 Sep 2026 (domestic 31 Oct 2026
    only; process now invitation-only per one source).
22. 11 Universities offering Entrance Scholarships in Canada 2027 -
    SKIPPED: listicle, not a single scheme.
23. Yale University Scholarships 2027 - VERIFIED: need-blind for all
    applicants worldwide, meets 100% of demonstrated need, average
    need-based scholarship $75,220/yr; Regular Decision 2 Jan 2027,
    aid documents 15 Feb 2027.
24. Singapore AI Safety Fellowship 2026 - SKIPPED: deadline passed
    10 Jul 2026 (SASH, SGD 5,000/month).
25. Yale Emerging Climate Leaders Fellowship 2027 - SKIPPED:
    deadline passed 30 Jul 2026.
26. Europe Scholarships for International Students 2027 - SKIPPED:
    listicle, not a single scheme.
27. KPMG Global Internship Program 2026 - not scanned (queue order
    resumes here next run; only the next candidates were checked).
28. 120 JSPS Postdoctoral Fellowship 2027 - VERIFIED: Standard
    Program, 2nd open-call round closes 23 Apr 2027, 5pm JST;
    ~120 fellowships per round; JPY 362,000/month.
29. Victoria University of Wellington Scholarships 2027 - VERIFIED
    (family): UG International NZ$15,000 / PG NZ$10,000 automatic on
    the offer; Wellington Doctoral NZ$32,000/yr + domestic fees,
    ~110/yr, next round 1 Nov 2026. Tongarewa discontinued 2026.

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
 'fsu-2027': {'mono': 'FS', 'title': 'Florida State University Scholarships 2027 in USA (Funded)',
   'href': 'florida-state-university-scholarships-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': 'A family of awards, not one prize: a 100% out-of-state tuition waiver (about $15,888 a year, about $63,555 over four years), Presidential Scholars $42,000 plus the waiver, Vires $16,000, IB Diploma $8,000, and five full-ride Stamps Scholarships. All admitted first-year students are automatically considered.',
   'elig': 'New international first-year students are automatically considered for the out-of-state tuition waiver; strong academics (typically no grades below B) and ACT/CLT/SAT scores are required for first-year admission.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'szu-phd-2027': {'mono': 'SZ', 'title': 'Shenzhen University PhD Scholarships 2027 in China (March Intake)',
   'href': 'shenzhen-university-phd-scholarships-2027-china.html',
   'dpill': 'Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
   'award': 'Liyuan International Scholarship: full tuition waiver plus CNY 4,000–6,000 a month (First Class CNY 6,000, Second CNY 5,000, Third CNY 4,000). Guangdong Government Scholarship CNY 30,000 a year and Shenzhen Universiade Scholarship CNY 40,000 a year are also available.',
   'elig': 'Non-Chinese citizens with a master’s degree, under 40; HSK5 180+ for Chinese-taught programmes, English proficiency certificate for English-taught programmes. A supervisor recommendation letter is required before applying.',
   'tags': [('PhD', 'blue'), ('China', 'teal')]},
 'yale-2027': {'mono': 'YA', 'title': 'Yale University Scholarships 2027 in USA (Fully Funded)',
   'href': 'yale-university-scholarships-2027-usa.html',
   'dpill': 'Deadline 2 Jan 2027 · %d days left' % dl_left('2027-01-02'),
   'award': 'Need-based, not merit: Yale meets 100% of demonstrated financial need for every admitted student, of any nationality. Average need-based scholarship $75,220 a year; families under $100,000 pay $0 (tuition, housing, food, travel and insurance); families under $200,000 pay $0 tuition. No loans, ever.',
   'elig': 'Any nationality. Admission is need-blind worldwide — ability to pay is not a factor. There is no GPA threshold and no separate scholarship application; the award follows admission.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'jsps-2027': {'mono': 'JS', 'title': 'JSPS Postdoctoral Fellowship 2027 in Japan (Fully Funded)',
   'href': 'jsps-postdoctoral-fellowship-2027-japan.html',
   'dpill': 'Deadline 23 Apr 2027 · %d days left' % dl_left('2027-04-23'),
   'award': 'Standard Program: ¥362,000 a month maintenance allowance, ¥200,000 settling-in allowance, round-trip airfare and overseas travel insurance, for 12–24 months of collaborative research in Japan. About 120 fellowships per recruitment round.',
   'elig': 'Citizens of countries with diplomatic relations with Japan (Taiwan and Palestine treated as eligible); PhD obtained on or after 2 April 2021; a Japanese host researcher must submit the application on your behalf.',
   'tags': [('Postdoctoral', 'blue'), ('Japan', 'teal')]},
 'vuw-2027': {'mono': 'VW', 'title': 'Victoria University of Wellington Scholarships 2027 in New Zealand (Funded)',
   'href': 'victoria-university-of-wellington-scholarships-2027-new-zealand.html',
   'dpill': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
   'award': 'VUW Undergraduate International Scholarship NZ$15,000 and VUW Postgraduate International Scholarship NZ$10,000, both automatic on the offer of place; Wellington Doctoral Scholarship NZ$32,000 a year plus domestic tuition fees for up to 3 years (about 110 a year).',
   'elig': 'International students paying full fees who are new to Victoria University of Wellington and hold an Offer of Place; doctoral applicants normally need a First Class Honours-equivalent degree and no doctorate already held.',
   'tags': [('Undergraduate to PhD', 'blue'), ('New Zealand', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Florida State University
A.append(dict(
 slug='florida-state-university-scholarships-2027-usa',
 title='Florida State University Scholarships 2027 in USA (Funded)',
 meta='Florida State University Scholarships 2027: a family of awards for first-year students — a 100% out-of-state tuition waiver, Presidential Scholars $42,000, Vires $16,000, IB Diploma $8,000 and five full-ride Stamps Scholarships. International students are automatically considered. Deadline 1 December 2026.',
 short='Florida State University Scholarships 2027', kicker='USA · Undergraduate · Funded', mono='FS',
 prov_short='Florida State University', prov_cat='University · USA',
 h1='Florida State University Scholarships 2027 in USA (Funded)',
 sub='Read this first, because “Florida State University Scholarships 2027” is not one scholarship — it is a family of awards, and the one that matters most for international students is automatic. Every admitted first-year student is automatically considered for FSU’s admissions merit scholarships; there is no separate scholarship form. Admitted international freshmen are automatically considered for the out-of-state tuition waiver, which covers 100% of the out-of-state tuition portion — about $15,888 a year. The big named awards (Presidential Scholars, Stamps, IB Diploma) all run on the 1 December 2026 deadline, so apply for admission early: scholarship funds are limited and FSU awards on academic merit, typically to students with no grades below B.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'Out-of-State Tuition Waiver: 100% of the out-of-state tuition portion, about $15,888 a year (about $63,555 over four years). Presidential Scholars Program: $42,000 plus the out-of-state tuition waiver, for Honors students (competitive interview). Vires Scholarship: $16,000 over eight semesters. IB Diploma Scholarship: $8,000 over four years. Stamps Scholars: five full-ride awards a year covering the full cost of attendance including the out-of-state waiver, plus $20,000 in enrichment funding. Out-of-State National Merit package: about $75,776 over four years (waiver + Vires + National Merit stipend). Benacquisto Scholarship: for Florida-resident National Merit Finalists only — full in-state cost of attendance ($16,000–$25,000 a year).'),
              ('Eligible', 'New international first-year students are automatically considered for the out-of-state tuition waiver; strong academics (typically no grades below B) and a rigorous curriculum with test scores. All first-year applicants must submit at least one set of ACT, CLT or SAT scores (Florida Board of Governors rule). Presidential Scholars and Stamps require the Honors application and an interview. National Merit Finalists must list FSU as first-choice by 1 May.'),
              ('How', 'Apply for admission to FSU (Common Application or the FSU application) by the priority deadline — no separate scholarship application. Awards are notified with the admission decision on the Admissions Portal. For Honors awards, submit the Honors Application by 1 December 2026.'),
              ('Deadline', '1 December 2026 — Presidential Scholars / Honors application and IB Diploma Scholarship. International priority deadline for admission: 15 January 2027 (per Collegedunia). Graduate assistantship applicants should verify with their department by 15 January 2027.'),
              ('Fine print', 'Scholarship funds are limited — apply early for admission. FSU does not engage in scholarship matching and does not send notifications to students who did not receive an award. FAFSA is for US citizens and permanent residents only; international students cannot use it. Graduate assistantships ($26,000 master’s / $29,000 PhD a year plus tuition waiver and health insurance) are departmental and separate from these undergraduate awards.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Florida State University (FSU)</strong> in Tallahassee, Florida, awards its first-year scholarships through the <strong>Office of Admissions</strong>, and the system is simpler than the aggregator pages make it look: <strong>all accepted first-year students are automatically considered</strong> for admissions merit scholarships, and <strong>admitted international freshmen are automatically considered for the out-of-state tuition waiver</strong>. There is no separate scholarship form and no extra essay for the main awards. The awards are competitive and based on academic merit — a rigorous curriculum and test scores — and students who receive them have typically earned no grades below B.</p>
      <p>The awards themselves: the <strong>Out-of-State Tuition Waiver</strong> covers 100% of the out-of-state tuition portion — about <strong>$15,888 a year, about $63,555 over four years</strong>. The <strong>Presidential Scholars Program</strong> adds <strong>$42,000</strong> on top of the waiver for Honors students, after a competitive interview. The <strong>Vires Scholarship</strong> pays <strong>$16,000</strong> over eight semesters, and the <strong>IB Diploma Scholarship</strong> pays <strong>$8,000</strong> over four years. New for fall 2027, an expanded partnership with the <strong>Stamps Scholars Program</strong> funds <strong>five first-year students a year</strong> with a full ride — the full cost of attendance including the out-of-state waiver, plus <strong>$20,000 in enrichment funding</strong> for internships, study abroad and research. National Merit Finalists who list FSU first-choice can receive the <strong>Out-of-State National Merit package of about $75,776 over four years</strong> (waiver + Vires + National Merit stipend).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>new international first-year student</strong> admitted to FSU — you are automatically considered for the <strong>out-of-state tuition waiver</strong>.</li>
        <li>Show <strong>strong academics</strong>: a rigorous curriculum and test scores; recipients have typically earned <strong>no grades below B</strong>.</li>
        <li>Submit at least one set of <strong>ACT, CLT or SAT scores</strong> — required of all first-year applicants by the Florida Board of Governors.</li>
        <li>For <strong>Presidential Scholars / Stamps</strong>: apply to the <strong>University Honors Program</strong> and pass a <strong>competitive interview</strong>.</li>
        <li>For the <strong>IB Diploma Scholarship</strong>: hold a <strong>full IB Diploma</strong> and enrol at the Tallahassee campus.</li>
        <li>For <strong>National Merit</strong> awards: be a <strong>National Merit Finalist</strong> and list FSU as your <strong>first-choice institution by 1 May</strong>.</li>
        <li>Note: the <strong>Benacquisto Scholarship is for Florida-resident finalists only</strong> — it covers the full in-state cost of attendance ($16,000–$25,000 a year). Out-of-state finalists get the Out-of-State National Merit package instead.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Out-of-State Tuition Waiver:</strong> 100% of the out-of-state tuition portion — about <strong>$15,888 a year</strong>, about <strong>$63,555 over four years</strong>.</li>
        <li><strong>Presidential Scholars Program:</strong> <strong>$42,000</strong> plus the out-of-state tuition waiver.</li>
        <li><strong>Vires Scholarship:</strong> <strong>$16,000</strong> over eight semesters ($2,000 a semester).</li>
        <li><strong>IB Diploma Scholarship:</strong> <strong>$8,000</strong> over four years.</li>
        <li><strong>Stamps Scholars:</strong> <strong>full cost of attendance</strong> for four years including the waiver, plus <strong>$20,000 enrichment funding</strong> — five awards a year.</li>
        <li><strong>Out-of-State National Merit package:</strong> about <strong>$75,776 over four years</strong>.</li>
        <li><strong>Graduate assistantships (separate):</strong> <strong>$26,000 a year (master’s) or $29,000 (PhD)</strong> plus tuition waiver and health insurance, awarded by departments.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>admission application</strong> (Common Application or FSU application) — no separate scholarship form.</li>
        <li><strong>Self-reported ACT, CLT or SAT scores</strong> (and official scores if required).</li>
        <li><strong>Self-reported transcript and academic record (STARS)</strong>.</li>
        <li>An <strong>essay</strong> and a <strong>resume / list of activities</strong>.</li>
        <li>For <strong>Honors awards</strong>: the <strong>Honors Application</strong> by 1 December 2026.</li>
        <li><strong>English proficiency</strong> (TOEFL/IELTS) where required for international applicants.</li>
        <li>US citizens and permanent residents seeking need-based aid should also file the <strong>FAFSA by 1 December</strong> — international students cannot use FAFSA.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to Florida State University for Fall 2027 — Early Action, Regular Decision or Rolling Decision — through the Common Application or the FSU application.</li>
        <li>Submit your <strong>test scores, transcript (STARS), essay and resume</strong> by the materials deadline for your application plan.</li>
        <li>For <strong>Presidential Scholars / Stamps</strong>: submit the <strong>Honors Application by 1 December 2026</strong> and attend the interview if invited.</li>
        <li><strong>No separate scholarship application</strong> — you are automatically considered for the merit awards and the out-of-state waiver.</li>
        <li>Check the <strong>Admissions Portal</strong>: scholarship offers are notified with the admission decision. If no award appears there, FSU was not able to offer one.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for FSU Scholarships 2027?',
  '1 December 2026 for the Presidential Scholars / Honors application and the IB Diploma Scholarship — and the strongest shot at the limited merit funds. The international priority deadline for admission is 15 January 2027.'),
 ('Do international students get FSU scholarships?',
  'Yes — admitted international freshmen are automatically considered for the out-of-state tuition waiver (100% of the out-of-state tuition portion, about $15,888 a year). Most other named awards depend on residency or National Merit status.'),
 ('Is there a separate application for FSU scholarships?',
  'No. All admitted first-year students are automatically considered for admissions merit scholarships. The only extra step is the Honors Application (by 1 December 2026) for Presidential Scholars and Stamps.'),
 ('How much is the FSU out-of-state tuition waiver worth?',
  'About $15,888 a year, or about $63,555 over four years. One source quotes $73,808 over four years, but the $15,888-a-year figure from two sources is the one used here.'),
 ('What is the Benacquisto Scholarship at FSU?',
  'It is for Florida-resident National Merit Finalists only: it covers the full in-state cost of attendance ($16,000–$25,000 a year). Out-of-state finalists instead receive the Out-of-State National Merit package of about $75,776 over four years.'),
 ('Does FSU offer a full-ride scholarship?',
  'Yes — the Stamps Scholars Program funds five first-year students a year with the full cost of attendance including the out-of-state waiver, plus $20,000 in enrichment funding for internships, study abroad and research.')]) + '''
      <p class="verify">Verified 27 Oct 2026: admissions.fsu.edu/first-year/scholarships (official FSU Office of Admissions) — all accepted first-year students automatically considered for admissions merit scholarships; scholarships competitive, based on academic merit, typically no grades below B; funds limited, apply early; Benacquisto for Florida-resident National Merit Finalists, award equals the in-state cost of attendance minus Bright Futures and any National Merit award, disbursement $16,000–$25,000/year, list FSU first-choice by 1 May; admissions.fsu.edu/first-year/scholarships/faq (official) — admitted international freshmen automatically considered for the out-of-state tuition waiver; notification with the admission decision on the Admissions Portal; no notification if no award; FSU does not engage in scholarship matching; National Merit finalists eligible for Benacquisto or the Out-of-State National Merit Scholarship; admissions.fsu.edu/international/faq (official) — at least one set of ACT/CLT/SAT scores required for all first-year applicants; all admitted first-year applicants automatically considered for merit scholarships; fsunews.com, 1 Oct 2026 — Stamps partnership expanded: five full-ride scholarships a year, full cost of attendance including the out-of-state waiver plus $20,000 enrichment funding; Collegedunia FSU page and Scholarships.BookNagri — waiver about $15,888/year (about $63,555 over four years), Presidential $42,000 + waiver, Vires $16,000, IB Diploma $8,000, Out-of-State National Merit about $75,776, graduate assistantships $26,000/$29,000 + waiver + health insurance, international priority deadline 15 January 2027, documents deadline 7 December 2026; Bright Scholarship (queue URL) — corroboration. CONFLICTS: Collegedunia quotes the waiver at $73,808 over four years and the Benacquisto at "up to $91,808 over four years for out-of-state finalists" — both contradict the official FSU page (Benacquisto is Florida-resident only and equals the in-state cost of attendance) and the $15,888/year figure from two sources; the article uses $63,555 and the official Benacquisto terms. The 1 December 2026 Presidential/IB deadline is per Collegedunia/BookNagri; FSU's own page does not state the 2027 dates in the text retrieved.</p>''',
 dl_long='1 December 2026 (Presidential Scholars, Honors & IB Diploma) — international admission priority deadline 15 January 2027',
 offlinks=[('Florida State University — Scholarships, First Year (official)', 'https://admissions.fsu.edu/first-year/scholarships'),
           ('Florida State University — Scholarships FAQ (official)', 'https://admissions.fsu.edu/first-year/scholarships/faq'),
           ('Bright Scholarship — Florida State University Scholarships 2027', 'https://brightscholarship.com/florida-state-university-scholarships-2027/')],
 related_titles=['florida-bf-2026-27', 'alabama-2027', 'dayton-merit', 'msu-oos'])),

# ---------------------------------------------------------------- 2. Shenzhen University
A.append(dict(
 slug='shenzhen-university-phd-scholarships-2027-china',
 title='Shenzhen University PhD Scholarships 2027 in China (March Intake)',
 meta='Shenzhen University PhD Scholarships 2027 (March intake): full tuition waiver plus CNY 4,000–6,000 a month under the Liyuan International Scholarship, plus Guangdong Government (CNY 30,000/year) and Shenzhen Universiade (CNY 40,000/year) awards. Applications 10 October – 30 November 2026.',
 short='Shenzhen University PhD Scholarships 2027', kicker='China · PhD · Fully Funded', mono='SZ',
 prov_short='Shenzhen University', prov_cat='University · China',
 h1='Shenzhen University PhD Scholarships 2027 in China (March Intake)',
 sub='Shenzhen University (SZU) is admitting international PhD students for March 2027, and the strongest award — the Liyuan International Scholarship — waives tuition and pays CNY 4,000 to 6,000 a month. Two other scholarships pay CNY 30,000 or CNY 40,000 a year. The catch is the order of operations: you must find a supervisor and get a recommendation letter from them before you apply — the application cannot be completed without it. Applications run from 10 October to 30 November 2026, the fee is CNY 400, and pre-admission results come in December 2026.',
 dpill='Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
 facts=facts([('Award', 'Liyuan International Scholarship: full tuition waiver plus a monthly living allowance — First Class CNY 6,000, Second Class CNY 5,000, Third Class CNY 4,000. Guangdong Government Outstanding International Student Scholarship: CNY 30,000 a year. Shenzhen Universiade Scholarship: CNY 40,000 a year. Supervisors also provide at least CNY 12,000 a year for research or academic exchange. Free accommodation is NOT explicitly included in the Liyuan benefits — the official brochure lists accommodation charges separately.'),
              ('Eligible', 'Non-Chinese citizens with a valid foreign passport, in good physical and mental health; hold a master’s degree or above and be under 40 (expected-graduation certificates accepted, diploma required before enrolment). Chinese-taught programmes: HSK5 180 or above. English-taught programmes: an English proficiency certificate (native speakers may be exempted after recognition by the university).'),
              ('How', 'Contact a potential supervisor first and ask for a recommendation letter (template in the brochure). Then register at lxs.szu.edu.cn, fill in personal and visa information, upload documents and the CNY 400 fee payment voucher, and submit by 30 November 2026.'),
              ('Deadline', '30 November 2026. Applications opened 10 October 2026. Pre-admission results in December 2026; admission documents in January 2027.'),
              ('Fine print', '21 PhD programme options (19 taught in English, 2 in Chinese — Education and Psychology); 3 to 4 years, 5 years at most; full-time only. Application fee CNY 400 (USD 60), non-refundable. Tuition CNY 34,000–52,000 a year by field; accommodation CNY 750–8,000 a semester; health insurance CNY 800 a year. This is a university-scholarship intake, not a general CSC deadline — do not confuse it with the CSC high-level postgraduate route.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Shenzhen University (SZU)</strong> in Shenzhen, Guangdong Province, runs two PhD intakes a year for international students, in March and September. This article covers the <strong>March 2027 intake</strong>, which opened on <strong>10 October 2026</strong> and closes on <strong>30 November 2026</strong>. There are <strong>21 PhD programme options</strong> in 17 academic and 4 professional doctoral degrees — <strong>19 taught in English and 2 in Chinese</strong> (Education and Psychology). All PhD study is full-time, lasting <strong>3 to 4 years</strong> (5 years at most).</p>
      <p>The main award is the <strong>Liyuan International Scholarship</strong>: a <strong>full tuition waiver plus CNY 4,000 to 6,000 a month</strong> — First Class CNY 6,000, Second Class CNY 5,000, Third Class CNY 4,000. Two other scholarships are available alongside it: the <strong>Guangdong Government Outstanding International Student Scholarship (CNY 30,000 a year)</strong> and the <strong>Shenzhen Universiade Scholarship (CNY 40,000 a year)</strong>. Supervisors also provide their recruited international PhD students with at least <strong>CNY 12,000 a year</strong> for research or academic exchange. Note what is not promised: the official brochure lists university accommodation charges separately, so <strong>free accommodation is not explicitly included</strong> in the Liyuan benefits — do not budget as if it were.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Chinese citizen</strong> with a <strong>valid foreign passport</strong>, in good physical and mental health, and abide by Chinese laws and university rules.</li>
        <li>Hold a <strong>master’s degree or above</strong> and be <strong>under 40</strong>. Applicants who have not yet graduated can provide an expected-graduation certificate, but the official diploma must be provided before enrolment.</li>
        <li>For <strong>Chinese-taught programmes</strong>: a minimum score of <strong>180 in HSK5</strong>.</li>
        <li>For <strong>English-taught programmes</strong>: an <strong>English proficiency certificate</strong> within its validity period. Native speakers of Chinese or English can be exempted after recognition by the university.</li>
        <li>Secure a <strong>recommendation letter from a potential supervisor</strong> before applying — this is mandatory, not optional.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Liyuan International Scholarship:</strong> full tuition waiver + <strong>CNY 6,000 / 5,000 / 4,000 a month</strong> (First / Second / Third Class).</li>
        <li><strong>Guangdong Government Scholarship:</strong> <strong>CNY 30,000 a year</strong>.</li>
        <li><strong>Shenzhen Universiade Scholarship:</strong> <strong>CNY 40,000 a year</strong>.</li>
        <li><strong>Supervisor support:</strong> at least <strong>CNY 12,000 a year</strong> for research or academic exchange.</li>
        <li><strong>Not explicitly included:</strong> free accommodation — the brochure lists accommodation charges separately (single room CNY 2,400–8,000 a semester; double room CNY 750 a semester).</li>
        <li><strong>Tuition for reference:</strong> CNY 34,000 a year (liberal arts), CNY 40,000 (science and engineering), CNY 52,000 (medicine/arts/physics); health insurance CNY 800 a year.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>recommendation letter from a potential supervisor</strong> (use the template in the official brochure).</li>
        <li>A <strong>valid passport</strong>.</li>
        <li><strong>Master’s degree certificate</strong> (or expected-graduation certificate) and <strong>transcripts</strong>.</li>
        <li>A <strong>language proficiency certificate</strong> (HSK5 for Chinese-taught; English proficiency certificate for English-taught).</li>
        <li>A <strong>study plan / research proposal</strong>.</li>
        <li>A <strong>physical examination form</strong>.</li>
        <li><strong>Proof of funds</strong> and other documents as required by the online system.</li>
        <li>The <strong>CNY 400 application fee payment voucher</strong> (CNY 400 / USD 60, non-refundable).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Contact a potential supervisor</strong> from the official list and ask for a <strong>recommendation letter</strong> — do this first, before anything else.</li>
        <li><strong>Register online</strong> at <strong>lxs.szu.edu.cn</strong> (College of International Exchange).</li>
        <li><strong>Fill in personal and visa information</strong> and upload all documents plus the fee payment voucher.</li>
        <li><strong>Submit by 30 November 2026.</strong></li>
        <li>Pre-admission results arrive in <strong>December 2026</strong>; admission documents in <strong>January 2027</strong>.</li>
        <li>Contact: <strong>szulxs@szu.edu.cn</strong>, +86-755-26558894 (College of International Exchange, Shenzhen University).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for Shenzhen University PhD Scholarships 2027?',
  '30 November 2026. Applications run from 10 October to 30 November 2026. Pre-admission results come in December 2026 and admission documents in January 2027.'),
 ('How much does the Liyuan Scholarship pay?',
  'A full tuition waiver plus CNY 6,000 a month (First Class), CNY 5,000 (Second Class) or CNY 4,000 (Third Class). Two other awards pay CNY 30,000 a year (Guangdong Government) or CNY 40,000 a year (Shenzhen Universiade).'),
 ('Do I need a supervisor before applying to SZU?',
  'Yes. You must contact a potential supervisor and get a recommendation letter from them before you apply — the application cannot be completed without it.'),
 ('Is IELTS required for Shenzhen University PhD admission?',
  'For English-taught programmes you need an English proficiency certificate; native speakers of English (or Chinese, for Chinese-taught programmes) can be exempted after recognition by the university. Chinese-taught programmes need HSK5 180 or above.'),
 ('Is accommodation free under the Liyuan Scholarship?',
  'Not explicitly. The official brochure lists accommodation charges separately (single room CNY 2,400–8,000 a semester; double room CNY 750 a semester), so do not assume free housing.'),
 ('Is this a CSC scholarship?',
  'No — this is SZU’s own March 2027 PhD intake with university scholarships (Liyuan, Guangdong Government, Shenzhen Universiade). It is not a general CSC deadline; the CSC high-level postgraduate route is separate.')]) + '''
      <p class="verify">Verified 27 Oct 2026: en.szu.edu.cn/info/1024/1979.htm (official SZU admission brochure, March 2027 intake, English) — programmes (21 options, 19 English, 2 Chinese), duration 3–4 years (max 5), eligibility (non-Chinese, valid passport, master’s degree or above, under 40, HSK5 180+ for Chinese-taught, English proficiency certificate for English-taught), application time 10 October–30 November 2026, procedure (contact supervisor for a recommendation letter first, register at lxs.szu.edu.cn, upload documents and fee voucher); lxs.szu.edu.cn/en/info/1112/3623.htm (official brochure, Chinese mirror) — same dates; ScholarshipClaude, scholarshipclaude.com/blog/shenzhen-university-phd-scholarship-application-guide — checked 16 October 2026 against the official brochure: Liyuan CNY 4,000–6,000/month, Guangdong CNY 30,000/year, Shenzhen Universiade CNY 40,000/year, supervisor support at least CNY 12,000/year, fee CNY 400, pre-admission December 2026, admission documents January 2027; CSCGuideOfficials — same figures, contact szulxs@szu.edu.cn, +86-755-26558894, apply link status.szu.edu.cn; DAADScholarship.com (deadlines of 37 Chinese universities, checked 25 October 2026) — SZU March 2027 PhD admission 10 October–30 November 2026, "university scholarship options, not a general CSC deadline", supervisor recommendation required; ScholarshipsLand — stipend CNY 4,000–6,000/month, 80 scholarships, age 40. CONFLICTS: none material. NOTES: (1) the queue title says "Graduate Research Opportunities 2026 (Master’s & PhD)" — the live scheme is the March 2027 PhD intake only; the article is written on the live cycle. (2) free accommodation is not explicitly included in the Liyuan benefits (per CSCGuideOfficials reading of the brochure) — stated as such. (3) tuition figures (CNY 34,000–52,000/year) and accommodation/insurance charges are from ScholarshipsLand's reading of the brochure, not from the en.szu.edu.cn text retrieved — flagged here, used in the article as brochure figures.</p>''',
 dl_long='30 November 2026 (applications 10 October – 30 November 2026)',
 offlinks=[('Shenzhen University — Admission Brochure, Doctoral Program, March 2027 Intake (official)', 'https://en.szu.edu.cn/info/1024/1979.htm'),
           ('Shenzhen University — Admission Brochure (official, Chinese mirror)', 'https://lxs.szu.edu.cn/en/info/1112/3623.htm'),
           ('Bright Scholarship — Shenzhen University Graduate Research Opportunities', 'https://brightscholarship.com/shenzhen-university-graduate-research-opportunities/')],
 related_titles=['gxnu-csc-2027', 'xiamen-csc-2027', 'hust-csc-2027', 'nju-csc-2027'])),

# ---------------------------------------------------------------- 3. Yale University
A.append(dict(
 slug='yale-university-scholarships-2027-usa',
 title='Yale University Scholarships 2027 in USA (Fully Funded)',
 meta='Yale University Scholarships 2027: need-blind admission for every applicant worldwide, 100% of demonstrated financial need met, average need-based scholarship $75,220 a year. Families under $100,000 pay $0; families under $200,000 pay $0 tuition. No separate scholarship application — Regular Decision 2 January 2027.',
 short='Yale University Scholarships 2027', kicker='USA · Undergraduate · Fully Funded', mono='YA',
 prov_short='Yale University', prov_cat='University · USA',
 h1='Yale University Scholarships 2027 in USA (Fully Funded)',
 sub='Yale does not hand out scholarships for good grades. It does something better: if you get admitted — from any country on earth — Yale pays whatever your family cannot afford. Admission is need-blind for every applicant worldwide, and the university meets 100% of demonstrated financial need with grants that never have to be repaid. The average need-based scholarship is $75,220 a year; families with typical assets earning under $100,000 pay nothing at all, and families under $200,000 pay no tuition. There is no separate scholarship application and no GPA threshold — the scholarship sits behind admission, and admission is the only gate. Regular Decision closes 2 January 2027; aid documents are due by 15 February 2027.',
 dpill='Deadline 2 Jan 2027 · %d days left' % dl_left('2027-01-02'),
 facts=facts([('Award', 'Average need-based scholarship $75,220 a year (about 56% of international undergraduates receive Yale grants). Families with typical assets earning under $100,000: expected contribution normally $0 — tuition, fees, housing, food, travel and hospitalisation insurance covered, plus a $2,000 start-up grant in the first year. Families under $200,000: tuition typically covered entirely. No loans, ever — aid packages contain zero loan expectation, and about 88% of graduates leave with no student loan debt.'),
              ('Eligible', 'Any nationality — admission is need-blind worldwide and aid meets 100% of demonstrated need regardless of citizenship or immigration status. There is no GPA threshold and no minimum test score for the scholarship itself; grades matter for getting admitted, and admission is the only gate. Yale offers no merit scholarships — all undergraduate aid is need-based.'),
              ('How', 'Apply for admission to Yale College (Single-Choice Early Action 1 November 2026 or Regular Decision 2 January 2027) and indicate interest in financial aid on the application. International students file the CSS Profile (Yale College code 3987) and submit tax documents via IDOC. US citizens and permanent residents also file the FAFSA (code 001426). Yale does not accept the ISFAA in place of its own forms.'),
              ('Deadline', 'Regular Decision admission: 2 January 2027. Aid documents priority: 15 February 2027 (Regular Decision); 1 December 2026 (Early Action, international citizens); 1 November 2026 (QuestBridge and Early Action, US citizens/permanent residents). Transfer students: 1 April 2027.'),
              ('Fine print', 'Graduate and professional programmes run their own aid and deadlines by department — this article covers Yale College undergraduate aid. Aid offers are not reduced for late submission (per finaid.yale.edu), but apply by the priority dates to get a decision with your admission. An English test is required if English is not your first language and you have not spent two or more years in an English-medium school; competitive applicants typically score IELTS 7 or higher (aggregator-reported).')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Yale University</strong> in New Haven, Connecticut, is one of the few universities in the world that is <strong>need-blind for every applicant, everywhere</strong>: a family’s ability to pay is not a factor in the admissions process for any student, anywhere in the world. Once admitted, Yale <strong>meets 100% of demonstrated financial need</strong> with grants that never have to be repaid. The average need-based scholarship is <strong>$75,220 a year</strong>, and about <strong>56% of international undergraduates</strong> receive Yale grants.</p>
      <p>The income markers are worth memorising. Families with typical assets earning <strong>under $100,000</strong> normally pay <strong>nothing</strong> — tuition, fees, housing, food, travel and even hospitalisation insurance are covered, plus a <strong>$2,000 start-up grant</strong> in the first year. Families earning <strong>under $200,000</strong> typically have <strong>tuition covered entirely</strong>. There are <strong>no loans, ever</strong>: Yale’s aid package contains zero loan expectation, and around <strong>88% of Yale graduates leave with no student loan debt</strong>. For a low- or middle-income family anywhere in the world, Yale can genuinely cost less than a local university. There is no separate scholarship application: financial aid is built into the standard admissions application, and there is no GPA threshold — your grades matter enormously for getting admitted, and admission is the only gate the scholarship sits behind.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be admitted to <strong>Yale College</strong> (undergraduate) — admission is <strong>need-blind worldwide</strong>.</li>
        <li>Be of <strong>any nationality</strong> — aid meets 100% of demonstrated need regardless of citizenship or immigration status.</li>
        <li>There is <strong>no GPA threshold and no minimum test score</strong> for the scholarship itself.</li>
        <li>Yale offers <strong>no merit scholarships</strong> — all undergraduate aid is based on financial need.</li>
        <li>Indicate your <strong>interest in financial aid on the admission application</strong>; you will then be contacted by Undergraduate Financial Aid with a document list.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Average need-based scholarship:</strong> <strong>$75,220 a year</strong>.</li>
        <li><strong>Families under $100,000</strong> (typical assets): <strong>$0</strong> — tuition, fees, housing, food, travel and hospitalisation insurance, plus a <strong>$2,000 first-year start-up grant</strong>.</li>
        <li><strong>Families under $200,000:</strong> <strong>tuition typically covered entirely</strong>.</li>
        <li><strong>No loans, ever</strong> — aid packages contain zero loan expectation.</li>
        <li><strong>Supplemental allowances:</strong> a $2,000 first-year international allowance and a $1,500 annual vacation allowance for aided internationals unable to return home during breaks (per Collegedunia).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>admission application</strong> (Common Application or Coalition Application) with <strong>essay, recommendations and transcripts</strong>.</li>
        <li>The <strong>CSS Profile</strong> (Yale College code <strong>3987</strong>) — required for international students seeking aid.</li>
        <li><strong>Parent and student tax returns / income documentation</strong> (2025 income for the 2027–28 year), submitted via <strong>IDOC</strong>.</li>
        <li>US citizens and permanent residents: also the <strong>FAFSA</strong> (Yale code <strong>001426</strong>).</li>
        <li>Yale does <strong>not accept the ISFAA</strong> in place of its own forms.</li>
        <li><strong>English proficiency test</strong> (TOEFL/IELTS/Duolingo) where required — if English is not your first language and you have not spent two or more years in an English-medium school.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to Yale College: <strong>Single-Choice Early Action by 1 November 2026</strong> or <strong>Regular Decision by 2 January 2027</strong>.</li>
        <li>Indicate your <strong>interest in financial aid</strong> on the admission application.</li>
        <li>File the <strong>CSS Profile</strong> (code 3987) and submit <strong>tax documents via IDOC</strong> by the priority date: <strong>1 December 2026</strong> (Early Action, international) or <strong>15 February 2027</strong> (Regular Decision).</li>
        <li>US citizens and permanent residents also file the <strong>FAFSA</strong> (code 001426).</li>
        <li>Your <strong>financial aid offer arrives with your admission decision</strong> if your aid application is complete.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is Yale need-blind for international students?',
  'Yes. Yale states that a family’s ability to pay is not a factor in the admissions process for any student, anywhere in the world, and that aid offers meet 100% of demonstrated need regardless of citizenship or immigration status.'),
 ('How much does Yale cost, and what does the scholarship pay?',
  'The published estimate for 2026–27 is $72,500 tuition plus housing, food, books and personal costs — about $97,985 in total, plus travel. The average need-based scholarship is $75,220 a year; families under $100,000 pay $0 and families under $200,000 pay $0 tuition.'),
 ('Is there a separate Yale Scholarship application?',
  'No. Financial aid is built directly into the standard admissions application; there is no extra scholarship form to complete. You indicate interest in aid on the application and then file the CSS Profile.'),
 ('Does applying for aid hurt my admission chances at Yale?',
  'No. Yale is need-blind for every applicant, so financial aid interest never factors into the admissions decision.'),
 ('What is the Yale application deadline for 2027 entry?',
  'Single-Choice Early Action closes 1 November 2026 and Regular Decision closes 2 January 2027. International aid documents are due 1 December 2026 (Early Action) or 15 February 2027 (Regular Decision).'),
 ('Does Yale offer merit scholarships?',
  'No. Yale’s financial aid office says merit-based scholarships are not offered by Yale. All undergraduate scholarships are based on financial need.')]) + '''
      <p class="verify">Verified 27 Oct 2026: finaid.yale.edu/apply/prospective (official Yale Undergraduate Financial Aid) — priority deadlines 2027–28: QuestBridge 1 November 2026, Early Action (US citizens/permanent residents) 1 November 2026, Early Action (international citizens) 1 December 2026, Regular Decision 15 February 2027, Transfer 1 April 2027; CSS Profile (Yale College code 3987) and FAFSA (code 001426) for US citizens/permanent residents; documents via IDOC; late applications still eligible, offers not reduced; Collegedunia Yale page and ILMHunt — average need-based scholarship $75,220/year, ~56% of international undergraduates receive grants, families under $100,000 pay $0 (tuition, housing, food, travel, insurance) + $2,000 start-up grant, families under $200,000 pay $0 tuition, no loans, ~88% graduate debt-free, tuition $72,500, total cost about $97,985 plus travel, $2,000 first-year international allowance, $1,500 annual vacation allowance; USAScholarships.net — need-blind worldwide, Yale does not accept the ISFAA in place of its own forms; AfroCareer — Single-Choice Early Action 1 November 2026, Regular Decision 2 January 2027; JobGader — IELTS 7 typically, English test required unless 2+ years in an English-medium school. CONFLICTS: none material. NOTE: one aggregator lists a "15 December 2026" Yale deadline — that is not an official Yale date and is not used; the operative dates are 1 November 2026 (Early Action), 1 December 2026 (international aid documents, Early Action), 2 January 2027 (Regular Decision admission) and 15 February 2027 (Regular Decision aid documents).</p>''',
 dl_long='2 January 2027 (Regular Decision admission) · aid documents by 15 February 2027',
 offlinks=[('Yale University — Undergraduate Financial Aid, Prospective Students (official)', 'https://finaid.yale.edu/apply/prospective'),
           ('Bright Scholarship — Yale University Scholarships 2027', 'https://brightscholarship.com/yale-university-scholarships-2027-in-usa/')],
 related_titles=['yale-wf', 'harvard-env-2027', 'uchicago', 'clarendon'])),

# ---------------------------------------------------------------- 4. JSPS Postdoctoral Fellowship
A.append(dict(
 slug='jsps-postdoctoral-fellowship-2027-japan',
 title='JSPS Postdoctoral Fellowship 2027 in Japan (Fully Funded)',
 meta='JSPS Postdoctoral Fellowship 2027 (Standard Program): ¥362,000 a month, ¥200,000 settling-in allowance, airfare and insurance for 12–24 months of research in Japan. About 120 fellowships per round — 1st round closed 28 August 2026; 2nd round closes 23 April 2027.',
 short='JSPS Postdoctoral Fellowship 2027', kicker='Japan · Postdoctoral · Fully Funded', mono='JS',
 prov_short='Japan Society for the Promotion of Science', prov_cat='JSPS · Japan',
 h1='JSPS Postdoctoral Fellowship 2027 in Japan (Fully Funded)',
 sub='The Japan Society for the Promotion of Science (JSPS) Postdoctoral Fellowship — Standard Program — is one of Japan’s major international postdoctoral programmes: 12 to 24 months of collaborative research at a Japanese university or research institution, with a monthly maintenance allowance of ¥362,000, a ¥200,000 settling-in allowance, a round-trip air ticket and overseas travel insurance. About 120 fellowships are planned in each recruitment round, across all fields — humanities, social sciences and natural sciences. The first FY2027 round closed on 28 August 2026; the second round closes on 23 April 2027 at 5:00 p.m. JST. One thing to get right early: you do not apply to JSPS yourself. Your Japanese host researcher submits the application on your behalf — so the first step is finding a host, not filling in a form.',
 dpill='Deadline 23 Apr 2027 · %d days left' % dl_left('2027-04-23'),
 facts=facts([('Award', 'Monthly maintenance allowance ¥362,000; settling-in allowance ¥200,000; round-trip air ticket under JSPS rules; overseas travel insurance; a separate Grant-in-Aid for Scientific Research for cooperative research expenses (applied for by the host researcher). About 120 fellowships per recruitment round.'),
              ('Eligible', 'Citizens of countries having diplomatic relations with Japan (Taiwan and Palestine are treated as eligible); Japanese citizens and foreign nationals holding permanent residence in Japan are NOT eligible. PhD obtained on or after 2 April 2021 (within six years of the award; maternity/parental leave deductible). All fields: humanities, social sciences and natural sciences. You must have a Japanese host researcher and an agreed research plan in advance.'),
              ('How', 'Arrange a host researcher at an eligible Japanese university or research institution first. The host researcher submits the application to JSPS on your behalf (open-call route), or you apply through your country’s overseas nominating authority where one exists — e.g. the British Academy for UK residents (humanities/social sciences, deadline 2 December 2026), CNRS for France (9 November 2026), or the ASEAN short-term PA route (16 November 2026).'),
              ('Deadline', '2nd open-call round: 23 April 2027, 5:00 p.m. JST (host institution submits to JSPS). 1st round closed 28 August 2026. Host institutions set their own earlier internal deadlines — check with your host first, as they can precede the JSPS deadline by weeks or more.'),
              ('Fine print', 'Fellowships start 1 September – 30 November 2027. The fellowship cannot be divided into multiple stays. If you already live in Japan before the start date, the airfare and settling-in allowance are not paid. Parallel applications through multiple nominating authorities in the same fiscal year are not allowed. Do not trust the "15 November 2026" deadline circulating online — it does not appear in the official JSPS FY2027 Standard Program schedule.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>JSPS Postdoctoral Fellowship for Research in Japan — Standard Program</strong> is run by the <strong>Japan Society for the Promotion of Science</strong> and offers outstanding early-career researchers from around the world the chance to spend <strong>12 to 24 months</strong> conducting collaborative research with leading research groups at Japanese universities and eligible research institutions, under the guidance of a Japanese host. It is open across an exceptionally broad range of fields — <strong>humanities, social sciences and natural sciences</strong> — and it is one of Japan’s major international postdoctoral research programmes.</p>
      <p>The funding is generous and simple: a <strong>monthly maintenance allowance of ¥362,000</strong>, a <strong>settling-in allowance of ¥200,000</strong>, a <strong>round-trip air ticket</strong> under JSPS rules, <strong>overseas travel insurance</strong>, and access to a separate <strong>Grant-in-Aid for Scientific Research</strong> for cooperative research expenses (applied for by the host researcher through their institution). For FY2027, JSPS scheduled <strong>two open-call recruitment rounds with about 120 fellowships in each</strong>. The first round closed on <strong>28 August 2026</strong>; the second round closes on <strong>23 April 2027 at 5:00 p.m. JST</strong>, with fellowships starting between <strong>1 September and 30 November 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of a country having diplomatic relations with Japan</strong> (Taiwan and Palestine are treated as eligible). <strong>Japanese citizens and foreign permanent residents of Japan are not eligible.</strong></li>
        <li>Hold a <strong>PhD obtained on or after 2 April 2021</strong> — within six years of the award. Researchers who have not yet formally received the doctorate can be nominated if they are expected to receive it before the fellowship starts. Qualifying maternity and parental leave is deductible from the six-year period.</li>
        <li>Have <strong>arranged a research plan in advance with a Japanese host researcher</strong> at an eligible Japanese university or research institution.</li>
        <li>Work in <strong>any field</strong> — humanities, social sciences or natural sciences.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly maintenance allowance:</strong> <strong>¥362,000</strong>.</li>
        <li><strong>Settling-in allowance:</strong> <strong>¥200,000</strong>.</li>
        <li><strong>Round-trip air ticket</strong> under JSPS rules.</li>
        <li><strong>Overseas travel insurance.</strong></li>
        <li><strong>Grant-in-Aid for Scientific Research</strong> for cooperative research expenses (host applies).</li>
        <li><strong>Duration:</strong> 12–24 months, not divisible into multiple stays.</li>
        <li><strong>Not paid</strong> if you already live in Japan before the start date: the airfare and settling-in allowance.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An <strong>agreed research plan</strong> with your Japanese host researcher.</li>
        <li>A <strong>letter of acceptance</strong> from the host researcher / host institution.</li>
        <li>Your <strong>CV</strong> and <strong>list of publications</strong>.</li>
        <li><strong>Doctoral degree certificate</strong> (or proof you will receive it before the fellowship starts — it does not need to accompany the initial application).</li>
        <li>A <strong>letter of recommendation</strong> from a referee who knows your research.</li>
        <li>The <strong>application form</strong> for the relevant route (open-call or nominating authority).</li>
        <li>Note: the host researcher submits the open-call application — confirm with your host which documents they need and their internal deadline.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Find a Japanese host researcher</strong> at an eligible university or research institution (search researchmap and JSPS-Net) and agree a research plan with them.</li>
        <li><strong>Open-call route:</strong> your host researcher submits the completed application to JSPS by <strong>23 April 2027, 5:00 p.m. JST</strong> — but meet your host institution’s earlier internal deadline first.</li>
        <li><strong>Nominating-authority route (where one exists):</strong> apply through your country’s authority instead — e.g. the <strong>British Academy</strong> for UK residents (humanities/social sciences, <strong>2 December 2026</strong>), <strong>CNRS</strong> for France (<strong>9 November 2026</strong>), or the <strong>ASEAN short-term PA route</strong> (<strong>16 November 2026</strong>).</li>
        <li><strong>Do not submit parallel applications</strong> through multiple nominating authorities in the same fiscal year.</li>
        <li>Results for the 2nd round come in <strong>early August 2027</strong>; fellowships start <strong>1 September – 30 November 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the JSPS Postdoctoral Fellowship 2027?',
  'The 2nd open-call round closes 23 April 2027 at 5:00 p.m. JST. The 1st round closed 28 August 2026. Nominating-authority routes have their own deadlines — the British Academy (UK) closes 2 December 2026, CNRS (France) 9 November 2026, and the ASEAN short-term PA route 16 November 2026.'),
 ('How much does the JSPS Fellowship pay?',
  '¥362,000 a month, plus a ¥200,000 settling-in allowance, a round-trip air ticket and overseas travel insurance. A separate Grant-in-Aid covers cooperative research expenses.'),
 ('Who can apply for the JSPS Postdoctoral Fellowship?',
  'Citizens of countries with diplomatic relations with Japan (Taiwan and Palestine treated as eligible), with a PhD obtained on or after 2 April 2021, in any field. Japanese citizens and permanent residents of Japan are not eligible.'),
 ('How do I apply — directly to JSPS?',
  'No. For the open-call route, your Japanese host researcher submits the application to JSPS on your behalf. Alternatively, apply through your country’s overseas nominating authority where one exists.'),
 ('How many JSPS fellowships are awarded?',
  'About 120 per recruitment round in the Standard Program — two rounds for FY2027, so about 240 in total across the year.'),
 ('What is the "15 November 2026" JSPS deadline I saw online?',
  'It does not appear in the official JSPS FY2027 Standard Program open-call schedule. It likely refers to a nominating-authority route (the ASEAN short-term PA route closes 16 November 2026) — do not treat it as the universal JSPS deadline.')]) + '''
      <p class="verify">Verified 27 Oct 2026: jspsusa.org/wp/fellowship/ (JSPS USA, official programme page) — Standard Program: 12–24 months, citizens of countries with diplomatic relations with Japan (Taiwan/Palestine treated as eligible), round-trip air ticket, maintenance allowance ¥362,000/month, settling-in allowance ¥200,000, overseas travel insurance, Grant-in-Aid for Scientific Research (host applies); deadlines from host institution to JSPS: 1st 28 August 2026, 2nd 23 April 2027 (5 p.m. JST); OpportunitiesForYouth, opportunitiesforyouth.org/2026/09/13/jsps-fellowship-2027/ — FY2027 two open-call rounds, ~120 fellowships per round, 1st deadline 28 Aug 2026, 2nd 23 Apr 2027, start windows 1 Apr–30 Sep 2027 (1st) and 1 Sep–30 Nov 2027 (2nd), and the warning that "15 November 2026" does not appear in the official schedule; CareerAidHub — same schedule and eligibility (PhD on/after 2 April 2021, maternity/parental leave deductible, host internal deadlines earlier); jsps.org/latest_calls/fellowships/ (JSPS London, official) — FY2027 call for humanities/social sciences only, deadline 2 December 2026, UK residents via the British Academy; thebritishacademy.ac.uk — scheme opens 7 Oct 2026, deadline 2 Dec 2026 17:00 GMT, 12–24 months, ¥362,000/month, ¥200,000 settling-in, UK/Isle of Man/Channel Islands residents; international.cnrs.fr — JSPS Standard 2027 deadline 9 November 2026 (France/CNRS route), JSPS Short-term 2027 deadline 2 November 2026; AUN/ASEAN short-term PA 2027/2028 — deadline 16 November 2026, 1–12 months, start 1 July 2027–31 March 2028; Bright Scholarship (queue URL) — corroboration. CONFLICTS: the "120" in the queue title is the per-round figure (~120 per round, two rounds), not the annual total — stated as such. The "15 November 2026" date on some aggregators is not the official open-call deadline — flagged in the article.</p>''',
 dl_long='23 April 2027, 5:00 p.m. JST (2nd open-call round; host institutions set earlier internal deadlines)',
 offlinks=[('JSPS USA — International Fellowships for Research in Japan (official programme page)', 'https://www.jspsusa.org/wp/fellowship/'),
           ('The British Academy — JSPS Postdoctoral Fellowships for Overseas Researchers 2027 (official nominating authority)', 'https://www.thebritishacademy.ac.uk/funding/schemes/jsps-postdoctoral-fellowship-for-overseas-researchers/'),
           ('Bright Scholarship — JSPS Postdoctoral Fellowship 2027', 'https://brightscholarship.com/jsps-postdoctoral-fellowship-2027-in-japan/')],
 related_titles=['science-tokyo', 'saitama-mext-2027', 'ylp-mext-grips-2027', 'honjo'])),

# ---------------------------------------------------------------- 5. Victoria University of Wellington
A.append(dict(
 slug='victoria-university-of-wellington-scholarships-2027-new-zealand',
 title='Victoria University of Wellington Scholarships 2027 in New Zealand (Funded)',
 meta='Victoria University of Wellington Scholarships 2027: VUW Undergraduate International Scholarship NZ$15,000 and Postgraduate NZ$10,000, both automatic on the offer of place; Wellington Doctoral Scholarship NZ$32,000 a year plus domestic tuition, about 110 a year. Next doctoral round closes 1 November 2026.',
 short='Victoria University of Wellington Scholarships 2027', kicker='New Zealand · Undergraduate to PhD · Funded', mono='VW',
 prov_short='Victoria University of Wellington', prov_cat='University · New Zealand',
 h1='Victoria University of Wellington Scholarships 2027 in New Zealand (Funded)',
 sub='Victoria University of Wellington (Te Herenga Waka) does not run one big scholarship — it runs a family, and the two most useful awards need no application at all. The VUW Undergraduate International Scholarship (NZ$15,000) and the VUW Postgraduate International Scholarship (NZ$10,000) are awarded automatically: if you are eligible, Victoria tells you in your offer letter. The big research award is the Wellington Doctoral Scholarship — NZ$32,000 a year plus domestic tuition fees for up to three years, about 110 a year, with three rounds a year. The next round closes on 1 November 2026. One warning: the old Tongarewa International Scholarship was stopped from 2026 — do not apply for it, and do not trust pages that still list its NZ$10,000 / NZ$5,000 awards as current.',
 dpill='Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
 facts=facts([('Award', 'VUW Undergraduate International Scholarship: NZ$15,000 toward tuition for one year (first enrolment). VUW Postgraduate International Scholarship: NZ$10,000 toward tuition for a master’s or postgraduate diploma. Wellington Doctoral Scholarship: NZ$32,000 a year stipend plus domestic tuition fees, up to 3 years, about 110 awards a year. Manaaki New Zealand Scholarships are a separate New Zealand government award (fully funded) — not a VUW award.'),
              ('Eligible', 'International students paying full international fees who are new to Victoria University of Wellington and hold a conditional or unconditional Offer of Place — for a bachelor’s (UG award) or a master’s / postgraduate diploma (PG award). Doctoral: international and domestic graduates of any university, normally with a First Class Honours-equivalent degree and strong research potential; people who already hold a doctorate cannot apply.'),
              ('How', 'Apply for admission first. The UG and PG International Scholarships are automatic — there is no separate form; eligible students are told in their offer letter. The Wellington Doctoral Scholarship needs a separate scholarship application after the admission application, with references, submitted before 4:30 pm NZ time on the closing date.'),
              ('Deadline', 'Wellington Doctoral Scholarship: 1 November 2026 (next round; then 1 March and 1 July 2027). VUW Undergraduate / Postgraduate International Scholarships: no separate deadline — they close when applications for your course close. One source lists 1 September for Trimester 1 and another lists 31 December 2026 — conflicting; check the official page.'),
              ('Fine print', 'The Tongarewa International Scholarship was stopped from 2026 — pages listing "10 awards of NZ$10,000 and 9 awards of NZ$5,000" describe the discontinued scheme, not the current awards. The doctoral stipend is NZ$32,000 a year on the most recent sources; one older page says NZ$30,500 and another (Tongarewa-era) says NZ$27,500 — both superseded. The $15,000 PG figure on one aggregator conflicts with the $10,000 PG figure on a newer source; the article uses UG $15,000 / PG $10,000.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Victoria University of Wellington — Te Herenga Waka</strong> — in Wellington, New Zealand, offers international scholarships at every level, and the system changed in 2025: the <strong>VUW Undergraduate International Scholarship</strong> and the <strong>VUW Postgraduate International Scholarship</strong> were established in August 2025, replacing and combining several previous awards including the <strong>Tongarewa International Scholarship</strong>, the Latin American Academic Achievement Scholarship, the International Alumni Fees Waiver and the New Zealand International School-Leaver Grant. Tongarewa itself was <strong>stopped from 2026</strong> — any page still listing its awards as current is out of date.</p>
      <p>The two new awards are refreshingly simple: the <strong>Undergraduate International Scholarship is NZ$15,000</strong> off first-year tuition for new international students starting a bachelor’s, and the <strong>Postgraduate International Scholarship is NZ$10,000</strong> off fees for a master’s or postgraduate diploma. Both are <strong>automatic</strong> — there is no separate application; if you are eligible, Victoria tells you in your offer letter, and the scholarship is applied directly to your tuition fees. The research award is the <strong>Wellington Doctoral Scholarship</strong>: a <strong>NZ$32,000 annual stipend plus domestic tuition fees</strong> for up to three years, with about <strong>110 scholarships a year</strong> across three rounds (1 March, 1 July, 1 November). The next round closes on <strong>1 November 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student paying full international fees</strong> (not a citizen of New Zealand or Australia).</li>
        <li>Be <strong>new to Victoria University of Wellington</strong> and entering your <strong>first year</strong> of a bachelor’s (UG award) or starting a <strong>master’s or postgraduate diploma</strong> (PG award).</li>
        <li>Hold a <strong>conditional or unconditional Offer of Place</strong> for the programme.</li>
        <li>For the <strong>Wellington Doctoral Scholarship</strong>: be a domestic or international graduate of any university, normally holding a bachelor’s or master’s degree with academic distinction equal to <strong>First Class Honours</strong> from a New Zealand university, with strong research potential. People who already hold a doctorate cannot apply.</li>
        <li>Show a <strong>strong academic record</strong> — doctoral awards are based on academic merit.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>VUW Undergraduate International Scholarship:</strong> <strong>NZ$15,000</strong> toward tuition, for one year (first enrolment only).</li>
        <li><strong>VUW Postgraduate International Scholarship:</strong> <strong>NZ$10,000</strong> toward tuition, for a master’s or postgraduate diploma.</li>
        <li><strong>Wellington Doctoral Scholarship:</strong> <strong>NZ$32,000 a year</strong> stipend plus <strong>domestic tuition fees</strong>, for up to <strong>3 years</strong>; about <strong>110 awards a year</strong>.</li>
        <li><strong>Not a VUW award:</strong> the <strong>Manaaki New Zealand Scholarships</strong> are a separate New Zealand government award (tuition + living + travel + insurance) for students from eligible partner countries.</li>
        <li><strong>Not current:</strong> the <strong>Tongarewa International Scholarship</strong> (NZ$10,000 / NZ$5,000 awards) was stopped from 2026.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>None separate for the UG/PG International Scholarships</strong> — they are assessed from your application for study.</li>
        <li>For <strong>admission</strong>: academic <strong>transcripts and degree certificates</strong>, and an <strong>Offer of Place</strong> (conditional or unconditional).</li>
        <li>For the <strong>Wellington Doctoral Scholarship</strong>: a <strong>personal statement (max 500 words)</strong> covering study goals, motivation and leadership experience, plus <strong>references</strong> and evidence of research output (thesis, publications) where available.</li>
        <li>All doctoral documents, including references, must arrive by <strong>4:30 pm NZ time on the closing date</strong> — late documents are not accepted.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to Victoria University of Wellington for your bachelor’s, master’s, postgraduate diploma or PhD.</li>
        <li>For the <strong>UG/PG International Scholarships</strong>: do nothing extra — if you are eligible, the scholarship appears in your <strong>offer letter</strong> and is credited to your tuition fees.</li>
        <li>For the <strong>Wellington Doctoral Scholarship</strong>: apply for <strong>PhD admission first</strong>, then submit the <strong>separate scholarship application</strong> with references before <strong>4:30 pm NZ time on 1 November 2026</strong>.</li>
        <li>For <strong>Manaaki New Zealand Scholarships</strong>: apply separately through the New Zealand government scheme for your country — not through VUW.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for Victoria University of Wellington Scholarships 2027?',
  'The Wellington Doctoral Scholarship closes 1 November 2026 (next round; then 1 March and 1 July 2027). The UG and PG International Scholarships have no separate deadline — they close when applications for your course close.'),
 ('Do I need a separate application for the VUW International Scholarships?',
  'No. There is no separate form: if you are eligible, Victoria tells you in your offer letter. The Wellington Doctoral Scholarship is the exception — it needs a separate application after your PhD admission application.'),
 ('How much is the VUW Undergraduate International Scholarship?',
  'NZ$15,000 toward tuition for one year, for new international students entering their first year of a bachelor’s. The postgraduate award is NZ$10,000.'),
 ('What is the Wellington Doctoral Scholarship worth?',
  'NZ$32,000 a year plus domestic tuition fees, for up to three years. About 110 scholarships are offered each year across three rounds.'),
 ('Is the Tongarewa Scholarship still available?',
  'No. Victoria stopped offering the Tongarewa International Scholarship from 2026. Its replacement is the VUW Undergraduate/Postgraduate International Scholarship. Pages still listing Tongarewa awards as current are out of date.'),
 ('Are Manaaki New Zealand Scholarships the same as VUW scholarships?',
  'No. Manaaki is a separate New Zealand government award (fully funded: tuition, living, travel and insurance) for students from eligible partner countries. Apply through the government scheme, not through VUW.')]) + '''
      <p class="verify">Verified 27 Oct 2026: yasassri.me, "New Zealand Scholarships 2027: Deadlines Sri Lankans Can't Miss" (updated 13 days ago) — VUW Undergraduate International Scholarship $15,000 off first-year fees for new international students starting a bachelor's; VUW Postgraduate International Scholarship $10,000 off fees for a master's or postgraduate diploma; automatic — "you don't apply separately... Victoria tells you in your offer letter. There's no extra deadline. It closes when applications for your course close"; "You might see the old Tongarewa Scholarship on other websites. Victoria stopped offering it from 2026"; thecareernews.org (reproducing VUW's own scholarship finder) — VUW Undergraduate International Scholarship NZ$15,000, deadline 1 September (Trimester 1 start); VUW Postgraduate International Scholarship, partial tuition support, 1 September; Wellington Doctoral Scholarship NZ$30,500/year + full tuition up to 3 years, rounds 1 March, 1 July, 1 November; established August 2025, replacing Tongarewa, Latin American Academic Achievement Scholarship, International Alumni Fees Waiver and NZ International School-Leaver Grant; careerglobalconnect.com, 27 Sep 2026 — Wellington Doctoral Scholarship $32,000/year + domestic tuition fees, up to 3 years, ~110/year, rounds 1 March, 1 July, 1 November; scholarshipsguider.com — same figures ($32,000/year, ~110/year, 4:30 pm NZ time closing, First Class Honours equivalent, next round 1 Nov 2026); myschoolscholarships.org — VUW International Scholarships valued at $15,000, deadline 31 December 2026, requires Offer of Place, new students only; Bright Scholarship (queue URL) — corroboration. CONFLICTS: (1) the doctoral stipend is $32,000/year on the two most recent sources; thecareernews says $30,500 and one Tongarewa-era page says $27,500 — the article uses $32,000. (2) the PG award is $10,000 (yasassri, recent) vs $15,000 (myschoolscholarships) — the article uses UG $15,000 / PG $10,000. (3) the UG/PG deadline is 1 September for Trimester 1 (thecareernews) vs 31 December 2026 (myschoolscholarships) — the article states no separate deadline and flags both. (4) the "10 awards of NZ$10,000 + 9 awards of NZ$5,000" figures on engineersjob.in are the discontinued Tongarewa scheme — not used as current. The official wgtn.ac.nz scholarship pages could not be opened by text fetch in this check — no wgtn.ac.nz URL is cited that was not verified here.</p>''',
 dl_long='1 November 2026 (Wellington Doctoral Scholarship round) · UG/PG awards have no separate deadline',
 offlinks=[('Bright Scholarship — Victoria University of Wellington Scholarships 2027', 'https://brightscholarship.com/victoria-university-of-wellington-scholarships-2027/'),
           ('The Career News — University of Wellington scholarships (VUW scholarship finder)', 'https://thecareernews.org/scholrships/university-of-wellington/')],
 related_titles=['lincoln-nz-2027', 'auckland', 'waikato2027', 'deakin-vc-2027'])),

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
    json.dump(sizes, open('/tmp/batch56_built.json','w'))

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

#!/usr/bin/env python3
"""Batch 51 (cron run 51, 26 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Doha Institute for Graduate Studies Scholarships 2027 — VERIFIED: deadline
   15 Jan 2027. Tamim (merit, full package) + Sanad (need-based 10-100%
   tuition). Two-stage: admission first, scholarship form after admission.
   Stipend amount NOT published - tracker figures not used.
2. FAO Young Professionals Program 2026 — SKIPPED: main 2026 YPP round
   closed 7 Sep 2026 (individual YPO vacancies are posted separately).
3. University of Minho Research Fellowship 2027 — SKIPPED: aggregator
   composite, no single scheme; the Architecture call (Lab2PT,
   EUR 1,090.98/month) closed 28 Aug 2026.
4. Croatia Scholarships Without IELTS 2027 — SKIPPED: listicle.
5. University of Toronto Postdoctoral Fellowship 2027 — SKIPPED: the
   Schmidt AI in Science Postdoc Fellowship closed 5 Oct 2026. (The UTSC
   Inclusive Excellence Postdoctoral Fellowship is a different, still-open
   scheme, 10 Nov 2026, restricted to Indigenous/Black researchers.)
6. Malmo University PhD Positions 2026 — SKIPPED: aggregator composite
   of individual doctoral vacancies; the 2026 vacancies closed 14/31 Aug
   2026. One tracker now shows the multi-omics vacancy with a 15 Nov 2026
   deadline, conflicting with the 31 Aug date - unresolved.
7. OHCHR Indigenous Fellowship 2027 — SKIPPED: deadline passed
   (6 Sep 2026; some trackers say 13 Sep 2026).
8. Mitacs Globalink Research Internship (GRI) 2027 — SKIPPED: deadline
   passed 16 Sep 2026, 1:00 p.m. PT.
9. Coca Cola Scholarship 2027 — SKIPPED: deadline passed 30 Sep 2026,
   5 p.m. ET (Coca-Cola Scholars Program, $20,000, 150 scholars).
10. Fully Funded University of Leeds PhD Scholarship 2027 — VERIFIED:
    Leeds Doctoral Scholarship. Deadline 23 Mar 2027, 17:00 UK time.
    Up to 5 awards, Home fee-rated students ONLY, full fees + GBP 21,805
    (2026/27 rate) for 3.5 years, start 1 Oct 2027. CORRECTION: Bright's
    page describes the School of Computer Science studentship (mixed
    precision methods), whose deadline passed 30 Sep 2026 and which was
    open to internationals - a different award, not this one.
11. Scholarships in Canada 2027 — SKIPPED: listicle.
12. Oregon State University Scholarships 2027 — SKIPPED: aggregator
    composite of many separate OSU awards.
13. National Tsing Hua University Scholarships 2027 — SKIPPED: Spring
    2027 deadline passed 30 Sep 2026.
14. Belgium Government ARES Scholarship 2027-28 — SKIPPED: closed
    18 Sep 2026.
15. Mental Health America Young Leaders Council 2027 — SKIPPED: deadline
    passed 28 Aug 2026.
16. Oxford Pershing Square Graduate Scholarship 2027 — VERIFIED: deadline
    6 Jan 2027 (1+1 MBA application; Master's deadline varies Dec/Jan).
    Up to 5 awards, full fees for both degrees + living grant at least
    GBP 21,805/year. No separate scholarship application - 500-word essay
    in the Funding section of the MBA application. Trackers differ (6/7/8
    Jan); Oxford's published deadline is 6 Jan 2027.
17. Yale Peace Fellowship 2027 — SKIPPED: deadline passed 9 Sep 2026.
18. Charles Sturt University International Scholarships 2027 — SKIPPED:
    aggregator composite; the queue title bundles the Success Scholarship
    (closes 31 Dec 2027), the Merit Scholarship (31 Dec 2026) and other
    awards under one "15 Jan 2027" deadline the official page does not
    confirm.
19. Full Ride USA Scholarship 2027 — SKIPPED: listicle, not a scheme.
20. WHO Business Operation Internship 2026 — SKIPPED: deadline passed
    21 Aug 2026.
21. Fully Funded FRIAS Fellowship Programmes 2026-27 — SKIPPED: deadline
    passed 18 Sep 2026.
22. Anhalt University STIBET Scholarships 2027 — VERIFIED: deadline
    15 Apr 2027. EUR 400/month for 3 months (EUR 1,200 total), DAAD /
    Federal Foreign Office funded. Two categories: Graduation Scholarship
    and Scholarship for Particularly Committed Students. Only for
    international students ALREADY enrolled at Anhalt. CORRECTION:
    "(Funded)" is misleading - partial short-term grant, not full funding.
23. Wissenschaftskolleg zu Berlin Fellowships 2027 — VERIFIED: the
    still-open College for Life Sciences (life and natural sciences)
    early-career call, deadline 1 Nov 2026, 23:59 CET (official
    wiko-berlin.de). 10 months, 2027/28 academic year; up to EUR 5,100/
    month for fellows without institutional income. CORRECTION: the
    humanities/social sciences early-career call closed 1 Sep 2026.
24. Olympic Refuge Foundation Remote Fellowship 2026-27 — SKIPPED:
    deadline passed 19 Aug 2026.

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
 'doha-2027': {'mono': 'DI', 'title': 'Doha Institute for Graduate Studies Scholarships 2027 in Qatar (Fully Funded)',
   'href': 'doha-institute-graduate-studies-scholarships-2027-qatar.html',
   'dpill': 'Deadline 15 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-15'),
   'award': 'Two tracks: the merit-based Tamim Scholarship (full tuition, dormitory, monthly stipend, health insurance, two travel tickets) and the need-based Sanad Scholarship (10\u2013100% of tuition). The stipend amount is not published.',
   'elig': 'All nationalities, Qatari and international, for Master\u2019s and PhD study in social sciences, humanities, public administration and development economics. Bachelor\u2019s degree for Master\u2019s; Master\u2019s degree for PhD.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Qatar', 'teal')]},
 'leeds-2027': {'mono': 'UL', 'title': 'Fully Funded University of Leeds PhD Scholarship 2027 (\u00a321,805 Stipend)',
   'href': 'leeds-doctoral-scholarship-2027-uk.html',
   'dpill': 'Deadline 23 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-23'),
   'award': 'The Leeds Doctoral Scholarship: up to 5 awards, full fees plus a \u00a321,805 maintenance grant a year (2026/27 rate) for 3.5 years, starting 1 October 2027. UK/Home fee-rated students only.',
   'elig': 'UK/Home fee-rated students only, new postgraduate researchers with at least a First Class Honours degree (or a Master\u2019s with Distinction), in any Faculty.',
   'tags': [('PhD', 'blue'), ('UK', 'teal')]},
 'pershing-2027': {'mono': 'OX', 'title': 'Oxford Pershing Square Graduate Scholarship 2027 in UK (Fully Funded)',
   'href': 'oxford-pershing-square-graduate-scholarship-2027-uk.html',
   'dpill': 'Deadline 6 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-06'),
   'award': 'Up to five full awards for the Oxford 1+1 MBA: course fees for both the Master\u2019s degree and the MBA, plus a living-cost grant of at least \u00a321,805 for each year of study.',
   'elig': 'All nationalities, admitted to both a 1+1 MBA partnering Master\u2019s programme and the Oxford MBA, with leadership potential and a commitment to addressing world-scale social challenges.',
   'tags': [('Master\u2019s + MBA', 'purple'), ('UK', 'teal')]},
 'anhalt-stibet-2027': {'mono': 'AH', 'title': 'Anhalt University STIBET Scholarships 2027 in Germany (Funded)',
   'href': 'anhalt-university-stibet-scholarships-2027-germany.html',
   'dpill': 'Deadline 15 Apr 2027 \u00b7 %d days left' % dl_left('2027-04-15'),
   'award': 'A short-term grant of \u20ac400 a month for three months (\u20ac1,200 in total) for international students already enrolled at Anhalt \u2014 a graduation scholarship or a scholarship for particularly committed students. Not full funding.',
   'elig': 'International students already enrolled full-time at Anhalt University of Applied Sciences in a Bachelor\u2019s or Master\u2019s programme, with good or very good grades, in their final stage or with proven voluntary engagement.',
   'tags': [('Bachelor\u2019s & Master\u2019s', 'blue'), ('Germany', 'teal')]},
 'wiko-2027': {'mono': 'WK', 'title': 'Wissenschaftskolleg zu Berlin Fellowships 2027 in Germany (Fully Funded)',
   'href': 'wissenschaftskolleg-berlin-fellowships-2027-germany.html',
   'dpill': 'Deadline 1 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-01'),
   'award': 'A 10-month residential fellowship in Berlin for early-career researchers in the life and natural sciences, 2027/28 academic year: up to \u20ac5,100 a month for fellows without institutional income, plus accommodation.',
   'elig': 'Early-career researchers in the life and natural sciences with a PhD or MD, at least one peer-reviewed publication as main author, working outside a Berlin-based organisation.',
   'tags': [('Fellowship', 'purple'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Doha
A.append(dict(
 slug='doha-institute-graduate-studies-scholarships-2027-qatar',
 title='Doha Institute for Graduate Studies Scholarships 2027 in Qatar (Fully Funded)',
 meta='Doha Institute for Graduate Studies Scholarships 2027: the merit-based Tamim Scholarship (full tuition, dormitory, stipend, health insurance, two travel tickets) and the need-based Sanad Scholarship (10\u2013100% of tuition) for Master\u2019s and PhD study in Qatar. Deadline 15 January 2027 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Doha Institute Graduate Studies Scholarships 2027', kicker='Qatar \u00b7 Master\u2019s & PhD \u00b7 Fully Funded', mono='DI',
 prov_short='Doha Institute for Graduate Studies', prov_cat='Institute \u00b7 Qatar',
 h1='Doha Institute for Graduate Studies Scholarships 2027 in Qatar (Fully Funded)',
 sub='The Doha Institute for Graduate Studies Scholarships 2027 fund Master\u2019s and PhD study in Qatar through two tracks that work very differently: the merit-based Tamim Scholarship, which is a full package, and the need-based Sanad Scholarship, which covers 10% to 100% of tuition depending on your financial situation. Read the two tracks carefully before you apply, because picking the wrong one is the most common mistake \u2014 and note the two-stage process: you apply for admission first, and only admitted students receive the scholarship application form. The deadline is 15 January 2027.',
 dpill='Deadline 15 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-15'),
 facts=facts([('Award', 'Two scholarship tracks. The merit-based Tamim Scholarship is a full package for outstanding students: full tuition fee coverage, free accommodation in the institute\u2019s dormitories for international students, a monthly living stipend, health insurance, and two round-trip travel tickets (one on arrival, one after graduation). The need-based Sanad Scholarship covers 10% to 100% of programme fees depending on financial need; international students with a full Sanad award also receive dormitory housing, a stipend, health insurance and travel support. The monthly stipend amount is NOT published in the official notification \u2014 do not budget around a figure quoted by a tracker.'),
              ('Eligible', 'Open to all nationalities, Qatari and international, with no age limit reported. For a Master\u2019s, hold a Bachelor\u2019s degree from a recognised institution (final-year undergraduate students may also apply); for a PhD, hold a Master\u2019s degree. Applicants need a strong academic record and must meet the language requirements of their chosen programme (Arabic or English, depending on the programme). English proficiency can be shown with IELTS/TOEFL or with a university English-proficiency certificate if the previous degree was taught in English. PhD students may be asked to work 10\u201315 hours a week in teaching or research roles.'),
              ('How', 'Apply for admission through the Doha Institute\u2019s online admissions portal: create an account, choose a programme, and upload your documents. Admitted students then receive the scholarship application form from the Admissions Office and complete it. Only one application per candidate is allowed \u2014 duplicate applications are rejected. There is no application fee.'),
              ('Deadline', '15 January 2027. Applications opened on 1 September 2026. The academic year starts in August 2027. One tracker gives an admission window ending 5 January 2027; that date was not confirmed, and the 15 January 2027 deadline is used here.'),
              ('Fine print', 'The scholarship is not automatic on admission \u2014 admission comes first, and the scholarship form follows. The two tracks are different awards: Tamim is merit-based and full, Sanad is need-based and ranges from 10% to 100% of tuition, so a Sanad award does not always mean full funding. The stipend amount is not published, and the "QAR 4,000\u20135,000 a month" figure quoted by one tracker was not confirmed and is not used here. Programmes are in social sciences, humanities, public administration and development economics \u2014 not in engineering or natural sciences.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>Doha Institute for Graduate Studies</strong>, founded in Doha in 2014 by the Arab Center for Research and Policy Studies, is Qatar\u2019s dedicated graduate research institute, focused on the <strong>social sciences, humanities, public administration and development economics</strong> rather than the broad multi-faculty model of most universities. Its scholarships fund Master\u2019s and PhD study through two tracks that sit side by side: the <strong>Tamim Scholarship</strong>, awarded on academic merit, and the <strong>Sanad Scholarship</strong>, awarded on financial need.</p>
      <p>The Tamim Scholarship is the full package: <strong>full tuition, free dormitory accommodation</strong> for international students, a <strong>monthly living stipend</strong>, <strong>health insurance</strong> and <strong>two round-trip travel tickets</strong>. The Sanad Scholarship is different \u2014 it covers <strong>10% to 100% of programme fees</strong> depending on need, with the same additional benefits for international students on full awards. The important thing to understand is that the two tracks are not interchangeable: Tamim rewards academic distinction, Sanad supports financial need, and a Sanad award does not always mean full funding.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be of <strong>any nationality</strong> \u2014 Qatari and international students are both eligible, with <strong>no age limit</strong> reported.</li>
        <li>For a Master\u2019s, hold a <strong>Bachelor\u2019s degree</strong> from a recognised institution; <strong>final-year undergraduate students may also apply</strong>.</li>
        <li>For a PhD, hold a <strong>Master\u2019s degree</strong>.</li>
        <li>Demonstrate a <strong>strong academic record</strong> (usually a GPA of 3.0 or above; higher for PhD).</li>
        <li>Meet the <strong>language requirements</strong> of the chosen programme (Arabic or English). English proficiency can be shown with IELTS/TOEFL or with a university English-proficiency certificate if your previous degree was taught in English.</li>
        <li>Note that <strong>PhD students may be asked to work 10\u201315 hours a week</strong> in teaching or research roles.</li>
        <li>Apply to a programme in the institute\u2019s fields: <strong>social sciences, humanities, public administration or development economics</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tamim Scholarship (merit-based):</strong> full tuition fee coverage, free accommodation in institute dormitories, a monthly living stipend, health insurance, and two round-trip travel tickets.</li>
        <li><strong>Sanad Scholarship (need-based):</strong> tuition coverage from <strong>10% to 100%</strong> depending on financial need; international students on full awards also receive dormitory housing, a stipend, health insurance and travel support.</li>
        <li><strong>No application fee</strong> for admission.</li>
        <li>Note that the <strong>monthly stipend amount is not published</strong> in the official notification \u2014 do not budget around a figure quoted by a tracker.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A valid <strong>passport</strong> (or Qatari ID for citizens/residents).</li>
        <li>Your <strong>Bachelor\u2019s degree certificate</strong> (or Master\u2019s certificate for PhD) and <strong>official academic transcripts</strong>.</li>
        <li>An updated <strong>CV</strong>.</li>
        <li>A <strong>personal statement</strong> and an <strong>academic essay</strong>.</li>
        <li><strong>Two letters of recommendation</strong> (academic references preferred).</li>
        <li><strong>English or Arabic proficiency evidence</strong> (IELTS/TOEFL, or a university English-proficiency certificate).</li>
        <li>A <strong>research proposal</strong> (for PhD programmes).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Visit the <strong>Doha Institute admissions portal</strong> and review the Master\u2019s and PhD programmes and their requirements.</li>
        <li>Create an <strong>account</strong> on the online admission portal and choose your programme.</li>
        <li>Complete the <strong>admission application</strong> and upload all required documents.</li>
        <li>Submit <strong>only one application</strong> \u2014 duplicate applications are rejected.</li>
        <li>If admitted, complete the <strong>scholarship application form</strong> sent by the Admissions Office.</li>
        <li>Submit everything by <strong>15 January 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Doha Institute Scholarships 2027?',
  '15 January 2027. Applications opened on 1 September 2026, and the academic year starts in August 2027. One tracker gives an admission window ending 5 January 2027; that date was not confirmed, and the 15 January 2027 deadline is used here.'),
 ('What is the difference between the Tamim and Sanad Scholarships?',
  'Tamim is merit-based and a full package: full tuition, dormitory, monthly stipend, health insurance and two travel tickets. Sanad is need-based and covers 10% to 100% of tuition depending on financial need, with the same additional benefits for international students on full awards.'),
 ('Is the Doha Institute Scholarship fully funded?',
  'The Tamim Scholarship is fully funded. The Sanad Scholarship is not always full \u2014 it ranges from 10% to 100% of tuition depending on need.'),
 ('Do I need IELTS or TOEFL?',
  'Not necessarily. English proficiency can be shown with IELTS/TOEFL or with a university English-proficiency certificate if your previous degree was taught in English. Check the language requirements of your chosen programme.'),
 ('How much is the monthly stipend?',
  'The stipend amount is not published in the official notification. Do not rely on a figure quoted by a tracker \u2014 the "QAR 4,000\u20135,000 a month" figure given by one tracker was not confirmed.'),
 ('Do I apply for the scholarship separately?',
  'No separate scholarship application at the start. You apply for admission first; admitted students receive the scholarship application form from the Admissions Office and complete it.'),
 ('Who can apply?',
  'Students of all nationalities, Qatari and international, with no age limit reported. A Bachelor\u2019s degree is needed for a Master\u2019s (final-year students may apply) and a Master\u2019s degree for a PhD.')]) + '''
      <p class="verify">Verified 26 Oct 2026: scholarshipsedge.com, insurab.com, opportunitiesradar.com, scholarshipshive.com, scholarships.af, engineersjob.in \u2014 deadline 15 January 2027, applications opened 1 September 2026, Tamim merit-based full package (tuition, dormitory, stipend, health insurance, two travel tickets), Sanad need-based 10\u2013100% of tuition, two-stage process (admission first, scholarship form after admission), documents list, no age limit, academic year starts August 2027. The monthly stipend amount is not published in the official notification; tracker figures (for example QAR 4,000\u20135,000 a month, and one tracker\u2019s QAR 60,000\u2013180,000 a month) were not confirmed and are not used. One tracker gives an admission window ending 5 January 2027; the 15 January 2027 deadline is used here.</p>''',
 dl_long='15 January 2027',
 offlinks=[('Bright Scholarship \u2014 Doha Institute for Graduate Studies Scholarships 2027', 'https://brightscholarship.com/doha-institute-for-graduate-studies-scholarships-2027/'),
           ('Scholarships Edge \u2014 Doha Institute for Graduate Studies Scholarship 2027', 'https://scholarshipsedge.com/doha-institute-for-graduate-studies-scholarship/')],
 related_titles=['kaust-2027', 'alqasimi-2027', 'google-srp-2027', 'mbzuai'])),

# ---------------------------------------------------------------- 2. Leeds
A.append(dict(
 slug='leeds-doctoral-scholarship-2027-uk',
 title='Fully Funded University of Leeds PhD Scholarship 2027 (\u00a321,805 Stipend)',
 meta='University of Leeds PhD Scholarship 2027: the Leeds Doctoral Scholarship pays full fees plus a \u00a321,805 maintenance grant a year for 3.5 years, for up to 5 Home fee-rated PhD students in any Faculty. Deadline 23 March 2027 \u2014 eligibility, how to apply and FAQs.',
 short='Leeds Doctoral Scholarship 2027', kicker='UK \u00b7 PhD \u00b7 Fully Funded', mono='UL',
 prov_short='University of Leeds', prov_cat='University \u00b7 United Kingdom',
 h1='Fully Funded University of Leeds PhD Scholarship 2027 (\u00a321,805 Stipend)',
 sub='The University of Leeds PhD Scholarship 2027 is the Leeds Doctoral Scholarship: up to five awards covering full fees plus a \u00a321,805 maintenance grant a year for three and a half years, for PhD study in any Faculty. Read the eligibility line first, because it decides everything: this scholarship is for UK/Home fee-rated students only. If you are an international student on a Student visa, this award is not for you \u2014 and the listing that describes it as open worldwide is describing a different award. The deadline is 23 March 2027.',
 dpill='Deadline 23 Mar 2027 \u00b7 %d days left' % dl_left('2027-03-23'),
 facts=facts([('Award', 'The Leeds Doctoral Scholarship: up to 5 awards for Session 2027/28, covering full academic fees and a tax-free maintenance grant of \u00a321,805 a year (2026/27 rate, rising in line with UKRI rates), for 3.5 years of full-time study (pro-rata part-time). Funding starts on 1 October 2027. Selection is on academic merit and ability; financial hardship is not considered. This is a fully funded award \u2014 but only for Home fee-rated students.'),
              ('Eligible', 'UK/Home fee-rated students only. You must be a new postgraduate researcher undertaking a PhD (not already registered on a PhD, and not previously awarded a PhD; students who started a PhD but did not complete it may be considered). Hold a first undergraduate degree equivalent to at least a UK First Class Honours degree; final-year undergraduates expected to achieve it may apply. Candidates with a lower undergraduate degree may be considered if they have, or expect to obtain, a Distinction in a relevant Master\u2019s degree. Meet the English-language requirements for postgraduate research study \u2014 normally IELTS 6.0 overall, with at least 5.5 in each component, though some Schools or Faculties may require a higher score. You must live within reasonable distance of the University of Leeds while receiving the scholarship.'),
              ('How', 'Two stages. Stage 1: apply for a PhD programme at the University of Leeds (research proposal, transcripts, CV, two references) and get your 9-digit student ID. Stage 2: submit the online scholarship form using that student ID. Your School nominates candidates; there is no financial-need criterion.'),
              ('Deadline', '23 March 2027, 17:00 UK time. Some trackers give a 1 April 2027 deadline; the University of Leeds\u2019 own funding pages list Tuesday 23 March 2027, which is used here.'),
              ('Fine print', 'Do not confuse this with the School of Computer Science studentship on "Mixed precision methods for numerical linear algebra at exascale", which Bright Scholarship\u2019s page describes: that studentship was open to UK and international students, but its deadline passed on 30 September 2026 and it is a different award with one funded place. This article covers the Leeds Doctoral Scholarship only \u2014 up to 5 awards, Home fee-rated students only, deadline 23 March 2027. The award is initially for one year and renewable on satisfactory progress.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Leeds Doctoral Scholarship</strong> is the University of Leeds\u2019 main funded PhD award for home students: <strong>up to five scholarships</strong> for Session 2027/28, available for research degree study in <strong>any Faculty</strong> \u2014 Arts, Humanities and Cultures; Biological Sciences; Business; Environment; Medicine and Health; and Social Sciences. You can propose your own research project or apply for an available linked PhD project, and you are encouraged to identify an appropriate supervisor and School or Faculty before you apply.</p>
      <p>The funding is genuinely full: <strong>full academic fees</strong> plus a tax-free <strong>maintenance grant of \u00a321,805 a year</strong> (the 2026/27 rate, rising in line with UKRI rates), for <strong>3.5 years</strong> of full-time study. But the eligibility is narrow in one decisive way: the award is for <strong>Home fee-rated students only</strong>. International students on a Student visa are not eligible for this scheme, and should look instead at the university\u2019s international routes \u2014 for example the China Scholarship Council / University of Leeds Scholarships, which close on 6 January 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be eligible for <strong>UK/Home fee status</strong>.</li>
        <li>Be a <strong>new postgraduate researcher</strong> undertaking a PhD \u2014 not already registered on a PhD, and not previously awarded a PhD. Students who started a PhD but did not complete it may be considered.</li>
        <li>Hold a first undergraduate degree equivalent to at least a <strong>UK First Class Honours degree</strong>; final-year undergraduates expected to achieve it may apply.</li>
        <li>Candidates with a lower undergraduate degree may be considered if they have, or expect to obtain, a <strong>Distinction in a relevant Master\u2019s degree</strong>. Relevant professional experience may also be considered.</li>
        <li>Meet the <strong>English-language requirements</strong> for postgraduate research study \u2014 normally <strong>IELTS 6.0 overall, with at least 5.5 in each component</strong>, or an equivalent qualification. Some Schools or Faculties may require a higher score.</li>
        <li>Live within a <strong>reasonable distance of the University of Leeds</strong> while receiving the scholarship.</li>
        <li>Take up the award by <strong>1 October 2027</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full academic fees</strong> for three years of full-time study (pro-rata part-time).</li>
        <li>A tax-free <strong>maintenance grant of \u00a321,805 a year</strong> (2026/27 rate), rising in line with UKRI rates, for <strong>3.5 years</strong> full-time.</li>
        <li>Available in <strong>any Faculty</strong> \u2014 propose your own project or apply for a linked PhD project.</li>
        <li>Full-time or part-time study (part-time awards are pro-rata).</li>
        <li>Note that the award is <strong>initially for one year</strong> and renewable on satisfactory academic progress.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Stage 1 (PhD programme):</strong> PhD application form, <strong>research proposal</strong>, academic <strong>transcripts</strong>, <strong>CV</strong>, and <strong>two references</strong>.</li>
        <li><strong>Stage 2 (scholarship):</strong> the online <strong>scholarship form</strong>, which needs your <strong>9-digit student ID</strong> from the PhD application.</li>
        <li><strong>English-language evidence</strong> (for example IELTS 6.0 overall, with at least 5.5 in each component) as your programme requires.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>PhD programme and supervisor</strong> at the University of Leeds and check the programme\u2019s requirements.</li>
        <li>Submit your <strong>PhD application</strong> with your research proposal, transcripts, CV and two references, and receive your <strong>9-digit student ID</strong>.</li>
        <li>Submit the <strong>online scholarship form</strong> using that student ID.</li>
        <li>Your <strong>School nominates</strong> candidates \u2014 there is no financial-need criterion, and selection is on academic merit and ability.</li>
        <li>Submit the scholarship form by <strong>23 March 2027, 17:00 UK time</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Leeds Doctoral Scholarship open to international students?',
  'No. It is for UK/Home fee-rated students only. International students on a Student visa are not eligible for this scheme.'),
 ('How much is the Leeds Doctoral Scholarship worth?',
  'Full academic fees plus a tax-free maintenance grant of \u00a321,805 a year (the 2026/27 rate, rising in line with UKRI rates), for 3.5 years of full-time study. Up to five awards are available.'),
 ('What is the deadline for the Leeds Doctoral Scholarship 2027?',
  '23 March 2027, 17:00 UK time. Some trackers give 1 April 2027, but the University of Leeds\u2019 own funding pages list Tuesday 23 March 2027, which is used here.'),
 ('What is the difference between this and the Computer Science studentship?',
  'The Computer Science studentship on "Mixed precision methods for numerical linear algebra at exascale" was a different award with one funded place, open to UK and international students, whose deadline passed on 30 September 2026. This article covers the Leeds Doctoral Scholarship only.'),
 ('What grades do I need?',
  'A first undergraduate degree equivalent to at least a UK First Class Honours degree. If your undergraduate degree is lower, a Distinction in a relevant Master\u2019s degree (or relevant professional experience) may be considered.'),
 ('When does the funding start?',
  '1 October 2027. The award must be taken up by that date.')]) + '''
      <p class="verify">Verified 26 Oct 2026: phd.leeds.ac.uk (official funding search) \u2014 up to 5 Leeds Doctoral Scholarships for Home fee-rated students for Session 2027/28, application deadline Tuesday 23 March 2027; researchersjob.com \u2014 full fees, \u00a321,805 maintenance grant (2026/27 rate), 3.5 years, funding start 1 October 2027, First Class Honours or Master\u2019s Distinction, IELTS 6.0 overall with 5.5 in each component; ehsaskafaalat.com, scholarshiproar.com \u2014 corroboration. CORRECTION: Bright Scholarship\u2019s page describes the School of Computer Science studentship ("Mixed precision methods for numerical linear algebra at exascale"), whose deadline passed 30 September 2026 and which was open to international students \u2014 that is a different award and is not covered here. Some trackers give a 1 April 2027 deadline; the official page lists 23 March 2027, which is used here.</p>''',
 dl_long='23 March 2027, 17:00 UK time',
 offlinks=[('University of Leeds \u2014 PhD funding search (official)', 'https://phd.leeds.ac.uk/search?num_ranks=20&clive=leeds%7Eds-pgr-web-funding&query&collection=leeds%7Esp-pgr-meta&start_rank=1'),
           ('Bright Scholarship \u2014 University of Leeds PhD Scholarship 2027', 'https://brightscholarship.com/university-of-leeds-phd-scholarship/')],
 related_titles=['dalarna-2027', 'hasselt-mm-2027', 'leiden-lexs-2027', 'unil'])),

# ---------------------------------------------------------------- 3. Pershing Square
A.append(dict(
 slug='oxford-pershing-square-graduate-scholarship-2027-uk',
 title='Oxford Pershing Square Graduate Scholarship 2027 in UK (Fully Funded)',
 meta='Oxford Pershing Square Graduate Scholarship 2027: up to five full awards for the Oxford 1+1 MBA \u2014 course fees for both the Master\u2019s degree and the MBA, plus a living-cost grant of at least \u00a321,805 for each year of study. Deadline 6 January 2027 \u2014 eligibility, how to apply and FAQs.',
 short='Oxford Pershing Square Graduate Scholarship 2027', kicker='UK \u00b7 Master\u2019s + MBA \u00b7 Fully Funded', mono='OX',
 prov_short='University of Oxford', prov_cat='University \u00b7 United Kingdom',
 h1='Oxford Pershing Square Graduate Scholarship 2027 in UK (Fully Funded)',
 sub='The Oxford Pershing Square Graduate Scholarship 2027 funds up to five exceptional students through the Oxford 1+1 MBA: one year of a Master\u2019s degree, then the one-year Oxford MBA at Sa\u00efd Business School, with full course fees for both degrees and a living-cost grant of at least \u00a321,805 for each year of study. The catch is the double admission: you must be admitted to both programmes before you can be considered, and there is no separate scholarship application \u2014 your 500-word essay goes in the Funding section of the MBA application. The deadline is 6 January 2027.',
 dpill='Deadline 6 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-06'),
 facts=facts([('Award', 'Up to five full awards a year for the Oxford 1+1 MBA. The award covers course fees for both the Master\u2019s degree and the MBA programme, plus a grant for living costs of at least \u00a321,805 for each year of study. Scholars also get mentorship, conferences, termly and scholar community events, and a spring trek to New York hosted by the Pershing Square Foundation. The scholarship is funded in perpetuity by a \u00a313 million endowment from the Pershing Square Foundation and the University of Oxford.'),
              ('Eligible', 'All nationalities, with no age limit. You must be admitted both to a 1+1 MBA partnering programme and to the MBA before being considered \u2014 applicants on a waiting list are not considered. Priority order: (1) new applicants to the Oxford 1+1 MBA; (2) applicants admitted to both a full-time one-year Master\u2019s course not on the partnering list and the MBA; (3) current Master\u2019s students admitted to the MBA who were not considered in the previous year. You need the intention to focus on addressing world-scale social challenges, leadership potential, academic achievement (including degree results and GMAT or GRE score), and strong personal character and integrity.'),
              ('How', 'Apply to both programmes in the same application cycle: the Master\u2019s programme and the Oxford MBA. Upload the scholarship essay (maximum 500 words, answering "How do you intend to change the world, and what does this tell us about you as a person?") in the Funding section of the 1+1 MBA application. There is no separate scholarship application.'),
              ('Deadline', '6 January 2027 for the 1+1 MBA application. Your chosen Master\u2019s programme has its own application deadline in December 2026 or January 2027, which you must also meet. One tracker gives 7 January 2027 and another 8 January 2027; Oxford\u2019s published deadline is 6 January 2027, which is used here.'),
              ('Fine print', 'Admission to both programmes is a hard requirement \u2014 being on a waiting list for either one disqualifies you. Shortlisting takes place in early April 2027, with interviews in late April or early May. With only five awards a year and the double-admission requirement, this is one of the most competitive scholarships on this site.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Oxford-Pershing Square Graduate Scholarships</strong> are funded by the <strong>Pershing Square Foundation</strong> \u2014 established by Bill Ackman and Karen Ackman \u2014 in partnership with the <strong>University of Oxford</strong>. The Foundation\u2019s gift of <strong>\u00a37.8 million</strong>, combined with <strong>\u00a35.2 million</strong> from the University\u2019s Graduate Scholarship Matched Fund, created a <strong>\u00a313 million endowment</strong>, so the scholarship is funded in perpetuity rather than year to year.</p>
      <p>What makes this award different from most Oxford MBA scholarships is its scope. It does not fund the MBA year alone \u2014 it covers <strong>both degrees</strong> in the Oxford <strong>1+1 MBA</strong>: a one-year Master\u2019s degree in a specialist subject, then the one-year MBA at <strong>Sa\u00efd Business School</strong>. That is two full Oxford degrees, both fully funded, with living costs for each year of study, plus mentorship, conferences and a spring trek to New York. The price is the double admission: you must win a place on both programmes in the same cycle, and only then are you considered for one of the five awards.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be of <strong>any nationality</strong>; there is no age limit.</li>
        <li>Be <strong>admitted to both</strong> a 1+1 MBA partnering programme and the MBA before being considered \u2014 applicants on a <strong>waiting list are not considered</strong>.</li>
        <li>Priority is given to <strong>new applicants to the Oxford 1+1 MBA</strong>; then to applicants admitted to a full-time one-year Master\u2019s course not on the partnering list plus the MBA; then to current Master\u2019s students admitted to the MBA who were not considered in the previous year.</li>
        <li>Show the <strong>intention to focus on addressing world-scale social challenges</strong> in your career, in an existing organisation or through a new enterprise.</li>
        <li>Demonstrate <strong>leadership potential</strong> and <strong>academic achievement</strong>, including degree results and GMAT or GRE score.</li>
        <li>Show <strong>strong personal character, integrity and commitment</strong>, and a clear vision of how the 1+1 MBA will help you achieve your goals.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Course fees for both degrees</strong> \u2014 the Master\u2019s degree and the MBA.</li>
        <li>A <strong>living-cost grant of at least \u00a321,805 for each year of study</strong>.</li>
        <li><strong>Mentorship</strong>, conferences, termly and scholar community events.</li>
        <li>A <strong>spring trek to New York</strong> hosted by the Pershing Square Foundation.</li>
        <li>Two full Oxford degrees under one funding umbrella \u2014 the only award that funds the complete 1+1 MBA combination.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Academic transcripts</strong> and <strong>degree certificate</strong>.</li>
        <li>An updated <strong>CV</strong>.</li>
        <li>A <strong>statement of purpose</strong>.</li>
        <li>The <strong>scholarship essay</strong> (maximum 500 words): "How do you intend to change the world, and what does this tell us about you as a person?"</li>
        <li><strong>English-language evidence</strong> if your previous education was not in English.</li>
        <li><strong>GMAT or GRE scores</strong> and <strong>letters of recommendation</strong>, as the MBA and Master\u2019s applications require.</li>
        <li>A valid <strong>passport or identification document</strong>.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose an <strong>eligible Master\u2019s programme</strong> that participates in the Oxford 1+1 MBA Programme.</li>
        <li>Submit <strong>separate applications</strong> for the Master\u2019s programme and the Oxford MBA, in the same application cycle.</li>
        <li>Upload the <strong>scholarship essay</strong> (maximum 500 words) in the <strong>Funding section</strong> of the 1+1 MBA application.</li>
        <li>Make sure both applications are complete and submitted by their <strong>respective deadlines</strong> \u2014 the MBA by <strong>6 January 2027</strong>, the Master\u2019s by its own deadline in December 2026 or January 2027.</li>
        <li>There is <strong>no separate scholarship application</strong> \u2014 consideration is based on the two programme applications and the essay.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Oxford Pershing Square Scholarship fully funded?',
  'Yes. It covers full course fees for both the Master\u2019s degree and the MBA, plus a living-cost grant of at least \u00a321,805 for each year of study.'),
 ('How many scholarships are awarded each year?',
  'Up to five scholarships are awarded annually.'),
 ('What is the deadline for the Oxford Pershing Square Scholarship 2027?',
  '6 January 2027 for the 1+1 MBA application. Your chosen Master\u2019s programme has its own deadline in December 2026 or January 2027. One tracker gives 7 January and another 8 January 2027; Oxford\u2019s published deadline of 6 January 2027 is used here.'),
 ('Do I need to apply separately for the scholarship?',
  'No. There is no separate scholarship application. You apply to both programmes and upload the 500-word scholarship essay in the Funding section of the 1+1 MBA application.'),
 ('Can I apply if I am already a Master\u2019s student at Oxford?',
  'Current Master\u2019s students admitted to the MBA who were not considered for the scholarship in the previous year are considered, but at the lowest priority. New applicants to the 1+1 MBA are considered first.'),
 ('What is the scholarship essay question?',
  '"How do you intend to change the world, and what does this tell us about you as a person?" \u2014 in 500 words or fewer.')]) + '''
      <p class="verify">Verified 26 Oct 2026: sbs.ox.ac.uk (official Oxford-Pershing Square Graduate Scholarships page) \u2014 up to five full awards covering both the Master\u2019s and MBA degrees, living-cost grant of at least \u00a321,805 for each year of study, eligibility priority order, admission to both programmes required (waiting list not considered); gradualin.com, scholarshipsads.com, european-funding-guide.eu, youthexpat.com \u2014 deadline 6 January 2027, 500-word essay question, shortlisting early April 2027, interviews late April/early May, spring trek to New York, \u00a313 million endowment. One tracker gives 7 January 2027 and another 8 January 2027; Oxford\u2019s published deadline of 6 January 2027 is used here.</p>''',
 dl_long='6 January 2027 (1+1 MBA application; Master\u2019s programme deadline varies)',
 offlinks=[('University of Oxford \u2014 Oxford-Pershing Square Graduate Scholarships (official)', 'https://www.sbs.ox.ac.uk/oxford-experience/scholarships-and-funding/oxford-pershing-square-graduate-scholarships'),
           ('Bright Scholarship \u2014 Oxford Pershing Square Graduate Scholarship 2027', 'https://brightscholarship.com/oxford-pershing-square-graduate-scholarship-2027/')],
 related_titles=['au-egls-2027', 'alabama-2027', 'trudeau-2027', 'ucalgary-2027'])),

# ---------------------------------------------------------------- 4. Anhalt STIBET
A.append(dict(
 slug='anhalt-university-stibet-scholarships-2027-germany',
 title='Anhalt University STIBET Scholarships 2027 in Germany (Funded)',
 meta='Anhalt University STIBET Scholarships 2027: a short-term grant of \u20ac400 a month for three months (\u20ac1,200 in total) for international students already enrolled at Anhalt University of Applied Sciences \u2014 a graduation scholarship or a scholarship for particularly committed students. Deadline 15 April 2027 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Anhalt University STIBET Scholarships 2027', kicker='Germany \u00b7 Bachelor\u2019s & Master\u2019s \u00b7 \u20ac1,200 grant', mono='AH',
 prov_short='Anhalt University of Applied Sciences', prov_cat='University \u00b7 Germany',
 h1='Anhalt University STIBET Scholarships 2027 in Germany (Funded)',
 sub='The Anhalt University STIBET Scholarships 2027 pay \u20ac400 a month for three months \u2014 \u20ac1,200 in total \u2014 to international students already studying at Anhalt University of Applied Sciences in Germany. Read that sentence twice, because it contains the two things most listings get wrong. First, this is a short-term grant, not full funding: it does not cover tuition, travel or a full degree. Second, it is only for students already enrolled at Anhalt \u2014 if you are applying from outside Germany for admission, this scholarship is not for you. The deadline is 15 April 2027.',
 dpill='Deadline 15 Apr 2027 \u00b7 %d days left' % dl_left('2027-04-15'),
 facts=facts([('Award', '\u20ac400 a month for three consecutive months, \u20ac1,200 in total. The grant is funded by the DAAD and the Federal Foreign Office (STIBET programme). There are two categories: the Graduation Scholarship, for students close to completing their degree and writing their thesis; and the Scholarship for Particularly Committed Students, for students with a proven record of voluntary international or social activities. This is short-term financial assistance, not full funding \u2014 it does not cover tuition, travel, all living costs, health insurance or accommodation.'),
              ('Eligible', 'International students (non-German nationality) enrolled full-time in a Bachelor\u2019s or Master\u2019s programme at Anhalt University of Applied Sciences, with good or very good academic results. For the Graduation Scholarship: be in the final stage of your degree, have completed most required credits, plan to submit your thesis within one semester, and live in Germany during the funding period. For the Scholarship for Particularly Committed Students: have completed at least one semester at Anhalt and demonstrate active participation in recognised voluntary, international or social activities, with evidence. Prospective students applying from outside Germany are NOT eligible.'),
              ('How', 'Complete the online application form on the official scholarship webpage and submit all documents electronically. Upload a motivation letter (maximum 1,800 characters, one A4 page), your academic transcript (His-Qis extract), a tabular CV (maximum 2 pages), and a copy of your passport or identity card. Arrange for a professor at Anhalt to send a reference letter directly to stibet.scholarship@hs-anhalt.de. Optionally include a provisional timetable for degree completion and confirmation of registration for your final thesis or exam. The university confirms receipt of your application by email.'),
              ('Deadline', '15 April 2027. Late applications cannot be considered.'),
              ('Fine print', 'One tracker gives \u20ac600 a month; six sources give \u20ac400 a month, which is used here. The grant is for three months only, and the motivation letter is capped at 1,800 characters \u2014 about one A4 page. Simply attending events is not enough for the commitment category: active, documented participation is required. The scholarship is evaluated on academic achievement, the possibility of completing the degree within the funding period, the quality of the motivation letter, the professor\u2019s recommendation, and evidence of engagement.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>STIBET Scholarship</strong> at <strong>Anhalt University of Applied Sciences</strong> (Hochschule Anhalt) is a short-term grant funded by the <strong>DAAD</strong> and the <strong>Federal Foreign Office</strong>, designed to help international students in the final stage of their studies. It pays <strong>\u20ac400 a month for three months</strong> \u2014 <strong>\u20ac1,200 in total</strong> \u2014 so that a student can focus on finishing a thesis, or to recognise outstanding voluntary work in the university community.</p>
      <p>The important thing to understand is what this grant is not. It is not a degree scholarship and it is not open to new applicants: only <strong>international students already enrolled full-time at Anhalt</strong> can apply, in one of two categories. The <strong>Graduation Scholarship</strong> supports students close to finishing, who will submit their thesis within a semester. The <strong>Scholarship for Particularly Committed Students</strong> rewards students who have actively volunteered in international or social activities while keeping good grades. If you are already at Anhalt and in your final stage, \u20ac1,200 of breathing room is real money \u2014 but do not plan a degree around it.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> (non-German nationality) enrolled <strong>full-time</strong> in a Bachelor\u2019s or Master\u2019s programme at <strong>Anhalt University of Applied Sciences</strong>.</li>
        <li>Have <strong>good or very good academic results</strong>.</li>
        <li>For the <strong>Graduation Scholarship</strong>: be in the <strong>final stage</strong> of your degree, have completed <strong>most required credits</strong>, plan to submit your <strong>thesis within one semester</strong>, and <strong>live in Germany</strong> during the funding period.</li>
        <li>For the <strong>Scholarship for Particularly Committed Students</strong>: have completed <strong>at least one semester</strong> at Anhalt and demonstrate <strong>active participation</strong> in recognised voluntary, international or social activities, with evidence.</li>
        <li><strong>Prospective students</strong> applying from outside Germany are <strong>not eligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac400 a month</strong> for <strong>three months</strong> \u2014 <strong>\u20ac1,200 in total</strong>.</li>
        <li>Financial support to <strong>focus on your final thesis</strong> or recognition for <strong>voluntary community work</strong>.</li>
        <li>Short-term help with <strong>living costs</strong> during the final study period.</li>
        <li>Note that this is <strong>not full funding</strong> \u2014 it does not cover tuition, travel, all living costs, health insurance or accommodation.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application form</strong> on the official scholarship webpage.</li>
        <li>A <strong>motivation letter</strong> (maximum <strong>1,800 characters</strong>, one A4 page).</li>
        <li>Your <strong>academic transcript</strong> (His-Qis extract).</li>
        <li>A <strong>tabular CV</strong> (maximum 2 pages).</li>
        <li>A copy of your <strong>passport or identity card</strong>.</li>
        <li>A <strong>reference letter from a professor</strong> at Anhalt, sent directly to <strong>stibet.scholarship@hs-anhalt.de</strong>.</li>
        <li>Optional: a <strong>provisional timetable</strong> for degree completion and <strong>confirmation of registration</strong> for your final thesis or exam.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check that you meet <strong>one of the two categories</strong> \u2014 Graduation Scholarship or Scholarship for Particularly Committed Students.</li>
        <li>Complete the <strong>online application form</strong> on the official scholarship webpage.</li>
        <li>Upload your <strong>motivation letter</strong> (maximum 1,800 characters), <strong>His-Qis transcript</strong>, <strong>tabular CV</strong> (maximum 2 pages) and <strong>passport copy</strong>.</li>
        <li>Ask a <strong>professor at Anhalt</strong> to send your reference letter directly to <strong>stibet.scholarship@hs-anhalt.de</strong>.</li>
        <li>Optionally add your <strong>provisional timetable</strong> and <strong>thesis registration confirmation</strong>.</li>
        <li>Submit all documents <strong>electronically before 15 April 2027</strong>. The university confirms receipt by email.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Anhalt STIBET Scholarship fully funded?',
  'No. It is a short-term grant of \u20ac400 a month for three months, \u20ac1,200 in total. It does not cover tuition, travel, all living costs, health insurance or accommodation.'),
 ('Can students outside Germany apply?',
  'No. The scholarship is only for international students already enrolled full-time at Anhalt University of Applied Sciences. Prospective students applying for admission from outside Germany are not eligible.'),
 ('What is the deadline for the Anhalt STIBET Scholarships 2027?',
  '15 April 2027. Late applications cannot be considered.'),
 ('What are the two STIBET categories?',
  'The Graduation Scholarship, for students in the final stage of their degree who will submit their thesis within one semester; and the Scholarship for Particularly Committed Students, for students with a proven record of voluntary international or social activities at Anhalt.'),
 ('What documents do I need?',
  'A motivation letter (maximum 1,800 characters), your His-Qis academic transcript, a tabular CV (maximum 2 pages), a copy of your passport or identity card, and a reference letter from an Anhalt professor sent directly to stibet.scholarship@hs-anhalt.de.'),
 ('How much is the STIBET grant?',
  '\u20ac400 a month for three months, \u20ac1,200 in total. One tracker gives \u20ac600 a month; six sources give \u20ac400 a month, which is used here.')]) + '''
      <p class="verify">Verified 26 Oct 2026: scholarshipsads.com, coursmooc.com, scholarshipunion.com, scholarshipbob.com, ehsaskafaalat.com, study.abgram.in \u2014 deadline 15 April 2027, \u20ac400 a month for 3 months (\u20ac1,200 total), DAAD and Federal Foreign Office funding, two categories (Graduation Scholarship and Scholarship for Particularly Committed Students), documents (motivation letter max 1,800 characters, His-Qis transcript, tabular CV max 2 pages, passport copy, professor\u2019s reference letter to stibet.scholarship@hs-anhalt.de), current Anhalt students only. CORRECTION: the "(Funded)" label is misleading \u2014 this is a short-term \u20ac1,200 grant, not full funding, and it is not open to prospective students applying from outside Germany. One tracker (shiksha.com) gives \u20ac600 a month; six sources give \u20ac400 a month, which is used here.</p>''',
 dl_long='15 April 2027',
 offlinks=[('Bright Scholarship \u2014 Anhalt University STIBET Scholarships 2027', 'https://brightscholarship.com/anhalt-university-stibet-scholarships-2027/'),
           ('Scholarship Union \u2014 STIBET Scholarship 2027 in Germany', 'https://scholarshipunion.com/stibet-scholarship-2027-germany/')],
 related_titles=['dalarna-2027', 'hasselt-mm-2027', 'leiden-lexs-2027', 'unil'])),

# ---------------------------------------------------------------- 5. Wissenschaftskolleg Berlin
A.append(dict(
 slug='wissenschaftskolleg-berlin-fellowships-2027-germany',
 title='Wissenschaftskolleg zu Berlin Fellowships 2027 in Germany (Fully Funded)',
 meta='Wissenschaftskolleg zu Berlin Fellowships 2027: a 10-month residential fellowship in Berlin for early-career researchers in the life and natural sciences \u2014 up to \u20ac5,100 a month plus accommodation, no teaching or administration. Deadline 1 November 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Wissenschaftskolleg zu Berlin Fellowships 2027', kicker='Germany \u00b7 Fellowship \u00b7 Fully Funded', mono='WK',
 prov_short='Wissenschaftskolleg zu Berlin', prov_cat='Institute for Advanced Study \u00b7 Germany',
 h1='Wissenschaftskolleg zu Berlin Fellowships 2027 in Germany (Fully Funded)',
 sub='The Wissenschaftskolleg zu Berlin Fellowships 2027 offer ten months of protected research time in Berlin for early-career researchers \u2014 no teaching, no administration, one shared meal a day and a Tuesday colloquium. This article covers the call that is still open: the College for Life Sciences early-career call for the life and natural sciences, which closes on 1 November 2026. The humanities and social sciences early-career call closed on 1 September 2026, so do not apply on the strength of the general "1 November" date without checking which call you belong to. The deadline is 1 November 2026, and it is six days away.',
 dpill='Deadline 1 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-01'),
 facts=facts([('Award', 'A 10-month residential fellowship at the Wissenschaftskolleg zu Berlin (Wiko) in the Grunewald, for the 2027/28 academic year. There is no single fixed figure, because Wiko calculates funding against your income situation: a fellow who arrives with a full salary and whose home institution expects no replacement costs receives an additional \u20ac850 a month towards meals and local expenses; a fellow with no institutional affiliation or fixed income can receive up to \u20ac5,100 a month plus a contribution to social security. The Wissenschaftskolleg provides apartments for its fellows (one room to five), offices, and help settling in to Berlin life. If your home institution continues to pay at least 20% of your salary, Wiko covers the net rent; otherwise you pay 10% of your stipend as net rent.'),
              ('Eligible', 'Early-career researchers in the life and natural sciences (this call). You must hold a PhD, MD or similar doctorate by the time the fellowship begins, have at least one peer-reviewed journal publication as main author, and be just starting out in your research career. Typically at least two years of postdoctoral experience is expected of successful candidates, but that is a sign of competitiveness rather than a mandatory requirement. You must work outside a Berlin-based organisation. Researchers who have been principal investigators for more than five years should apply for a standard Wissenschaftskolleg fellowship instead. There are no restrictions on age, nationality or specific subject within the life and natural sciences.'),
              ('How', 'Apply through the Wissenschaftskolleg\u2019s official application platform: a project proposal (maximum 1,000 words), a letter of motivation (maximum 500 words), a CV, and a list of up to five significant publications. Selection interviews are scheduled for 18 and 19 February 2027.'),
              ('Deadline', '1 November 2026, 23:59 CET \u2014 the College for Life Sciences (life and natural sciences) early-career call. The humanities and social sciences early-career call closed on 1 September 2026. Regular fellowships can be submitted at any time but carry a lead time of about two years.'),
              ('Fine print', 'The exact fellowship start month differs between trackers (September 2027 vs October 2027); this article gives the 10-month duration in the 2027/28 academic year only. Fellows must live at the Wissenschaftskolleg for the ten months, come to one communal meal a day, and attend the Tuesday colloquium, where a Fellow presents their work. There is no teaching, no administration and no required output. Applications may be submitted in English, German or French for the humanities and social sciences call; the life and natural sciences call uses the application platform linked below.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Wissenschaftskolleg zu Berlin</strong> (Wiko), modelled on Princeton\u2019s Institute for Advanced Study, is one of Europe\u2019s most prestigious residential research institutes. Each academic year it hosts a cohort of around <strong>forty Fellows</strong> from all over the world \u2014 in the sciences, humanities and social sciences, and the arts \u2014 in its villa campus in the Grunewald, Berlin. The deal is simple and unusually generous: ten months to focus entirely on your own research, with an office, an apartment, one shared meal a day and a weekly colloquium, and no teaching or administration.</p>
      <p>The fellowship comes in several routes, and the route decides the deadline. The <strong>College for Life Sciences</strong> early-career call \u2014 for postdoctoral researchers, junior group leaders and assistant professors in biology, medicine and the natural sciences \u2014 closes on <strong>1 November 2026</strong> and is the call this article covers. The <strong>humanities and social sciences</strong> early-career call closed on <strong>1 September 2026</strong>. The funding is also unusual: there is no single figure, because Wiko calculates it against your income situation \u2014 up to <strong>\u20ac5,100 a month</strong> for a fellow with no institutional income, or an <strong>\u20ac850 a month</strong> top-up where your salary continues.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>early-career researcher in the life and natural sciences</strong> (this call): postdoctoral researchers, physicians, junior group leaders, instructors, assistant or associate professors, and early-career principal investigators.</li>
        <li>Hold a <strong>PhD, MD or similar doctorate</strong> by the time the fellowship begins.</li>
        <li>Have at least <strong>one peer-reviewed journal publication as main author</strong>.</li>
        <li>Be <strong>just starting out</strong> in your research career \u2014 typically at least two years of postdoctoral experience is expected of successful candidates, but that is a sign of competitiveness rather than a mandatory requirement.</li>
        <li>Work <strong>outside a Berlin-based organisation</strong>.</li>
        <li>Researchers who have been <strong>principal investigators for more than five years</strong> should apply for a standard Wissenschaftskolleg fellowship instead.</li>
        <li>There are <strong>no restrictions on age, nationality or specific subject</strong> within the life and natural sciences.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Ten months</strong> of protected research time in Berlin, in the 2027/28 academic year.</li>
        <li>Funding calculated against your income: up to <strong>\u20ac5,100 a month</strong> plus a social-security contribution for fellows without institutional income, or an additional <strong>\u20ac850 a month</strong> where your salary continues.</li>
        <li><strong>Accommodation</strong> in Wissenschaftskolleg apartments (one room to five), plus an <strong>office</strong>.</li>
        <li>One <strong>shared meal a day</strong> and the weekly <strong>Tuesday colloquium</strong> with around forty Fellows from all disciplines.</li>
        <li>Help settling in to <strong>Berlin life</strong> for you and your family.</li>
        <li><strong>No teaching, no administration and no required output</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>project proposal</strong> (maximum <strong>1,000 words</strong>).</li>
        <li>A <strong>letter of motivation</strong> (maximum <strong>500 words</strong>).</li>
        <li>An updated <strong>CV</strong>.</li>
        <li>A <strong>list of up to five significant publications</strong>.</li>
        <li>Any <strong>additional supporting documents</strong> requested by the institute.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm you belong to the <strong>life and natural sciences</strong> early-career call \u2014 the humanities and social sciences call closed on 1 September 2026.</li>
        <li>Prepare your <strong>1,000-word project proposal</strong> and <strong>500-word motivation letter</strong>, your <strong>CV</strong> and your <strong>list of up to five significant publications</strong>.</li>
        <li>Submit your application through the <strong>Wissenschaftskolleg\u2019s official application platform</strong>.</li>
        <li>Submit by <strong>1 November 2026, 23:59 CET</strong>.</li>
        <li>Selection interviews are scheduled for <strong>18 and 19 February 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Wissenschaftskolleg zu Berlin Fellowships 2027?',
  '1 November 2026, 23:59 CET, for the College for Life Sciences (life and natural sciences) early-career call. The humanities and social sciences early-career call closed on 1 September 2026.'),
 ('How much does the Wissenschaftskolleg pay its Fellows?',
  'There is no single figure, because Wiko calculates funding against your income situation. A Fellow with no institutional affiliation or fixed income can receive up to \u20ac5,100 a month plus a contribution to social security; a Fellow whose full salary continues receives an additional \u20ac850 a month towards meals and local expenses.'),
 ('How long is the fellowship?',
  'Ten months, in the 2027/28 academic year. The exact start month differs between trackers (September 2027 vs October 2027), so this article does not state one.'),
 ('Who can apply for the College for Life Sciences call?',
  'Early-career researchers in the life and natural sciences \u2014 postdoctoral researchers, physicians, junior group leaders, instructors, assistant or associate professors, and early-career principal investigators \u2014 with a PhD or MD and at least one peer-reviewed publication as main author, working outside a Berlin-based organisation.'),
 ('Does the fellowship provide accommodation?',
  'Yes. The Wissenschaftskolleg has apartments for its Fellows ranging from one room to five, along with offices. If your home institution continues to pay at least 20% of your salary, Wiko covers the net rent; otherwise you pay 10% of your stipend as net rent.'),
 ('What are the obligations of a Wiko Fellow?',
  'Three: live at the Wissenschaftskolleg for the ten months, come to one communal meal a day, and attend the Tuesday colloquium. There is no teaching, no administration and no required output.')]) + '''
      <p class="verify">Verified 26 Oct 2026: wiko-berlin.de (official application page) \u2014 next deadline 1 November 2026 (23:59 CET), project proposal max 1,000 words, motivation letter max 500 words, CV, selection interviews 18\u201319 February 2027; networks.h-net.org (H-Net) \u2014 humanities and social sciences early-career call closed 1 September 2026, doctorate no more than five years before the fellowship begins; europescholarships.com, scholarshipsads.com \u2014 funding up to \u20ac5,100 a month for fellows without institutional income, \u20ac850 a month top-up where salary continues, accommodation, 10 months, no teaching or administration. CORRECTION: Bright Scholarship\u2019s 1 November 2026 deadline is the life and natural sciences (College for Life Sciences) call only \u2014 the humanities and social sciences early-career call closed 1 September 2026 and is not covered here. The exact fellowship start month differs between trackers (September 2027 vs October 2027); this article gives the 10-month duration in the 2027/28 academic year only.</p>''',
 dl_long='1 November 2026, 23:59 CET (life and natural sciences call)',
 offlinks=[('Wissenschaftskolleg zu Berlin \u2014 Application (official)', 'https://www.wiko-berlin.de/en/becoming-a-fellow/wiko-early-career-calls/early-career-call-life-and-natural-sciences/application'),
           ('Bright Scholarship \u2014 Wissenschaftskolleg zu Berlin Fellowships 2027', 'https://brightscholarship.com/wissenschaftskolleg-zu-berlin-fellowships/')],
 related_titles=['tietze-2027', 'dalarna-2027', 'leiden-lexs-2027', 'unil'])),

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
    json.dump(sizes, open('/tmp/batch51_built.json','w'))

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

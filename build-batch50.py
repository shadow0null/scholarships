#!/usr/bin/env python3
"""Batch 50 (cron run 50, 25 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Study in Belarus Without IELTS 2027 — SKIPPED: aggregator listicle
   bundling many separate schemes, not one scholarship.
2. IIAS Asia in the World Fellowship 2027 — SKIPPED: deadline passed
   (10 Sep 2026); "(Fully Funded)" applies only to Category A.
3. Endeavour Women in Tech Scholarships 2026 — SKIPPED: deadline passed
   (8 Sep 2026); official site confirms applications closed.
4. University of Manitoba Fellowship 2026 — VERIFIED: University of
   Manitoba Graduate Fellowship (UMGF). CAD 20,000/year Master's (up to
   24 months, max CAD 40,000), CAD 25,000/year PhD (up to 48 months, max
   CAD 100,000). CORRECTION: Bright's CAD 14,000/18,000 figures are
   outdated. Deadline varies by department — no single university-wide
   deadline; aggregator claims of 1 Dec 2026 / 1 Oct 2026 not confirmed.
   Funded stipend, not fully funded.
5. Al Qasimi Foundation Internship 2027 — VERIFIED: winter deadline
   31 Oct 2026 (6 days away), summer 30 Apr 2027. Partially funded:
   furnished shared accommodation, modest living stipend (amount not
   published), local transport, mentorship, certificate. Airfare and
   personal expenses NOT covered. Not fully funded.
6. Dalarna University Masters Scholarships 2027 — VERIFIED: scholarship
   deadline 15 Feb 2027; programme application via UniversityAdmissions.se
   by 15 Jan 2027. CORRECTION: "(Funded)" is misleading — partial
   tuition waiver only (Choose Dalarna First SEK 5,000; Academic
   Excellence SEK 5,000-15,000/semester, total SEK 20,000-90,000).
   No living costs, housing or travel.
7. University of Vienna Andreas Tietze Memorial Fellowship 2027 —
   VERIFIED: deadline 30 Nov 2026. EUR 1,500/month for 1-3 months.
   CORRECTION: "(Fully Funded)" is wrong — stipend only, travel to/from
   Vienna NOT reimbursed, accommodation from the stipend. Official page
   was down for maintenance at check time; date corroborated by 5 sources.
8. University of Bern Scholarship 2027 — SKIPPED: aggregator composite;
   no single University of Bern Scholarship 2027 exists (bundles Swiss
   Government Excellence, Heyning-Roelli, SEMP, SNSF).
9. Bocconi University Scholarships 2027 — SKIPPED: aggregator composite
   bundling several distinct schemes (Merit Award, International Award,
   ISU need-based grant), not one scheme.
10. SJPL Rhodes Scholarships 2027 — SKIPPED: deadline passed
    (27 Aug 2026, 23:59 GMT, official Rhodes House); correct acronym SJLP.
11. US Department of State Paid Student Internships 2027 — SKIPPED:
    deadline passed (window 7 Aug - 1 Sep 2026; Spring and Summer 2027
    intakes both closed).
12. American University Global Leader Scholarship 2027 — VERIFIED: AU
    Emerging Global Leader Scholarship (AU EGLS). Deadline 15 Jan 2027.
    CORRECTIONS: official name is "Emerging Global Leader" (queue drops
    "Emerging"); queue deadline "November 2026" is wrong. Two full
    scholarships covering all billable expenses for up to 4 years;
    additional partial scholarships up to $40,000/year. "Fully funded"
    applies only to the 2 full awards.

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
 'manitoba-2026': {'mono': 'UM', 'title': 'University of Manitoba Fellowship 2026 in Canada (Funded)',
   'href': 'university-of-manitoba-graduate-fellowship-2026-canada.html',
   'dpill': 'Deadline varies by department \u00b7 Apply early',
   'award': 'The University of Manitoba Graduate Fellowship: CAD 20,000 a year for Master\u2019s students (up to 24 months) and CAD 25,000 a year for PhD students (up to 48 months) \u2014 a funded stipend, not full funding.',
   'elig': 'Full-time Master\u2019s or PhD students of all nationalities in a Tri-Agency-eligible programme, with a minimum admission GPA of 3.0, nominated by their department.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Canada', 'teal')]},
 'alqasimi-2027': {'mono': 'AQ', 'title': 'Al Qasimi Foundation Internship 2027 in UAE (Funded)',
   'href': 'al-qasimi-foundation-internship-2027-uae.html',
   'dpill': 'Deadline 31 Oct 2026 \u00b7 %d days left' % dl_left('2026-10-31'),
   'award': 'A partially funded internship of up to 3 months in Ras Al Khaimah: furnished shared accommodation, a modest living stipend, local transport, mentorship and a certificate. Airfare is not covered.',
   'elig': 'Current undergraduate or graduate students in good academic standing, or recent graduates within 2 years, of all nationalities, in education, public policy, public health, urban planning or economic development.',
   'tags': [('Internship', 'blue'), ('UAE', 'teal')]},
 'dalarna-2027': {'mono': 'DU', 'title': 'Dalarna University Masters Scholarships 2027 in Sweden (Funded)',
   'href': 'dalarna-university-masters-scholarships-2027-sweden.html',
   'dpill': 'Deadline 15 Feb 2027 \u00b7 %d days left' % dl_left('2027-02-15'),
   'award': 'A partial tuition-fee waiver only: SEK 5,000 off the first semester (Choose Dalarna First) or SEK 5,000\u201315,000 per semester (Academic Excellence), up to SEK 90,000 in total. No living costs, housing or travel.',
   'elig': 'Master\u2019s applicants from outside the EU/EEA/Switzerland who pay tuition fees, with a Bachelor\u2019s degree equivalent to a Swedish Bachelor\u2019s and English proficiency.',
   'tags': [('Master\u2019s', 'blue'), ('Sweden', 'teal')]},
 'tietze-2027': {'mono': 'VT', 'title': 'University of Vienna Andreas Tietze Memorial Fellowship 2027 in Austria (Fully Funded)',
   'href': 'university-of-vienna-andreas-tietze-memorial-fellowship-2027-austria.html',
   'dpill': 'Deadline 30 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-30'),
   'award': '\u20ac1,500 a month for 1\u20133 months for advanced doctoral candidates and early-stage postdoctoral researchers in Turkish Studies, with a workplace and full library use in Vienna. Travel is not reimbursed.',
   'elig': 'Advanced doctoral candidates (ABD stage) and postdoctoral researchers with a PhD no more than 5 years old, of all nationalities, working on a Turkish Studies topic, with a high level of English.',
   'tags': [('Fellowship', 'purple'), ('Austria', 'teal')]},
 'au-egls-2027': {'mono': 'AU', 'title': 'American University Emerging Global Leader Scholarship 2027 in USA (Fully Funded)',
   'href': 'american-university-emerging-global-leader-scholarship-2027-usa.html',
   'dpill': 'Deadline 15 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-15'),
   'award': 'Two full scholarships covering all billable expenses (full tuition, room and board) for up to four years, plus additional partial scholarships of up to $40,000 a year. Only the two full awards are fully funded.',
   'elig': 'International students only, still in secondary or high school and graduating by June 2027, with no prior university enrolment and a minimum GPA of 3.8/4.0 or top 10% of the class.',
   'tags': [('Bachelor\u2019s', 'blue'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Manitoba
A.append(dict(
 slug='university-of-manitoba-graduate-fellowship-2026-canada',
 title='University of Manitoba Fellowship 2026 in Canada (Funded)',
 meta='University of Manitoba Fellowship 2026: the University of Manitoba Graduate Fellowship pays CAD 20,000 a year for Master\u2019s students and CAD 25,000 a year for PhD students. The deadline varies by department \u2014 eligibility, nomination, how to apply and FAQs.',
 short='University of Manitoba Fellowship 2026', kicker='Canada \u00b7 Master\u2019s & PhD \u00b7 Funded', mono='UM',
 prov_short='University of Manitoba', prov_cat='University \u00b7 Canada',
 h1='University of Manitoba Fellowship 2026 in Canada (Funded)',
 sub='The University of Manitoba Fellowship 2026 is the University of Manitoba Graduate Fellowship (UMGF), a funded stipend for full-time Master\u2019s and PhD students: CAD 20,000 a year for Master\u2019s students and CAD 25,000 a year for PhD students. Two things to read carefully before you plan around it. First, some listings still give the old figures of CAD 14,000 and CAD 18,000 a year \u2014 those are outdated and this article uses the current CAD 20,000 and CAD 25,000 figures. Second, there is no single university-wide deadline: the deadline varies by department, and your department nominates you \u2014 you cannot apply for the fellowship directly.',
 dpill='Deadline varies by department \u00b7 Apply early',
 facts=facts([('Award', 'The University of Manitoba Graduate Fellowship (UMGF): CAD 20,000 a year for Master\u2019s students, for up to 24 months (a maximum of CAD 40,000), and CAD 25,000 a year for PhD students, for up to 48 months (a maximum of CAD 100,000). This is a funded stipend, not full funding \u2014 no tuition, accommodation or travel cover is confirmed for the fellowship. Some listings still give the older figures of CAD 14,000 (Master\u2019s) and CAD 18,000 (PhD) a year; those are outdated and are not used here.'),
              ('Eligible', 'Students of all nationalities, Canadian and international, in full-time Master\u2019s or PhD study at the University of Manitoba in a Tri-Agency-eligible programme. Applicants need a minimum admission GPA of 3.0, though departments may require a higher GPA. Pre-Master\u2019s and occasional students are not eligible. Students must be recommended or nominated by their department \u2014 there is no direct application to the Faculty of Graduate Studies. Total UMGF support is capped at four years, and a student cannot hold the UMGF at the same time as another award of equal or greater value.'),
              ('How', 'Apply for admission to a graduate programme at the University of Manitoba and tell your department you want to be considered for the UMGF. The department nominates its candidates to the Faculty of Graduate and Postdoctoral Studies; students do not submit a fellowship application themselves. Check your own department\u2019s page for its UMGF deadline and nomination process.'),
              ('Deadline', 'There is no single university-wide deadline \u2014 the deadline varies by department. Some department deadlines have already passed (for example the Electrical and Computer Engineering UMGF deadline of 15 April 2026 and the UMIH Graduate Fellowship deadline of 30 April 2026), so check your own department rather than relying on a general date. Aggregator claims of a 1 December 2026 or 1 October 2026 deadline were not confirmed from any official source and are not used here.'),
              ('Fine print', 'The UMGF is a stipend, not a full scholarship: it does not cover tuition, accommodation or travel, and the amounts above are the confirmed current values. Support is capped at four years in total, and holding another award of equal or greater value at the same time is not allowed. Departments may set a higher GPA bar than the 3.0 minimum, and the exact documents depend on the department.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>University of Manitoba</strong>, in Winnipeg, funds its graduate students through the <strong>University of Manitoba Graduate Fellowship (UMGF)</strong> \u2014 the main internal fellowship for full-time Master\u2019s and PhD students. It is a straightforward stipend: <strong>CAD 20,000 a year</strong> for Master\u2019s students, for up to two years, and <strong>CAD 25,000 a year</strong> for PhD students, for up to four years. It is open to students of all nationalities, and it is awarded on academic merit through the departments.</p>
      <p>The structure is what makes this fellowship different from most on this site. There is no fellowship application form and no single deadline. You apply for admission to a graduate programme, you tell your department you want to be considered, and the <strong>department nominates</strong> its candidates to the Faculty of Graduate and Postdoctoral Studies. That means the real deadline is your department\u2019s deadline, and the real competition is inside your department \u2014 so the first step is to find your department\u2019s UMGF page, not a general scholarship deadline.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>full-time Master\u2019s or PhD student</strong> at the University of Manitoba, in a <strong>Tri-Agency-eligible programme</strong>.</li>
        <li>Be of <strong>any nationality</strong> \u2014 Canadian and international students are both eligible.</li>
        <li>Hold a minimum <strong>admission GPA of 3.0</strong> \u2014 departments may require a higher GPA.</li>
        <li>Be <strong>recommended or nominated by your department</strong> \u2014 students cannot apply directly to the Faculty of Graduate Studies.</li>
        <li><strong>Pre-Master\u2019s and occasional students are not eligible.</strong></li>
        <li>Note the <strong>four-year cap</strong> on total UMGF support, and that you cannot hold the UMGF at the same time as <strong>another award of equal or greater value</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CAD 20,000 a year</strong> for Master\u2019s students, for up to <strong>24 months</strong> (maximum CAD 40,000).</li>
        <li><strong>CAD 25,000 a year</strong> for PhD students, for up to <strong>48 months</strong> (maximum CAD 100,000).</li>
        <li>Open to <strong>all nationalities</strong>, with no separate fellowship application to file.</li>
        <li>Note that the fellowship is a <strong>stipend, not full funding</strong> \u2014 tuition, accommodation and travel are not covered by the UMGF.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>graduate admission application</strong> to the University of Manitoba \u2014 the fellowship is considered through the department, not a separate form.</li>
        <li>Documents depend on the department; typically <strong>transcripts, a CV, a statement of purpose or research proposal, recommendation letters</strong> and <strong>proof of English proficiency</strong> as the admission application requires.</li>
        <li>Confirm the exact list with <strong>your own department</strong> \u2014 it varies, and the official department pages are the authority, not aggregator lists.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for <strong>admission to a graduate programme</strong> at the University of Manitoba.</li>
        <li>Tell your <strong>department</strong> you want to be considered for the UMGF and confirm its own deadline and nomination process.</li>
        <li>Prepare the <strong>admission documents</strong> your department asks for.</li>
        <li>The <strong>department nominates</strong> its candidates to the Faculty of Graduate and Postdoctoral Studies \u2014 there is no fellowship form for you to submit.</li>
        <li>Do not wait for a single university deadline \u2014 there is not one. Your department\u2019s date is the deadline that matters.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How much is the University of Manitoba Graduate Fellowship worth?',
  'CAD 20,000 a year for Master\u2019s students, for up to 24 months (a maximum of CAD 40,000), and CAD 25,000 a year for PhD students, for up to 48 months (a maximum of CAD 100,000). Some listings still give the older figures of CAD 14,000 and CAD 18,000 a year; those are outdated.'),
 ('Is the UMGF fully funded?',
  'No. It is a funded stipend. It does not cover tuition, accommodation or travel, so budget for those costs separately.'),
 ('What is the deadline for the University of Manitoba Fellowship 2026?',
  'There is no single university-wide deadline \u2014 the deadline varies by department. Some department deadlines have already passed (for example Electrical and Computer Engineering, 15 April 2026), so check your own department\u2019s page. Aggregator dates of 1 December 2026 and 1 October 2026 were not confirmed from any official source.'),
 ('Can I apply for the UMGF directly?',
  'No. Students cannot apply directly to the Faculty of Graduate Studies. You apply for admission to a graduate programme and your department nominates its candidates.'),
 ('Who is eligible for the UMGF?',
  'Full-time Master\u2019s or PhD students of all nationalities in a Tri-Agency-eligible programme, with a minimum admission GPA of 3.0 (departments may require more). Pre-Master\u2019s and occasional students are not eligible, and total UMGF support is capped at four years.'),
 ('Can I hold the UMGF with another scholarship?',
  'Not if the other award is of equal or greater value \u2014 a student cannot hold the UMGF at the same time as another award of equal or greater value.')]) + '''
      <p class="verify">Verified 25 Oct 2026: umanitoba.ca (official, Faculty of Graduate and Postdoctoral Studies UMGF pages, including the Electrical and Computer Engineering UMGF page) \u2014 department nomination, no direct application, GPA 3.0 minimum, four-year cap, no concurrent award of equal or greater value; ilmkidunya.com, educatewithguide.com, careerical.com, wemakescholars.com, jobs.iammagnus.com \u2014 CAD 20,000 a year (Master\u2019s, up to 24 months) and CAD 25,000 a year (PhD, up to 48 months), deadline varies by department, department deadlines 15 April 2026 (ECE) and 30 April 2026 (UMIH) passed. Bright Scholarship\u2019s CAD 14,000/18,000 figures are outdated and are not used. Aggregator deadline claims of 1 December 2026 and 1 October 2026 were not confirmed from any official source and are not used.</p>''',
 dl_long='Varies by department \u2014 no single university-wide deadline',
 offlinks=[('University of Manitoba \u2014 Graduate Fellowship (official)', 'https://umanitoba.ca/engineering/electrical-and-computer-engineering/umgf'),
           ('Bright Scholarship \u2014 University of Manitoba Fellowship 2026', 'https://brightscholarship.com/university-of-manitoba-fellowship-2026/')],
 related_titles=['ubc-killam-2027', 'ucalgary-2027', 'trent-2027', 'trudeau-2027'])),

# ---------------------------------------------------------------- 2. Al Qasimi
A.append(dict(
 slug='al-qasimi-foundation-internship-2027-uae',
 title='Al Qasimi Foundation Internship 2027 in UAE (Funded)',
 meta='Al Qasimi Foundation Internship 2027: a partially funded internship of up to 3 months in Ras Al Khaimah \u2014 furnished shared accommodation, a modest living stipend, local transport, mentorship and a certificate. Winter deadline 31 October 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Al Qasimi Foundation Internship 2027', kicker='UAE \u00b7 Internship \u00b7 Funded', mono='AQ',
 prov_short='Al Qasimi Foundation', prov_cat='Foundation \u00b7 United Arab Emirates',
 h1='Al Qasimi Foundation Internship 2027 in UAE (Funded)',
 sub='The Al Qasimi Foundation Internship 2027 is a partially funded internship of up to three months in Ras Al Khaimah, in the United Arab Emirates, for current students and recent graduates. It covers furnished shared accommodation, a modest living stipend, local transport, mentorship and a certificate \u2014 but not airfare or personal expenses, so do not read \u201cfunded\u201d as \u201cfree\u201d. The winter intake closes on 31 October 2026, only six days from now, so if you want the winter place, apply immediately; the summer intake closes on 30 April 2027.',
 dpill='Deadline 31 Oct 2026 \u00b7 %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'A partially funded internship of up to three months in Ras Al Khaimah. The foundation provides furnished shared accommodation, a modest living stipend (the exact amount is not published in the official notification), local transport, mentorship and a certificate of completion. Airfare and personal expenses are NOT covered \u2014 this is not a fully funded internship, and the stipend amount is not published, so do not budget around a figure you have seen on an aggregator.'),
              ('Eligible', 'Current undergraduate or graduate students in good academic standing at an accredited university, and recent graduates within two years of graduating. All nationalities may apply. Relevant fields include education, public policy, public health, urban planning and economic development, with other areas such as public relations, multimedia and translation also listed. If English is not your first language, the foundation asks for TOEFL iBT 85 or IELTS 6.5.'),
              ('How', 'Submit the online application form through the official internship page on the Al Qasimi Foundation website. Questions go to the foundation\u2019s internships email, internships@alqasimifoundation.rak.ae. There is no application fee mentioned on the official page.'),
              ('Deadline', '31 October 2026 for the winter intake and 30 April 2027 for the summer intake. No time of day or timezone is published for either date, so treat the winter deadline as the end of 31 October 2026 and apply well before it.'),
              ('Fine print', 'The stipend is described as modest and its amount is not published, so the internship suits applicants who can cover their airfare and personal expenses. Accommodation is furnished and shared, not a private flat, and local transport is provided. The internship lasts up to three months in Ras Al Khaimah, not in Dubai or Abu Dhabi.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>Al Qasimi Foundation</strong>, based in Ras Al Khaimah in the United Arab Emirates, runs an internship programme for students and recent graduates who want to work on the foundation\u2019s research and community projects. Interns spend <strong>up to three months</strong> in Ras Al Khaimah, working in areas such as education, public policy, public health, urban planning and economic development \u2014 the fields the foundation itself works in \u2014 with mentorship from its staff and a certificate at the end.</p>
      <p>The funding is real but partial. The foundation provides <strong>furnished shared accommodation</strong>, a <strong>modest living stipend</strong>, <strong>local transport</strong> and mentorship. It does not pay your <strong>airfare</strong> or your personal expenses, and the stipend amount is not published, so plan your budget on the assumption that you will need your own money for the flight and for day-to-day costs beyond the basics. The winter intake is the urgent one: it closes on <strong>31 October 2026</strong>, six days from now.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>current undergraduate or graduate student</strong> in good academic standing at an accredited university, or a <strong>recent graduate within two years</strong> of graduating.</li>
        <li>Be of <strong>any nationality</strong>.</li>
        <li>Work in a <strong>relevant field</strong>: education, public policy, public health, urban planning or economic development (other areas such as public relations, multimedia and translation are also listed).</li>
        <li>If English is not your first language, meet the <strong>TOEFL iBT 85 or IELTS 6.5</strong> requirement.</li>
        <li>Be available for an internship of <strong>up to three months</strong> in Ras Al Khaimah.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Furnished shared accommodation</strong> in Ras Al Khaimah.</li>
        <li>A <strong>modest living stipend</strong> (the amount is not published in the official notification).</li>
        <li><strong>Local transport</strong> during the internship.</li>
        <li><strong>Mentorship</strong> from foundation staff and a <strong>certificate</strong> on completion.</li>
        <li>Work experience in <strong>education, public policy, public health, urban planning or economic development</strong> in the UAE.</li>
        <li>Note that <strong>airfare and personal expenses are not covered</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application form</strong> on the official internship page.</li>
        <li>A <strong>cover letter</strong>.</li>
        <li>A current <strong>CV</strong>.</li>
        <li>A <strong>1-minute video introduction</strong>.</li>
        <li>Note: aggregators also list transcripts, a TOEFL/IELTS report, two or three references and an academic writing sample. Those are <strong>not confirmed on the official page</strong> \u2014 use the four items above as the official list and check the application form itself for anything else.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the <strong>official internship page</strong> on the Al Qasimi Foundation website (alqasimifoundation.com/internship-opportunities).</li>
        <li>Prepare your <strong>cover letter, CV and 1-minute video introduction</strong>.</li>
        <li>Submit the <strong>online application form</strong> through the page.</li>
        <li>For questions, email the foundation at <strong>internships@alqasimifoundation.rak.ae</strong>.</li>
        <li>Apply by <strong>31 October 2026</strong> for the winter intake \u2014 or by <strong>30 April 2027</strong> for the summer intake.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Al Qasimi Foundation Internship fully funded?',
  'No. It is partially funded: furnished shared accommodation, a modest living stipend, local transport, mentorship and a certificate are provided, but airfare and personal expenses are not covered. The stipend amount is not published.'),
 ('What is the deadline for the Al Qasimi Foundation Internship 2027?',
  '31 October 2026 for the winter intake and 30 April 2027 for the summer intake. No time of day or timezone is published, so apply well before the date.'),
 ('Who can apply?',
  'Current undergraduate or graduate students in good academic standing at an accredited university, and recent graduates within two years of graduating, of all nationalities, in fields such as education, public policy, public health, urban planning and economic development.'),
 ('How much is the stipend?',
  'The foundation describes it as a modest living stipend, but the exact amount is not published in the official notification. Do not rely on a figure quoted by an aggregator.'),
 ('Do I need IELTS or TOEFL?',
  'If English is not your first language, the foundation asks for TOEFL iBT 85 or IELTS 6.5.'),
 ('How long is the internship and where is it?',
  'Up to three months, in Ras Al Khaimah in the United Arab Emirates \u2014 not in Dubai or Abu Dhabi.')]) + '''
      <p class="verify">Verified 25 Oct 2026: alqasimifoundation.com/internship-opportunities (official internship page, opened and read) \u2014 winter deadline 31 October 2026, summer deadline 30 April 2027, furnished shared accommodation, modest living stipend, local transport, mentorship, certificate, airfare not covered, eligibility (current students and recent graduates within 2 years, all nationalities), TOEFL iBT 85 / IELTS 6.5, documents (online form, cover letter, CV, 1-minute video introduction), internships@alqasimifoundation.rak.ae; o4af.com, zombomenu.com \u2014 corroboration. The stipend amount is not published in the official notification. Aggregator-listed extras (transcripts, test report, 2\u20133 references, writing sample) were not confirmed on the official page.</p>''',
 dl_long='31 October 2026 (winter intake) \u00b7 30 April 2027 (summer intake)',
 offlinks=[('Al Qasimi Foundation \u2014 Internship Opportunities (official)', 'https://www.alqasimifoundation.com/internship-opportunities'),
           ('Bright Scholarship \u2014 Al Qasimi Foundation Internship 2027', 'https://brightscholarship.com/al-qasimi-foundation-internship-2027-in-uae/')],
 related_titles=['kaust-vsrp', 'wto-internship-2027', 'mbzuai', 'oecd'])),

# ---------------------------------------------------------------- 3. Dalarna
A.append(dict(
 slug='dalarna-university-masters-scholarships-2027-sweden',
 title='Dalarna University Masters Scholarships 2027 in Sweden (Funded)',
 meta='Dalarna University Masters Scholarships 2027: a partial tuition-fee waiver for Master\u2019s students in Sweden \u2014 SEK 5,000 off the first semester, or SEK 5,000\u201315,000 a semester for top students. Scholarship deadline 15 February 2027 \u2014 eligibility, how to apply and FAQs.',
 short='Dalarna University Masters Scholarships 2027', kicker='Sweden \u00b7 Master\u2019s \u00b7 Partial tuition waiver', mono='DU',
 prov_short='Dalarna University', prov_cat='University \u00b7 Sweden',
 h1='Dalarna University Masters Scholarships 2027 in Sweden (Funded)',
 sub='The Dalarna University Masters Scholarships 2027 are partial tuition-fee waivers for international Master\u2019s students in Sweden \u2014 and that word \u201cpartial\u201d is the most important thing on this page. Despite the \u201cfunded\u201d label on the listing, these scholarships do not pay your living costs, housing or travel: the largest award is SEK 5,000 off your first semester, or SEK 5,000 to SEK 15,000 a semester for top-performing students. The scholarship application closes on 15 February 2027, but you must first apply to a Dalarna Master\u2019s programme on UniversityAdmissions.se by 15 January 2027.',
 dpill='Deadline 15 Feb 2027 \u00b7 %d days left' % dl_left('2027-02-15'),
 facts=facts([('Award', 'A partial tuition-fee waiver only \u2014 not full funding and not a living-cost scholarship. Two Dalarna schemes: (a) Choose Dalarna First \u2014 a guaranteed SEK 5,000 off first-semester tuition if your Dalarna Master\u2019s is your first-choice programme and you are admitted; (b) Academic Excellence \u2014 SEK 5,000 to SEK 15,000 per semester plus a programme distinction, with a total possible value of SEK 20,000 to SEK 90,000 depending on the programme. No living costs, housing or travel are covered. The Swedish Institute SISGP scholarship (full tuition plus SEK 12,000 a month) is a separate scheme with its own February 2027 application \u2014 do not confuse it with these Dalarna awards.'),
              ('Eligible', 'Master\u2019s programmes only (60 or 120 credits, including online programmes). You must be a citizen of a country outside the EU/EEA/Switzerland who is required to pay tuition fees, and hold a Bachelor\u2019s degree equivalent to a Swedish Bachelor\u2019s. English proficiency is required; aggregators generally give IELTS 6.5 or TOEFL iBT 90, but those scores were not confirmed on the official page. The Academic Excellence award requires completing all 30 credits in a semester with top grades (15 credits at the top grade) and good standing.'),
              ('How', 'First apply to a Dalarna Master\u2019s programme on UniversityAdmissions.se, ranking it as your first choice, by 15 January 2027. Then submit the separate Dalarna scholarship application form from the university\u2019s scholarships page by 15 February 2027. The scholarship form opens in January 2027.'),
              ('Deadline', '15 February 2027 for the scholarship application (autumn intake; the spring intake scholarship deadline is 15 September). The programme application on UniversityAdmissions.se closes on 15 January 2027 at midnight CET, and documents and the application fee are due by 1 February 2027. Apply to the programme first \u2014 the scholarship application cannot stand alone.'),
              ('Fine print', 'These are tuition waivers, not cash: the money comes off your tuition fee, and you still pay the rest of the tuition plus all living costs, housing and travel. The scholarship application form opens in January 2027, so you cannot submit it before then. The English test scores quoted by aggregators (IELTS 6.5 / TOEFL iBT 90) were not confirmed on the official page \u2014 check the programme page for the requirement that applies to you.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Dalarna University</strong>, in central Sweden, offers two of its own scholarships for international Master\u2019s students who pay tuition fees. The first, <strong>Choose Dalarna First</strong>, is a guaranteed <strong>SEK 5,000</strong> off your first-semester tuition if you rank a Dalarna Master\u2019s as your first choice and are admitted. The second, <strong>Academic Excellence</strong>, rewards students who perform at the top of their class: <strong>SEK 5,000 to SEK 15,000 a semester</strong>, with a total possible value of <strong>SEK 20,000 to SEK 90,000</strong> depending on the programme, plus a programme distinction.</p>
      <p>Be clear about what these awards are not. They are <strong>partial tuition waivers</strong>, not full scholarships: they do not pay your living costs, your housing or your travel, and the largest single-semester amount is SEK 15,000 against tuition fees that run far higher. If you need full funding, the separate <strong>Swedish Institute SISGP</strong> scholarship \u2014 full tuition plus SEK 12,000 a month \u2014 is a different scheme with its own February 2027 application, and this article does not cover it. What Dalarna\u2019s own awards do well is cut the tuition bill for strong students, and the Choose Dalarna First award is guaranteed rather than competitive.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Apply to a <strong>Master\u2019s programme</strong> at Dalarna University (60 or 120 credits, including online programmes).</li>
        <li>Be a citizen of a country <strong>outside the EU/EEA/Switzerland</strong> who is required to pay tuition fees.</li>
        <li>Hold a <strong>Bachelor\u2019s degree equivalent to a Swedish Bachelor\u2019s</strong>.</li>
        <li>Meet the <strong>English proficiency</strong> requirement for your programme (aggregators generally give IELTS 6.5 or TOEFL iBT 90, but those scores were not confirmed on the official page).</li>
        <li>For the <strong>Choose Dalarna First</strong> award: rank your Dalarna Master\u2019s as your <strong>first choice</strong> and be admitted.</li>
        <li>For the <strong>Academic Excellence</strong> award: complete all <strong>30 credits in a semester with top grades</strong> (15 credits at the top grade) and remain in good standing.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Choose Dalarna First:</strong> a guaranteed <strong>SEK 5,000</strong> off first-semester tuition for admitted first-choice applicants.</li>
        <li><strong>Academic Excellence:</strong> <strong>SEK 5,000 to SEK 15,000 per semester</strong> plus a programme distinction, with a total possible value of <strong>SEK 20,000 to SEK 90,000</strong> depending on the programme.</li>
        <li>The Choose Dalarna First award is <strong>guaranteed</strong>, not competitive \u2014 rank Dalarna first and get admitted, and the SEK 5,000 follows.</li>
        <li>Note that these are <strong>partial tuition waivers only</strong> \u2014 no living costs, housing or travel are covered.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>programme application</strong> on UniversityAdmissions.se, with the degree, transcripts and language proof that portal requires.</li>
        <li>The <strong>separate Dalarna scholarship application form</strong>, from the university\u2019s scholarships page \u2014 it opens in January 2027.</li>
        <li>No fixed document list for the scholarship itself is published in the official notification, so use the programme application\u2019s requirements and the scholarship form when it opens.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose a <strong>Dalarna Master\u2019s programme</strong> and check its requirements on the university\u2019s website.</li>
        <li>Apply to the programme on <strong>UniversityAdmissions.se</strong>, ranking it as your <strong>first choice</strong>, by <strong>15 January 2027 at midnight CET</strong>.</li>
        <li>Submit your <strong>documents and application fee</strong> by <strong>1 February 2027</strong>.</li>
        <li>When the scholarship form opens in <strong>January 2027</strong>, submit the <strong>separate Dalarna scholarship application</strong> from the university\u2019s scholarships page.</li>
        <li>Submit the scholarship application by <strong>15 February 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Are the Dalarna University Masters Scholarships fully funded?',
  'No. They are partial tuition-fee waivers only: SEK 5,000 off the first semester (Choose Dalarna First) or SEK 5,000 to SEK 15,000 a semester (Academic Excellence). Living costs, housing and travel are not covered.'),
 ('How much are the Dalarna scholarships worth?',
  'Choose Dalarna First is a guaranteed SEK 5,000 off first-semester tuition. Academic Excellence pays SEK 5,000 to SEK 15,000 a semester, with a total possible value of SEK 20,000 to SEK 90,000 depending on the programme.'),
 ('What is the deadline for the Dalarna University Masters Scholarships 2027?',
  '15 February 2027 for the scholarship application (autumn intake). But the programme application on UniversityAdmissions.se closes earlier, on 15 January 2027 at midnight CET, with documents and the fee due by 1 February 2027.'),
 ('Do I need to apply separately for the scholarship?',
  'Yes. Apply to the Master\u2019s programme on UniversityAdmissions.se first, then submit the separate Dalarna scholarship application form (it opens in January 2027) by 15 February 2027.'),
 ('What is the Choose Dalarna First scholarship?',
  'A guaranteed SEK 5,000 off your first-semester tuition if you rank a Dalarna Master\u2019s as your first choice on UniversityAdmissions.se and are admitted. It is not competitive \u2014 it follows admission.'),
 ('Is the Swedish Institute SISGP the same as the Dalarna scholarship?',
  'No. SISGP is a separate scheme (full tuition plus SEK 12,000 a month) with its own February 2027 application. Do not confuse it with Dalarna\u2019s own partial tuition waivers.')]) + '''
      <p class="verify">Verified 25 Oct 2026: du.se/en/study-at-du/tuition-fees-and-scholarships/scholarships/ (official Dalarna University scholarships page, opened and read, last reviewed 16 Sep 2026) \u2014 Choose Dalarna First SEK 5,000, Academic Excellence SEK 5,000\u201315,000 per semester and SEK 20,000\u201390,000 total, scholarship deadline 15 February 2027, programme application 15 January 2027 midnight CET, documents and fee 1 February 2027, spring intake scholarship deadline 15 September; studyabroadwitharbaz.com, scholarships.af, oyaop.com \u2014 corroboration, English scores IELTS 6.5 / TOEFL iBT 90 (aggregator-reported, not confirmed on the official page). No fixed document list for the scholarship itself is published in the official notification.</p>''',
 dl_long='15 February 2027 (scholarship application; programme application by 15 January 2027)',
 offlinks=[('Dalarna University \u2014 Scholarships (official)', 'https://www.du.se/en/study-at-du/tuition-fees-and-scholarships/scholarships/'),
           ('Bright Scholarship \u2014 Dalarna University Masters Scholarships 2027', 'https://brightscholarship.com/dalarna-university-masters-scholarships-2027/')],
 related_titles=['stockholm-2027', 'hasselt-mm-2027', 'leiden-lexs-2027', 'unil'])),

# ---------------------------------------------------------------- 4. Vienna Tietze
A.append(dict(
 slug='university-of-vienna-andreas-tietze-memorial-fellowship-2027-austria',
 title='University of Vienna Andreas Tietze Memorial Fellowship 2027 in Austria (Fully Funded)',
 meta='University of Vienna Andreas Tietze Memorial Fellowship 2027: \u20ac1,500 a month for 1\u20133 months for advanced doctoral candidates and early-stage postdoctoral researchers in Turkish Studies. Deadline 30 November 2026 \u2014 eligibility, documents, how to apply and FAQs.',
 short='Andreas Tietze Memorial Fellowship 2027', kicker='Austria \u00b7 Fellowship \u00b7 Stipend', mono='VT',
 prov_short='University of Vienna', prov_cat='University \u00b7 Austria',
 h1='University of Vienna Andreas Tietze Memorial Fellowship 2027 in Austria (Fully Funded)',
 sub='The University of Vienna Andreas Tietze Memorial Fellowship 2027 pays \u20ac1,500 a month for one to three months to advanced doctoral candidates and early-stage postdoctoral researchers working on Turkish Studies, with a workplace and full library use in Vienna. Read the title with care: despite the \u201cfully funded\u201d label on the listing, this is a stipend, not full funding \u2014 travel to and from Vienna is not reimbursed, and your accommodation comes out of the \u20ac1,500 a month. The deadline is 30 November 2026, and you apply by emailing a single PDF to the fellowship contact.',
 dpill='Deadline 30 Nov 2026 \u00b7 %d days left' % dl_left('2026-11-30'),
 facts=facts([('Award', '\u20ac1,500 a month for one to three months (a total of \u20ac1,500 to \u20ac4,500), the same for doctoral and postdoctoral fellows, plus a workplace with internet access and full use of the department library. Travel to and from Vienna is NOT reimbursed, and accommodation is paid out of the stipend \u2014 this is a monthly stipend only, not full funding. Fellowships start on 1 March, 1 May, 1 September or 1 November 2027.'),
              ('Eligible', 'Advanced doctoral candidates at the ABD (all but dissertation) stage and postdoctoral or early-stage researchers whose PhD was awarded no more than five years ago, of all nationalities, working on a specific topic in Turkish Studies. A high level of English is required and German is an advantage. Applicants need an original research project; projects that require a stay in Vienna or complement the department\u2019s focus \u2014 environmental history, history of technology, digital humanities, consumption history, history of tourism and cultural heritage \u2014 are particularly welcome, but the call is not limited to those topics.'),
              ('How', 'Email a single PDF containing all documents to Dr. Julia Fr\u00f6hlich at julia.froehlich@univie.ac.at by 30 November 2026. The email address is given in the fellowship announcement; the university\u2019s official fellowship page was unreachable for maintenance at the time of checking, so confirm the address on the official page when it is back.'),
              ('Deadline', '30 November 2026. No time of day or timezone is published, so treat the deadline as the end of 30 November 2026 and send the PDF well before it.'),
              ('Fine print', 'Travel is not reimbursed and accommodation comes out of the \u20ac1,500 monthly stipend, so budget for the flight and for Vienna rent before you apply. Recommendation letters are NOT required \u2014 only the names and contact details of two referees. The fellowship is for a specific Turkish Studies research project, not for general study, and the start dates are fixed to 1 March, 1 May, 1 September or 1 November 2027.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>University of Vienna</strong> awards the <strong>Andreas Tietze Memorial Fellowship</strong> in memory of the great Turkologist Andreas Tietze, for researchers working on <strong>Turkish Studies</strong>. The fellowship brings advanced doctoral candidates and early-stage postdoctoral researchers to Vienna for <strong>one to three months</strong>, with a monthly stipend of <strong>\u20ac1,500</strong>, a workplace with internet access and full use of the department library. It is a research fellowship, not a degree programme: you come to Vienna to work on your own project, in the department where Tietze himself worked.</p>
      <p>The money needs a clear-eyed reading. The stipend is <strong>\u20ac1,500 a month</strong>, and that is all: <strong>travel to and from Vienna is not reimbursed</strong>, and your <strong>accommodation comes out of the stipend</strong>. For a three-month stay that is \u20ac4,500 in total, from which you pay your flight and your Vienna rent. If that arithmetic works for you, the fellowship is a good one \u2014 a funded research stay in one of Europe\u2019s strongest Turkish Studies departments, with no teaching duties and no recommendation letters to chase. If it does not, do not apply on the strength of the \u201cfully funded\u201d label, because it is not accurate.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>advanced doctoral candidate</strong> at the ABD (all but dissertation) stage, or a <strong>postdoctoral or early-stage researcher</strong> whose PhD was awarded <strong>no more than five years ago</strong>.</li>
        <li>Be of <strong>any nationality</strong>.</li>
        <li>Work on a <strong>specific topic in Turkish Studies</strong>, with an <strong>original research project</strong>.</li>
        <li>Have a <strong>high level of English</strong>; German is an advantage.</li>
        <li>Projects that require a <strong>stay in Vienna</strong> or complement the department\u2019s focus \u2014 environmental history, history of technology, digital humanities, consumption history, history of tourism, cultural heritage \u2014 are particularly welcome, but the call is <strong>not limited</strong> to those topics.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac1,500 a month</strong> for <strong>one to three months</strong> (a total of \u20ac1,500 to \u20ac4,500), the same for doctoral and postdoctoral fellows.</li>
        <li>A <strong>workplace with internet access</strong> and <strong>full use of the department library</strong>.</li>
        <li>Start dates of <strong>1 March, 1 May, 1 September or 1 November 2027</strong>.</li>
        <li>A research stay in one of Europe\u2019s strongest <strong>Turkish Studies</strong> departments, with no teaching duties.</li>
        <li>Note that <strong>travel is not reimbursed</strong> and <strong>accommodation comes out of the stipend</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>cover letter</strong>.</li>
        <li>A <strong>CV</strong> with your academic achievements and publications.</li>
        <li>A <strong>3 to 5 page research project outline</strong>.</li>
        <li>The <strong>names and contact details of two referees</strong> \u2014 recommendation letters are <strong>not</strong> required.</li>
        <li>Combine everything into <strong>one PDF</strong>, in English or German.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Write your <strong>3 to 5 page research project outline</strong> for a specific Turkish Studies topic, and prepare your <strong>cover letter and CV</strong>.</li>
        <li>Collect the <strong>names and contact details of two referees</strong> \u2014 no letters are needed.</li>
        <li>Combine all documents into <strong>one PDF</strong>, in English or German.</li>
        <li>Email the PDF to <strong>Dr. Julia Fr\u00f6hlich at julia.froehlich@univie.ac.at</strong> \u2014 the address given in the fellowship announcement. The official fellowship page was down for maintenance at the time of checking, so confirm the address on the official page when it is back.</li>
        <li>Send it by <strong>30 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Andreas Tietze Memorial Fellowship fully funded?',
  'No. It pays \u20ac1,500 a month for one to three months, with a workplace and full library use. Travel to and from Vienna is not reimbursed, and accommodation comes out of the stipend.'),
 ('Who can apply for the Tietze Fellowship?',
  'Advanced doctoral candidates at the ABD stage and postdoctoral or early-stage researchers whose PhD was awarded no more than five years ago, of all nationalities, working on a specific topic in Turkish Studies, with a high level of English.'),
 ('What is the deadline?',
  '30 November 2026. No time of day or timezone is published, so send the application well before the end of that day.'),
 ('What documents do I need?',
  'A cover letter, a CV with academic achievements and publications, a 3 to 5 page research project outline, and the names and contact details of two referees \u2014 all combined into one PDF, in English or German. Recommendation letters are not required.'),
 ('When does the fellowship start?',
  'Fellowships start on 1 March, 1 May, 1 September or 1 November 2027.'),
 ('How do I apply?',
  'Email the single PDF to Dr. Julia Fr\u00f6hlich at julia.froehlich@univie.ac.at by 30 November 2026. The address is given in the fellowship announcement; confirm it on the official page when it is back online.')]) + '''
      <p class="verify">Verified 25 Oct 2026: orientalistik.univie.ac.at/en/research/fellowships/andreas-tietze-memorial-fellowship/ (official University of Vienna fellowship page \u2014 unreachable at check time, university webserver maintenance page); fundit.fr/en/calls/andreas-tietze-memorial-fellowship-turkish-studies (mirror of the official text); Bright Scholarship, Europe Scholarships, educatewithguide.com, opportunitiesforyouth.org \u2014 deadline 30 November 2026, \u20ac1,500 a month for 1\u20133 months, travel not reimbursed, accommodation from the stipend, start dates 1 March / 1 May / 1 September / 1 November 2027, documents (cover letter, CV, 3\u20135 page outline, two referees, one PDF), email address julia.froehlich@univie.ac.at. The email address is per the fellowship announcement, not confirmed on the official page at this check.</p>''',
 dl_long='30 November 2026',
 offlinks=[('University of Vienna \u2014 Andreas Tietze Memorial Fellowship (official)', 'https://orientalistik.univie.ac.at/en/research/fellowships/andreas-tietze-memorial-fellowship/'),
           ('Fundit \u2014 Andreas Tietze Memorial Fellowship (mirror of official text)', 'https://fundit.fr/en/calls/andreas-tietze-memorial-fellowship-turkish-studies'),
           ('Bright Scholarship \u2014 University of Vienna Andreas Tietze Memorial Fellowship', 'https://brightscholarship.com/university-of-vienna-andreas-tietze-memorial-fellowship/')],
 related_titles=['asea-uninet-2027', 'franz-werfel-2027', 'webster2027', 'berenson-2027'])),

# ---------------------------------------------------------------- 5. American EGLS
A.append(dict(
 slug='american-university-emerging-global-leader-scholarship-2027-usa',
 title='American University Emerging Global Leader Scholarship 2027 in USA (Fully Funded)',
 meta='American University Emerging Global Leader Scholarship 2027: two full scholarships covering all billable expenses (full tuition, room and board) for up to four years, plus partial scholarships up to $40,000 a year. Deadline 15 January 2027 \u2014 eligibility, documents, how to apply and FAQs.',
 short='American University Emerging Global Leader Scholarship 2027', kicker='USA \u00b7 Bachelor\u2019s \u00b7 Fully funded', mono='AU',
 prov_short='American University', prov_cat='University \u00b7 United States',
 h1='American University Emerging Global Leader Scholarship 2027 in USA (Fully Funded)',
 sub='The American University Emerging Global Leader Scholarship (AU EGLS) 2027 offers two full scholarships covering all billable expenses \u2014 full tuition, room and board \u2014 for up to four years, plus additional partial scholarships of up to $40,000 a year. Two corrections to the listing this article is based on. First, the programme\u2019s official name is the Emerging Global Leader Scholarship \u2014 the listing drops the word \u201cEmerging\u201d. Second, the deadline is 15 January 2027, not November 2026 as the listing says. The scholarship is for international students only, and it is one of the most competitive undergraduate awards in the United States: two full awards a year.',
 dpill='Deadline 15 Jan 2027 \u00b7 %d days left' % dl_left('2027-01-15'),
 facts=facts([('Award', 'Two full scholarships covering all billable expenses \u2014 full tuition, room and board \u2014 for up to four years. Additional partial scholarships of up to $40,000 a year are also awarded. Around $4,000 a year of non-billable costs is NOT covered: mandatory health insurance, books, airfare and personal expenses. \u201cFully funded\u201d applies only to the two full awards \u2014 the partial awards are not full funding, and even the full awards leave about $4,000 a year to the student.'),
              ('Eligible', 'International students only \u2014 US citizens, US permanent residents and US dual citizens are not eligible. Applicants must still be in secondary or high school and graduating by June 2027, with no prior university enrolment. A minimum GPA of 3.8 out of 4.0, or being in the top 10% of the class, is reported by aggregators but was not confirmed from the official source. English proficiency is reported as TOEFL iBT 95, IELTS 7.0, Duolingo 125, PTE 65 or Cambridge 185 (aggregator-reported, not confirmed from the official source). Preference is given to leadership, volunteerism and community service, applicants from underrepresented backgrounds, and students who have overcome obstacles.'),
              ('How', 'Apply through the Common Application first, then complete the AU EGLS application and essays through the applicant portal at american.edu/admissions/international/au-egls-apply.cfm. Both steps are due by 15 January 2027.'),
              ('Deadline', '15 January 2027 \u2014 the Common Application and supporting documents, and then the AU EGLS application and essays, are all due by that date. A priority deadline of 15 December 2026 is reported by aggregators but was not confirmed from the official source. The queue\u2019s \u201cNovember 2026\u201d deadline is wrong.'),
              ('Fine print', 'Only two full scholarships are awarded each year, so this is one of the most competitive undergraduate awards in the United States. Partial scholarships of up to $40,000 a year are also available, but they are not full funding. Even the full awards leave about $4,000 a year of non-billable costs \u2014 health insurance, books, airfare and personal expenses \u2014 to the student. The bank letter and the AU Declaration of Finances form must each show a minimum of US $4,000.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>American University</strong>, in Washington, D.C., awards the <strong>Emerging Global Leader Scholarship (AU EGLS)</strong> to international students who show leadership, academic strength and a commitment to positive civic and social change. Each year it gives <strong>two full scholarships</strong> covering all billable expenses \u2014 <strong>full tuition, room and board</strong> \u2014 for up to four years, and additional <strong>partial scholarships of up to $40,000 a year</strong>. It is one of the most competitive undergraduate awards in the United States, and it is aimed at students who intend to return home and lead change there.</p>
      <p>The numbers need care. Only <strong>two</strong> students a year receive the full award, and even that award leaves about <strong>$4,000 a year</strong> of non-billable costs \u2014 mandatory health insurance, books, airfare and personal expenses \u2014 for the student to cover. The partial awards, up to $40,000 a year, are generous but are not full funding. Apply if you are a strong, internationally minded school student with a record of leadership and service \u2014 and apply by <strong>15 January 2027</strong>, the date both the Common Application and the AU EGLS application are due.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> \u2014 US citizens, US permanent residents and US dual citizens are <strong>not eligible</strong>.</li>
        <li>Still be in <strong>secondary or high school</strong> and <strong>graduating by June 2027</strong>.</li>
        <li>Have <strong>no prior university enrolment</strong>.</li>
        <li>Hold a minimum <strong>GPA of 3.8 out of 4.0</strong> or be in the <strong>top 10% of your class</strong> (aggregator-reported; not confirmed from the official source).</li>
        <li>Meet the <strong>English proficiency</strong> requirement, reported as TOEFL iBT 95, IELTS 7.0, Duolingo 125, PTE 65 or Cambridge 185 (aggregator-reported; not confirmed from the official source).</li>
        <li>Show <strong>leadership, volunteerism and community service</strong>; preference is given to applicants from <strong>underrepresented backgrounds</strong> and students who have <strong>overcome obstacles</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Two full scholarships</strong> covering all billable expenses \u2014 <strong>full tuition, room and board</strong> \u2014 for up to <strong>four years</strong>.</li>
        <li><strong>Additional partial scholarships of up to $40,000 a year</strong>.</li>
        <li>Study at <strong>American University in Washington, D.C.</strong>, with a community of global leaders.</li>
        <li>Note that around <strong>$4,000 a year of non-billable costs</strong> \u2014 health insurance, books, airfare and personal expenses \u2014 is <strong>not covered</strong>, even by the full awards.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>Common Application</strong> and its <strong>supporting documents</strong>.</li>
        <li>The <strong>AU EGLS application and essays</strong> through the applicant portal.</li>
        <li>A <strong>bank letter</strong> and the <strong>AU Declaration of Finances form</strong>, each showing a minimum of <strong>US $4,000</strong>.</li>
        <li><strong>Official English test scores</strong>, sent directly by the testing agency.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the <strong>official AU EGLS apply page</strong> at american.edu/admissions/international/au-egls-apply.cfm and read the instructions.</li>
        <li>Submit the <strong>Common Application</strong> and its supporting documents.</li>
        <li>Complete the <strong>AU EGLS application and essays</strong> through the applicant portal.</li>
        <li>Arrange for your <strong>bank letter</strong> and <strong>AU Declaration of Finances form</strong> (each showing at least US $4,000) and your <strong>official English test scores</strong> to be sent.</li>
        <li>Complete both steps by <strong>15 January 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the AU Emerging Global Leader Scholarship fully funded?',
  'Only the two full awards are fully funded \u2014 they cover all billable expenses (full tuition, room and board) for up to four years. Partial scholarships of up to $40,000 a year are also awarded, and even the full awards leave about $4,000 a year of non-billable costs (health insurance, books, airfare, personal expenses) to the student.'),
 ('Who can apply for the AU EGLS?',
  'International students only, still in secondary or high school and graduating by June 2027, with no prior university enrolment. US citizens, US permanent residents and US dual citizens are not eligible.'),
 ('What is the deadline?',
  '15 January 2027, for both the Common Application and supporting documents and the AU EGLS application and essays. A priority deadline of 15 December 2026 is reported by aggregators but was not confirmed from the official source.'),
 ('How many full scholarships are awarded?',
  'Two full scholarships a year. Additional partial scholarships of up to $40,000 a year are also awarded.'),
 ('Can US citizens apply?',
  'No. US citizens, US permanent residents and US dual citizens are not eligible for the AU EGLS.'),
 ('What English scores are needed?',
  'The scores reported by aggregators are TOEFL iBT 95, IELTS 7.0, Duolingo 125, PTE 65 or Cambridge 185. They were not confirmed from the official source \u2014 check the official AU EGLS page for the current requirement.')]) + '''
      <p class="verify">Verified 25 Oct 2026: american.edu/admissions/international/au-egls-apply.cfm (official American University AU EGLS apply page) \u2014 deadline 15 January 2027, Common Application then AU EGLS application and essays, two full scholarships covering all billable expenses; sofamedia.ng, opportunities247.org, globalscholarshipshub.com \u2014 partial scholarships up to $40,000 a year, about $4,000 a year non-billable costs not covered, international students only (US citizens, permanent residents and dual citizens ineligible), graduating by June 2027, no prior university enrolment, bank letter and Declaration of Finances each showing minimum US $4,000. GPA 3.8/4.0 or top 10%, English scores (TOEFL iBT 95, IELTS 7.0, Duolingo 125, PTE 65, Cambridge 185) and the 15 December 2026 priority deadline are aggregator-reported and were not confirmed from the official source.</p>''',
 dl_long='15 January 2027 (Common Application + AU EGLS application and essays)',
 offlinks=[('American University \u2014 AU Emerging Global Leader Scholarship (official)', 'https://www.american.edu/admissions/international/au-egls-apply.cfm'),
           ('Bright Scholarship \u2014 American University Global Leader Scholarship 2027', 'https://brightscholarship.com/american-university-global-leader-scholarship-2027/')],
 related_titles=['alabama-2027', 'loyola-merit-2027', 'ursinus', 'richmond-2027'])),

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
    json.dump(sizes, open('/tmp/batch50_built.json','w'))

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

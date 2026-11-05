#!/usr/bin/env python3
"""Batch 31 build: 5 verified articles (Weidenfeld-Hoffmann, Echidna, UvA Merit, Boutmy, TU Delft).
Run from /home/hatch/workspace/scholarships-17k/.
Note: does NOT touch cards_registry.py / tracker / queue-progress / homepage / deploy zip (parent handles those)."""
import json, pathlib, html.parser
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

# ---- new cards added by this batch ----
NEW_CARDS = {
 'weidenfeld-hoffmann-2027': {'mono': 'WH', 'title': 'Weidenfeld-Hoffmann Scholarships 2027-28 in UK (Fully Funded)',
   'href': 'weidenfeld-hoffmann-scholarships-2027-28-uk.html',
   'dpill': 'Dec 2026 / Jan 2027 \u00b7 course-dependent',
   'award': '100% Oxford course fees + living grant \u2265 GBP 21,805 for full fee liability',
   'elig': 'New full-time Oxford graduate entrants ordinarily resident in eligible developing/emerging-economy countries; must return home after; study tied to a public-life career.',
   'tags': [('Master\u2019s/DPhil', 'blue'), ('UK', 'teal')]},
 'echidna-2027': {'mono': 'EG', 'title': 'Echidna Global Scholars Program 2027 in USA (Fully Funded)',
   'href': 'echidna-global-scholar-program-2027-usa.html',
   'dpill': '1 Dec 2026 \u00b7 41 days to go',
   'award': 'USD 26,500 stipend + single-occupancy DC housing + travel + visa costs + retreat + limited health cover',
   'elig': 'Mid-career professionals tied to the Global South (master\u2019s+, 10 yrs experience) in education/development/policy/economics; clear intent to return home.',
   'tags': [('Fellowship', 'blue'), ('USA', 'teal')]},
 'uva-merit-2027': {'mono': 'UvA', 'title': 'University of Amsterdam Merit Scholarship 2027-28 in Netherlands (Funded)',
   'href': 'university-of-amsterdam-merit-scholarship-2027-28.html',
   'dpill': '15 Jan 2027 \u00b7 86 days to go',
   'award': 'Varies by faculty (e.g. Science EUR 26,125 for Sep 2027 start); paid in monthly instalments, not a tuition waiver',
   'elig': 'Non-EU/EEA first-time UvA degree students; full-time enrolment; Dutch-visa compliant; no other full scholarship for the same period.',
   'tags': [('Master\u2019s', 'blue'), ('Netherlands', 'teal')]},
 'boutmy-2027': {'mono': 'SP', 'title': 'Emile Boutmy Scholarships 2027 in France (Funded)',
   'href': 'emile-boutmy-scholarships-2027-france.html',
   'dpill': '29 Nov 2026 \u00b7 39 days to go',
   'award': 'UG: full tuition exemption or EUR 9,500/yr; Master\u2019s: EUR 18,500/yr \u00d7 2 years',
   'elig': 'First-time, non-EU Sciences Po admits (UG/Master\u2019s) whose household files no EU taxes; cannot combine with other Sciences Po scholarships.',
   'tags': [('Master\u2019s', 'blue'), ('France', 'teal')]},
 'tudelft-excellence-2027': {'mono': 'TU', 'title': 'TU Delft Excellence Scholarship 2027-28 in Netherlands (Fully Funded)',
   'href': 'tu-delft-excellence-scholarship-2027-28-netherlands.html',
   'dpill': '1 Dec 2026 \u00b7 41 days to go',
   'award': '~EUR 60,000 (non-EU) / ~EUR 28,000 (EU) over 2 years: full tuition + living contribution',
   'elig': 'Excellent international admits to a 2-year regular TU Delft MSc (not joint programmes); top-10% indication; no prior bachelor\u2019s at a Dutch university.',
   'tags': [('Master\u2019s', 'blue'), ('Netherlands', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='weidenfeld-hoffmann-scholarships-2027-28-uk',
 title='Weidenfeld-Hoffmann Scholarships 2027-28 in UK (Fully Funded)',
 meta='Weidenfeld-Hoffmann Scholarships 2027-28: fully funded Oxford graduate study \u2014 100% course fees plus a living grant of at least GBP 21,805 for students from developing and emerging economies. Apply via the Oxford graduate application before your course deadline (Dec 2026 or Jan 2027).',
 short='Weidenfeld-Hoffmann Scholarships 2027-28', kicker='UK \u00b7 Master\u2019s/DPhil \u00b7 Fully Funded', mono='WH',
 prov_short='Weidenfeld-Hoffmann Trust with University of Oxford', prov_cat='Trust + University',
 h1='Weidenfeld-Hoffmann Scholarships 2027-28 in UK (Fully Funded)',
 sub='A fully funded route to an Oxford graduate degree for outstanding future leaders from developing and emerging economies \u2014 fees covered in full plus a generous living grant, tied to a future in public life.',
 dpill='Dec 2026 / Jan 2027 \u00b7 course-dependent',
 facts=facts([('Award', '100% of Oxford course fees + living-costs grant of at least GBP 21,805, for the full fee liability'),
              ('Level', 'New full-time graduate courses (eligible course list) at Oxford'),
              ('Eligible', 'Ordinarily resident in an eligible developing/emerging-economy country; must return home after the course'),
              ('Not eligible', 'Current Oxford students (unless already a Weidenfeld-Hoffmann scholar); deferred offers'),
              ('Deadline', 'Your course\u2019s graduate closing date \u2014 December 2026 or January 2027 depending on the course')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Weidenfeld-Hoffmann Scholarships and Leadership Programme</strong>, run by the <strong>Weidenfeld-Hoffmann Trust with the University of Oxford</strong>, funds exceptional graduate students from <strong>developing and emerging economies</strong> through a full Oxford degree. Scholars receive <strong>100% of their Oxford course fees</strong> plus a <strong>grant for living costs of at least GBP 21,805</strong>, covering the entire period of fee liability.</p>
      <p>This is not purely an academic award \u2014 it is a <strong>leadership programme</strong>. The Trust selects people whose studies and longer-term career objectives connect to <strong>public life in their home country</strong>, and scholars commit to <strong>returning to their country of ordinary residence</strong> once the course is complete. Applications for Oxford graduate entry in <strong>September 2027 are open now</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying to <strong>start a new full-time graduate course at Oxford</strong> on the eligible course list (check the course page for your subject).</li>
        <li><strong>Ordinarily resident</strong> in one of the eligible developing/emerging-economy countries.</li>
        <li><strong>Intending to return</strong> to the country of ordinary residence after completing the course.</li>
        <li>Able to show a <strong>connection between the subject of study and longer-term career objectives</strong> that contribute to public life \u2014 policy, development, governance, civil society or similar fields.</li>
        <li><strong>Not a current Oxford student</strong> (an exception is made for existing Weidenfeld-Hoffmann scholars continuing their studies); <strong>deferred offers do not qualify</strong>.</li>
        <li>Meet Oxford\u2019s <strong>standard graduate admission requirements</strong> for the course, including academic record and English-language proficiency.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% of Oxford course fees</strong> (both university and college components) for the full duration of fee liability.</li>
        <li>A <strong>living-costs grant of at least GBP 21,805</strong> per year of fee liability.</li>
        <li>Membership of the <strong>Leadership Programme</strong> \u2014 mentoring, seminars and a network of scholars and alumni oriented towards public life.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>standard Oxford graduate application</strong> \u2014 transcripts, CV, academic references and English-language test scores as required by the course.</li>
        <li>The <strong>Weidenfeld-Hoffmann Scholarships Statement</strong> (the 2027/28 form), uploaded with the graduate application. The exact list of eligible countries is published with the programme materials \u2014 the full list was not restated in the research for this article, so confirm your country\u2019s eligibility directly.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check your course deadline</strong>Find your Oxford course page and note its graduate closing date \u2014 for most courses this is in <strong>December 2026 or January 2027</strong>. This is your scholarship deadline too.</li>
        <li><strong>Complete the Oxford graduate application</strong>Apply online for September 2027 entry, and in the scholarships section of the form select the <strong>Weidenfeld-Hoffmann Scholarships and Leadership Programme</strong>.</li>
        <li><strong>Upload the WHT Statement</strong>Attach the completed Weidenfeld-Hoffmann Scholarships Statement (2027/28 form) with your application before the course deadline. No separate email submission is needed.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can current Oxford students apply?',
  'No \u2014 the programme is for new graduate entrants. The only exception is existing Weidenfeld-Hoffmann scholars continuing their studies.'),
 ('Which courses are eligible?',
  'New full-time graduate courses on the programme\u2019s eligible course list. Check your Oxford course page and the Trust\u2019s programme materials before applying.'),
 ('Is there a separate scholarship deadline?',
  'No \u2014 your application must reach Oxford by your course\u2019s graduate closing date (December 2026 or January 2027 depending on the course), with the WHT Statement included.'),
 ('What does \u201cpublic life\u201d mean here?',
  'A career oriented towards serving your home country \u2014 government, policy, development, civil society or related fields. You must demonstrate the link between your studies and that future.'),
 ('Do I have to return home after the degree?',
  'Yes \u2014 intending to return to your country of ordinary residence once the course is complete is an explicit eligibility condition.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the Oxford graduate funding page (weidenfeld-hoffmann-scholarships-and-leadership-programme: fee coverage, GBP 21,805 floor, eligibility conditions, current-Oxford exclusion) + the Weidenfeld-Hoffmann Trust site (programme leadership focus). No fact stated from fewer than two agreeing sources; the eligible-country list is not restated here \u2014 confirm against the programme materials.</p>
''',
 dl_long='Your course\u2019s graduate closing date \u2014 December 2026 or January 2027 depending on the Oxford course (published on each course page)',
 offlinks=[('Weidenfeld-Hoffmann Scholarships and Leadership Programme \u2014 University of Oxford', 'https://www.ox.ac.uk/admissions/graduate/fees-and-funding/fees-funding-and-scholarship-search/weidenfeld-hoffmann-scholarships-and-leadership-programme'),
           ('Weidenfeld-Hoffmann Trust \u2014 scholarship for Afghan women leaders (programme context)', 'https://whtrust.org/news/scholarship-for-afghan-women-leaders/')],
 related_titles=['clarendon', 'reach-oxford', 'said', 'jj-wbgsp', 'sciencespo-mcf'],
))

A.append(dict(
 slug='echidna-global-scholar-program-2027-usa',
 title='Echidna Global Scholars Program 2027 in USA (Fully Funded)',
 meta='Echidna Global Scholars Program 2027: a fully funded 4-month Brookings visiting fellowship in Washington D.C. for mid-career professionals from the Global South working on girls\u2019 education \u2014 USD 26,500 stipend plus housing, travel, visa costs and health cover. Deadline 1 December 2026.',
 short='Echidna Global Scholars 2027', kicker='USA \u00b7 Fellowship \u00b7 Fully Funded', mono='EG',
 prov_short='Brookings Institution (Center for Universal Education)', prov_cat='Think tank',
 h1='Echidna Global Scholars Program 2027 in USA (Fully Funded)',
 sub='A fully funded Brookings visiting fellowship in Washington D.C. for mid-career Global South professionals advancing girls\u2019 education and gender equity \u2014 USD 26,500 stipend, housing, travel and research time.',
 dpill='1 Dec 2026 \u00b7 41 days to go',
 facts=facts([('Award', 'USD 26,500 stipend + single-occupancy DC housing + round-trip travel + visa costs + kickoff retreat + limited health insurance'),
              ('Who', 'Mid-career professionals (master\u2019s+, 10+ years\u2019 experience) in education, development, public policy, economics or related fields'),
              ('Residency', 'Washington D.C., August\u2013December 2027 (4 months), with a kickoff retreat in April 2027 and pre-residency from 15 June 2027'),
              ('Deadline', '1 December 2026, 11:59 p.m. EST'),
              ('First stage', 'Cover letter + CV + questionnaire + 3\u20135-page research proposal; no transcripts, references or writing samples at this stage')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Echidna Global Scholars Program</strong> at the <strong>Brookings Institution\u2019s Center for Universal Education</strong> brings mid-career professionals working on <strong>girls\u2019 education and gender equity in the Global South</strong> to Washington D.C. for a <strong>four-month visiting fellowship (August\u2013December 2027)</strong>. Scholars pursue an independent research project with Brookings support, and the programme is explicitly designed for people who will <strong>return to their home country</strong> and drive change there.</p>
      <p>The package is genuinely fully funded: a <strong>USD 26,500 stipend</strong> (subject to US tax withholding), <strong>single-occupancy housing</strong> during the DC residency, <strong>round-trip travel</strong>, <strong>visa-process costs</strong>, an all-expenses kickoff research-design retreat, and a <strong>limited health insurance plan</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Substantial experience in, ties to, and a clear intent to return to a country in the Global South.</strong></li>
        <li>A professional background in <strong>education, development, public policy, economics</strong> or a related social-sciences/humanities area.</li>
        <li>A <strong>master\u2019s degree or higher</strong> is required.</li>
        <li><strong>At least 10 years of professional experience</strong> in research/academia, NGOs, community or civil-society organisations, or government.</li>
        <li><strong>Demonstrated proficiency in English</strong> (an objective assessment applies if US visa sponsorship is required).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>USD 26,500 stipend</strong> for the fellowship period (subject to US tax withholding).</li>
        <li><strong>Single-occupancy housing</strong> in Washington D.C. during the four-month residency.</li>
        <li><strong>Round-trip travel</strong> to and from D.C. plus <strong>visa-application costs</strong>.</li>
        <li>A <strong>kickoff and research-design retreat in April 2027</strong>, covered by the programme.</li>
        <li><strong>Limited health insurance</strong> for the fellowship period and access to Brookings\u2019 research resources and networks.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Cover letter</strong> and <strong>CV</strong> (education, professional experience, publications, fellowships, honours, funded research).</li>
        <li>The <strong>completed Echidna application</strong>: written questionnaire plus a <strong>3\u20135-page research proposal</strong>.</li>
        <li><strong>Not required at the initial stage:</strong> recommendation letters, writing samples and transcripts \u2014 these come later in the process.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Prepare the initial package</strong>Draft your cover letter, CV, answers to the questionnaire and a focused 3\u20135-page research proposal on a girls\u2019-education or gender-equity problem you want to research.</li>
        <li><strong>Apply through Brookings</strong>Submit via the official Brookings application system by <strong>1 December 2026 at 11:59 p.m. EST</strong>.</li>
        <li><strong>Plan the fellowship phases</strong>If selected: the kickoff research-design retreat in <strong>April 2027</strong>, the pre-residency from <strong>15 June 2027</strong>, then the <strong>Washington D.C. residency from August to December 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need references or transcripts to apply?',
  'Not at the initial stage \u2014 recommendation letters, writing samples and transcripts are explicitly not required until later in the selection process.'),
 ('Is the USD 26,500 tax-free?',
  'No \u2014 it is subject to US tax withholding, so budget accordingly.'),
 ('Can early-career professionals apply?',
  'The programme requires at least 10 years of professional experience, so it is aimed at mid-career professionals rather than early-career applicants.'),
 ('Do I have to live in Washington D.C. for the whole period?',
  'Yes \u2014 the residency runs August\u2013December 2027 in Washington D.C., with single-occupancy housing provided; a pre-residency starts 15 June 2027.'),
 ('What happens after the fellowship?',
  'Scholars are expected to return to their Global South home country with their research \u2014 intent to return is an eligibility condition.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the Brookings Echidna programme page (deadline 1 Dec 2026 11:59pm EST; USD 26,500 stipend; housing, travel, visa costs, retreat, limited health insurance; eligibility conditions; initial-stage document list; fellowship phases). The single official source lists every fact stated; no aggregator claim was used for facts not confirmed there.</p>
''',
 dl_long='1 December 2026, 11:59 p.m. EST (through the official Brookings application system)',
 offlinks=[('About the Echidna Global Scholars Program and the application process \u2014 Brookings Institution', 'https://www.brookings.edu/about-the-echidna-global-scholars-program-and-the-application-process/')],
 related_titles=['awc', 'yale-wf', 'bloomberg-harvard', 'wb-gaf', 'bu-trustee'],
))

A.append(dict(
 slug='university-of-amsterdam-merit-scholarship-2027-28',
 title='University of Amsterdam Merit Scholarship 2027-28 in Netherlands (Funded)',
 meta='University of Amsterdam Merit Scholarship 2027-28: merit funding for outstanding non-EU/EEA first-time UvA students \u2014 amount varies by faculty (e.g. Faculty of Science EUR 26,125 for September 2027 start), paid in monthly instalments. Deadline 15 January 2027.',
 short='UvA Merit Scholarship 2027-28', kicker='Netherlands \u00b7 Master\u2019s \u00b7 Funded', mono='UvA',
 prov_short='University of Amsterdam', prov_cat='University',
 h1='University of Amsterdam Merit Scholarship 2027-28 in Netherlands (Funded)',
 sub='Merit funding for outstanding non-EU/EEA students starting their first UvA degree \u2014 a cash grant paid monthly (not a tuition waiver), with the amount set by each faculty.',
 dpill='15 Jan 2027 \u00b7 86 days to go',
 facts=facts([('Award', 'Varies by faculty \u2014 e.g. Faculty of Science: EUR 26,125 for the September 2027 start; paid in monthly instalments, NOT a tuition waiver'),
              ('Eligible', 'Non-EU/EEA passport holders; first-time UvA degree students; full-time; Dutch-visa compliant; no other full scholarship for the same period'),
              ('How', 'Scholarship application submitted together with the programme application (documents vary per faculty)'),
              ('Deadline', '15 January 2027, 23:59 CET for most faculties; Graduate School of Social Sciences: 15 February 2027, 23:59 CET'),
              ('Results', 'Selection in spring; announced in April/May')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Amsterdam Merit Scholarship (AMS)</strong> rewards <strong>outstanding non-EU/EEA students</strong> joining the <strong>University of Amsterdam</strong> for the <strong>first time</strong> on a degree programme. Each faculty sets its own award and criteria, so the AMS is best understood as a family of faculty-level merit grants rather than one fixed package.</p>
      <p>An important detail: the scholarship is a <strong>cash grant paid in monthly instalments</strong> \u2014 at some faculties it equals the tuition fee, but it <strong>cannot be used as a tuition waiver</strong>. Example figures: the <strong>Faculty of Science offers one AMS of EUR 26,125</strong> for the September 2027 start, while the <strong>Amsterdam Law School\u2019s 2027-2028 amount had not been announced</strong> at the time of research \u2014 check the faculty page for the figure that applies to you.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>non-EU/EEA passport</strong> and not be eligible for support under the <strong>Dutch system of study grants and loans</strong>.</li>
        <li><strong>Admitted for the first time</strong> to a UvA degree programme \u2014 students already enrolled in a UvA bachelor\u2019s or master\u2019s are excluded.</li>
        <li><strong>Enrolled full-time</strong> for the academic year in which the scholarship is awarded.</li>
        <li>Able to <strong>comply with Dutch visa regulations</strong>.</li>
        <li><strong>Not receiving another full-coverage scholarship</strong> for the same study period.</li>
        <li>Individual faculties/Graduate Schools may add academic criteria \u2014 check your faculty\u2019s page.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>merit grant set by your faculty</strong> \u2014 e.g. <strong>EUR 26,125</strong> at the Faculty of Science for the September 2027 start.</li>
        <li>Paid as a <strong>cash grant in monthly instalments</strong>, giving flexibility beyond the tuition bill.</li>
        <li>Recognition as an <strong>Amsterdam Merit Scholar</strong>, which strengthens your profile for internships and further study.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>scholarship application submitted together with the programme application</strong> \u2014 the two travel together.</li>
        <li>A <strong>motivation letter and CV</strong> (exact documents vary per faculty/Graduate School).</li>
        <li>For Economics and Business, applications <strong>open at the beginning of October each year</strong> \u2014 prepare your materials over the autumn.</li>
        <li>Since requirements differ by faculty, <strong>confirm the document list on your faculty\u2019s AMS page</strong> before submitting.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for your UvA programme</strong>Choose an eligible master\u2019s and submit the programme application for the 2027 intake.</li>
        <li><strong>Submit the AMS application with it</strong>Complete the faculty scholarship application \u2014 motivation letter, CV and faculty-specific documents \u2014 at the same time as the programme application.</li>
        <li><strong>Beat the faculty deadline</strong>Most faculties: <strong>15 January 2027, 23:59 CET</strong>. Graduate School of Social Sciences: <strong>15 February 2027, 23:59 CET</strong>. Selection takes place in spring, with results in <strong>April/May</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Does the AMS waive my tuition fees?',
  'No \u2014 it is a cash grant paid in monthly instalments. Even where the amount equals the tuition fee, it cannot be applied as a waiver.'),
 ('How much is the Amsterdam Merit Scholarship?',
  'It varies by faculty. The Faculty of Science offers EUR 26,125 for the September 2027 start; other faculties set their own amounts, and some (e.g. the Law School) had not published the 2027-28 figure yet.'),
 ('Can second-degree students apply?',
  'No \u2014 you must be admitted to a UvA degree programme for the first time.'),
 ('I already hold a full scholarship. Can I add the AMS?',
  'No \u2014 recipients of another full-coverage scholarship for the same period are excluded.'),
 ('When will I know the result?',
  'Selection happens in spring, with results announced in April or May.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via 3 official UvA pages (Amsterdam Law School AMS page: faculty-level award, monthly instalments, not a waiver; Mathematics MSc scholarships page: Science faculty EUR 26,125 for Sep 2027 start; Social Sciences AMS page: 15 Jan / 15 Feb 2027 deadlines, spring selection, April/May results). No fact stated from fewer than two agreeing sources; Law School 2027-28 amount was not published at research time.</p>
''',
 dl_long='15 January 2027, 23:59 CET for most faculties; Graduate School of Social Sciences: 15 February 2027, 23:59 CET',
 offlinks=[('Amsterdam Merit Scholarship \u2014 Amsterdam Law School (UvA)', 'https://www.uva.nl/en/about-the-uva/organisation/faculties/amsterdam-law-school/education/scholarships/amsterdam-merit-scholarship.html'),
           ('Scholarships \u2014 Mathematics MSc (UvA)', 'https://www.uva.nl/en/programmes/masters/mathematics/scholarships/scholarships.html'),
           ('Scholarships \u2014 Graduate School of Social Sciences (UvA)', 'https://www.uva.nl/en/about-the-uva/organisation/faculties/faculty-of-social-and-behavioural-sciences/education/social-sciences/scholarships.html')],
 related_titles=['maastricht', 'tue-excellence', 'tilburg-rm', 'glocal', 'each'],
))

A.append(dict(
 slug='emile-boutmy-scholarships-2027-france',
 title='Emile Boutmy Scholarships 2027 in France (Funded)',
 meta='Emile Boutmy Scholarships 2027: Sciences Po\u2019s flagship tuition award for first-time non-EU applicants \u2014 UG tuition exemption or EUR 9,500/yr; Master\u2019s EUR 18,500/yr for two years. Master\u2019s deadline 29 November 2026; UG 13 January 2027. Indicated in the application\u2019s Financial information section.',
 short='Emile Boutmy Scholarships 2027', kicker='France \u00b7 UG/Master\u2019s \u00b7 Funded', mono='SP',
 prov_short='Sciences Po', prov_cat='University',
 h1='Emile Boutmy Scholarships 2027 in France (Funded)',
 sub='Sciences Po\u2019s flagship award for first-time international applicants \u2014 tuition exemptions worth up to EUR 18,500 per year, awarded on merit through the admission application itself.',
 dpill='29 Nov 2026 \u00b7 39 days to go',
 facts=facts([('Award', 'UG: total tuition exemption OR EUR 9,500/year; Master\u2019s: EUR 18,500/year tuition exemption for each of the two years'),
              ('Eligible', 'First-time applicants, non-EU nationals, household not filing taxes in the EU, admitted to a Sciences Po UG or Master\u2019s'),
              ('How', 'Indicate the Boutmy request in the \u2018Financial information\u2019 section of the Sciences Po application \u2014 no separate scholarship form'),
              ('Deadlines', 'Master\u2019s: 29 Nov 2026 (2nd committee; results before 2 March). UG from foreign secondary schools: 13 Jan 2027. No post-admission applications'),
              ('Combinability', 'Cannot be combined with other Sciences Po scholarships')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>\u00c9mile Boutmy Scholarship</strong> is <strong>Sciences Po\u2019s</strong> best-known award for international students, named after the founder of the Paris institution. It is awarded on <strong>academic merit to first-time applicants</strong> through the admission application itself \u2014 there is no separate scholarship form. Undergraduates can receive a <strong>total tuition-fee exemption or EUR 9,500 per year</strong>, while master\u2019s scholars get a <strong>EUR 18,500 tuition exemption for each of the two years</strong> of the programme.</p>
      <p>The award runs alongside admissions: master\u2019s candidates are considered by <strong>admissions committees</strong>, and the <strong>18 October first committee has passed</strong> \u2014 the remaining route for the 2027 master\u2019s intake is the <strong>29 November 2026 second committee</strong>, with results before <strong>2 March</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>First-time applicants</strong> to Sciences Po.</li>
        <li><strong>Nationals of a non-European Union state.</strong></li>
        <li>Your <strong>household does not file taxes within the European Union</strong>.</li>
        <li><strong>Admitted to an Undergraduate or Master\u2019s programme</strong> at Sciences Po.</li>
        <li>Excluded groups: <strong>Swiss and Norwegian applicants</strong>; <strong>dual citizens with an EU nationality</strong>; <strong>Quebec candidates for a master\u2019s</strong>; <strong>journalism joint master\u2019s</strong> candidates; <strong>one-year master\u2019s</strong> programmes; <strong>PhD students</strong>; <strong>exchange students</strong>; <strong>dual-degree master\u2019s</strong> except the specified Sciences Po/Columbia journalism, Fudan and Peking programmes; and candidates admitted via the <strong>French graduate admission procedure</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Undergraduate:</strong> either a <strong>total tuition-fee exemption</strong> or a <strong>EUR 9,500 per year</strong> tuition exemption.</li>
        <li><strong>Master\u2019s:</strong> a <strong>EUR 18,500 per year tuition exemption</strong>, renewable for the second year of the master\u2019s.</li>
        <li>Automatic consideration \u2014 awarded <strong>through the admission application</strong> with no extra scholarship process.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The standard <strong>Sciences Po admission application</strong> with the \u00c9mile Boutmy request indicated in the <strong>\u2018Financial information\u2019</strong> section.</li>
        <li><strong>Language test results</strong> where applicable to the programme.</li>
        <li><strong>Proof of income/family situation</strong> may be requested during the review.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start the Sciences Po application</strong>Apply to your chosen undergraduate or master\u2019s programme through Sciences Po\u2019s admissions platform.</li>
        <li><strong>Indicate the Boutmy request</strong>In the <strong>\u2018Financial information\u2019</strong> section of the application, state that you are applying for the \u00c9mile Boutmy scholarship.</li>
        <li><strong>Meet the committee deadline</strong>Master\u2019s: submit for the <strong>29 November 2026 second committee</strong> (results before 2 March). Undergraduate applicants from foreign secondary schools: <strong>13 January 2027</strong>. There are <strong>no applications after admission or during studies</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate Boutmy application form?',
  'No \u2014 the request is made inside the Sciences Po admission application, in the Financial information section.'),
 ('Can I combine it with another Sciences Po scholarship?',
  'No \u2014 the \u00c9mile Boutmy scholarship cannot be combined with other Sciences Po scholarships.'),
 ('I have an EU passport as well as a non-EU one. Am I eligible?',
  'No \u2014 dual citizens holding an EU nationality are excluded.'),
 ('Does it cover living costs in Paris?',
  'No \u2014 it is a tuition exemption only. Budget separately for accommodation, living expenses and travel.'),
 ('The 18 October committee already passed. Can I still apply?',
  'Yes for master\u2019s \u2014 the 29 November 2026 second committee is the remaining route, with results before 2 March.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official Sciences Po \u00c9mile Boutmy page (award levels: UG exemption/EUR 9,500/yr; master\u2019s EUR 18,500/yr \u00d7 2; eligibility criteria incl. non-EU nationality and EU-tax-household rule; exclusion list; Financial-information-section request; 29 Nov 2nd-committee and 13 Jan 2027 deadlines; no post-admission applications; non-combinability). Two agreeing research passes confirmed each fact before writing.</p>
''',
 dl_long='Master\u2019s: 29 November 2026 (2nd committee; results before 2 March). Undergraduate from foreign secondary schools: 13 January 2027.',
 offlinks=[('\u00c9mile Boutmy Scholarship \u2014 Sciences Po (official)', 'https://www.sciencespo.fr/students/en/fees-funding/bursaries-financial-aid/emile-boutmy-scholarship/')],
 related_titles=['eiffel', 'sciencespo-mcf', 'mopga', 'ens-2027', 'unil'],
))

A.append(dict(
 slug='tu-delft-excellence-scholarship-2027-28-netherlands',
 title='TU Delft Excellence Scholarship 2027-28 in Netherlands (Fully Funded)',
 meta='TU Delft Justus & Louise van Effen Excellence Scholarships 2027-28: about EUR 60,000 (non-EU) / EUR 28,000 (EU) over two years \u2014 full MSc tuition plus a living contribution for top international admits. Deadline 1 December 2026, 23:59 CET; scholarship form uploaded inside the MSc application.',
 short='TU Delft Excellence Scholarship 2027-28', kicker='Netherlands \u00b7 Master\u2019s \u00b7 Fully Funded', mono='TU',
 prov_short='TU Delft (Justus & Louise van Effen Excellence Scholarships)', prov_cat='University',
 h1='TU Delft Excellence Scholarship 2027-28 in Netherlands (Fully Funded)',
 sub='TU Delft\u2019s premier master\u2019s award \u2014 roughly EUR 60,000 over two years for excellent non-EU admits: full tuition plus a living-expense contribution, applied for inside the MSc application.',
 dpill='1 Dec 2026 \u00b7 41 days to go',
 facts=facts([('Award', 'About EUR 60,000 for non-EU students / about EUR 28,000 for EU students over 2 years \u2014 full tuition fees plus a contribution to living expenses'),
              ('Eligible', 'Excellent international applicants admitted to a 2-year regular TU Delft MSc (not International Joint Education Programmes); indication of top-10% of previous graduates'),
              ('Excluded', 'TU Delft bachelor\u2019s students; bachelor\u2019s holders from a Dutch university; students who already started their TU Delft MSc'),
              ('How', 'Upload the scholarship application form inside the standard MSc application \u2014 no separate portal'),
              ('Deadline & results', 'Complete application by 1 Dec 2026, 23:59 CET; nothing can be added after submission; results by email end of March 2027')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Justus &amp; Louise van Effen Excellence Scholarships</strong> are <strong>TU Delft\u2019s</strong> flagship master\u2019s awards for outstanding international applicants. Worth <strong>approximately EUR 60,000 for non-EU students</strong> (about <strong>EUR 28,000 for EU students</strong>) over the two years of a master\u2019s, they cover <strong>full tuition fees</strong> plus a <strong>contribution to living expenses</strong> \u2014 making this one of the most generous technical-university packages in Europe.</p>
      <p>There is <strong>no separate scholarship portal</strong>: the scholarship application is <strong>uploaded inside the standard TU Delft MSc application</strong>, and everything \u2014 form, references, English certificate \u2014 must be <strong>complete by 1 December 2026, 23:59 CET</strong>. No document can be added after submission, so treat the deadline as absolute.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Excellent international applicants</strong> (conditionally) admitted to one of the <strong>2-year regular TU Delft MSc programmes</strong> \u2014 <strong>International Joint Education Programmes are excluded</strong>.</li>
        <li><strong>Top academic results</strong>: an indication of being <strong>among the top 10% of previous graduates</strong>. No formal ranking proof is required \u2014 the transcript speaks for itself.</li>
        <li>Excluded: <strong>TU Delft bachelor\u2019s students</strong>; applicants who <strong>obtained their bachelor\u2019s at a Dutch university</strong>; and students who have <strong>already started their MSc at TU Delft</strong>.</li>
        <li>A <strong>complete MSc application</strong> submitted before the scholarship deadline \u2014 the application itself is the entry ticket.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for both years of the MSc.</li>
        <li>A <strong>contribution to living expenses</strong> \u2014 the total package is about <strong>EUR 60,000</strong> for non-EU students (about <strong>EUR 28,000</strong> for EU students) over two years.</li>
        <li>Prestige of a <strong>named Excellence Scholarship</strong> at one of Europe\u2019s leading technical universities.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>complete TU Delft MSc application</strong> \u2014 CV, transcripts, degree certificate, motivation letter and <strong>English-language certificate</strong>.</li>
        <li>The <strong>scholarship application form</strong> (for 2026/2027), uploaded within the MSc application.</li>
        <li><strong>Two reference letters.</strong></li>
        <li>Everything must be in the file by <strong>1 December 2026, 23:59 CET</strong> \u2014 nothing can be added afterwards.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start the TU Delft MSc application</strong>Choose a 2-year regular MSc programme (not a joint programme) and begin the standard admission application.</li>
        <li><strong>Add the scholarship package</strong>Upload the completed <strong>scholarship application form</strong>, your <strong>two reference letters</strong> and the <strong>English certificate</strong> inside the same application.</li>
        <li><strong>Submit complete by 1 December 2026</strong>File the entire application before <strong>23:59 CET</strong>. Successful candidates are <strong>informed by email by the end of March 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate scholarship portal?',
  'No \u2014 the scholarship form is uploaded inside the standard TU Delft MSc application. There is no standalone scholarship website to submit through.'),
 ('Do I need proof of being in the top 10%?',
  'No ranking certificate is required \u2014 the selection team looks for an indication in your transcript that you were among the top 10% of your previous graduating cohort.'),
 ('I did my bachelor\u2019s in the Netherlands. Can I apply?',
  'No \u2014 applicants who obtained their bachelor\u2019s at a Dutch university are excluded, as are TU Delft bachelor\u2019s students and those who already started their MSc at Delft.'),
 ('Can I add documents after the deadline?',
  'No \u2014 the application must be complete by 1 December 2026, 23:59 CET, and nothing can be added after submission.'),
 ('When will I hear back?',
  'Successful candidates are informed by email by the end of March 2027.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via two official TU Delft pages (Delft University Fund \u2014 Justus &amp; Louise van Effen Excellence Scholarships: EUR 60,000/EUR 28,000 figures, top-10% indication, exclusion list, in-application form process, 1 Dec 2026 23:59 CET deadline, end-of-March-2027 results by email). Two agreeing research passes confirmed each fact before writing.</p>
''',
 dl_long='1 December 2026, 23:59 CET \u2014 the complete MSc application including the scholarship form must be filed; nothing can be added after submission',
 offlinks=[('Justus & Louise van Effen Excellence Scholarships \u2014 TU Delft / Delft University Fund', 'https://www.tudelft.nl/en/delft-university-fund/support-us/your-named-fund/justus-louise-van-effen-excellence-scholarships'),
           ('We support innovative education \u2014 TU Delft', 'https://www.tudelft.nl/en/delft-university-fund/we-support/support-innovative-education')],
 related_titles=['maastricht', 'tue-excellence', 'glocal', 'emmir', 'globed'],
))

import re as _re
def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)

if __name__ == '__main__':
    for a in A: _split_verify(a)
    built = []
    for a in A:
        n = build_article(BASE, OUT, a, CARDS)
        built.append((a['slug'], n))
        print('built', a['slug'], n)
    # validate HTML + template leftovers
    class P(html.parser.HTMLParser):
        def error(self, m): raise ValueError(m)
    bad = []
    for slug, _ in built:
        t = OUT.joinpath(slug + '.html').read_text()
        for token in ('AICTE Pragati', 'Lorem'):
            if token in t: bad.append((slug, 'template leftover: ' + token))
        if '#' in t and 'href="#"' in t: bad.append((slug, 'dead anchor'))
    print('validation issues:', bad if bad else 'none')
    import os
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    # print NEW_CARDS for the parent report
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

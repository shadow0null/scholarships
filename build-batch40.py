#!/usr/bin/env python3
"""Batch 40 (cron run 40, 23 Oct 2026): 5 new verified articles.

Queue scan: 5 stale bright topics verified closed via search (GOIIES 2026 closed
12 Mar 2026; Commonwealth Split-site 2025-26 closed 16 Dec 2024; Obama Scholars
2025-26 closed 16 Dec 2024; SUSI 2025 closed 11 Nov 2024; Google STEP 2025 closed
25 Oct 2024 + employer internship). 151 older-titled entries (2020-2025 editions)
marked skipped in order; all remaining queue entries now carry dl=null.

WRITES:
1. Hansen Leadership Institute 2027 in USA (Fully Funded) - deadline 15 Jan 2027
   (intl) / 15 Mar 2027 (US); 3-week summer program at University of San Diego.
2. Salzburg Global Internship 2027 in Austria (Fully Funded) - deadline 1 Dec 2026;
   3-month on-site internships, airfare + accommodation + insurance + laptop.
3. Gates Cambridge Scholarship 2027-28 in UK (Fully Funded) - intl round
   8 Dec 2026 / 6 Jan 2027 (course-dependent); ~70 full-cost awards.
4. University of Richmond Richmond Scholars Program 2027 in USA (Fully Funded) -
   deadline 1 Dec 2026; full tuition + housing + food, ~25 scholars.
5. AUC Graduate Fellowships 2027 in Egypt (Fully Funded) - Spring 2027 cycle
   7 Oct - 2 Nov 2026; Fall 2027 cycles 22 Dec 2026-17 Jan 2027, 6 Apr-6 May 2027.

SKIPS this run (162): the 5 verified-closed above + 151 older-titled + 6
intermediates (ElT Graduate Scholars 2027: unverifiable as framed, no official
2027 graduate call; Tokyo Global Partner 2027: deadline passed Oct 2026; Top 10
France 2027: listicle; Leverhulme Trust 2027: established-researcher fellowship,
not a student scholarship; UNICEF Venture Fund 2027: deadline passed 25 Sep 2026;
Martingale 2027: deadline passed 18 Oct 2026; EUI Jean Monnet 2027: deadline
23 Oct 2026, effectively closed; Chung Hwa Rotary 2027: deadline passed Oct 2026;
African Students 2027: listicle; UChicago Harris 2027: deadline passed 19 Oct 2026;
Global Korea Undergraduate 2027: near-duplicate of published
korean-government-gks-scholarship-2027-korea.html).

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'hansen-2027': {'mono': 'HLI', 'title': 'Hansen Leadership Institute 2027 in USA (Fully Funded)',
   'href': 'hansen-leadership-institute-2027-usa.html',
   'dpill': 'Deadline 15 Jan 2027 \u00b7 84 days left',
   'award': 'International airfare + room and board + all program costs + health insurance assistance for a 3-week summer program at the University of San Diego.',
   'elig': 'Age 20-25 on 1 Jul 2027; completed 1 year of university (or recent graduate); demonstrated leadership outside the classroom; interest in IR/development/diplomacy.',
   'tags': [('Exchange', 'blue'), ('USA', 'teal')]},
 'salzburg-int-2027': {'mono': 'SG', 'title': 'Salzburg Global Internship 2027 in Austria (Fully Funded)',
   'href': 'salzburg-global-internship-2027-austria.html',
   'dpill': 'Deadline 1 Dec 2026 \u00b7 39 days left',
   'award': '3-month on-site internship at Schloss Leopoldskron: round-trip airfare, accommodation, health insurance, visa support, work laptop.',
   'elig': 'Age 18+; all nationalities; undergrads with 3+ years completed, recent graduates (preferred) or graduate students; English proficiency.',
   'tags': [('Internship', 'blue'), ('Austria', 'teal')]},
 'gates-cam-2027': {'mono': 'GC', 'title': 'Gates Cambridge Scholarship 2027-28 in UK (Fully Funded)',
   'href': 'gates-cambridge-scholarship-2027-28-uk.html',
   'dpill': 'Deadline 8 Dec 2026 \u00b7 46 days left',
   'award': '~70 full-cost awards/yr (~55 international): university + college fees, maintenance allowance, return airfare, visa + IHS, discretionary funding.',
   'elig': 'Citizens of any country outside the UK applying to an eligible full-time Cambridge postgraduate course. Not undergrad/part-time.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('UK', 'teal')]},
 'richmond-2027': {'mono': 'UR', 'title': 'University of Richmond Richmond Scholars Program 2027 in USA (Fully Funded)',
   'href': 'richmond-scholars-program-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 \u00b7 39 days left',
   'award': 'Full tuition + housing + food for 8 semesters; ~25 incoming scholars; $5,500 enrichment grant; faculty mentorship; priority registration.',
   'elig': 'First-year undergraduate applicants (US + international); complete admission application by 1 Dec 2026; test-optional for 2027 entry.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'auc-fellow-2027': {'mono': 'AUC', 'title': 'AUC Graduate Fellowships 2027 in Egypt (Fully Funded)',
   'href': 'auc-graduate-fellowships-2027-egypt.html',
   'dpill': 'Spring 2027 deadline 2 Nov 2026 \u00b7 10 days left',
   'award': 'Institutional + sponsored fellowships: tuition (up to 9 credits/semester), stipend, health insurance, housing allowance for full-time internationals.',
   'elig': 'New/continuing degree-seeking AUC graduate students; excellent standing + financial need; 3.2 GPA to retain; excludes diploma/MEng/MComp/non-degree.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Egypt', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Hansen
A.append(dict(
 slug='hansen-leadership-institute-2027-usa',
 title='Hansen Leadership Institute 2027 in USA (Fully Funded)',
 meta='Hansen Leadership Institute 2027: fully funded 3-week summer leadership program at the University of San Diego. International deadline 15 January 2027, eligibility, benefits and how to apply.',
 short='Hansen Leadership Institute 2027', kicker='USA \u00b7 Exchange \u00b7 Fully Funded', mono='HLI',
 prov_short='Fred J. Hansen Foundation', prov_cat='Foundation \u00b7 USA',
 h1='Hansen Leadership Institute 2027 in USA (Fully Funded)',
 sub='Three weeks in San Diego with emerging leaders from around the world: the Fred J. Hansen Foundation covers your airfare, room and board, and every program cost while you train in leadership, mediation and international cooperation.',
 dpill='Deadline 15 Jan 2027 \u00b7 84 days left',
 facts=facts([('Award', 'Fully funded three-week summer program (late June to late July 2027) at the University of San Diego, California. The Fred J. Hansen Foundation covers international airfare, accommodation and meals, all programmatic costs, and health-insurance assistance. Visa documentation support is provided (acceptance letter, financial-support letter, DS-2019 and SEVIS fee receipt). Passport fees and personal spending are not covered.'),
              ('Eligible', 'Aged 20\u201325 on 1 July 2027; completed at least one year of university (upper-division undergraduate) or a recent graduate, with a professional or scholarly interest in international relations, diplomacy, international economic development or a related field; demonstrated leadership potential outside the classroom; English proficiency verified in writing by an academic adviser or professor (no IELTS/TOEFL required); valid international passport; must attend the full program. Preference is given to applicants who have never visited the United States.'),
              ('How', 'Apply online through the official Hansen application portal (hansencenter.org/apply). Create an account, complete every section (academic background, leadership experience, transcripts), and arrange your two references \u2014 one academic reference that verifies your English, and one from an NGO, community or public-service organization you have worked with. Submit before the international deadline.'),
              ('Deadline', '15 January 2027, 11:55 PM Pacific Time for international applicants. 15 March 2027, 11:55 PM Pacific Time for U.S. applicants. Results are expected in early March 2027 (international).'),
              ('Fine print', 'You may submit only one application. Participants cannot arrive late or leave early \u2014 make sure you are available for the complete three-week period. Selection reviews start in February 2027 for international applicants. Some trackers phrase the graduate-student line differently; the foundation\u2019s own eligibility text opens the program to graduate students with a professional interest in the listed fields.')]),
 body='''
      <h2 id="about">About the program</h2>
      <p>The <strong>Hansen Leadership Institute</strong>, funded by the <strong>Fred J. Hansen Foundation</strong>, brings together emerging leaders from the United States and around the world for an intensive three-week summer program at the <strong>University of San Diego, California</strong>. Its stated mission is to promote world peace and international cooperation by training the next generation of leaders in communication, mediation, conflict resolution and cross-cultural understanding.</p>
      <p>The program blends classroom instruction with hands-on workshops, interactive activities and educational field trips. Participants explore leadership topics including conflict resolution, mediation, intercultural dialogue, social entrepreneurship, public speaking and international cooperation \u2014 while living and working with peers from different cultural and national backgrounds. It is a summer leadership program, not a degree: the reward is training, mentorship and an international network, not academic credit.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be <strong>20 to 25 years old on 1 July 2027</strong>.</li>
        <li>Have <strong>completed at least one year of university</strong> \u2014 an upper-division undergraduate, or a graduate student / recent graduate with a professional interest in international relations, diplomacy, international economic development or a related field.</li>
        <li>Show <strong>demonstrated leadership potential outside the classroom</strong> in the community, nation or region.</li>
        <li>Have an <strong>academic adviser or professor verify your English proficiency in writing</strong> \u2014 no IELTS or TOEFL score is required.</li>
        <li>Hold a <strong>valid international passport</strong> (or be able to obtain one before the program starts).</li>
        <li>Be available for the <strong>entire three-week program</strong> \u2014 late arrivals and early departures are not permitted.</li>
        <li>Preference is given to applicants who have <strong>never visited the United States</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>International airfare</strong> to and from San Diego.</li>
        <li><strong>Accommodation and meals</strong> for the full program.</li>
        <li><strong>All programmatic costs</strong> \u2014 training, materials, visits and activities.</li>
        <li><strong>Health-insurance assistance</strong> for the program period.</li>
        <li><strong>Visa documentation support</strong> \u2014 letter of acceptance, letter defining financial support, DS-2019 issued by the University of San Diego, and a receipt for paid SEVIS fees.</li>
        <li>Intensive training in <strong>leadership, communication, public speaking, mediation and conflict resolution</strong>.</li>
        <li>Meetings and networking with <strong>political and business leaders</strong>, plus a certificate of participation.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed online application</strong> \u2014 academic, leadership and personal background, with every section filled.</li>
        <li><strong>Academic transcripts</strong> confirming your completed year(s) of study or graduation.</li>
        <li><strong>Academic reference</strong> \u2014 from a professor or academic adviser who also verifies your English proficiency.</li>
        <li><strong>NGO / community / public-service reference</strong> \u2014 from an organization you have genuinely worked with, speaking to your leadership and service involvement.</li>
        <li><strong>Valid international passport</strong> details.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm you meet every eligibility line</strong>Check your age, education status and availability for the full three weeks before you begin.</li>
        <li><strong>Create an account on the official portal</strong>Go to <strong>hansencenter.org/apply</strong> and register for the 2027 application. You may submit only one application.</li>
        <li><strong>Complete every section</strong>Fill in your academic background, leadership experience and community involvement in full \u2014 incomplete applications are not reviewed by the selection committee.</li>
        <li><strong>Request your two references early</strong>Contact your academic referee (who verifies your English) and your NGO/community referee well ahead of the deadline, because their forms are part of your completed application.</li>
        <li><strong>Submit before the international deadline</strong>All materials, including references, must be in by <strong>15 January 2027, 11:55 PM Pacific Time</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this a degree program?',
  'No. The Hansen Leadership Institute is a three-week summer leadership program \u2014 training in leadership, communication, mediation and international cooperation \u2014 not an academic degree.'),
 ('Do I need IELTS or TOEFL?',
  'No. Instead, an academic adviser or professor must verify your English proficiency in writing as part of your reference.'),
 ('Can graduate students apply?',
  'The foundation\u2019s eligibility text opens the program to graduate students with a professional interest in international relations, diplomacy, international economic development or a related field. Some trackers phrase this differently \u2014 check the current wording on hansencenter.org before you apply.'),
 ('What does \u201cfully funded\u201d actually cover?',
  'International airfare, accommodation and meals, all program costs, health-insurance assistance, and visa documentation support (DS-2019, SEVIS fee receipt). You pay for your passport and personal spending.'),
 ('When will I hear back?',
  'The selection committee begins reviewing international applications in February 2027, and results are expected to be emailed in early March 2027.'),
 ('I have visited the US before. Can I still apply?',
  'Yes \u2014 but preference is given to applicants who have never visited the United States.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: opportunitiesradar.com (Sep 2026) \u2014 deadlines 15 Jan 2027 (international, 11:55 PM PT) and 15 Mar 2027 (US), program late Jun\u2013late Jul 2027, coverage (airfare, accommodation, program costs, training) and exclusions (no visa support claim vs passport/personal expenses), eligibility (20\u201325 on 1 Jul 2027, one year of university completed, full attendance required); globalsouthopportunities.com (23 Oct 2026) \u2014 official site hansencenter.org with apply page hansencenter.org/apply; o4af.com \u2014 official FAQ wording (graduate students with professional interest eligible; English verified by adviser/professor; visa documentation incl. DS-2019 and SEVIS fee receipt; preference to never-visited-US). Queue title \u201cHansen Leadership Exchange Program 2027\u201d retitled to the foundation\u2019s official program name, Hansen Leadership Institute.</p>
''',
 dl_long='Deadline: 15 January 2027 (11:55 PM Pacific Time) for international applicants; 15 March 2027 (11:55 PM PT) for U.S. applicants. Apply early \u2014 your two references must be submitted before the deadline.',
 offlinks=[('Hansen Leadership Institute 2027 \u2014 deadlines, eligibility & official apply page (globalsouthopportunities.com)', 'https://www.globalsouthopportunities.com/2026/10/23/hansen/'),
           ('Hansen Leadership Institute 2027 \u2014 coverage and requirements (opportunitiesradar.com)', 'https://opportunitiesradar.com/hansen-leadership-institute-2027/')],
 related_titles=['echidna-2027', 'yale-wf', 'bsrp-2027'],
))

# ---------------------------------------------------------------- 2. Salzburg
A.append(dict(
 slug='salzburg-global-internship-2027-austria',
 title='Salzburg Global Internship 2027 in Austria (Fully Funded)',
 meta='Salzburg Global Internship 2027: fully funded 3-month internships in Austria at Schloss Leopoldskron \u2014 airfare, accommodation, insurance, visa support, laptop. Deadline 1 December 2026, eligibility and how to apply.',
 short='Salzburg Global Internship 2027', kicker='Austria \u00b7 Internship \u00b7 Fully Funded', mono='SG',
 prov_short='Salzburg Global', prov_cat='Nonprofit \u00b7 Austria',
 h1='Salzburg Global Internship 2027 in Austria (Fully Funded)',
 sub='Work inside a 1947-founded global convening organization \u2014 on site at Schloss Leopoldskron in Salzburg, with your flights, housing, insurance, visa and laptop covered for three months.',
 dpill='Deadline 1 Dec 2026 \u00b7 39 days left',
 facts=facts([('Award', 'Fully funded 3-month internship at Salzburg Global\u2019s headquarters in Salzburg, Austria (on site, not remote). Selected interns receive round-trip airfare to and from Salzburg, free accommodation at Schloss Leopoldskron, health insurance, visa processing assistance and visa costs, airport transfer, and a work laptop with all required software. No application fee.'),
              ('Eligible', 'Open to all nationalities. Applicants must be 18 or older; undergraduates who have completed at least three years of recognized coursework (recent graduates are given preference); students currently enrolled in a graduate program may also apply. Your academic background must be relevant to the position; you need an excellent command of English and proficiency in Microsoft Office (Word, Excel, PowerPoint, Outlook). IELTS is not required.'),
              ('How', 'Apply through Salzburg Global\u2019s official online recruitment platform (see the Our Opportunities page on salzburgglobal.org). Choose the internship track that fits your background \u2014 applications are for specific positions, so apply deliberately rather than to everything. A complete application is a CV/resume plus a tailored cover letter.'),
              ('Deadline', '1 December 2026 for the 2027 internship call.'),
              ('Fine print', 'Five tracks are offered: Communications, Development, Library, Program, and a Hong Kong University internship (only for graduates of Hong Kong universities). Applications are reviewed after the deadline and shortlisted candidates may be interviewed. Because of application volume, Salzburg Global states it cannot respond to questions about individual applications.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p><strong>Salzburg Global</strong> is an independent nonprofit organization, founded in <strong>1947</strong>, that convenes leaders from around the world to work through pressing global challenges. It has brought together more than <strong>40,000 Fellows from 170+ countries</strong> across 1,100+ sessions. Its internship program places students and recent graduates inside the organization\u2019s international team at <strong>Schloss Leopoldskron in Salzburg, Austria</strong>, for three months of professional work experience in an international nonprofit environment.</p>
      <p>The 2027 call offers <strong>five internship tracks</strong>: Communications (for journalism, communications, PR, digital marketing backgrounds), Development (nonprofit management and fundraising), Library (graduate students in library/information science \u2014 archival work and oversight of the organization\u2019s private collection), Program (interest in Salzburg Global\u2019s program areas), and a Hong Kong University internship reserved for graduates of Hong Kong universities.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>all nationalities</strong> \u2014 you must be <strong>18 or older</strong> at the time of application.</li>
        <li><strong>Undergraduates</strong> who have finished <strong>at least three years</strong> of recognized coursework; <strong>recent graduates are given preference</strong>.</li>
        <li>Students <strong>currently enrolled in a graduate program</strong> may also apply.</li>
        <li>Your <strong>academic background must be relevant</strong> to the internship position you choose.</li>
        <li><strong>Excellent command of English</strong>, spoken and written (IELTS is not required).</li>
        <li>Proficiency in <strong>Microsoft Office</strong> (Word, Excel, PowerPoint, Outlook).</li>
        <li>Able to work in a <strong>professionally diverse, multicultural environment</strong> \u2014 and able to complete the internship <strong>on site in Salzburg</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Round-trip airfare</strong> to and from Salzburg.</li>
        <li><strong>Free accommodation</strong> at Schloss Leopoldskron, plus airport transfer.</li>
        <li><strong>Health insurance</strong> for the internship period.</li>
        <li><strong>Visa processing assistance and visa costs</strong> (the Internship Program Manager helps with your visa once you accept an offer).</li>
        <li>A <strong>work laptop with all required software</strong>.</li>
        <li>No application fee; professional experience inside an internationally respected organization and a global peer network.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV / resume</strong> \u2014 concise, highlighting education and relevant experience.</li>
        <li><strong>Tailored cover letter</strong> \u2014 explain why you want to work for Salzburg Global and why you fit the specific internship (a one-page letter for the Library track).</li>
        <li>Apply <strong>per position</strong> \u2014 select your track(s) carefully on the official recruitment platform.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick your track</strong>Read the five 2027 internship descriptions (Communications, Development, Library, Program, Hong Kong University) and choose the one that matches your background.</li>
        <li><strong>Go to the official opportunities page</strong>Find the 2027 internship vacancies on <strong>salzburgglobal.org \u2014 Our Opportunities</strong> and open the vacancy for your track.</li>
        <li><strong>Prepare your CV and cover letter</strong>Tailor the cover letter to the track: relevant coursework, volunteer or research experience, and why Salzburg Global\u2019s mission interests you.</li>
        <li><strong>Submit on the official recruitment platform</strong>Complete the online form and upload your documents. There is no application fee.</li>
        <li><strong>Apply by 1 December 2026</strong>Applications are reviewed after the deadline; shortlisted candidates may be invited to an interview call, and all applicants are informed of the outcome.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is IELTS required?',
  'No. IELTS is explicitly not required for this internship; what matters is a strong command of English.'),
 ('Can I do the internship remotely?',
  'No. All internships are on site and must be completed in Salzburg, Austria.'),
 ('I am not an EU citizen. Will I get visa help?',
  'Yes. Salzburg Global provides visa processing assistance and covers visa costs; the Internship Program Manager helps you apply for the visa once you accept the offer.'),
 ('Which track is the Hong Kong University internship?',
  'It is a separate track reserved for students who are currently enrolled in, or have graduated from, a Hong Kong university.'),
 ('Is there an application fee?',
  'No. The application is completely free.'),
 ('When are results announced?',
  'Applications are reviewed after the 1 December 2026 deadline; shortlisted candidates may be interviewed in the new year, and every applicant is informed of the outcome.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: opportunitiesradar.com (Sep 2026) \u2014 2027 call open, deadline 1 Dec 2026, 3-month duration, 5 positions, coverage (accommodation at Schloss Leopoldskron, round-trip airfare, health insurance, visa assistance + costs), eligibility (18+, all nationalities, bachelor\u2019s/master\u2019s enrolled or recently graduated, relevant background, English, MS Office); salzburgglobal.org/about-us/our-opportunities (official opportunities page, crawled 22 h ago); fellowshipsguide.com \u2014 deadline 1 Dec 2026, free application, visa support for non-EU citizens, laptop provided. Queue title \u201cSalzburg Global Seminar Internship 2027\u201d retitled to the organization\u2019s internship branding.</p>
''',
 dl_long='Deadline: 1 December 2026 for the 2027 internship call. Apply through Salzburg Global\u2019s official recruitment platform with your CV and a tailored cover letter.',
 offlinks=[('Salzburg Global \u2014 Our Opportunities (official vacancies page)', 'https://www.salzburgglobal.org/about-us/our-opportunities'),
           ('Salzburg Global Internship 2027 \u2014 positions & coverage (opportunitiesradar.com)', 'https://opportunitiesradar.com/salzburg-global-internship-2027/')],
 related_titles=['webster2027', 'faspe-2027', 'epfl-summer'],
))

# ---------------------------------------------------------------- 3. Gates Cambridge
A.append(dict(
 slug='gates-cambridge-scholarship-2027-28-uk',
 title='Gates Cambridge Scholarship 2027-28 in UK (Fully Funded)',
 meta='Gates Cambridge Scholarship 2027-28: full-cost postgraduate scholarships at the University of Cambridge. International deadline 8 December 2026, eligibility, funding and how to apply.',
 short='Gates Cambridge 2027-28', kicker='UK \u00b7 Postgraduate \u00b7 Fully Funded', mono='GC',
 prov_short='Gates Cambridge Trust', prov_cat='Trust \u00b7 University of Cambridge',
 h1='Gates Cambridge Scholarship 2027-28 in UK (Fully Funded)',
 sub='One of the world\u2019s most competitive postgraduate awards: about 70 full-cost scholarships a year for non-UK citizens to study at Cambridge \u2014 fees, living costs, airfare, visa and health surcharge covered.',
 dpill='Deadline 8 Dec 2026 \u00b7 46 days left',
 facts=facts([('Award', 'A full-cost scholarship: the University composition fee and College fees at the appropriate rate, a maintenance allowance for a single student (indicative \u00a323,152 for 12 months at 2026-27 rates, pro rata for shorter courses), one economy single airfare to the UK at the start and one back at the end, visa costs and the Immigration Health Surcharge. Discretionary funding is available for academic development (conferences, courses) and a dependants allowance where applicable. Around 70 scholarships are awarded each year, roughly 55 in the international round, with about two-thirds going to PhD students.'),
              ('Eligible', 'A citizen of any country outside the United Kingdom; applying for admission to an eligible full-time postgraduate degree at the University of Cambridge (PhD, MSc, MLitt, or eligible one-year courses such as MPhil). Undergraduate degrees, part-time courses, non-degree courses and some specific courses are not eligible \u2014 check your course in Cambridge\u2019s Course Directory. Selection is on four criteria: outstanding intellectual ability, reasons for choice of course, a commitment to improving the lives of others, and leadership potential.'),
              ('How', 'There is no separate Gates Cambridge form: you apply through the University of Cambridge Graduate Application Portal for admission, a College place and funding in one application. Complete the Gates Cambridge funding section \u2014 a Gates Cambridge statement (~500 words), written answers to the selection-criteria questions, and the details of your Gates Cambridge referee (in addition to your two standard academic references). PhD applicants add a research proposal where the course requires one, plus a CV. Every document and reference must arrive before your course\u2019s funding deadline.'),
              ('Deadline', 'International round: 8 December 2026 or 6 January 2027, depending on your course\u2019s funding deadline (11:59 pm UK time). The U.S. round (U.S. citizens normally resident in the USA) closed on 14 October 2026. Applications for 2027-28 entry opened 11 September 2026.'),
              ('Fine print', 'Your deadline is the \u201ccourse funding deadline\u201d shown on your specific course page \u2014 never assume one date fits every course. Referees must submit by the same deadline; late references can sink an application. A previous unsuccessful Gates Cambridge application does not affect future consideration. The Trust continues to pilot funding for a part-time doctoral degree. The scholarship was established in 2000 through a donation from the Bill & Melinda Gates Foundation.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Gates Cambridge Scholarship</strong> was established in <strong>2000</strong> through a donation from the <strong>Bill &amp; Melinda Gates Foundation</strong> to the University of Cambridge. It is one of the world\u2019s most prestigious international postgraduate scholarships, awarded each year to outstanding applicants from outside the UK who show the potential to become leaders committed to improving the lives of others.</p>
      <p>Each year the Trust offers around <strong>70 full-cost scholarships</strong> in any subject available at Cambridge, with roughly <strong>55 in the international round</strong> and about two-thirds of all awards going to <strong>PhD students</strong>. Selection rests on four criteria: <strong>outstanding intellectual ability</strong>, <strong>reasons for choice of course</strong>, a <strong>commitment to improving the lives of others</strong>, and <strong>leadership potential</strong>. There is no separate scholarship application \u2014 the Gates Cambridge section lives inside your Cambridge postgraduate application.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>citizen of any country outside the United Kingdom</strong> (including India).</li>
        <li>Apply for an <strong>eligible full-time postgraduate degree</strong> at the University of Cambridge: PhD (full-time or the part-time pilot), MSc, MLitt, or eligible one-year postgraduate courses (e.g. MPhil, LLM).</li>
        <li><strong>Not eligible:</strong> undergraduate degrees, part-time courses (except the PhD pilot), non-degree courses, and some specific courses such as the MBA and MFin \u2014 confirm in the Course Directory.</li>
        <li>Meet the <strong>academic and admission criteria</strong> of your chosen Cambridge course \u2014 the Trust does not admit students; the University does.</li>
        <li>Demonstrate the four selection criteria: intellectual ability, a credible reason for choosing the course, commitment to improving lives, and leadership potential.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>University composition fee and College fees</strong> covered in full.</li>
        <li><strong>Maintenance allowance</strong> for a single student (indicative \u00a323,152 for 12 months at 2026-27 rates; pro rata for shorter courses).</li>
        <li><strong>One economy single airfare</strong> to the UK at the start of the course and one back at the end.</li>
        <li><strong>Visa costs and the Immigration Health Surcharge</strong> covered.</li>
        <li><strong>Discretionary funding</strong>: academic development funding (conferences, courses) and a dependants allowance where applicable.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Cambridge Graduate Application</strong> with the Gates Cambridge funding section completed.</li>
        <li><strong>Gates Cambridge statement</strong> (~500 words on why you are applying and how you meet the four criteria) plus written answers to the selection-criteria questions.</li>
        <li><strong>Gates Cambridge reference</strong> \u2014 separate from your <strong>two standard academic references</strong>; it should speak specifically to your fit with the scholarship.</li>
        <li><strong>CV / resume</strong> and all course-specific documents (transcripts, written work, English-language evidence).</li>
        <li><strong>Research proposal</strong> for PhD applicants, where the course requires one.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose an eligible course</strong>Use the Cambridge Postgraduate Course Directory to pick your programme and note its exact <strong>course funding deadline</strong> \u2014 8 December 2026 or 6 January 2027.</li>
        <li><strong>Start the Cambridge application</strong>Apply through the official University of Cambridge Applicant Portal for admission, a College place and funding together.</li>
        <li><strong>Complete the Gates Cambridge section</strong>In the funding section, opt into the Gates Cambridge Scholarship; write your statement and answers to the criteria questions.</li>
        <li><strong>Line up three referees early</strong>Two academic references for admission plus your Gates Cambridge reference \u2014 all must submit by the same funding deadline, and referees are the part of the application you cannot control.</li>
        <li><strong>Upload everything and submit</strong>Transcripts, CV, research proposal (PhD), English evidence \u2014 submit the complete application before 11:59 pm UK time on your course\u2019s funding deadline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate Gates Cambridge application?',
  'No. You apply once through the Cambridge Graduate Application Portal; the Gates Cambridge section (statement, criteria questions, Gates reference) is part of that application.'),
 ('I am a U.S. citizen living in the USA. What is my deadline?',
  'The U.S. round deadline was 14 October 2026. If you missed it, you cannot be considered for 2027-28 entry.'),
 ('Which deadline applies to me \u2014 8 December or 6 January?',
  'Whichever is the \u201ccourse funding deadline\u201d shown on your specific course\u2019s page in the Cambridge Course Directory. Check the course, not the rumor.'),
 ('Does it cover undergraduate study?',
  'No. Gates Cambridge funds postgraduate study only \u2014 not undergraduate, part-time (except the PhD pilot), or non-degree courses.'),
 ('I applied before and was rejected. Can I try again?',
  'Yes. A previous unsuccessful application does not affect future consideration.'),
 ('How many scholarships are awarded?',
  'Around 70 full-cost scholarships per year, with roughly 55 in the international round and about two-thirds going to PhD students.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: opportunitystation.com (2027-28 guide) \u2014 applications opened 11 Sep 2026, US round 14 Oct 2026, international round 8 Dec 2026 / 6 Jan 2027 course-dependent, ~70 full-cost awards (~2/3 PhD), selection on intellectual ability / course fit / commitment to improving lives / leadership; scholarhunter.com (verified 30 Sep 2026 against gatescambridge.org) \u2014 official how-to-apply and timeline pages, Cambridge Applicant Portal route, referees by the same deadline; pontly.africa \u2014 coverage (composition + college fees, maintenance, airfare, visa + IHS, discretionary funding), eligibility (non-UK citizens; eligible full-time postgraduate; MBA/MFin excluded). Queue deadline \u201c8 December 2026\u201d confirmed as the main international date.</p>
''',
 dl_long='Deadline: 8 December 2026 or 6 January 2027 depending on your course\u2019s funding deadline (11:59 pm UK time). The U.S. round closed 14 October 2026. Every reference must arrive by the same deadline.',
 offlinks=[('Gates Cambridge \u2014 how to apply (official, gatescambridge.org)', 'https://www.gatescambridge.org/apply/how-to-apply/'),
           ('Gates Cambridge \u2014 application timeline 2027/28 (official, gatescambridge.org)', 'https://www.gatescambridge.org/apply/timeline/'),
           ('Gates Cambridge Scholarships 2027-2028 \u2014 full guide (opportunitystation.com)', 'https://www.opportunitystation.com/opportunities/gates-cambridge-scholarships-2027-2028')],
 related_titles=['weidenfeld-hoffmann-2027', 'clarendon', 'warwick-2027'],
))

# ---------------------------------------------------------------- 4. Richmond
A.append(dict(
 slug='richmond-scholars-program-2027-usa',
 title='University of Richmond Richmond Scholars Program 2027 in USA (Fully Funded)',
 meta='Richmond Scholars Program 2027: the University of Richmond\u2019s top merit award \u2014 full tuition, housing and food for ~25 incoming undergraduates. Deadline 1 December 2026, eligibility and how to apply.',
 short='Richmond Scholars 2027', kicker='USA \u00b7 Undergraduate \u00b7 Fully Funded', mono='UR',
 prov_short='University of Richmond', prov_cat='University \u00b7 USA',
 h1='University of Richmond Richmond Scholars Program 2027 in USA (Fully Funded)',
 sub='Richmond\u2019s most prestigious merit award: full tuition plus housing and food for four years \u2014 and there is no separate application. Your admission file, on time, is your scholarship application.',
 dpill='Deadline 1 Dec 2026 \u00b7 39 days left',
 facts=facts([('Award', 'The Richmond Scholars Program is the University of Richmond\u2019s top academic merit award: full undergraduate tuition plus university housing and food, renewable for up to eight consecutive semesters of full-time enrollment. About 25 incoming first-year students receive it each year. Scholars also get a one-time enrichment grant of up to $5,500 for faculty-mentored activities (study abroad, research, unpaid internships), priority course registration, guaranteed on-campus housing, dedicated faculty mentorship, cultural event vouchers and specialized scholar advising.'),
              ('Eligible', 'First-year undergraduate applicants \u2014 U.S. and international students are both eligible. For 2027 entry Richmond is test-optional (SAT/ACT not required). Selection is on four criteria: academic achievement, engaged leadership, a strong sense of purpose, and interest in a diverse and inclusive community. Note: admission for international applicants is need-aware, but non-U.S. citizens are fully eligible for this merit award.'),
              ('How', 'There is no separate Richmond Scholars application. Submit a complete University of Richmond first-year admission application \u2014 via the Common Application or the Coalition Application (Scoir), with the Richmond supplemental questions, transcript, school report, recommendation and English-proficiency evidence where required \u2014 by 1 December 2026, and you are automatically considered. Finalists are notified through the Spider Portal by February 1 and interviewed by a faculty selection committee over Zoom in mid-February; final selections are completed by March 1.'),
              ('Deadline', '1 December 2026 \u2014 your complete admission application must be on file by this date for Richmond Scholars consideration. (Regular Decision closes 1 January 2027, but that is too late for the scholarship.)'),
              ('Fine print', 'The award is merit-based and renewable for eight semesters, subject to the university\u2019s requirements. Airfare, visa costs, health insurance, books and personal expenses are not covered. Reaching the interview stage does not guarantee admission or the scholarship.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Richmond Scholars Program</strong> is the <strong>University of Richmond\u2019s most prestigious merit award</strong>, offered to approximately <strong>25 incoming first-year students</strong> each year. It is designed to attract high-achieving students defined by academic success, leadership, purpose and commitment to diversity \u2014 and it covers the three biggest costs of a U.S. undergraduate degree: <strong>tuition, housing and food</strong>, for the full four years.</p>
      <p>What makes this award unusually simple is the application: <strong>there is no separate scholarship form</strong>. Every first-year applicant whose complete admission application is on file by <strong>December 1</strong> is automatically considered. The admission application \u2014 your grades, essays, activities and recommendations \u2014 is the entire scholarship application.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>first-year undergraduate applicant</strong> to the University of Richmond (not a transfer or postgraduate applicant).</li>
        <li><strong>U.S. and international students</strong> are both eligible \u2014 non-U.S. citizens can be considered for this merit-based award.</li>
        <li>Submit a <strong>complete admission application by 1 December 2026</strong>.</li>
        <li><strong>SAT/ACT scores are optional</strong> for students entering in 2027 (Richmond is test-optional).</li>
        <li>International applicants must meet general admission requirements, including <strong>English-language proficiency</strong> (IELTS, TOEFL, Duolingo, or a waiver where it applies) and financial certification.</li>
        <li>Selection looks at <strong>academic achievement, engaged leadership, a strong sense of purpose, and interest in a diverse and inclusive community</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full undergraduate tuition</strong> for up to eight consecutive semesters.</li>
        <li><strong>University housing and food</strong> (on-campus accommodation and meal plan).</li>
        <li><strong>One-time enrichment grant of up to $5,500</strong> for a faculty-mentored activity such as study abroad, research or an unpaid internship.</li>
        <li><strong>Priority course registration</strong> and guaranteed on-campus housing.</li>
        <li><strong>Dedicated faculty mentorship</strong>, cultural event vouchers and specialized scholar advising.</li>
        <li>Membership in a small, multidisciplinary scholars\u2019 community with dedicated programming.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Complete first-year admission application</strong> via the Common Application or the Coalition Application (Scoir), including the <strong>Richmond supplemental questions</strong>.</li>
        <li><strong>High school transcript</strong> (grades 9\u201311), <strong>school report</strong>, senior progress grades, and <strong>at least one recommendation</strong> from a school official.</li>
        <li>Activities and achievements record.</li>
        <li><strong>English-proficiency evidence</strong> where the university requires it.</li>
        <li>Optional: SAT/ACT scores (not required for 2027 entry), arts portfolios where eligible.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start your Richmond application</strong>Create an account on the Common Application or the Coalition Application (Scoir) and select the University of Richmond.</li>
        <li><strong>Complete the Richmond supplement</strong>Answer the university\u2019s supplemental questions thoughtfully \u2014 this is where leadership, purpose and community engagement show.</li>
        <li><strong>Arrange your documents early</strong>Transcript, school report, recommendation and English evidence all take time; your counselor needs a head start too.</li>
        <li><strong>Submit everything by 1 December 2026</strong>Your complete admission application must be on file by this date \u2014 this is what puts you in the Richmond Scholars pool. No separate scholarship form exists.</li>
        <li><strong>Watch the Spider Portal</strong>Finalists are notified by February 1 and interviewed by a faculty committee over Zoom in mid-February; final selections are completed by March 1.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a separate Richmond Scholars application?',
  'No. Students who submit a complete University of Richmond admission application by 1 December 2026 are automatically considered for the Richmond Scholars Program.'),
 ('Can international students win it?',
  'Yes. Non-U.S. citizens are fully eligible for this merit-based award. Note that Richmond\u2019s admission process is need-aware for international applicants, which is separate from the merit decision.'),
 ('How many scholarships are awarded?',
  'Approximately 25 incoming first-year students each year.'),
 ('Are SAT or ACT scores required?',
  'No. For students entering in Fall 2027, the University of Richmond is test-optional \u2014 scores are not required for Richmond Scholars consideration.'),
 ('Is there an interview?',
  'Yes, for finalists. Applicants who advance are notified through the Spider Portal by February 1 and interviewed by a faculty selection committee over Zoom in mid-February.'),
 ('Does it cover everything?',
  'It covers full tuition, housing and food for eight semesters, plus the enrichment grant. Airfare, U.S. student-visa costs, health insurance, books and personal spending are not covered.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: opportunities247.org \u2014 deadline 1 Dec 2026, full tuition + housing + food, ~25 scholars, automatic consideration, 4 selection criteria, Zoom interviews mid-Feb; daadscholarship.com (checked 14 Sep 2026) \u2014 no separate application, Common/Coalition via Scoir, enrichment grant $5,500, finalists notified by Feb 1 via Spider Portal, final selection by Mar 1, RD 1 Jan 2027 vs scholarship deadline 1 Dec 2026; pontly.africa \u2014 international eligibility with need-aware admission context, test-optional for 2027. Queue deadline \u201cDecember 2026\u201d confirmed as 1 December 2026.</p>
''',
 dl_long='Deadline: 1 December 2026 \u2014 your complete University of Richmond admission application must be on file by this date. There is no separate scholarship application; Regular Decision (1 January 2027) is too late for Richmond Scholars.',
 offlinks=[('Richmond Scholars Program 2027 \u2014 how to submit (daadscholarship.com)', 'https://daadscholarship.com/richmond-usa-fully-funded-scholarships-2027-here-is-how-to-submit-application/'),
           ('Richmond Scholars Program 2027 \u2014 FAQs & timeline (opportunities247.org)', 'https://opportunities247.org/richmond-scholars-program-2027/')],
 related_titles=['dayton-merit', 'uchicago', 'bu-trustee'],
))

# ---------------------------------------------------------------- 5. AUC
A.append(dict(
 slug='auc-graduate-fellowships-2027-egypt',
 title='AUC Graduate Fellowships 2027 in Egypt (Fully Funded)',
 meta='AUC Graduate Fellowships 2027: institutional and sponsored fellowships at the American University in Cairo. Spring 2027 deadline 2 November 2026, eligibility, funding and how to apply.',
 short='AUC Graduate Fellowships 2027', kicker='Egypt \u00b7 Master\u2019s/PhD \u00b7 Fully Funded', mono='AUC',
 prov_short='The American University in Cairo', prov_cat='University \u00b7 Egypt',
 h1='AUC Graduate Fellowships 2027 in Egypt (Fully Funded)',
 sub='Graduate study in Cairo with tuition, stipend, housing and insurance support: AUC runs three fellowship application windows for 2027, and the Spring 2027 window closes 2 November 2026.',
 dpill='Spring 2027 deadline 2 Nov 2026 \u00b7 10 days left',
 facts=facts([('Award', 'Two categories of fellowships: institutional (funded by the university) and sponsored (donor/endowed). Coverage varies by award \u2014 typically tuition for up to nine credits per semester plus activity fees, a stipend, health insurance and medical services, and a monthly housing allowance or accommodation in AUC residences at the New Cairo campus for full-time international students. Awards are competitive and recognize academic merit alongside financial need.'),
              ('Eligible', 'New and continuing degree-seeking graduate students at AUC. Excellent academic standing and full admission receive priority; financial need is considered; full-time study is preferred (sponsored fellowships require full-time status). Continuing students generally need a minimum 3.2 GPA to retain funding. Excluded from institutional fellowships: graduate diploma students, Master of Engineering and Master in Computing students, non-degree students, and applicants admitted subject to prerequisite undergraduate courses.'),
              ('How', 'First submit the online AUC graduate admission application. Allow about five to seven working days for the system to generate your student ID, then complete the separate fellowship application through Banner Self-Service (you may apply for up to three fellowships in one application, but only one can be awarded). Submit your admission application at least two weeks before the fellowship deadline \u2014 you do not need to wait for the admission decision before applying for the fellowship.'),
              ('Deadline', 'Spring 2027: applications open 7 October 2026, deadline 2 November 2026. Fall 2027 Cycle 1: 22 December 2026 \u2013 17 January 2027. Fall 2027 Cycle 2: 6 April 2027 \u2013 6 May 2027.'),
              ('Fine print', 'Coverage and conditions differ between individual fellowship listings \u2014 always read the specific award\u2019s page. Some fellowships carry responsibilities such as teaching or research assistantship duties (around 12 hours per week) with mandatory training. Receiving admission does not guarantee fellowship funding.')]),
 body='''
      <h2 id="about">About the fellowships</h2>
      <p>The <strong>American University in Cairo (AUC)</strong> offers graduate fellowships in two categories: <strong>institutional fellowships</strong>, funded by the university itself, and <strong>sponsored fellowships</strong>, funded through private endowments and donors. Some are discipline-specific; others are based on the student\u2019s country or region of origin. Together they form one of the most generous graduate funding routes in the Middle East and Africa, aimed at outstanding students who also demonstrate financial need.</p>
      <p>Fellowships are <strong>highly competitive</strong> and open to both new and continuing graduate students, depending on the funds allocated to each award. AUC runs <strong>three application windows for 2027</strong> \u2014 Spring 2027, and two Fall 2027 cycles \u2014 so check which window matches your intended intake.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>new or continuing degree-seeking graduate student</strong> at AUC, fully admitted and meeting graduate admission requirements.</li>
        <li>Show <strong>excellent academic standing</strong>; financial need is also considered.</li>
        <li>Pursue <strong>full-time study</strong> where possible \u2014 preference goes to full-time students, and sponsored fellowships require full-time status.</li>
        <li><strong>Continuing students</strong> generally need a minimum <strong>3.2 GPA</strong> to retain fellowship funding.</li>
        <li><strong>Excluded from institutional fellowships:</strong> graduate diploma students, Master of Engineering and Master in Computing students, non-degree students, and applicants admitted subject to prerequisite undergraduate courses.</li>
        <li>Hold a recognized <strong>bachelor\u2019s degree</strong>; credentials must be in English or accompanied by an official translation.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition coverage</strong> \u2014 typically full tuition for up to nine credits per semester (varies by award).</li>
        <li><strong>Activity and student-services fees</strong> covered.</li>
        <li><strong>Monthly stipend</strong> and <strong>health insurance / medical services</strong>.</li>
        <li><strong>Housing allowance or AUC residence accommodation</strong> at the New Cairo campus for full-time international students.</li>
        <li>Remedial English-language requirements covered where applicable.</li>
        <li>Note: coverage is <strong>not identical across awards</strong> \u2014 institutional and sponsored fellowships each set their own terms.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>AUC graduate admission application</strong> with all academic records, in English or officially translated.</li>
        <li><strong>Student ID</strong> (generated ~5\u20137 working days after the admission application) to access Banner Self-Service.</li>
        <li><strong>Separate online fellowship application</strong> \u2014 up to three fellowships per application.</li>
        <li>Program-specific documents per the individual fellowship listing (personal statement, evidence of financial need, etc.).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your AUC graduate program</strong>Check the admission requirements of your department \u2014 some set higher bars than the university minimum.</li>
        <li><strong>Submit the graduate admission application</strong>Do this at least <strong>two weeks before the fellowship deadline</strong> (for the 2 November 2026 deadline, aim for 19 October 2026 or earlier).</li>
        <li><strong>Wait for your student ID</strong>Allow about five to seven working days after the admission application for the system to generate your ID and activate Banner Self-Service.</li>
        <li><strong>Complete the fellowship application</strong>Log into Banner Self-Service and submit the online fellowship application \u2014 you may list up to three fellowships, but only one can be awarded. You do not need your admission decision first.</li>
        <li><strong>Meet the window deadline</strong>Spring 2027: <strong>2 November 2026</strong>. Fall 2027: <strong>17 January 2027</strong> (Cycle 1) or <strong>6 May 2027</strong> (Cycle 2).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How many fellowships can I apply for?',
  'You can list up to three fellowships in the fellowship application, but you can only be awarded one.'),
 ('Do I need to be admitted before applying for the fellowship?',
  'No. You should not wait for the admission decision \u2014 but you must submit the admission application first (at least two weeks before the fellowship deadline) so your student ID is generated.'),
 ('Are the fellowships open to international students?',
  'Yes. New and continuing degree-seeking graduate students compete for fellowships, and full-time international students receiving fellowship support may be eligible for a housing allowance.'),
 ('What GPA do I need to keep the fellowship?',
  'Continuing students generally need to maintain at least a 3.2 GPA; individual awards may set higher bars.'),
 ('Do fellows have work duties?',
  'Some do. Certain fellowships include around 12 hours per week of related academic or teaching-assistantship work, with mandatory training where teaching duties apply.'),
 ('Is there an application fee?',
  'Check the provider details for the current cycle; the published fellowship guides do not list a universal fee.'),
]) + '''
      <p class="verify">Verified 23 Oct 2026: aucegypt.edu Graduate Studies FAQ (official) \u2014 institutional vs sponsored categories, competitive awards, financial need considered, full-time preference, admission application before fellowship application (~5 working days for student ID), up to 3 fellowships per application; primescholarshipalerts.com (recorded source check 11 Oct 2026) \u2014 Spring 2027 window 7 Oct\u20132 Nov 2026, coverage varies by award, exclusions (diploma, MEng, MComp, non-degree), 3.2 GPA retention, admission app at least 2 weeks before deadline; lanternpost.org + scholarships.af + globalsouthopportunities.com \u2014 Fall 2027 Cycle 1: 22 Dec 2026\u201317 Jan 2027; Cycle 2: 6 Apr\u20136 May 2027. Queue deadline \u201c2 November 2026\u201d confirmed.</p>
''',
 dl_long='Deadline: Spring 2027 fellowship applications close 2 November 2026 (apply from 7 October 2026). Fall 2027: Cycle 1 runs 22 December 2026 \u2013 17 January 2027; Cycle 2 runs 6 April \u2013 6 May 2027. Submit your graduate admission application at least two weeks before the fellowship deadline.',
 offlinks=[('AUC Graduate Studies \u2014 fellowships FAQ (official, aucegypt.edu)', 'https://www.aucegypt.edu/academics/graduate-studies/frequently-asked-questions'),
           ('AUC Graduate Fellowships \u2014 Spring 2027 call details (primescholarshipalerts.com)', 'https://primescholarshipalerts.com/scholarships/american-university-in-cairo-graduate-fellowships-spring-2027')],
 related_titles=['nias-safehaven', 'mopga', 'bevisioneers2027'],
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
    class P(html.parser.HTMLParser):
        def error(self, m): raise ValueError(m)
        def __init__(self):
            super().__init__(); self.errs = []
    bad = []
    for slug, _ in built:
        t = OUT.joinpath(slug + '.html').read_text()
        for token in ('AICTE Pragati', 'Lorem', '{{', 'data:image'):
            if token in t: bad.append((slug, 'template leftover / forbidden token: ' + token))
        for mm in re.finditer(r'href=["\']#["\']', t):
            bad.append((slug, 'suspicious placeholder: ' + mm.group(0)))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

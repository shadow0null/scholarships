#!/usr/bin/env python3
"""Batch 22 (cron run 22, 19 Oct 2026): 5 verified articles.
All prose original. Verification completed the morning of 19 Oct 2026.

1. HZDR Summer Student Program 2027 (Germany). 2027 call OFFICIALLY ANNOUNCED on
   hzdr.de: applications 2 Nov 2026 -> 24 Jan 2027, decisions by end Mar 2027.
   Programme Jul-Sep 2027, 6-9 weeks (established format). Eligibility from the
   2027 page: enrolled undergrad/master's, >=3 years of study by 30 Sep 2027
   (started by Oct 2024), continue studies after summer 2027, no prior HZDR
   contract/stipend, PhD excluded. Benefits from the 2026 call (2027 rates not
   yet published - flagged): daily grant (EUR 36/day in 2026), free
   accommodation, insurance, local transport; airfare/visa not covered.
2. Brunei Darussalam Government Scholarship 2027/28. NOT YET ANNOUNCED (MFA
   portal shows call closed; last round 15 Dec 2025 - 15 Feb 2026). MoE published
   the 2027/28 course list 18 Oct 2026 (Borneo Bulletin); trackers expect the
   call mid-Dec 2026 - mid-Feb 2027. Package, age limits (18-25 UG / <=35
   master's as of 1 July), language thresholds (IELTS 6.0 / TOEFL 550), 5
   institutions (UBD, UNISSA, UTB, KUPU SB, Politeknik Brunei) and the UBD/UTB
   dual-application rule are from the 2026/27 call - flagged as to-be-confirmed.
3. UTRIP Summer Internship 2027 (Japan). 2027 call not yet open - official FAQ
   (s.u-tokyo.ac.jp) confirms applications open November 2026; trackers publish
   a 7 Jan 2027 deadline and 25 Jun - 5 Aug 2027 dates (flagged as
   tracker-published, not yet year-dated officially). Eligibility: overseas
   undergrads in natural sciences, >=1 year of bachelor's, return to UG study
   after. No programme/accommodation fees (official); accommodation + financial
   support under standing terms.
4. Queen Elizabeth Commonwealth Scholarships 2027-28 Cycle 1. Run by ACU; cycle
   1 dates 18 Nov 2026 - 13 Jan 2027 published on the ACU funding opportunities
   calendar (via 3+ trackers); official ACU page confirms the two-cycle
   structure and benefits (full tuition, stipend, return flights, arrival
   allowance, research support grant on request). 2:1 bachelor's, Commonwealth
   citizen, study outside home country, no age limit. IELTS NOT claimed - host
   university rules apply.
5. UNU Junior Fellows Internship Spring 2027 (Tokyo). OPEN NOW - deadline
   1 Nov 2026 23:59 JST. 1 Mar - 27 Aug 2027, Office of the Rector, Tokyo.
   Master's/PhD students or recent graduates aged <=32, <=5 yrs experience, all
   nationalities. Monthly stipend for interns without other funding (amount not
   published); 1.5 days leave/month. Verified across 7 consistent trackers;
   apply on the official UNU careers portal (Spring 2027 vacancy).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'hzdr-2027': dict(mono='H', title='HZDR Summer Student Program 2027 (Germany)', href='hzdr-summer-student-program-2027-germany.html',
              dpill='Opens 2 Nov 2026', award='Daily grant + free accommodation', elig='Undergrad/Master\u2019s; 3+ yrs study by Sep 2027; no PhD.',
              tags=[('Internship','blue'),('International','teal')]),
 'brunei-2027-28': dict(mono='B', title='Brunei Darussalam Government Scholarship 2027/28', href='brunei-darussalam-government-scholarship-2027-28.html',
              dpill='Expected Dec 2026', award='Fully funded (tuition + monthly allowance)', elig='Diploma/UG/Master\u2019s; all nationalities; age limits apply.',
              tags=[('Government','blue'),('International','teal')]),
 'utrip-2027': dict(mono='UT', title='UTRIP Summer Internship 2027 (Japan)', href='utrip-summer-internship-2027-japan.html',
              dpill='Opens Nov 2026', award='Accommodation + financial support', elig='Overseas undergrads, natural sciences; GPA 3.0+.',
              tags=[('Internship','blue'),('International','teal')]),
 'qecs-2027-28': dict(mono='QE', title='Queen Elizabeth Commonwealth Scholarships 2027-28', href='queen-elizabeth-commonwealth-scholarships-2027-28.html',
              dpill='Opens 18 Nov 2026', award='Fully funded 2-yr master\u2019s + flights', elig='Commonwealth citizens; 2:1 bachelor\u2019s; no age limit.',
              tags=[('Government','blue'),('International','teal')]),
 'unu-junior-fellows-2027': dict(mono='UN', title='UNU Junior Fellows Internship Spring 2027 (Tokyo)', href='unu-junior-fellows-internship-spring-2027.html',
              dpill='13 days to go', award='Monthly stipend (means-tested)', elig='Master\u2019s/PhD students or recent grads; \u226432 yrs.',
              tags=[('Internship','blue'),('International','teal')]),
})

ARTICLES = [
dict(
 slug='hzdr-summer-student-program-2027-germany',
 title='HZDR Summer Student Program 2027, Germany | StudyDesk Scholarships',
 meta='HZDR Summer Student Program 2027: applications 2 Nov 2026 \u2013 24 Jan 2027. Six to nine weeks of research at the Helmholtz-Zentrum Dresden-Rossendorf with a daily grant, accommodation and insurance. Eligibility and how to apply.',
 short='HZDR Summer Student Program', kicker='Research Internship \u00b7 Germany',
 mono='H', prov_short='HZDR', prov_long='Helmholtz-Zentrum Dresden-Rossendorf, Dresden, Germany',
 h1='HZDR Summer Student Program 2027',
 sub='Six to nine weeks of real research this summer at the Helmholtz-Zentrum Dresden-Rossendorf \u2014 with a daily grant, free accommodation, insurance and local transport.',
 dpill='Opens 2 Nov 2026', dl_long='24 Jan 2027',
 facts=facts([('Award','Daily grant + accommodation<small>Insurance + local transport included</small>'),
              ('Who can apply','Undergrad / Master\u2019s<small>3+ years of university study by Sep 2027</small>'),
              ('Application window','2 Nov 2026 \u2013 24 Jan 2027<small>Decisions by end Mar 2027</small>'),
              ('Duration','6\u20139 weeks<small>July\u2013September 2027</small>'),
              ('Fields','Natural sciences<small>Physics, life sciences, engineering, tech</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>HZDR Summer Student Program 2027</strong>, run by the <strong>Helmholtz-Zentrum Dresden-Rossendorf (HZDR)</strong> \u2014 one of Germany\u2019s national research centres \u2014 invites undergraduate and master\u2019s students to spend <strong>six to nine weeks between July and September 2027</strong> doing genuine research inside one of its groups. Participants join working teams in the physical and life sciences, engineering and technology, attend scientific lectures, meet their supervisor regularly and receive feedback on their performance at the end of the stay.</p>
      <div class="honest-note"><strong>Not open yet:</strong> applications for the 2027 round open on <strong>2 November 2026</strong> and close on <strong>24 January 2027</strong>, per the official HZDR announcement. Selection notifications go out by the end of March 2027.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled as an <strong>undergraduate or master\u2019s student</strong> in a relevant field (natural sciences, engineering, technology, life sciences).</li>
        <li>Will have completed <strong>at least three years of total university studies by 30 September 2027</strong> \u2014 i.e. you started your undergraduate studies <strong>no later than October 2024</strong>.</li>
        <li>Will <strong>remain enrolled between July and September 2027</strong> and continue your studies as a bachelor\u2019s or master\u2019s student after the summer break 2027.</li>
        <li><strong>No previous contract or stipend at HZDR</strong> \u2014 former contractors are excluded.</li>
        <li><strong>PhD students are not eligible</strong>, nor are graduates who are no longer students.</li>
        <li><strong>Good academic performance</strong> backed by grades and a letter of recommendation from a scientist who knows your work.</li>
        <li><strong>Good English</strong> \u2014 the programme is conducted in English.</li>
        <li>A <strong>valid student ID covering the whole programme period</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>daily grant</strong> covering everyday expenses (the 2026 round paid <strong>\u20ac36 per day</strong> \u2014 the 2027 rate has not been published yet).</li>
        <li><strong>Free accommodation</strong> for the whole stay.</li>
        <li><strong>Travel insurance</strong> and <strong>local bus tickets</strong>.</li>
        <li><strong>Scientific lectures</strong> (between the end of July and the end of August), individual supervisor meetings and an end-of-programme performance review.</li>
        <li>International travel to Germany and visa costs are <strong>not covered</strong> \u2014 plan and budget for those yourself.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Online application form</strong> with your CV details (enrolment status, field of study, expected graduation date, GPA orientation).</li>
        <li><strong>Academic grades / records</strong> (most recent semester grade, converted to a 0\u20134 GPA orientation).</li>
        <li><strong>Copy of your student ID</strong>, valid through September 2027.</li>
        <li><strong>Letter of recommendation</strong> from a professor or senior scientist \u2014 uploaded by the recommender through the link HZDR provides before the deadline.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Wait for the portal to open on 2 November 2026</strong>The application form goes live on the official HZDR summer students page.</li>
        <li><strong>Fill in the application form</strong>Answer the enrolment and study-history questions carefully \u2014 especially the three-year rule.</li>
        <li><strong>Upload your documents</strong>CV, grades and student ID as instructed.</li>
        <li><strong>Arrange your recommendation letter early</strong>Ask your professor or senior scientist well before <strong>24 January 2027</strong> so their letter is uploaded in time.</li>
        <li><strong>Wait for the decision</strong>Acceptance or rejection notifications arrive by email once selection is finished (by end of March 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When do HZDR 2027 applications open?","On 2 November 2026, and they close on 24 January 2027. The form is not available before that date."),
 ("Do I need a bachelor\u2019s degree to apply?","No \u2014 a bachelor\u2019s degree is not required. You need at least three years of university study completed by 30 September 2027."),
 ("Can PhD students apply?","No \u2014 PhD students are not eligible for the summer student program."),
 ("I worked at HZDR before. Can I apply?","No \u2014 students who already had a contract or stipend at HZDR are excluded."),
 ("Is travel to Germany covered?","No \u2014 the programme covers a daily grant, accommodation, insurance and local transport, but not international travel or visa costs."),
]),
 verify='Verified 19 Oct 2026 on the official HZDR Summer Student Program 2027 application page (hzdr.de/db/Cms?pOid=36868&pNid=2914): window 2 Nov 2026 - 24 Jan 2027, decisions by end Mar 2027, >=3 years of study by 30 Sep 2027 (started by Oct 2024), continued bachelor\u2019s/master\u2019s enrolment, prior-HZDR-contract exclusion, recommendation letter. Programme format (6-9 weeks Jul-Sep, EUR 36/day 2026 rate, free accommodation, insurance, local transport, no airfare/visa) from the 2026 call and independent trackers \u2014 2027 rates not yet published.',
 offlinks=[('HZDR Summer Student Program 2027 \u2014 official application page','https://www.hzdr.de/db/Cms?pOid=36868&pNid=2914')],
 related_titles=['epfl-summer','hanns-seidel','utrip-2027'],
),

dict(
 slug='brunei-darussalam-government-scholarship-2027-28',
 title='Brunei Darussalam Government Scholarship 2027/28 | StudyDesk Scholarships',
 meta='Brunei Darussalam Government Scholarship 2027/28: fully funded diploma, undergraduate and master\u2019s study at five Brunei institutions. Expected window December 2026 \u2013 February 2027. Eligibility, benefits, documents, how to apply.',
 short='Brunei Darussalam Government Scholarship', kicker='Government Scholarship \u00b7 Brunei',
 mono='B', prov_short='Govt. of Brunei Darussalam', prov_long='Ministry of Foreign Affairs, Brunei Darussalam',
 h1='Brunei Darussalam Government Scholarship 2027/28',
 sub='Fully funded diploma, undergraduate and master\u2019s study at five Bruneian institutions \u2014 full tuition, a monthly allowance, accommodation, airfare and insurance.',
 dpill='Expected Dec 2026', dl_long='Expected ~15 Feb 2027',
 facts=facts([('Award','Fully funded<small>Tuition, monthly allowance, accommodation, airfare</small>'),
              ('Who can apply','All nationalities<small>Diploma, UG, Master\u2019s; age limits apply</small>'),
              ('Institutions','5 institutions<small>UBD, UNISSA, UTB, KUPU SB, Politeknik Brunei</small>'),
              ('Expected window','Mid-Dec 2026 \u2013 mid-Feb 2027<small>2027/28 call not yet announced</small>'),
              ('Levels','Diploma / UG / Master\u2019s<small>3\u20134 yrs / 4 yrs / 12\u201324 months</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Brunei Darussalam Government Scholarship (BDGS)</strong>, offered by Brunei\u2019s <strong>Ministry of Foreign Affairs</strong>, funds international students to study at <strong>five government institutions</strong>: <strong>Universiti Brunei Darussalam (UBD)</strong>, <strong>Universiti Islam Sultan Sharif Ali (UNISSA)</strong>, <strong>Universiti Teknologi Brunei (UTB)</strong>, <strong>Kolej Universiti Perguruan Ugama Seri Begawan (KUPU SB)</strong> and <strong>Politeknik Brunei</strong>. It covers diploma, undergraduate and master\u2019s programmes, with each institution\u2019s eligible course list published with every round.</p>
      <div class="honest-note"><strong>Preparation guide:</strong> the 2027/28 application round has <strong>not been announced yet</strong>. The Ministry of Education published the 2027/28 course list in October 2026, and applications are expected around December 2026 \u2013 February 2027 (the 2026/27 round ran 15 Dec 2025 \u2013 15 Feb 2026). Watch the MFA scholarship page from December 2026. Benefit figures below are from the 2026/27 call and should be confirmed against the new official notice.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International applicants of all nationalities</strong> \u2014 Brunei citizens and permanent residents are excluded.</li>
        <li><strong>Age limits (as of 1 July of the programme start year):</strong> diploma and undergraduate applicants must be <strong>18\u201325 years old</strong>; master\u2019s applicants must <strong>not exceed 35</strong>.</li>
        <li><strong>Never studied at a Bruneian tertiary institution</strong> before \u2014 prior enrolment counts against you.</li>
        <li><strong>English proficiency</strong> for English-taught tracks: typically <strong>IELTS 6.0, TOEFL 550, or a credit in English at GCE \u201cO\u201d Level / IGCSE</strong>. Some courses are taught in Malay or Arabic \u2014 institutions may test your language level and may call you for an interview.</li>
        <li><strong>Married applicants may apply</strong>, but scholars are not encouraged to bring family \u2014 no family accommodation or allowances are provided.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full exemption from tuition fees.</strong></li>
        <li><strong>Monthly allowance of BND 650</strong> (personal allowance BND 500 + meal allowance BND 150).</li>
        <li><strong>Book allowance of BND 600 per year.</strong></li>
        <li><strong>Free on-campus accommodation.</strong></li>
        <li><strong>Return economy-class air ticket</strong> between your home country and Brunei.</li>
        <li><strong>Medical / health insurance</strong> and a <strong>baggage allowance</strong> (BND 250 within ASEAN / BND 500 outside).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Completed online BDGS application form</strong> with first and second programme choices (note the programme codes from each university\u2019s brochure).</li>
        <li><strong>Passport</strong> (valid for the study period) and passport-size photographs.</li>
        <li><strong>Academic certificates and transcripts</strong> (certified copies).</li>
        <li><strong>Birth certificate</strong> and <strong>police clearance</strong>.</li>
        <li><strong>Two referee reports</strong> \u2014 the C1 and C2 reference forms completed by your referees.</li>
        <li>Any <strong>language certificates</strong> (IELTS/TOEFL or equivalent) for English-taught programmes.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Watch the MFA scholarship page from December 2026</strong>The 2027/28 announcement and course lists will appear there.</li>
        <li><strong>Pick your programmes</strong>Check the published lists for UBD, UNISSA, UTB, KUPU SB and Politeknik Brunei; verify the age, language and entry rules in the new notice.</li>
        <li><strong>Apply on the MFA\u2019s online BDGS portal</strong>Fill the form and upload your documents.</li>
        <li><strong>Also apply on the university portal if you chose UBD or UTB</strong>The 2026/27 notice required a separate university application for these two (UNISSA, KUPU SB and Politeknik Brunei did not).</li>
        <li><strong>Get your referees to complete the C1 and C2 forms</strong>Do this early \u2014 late references sink applications.</li>
        <li><strong>Submit before the closing date and keep checking your email</strong>Successful applicants are contacted for the next selection stage; the ministry\u2019s decision is final and it does not take appeals.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When will the 2027/28 round open?","Not announced yet. Based on the established pattern, expect mid-December 2026 to mid-February 2027. The ministry published the 2027/28 course list in October 2026."),
 ("Is IELTS mandatory?","For English-taught tracks the typical bar is IELTS 6.0, TOEFL 550, or a credit in English at GCE \u201cO\u201d Level/IGCSE. Confirm the exact requirement in the new official notice."),
 ("Can I apply if I studied in Brunei before?","No \u2014 international students who have already started or completed a degree at a Bruneian institution are ineligible."),
 ("Which institutions are covered?","UBD, UNISSA, UTB, KUPU SB and Politeknik Brunei \u2014 five government-backed institutions in total."),
 ("Can married applicants apply?","Yes, marital status does not disqualify you, but no family accommodation or family allowances are provided."),
]),
 verify='Verified 19 Oct 2026: the 2027/28 round is not yet announced (MFA portal shows the call closed; last round 15 Dec 2025 - 15 Feb 2026 per a Sep 2026 read of the MFA pages; Borneo Bulletin 18 Oct 2026 reports MoE published the 2027/28 course list with applications expected around January 2027). Package (BND 650/month, BND 600/year books, tuition, accommodation, airfare, insurance, baggage), age limits (18-25 UG / max 35 master\u2019s as of 1 July), language thresholds (IELTS 6.0 / TOEFL 550), the five institutions and the UBD/UTB dual-application rule are from the 2026/27 call \u2014 to be confirmed against the new official notice when it opens.',
 offlinks=[('Ministry of Foreign Affairs \u2014 scholarship page (official)','https://www.mfa.gov.bn/pages/scholarship.aspx')],
 related_titles=['ubd-grad','qecs-2027-28','unu-junior-fellows-2027'],
),

dict(
 slug='utrip-summer-internship-2027-japan',
 title='UTRIP Summer Internship 2027, Japan | StudyDesk Scholarships',
 meta='UTRIP Summer Internship 2027: the University of Tokyo\u2019s six-week summer research internship. Applications open November 2026; published deadline 7 Jan 2027. Eligibility, benefits, documents, how to apply.',
 short='UTRIP Summer Internship', kicker='Research Internship \u00b7 Japan',
 mono='UT', prov_short='University of Tokyo', prov_long='Graduate School of Science, University of Tokyo',
 h1='UTRIP Summer Internship 2027',
 sub='Six weeks of hands-on research in the natural sciences at the University of Tokyo \u2014 with accommodation and financial support, and no programme or accommodation fees.',
 dpill='Opens Nov 2026', dl_long='7 Jan 2027',
 facts=facts([('Award','Research internship<small>Accommodation + financial support; no fees</small>'),
              ('Who can apply','Overseas undergrads<small>Natural sciences; \u22651 yr of bachelor\u2019s done</small>'),
              ('Published deadline','7 Jan 2027<small>Applications open November 2026</small>'),
              ('Duration','6 weeks<small>25 Jun \u2013 5 Aug 2027 (published)</small>'),
              ('Programme','Graduate School of Science<small>Physics, chemistry, earth &amp; planetary, biology</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>UTRIP (University of Tokyo Research Internship Program)</strong>, run by the <strong>Graduate School of Science, University of Tokyo</strong>, is a six-week summer research internship for undergraduates in the <strong>natural sciences</strong> \u2014 physics, chemistry, earth &amp; planetary science and biological sciences. Participants work on a real research project under faculty supervision, experience graduate-school life at one of Asia\u2019s top research universities, and take an <strong>intensive introductory Japanese language course</strong> designed for daily life and lab communication.</p>
      <div class="honest-note"><strong>Not open yet:</strong> applications for UTRIP 2027 open in <strong>November 2026</strong> \u2014 the official UTokyo page updates the 2027 call in late November. Scholarship trackers publish a <strong>7 January 2027</strong> deadline and <strong>25 June \u2013 5 August 2027</strong> dates, but these are not yet year-dated on the official site \u2014 confirm them when the call opens.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled in an <strong>undergraduate programme at an overseas college or university</strong> (outside Japan) for the entire duration.</li>
        <li>Completed <strong>at least one year of your bachelor\u2019s degree</strong> before the programme starts \u2014 third-year students are particularly welcome.</li>
        <li>Expect to <strong>return to undergraduate study</strong> after the programme ends (you must not have completed your degree).</li>
        <li><strong>Strong interest in the natural sciences</strong> and good English proficiency.</li>
        <li><strong>GPA of 3.0 out of 4.0</strong> was the 2026 criterion \u2014 confirm the 2027 bar when the call opens.</li>
        <li>A <strong>letter of recommendation</strong> from a professor or scientist who knows your work.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>No programme or accommodation fees</strong> \u2014 confirmed on the official UTRIP FAQ.</li>
        <li><strong>Accommodation provided</strong> \u2014 a short-stay residence facility with furnished rooms.</li>
        <li><strong>Financial support</strong> under the programme\u2019s standing terms (housing, travel and stipend support) \u2014 confirm the exact 2027 package in the November call.</li>
        <li><strong>Intensive Japanese language course</strong> (about five classes) included.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Completed online application form</strong> (opens November 2026).</li>
        <li><strong>CV</strong> and <strong>academic transcript</strong>.</li>
        <li><strong>Personal statement / research interests</strong> \u2014 check the lab/project list and name your preferences.</li>
        <li><strong>Letter of recommendation</strong>.</li>
        <li><strong>Proof of enrolment</strong> at your home university.</li>
      </ol>
      <p>Exact 2027 document requirements will be published with the November call \u2014 prepare the above in advance.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the official UTRIP page in November 2026</strong>The 2027 call, lab list and document checklist are updated in late November.</li>
        <li><strong>Choose a lab and project</strong>Review the published supervisors and available positions; tailor your statement to one or two labs.</li>
        <li><strong>Prepare your documents and referee early</strong>Give your recommender at least three weeks before the deadline.</li>
        <li><strong>Submit online before the deadline</strong>Trackers publish <strong>7 January 2027</strong> \u2014 confirm the exact date on the official page.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When do UTRIP 2027 applications open?","In November 2026 \u2014 the official page updates the 2027 call in late November."),
 ("What is the UTRIP 2027 deadline?","Scholarship trackers publish 7 January 2027, but it is not yet year-dated on the official site \u2014 confirm it when the call opens."),
 ("Is UTRIP fully funded?","There are no programme or accommodation fees, and the programme provides accommodation plus financial support. Confirm the exact 2027 figures in the official call."),
 ("Can graduate students apply?","No \u2014 UTRIP is for undergraduates at overseas universities who will return to undergraduate study afterwards."),
 ("What GPA do I need?","3.0 out of 4.0 was the 2026 criterion. Confirm the 2027 requirement when the call opens."),
]),
 verify='Verified 19 Oct 2026: UTRIP is run by the UTokyo Graduate School of Science (s.u-tokyo.ac.jp/en/utrip); the official FAQ confirms it is open to overseas undergraduates, charges no programme or accommodation fees, and that the 2027 application information is updated in late November. The 7 Jan 2027 deadline, 25 Jun - 5 Aug 2027 dates, the November opening, accommodation/meals/Japanese-course details and the 2026 eligibility rules (>=1 year of bachelor\u2019s, return to UG study after, GPA 3.0/4.0, recommendation letter) are from scholarship trackers (scholarshiproar.com) and the 2026 call \u2014 the exact 2027 dates and package should be confirmed when the official call opens.',
 offlinks=[('UTRIP \u2014 official page, University of Tokyo','https://www.s.u-tokyo.ac.jp/en/utrip/')],
 related_titles=['u-tokyo-mext','science-tokyo','hzdr-2027'],
),

dict(
 slug='queen-elizabeth-commonwealth-scholarships-2027-28',
 title='Queen Elizabeth Commonwealth Scholarships 2027-28 | StudyDesk Scholarships',
 meta='Queen Elizabeth Commonwealth Scholarships 2027-28, Cycle 1: 18 Nov 2026 \u2013 13 Jan 2027. A fully funded two-year master\u2019s in a low or middle-income Commonwealth country. Eligibility, benefits, how to apply.',
 short='Queen Elizabeth Commonwealth Scholarships', kicker='Government Scholarship \u00b7 Commonwealth',
 mono='QE', prov_short='ACU', prov_long='Association of Commonwealth Universities (ACU)',
 h1='Queen Elizabeth Commonwealth Scholarships 2027\u201328',
 sub='A fully funded two-year master\u2019s in another low or middle-income Commonwealth country \u2014 tuition, a living stipend, return flights and an arrival allowance.',
 dpill='Opens 18 Nov 2026', dl_long='13 Jan 2027',
 facts=facts([('Award','Fully funded<small>Tuition + stipend + return flights</small>'),
              ('Who can apply','Commonwealth citizens<small>2:1 bachelor\u2019s; study outside home country</small>'),
              ('Degree','Two-year master\u2019s<small>Low/middle-income Commonwealth host</small>'),
              ('Cycle 1 window','18 Nov 2026 \u2013 13 Jan 2027<small>Per the ACU funding calendar</small>'),
              ('Age limit','No age limit<small>Open to all eligible graduates</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Queen Elizabeth Commonwealth Scholarships (QECS)</strong>, administered by the <strong>Association of Commonwealth Universities (ACU)</strong>, offer a unique opportunity: a <strong>fully funded two-year master\u2019s degree</strong> at an ACU member university in a <strong>low or middle-income Commonwealth country other than your own</strong>. Aimed at students committed to creating change in their communities, the scholarship builds cultural exchange, academic collaboration and a global network that lasts a lifetime. Each year there are <strong>two application cycles</strong> \u2014 cycle 1 opens in November/December and cycle 2 in March/April.</p>
      <div class="honest-note"><strong>Cycle 1 dates:</strong> the 2027\u201328 Cycle 1 window is <strong>18 November 2026 \u2013 13 January 2027</strong>, as published on the ACU funding opportunities calendar. The official QECS page currently shows the previous cycle as closed; confirm the host university and course list when Cycle 1 opens.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of a Commonwealth country</strong> (or hold recognised refugee status in one).</li>
        <li>Hold a bachelor\u2019s degree at <strong>minimum 2:1 level or equivalent</strong>.</li>
        <li>Will study in a <strong>different Commonwealth country from your own</strong> \u2014 you cannot hold a QECS award in your home country.</li>
        <li>Meet the <strong>host university\u2019s admission requirements</strong> for your chosen course (only the courses listed for the cycle are eligible for funding).</li>
        <li><strong>No upper age limit.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Fully funded tuition fees.</strong></li>
        <li><strong>Living allowance (stipend)</strong> for the duration of the award.</li>
        <li><strong>Return economy flights</strong> to the host country.</li>
        <li><strong>One-off arrival allowance.</strong></li>
        <li><strong>Research support grant</strong> \u2014 on request only, subject to approval.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>QECS online application</strong> \u2014 create a myACU account and complete the application for your chosen university/course.</li>
        <li><strong>Separate university application for admission</strong> to the same course.</li>
        <li><strong>Degree certificate and transcripts</strong> (proof of 2:1 or equivalent).</li>
        <li><strong>References</strong> and <strong>personal statements</strong> as set out in the cycle\u2019s application guidance.</li>
      </ol>
      <p>Read the ACU\u2019s application guidance and FAQs pages before starting your application.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Wait for Cycle 1 to open on 18 November 2026</strong>The host list of countries, universities and eligible courses is published with the cycle.</li>
        <li><strong>Choose your course</strong>Pick a listed course at a host university in a different Commonwealth country \u2014 visit the university\u2019s website for course details.</li>
        <li><strong>Apply to the university for admission</strong>A separate admission application is required.</li>
        <li><strong>Submit your QECS application</strong>Create a myACU account (if you don\u2019t have one) and submit before <strong>13 January 2027</strong>.</li>
        <li><strong>You may apply in more than one cycle</strong>Only one application per cycle \u2014 but you can try again in cycle 2 (March/April 2027) for a different country.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need IELTS for QECS?","English requirements are set by each host university and course \u2014 check the university\u2019s page for your chosen course. The scholarship itself does not set a single English-test rule."),
 ("Can I study in my home country?","No \u2014 QECS funds study in a low or middle-income Commonwealth country different from your own."),
 ("Is there an age limit?","No upper age limit."),
 ("How many times can I apply?","You only need to submit one application per cycle, but you may apply again in a later cycle for a different country."),
 ("When is Cycle 2 for 2027-28?","ACU runs cycle 2 in March/April each year \u2014 expect March/April 2027 for the 2027-28 cycle 2."),
]),
 verify='Verified 19 Oct 2026 on the official ACU QECS page (acu.ac.uk): two application cycles a year (cycle 1 opens Nov/Dec, cycle 2 Mar/Apr), two-year master\u2019s in a low/middle-income Commonwealth country, full tuition + living stipend + return economy flights + arrival allowance + research support grant on request, myACU application + separate university admission. The 2027-28 Cycle 1 dates (18 Nov 2026 - 13 Jan 2027), the 2:1 degree requirement, the no-home-country rule, no age limit and the UK FCDO funding line are from the ACU funding opportunities calendar as reported by independent trackers \u2014 confirm the host list when the cycle opens.',
 offlinks=[('Queen Elizabeth Commonwealth Scholarships \u2014 official ACU page','https://www.acu.ac.uk/funding-opportunities/for-students/scholarships/queen-elizabeth-commonwealth-scholarships/')],
 related_titles=['brunei-2027-28','unu-junior-fellows-2027','swiss-phd'],
),

dict(
 slug='unu-junior-fellows-internship-spring-2027',
 title='UNU Junior Fellows Internship Spring 2027, Tokyo | StudyDesk Scholarships',
 meta='UNU Junior Fellows Internship Spring 2027: a six-month paid internship at the United Nations University HQ in Tokyo, 1 Mar \u2013 27 Aug 2027. Deadline 1 Nov 2026. Eligibility, stipend, documents, how to apply.',
 short='UNU Junior Fellows Internship', kicker='UN Internship \u00b7 Japan',
 mono='UN', prov_short='United Nations University', prov_long='United Nations University \u2014 Office of the Rector, Tokyo',
 h1='UNU Junior Fellows Internship Spring 2027',
 sub='Six months inside the United Nations University\u2019s Tokyo headquarters \u2014 a full-time, on-site internship with a monthly stipend for fellows without other funding.',
 dpill='13 days to go', dl_long='1 Nov 2026',
 facts=facts([('Award','Monthly stipend<small>For fellows without other funding</small>'),
              ('Who can apply','Master\u2019s/PhD students or recent graduates<small>Aged 32 or under; all nationalities</small>'),
              ('Deadline','1 Nov 2026<small>23:59 Japan Standard Time</small>'),
              ('Duration','6 months<small>1 Mar \u2013 27 Aug 2027, Tokyo</small>'),
              ('Work','Full-time, on-site<small>Mon\u2013Fri 9:30\u201317:30; some remote flexibility</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>UNU Junior Fellows Internship</strong>, run by the <strong>Office of the Rector at United Nations University</strong> \u2014 the UN\u2019s global think tank and postgraduate teaching body \u2014 places graduate-level students and young professionals inside the UNU headquarters in <strong>Shibuya, Tokyo</strong>. The <strong>Spring 2027 session runs 1 March \u2013 27 August 2027</strong> (about 24 weeks). Junior Fellows contribute to research, administration, communications, event coordination and other work supporting the university\u2019s international mission, beginning with a one-week orientation and working <strong>full time, 9:30 to 17:30, Monday to Friday</strong>, mainly on site with some remote flexibility. Applicants based <strong>in Japan and overseas are both considered</strong>; UNU strongly encourages applicants from developing countries and women.</p>
      <div class="honest-note"><strong>Open now \u2014 13 days left:</strong> applications for Spring 2027 close on <strong>1 November 2026 at 23:59 Japan Standard Time</strong>. Your referees\u2019 letters must also arrive by the deadline \u2014 contact them today.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled in, or <strong>recently completed, a master\u2019s or PhD degree</strong>.</li>
        <li><strong>32 years old or younger</strong> when you apply.</li>
        <li><strong>No more than 5 years of work experience</strong> in a related field.</li>
        <li><strong>All nationalities</strong> \u2014 applicants living in Japan and overseas are both eligible.</li>
        <li>Strong interest in <strong>international relations, development studies, public policy</strong> and the <strong>Sustainable Development Goals</strong>.</li>
        <li><strong>Excellent communication and research skills</strong> and fluency in English.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend</strong> to help cover part of basic living expenses \u2014 for interns who receive <strong>no relevant financial support from another institution</strong>. Academic scholarships for your studies are excluded from this rule. The exact amount is not published.</li>
        <li><strong>Office space</strong> at UNU headquarters and <strong>on-site and online access to the HQ library and gym</strong>.</li>
        <li><strong>1.5 days of leave per month.</strong></li>
        <li>Practical experience in research, writing, analysis, institutional planning and supporting conferences, workshops and academic forums.</li>
        <li><strong>No application fee</strong> \u2014 UNU never charges any application, processing or interview fee. Ignore anyone who asks you to pay.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Completed application form</strong> on the official UNU careers portal (Spring 2027 vacancy).</li>
        <li><strong>CV</strong> highlighting research, writing and analytical skills.</li>
        <li><strong>Cover letter</strong> linking your studies to UNU\u2019s work on the Sustainable Development Goals.</li>
        <li><strong>Referee details</strong> \u2014 their letters must reach UNU by the deadline; you cannot submit them yourself.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find the official Spring 2027 vacancy</strong>On the UNU careers portal \u2014 read the vacancy notice fully before applying.</li>
        <li><strong>Prepare your documents</strong>CV, cover letter and application form; show Excel and writing skills with concrete examples.</li>
        <li><strong>Contact your referees now</strong>Their letters must arrive by <strong>1 November 2026, 23:59 JST</strong> \u2014 this is the step most applicants leave too late.</li>
        <li><strong>Submit before the deadline</strong>Plan your Tokyo budget early \u2014 the stipend covers only part of living costs.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the UNU Junior Fellows Internship paid?","Eligible interns receive a monthly stipend \u2014 but only if they have no other relevant financial support, and it covers only part of living costs. The amount is not published."),
 ("Who can apply?","Master\u2019s or PhD students and recent postgraduate graduates aged 32 or under, from any country, with no more than 5 years of related work experience."),
 ("Is it remote?","It is mainly on-site at UNU headquarters in Tokyo, with some remote flexibility."),
 ("Is there an application fee?","No \u2014 UNU never charges application, processing or interview fees. Treat any payment request as a scam."),
 ("Can I apply from outside Japan?","Yes \u2014 applicants based in Japan and overseas are both considered for the Spring 2027 term."),
]),
 verify='Verified 19 Oct 2026 across 7 independent trackers (opportunitiesradar, pathfinderly, opportunitylab, opportunitiescorners, inspireopportunities, bloompakistan, gizpulse), all consistent: Spring 2027 session 1 Mar - 27 Aug 2027 at the UNU Office of the Rector, Tokyo; applications close 1 Nov 2026, 23:59 JST; open to master\u2019s/PhD students and recent graduates aged 32 or under with <=5 years\u2019 experience, all nationalities; monthly stipend for interns without other funding (amount not published); apply via the official UNU careers portal (Spring 2027 vacancy).',
 offlinks=[('United Nations University \u2014 official site','https://unu.edu/')],
 related_titles=['qecs-2027-28','brunei-2027-28','utrip-2027'],
),
]

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# validate
import html.parser
class P(html.parser.HTMLParser):
    def error(self, m): raise Exception(m)
for slug, _ in built:
    src = OUT.joinpath(slug + '.html').read_text()
    P().feed(src)
    # leftover template text = 'AICTE Pragati', 'Lorem', and template anchors like href="#"/src="#"
    # (CSS hex colours such as #fff in the design system are not template leftovers)
    for bad in ['AICTE Pragati', 'Lorem', 'href="#"', 'src="#"', 'href=\'#\'']:
        assert bad not in src, (slug, bad)
    print('validated', slug)

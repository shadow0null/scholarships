#!/usr/bin/env python3
"""Batch 32 build: 5 verified articles (YLP MEXT GRIPS 2027, MESPOM 2027-29,
Tomorrow's Leaders 2027-28, Radboud 2027/28, Imperial MBA 2027).
All five queue "2026" titles had closed cycles; the articles are written for the
live 2027 cycles (Radboud/Tomorrow's-Leaders/Imperial retitled accordingly;
MESPOM "Fully Funded" downgraded to "Funded" per the official 2027 call page).
Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'ylp-mext-grips-2027': {'mono': 'MEXT', 'title': 'YLP MEXT Scholarship at GRIPS 2027 in Japan (Fully Funded)',
   'href': 'ylp-mext-grips-scholarship-2027-japan.html',
   'dpill': 'Varies by country · check the Japanese embassy',
   'award': 'JPY 242,000/month allowance + tuition waived + air tickets + arranged housing',
   'elig': 'Participating YLP-country nationals; <40 on 1 Oct 2027; bachelor\u2019s + \u22653 yrs public-service experience; English required.',
   'tags': [("Master\u2019s", 'blue'), ('Japan', 'teal')]},
 'mespom-2027': {'mono': 'MES', 'title': 'Erasmus Mundus MESPOM Scholarship 2027\u20132029 in Europe (Funded)',
   'href': 'erasmus-mundus-mespom-scholarship-2027-29-europe.html',
   'dpill': '7 Jan 2027 · 78 days to go',
   'award': 'Competitive partial tuition waivers + living stipends (exact amounts not published)',
   'elig': 'All nationalities; first degree in a relevant field; GPA 3.5+; English proficiency.',
   'tags': [("Master\u2019s", 'blue'), ('Europe', 'teal')]},
 'tomorrows-leaders-2027': {'mono': 'TL', 'title': "Tomorrow's Leaders Scholarship 2027-28 (Fully Funded)",
   'href': 'tomorrows-leaders-scholarship-2027-28.html',
   'dpill': '18 Nov 2026 · 28 days to go',
   'award': 'Tuition + housing + insurance + visa fees + laptop + 2 flights home/yr + monthly stipend + one US semester',
   'elig': 'MENA-region nationals (12 states); high-school seniors/2026 graduates; English required; not US citizens/PRs.',
   'tags': [('Undergraduate', 'blue'), ('Lebanon', 'teal')]},
 'radboud-2027': {'mono': 'RU', 'title': 'Radboud Scholarship Programme 2027-28 in Netherlands (Funded)',
   'href': 'radboud-scholarship-programme-2027-28-netherlands.html',
   'dpill': '31 Jan 2027 · 102 days to go',
   'award': 'Tuition reduced to EUR 2,771 (was ~EUR 19,000) + visa/permit costs + health & liability insurance; living costs NOT covered',
   'elig': 'Non-EU/EEA passport; bachelor\u2019s outside the Netherlands; admitted to an English-taught master\u2019s starting Sep 2027.',
   'tags': [("Master\u2019s", 'blue'), ('Netherlands', 'teal')]},
 'imperial-mba-2027': {'mono': 'IC', 'title': 'Imperial College MBA Scholarships 2027 in UK (Funded)',
   'href': 'imperial-college-mba-scholarships-2027-uk.html',
   'dpill': '12 Jan 2027 (Round 2) · 83 days to go',
   'award': 'Multiple awards: 20%\u2013100% tuition-fee reductions incl. named scholarships (Dean\u2019s Impact, Advisory Board, Fort\u00e9, Female Future Leaders GBP 20,000)',
   'elig': 'Self-funded applicants to the Full-Time MBA (Sep 2027); strong academics, leadership impact; GMAT/GRE for some awards.',
   'tags': [('MBA', 'blue'), ('UK', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='ylp-mext-grips-scholarship-2027-japan',
 title='YLP MEXT Scholarship at GRIPS 2027 in Japan (Fully Funded)',
 meta='YLP MEXT Scholarship at GRIPS 2027: the Japanese Government\u2019s fully funded Young Leaders\u2019 Program for a one-year Master of Public Policy in Tokyo \u2014 JPY 242,000/month, tuition waived, air tickets and arranged housing. Apply through your recommending authority; deadlines vary by country.',
 short='YLP MEXT Scholarship at GRIPS 2027', kicker='Japan \u00b7 Master\u2019s \u00b7 Fully Funded', mono='MEXT',
 prov_short='MEXT (Japanese Government) at GRIPS, Tokyo', prov_cat='Government \u00b7 Japan',
 h1='YLP MEXT Scholarship at GRIPS 2027 in Japan (Fully Funded)',
 sub='The Japanese Government\u2019s flagship leadership scholarship for mid-career public servants \u2014 one fully funded year at GRIPS in Tokyo for a Master of Public Policy.',
 dpill='Varies by country \u2014 check the Japanese embassy',
 facts=facts([('Award', 'Fully funded: JPY 242,000/month allowance + tuition/examination/matriculation fees waived + economy air tickets to and from Japan + accommodation arranged (TIEC residence halls in principle)'),
              ('Eligible', 'Nationals of participating YLP countries; under 40 on 1 Oct 2027 (born on/after 2 Oct 1987); bachelor\u2019s degree; \u22653 years\u2019 full-time public-administration experience (5+ preferred); English proficiency; non-Japanese'),
              ('Programme', 'Master of Public Policy, 1 year (Oct 2027\u2013Sep 2028), GRIPS School of Government; ~20 places'),
              ('How', 'Obtain the application form from the Japanese embassy or recommending authority; submit hard-copy documents to the recommending authority'),
              ('Deadline', 'No central deadline \u2014 set by the recommending authority in each country; third-party trackers cite 20 Nov 2026, not confirmed on official pages')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Young Leaders\u2019 Program (YLP)</strong>, funded by the <strong>Japanese Government (MEXT)</strong> and hosted by the <strong>National Graduate Institute for Policy Studies (GRIPS)</strong> in Tokyo, is designed for promising <strong>public officials</strong> from partner countries who are expected to play active roles as future national leaders. The <strong>2027 intake</strong> leads to a <strong>one-year Master of Public Policy</strong> (October 2027 \u2013 September 2028) at the GRIPS School of Government, with the School of Local Governance offering a parallel track.</p>
      <p>The package is genuinely fully funded: a <strong>JPY 242,000 monthly allowance</strong>, <strong>waived entrance-examination, matriculation and tuition fees</strong>, <strong>economy-class air tickets</strong> from the home country to Japan on enrolment and back on completion, and <strong>accommodation arranged</strong> at GRIPS-provided residence halls.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>National of a participating YLP country</strong> and <strong>non-Japanese</strong> (dual nationals residing outside Japan may apply if they renounce Japanese nationality).</li>
        <li><strong>Under 40 years old as of 1 October 2027</strong> (born on or after 2 October 1987).</li>
        <li><strong>Bachelor\u2019s degree or equivalent</strong> with an excellent academic record.</li>
        <li><strong>At least 3 years of full-time work experience in public administration</strong> as of 1 October 2027 (<strong>5+ years preferred</strong>).</li>
        <li><strong>English ability</strong> \u2014 admission priority is given to applicants at <strong>TOEFL iBT 79+ or IELTS Academic 6.0+</strong> (waivers may apply for degrees completed in English).</li>
        <li>Physically fit; able to obtain a new \u201cStudent\u201d visa; <strong>expected to return home and resume public service</strong> after the programme. <strong>Military personnel are excluded.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>JPY 242,000 monthly allowance</strong> for the programme duration.</li>
        <li><strong>Examination, matriculation and tuition fees waived.</strong></li>
        <li><strong>Economy-class air tickets</strong> to Japan on enrolment and back home on completion.</li>
        <li><strong>Accommodation arranged</strong> at GRIPS-provided residence halls.</li>
        <li>One year of policy training in Tokyo with a cohort of future public-sector leaders.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>designated application form</strong> with a photo.</li>
        <li><strong>Recommendation letter from the recommending authority</strong>, plus <strong>two recommendation letters on the designated forms</strong> (sealed, at least one from an immediate work superior).</li>
        <li><strong>Official academic transcripts</strong> and <strong>degree certificates</strong>.</li>
        <li><strong>Official evidence of English ability</strong> (TOEFL/IELTS or equivalent).</li>
        <li><strong>Passport copy</strong>; a <strong>three-page essay</strong> on aspirations and future plans; <strong>answers to the essay questions</strong>; and a <strong>certificate of health on the designated form</strong>.</li>
        <li>Hard copies only \u2014 the guidelines call for <strong>10 document items</strong> in total, submitted through the recommending authority.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find your recommending authority</strong>Check the GRIPS website or your local <strong>Japanese embassy</strong> for the recommending authority in your country and obtain the application form.</li>
        <li><strong>Prepare the hard-copy set</strong>Complete all ten document items \u2014 sealed references, transcripts, English test evidence, health certificate and essays.</li>
        <li><strong>Submit to the recommending authority</strong>Do not send documents directly to GRIPS. Submit the complete set to your country\u2019s recommending authority <strong>by its designated deadline</strong> \u2014 screening runs recommending authority \u2192 GRIPS \u2192 the final MEXT YLP committee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the application deadline for the 2027 intake?',
  'There is no central deadline \u2014 each country\u2019s recommending authority sets its own. Contact your Japanese embassy now. Third-party trackers cite 20 November 2026, but this date is not on any official page, so treat it as unconfirmed.'),
 ('Can I apply directly to GRIPS?',
  'No \u2014 applications go through the recommending authority in your country (often via the Japanese embassy). GRIPS does not accept direct submissions.'),
 ('Is the JPY 242,000 monthly allowance confirmed for 2027?',
  'The allowance is stated in the programme materials; the exact 2027 figure should be confirmed against the official guidelines for your country.'),
 ('Do I need TOEFL or IELTS?',
  'English ability is required, and admission priority goes to applicants with TOEFL iBT 79+ or IELTS Academic 6.0+. Applicants whose degrees were completed in English may be waived \u2014 check with your recommending authority.'),
 ('Must I return to my home country afterwards?',
  'Yes \u2014 scholars are expected to return home and resume public service on completion.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official GRIPS YLP page (grips.ac.jp: programme structure, recommending-authority route, 2027/28 admission window) + the official MEXT 2027 YLP School-of-Government application guidelines (age/experience rules, JPY 242,000 allowance, 10-item hard-copy document list, three-stage screening) + the Embassy of Japan in Laos 2027 announcement. The deadline is the weakest fact: the only official line is the recommending authority\u2019s designated deadline; the 20 Nov 2026 tracker figure is explicitly flagged as unconfirmed by any official source.</p>
''',
 dl_long='Varies by country \u2014 set by the recommending authority / Japanese embassy. Third-party trackers cite 20 Nov 2026 (unconfirmed on official pages). Check your local Japanese embassy now.',
 offlinks=[('Young Leaders\u2019 Program \u2014 GRIPS (official)', 'https://www.grips.ac.jp/en/education/inter_programs/leader/'),
           ('MEXT YLP 2027 Application Guidelines \u2014 School of Government (official PDF via gov.pl)', 'https://www.gov.pl/attachment/7504984b-07db-4a1a-a6f1-dce85f596b30'),
           ('Young Leaders\u2019 Program (YLP) 2027 \u2014 Embassy of Japan in the Lao PDR (official)', 'https://www.la.emb-japan.go.jp/itpr_ja/11_000001_01153.html')],
 related_titles=['apu-adb', 'honjo', 'iuj', 'saitama-mext-2027', 'u-tokyo-mext'],
))

A.append(dict(
 slug='erasmus-mundus-mespom-scholarship-2027-29-europe',
 title='Erasmus Mundus MESPOM Scholarship 2027\u20132029 in Europe (Funded)',
 meta='MESPOM 2027\u20132029: Erasmus Mundus Masters in Environmental Sciences, Policy and Management at CEU, University of the Aegean, Lund and Manchester \u2014 competitive partial tuition waivers and living stipends. Financial-aid deadline 7 Jan 2027.',
 short='Erasmus Mundus MESPOM 2027\u20132029', kicker='Europe \u00b7 Master\u2019s \u00b7 Funded', mono='MES',
 prov_short='MESPOM Consortium (CEU Vienna)', prov_cat='Erasmus Mundus \u00b7 Europe',
 h1='Erasmus Mundus MESPOM Scholarship 2027\u20132029 in Europe (Funded)',
 sub='Erasmus Mundus Masters in Environmental Sciences, Policy and Management \u2014 study across four European universities with competitive partial funding for outstanding candidates.',
 dpill='7 Jan 2027 · 78 days to go',
 facts=facts([('Award', 'Competitive partial tuition-fee waivers and living stipends for outstanding students \u2014 exact amounts and award counts not published for the 2027 cycle'),
              ('Eligible', 'All nationalities; first degree (bachelor\u2019s or equivalent) in a relevant field; GPA 3.5 or above; English proficiency; admission highly competitive'),
              ('Consortium', 'Central European University (Vienna, administering), University of the Aegean (Lesvos, Greece), Lund University (Sweden), University of Manchester (UK)'),
              ('How', 'Online application via the CEU online application form (SITS) on behalf of the MESPOM Consortium; contact coordinator@mespom.eu'),
              ('Deadlines', 'Financial-aid applicants / visa-sensitive countries: 7 Jan 2027; self-financing non-EU/EEA needing a visa: 15 Apr 2027; self-financing visa-free entry to Austria: 15 Jul 2027 (all 23:59 CET)')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>MESPOM</strong> \u2014 the <strong>Erasmus Mundus Masters in Environmental Sciences, Policy and Management</strong> \u2014 is a two-year joint master\u2019s run by a four-university consortium: <strong>Central European University (Vienna, Austria)</strong>, the <strong>University of the Aegean (Lesvos, Greece)</strong>, <strong>Lund University (Sweden)</strong> and the <strong>University of Manchester (UK)</strong>. CEU administers admissions on behalf of the consortium. The <strong>2027\u20132029 call is officially open</strong>; the 2026\u20132028 cycle is closed.</p>
      <p>A note on funding language: the official 2027 call page confirms <strong>partial tuition-fee waivers and living stipends for outstanding students</strong>. It is <strong>not marketed as a guaranteed full Erasmus Mundus package</strong> for 2027 \u2014 exact award counts and stipend amounts were <strong>not published</strong> at the time of research, so apply early if you need funding.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Open to all nationalities.</strong></li>
        <li>A <strong>good first degree</strong> (bachelor\u2019s or equivalent) in a <strong>relevant field</strong> \u2014 environmental sciences, policy/management, natural or social sciences, engineering or management \u2014 with a <strong>GPA of 3.5 or above</strong>.</li>
        <li>Holders of other degrees may be considered if they demonstrate <strong>commitment to environmental challenges</strong> through work or volunteering.</li>
        <li><strong>English proficiency</strong> required (TOEFL/IELTS scores submitted with the application).</li>
        <li>Admission is <strong>highly competitive</strong> \u2014 academic record and motivation both count.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Partial tuition-fee waivers</strong> for outstanding admitted students.</li>
        <li><strong>Living stipends</strong> for a competitive selection of students (amounts not published for 2027).</li>
        <li>A <strong>joint master\u2019s across four European universities</strong> \u2014 Vienna, Lesvos, Lund and Manchester \u2014 with the Erasmus Mundus network behind it.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>CEU online application form</strong>, completed in full.</li>
        <li><strong>Scanned bachelor\u2019s transcript and diploma</strong> (in English).</li>
        <li>An <strong>essay/statement on career goals</strong>.</li>
        <li><strong>Reference letters</strong> (referees are contacted by email).</li>
        <li><strong>English test scores</strong> (TOEFL/IELTS) and the <strong>CEU application fee</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the official 2027 call page</strong>Read the 2027\u20132029 call at mespom.eu and note which of the three deadlines applies to you.</li>
        <li><strong>Apply via the CEU form</strong>Submit the online application through CEU\u2019s SITS system (linked from the call page) on behalf of the MESPOM Consortium.</li>
        <li><strong>Beat the right deadline</strong>Need funding or a visa? File by <strong>7 January 2027, 23:59 CET</strong>. Self-financing: <strong>15 April 2027</strong> (non-EU/EEA needing a study visa) or <strong>15 July 2027</strong> (visa-free entry to Austria). Questions: <strong>coordinator@mespom.eu</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is MESPOM 2027 fully funded?',
  'The official 2027 call page confirms competitive partial tuition waivers and living stipends \u2014 not a guaranteed full package. Do not assume full funding; apply early and plan backup financing.'),
 ('Which universities will I study at?',
  'The consortium comprises CEU (Vienna, administering), the University of the Aegean (Lesvos), Lund University (Sweden) and the University of Manchester (UK).'),
 ('Is there an English test requirement?',
  'Yes \u2014 English proficiency is required and test scores are part of the application.'),
 ('What is the GPA requirement?',
  'A GPA of 3.5 or above in the first degree is the stated bar; other-degree holders can still qualify with demonstrated environmental commitment.'),
 ('Which deadline applies to me?',
  'Financial-aid seekers and visa-sensitive applicants: 7 Jan 2027. Self-financing non-EU/EEA students needing an Austrian study visa: 15 Apr 2027. Self-financing students with visa-free entry to Austria: 15 Jul 2027 \u2014 all at 23:59 CET.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official mespom.eu 2027\u20132029 call page (consortium, CEU administration, partial waivers/stipends for outstanding students) + the official deadlines-and-admissions-calendar page (7 Jan / 15 Apr / 15 Jul 2027, 23:59 CET) + two agreeing trackers for the document list (the official call page does not enumerate documents). The 2026 cycle deadlines (7 Jan / 15 Apr / 15 Jul 2026) are confirmed past; no fact stated from fewer than two agreeing sources; exact award counts/amounts are explicitly flagged as not published.</p>
''',
 dl_long='7 January 2027, 23:59 CET for financial-aid applicants and visa-sensitive countries; 15 April 2027 (self-financing non-EU/EEA needing a study visa); 15 July 2027 (self-financing with visa-free entry to Austria)',
 offlinks=[('Call for applications 2027\u20132029 \u2014 MESPOM (official)', 'https://mespom.eu/call-applications-2027-2029'),
           ('Application deadlines and admissions calendar \u2014 MESPOM (official)', 'http://mespom.eu/application-deadlines-and-admissions-calendar')],
 related_titles=['global-minds-2027', 'emmir', 'globed', 'each', 'glocal'],
))

A.append(dict(
 slug='tomorrows-leaders-scholarship-2027-28',
 title="Tomorrow's Leaders Scholarship 2027-28 (Fully Funded)",
 meta="Tomorrow's Leaders Scholarship 2027-28: the U.S. State Department's MEPI programme offers fully funded undergraduate study at AUB and LAU in Lebanon \u2014 tuition, housing, insurance, laptop, monthly stipend and two flights home a year. Deadline 18 November 2026.",
 short="Tomorrow's Leaders 2027-28", kicker='Lebanon \u00b7 Undergraduate \u00b7 Fully Funded', mono='TL',
 prov_short='U.S. Department of State (MEPI), administered by FHI 360', prov_cat='Government \u00b7 USA',
 h1="Tomorrow's Leaders Scholarship 2027-28 (Fully Funded)",
 sub='The U.S. State Department\u2019s Middle East Partnership Initiative funds outstanding MENA students through full undergraduate degrees at the American University of Beirut and the Lebanese American University \u2014 tuition, housing, stipend and a semester in the US.',
 dpill='18 Nov 2026 · 28 days to go',
 facts=facts([('Award', 'Fully funded undergraduate study: tuition + enrollment fees (up to 4 academic years), health insurance, housing, visa/residency fees, textbooks, laptop, two round trips home per year, monthly living stipend, internships, faculty mentorship, leadership workshops, one semester of study in the US'),
              ('Eligible', 'Citizens of Algeria, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Syria, Tunisia, Yemen, West Bank; Palestinian students residing in a third country with legal residency; current high-school seniors or 2026 graduates (2025 graduates also eligible for Iraq, Libya, Syria, Yemen, West Bank, third-country Palestinians); English proficiency required; NOT open to US citizens/permanent residents'),
              ('How', 'Online application only via the official program website \u2014 no separate AUB/LAU application needed'),
              ('Deadline', '18 November 2026 (for the 2027\u20132028 intake; applications opened October 2026)'),
              ('Host universities', 'American University of Beirut (AUB) and Lebanese American University (LAU), Lebanon')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Tomorrow\u2019s Leaders Program</strong>, funded by the <strong>U.S. Department of State\u2019s Middle East Partnership Initiative (MEPI)</strong> and administered by <strong>FHI 360</strong>, offers <strong>fully funded undergraduate degrees</strong> to outstanding students from the Middle East and North Africa. Scholars study at two US-accredited universities in <strong>Lebanon</strong> \u2014 the <strong>American University of Beirut (AUB)</strong> and the <strong>Lebanese American University (LAU)</strong> \u2014 with the <strong>opportunity to spend one semester in the United States</strong>.</p>
      <p>The package is genuinely comprehensive: <strong>tuition and enrollment fees</strong> (up to four academic years), <strong>health insurance</strong>, <strong>housing</strong>, <strong>visa and residency fees</strong>, <strong>textbooks and a laptop</strong>, <strong>two round trips home per year</strong>, a <strong>monthly living stipend</strong> during programme activities, <strong>internships</strong>, <strong>faculty mentorship</strong> and <strong>leadership workshops</strong>. Applications for the <strong>2027\u20132028 intake opened in October 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of Algeria, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Syria, Tunisia, Yemen or the West Bank</strong> \u2014 Palestinian students residing in a third country with <strong>legal residency</strong> may also apply.</li>
        <li><strong>US citizens and US permanent residents are NOT eligible.</strong></li>
        <li><strong>Current high-school seniors or 2026 graduates</strong> (2025 graduates are additionally eligible for Iraq, Libya, Syria, Yemen, the West Bank and third-country Palestinians).</li>
        <li><strong>Strong academics</strong>, maturity, flexibility and leadership potential.</li>
        <li><strong>English proficiency required</strong> \u2014 classes are taught in English; a <strong>free ASU online assessment</strong> is part of the application, and <strong>TOEFL/IELTS scores are required only for shortlisted finalists</strong>.</li>
        <li>Must be able to <strong>begin undergraduate studies in August 2027</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and enrollment fees</strong> for up to four academic years.</li>
        <li><strong>Housing, health insurance</strong> and <strong>visa/residency fees</strong> covered.</li>
        <li><strong>Textbooks and a laptop</strong>; <strong>two round trips home per year</strong>; <strong>monthly living stipend</strong> during programme activities.</li>
        <li><strong>Internships, faculty mentorship and leadership workshops</strong> \u2014 plus the chance to spend <strong>one semester studying in the US</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>School transcripts (grades 10\u201312)</strong> and, if graduated, the <strong>graduation certificate/diploma</strong> (with English translations where needed).</li>
        <li><strong>Evidence of extracurricular and volunteer activities.</strong></li>
        <li><strong>Two recommendation letters</strong> (at least one academic).</li>
        <li>The <strong>online English assessment</strong> taken as part of the application.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply online on the program site</strong>Submit the application at tomorrowsleadersprogram.org \u2014 it is the only application you need; <strong>no separate AUB or LAU application is required</strong>.</li>
        <li><strong>Complete the English assessment</strong>Take the free online assessment inside the application; keep TOEFL/IELTS plans only in case you are shortlisted as a finalist.</li>
        <li><strong>File before 18 November 2026</strong>Early applications are encouraged; the portal closes on <strong>18 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Where do scholars actually study?',
  'At the American University of Beirut (AUB) or the Lebanese American University (LAU) in Lebanon \u2014 the programme funds full degrees there, with one optional semester of study in the US.'),
 ('Can US citizens apply?',
  'No \u2014 US citizens and US permanent residents are explicitly excluded.'),
 ('Is there a graduate (master\u2019s) component?',
  'The 2027\u20132028 call being advertised is the undergraduate programme. A graduate track has existed at LAU, but it is not the intake currently advertised \u2014 the details here cover the undergraduate track.'),
 ('Do I need TOEFL or IELTS before applying?',
  'No \u2014 the application includes a free online English assessment; TOEFL or IELTS scores are required only for shortlisted finalists.'),
 ('Can Gaza residents apply?',
  'Some trackers report that Gaza residents cannot apply for this intake because of travel-access limitations, but this is not confirmed on the official programme site \u2014 check with the programme directly if this affects you.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official Tomorrow\u2019s Leaders site (tomorrowsleadersprogram.org: 2027\u20132028 application announcement dated 16 Oct 2026, 18 Nov 2026 deadline, AUB/LAU host universities, eligibility and document checklist) + the LAU partner eligibility page (graduate track context) + independent coverage (Education Post). Stale third-party pages claiming 25 Nov 2026 were discarded in favour of the official 18 Nov 2026 date; the exact monthly stipend is not published; the graduate-track intake status and Gaza-resident reports are explicitly flagged as unconfirmed.</p>
''',
 dl_long='18 November 2026 (2027\u20132028 intake)',
 offlinks=[('Application now open for the 2027\u20132028 Tomorrow\u2019s Leaders Program (official announcement)', 'https://www.tomorrowsleadersprogram.org/blog/2026/10/16/the-application-is-now-open-for-the-2027-2028-tomorrows-leaders-program/'),
           ('Tomorrow\u2019s Leaders Program \u2014 official site', 'https://www.tomorrowsleadersprogram.org/')],
 related_titles=['bu-trustee', 'said', 'concordia-talent', 'reach-oxford', 'echidna-2027'],
))

A.append(dict(
 slug='radboud-scholarship-programme-2027-28-netherlands',
 title='Radboud Scholarship Programme 2027-28 in Netherlands (Funded)',
 meta='Radboud Scholarship Programme 2027-28: Radboud University cuts non-EU/EEA tuition to EUR 2,771 and adds visa costs plus health & liability insurance \u2014 max 26 awards. Living costs NOT covered: it is a partial scholarship. Deadline 31 January 2027.',
 short='Radboud Scholarship Programme 2027-28', kicker='Netherlands \u00b7 Master\u2019s \u00b7 Funded', mono='RU',
 prov_short='Radboud University, Nijmegen', prov_cat='University \u00b7 Netherlands',
 h1='Radboud Scholarship Programme 2027-28 in Netherlands (Funded)',
 sub='Radboud\u2019s merit award for outstanding non-EEA master\u2019s students \u2014 tuition cut to EUR 2,771 plus visa and insurance costs, but no living-cost cover: read the terms honestly.',
 dpill='31 Jan 2027 · 102 days to go',
 facts=facts([('Award', 'Tuition fee reduced to EUR 2,771 (figure to be confirmed) instead of ~EUR 19,000 non-EEA tuition; visa + residence permit costs covered; health + liability insurance (Aon Student Insurance) during the stay; living costs and other study costs NOT covered \u2014 officially classified as a partial scholarship; maximum 26 awards'),
              ('Eligible', 'Non-EU/non-EEA passport holders; not eligible for lower EU/EEA tuition for other reasons; bachelor\u2019s obtained outside the Netherlands; meets the chosen master\u2019s English proficiency requirement; fully admitted to an English-taught master\u2019s starting 1 September 2027; able to comply with Dutch visa conditions; enrolled full-time'),
              ('How', 'No separate scholarship form \u2014 indicate the Radboud Scholarship in the OSIRIS Application for master\u2019s admission; upload 2 reference letters + CV'),
              ('Deadline', 'Initial submission 31 January 2027, 23:59 CET; application file must be complete by 14 February 2027, 23:59 CET; decisions before mid-April 2027'),
              ('Selection', 'Academic excellence, ambition and reference quality \u2014 no published minimum GPA; second-year funding for two-year programmes requires passing all first-year courses')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Radboud Scholarship Programme</strong> at <strong>Radboud University, Nijmegen</strong>, rewards outstanding non-EEA students with a <strong>partial tuition award</strong> for a full English-taught master\u2019s starting <strong>1 September 2027</strong>. Successful scholars pay a <strong>reduced tuition fee of EUR 2,771</strong> (amount to be confirmed) instead of the regular non-EEA fee of <strong>around EUR 19,000</strong> \u2014 a programme-dependent cut \u2014 and the university also covers <strong>visa and residence permit costs</strong> plus <strong>health and liability insurance</strong> (Aon Student Insurance) during the stay.</p>
      <p>Be clear-eyed about what it is not: <strong>living costs and other study costs are not covered</strong>, and Radboud classifies the award as a <strong>partial scholarship</strong>. A maximum of <strong>26 scholarships</strong> is awarded across the faculties \u2014 Arts (2), Law (2), Nijmegen School of Management (5), Philosophy/Theology/Religious Studies (1), Science (9) and Social Sciences (7). For two-year programmes, the <strong>second year requires passing all first-year courses</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>non-EU/non-EEA passport</strong> and be <strong>not eligible for lower EU/EEA tuition</strong> for any other reason.</li>
        <li>Have <strong>obtained a bachelor\u2019s degree outside the Netherlands</strong> (no prior Dutch degree or education; exchange parts of the degree are excluded).</li>
        <li><strong>Fully admitted</strong> to an <strong>English-taught master\u2019s programme</strong> starting <strong>1 September 2027</strong>, and meet the programme\u2019s <strong>English language proficiency requirement</strong>.</li>
        <li><strong>Enrolled as a full-time student</strong> and able to <strong>comply with Dutch visa conditions</strong>.</li>
        <li>Selection is based on <strong>academic excellence, ambition and reference quality</strong> \u2014 the official page publishes <strong>no minimum GPA or test-score threshold</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition reduced to EUR 2,771</strong> (to be confirmed) instead of the regular non-EEA fee.</li>
        <li><strong>Visa and residence permit costs</strong> covered.</li>
        <li><strong>Health and liability insurance</strong> (Aon Student Insurance) during the stay.</li>
        <li>Not covered: <strong>living costs and other study costs</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>standard master\u2019s admission file</strong> \u2014 transcripts, motivation letter for the programme (which feeds the \u201cambition\u201d criterion) and <strong>proof of English proficiency</strong> (recommended before 14 February 2027).</li>
        <li>Three <strong>scholarship-specific</strong> documents: <strong>two reference letters</strong> and a <strong>curriculum vitae</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for master\u2019s admission</strong>Submit your application for an English-taught master\u2019s starting September 2027 in the <strong>OSIRIS Application</strong> system.</li>
        <li><strong>Indicate the scholarship</strong>During the admission application, state that you wish to apply for a Radboud Scholarship and <strong>upload the two reference letters and your CV</strong>.</li>
        <li><strong>Complete the file by the deadlines</strong>Initial submission by <strong>31 January 2027, 23:59 CET</strong>; file fully complete \u2014 handling fee, corrections, documents \u2014 by <strong>14 February 2027, 23:59 CET</strong>. Decisions are communicated <strong>before mid-April 2027</strong>. Enquiries (not applications): <strong>scholarships@ru.nl</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Radboud Scholarship fully funded?',
  'No \u2014 Radboud officially classifies it as a partial scholarship. Tuition is reduced (not eliminated), visa and insurance costs are covered, but living costs are entirely yours to fund.'),
 ('Is there a minimum GPA?',
  'No published minimum GPA or test-score threshold exists on the official page; selection weighs academic excellence, ambition and reference quality.'),
 ('Can current bachelor\u2019s students in the Netherlands apply?',
  'No \u2014 your bachelor\u2019s must have been obtained outside the Netherlands.'),
 ('Is there a separate scholarship application?',
  'No \u2014 the scholarship is requested inside the OSIRIS master\u2019s admission application, with the two reference letters and CV uploaded there.'),
 ('What if my programme is two years long?',
  'The reduced tuition applies for both years, but the second year requires you to pass all first-year courses.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official Radboud Scholarship Programme page (ru.nl: 2027/2028 cycle, 31 Jan 2027 23:59 CET initial + 14 Feb 2027 23:59 CET complete-by, EUR 2,771 reduced tuition to-be-confirmed, visa/permit + Aon insurance covered, living costs excluded, partial classification, max 26 awards with faculty split, second-year progression rule, eligibility and 2-reference+CV document list) + three agreeing independent trackers (YouthExpat, WorldOpportunitiesHub, AfterSchoolAfrica) for the award counts, amounts and deadlines. The 2026/2027 cycle (closed 31 Jan 2026) was excluded.</p>
''',
 dl_long='31 January 2027, 23:59 CET (initial submission); the application file must be complete by 14 February 2027, 23:59 CET',
 offlinks=[('Radboud Scholarship Programme \u2014 Radboud University (official)', 'https://www.ru.nl/en/education/scholarships/radboud-scholarship-programme'),
           ('Radboud Scholarship Programme 2027 \u2014 YouthExpat (independent corroboration)', 'https://youthexpat.com/2026/10/05/radboud-scholarship-programme-2/'),
           ('Radboud Scholarship Programme 2027 \u2014 WorldOpportunitiesHub (independent corroboration)', 'https://worldopportunitieshub.com/opportunities/scholarship/radboud-scholarship-programme-2027-study-your-masters-in-the-netherlands')],
 related_titles=['uva-merit-2027', 'tudelft-excellence-2027', 'maastricht', 'tue-excellence', 'tilburg-rm'],
))

A.append(dict(
 slug='imperial-college-mba-scholarships-2027-uk',
 title='Imperial College MBA Scholarships 2027 in UK (Funded)',
 meta='Imperial College MBA Scholarships 2027: Imperial Business School\u2019s suite of MBA awards from 20% to 100% tuition \u2014 Dean\u2019s Impact, Advisory Board, Fort\u00e9, Female Future Leaders (GBP 20,000) and more. Self-funded applicants auto-evaluated; next deadline Round 2, 12 January 2027.',
 short='Imperial College MBA Scholarships 2027', kicker='UK \u00b7 MBA \u00b7 Funded', mono='IC',
 prov_short='Imperial College Business School', prov_cat='University \u00b7 UK',
 h1='Imperial College MBA Scholarships 2027 in UK (Funded)',
 sub='Imperial\u2019s suite of Full-Time MBA awards \u2014 20% to 100% tuition reductions across named scholarships for leadership, innovation, diversity and social impact.',
 dpill='12 Jan 2027 (Round 2) · 83 days to go',
 facts=facts([('Award', 'Multiple targeted scholarships awarded as tuition-fee reductions, from 20% up to 100% of tuition, incl. Dean\u2019s Impact, Advisory Board, Fort\u00e9 Fellowship, Sir Andrew Witty (healthcare), Military & Public Service, ROMBA, Imperial Alumni, Discretionary and Female Future Leaders (GBP 20,000 for 2027\u201328)'),
              ('Eligible', 'Self-funded international applicants worldwide to the Full-Time MBA (12 months, September 2027 start); strong academic merit, professional achievement and leadership impact; some awards require GMAT/GRE scores and references'),
              ('How', 'Self-funded MBA applicants are automatically evaluated for eligible internal awards on applying; the offer email explains how to complete the scholarship written/video assessment'),
              ('Deadlines (2027 intake)', 'Round 1: 22 Sep 2026 (passed); Round 2: 12 Jan 2027; Round 3: 16 Mar 2027; Round 4: 11 May 2027 \u2014 apply earlier: awards are limited and the Advisory Board Scholarship is rounds 1\u20132 only'),
              ('Programme', 'Master of Business Administration, full-time, 12 months, London, starting September 2027')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Imperial College Business School</strong> funds its <strong>Full-Time MBA</strong> (a 12-month programme starting <strong>September 2027</strong>) through a suite of <strong>named scholarships</strong> rather than a single award \u2014 from the <strong>Dean\u2019s Impact Scholarship</strong> (entrepreneurship, technology and innovation, sustainability, social impact, leadership) and the <strong>Advisory Board Scholarship</strong>, to the <strong>Fort\u00e9 Fellowship</strong> (women leaders), the <strong>Sir Andrew Witty Scholarship</strong> (healthcare leadership), the <strong>Military &amp; Public Service Scholarship</strong>, the <strong>ROMBA Fellowship</strong>, the <strong>Imperial Alumni Scholarship</strong> and discretionary awards \u2014 plus the <strong>Female Future Leaders Scholarship (GBP 20,000)</strong> listed for 2027\u201328 entry.</p>
      <p>Awards are <strong>tuition-fee reductions ranging from 20% up to 100% of tuition</strong>, allocated across the admissions rounds. <strong>Self-funded applicants are automatically evaluated</strong> for eligible internal awards when they apply to the MBA \u2014 there is no separate scholarship application portal for most awards.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Self-funded applicant</strong> to the <strong>Full-Time MBA</strong> starting <strong>September 2027</strong> (other MBA formats \u2014 Executive, Weekend, Global Online \u2014 have separate opportunities).</li>
        <li><strong>Strong academic merit and professional achievement</strong>, with demonstrated leadership impact.</li>
        <li>Some awards add conditions: <strong>GMAT/GRE scores and references</strong> for certain scholarships; the <strong>Advisory Board Scholarship requires applying in rounds one or two</strong>; the <strong>Female Future Leaders award</strong> is open to Home and Overseas fee-status applicants.</li>
        <li><strong>New entrants only</strong> \u2014 students already studying the course are not eligible.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition-fee reductions from 20% up to 100%</strong> of the Full-Time MBA fees.</li>
        <li>Named awards targeting impact areas \u2014 <strong>Dean\u2019s Impact, Advisory Board, Fort\u00e9, Sir Andrew Witty, ROMBA, Alumni, Discretionary</strong>.</li>
        <li><strong>Female Future Leaders: GBP 20,000</strong> towards 2027\u201328 MBA costs (Home and Overseas fee status).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>complete Imperial MBA application</strong> \u2014 CV, transcripts, references and essays; strong evidence of impact in the award\u2019s focus area.</li>
        <li><strong>GMAT or GRE scores</strong> where the award requires them.</li>
        <li>The <strong>written/video assessment Imperial invites</strong> after a course offer (details arrive in the offer email \u2014 about two weeks after the offer for most awards).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to the Full-Time MBA in an early round</strong>Submit the MBA application by the round deadline \u2014 <strong>Round 2 closes 12 January 2027</strong>. Round 1 (22 Sep 2026) has passed.</li>
        <li><strong>Get evaluated automatically</strong>As a self-funded applicant you are automatically considered for eligible internal scholarships; your <strong>offer email explains the scholarship written/video assessment</strong>.</li>
        <li><strong>Note round-sensitive awards</strong>The <strong>Advisory Board Scholarship is available only in rounds one and two</strong> (final recipients notified by May), so apply in Round 2 at the latest if it fits your profile.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a separate scholarship application form?',
  'For most internal awards, no \u2014 self-funded applicants are automatically evaluated when they apply to the MBA. Imperial invites scholarship assessments through the offer email.'),
 ('Which admissions round should I target?',
  'Round 2 (12 January 2027) \u2014 Round 1 has passed, and Imperial allocates awards across the cycle with limited numbers, so earlier rounds are better. The Advisory Board Scholarship is rounds 1\u20132 only.'),
 ('Are the scholarships full tuition?',
  'Award values vary from 20% up to 100% tuition depending on the scholarship and the round; do not assume a full award.'),
 ('I am a Home (UK) applicant. Am I eligible?',
  'Most awards are open to self-funded applicants worldwide; the Female Future Leaders Scholarship is explicitly open to both Home and Overseas fee-status applicants.'),
 ('Do I need GMAT or GRE?',
  'Some awards require a GMAT or GRE score \u2014 check the criteria for the specific scholarship you are targeting.'),
]) + '''
      <p class="verify">Verified 21 Oct 2026 via three agreeing sources (Pontly: R1 22 Sep 2026 / R2 12 Jan 2027 / R3 16 Mar 2027 / R4 11 May 2027, 20%\u2013100% tuition awards, auto-evaluation for self-funded applicants; mim-essay.com: same round dates with decision timelines, named-award profile table, rounds-1\u20132 Advisory Board limit; the official Imperial Dean\u2019s Impact Scholarship page (imperial.ac.uk) confirming the award exists and new-entrants-only rule) + Scholar Gem for the Female Future Leaders GBP 20,000 2027\u201328 listing. Round 1 has passed; the figures stated come from two agreeing sources.</p>
''',
 dl_long='Round 2: 12 January 2027 (Round 1, 22 Sep 2026, has passed; Round 3: 16 March 2027; Round 4: 11 May 2027)',
 offlinks=[('Imperial College London MBA Scholarships 2027 \u2014 Pontly', 'https://www.pontly.africa/blog/imperial-college-london-mba-scholarships-2027-full-time-mba-funding-in-the-uk'),
           ('Imperial College London MBA Scholarships 2027 \u2014 mim-essay.com', 'https://www.mim-essay.com/imperial-college-london-mba-scholarships'),
           ('Dean\u2019s Impact Scholarship \u2014 Imperial College London (official)', 'https://www.imperial.ac.uk/study/fees-and-funding/scholarships-search/deans-impact-scholarship-20262027.php')],
 related_titles=['bi-presidential', 'weidenfeld-hoffmann-2027', 'clarendon', 'said', 'reach-oxford'],
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
        for token in ('AICTE Pragati', 'Lorem'):
            if token in t: bad.append((slug, 'template leftover: ' + token))
        if 'href="#"' in t: bad.append((slug, 'dead anchor'))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

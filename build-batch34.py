#!/usr/bin/env python3
"""Batch 34 build: 5 verified articles (CERN Research Fellowship 2026,
FASPE 2027, Polimi merit scholarships 2027-28, Swiss Government
Excellence Scholarships 2027-28, Fulbright Swedish Scholar Program 2027-28).
Queue "2026" labels were stale; every article is written for the live cycle
and states the academic year explicitly. Fulbright Swedish is NOT marketed
as fully funded (fixed SEK grant), per the official page.
Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'cern-rf-2026': {'mono': 'CERN', 'title': 'CERN Research Fellowship 2026 in Switzerland (Fully Funded)',
   'href': 'cern-research-fellowship-2026.html',
   'dpill': '2 Nov 2026 \u00b7 11 days to go',
   'award': 'Tax-free CHF 7,004\u20137,425/month + health insurance, pension, family allowances, relocation',
   'elig': 'PhD in theoretical physics; \u22646 yrs post-PhD; never held a CERN fellow/graduate contract.',
   'tags': [('Fellowship', 'blue'), ('Switzerland', 'teal')]},
 'faspe-2027': {'mono': 'FA', 'title': 'FASPE Fellowship 2027 in Germany and Poland (Fully Funded)',
   'href': 'faspe-fellowship-2027.html',
   'dpill': '3 Jan 2027 \u00b7 73 days to go',
   'award': 'Fully funded 2-week ethics fellowship: flights, hotels, meals, materials covered',
   'elig': 'Graduate students or early-career professionals; 6 tracks; all nationalities.',
   'tags': [('Fellowship', 'blue'), ('Germany', 'teal')]},
 'polimi-2027': {'mono': 'PM', 'title': 'Politecnico di Milano Scholarships 2027-28 in Italy (Fully Funded)',
   'href': 'polimi-scholarships-2027-28.html',
   'dpill': '15 Dec 2026 \u00b7 54 days to go',
   'award': 'Full tuition waiver + up to \u20ac10,000/year (merit awards)',
   'elig': 'International applicants to first-year English-taught MSc; fee paid by 1 Dec 2026.',
   'tags': [("Master\u2019s", 'blue'), ('Italy', 'teal')]},
 'sges-2027': {'mono': 'CH', 'title': 'Swiss Government Excellence Scholarships 2027-28 (Funded)',
   'href': 'swiss-government-scholarships-2027-28.html',
   'dpill': 'Varies by country \u00b7 Aug\u2013Nov 2026',
   'award': 'Monthly stipend + health insurance + housing & travel allowances (tuition not covered)',
   'elig': 'Master\u2019s holders (research) / PhD holders (postdoc); Swiss supervisor invitation required.',
   'tags': [('PhD', 'blue'), ('Switzerland', 'teal')]},
 'fulbright-se-2027': {'mono': 'FS', 'title': 'Fulbright Swedish Scholar Program 2027-28 in USA (Grant)',
   'href': 'fulbright-swedish-scholar-program-2027-28.html',
   'dpill': '11 Jan 2027 \u00b7 81 days to go',
   'award': 'SEK 50,000 grant + SEK 15,000 travel allowance + visa fees + insurance (partial grant)',
   'elig': 'Swedish citizens; doctoral degree; established US host affiliation; 3\u201312 month stay.',
   'tags': [('Scholarship', 'blue'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='cern-research-fellowship-2026',
 title='CERN Research Fellowship 2026 in Switzerland (Fully Funded)',
 meta='CERN Research Fellowship 2026: a tax-free postdoctoral fellowship in Geneva with a CHF 7,004\u20137,425/month stipend, health insurance, pension and relocation support. Theoretical Physics track closes 2 Nov 2026.',
 short='CERN Research Fellowship 2026', kicker='Switzerland \u00b7 Postdoc \u00b7 Fully Funded', mono='CERN',
 prov_short='CERN (European Organization for Nuclear Research)', prov_cat='Research \u00b7 Switzerland',
 h1='CERN Research Fellowship 2026 in Switzerland (Fully Funded)',
 sub='A tax-free postdoctoral fellowship at the world\u2019s largest particle-physics laboratory \u2014 two years of independent research in Geneva with full benefits.',
 dpill='2 November 2026, 23:59 CET \u00b7 11 days to go',
 facts=facts([('Award', 'Tax-free net stipend of CHF 7,004\u20137,425/month (degree-dependent), health insurance, CERN Pension Fund membership, family/child/infant allowances, relocation package, 30 days paid leave + 2 weeks annual closure, and training including language classes'),
              ('Eligible', 'PhD in theoretical physics (or defence scheduled); \u22646 years post-PhD research experience; not current CERN staff; never held a CERN fellow or graduate contract'),
              ('Contract', '24-month full-time employment contract, extendable to 36 months; ideal start 1 October 2027'),
              ('How', 'Apply online via CERN\u2019s recruitment portal; forward the referee link to three referees who upload letters confidentially before the deadline'),
              ('Deadline', '2 November 2026, 23:59 CET \u2014 Theoretical Physics track (2026 call). Other 2026 tracks have closed.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>CERN Research Fellowship Programme</strong> hires early-career physicists to lead their <strong>own independent research programme</strong> at CERN in Geneva, alongside members of one of the laboratory\u2019s research groups. This is not a degree grant \u2014 it is a <strong>salaried postdoctoral appointment</strong> with a 24-month employment contract that can extend to 36 months.</p>
      <p>The currently open vacancy is the <strong>Theoretical Physics track of the 2026 call</strong> (reference TH-2026-1/Cat1). Earlier 2026 tracks, including experimental physics, have already closed. If you work in theory, the window is still open \u2014 but only until <strong>2 November 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>PhD in theoretical physics</strong> by the application deadline (a defence already scheduled also qualifies; the degree must be completed before taking up the appointment).</li>
        <li><strong>No more than six years</strong> of research experience after the PhD by the start of the contract.</li>
        <li>Must <strong>not be a current CERN staff member</strong> and must <strong>never have held a CERN fellow or graduate contract</strong>.</li>
        <li>The vacancy notice states <strong>no nationality restriction</strong>, but requirements can differ between tracks \u2014 always read the notice for your field.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tax-free net stipend of CHF 7,004 or 7,425 per month</strong>, depending on the degree.</li>
        <li><strong>Comprehensive health insurance</strong> for the fellow, spouse and children, plus <strong>CERN Pension Fund membership</strong>.</li>
        <li><strong>Family, child and infant monthly allowances</strong> and a <strong>relocation package</strong> (installation grant and travel expenses).</li>
        <li><strong>30 days of paid leave per year</strong> plus CERN\u2019s 2-week annual closure.</li>
        <li>On-the-job and formal <strong>training, including language classes</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV</strong> in English or French.</li>
        <li>Copy of the <strong>most relevant diploma</strong> or certificate of achievement from the university.</li>
        <li><strong>Statement of research interests</strong> outlining your plans for the fellowship.</li>
        <li><strong>Three recent letters of recommendation</strong> (not older than one year at the application deadline), uploaded <strong>confidentially by the referees</strong> \u2014 not by the applicant.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm the track</strong>Check the Theoretical Physics vacancy notice on CERN Careers and make sure your profile fits the requirements.</li>
        <li><strong>Submit the online application</strong>Apply through CERN\u2019s recruitment portal (SmartRecruiters) before <strong>2 November 2026, 23:59 CET</strong>.</li>
        <li><strong>Forward the referee link</strong>After submitting, send the referee submission link you receive to your three referees.</li>
        <li><strong>Chase the letters</strong>Make sure referees upload their letters confidentially before the closing date \u2014 late letters are not accepted.</li>
        <li><strong>Await the outcome</strong>The ideal start date is 1 October 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the CERN Research Fellowship a degree scholarship?',
  'No. It is a salaried postdoctoral fellowship: a full-time, 24-month employment contract at CERN in Geneva, extendable to 36 months.'),
 ('Who can apply for the 2026 call?',
  'PhD holders in theoretical physics with no more than six years of post-PhD research experience. CERN staff, and anyone who has previously held a CERN fellow or graduate contract, are ineligible.'),
 ('Is there a nationality restriction?',
  'The Theoretical Physics vacancy notice states none. Requirements can differ between tracks, so always check the specific vacancy notice for your field.'),
 ('How much is the stipend and is it tax-free?',
  'The net monthly stipend is CHF 7,004 or 7,425 depending on the degree, and it is paid tax-free, with health insurance, pension membership, family allowances and a relocation package on top.'),
 ('Can my referees email the letters to me for upload?',
  'No \u2014 the three letters must be uploaded confidentially by the referees themselves through the link you forward to them.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via CERN\u2019s official vacancy notice on its SmartRecruiters recruitment portal (Ref TH-2026-1/Cat1: stipend, contract length, eligibility, referee process, 2 Nov 2026 deadline) + corroborating mirrors of the programme\u2019s 2026 postings (experimental physics call closed 01/09/2026). This article covers the Theoretical Physics track of the 2026 call, the still-open vacancy; other 2026 tracks closed earlier.</p>
''',
 dl_long='2 November 2026, 23:59 CET \u2014 Theoretical Physics track (2026 call). Other 2026 tracks have already closed.',
 offlinks=[('Official vacancy notice: Research Fellowship (Theoretical Physics) \u2014 Ref TH-2026-1/Cat1', 'https://jobs.smartrecruiters.com/CERN/744000150312819-research-fellowship-theoretical-physics'),
           ('CERN Careers', 'https://careers.cern')],
 related_titles=['nasa-hubble', 'iiser-pdrf', 'ramanujan', 'perugia-phd', 'justcool'],
))

A.append(dict(
 slug='faspe-fellowship-2027',
 title='FASPE Fellowship 2027 in Germany and Poland (Fully Funded)',
 meta='FASPE Fellowship 2027: a fully funded two-week ethics fellowship in Germany and Poland for graduate students and early-career professionals. Flights, hotels, meals and materials covered. Apply by 3 Jan 2027.',
 short='FASPE Fellowship 2027', kicker='Germany & Poland \u00b7 Short Programme \u00b7 Fully Funded', mono='FA',
 prov_short='Fellowships at Auschwitz for the Study of Professional Ethics (FASPE)', prov_cat='Fellowship \u00b7 Ethics Education',
 h1='FASPE Fellowship 2027 in Germany and Poland (Fully Funded)',
 sub='A fully funded two-week fellowship examining professional ethics through the history of the Holocaust \u2014 for graduate students and early-career professionals in six fields.',
 dpill='3 January 2027, 11:59 PM ET \u00b7 73 days to go',
 facts=facts([('Award', 'Fully funded: round-trip airfare (international travel to Berlin covered for all Fellows), all in-country transport, hotels, admission fees, programme materials, group meals and pocket money for non-group meals'),
              ('Eligible', 'Enrolled in a graduate programme, or holding an undergraduate or graduate degree while working in a related field; generally \u226410 years of professional experience; all nationalities'),
              ('Tracks', 'Six tracks: Business, Clergy & Religious Leaders, Design & Technology, Journalism, Law, or Medical \u2014 apply to one'),
              ('How', 'Apply online via the Submittable portal: form, CV, transcripts, track-specific essays; two recommendation letters submitted directly by referees'),
              ('Deadline', '3 January 2027, 11:59 PM ET \u2014 2027 cycle now officially open (the 2026 cycle closed 4 Jan 2026)')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p><strong>FASPE (Fellowships at Auschwitz for the Study of Professional Ethics)</strong> runs a <strong>two-week, fully funded fellowship</strong> in Germany and Poland where graduate students and early-career professionals study <strong>professional ethics through the history of the Holocaust</strong>. The 2027 cycle is now <strong>officially open for applications</strong> \u2014 the 2026 cycle closed on 4 January 2026, so this article covers the current 2027 intake.</p>
      <p>Six tracks are offered \u2014 <strong>Business, Clergy & Religious Leaders, Design & Technology, Journalism, Law, and Medical</strong> \u2014 and each applicant chooses one. The programme is fully funded for every Fellow, including international travel to Berlin, so participation does not depend on financial means.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Enrolled in a graduate programme</strong>, OR have completed an undergraduate degree and be working in a related field, OR have completed a graduate degree and be working in a related field.</li>
        <li>Preparing for or in the <strong>early stages of a career</strong> \u2014 total professional experience generally <strong>not exceeding 10 years</strong>.</li>
        <li><strong>Open to all nationalities and residencies</strong> \u2014 you do not need to be American or live in the US. Fellows arrange their own visas; FASPE provides supporting documentation.</li>
        <li>Apply to <strong>one of the six tracks</strong> listed above.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Round-trip economy airfare</strong>, including international travel to Berlin for non-US Fellows.</li>
        <li><strong>All transportation</strong> for group travel and activities in Germany and Poland.</li>
        <li><strong>All hotel costs, admission fees and programme materials.</strong></li>
        <li><strong>All group meals</strong>, plus <strong>pocket money</strong> for non-group meals.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed online application form</strong> via Submittable.</li>
        <li><strong>Updated resume/CV</strong> and <strong>transcripts</strong> (unofficial accepted \u2014 no portal screenshots).</li>
        <li><strong>Short essay responses</strong> specific to the chosen fellowship track.</li>
        <li><strong>Two letters of recommendation</strong>, submitted <strong>directly by the referees</strong>. Trackers cite a recommender deadline of 10 January 2027, which was not seen on the official FAQ \u2014 confirm on Submittable and get letters in early.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your track</strong>Pick one of the six FASPE fellowship tracks on faspe-ethics.org.</li>
        <li><strong>Start on Submittable</strong>Begin the application on the Submittable portal and complete the online form.</li>
        <li><strong>Upload materials</strong>Attach your CV and transcripts, and answer the track-specific short essay questions.</li>
        <li><strong>Enter recommender details</strong>Submit your referees\u2019 details so they receive the upload link directly.</li>
        <li><strong>Submit by the deadline</strong>Submit the full application by <strong>3 January 2027, 11:59 PM ET</strong>; ensure recommenders submit their letters by 10 January 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need to be American or live in the US to apply?',
  'No. FASPE accepts all eligible applicants regardless of citizenship or residency; international Fellows\u2019 travel to Berlin is also covered.'),
 ('I\u2019m no longer a student. Can I still apply?',
  'Yes. All FASPE programmes accept early-career professionals, generally with no more than 10 years of professional experience.'),
 ('Is the fellowship fully funded?',
  'Yes. FASPE covers programme costs and travel so that financial ability does not affect participation.'),
 ('When does the 2027 programme run?',
  'The programme runs for two weeks; for example, the 2027 Journalism track runs 18 June \u2013 2 July 2027.'),
 ('Do I need to arrange my own visa?',
  'Yes, Fellows arrange their own visas, but FASPE provides supporting documentation for the application.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official provider site (faspe-ethics.org FAQs and Journalism pages: 2027 call open, 3 Jan 2027 deadline, eligibility, funding coverage, six tracks) + corroborating trackers (fundsforngos, fellowshipsguide, globalsouthopportunities) on benefits/documents + scholarshipunion and scholarships.af confirming the 2026-cycle closure (deadline 4 Jan 2026). The 10 Jan 2027 recommender deadline is reported by two trackers only and is explicitly flagged as unconfirmed on the official FAQ \u2014 confirm it on Submittable.</p>
''',
 dl_long='3 January 2027, 11:59 PM ET \u2014 2027 cycle (now officially open; the 2026 cycle closed 4 Jan 2026).',
 offlinks=[('FASPE FAQs (official)', 'https://www.faspe-ethics.org/faqs/'),
           ('FASPE Journalism fellowship (official)', 'https://www.faspe-ethics.org/journalism/')],
 related_titles=['nyt-fellowship', 'dw-2028', 'echidna-2027', 'harvard-lead', 'ccp-2027'],
))

A.append(dict(
 slug='polimi-scholarships-2027-28',
 title='Politecnico di Milano Scholarships 2027-28 in Italy (Fully Funded)',
 meta='Politecnico di Milano scholarships 2027-28: merit-based full tuition waiver for international Master\u2019s students, with up to \u20ac10,000/year on some awards. Apply for admission by 1 Dec and the scholarship by 15 Dec 2026.',
 short='Politecnico di Milano Scholarships 2027-28', kicker='Italy \u00b7 Master\u2019s \u00b7 Fully Funded', mono='PM',
 prov_short='Politecnico di Milano (Polytechnic University of Milan)', prov_cat='University \u00b7 Italy',
 h1='Politecnico di Milano Scholarships 2027-28 in Italy (Fully Funded)',
 sub='Merit-based scholarships for international students entering English-taught Master\u2019s programmes \u2014 a full tuition waiver with up to \u20ac10,000 a year on top.',
 dpill='15 December 2026, 12:00 noon (Italian time) \u00b7 54 days to go',
 facts=facts([('Award', 'Full tuition fee waiver (only ~\u20ac170 administrative fee + insurance still payable); some merit awards add a gross allowance of up to \u20ac10,000 per year'),
              ('Eligible', 'International students applying to the first year of an English-taught Master of Science programme (September 2027 intake); admission fee paid between 1 October and 1 December 2026; valid English certificate verified by the International Students Office'),
              ('Selection', 'Purely merit-based \u2014 GPA, academic match, documents, and portfolio where requested'),
              ('How', 'Apply for admission first (fee paid by 1 Dec 2026), then submit the separate scholarship form via Politecnico di Milano Online Services by 15 Dec 2026, 12:00 noon Italian time'),
              ('Deadline', '15 December 2026, 12:00 noon (Italian time) \u2014 open 2027-28 call. Admission application fee must be paid between 1 October and 1 December 2026.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Politecnico di Milano (Polimi)</strong>, Italy\u2019s leading technical university, runs a <strong>merit-based international scholarship call</strong> for students entering its English-taught <strong>Master of Science programmes</strong>. The current open round covers the <strong>2027-28 academic year</strong> \u2014 the 2026-27 cycle (deadlines 29 January / 31 March 2026) is closed, so apply only to this round.</p>
      <p>The scholarship pairs a <strong>full tuition fee waiver</strong> with, on some awards, a <strong>gross allowance of up to \u20ac10,000 per year</strong>. Only the administrative fee (around \u20ac170) and insurance are still payable. Selection is <strong>purely merit-based</strong>: your GPA, the academic match with the programme, your documents, and a portfolio where the programme asks for one.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International students</strong> applying to the <strong>first year of an English-taught Master of Science programme</strong> for the <strong>September 2027 intake</strong>.</li>
        <li>Must have <strong>submitted the admission application and paid the application fee between 1 October and 1 December 2026</strong>.</li>
        <li>Must be <strong>admitted to the degree programme</strong> and accept the evaluation outcome.</li>
        <li>Must hold a <strong>valid English language certificate</strong> verified by the International Students Office.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee waiver</strong> for the academic year (Silver scholarships) \u2014 only the administrative fee and insurance remain payable.</li>
        <li><strong>Up to \u20ac10,000 per year gross allowance</strong> on some merit awards.</li>
        <li>No income test \u2014 the awards are allocated <strong>entirely on academic merit</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Online admission application</strong> for the MSc programme with the <strong>application fee receipt</strong>.</li>
        <li><strong>Scholarship application form</strong> submitted through <strong>Politecnico di Milano Online Services</strong>.</li>
        <li><strong>Valid English language certificate</strong> (verified by the International Students Office).</li>
        <li><strong>Academic transcripts and degree documents.</strong></li>
        <li><strong>Portfolio</strong> \u2014 required for Design and Architecture programmes.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission</strong>Submit the admission application for a first-year English-taught MSc programme and pay the application fee between <strong>1 October and 1 December 2026</strong>.</li>
        <li><strong>Submit the scholarship form</strong>File the separate scholarship application in Politecnico di Milano Online Services between 1 October and <strong>12:00 noon (Italian time) on 15 December 2026</strong>.</li>
        <li><strong>Upload the language certificate</strong>Get your English certificate verified by the International Students Office within the stated deadline.</li>
        <li><strong>Await the decision</strong>The Commission\u2019s decision is communicated within <strong>three to four months</strong> of the deadline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I hold another scholarship alongside the Polimi merit scholarship?',
  'No. The Merit Based International Scholarship is incompatible with other scholarships from Polimi or any other public or private body, except mobility-programme grants. If you receive an incompatible award, you must choose one within ten days.'),
 ('Is there a separate application for the scholarship?',
  'Yes. Admission alone does not count \u2014 only international students who have already applied for admission may submit the separate scholarship form in Online Services.'),
 ('What does the tuition waiver not cover?',
  'The administrative fee (around \u20ac170) and insurance are not covered by the waiver.'),
 ('When will I know the result?',
  'The outcome is communicated within three to four months after the application deadline.'),
 ('Can the \u20ac10,000 allowance be renewed for the second year?',
  'The official call PDF describes the award for the academic year in which it is granted; renewal terms are set out in the call document \u2014 read it before applying.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official polimi.it Merit-Based Call for Applications PDF for a.y. 2027-2028 (open Oct 1 \u2013 Dec 15, 2026, tuition waiver, up to \u20ac10,000 allowance, incompatible-scholarship rule, application-fee window) + two agreeing trackers (greatyop.com, opportunitiesng.com) on the allowance figure and waiver terms. The 2026-27 cycle is confirmed closed; the only currently open call is the 2027-28 round, and the article is framed accordingly.</p>
''',
 dl_long='15 December 2026, 12:00 noon (Italian time) \u2014 open 2027-28 call. Admission application fee must be paid between 1 Oct and 1 Dec 2026.',
 offlinks=[('Merit-Based Call for Applications a.y. 2027-2028 (official PDF)', 'https://www.polimi.it/fileadmin/user_upload/futuri_studenti/borse-di-studio/Merit_Based_Call_For_Applications_a.y._2027-2028.pdf')],
 related_titles=['polito-42', 'italy-guide', 'unil', 'warwick-2027', 'tudelft-excellence-2027'],
))

A.append(dict(
 slug='swiss-government-scholarships-2027-28',
 title='Swiss Government Excellence Scholarships 2027-28 (Funded)',
 meta='Swiss Government Excellence Scholarships 2027-28: postgraduate research, PhD and postdoc scholarships in Switzerland with monthly stipend, health insurance and allowances. Deadlines vary by country (Aug\u2013Nov 2026); tuition not covered.',
 short='Swiss Government Excellence Scholarships 2027-28', kicker='Switzerland \u00b7 Postgraduate \u00b7 Funded', mono='CH',
 prov_short='Swiss Confederation \u2014 Federal Commission for Scholarships for Foreign Students (FCS)', prov_cat='Government \u00b7 Switzerland',
 h1='Swiss Government Excellence Scholarships 2027-28 (Funded)',
 sub='Switzerland\u2019s federal scholarships for postgraduate researchers from 180+ countries \u2014 monthly stipend, insurance and allowances, with country-specific deadlines running through November 2026.',
 dpill='Varies by country \u00b7 Aug\u2013Nov 2026 (India: 10 Nov 2026)',
 facts=facts([('Award', 'Monthly living stipend (around CHF 2,450 for 2027-28 research fellowships \u2014 confirm on your country page), mandatory Swiss health insurance (non-EU/EFTA), one-off housing allowance, public-transport card, and a lump-sum flight allowance for grantees outside continental Europe. Tuition/semester fees are NOT included.'),
              ('Eligible', 'Citizens of 180+ eligible countries; Master\u2019s completed (research fellowship / doctoral scholarship) or PhD completed (postdoctoral route \u2014 note new postdoc applications via ETH are no longer possible); confirmed Swiss academic supervisor with invitation letter; not resident in Switzerland for more than one year before the start'),
              ('How', 'Secure a Swiss supervisor and invitation letter first; check your country-of-origin page for the exact deadline and eligible types; apply in the GO-ESKAS portal \u2014 no email or paper submissions'),
              ('Deadline', 'No single deadline \u2014 varies by country, 20 August to late November 2026 for the 2027-28 intake (e.g. India 10 Nov 2026, Pakistan 31 Oct 2026; ETH window 20 Aug \u2013 30 Nov 2026)'),
              ('Decision', 'Announced by the end of May')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>Each year the <strong>Swiss Confederation</strong> funds postgraduate researchers from more than <strong>180 countries</strong> through the <strong>Federal Commission for Scholarships for Foreign Students (FCS)</strong>. The scholarships cover <strong>research fellowships, doctoral scholarships and (where still available) postdoctoral grants</strong> \u2014 they are for postgraduate research only, not for undergraduate study or a first Master\u2019s degree.</p>
      <p>The <strong>2027-28 call is open now</strong>, with country-specific deadlines running from August through November 2026. This article covers the 2027-28 intake \u2014 the 2026 cycle is closed. A separate art-track scheme exists but is not covered here.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizens of one of the 180+ eligible countries</strong> \u2014 check the country-specific page, because offer types vary.</li>
        <li><strong>Master\u2019s degree completed</strong> (research fellowship or doctoral scholarship) or <strong>PhD completed</strong> (postdoctoral route \u2014 note ETH\u2019s page says new postdoc applications are no longer possible).</li>
        <li>A <strong>confirmed Swiss academic supervisor with an invitation letter</strong> \u2014 the research track is not open without one.</li>
        <li>Must <strong>not have lived in Switzerland for more than one year</strong> before the scholarship start.</li>
        <li>Age and degree-date limits <strong>vary by country</strong> (e.g. India: born after 31 December 1991, Master\u2019s by 31 July 2027).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend</strong> covering basic living costs (reported around CHF 2,450 for 2027-28 research fellowships \u2014 confirm on the official page for your country).</li>
        <li><strong>Mandatory Swiss health insurance</strong> covered by the FCS (non-EU/EFTA grantees).</li>
        <li><strong>One-time housing allowance</strong> plus a <strong>public-transport card</strong>.</li>
        <li><strong>Lump-sum flight allowance</strong> home at the end of the programme for grantees from outside continental Europe.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Online application in the GO-ESKAS portal</strong> \u2014 email or paper submissions are not accepted.</li>
        <li><strong>Detailed research proposal.</strong></li>
        <li><strong>CV and academic transcripts.</strong></li>
        <li><strong>Invitation letter</strong> from a Swiss academic supervisor.</li>
        <li><strong>Recommendation letters</strong> and proof of meeting your country\u2019s deadlines.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find a supervisor</strong>Identify a Swiss professor willing to supervise your research and obtain an invitation letter \u2014 this comes first.</li>
        <li><strong>Check your country page</strong>Open your country-of-origin page to confirm the exact deadline and the scholarship types you may apply for.</li>
        <li><strong>Register on GO-ESKAS</strong>Prepare and submit the full application in the GO-ESKAS portal before your country\u2019s deadline.</li>
        <li><strong>Preliminary selection</strong>National authorities and the Swiss diplomatic representation shortlist candidates.</li>
        <li><strong>FCS assessment</strong>The Commission assesses candidate profile, project quality and research-cooperation potential; the final decision arrives by the end of May.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a supervisor before applying?',
  'Yes for the research tracks \u2014 ETH\u2019s page states you can only submit once a professor has agreed to supervise you and issued an invitation letter.'),
 ('Are tuition fees covered?',
  'No. Tuition and semester fees (CHF 600\u20132,000 per semester depending on the university) must be paid separately from the stipend.'),
 ('Is there a single deadline?',
  'No. Deadlines differ by country and all fall in autumn 2026 for the 2027-28 intake; check the page for your passport country.'),
 ('Can I apply if I have already lived in Switzerland?',
  'Only if you have resided there for no more than one year during the application process.'),
 ('How long does the scholarship run?',
  'The research fellowships are awarded for the 2027-28 academic year, extendable under the programme rules \u2014 check the country page for exact durations.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via ETH Zurich\u2019s official Swiss Government Excellence Scholarships page (20 Aug \u2013 30 Nov 2026 window, supervisor-invitation requirement) + the Swiss Embassy (Pakistan) announcement and LeapScholar confirming the 2027-28 intake and country deadlines (India 10 Nov 2026, Pakistan 31 Oct 2026). The article is framed for the 2027-28 intake \u2014 the \u20182026\u2019 cycle is closed \u2014 and the deadline is presented as country-dependent, not a single date. The CHF 2,450 stipend figure is tracker-reported; confirm on the official country page.</p>
''',
 dl_long='Varies by country \u2014 20 August to late November 2026 for the 2027-28 intake (e.g. India: 10 Nov 2026; ETH window: 20 Aug \u2013 30 Nov 2026).',
 offlinks=[('Swiss Government Excellence Scholarships \u2014 ETH Zurich (official)', 'https://ethz.ch/en/studies/non-degree-courses/sges.html')],
 related_titles=['swiss-phd', 'epfl-summer', 'eth-esop-2027', 'unil', 'bis-phd-2027'],
))

A.append(dict(
 slug='fulbright-swedish-scholar-program-2027-28',
 title='Fulbright Swedish Scholar Program 2027-28 in USA (Grant)',
 meta='Fulbright Swedish Scholar Program 2027-28: the Swedish Fulbright Commission\u2019s grant for Swedish researchers and lecturers \u2014 SEK 50,000 grant, SEK 15,000 travel allowance, visa fees and insurance. Deadline 11 Jan 2027.',
 short='Fulbright Swedish Scholar Program 2027-28', kicker='USA \u00b7 Scholars \u00b7 Grant', mono='FS',
 prov_short='Swedish Fulbright Commission', prov_cat='Commission \u00b7 Sweden\u2013USA',
 h1='Fulbright Swedish Scholar Program 2027-28 in USA (Grant)',
 sub='Research and lecturing grants for Swedish scholars at American universities \u2014 a fixed SEK 50,000 package (not full funding), open for 2027-28 applications until January 2027.',
 dpill='11 January 2027 \u00b7 81 days to go',
 facts=facts([('Award', 'Fixed grant package: SEK 50,000 grant award + SEK 15,000 one-time travel allowance + coverage of all SEVIS and J-1 visa fees + accident and sickness insurance for the grantee. This is a partial grant, not full funding.'),
              ('Eligible', 'Swedish citizens only (dual U.S.-Swedish citizens are NOT eligible); doctoral or other terminal degree completed by departure; established affiliation with a U.S. university or research centre; English proficiency; not already researching at a U.S. institution'),
              ('Stay', '3 to 12 months, with J-1 visa sponsorship up to 12 months'),
              ('How', 'Secure the U.S. host affiliation first, then complete the online application (project proposal up to 5 pages, CV, affiliation proof, three recommendations) by the deadline'),
              ('Deadline', '11 January 2027 \u2014 2027-28 cycle; online application opened 15 August 2026; selection notifications in March 2027')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Swedish Fulbright Commission</strong> offers grants to <strong>Swedish researchers and lecturers</strong> for research or teaching stays at universities and research centres in the <strong>United States</strong>. The <strong>2027-28 competition is open now</strong>, with applications closing on <strong>11 January 2027</strong>.</p>
      <p>A note on the funding, stated plainly: this is <strong>not a fully funded scholarship</strong>. The Commission grants a <strong>fixed SEK 50,000 award plus a SEK 15,000 travel allowance</strong>, with SEVIS/J-1 visa fees and accident-and-sickness insurance covered. It is a generous partial package that does not cover all living costs in the US, so plan your finances accordingly.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Swedish citizenship required</strong> \u2014 holders of <strong>dual U.S.-Swedish citizenship are not eligible</strong>.</li>
        <li><strong>Proficiency in English.</strong></li>
        <li>An <strong>established affiliation with an American university or research centre</strong> \u2014 this is a formal requirement, not a nice-to-have.</li>
        <li><strong>Doctoral or other terminal degree</strong> completed by the time of departure.</li>
        <li>Not already <strong>conducting research at a U.S. institution</strong> at the time of application.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>SEK 50,000 grant award</strong> for the research or lecturing stay.</li>
        <li><strong>SEK 15,000 one-time travel allowance.</strong></li>
        <li><strong>All SEVIS and J-1 visa fees covered</strong>, with personal assistance in the visa process.</li>
        <li><strong>Accident and sickness insurance</strong> for the grantee.</li>
        <li>Stay of <strong>3 to 12 months</strong>, with J-1 visa sponsorship possible up to twelve months.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Completed online application</strong> (select \u201cFulbright Visiting Scholar Program\u201d).</li>
        <li><strong>Project proposal</strong> of up to 5 pages.</li>
        <li><strong>Updated CV.</strong></li>
        <li><strong>Proof of affiliation</strong> with the U.S. host university or research centre.</li>
        <li><strong>Three letters of recommendation.</strong></li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure the affiliation</strong>Arrange an affiliation with a U.S. university or research centre before applying \u2014 applications without one are not complete.</li>
        <li><strong>Register on the portal</strong>The Fulbright Commission\u2019s online application for the 2027-28 cycle runs <strong>15 August 2026 \u2013 11 January 2027</strong>.</li>
        <li><strong>Complete every section</strong>Fill in personal details, the project proposal and host-institution information, and upload the CV, proposal, affiliation proof and three recommendation letters.</li>
        <li><strong>Submit on time</strong>Submit before <strong>11 January 2027</strong>; late applications are not accepted.</li>
        <li><strong>Await selection</strong>Selection and notification take place in <strong>March 2027</strong>, with visa processing and departure in <strong>July\u2013August 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this really fully funded?',
  'No. The commission grants SEK 50,000 plus a SEK 15,000 travel allowance, visa fees and insurance \u2014 a generous partial package, but it does not cover all living costs in the U.S.'),
 ('Can dual citizens apply?',
  'No. Holders of dual U.S.-Swedish citizenship are explicitly ineligible.'),
 ('How long can I stay?',
  'A minimum of three months, with J-1 visa sponsorship possible up to twelve months.'),
 ('Do I need the host affiliation before I apply?',
  'Yes. An established affiliation with an American university or research centre is a formal requirement.'),
 ('Who can be a \u201cscholar\u201d here?',
  'The programme covers recent PhD holders up to full professors \u2014 researchers and lecturers at any seniority with a doctoral or terminal degree.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official fulbright.se Scholar Program page (real programme name, 2027-28 timeline 15 Aug 2026 \u2013 11 Jan 2027, exact grant figures, visa/insurance coverage, March 2027 notification, July\u2013August 2027 departure) + Ume\u00e5 University funding-call pages independently confirming the same amounts and structure + agreeing aggregators on the document set. Important correction vs the stale queue title: this is NOT fully funded \u2014 the article states the fixed SEK 50,000 + SEK 15,000 grant package explicitly, and Swedish citizenship (no dual U.S. citizens) is a hard requirement.</p>
''',
 dl_long='11 January 2027 \u2014 2027-28 cycle (online application opened 15 August 2026; late applications not accepted).',
 offlinks=[('Fulbright Swedish Scholar Program \u2014 official page', 'https://fulbright.se/scholar-program/')],
 related_titles=['fulbright-dk', 'echidna-2027', 'yale-wf', 'harvard-lead', 'said'],
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

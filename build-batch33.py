#!/usr/bin/env python3
"""Batch 33 build: 4 verified articles (ARC Future Fellowships 2027,
Politecnico di Torino PhD 42nd cycle, ECU Scholarships 2027, VISTEC Scholarship 2027).
All four queue "2026" titles had closed cycles; articles are written for the live
cycles (ARC FT27, Polito 42nd cycle, ECU 2027 suite, VISTEC 2027).
Stellenbosch PSP skipped: 2027 cycle closed 30 Sep 2026, no 2028 call announced.
The 5th article (NUS ADB) is appended after its research lands.
Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'arc-ft27': {'mono': 'ARC', 'title': 'ARC Future Fellowships 2027 in Australia (Funded): Applications Close 6 November 2026',
   'href': 'arc-future-fellowships-2027-australia.html',
   'dpill': '6 Nov 2026 · 16 days to go',
   'award': '4-year fellowship salary at 3 ARC salary levels + up to AUD 60,000/yr project funding',
   'elig': 'Mid-career researchers; PhD awarded 1 Mar 2012–1 Mar 2022 (or career-interruption exemptions); hosted at an eligible Australian organisation.',
   'tags': [('Fellowship', 'blue'), ('Australia', 'teal')]},
 'polito-42': {'mono': 'PoliTO', 'title': 'Politecnico di Torino PhD Scholarships 2026–27 in Italy (Fully Funded): 42nd Cycle — Second Session Closes 16 November 2026',
   'href': 'politecnico-di-torino-phd-scholarships-42nd-cycle-italy.html',
   'dpill': '16 Nov 2026 · 26 days to go',
   'award': 'Min. 110 fully funded positions; €18,854.52/yr gross (~€1,386/month net) +50% abroad +10% research budget',
   'elig': 'Master’s degree; 95/110 for Italian degrees; B2 English; all nationalities; no prior Italian doctoral scholarship.',
   'tags': [('PhD', 'blue'), ('Italy', 'teal')]},
 'ecu-2027': {'mono': 'ECU', 'title': 'Edith Cowan University Scholarships 2027 in Australia (Funded): 15–25% Tuition Fee Reduction for International Students',
   'href': 'edith-cowan-university-scholarships-2027-australia.html',
   'dpill': '31 Dec 2027 · 436 days to go',
   'award': 'ECU Success Scholarship: 15% → 20% → 25% tuition reduction; ASEAN award 20% off; assessed automatically',
   'elig': 'International full-fee students with an offer for an eligible course; onshore study; prospective students only.',
   'tags': [('Master’s', 'blue'), ('Australia', 'teal')]},
 'vistec-2027': {'mono': 'VISTEC', 'title': 'VISTEC Scholarship 2027 in Thailand (Fully Funded): MS & PhD, Deadline 15 February 2027',
   'href': 'vistec-scholarship-2027-thailand.html',
   'dpill': '15 Feb 2027 · 117 days to go',
   'award': 'Fully funded, worth up to THB 5 million: fees waived + dormitory + up to THB 20,000/month + research budget',
   'elig': 'All nationalities; bachelor’s for MS / master’s for PhD in a relevant field; English test before interview.',
   'tags': [('MS & PhD', 'blue'), ('Thailand', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='arc-future-fellowships-2027-australia',
 title='ARC Future Fellowships 2027 in Australia (Funded): Applications Close 6 November 2026',
 meta='ARC Future Fellowships 2027 (FT27): the Australian Research Council\u2019s four-year funded fellowship for mid-career researchers. Salary at three ARC levels + up to AUD 60,000/year project funding. Applications close 6 November 2026, 5:00 PM Canberra time.',
 short='ARC Future Fellowships 2027', kicker='Australia \u00b7 Fellowship \u00b7 Funded', mono='ARC',
 prov_short='Australian Research Council (ARC)', prov_cat='Government \u00b7 Australia',
 h1='ARC Future Fellowships 2027 in Australia (Funded)',
 sub='The Australian Research Council\u2019s four-year funded fellowship for mid-career researchers \u2014 a salary award plus project funding, hosted at an eligible Australian organisation. The FT27 round closes 6 November 2026.',
 dpill='6 Nov 2026 \u00b7 16 days to go',
 facts=facts([('Award', 'Funded: four-year fellowship salary at one of three ARC Future Fellow salary levels (exact dollar amounts not published in the official notification summary) + up to AUD 60,000 per year in project funding to the administering organisation (up to AUD 240,000 over four years) for personnel, equipment, travel and field research.'),
              ('Eligible', 'Mid-career researchers with a strong research record; PhD awarded between 1 March 2012 and 1 March 2022 at the closing date (career interruptions can be counted through an eligibility exemption); researchers nominated on three previous occasions cannot re-apply in the same eligible period; international researchers eligible if an eligible Australian institution agrees to administer the application.'),
              ('Fellowship', 'Four years, hosted at an eligible Australian administering organisation; funding commencement expected 1 July 2027.'),
              ('How', 'You cannot apply to the ARC directly as an individual. Secure an eligible Australian host institution first, complete your Person Profile in the ARC\u2019s Research Management System (RMS), and submit through your host\u2019s research office for compliance review and certification.'),
              ('Deadline', '6 November 2026, 5:00 PM Canberra time (FT27 round; opened 23 September 2026). Rejoinder 19 March\u20135 April 2027; outcomes anticipated 26 October\u20139 November 2027.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>ARC Future Fellowships</strong>, run by the <strong>Australian Research Council (ARC)</strong> under its Discovery Program, support <strong>mid-career researchers</strong> to take up a four-year fellowship at an Australian institution and build the next stage of their research careers. The scheme is designed for researchers with demonstrated capacity for high-quality research, leadership, mentoring and collaboration.</p>
      <p>The live round is <strong>FT27</strong> (grant opportunity GO8625): it opened on <strong>23 September 2026</strong> and <strong>applications close on 6 November 2026 at 5:00 PM Canberra time</strong>. The earlier FT26 round closed on 5 November 2025 and its outcomes were announced \u2014 do not confuse the two. Funding for the FT27 cohort is expected to commence on <strong>1 July 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Mid-career researcher</strong> with demonstrated capacity for high-quality research, leadership, mentoring and collaboration.</li>
        <li><strong>PhD timing:</strong> as at the closing date, your PhD must have been awarded <strong>on or between 1 March 2012 and 1 March 2022</strong>. Career interruptions can be counted to bring you within that window through the ARC\u2019s eligibility exemption process.</li>
        <li><strong>Prior nominations:</strong> a researcher nominated for a Future Fellowship on <strong>three previous occasions</strong> cannot apply again in the same eligible period.</li>
        <li><strong>International researchers can be considered</strong> if an eligible Australian institution agrees to administer the application.</li>
        <li>The project must be hosted at an <strong>eligible Australian administering organisation</strong> (for example, a university) \u2014 the ARC does not fund direct individual applications.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Four-year fellowship salary</strong> paid at one of <strong>three ARC Future Fellow salary levels</strong>. The ARC does not publish the exact dollar figures in its public notification summary, so no salary number is quoted here \u2014 check the FT27 guidelines.</li>
        <li><strong>Up to AUD 60,000 per year</strong> in non-salary project funding to the administering organisation \u2014 up to <strong>AUD 240,000 over the four years</strong> \u2014 for personnel, equipment, travel, field research and related costs directly tied to the Fellow\u2019s research.</li>
        <li>Four funded years to establish or scale a research programme at a leading Australian institution.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The exact authoritative document list is <strong>not published in the official notification summary</strong> \u2014 the definitive checklist sits in the <strong>FT27 Grant Guidelines / Instructions to Applicants</strong>, so download those first.</li>
        <li>University research-office guidance indicates the typical application sections: the <strong>research proposal</strong>, <strong>research opportunity and performance evidence (ROPE)</strong>, <strong>publication record / CV</strong>, and a <strong>National Interest Test statement</strong>.</li>
        <li>Institutional templates plus an <strong>application certification form</strong> and a <strong>declaration of pending and newly funded ARC grants</strong> are part of the institutional lodgement.</li>
        <li>Your <strong>Person Profile in the ARC\u2019s Research Management System (RMS)</strong> must be complete before submission.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure a host institution</strong>Contact an eligible Australian administering organisation (e.g. a university) early and get agreement that it will administer your application.</li>
        <li><strong>Build your RMS profile</strong>Complete your full Person Profile in the ARC\u2019s Research Management System and draft the application using the FT27 Instructions to Applicants.</li>
        <li><strong>Submit to the research office</strong>Send your application to your host institution\u2019s research office by its <strong>internal deadline</strong> (several universities set notice-of-intent and review deadlines in early to mid-October 2026) for compliance review and certification.</li>
        <li><strong>ARC lodgement</strong>The research office certifies and lodges the application to the ARC before the <strong>6 November 2026, 5:00 PM Canberra time</strong> close. No direct individual applications are accepted.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the ARC Future Fellowship fully funded?',
  'It is a salary fellowship, not a fee-covering scholarship: the ARC pays a four-year salary at one of three salary levels and adds up to AUD 60,000 per year in project funding. Exact salary figures are not published in the official notification summary, so be wary of third-party pages quoting precise bands.'),
 ('Can I apply directly to the ARC as an individual?',
  'No. You must be hosted by an eligible Australian administering organisation and submit through its research office via the ARC\u2019s Research Management System (RMS).'),
 ('Can international researchers apply?',
  'Yes \u2014 international researchers can be considered if an eligible Australian institution agrees to administer the application; the project must be hosted in Australia.'),
 ('What are the key FT27 dates after the deadline?',
  'Rejoinder period 19 March\u20135 April 2027, outcomes anticipated 26 October\u20139 November 2027, and funding commencement expected 1 July 2027.'),
 ('What is the PhD timing rule?',
  'Your PhD must have been awarded between 1 March 2012 and 1 March 2022 as at the closing date, or career interruptions must be counted through the eligibility exemption process.')]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official ARC Future Fellowships page (arc.gov.au: FT27 grant opportunity GO8625, salary levels, up to AUD 60,000/yr project funding, 6 Nov 2026 5:00 PM Canberra close, funding commencement 1 July 2027, rejoinder 19 Mar\u20135 Apr 2027, outcomes Oct\u2013Nov 2027) + University of Queensland, Flinders University and University of Melbourne research-office pages (eligibility window 1 Mar 2012\u20131 Mar 2022, 3-nomination rule, RMS route, internal deadlines). The FT26 round (closed 5 Nov 2025) was excluded. Exact salary dollar figures and the authoritative document checklist are not published in the official notification summary \u2014 stated as such.</p>
''',
 dl_long='6 November 2026, 5:00 PM Canberra time (FT27 round; opened 23 September 2026)',
 offlinks=[('Future Fellowships \u2014 Australian Research Council (official)', 'https://www.arc.gov.au/grants/discovery-program/future-fellowships')],
 related_titles=['melbourne2027', 'adelaide2027', 'mcneill', 'deakin-vc-2027', 'nasa-hubble'],
))

A.append(dict(
 slug='politecnico-di-torino-phd-scholarships-42nd-cycle-italy',
 title='Politecnico di Torino PhD Scholarships 2026\u201327 in Italy (Fully Funded): 42nd Cycle \u2014 Second Session Closes 16 November 2026',
 meta='Politecnico di Torino PhD Scholarships 2026\u201327 (42nd cycle): at least 110 fully funded PhD positions in Italy \u2014 \u20ac18,854.52/year gross (~\u20ac1,386/month net), +50% for research abroad, 10% research budget. Session 2 closes 16 November 2026.',
 short='Politecnico di Torino PhD 42nd Cycle', kicker='Italy \u00b7 PhD \u00b7 Fully Funded', mono='PoliTO',
 prov_short='Politecnico di Torino', prov_cat='University \u00b7 Italy',
 h1='Politecnico di Torino PhD Scholarships 2026\u201327 in Italy (Fully Funded)',
 sub='The live 42nd-cycle call (a.y. 2026/2027) offers at least 110 fully funded PhD positions across 16 programmes in Turin \u2014 \u20ac18,854.52 per year gross, tax-exempt. The second application session closes 16 November 2026.',
 dpill='16 Nov 2026 \u00b7 26 days to go',
 facts=facts([('Award', 'Fully funded: minimum 110 scholarships; \u20ac18,854.52 per year gross (~\u20ac1,386/month net), exempt from IRPEF income tax; +50% stipend for authorised research periods abroad; 10% of the total scholarship as a research-activity budget over 36 months.'),
              ('Eligible', 'Master\u2019s degree (or equivalent second-level degree); conditional application allowed if you have not yet graduated; minimum final grade 95/110 for Italian degrees (minimum GPA thresholds for foreign degrees per Annex 2); B2 English certification; open to all nationalities; must not have previously held an Italian doctoral scholarship.'),
              ('Programmes', '16 PhD programmes: Architecture \u2014 History and Project; Bioengineering and Medical-Surgical Sciences; Design and Technology \u2014 People, Environment, Systems; Energetics; Physics; Aerospace Engineering; Chemical Engineering; Civil and Environmental Engineering; Electrical, Electronics and Communications Engineering; Management and Production Engineering; Computer and Control Engineering; Mechanical Engineering; Architectural Heritage; Materials Science and Technology; Mathematical Sciences; Urban and Regional Development.'),
              ('How', 'Apply online on the Apply@polito platform; \u20ac30 fee per programme (non-refundable); upload PDF documents; shortlisted candidates attend an oral interview (qualifications up to 40 pts, statement/references up to 20, interview up to 40).'),
              ('Deadline', 'Second session: 16 November 2026, 2:00 PM CET (open now). Third session opens 14 January 2027 and closes 15 February 2027, 2:00 PM CET.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Politecnico di Torino</strong> funds its doctoral programmes through numbered national cycles. The queue\u2019s \u201c41st call\u201d framing is stale: the <strong>41st cycle is closed</strong> (both 2025 sessions passed). The live opportunity is the <strong>42nd cycle (academic year 2026/2027)</strong>, with a <strong>minimum of 110 fully funded PhD positions</strong> across the university\u2019s doctoral programmes in Turin, Italy.</p>
      <p>Session 1 closed on 30 April 2026. The <strong>second session is open now</strong> (opened 15 October 2026) and closes on <strong>16 November 2026 at 2:00 PM CET</strong>; the third session opens 14 January 2027 and closes 15 February 2027. Session dates are confirmed across four independent trackers; confirm them on the official call page before submitting.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Master\u2019s degree</strong> (or equivalent second-level degree). You may apply <strong>conditionally</strong> if you have not yet graduated \u2014 the degree must be completed by the deadline of your chosen session.</li>
        <li><strong>Minimum final grade 95/110</strong> for Italian degrees; foreign degrees must meet the minimum GPA thresholds in Annex 2 of the call.</li>
        <li><strong>B2-level English certification</strong> from the accepted list in Annex 4 of the call.</li>
        <li><strong>Open to all nationalities.</strong></li>
        <li>You must <strong>not have previously held an Italian doctoral scholarship</strong>.</li>
        <li>No age limit, except for apprenticeship-format positions (maximum 29 years old at hiring).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac18,854.52 per year gross</strong> (2026/27 figure), roughly <strong>\u20ac1,386 per month net</strong> \u2014 <strong>exempt from IRPEF income tax</strong>, with INPS social-security contributions split two-thirds by the university and one-third by the holder.</li>
        <li><strong>+50% stipend</strong> for authorised research periods abroad.</li>
        <li><strong>10% of the total scholarship</strong> as a research-activity budget over the 36 months.</li>
        <li>Duration up to <strong>36 months</strong>, renewed annually.</li>
        <li>Reserved positions for refugees under the POLITO for REFUGEES initiative, alongside positions on predefined research topics or independent research projects.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Bachelor\u2019s and master\u2019s certificates + transcripts</strong> (foreign degrees need a CIMEA comparability certificate or Declaration of Value).</li>
        <li><strong>CV</strong> and a <strong>statement of purpose / motivation</strong> outlining research interests and proposed methodology.</li>
        <li><strong>Master\u2019s thesis abstract</strong> (3,000\u20136,000 characters, in English).</li>
        <li><strong>Two academic referees</strong> (names and emails) \u2014 trackers note one should ideally be from an external university and one from Politecnico itself.</li>
        <li><strong>B2 English proof</strong>, a <strong>valid ID</strong>, and the <strong>\u20ac30 fee payment receipt</strong> per programme.</li>
        <li>Refugee applicants may use the <strong>European Qualifications Passport for Refugees</strong>. Optional but recommended: GRE scores, recommendation letters, publication list. All uploads in PDF on Apply@polito.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register on Apply@polito</strong>Create an account on the university\u2019s official application platform.</li>
        <li><strong>Choose your programme(s)</strong>Select one or more of the 16 PhD programmes and complete the application form.</li>
        <li><strong>Upload documents and pay the fee</strong>Attach all documents in PDF and pay the <strong>\u20ac30 non-refundable fee per programme</strong> (credit card / PagoPA).</li>
        <li><strong>Submit before the session deadline</strong>Session 2: <strong>16 November 2026, 2:00 PM CET</strong>. Accepting a position in one session bars entry to later sessions of the same cycle.</li>
        <li><strong>Oral interview</strong>Shortlisted candidates are invited to an interview. Results are posted on the official site \u2014 no personal notifications are sent.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this really fully funded?',
  'Yes \u2014 the 42nd-cycle call offers a minimum of 110 scholarships with full tuition coverage plus a \u20ac18,854.52/year tax-exempt stipend, a 50% mobility bonus for research abroad and a 10% research-activity budget.'),
 ('What happened to the 41st call?',
  'The 41st cycle is closed: both 2025 sessions have passed, and the special conflict-zone call closed on 16 February 2026. Apply to the 42nd cycle instead.'),
 ('Can I apply without B2 English?',
  'No \u2014 a B2-level English certificate from the accepted list in Annex 4 of the call is a requirement.'),
 ('Can I apply to more than one programme?',
  'Yes, but the \u20ac30 application fee applies per programme, and accepting a position in one session bars entry to later sessions of the same cycle.'),
 ('How does the selection work?',
  'Qualifications are scored up to 40 points, the statement of purpose and references up to 20, and the oral interview up to 40. Results are posted on the official site only.')]) + '''
      <p class="verify">Verified 21 Oct 2026 via four agreeing independent trackers (gradualin, fellowshipsguide, scholarships.af, daadscholarship: 42nd cycle, minimum 110 fully funded positions, \u20ac18,854.52/yr gross, session 2 opens 15 Oct 2026 and closes 16 Nov 2026 2:00 PM CET, session 3 14 Jan\u201315 Feb 2027, eligibility and document list) + the official polito.it funding-deadlines page confirming the 42nd cycle. The stale 41st cycle was excluded. Session dates should be confirmed on the official bando page before submitting.</p>
''',
 dl_long='Second session: 16 November 2026, 2:00 PM CET (open now; first session closed 30 April 2026; third session 14 January \u2013 15 February 2027)',
 offlinks=[('PhD scholarships \u2014 Politecnico di Torino (official)', 'https://www.polito.it/en/education/phd-programmes-and-postgraduate-school/phds-and-companies/funding-phd-scholarships'),
           ('42nd-cycle PhD scholarships at Politecnico di Torino \u2014 Fellowships Guide', 'https://fellowshipsguide.com/politecnico-di-torino-phd/'),
           ('Politecnico di Torino PhD Scholarship 2026 (42nd cycle) \u2014 Gradualin', 'https://gradualin.com/politecnico-di-torino-phd-scholarship-2026-italy-42nd-cycle/')],
 related_titles=['perugia-phd', 'italy-guide', 'mespom-2027', 'radboud-2027', 'tudelft-excellence-2027'],
))

A.append(dict(
 slug='edith-cowan-university-scholarships-2027-australia',
 title='Edith Cowan University Scholarships 2027 in Australia (Funded): 15\u201325% Tuition Fee Reduction for International Students',
 meta='Edith Cowan University Scholarships 2027: international students get a 15\u201325% tuition fee reduction (ECU Success Scholarship; ASEAN award 20% off) with automatic assessment \u2014 no separate application. Open 1 July 2026, closes 31 December 2027.',
 short='Edith Cowan University Scholarships 2027', kicker='Australia \u00b7 Master\u2019s \u00b7 Funded', mono='ECU',
 prov_short='Edith Cowan University', prov_cat='University \u00b7 Australia',
 h1='Edith Cowan University Scholarships 2027 in Australia (Funded)',
 sub='An important correction first: ECU\u2019s international awards are percentage tuition reductions \u2014 <strong>not</strong> fully funded scholarships. For the 2027 intake the ECU Success Scholarship rises from 15% to 25% as you pass credit milestones, and it is awarded automatically when you apply for your course.',
 dpill='31 Dec 2027 \u00b7 436 days to go',
 facts=facts([('Award', 'Funded (tuition reduction, NOT fully funded): the 2027 ECU Success Scholarship starts at 15% and rises to 20% then 25% tuition-fee reduction as credit-point milestones are met; the 2027 ASEAN International Scholarship gives 20% off for the standard course duration. Applied unit-by-unit at census dates; no cash alternative; no living stipend, visa or relocation support.'),
              ('Eligible', 'International student (not an Australian citizen, permanent resident or NZ citizen); hold an offer, conditional offer or packaged pathway offer for an eligible course; commence onshore at Joondalup, Mount Lawley, City Campus or South West (Bunbury); prospective (not current) ECU student; not holding another ECU scholarship or a government scholarship/sponsorship. Regional awards are citizenship-based (e.g. ASEAN: Cambodia, Indonesia, Laos, Malaysia, Philippines, Singapore, Thailand, Vietnam); the Success Scholarship covers students from countries without a regional award.'),
              ('Documents', 'No separate scholarship documents checklist is published in the official notification \u2014 the only stated requirement is meeting the course\u2019s academic and English entry requirements and accepting the Letter of Offer.'),
              ('How', 'No separate scholarship application exists. ECU\u2019s Admissions Office assesses you automatically when you apply for an eligible course (online application portal or an authorised agent); a separate scholarship letter is issued with the Letter of Offer. To accept: meet the offer conditions, accept by its stated deadline, and pay the indicative deposit plus Overseas Student Health Cover.'),
              ('Deadline', 'The 2027 ECU Success Scholarship page states opens 1 July 2026 and closes 31 December 2027. The 2026 intake (Semester One/Two 2026) is now closed; the queue\u2019s \u201cOctober 2025\u201d date comes from a third-party aggregator, not ECU, and is unverified.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Edith Cowan University (ECU)</strong> in Western Australia does not run a single umbrella \u201cECU Scholarship\u201d. Its international awards are a <strong>suite of tuition-fee reductions</strong>, and for 2027 the flagship is the <strong>2027 ECU Success Scholarship</strong>, which ECU advertises as part of its \u201cScholarships for 2027 are now available\u201d intake. A correction to the queue listing: these awards are <strong>percentage reductions \u2014 they are not fully funded</strong>. There is no full tuition, no living stipend, and no visa or relocation support.</p>
      <p>The 2026 cycle (the <strong>2026 International Masters Scholarship</strong>, 20% off tuition) covered commencements in Semester One and Two 2026 only and is now closed. Students from the ASEAN region have a parallel option \u2014 the <strong>2027 ASEAN International Scholarship</strong> at 20% off the standard course duration. There is <strong>no separate scholarship application</strong>: ECU\u2019s Admissions Office assesses every eligible course application automatically.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student</strong> \u2014 not an Australian citizen, permanent resident or New Zealand citizen.</li>
        <li>Hold an <strong>offer, conditional offer or packaged pathway offer</strong> for an eligible course.</li>
        <li>Commence <strong>onshore</strong> at Joondalup, Mount Lawley, City Campus or South West (Bunbury).</li>
        <li>Be a <strong>prospective (not current)</strong> ECU student and <strong>full fee-paying, non-sponsored</strong>.</li>
        <li><strong>Not hold another ECU scholarship</strong> or a government scholarship/sponsorship.</li>
        <li><strong>Regional routing:</strong> students from countries with a regional award are assessed for it (e.g. ASEAN citizens for the ASEAN award); the Success Scholarship covers students from countries without a regional award. Note that India and Pakistan are routed to ECU\u2019s separate International Excellence Scholarship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>ECU Success Scholarship 2027:</strong> starts at a <strong>15% tuition-fee reduction</strong>, rising to <strong>20% and then 25%</strong> as credit-point milestones are met \u2014 for the duration of the eligible course.</li>
        <li><strong>ASEAN International Scholarship 2027:</strong> <strong>20% off tuition</strong> for the standard course duration (master\u2019s included).</li>
        <li>The reduction is <strong>applied unit-by-unit at census dates</strong>; it cannot be exchanged for cash or used for non-tuition expenses.</li>
        <li>A <strong>separate scholarship letter</strong> is issued together with the Letter of Offer.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Not published in the official notification</strong> \u2014 ECU publishes no separate scholarship documents checklist.</li>
        <li>The only stated requirement is meeting your <strong>course\u2019s academic and English entry requirements</strong> and <strong>accepting the Letter of Offer</strong> by its stated deadline.</li>
        <li>Contact for questions: <strong>enquiries@ecu.edu.au</strong>, 134 328 (within Australia) / +61 8 6304 0000 (international).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for an eligible ECU course</strong>Submit a course application through ECU\u2019s online application portal or an authorised agent \u2014 this single application also puts you in the scholarship pool.</li>
        <li><strong>Automatic assessment</strong>ECU\u2019s Admissions Office assesses scholarship eligibility automatically; no separate form exists.</li>
        <li><strong>Receive the scholarship letter</strong>If eligible, a separate scholarship letter arrives with your Letter of Offer.</li>
        <li><strong>Accept the offer</strong>Meet the offer conditions, accept the Letter of Offer by its stated deadline, and pay the indicative deposit plus Overseas Student Health Cover.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the ECU scholarship fully funded?',
  'No \u2014 that is the most important correction. ECU\u2019s international awards are percentage tuition reductions (15\u201325% for 2027; 20% for the ASEAN award). There is no living stipend, visa support or relocation funding.'),
 ('Is there a separate scholarship application form?',
  'No. Every eligible course application is assessed automatically by ECU\u2019s Admissions Office.'),
 ('What is the deadline?',
  'The official 2027 ECU Success Scholarship page states opens 1 July 2026 and closes 31 December 2027. Apply for your course in good time so the Letter of Offer and scholarship letter can be issued.'),
 ('Can current ECU students apply?',
  'No \u2014 you must be a prospective (new) student, and you cannot hold another ECU scholarship or a government scholarship/sponsorship.'),
 ('I am from India or Pakistan \u2014 which award applies?',
  'ECU routes India and Pakistan to its separate International Excellence Scholarship rather than the standard country-based awards; check the ECU scholarships page for that award\u2019s terms.')]) + '''
      <p class="verify">Verified 21 Oct 2026 via three official ECU pages (2027 ECU Success Scholarship: 15%\u219220%\u219225% tuition reduction, opens 1 Jul 2026, closes 31 Dec 2027; 2027 ASEAN International Scholarship: 20% off; 2026 International Masters Scholarship, closed) + a corroborating ECU scholarship table. The queue\u2019s \u201cFully funded\u201d label and \u201cOctober 2025\u201d deadline are not supported by ECU \u2014 both corrected or flagged. The scholarship documents checklist is not published in the official notification \u2014 stated as such.</p>
''',
 dl_long='Opens 1 July 2026; closes 31 December 2027 (2027 ECU Success Scholarship, official ECU page). The 2026 intake is closed.',
 offlinks=[('2027 ECU Success Scholarship \u2014 ECU (official)', 'https://www.ecu.edu.au/scholarships/details/2027-ecu-success-scholarship'),
           ('2027 ASEAN International Scholarship \u2014 ECU (official)', 'https://www.ecu.edu.au/scholarships/details/2027-asean-international-scholarship'),
           ('2026 International Masters Scholarship (closed) \u2014 ECU (official)', 'https://www.ecu.edu.au/scholarships/details/2026-international-masters-scholarship')],
 related_titles=['melbourne2027', 'adelaide2027', 'mcneill', 'deakin-vc-2027', 'udem-exempt'],
))

A.append(dict(
 slug='vistec-scholarship-2027-thailand',
 title='VISTEC Scholarship 2027 in Thailand (Fully Funded): MS & PhD, Deadline 15 February 2027',
 meta='VISTEC Scholarship 2027: the Vidyasirimedhi Institute of Science and Technology\u2019s fully funded MS & PhD scholarship in Thailand \u2014 up to THB 5 million in value, fees waived, dormitory, up to THB 20,000/month stipend. Applications open until 15 February 2027.',
 short='VISTEC Scholarship 2027', kicker='Thailand \u00b7 MS & PhD \u00b7 Fully Funded', mono='VISTEC',
 prov_short='Vidyasirimedhi Institute of Science and Technology (VISTEC)', prov_cat='Institute \u00b7 Thailand',
 h1='VISTEC Scholarship 2027 in Thailand (Fully Funded)',
 sub='The Vidyasirimedhi Institute of Science and Technology in Rayong, Thailand funds MS and PhD students with a full scholarship worth up to THB 5 million \u2014 fees waived, dormitory, monthly stipend, research budget and no post-graduation obligation. The 2027 intake is open now and closes 15 February 2027.',
 dpill='15 Feb 2027 \u00b7 117 days to go',
 facts=facts([('Award', 'Fully funded, worth up to THB 5 million per awardee with no post-graduation obligation: university fees waived; on-campus housing/dormitory; monthly stipend up to THB 20,000; research budget support up to THB 500,000; study/equipment support up to THB 30,000. PhD enrollees also receive up to THB 1 million for up to one year of research abroad; high-performing PhD students may additionally apply for the Royal Srimedhi Scholarship for up to 2 years abroad.'),
              ('Eligible', 'Open to all nationalities (Thai and international). Master\u2019s applicants need a bachelor\u2019s degree; PhD applicants need a master\u2019s degree. The degree must be in a field relevant to one of VISTEC\u2019s four schools: Molecular Science and Engineering (MSE), Energy Science and Engineering (ESE), Biomolecular Science and Engineering (BSE), Information Science and Technology (IST). An English test score (TOEFL, IELTS or CU-TEP; equivalents accepted temporarily) is required before the interview.'),
              ('Documents', 'CV; transcript; statement of purpose (official form downloadable during the application, submittable up to interview day); two letters of recommendation (same late-submission allowance); official English test score before the interview. Optional: publications, awards & honours, portfolio.'),
              ('How', 'Apply online through the official VISTEC admission portal: explore the schools and programmes, create an account (maximum 2 application forms per applicant), complete the form and upload documents, then attend the interview and written exam if shortlisted.'),
              ('Deadline', '15 February 2027 for the 2027 intake (admission window 1 October 2026 \u2013 15 February 2027). Interview/written-exam notification 22 February 2027; interview & written exam 27 February 2027; results 31 March 2027.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Vidyasirimedhi Institute of Science and Technology (VISTEC)</strong> in Rayong, Thailand \u2014 the country\u2019s graduate research institute focused on science and technology \u2014 offers a <strong>fully funded scholarship</strong> for its <strong>MS and PhD programmes</strong>, worth up to <strong>THB 5 million per awardee</strong> with <strong>no post-graduation obligation</strong>.</p>
      <p>The queue\u2019s \u201c2026\u201d framing is stale: the 2026 intake (deadline 15 February 2026) is closed. The <strong>2027 intake is open right now</strong> \u2014 applications opened <strong>1 October 2026</strong> on VISTEC\u2019s official admission portal and close on <strong>15 February 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Open to all nationalities</strong> \u2014 Thai and international applicants.</li>
        <li><strong>Master\u2019s applicants:</strong> a <strong>bachelor\u2019s degree</strong>. <strong>PhD applicants:</strong> a <strong>master\u2019s degree</strong>.</li>
        <li>The degree must be in a field <strong>relevant to one of VISTEC\u2019s four schools</strong>: Molecular Science and Engineering (MSE), Energy Science and Engineering (ESE), Biomolecular Science and Engineering (BSE), or Information Science and Technology (IST).</li>
        <li><strong>English test score required before the interview</strong> \u2014 TOEFL, IELTS or CU-TEP (equivalent or other scores accepted temporarily).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>University fees waived</strong> and <strong>on-campus housing/dormitory</strong> provided.</li>
        <li><strong>Monthly stipend up to THB 20,000.</strong></li>
        <li><strong>Research budget support up to THB 500,000</strong> and <strong>study/equipment support up to THB 30,000</strong>.</li>
        <li><strong>PhD enrollees:</strong> up to <strong>THB 1 million</strong> for up to one year of research abroad.</li>
        <li>High-performing PhD students may additionally apply for the <strong>Royal Srimedhi Scholarship</strong> for up to 2 years abroad.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV</strong> and <strong>transcript</strong>.</li>
        <li><strong>Statement of purpose</strong> \u2014 the official form is downloadable during the application and can be submitted up to the interview day.</li>
        <li><strong>Two letters of recommendation</strong> (same late-submission allowance).</li>
        <li><strong>Official English test score</strong> (TOEFL/IELTS/CU-TEP) before the interview.</li>
        <li>Optional: <strong>publications, awards & honours, portfolio</strong>.</li>
        <li>Contact for admissions questions: <strong>admission@vistec.ac.th</strong>, +66 33 01 4116.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Explore programmes</strong>Read the schools and programmes on the official VISTEC admission portal.</li>
        <li><strong>Create an account</strong>Register on admission.vistec.ac.th \u2014 a maximum of <strong>2 application forms per applicant</strong> is allowed.</li>
        <li><strong>Complete the form and upload documents</strong>Fill in the application, upload your documents, and submit the statement of purpose (which may be finalised up to the interview day).</li>
        <li><strong>Shortlisting and exam</strong>If shortlisted, you are notified on 22 February 2027 and attend the <strong>interview and written exam on 27 February 2027</strong>; results are announced on <strong>31 March 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the VISTEC scholarship fully funded?',
  'Yes \u2014 the official admission page describes a full scholarship worth up to THB 5 million: fees waived, dormitory, up to THB 20,000/month stipend, research and equipment budgets, and no post-graduation obligation.'),
 ('Who can apply?',
  'All nationalities. Master\u2019s applicants need a bachelor\u2019s degree and PhD applicants need a master\u2019s, in a field relevant to one of VISTEC\u2019s four schools (MSE, ESE, BSE, IST).'),
 ('Do I need an English test score?',
  'Yes \u2014 an official English test score (TOEFL, IELTS or CU-TEP) is required before the interview.'),
 ('Can I submit more than one application?',
  'A maximum of 2 application forms per applicant is allowed on the admission portal.'),
 ('Is there an application fee?',
  'One third-party listing mentions a USD 20 fee for international applicants, but this is not confirmed by a second source \u2014 treat it as unverified and check the official portal before paying anything.')]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official VISTEC admission portal (admission.vistec.ac.th, read directly: up to THB 5 million full scholarship, fees waived, dormitory, up to THB 20,000/month stipend, up to THB 500,000 research budget, up to THB 30,000 study/equipment support, PhD THB 1 million abroad year, Royal Srimedhi add-on, 15 Feb 2027 deadline, 1 Oct 2026\u201315 Feb 2027 window, exam schedule) + multiple agreeing third-party listings. The closed 2026 intake was excluded. The USD 20 application-fee claim (one listing only) is flagged as unverified.</p>
''',
 dl_long='15 February 2027 (2027 intake; admission window 1 October 2026 \u2013 15 February 2027)',
 offlinks=[('VISTEC Admission System \u2014 official admission portal', 'https://admission.vistec.ac.th/')],
 related_titles=['kaist-ug', 'apu-adb', 'honjo', 'singa2027', 'iuj'],
))

A.append(dict(
 slug='nus-adb-japan-scholarship-program-2027-singapore',
 title='ADB\u2013Japan Scholarship Program at NUS 2027 in Singapore (Fully Funded): Master in Public Policy',
 meta='ADB\u2013Japan Scholarship Program at NUS 2027: fully funded master\u2019s study at the National University of Singapore \u2014 full tuition, monthly subsistence with housing, books, medical insurance and airfare. No central deadline; Lee Kuan Yew MPP intake cited as 15 December (third-party figure \u2014 confirm on the NUS admissions page).',
 short='ADB\u2013Japan Scholarship Program at NUS 2027', kicker='Singapore \u00b7 Master\u2019s \u00b7 Fully Funded', mono='ADB',
 prov_short='ADB\u2013Japan Scholarship Program / National University of Singapore', prov_cat='Multilateral \u00b7 Singapore',
 h1='ADB\u2013Japan Scholarship Program at NUS 2027 in Singapore (Fully Funded)',
 sub='A standing fully funded master\u2019s programme financed by the Government of Japan through the Asian Development Bank, with the National University of Singapore as its Singapore partner institution. The live window is the 2027 intake \u2014 there is no central deadline; the university\u2019s admissions cycle decides.',
 dpill='15 Dec 2026 (unconfirmed) \u00b7 55 days to go',
 facts=facts([('Award', 'Fully funded: full tuition fees; monthly subsistence allowance including housing; books and instructional-materials allowance; medical insurance; economy-class return airfare between the home country and the institution; a special thesis-preparation grant may be available for research scholars. Exact subsistence amounts are not published for the NUS track \u2014 avoid the figures quoted for Japan-based institutions.'),
              ('Eligible', 'Citizen of an ADB borrowing member country eligible for Japanese ODA scholarships (a developing member country); not a dual citizen of a developed country; gained admission to an approved master\u2019s course at the designated institution; bachelor\u2019s degree or equivalent with a superior academic record; at least 2 years of full-time professional work experience after the degree; English proficiency; no more than 35 years old at application; good health; agree to return and work in the home country for at least 2 years after the studies.'),
              ('Level', 'Master\u2019s-level study only (not PhD), in economics, business and management, science and technology, and other development-related fields, including public policy. Multiple independent guides list the Lee Kuan Yew School of Public Policy\u2019s Master in Public Policy (July/August intake) as NUS\u2019s ADB-JSP track \u2014 this is not published in the official ADB notification, which names only \u201cNational University of Singapore\u201d.'),
              ('How', 'No central deadline and no central application. Apply for admission to NUS and indicate interest in the ADB-JSP; submit the institution\u2019s completed forms plus the ADB-JSP application form and required documents to the university; the institution shortlists and ranks candidates; final selection is made by ADB in consultation with the Government of Japan.'),
              ('Deadline', 'No central ADB-JSP deadline \u2014 ADB instructs applicants to apply through the partner institution at least six months before the intended intake. For the Lee Kuan Yew MPP July/August intake, multiple independent guides cite 15 December, but this date is not published in the official ADB notification \u2014 confirm it on NUS/LKYSPP\u2019s own admissions page before relying on it.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Asian Development Bank\u2013Japan Scholarship Program (ADB-JSP)</strong>, financed by the <strong>Government of Japan through the Asian Development Bank</strong>, funds postgraduate study at 27 partner institutions across Asia and the Pacific. The <strong>National University of Singapore (NUS)</strong> is the programme\u2019s Singapore partner institution, listed in ADB\u2019s official ADB-JSP brochure.</p>
      <p>There is no branded \u201cNUS ADB Scholarship 2026\u201d with its own cycle \u2014 this is the standing ADB-JSP, open every year and administered per institution. A \u201c2026\u201d NUS intake would have been the July/August 2026 round, whose window has closed; <strong>the live window is the 2027 intake</strong>. Multiple independent guides point to the <strong>Lee Kuan Yew School of Public Policy\u2019s Master in Public Policy</strong> as the NUS ADB-JSP track, though the ADB brochure itself does not publish per-institution approved programme lists.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of an ADB borrowing member country</strong> eligible for Japanese ODA scholarships (a developing member country); <strong>not a dual citizen of a developed country</strong>.</li>
        <li><strong>Gained admission</strong> to an approved master\u2019s course at the designated institution.</li>
        <li><strong>Bachelor\u2019s degree or equivalent</strong> with a superior academic record.</li>
        <li><strong>At least 2 years of full-time professional work experience</strong> after the degree.</li>
        <li><strong>English proficiency</strong> and <strong>good health</strong>.</li>
        <li><strong>No more than 35 years old</strong> at the time of application.</li>
        <li>Agree to <strong>return and work in the home country for at least 2 years</strong> after completing the studies.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees.</strong></li>
        <li><strong>Monthly subsistence allowance including housing.</strong></li>
        <li><strong>Books and instructional-materials allowance.</strong></li>
        <li><strong>Medical insurance.</strong></li>
        <li><strong>Travel expenses</strong> \u2014 economy-class return airfare between the home country and the institution.</li>
        <li>A <strong>special thesis-preparation grant</strong> may be available for research scholars.</li>
        <li>Note what it does <strong>not</strong> cover: family expenses, extra-curricular courses, additional travel during the course, or computers/equipment.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>Completed <strong>institution + ADB-JSP application forms</strong>.</li>
        <li><strong>Latest income-tax return or salary certification</strong>, plus <strong>certification of family income</strong> (parents\u2019 income).</li>
        <li>Standard admission documents per the institution: <strong>transcripts, CV, English test proof, recommendation letters, work-experience certificates</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to NUS</strong>Apply to the relevant NUS programme (third-party guides point to the Lee Kuan Yew MPP) and indicate interest in the ADB-JSP.</li>
        <li><strong>Submit the ADB-JSP forms</strong>Send the completed institution forms, the ADB-JSP application form and all required documents to the university.</li>
        <li><strong>Institution shortlisting</strong>NUS evaluates and ranks its ADB-JSP applicants; ADB gives priority to the order the institution proposes.</li>
        <li><strong>Final selection</strong>ADB selects the scholars in consultation with the Government of Japan and informs the institution, which notifies the scholars. Until the institution confirms your award, treat nothing as final \u2014 ADB\u2019s own guidance says not to act on employment or travel plans before then.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a central ADB-JSP deadline?',
  'No. ADB instructs applicants to apply through the partner institution at least six months before the intended intake; each institution sets its own date. For the LKY MPP, guides cite 15 December \u2014 confirm it on NUS\u2019s own admissions page.'),
 ('Is the LKY School MPP the official NUS track?',
  'Multiple independent guides list it as the NUS ADB-JSP track, but the official ADB brochure names only \u201cNational University of Singapore\u201d and does not publish per-institution approved programme lists \u2014 treat the track designation as third-party consensus.'),
 ('How old can I be?',
  'No more than 35 years old at the time of application.'),
 ('Do I have to return home after the degree?',
  'Yes \u2014 scholars agree to return and work in their home country for at least 2 years after completing their studies.'),
 ('Does it cover my family or a PhD?',
  'No \u2014 family expenses are not covered, and the ADB-JSP is master\u2019s-level only, not PhD.')]) + '''
      <p class="verify">Verified 21 Oct 2026 via the official ADB\u2013Japan Scholarship Program brochure (adb.org, Publication Stock No. ARM250108-2: NUS as Singapore partner institution, award coverage, eligibility, documents, institution-route application, final selection by ADB) + two agreeing third-party guides for the 15 December LKY MPP figure and the LKY MPP track designation \u2014 both flagged as not published in the official notification. Subsistence amounts for the NUS track are not published \u2014 Japan-track figures deliberately excluded.</p>
''',
 dl_long='No central ADB-JSP deadline \u2014 apply through NUS at least six months before the intended intake. The Lee Kuan Yew MPP 15 December figure is third-party-corroborated only; confirm on the NUS admissions page.',
 offlinks=[('ADB\u2013Japan Scholarship Program \u2014 ADB (official)', 'https://www.adb.org/JSP/'),
           ('ADB-JSP brochure (official, PDF)', 'https://www.adb.org/sites/default/files/publication/29268/jsp-brochure.pdf'),
           ('ADB-JSP 2027 partner universities guide', 'https://guides.scholarshipunion.com/adb-jsp/partner-universities.html')],
 related_titles=['apu-adb', 'keio-adb', 'singa2027', 'nus2027', 'amgen-2027'],
))

# --- Batch 33 card registry entry (appended to NEW_CARDS) ---
NEW_CARDS['nus-adb-2027'] = {'mono': 'ADB', 'title': 'ADB\u2013Japan Scholarship Program at NUS 2027 in Singapore (Fully Funded): Master in Public Policy',
   'href': 'nus-adb-japan-scholarship-program-2027-singapore.html',
   'dpill': '15 Dec 2026 (unconfirmed) \u00b7 55 days to go',
   'award': 'Full tuition + monthly subsistence incl. housing + books + medical insurance + airfare; thesis grant possible',
   'elig': 'Developing-member-country citizens \u226435; bachelor\u2019s with superior record; \u22652 yrs work experience; 2-yr return-home commitment.',
   'tags': [('Master\u2019s', 'blue'), ('Singapore', 'teal')]}
CARDS['nus-adb-2027'] = NEW_CARDS['nus-adb-2027']

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

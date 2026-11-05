#!/usr/bin/env python3
"""Batch 36 (cron run 36, 22 Oct 2026): 5 verified articles.

Topics from the queue (order): Kassel Exposé (#4), Optiver (#3), NVIDIA (#6),
Cologne CGA (#13), Minnesota Global Excellence (#23).

HONESTY CALLS (22 Oct 2026, Asia/Kolkata):
- Kassel Exposé: the live call is the 26 Aug 2026 round, deadline
  1 December 2026 (official uni-kassel.de call PDF). Stipend €1,300/month for
  up to 9 months + €200/month family allowance on request. A supervisor
  commitment from a Kassel professor is mandatory before applying; only the
  first doctorate is fundable; one application per person (re-application
  only after interruption by illness/childbirth/caregiving). No funding
  start date for the new round is published in the call — not invented.
- Oxford Optiver: queue title says 2026, but the 2026 intake (Oct 2026 start)
  is closed. The official ox.ac.uk page shows the live fifth cohort starting
  October 2027; applications via Oxford course deadlines Nov 2026 - Jan 2027.
  Article retitled to the 2027 intake. Women only, ordinarily resident in
  eligible low/middle-income countries (list on the official page), 9 listed
  STEM MSc courses. Full course fees + living-cost grant + mentoring/induction.
- NVIDIA: queue title says 2026; the live round is the 2027-28 fellowship,
  applications closing 30 October 2026 (recommendations included). Up to
  $60,000 per award paid through the fellow's university (stipend + tuition
  + fees); mandatory in-person summer internship (summer 2027) before the
  fellowship year. First year of PhD complete; international students
  eligible; full-time NVIDIA employees and their immediate family excluded.
  Title: NVIDIA Graduate Fellowship 2027-28.
- Cologne CGA: 12 fully funded PhD positions, application period
  11 Aug - 3 Nov 2026 (official CGA call PDF, daad.de, mpg.de, EURAXESS).
  Referee letters due 10 Nov 2026; panel interviews 7-9 Dec 2026;
  recruitment week 15-19 Feb 2027; projects start 1 Jul - 1 Oct 2027.
  Funding: employment contracts >=3 years at TV-L E13 65% (or equivalent
  Max Planck PhD support contract). MSc in life-sciences fields + English C1.
- Minnesota Global Excellence: queue title says 2026; the live cycle is
  Fall 2027 admission. Merit awards for international freshmen and transfer
  students, automatic with the admission application (no separate form).
  Freshmen $5,000-$20,000/yr (up to 4 yrs), transfers $10,000/yr (up to 3
  yrs, fall entry). Early Action I: 1 Nov 2026. Marketed as
  "(Partially Funded)" because it is a tuition award, not a full ride.
  Amounts above $20,000/yr quoted by some trackers are stale 2026-cycle
  figures and are not repeated.

SKIPPED (queue order): Government of Ireland Scholarships 2026 (GOI-IES 2026
closed 12 Mar 2026; Research Ireland GOIPG 2027 applicant deadline passed
10 Oct 2026); MBZUAI UGRIP 2026 (2026 cycle closed 28 Feb 2026, 2027 call not
officially published); Toronto National Scholarship 2026 (domestic-only
scheme; 2027-intake school nomination deadline 9 Oct 2026 passed);
University of Nottingham PhD Studentship 2026 (generic topic; flagship CS
fellowship closed 7 Jan 2026, other studentships UK/home-only or
project-specific); 36 Birmingham City University PhD Scholarship 2026 (the
36-scholarship ABCE 2026 call closed 17 Sep 2025); Brazil Government PEC-PG
2026 (2026 window closed 30 Dec 2025; trackers quote contradictory amounts);
KATIP Turkish Language Program 2026 (KATIP 2026-27 closed 1 Jun 2026);
MLU PhD Scholarship Program 2026 (aggregator construct - no unified call;
doctoral funding is project-based or Grafö state scholarships via
faculties); Boeing Future Flight Operations Internship 2026 (employer job
listing, not a scholarship); Switzerland Research Fellowship 2026
(near-duplicate of the already-written Swiss Government Excellence
Scholarship articles).

Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'kassel-expose': {'mono': 'UKAS', 'title': 'University of Kassel Exposé Scholarships 2026 in Germany (Funded)',
   'href': 'university-of-kassel-expose-scholarships-2026-germany.html',
   'dpill': 'Deadline 1 Dec 2026 · 40 days left',
   'award': '€1,300/month for up to 9 months while writing your dissertation exposé; €200/month family allowance on request.',
   'elig': 'Doctoral candidates with a supervision commitment from a University of Kassel professor; first doctorate only; all disciplines.',
   'tags': [('PhD', 'purple'), ('Germany', 'blue')]},
 'optiver-2027': {'mono': 'OX', 'title': 'Oxford Optiver Foundation Scholarship 2027 in UK (Funded)',
   'href': 'oxford-optiver-foundation-scholarship-2027-uk.html',
   'dpill': 'Deadlines Nov 2026 – Jan 2027 (course-dependent)',
   'award': 'Full Oxford course fees + a grant for living costs + induction, mentoring and on-course support.',
   'elig': 'Women ordinarily resident in eligible low/middle-income countries, starting an eligible STEM MSc at Oxford in Oct 2027.',
   'tags': [('Master\u2019s', 'blue'), ('UK', 'teal')]},
 'nvidia-2027': {'mono': 'NV', 'title': 'NVIDIA Graduate Fellowship 2027-28 (Stipend $60,000)',
   'href': 'nvidia-graduate-fellowship-2027-28.html',
   'dpill': 'Deadline 30 Oct 2026 · 8 days left',
   'award': 'Up to $60,000 through your university (stipend, tuition, fees) + a mandatory paid summer internship at NVIDIA.',
   'elig': 'PhD students (any country) with the first PhD year complete, in CS, computer engineering, EE or related fields.',
   'tags': [('PhD', 'purple'), ('Global', 'teal')]},
 'cga-phd': {'mono': 'CGA', 'title': 'Cologne CGA PhD Fellowship 2026 in Germany (Fully Funded)',
   'href': 'cologne-cga-phd-fellowship-2026-germany.html',
   'dpill': 'Deadline 3 Nov 2026 · 12 days left',
   'award': '12 fully funded PhD positions — employment contracts of 3+ years at TV-L E13 65% with a Max Planck-ageing research cluster.',
   'elig': 'MSc (or equivalent) in biology/life-science fields with an excellent record and strong English (C1); strong motivation for ageing research.',
   'tags': [('PhD', 'purple'), ('Germany', 'blue')]},
 'minnesota-ges': {'mono': 'UMN', 'title': 'University of Minnesota Global Excellence Scholarships 2027 in USA (Partially Funded)',
   'href': 'university-of-minnesota-global-excellence-scholarship-2027-usa.html',
   'dpill': 'Early Action I 1 Nov 2026 · 10 days left',
   'award': 'Freshmen: $5,000–$20,000/yr for up to 4 years. Transfers: $10,000/yr for up to 3 years. No separate application.',
   'elig': 'International (non-US) undergraduate applicants to UMN Twin Cities; automatic consideration with the admission application.',
   'tags': [('Bachelor\u2019s', 'blue'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Kassel
A.append(dict(
 slug='university-of-kassel-expose-scholarships-2026-germany',
 title='University of Kassel Exposé Scholarships 2026 in Germany (Funded)',
 meta='University of Kassel Exposé Scholarships 2026: €1,300/month for up to 9 months to write your dissertation exposé at Kassel. Supervisor commitment required. Deadline 1 December 2026. Eligibility, documents and how to apply.',
 short='University of Kassel Exposé Scholarships', kicker='Germany · PhD · Funded', mono='UKAS',
 prov_short='University of Kassel', prov_cat='University · Germany',
 h1='University of Kassel Exposé Scholarships 2026 in Germany (Funded)',
 sub='Nine months of paid time to write the dissertation exposé your doctorate needs — €1,300 a month, provided you already have a Kassel professor willing to supervise you.',
 dpill='Deadline 1 Dec 2026 · 40 days left',
 facts=facts([('Award', '€1,300 per month for up to 9 months; a family allowance of €200 per month is possible on request. The main goal is writing the exposé required for acceptance as a doctoral candidate at Kassel.'),
              ('Eligible', 'Anyone with a commitment from a University of Kassel professor to supervise the doctorate. Only the first doctorate of a person can be funded. An application is possible only once (re-application only after interruption by childbirth, long-term illness or caregiving). All disciplines are eligible.'),
              ('How', 'Apply electronically in English or German: one combined PDF, in the order stated — motivation letter, project abstract, CV, degree copy/transcript, supervisor\u2019s letter of recommendation (you attach it yourself). Submit via the official application link on the uni-kassel.de exposé page.'),
              ('Deadline', '1 December 2026 (current call of 26 August 2026). The exposé-scholarship committee meets in mid-February and results are sent out by the end of February.'),
              ('Fine print', 'Each supervisor may support only one applicant per award round. The German version of the call is legally binding. Funding ends at the end of the funding period or on acceptance by the doctoral committee, whichever comes first.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Kassel</strong> (Universität Kassel, founded 1971, in central Germany) awards <strong>Exposé Scholarships</strong> to people who are planning a doctorate at the university and need paid, supervised time to write the <strong>dissertation exposé</strong> — the detailed research proposal that German universities require for acceptance as a doctoral candidate, and that also serves as the basis for applying to external scholarship foundations. This is a bridge grant: it covers the months between having a supervisor and being formally accepted as a doctoral candidate.</p>
      <p>The scholarship is <strong>€1,300 per month for up to nine months</strong>, with a <strong>family allowance of €200 per month</strong> possible on request. You work on the exposé under the guidance of your supervisor and gain access to the university\u2019s academic environment while you prepare the full doctoral proposal.</p>
      <p>The current call (published 26 August 2026) closes on <strong>1 December 2026</strong> — 40 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Have a <strong>commitment from a professor of the University of Kassel</strong> to supervise your doctorate. You cannot apply without this.</li>
        <li>It must be your <strong>first doctorate</strong> — repeat doctoral funding is not permitted.</li>
        <li>An application is <strong>possible only once</strong>; re-application is allowed only if a previous funding period was interrupted by unusual life circumstances such as childbirth, long-term illness or caregiving duties.</li>
        <li>Each supervisor may support <strong>only one person per award round</strong>, so secure the commitment early.</li>
        <li>All disciplines at the university are eligible — natural sciences, engineering, architecture and planning, agriculture and environmental protection, social sciences, humanities and fine arts.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€1,300 per month</strong>, granted for up to nine months.</li>
        <li><strong>€200 per month family allowance</strong> on request.</li>
        <li>Structured supervision by a University of Kassel professor while preparing the dissertation exposé.</li>
        <li>A finished exposé that qualifies you for <strong>acceptance as a doctoral candidate</strong> at Kassel and for applications to other German scholarship foundations.</li>
        <li>No tuition fees are charged to doctoral candidates at public German universities.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>A <strong>letter of motivation</strong> (max. two pages) stating (a) your motivation for the doctorate, (b) your motivation for doing it at the University of Kassel, and (c) how you plan to finance the doctorate after the funding period ends.</li>
        <li>An <strong>abstract of the planned project</strong> (max. two pages plus bibliography): current state of research and your preliminary work, goals and research questions, methods, and expected scientific contribution.</li>
        <li>A <strong>CV in tabular form</strong>.</li>
        <li>A <strong>copy of your higher qualifying university degree</strong> (if not yet available, attach a transcript of records).</li>
        <li>A <strong>letter of recommendation from your supervisor</strong>, assuring supervision and outlining how the doctorate should be financed after the funding period — you attach this letter to your own application.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure a supervisor first</strong>Contact professors at the University of Kassel in your research area with a CV and research idea, and obtain a written commitment to supervise your doctorate plus a letter of recommendation.</li>
        <li><strong>Draft the exposé materials</strong>Prepare the motivation letter and the two-page project abstract with bibliography in German or English, following the official call exactly.</li>
        <li><strong>Combine everything into one PDF</strong>Merge the documents in the order stated in the call (motivation letter, abstract, CV, degree copy, supervisor letter). A wrong order or split files is an exclusion criterion.</li>
        <li><strong>Submit electronically</strong>Apply via the official electronic application link given in the call for applications on uni-kassel.de by <strong>1 December 2026</strong>.</li>
        <li><strong>Wait for the committee decision</strong>The exposé-scholarship committee meets in mid-February; results are sent out by the end of February.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this a full PhD scholarship?',
  'No — and that is its honest purpose. It is a preparatory grant (up to 9 months) that pays you to write the dissertation exposé needed for acceptance as a doctoral candidate. Full doctoral funding (employment contract, DAAD, foundations) comes afterwards.'),
 ('Do I need a supervisor before applying?',
  'Yes. A confirmed supervision commitment from a University of Kassel professor is a hard requirement, and each professor may support only one applicant per round. Without it, the application cannot succeed.'),
 ('Can I apply if I already have a PhD or started another doctorate?',
  'No. Only the first doctorate of a person can be funded, and each person may apply only once.'),
 ('What language should the application be in?',
  'German or English, per the official call. All documents go into a single PDF in the order the call lists them.'),
 ('What happens if the supervisor letter is missing or the PDF order is wrong?',
  'The call states the documents must be combined in one PDF in the order given — an exclusion criterion. Attach the supervisor letter yourself; do not have the professor send it separately.'),
 ('How much is the family allowance?',
  '€200 per month, possible upon request — on top of the €1,300 monthly stipend.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official call for applications "Exposé Scholarships of the University of Kassel" (call of 26 August 2026, hosted on uni-kassel.de): closing date 1 December 2026; €1,300/month up to 9 months; €200/month family allowance on request; supervisor commitment required; first doctorate only; one application per person (re-application only after interruption by childbirth/illness/caregiving); one applicant per supervisor per round; committee meets mid-February, results by end of February; documents in German or English in one PDF in stated order (motivation letter max 2 pages incl. post-funding financing plan, project abstract max 2 pages + bibliography, tabular CV, degree copy or transcript, supervisor recommendation letter attached by the applicant); contact per the official call: stipendium@uni-kassel.de, phone +49 561 804-7742 / -2263. Corroborated by the uni-kassel.de exposé-scholarships page ("Next application deadline: 1 December 2026"), opportunitiesinfo.com and the Earlier round Indeed posting. The exact funding start date for this round is not stated in the call and is not invented. No GPA, IELTS or test thresholds are published — none are stated.</p>
''',
 dl_long='Deadline: 1 December 2026 (current call published 26 August 2026; 40 days from 22 Oct 2026). Committee meets mid-February; results sent out by the end of February.',
 offlinks=[('Exposé Scholarships — official page (uni-kassel.de)', 'https://www.uni-kassel.de/uni/en/research/supporting-the-next-generation-of-scientists/graduiertenakademie/financing/scholarships-and-fellowships/expose-scholarships.html')],
 related_titles=['erfurt-phd', 'ieg-mainz', 'daad', 'hzdr-2027', 'hanns-seidel'],
))

# ---------------------------------------------------------------- 2. Optiver
A.append(dict(
 slug='oxford-optiver-foundation-scholarship-2027-uk',
 title='Oxford Optiver Foundation Scholarship 2027 in UK (Funded)',
 meta='Oxford Optiver Foundation Scholarship 2027: up to 6 awards for women from low/middle-income countries for eligible STEM master\u2019s at the University of Oxford. Full course fees + living-cost grant. Apply by your course deadline (Nov 2026 – Jan 2027).',
 short='Oxford Optiver Foundation Scholarship', kicker='UK · Master\u2019s (STEM) · Funded', mono='OX',
 prov_short='University of Oxford', prov_cat='University · UK',
 h1='Oxford Optiver Foundation Scholarship 2027 in UK (Funded)',
 sub='Full Oxford course fees plus a grant for living costs — for women from low and middle-income countries taking up a STEM master\u2019s. The next cohort starts in October 2027.',
 dpill='Deadlines Nov 2026 – Jan 2027 (course-dependent)',
 facts=facts([('Award', 'Full financial support covering course fees, plus a grant for living costs. Scholars also get tailored induction activities, mentoring and on-course support. Up to 6 scholarships for the October 2027 intake (fifth cohort of a five-year programme supporting up to 30 students in total).'),
              ('Eligible', 'Women who are ordinarily resident in an eligible low or middle-income country, applying to start an eligible taught STEM master\u2019s at Oxford in October 2027. Current Oxford students and holders of deferred offers are not eligible.'),
              ('How', 'No separate first step: submit your Oxford graduate application by your course\u2019s November, December or January deadline and tick the scholarship box. Eligible applicants are then invited to complete an additional form about their socio-economic background; an academic panel assesses on merit and potential.'),
              ('Deadline', 'Your course\u2019s graduate-application deadline (November, December or January — check your chosen MSc). Scholarship decisions are mostly sent out by email in May.'),
              ('Fine print', 'The sex indicated on the graduate application must match identity documents (passport/visa); transgender applicants with a binary female passport/visa marker are included. Eligibility is judged against the official low/middle-income country list on the Oxford page.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Optiver Foundation Scholarships</strong> at the <strong>University of Oxford</strong> exist for a precise reason: financial barriers keep talented students — especially women from disadvantaged backgrounds — away from postgraduate study, and the gap is widest in STEM subjects outside the biomedical and life sciences. Funded by a generous donation from the <strong>Optiver Foundation</strong>, the five-year programme supports up to <strong>30 taught master\u2019s students in total</strong>, and the next cohort — the <strong>fifth</strong> — begins in <strong>October 2027</strong>.</p>
      <p>Scholars join the Departments of <strong>Statistics, Computer Science, Physics, Chemistry and Engineering Science</strong>, or the <strong>Mathematical Institute</strong>, and receive <strong>full financial support for course fees plus a grant for living costs</strong>, together with tailored induction activities, mentoring and on-course support throughout their degree.</p>
      <p>There is no single scholarship deadline: you apply through your <strong>course\u2019s normal graduate-application deadline in November, December or January</strong> (from today, 22 October 2026, those are weeks to months away — check your course page).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be <strong>female</strong> — the sex stated on the graduate application must match that shown in identity documents (e.g. passport or visa). Transgender people able to obtain a passport or visa in a binary sex other than their legal sex are included under this rule.</li>
        <li>Be <strong>ordinarily resident in an eligible low or middle-income country</strong> (the official list is on the Oxford scholarship page; India, Pakistan, Bangladesh, Nigeria, Ghana, Kenya, Egypt, South Africa and Brazil are among the eligible countries reported).</li>
        <li>Be <strong>applying to start an eligible full-time taught master\u2019s at Oxford in October 2027</strong> in one of the participating STEM courses (list below).</li>
        <li><strong>Not be a current Oxford student</strong> and <strong>not hold a deferred offer</strong> — the scheme is for new applicants only.</li>
        <li>Meet the <strong>academic entry requirements of the chosen course</strong> (assessed by the academic panel on merit and potential).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full coverage of Oxford course fees</strong> for the master\u2019s programme.</li>
        <li><strong>A grant for living costs</strong> throughout the programme.</li>
        <li><strong>Tailored induction activities</strong> designed for the scholars.</li>
        <li><strong>Mentoring and on-course academic support</strong> from Oxford staff and the programme team.</li>
        <li>Networking with fellow women scholars in Oxford\u2019s STEM community.</li>
      </ul>
      <h2 id="courses">Eligible courses</h2>
      <p>The eligible taught master\u2019s courses are:</p>
      <ul>
        <li>MSc Energy Systems (Engineering Science)</li>
        <li>MSc Advanced Computer Science</li>
        <li>MSc Mathematical and Theoretical Physics</li>
        <li>MSc Mathematical Modelling and Scientific Computing</li>
        <li>MSc Mathematical Sciences</li>
        <li>MSc Mathematics and Foundations of Computer Science</li>
        <li>MSc in Quantum Technologies</li>
        <li>MSc Statistical Science</li>
        <li>MSc Theoretical and Computational Chemistry</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>complete graduate application for your chosen MSc</strong> with all course-required documents (transcripts, references, statement of purpose, CV — requirements vary by course, so check the course page rather than any generic list).</li>
        <li>The <strong>additional Optiver scholarship form</strong> (only if invited): this asks about your socio-economic background to assess disadvantage and under-representation. Answer accurately and follow its evidence instructions.</li>
        <li>Evidence that your stated sex matches your <strong>identity documents</strong> (passport or visa).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check your country and course</strong>Confirm on the official Oxford page that your country of ordinary residence is eligible and that your chosen MSc is one of the nine eligible courses, then note the course\u2019s November, December or January deadline.</li>
        <li><strong>Apply for graduate study</strong>Submit the full Oxford graduate application for your course by that deadline, and <strong>tick the Optiver Foundation Scholarship box</strong> on the form.</li>
        <li><strong>Complete the additional form if invited</strong>If you meet the advertised eligibility criteria, Oxford will invite you to complete the extra socio-economic background form — submit it as instructed.</li>
        <li><strong>Assessment by academic panel</strong>Eligible offer-holders who completed the form are assessed by an academic panel on academic merit and potential.</li>
        <li><strong>Decision</strong>Most scholarship offers are sent by email in May 2027. Accepting the scholarship secures your funding as long as you meet the conditions of your offer of a place.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Optiver Scholarship fully funded?',
  'Yes, for the scholars selected: full Oxford course fees plus a grant for living costs, plus induction, mentoring and on-course support. Only up to 6 awards are available for the October 2027 intake, so it is highly competitive.'),
 ('Who exactly can apply?',
  'Women ordinarily resident in the eligible low/middle-income countries, who are new applicants to one of the nine eligible STEM master\u2019s starting October 2027. Current Oxford students and deferred-offer holders are excluded.'),
 ('Is there a separate scholarship application?',
  'Not at first — you tick the scholarship box on the Oxford graduate application. Only candidates who meet the advertised eligibility are then asked to complete an additional socio-economic background form.'),
 ('What is the deadline?',
  'There is no single date: apply by your course\u2019s November, December or January graduate-application deadline. Offers are mostly made in May.'),
 ('Does it cover biomedical or life-science courses?',
  'No. The programme targets STEM disciplines where women\u2019s postgraduate participation is lowest — statistics, computer science, physics, chemistry, engineering science and mathematics — not biomedical or life sciences.'),
 ('Can transgender women apply?',
  'The official terms state that the sex on the graduate application must match identity documents, and note that transgender people may be able to obtain a passport or visa in a binary sex other than their legal sex.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official University of Oxford page "Optiver Foundation Scholarships" (ox.ac.uk): five-year programme, up to 30 taught master\u2019s students total, next (fifth) cohort begins October 2027; departments (Statistics, Computer Science, Physics, Chemistry, Engineering Science, Mathematical Institute); full fees + living-cost grant + induction/mentoring/on-course support; eligible applicants apply by the course\u2019s November/December/January deadline and tick the box, then complete an additional socio-economic form; assessed by academic panel on merit and potential; offers mostly by May; excludes current students and deferred-offer holders; sex on application must match identity documents. Eligible-course list (9 MSc programmes) and the October 2027 fifth-cohort framing corroborated by youthexpat.com, afterschoolafrica.com and scholarshipunion.com (all updated within ~45 days). Queue title "2026 (Funded)" was stale: the October 2026 intake is closed, so the article covers the live October 2027 intake. No single "31 January" deadline is official — deadlines are course-dependent. No exact living-grant figure is published on the Oxford page — none is invented.</p>
''',
 dl_long='Deadline: your course\u2019s Oxford graduate-application deadline — November, December or January (course-dependent; check your chosen MSc page). Scholarship offers are mostly sent out by email in May 2027.',
 offlinks=[('Optiver Foundation Scholarships — official page (University of Oxford)', 'https://www.ox.ac.uk/admissions/graduate/fees-and-funding/fees-funding-and-scholarship-search/optiver-foundation-scholarships')],
 related_titles=['vidyadhan', 'wings', 'clara-collet', 'reach-oxford', 'harvard-lead'],
))

# ---------------------------------------------------------------- 3. NVIDIA
A.append(dict(
 slug='nvidia-graduate-fellowship-2027-28',
 title='NVIDIA Graduate Fellowship 2027-28 (Stipend $60,000)',
 meta='NVIDIA Graduate Fellowship 2027-28: up to $60,000 per award for PhD students in accelerated-computing research, paid through your university, plus a mandatory summer internship at NVIDIA. Deadline 30 October 2026 (recommendations included).',
 short='NVIDIA Graduate Fellowship', kicker='Global · PhD · Funded', mono='NV',
 prov_short='NVIDIA Research', prov_cat='Corporate · Global',
 h1='NVIDIA Graduate Fellowship 2027-28 (Stipend $60,000)',
 sub='Up to $60,000 for your PhD research, mentorship from NVIDIA researchers, and a required summer internship inside the company — open to doctoral students worldwide.',
 dpill='Deadline 30 Oct 2026 · 8 days left',
 facts=facts([('Award', 'Up to US$60,000 per award for the 2027–28 academic year (9 months), paid through the fellow\u2019s university for stipend, tuition and required fees. Amounts can vary with country/region. Includes a mandatory paid in-person summer internship at an NVIDIA research office in summer 2027, plus access to NVIDIA researchers, products and technology.'),
              ('Eligible', 'Full-time PhD students from any country who have completed at least the first year of PhD studies, majoring in computer science, computer engineering, system architecture, electrical engineering or a related field; actively engaged in thesis research; remaining a full-time student through the award year and not planning to graduate before May/June 2028. Full-time NVIDIA employees and immediate family members of NVIDIA employees are excluded.'),
              ('How', 'Submit in the official submission portal: research proposal (max 2 pages + bibliography), CV/resume, and 2–3 recommendation letters (at least 2, including the thesis advisor). The university must administer the award — payment goes to the university, not the student. All materials including recommendations are due by the deadline.'),
              ('Deadline', '30 October 2026 — including all recommendation letters. Past fellows may reapply.'),
              ('Research fit', 'Research relevant to accelerated computing: AI/ML, autonomous vehicles, computer graphics, robotics, healthcare, high-performance computing, plus architecture, networking, security and scientific computing. The proposal should show a concrete link to NVIDIA\u2019s technologies or research interests.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>NVIDIA Graduate Fellowship Program</strong> — running since 2002 and now in its 26th year, with more than <strong>220 grants worth around $8 million</strong> awarded to date — supports doctoral students whose research advances <strong>accelerated computing</strong>. It is one of the most generous corporate doctoral awards in computing: fellows get funding, a mentor network inside NVIDIA, and a required summer internship at an NVIDIA research office before the fellowship year begins.</p>
      <p>The current round covers the <strong>2027–28 academic year (9 months)</strong>. Each award provides <strong>up to US$60,000</strong>, paid through the fellow\u2019s university to cover stipend, tuition and required fees. Applications — including all recommendation letters — close on <strong>30 October 2026</strong>, 8 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>full-time PhD student</strong> who has <strong>completed at least the first year</strong> of PhD-level studies at the time of application.</li>
        <li>Major in <strong>computer science, computer engineering, system architecture, electrical engineering, or a related field</strong>, and be actively engaged in research as part of the PhD thesis.</li>
        <li>Remain a <strong>full-time, active PhD student throughout the nine-month award year</strong> and <strong>not plan to graduate before May/June 2028</strong>.</li>
        <li>Be <strong>available for the mandatory in-person summer internship</strong> at an NVIDIA research office in summer 2027 (offices listed include the US, Canada, Germany, Sweden, Finland, Switzerland, Israel, Taiwan and Singapore).</li>
        <li>Be from <strong>any country</strong> — international students are explicitly eligible.</li>
        <li><strong>Not be a full-time NVIDIA employee</strong> or an <strong>immediate family member</strong> of a current NVIDIA employee.</li>
        <li>Your <strong>university must be able to administer the award</strong> — funds are paid to the university, not directly to the fellow.</li>
        <li>Past fellows may reapply.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to $60,000</strong> per award for the 2027–28 academic year (amounts can vary with country/region), administered through your university for stipend, tuition and required fees.</li>
        <li><strong>Mandatory paid summer internship</strong> at an NVIDIA research office before the fellowship year — real industry research experience, not an optional extra.</li>
        <li><strong>Mentorship from NVIDIA researchers</strong> and access to NVIDIA products, technology and technical staff.</li>
        <li>A credential from one of the longest-running corporate research fellowship programmes (since 2002), with a network of 220+ past fellows.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Research proposal</strong> — max 2 pages plus a bibliography (the bibliography does not count toward the limit). Put your name at the top; text and images must fit within 2 pages.</li>
        <li><strong>Resume or CV</strong> with contact information.</li>
        <li><strong>2–3 recommendation letters</strong> — at least 2, including one from the thesis advisor/professor; no more than 3. Letters are submitted through the portal and are due by the same deadline.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm eligibility</strong>First year of PhD complete, thesis research active, full-time through 2027–28, internship availability in summer 2027, university able to administer the award.</li>
        <li><strong>Sharpen the research question</strong>Write a proposal that links your research concretely to accelerated computing and NVIDIA\u2019s technologies — a precise question, method and results achieved beats a broad "machine learning" label.</li>
        <li><strong>Line up recommenders early</strong>Secure 2–3 letters including your thesis advisor now — letters are due on the same 30 October deadline and cannot arrive later.</li>
        <li><strong>Submit in the official portal</strong>Manage the application and recommendation letters in NVIDIA\u2019s fellowship submission portal before <strong>30 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the NVIDIA fellowship open to international students?',
  'Yes. The programme is open to PhD students from any country, as long as they meet the field, enrolment and internship requirements and their university can administer the award.'),
 ('Is the $60,000 paid to me directly?',
  'No. The award is disbursed to your university, which administers it for stipend, tuition and required fees. NVIDIA notes that amounts can vary with country or region.'),
 ('Is the summer internship really mandatory?',
  'Yes. An in-person summer internship at an NVIDIA research office before the fellowship year is a required part of the programme. Do not apply if you cannot be available in summer 2027.'),
 ('Can I apply if I graduate in early 2028?',
  'The terms require you to remain a full-time PhD student through the award year and not plan to graduate before May/June 2028.'),
 ('What does the research proposal need?',
  'A maximum of 2 pages plus bibliography, your name at the top, showing how the research connects to NVIDIA\u2019s technologies or research interests. Be precise about the question, method and results so far.'),
 ('Can past fellows apply again?',
  'Yes — past fellows may reapply in a new cycle.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across six corroborating sources: buddy4study.com (deadline 30-Oct-2026; up to $60,000; completed first year of PhD; CS/CE/system architecture/EE or related; full-time through award year; mandatory summer internship; not immediate family of NVIDIA employee; award paid to the university; documents: 2-page proposal + bibliography, CV, 2-3 letters incl. advisor), al-khwarizmi.com (2027-28 round; deadline 30 Oct 2026 incl. letters; international eligible; past fellows may reapply), scholargem.org (up to $60,000; deadline 30 Oct 2026; research relevant to accelerated computing), en.cryptonomist.ch (since 2002; 220+ grants, ~$8M; up to $60,000; deadline 30 Oct 2026), charityjournal.org (26th year; mandatory paid summer 2027 internship; internship offices US/Canada/Germany/Sweden/Finland/Switzerland/Israel/Taiwan/Singapore; must not graduate before May/June 2028), selibeng.com (2-3 letters; proposal format; university administration). Queue title "NVIDIA Graduate Fellowship 2026" was stale: the live round is the 2027-28 fellowship, so the article is titled accordingly. Research-area lists (AI/ML, autonomous vehicles, graphics, robotics, healthcare, HPC) are as reported by the trackers. No invented stipend breakdown or selection timeline is stated.</p>
''',
 dl_long='Deadline: 30 October 2026 — including all recommendation letters (8 days from 22 Oct 2026). Fellowship year: 2027–28 (9 months); mandatory summer internship in summer 2027.',
 offlinks=[('NVIDIA Graduate Fellowship 2027–28 — full guide (ScholarGem)', 'https://scholargem.org/nvidia-graduate-fellowship/'),
           ('NVIDIA Graduate Fellowship Program 2027/2028 — apply guide', 'https://www.buddy4study.com/scholarship/nvidia-graduate-fellowship-program'),
           ('NVIDIA International Graduate Fellowship 2027/2028 — requirements', 'https://selibeng.com/nvidia-international-graduate-fellowship-program-2027-2028/')],
 related_titles=['singa2027', 'bis-phd-2027', 'jispa-phd', 'justcool', 'erfurt-phd'],
))

# ---------------------------------------------------------------- 4. CGA
A.append(dict(
 slug='cologne-cga-phd-fellowship-2026-germany',
 title='Cologne CGA PhD Fellowship 2026 in Germany (Fully Funded)',
 meta='Cologne Graduate School of Ageing Research (CGA) 2026: 12 fully funded PhD positions in ageing research at Cologne/Max Planck. TV-L E13 65% contracts for 3+ years. Application deadline 3 November 2026. Eligibility and how to apply.',
 short='Cologne CGA PhD Fellowship', kicker='Germany · PhD · Fully Funded', mono='CGA',
 prov_short='Cologne Graduate School of Ageing Research', prov_cat='Graduate School · Germany',
 h1='Cologne CGA PhD Fellowship 2026 in Germany (Fully Funded)',
 sub='Twelve fully funded PhD positions in the biology of ageing — paid employment contracts, 49 research groups, and a structured English-language doctoral programme in Cologne.',
 dpill='Deadline 3 Nov 2026 · 12 days left',
 facts=facts([('Award', '12 fully funded PhD positions: initial employment contracts of at least 3 years at TV-L E13 65% (or an equivalently paid Max Planck PhD support contract), dedicated supervision with thesis advisory committees, a comprehensive English-language PhD programme, mentoring and coaching, methodology and soft-skills courses, annual conference travel grants, and intensive administrative support for international students.'),
              ('Eligible', 'MSc or equivalent in biology, cell/molecular biology, biochemistry, bioengineering, bioinformatics, biophysics, genetics, medical biology, translational medicine or related fields; excellent academic performance; strong motivation for ageing research; very good English (C1, written and spoken). International applicants welcome.'),
              ('How', 'Apply online at the official CGA application portal (application.ageing-grad-school.de): motivation letter, certificates, transcripts, CV, references. Two recommendations must be submitted by 10 November 2026. Up to 80 shortlisted candidates are interviewed online 7–9 Dec 2026; 25 finalists are invited to a recruitment week in Cologne 15–19 Feb 2027.'),
              ('Deadline', '3 November 2026 (application period 11 August – 3 November 2026). Projects can start individually between 1 July and 1 October 2027; CGA Welcome Days in October 2027.'),
              ('Fine print', 'The school encourages women and applicants with disabilities to apply. Applications may be screened with AI text detectors — write authentically. The programme suits life-science graduates with real lab experience.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Cologne Graduate School of Ageing Research (CGA)</strong> — a joint graduate school of the <strong>University of Cologne</strong> and the <strong>Max Planck Society</strong> (including the Max Planck Institute for Biology of Ageing and the CECAD Cluster of Excellence) — is one of Europe\u2019s most prestigious ageing-research clusters, with <strong>49 interdisciplinary research groups</strong>. For the 2026 call it offers <strong>12 fully funded PhD positions</strong> in the molecular biology of ageing.</p>
      <p>Unlike stipend scholarships, these are <strong>employment contracts</strong>: initial contracts of <strong>at least three years</strong>, paid on the German public-sector scale <strong>TV-L E13 at 65%</strong> (or an equivalently remunerated Max Planck PhD support contract). The programme is conducted entirely in <strong>English</strong>, with thesis advisory committees, individual career mentoring, methodology and soft-skills courses, annual conference travel grants, and intensive support for international students in all administrative matters.</p>
      <p>The application window — <strong>11 August to 3 November 2026</strong> — closes in 12 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold an <strong>MSc or equivalent degree</strong> in biology, cell/molecular biology, biochemistry, bioengineering, bioinformatics, biophysics, genetics, medical biology, translational medicine, or a related field.</li>
        <li>Show <strong>excellent academic performance</strong> in BSc and MSc studies.</li>
        <li>Have a <strong>clear interest in the research areas above and strong motivation for ageing research</strong> — real lab experience and a research thesis or internship strengthen the application.</li>
        <li>Have <strong>very good English skills (C1 level, written and spoken)</strong>.</li>
        <li>International applicants are explicitly welcome; the school is committed to diversity and equal opportunities and especially encourages women and people with disabilities to apply.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>12 fully funded PhD positions</strong> with employment contracts of at least 3 years (TV-L E13 65% or equivalent Max Planck support contract).</li>
        <li><strong>Dedicated supervision</strong> with academic guidance from thesis advisory committees.</li>
        <li><strong>Comprehensive English-language PhD programme</strong> in Cologne — a vibrant, affordable student city.</li>
        <li><strong>Individual career mentoring and coaching</strong>, plus methodology and soft-skills courses.</li>
        <li><strong>Annual conference travel grants</strong>.</li>
        <li><strong>Intensive support for international students</strong> in all administrative matters (visa, registration, housing guidance).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Motivation letter</strong> — written authentically (the school notes it may use AI text detectors on applications).</li>
        <li><strong>Degree certificates and transcripts</strong> (BSc and MSc).</li>
        <li><strong>CV</strong>.</li>
        <li><strong>Research proposal</strong> — per the official application scheme: prepare your CV, transcripts, certificates/diplomas and research proposal before starting.</li>
        <li><strong>Two recommendations</strong> — these must be submitted by <strong>10 November 2026</strong>, one week after the application deadline. Contact referees early.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Prepare your documents</strong>Finalise your CV, transcripts, certificates/diplomas and research proposal, and contact your two referees now so their letters land by 10 November 2026.</li>
        <li><strong>Submit online</strong>Complete and submit the application via the official portal — application.ageing-grad-school.de — by <strong>3 November 2026</strong>.</li>
        <li><strong>Multistep screening (4–26 Nov 2026)</strong>The CGA coordination checks completeness and eligibility; qualifying applications are assessed by CGA faculty on academic qualifications and research achievements.</li>
        <li><strong>Online panel interviews (7–9 Dec 2026)</strong>Up to 80 shortlisted candidates get ~20-minute online panel interviews, including a short presentation of their current research project.</li>
        <li><strong>Onsite recruitment week (15–19 Feb 2027)</strong>About 25 top candidates are invited to Cologne: faculty poster session, up to five lab visits with personal interviews, campus tour. Hotel accommodation is provided for those travelling far; travel costs are refunded.</li>
        <li><strong>Admission and start</strong>Final offers about two weeks after recruitment week; individual PhD projects can start between <strong>1 July and 1 October 2027</strong>, with CGA Welcome Days in October 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this a stipend or a salary?',
  'Effectively a salary: fellows are hired on employment contracts of at least 3 years at TV-L E13 65% (or an equivalent Max Planck PhD support contract), not on a fixed stipend. That also means standard German social-security coverage.'),
 ('How many positions are there and how competitive is it?',
  '12 positions. The selection funnel narrows to ~80 online interviews, then 25 candidates at the onsite recruitment week, then up to 12 offers. Start early and submit well before the deadline.'),
 ('When do the referees\u2019 letters have to arrive?',
  'By 10 November 2026 — one week after the 3 November application deadline. Ask your referees now.'),
 ('Is the programme in German?',
  'No. The PhD programme is conducted in English, and applicants need very good English (C1, written and spoken).'),
 ('Who is this programme best suited for?',
  'Life-science graduates with genuine lab experience (a research thesis or internship) who can describe a scientific question clearly and want to specialise in the molecular biology of ageing in a structured international programme.'),
 ('Can I use AI tools on my application?',
  'The school warns it may use AI text detectors on applications — write the motivation letter and proposal in your own authentic voice.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official CGA call PDF (application period 11 Aug - 3 Nov 2026; online application at application.ageing-grad-school.de; contact cga-coordination@uni-koeln.de; website ageing-grad-school.de) and the official "Application scheme 2026-2027" PDF (references due 10 Nov 2026; assessment 4-26 Nov; online panel interviews 7-9 Dec 2026; onsite recruitment week 15-19 Feb 2027; admission ~2 weeks after; projects start 1 Jul - 1 Oct 2027; CGA Welcome Days Oct 2027), corroborated by daad.de, mpg.de ("12 fully funded PhD positions"), EURAXESS and nextdeadlines.com. Eligibility and funding terms (MSc fields listed, excellent record, English C1, TV-L E13 65% contracts of >=3 years, 49 research groups, mentoring, travel grants, international-student support) are consistent across the official PDF, DAAD and Max Planck listings. No invented salary figure is stated — TV-L E13 65% is the published pay scale, not a monthly amount.</p>
''',
 dl_long='Deadline: 3 November 2026 (12 days from 22 Oct 2026). Referee letters due 10 November 2026. Online panel interviews 7–9 December 2026; onsite recruitment week 15–19 February 2027; projects start 1 July – 1 October 2027.',
 offlinks=[('CGA application scheme 2026-2027 — official PDF', 'https://www.ageing-grad-school.de/fileadmin/user_upload/Downloads/Application_scheme_2026_2027.pdf'),
           ('12 fully funded PhD positions — Max Planck (mpg.de)', 'https://www.mpg.de/26912615/12-fully-funded-phd-positions-2026'),
           ('12 fully funded PhD positions at CGA — DAAD', 'https://www.daad.de/en/studying-in-germany/phd-studies-research/phd-germany/detail/mpi-for-biology-tuebingen-university-of-tuebingen-friedrich-miescher-laboratory-tuebingeninternational-max-planck-research-school-from-molecules-to-organisms-fully-funded-phd-positions-imprs-from-molecules-to-organisms-10061/')],
 related_titles=['ieg-mainz', 'erfurt-phd', 'daad', 'hzdr-2027', 'singa2027'],
))

# ---------------------------------------------------------------- 5. Minnesota
A.append(dict(
 slug='university-of-minnesota-global-excellence-scholarship-2027-usa',
 title='University of Minnesota Global Excellence Scholarships 2027 in USA (Partially Funded)',
 meta='University of Minnesota Global Excellence Scholarships 2027: $5,000–$20,000/yr merit awards for international freshmen (up to 4 years) and $10,000/yr for transfers (up to 3 years). No separate application. Early Action I deadline 1 November 2026.',
 short='University of Minnesota Global Excellence Scholarships', kicker='USA · Bachelor\u2019s · Partially Funded', mono='UMN',
 prov_short='University of Minnesota', prov_cat='University · USA',
 h1='University of Minnesota Global Excellence Scholarships 2027 in USA (Partially Funded)',
 sub='A merit award for international undergraduates at Minnesota Twin Cities — $5,000 to $20,000 a year, and your admission application is automatically your scholarship application.',
 dpill='Early Action I 1 Nov 2026 · 10 days left',
 facts=facts([('Award', 'Freshmen: $5,000–$20,000 per year toward tuition, renewable for up to 4 years. International transfer students entering in the fall semester: $10,000 per year for up to 3 years. The scholarship covers tuition only — not living expenses, health insurance or other personal costs.'),
              ('Eligible', 'International students (non-US citizens) applying for a full-time undergraduate degree at the University of Minnesota Twin Cities; strong academic record with leadership and extracurricular achievement. F-1 student-visa holders.'),
              ('How', 'There is no separate scholarship application: eligible applicants are automatically considered from their admission application (Common App or the university application). Apply by the Early Action deadline for full consideration.'),
              ('Deadline', '1 November 2026 (Early Action I) for the fall 2027 intake — 10 days from today (22 Oct 2026). Regular Decision: 1 January 2027. Spring-entry transfers are considered only on a funds-available basis.'),
              ('Renewal', 'Awards renew annually with satisfactory academic progress (the university requires a minimum of 30 credits per year for renewal) and continued full-time enrolment.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Global Excellence Scholarship (GES)</strong> is the <strong>University of Minnesota Twin Cities\u2019</strong> flagship merit award for international undergraduates — competitive, academic-merit-based, and refreshingly simple: <strong>there is no separate scholarship form</strong>. Every international freshman or transfer applicant is automatically considered from the admission application itself.</p>
      <p>An honest framing first: this is a <strong>tuition award</strong>, not a full ride. For the current fall 2027 cycle, international <strong>freshmen can receive $5,000–$20,000 per year</strong> for up to four years, and <strong>fall-entry transfer students $10,000 per year</strong> for up to three years. Living expenses, health insurance and personal costs are not covered, so plan additional funding for those.</p>
      <p>The live cycle is <strong>fall 2027 admission</strong>. The <strong>Early Action I deadline — 1 November 2026</strong> — is 10 days from today (22 October 2026), and applying by it gives full scholarship consideration.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> (a non-US citizen — the award is not open to US nationals).</li>
        <li>Apply for a <strong>full-time undergraduate degree programme</strong> at the University of Minnesota Twin Cities.</li>
        <li>Show a <strong>strong academic record</strong> — top grades, plus leadership, extracurriculars and the personal qualities the university cites (motivation, perseverance, maturity).</li>
        <li>Hold or plan to hold an <strong>F-1 student visa</strong> and enrol full time.</li>
        <li>Meet the university\u2019s <strong>English-proficiency requirements</strong> (e.g. TOEFL, IELTS or PTE — some applicants may qualify for an exemption).</li>
        <li>Submit a <strong>complete admission application by the deadline</strong> — automatic consideration only applies to complete, on-time applications.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Freshmen: $5,000–$20,000 per year</strong> toward tuition, renewable for <strong>up to 4 years</strong>.</li>
        <li><strong>Transfer students (fall entry): $10,000 per year</strong> for <strong>up to 3 years</strong>.</li>
        <li><strong>No separate application</strong> — the award decision arrives with the admission offer.</li>
        <li><strong>No GRE/GMAT</strong> and <strong>test-optional admissions</strong> (ACT/SAT optional).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>undergraduate admission application</strong> (Common App or the university\u2019s own application) — this doubles as the scholarship application.</li>
        <li><strong>High-school transcript</strong> (with a certified English translation if not in English).</li>
        <li><strong>English-proficiency evidence</strong> (TOEFL/IELTS/PTE) unless an exemption applies.</li>
        <li>A <strong>$55 non-refundable application fee</strong> (automatic fee waivers may apply to eligible applicants).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Start the admission application</strong>Begin the University of Minnesota Twin Cities undergraduate application (Common App or university application) now — scholarship consideration is automatic, so the admission application is the whole task.</li>
        <li><strong>Complete it by Early Action I</strong>Submit everything — transcript, English-proficiency evidence, fee — by <strong>1 November 2026</strong> for full scholarship consideration.</li>
        <li><strong>Receive the award with your offer</strong>If selected, the scholarship amount is included in the admission offer.</li>
        <li><strong>Keep it renewed</strong>Maintain full-time enrolment and the required academic progress (minimum 30 credits per year) to renew the award each year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Global Excellence Scholarship fully funded?',
  'No — it is a merit-based tuition award. Freshmen get $5,000–$20,000 per year and transfers $10,000 per year. It does not cover living expenses, health insurance or personal costs, so it is honestly a partial award.'),
 ('Do I need a separate scholarship application?',
  'No. Every eligible international applicant is automatically considered from the admission application. Just make sure the application is complete and on time.'),
 ('What is the deadline?',
  '1 November 2026 for Early Action I (fall 2027 intake) — the deadline for full scholarship consideration. Regular Decision is 1 January 2027. Transfer students entering in spring are considered only if funds remain.'),
 ('Are SAT/ACT scores required?',
  'No — the university is test-optional for admission.'),
 ('What does it take to renew the scholarship?',
  'Satisfactory academic progress — the university requires at least 30 credits per year — plus continued full-time enrolment.'),
 ('Can transfer students get it?',
  'Yes: international transfer students entering in the fall semester may receive $10,000 per year for up to three years. Spring entrants are considered only on a funds-available basis.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 across four corroborating sources: opportunities247.org (deadline 1 Nov 2026 Early Action I; freshmen $5,000–$20,000/yr up to 4 years; automatic consideration; $55 fee; test-optional; 30 credits/year renewal), wemakescholars.com (deadline 1 Nov 2026; freshmen up to $20,000, transfers up to $10,000; open to all except US nationals; partial funding), scholarshipsedge.com (fall 2027 figures: freshmen $5,000–$20,000/yr up to 4 yrs, transfers $10,000/yr up to 3 yrs; Early Action I 1 Nov 2026; no separate application), shiksha.com (max $25,000; auto-consideration; yearly). The older $10,000–$25,000 band quoted by some trackers reflects the 2026 cycle; the article uses the current fall-2027 figures and is marketed as Partially Funded, not fully funded. Queue title "2026 (Funded)" was stale — the live cycle is fall 2027 admission. No invented GPA cut-off is stated; the university publishes academic-merit criteria, not a numeric threshold.</p>
''',
 dl_long='Deadline: 1 November 2026 (Early Action I, fall 2027 intake — 10 days from 22 Oct 2026). Regular Decision: 1 January 2027. Spring-entry transfers: funds-available basis only.',
 offlinks=[('Global Excellence Scholarship — overview (wemakescholars)', 'https://www.wemakescholars.com/scholarship/global-excellence-scholarship-at-university-of-minnesota'),
           ('University of Minnesota Global Excellence Scholarship 2027 — guide', 'https://opportunities247.org/university-of-minnesota-global-excellence-scholarship-2027/')],
 related_titles=['dayton-merit', 'ursinus', 'uchicago', 'msu-oos', 'concordia-talent'],
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
        # flag '#' only when used as a placeholder link (href="#"), not in-page anchors (#about) or CSS hex colors
        for mm in re.finditer(r'href=["\']#["\']', t):
            bad.append((slug, 'suspicious placeholder: ' + mm.group(0)))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

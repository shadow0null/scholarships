#!/usr/bin/env python3
"""Batch 60 (cron run 60, 28 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Alexander Rave Foundation Scholarship 2027 - SKIPPED: deadline passed
   30 Jun 2026 (official ifa.de call; results Sep 2026; stays Feb-Dec 2027).
2. Excelsior Scholarship 2027 - SKIPPED: deadline passed 31 Aug 2026
   (official governor.ny.gov announcement for the 2026-27 academic year).
3. Scholarships in Japan 2026 - SKIPPED: listicle.
4. Stanford Knight Hennessy Scholarship 2027 - SKIPPED: deadline passed
   6 Oct 2026, 1:00 PM PT (2027 cohort; next cycle opens ~Jun 2027).
5. UNDP Administration Internship 2026 South Korea - SKIPPED: deadline
   passed 30 Jun 2026 (6-month placement 17 Aug 2026 - 16 Feb 2027).
6. France Embassy Uganda Scholarships 2027 - SKIPPED: deadline passed
   11 Jun 2026 (Embassy of France in Uganda Master's call).
7. IST Austria Scientific Internships 2027 - VERIFIED (year-round, no
   central deadline; min EUR 1,583 gross/month; official ISTA page read
   in full; ISTernship paused 2026/2027).
8. Portugal AQUA Research Scholarship 2026 - SKIPPED: deadline passed
   22 Jun 2026 (S2AQUAcoLAB MultiAlive call).
9. Rhodes Scholarships at Oxford 2027 - SKIPPED: deadline passed (all
   constituencies closed; latest was USA 7 Oct 2026).
10. Georgia Government Scholarships 2027 - SKIPPED: aggregator umbrella
    label, not a single scheme (mixes US state of Georgia awards with the
    country Georgia); no official source or single deadline.
11. Michael Adamson NEBOSH Diploma Scholarship 2026 - SKIPPED: deadline
    passed 12 Jun 2026 (official NEBOSH page; 20 winners announced).
12. University of Verona PhD Scholarships 2027 - SKIPPED: deadline passed
    9 Jun 2026 (XLII cycle, 104 funded positions).
13. Adidas Internships 2026 - VERIFIED as the March 2027 HQ cohort
    (deadline 31 Oct 2026, 11:59 PM CET; EUR 2,470/1,930 gross/month;
    official jobs.adidas-group.com postings).
14. Aarhus University Scholarships 2026 - SKIPPED: deadline passed
    15 Sep 2026 (winter intake; summer 15 Jan 2026).
15. SECAI AI Masters Scholarship 2026 - SKIPPED: deadline passed
    30 Jun 2026 (TU Dresden / Leipzig; DAAD Zuse School).
16. DAAD Helmut Schmidt Scholarship 2026-27 - SKIPPED: deadline passed
    31 Jul 2026 (application period 1 Jun - 31 Jul 2026).
17. University of Reading Scholarships 2027 - SKIPPED: the named 2027
    award (Global Sustainability Leaders) closed 3 Sep 2026 (Tranches 2/3:
    12 Jun / 3 Sep 2026); Reading's other awards are separate schemes.
18. 10 Best Scholarships in Sweden 2026 - SKIPPED: listicle.
19. Konrad Zuse relAI Scholarship 2027 - SKIPPED: deadline passed
    15 Jun 2026 (official zuseschoolrelai.de call).
20. DAAD STEM Scholarship 2027 - SKIPPED: deadline passed (country
    groups 31 Aug / 3 Sep / 24 Sep / 30 Sep / 21 Oct 2026; last group
    closed 21 Oct 2026).
21. NSP National Scholarship Program 2027 Slovakia - VERIFIED
    (deadline 31 Oct 2026, 16:00 CET; EUR 620 / 1,025.50 / 1,370 / 1,470
    per month; official scholarships.sk terms).
22. GCUB International Mobility Scholarship 2027 Brazil - SKIPPED:
    deadline passed 6 Jul 2026, 11:59 PM BRT.
23. Geneva Peace Fellowship 2026 - SKIPPED: deadline passed 7 Jun 2026
    (official Graduate Institute terms of reference).
24. UNDP Communications Internship 2026 Malaysia - SKIPPED: deadline
    passed 13 Jun 2026 (one source says 16 Jun; either way passed).
25. ARICE Scholarship Program 2026 Romania - SKIPPED: deadline passed
    12 Jun 2026, 2:00 PM Romanian time.
26. Scholarships in Japan Without IELTS 2026 - SKIPPED: listicle.
27. UNDP Digital AI and Innovation Internship 2026 - SKIPPED: deadline
    passed 30 Sep 2026 (one source says 1 Oct 2026; either way passed).
28. University of Miami Bachelors Scholarship 2026 - VERIFIED as the
    Stamps Scholarship (deadline 1 Nov 2026; full cost of attendance +
    $12,000 enrichment fund; official admissions.miami.edu page).
29. Kyoto University ADB Scholarship 2026 - SKIPPED: deadline passed
    June 2026 (April 2027 intake); the November 2026 window for the
    October 2027 intake has no published exact date.
30. United Nations Internship Program 2026 - SKIPPED: rolling family of
    vacancies, no single scheme or deadline.
31. World Food Program Internship 2026 - SKIPPED: rolling family of
    vacancies, no single scheme or deadline.
32. Highest Paid Canadian Scholarships 2026 - SKIPPED: listicle.
33. Morgan Stanley Internships 2026 - SKIPPED: rolling family of
    vacancies, no single scheme or deadline.
34. University of Pisa Scholarship 2027 - VERIFIED as the DSU Toscana
    Scholarship (Bachelor's/Master's closed 7 Sep 2026; PhD and
    specialisation window open 25 Sep - 16 Nov 2026).

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 28)
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
 'ista-internships-2027': {'mono': 'IS', 'title': 'ISTA Scientific Internships in Austria (Paid, Year-Round)',
   'href': 'ista-scientific-internships-year-round-austria.html',
   'dpill': 'No central deadline · Year-round',
   'award': 'Paid employment contract with a minimum salary of €1,583 gross a month, for 2–12 months at ISTA in Klosterneuburg, Austria. No application fee at any stage.',
   'elig': 'Bachelor’s or Master’s students or recent graduates in the natural sciences, computer sciences, mathematics or a related discipline; available for at least 2 months; good command of English.',
   'tags': [('Internship', 'blue'), ('Austria', 'teal')]},
 'adidas-internships-2027': {'mono': 'ad', 'title': 'adidas Internships 2026–27 in Germany (Paid, Herzogenaurach)',
   'href': 'adidas-internships-2027-herzogenaurach-germany.html',
   'dpill': 'Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': '€2,470 gross a month for a non-compulsory internship (€1,930 for a compulsory one; net is the same), 6 months full-time from 1 March 2027 at adidas HQ in Herzogenaurach, plus employee discounts, training and mentorship.',
   'elig': 'Enrolled full-time students for the whole internship (or in a gap year between Bachelor’s and Master’s, EU citizens only); penultimate year preferred; available March–August/September 2027; able to relocate to Herzogenaurach.',
   'tags': [('Internship', 'blue'), ('Germany', 'teal')]},
 'nsp-slovakia-2027': {'mono': 'NS', 'title': 'NSP National Scholarship Programme 2027 in Slovakia (Fully Funded)',
   'href': 'nsp-national-scholarship-programme-slovakia-2027.html',
   'dpill': 'Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': 'Monthly living allowance: €620 for Master’s students, €1,025.50 for PhD students, and €1,025.50–€1,470 for university teachers, researchers and artists. A distance-based travel grant is also available for students and PhD students.',
   'elig': 'International students, PhD students, university teachers, researchers and artists enrolled at a university outside Slovakia, with an acceptance or invitation letter from a Slovak host institution.',
   'tags': [('Master’s & PhD', 'blue'), ('Slovakia', 'teal')]},
 'miami-stamps-2027': {'mono': 'UM', 'title': 'University of Miami Stamps Scholarship 2027 in USA (Fully Funded)',
   'href': 'university-of-miami-stamps-scholarship-2027-usa.html',
   'dpill': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
   'award': 'Full cost of attendance for up to eight semesters (ten for Architecture): tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks, a laptop allowance, and a $12,000 enrichment fund.',
   'elig': 'Exceptional high-school seniors applying as first-year undergraduates from any country; apply under Early Decision I or Early Action by 1 November. No separate scholarship application.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'pisa-dsu-2027': {'mono': 'UP', 'title': 'University of Pisa Scholarship 2027 in Italy (DSU Toscana, Fully Funded)',
   'href': 'university-of-pisa-dsu-scholarship-2027-italy.html',
   'dpill': 'Deadline 16 Nov 2026 · %d days left' % dl_left('2026-11-16'),
   'award': 'DSU Toscana Scholarship: a monetary allowance (varies by economic status and student classification), free meals, free accommodation for eligible off-site winners, accommodation support, exemption from the regional study tax and full tuition exemption.',
   'elig': 'Students enrolled or intending to enrol at the University of Pisa (Bachelor’s, Master’s, PhD or specialisation); economic and merit criteria per the annual DSU call. PhD and specialisation applications are open now.',
   'tags': [('Bachelor’s to PhD', 'blue'), ('Italy', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. ISTA Scientific Internships (year-round)
A.append(dict(
 slug='ista-scientific-internships-year-round-austria',
 title='ISTA Scientific Internships in Austria (Paid, Year-Round)',
 meta='ISTA Scientific Internships: paid year-round research internships at the Institute of Science and Technology Austria. Minimum salary €1,583 gross a month for 2–12 months, no central deadline — apply at least 4 months before your intended start date.',
 short='ISTA Scientific Internships (Year-Round)', kicker='Austria · Internship · Paid', mono='IS',
 prov_short='Institute of Science and Technology Austria (ISTA)', prov_cat='Institute · Austria',
 h1='ISTA Scientific Internships in Austria (Paid, Year-Round)',
 sub='Read this first, because there are two different ISTA internships and only one of them is open right now. The ISTernship Summer Fellowship — the competitive, centrally-run summer programme — has been paused for the 2026 and 2027 application cycles and is not taking place. The year-round Scientific Internships are a different route and are still available: you contact a research group directly, agree dates with them, and join for 2 to 12 months on a paid employment contract, with a minimum salary of €1,583 gross a month. There is no central deadline — applications are accepted on a continuous basis — but you should apply at least 4 months before your intended start date, because the formal portal registration must be completed at least 2 months ahead.',
 dpill='No central deadline · Year-round',
 facts=facts([('Award', 'A paid employment contract with ISTA and a minimum salary of €1,583 gross a month. ISTA charges no processing or application fee for any of its programmes at any stage. Interns may be eligible for ISTA campus apartments in Klosterneuburg, subject to availability and for a cost; Vienna is a 25-minute bus ride away. Visa assistance is provided once an offer is made, for interns from outside the EU/EEA and Switzerland.'),
              ('Eligible', 'Students who are pursuing or have obtained a Bachelor’s or a Master’s degree in the natural sciences, computer sciences, mathematics or a related discipline. You must be available for at least 2 months, have an interest in the work of at least one ISTA research group, and have a good command of English (ISTA’s working language). PhD students at other institutions can also visit ISTA research groups for 2–12 months through the same route, and may be eligible for a higher salary range. Eligibility is also assessed under ISTA’s Research Security policy, considering current and recent affiliations, research area and project description.'),
              ('How', '1) Browse ISTA’s research groups and staff scientists and pick the group whose work matches your background. 2) Email the group leader or staff scientist directly with a short introduction to your background and motivation, a CV in PDF format, and possible internship dates — the start date must be at least 2 months ahead. 3) If the group is interested, they or their assistant will contact you for further steps through ISTA’s application portal. 4) Complete the portal registration at least 2 months before your start date; ISTA recommends applying at least 4 months ahead. Only selected candidates receive a reply, because of the volume of applications.'),
              ('Deadline', 'No central deadline — applications are accepted on a continuous basis. Plan ahead: portal registration must be completed at least 2 months before your start date, and ISTA recommends applying at least 4 months ahead. The ISTernship Summer Fellowship is paused for the 2026 and 2027 cycles and has no call.'),
              ('Fine print', 'You cannot be employed as a scientific intern at ISTA if you are employed or funded elsewhere. If you hold an external scholarship (for example Erasmus+), you may join a group as a visiting student for 2–6 months instead — visiting students are not employees and do not receive a salary. Not all research groups can accept an intern. Completing an internship does not improve or guarantee your chances of admission to the ISTA PhD programme; PhD applications are evaluated independently.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>Institute of Science and Technology Austria (ISTA)</strong>, in Klosterneuburg near Vienna, offers <strong>Scientific Internships</strong> throughout the year to students and recent graduates in the <strong>natural sciences, computer sciences, mathematics and related disciplines</strong>. An intern is appointed for <strong>2 months to 1 year</strong>, works inside one of ISTA’s 90+ research groups under a professor or staff scientist, and is paid under an <strong>employment contract</strong> — a minimum salary of <strong>€1,583 gross a month</strong>. There is <strong>no application fee</strong> at any stage.</p>
      <p>The route matters more than the paperwork. There is <strong>no central annual application form</strong> and no fixed deadline: you identify a research group, <strong>contact its leader or a staff scientist directly</strong>, and agree the dates with them. Candidates are selected by the head of the research group or the staff scientists, subject to funding for the salary and formal approval by ISTA’s Academic Affairs division. Because the volume of applications is high, ISTA replies <strong>only to selected candidates</strong> — so the email itself, and how closely your background matches the group’s work, is the application.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A student or recent graduate of a <strong>Bachelor’s or Master’s degree</strong> in the <strong>natural sciences, computer sciences, mathematics</strong>, or a related discipline.</li>
        <li>Available for <strong>at least 2 months</strong> to conduct the internship at ISTA.</li>
        <li>An interest in topics related to the work of <strong>at least one ISTA research group</strong>, and willing to share it with the group leader and team members.</li>
        <li>A <strong>good command of English</strong> (ISTA’s working language).</li>
        <li><strong>PhD students at other institutions</strong> can also visit ISTA research groups for <strong>2–12 months</strong> through the same route, and may be eligible for a <strong>higher salary range</strong> than the intern rate.</li>
        <li>Eligibility is assessed under ISTA’s <strong>Research Security policy</strong> — current and recent affiliations, research area and project description are considered, and ISTA does not host short-term stays of people affiliated with EU-sanctioned institutions.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Minimum salary of €1,583 gross a month</strong> under an ISTA employment contract.</li>
        <li><strong>2–12 months</strong> of hands-on research in a real ISTA research group, with access to shared facilities including advanced microscopy, high-performance computing clusters and cleanrooms.</li>
        <li><strong>No application or processing fee</strong> at any stage.</li>
        <li><strong>Visa assistance</strong> once an offer is made, for interns from outside the EU/EEA and Switzerland.</li>
        <li>Possible <strong>campus accommodation</strong> in ISTA apartments in Klosterneuburg, subject to availability and for a cost; Vienna is about a 25-minute bus ride away.</li>
        <li>Freedom to <strong>engage with more than one group</strong> — each intern has a primary host group, but interdisciplinary collaboration is welcomed.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>CV in PDF format</strong>, listing relevant experience and education history.</li>
        <li>A <strong>short introduction</strong> to your background and your <strong>motivation</strong> to work with the group, in the email itself.</li>
        <li><strong>Possible dates</strong> for the internship — the start date must be at least <strong>2 months ahead</strong>.</li>
        <li>Note: <strong>academic transcripts and recommendation letters are not listed by ISTA as universal mandatory documents</strong> for the initial direct-contact email. A host group may request additional material later, and the formal portal step follows only if the group is interested.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Browse ISTA’s <strong>research groups and staff scientists</strong> and identify the group whose work matches your academic background and research interests.</li>
        <li><strong>Email the group leader or staff scientist directly</strong>, including a short introduction to your background, your motivation to work with them, a CV in PDF format, and possible internship dates (start date at least 2 months ahead).</li>
        <li>You may <strong>contact more than one group leader at the same time</strong> — ISTA says this is quite common — but select laboratories that closely match your interests and explain your preferences.</li>
        <li>If the group is interested in hosting you, they or their assistant will contact you for further steps, requesting further information through ISTA’s <strong>application portal</strong>.</li>
        <li>Complete the <strong>portal registration at least 2 months before your intended start date</strong>; ISTA recommends applying <strong>at least 4 months ahead</strong>.</li>
        <li>For administrative questions about year-round Scientific Internships, the contact published by ISTA is <strong>predoc@ista.ac.at</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a deadline for the ISTA Scientific Internships?',
  'No. Applications are accepted on a continuous basis, so there is no central deadline. Plan ahead: the portal registration must be completed at least 2 months before your start date, and ISTA recommends applying at least 4 months ahead of your desired start date.'),
 ('How much do ISTA Scientific Interns get paid?',
  'Scientific interns receive an employment contract with ISTA and a minimum salary of €1,583 gross a month. You cannot be employed as a scientific intern at ISTA if you are employed or funded elsewhere.'),
 ('What is the difference between the ISTA Scientific Internship and the ISTernship Fellowship?',
  'The ISTernship Summer Fellowship is a centrally-run summer programme (May–September, 2–3 months) with its own application call — and it has been paused for the 2026 and 2027 application cycles. The year-round Scientific Internship is a separate route: you contact a research group directly and agree dates with them, for 2–12 months at any time of year. It is not affected by the ISTernship pause.'),
 ('Do I need to contact a professor to apply?',
  'Yes, for the year-round Scientific Internship. Identify a suitable research group and contact the group leader or staff scientist directly. Do not contact professors for the ISTernship Fellowship — that programme uses a centralised call (and is currently paused).'),
 ('Who can apply for the ISTA Scientific Internship?',
  'Students pursuing or having obtained a Bachelor’s or a Master’s degree in the natural sciences, computer sciences, mathematics or a related discipline, available for at least 2 months, with a good command of English. PhD students at other institutions can also visit ISTA groups for 2–12 months through the same route.'),
 ('What documents do I need for the initial application?',
  'A short introduction to your background and motivation, a CV in PDF format, and possible internship dates, sent by email to the group leader or staff scientist. Transcripts and recommendation letters are not listed by ISTA as mandatory for the initial email; the host group may ask for more later.'),
 ('Does an ISTA internship help me get into the ISTA PhD programme?',
  'No. ISTA states that participation in the Scientific Internship Program does not improve or guarantee your chances of admission to the ISTA PhD Program; PhD applications are evaluated independently.'),
 ('Is accommodation available at ISTA during the internship?',
  'ISTA owns and operates apartments on its campus in Klosterneuburg, and interns may be eligible to stay in them, subject to availability and for a cost. Short- and long-term options are available; Vienna is about a 25-minute bus ride away.'),
 ('Can I use an external scholarship, like Erasmus+, for an ISTA internship?',
  'Yes, in a different form: with external funding you may join a research group as a visiting student for 2–6 months. Visiting students are not employees and do not receive a salary from ISTA.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against ISTA's official Scientific Internships page (phd.ista.ac.at/scientific-internships/, read in full, crawled 28 Oct 2026) and corroborated by the Harvard FAS careers listing and two independent guides: year-round Scientific Internships for students pursuing or having obtained a Bachelor's or Master's degree in the natural or computer sciences, mathematics or a related discipline; appointment 2 months to 1 year; candidates selected by the head of a research group or staff scientists, subject to funds and Academic Affairs approval; applications accepted on a continuous basis, no central deadline; contact the group leader or staff scientist directly; start date must be at least 2 months ahead; portal registration at least 2 months before the start date, apply at least 4 months ahead recommended; minimum salary EUR 1,583 gross/month under an ISTA employment contract; no processing or application fees; ISTA replies only to selected candidates; administrative contact predoc@ista.ac.at; PhD students at other institutions may visit for 2-12 months (possibly a higher salary range); Research Security policy screening applies; campus apartments subject to availability and cost; Vienna about 25 minutes by bus; visa assistance after an offer for non-EU/EEA/Swiss nationals. CONFLICTS: (1) The widely repeated EUR 1,184/month stipend on aggregator pages (e.g. ehsaskafaalat) is OUTDATED — the official ISTA page now states a minimum salary of EUR 1,583 gross/month, and the 2026 guides corroborate EUR 1,583. (2) Several aggregators present the ISTernship Summer Fellowship as the live programme; the official ISTA page states the ISTernship programme has been paused for the 2026 and 2027 application cycles and will not take place — only the year-round Scientific Internships continue. The article leads with that distinction. Documents: transcripts and recommendation letters are NOT listed by ISTA as mandatory for the initial direct-contact email, so they are not presented as requirements. The official page does not publish an intern headcount or a housing price, so neither is stated.</p>''',
 dl_long='No central deadline — apply at least 4 months before your intended start date (portal registration at least 2 months before)',
 offlinks=[('ISTA — Scientific Internships, Year-Round (official)', 'https://phd.ista.ac.at/scientific-internships/'),
           ('Harvard FAS — ISTA Scientific Internships (Year-Round)', 'https://careerservices.fas.harvard.edu/jobs/institute-of-science-and-technology-austria-ist-austria-scientific-internships-year-round/'),
           ('Bright Scholarship — IST Austria Scientific Internships 2027', 'https://brightscholarship.com/ist-austria-scientific-internships-2027-paid/')],
 related_titles=['epfl-cyd-2027', 'tsukuba-mext-2027', 'jsps-2027', 'gottingen-daad-2027'])),

# ---------------------------------------------------------------- 2. adidas Internships (Herzogenaurach, March 2027 cohort)
A.append(dict(
 slug='adidas-internships-2027-herzogenaurach-germany',
 title='adidas Internships 2026–27 in Germany (Paid, Herzogenaurach)',
 meta='adidas Internships 2026–27: paid 6-month internships at adidas HQ in Herzogenaurach, Germany, starting 1 March 2027. Monthly allowance €2,470 gross (non-compulsory) or €1,930 (compulsory). Deadline 31 October 2026, 11:59 PM CET.',
 short='adidas Internships 2026–27', kicker='Germany · Internship · Paid', mono='ad',
 prov_short='adidas', prov_cat='Company · Germany',
 h1='adidas Internships 2026–27 in Germany (Paid, Herzogenaurach)',
 sub='Read this first, because "adidas internships" is not one internship with one deadline — it is a family of roles, and the one that matters right now is the March 2027 cohort at adidas headquarters in Herzogenaurach, Germany. Roles across Footwear Development, Workplace Management, Creative Direction, Sales, and Finance, Controlling & Audit all share the same terms: 6 months full-time from 1 March 2027, a monthly gross allowance of €2,470 for a non-compulsory internship (€1,930 for a compulsory one, with the same net), and a hard application deadline of 31 October 2026 at 11:59 PM CET. You apply per role, with a CV — no motivation letter is required — and if it is a match you are invited to a video interview.',
 dpill='Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'Monthly gross allowance of €2,470 for a non-compulsory internship, or €1,930 for a compulsory internship — adidas states the difference is due to taxation and the net amount is the same. 6 months full-time, starting 1 March 2027, at adidas headquarters in Herzogenaurach (near Nuremberg), Germany. Also included: employee discounts, structured training and development, LinkedIn Learning, language training and the adidas Learning Portal, a mentorship programme, networking and employee resource groups, an international intern community, regular development conversations, on-campus events and sponsored adidas events/games, a campus with canteens, cafes, reflection rooms and sports facilities including an on-site gym (€25/month), a company sports programme, and flexible working (40% home office possible).'),
              ('Eligible', 'Enrolled as a full-time student for the complete duration of the internship, or in the so-called gap year between a Bachelor’s and a Master’s degree — the gap-year route applies only to EU citizens, due to working-permit regulations. Candidates in their penultimate year of study are preferred (after the internship, students should have a maximum of one year left to graduate). Available for the full duration of the internship from March 2027 to August/September 2027, and able to relocate to Herzogenaurach in Germany for the full duration.'),
              ('How', 'Apply online for the specific role through adidas’s careers site (jobs.adidas-group.com) or a job board carrying the posting. Submit your CV — you do not have to write a motivation letter, but you may add one if you have something to say. Apply in English, or in the same language as the job description. If adidas feels it is a match, you are invited to a video interview and will be fully briefed. Each role is a separate application; there is no single central application form.'),
              ('Deadline', '31 October 2026, 11:59 PM CET, for the March 2027 cohort at Herzogenaurach HQ. Start date 1 March 2027; duration 6 months (March–August 2027 for most roles, March–September 2027 for some).'),
              ('Fine print', 'The queue title "Adidas Internships 2026" is the listing year — the live cohort starts in March 2027. The roles are at adidas headquarters in Herzogenaurach, not at regional offices; other adidas internships elsewhere run on their own timelines. The "12 weeks for MBA students" and "one-year Summer program" claims on aggregator pages do not match the HQ postings checked, which state 6 months. A stipend figure is not published per role beyond the €2,470/€1,930 monthly allowance.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p><strong>adidas</strong> is hiring interns for its <strong>March 2027 cohort</strong> at its headquarters in <strong>Herzogenaurach, near Nuremberg, Germany</strong>. The roles span <strong>Footwear Development, Workplace Management, Creative Direction – Brand Identity, Sales, and Finance, Controlling &amp; Audit</strong>, and they share the same terms: <strong>6 months full-time from 1 March 2027</strong>, a monthly gross allowance of <strong>€2,470 for a non-compulsory internship</strong> or <strong>€1,930 for a compulsory one</strong> (adidas states the difference is due to taxation and the net amount is the same), and an application deadline of <strong>31 October 2026, 11:59 PM CET</strong>.</p>
      <p>What the posting actually asks for is refreshingly light: a <strong>CV</strong>. You do not have to write a motivation letter, though you may add one if you have something to say. If adidas feels it is a match, you are invited to a <strong>video interview</strong> and will be fully briefed. The internship is built around the campus experience — an <strong>international intern community</strong>, structured training, <strong>LinkedIn Learning and language training</strong>, a <strong>mentorship programme</strong>, networking and employee resource groups, and on-campus events and sponsored adidas events and games — plus practical perks like <strong>employee discounts</strong>, a campus gym for <strong>€25 a month</strong>, and <strong>40% home office</strong> possible.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled as a <strong>full-time student for the complete duration</strong> of the internship.</li>
        <li>Or in the so-called <strong>gap year between a Bachelor’s and a Master’s degree</strong> — the gap-year route applies only to <strong>EU citizens</strong>, due to working-permit regulations.</li>
        <li>Candidates in their <strong>penultimate year of study are preferred</strong> — after the internship, students should have a maximum of <strong>one year left to graduate</strong>.</li>
        <li>Available for the <strong>full duration</strong> of the internship from <strong>March 2027 to August 2027</strong> (some roles run to September 2027).</li>
        <li>Able to <strong>relocate to Herzogenaurach in Germany</strong> for the full duration of the internship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly gross allowance: €2,470</strong> for a non-compulsory internship, <strong>€1,930</strong> for a compulsory internship (net the same).</li>
        <li><strong>6 months full-time</strong> from <strong>1 March 2027</strong> at adidas headquarters in Herzogenaurach.</li>
        <li><strong>Employee discounts</strong> on products.</li>
        <li>Structured training and development, <strong>LinkedIn Learning, language training</strong> and the adidas Learning Portal.</li>
        <li><strong>Mentorship programme</strong>, networking opportunities and employee resource groups.</li>
        <li><strong>International intern community</strong> and work environment; chances to attend on-campus events and sponsored adidas events/games.</li>
        <li>Inspiring campus with canteens, cafes, reflection rooms and sports facilities including an <strong>on-site gym (€25/month)</strong> and a company sports programme.</li>
        <li><strong>Flexible working arrangements</strong> — 40% home office possible.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>CV</strong> — the only document the postings require.</li>
        <li>A <strong>motivation letter is optional</strong> — the postings say you do not have to write one, but you may add one if you have something to say.</li>
        <li>Apply in <strong>English</strong>, or in the same language as the job description for that role.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Find the role that fits you on <strong>adidas’s careers site (jobs.adidas-group.com)</strong> or a job board carrying the posting — Footwear Development, Workplace Management, Creative Direction, Sales, Finance, Controlling &amp; Audit, and others.</li>
        <li>Check that role’s own <strong>eligibility and dates</strong> — all HQ March 2027 roles checked share the 31 October 2026 deadline and the 1 March 2027 start, but durations differ slightly (March–August vs March–September 2027).</li>
        <li>Submit your <strong>CV</strong> through the role’s application page, in English or the language of the job description.</li>
        <li>Optionally add a <strong>motivation letter</strong> if you have something to say.</li>
        <li>If adidas feels it is a match, you will be invited to a <strong>video interview</strong> — adidas says it will fully brief you.</li>
        <li>Submit before <strong>31 October 2026, 11:59 PM CET</strong> — each role is a separate application.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the adidas internships 2026–27?',
  '31 October 2026 at 11:59 PM CET, for the March 2027 cohort at adidas headquarters in Herzogenaurach. The internships start on 1 March 2027 and last 6 months.'),
 ('How much do adidas interns get paid?',
  'The monthly gross allowance is €2,470 for a non-compulsory internship and €1,930 for a compulsory internship. adidas states the difference is due to taxation and the net amount is the same.'),
 ('Where are the adidas internships located?',
  'At adidas headquarters in Herzogenaurach, near Nuremberg, Germany. You must be able to relocate there for the full duration. Other adidas internships at regional offices run on their own timelines and are not covered by this deadline.'),
 ('Who can apply for an adidas internship?',
  'Students enrolled full-time for the whole internship, or in a gap year between a Bachelor’s and a Master’s degree (EU citizens only, due to working-permit regulations). Penultimate-year students are preferred — you should have at most one year left to graduate after the internship.'),
 ('Do I need a motivation letter for the adidas internship?',
  'No. The postings say you do not have to write a motivation letter, but you may add one if you have something to say. A CV is the required document.'),
 ('How long is the adidas internship?',
  '6 months full-time, from 1 March 2027 — March to August 2027 for most roles, March to September 2027 for some.'),
 ('Is there a single application for all adidas internships?',
  'No. Each role is a separate application on adidas’s careers site. The roles checked here — Footwear Development, Workplace Management, Creative Direction, Sales, Finance, Controlling & Audit — all share the same 31 October 2026 deadline and 1 March 2027 start.'),
 ('Is the adidas internship really open to international students?',
  'The postings do not restrict nationality, but you must be enrolled as a full-time student (or in an EU-citizen gap year) and able to relocate to Herzogenaurach. Working-permit rules apply — the gap-year route is explicitly limited to EU citizens.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against adidas's own job postings (jobs.adidas-group.com Workplace Management posting and Business of Fashion listings for Footwear Development, Creative Direction – Brand Identity, Sales, and Finance, Controlling & Audit — all crawled 28 Oct 2026): March 2027 cohort at adidas HQ, Herzogenaurach; application deadline 31 October 2026, 11:59 PM CET; start 1 March 2027; duration 6 months full-time (March–August 2027, some roles March–September 2027); monthly gross allowance EUR 2,470 non-compulsory / EUR 1,930 compulsory, difference due to taxation, net the same; enrolled full-time for the complete duration or gap year between Bachelor's and Master's (EU citizens only, due to working-permit regulations); penultimate year preferred (max one year to graduation after the internship); relocate to Herzogenaurach for the full duration; CV only, motivation letter optional, apply in English or the language of the job description; video interview if matched; perks as listed (employee discounts, LinkedIn Learning, language training, adidas Learning Portal, mentorship, networking, employee resource groups, international intern community, on-campus events, gym EUR 25/month, 40% home office). CONFLICTS: (1) Aggregators (e.g. Scholarship Union) claim "no specific deadline, applications accepted year-round" — WRONG for this HQ cohort, which has a hard 31 October 2026 deadline on adidas's own postings. (2) The same aggregators claim "12 weeks for MBA students" and a "one-year Summer program" — not in the HQ postings checked, which state 6 months. (3) A "1,382 vacant positions across 353 locations in 52 countries" figure describes adidas hiring generally, not this cohort, and is not used. The queue title "Adidas Internships 2026" is the listing year; the live cohort starts March 2027. No per-role headcount is published, so none is stated.</p>''',
 dl_long='31 October 2026, 11:59 PM CET (March 2027 cohort, Herzogenaurach HQ)',
 offlinks=[('adidas Careers — Internship, Workplace Management (official)', 'https://jobs.adidas-group.com/job/Herzogenaurach-INTERNSHIP-WORKPLACE-MANAGEMENT-%28MFD%29-BY/1442839233/'),
           ('Business of Fashion — adidas Internship, Footwear Development', 'https://www.businessoffashion.com/careers/job/323582/adidas-internship-footwear-development-m-f-d-/?LinkSource=HomePage'),
           ('Bright Scholarship — Adidas Internships 2026', 'https://brightscholarship.com/adidas-internships-2026-paid-internships/')],
 related_titles=['wto-internship-2027', 'gottingen-daad-2027', 'epfl-cyd-2027', 'duke-karsh-2026'])),

# ---------------------------------------------------------------- 3. NSP National Scholarship Programme, Slovakia
A.append(dict(
 slug='nsp-national-scholarship-programme-slovakia-2027',
 title='NSP National Scholarship Programme 2027 in Slovakia (Fully Funded)',
 meta='NSP National Scholarship Programme 2027 in Slovakia: monthly living allowance €620 for Master’s students and €1,025.50 for PhD students, plus a travel grant. Deadline 31 October 2026, 16:00 CET, for stays in the summer semester 2026/27.',
 short='NSP National Scholarship Programme 2027', kicker='Slovakia · Master’s & PhD · Funded', mono='NS',
 prov_short='SAIA', prov_cat='Government · Slovakia',
 h1='NSP National Scholarship Programme 2027 in Slovakia (Fully Funded)',
 sub='Read this first, because the NSP is not a scholarship for a full degree in Slovakia — it is a mobility programme. It pays international students, PhD students, university teachers, researchers and artists to spend a study, research, teaching or artistic stay at a Slovak university or research institution, while they stay enrolled at their home university abroad. The current call closes on 31 October 2026 at 16:00 CET and covers stays in the summer semester of 2026/27. The monthly allowance is €620 for Master’s students and €1,025.50 for PhD students, with higher rates for experienced academics and artists — and you cannot apply without an acceptance or invitation letter from a Slovak host institution first.',
 dpill='Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'Monthly living allowance: €620 for university students (second level, i.e. Master’s); €1,025.50 for PhD students; €1,025.50 for university teachers, researchers and artists without a PhD and with less than 4 years of relevant experience; €1,370 with a PhD and less than 10 years of experience; €1,470 with a PhD and more than 10 years of experience. Students and PhD students can also request a travel grant — a lump sum based on the straight-line distance between home and the Slovak host institution, paid at the end of the stay with the final scholarship payment. The allowance is meant to cover living costs in Slovakia (food, accommodation and other ordinary expenses). It is not a tuition payment for a full degree.'),
              ('Eligible', 'International applicants from all countries except Slovakia, subject to the programme conditions. Categories: university students at the second level of higher education (Master’s); PhD students; university teachers, researchers and artists. You must be enrolled at a university outside Slovakia and hold an acceptance or invitation letter from a Slovak host institution. Applicants who have already received an NSP scholarship generally need at least two years to have passed between the relevant application deadlines.'),
              ('How', '1) Find a suitable host institution in Slovakia and secure an acceptance or invitation letter. 2) Register and complete the online application at scholarships.sk — the system opens at least 6 weeks before the deadline. 3) Attach all required documents in Slovak or English and submit before 31 October 2026, 16:00 CET. 4) Deliver the original signed acceptance/invitation letter to SAIA in Bratislava (SAIA, n. o., Sasinkova 10, 812 20 Bratislava) by 12:00 noon on the third Slovak working day after the deadline. Only one application per applicant per call.'),
              ('Deadline', '31 October 2026 at 16:00 CET, for stays during the summer semester of the academic year 2026/2027. The next call is 30 April 2027 at 16:00 CET, for stays during the academic year 2027/2028. The original acceptance/invitation letter must reach SAIA by 12:00 noon on the third working day after the deadline.'),
              ('Fine print', 'Stay windows for this call: university students start between 1 February and 1 April 2027 and finish by 31 August 2027; PhD students, university teachers, researchers and artists start between 1 February and 31 August 2027 and finish by 30 November 2027. Student stays last 1–2 full semesters (4–5 or 9–10 months) or 1–3 full trimesters (3–4, 6–7 or 9–10 months); PhD and academic stays last 1–10 months. The programme is administered by SAIA, the Slovak Academic Information Agency, for the Ministry of Education, Research, Development and Youth of the Slovak Republic. Applicants needing a visa or temporary residence permit should allow extra time.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>National Scholarship Programme of the Slovak Republic (NSP)</strong> is a government-funded mobility programme, administered by <strong>SAIA, the Slovak Academic Information Agency</strong>, for the Ministry of Education, Research, Development and Youth of the Slovak Republic. It supports <strong>international university students, PhD students, university teachers, researchers and artists</strong> who want to spend a study, research, teaching or artistic stay at a university or research organisation in Slovakia — while remaining enrolled at, or affiliated with, an institution outside Slovakia. It does <strong>not</strong> pay for a complete degree in Slovakia.</p>
      <p>The money is a <strong>monthly living allowance</strong>, not a lump-sum prize: <strong>€620 a month</strong> for Master’s-level university students, <strong>€1,025.50</strong> for PhD students, and <strong>€1,025.50 to €1,470</strong> for university teachers, researchers and artists, depending on qualifications and experience. Students and PhD students can also request a <strong>travel grant</strong>, paid as a lump sum at the end of the stay. There are <strong>two application deadlines a year</strong> — 30 April for the following academic year and 31 October for the summer semester of the current academic year — and the call open now closes on <strong>31 October 2026 at 16:00 CET</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>international applicant from any country except Slovakia</strong>, subject to the programme’s eligibility rules — including the eligibility wizard and the yearly offer that shows how many places your country has and which fields it supports.</li>
        <li>One of the following categories: <strong>university student at the second level of higher education</strong> (Master’s); <strong>PhD student</strong>; <strong>university teacher, researcher or artist</strong>.</li>
        <li><strong>Enrolled at a university outside Slovakia</strong> (or, for teachers/researchers/artists, affiliated with an institution outside Slovakia).</li>
        <li>Holding an <strong>acceptance or invitation letter</strong> from a Slovak host institution — this document is needed before you can submit the scholarship application, and the <strong>original</strong> must reach SAIA by the deadline for physical delivery.</li>
        <li>Applicants who have already received an NSP scholarship generally need at least <strong>two years</strong> to have passed between the relevant application deadlines.</li>
        <li>For university teachers, researchers and artists, <strong>professional experience is calculated up to the application deadline</strong>; PhD studies may count as professional experience, subject to the programme’s stated maximum of six years.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly living allowance</strong> — €620 (Master’s students), €1,025.50 (PhD students), €1,025.50 / €1,370 / €1,470 (university teachers, researchers and artists, by qualification and experience).</li>
        <li><strong>Travel grant</strong> for students and PhD students — a lump sum based on the straight-line distance between home and the Slovak host institution, requested with the application and paid at the end of the stay with the final scholarship payment.</li>
        <li>Stays of <strong>1–2 semesters or 1–3 trimesters</strong> for students, and <strong>1–10 months</strong> for PhD students, teachers, researchers and artists.</li>
        <li>Assistance from the host institution with <strong>accommodation and formalities</strong> for entering and staying in Slovakia (or you may handle them independently).</li>
        <li>Access to Slovak universities and research institutions, laboratories and academic networks for the duration of the stay.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Acceptance or invitation letter</strong> from the Slovak host institution — the original signed letter must be delivered to SAIA (the scan goes in the online application).</li>
        <li><strong>CV</strong> and <strong>motivation letter</strong>.</li>
        <li><strong>Detailed study or research programme</strong> for the stay.</li>
        <li><strong>Two letters of recommendation</strong>.</li>
        <li><strong>Academic transcripts and diplomas</strong>, and proof of enrolment at your home university.</li>
        <li><strong>List of publications or artistic activities</strong> (for artists and researchers, as applicable).</li>
        <li>Documents must be attached in <strong>Slovak or English</strong> in the prescribed form; the exact list depends on your applicant category, so check the programme terms for your category before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Run the official <strong>eligibility wizard</strong> first (vladnestipendia.sk/en/wizard) — if your country is not listed, you cannot apply; then check the yearly offer for your country’s places and fields.</li>
        <li>Identify a suitable <strong>host institution in Slovakia</strong>, agree a feasible programme with them, and request the <strong>acceptance or invitation letter</strong> early — the original must reach SAIA within days of the deadline.</li>
        <li>Register on the official application system at <strong>www.scholarships.sk</strong> (opened at least 6 weeks before the deadline) and complete the online form.</li>
        <li>Upload all required attachments in Slovak or English, in the prescribed form.</li>
        <li>Submit the application before <strong>31 October 2026, 16:00 CET</strong> — saving a draft is not enough; click SEND. Only one application per applicant per call.</li>
        <li>Ensure the <strong>original acceptance/invitation letter reaches SAIA</strong> (SAIA, n. o., Sasinkova 10, 812 20 Bratislava, Slovakia) by <strong>12:00 noon on the third Slovak working day</strong> after the deadline. SAIA usually informs applicants within 8 weeks of the deadline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the NSP National Scholarship Programme 2027?',
  '31 October 2026 at 16:00 CET, for stays during the summer semester of the academic year 2026/2027. The original acceptance/invitation letter must reach SAIA by 12:00 noon on the third Slovak working day after the deadline. The next call is 30 April 2027 at 16:00 CET, for stays during the academic year 2027/2028.'),
 ('How much does the NSP Slovakia scholarship pay?',
  '€620 a month for Master’s-level university students, €1,025.50 for PhD students, and €1,025.50, €1,370 or €1,470 for university teachers, researchers and artists, depending on qualifications and experience. Students and PhD students can also request a distance-based travel grant.'),
 ('Is the NSP a scholarship for a full degree in Slovakia?',
  'No. It is a mobility programme: you spend an approved study, research, teaching or artistic stay at a Slovak host institution while remaining enrolled at, or affiliated with, an institution outside Slovakia. It does not pay for a complete degree.'),
 ('Who can apply for the NSP Slovakia scholarship?',
  'International university students (Master’s level), PhD students, university teachers, researchers and artists from all countries except Slovakia, subject to the programme’s eligibility rules. You must be enrolled at a university outside Slovakia and hold an acceptance or invitation letter from a Slovak host institution.'),
 ('Do I need an invitation letter before applying for the NSP?',
  'Yes. You need an acceptance or invitation letter from a Slovak host institution to submit the application, and the original signed letter must reach SAIA in Bratislava by 12:00 noon on the third working day after the deadline.'),
 ('How long can an NSP stay last?',
  'University students: 1–2 full semesters (4–5 or 9–10 months) or 1–3 full trimesters (3–4, 6–7 or 9–10 months). PhD students, university teachers, researchers and artists: 1–10 months. For this call, students start between 1 February and 1 April 2027 and finish by 31 August 2027; other categories start between 1 February and 31 August 2027 and finish by 30 November 2027.'),
 ('What is the NSP travel grant worth?',
  'It is a lump sum based on the straight-line distance between your place of residence (or home institution) and the Slovak host institution, requested with the application and paid at the end of the stay with the final scholarship payment. Guides differ on the maximum — some state up to €1,000, others up to €1,500 — so this article does not state a hard maximum; check the current programme terms on scholarships.sk.'),
 ('Who administers the NSP?',
  'SAIA, the Slovak Academic Information Agency, for the Ministry of Education, Research, Development and Youth of the Slovak Republic. Applications go through the official portal at scholarships.sk.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the official National Scholarship Programme terms (scholarships.sk — programme terms and conditions, including the monthly rates table) and corroborated by swissuniversities.ch, AfterSchoolAfrica, Opportunities for Youth, DAADScholarship and Scholarships365: monthly rates — university student (second level) 620 EUR; PhD student 1025,50 EUR; university teacher/researcher/artist without PhD and less than 4 years' experience 1025,50 EUR; with PhD and less than 10 years' experience 1 370 EUR; with PhD and more than 10 years' experience 1 470 EUR; deadlines 30.04.2026 16:00 CET (academic year 2026/2027) and 31.10.2026 16:00 CET (summer semester 2026/2027); online application at www.scholarships.sk, opened at least 6 weeks before the deadline; original admission/invitation letter to SAIA, n. o., Sasinkova 10, 812 20 Bratislava, by 12:00 on the 3rd working day after the deadline; student stays 1-2 semesters (4-5 or 9-10 months) or 1-3 trimesters (3-4, 6-7, 9-10 months); PhD/teachers/researchers/artists 1-10 months; this call's windows — students start 1 February-1 April 2027, finish by 31 August 2027; PhD/teachers/researchers/artists start 1 February-31 August 2027, finish by 30 November 2027; travel allowance for students and PhD students, lump sum by distance, paid at the end of the stay; SAIA usually informs applicants within 8 weeks; previous recipients generally need a two-year gap between relevant deadlines. CONFLICTS: (1) EngineersJob lists EUR 650/month for Master's students — OUTDATED; the official current rate is EUR 620. (2) The travel-grant maximum differs across guides (EUR 1,000 per StudyHunt vs EUR 1,500 per Scholarships365/AfterSchoolAfrica, with distance bands quoted differently) — the article states the grant exists and is distance-based, and does not state a hard maximum. (3) One guide's "EUR 250 medical confirmation reimbursement" for non-EU/EEA/Swiss nationals staying over 90 days appears in a single source only and is NOT stated in the article. (4) The queue's "Fully Funded" label is softened: the NSP is a living-cost mobility allowance, not full-degree funding. The eligibility wizard and yearly country offer (vladnestipendia.sk) are per the Scholarship Union guide.</p>''',
 dl_long='31 October 2026, 16:00 CET (next call 30 April 2027)',
 offlinks=[('National Scholarship Programme — programme terms (official, scholarships.sk)', 'https://www.scholarships.sk/en/main/programme-terms-and-conditions/archive/2023-2025/international-applicants'),
           ('swissuniversities — NSP Slovakia (official listing)', 'https://www.swissuniversities.ch/en/service/stipendien-ausland/regierungsstipendien/liste/slovakia-national-scholarship-programme-of-the-slovak-republic'),
           ('Bright Scholarship — NSP National Scholarship Program Slovakia 2027', 'https://brightscholarship.com/national-scholarship-program-slovakia-2027/')],
 related_titles=['gottingen-daad-2027', 'ucl-impact-2027', 'york-pise-2027', 'duke-karsh-2026'])),

# ---------------------------------------------------------------- 4. University of Miami Stamps Scholarship
A.append(dict(
 slug='university-of-miami-stamps-scholarship-2027-usa',
 title='University of Miami Stamps Scholarship 2027 in USA (Fully Funded)',
 meta='University of Miami Stamps Scholarship 2027: full cost of attendance for up to eight semesters — tuition and fees, housing, meal plan, health insurance, textbooks, laptop allowance and a $12,000 enrichment fund. Apply under Early Decision I or Early Action by 1 November 2026.',
 short='University of Miami Stamps Scholarship 2027', kicker='USA · Undergraduate · Fully Funded', mono='UM',
 prov_short='University of Miami', prov_cat='University · USA',
 h1='University of Miami Stamps Scholarship 2027 in USA (Fully Funded)',
 sub='Read this first, because the Stamps Scholarship has exactly one way in and one deadline — and the queue title behind this article, "University of Miami Bachelors Scholarship 2026", hides both. The Stamps Scholarship is the University of Miami’s most prestigious merit award: it covers the full cost of attendance for up to eight semesters, including tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks and a laptop allowance, plus a $12,000 enrichment fund. There is no separate scholarship application — but you are only considered if you apply under Early Decision I or Early Action and submit all first-year admission requirements by 1 November 2026. Regular Decision applicants are not considered.',
 dpill='Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
 facts=facts([('Award', 'Full cost of attendance for the completion of one undergraduate degree — up to eight semesters, or ten semesters for students in the School of Architecture. The award includes tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks, a laptop allowance, and access to a $12,000 enrichment fund, which may be used toward study abroad, undergraduate research, unpaid internships, and other educational purposes. The enrichment fund is for approved expenses, not pocket money — expenses need prior approval. Recipients must maintain full-time student status (at least 12 credit hours per semester) and a minimum GPA of 3.0.'),
              ('Eligible', 'Exceptional and academically accomplished high-school seniors applying as first-year undergraduates at the University of Miami, from any country — there are no residency or citizenship restrictions. You must apply under Early Decision I or Early Action and submit all First-Year Admission Requirements by 1 November. The scholarship is awarded on a thorough evaluation of the application and supporting documents; semi-finalists are interviewed via Zoom in January, and finalists are interviewed by the Stamps Family Charitable Foundation. Note: the Frost School of Music has a separate Stamps Ensemble Scholarship for top instrumental performance majors — a different award.'),
              ('How', '1) Complete the Common Application and select the University of Miami. 2) Submit all first-year admission requirements — transcripts, school report, recommendation(s), English-proficiency scores if applicable, and the International Financial Certification Form — under Early Decision I or Early Action by 1 November. 3) If selected as a semi-finalist, interview via Zoom with the Stamps Scholarship Selection Committee in January. 4) Finalists are notified of their status at the time of admission in late January and are interviewed by the Stamps Family Charitable Foundation thereafter. 5) Recipients are announced by early March. There is no separate scholarship application.'),
              ('Deadline', '1 November 2026 — Early Decision I and Early Action. Semi-finalist Zoom interviews in January; finalist notification in late January; Stamps Foundation interviews thereafter; recipients announced by early March. Regular Decision (1 January) applicants are not considered for Stamps.'),
              ('Fine print', 'SAT/ACT scores are optional (UM is test-optional). The $12,000 is an enrichment fund for approved educational purposes, not a cash stipend. Stamps does not combine with other UM admission merit awards. Outside scholarships and need-based aid may layer in, but total aid cannot exceed the cost of attendance. Architecture applicants must submit test scores or a portfolio; music applicants need an audition. A "top 1–2% of school cohort" claim on aggregator pages is not an official UM requirement and is not stated here.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Stamps Scholarship</strong> is the <strong>University of Miami’s most prestigious merit award</strong>, offered in partnership with the <strong>Stamps Family Charitable Foundation</strong> to a select group of incoming first-year students each year. It covers the <strong>full cost of attendance</strong> for the completion of one undergraduate degree — up to <strong>eight semesters</strong>, or <strong>ten semesters</strong> for students in the School of Architecture. That means <strong>tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks and a laptop allowance</strong>, plus access to a <strong>$12,000 enrichment fund</strong> for study abroad, undergraduate research, unpaid internships, conferences, leadership development and other educational purposes.</p>
      <p>Two things decide whether this award is available to you. First, there is <strong>no separate scholarship application</strong> — all applicants are automatically considered for merit scholarships when they apply for admission. Second, and decisively, only the most academically competitive students admitted through <strong>Early Decision I or Early Action (1 November deadline)</strong> are considered for Premier Scholarships, which include Stamps. Apply under Regular Decision and you are <strong>not</strong> considered for Stamps, however strong your application. Selection is holistic: the committee evaluates the rigour of your curriculum, grades, essays, recommendations, extracurricular activities and awards, then interviews semi-finalists by Zoom in January and finalists through the Stamps Foundation, with recipients announced by early March.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>exceptional and academically accomplished high-school senior</strong> applying as a <strong>first-year undergraduate</strong> at the University of Miami.</li>
        <li><strong>Any nationality</strong> — there are no residency or citizenship restrictions.</li>
        <li>Apply under <strong>Early Decision I or Early Action</strong> and submit <strong>all First-Year Admission Requirements by 1 November</strong>.</li>
        <li>Strong academic record: a challenging, well-rounded curriculum, strong grades, and meaningful extracurricular participation.</li>
        <li>Recipients must maintain <strong>full-time student status (at least 12 credit hours per semester)</strong> and a <strong>minimum GPA of 3.0</strong>.</li>
        <li>Note: the <strong>Frost School of Music Stamps Ensemble Scholarship</strong> is a separate award for top instrumental performance majors — different requirements, different process.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and fees</strong> for up to eight semesters (ten for Architecture).</li>
        <li><strong>On-campus housing</strong> and a full <strong>meal plan</strong>.</li>
        <li><strong>University health insurance</strong>, <strong>textbooks</strong> and a <strong>laptop allowance</strong>.</li>
        <li><strong>$12,000 enrichment fund</strong> for study abroad, undergraduate research, unpaid internships, conferences, leadership development and other educational purposes (approved expenses).</li>
        <li>Access to the <strong>Stamps Scholars community</strong> on campus and nationally, including the biannual <strong>Stamps Scholars National Convention</strong>, leadership programmes and networking events.</li>
        <li>Funding to support <strong>academic and scientific research projects</strong> and cultural and leadership programmes during the academic year.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The completed <strong>Common Application</strong> (including the personal statement and any supplemental essay).</li>
        <li><strong>Official high-school transcripts</strong>.</li>
        <li><strong>School Report</strong> completed by your high-school guidance counsellor.</li>
        <li><strong>Letter(s) of recommendation</strong> — one from a counsellor or teacher (some guides list two; UM asks for the counsellor report plus a teacher recommendation — confirm the current requirement on the UM admissions page).</li>
        <li><strong>English-proficiency test scores</strong> (TOEFL or IELTS) for applicants whose native language is not English.</li>
        <li><strong>International Financial Certification Form</strong>; applicants seeking need-based aid also submit the CSS Profile.</li>
        <li><strong>SAT/ACT scores are optional</strong> — UM is test-optional. Architecture applicants must submit test scores or a portfolio; music applicants need an audition.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete the <strong>Common Application</strong> and select the University of Miami as one of your schools (application fee $70 as listed by guides).</li>
        <li>Submit <strong>all First-Year Admission Requirements</strong> — transcripts, school report, recommendation(s), English-proficiency scores if applicable, and the Financial Certification Form — under <strong>Early Decision I or Early Action by 1 November 2026</strong>.</li>
        <li>There is <strong>no separate scholarship application</strong> — you are automatically considered for Stamps when you apply early.</li>
        <li>If selected as a <strong>semi-finalist</strong>, interview via <strong>Zoom with the Stamps Scholarship Selection Committee in January</strong>.</li>
        <li><strong>Finalists</strong> are notified of their status at the time of admission in <strong>late January</strong> and are then interviewed by the <strong>Stamps Family Charitable Foundation</strong>.</li>
        <li>Stamps Scholarship recipients are <strong>announced by early March</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Miami Stamps Scholarship?',
  '1 November 2026 — you must apply under Early Decision I or Early Action and submit all first-year admission requirements by that date. Regular Decision applicants are not considered for Stamps. Semi-finalist interviews are in January, finalists are notified in late January, and recipients are announced by early March.'),
 ('Is there a separate application for the Stamps Scholarship?',
  'No. All applicants are automatically considered for merit scholarships when they apply for admission. For Stamps specifically, the only route is an Early Decision I or Early Action application submitted by 1 November.'),
 ('What does the Stamps Scholarship cover?',
  'The full cost of attendance for up to eight semesters (ten for Architecture): tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks, a laptop allowance, and a $12,000 enrichment fund for study abroad, research, unpaid internships, conferences and leadership development.'),
 ('Is the $12,000 enrichment fund a cash stipend?',
  'No. It is a fund you draw on for approved educational purposes — study abroad, undergraduate research, an unpaid internship, conferences and similar — and expenses need prior approval. It is not pocket money.'),
 ('Can international students apply for the Stamps Scholarship?',
  'Yes. There are no residency or citizenship restrictions; international and domestic high-school seniors are both eligible, provided they apply under Early Decision I or Early Action by 1 November.'),
 ('What grades do I need for the Stamps Scholarship?',
  'UM does not publish a GPA or rank cut-off for Stamps. Selection is holistic — curriculum rigour, grades, essays, recommendations, extracurricular activities and awards — followed by interviews. Aggregator claims that winners "usually rank in the top 1–2% of their school cohort" are not an official UM requirement and are not used here.'),
 ('Do I need SAT or ACT scores for the Stamps Scholarship?',
  'No — the University of Miami is test-optional, and scores are optional for Stamps. Architecture applicants must submit test scores or a portfolio, and music applicants need an audition.'),
 ('What is the difference between the Stamps Scholarship and the Frost School of Music Stamps Ensemble Scholarship?',
  'The Stamps Scholarship is UM’s top merit award for first-year undergraduates in any field. The Frost School of Music offers separate Stamps Ensemble Scholarship Awards to top instrumental performance majors who perform in a Stamps Distinguished Ensemble — a different award with different requirements.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the University of Miami's official First-Year Merit Scholarships page (admissions.miami.edu/undergraduate/financial-aid/scholarships/freshman/index.html): Stamps Scholarship is UM's most prestigious merit award, awarded to exceptional and academically accomplished high school seniors; full cost of attendance for up to eight semesters (ten for School of Architecture); includes tuition and fees, on-campus housing, a meal plan, University health insurance, textbooks, a laptop allowance, and a $12,000 enrichment fund for study abroad, undergraduate research, unpaid internships and other educational purposes; all applicants automatically considered for merit scholarships on admission; most academically competitive students admitted through Early Decision I or Early Action (November 1 deadline) are considered for Premier Scholarships; additional information may be required. Corroborated by five independent guides (AfterSchoolAfrica, ScholarWaka, ScholarshipUnion, OpportunitiesRadar, Scholarships for Africans) on: semi-finalist Zoom interviews in January, finalists notified with admission in late January, interviews by the Stamps Family Charitable Foundation thereafter, recipients announced by early March; maintenance of full-time status (at least 12 credit hours per semester) and minimum 3.0 GPA; Regular Decision applicants not considered. CONFLICTS: (1) Several aggregators call the $12,000 a "stipend" — UM describes it as an enrichment fund for approved purposes; the article corrects this. (2) "Top 1-2% of school cohort" on aggregator pages is not an official UM requirement and is not stated. (3) One aggregator lists a $70 Common Application fee and 250/650-word essay limits — these are aggregator-sourced and are flagged as such in the article (fee) or omitted (word counts). (4) A "November 1 (annually)" date on one guide is the same deadline, not a separate one. The queue's "Bachelors Scholarship 2026" label is corrected to the Stamps Scholarship for fall 2027 entry. The Frost School of Music Stamps Ensemble Scholarship is a different award and is distinguished in the article.</p>''',
 dl_long='1 November 2026 (Early Decision I / Early Action; Regular Decision not considered)',
 offlinks=[('University of Miami — First-Year Merit Scholarships (official)', 'https://admissions.miami.edu/undergraduate/financial-aid/scholarships/freshman/index.html'),
           ('AfterSchoolAfrica — University of Miami Stamps Scholarship 2027', 'https://www.afterschoolafrica.com/95685/university-of-miami-stamps-scholarship/'),
           ('Bright Scholarship — University of Miami Bachelors Scholarship 2026', 'https://brightscholarship.com/university-of-miami-bachelors-scholarship-2026/')],
 related_titles=['duke-karsh-2026', 'york-pise-2027', 'ucl-impact-2027', 'gottingen-daad-2027'])),

# ---------------------------------------------------------------- 5. University of Pisa — DSU Toscana Scholarship
A.append(dict(
 slug='university-of-pisa-dsu-scholarship-2027-italy',
 title='University of Pisa Scholarship 2027 in Italy (DSU Toscana, Fully Funded)',
 meta='University of Pisa Scholarship 2027: the DSU Toscana Scholarship offers a monetary allowance, free meals, free accommodation for eligible off-site winners, and full tuition exemption. PhD and specialisation applications are open until 16 November 2026; Bachelor’s/Master’s closed 7 September 2026.',
 short='University of Pisa Scholarship 2027', kicker='Italy · Bachelor’s to PhD · Fully Funded', mono='UP',
 prov_short='University of Pisa', prov_cat='University · Italy',
 h1='University of Pisa Scholarship 2027 in Italy (DSU Toscana, Fully Funded)',
 sub='Read this first, because the deadline in the queue title — "September 2026" — is only half the story. The main funding route at the University of Pisa is the DSU Toscana Scholarship, a regional need-based award run by Tuscany’s right-to-study authority, not by the university itself. For Bachelor’s, Master’s and single-cycle students the 2026/27 DSU window closed on 7 September 2026. But PhD and specialisation students have a separate application period, from 25 September to 16 November 2026 — and that window is still open. The award can combine a monetary allowance with free meals, free accommodation for eligible off-site winners, accommodation support, exemption from the regional study tax and full exemption from the university’s tuition fee (maximum €2,900 for 2026/27).',
 dpill='Deadline 16 Nov 2026 · %d days left' % dl_left('2026-11-16'),
 facts=facts([('Award', 'The DSU Toscana Scholarship can provide: a monetary scholarship (the amount varies according to economic circumstances and whether the student is classified as on-site, commuter or off-site); free meals through DSU food services; free accommodation for eligible off-site scholarship winners, subject to availability; accommodation-related support for eligible students who do not receive a residence place; exemption from the regional university study tax; and full exemption from the annual all-inclusive tuition fee (maximum €2,900 for regular students in 2026/27) under the University’s rules. Both scholarship winners and eligible non-winners can access free DSU catering services. The DSU grant is not a single fixed-value scholarship — the actual benefits depend on eligibility, economic status, student classification and the annual call.'),
              ('Eligible', 'Students pursuing their first higher-education qualification at participating Tuscan institutions — the universities of Pisa, Florence and Siena, among others — including Bachelor’s, Master’s, doctoral and eligible specialisation programmes. The specific economic and merit criteria are set in the annual DSU call. International students with income or assets outside Italy must provide foreign financial documentation, translated into Italian and legalised as required. Students apply for the DSU scholarship separately from University of Pisa admission and from Universitaly pre-enrolment.'),
              ('How', 'Register on the DSU Toscana Sportello Studente portal and complete the online application. For PhD and specialisation courses, the application period is 25 September to 16 November 2026, closing at 1:00 PM Italian time. Admission to the University of Pisa is a separate process with its own deadlines, and non-EU students requiring a visa must also complete Universitaly pre-enrolment (general 2026/27 deadline 30 September 2026) — the DSU deadline does not cover those steps.'),
              ('Deadline', 'PhD and specialisation courses: 16 November 2026 at 1:00 PM Italian time (applications open 25 September 2026). Bachelor’s, Master’s and single-cycle degree courses: 7 September 2026 at 1:00 PM — CLOSED. Provisional ranking for PhD/specialisation: 15 December 2026; final ranking: 15 January 2027.'),
              ('Fine print', 'DSU Toscana is the regional right-to-study authority (Azienda Regionale per il Diritto allo Studio Universitario della Toscana), separate from the University of Pisa; applications go through its online Sportello Studente portal. The other funding routes named in the queue — Invest Your Talent in Italy (IYT) closed 11 May 2026, and the MAECI scholarships have their own calls — are not this article. The monetary component is not a fixed figure: guides do not publish a single DSU amount for 2026/27, so none is stated here. The Single Substitutive Declaration (DSU/ISEE) for subsidised benefits is part of the documentation; the call summary states it must be signed by 7 September 2026 for the general competition — check the current call for the PhD/specialisation position on this document.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The main funding route for international students at the <strong>University of Pisa</strong> is the <strong>DSU Toscana Scholarship</strong>, a regional need-based award run by <strong>DSU Toscana</strong> — the Azienda Regionale per il Diritto allo Studio Universitario della Toscana, the regional right-to-study authority serving the universities of <strong>Pisa, Florence and Siena</strong> and other Tuscan institutions. The scholarship is based primarily on the student’s <strong>economic situation and academic/merit requirements</strong>, and it can combine a <strong>monetary allowance</strong> with <strong>free meals</strong>, <strong>free accommodation</strong> for eligible off-site winners, accommodation support, exemption from the <strong>regional university study tax</strong> and <strong>full exemption from the university’s tuition fee</strong> (maximum €2,900 all-inclusive for regular students in 2026/27).</p>
      <p>The important thing to understand is that the DSU scholarship is <strong>not a single fixed-value award</strong> that automatically covers every expense. The monetary component varies with economic circumstances and with whether the student is classified as <strong>on-site, commuter or off-site</strong>, and the exact benefits depend on the annual call. It is also a <strong>separate process from admission</strong>: you apply for your University of Pisa degree programme through the university, complete <strong>Universitaly pre-enrolment</strong> if you are a non-EU student requiring a visa, and apply for DSU through the DSU portal — three different steps, with three different deadlines.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Students pursuing their <strong>first higher-education qualification</strong> at a participating Tuscan institution, including <strong>Bachelor’s, Master’s, doctoral and eligible specialisation</strong> programmes.</li>
        <li><strong>Economic and merit criteria</strong> as set in the annual DSU call — the scholarship is need-based first, with academic requirements attached.</li>
        <li><strong>All nationalities</strong> — Italian, EU and non-EU students, including stateless students, refugees and asylum seekers, subject to the documentation rules.</li>
        <li>International students with income or assets outside Italy must provide <strong>foreign financial documentation</strong> covering family composition, income, real estate and movable assets, <strong>translated into Italian</strong> and <strong>legalised</strong> as required.</li>
        <li>Students from countries on DSU’s list of <strong>particularly poor and developing countries</strong> can instead submit a certificate that the family is not wealthy (per the call’s Appendix C).</li>
        <li>For the <strong>PhD and specialisation window</strong> open now: students enrolled in, or intending to enrol in, eligible doctoral or specialisation programmes at the University of Pisa.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monetary scholarship</strong> — the amount varies according to economic status and student classification (on-site, commuter or off-site).</li>
        <li><strong>Free meals</strong> through DSU food services, for scholarship winners and eligible non-winners alike.</li>
        <li><strong>Free accommodation</strong> for eligible off-site scholarship winners, subject to availability.</li>
        <li><strong>Accommodation-related support</strong> for eligible students who do not receive a residence place.</li>
        <li><strong>Exemption from the regional university study tax</strong>.</li>
        <li><strong>Full exemption from the annual all-inclusive tuition fee</strong> (maximum €2,900 for regular students in 2026/27) under the University’s rules.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Documentation of <strong>family status</strong> — the composition of the family unit whose income and assets are considered under the DSU rules.</li>
        <li>Documentation of <strong>income</strong> — official certificates showing the relevant annual income of family members.</li>
        <li>Documentation of <strong>real estate / buildings</strong> — houses, land or other property owned by the applicant or family members.</li>
        <li>Documentation of <strong>movable assets</strong> — bank accounts, deposits, securities and other financial holdings.</li>
        <li>Foreign documents must be <strong>translated into Italian</strong> and <strong>legalised or apostilled</strong> as required — the correct route depends on the issuing country and the Apostille Convention status; check the DSU instructions and the Italian embassy or consulate for your country.</li>
        <li>A <strong>Single Substitutive Declaration (DSU/ISEE)</strong> for subsidised benefits for the right to education — the call summary states it must be signed by 7 September 2026 for the general competition; check the current call for the PhD/specialisation position on this document.</li>
        <li>Do not begin with a generic legalisation procedure copied from another student’s experience — the exact procedure depends on your country, the document type and the issuing authority.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official <strong>DSU Toscana Scholarship &amp; Accommodation Call 2026/27</strong> before submitting — it sets the economic and merit criteria and the documentation rules.</li>
        <li>Prepare your <strong>financial documentation</strong> early: family status, income, property and movable assets, with translation into Italian and legalisation/apostille as required. This is the step that causes most delays for international applicants.</li>
        <li>Register on the <strong>DSU Toscana Sportello Studente portal</strong> and fill out the online application form.</li>
        <li>For <strong>PhD and specialisation courses</strong>, submit between <strong>25 September and 16 November 2026, 1:00 PM Italian time</strong>.</li>
        <li>Separately, complete your <strong>University of Pisa admission</strong> application for your chosen programme, and <strong>Universitaly pre-enrolment</strong> if you are a non-EU student requiring a visa — these are not covered by the DSU deadline.</li>
        <li>Watch for the rankings: provisional ranking for PhD/specialisation on <strong>15 December 2026</strong>, final ranking on <strong>15 January 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Pisa DSU Scholarship 2027?',
  'For PhD and specialisation courses: 16 November 2026 at 1:00 PM Italian time (applications open 25 September 2026). For Bachelor’s, Master’s and single-cycle degree courses the 2026/27 deadline was 7 September 2026 at 1:00 PM and has passed.'),
 ('How much is the DSU Toscana Scholarship worth?',
  'There is no single fixed amount. The monetary component varies according to the student’s economic circumstances and whether they are classified as on-site, commuter or off-site, on top of free meals, possible free accommodation, accommodation support, exemption from the regional study tax and full tuition exemption. Guides do not publish a single 2026/27 figure, so none is stated here.'),
 ('Who can apply for the DSU Toscana Scholarship at the University of Pisa?',
  'Students pursuing their first higher-education qualification at the University of Pisa (and other Tuscan institutions) — Bachelor’s, Master’s, doctoral and eligible specialisation programmes — of any nationality, subject to the economic and merit criteria in the annual DSU call. International students must provide foreign financial documentation, translated into Italian and legalised.'),
 ('Is the DSU Toscana Scholarship the same as University of Pisa admission?',
  'No. DSU Toscana is a separate regional authority, and the DSU application is a separate process through the Sportello Studente portal. You must also apply for admission to your University of Pisa programme, and complete Universitaly pre-enrolment if you are a non-EU student requiring a visa.'),
 ('What documents do international students need for the DSU Scholarship?',
  'Documentation of family status, income, real estate/buildings and movable assets (bank accounts, deposits, securities), translated into Italian and legalised or apostilled as required, plus a Single Substitutive Declaration (DSU/ISEE) for subsidised benefits. Students from countries on DSU’s list of particularly poor and developing countries can instead submit a certificate that the family is not wealthy.'),
 ('When are the DSU Toscana results announced?',
  'For PhD and specialisation courses: provisional ranking 15 December 2026, final ranking 15 January 2027. For Bachelor’s, Master’s and single-cycle courses, the provisional ranking was 30 September 2026 and the final ranking is 30 November 2026 (4 November 2026 for first-year Bachelor’s/single-cycle scholarship rankings).'),
 ('What other scholarships are available at the University of Pisa?',
  'The university also lists Italian Ministry of Foreign Affairs (MAECI) scholarships and Invest Your Talent in Italy, offered by MAECI and the university — each has its own call and deadline. Invest Your Talent in Italy for 2026/27 closed on 11 May 2026.'),
 ('Do I need to know Italian to apply for the DSU Scholarship?',
  'The application and documentation are in Italian — foreign financial documents must be translated into Italian. The DSU call and the University of Pisa’s international pages explain the requirements; check the current call for the language rules that apply to your category.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the DSU Toscana 2026/27 call as reported in the Scholarships Central guide (scholarshipscentral.com, read in full, crawled 28 Oct 2026) and corroborated by ScholarshipsTab, Kabul Scholarship, UniPage and DAADScholarship: DSU Toscana is the regional right-to-study authority for Tuscany (universities of Pisa, Florence, Siena); benefits — monetary scholarship varying by economic status and on-site/commuter/off-site classification, free DSU catering for winners and eligible non-winners, free accommodation for eligible off-site winners subject to availability, accommodation-related support, exemption from the regional university study tax, full tuition exemption under University rules (maximum all-inclusive tuition EUR 2,900 for 2026/27); application periods — Bachelor's/Master's/single-cycle 20 July-7 September 2026, 1:00 PM Italian time; PhD/specialisation 25 September-16 November 2026, 1:00 PM; rankings — PhD/specialisation provisional 15 December 2026, final 15 January 2027; Bachelor's/Master's provisional 30 September 2026, final 30 November 2026; portal Sportello Studente; foreign documentation categories — family status, income, buildings, movable assets, translated into Italian and legalised/apostilled; Single Substitutive Declaration (DSU/ISEE) for subsidised benefits; Invest Your Talent in Italy closed 11 May 2026; Universitaly general deadline 30 September 2026; University accepts only visas issued by 30 November 2026 for enrolment. CONFLICTS: (1) The queue's "September 2026" deadline was the Bachelor's/Master's window (closed 7 September 2026) — the article leads with the split and the still-open PhD/specialisation window to 16 November 2026. (2) LegitScholarship states a 5 September 2026 DSU deadline — superseded by the call's 7 September 2026, 1:00 PM date, corroborated by four other sources; 5 September is not used. (3) No single monetary amount is published for the 2026/27 DSU award in any source checked — the article states the benefit structure and does not invent a figure. (4) The 7 September 2026 date for the Single Substitutive Declaration is stated in the call summary for the general competition; the article flags readers to check the current call for the PhD/specialisation position on that document rather than asserting it applies unchanged. The official DSU call link is www.dsu.toscana.it (linked via the guide); the University of Pisa is www.unipi.it.</p>''',
 dl_long='PhD and specialisation: 16 November 2026, 1:00 PM (Bachelor’s/Master’s closed 7 September 2026)',
 offlinks=[('Scholarships Central — University of Pisa Scholarship 2026/27 (DSU guide)', 'https://www.scholarshipscentral.com/blog/university-of-pisa-scholarship-2026-2027'),
           ('ScholarshipsTab — University of Pisa DSU Scholarship 2026/2027', 'https://www.scholarshiptab.com/scholarships/university-of-pisa-dsu-scholarship-2026-2027'),
           ('DAADScholarship — Italy DSU Toscana Scholarships 2027 Explained', 'https://daadscholarship.com/italy-dsu-toscana-scholarships-2027-application-procedure-explained/'),
           ('Bright Scholarship — University of Pisa Scholarship 2027', 'https://brightscholarship.com/university-of-pisa-scholarship-2027-italy/')],
 related_titles=['perugia-phd', 'gottingen-daad-2027', 'ucl-impact-2027', 'tsukuba-mext-2027'])),

# ---------------------------------------------------------------- build + validate
class _P(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.errs = []
    def error(self, m): self.errs.append(m)

for a in A:
    _split_verify(a)
    n = build_article(BASE, OUT, a, CARDS)
    p = OUT / (a['slug'] + '.html')
    assert p.exists(), a['slug']
    t = p.read_text()
    for bad in ('AICTE Pragati', 'Lorem'):
        assert bad not in t, (a['slug'], bad)
    assert '#' not in a['slug'], a['slug']
    assert '919905166009' in t, a['slug'] + ' missing WhatsApp'
    pr = _P(); pr.feed(t)
    assert not pr.errs, (a['slug'], pr.errs)
    print('OK', a['slug'], n, 'chars')
print('built', len(A), 'articles')

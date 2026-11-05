#!/usr/bin/env python3
"""Batch 63 (cron run 63, 29 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. 20th Japan International MANGA Award 2026 - SKIPPED: deadline passed
   30 Jun 2026 (official MOFA / Japan embassy pages).
2. Judicial Fellowship Program 2026 in USA - SKIPPED: deadline passed
   1 Jun 2026 (official uschamberfoundation.org FAQ); 2026 programme
   already ran 26 Sep-10 Oct 2026.
3. Erasmus Mundus WOP-P Scholarships 2026 - SKIPPED: deadline passed
   10 May 2026.
4. European University Institute Traineeships 2026 in Italy - VERIFIED
   (open calls; current published vacancies close 2 Nov 2026, 23:59 CET;
   grant EUR 1,540/month from 1 Jan 2026).
5. Discover Niagara Cultural Exchange Program 2026 in Canada - SKIPPED:
   deadline passed 15 Jun 2026; programme dates 24-27 Aug 2026 passed.
6. University of Freiburg DAAD EPOS Scholarship 2027 - SKIPPED: deadline
   passed 15 Oct 2026 (official meg.uni-freiburg.de).
7. UK Government DSIT Fellowship 2026 in UK - SKIPPED: applications
   closed 6 May 2026 (gov.uk: "closed for applications").
8. Chula LINK Scholarships 2026 in Thailand - SKIPPED: deadline passed
   24 May 2026.
9. Scout Adventures Volunteer Program 2026 in UK - VERIFIED (rolling;
   applications open for Sep 2026-Sep 2027 and Jan 2027-Nov 2027
   placements; official scoutadventures.org.uk).
10. Purdue University Scholarship 2026 in USA - VERIFIED (Nov 1 firm
    deadline, official admissions.purdue.edu; Trustees USD 16,000/yr
    nonresidents, Presidential USD 10,000/yr nonresidents; domestic-only
    caveat recorded from secondary sources).
11. CERN Administrative Student Program 2026 - SKIPPED: 2026 cycles
    closed (2026-1 deadline 16 Nov 2025; 2026-2 deadline 23 Feb 2026).
12. Tobe Maki Scholarship Program 2026 in Japan - SKIPPED: deadline
    passed 8 May 2026 (web) / 12 May 2026 (postal).
13. Young Leaders in National Security Fellowship 2026 in UK - SKIPPED:
    deadline passed 5 Jun 2026; programme 7-11 Sep 2026 passed.
14. Simmons University Kotzen Scholarship 2026 in USA - VERIFIED
    (1 Dec 2026 deadline widely reported; full tuition + room/board +
    USD 3,000/yr enrichment award).
15. South Korea Scholarships Without IELTS 2026 - SKIPPED: listicle,
    not a single scheme.
16. DAAD Procope Scholarship Program 2026 in Germany - SKIPPED:
    deadline passed 1 Jul 2026.
17. United Nations Volunteer Program 2026 - VERIFIED (rolling via the
    UNV Unified Volunteering Platform; onsite assignments supported
    under UNV conditions of service; online volunteering unpaid, up to
    20 hrs/week, max 12 weeks).
18. UNU Junior Fellows Internship 2026 in Japan - SKIPPED: Fall 2026
    deadline passed 8 May 2026 (Spring 2027 is a different intake).
19. UST Scholarships 2026 in South Korea - SKIPPED: deadline passed
    16 Oct 2026.
20. Japanese Government MEXT Scholarship 2026-27 - SKIPPED: embassy
    deadlines for the 2026-27 round passed (May-Jun 2026 across
    embassies checked).
21. AKS Graduate Fellowship 2026 in South Korea - SKIPPED: deadline
    passed 8 May 2026.
22. OpenAI Safety Fellowship 2026 - SKIPPED: deadline passed 3 May 2026
    (official openai.com announcement); programme Sep 2026-Feb 2027.
23. WTO Young Professionals Program 2027 - SKIPPED: deadline passed
    6/7 May 2026.
24. CATS Fellowship Programs 2026 in Germany - SKIPPED: deadline
    passed 30 Apr 2026.
25. Deloitte Discovery Internship 2026 in USA - SKIPPED: Summer 2026
    recruiting closed 1 May 2026 (official Deloitte posting); the
    aggregator claim of "open all year" is not a single current deadline.
26. Sabanci University PURE Summer Program 2026 in Turkey - SKIPPED:
    deadline passed 28 Apr 2026; programme 6 Jul-20 Aug 2026 passed.
27. UN OHCHR Fellowship Program 2026 in Switzerland - SKIPPED: all
    2026 tracks closed (African Descent 15 May 2026; Indigenous
    6 Sep 2026; Minorities 31 Jan 2026).
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 29)
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
 'eui-2026': {'mono': 'EUI', 'title': 'European University Institute Traineeships 2026 in Italy (Fully Funded)',
   'href': 'european-university-institute-traineeships-2026-italy.html',
   'dpill': 'Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
   'award': 'Paid traineeships in Florence of up to 12 months: a maintenance grant of €1,540 a month (from 1 January 2026; €770 for non-EU/EEA trainees on the 20-hour part-time arrangement), travel reimbursement at the start and end, and access to EUI facilities, training and seminars.',
   'elig': 'Nationals of EU Member States and candidate countries (plus Ukrainian nationals; a limited number of non-Member State nationals by agreement); a first university degree obtained no more than 3 years before the deadline; English at B2 or above plus another language.',
   'tags': [('Traineeship', 'blue'), ('Italy', 'teal')]},
 'scout-2026': {'mono': 'SA', 'title': 'Scout Adventures Volunteer Program 2026 in UK (Fully Funded)',
   'href': 'scout-adventures-volunteer-program-2026-uk.html',
   'dpill': 'Rolling · open now',
   'award': 'Residential volunteering at Scout Adventures centres: free on-site accommodation and meals, uniform, a weekly allowance (£35 for the UK Volunteer Trainee programme), full instructing training and outdoor qualifications, and hundreds of hours of hands-on experience.',
   'elig': 'Aged 18+ at the start of the placement; based in the UK for the trainee programme; a good standard of English; energy for outdoor work in all weathers; no formal qualifications or prior experience required.',
   'tags': [('Volunteer Programme', 'blue'), ('United Kingdom', 'teal')]},
 'purdue-2026': {'mono': 'PU', 'title': 'Purdue University Scholarship 2026 in USA (Funded)',
   'href': 'purdue-university-scholarship-2026-usa.html',
   'dpill': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
   'award': 'University-wide merit scholarships with no separate application: Trustees $16,000 a year for nonresidents ($10,000 for Indiana residents), Presidential $10,000 a year for nonresidents ($4,000 for residents), Indy Scholars $10,000 a year minimum, and Lilly Scholars full tuition — renewable for up to four years at a 3.00 Purdue GPA.',
   'elig': 'Incoming first-year undergraduates whose admission application is complete by the firm 1 November deadline; awards are made by holistic review of the admission application. Two secondary sources describe the university-wide awards as domestic-only — confirm eligibility on Purdue’s official page before applying.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'simmons-kotzen-2026': {'mono': 'SU', 'title': 'Simmons University Kotzen Scholarship 2026 in USA (Fully Funded)',
   'href': 'simmons-university-kotzen-scholarship-2026-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': 'Simmons’ most distinguished merit award (the Distinguished Scholar Award): full tuition, mandatory fees and room and board, plus an additional $3,000 a year for study abroad, summer internship tuition, short-term courses or research — for up to four years of full-time undergraduate study.',
   'elig': 'First-year undergraduate applicants, including international students, with an outstanding academic record (reported benchmarks: GPA 3.3+, honours/AP/IB coursework, ACT 28+ or SAT 1300+); apply for admission and the scholarship by 1 December.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'unv-2026': {'mono': 'UN', 'title': 'United Nations Volunteer Program 2026 (Fully Funded)',
   'href': 'united-nations-volunteer-program-2026.html',
   'dpill': 'Rolling · open all year',
   'award': 'A route into UN service, not a single award: onsite UN Volunteer assignments are supported under UNV conditions of service (including a resettlement allowance on successful completion), while UN Online Volunteering offers unpaid remote assignments of up to 20 hours a week for a maximum of 12 weeks.',
   'elig': 'Aged 18+; requirements vary by assignment — professional onsite roles typically need a degree and relevant experience, while online volunteering sets no single academic background and each host organisation states its own skills and language needs.',
   'tags': [('Volunteer Programme', 'blue'), ('Global', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. EUI Traineeships
A.append(dict(
 slug='european-university-institute-traineeships-2026-italy',
 title='European University Institute Traineeships 2026 in Italy (Fully Funded)',
 meta='European University Institute (EUI) Traineeships 2026 in Florence, Italy: paid placements of up to 12 months with a €1,540 monthly grant. Current published vacancies close 2 November 2026 — check the vacancy notice, as other EUI calls are open calls.',
 short='EUI Traineeships 2026', kicker='Italy · Traineeship · Paid', mono='EUI',
 prov_short='European University Institute', prov_cat='Institute · Italy',
 h1='European University Institute Traineeships 2026 in Italy (Fully Funded)',
 sub='Do not read this as one deadline. The European University Institute in Florence publishes traineeships vacancy by vacancy, and each notice carries its own terms: the notices published for the February 2027 intake close on 2 November 2026 at 23:59 CET, while other EUI calls are open calls with no fixed closing date. What is common to the paid route is the package — a maintenance grant of €1,540 a month from 1 January 2026, for a placement of up to one year — and the shape of the work: a real job inside an international research institute, under a supervisor, in units ranging from the Library and the Historical Archives of the European Union to ICT, communications and central administration.',
 facts=facts([
  ('Provider', 'European University Institute (EUI), Florence, Italy'),
  ('Award', 'Paid traineeship: €1,540/month grant (from 1 January 2026); up to 12 months'),
  ('Level', 'Graduates — first university degree required for paid traineeships'),
  ('Deadline', '2 November 2026, 23:59 CET (current published vacancies; other calls are open calls)'),
  ('Eligibility', 'EU / candidate-country nationals (plus Ukrainians; limited non-Member State places by agreement); degree within the last 3 years; English B2+'),
 ]),
 body='''
      <h2 id="about">About the traineeship</h2>
      <p>The European University Institute is a postgraduate research institute in Florence dedicated to the social sciences and humanities, and its traineeships place graduates inside the working units of the Institute rather than in a classroom. Trainees are assigned to a unit and contribute to that unit's projects under an experienced supervisor. The units that regularly take trainees include the Library, the ICT Service, the Historical Archives of the European Union, academic units, and central services such as communications, administration and the legal office. Recent published vacancies illustrate the range: events, graphic design, multimedia, research and institutional communications, marketing, academic services and administrative systems.</p>
      <p>Two kinds of traineeship exist, and the distinction matters for pay. A paid traineeship can last up to one year (three months minimum in justified cases) and carries the monthly maintenance grant. An unpaid traineeship lasts at most three months and must be covered by an agreement between the trainee's home university or organisation and the EUI if a home grant is involved. This article describes the paid route in detail; if you are still enrolled, check whether your university can support an unpaid placement instead.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly grant:</strong> €1,540 a month for paid traineeships, at the rate applying from 1 January 2026. Trainees from outside the EU/EEA who are on the 20-hour part-time arrangement required by Italian law receive €770 a month.</li>
        <li><strong>Travel:</strong> reimbursement of travel expenses at the beginning and end of the traineeship for trainees recruited from outside Florence.</li>
        <li><strong>Meals and facilities:</strong> a discounted lunch each day at the EUI canteen, and access to EUI facilities including the Library, reading rooms and the Centre for Academic Literacies and Languages.</li>
        <li><strong>Training:</strong> participation in professional training, public seminars, workshops and wellbeing activities, plus experience in an international, multicultural research institution.</li>
        <li><strong>Leave:</strong> paid leave arrangements apply under the traineeship rules — the vacancy notice for your role states the exact terms.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Nationality:</strong> nationals of EU Member States and of candidate countries benefiting from a pre-accession strategy can apply, and Ukrainian nationals are also eligible. A limited number of nationals of non-Member States may be accepted on the basis of a specific agreement.</li>
        <li><strong>Degree:</strong> for a paid traineeship you must hold a completed first university degree (Bachelor's or equivalent). Your last university diploma must have been obtained no longer than three years before the deadline — unless you are enrolled in further university studies when you apply.</li>
        <li><strong>Languages:</strong> proven knowledge of spoken and written English at CEFR level B2 or above, plus a satisfactory knowledge of another language. English, French and Italian are the Institute's main working languages.</li>
        <li><strong>Start dates:</strong> traineeships normally start on 1 February, 1 April, 1 June, 1 September or 1 November. The vacancies published for the February 2027 intake start on 1 February 2027 and last 12 months.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV</strong>, uploaded through the online application form.</li>
        <li><strong>ID or passport</strong>, uploaded through the same form.</li>
        <li>Your application counts as submitted only once you receive the automatic confirmation email — if that email does not arrive, the application has not gone through.</li>
        <li>Shortlisted candidates are invited to interview. Only candidates invited to interview receive information from the EUI on their selection status.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the EUI traineeships page and open the vacancy notice for the role you want — the notice (for example V.TR.ACS.2.2026 for the Academic Service traineeship) is the binding document, and different roles have different closing dates.</li>
        <li>Check the notice for its deadline: the current published vacancies for the February 2027 intake close on <strong>2 November 2026 at 23:59 CET</strong>. Other EUI calls are published as open calls with no specific deadline, and applications are considered as they arrive.</li>
        <li>Complete the online application form and upload your CV and ID/passport. Only applications submitted through the online form are accepted.</li>
        <li>Wait for the automatic confirmation email, then for an interview invitation if you are shortlisted. If you have difficulty submitting, the EUI gives the contact Traineeships@EUI.eu.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the EUI Traineeships 2026?',
  'There is no single deadline. The vacancy notices published for the February 2027 intake close on 2 November 2026 at 23:59 CET, while other EUI traineeship calls are open calls with no specific deadline. Always read the vacancy notice for the role you are applying to.'),
 ('How much does an EUI traineeship pay?',
  'Paid traineeships carry a maintenance grant of €1,540 a month at the rate from 1 January 2026. Non-EU/EEA trainees on the 20-hour part-time arrangement required by Italian law receive €770 a month. Unpaid traineeships, up to three months, carry no grant.'),
 ('How long does an EUI traineeship last?',
  'A paid traineeship lasts up to one year (three months minimum in justified cases). An unpaid traineeship lasts at most three months. The February 2027 intake roles last 12 months full-time.'),
 ('Who can apply for an EUI traineeship?',
  'Nationals of EU Member States and candidate countries, plus Ukrainian nationals; a limited number of non-Member State nationals may be accepted by agreement. Paid trainees need a first university degree obtained within the last three years (unless still studying) and English at B2 or above.'),
 ('Do I need to know Italian to apply?',
  'Not necessarily. English at B2 or above is required, plus a satisfactory knowledge of another language; English, French and Italian are the main working languages. Individual vacancy notices may ask for more.'),
 ('What documents do I need to apply?',
  'A CV and an ID or passport, uploaded through the online application form. The application is only complete once you receive the automatic confirmation email.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the EUI's own vacancy notice (eui.eu, V.TR.ACS.2.2026: deadline 2 November 2026 at 23:59 CET; online form only; CV + ID/passport; confirmation email; contact Traineeships@EUI.eu; travel reimbursement, discounted canteen lunch, library and language-centre access, training and seminars) plus ScholarshipsAds (paid €1,540/month from 1 Jan 2026, non-EU/EEA part-time €770; paid up to 1 year, minimum 3 months; unpaid up to 3 months; start dates 1 Feb / 1 Apr / 1 Jun / 1 Sep / 1 Nov; February-intake notices closing annually 30 November in some years vs open calls) and Youth Works Hub (six 2026 open calls at €1,540/month, 12 months; Academic Service and Administrative Systems vacancies closing 2 November 2026 at 23:59 CET, starting 1 February 2027; degree within 3 years; English B2 plus another language). CONFLICTS: (1) Older secondary summaries quote €1,400–€1,490/month — the current published rate from 1 January 2026 is €1,540, and the article uses that. (2) Some guides say February-intake notices close 30 November; the current vacancy notices checked for this run close 2 November 2026, and the article leads with the notice date. (3) One aggregator describes EUI traineeships as open to all nationalities — the vacancy rules restrict paid places to EU/candidate-country nationals (plus Ukrainians, with limited non-Member State places by agreement), and the article follows the vacancy rules.</p>''',
 dl_long='2 November 2026, 23:59 CET (current published vacancies for the February 2027 intake; other EUI traineeship calls are open calls with their own dates — check the vacancy notice)',
 offlinks=[('European University Institute — Traineeship vacancy notice (official PDF)', 'https://www.eui.eu/Documents/ServicesAdmin/PersonnelService/Administrative-Positions/2026/V.TR.ACS.2.2026.pdf'),
           ('ScholarshipsAds — European University Institute Traineeships', 'https://www.scholarshipsads.com/internship/european-university-institute-eui-italy-traineeship'),
           ('Youth Works Hub — Paid EUI Traineeships in Florence', 'https://youthworkshub.org/30960'),
           ('Bright Scholarship — European University Institute Traineeships 2026', 'https://brightscholarship.com/european-university-institute-traineeships/')],
 related_titles=['boell-2027', 'ista-internships-2027', 'pisa-dsu-2027', 'gottingen-daad-2027'])),

# ---------------------------------------------------------------- 2. Scout Adventures
A.append(dict(
 slug='scout-adventures-volunteer-program-2026-uk',
 title='Scout Adventures Volunteer Program 2026 in UK (Fully Funded)',
 meta='Scout Adventures Volunteer Program 2026 in the UK: residential volunteering at Scout adventure centres with free accommodation and meals, a weekly allowance, instructing training and outdoor qualifications. Applications open now for September 2026–September 2027 and January 2027–November 2027 placements.',
 short='Scout Adventures Volunteer Program 2026', kicker='United Kingdom · Volunteer Programme · Residential', mono='SA',
 prov_short='Scout Adventures', prov_cat='The Scout Association · United Kingdom',
 h1='Scout Adventures Volunteer Program 2026 in UK (Fully Funded)',
 sub='This is a working year outdoors, not a scholarship and not a holiday placement. Scout Adventures, the Scout Association activity-centre arm, takes residential volunteers who live on site and spend their weeks instructing young people in outdoor activities — climbing, water sports, target sports, high ropes and more — while earning the instructing qualifications to do it properly. Applications are open now for two placement windows, September 2026 to September 2027 and January 2027 to November 2027, and the programme is deliberately open to people without formal qualifications: energy, a good standard of English and a willingness to be outside in all weathers matter more than a CV full of certificates.',
 facts=facts([
  ('Provider', 'Scout Adventures (The Scout Association), United Kingdom'),
  ('Award', 'Residential volunteering: free accommodation + meals, uniform, £35/week allowance (UK trainee programme), training + qualifications'),
  ('Duration', 'September 2026–September 2027, or January 2027–November 2027'),
  ('Deadline', 'Rolling — applications open now for both placement windows'),
  ('Eligibility', 'Aged 18+ at the start of the placement; UK-based for the trainee programme; good English; no formal qualifications required'),
 ]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>Scout Adventures runs five activity centres across the UK, and its residential volunteers are part of the team that delivers adventures to thousands of young people each year. As a volunteer you work around 35 hours a week on average — quieter in winter, busier in summer, spread across five days including evenings and weekends — with up to 18 days off during the placement. The role is that of an outdoor activity instructor in training: you learn the skills, then you teach them, logging hundreds of hours of hands-on instructing time by the end of the year.</p>
      <p>Two routes sit under the same umbrella, and applicants often confuse them. The UK Volunteer Trainee Instructor Programme is for people based in the UK, aged 18 or over at the start of the placement, and is the route described on Scout Adventures' own programme page. A separate Residential Volunteer programme is open to UK and international applicants; international volunteers have historically needed a visa route such as the Charity Worker route and have received a higher weekly allowance (reported at £45 a week against £35 for the UK trainee route). If you are applying from outside the UK, confirm the current visa and allowance position with Scout Adventures before you apply — the official trainee page describes the UK-based route.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Living:</strong> live on site with residential volunteers from the UK and around the world, with all meals and your uniform covered.</li>
        <li><strong>Allowance:</strong> a weekly allowance of £35 on the UK Volunteer Trainee programme, plus reimbursement of direct costs. (The £45 figure reported for the international Residential Volunteer route is not stated on the official trainee page and is flagged as reported, not confirmed.)</li>
        <li><strong>Training:</strong> a full induction covering instructing skills, first aid, safeguarding and customer service, then a range of outdoor qualifications — including ERCA High Ropes, Target Sports, Water Sports, Mountain Training, First Aid and Health and Safety courses.</li>
        <li><strong>Experience:</strong> hundreds of hours instructing youth groups, plus experience of centre operations, and a CV built around real instructing qualifications rather than classroom certificates alone.</li>
        <li><strong>Community:</strong> a volunteering family of over 100 volunteers across the centres, and the chance to be part of the 2026/2027 season's story.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Age:</strong> 18 or older at the start of the placement.</li>
        <li><strong>Base:</strong> the UK Volunteer Trainee Instructor Programme welcomes applications from anyone based in the UK. It is advantageous but not essential to be a Scout or Guide member or part of a youth organisation.</li>
        <li><strong>Attitude and fitness:</strong> high energy, a positive can-do attitude, and willingness to work outdoors in all weather conditions, including evenings and weekends.</li>
        <li><strong>English:</strong> a good standard of English, since you will be instructing and safeguarding young people.</li>
        <li><strong>Qualifications:</strong> no specific formal qualifications or previous experience are required — training is provided from the start.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Online application form</strong> with personal details and your motivation for joining.</li>
        <li><strong>A letter of recommendation</strong> from a school, university or employer.</li>
        <li><strong>A short video</strong> (around two minutes) introducing yourself and why you want to volunteer.</li>
        <li><strong>A recent photograph.</strong></li>
        <li>If you are a current Scout or Guide, membership confirmation from your National Scout or Guide organisation.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official programme page and choose your placement window: <strong>September 2026 to September 2027</strong> or <strong>January 2027 to November 2027</strong>. Applications are open now for both.</li>
        <li>Prepare your recommendation letter and record your two-minute introduction video.</li>
        <li>Submit the online application form with all attachments. There is no application fee.</li>
        <li>Eligible applicants may be contacted for an online interview. If selected, you will be invited to initial training and supported with planning your arrival and your residential volunteering experience.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Scout Adventures Volunteer Program fully funded?',
  'It is a residential volunteering programme rather than a cash scholarship: accommodation and meals are covered, uniform is provided, and trainees receive a weekly allowance (£35 on the UK trainee programme) plus reimbursement of direct costs. Travel to the UK and visa costs for international applicants are not stated as covered.'),
 ('What is the deadline for the Scout Adventures Volunteer Program 2026?',
  'There is no single published deadline — applications are open now on a rolling basis for the September 2026–September 2027 and January 2027–November 2027 placements. Apply early, since centres fill their volunteer teams ahead of each season.'),
 ('Do I need qualifications or Scout experience to apply?',
  'No. No specific formal qualifications or prior experience are required, and being a Scout or Guide member is advantageous but not essential. Training and qualifications are provided during the placement.'),
 ('How many hours a week will I work?',
  'Around 35 hours a week on average on the UK trainee programme, spread across five days including evenings and weekends, with quieter winter weeks and busier summer weeks, and up to 18 days off during the placement.'),
 ('Can international applicants apply?',
  'A Residential Volunteer route for UK and international applicants is widely reported, but the official programme page checked for this article describes the UK-based trainee programme. International applicants should confirm the current visa route and allowance with Scout Adventures before applying.'),
 ('Is there an application fee?',
  'No — there is no application fee.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against Scout Adventures' own programme page (scoutadventures.org.uk, UK Volunteer Trainee Instructor Programme: applications open now for September 2026–September 2027 and January 2027–November 2027; 35 hours/week average across 5 days; up to 18 days off; UK-based, 18+; induction in instructing, first aid, safeguarding and customer service; ERCA High Ropes, Target Sports, Water Sports, Mountain Training, First Aid and Health and Safety courses; on-site living with meals and uniform covered; £35/week allowance plus direct-cost reimbursement) plus Opportunities Radar (11–12 months, 5 days/week, no fee; £45 foreign nationals / £35 UK nationals; food, accommodation and uniform) and Scholarship Union (18+, recommendation letter, ~2-minute video, no formal qualifications needed; residential volunteer and UK trainee routes). CONFLICTS: (1) Aggregators describe a single "fully funded" programme with a £45/£35 split, while the official page describes the UK trainee route at £35 — the article states £35 as the confirmed figure and flags £45 as reported for the international route, not confirmed on the official page. (2) Some aggregator pages print a 30 November 2025 deadline for the 2026 cycle — that date belongs to an earlier intake; the official page currently shows applications open for the 2026/27 and 2027 windows, and the article follows the official page. (3) Visa sponsorship for international volunteers is described by third-party guides (Charity Worker route, applicant-paid visa and health-surcharge costs) and is not confirmed on the official trainee page, so the article tells international applicants to confirm it directly.</p>''',
 dl_long='Rolling — applications open now for September 2026–September 2027 and January 2027–November 2027 placements',
 offlinks=[('Scout Adventures — UK Volunteer Trainee Instructor Programme (official)', 'https://www.scoutadventures.org.uk/uk-volunteer-trainee-instructor-programme'),
           ('Opportunities Radar — Scout Adventures Volunteer Programme 2026', 'https://opportunitiesradar.com/scout-adventures-volunteer-programme-2026/'),
           ('Bright Scholarship — Scout Adventures Volunteer Program 2026 in UK', 'https://brightscholarship.com/scout-adventures-volunteer-program-2026/')],
 related_titles=['uflp-2026', 'ista-internships-2027', 'adidas-internships-2027', 'fbi-honors-2027'])),

# ---------------------------------------------------------------- 3. Purdue
A.append(dict(
 slug='purdue-university-scholarship-2026-usa',
 title='Purdue University Scholarship 2026 in USA (Funded)',
 meta='Purdue University Scholarship 2026 in the USA: university-wide merit scholarships for incoming first-year undergraduates — Trustees $16,000 a year for nonresidents, Presidential $10,000 a year, renewable for four years. No separate application; the admission application must be complete by 1 November 2026.',
 short='Purdue University Scholarship 2026', kicker='USA · Undergraduate · Merit', mono='PU',
 prov_short='Purdue University', prov_cat='University · USA',
 h1='Purdue University Scholarship 2026 in USA (Funded)',
 sub='There is no separate Purdue scholarship form to hunt down, and that is the whole point: Purdue considers incoming first-year students for its university-wide merit scholarships automatically, from the admission application itself. The catch is the date, and it is firm — your admission application must be complete by 1 November, or you are not in the running for the Trustees, Presidential, Indy Scholars or Lilly Scholars awards at all. The headline figures are $16,000 a year for nonresidents on the Trustees Scholarship and $10,000 a year for nonresidents on the Presidential Scholarship, renewable for up to four years if you keep a 3.00 Purdue GPA and stay enrolled full-time. One warning before you get excited: two secondary sources describe these university-wide awards as domestic-only, so international applicants should confirm their eligibility on Purdue\'s official scholarships page before treating this as their plan.',
 facts=facts([
  ('Provider', 'Purdue University, West Lafayette (and Indianapolis), USA'),
  ('Award', 'Trustees $16,000/yr (nonresidents) / $10,000/yr (residents); Presidential $10,000/yr / $4,000/yr; Lilly full tuition'),
  ('Level', 'Incoming first-year undergraduates (first undergraduate degree)'),
  ('Deadline', '1 November 2026 (firm — admission application must be complete)'),
  ('Eligibility', 'Holistic review of the admission application; renewable at a 3.00 Purdue GPA; see the domestic-only caveat in the article'),
 ]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>Purdue's university-wide merit scholarships are awarded through holistic review of the admission application — academic information, essay, recommendations and additional personal experience information all count, and no single GPA or test-score cutoff is published. Notification comes with the admission decision, typically from mid-January. Roughly 15% of applicants receive a merit award in a typical year, so these are competitive awards for the top tier of admitted students, not automatic entitlements. The awards are stackable with other aid, but Purdue adjusts the total if your overall package exceeds the published cost of attendance.</p>
      <p>The four university-wide awards covered here are the core of the scheme. Beyond them, Purdue's colleges run their own scholarships, and there are smaller named awards (for example a National Recognition Programs Scholarship of $1,000 a year and a National Merit Scholarship of $500 a year), but the November 1 deadline and the no-separate-application rule are what matter for the main awards.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Trustees Scholarship:</strong> $16,000 a year for nonresidents, $10,000 a year for Indiana residents — Purdue's largest university-wide merit award, worth up to $64,000 over four years for a nonresident who renews it.</li>
        <li><strong>Presidential Scholarship:</strong> $10,000 a year for nonresidents, $4,000 a year for Indiana residents, recognising high academic achievement plus leadership and service.</li>
        <li><strong>Indy Scholars:</strong> $10,000 a year minimum; to receive it you must accept your offer and enrol as a full-time student in Indianapolis.</li>
        <li><strong>Lilly Scholars at Purdue Program:</strong> full tuition, aimed at students from under-resourced urban and rural populations who have overcome socioeconomic or educational disadvantages or who are among the first generation in their family to attend college, with an opt-in process.</li>
        <li><strong>Renewal:</strong> up to four years (eight semesters) while pursuing your first undergraduate degree, based on continuous full-time enrolment and meeting Purdue's GPA requirement — 3.00 or higher for the main awards.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Who:</strong> incoming first-year undergraduates applying to Purdue. Awards are made by holistic review; Purdue publishes no GPA or test cutoff for the Trustees award, and strong academics alongside a compelling essay, leadership and service are what winning profiles typically show.</li>
        <li><strong>Nationality caveat:</strong> two secondary sources state that these university-wide merit scholarships are for domestic students only (US citizens, nationals and permanent residents) and that international students on F, J or similar visas are not eligible. Purdue's official scholarships page section checked for this article does not state that restriction in the excerpt available, so treat the domestic-only point as reported, not confirmed — and confirm it on the official page before you apply.</li>
        <li><strong>No appeal:</strong> Purdue does not match offers from other institutions and does not consider appeals for merit aid; awards rest on the credentials presented with the application and are non-negotiable.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>No separate scholarship application</strong> and no separate scholarship document set: consideration is based solely on the admission application.</li>
        <li>That means your admission application itself must be complete by the deadline — academic records, essay, recommendations and any additional personal experience information Purdue asks for.</li>
        <li>Check Purdue's admissions pages for the current first-year application requirements for your applicant type, since those are the materials your scholarship decision will be based on.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to Purdue as a first-year undergraduate and make sure the application is <strong>complete by 1 November</strong> — Purdue marks this deadline "firm" for the Trustees, Presidential, Indy Scholars and Lilly Scholars awards.</li>
        <li>There is nothing else to submit for these awards: no separate scholarship form, no extra essay beyond what the admission application asks for.</li>
        <li>Wait for the admission decision, which includes notification of any merit award, typically from mid-January.</li>
        <li>If you are an international applicant, confirm your eligibility for university-wide merit awards on Purdue's official scholarships page first — see the caveat above.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Purdue University Scholarship 2026?',
  '1 November, and it is firm: your admission application must be complete by that date to be considered for the Trustees, Presidential, Indy Scholars and Lilly Scholars awards.'),
 ('Do I need a separate application for Purdue merit scholarships?',
  'No. For the university-wide merit scholarships, consideration is based solely on your admission application. No separate scholarship application is required.'),
 ('How much is the Purdue Trustees Scholarship worth?',
  '$16,000 a year for nonresidents and $10,000 a year for Indiana residents, renewable for up to four years at a Purdue GPA of 3.00 or higher — up to $64,000 in total for a nonresident.'),
 ('Are international students eligible for Purdue merit scholarships?',
  'Two secondary sources describe the university-wide awards as domestic-only, with international students on F, J or similar visas not eligible. That restriction is not stated in the official-page excerpt checked for this article, so confirm it on Purdue’s official scholarships page before applying.'),
 ('Can a Purdue merit award be renewed?',
  'Yes, for up to four years (eight semesters) while pursuing your first undergraduate degree, based on continuous full-time enrolment and a Purdue cumulative GPA of 3.00 or higher.'),
 ('Can I appeal or negotiate a Purdue merit award?',
  'No. Purdue does not match offers from other institutions and does not consider appeals for merit aid.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against Purdue's official first-year scholarships page (admissions.purdue.edu/cost-financial-aid/scholarships: university-wide scholarships; value varies by residency; admission application must be complete to meet a scholarship deadline; holistic review; up to four years/eight semesters for a first undergraduate degree on continuous full-time enrolment and GPA requirements; Trustees $16,000/year nonresidents / $10,000/year residents, deadline Nov. 1 (firm), renewable at 3.00+; Presidential $10,000/year nonresidents / $4,000/year residents, Nov. 1 (firm), renewable at 3.00+; Indy Scholars $10,000/year minimum, Nov. 1 (firm), Indianapolis enrolment required; Lilly Scholars full tuition, Nov. 1 (firm)) plus Coursmooc (international students on F/J visas not eligible for the university-wide awards; ~15% of applicants receive an award; no separate application; awards non-negotiable) and CollegeReadyParent (Trustees $16,000/year nonresident, $64,000 over four years if renewed; results with the admission decision, typically after mid-January; stackable subject to cost of attendance). CONFLICTS: (1) The domestic-only restriction comes from secondary sources only — it is not stated in the official-page excerpt checked, so the article flags it as reported and tells international applicants to confirm it officially. (2) Aggregator pages disagree on minor awards (for example National Merit $500/year vs $2,000–$4,000 total across sources); the article uses only the four main university-wide awards' figures, which the official page confirms.</p>''',
 dl_long='1 November 2026 (firm — admission application must be complete by this date)',
 offlinks=[('Purdue University — First-year Scholarships (official)', 'https://admissions.purdue.edu/cost-financial-aid/scholarships/'),
           ('Coursmooc — Purdue University Undergraduate Scholarship 2026', 'https://coursmooc.com/scholarships/purdue-university-scholarship-2026/'),
           ('CollegeReadyParent — Purdue Scholarships 2026–2027', 'https://collegereadyparent.org/purdue-university-scholarships/'),
           ('Bright Scholarship — Purdue University Scholarship 2026 in USA', 'https://brightscholarship.com/purdue-university-scholarship-2026/')],
 related_titles=['bu-presidential-2027', 'miami-stamps-2027', 'duke-karsh-2026', 'york-pise-2027'])),

# ---------------------------------------------------------------- 4. Simmons Kotzen
A.append(dict(
 slug='simmons-university-kotzen-scholarship-2026-usa',
 title='Simmons University Kotzen Scholarship 2026 in USA (Fully Funded)',
 meta='Simmons University Kotzen Scholarship 2026 in the USA: Simmons’ Distinguished Scholar Award — full tuition, mandatory fees and room and board, plus $3,000 a year for study abroad, internships or research, for up to four years. Deadline 1 December 2026.',
 short='Simmons University Kotzen Scholarship 2026', kicker='USA · Undergraduate · Fully Funded', mono='SU',
 prov_short='Simmons University', prov_cat='University · USA',
 h1='Simmons University Kotzen Scholarship 2026 in USA (Fully Funded)',
 sub='Simmons University in Boston calls the Kotzen Scholarship its most distinguished merit award, and the package explains why: full tuition, mandatory fees and room and board, plus $3,000 a year to spend on study abroad, a summer internship, a short-term course or research — for up to four years of full-time undergraduate study. It replaces any other merit scholarship Simmons offered you, so it is an either/or, not a top-up. The award is open to international students as well as domestic applicants, but only to first-year undergraduates: transfer students are not eligible for the full Distinguished Scholar award. Applications are due on 1 December, and the application is a scholarship application in its own right — a short answer, a formal essay and a resume, sent by email — on top of the admission application.',
 facts=facts([
  ('Provider', 'Simmons University, Boston, Massachusetts, USA'),
  ('Award', 'Full tuition + mandatory fees + room and board + $3,000/year enrichment award, up to 4 years'),
  ('Level', 'First-year undergraduates (including international students)'),
  ('Deadline', '1 December 2026'),
  ('Eligibility', 'Outstanding academic record (reported: GPA 3.3+, honours/AP/IB, ACT 28+ or SAT 1300+); essay + interview for finalists'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The Kotzen Scholarship is the formal name used in scholarship listings for what Simmons itself calls the Distinguished Scholar Award. It is a merit award, not a need-based one — and that distinction matters for international applicants, because Simmons states that international students do not receive need-based aid, while merit scholarships are open to them. The award is made for the normal period of study, up to four years of full-time undergraduate study, and it supersedes any previously awarded merit scholarship: if you win it, it replaces your earlier merit offer rather than stacking on top of it.</p>
      <p>Simmons is a private university in Boston founded in 1899, and the Kotzen competition is deliberately small and selective: a short answer and a formal essay, then finalist interviews, with winners notified by 1 March. The total value is commonly put above $120,000 over four years once tuition, fees and room and board are counted together — treat that total as an aggregator estimate, since Simmons publishes the components (full tuition, fees, room and board, plus the $3,000 annual award) rather than a single headline total.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition</strong> for up to four years of full-time undergraduate study.</li>
        <li><strong>Mandatory fees</strong> covered in full.</li>
        <li><strong>Room and board</strong> covered in full.</li>
        <li><strong>$3,000 a year</strong> for study abroad, summer internship tuition, short-term courses or research support — the enrichment award that sets Kotzen apart from a plain full-tuition offer.</li>
        <li><strong>Renewal</strong> for the normal period of study, subject to remaining a full-time undergraduate in good standing.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Level:</strong> first-year undergraduate applicants only, for a Fall start. Transfer students are not eligible for the full Distinguished Scholar award.</li>
        <li><strong>Nationality:</strong> open to international students of all nationalities as well as domestic applicants.</li>
        <li><strong>Academics:</strong> an outstanding record — the benchmarks reported across listings are a GPA of 3.3 or higher, honours, Advanced Placement or International Baccalaureate coursework, and test scores of ACT 28+ or SAT 1300+ (new SAT) / 1250+ (old SAT, with at least 600 in each section highly recommended). These are reported competitive profiles, not a published Simmons cutoff, so treat them as a guide to the standard, not a guarantee.</li>
        <li><strong>English:</strong> TOEFL or IELTS for non-native English speakers, per the listings.</li>
        <li><strong>Selection:</strong> academic record, essay quality and programme fit, followed by a finalist interview. Finalists are notified in mid-January and winners by 1 March.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Admission application</strong> to Simmons as a first-year undergraduate, submitted before 1 December.</li>
        <li><strong>Short answer</strong> (250 words) explaining how you will spend the annual $3,000 grant.</li>
        <li><strong>Formal essay</strong> (500 words).</li>
        <li><strong>Resume</strong>, sent with the essays by email to ugadm@simmons.edu in PDF or Word format, including your full name and date of birth.</li>
        <li>Finalists are interviewed before the final decision.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to Simmons University as a first-year undergraduate.</li>
        <li>Prepare the short answer (250 words), the formal essay (500 words) and your resume.</li>
        <li>Email both essays and the resume to <strong>ugadm@simmons.edu</strong> in PDF or Word format before the <strong>1 December</strong> deadline — and submit the admission application before the same date.</li>
        <li>Watch for finalist notification in mid-January and an interview in February; winners are notified by 1 March.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What does the Simmons Kotzen Scholarship cover?',
  'Full tuition, mandatory fees and room and board, plus an additional $3,000 a year for study abroad, summer internship tuition, short-term courses or research, for up to four years of full-time undergraduate study.'),
 ('What is the deadline for the Simmons Kotzen Scholarship?',
  '1 December. Both the admission application and the scholarship essays must be submitted before that date; Simmons publishes the date annually as December 1.'),
 ('Can international students apply for the Kotzen Scholarship?',
  'Yes. The award is open to international students of all nationalities. Note that Simmons does not offer need-based aid to international students — Kotzen is a merit award.'),
 ('Can transfer students apply?',
  'No. Transfer students are not eligible for the full Distinguished Scholar award; it is for first-year undergraduates only.'),
 ('What GPA and test scores do I need?',
  'Reported competitive benchmarks are a GPA of 3.3 or higher, honours/AP/IB coursework, and ACT 28+ or SAT 1300+. These are aggregator-reported profiles, not a published Simmons cutoff.'),
 ('Is there a separate application, or is it automatic?',
  'It is a separate application: a 250-word short answer, a 500-word essay and a resume, emailed to ugadm@simmons.edu, in addition to the admission application. Finalists are interviewed.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against EngineersJob (full tuition, room and board, $3,000 for academic pursuits; deadline 1 December 2026; GPA 3.3+, ACT/SAT/TOEFL/IELTS; 250-word short answers + 500-word essay + resume by email to ugadm@simmons.edu), StudentArrive (full tuition, mandatory fees, room and board; $3,000/year for study abroad, summer internship tuition, short-term courses or research; four years; supersedes any previously awarded merit scholarship; deadline 1 December 2026) and StudyHunt (honours/AP/IB; GPA 3.3+; ACT 28+ / SAT 1300+ new / 1250+ old, 600 per section highly recommended; 250-word short answer on the annual grant; finalists notified mid-January, winners by 1 March; deadline 1 December 2026). CONFLICTS: (1) Some pages list the deadline as 1 December 2025 — that was the Fall 2026 entry deadline; the live annual date for the next entry is 1 December 2026, and the article uses that. (2) The "over $120,000 over four years" total is an aggregator estimate from the components, not a Simmons-published total, and is flagged as such. (3) Some aggregator breakdowns add airfare, health insurance and visa-fee reimbursement — those items are not in the core published package (tuition, fees, room and board, $3,000/year) and are not stated in the article.</p>''',
 dl_long='1 December 2026',
 offlinks=[('Simmons University — Admissions (official)', 'https://www.simmons.edu/admissions'),
           ('EngineersJob — Simmons University Kotzen Scholarship 2026', 'https://engineersjob.in/simmons-university-kotzen-scholarship-2/'),
           ('StudentArrive — Simmons University Kotzen Scholarships 2026', 'https://studentarrive.com.ng/simmons-university-kotzen-scholarships-2026/'),
           ('Bright Scholarship — Simmons University Kotzen Scholarship 2026', 'https://brightscholarship.com/simmons-university-kotzen-scholarship-2026/')],
 related_titles=['duke-karsh-2026', 'miami-stamps-2027', 'bu-presidential-2027', 'york-pise-2027'])),

# ---------------------------------------------------------------- 5. UN Volunteer
A.append(dict(
 slug='united-nations-volunteer-program-2026',
 title='United Nations Volunteer Program 2026 (Fully Funded)',
 meta='United Nations Volunteer Program 2026: volunteer with the UN through the Unified Volunteering Platform — onsite assignments supported under UNV conditions of service, and unpaid online volunteering of up to 20 hours a week for up to 12 weeks. Rolling: each vacancy carries its own closing date.',
 short='United Nations Volunteer Program 2026', kicker='Global · Volunteer Programme · Rolling', mono='UN',
 prov_short='United Nations Volunteers', prov_cat='United Nations · Global',
 h1='United Nations Volunteer Program 2026 (Fully Funded)',
 sub='Be careful with the label "fully funded" here, because the United Nations Volunteer programme is not one award with one deadline — it is a standing recruitment system with thousands of individual assignments, and what you get depends entirely on which kind of assignment you take. Onsite UN Volunteers serve with a UN host entity — a peace operation, a UN agency, a government partner — and are supported under UNV conditions of service, which include a resettlement allowance on successful completion. Online Volunteers, by contrast, work remotely on defined tasks, receive no allowance or benefits at all, and are capped at 20 hours a week for a maximum of 12 weeks. Both routes run through the same platform, the UNV Unified Volunteering Platform, and both are open year-round: each vacancy carries its own closing date, so there is no single programme deadline to miss.',
 facts=facts([
  ('Provider', 'United Nations Volunteers (UNV), Bonn — serving UN entities worldwide'),
  ('Award', 'Onsite: support under UNV conditions of service incl. resettlement allowance. Online: unpaid, no benefits'),
  ('Routes', 'Onsite UN Volunteer assignments + UN Online Volunteering (remote)'),
  ('Deadline', 'Rolling — each advertised assignment carries its own closing date'),
  ('Eligibility', 'Aged 18+; requirements vary by assignment (professional roles need a degree + experience; online has no single academic bar)'),
 ]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>United Nations Volunteers is the UN organisation that deploys volunteers to support peace, development and humanitarian work. It runs two distinct routes. Onsite UN Volunteers take up full-time assignments — typically six to twelve months, sometimes longer — inside a host UN entity, in duty stations around the world, including hardship locations. They work as part of the host team, not as interns, and the assignments span everything from child protection and public health to programme management, communications, logistics and data work. Online Volunteering is the remote counterpart: volunteers anywhere in the world take on defined tasks — writing, research, translation, graphic design, digital marketing — for host organisations working towards the Sustainable Development Goals, without travelling and without a contract with UNV or the engaging organisation.</p>
      <p>That distinction drives everything else in this article. If a listing promises a "fully funded UN Volunteer scholarship" with a single deadline, it is almost certainly describing onsite assignments in general terms, or it is simply wrong. Read the individual vacancy: it states the duty station, the duration, the required experience and languages, and the closing date.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Onsite assignments:</strong> support under UNV conditions of service, set out in each vacancy's description of assignment. Summaries of the programme list a resettlement allowance paid after successful completion of the assignment, alongside the living and assignment support that comes with serving in a duty station. Amounts vary by assignment and duty station, so no single figure is stated here.</li>
        <li><strong>Online volunteering:</strong> no allowance, financial compensation or benefits — this is unpaid, remote, task-based volunteering. The return is experience, skills, a certificate of completion for the assignment, and a stronger profile for future UN or development roles.</li>
        <li><strong>Both routes:</strong> practical experience inside the UN system, professional networks, and work that counts as real UN experience on a CV. UNV charges no recruitment fee at any stage — any request for payment connected to a UNV application is a scam signal.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Age:</strong> at least 18 years old for both routes. Some youth-focused onsite programmes set their own upper age limits — the vacancy states them.</li>
        <li><strong>Onsite roles:</strong> requirements depend on the specific role. Professional specialist roles typically require a degree and relevant work experience (for example, a recent UNICEF specialist vacancy asked for a Bachelor's degree in social work, psychology or a related field plus at least three years of relevant experience); community-level roles set lower bars. Language requirements are stated per vacancy — working knowledge of English, French or Spanish is commonly required.</li>
        <li><strong>Online volunteering:</strong> open to adults aged 18 or over worldwide. There is no single academic or professional background for the whole service; each host organisation sets the skills, language and experience requirements for its own task. No IELTS or TOEFL is required as a blanket rule.</li>
        <li><strong>Commitment:</strong> online assignments run up to 20 hours a week for a maximum of 12 weeks; onsite assignments are full-time for their stated duration.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>A UNV profile</strong> on the Unified Volunteering Platform (app.unv.org) — education, skills, languages and professional experience. This profile is your application base; there is no separate paper form.</li>
        <li><strong>Vacancy-specific material</strong> as each assignment asks for it — typically a motivation statement tailored to the role, and sometimes work samples.</li>
        <li><strong>Online volunteering:</strong> register on the platform, complete your profile, and apply to advertised tasks that match your skills. Host organisations set the task requirements and the closing date for each listing.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Create an account on the <strong>UNV Unified Volunteering Platform (UVP)</strong> at app.unv.org and build a complete profile — education, skills, languages and experience.</li>
        <li>Search the advertised assignments (onsite) or the online assignment board (remote) and read each vacancy in full: duty station, duration, requirements and closing date.</li>
        <li>Apply directly through the platform to the roles that match your profile. For onsite roles, only applications submitted through the official process are considered.</li>
        <li>Apply early for any vacancy with a near closing date — for example, specialist onsite vacancies have closed within days of advertisement — and never pay anyone who claims to secure a UNV placement.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the United Nations Volunteer Program 2026?',
  'There is no single deadline. Applications are accepted on a rolling basis throughout the year, and each advertised assignment carries its own closing date — check the vacancy, not a roundup page.'),
 ('Is the UN Volunteer Program fully funded?',
  'Only in the limited sense that onsite assignments are supported under UNV conditions of service, including a resettlement allowance on successful completion. Online volunteering is unpaid, with no allowance or benefits. Neither route is a scholarship with a fixed cash package.'),
 ('Is UN Online Volunteering paid?',
  'No. Online Volunteers receive no living allowance, financial compensation or benefits, and have no contract with UNV or the engaging organisation. Assignments run up to 20 hours a week for a maximum of 12 weeks.'),
 ('Who can apply for UN Volunteering?',
  'Anyone aged 18 or over. Onsite professional roles typically need a degree and relevant experience; online volunteering has no single academic bar — each host organisation states its own requirements.'),
 ('Do I need IELTS to volunteer with the UN?',
  'No blanket IELTS or TOEFL requirement applies. Vacancies state their own language requirements, commonly working knowledge of English, French or Spanish.'),
 ('Does UNV charge an application fee?',
  'No. UNV charges no recruitment fee, and the United Nations does not charge any application, processing, training, interview, testing or recruitment fee. Treat any payment request as a scam.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against ScholarshipHub (UNV Program 2026: minimum age 18; requirements vary by role; working knowledge of English, French or Spanish often required; online volunteering open worldwide; apply via the UNV Unified Volunteering Platform; rolling applications; resettlement allowance after successful completion) plus CrispNG (UNV online volunteering eligibility and how to apply, last checked 27 October 2026: open to adults 18+ worldwide; unpaid, no allowance or benefits, no recruitment fee; up to 20 hours/week, maximum 12 weeks per assignment; each host sets its own skills requirements and deadlines) and a live October 2026 onsite vacancy (UNICEF Viet Nam National UN Volunteer Specialist, Child Protection, Hanoi: Bachelor's in social work/psychology or related field plus 3+ years' relevant experience; apply via app.unv.org; UN no-fee warning). CONFLICTS: (1) One aggregator prints a single "official deadline" of 31 December 2026 — that is not a UNV programme deadline; UNV assignments are rolling with per-vacancy closing dates, and the article follows the platform model. (2) Aggregator pages that call the whole programme "fully funded" conflate onsite support with online volunteering, which is explicitly unpaid — the article separates the two routes. (3) A "UN Volunteer Internship Programme for ages 18–29" described by one aggregator is not a distinct UNV programme in the sources checked; the article describes the two established routes (onsite assignments and online volunteering) only.</p>''',
 dl_long='Rolling — assignments are advertised throughout the year; each vacancy carries its own closing date',
 offlinks=[('United Nations Volunteers — Unified Volunteering Platform (official)', 'https://app.unv.org/'),
           ('CrispNG — UNV online volunteering: eligibility and how to apply', 'https://crispng.com/unv-online-volunteering-eligibility-how-to-apply/'),
           ('ScholarshipHub — United Nations Volunteer (UNV) Program 2026', 'https://scholarshiphub.website/scholarship/united-nations-volunteer-unv-program-2026-2026'),
           ('Bright Scholarship — United Nations Volunteer Program 2026', 'https://brightscholarship.com/united-nations-volunteer-program-2026/')],
 related_titles=['uflp-2026', 'ista-internships-2027', 'fbi-honors-2027', 'adidas-internships-2027'])),

DPILLS = {
 'european-university-institute-traineeships-2026-italy': 'Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
 'scout-adventures-volunteer-program-2026-uk': 'Rolling · open now',
 'purdue-university-scholarship-2026-usa': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
 'simmons-university-kotzen-scholarship-2026-usa': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 'united-nations-volunteer-program-2026': 'Rolling · open all year',
}

for a in A:
    a['dpill'] = DPILLS[a['slug']]
    _split_verify(a)
    n = build_article(BASE, OUT, a, CARDS)
    print('built', a['slug'], n)

# validate
import html.parser as _hp
bad = []
for a in A:
    p = OUT / (a['slug'] + '.html')
    txt = p.read_text()
    class P(_hp.HTMLParser):
        def __init__(self):
            super().__init__(); self.err = None
        def error(self, m): self.err = m
    pp = P(); pp.feed(txt)
    if 'AICTE Pragati' in txt or 'Lorem' in txt:
        bad.append((a['slug'], 'leftover template text'))
    if pp.err:
        bad.append((a['slug'], pp.err))
print('validation issues:', bad if bad else 'none')
print('done')

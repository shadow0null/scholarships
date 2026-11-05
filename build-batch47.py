#!/usr/bin/env python3
"""Batch 47 (cron run 47, 25 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. EU Political Integrity Traineeship 2026 — SKIPPED: deadline passed
   (6 September 2026, 23:59 Brussels time; official transparency.eu page).
2. Open Door Russian Scholarship 2027 — VERIFIED: registration closes
   1 November 2026; full tuition from the Russian federal budget; no
   IELTS; four tracks (Bachelor's/Master's/PhD/Postdoctoral) with age
   bands; official portal od.globaluni.ru.
3. Harvard University Berenson Fellowship 2027 — VERIFIED: $5,200/month
   + up to $1,800 relocation; deadline 16 November 2026 (recommendations
   21 November 2026); PhD required; 4 or 6 months at Villa I Tatti.
4. NVIDIA AMRI Research PhD Internship 2027 — VERIFIED (official
   research.nvidia.com): PhD candidates in CS/CE/EE/Physics/Maths, email
   application with subject "Seeking Research Internship 2027". No
   deadline and no stipend figure published in the official notification
   — both stated as not published, never guessed.
5. DLGS PhD Scholarships 2027 — SKIPPED: deadline passed
   (1 September 2026).
6. EU Jean Monnet Scholarship 2027-2028 — VERIFIED (EEAS +
   jeanmonnet.org.tr): ~170 awards, deadline 27 October 2026, sealed
   envelope to Ankara. CORRECTION: the queue title says "for
   International Students" but the programme is for people working or
   studying in Turkiye, not open to all nationalities — the article
   states this plainly.
7. AAUW International Fellowship Program 2027 — SKIPPED: deadline passed
   (17 September 2026, 5:00 p.m. ET).
8. i-SEA Fellowship Program 2026 — SKIPPED: deadline passed
   (official timeline 10 July-30 August 2026; one aggregator claims it
   is still open — unresolved, so skipped rather than published).
9. Dartmouth College DAAD Master Scholarship 2027 — VERIFIED: DAAD Study
   Scholarship via Dartmouth Fellowships Office endorsement; DAAD portal
   deadline 30 October 2026; EUR 992/month standard DAAD master's rate;
   10-24 months; funding from October 2027. Dartmouth's internal
   endorsement cutoff falls in early October 2026 — the article warns
   applicants to check with the Fellowships Office at once.

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
 'open-door-2027': {'mono': 'OD', 'title': 'Open Door Russian Scholarship 2027 in Russia (Funded)',
   'href': 'open-door-russian-scholarship-2027-russia.html',
   'dpill': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
   'award': 'Full tuition from the Russian federal budget for Bachelor\u2019s, Master\u2019s, PhD and Postdoctoral tracks, plus a free one-year Russian preparatory course where needed; the host university pays a monthly stipend (amount not published centrally).',
   'elig': 'Foreign citizens and stateless persons, including compatriots living abroad; age bands 16\u201323 (Bachelor\u2019s), 20\u201333 (Master\u2019s), 22\u201335 (PhD), 24\u201339 (Postdoctoral).',
   'tags': [('Bachelor\u2019s, Master\u2019s & PhD', 'blue'), ('Russia', 'teal')]},
 'berenson-2027': {'mono': 'HB', 'title': 'Harvard University Berenson Fellowship 2027 in Italy (Stipend $5,200)',
   'href': 'harvard-university-berenson-fellowship-2027-italy.html',
   'dpill': 'Deadline 16 Nov 2026 · %d days left' % dl_left('2026-11-16'),
   'award': '$5,200 per month for 4 or 6 months, plus up to $1,800 relocation support and possible rent-free accommodation or a housing subsidy.',
   'elig': 'Scholars with a completed PhD researching \u201cItaly in the World\u201d (14th\u201317th centuries); all nationalities; early- and mid-career priority.',
   'tags': [('Postdoc & research', 'purple'), ('Italy', 'teal')]},
 'nvidia-amri-2027': {'mono': 'NV', 'title': 'NVIDIA AMRI Research PhD Internship 2027 (Funded)',
   'href': 'nvidia-amri-research-phd-internship-2027.html',
   'dpill': 'No deadline published · Apply early',
   'award': 'Research internship with NVIDIA Research\u2019s AMRI group on embodied AI, human-AI interaction and 4D world modelling; the stipend figure is not published in the official notification.',
   'elig': 'Current PhD candidates in CS, CE, EE, Physics or Maths with top-tier publications and strong PyTorch, Python, C++ and CUDA skills.',
   'tags': [('PhD internship', 'purple'), ('AI & research', 'blue')]},
 'jean-monnet-2027': {'mono': 'JM', 'title': '170 EU Jean Monnet Scholarship 2027\u20132028 for International Students (Fully Funded)',
   'href': 'eu-jean-monnet-scholarship-2027-2028.html',
   'dpill': 'Deadline 27 Oct 2026 · %d days left' % dl_left('2026-10-27'),
   'award': 'Tuition up to \u20ac22,000, a country-specific living allowance and a fixed \u20ac3,500 one-time payment for around 170 scholars studying in EU member states.',
   'elig': 'People working or studying in T\u00fcrkiye \u2014 public and private sector employees, university staff, and final-year or postgraduate students \u2014 specialising in EU acquis fields.',
   'tags': [('Master\u2019s', 'blue'), ('Europe', 'teal')]},
 'dartmouth-daad-2027': {'mono': 'DD', 'title': 'Dartmouth College DAAD Master Scholarship 2027 in Germany for International Students',
   'href': 'dartmouth-college-daad-master-scholarship-2027-germany.html',
   'dpill': 'Deadline 30 Oct 2026 · %d days left' % dl_left('2026-10-30'),
   'award': 'DAAD Study Scholarship via Dartmouth endorsement: \u20ac992 per month for 10\u201324 months, plus insurance, travel and study allowances, for a Master\u2019s in Germany.',
   'elig': 'Dartmouth seniors and recent alumni with a strong first degree (not more than 6 years old) and a clear academic project that makes study in Germany essential.',
   'tags': [('Master\u2019s', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Open Door Russia
A.append(dict(
 slug='open-door-russian-scholarship-2027-russia',
 title='Open Door Russian Scholarship 2027 in Russia (Funded)',
 meta='Open Door Russian Scholarship 2027: the Open Doors competition offers tuition-free study in Russia for Bachelor\u2019s, Master\u2019s, PhD and Postdoctoral tracks, with no IELTS and no application fee. Registration closes 1 November 2026 — eligibility, age bands, documents, how to apply and FAQs.',
 short='Open Door Russian Scholarship 2027', kicker='Russia · Bachelor\u2019s, Master\u2019s, PhD & Postdoc · Funded', mono='OD',
 prov_short='Association of Global Universities', prov_cat='Government of Russia · Open Doors',
 h1='Open Door Russian Scholarship 2027 in Russia (Funded)',
 sub='The Open Door Russian Scholarship 2027 — formally the Open Doors: Russian Scholarship Project — is an international competition that offers tuition-free study at leading Russian universities for Bachelor\u2019s, Master\u2019s, PhD and Postdoctoral tracks. There is no application fee, no IELTS requirement and no entrance examination: winners are chosen on their portfolio and online tasks, with interviews for doctoral and postdoctoral candidates. Registration closes on 1 November 2026, and the prize is a place under the Russian Government education quota, with tuition paid from the federal budget.',
 dpill='Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
 facts=facts([('Award', 'Full tuition for the whole degree, funded from the Russian federal budget under the Russian Government education quota. Winners whose programme is taught in Russian and who need language preparation also get a free one-year preparatory course, with their degree place held. The host university pays a monthly stipend on top — the amount varies by university and is not published centrally, so confirm it with your chosen university. Travel to Russia, accommodation, food, medical insurance and personal expenses are not covered. Postdoctoral winners do not get a degree scholarship; they are offered a research position at an organising university.'),
              ('Eligible', 'Foreign citizens and stateless persons, including compatriots living abroad — there is no restricted list of eligible countries. Each track has an age band and a qualification rule, both measured at the registration opening date (20 August 2026): Bachelor\u2019s, 16\u201323, holding or completing a qualification that permits university entry, and not already holding a Bachelor\u2019s, Specialist or Master\u2019s degree; Master\u2019s, 20\u201333, holding or completing at least a Bachelor\u2019s degree, and not already holding a Specialist or Master\u2019s degree; PhD, 22\u201335, holding or completing a Specialist or Master\u2019s degree, and not already holding a doctorate; Postdoctoral, 24\u201339, already holding a PhD, Candidate of Sciences or Doctor of Sciences degree.'),
              ('How', 'Register on the official portal od.globaluni.ru, choose your track and one or more of the 14 subject areas, build your portfolio, and choose up to six universities in order of preference. There is no fee at any stage. The competition is run in English or Russian.'),
              ('Deadline', 'Registration and portfolio submission close on 1 November 2026 — after that you cannot create an account, edit your personal information or add to your portfolio. The first stage continues to 13 November 2026 for participants who registered before the deadline. Bachelor\u2019s and Master\u2019s results are announced on 21 December 2026; PhD and Postdoctoral results on 26 February 2027.'),
              ('Fine print', 'Do not read \u201cfully funded\u201d as \u201ceverything paid\u201d: tuition is covered, but living costs are yours, and dormitory accommodation — generally inexpensive — is the usual route. Additional Russian Government grant support may be available to qualifying winners or runners-up who obtain quota admission and agree to full-time study in Russian, but it is not guaranteed to every winner. Winners may also need to complete an Education Quota application in their Open Doors account after winning.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Open Doors: Russian Scholarship Project</strong> is organised by the <strong>Association of Global Universities</strong> with the support of Russia\u2019s <strong>Ministry of Science and Higher Education</strong> and Rossotrudnichestvo. It has run since 2017 and, according to the organisers, has drawn more than 618,000 participants from over 200 countries, with more than 16,700 winners and runners-up. More than 20 leading Russian universities take part, across 14 interdisciplinary subject areas that include computer science, artificial intelligence, engineering, medicine, business, mathematics, natural sciences, economics and the humanities.</p>
      <p>What makes Open Doors unusual is what it does not ask for. There is no application fee, no IELTS or TOEFL requirement to enter the competition, and no entrance examination at the university. Language proficiency is assessed by the admitting university at enrolment, and if your chosen programme is taught only in Russian, the funded one-year preparatory course covers the gap. Selection runs on your portfolio and on subject tasks completed online, with interviews only for the doctoral and postdoctoral tracks.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>foreign citizen or stateless person</strong>, including a compatriot residing abroad. There are no nationality restrictions.</li>
        <li><strong>Bachelor\u2019s track:</strong> aged <strong>16\u201323</strong> on 20 August 2026; hold, or be due to obtain during the relevant academic year, a qualification allowing entry into higher education in your country; and not already hold a Bachelor\u2019s, Specialist or Master\u2019s degree.</li>
        <li><strong>Master\u2019s track:</strong> aged <strong>20\u201333</strong> on 20 August 2026; hold, or be due to obtain, a qualification equivalent to at least a Bachelor\u2019s degree; and not already hold a Specialist or Master\u2019s degree.</li>
        <li><strong>PhD track:</strong> aged <strong>22\u201335</strong> on 20 August 2026; hold, or be due to obtain, a Specialist or Master\u2019s degree; and not have completed a doctoral programme.</li>
        <li><strong>Postdoctoral track:</strong> aged <strong>24\u201339</strong> on 20 August 2026; already hold a <strong>Candidate of Sciences, Doctor of Sciences or PhD</strong> degree.</li>
        <li>Consent to the processing of your personal data under Russian law, as the competition rules require.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition</strong> for the entire degree, funded from the Russian federal budget under the Russian Government education quota.</li>
        <li>A <strong>free one-year Russian preparatory course</strong> for winners entering Russian-taught programmes, with the degree place held.</li>
        <li>A <strong>monthly stipend paid by the host university</strong> — the amount varies by institution and is not published centrally.</li>
        <li>Priority when selecting an eligible degree at participating universities; winners choose up to <strong>six universities</strong> in order of preference.</li>
        <li><strong>Work while studying</strong> is permitted, with no separate work permit required.</li>
        <li>For Postdoctoral winners: a <strong>research position</strong> at an organising university, working with leading scientists.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>motivation letter</strong> for each subject area you apply to (mandatory).</li>
        <li><strong>Proof of education</strong> — degree, transcript or grade sheet (mandatory).</li>
        <li><strong>Language certificates</strong> (IELTS/TOEFL/Russian) — optional, but they boost your portfolio score.</li>
        <li><strong>Achievement and olympiad certificates</strong>, awards, research papers and project records — optional, but they boost your score.</li>
        <li>A <strong>CV and recommendation letters</strong> — optional, but they boost your score.</li>
        <li>Certified translations are <strong>not needed at the first stage</strong>; they are only required later, at a Russian Embassy, Consulate or notary, once you are confirmed as a winner or runner-up.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to <strong>od.globaluni.ru</strong> and create your account before <strong>1 November 2026</strong>.</li>
        <li>Select your <strong>track</strong> (Bachelor\u2019s, Master\u2019s, PhD or Postdoctoral) and <strong>one or more subject areas</strong>.</li>
        <li>Build your <strong>portfolio</strong>: upload proof of education, a motivation letter for each subject, and any optional achievements, certificates and CV.</li>
        <li>Practise with the <strong>sample tasks</strong> for your subject area and check that your computer meets the technical requirements for the online test.</li>
        <li>Choose up to <strong>six universities</strong> in order of preference.</li>
        <li>Submit before <strong>1 November 2026</strong> — after this your account and portfolio are locked. PhD and Postdoctoral candidates who pass the earlier stages are then interviewed by potential supervisors or project leaders.</li>
        <li>If you win, complete the <strong>Education Quota application</strong> in your Open Doors account and upload the required documents.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Open Door Russian Scholarship fully funded?',
  'Tuition is covered in full from the Russian federal budget, and a free Russian preparatory year is included where needed. Travel, accommodation, food, medical insurance and personal expenses are not covered, and the monthly stipend amount varies by university — so treat it as tuition-funded rather than all-expenses-paid.'),
 ('Do I need IELTS to apply?',
  'No. There is no IELTS, TOEFL or PTE requirement to enter the competition, and no entrance examination at the university. Language proficiency is confirmed or assessed by the admitting university at enrolment.'),
 ('What are the age limits?',
  'Bachelor\u2019s 16\u201323, Master\u2019s 20\u201333, PhD 22\u201335, Postdoctoral 24\u201339 — all measured on 20 August 2026, the registration opening date.'),
 ('Can I apply for more than one subject area?',
  'Yes. You may enter as many of the 14 subject areas as you wish, with a motivation letter for each, and you can list up to six universities in order of preference.'),
 ('When are the results announced?',
  'Bachelor\u2019s and Master\u2019s results on 21 December 2026; PhD and Postdoctoral results on 26 February 2027. The first stage continues to 13 November 2026, but only for participants who registered before the 1 November deadline.')]) + '''
      <p class="verify">Verified 25 Oct 2026: opportunitiesnexus.com/open-doors-scholarship-russia-2027/ — registration deadline 1 November 2026, tuition covered in full from the Russian federal budget, monthly stipend paid by host university (amount varies, not published centrally), no IELTS, no fee, 26 participating universities, 14 subject areas, age bands and results dates, facts verified directly from the official Open Doors website on 30 September 2026; admitstudy.com/scholarship/5120ed3d-afe8-4b80-98bf-4875b9aa05cb — registration and portfolio 20 August–1 November 2026, free tuition and free Russian preparation, travel and living costs not covered; daadscholarship.com/russia-open-doors-scholarship-2027-3-stage-application-process-explained-for-bachelors-masters-phd-and-postdoc-admissions/ — age bands 16–23 / 20–33 / 22–35 / 24–39, registration deadline 1 November 2026, first-stage results 13 November 2026, Bachelor\u2019s/Master\u2019s results 21 December 2026, PhD/Postdoc results 26 February 2027; daily-sun.com/bangladesh/903649/open-doors-olympiad-offers-tuition-free-study-opportunities-in-russia — press release from the Russian House in Dhaka, 1 November 2026 deadline, 618,000+ participants since 2017, 16,700+ winners, government grant benefits for Russian-taught winners subject to conditions; scholarhunter.com/open-doors-russian-scholarship-project-2026-27-100-fully-funded/2026/ — required documents table, motivation letter and proof of education mandatory, certified translations only after winning.</p>''',
 dl_long='1 November 2026',
 offlinks=[('Open Doors — Official portal (od.globaluni.ru)', 'https://od.globaluni.ru/'),
           ('Open Doors — Rules of Participation (official)', 'https://od.globaluni.ru/index.php/rules')],
 related_titles=['turkiye2027', 'gks2027', 'xiamen-csc-2027', 'daad'])),

# ---------------------------------------------------------------- 2. Berenson Fellowship
A.append(dict(
 slug='harvard-university-berenson-fellowship-2027-italy',
 title='Harvard University Berenson Fellowship 2027 in Italy (Stipend $5,200)',
 meta='Harvard University Berenson Fellowship 2027: a residential research fellowship at Villa I Tatti in Florence, paying $5,200 a month for 4 or 6 months plus up to $1,800 relocation support. Deadline 16 November 2026 — eligibility, documents, how to apply and FAQs.',
 short='Harvard University Berenson Fellowship 2027', kicker='Italy · Postdoctoral Fellowship · Funded', mono='HB',
 prov_short='Villa I Tatti, Harvard University', prov_cat='Fellowship · Italy',
 h1='Harvard University Berenson Fellowship 2027 in Italy (Stipend $5,200)',
 sub='The Harvard University Berenson Fellowship 2027 offers postdoctoral scholars four or six months of residential research at Villa I Tatti, the Harvard University Center for Italian Renaissance Studies in Florence, Italy. Fellows receive $5,200 a month, a relocation supplement of up to $1,800, and — when available — a rent-free apartment or a housing subsidy, with full access to the Biblioteca Berenson. The fellowship supports research on \u201cItaly in the World\u201d: transnational exchanges between Italy and other cultures during the Renaissance, from the 14th to the 17th century. Applications close on 16 November 2026.',
 dpill='Deadline 16 Nov 2026 · %d days left' % dl_left('2026-11-16'),
 facts=facts([('Award', 'A grant of $5,200 per month for four or six months, plus a one-time relocation supplement of up to $1,800. When available, fellows may also receive a rent-free apartment (utilities remain the fellow\u2019s responsibility) or, if no apartment can be provided, a housing subsidy. Fellows get full access to the Biblioteca Berenson seven days a week, a personal desk or carrel in the library, weekday lunches with the Villa I Tatti scholarly community, and participation in lectures, conferences and concerts. Up to four fellowships are awarded each year.'),
              ('Eligible', 'Scholars of any nationality with a PhD completed at the time of application, researching connections between Italy and other world cultures during the Renaissance (14th\u201317th centuries). Priority goes to early- and mid-career scholars. Applicants must not have previously held a Term Fellowship at I Tatti (prior Graduate Fellows are excluded from this restriction) and must not be working towards a second PhD at the time of application. Conversational English is required, with familiarity with Italian. There is no age limit and no application fee stated on the official fellowship page.'),
              ('How', 'Apply online through the official Villa I Tatti application portal (itatti.slideroom.com), in English or Italian. The application requires a research proposal, a CV, a copy of your PhD certificate, and two academic referees who submit recommendation letters online.'),
              ('Deadline', '16 November 2026, midnight Cambridge, Massachusetts time. The two required recommendation letters must be submitted online by 21 November 2026.'),
              ('Fine print', 'The fellowship is residential: the research must be suitable for completion primarily in Florence, and fellows are expected to work only on the project submitted for the fellowship. The four-month option runs September to December; the six-month option runs January to June.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p><strong>Villa I Tatti</strong>, the Harvard University Center for Italian Renaissance Studies, sits in the hills above Florence in the former home of the art historian Bernard Berenson. The <strong>Berenson Fellowship</strong> is its flagship residential award for scholars outside Harvard who are working on how Renaissance Italy connected with the rest of the world — the theme the centre calls \u201cItaly in the World\u201d. That covers transnational exchanges between Italy and regions such as Africa, Asia, Latin America and the wider Mediterranean, across architecture, art, history, philosophy, literature, music and the history of science.</p>
      <p>The award is deliberately generous in the ways that matter to a researcher: a $5,200 monthly grant, relocation support, a desk in one of the great Renaissance libraries, and daily contact with a small international scholarly community over lunch and in the library. With up to four fellowships a year, it is competitive — but the field is defined by the research theme, not by nationality or discipline.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>PhD at the time of application</strong> and be able to upload proof of the degree.</li>
        <li>Propose a research project on <strong>\u201cItaly in the World\u201d</strong> — transnational exchanges involving Renaissance Italy between the <strong>14th and 17th centuries</strong> — that can be completed primarily in Florence.</li>
        <li>Be open to scholars of <strong>all nationalities</strong>; early- and mid-career scholars are given priority.</li>
        <li><strong>Not have previously held a Term Fellowship at I Tatti</strong> (prior Graduate Fellows are exempt from this restriction).</li>
        <li>Not be working towards a <strong>second PhD</strong> at the time of application.</li>
        <li>Be <strong>conversant in English</strong>, with familiarity with Italian; no IELTS score is specified.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$5,200 per month</strong> for four or six months.</li>
        <li>A one-time <strong>relocation supplement of up to $1,800</strong>.</li>
        <li>A <strong>rent-free apartment when available</strong> (utilities are the fellow\u2019s responsibility), or a <strong>housing subsidy</strong> if university accommodation is unavailable.</li>
        <li>Full access to the <strong>Biblioteca Berenson seven days a week</strong>, with a personal desk or carrel in the library.</li>
        <li><strong>Weekday lunches</strong> with the Villa I Tatti scholarly community and participation in lectures, conferences and concerts.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>research proposal</strong> showing how your project connects Italy with other cultures or regions during the Renaissance.</li>
        <li>An academic <strong>CV</strong>.</li>
        <li>A copy of your <strong>PhD certificate</strong>.</li>
        <li><strong>Two academic referees</strong> who will submit recommendation letters online (by 21 November 2026).</li>
        <li>Details of your <strong>previous research</strong> where the application asks for them.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the fellowship guidelines and eligibility criteria on the official Villa I Tatti fellowship page.</li>
        <li>Prepare your <strong>research proposal and CV</strong>, and have your <strong>PhD certificate</strong> ready to upload.</li>
        <li>Register <strong>two academic referees</strong> in the application system so they can submit recommendation letters.</li>
        <li>Submit the completed application through the official online portal (<strong>itatti.slideroom.com</strong>) in English or Italian before <strong>16 November 2026</strong>, midnight Cambridge, Massachusetts time.</li>
        <li>Make sure your referees submit their letters by <strong>21 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What research does the Berenson Fellowship support?',
  'Research examining \u201cItaly in the World\u201d between the 14th and 17th centuries — transnational exchanges between Italy and regions such as Africa, Asia, Latin America or the wider Mediterranean, in fields from art history and architecture to literature, music and the history of science.'),
 ('How long is the fellowship?',
  'Either 4 months (September to December) or 6 months (January to June), residential at Villa I Tatti in Florence.'),
 ('Do I need to speak Italian?',
  'You need to be conversant in English and have familiarity with Italian; no IELTS score is specified.'),
 ('Can I apply if I have already held a fellowship at I Tatti?',
  'Not if you have previously held a Term Fellowship at I Tatti. Prior Graduate Fellows are exempt from that restriction.'),
 ('What is the difference between the application deadline and the recommendation deadline?',
  'Your application must be submitted by 16 November 2026, midnight Cambridge, Massachusetts time. Your two referees have until 21 November 2026 to submit their letters.')]) + '''
      <p class="verify">Verified 25 Oct 2026: afterschoolafrica.com/120810/berenson-fellowship-2027-2028-at-harvard-universitys-i-tatti-in-florence-italy/ — USD 5,200 per month, up to USD 1,800 relocation, rent-free accommodation when available or housing subsidy, 4 months (September–December) or 6 months (January–June), deadline 16 November 2026, application portal itatti.slideroom.com; universities.nspscholarships.com/harvard-university-berenson-fellowship/ — same figures, PhD required, all nationalities, deadline 16 November 2026 11:59 p.m. Cambridge, MA time, recommendation deadline 16 November 2026; daadscholarship.com/harvard-universitys-berenson-fellowship-2027-2028-5-application-steps/ — USD 5,200/month, up to USD 1,800 relocation, applicant deadline 16 November 2026, recommendation deadline 21 November 2026, official information verified 22 September 2026; opportunitiesfeed.com/2026/09/04/harvard-berenson-fellowship/ — up to 4 awarded each year, rent-free apartment or housing subsidy, all nations, conversant in English and familiarity with Italian, early- and mid-career priority.</p>''',
 dl_long='16 November 2026',
 offlinks=[('Villa I Tatti — Berenson Fellowship application portal (itatti.slideroom.com)', 'https://itatti.slideroom.com/'),
           ('Bright Scholarship — Harvard University Berenson Fellowship 2027', 'https://brightscholarship.com/harvard-university-berenson-fellowship/')],
 related_titles=['harvard-env-2027', 'harvard-lead', 'bloomberg-harvard', 'perugia-phd'])),

# ---------------------------------------------------------------- 3. NVIDIA AMRI
A.append(dict(
 slug='nvidia-amri-research-phd-internship-2027',
 title='NVIDIA AMRI Research PhD Internship 2027 (Funded)',
 meta='NVIDIA AMRI Research PhD Internship 2027: a research internship with NVIDIA Research\u2019s AI-Mediated Reality and Interaction group for current PhD candidates in AI, computer vision and robotics. Apply by email with the subject \u201cSeeking Research Internship 2027\u201d — eligibility, research areas, documents and FAQs.',
 short='NVIDIA AMRI Research PhD Internship 2027', kicker='USA · PhD Internship · Funded', mono='NV',
 prov_short='NVIDIA Research', prov_cat='Corporate · Global',
 h1='NVIDIA AMRI Research PhD Internship 2027 (Funded)',
 sub='The NVIDIA AMRI Research PhD Internship 2027 places current doctoral researchers inside NVIDIA Research\u2019s AI-Mediated Reality and Interaction (AMRI) group, working on interactive embodied AI, human-AI interaction, 4D world modelling and neural rendering alongside NVIDIA scientists and engineers. There is no online application form and no published deadline: interested PhD candidates email the team lead or a specific AMRI team member directly, using the exact subject line \u201cSeeking Research Internship 2027\u201d. The official announcement does not publish a stipend figure, so this article states that plainly rather than quoting a number from another NVIDIA posting.',
 dpill='No deadline published · Apply early',
 facts=facts([('Award', 'A research internship with NVIDIA Research\u2019s AMRI group, with mentorship from NVIDIA scientists and engineers, access to top-tier computational resources, and the chance to publish and patent research in top-tier conferences and to take part in technology transfer into NVIDIA products. The official AMRI announcement does not specify a stipend or salary amount — do not assume a figure from other NVIDIA internship postings; confirm compensation directly with the team during recruitment.'),
              ('Eligible', 'Current PhD candidates in a relevant technical or quantitative field — Computer Science, Computer Engineering, Electrical Engineering, Physics or Mathematics. You need an outstanding research track record, especially publications at top-tier conferences on AI, computer vision and graphics (CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, SIGGRAPH), a solid theoretical and practical understanding of computer vision and artificial intelligence, knowledge of distributed deep learning frameworks (especially PyTorch), outstanding Python and C++ programming skills, familiarity with CUDA for GPU processing, and excellent written and spoken communication skills. Familiarity with computer graphics is a plus, not a requirement.'),
              ('How', 'Email the AMRI team lead or a specific research team member directly, with the exact email subject line \u201cSeeking Research Internship 2027\u201d, and include application materials that showcase your research expertise and publications. Contact the team member whose research interests most closely match your own. (Some aggregator sites quote a different subject line, \u201cLooking for a 2027 Research Internship\u201d — the official NVIDIA Research page uses \u201cSeeking Research Internship 2027\u201d, so use that.)'),
              ('Deadline', 'Not published in the official notification. The AMRI announcement gives no closing date and advises applying as soon as possible; because places are filled by direct contact with the team, check the official NVIDIA Research page and contact the relevant team members for current availability.'),
              ('Fine print', 'This is a research role, not a taught programme: interns are expected to propose novel fundamental research, prototype and test ideas, and publish and patent results. The internship is with the AMRI group specifically — your email should show why your work fits that group\u2019s research areas, not NVIDIA in general.')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p><strong>NVIDIA Research</strong> is the company\u2019s research arm, and the <strong>AI-Mediated Reality and Interaction (AMRI)</strong> group is the team working on how people and intelligent systems meet: embodied AI that acts in the world, interfaces between humans and AI, and models of the world in four dimensions. Interns join that group as researchers, not as trainees — the posting asks them to lead ambitious research initiatives, propose novel fundamental research, prototype and test ideas, and publish and patent the results in top-tier conferences.</p>
      <p>The application route is unusual and worth reading carefully. There is no portal and no form. You identify the AMRI team member whose research is closest to yours, email them directly with a precise subject line, and make the case with your publications and research background. That direct-contact route is also why there is no published deadline: availability depends on the team, so the honest advice is to contact them now rather than wait for a closing date that may never be announced.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be <strong>currently enrolled in a PhD programme</strong> in a relevant technical or quantitative field, such as Computer Science, Computer Engineering, Electrical Engineering, Physics or Mathematics.</li>
        <li>Show an <strong>outstanding track record of academic research</strong>, especially publications at prestigious conferences on AI, computer vision and graphics — CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML and SIGGRAPH are named in the announcement.</li>
        <li>Have a solid theoretical and practical understanding of <strong>computer vision and artificial intelligence</strong>.</li>
        <li>Know <strong>distributed deep learning frameworks</strong>, especially PyTorch.</li>
        <li>Have outstanding <strong>Python and C++</strong> programming skills and familiarity with <strong>CUDA</strong> for GPU processing.</li>
        <li>Have <strong>excellent communication skills</strong>, both written and spoken.</li>
        <li>Familiarity with <strong>computer graphics</strong> is a plus, not a requirement.</li>
      </ul>
      <h2 id="research-areas">Research areas</h2>
      <ul>
        <li><strong>Interactive Embodied AI</strong> and <strong>Human-AI Interaction</strong></li>
        <li><strong>4D World Modeling</strong> and <strong>World Models</strong></li>
        <li><strong>Computer Vision</strong> and <strong>Neural Rendering</strong></li>
        <li><strong>Robotics</strong> and <strong>Human Behavior Understanding</strong></li>
        <li><strong>Artificial Intelligence and Machine Learning</strong> more broadly</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Work directly with <strong>NVIDIA scientists and engineers</strong> on research that feeds NVIDIA\u2019s long-term priorities.</li>
        <li><strong>Publish and patent</strong> your research in top-tier international conferences and journals.</li>
        <li>Take part in <strong>technology transfer</strong> when research advances graduate into NVIDIA products.</li>
        <li>Access to <strong>top-tier computational resources</strong> and a collaborative environment that values scientific rigour.</li>
        <li>Guidance and autonomy: the posting describes the internship as fostering <strong>independent thinking</strong> while offering mentorship.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>CV</strong> that clearly highlights your PhD programme, research interests, publications, conference papers and research projects.</li>
        <li>A <strong>publication list</strong> emphasising top-tier venues (CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, SIGGRAPH).</li>
        <li>A short account of your <strong>research background</strong> and why it aligns with the AMRI group\u2019s work.</li>
        <li>Evidence of your <strong>programming and deep-learning skills</strong> (PyTorch, Python, C++, CUDA).</li>
        <li>Any <strong>research materials</strong> that showcase your expertise — the announcement asks for materials highlighting research experience and publications.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official AMRI internship page on <strong>research.nvidia.com</strong> and pick the <strong>team member whose research interests most closely match your own</strong>.</li>
        <li>Prepare your <strong>CV and research materials</strong> so they demonstrate your publication record and your fit with that person\u2019s work.</li>
        <li><strong>Email the team lead or that specific team member directly</strong>, using the exact subject line <strong>\u201cSeeking Research Internship 2027\u201d</strong>.</li>
        <li>In the email, explain clearly <strong>why your research fits the AMRI group</strong> and what you would work on.</li>
        <li>Apply <strong>as soon as possible</strong> — there is no published deadline, and places depend on the team\u2019s availability.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the exact email subject line for the NVIDIA AMRI internship?',
  'The official NVIDIA Research page says to use the subject \u201cSeeking Research Internship 2027\u201d. Some aggregator sites quote \u201cLooking for a 2027 Research Internship\u201d instead — use the official wording, since that is what the team expects.'),
 ('Is there an application deadline?',
  'No. The official announcement does not specify a deadline and advises applying as soon as possible. Contact the AMRI team to confirm current availability.'),
 ('How much does the internship pay?',
  'The official AMRI announcement does not specify a stipend or salary amount, so this article does not quote one. Figures circulating online for other NVIDIA internship postings are not the AMRI figure — confirm compensation with the team during recruitment.'),
 ('Do I apply through a portal?',
  'No. You email the AMRI team lead or a specific team member directly. There is no online application form for this posting.'),
 ('What publications help most?',
  'Publications at top-tier conferences on AI, computer vision and graphics — the announcement names CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML and SIGGRAPH. A proven record of high-impact research greatly strengthens an application.')]) + '''
      <p class="verify">Verified 25 Oct 2026: research.nvidia.com/labs/amri/post/internships_for_summer_2027/ (official NVIDIA Research page) — pursuing a PhD in CS, CE, EE, Physics or Maths; outstanding publication record at CVPR, ICCV, ECCV, NeurIPS, ICLR, ICML, SIGGRAPH; proficiency in AI and computer vision, PyTorch, Python, C++, CUDA; email the team lead or specific team members with the subject \u201cSeeking Research Internship 2027\u201d; brightscholarship.com/nvidia-amri-research-phd-internship/ — same research areas and eligibility, deadline not specified, apply as soon as possible, quotes the subject line as \u201cLooking for a 2027 Research Internship\u201d (aggregator wording; the official page\u2019s \u201cSeeking Research Internship 2027\u201d is used in this article); careerglobalconnect.com/2026/08/31/research-internship/ — announcement does not specify a stipend or a deadline, contact the team for current availability; scholarshipunion.com/nvidia-amri-internship-2027/ — same, official announcement states the last date is not specified.</p>''',
 dl_long='Not published in the official notification — apply as soon as possible',
 offlinks=[('NVIDIA Research — AMRI Research Intern 2027 (official)', 'http://research.nvidia.com/labs/amri/post/internships_for_summer_2027/'),
           ('Bright Scholarship — NVIDIA AMRI Research PhD Internship 2027', 'https://brightscholarship.com/nvidia-amri-research-phd-internship/')],
 related_titles=['nvidia-2027', 'msrp-2027', 'epfl-summer', 'ustc-2027'])),

# ---------------------------------------------------------------- 4. Jean Monnet
A.append(dict(
 slug='eu-jean-monnet-scholarship-2027-2028',
 title='170 EU Jean Monnet Scholarship 2027\u20132028 for International Students (Fully Funded)',
 meta='EU Jean Monnet Scholarship 2027-2028: around 170 EU-funded scholarships for people working or studying in T\u00fcrkiye to pursue postgraduate study in an EU member state — tuition up to \u20ac22,000 plus a \u20ac3,500 allowance. Deadline 27 October 2026, sealed-envelope submission — eligibility, documents, how to apply and FAQs.',
 short='EU Jean Monnet Scholarship 2027\u20132028', kicker='Europe · Master\u2019s · Funded', mono='JM',
 prov_short='Jean Monnet Scholarship Programme', prov_cat='European Union · T\u00fcrkiye',
 h1='170 EU Jean Monnet Scholarship 2027\u20132028 for International Students (Fully Funded)',
 sub='The EU Jean Monnet Scholarship 2027\u20132028 will fund around 170 people to specialise in fields related to the EU acquis at a university in an EU member state, with tuition of up to \u20ac22,000, a country-specific living allowance and a fixed \u20ac3,500 payment for other expenses. Applications close on 27 October 2026 — and this is not an online form: applications must arrive in a sealed envelope at the Central Finance and Contracts Unit in Ankara. One correction matters before you read further: despite the \u201cfor International Students\u201d label in the title, this programme is for people working or studying in T\u00fcrkiye. It is not open to applicants worldwide.',
 dpill='Deadline 27 Oct 2026 · %d days left' % dl_left('2026-10-27'),
 facts=facts([('Award', 'Tuition fees up to \u20ac22,000; living expenses based on the approved rate for the destination EU country; and a fixed \u20ac3,500 one-time allowance for expenses such as travel, visa and passport costs, insurance, educational materials and registration. Programmes charging more than \u20ac22,000 in tuition are not automatically topped up — the scholarship does not absorb the excess. Around 170 scholarships are planned for the 2027\u20132028 academic year, subject to the final budget allocation and the quality of applications.'),
              ('Eligible', 'The programme is open to people working or studying in T\u00fcrkiye who wish to specialise in areas related to the EU acquis: (1) public sector employees working in T\u00fcrkiye, including staff of professional organisations, chambers, local governments, development agencies and public banks; (2) private sector employees working in T\u00fcrkiye, including staff of NGOs and resident diplomatic missions; (3) academic or administrative staff working at universities in T\u00fcrkiye; and (4) final-year undergraduate students and postgraduate (Master\u2019s or PhD) students studying in T\u00fcrkiye. The proposed programme must be in-person study at a university or equivalent institution in an EU member state — fully online or distance-learning programmes are not eligible.'),
              ('How', 'Submit a physical application in a sealed envelope by mail, courier or in person to the Central Finance and Contracts Unit (Merkezi Finans ve \u0130hale Birimi) in Ankara. Email applications are not accepted. After submission there is an administrative eligibility review and a written examination, followed by the placement and approval process.'),
              ('Deadline', '27 October 2026. Applications opened on 27 August 2026 and must reach the Central Finance and Contracts Unit by the deadline; late submissions are not accepted.'),
              ('Fine print', 'This is a scholarship competition, not a university admission: passing the written examination is followed by a separate placement and approval process, so do not treat a scholarship award as an admission offer. The exact coverage amounts for the current year are set in the official Announcement Document on jeanmonnet.org.tr — confirm the figures there before applying. The programme exists to build T\u00fcrkiye\u2019s administrative capacity in EU acquis fields, in line with the country\u2019s EU membership objective.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Jean Monnet Scholarship Programme (JMSP)</strong> is one of T\u00fcrkiye\u2019s most prestigious EU-funded scholarship schemes, run with the <strong>European Union</strong> and administered through the <strong>Central Finance and Contracts Unit</strong> in Ankara. Its purpose is specific: to increase the number of experts in fields related to the <strong>EU acquis</strong> — the body of EU law and policy — and so contribute to T\u00fcrkiye\u2019s administrative capacity-building in line with its objective of full EU membership.</p>
      <p>For the <strong>2027\u20132028 academic year</strong> the programme plans to award scholarships to approximately <strong>170 people</strong>. The funding is broad — tuition up to \u20ac22,000, a living allowance set by destination country, and a fixed \u20ac3,500 for other costs — but the eligibility is narrow in a way many listings get wrong: it is for people who work or study in T\u00fcrkiye, in the public sector, the private sector, universities, or as students. If you are not based in T\u00fcrkiye, this is not your scholarship, however the title reads.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be working or studying in <strong>T\u00fcrkiye</strong> in one of four categories:
          <ul>
            <li><strong>Public sector employees</strong> — including staff of professional organisations, chambers, local governments (municipalities and special provincial administrations), development agencies, and public development and investment banks.</li>
            <li><strong>Private sector employees</strong> — including staff of NGOs, resident diplomatic missions and private companies in relevant fields.</li>
            <li><strong>Academic or administrative staff</strong> working at universities in T\u00fcrkiye.</li>
            <li><strong>Students</strong> — final-year undergraduate students, and Master\u2019s or PhD students, studying in T\u00fcrkiye.</li>
          </ul>
        </li>
        <li>Wish to specialise in a field related to the <strong>EU acquis</strong>, such as EU law and institutions, economics and competition, environment and climate, transport, agriculture, energy, migration and justice, public administration, employment and social policy, or digital and regulatory policy.</li>
        <li>Plan <strong>in-person study</strong> at a university or equivalent institution in an <strong>EU member state</strong>. Fully online or distance-learning programmes are not eligible.</li>
        <li>Meet the requirements of the current year\u2019s <strong>official Announcement Document</strong> on jeanmonnet.org.tr for your category — the required documents vary by sector.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition fees up to \u20ac22,000</strong>.</li>
        <li><strong>Living expenses</strong> based on the approved rate for the destination EU country.</li>
        <li>A fixed <strong>\u20ac3,500 one-time allowance</strong> for travel, visa and passport costs, insurance, educational materials, registration and related costs.</li>
        <li>The opportunity to study in an <strong>EU member state</strong> and build an international professional network in European policy, law and institutions.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>application form and documents listed in the official Announcement Document</strong> for your category (public sector, private sector, academic/administrative staff, or student) — the list varies, so check jeanmonnet.org.tr for your specific category.</li>
        <li>Evidence of your <strong>employment or enrolment in T\u00fcrkiye</strong> (employer letter, university enrolment or staff certificate as applicable).</li>
        <li><strong>Academic records</strong> and any language evidence your proposed programme requires.</li>
        <li>A <strong>sealed envelope</strong> addressed as the Announcement Document specifies, marked with the subject \u201cJean Monnet Scholarship Programme \u2013 2027\u20132028 Academic Year\u201d.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the <strong>official Announcement Document</strong> for the 2027\u20132028 academic year on <strong>jeanmonnet.org.tr</strong> and confirm the document list for your category.</li>
        <li>Prepare your application and place it in a <strong>sealed envelope</strong> marked \u201cJean Monnet Scholarship Programme \u2013 2027\u20132028 Academic Year\u201d.</li>
        <li>Send it by <strong>mail or courier, or deliver it in person</strong>, to:<br>
          Merkezi Finans ve \u0130hale Birimi<br>
          Gelir \u0130daresi Ba\u015fkanl\u0131\u011f\u0131 E\u011fitim Merkezi ve OECD Ankara \u00c7ok Tarafl\u0131 Vergi Merkezi<br>
          25 Mart Mahallesi, \u0130stiklal Caddesi No: 7, Yenimahalle, 06200 Ankara / T\u00fcrkiye</li>
        <li>Make sure it <strong>arrives by 27 October 2026</strong>. Late submissions are not accepted, and <strong>email applications are not accepted</strong>.</li>
        <li>After submission, the process runs through an <strong>administrative eligibility review</strong> and a <strong>written examination</strong>, followed by placement and approval requirements.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can anyone in the world apply for the Jean Monnet Scholarship?',
  'No. The programme is for people working or studying in T\u00fcrkiye — public and private sector employees, university staff, and final-year or postgraduate students there. Listings that say \u201call nationalities\u201d are wrong for this scheme.'),
 ('Can I apply by email?',
  'No. Applications must be submitted in a sealed envelope by mail, courier or in person to the Central Finance and Contracts Unit in Ankara. Email applications are not accepted.'),
 ('What can I study?',
  'A postgraduate programme related to the EU acquis — EU law and institutions, economics, environment, transport, agriculture, energy, migration and justice, public administration, digital policy and similar fields — in person at a university in an EU member state. Online or distance programmes are not eligible.'),
 ('Does the scholarship cover all tuition?',
  'Tuition is covered up to \u20ac22,000, plus a country-specific living allowance and a fixed \u20ac3,500 payment. If your programme charges more than \u20ac22,000 in tuition, the excess is not automatically covered.'),
 ('What happens after I submit?',
  'An administrative eligibility review and a written examination, after which successful candidates go through the programme\u2019s placement and approval requirements. The scholarship competition and the university admission are separate processes.')]) + '''
      <p class="verify">Verified 25 Oct 2026: eeas.europa.eu/delegations/turkiye/applications-jean-monnet-scholarship-programme-2027-2028-academic-year-started_en (EU Delegation to T\u00fcrkiye, official) — applications open for 2027–2028, application deadline 27 October 2026, approximately 170 scholarships planned, open to public sector employees, private sector employees, academic/administrative university staff and students in T\u00fcrkiye; jeanmonnet.org.tr/en/applications-for-the-2027-2028-academic-year-jean-monnet-scholarships-started (official programme site) — applications started 27 August 2026, deadline 27 October 2026, same 170 figure and eligibility categories; daadscholarship.com/eu-opens-jean-monnet-scholarship-2027-2028-170-seats-to-study-for-free-in-europe/ — tuition up to \u20ac22,000, country-specific living allowance, fixed \u20ac3,500 allowance, sealed-envelope physical submission, written examination and placement process, online programmes not eligible; jobs.iammagnus.com/jean-monnet-scholarship-programme-2027-2028-fully-eu-funded-masters-in-europe-for-turkish-professionals-and-students-deadline-27-october-2026/ — CFCU Ankara postal address, subject line, documents vary by category, email applications not accepted.</p>''',
 dl_long='27 October 2026',
 offlinks=[('Jean Monnet Scholarship Programme — 2027–2028 applications (official)', 'https://jeanmonnet.org.tr/en/applications-for-the-2027-2028-academic-year-jean-monnet-scholarships-started'),
           ('EU Delegation to T\u00fcrkiye — Jean Monnet 2027–2028 call (official)', 'https://www.eeas.europa.eu/delegations/turkiye/applications-jean-monnet-scholarship-programme-2027-2028-academic-year-started_en?s=230')],
 related_titles=['turkiye2027', 'sabanci', 'emabg', 'daad'])),

# ---------------------------------------------------------------- 5. Dartmouth DAAD
A.append(dict(
 slug='dartmouth-college-daad-master-scholarship-2027-germany',
 title='Dartmouth College DAAD Master Scholarship 2027 in Germany for International Students',
 meta='Dartmouth College DAAD Master Scholarship 2027: the DAAD Study Scholarship for Master\u2019s study in Germany, accessed through Dartmouth College\u2019s Fellowships Office endorsement — \u20ac992 a month for 10–24 months. DAAD portal deadline 30 October 2026 — eligibility, documents, how to apply and FAQs.',
 short='Dartmouth College DAAD Master Scholarship 2027', kicker='Germany · Master\u2019s · Funded', mono='DD',
 prov_short='DAAD (via Dartmouth College)', prov_cat='Exchange Service · Germany',
 h1='Dartmouth College DAAD Master Scholarship 2027 in Germany for International Students',
 sub='The Dartmouth College DAAD Master Scholarship 2027 is the German Academic Exchange Service (DAAD) Study Scholarship for Master\u2019s study in Germany, reached through Dartmouth College\u2019s Fellowships Office, which advises candidates and provides the institutional endorsement. It is a DAAD award, not a Dartmouth-funded scholarship. The standard DAAD rate for Master\u2019s students is \u20ac992 a month for 10 to 24 months, with insurance, travel and study allowances on top, and funding starts around October 2027. The DAAD portal deadline is 30 October 2026 — but Dartmouth\u2019s internal endorsement cutoff falls in early October 2026, so candidates should check with the Fellowships Office immediately whether late endorsement is still possible.',
 dpill='Deadline 30 Oct 2026 · %d days left' % dl_left('2026-10-30'),
 facts=facts([('Award', 'The standard DAAD Study Scholarship package for Master\u2019s students: a monthly stipend of \u20ac992; payments towards health, accident and personal liability insurance; a travel allowance (on application); an annual study allowance of \u20ac460; and coverage of the semester contribution fee (\u20ac150\u2013\u20ac350 per semester), since most German public universities charge no tuition fees for international students. A monthly rent subsidy and a monthly allowance for accompanying family members may be available under certain circumstances after funding starts. Funding lasts 10 to 24 months depending on the chosen Master\u2019s programme, awarded for the standard period of study up to a maximum of 24 months.'),
              ('Eligible', 'For the Dartmouth-supported route: eligible current Dartmouth seniors and recent alumni with a clear academic project that makes study in Germany essential, who go through the College\u2019s fellowship process and receive institutional endorsement. DAAD New York allows US and Canadian citizens or permanent residents, as well as certain foreign nationals studying in the United States or Canada, to apply under its regional rules — international Dartmouth students should verify their individual eligibility with DAAD New York rather than assuming Dartmouth enrolment alone is sufficient. General DAAD rules for this scholarship: your first degree (Bachelor\u2019s or equivalent) must be completed by the time funding begins in October 2027; as a rule your most recent university degree should not date back more than 6 years at the application deadline; you must not have been resident in Germany for longer than 15 months at the deadline; and your Bachelor\u2019s average grade must be at least 90 per cent or equivalent. Funding is not possible for a Master\u2019s programme that has already begun in Germany, and only for programmes starting in the winter semester of the following year.'),
              ('How', 'Consult the Dartmouth Fellowships Office and secure institutional endorsement; research Master\u2019s programmes at state-recognised German universities and build contact with a potential host institution (preference can be given to applicants who have secured admission or can demonstrate meaningful contact); register on the DAAD portal (portal.daad.de) and upload the required documents; submit by the DAAD deadline; and apply separately to your target German universities for course admission.'),
              ('Deadline', 'DAAD portal deadline: 30 October 2026 (midnight CET). Dartmouth\u2019s internal campus cutoff for endorsement falls in early October 2026 — if that has passed, contact the Fellowships Office at once to ask whether late endorsement is possible. Selection takes place in January–February 2027, with award notifications in March–April 2027 and funding starting around 1 October 2027.'),
              ('Fine print', 'This is not a Dartmouth-funded scholarship: it is a DAAD award administered through the German Academic Exchange Service, with Dartmouth providing campus-level advising, endorsement and nomination support. German language is not necessarily required for English-taught programmes, but you must meet the language requirements of your chosen German university. Preference can be given to applicants who have already secured admission to a German institution or can demonstrate meaningful contact with one.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DAAD Study Scholarship for Master Studies in All Academic Disciplines</strong> is the German Academic Exchange Service\u2019s main route for highly qualified graduates to take a full Master\u2019s degree in Germany. <strong>Dartmouth College</strong> supports its own students and recent alumni through that route: the College\u2019s <strong>Fellowships Office</strong> advises candidates, runs an internal nomination process and provides the institutional endorsement that the Dartmouth-supported application carries.</p>
      <p>Two things about the structure are easy to get wrong. First, the money comes from DAAD, not from Dartmouth — the standard DAAD Master\u2019s package is \u20ac992 a month plus insurance, travel and study allowances, for 10 to 24 months. Second, there are two deadlines, not one: the DAAD portal closes on <strong>30 October 2026</strong>, but Dartmouth\u2019s internal endorsement cutoff falls in <strong>early October 2026</strong>. A strong application that misses the campus cutoff cannot go forward through the Dartmouth route, which is why the first step in this article is to contact the Fellowships Office, not the DAAD portal.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>For the Dartmouth-supported route: be an <strong>eligible current Dartmouth senior or recent alumnus</strong>, and go through the College\u2019s fellowship process to receive <strong>institutional endorsement</strong>.</li>
        <li>Have a <strong>clear academic project that makes study in Germany essential</strong> — the scholarship is for students who can explain what they want to study, why Germany matters for that objective, why the selected programme fits their preparation, and how the degree serves their longer-term plan.</li>
        <li>Have completed a <strong>first degree (Bachelor\u2019s or equivalent) recognised in Germany</strong> by the time funding begins in October 2027.</li>
        <li>As a rule, your most recent university degree should <strong>not date back more than 6 years</strong> at the application deadline.</li>
        <li>Not have been <strong>resident in Germany for longer than 15 months</strong> at the application deadline.</li>
        <li>Hold a Bachelor\u2019s average grade of <strong>at least 90 per cent or equivalent</strong> (above-average academic performance).</li>
        <li>Not be seeking funding for a Master\u2019s programme that has <strong>already begun in Germany</strong>; funding is only for programmes starting in the winter semester of the following year.</li>
        <li>International Dartmouth students: <strong>verify your individual eligibility with DAAD New York</strong> — DAAD\u2019s US/Canada regional rules cover US and Canadian citizens or permanent residents and certain foreign nationals studying in the US or Canada, subject to residence and degree conditions.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac992 per month</strong> for Master\u2019s students (standard DAAD rate).</li>
        <li>Payments towards <strong>health, accident and personal liability insurance</strong> cover.</li>
        <li><strong>Travel allowance</strong> on application.</li>
        <li>An annual <strong>study allowance of \u20ac460</strong>.</li>
        <li>Coverage of the <strong>semester contribution fee</strong> (\u20ac150\u2013\u20ac350 per semester).</li>
        <li>A <strong>monthly rent subsidy</strong> under certain circumstances, after funding starts.</li>
        <li>A <strong>monthly allowance for accompanying family members</strong> under certain circumstances, after funding starts.</li>
        <li>Funding for <strong>10 to 24 months</strong>, for the standard period of study up to a maximum of 24 months.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An academic <strong>CV</strong>.</li>
        <li>A <strong>letter of motivation</strong> explaining what you want to study, why Germany is essential, and how the degree fits your longer-term plan.</li>
        <li>A <strong>research or study plan</strong> for the proposed Master\u2019s programme.</li>
        <li>Academic <strong>transcripts</strong> and degree certificates.</li>
        <li><strong>Recommendation letters</strong> as required by DAAD and Dartmouth\u2019s nomination process.</li>
        <li>Evidence of the <strong>language skills</strong> your chosen German university requires (not necessarily German for English-taught programmes).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Contact the Dartmouth Fellowships Office immediately</strong> and ask whether endorsement is still possible — the internal campus cutoff falls in early October 2026.</li>
        <li>Research <strong>Master\u2019s programmes at state-recognised German universities</strong> and build contact with a potential host institution; preference can be given to applicants who have secured admission or can demonstrate meaningful contact.</li>
        <li>Register a user account on the official DAAD portal at <strong>portal.daad.de</strong> (the portal opened in June 2026).</li>
        <li>Complete the online application form, select your target programmes, and upload all required documents as PDFs.</li>
        <li>Submit the completed DAAD application by <strong>30 October 2026</strong> (the portal closes at midnight CET).</li>
        <li>Apply <strong>separately to your target German universities</strong> for course admission.</li>
        <li>Selection takes place in <strong>January–February 2027</strong>; award notifications follow in <strong>March–April 2027</strong>; funding starts around <strong>1 October 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this a Dartmouth-funded scholarship?',
  'No. It is a DAAD award administered through the German Academic Exchange Service. Dartmouth provides campus-level advising, endorsement and nomination support through its Fellowships Office.'),
 ('What is the deadline?',
  'The DAAD portal deadline is 30 October 2026, midnight CET. Dartmouth\u2019s internal endorsement cutoff falls in early October 2026, so check with the Fellowships Office at once whether late endorsement is still possible.'),
 ('Can international Dartmouth students apply?',
  'Potentially, yes. DAAD New York allows US and Canadian citizens or permanent residents and certain foreign nationals studying in the United States or Canada under its regional rules. International Dartmouth students should verify their individual eligibility with DAAD New York rather than assuming Dartmouth enrolment alone is sufficient.'),
 ('Do I need to speak German?',
  'Not necessarily for English-taught programmes. You must meet the language requirements of your chosen German university, whatever they are.'),
 ('How much does the DAAD scholarship pay?',
  'The standard DAAD rate for Master\u2019s students is \u20ac992 a month, plus insurance payments, a travel allowance, a \u20ac460 annual study allowance and semester-contribution coverage, for 10 to 24 months.')]) + '''
      <p class="verify">Verified 25 Oct 2026: daadscholarship.com/dartmouth-college-opens-daad-master-scholarships-in-germany-to-study-for-free/ — DAAD deadline 30 October 2026, funding start around October 2027, up to 2 years, Dartmouth endorsement required for the Dartmouth-supported route, eligible current seniors and recent alumni, not a Dartmouth-funded scholarship, DAAD New York regional rules for international students; universities.nspscholarships.com/dartmouth-college-daad-master-scholarship-2027-in-germany-for-international-students/ — DAAD portal deadline 30 October 2026 midnight CET, Dartmouth campus internal cutoff early October 2026, selection January–February 2027, notifications March–April 2027, funding start 1 October 2027, register on portal.daad.de, apply separately to German universities; scholarshipunion.com/daad-master-scholarship-2027-germany/ — deadline 30 October 2026, funding 10–24 months, CV, motivation letter, research plan, transcripts and recommendation letters; jolsaconsulting.com/scholarship-daad-scholarship-2027-germany-masters.html — standard DAAD Study Scholarship terms: \u20ac992/month for Master\u2019s students, insurance payments, travel allowance, \u20ac460 annual study allowance, semester contribution \u20ac150–350, rent subsidy and family allowance under certain circumstances, degree not more than 6 years old, not resident in Germany longer than 15 months, 90% average grade, funding only for programmes starting in the winter semester of the following year.</p>''',
 dl_long='30 October 2026 (DAAD portal deadline; Dartmouth internal endorsement cutoff early October 2026)',
 offlinks=[('DAAD — Application portal (portal.daad.de)', 'https://portal.daad.de/'),
           ('Bright Scholarship — Dartmouth College DAAD Master Scholarship 2027', 'https://brightscholarship.com/dartmouth-college-daad-master-scholarship/')],
 related_titles=['daad', 'daad-pg-2026', 'erfurt-phd', 'vechta-phd-2027'])),

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
    json.dump(sizes, open('/tmp/batch47_built.json','w'))

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

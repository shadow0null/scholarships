#!/usr/bin/env python3
"""Batch 45 (cron run 45, 24 Oct 2026): 5 new verified articles.

Queue scan order (next 5 not in done/skipped, file order):
1. Robert Gordon University Vice Chancellors Scholarship 2027 in Scotland
   (Funded) — VERIFIED: full first-year tuition only (not cash, not living
   costs) for international/EU undergraduates, September 2027 intake;
   applications open in the New Year, deadline June 2027 (exact closing day
   not published in the official notification checked). Sources:
   daadscholarship.com, mastersportal.com, youapply.com, collegedunia.com.
2. List of Scotland Scholarships 2027 — SKIPPED: listicle, not a scheme
   (same precedent as earlier listicle skips).
3. USTC Research Internship Program 2027 in China (Fully Funded) — VERIFIED:
   official USTC fellowship page (ic.ustc.edu.cn): Level A = tuition waiver
   + insurance + dormitory + RMB 2,500/3,000/3,500 stipend; Fall Level A
   window 1 Jan-31 Mar 2027; Spring window closed 30 Sep 2026.
4. Peking University Yenching Academy Scholarship 2027 — VERIFIED: 2-year
   MA in China Studies, ~120 scholars, first-year fellowship covers tuition,
   accommodation, stipend, round-trip travel, insurance, research costs;
   deadline 30 Nov 2026, 9:00 am Beijing time. Sources: leapkite.com,
   scholarpositions.com, opportunitiesforyouth.org, scholarshipsedge.com.
5. Kennedy-Lugar YES Scholarship 2027 — SKIPPED: Spring 2027 deadlines
   passed (15 Sep 2026 most countries; Bangladesh 23 Sep 2026).
6. LMU SIST Doctoral Scholarships 2027 — SKIPPED: deadline 22 Oct 2026
   passed (closed 2 days before this run).
7. Harvard Environmental Fellowship Program 2027 — VERIFIED (official):
   environment.harvard.edu programme requirements + Harvard academic
   positions posting: $92,000/year, 2 years, ~5 fellowships, deadline
   1 Dec 2026 5pm ET, host/rec letters 11 Dec 2026.
8. University of Potsdam Scholarships 2027 — VERIFIED: University
   Scholarship Potsdam within Deutschlandstipendium, EUR 300/month;
   2026/27 window was 1-22 Jul 2026 (closed); next window opens 1 Jul 2027,
   closing date not yet published. Sources: uni-potsdam.de official
   application page + 2026/27 call PDF, medjouel.com, collegedunia.com.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 24)
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
 'rgu-vc-2027': {'mono': 'RG', 'title': 'Robert Gordon University Vice Chancellors Scholarship 2027 in Scotland (Funded)',
   'href': 'robert-gordon-university-vice-chancellors-scholarship-2027-scotland.html',
   'dpill': 'Deadline Jun 2027 · opens in the New Year',
   'award': 'Full first-year tuition fee for an eligible undergraduate degree (not cash, not living costs); value equals your programme fee.',
   'elig': 'International or European fee-paying, self-funded offer-holders for full-time on-campus undergraduate study, Year 1 or direct Year 2, September intake.',
   'tags': [('Undergraduate', 'blue'), ('Scotland', 'teal')]},
 'ustc-2027': {'mono': 'UT', 'title': 'USTC Research Internship Program 2027 in China (Fully Funded)',
   'href': 'ustc-research-internship-program-2027-china.html',
   'dpill': 'Fall Level A: 31 Mar 2027 · %d days left' % dl_left('2027-03-31'),
   'award': 'Level A: tuition waiver + medical insurance + free dormitory + monthly stipend RMB 2,500 (bachelor) / 3,000 (master) / 3,500 (PhD).',
   'elig': 'Non-Chinese citizens aged 18–40, full-time Year 3/4 undergraduates or master/PhD students, with a USTC professor pre-acceptance.',
   'tags': [('Research Internship', 'purple'), ('China', 'teal')]},
 'yenching-2027': {'mono': 'YA', 'title': 'Peking University Yenching Academy Scholarship 2027 in China (Fully Funded)',
   'href': 'peking-university-yenching-academy-scholarship-2027-china.html',
   'dpill': 'Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
   'award': 'First-year Yenching Fellowship: full tuition, accommodation, monthly stipend, one round-trip travel allowance, insurance, research costs.',
   'elig': 'Bachelor degree in any field (or graduating by August 2027); outstanding record; IELTS 7.0 / TOEFL iBT 100; leadership and community engagement.',
   'tags': [('Master’s', 'blue'), ('China', 'teal')]},
 'harvard-env-2027': {'mono': 'HE', 'title': 'Harvard Environmental Fellowship Program 2027 (Fully Funded)',
   'href': 'harvard-environmental-fellows-program-2027-usa.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': '$92,000 annual salary for two years + employee health insurance eligibility, up to $2,500 relocation, $2,500/year professional allowance.',
   'elig': 'Doctorate or comparable terminal degree awarded May 2023–August 2027, any discipline, with a committed Harvard faculty host.',
   'tags': [('Postdoc & research', 'purple'), ('USA', 'teal')]},
 'potsdam-2027': {'mono': 'UP', 'title': 'University of Potsdam Scholarships 2027 in Germany (Stipend €300 per month)',
   'href': 'university-of-potsdam-scholarships-2027-germany.html',
   'dpill': 'Next window opens 1 Jul 2027',
   'award': '€300 per month through the Deutschlandstipendium (half federal funds, half private sponsors) for the scholarship period in the call.',
   'elig': 'Enrolled Potsdam bachelor/master students within the standard period of study (or about to begin with admission documents); all nationalities.',
   'tags': [('Bachelor’s & Master’s', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. RGU
A.append(dict(
 slug='robert-gordon-university-vice-chancellors-scholarship-2027-scotland',
 title='Robert Gordon University Vice Chancellors Scholarship 2027 in Scotland (Funded)',
 meta='Robert Gordon University Vice Chancellors Scholarship 2027: full first-year tuition for international and EU undergraduates starting September 2027 in Aberdeen, Scotland. Deadline June 2027, eligibility, documents, how to apply and FAQs.',
 short='Robert Gordon University Vice Chancellors Scholarship 2027', kicker='Scotland · Undergraduate · Funded', mono='RG',
 prov_short='Robert Gordon University', prov_cat='University · Scotland',
 h1='Robert Gordon University Vice Chancellors Scholarship 2027 in Scotland (Funded)',
 sub='The Robert Gordon University Vice-Chancellor’s Undergraduate Scholarship covers the entire first-year tuition fee for one eligible international or EU undergraduate student starting in September 2027 in Aberdeen — it is a fee waiver, not cash, and it does not pay for housing or living costs. Applications for the September 2027 round open in the New Year, with a June 2027 deadline.',
 dpill='Deadline Jun 2027 · opens in the New Year',
 facts=facts([('Award', 'The full first-year tuition fee for your chosen eligible undergraduate programme at Robert Gordon University (RGU), Aberdeen. The cash value therefore equals that programme’s first-year international fee — secondary summaries place typical first-year international fees at roughly £15,910–£18,760, but confirm your own programme’s fee on rgu.ac.uk. It is not a stipend: accommodation, living costs, travel and visa fees are not covered.'),
              ('Eligible', 'International or European fee-paying students who are self-funding, hold an offer for a full-time, on-campus undergraduate course at RGU, and are entering Year 1 or directly entering Year 2 for the September intake. You must have met all offer conditions except the tuition deposit by the scholarship deadline, and you must be willing to take part in university activities and act as an ambassador for RGU. Selection is on academic merit, community engagement and extra-curricular activity.'),
              ('How', 'Apply for an eligible RGU undergraduate course first and secure your offer, then submit the separate Vice-Chancellor’s Undergraduate Scholarship application once the September 2027 window opens in the New Year — the deadline month is June 2027.'),
              ('Deadline', 'June 2027 (September 2027 intake). Applications open in the New Year. The exact closing day was not published in the official notification checked — one secondary summary lists 30 June 2027, so treat June 2027 as the deadline and confirm the exact day on rgu.ac.uk when the window opens.'),
              ('Fine print', 'RGU applies only one university scholarship, financial award or discount per offer — normally the most beneficial one for you. January fast-track students become eligible for this scholarship when they begin their second year in September of the same year; January-start shorter-programme students are not eligible.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Robert Gordon University (RGU)</strong> sits on a riverside campus in Garthdee, Aberdeen, and is known for industry-linked degrees built with employers. Its flagship undergraduate award for overseas students is the <strong>Vice-Chancellor’s Undergraduate Scholarship</strong>: a merit-based fee waiver that pays the whole first-year tuition bill for an eligible international or EU undergraduate.</p>
      <p>The single most important thing to understand is what the award is not. It is not a living-cost grant, not a cash payment, and not funding for the whole degree. If your programme’s first-year international fee is covered, years two, three and four — plus rent, food, travel and visa costs — remain yours to fund. Used with that understanding, it is still a very large saving: a full year of tuition at a UK university, awarded on merit.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold an offer from RGU for a <strong>full-time, on-campus undergraduate course</strong>.</li>
        <li>Be classed by the university as an <strong>international or European fee payer</strong>.</li>
        <li>Be a <strong>self-funding</strong> student (externally sponsored students are excluded from RGU scholarships and awards).</li>
        <li>Be entering <strong>Year 1, or directly entering Year 2</strong>, for the <strong>September intake</strong>.</li>
        <li>Have met <strong>all offer conditions except the tuition deposit</strong> by the scholarship deadline.</li>
        <li>Be willing to engage in extra-curricular activities and <strong>act as an ambassador</strong> for RGU, promoting the value of studying there.</li>
        <li>Selection is based on <strong>academic merit, community engagement and extra-curricular activities</strong> — not on financial need.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full first-year tuition fee</strong> for any eligible undergraduate degree — the value follows your programme’s fee.</li>
        <li>Applied on enrolment as a fee waiver; there is no cash payment to manage.</li>
        <li>Open to students from <strong>all countries</strong> who meet the international/European fee-payer test, including India.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your RGU <strong>offer letter</strong> for a full-time, on-campus undergraduate course.</li>
        <li><strong>Academic transcripts and proof of qualifications</strong> meeting RGU’s entry requirements.</li>
        <li>A valid <strong>passport</strong>.</li>
        <li><strong>English-language evidence</strong> where required by your course.</li>
        <li>A <strong>personal/support statement</strong> (published guidance for the scholarship application refers to a statement of around 500 words) setting out why you chose the course and what you bring to RGU life.</li>
        <li>Any <strong>written recommendation</strong> from a teacher or adviser who knows you academically, where the application form asks for one.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for an <strong>eligible RGU undergraduate course</strong> for September 2027 and receive your offer.</li>
        <li>Work through your <strong>offer conditions</strong> so that everything except the tuition deposit is met well before June 2027.</li>
        <li>Watch for the scholarship window opening in the <strong>New Year</strong> and submit the separate Vice-Chancellor’s Undergraduate Scholarship application before the <strong>June 2027</strong> deadline.</li>
        <li>Do not stack expectations: RGU applies only <strong>one award per offer</strong>, normally the most beneficial one — check on rgu.ac.uk whether the separate early-deposit discount stacks for your intake.</li>
        <li>Keep your ambassador commitment in mind: winners are expected to take part in university activities and promote the international student experience.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the RGU Vice-Chancellor’s Scholarship fully funded?',
  'No. It covers the full first-year tuition fee only. Living costs, accommodation, travel, visa fees and later years of tuition are not covered — it is a fee waiver, not a cash grant.'),
 ('Do I need a separate application?',
  'Yes. You need a course offer first, then a separate scholarship application in the window that opens in the New Year for the September 2027 intake.'),
 ('When exactly does it close?',
  'The deadline month published across summaries is June 2027. The exact closing day was not published in the official notification checked — one secondary summary lists 30 June 2027 — so confirm the exact day on rgu.ac.uk as soon as the window opens.'),
 ('Can I combine it with RGU’s £2,000 International Student Discount?',
  'No — RGU applies only one university scholarship, financial award or discount per offer, normally the most beneficial one. The £2,000 discount is the fallback award for students who do not win a named scholarship.'),
 ('Who is excluded?',
  'January-start shorter-programme students are not eligible for this September-intake award (January fast-track students become eligible when they start year two in September). Sponsored students are excluded because RGU scholarships are for self-funding students only.')]) + '''
      <p class="verify">Verified 24 Oct 2026: daadscholarship.com/robert-gordon-university-vice-chancellors-scholarship-2027-in-scotland-open-for-international-students/ — full first-year tuition, international/EU undergraduates, September 2027, June 2027 deadline, separate application expected, offer conditions except deposit, ambassador role, not a cash stipend, no living-cost cover; mastersportal.com/scholarships/8100/vice-chancellors-undergraduate-scholarship.html — merit-based, multiple awards, full first-year tuition, Year 1/direct Year 2, September intake, conditions except deposit, ambassador role; youapply.com/universities/united-kingdom/robert-gordon-university — September 2027 applications open in the New Year, June 2027 shown as deadline month; collegedunia.com/uk/university/783-robert-gordon-university-aberdeen/scholarship — tentative January 2027 opening, typical first-year international fees roughly £15,910–£18,760, £2,000 discount as separate recurring award. Exact closing day not published in the official notification checked.</p>''',
 dl_long='June 2027 (September 2027 intake; applications open in the New Year — the exact closing day was not published in the official notification checked)',
 offlinks=[('Bright Scholarship — Robert Gordon University Vice Chancellors Scholarship 2027', 'https://brightscholarship.com/robert-gordon-university-vice-chancellors-scholarship/'),
           ('DAADScholarships — RGU Vice-Chancellor’s Scholarship 2027', 'https://daadscholarship.com/robert-gordon-university-vice-chancellors-scholarship-2027-in-scotland-open-for-international-students/')],
 related_titles=['cardiff-vc-2027', 'stirling-vc-2027', 'glos-merit-2027', 'swinburne-2027'])),

# ---------------------------------------------------------------- 2. USTC
A.append(dict(
 slug='ustc-research-internship-program-2027-china',
 title='USTC Research Internship Program 2027 in China (Fully Funded)',
 meta='USTC Research Internship Program 2027: 3-month to 1-year research placements at the University of Science and Technology of China, Hefei. Level A fellowship covers tuition, insurance, dormitory and a monthly stipend. Fall Level A deadline 31 March 2027 — eligibility, documents, how to apply and FAQs.',
 short='USTC Research Internship Program 2027', kicker='China · Research Internship · Fully Funded (Level A)', mono='UT',
 prov_short='University of Science and Technology of China (USTC)', prov_cat='University · China',
 h1='USTC Research Internship Program 2027 in China (Fully Funded)',
 sub='The USTC Research Internship Program 2027 places international undergraduates and graduates in research laboratories at the University of Science and Technology of China in Hefei for 3 months to 1 year. The top tier, Fellowship Level A, is the fully funded one — tuition waiver, medical insurance, free university dormitory and a monthly stipend. The Spring 2027 Level A window closed on 30 September 2026; the live target is the Fall window, 1 January to 31 March 2027.',
 dpill='Fall Level A: 31 Mar 2027 · %d days left' % dl_left('2027-03-31'),
 facts=facts([('Award', 'Three USTC Fellowship levels. Level A (fully funded): full tuition waiver, comprehensive medical insurance, free university dormitory, and a monthly stipend of RMB 2,500 for bachelor students, RMB 3,000 for master students and RMB 3,500 for PhD students. Level B: tuition waiver, medical insurance and free dormitory, but no stipend. Level C: tuition waiver only. You may apply for one level or all three at once; USTC decides which level you receive.'),
              ('Eligible', 'Non-Chinese citizens holding a foreign passport, aged 18–40, in good health, with no criminal record and a good command of English. You must be currently enrolled full-time as a Year 3 or Year 4 undergraduate, or as a master or doctoral student. A pre-acceptance from a USTC professor in your field is part of the application route.'),
              ('How', 'Create an account on the USTC online application system (ustc.17gz.org), select Non-degree programme → Research Internship, choose your fellowship level(s), upload the required documents and submit inside the window for your semester.'),
              ('Deadline', 'Fall-semester Level A: 1 January–31 March 2027. Spring-semester Level A closed 30 September 2026. Level B, Level C and self-funded applicants must apply at least three months before their intended start date.'),
              ('Fine print', '“Fully funded” applies to Level A only — Level B and C are partial, and self-funded participation is also possible (published self-funded tuition is roughly RMB 2,160/month for undergraduate/master and RMB 2,660/month for PhD, plus dormitory roughly RMB 500–1,000/month and insurance RMB 160/month). Dormitory places for Level A and B are offered first-come, first-served; if campus housing is full you arrange your own accommodation.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>University of Science and Technology of China (USTC)</strong>, based in Hefei in Anhui province, is one of China’s leading science and technology universities. Its <strong>Research Internship Program</strong> brings international students into USTC laboratories for <strong>3 months to 1 year</strong> of supervised research, alongside free Chinese language and culture classes and a direct route into USTC’s academic community — useful if you later apply for a USTC master’s or PhD.</p>
      <p>Research areas span the university’s strengths: life sciences, chemistry and materials science, computer science and technology, earth and space sciences, engineering science, information science and technology, mathematical sciences, physical sciences, management, public affairs, humanities and social science, software engineering and more.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Chinese citizen</strong> holding a valid foreign passport.</li>
        <li>Be aged <strong>18–40</strong> and in good physical and mental health, with <strong>no criminal record</strong>.</li>
        <li>Be currently enrolled <strong>full-time</strong> as a <strong>Year 3 or Year 4 undergraduate</strong>, or as a <strong>master’s or doctoral student</strong>.</li>
        <li>Have a <strong>good command of English</strong> — the official fellowship page does not state a mandatory IELTS score, so follow whatever evidence the current online system asks for.</li>
        <li>Secure <strong>pre-acceptance from a USTC professor</strong> in your research field before submitting — contact supervisors through their school pages first.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Level A (fully funded):</strong> tuition waiver, comprehensive medical insurance, free university dormitory, and a monthly stipend — <strong>RMB 2,500</strong> (bachelor), <strong>RMB 3,000</strong> (master), <strong>RMB 3,500</strong> (PhD).</li>
        <li><strong>Level B:</strong> tuition waiver, medical insurance and free dormitory.</li>
        <li><strong>Level C:</strong> tuition waiver.</li>
        <li>Hands-on research with USTC professors, free Chinese language and culture classes, and exposure to USTC’s graduate programmes.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Valid <strong>passport</strong> (with a foreign nationality).</li>
        <li><strong>CV</strong> and academic <strong>transcripts</strong> / degree or enrolment certificates.</li>
        <li><strong>Pre-acceptance letter</strong> from a USTC professor.</li>
        <li><strong>English-language proficiency</strong> certificate or test results, as the portal requires.</li>
        <li><strong>No criminal record</strong> certificate or form.</li>
        <li>Any further documents marked with an asterisk in the online application form.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Browse USTC schools and supervisor profiles, then <strong>contact a professor</strong> in your field and secure pre-acceptance.</li>
        <li>Create an account on the USTC application system (<strong>ustc.17gz.org</strong>) and select <strong>Non-degree → Research Internship</strong>.</li>
        <li>Choose the fellowship level(s) you are applying for — you may apply for one level or all three at once.</li>
        <li>Complete the form, upload every required document, and submit inside the window: for <strong>Fall Level A, 1 January–31 March 2027</strong>.</li>
        <li>If admitted, apply for a <strong>student visa</strong> (JW201 or JW202 form plus admission notice) at a Chinese embassy or consulate, and arrange the required <strong>medical insurance</strong> before arrival.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the USTC Research Internship fully funded for everyone?',
  'No. Only Fellowship Level A is fully funded (tuition, insurance, dormitory and stipend). Level B drops the stipend and Level C is a tuition waiver only — and self-funded participation is also possible.'),
 ('Can I still apply for Spring 2027?',
  'No — the Spring-semester Level A window closed on 30 September 2026. The live window is Fall-semester Level A, 1 January to 31 March 2027.'),
 ('Is IELTS mandatory?',
  'The official fellowship page requires a good command of English but does not state a mandatory IELTS score. Follow the evidence requirements shown in the current online application system.'),
 ('Can undergraduates apply?',
  'Yes, but only if you are currently enrolled full-time in Year 3 or Year 4. First- and second-year undergraduates are not eligible.'),
 ('How long does the internship last?',
  'Between 3 months and 1 year, depending on your research plan and the host professor’s agreement.')]) + '''
      <p class="verify">Verified 24 Oct 2026: ic.ustc.edu.cn (official USTC International College fellowship page) — three fellowship levels with stipend figures, eligibility (non-Chinese, 18–40, Year 3/4 UG or master/PhD, good health, no criminal record, good English), Fall window Jan 1–Mar 31 and Spring window Jul 1–Sep 30, Level B/C and self-funded 3-months-ahead rule; mindshipglobal.com/opportunities/ustc-research-internship-program-2027/ — Fall Level A window 1 Jan–31 Mar 2027, Spring window closed 30 Sep 2026, Level A stipend figures, accommodation first-come first-served; oyaop.com/opportunity/internships/ustc-research-internship-program-2026-2027-fully-funded-research-internship-in-china/ — self-funded tuition and dormitory/insurance figures, portal route Non-degree → Research Internship.</p>''',
 dl_long='March 31, 2027 (Fall-semester Level A window: 1 January–31 March 2027; the Spring 2027 window closed 30 September 2026)',
 offlinks=[('USTC International College — USTC Fellowship for Non-degree Programs (official)', 'http://ic.ustc.edu.cn/?abroad=356'),
           ('Bright Scholarship — USTC Research Internship Program 2027', 'https://brightscholarship.com/ustc-research-internship-program-china/')],
 related_titles=['nctu-2027', 'kaist-grad-2027', 'gxnu-csc-2027', 'hkpfs-2027'])),

# ---------------------------------------------------------------- 3. Yenching
A.append(dict(
 slug='peking-university-yenching-academy-scholarship-2027-china',
 title='Peking University Yenching Academy Scholarship 2027 in China (Fully Funded)',
 meta='Peking University Yenching Academy Scholarship 2027: a fully funded 2-year interdisciplinary master’s in China Studies in Beijing for about 120 scholars a year. Deadline 30 November 2026, 9:00 am Beijing time — eligibility, benefits, documents, how to apply and FAQs.',
 short='Peking University Yenching Academy Scholarship 2027', kicker='China · Master’s · Fully Funded', mono='YA',
 prov_short='Yenching Academy, Peking University', prov_cat='University · China',
 h1='Peking University Yenching Academy Scholarship 2027 in China (Fully Funded)',
 sub='The Yenching Academy Scholarship 2027 funds a two-year interdisciplinary master’s in China Studies at Peking University in Beijing for roughly 120 scholars a year. Every admitted scholar receives the first-year Yenching Fellowship — full tuition, accommodation, a monthly stipend, one round-trip travel allowance, medical insurance and research costs — and applications for the 2027 cohort close on 30 November 2026 at 9:00 a.m. Beijing time.',
 dpill='Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
 facts=facts([('Award', 'The first-year Yenching Fellowship covers: full tuition for the master’s in China Studies, accommodation in the Yenching Academy House on the Peking University campus, a monthly stipend for living costs, one round-trip travel allowance between your home city and Beijing, basic medical insurance, and designated research/field-study expenses. Scholars who maintain good academic standing and remain in Beijing for the second year may apply for a second-year fellowship covering tuition, accommodation, insurance and a stipend.'),
              ('Eligible', 'A bachelor’s degree in any field, or current bachelor’s students who will graduate by August 2027. You need an outstanding academic record, a clear interdisciplinary interest in China, demonstrated leadership potential and community engagement. English: IELTS Academic 7.0 or TOEFL iBT 100 (or accepted equivalents such as Cambridge English Scale 185, CET-6 600 or TEM-4 pass). Native English speakers and graduates of English-taught programmes may be exempt; applicants from Hong Kong, Macao and Taiwan must still submit scores.'),
              ('How', 'Apply through the Yenching Academy application portal from 1 September 2026. If your university is a Yenching partner university, you must first complete its internal pre-selection process. Submit before 30 November 2026, 9:00 a.m. Beijing time.'),
              ('Deadline', '30 November 2026 at 9:00 a.m. Beijing time (UTC+8), for all applicant categories.'),
              ('Fine print', 'The programme is a full-time, residential two-year master’s. Students choose one of six research areas — Economics and Management; History and Archaeology; Philosophy and Religion; Politics and International Relations; Law and Society; Literature and Culture — and all students enrol in the Master of Arts in China Studies, with the diploma degree name depending on the specialisation track.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Yenching Academy of Peking University</strong> runs an interdisciplinary graduate programme designed to give a deeper understanding of China and its role in the world. It combines coursework, independent research, field study and a residential community in Beijing, with students working with academic advisers to shape their own study path inside six research areas.</p>
      <p>Each year roughly <strong>120 scholars</strong> join the Academy — around three-quarters of them international — and every admitted scholar receives the <strong>Yenching Fellowship for the first academic year</strong>. That is what makes this one of the most sought-after fully funded master’s routes in Asia: tuition, housing, a living stipend and a flight are all covered from day one, rather than topped up later.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>bachelor’s degree in any field</strong>, or be on track to graduate by <strong>August 2027</strong>.</li>
        <li>Show an <strong>outstanding academic record</strong> and a clear interest in the interdisciplinary study of China.</li>
        <li>Demonstrate <strong>leadership potential</strong>, community engagement and extracurricular achievement.</li>
        <li>Meet the English requirement: <strong>IELTS Academic 7.0</strong> or <strong>TOEFL iBT 100</strong> (accepted equivalents include Cambridge English Scale 185, CET-6 600 and TEM-4 at pass level “good” or above), taken after 1 September 2025. Exemptions may apply to native speakers and English-taught graduates; applicants from Hong Kong, Macao and Taiwan must still submit scores.</li>
        <li>International applicants must be <strong>non-Chinese citizens</strong> holding a valid passport.</li>
        <li>If you are affiliated with a <strong>Yenching partner university</strong>, complete your institution’s <strong>internal pre-selection</strong> before submitting to the Academy.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition</strong> for the master’s in China Studies.</li>
        <li><strong>Accommodation</strong> in the Yenching Academy House on the Peking University campus (first year).</li>
        <li><strong>Monthly stipend</strong> for living costs.</li>
        <li><strong>One round-trip travel allowance</strong> between your base city and Beijing.</li>
        <li><strong>Basic medical insurance</strong> and <strong>designated research/field-study expenses</strong>.</li>
        <li>A second-year fellowship is available by application for scholars in good standing who remain in Beijing.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Personal statement</strong> — maximum 750 words.</li>
        <li><strong>Research interest statement</strong> — maximum 1,500 words excluding citations.</li>
        <li><strong>Two recommendation letters</strong> from full professors, associate professors or equivalents.</li>
        <li>Academic <strong>transcripts</strong> and degree certificate (or proof of expected graduation by August 2027).</li>
        <li><strong>English test scores</strong> meeting the thresholds above, unless an exemption applies.</li>
        <li>Valid <strong>passport</strong> and a CV setting out leadership and community engagement.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check whether your university is a <strong>Yenching partner university</strong> — if so, clear its internal pre-selection first.</li>
        <li>Create an account on the <strong>Yenching Academy application portal</strong> (applications for the 2027 cohort opened 1 September 2026).</li>
        <li>Upload your personal statement, research statement, recommendation letters, transcripts and English scores.</li>
        <li>Submit before <strong>30 November 2026 at 9:00 a.m. Beijing time</strong> — the deadline is the same for all applicant categories.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a degree in China Studies to apply?',
  'No. Applicants may hold a bachelor’s degree in any field, provided they show a strong interest in the interdisciplinary study of China and meet the academic and English requirements.'),
 ('Is there an age limit?',
  'No official age cutoff is published, but published summaries note most admitted scholars are under 28. Age is not listed as an eligibility condition.'),
 ('Is the second year funded too?',
  'The first-year fellowship is guaranteed for every admitted scholar. For the second year, scholars in good academic standing who remain in Beijing may apply for a second-year fellowship covering tuition, accommodation, insurance and a stipend.'),
 ('What are the six research areas?',
  'Economics and Management; History and Archaeology; Philosophy and Religion; Politics and International Relations; Law and Society; and Literature and Culture.'),
 ('Do I need Chinese language skills?',
  'The published eligibility criteria centre on academic record, leadership, community engagement and English proficiency (IELTS 7.0 / TOEFL iBT 100 or equivalents). No Chinese-language test threshold is stated in the sources checked — confirm any language expectations in the Academy’s own application instructions.')]) + '''
      <p class="verify">Verified 24 Oct 2026: leapkite.com/opportunities/yenching-academy-scholarship/ — 30 Nov 2026 9:00 am Beijing deadline, full tuition, accommodation, stipend, round-trip airfare, field-study costs, IELTS 7.0/TOEFL 100 after 1 Sep 2025, official site yenchingacademy.pku.edu.cn; scholarpositions.com/yenching-academy-scholarship-2027/ — 2-year master’s, ~120 scholars, full coverage, 30 Nov 2026; opportunitiesforyouth.org/2026/09/07/yenching-academy-of-peking-university-scholarship-2027-fully-funded-masters-fellowship-in-china-for-international-students/ — 750-word personal statement, 1,500-word research statement, two letters from full/associate professors, Cambridge 185, CET-6 600, TEM-4 pass, partner-university pre-selection, second-year fellowship conditions; scholarshipsedge.com/yenching-academy-scholarship-in-china/ — six research areas, 120 scholarships, 30 Nov 2026 9:00 am Beijing. Monthly stipend amount not published in the sources checked.</p>''',
 dl_long='30 November 2026 at 9:00 a.m. Beijing time (all applicant categories)',
 offlinks=[('Yenching Academy of Peking University (official website)', 'https://yenchingacademy.pku.edu.cn/'),
           ('Bright Scholarship — Peking University Yenching Academy Scholarship 2027', 'https://brightscholarship.com/peking-university-yenching-academy-scholarship/')],
 related_titles=['hkpfs-2027', 'utokyo-adb-2027', 'neukom-2027', 'hawaii-ewc'])),

# ---------------------------------------------------------------- 4. Harvard
A.append(dict(
 slug='harvard-environmental-fellows-program-2027-usa',
 title='Harvard Environmental Fellowship Program 2027 (Fully Funded)',
 meta='Harvard Environmental Fellowship Program 2027: a two-year postdoctoral fellowship at Harvard paying $92,000 a year for about five fellows. Deadline 1 December 2026, 5pm ET — eligibility, benefits, documents, host requirement, how to apply and FAQs.',
 short='Harvard Environmental Fellowship Program 2027', kicker='USA · Postdoctoral Fellowship · Fully Funded', mono='HE',
 prov_short='Harvard University Center for the Environment', prov_cat='Fellowship · USA',
 h1='Harvard Environmental Fellowship Program 2027 (Fully Funded)',
 sub='The Harvard Environmental Fellows Program 2027 offers about five recent doctorate holders a two-year postdoctoral fellowship at Harvard University, with a salary of $92,000 a year, employee health insurance eligibility, relocation support and a professional allowance. Applications close on 1 December 2026 at 5:00 p.m. Eastern Time, and every applicant must arrive with a committed Harvard faculty host.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'A salary of $92,000 per year for two years (about $184,000 over the fellowship), eligibility for Harvard employee health insurance, reimbursement of up to $2,500 for relocation expenses, and a $2,500 annual allowance for travel and other professional expenses. Fellows join a co-curricular programme of biweekly dinners with other fellows, Harvard faculty and invited speakers.'),
              ('Eligible', 'Holders of a doctorate or comparable terminal degree awarded between May 2023 and August 2027 (dissertation filed before the September 2027 start), in any discipline, from any university in the world. Foreign nationals are eligible, subject to Harvard immigration requirements and English proficiency. You must secure a commitment from one or more Harvard faculty members to serve as mentor and provide office or lab space; a faculty member may host only one fellow at a time. Harvard degree holders and current Harvard postdocs are eligible only if the project and host take them in a significantly new direction — not a continuation with the same professors or lab, and never extensive work with the thesis adviser.'),
              ('How', 'Complete the online application form on Harvard’s academic positions portal by 1 December 2026 at 5:00 p.m. ET, attaching a CV with publications, a detailed research proposal of at most five pages (references counted separately) and up to three publications or writing samples. Three reference letters (including one from the dissertation adviser) and a host support letter are due by 11 December 2026 at 5:00 p.m. ET.'),
              ('Deadline', '1 December 2026 at 5:00 p.m. Eastern Time. Host letters and recommendation letters are due 11 December 2026 at 5:00 p.m. ET. Decisions are expected in late January 2027.'),
              ('Fine print', 'Fellows must live in the Cambridge, Massachusetts area for the full two years; fieldwork must be scheduled during the summer or the January recess. The programme lists faculty who cannot host in 2027 — including Charles Davis, Charles Taylor, Scott Edwards, Le Xie, Robin Kelsey and Phillip Deloria, plus Richard Lazarus and Joyce Chaplin, who are unavailable as hosts — so confirm host eligibility before you build your proposal around a name.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Environmental Fellows Program</strong> was created by the <strong>Harvard University Center for the Environment (HUCE)</strong>, a centre of Harvard’s Salata Institute for Climate and Sustainability, so that recent doctorate recipients can use Harvard’s resources to tackle complex environmental problems. Fellows spend <strong>two years working with Harvard faculty</strong> in any school or department, forming a cross-disciplinary community that strengthens links across the university.</p>
      <p>The programme is deliberately discipline-blind: successful fellows and hosts have come from the sciences, economics, law, government, public policy, public health, medicine, design and the humanities. What matters is that the proposed research addresses an environmental issue and represents an independent direction — not a rerun of the applicant’s PhD or the host’s ongoing work.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>doctorate or comparable terminal degree</strong> awarded between <strong>May 2023 and August 2027</strong>; applicants without a PhD may apply where their field uses another terminal degree as the standard.</li>
        <li>Have <strong>filed the dissertation</strong> before the fellowship starts in <strong>September 2027</strong>.</li>
        <li>Propose research on an <strong>environmental issue</strong>, in any discipline.</li>
        <li>Have earned your degree at <strong>any university in the world</strong> — foreign nationals are eligible, subject to Harvard immigration requirements and English proficiency.</li>
        <li>Secure a <strong>Harvard faculty host</strong> who commits to mentoring you and providing office or lab space (one fellow per host at a time).</li>
        <li>Be prepared to <strong>live in the Cambridge, Massachusetts area</strong> for the full two years.</li>
        <li>Harvard graduates and current Harvard postdocs: eligible only with a <strong>significantly new direction and new host</strong> — do not propose continuing with the same professors or lab, or working extensively with your thesis adviser.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$92,000 annual salary</strong> for two years.</li>
        <li>Eligibility for <strong>Harvard employee health insurance</strong>.</li>
        <li>Up to <strong>$2,500 relocation reimbursement</strong>.</li>
        <li><strong>$2,500 per year</strong> for travel and other professional expenses.</li>
        <li>A <strong>co-curricular programme</strong>: biweekly dinners with fellows, Harvard faculty and invited speakers.</li>
        <li>About <strong>five fellowships</strong> are expected for the 2027 cohort.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>CV including a list of publications</strong>.</li>
        <li><strong>Detailed research proposal</strong> — maximum five pages, references counted separately — explaining your specific reasons for applying; the final product must clearly be your own work even though you should discuss it with your potential host.</li>
        <li><strong>Up to three publications or writing samples</strong>.</li>
        <li><strong>Three letters of reference</strong>, including one from your dissertation adviser (the system sends letter requests only after you submit, so brief your referees in advance).</li>
        <li><strong>Host support letter</strong> from your Harvard faculty host, committing to mentor you and provide office or lab space, sent directly to the Center.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Find your host first.</strong> Approach Harvard faculty whose work connects with your proposal and secure a firm commitment — an application without a host letter will not be reviewed.</li>
        <li>Check the host is <strong>eligible to host in 2027</strong> (the programme publishes a short ineligible/unavailable list each year).</li>
        <li>Draft the <strong>five-page proposal</strong> as an independent research direction, distinct from your PhD and from the host’s ongoing work.</li>
        <li>Complete the <strong>online application form</strong> on Harvard’s academic positions portal and attach your CV, proposal and writing samples by <strong>1 December 2026 at 5:00 p.m. ET</strong>.</li>
        <li>Make sure your <strong>three referees and your host</strong> submit their letters by <strong>11 December 2026 at 5:00 p.m. ET</strong> — referees get their upload link only after you submit, so submit early.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do I need a Harvard faculty host before applying?',
  'Yes. Every candidate must secure a commitment from one or more Harvard faculty members to serve as mentor and provide office or lab space. An application without a host letter will not be reviewed.'),
 ('Can I continue my PhD research at Harvard?',
  'No. The proposed project must represent an independent research direction that extends beyond your PhD research and the host’s ongoing work. Harvard graduates and current Harvard postdocs face the same test, and must not propose working extensively with their thesis adviser.'),
 ('How many fellowships are awarded?',
  'HUCE expects to award approximately five fellowships for the 2027 cohort.'),
 ('Can international scholars apply?',
  'Yes. Candidates may have earned their degrees at any university worldwide, and foreign nationals are eligible, subject to Harvard’s immigration requirements and adequate English proficiency.'),
 ('When will I hear the outcome?',
  'Harvard expects to notify applicants by late January 2027; selected applicants are interviewed by video.')]) + '''
      <p class="verify">Verified 24 Oct 2026: environment.harvard.edu (official HUCE programme requirements page) — 1 Dec 2026 5:00pm EST deadline, host/rec letters 11 Dec 2026 5:00pm EST, May 2023–August 2027 degree window, dissertation filed before September 2027 start, host commitment and one-fellow-per-host rule, Harvard-candidate new-direction rule, ineligible/unavailable host names, Cambridge residency and fieldwork timing; academicpositions.harvard.edu/postings/16664 (official application posting) — form, CV with publications, 5-page proposal, up to 3 writing samples, 3 reference letters including dissertation adviser, host letter to environmental_fellows@harvard.edu, late-January 2027 decisions; oyaop.com/opportunity/scholarships-and-fellowships/harvard-environmental-fellows-program-2027-92000-annual-salary-at-harvard-university/ — $92,000 salary, $2,500 relocation, $2,500/year allowance, ~5 awards, biweekly dinners.</p>''',
 dl_long='1 December 2026 at 5:00 p.m. Eastern Time (host and recommendation letters due 11 December 2026 at 5:00 p.m. ET)',
 offlinks=[('Harvard University Center for the Environment — Environmental Fellows Program Requirements (official)', 'https://www.environment.harvard.edu/program-requirements-environmental-fellows-programs'),
           ('Harvard Academic Positions — Harvard Environmental Fellow application (official)', 'https://academicpositions.harvard.edu/postings/16664')],
 related_titles=['neukom-2027', 'elevate-2027', 'hawaii-ewc', 'lawai-2027'])),

# ---------------------------------------------------------------- 5. Potsdam
A.append(dict(
 slug='university-of-potsdam-scholarships-2027-germany',
 title='University of Potsdam Scholarships 2027 in Germany (Stipend €300 per month)',
 meta='University of Potsdam Scholarships 2027: the University Scholarship Potsdam within the Deutschlandstipendium pays €300 a month to talented bachelor and master students of all nationalities. Next window opens 1 July 2027 — eligibility, documents, how to apply and FAQs.',
 short='University of Potsdam Scholarships 2027', kicker='Germany · Bachelor’s & Master’s · Funded', mono='UP',
 prov_short='University of Potsdam', prov_cat='University · Germany',
 h1='University of Potsdam Scholarships 2027 in Germany (Stipend €300 per month)',
 sub='The University Scholarship Potsdam, awarded within Germany’s national Deutschlandstipendium programme, pays €300 a month to talented and high-achieving bachelor’s and master’s students at the University of Potsdam, near Berlin. The 2026/27 application window ran from 1 to 22 July 2026 and is closed; the next application phase for the 2027/28 winter semester starts on 1 July 2027, and its closing date has not yet been published.',
 dpill='Next window opens 1 Jul 2027',
 facts=facts([('Award', '€300 per month, funded equally by federal funds and private sponsors (foundations, companies or individuals) under the Deutschlandstipendium. In the 2026/27 call the scholarship ran for the winter-semester funding period; the 2027/28 call will set its own period. The award also brings contact with sponsors and invitations to university scholarship events.'),
              ('Eligible', 'Students of the University of Potsdam who have not yet exceeded the standard period of study in their degree programme (serious reasons such as impairment, pregnancy, childcare or a subject-related stay abroad can justify an extension), and applicants about to begin their studies who can provide the necessary admission documents. You must show excellent performance in school or during your studies, plus motivation, and the selection also weighs financial need, special achievements and awards, extracurricular involvement and personal or social circumstances. International students are eligible; their academic average must be converted into the German grading system, for example through uni-assist, with documentation of voluntary engagement.'),
              ('How', 'Apply once through the University Scholarship online application portal during the July window. A letter of recommendation is not required. If you apply for a Denkwerkstatt (think tank) place you automatically also apply for a general university scholarship, so submit only one application.'),
              ('Deadline', 'Next application window opens 1 July 2027 (for the 2027/28 winter semester). The closing date for that window has not yet been published — the 2026/27 window ran 1–22 July 2026, so do not assume the same closing day.'),
              ('Fine print', '€300 a month is partial support, not a living-cost grant: Potsdam charges no tuition, but you still need funding for rent, food, health insurance and the semester contribution. Separately, Potsdam runs a degree-completion grant for international students in their final phase (€700/month for up to 5 months) and the DAAD PROMOS mobility scheme for short stays abroad — see the article for those routes.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Potsdam</strong>, minutes from Berlin, awards its <strong>University Scholarship</strong> as part of the national <strong>Deutschlandstipendium</strong> programme launched by Germany’s Federal Ministry of Education and Research. The idea is simple: private sponsors — foundations, companies and individuals — put up half of each €300 monthly award, and the federal government matches it, so talented students get recognised and supported without a separate bureaucracy for every donor.</p>
      <p>Selection is broader than grades alone. Alongside school or university performance, Potsdam weighs motivation, financial need, special achievements and awards, internships and voluntary service, and personal or social circumstances that shaped your educational path. That breadth is why international students, first-generation students and students with interrupted study histories can all be competitive here.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>student of the University of Potsdam</strong> who has not exceeded the <strong>standard period of study</strong> (exceptions for serious reasons: impairment, pregnancy, childcare, or a subject-related stay abroad).</li>
        <li>Or be an <strong>applicant about to begin studies</strong> at Potsdam who can provide the necessary <strong>admission documents</strong> (first-year applicants may submit their enrolment certificate afterwards, within the university’s deadline).</li>
        <li>Show <strong>excellent performance</strong> in school or during your studies, plus motivation for the programme.</li>
        <li>International applicants: have your academic average <strong>converted into the German grading system</strong> (for example through uni-assist) and document your <strong>voluntary/social engagement</strong>.</li>
        <li>Open to <strong>all nationalities</strong> and to bachelor’s and master’s students across faculties.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€300 per month</strong>, half federal funds and half private sponsorship.</li>
        <li>Funding for the <strong>scholarship period set in the call</strong> (one academic year in the 2026/27 round).</li>
        <li><strong>Contact with your sponsor</strong> — donors are matched to scholars, and you may indicate donor preferences in the application form.</li>
        <li>Invitations to university scholarship events, including the onboarding event and scholarship celebration.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The completed <strong>online application form</strong> on the University Scholarship portal.</li>
        <li>Proof of <strong>enrolment or admission</strong> at the University of Potsdam.</li>
        <li><strong>Academic records</strong> (transcripts / grade overview), converted to the German system where you studied abroad.</li>
        <li>Evidence of <strong>voluntary or social engagement</strong> — bundle several certificates into a single PDF per upload field, titled “Surname_firstname_engagement”.</li>
        <li>An <strong>essay as a PDF</strong> if you are applying to a Denkwerkstatt (think tank) place.</li>
        <li>No letter of recommendation is required for the general university scholarship.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for <strong>admission to a Potsdam bachelor’s or master’s programme</strong> if you are not yet enrolled — applicants about to begin studies can apply for the scholarship with their admission documents.</li>
        <li>Prepare your documents as PDFs with the university’s naming pattern (“Surname_firstname_…” for each file).</li>
        <li>Submit <strong>one application only</strong> in the online portal during the July window — a think-tank application automatically counts as a general scholarship application too.</li>
        <li>Watch for the <strong>1 July 2027 opening</strong> of the 2027/28 window and confirm the closing date in the new call — do not assume the 2026/27 dates (1–22 July) repeat exactly.</li>
        <li>Expect selection over July–September, with award notifications from mid-October in the 2026/27 pattern.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is €300 a month enough to live on in Potsdam?',
  'No — it is partial support. Potsdam charges no tuition, but rent near Berlin, food, health insurance and the semester contribution still need separate funding. Treat the scholarship as a top-up and a mark of recognition, not a full living budget.'),
 ('Can first-year or not-yet-enrolled students apply?',
  'Yes. Applicants about to begin their studies at Potsdam who can provide the necessary admission documents are eligible, and first-year applicants may submit their enrolment certificate afterwards within the university’s deadline.'),
 ('Is a recommendation letter required?',
  'No. The official application page states a letter of recommendation is not required for the University Scholarship.'),
 ('What if I also want a think-tank (Denkwerkstatt) place?',
  'Apply for the think-tank place and you automatically also apply for a general university scholarship — submit only one application, and upload the required essay as a PDF.'),
 ('Are there other Potsdam funding routes for international students?',
  'Yes. The degree-completion grant (Studienabschlussbeihilfe) pays €700 a month for up to 5 months to non-German students in the final phase of a bachelor’s or master’s who can finish within a year and show financial need. The DAAD PROMOS scheme funds short stays abroad (internships, thesis research); its next published deadline is 15 November 2026 for stays beginning January–April 2027.')]) + '''
      <p class="verify">Verified 24 Oct 2026: uni-potsdam.de official University Scholarship application page — July 1–22, 2026 online application period, selection July–September, notifications from mid-October, onboarding 6 November 2026, no recommendation letter required, think-tank auto-application rule, one-application rule, PDF naming pattern; uni-potsdam.de 2026/27 call for applications PDF — €300/month, half federal and half private sponsors, eligibility including about-to-begin applicants, standard-period rule and exceptions, motivation/need/achievement/engagement criteria; medjouel.com/jobs/university-of-potsdam-scholarships-2026-27-funding-opportunities-for-international-students-in-germany/ — next application phase starts 1 July 2027 for the 2027/28 winter semester, uni-assist grade conversion for international applicants; uni-potsdam.de degree-completion grant page — €700/month up to 5 months, final-phase non-German students; uni-potsdam.de PROMOS page — next deadline 15 November 2026 for stays beginning January–April 2027. Closing date for the 2027/28 window not yet published.</p>''',
 dl_long='1 July 2027 (next application window opens; closing date not yet published — the 2026/27 window ran 1–22 July 2026)',
 offlinks=[('University of Potsdam — University Scholarship Application (official)', 'http://www.uni-potsdam.de/en/universitaetsstipendium/information-for-students/bewerbung'),
           ('Bright Scholarship — University of Potsdam Scholarships 2027', 'https://brightscholarship.com/university-of-potsdam-scholarships/')],
 related_titles=['cardiff-vc-2027', 'gates-cam-2027', 'swinburne-2027', 'glos-merit-2027'])),

sizes = {}
for a in A: _split_verify(a)
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch45_built.json','w'))

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

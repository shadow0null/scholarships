#!/usr/bin/env python3
"""Batch 65 (cron run 65, 29 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
- Embassy of UK Scholarships 2026 - SKIPPED: listicle/umbrella, not a single scheme.
- UNICAF Online Scholarship Program 2026 - WRITTEN (rolling; partial, up to 80%).
- Harvard University MBA Scholarship 2027 - WRITTEN as Boustany MBA Harvard
  Scholarship (75% tuition, 31 May 2027; 'Fully Funded' aggregator label rejected).
- LUND University Summer School 2026 - SKIPPED: deadline passed 15 Apr 2026;
  programme ran 22-26 Jun 2026.
- Study in Germany without IELTS 2026 - SKIPPED: listicle.
- UNHCR Internship 2026 - WRITTEN (rolling per-vacancy; allowance, not a salary).
- Mandela Rhodes Scholarships 2026 - SKIPPED: 2027 cycle closed 14 Apr 2026;
  2028 opens 9 Mar 2027, closing date not yet published.
- ERA Summer Fellowship 2026 - SKIPPED: deadline passed 12 Apr 2026.
- 6000+ Free Scholarships Without IELTS 2026 - SKIPPED: listicle.
- University of Michigan Dearborn Scholarship 2026 - WRITTEN (15 Nov 2026;
  GPA tier table $5,000-$12,500/year, not a flat $10,000).
- High Commission of New Zealand Scholarships 2026 - SKIPPED: listicle/umbrella.
- High Commission of Saudi Arabia Scholarships 2026 - SKIPPED: listicle/umbrella.
- Richard and Susan Hayden Fellowship 2026 - SKIPPED: deadline passed
  7/17 Apr 2026 (sources disagree on the day; either way it has passed).
- University of Padua Scholarship 2026 - SKIPPED: deadline passed 2 May 2026.
- Qatar Scholarships Without IELTS 2026 - SKIPPED: listicle.
- Best Universities Without IELTS 2026 - SKIPPED: listicle.
- Stanford Venture Fellowship 2026 - SKIPPED: deadline passed 4 Apr 2026;
  programme ran 29 May-3 Jun 2026.
- UNCCD COP17 Media Reporting Fellowship 2026 - SKIPPED: deadline passed
  15 Apr 2026; COP17 reporting Aug 2026 ended.
- Youth Summer Fest Program 2026 Romania - SKIPPED: programme ran
  19 Jul-17 Aug 2026, ended.
- High Commission of Australia Scholarships 2026 - SKIPPED: listicle/umbrella.
- Computer Science Universities in Germany with No Fee 2026 - SKIPPED: listicle.
- ITRI Summer Internship 2026 Taiwan - SKIPPED: 2026 summer season
  (May-Sep 2026) over; no 2027 dates published.
- La Trobe University Scholarship 2026 - SKIPPED: umbrella label (many separate
  awards with different deadlines, e.g. High Achiever 31 Dec 2026).
- KAAD Scholarship 2026 Germany - SKIPPED: deadline passed 30 Jun 2026.
- University of Waterloo Undergraduate Scholarships 2026 - SKIPPED: umbrella
  (170+ entrance awards); 2026 entry cycle closed.
- Study in Australia Without IELTS 2026 - SKIPPED: listicle.
- Friedrich Ebert Foundation Scholarship 2026 - WRITTEN (Master's winter
  deadline 30 Nov 2026; current stipend EUR 992/month in latest guide).
"""
import pathlib, html.parser, re as _re
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
 'unicaf-2026': {'mono': 'UNI', 'title': 'UNICAF Online Scholarship Programme 2026 for International Students',
   'href': 'unicaf-online-scholarship-program-2026.html',
   'dpill': 'Rolling · no fixed deadline published',
   'award': 'A partial tuition scholarship for online degrees with UNICAF partner universities: up to 80% of tuition fees covered on UNICAF’s own page, with the remaining balance paid in monthly instalments. It is a fee discount, not a cash grant and not full funding.',
   'elig': 'Applicants who meet the entry requirements of their chosen programme and can pay the remaining portion of the fees; academic qualifications and financial situation are both considered. Degrees at Bachelor’s, Master’s and Doctorate level, studied online.',
   'tags': [('Online', 'blue'), ('International', 'teal')]},
 'harvard-mba-2027': {'mono': 'BOU', 'title': 'Boustany MBA Harvard Scholarship 2027 (75% of Tuition)',
   'href': 'harvard-university-mba-scholarship-2027-usa.html',
   'dpill': 'Deadline 31 May 2027 · %d days left' % dl_left('2027-05-31'),
   'award': 'Financial aid of 75% of Harvard MBA tuition fees for the two-year programme, awarded to one candidate once every two years, plus a two-month unpaid internship at the Boustany Foundation in Monaco with travel, food and accommodation covered.',
   'elig': 'Candidates with an excellent academic background and considerable promise who already hold an offer of admission from the Harvard MBA programme; any nationality, with priority to candidates of Lebanese descent.',
   'tags': [('MBA', 'blue'), ('USA', 'teal')]},
 'unhcr-2026': {'mono': 'UNH', 'title': 'UNHCR Internship Programme 2026 (Rolling Applications Worldwide)',
   'href': 'unhcr-internship-2026-online-apply.html',
   'dpill': 'Rolling · per-vacancy deadlines',
   'award': 'A 2-6 month humanitarian internship at UNHCR headquarters, global service centres or field offices. Not a salary: interns without external funding may receive a food and local transport allowance (70% of GS-3 Step 1 net salary at most duty stations, 50% at hardship stations), plus return travel reimbursement in some cases.',
   'elig': 'Current students or recent graduates (within 2 years) from a UNESCO-accredited institution, with at least 2 years of undergraduate study completed, English at B2 minimum, and no immediate relatives working for UNHCR.',
   'tags': [('Internship', 'blue'), ('Worldwide', 'teal')]},
 'umdearborn-2026': {'mono': 'UMD', 'title': 'University of Michigan-Dearborn Scholarship 2026 in USA (Funded)',
   'href': 'university-of-michigan-dearborn-scholarship-2026-usa.html',
   'dpill': 'Deadline 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
   'award': 'Merit awards for non-resident and international undergraduates set by GPA at admission: $5,000 a year (GPA 3.00-3.24), $7,500 (3.25-3.49), $10,000 (3.50-3.99) or $12,500 (4.00+), renewable for up to 8 semesters for freshmen. Automatically considered on admission; no separate scholarship application.',
   'elig': 'International or out-of-state first-year or transfer students enrolling full-time in a degree programme at UM-Dearborn, with a GPA of 3.0 or higher and English proficiency (IELTS 6.5 or TOEFL iBT 80 in the older international criteria).',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'fes-2026': {'mono': 'FES', 'title': 'Friedrich Ebert Foundation Scholarship 2026 in Germany (Fully Funded)',
   'href': 'friedrich-ebert-foundation-scholarship-2026-germany.html',
   'dpill': 'Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
   'award': 'For international students already studying in Germany: a monthly stipend (EUR 992 a month for students in the latest guide; older pages list EUR 934, EUR 850 or EUR 750), health insurance costs covered, and a child allowance. Doctoral candidates receive EUR 1,500 a month in the latest guide. Nothing is repayable; flights are not covered.',
   'elig': 'International students from the Global South, former CIS states and eastern/south-eastern Europe (OECD nationals excluded) with outstanding academic merit and social/political commitment to social-democratic values, German at B2, and not longer than 15 months in Germany at application (exemptions apply).',
   'tags': [('Bachelor’s & Master’s & PhD', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)
A = []

# ---------------------------------------------------------------- 1. UNICAF
A.append(dict(
 slug='unicaf-online-scholarship-program-2026',
 title='UNICAF Online Scholarship Programme 2026 for International Students',
 meta='UNICAF Scholarship Programme 2026: a partial online-degree scholarship covering up to 80% of tuition fees at partner universities, with the balance paid in monthly instalments. Rolling applications, monthly intakes, Bachelor’s, Master’s and Doctorate degrees studied online.',
 short='UNICAF Scholarship 2026', kicker='Online · International · Partial Scholarship', mono='UNI',
 prov_short='UNICAF', prov_cat='Online Education · International',
 h1='UNICAF Online Scholarship Programme 2026 for International Students',
 sub='Read the headline with care, because aggregator pages routinely mislabel this opportunity. UNICAF does not offer a fully funded scholarship, a visa, or an immigration pathway. What it offers is a partial tuition scholarship — up to 80% of tuition fees on UNICAF’s own page — for online degrees awarded by its partner universities, with the remaining balance paid in monthly instalments while you keep working. Applications are rolling, with monthly intakes, so there is no single closing date to miss — but there is also no fixed cash award, no stipend, and no campus place attached. If you need a degree you can study for from home at a fraction of the usual fee, and you can afford the remaining portion, this is a genuine route. If you need full funding or a study visa, it is not.',
 facts=facts([
  ('Provider', 'UNICAF (online higher-education platform, headquartered in Europe)'),
  ('Award', 'Partial tuition scholarship: up to 80% of tuition fees (UNICAF’s own page); the balance is paid by the student in monthly instalments — a fee discount, not a cash grant'),
  ('Level', 'Bachelor’s, Master’s and Doctorate (PhD, DBA, EdD), studied online (some programmes blended or on campus)'),
  ('Deadline', 'Rolling — no fixed deadline published; monthly intakes'),
  ('Eligibility', 'Meet the entry requirements of the chosen programme at the chosen partner university, and be able to pay the remaining portion of the fees; academic record and financial situation both considered'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>UNICAF is an online higher-education platform that partners with established universities to deliver their degrees at a reduced fee. UNICAF itself does not award the degree: the degree comes from the partner university, and UNICAF’s own page states that the degree title has the same value and status as one earned on that university’s campus. The partner list most often cited in current guides is the University of East London, Liverpool John Moores University and the University of Suffolk in the United Kingdom, Unicaf University (with campuses in Zambia and Malawi), and the University of California, Riverside Extension in the United States. Not every subject is offered through every partner, so the first check before applying is whether your chosen degree is actually open through a UNICAF partner at your level.</p>
      <p>The scholarship model is deliberately different from a conventional award. There is no separate scholarship competition with a closing date and a winner list. You apply for a degree through UNICAF, a Student Adviser discusses your options and the portion of fees you will need to pay, and the UNICAF Scholarship Committee and the Admissions Officer review your application and documents. If all is in order you receive an Offer Letter for the specific programme, stating the scholarship and the fees you must pay. Only after you accept the offer and pay the relevant fees do your studies begin, starting with an induction module on the virtual learning environment and a personal tutor assigned to support you through to graduation.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to 80% off tuition fees:</strong> the UNICAF Scholarship Programme can cover up to 80% of the cost of tuition fees, according to UNICAF’s own page. The exact percentage for your programme is set in your Offer Letter — it is not a guaranteed 80% for every applicant or every course.</li>
        <li><strong>Monthly instalments for the balance:</strong> the remaining fees are spread in monthly payments over the duration of your studies, so you study while you earn rather than paying a lump sum up front.</li>
        <li><strong>Study from anywhere, at your own pace:</strong> courses are delivered online through UNICAF’s digital platform, with 24/7 access to materials, so you can keep a job and family commitments. Some programmes offer blended or on-campus options through Unicaf University.</li>
        <li><strong>A recognised degree, not a UNICAF certificate:</strong> the qualification is awarded by the partner university. UNICAF’s page adds that you may attend the graduation ceremony on the relevant campus, with travel, visa and accommodation costs covered by yourself.</li>
        <li><strong>What it does not include:</strong> no living-cost stipend, no accommodation, no travel funding and no visa sponsorship are published as part of this scholarship. Aggregator claims of “fully funded” study, visa sponsorship or an immigration pathway are not supported by UNICAF’s own page and should be ignored.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Programme entry requirements:</strong> you must meet the entry requirements of the specific programme at the specific partner university — a Bachelor’s for a Master’s, a Master’s for a doctorate, and any subject or experience requirements that programme sets.</li>
        <li><strong>Able to pay the balance:</strong> UNICAF’s page is explicit that candidates should be in a position to pay the portion of fees left after the scholarship. The scholarship was set up for candidates who have the qualifications but not the funds for full fees — not for candidates who cannot pay anything.</li>
        <li><strong>Academic record and financial situation:</strong> both are taken into consideration when eligibility is assessed. UNICAF states that it aims to offer scholarships to all candidates who need them provided they have a good academic record and the required qualifications.</li>
        <li><strong>English:</strong> guides note that applicants whose first language is not English may need to evidence English proficiency, depending on the programme. Confirm the exact requirement for your programme with your adviser, since UNICAF’s own scholarship page does not publish a single test score.</li>
        <li><strong>No single nationality rule is published:</strong> current guides describe the programme as open to applicants from many countries, with awards depending on qualifications, financial ability and country of residence. Do not trust any page that promises eligibility for “all nationalities” without that qualification check.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>The online application form</strong> itself — your basic information, academic history and chosen programme — is the starting point, not a separate scholarship form.</li>
        <li><strong>Identification documents and academic transcripts</strong> or qualification certificates, as requested by your Student Adviser for your chosen programme.</li>
        <li><strong>Any further documents your adviser requests</strong> for the partner university’s admission decision. Because the document set varies by programme and partner, this article does not invent a fixed checklist: get your list from your adviser in writing before you pay anything.</li>
        <li>Get the fee breakdown in writing in your Offer Letter — the scholarship percentage, the balance you owe, and the instalment schedule — before accepting. That letter is the only reliable statement of what you will pay.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check your eligibility on the UNICAF website for the programme you want: your academic qualifications for that course, and your ability to pay the remaining fees.</li>
        <li>Complete the online application form with your basic information. A Student Adviser will call you to discuss your options, the portion of fees you will need to pay, payment plans, and any additional documents you may need.</li>
        <li>Submit the documents your adviser requests. The UNICAF Scholarship Committee and the Admissions Officer review your application and documentation.</li>
        <li>If all is in order, you receive an Offer Letter for the specific programme, stating the scholarship and the fees due. Read it carefully — especially the balance and instalment terms — before accepting.</li>
        <li>Accept the offer and pay the relevant fees, then begin with the induction module on the virtual learning environment. A personal tutor is assigned to support you until graduation.</li>
        <li>There is no fixed closing date, and intakes run monthly, so apply when your documents and finances are ready rather than rushing to a deadline that does not exist.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the UNICAF Scholarship fully funded?',
  'No. It is a partial tuition scholarship: up to 80% of tuition fees on UNICAF’s own page, with the student paying the balance in monthly instalments. Any page calling it fully funded is wrong, and any page promising a visa or immigration pathway from it is inventing a benefit UNICAF does not publish.'),
 ('What degrees can I study with a UNICAF Scholarship?',
  'Bachelor’s, Master’s and Doctorate degrees (including PhD, DBA and EdD in current guides), awarded by partner universities — most often the University of East London, Liverpool John Moores University, the University of Suffolk, Unicaf University, and the University of California, Riverside Extension. Not every subject is available through every partner.'),
 ('Is there an application deadline?',
  'No fixed deadline is published. Applications are rolling and intakes run monthly, so you apply when you are ready — but your Offer Letter, not an aggregator page, states your actual fees and start date.'),
 ('Do I need to pay anything?',
  'Yes. You pay the portion of tuition fees left after the scholarship, in monthly instalments, plus any deposit or fees stated in your Offer Letter. Get that breakdown in writing before accepting.'),
 ('Is the degree recognised?',
  'The degree is awarded by the partner university, and UNICAF’s own page states it has the same value and status as a degree earned on that university’s campus. Check the specific university and programme accreditation for your own country before enrolling, since recognition rules vary.'),
 ('Do I have to quit my job to study?',
  'No — that is the point of the model. Study is online, at your own pace and place, through UNICAF’s digital platform, so you can keep working while you study.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against UNICAF's own scholarship page (unicaf.org/change-life-unicaf-scholarship: scholarship can cover up to 80% of tuition fees; eligibility considers academic qualifications for the chosen course and financial situation; three steps - check eligibility, application page, adviser call about the portion of fees to pay, payment plans and additional documents; Scholarship Committee and Admissions Officer review, then an Offer Letter; after accepting and paying relevant fees studies begin with an induction module and a personal tutor; degrees from partner universities in the UK, US, Africa or Europe, studied online; graduation ceremony attendance at own cost) plus current guides (Bachelor's, Master's, Doctorate levels; partners University of East London, Liverpool John Moores University, University of Suffolk, Unicaf University Zambia/Malawi, University of California Riverside Extension; monthly intakes; partial scholarship paid as a discount with the balance in instalments). CONFLICTS: (1) Aggregator pages labelling this 'fully funded' with visa sponsorship and immigration pathways are REJECTED - UNICAF's own page publishes none of those. (2) No single English test score or fixed document checklist is published on UNICAF's own page, so the article states none and directs applicants to their adviser and Offer Letter. (3) Partner lists vary slightly between guides; the article uses the most commonly cited five and warns that not every subject runs through every partner.</p>''',
 dl_long='Rolling — no fixed deadline published (monthly intakes)',
 offlinks=[('UNICAF — Change Your Life with a UNICAF Scholarship (official)', 'https://www.unicaf.org/change-life-unicaf-scholarship/'),
           ('Bright Scholarship — UNICAF Online Scholarship Program 2026', 'https://brightscholarship.com/unicaf-online-scholarship-program-2026/')],
 related_titles=['harvard-mba-2027', 'unhcr-2026', 'umdearborn-2026', 'fes-2026'])),

# ---------------------------------------------------------------- 2. Harvard MBA (Boustany)
A.append(dict(
 slug='harvard-university-mba-scholarship-2027-usa',
 title='Boustany MBA Harvard Scholarship 2027 (75% of Tuition)',
 meta='Boustany MBA Harvard Scholarship 2027: 75% of Harvard Business School MBA tuition for one outstanding candidate every two years, plus a two-month Monaco internship with travel, food and accommodation covered. You must already hold a Harvard MBA offer; deadline 31 May 2027.',
 short='Boustany MBA Harvard 2027', kicker='USA · MBA · Partial Funding', mono='BOU',
 prov_short='Boustany Foundation', prov_cat='Foundation · USA',
 h1='Boustany MBA Harvard Scholarship 2027 (75% of Tuition)',
 sub='Correct the title first, because the queue title misleads almost every reader. Aggregator pages call this a “Fully Funded” Harvard scholarship. It is not. The Boustany Foundation — a private foundation independent of Harvard — pays 75% of Harvard Business School MBA tuition for one candidate, once every two years, and covers the travel, food and accommodation for a compulsory two-month internship at its Monaco office. The remaining 25% of tuition, plus living costs in Boston, remain yours to fund. There is also a hard gate most applicants miss: you may apply only after receiving an offer of admission from the Harvard MBA programme. Without that offer, there is no application at all. The deadline for the class commencing in autumn 2027 is 31 May 2027, and the award is announced in June 2027.',
 facts=facts([
  ('Provider', 'Boustany Foundation (independent of Harvard University)'),
  ('Award', '75% of Harvard MBA tuition fees for the two-year programme, for ONE candidate once every two years; two-month unpaid internship in Monaco with travel, food and accommodation covered'),
  ('Level', 'MBA — Harvard Business School, two-year programme, class commencing autumn 2027'),
  ('Deadline', '31 May 2027 (award announced June 2027)'),
  ('Eligibility', 'Excellent academic background and considerable promise; must already hold a Harvard MBA offer; any nationality, priority to candidates of Lebanese descent'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The Boustany Foundation was established in 2006 and is based in Switzerland and Monaco, with a mission of promoting access to world-class education. Its MBA scholarship at Harvard Business School is one of its flagship awards, and its scarcity is the point: it is awarded to a single outstanding candidate once every two years, not to a cohort. The Foundation’s own page states the two conditions plainly — candidates must have an excellent academic background and show considerable promise, and candidates may apply only after receiving an offer of admission from the Harvard MBA programme. Candidates of any nation may apply, although priority is given to candidates of Lebanese descent.</p>
      <p>The money needs the same plain reading. Aggregator pages repeat a total of about $102,200 in tuition support (about $51,100 a year), which is consistent with 75% of Harvard MBA tuition, but the Foundation’s own page does not restate a dollar figure for the 2027 cycle in the text checked — so this article leads with the confirmed 75% proportion rather than presenting an aggregator dollar total as the official award. The remaining 25% of tuition, plus Boston living costs, books, insurance and travel to the United States, are not covered by this scholarship and must be funded separately.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>75% of tuition fees</strong> for the full two-year Harvard MBA programme — the core award, worth roughly $102,200 in total on aggregator arithmetic, but stated here as the confirmed proportion.</li>
        <li><strong>Two-month internship in Monaco:</strong> over the summer between the two years, scholars complete an unpaid internship at the Boustany Foundation’s office in Monaco, working on increasing awareness of the Foundation, designing or proposing new scholarships, or other initiatives that further its vision. The exact project is set on the first day and can be shaped by the scholar’s interests.</li>
        <li><strong>Internship costs covered:</strong> travel, food and accommodation expenses connected to the Monaco internship are covered by the Foundation, with dates set case by case between the scholar and the Foundation.</li>
        <li><strong>Network and prestige:</strong> a single-scholar, biennial award carries weight beyond the money, and the internship gives direct experience of a philanthropic foundation’s work.</li>
        <li><strong>What is not covered:</strong> the remaining 25% of tuition, living costs in Boston, and travel to the United States for study. Do not budget as if this were full funding.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>A Harvard MBA offer first:</strong> you must already hold an offer of admission from the Harvard MBA programme before applying. This is a mandatory prerequisite, not a preference — the Foundation will not consider an application without it.</li>
        <li><strong>Excellent academic background and considerable promise:</strong> the Foundation’s own words. In practice this means a strong academic record plus the GMAT performance and leadership evidence that won the Harvard offer in the first place.</li>
        <li><strong>Any nationality:</strong> candidates of any nation may apply, with priority given to candidates of Lebanese descent. Priority is not exclusivity — non-Lebanese candidates are eligible and have won in past cycles.</li>
        <li><strong>One award, every two years:</strong> only one candidate is selected per cycle. Treat this as an exceptionally competitive, single-seat award and keep other funding plans live.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Curriculum vitae with a photograph</strong> — explicitly required by the Foundation’s own page.</li>
        <li><strong>GMAT scores</strong> — explicitly required by the Foundation’s own page.</li>
        <li><strong>Acceptance letter from Harvard Business School</strong> — the proof of the admission offer, explicitly required by the Foundation’s own page.</li>
        <li>The Foundation states that incomplete applications, or applications missing any required document, will not be considered. Submit through the Foundation’s online application form, including all information requested; older aggregator pages that direct applicants to email the documents describe an earlier route and should not be followed over the Foundation’s current form.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply to the Harvard MBA programme through Harvard Business School’s admissions route, well in advance — the scholarship deadline is meaningless without an offer in hand.</li>
        <li>Once you hold an official offer of admission, prepare your CV with a photograph, your GMAT scores, and your Harvard acceptance letter.</li>
        <li>Complete and submit your application through the Boustany Foundation’s online application form, including all information requested, before <strong>31 May 2027</strong>.</li>
        <li>If shortlisted, attend one or more interviews with the Foundation. One candidate is awarded the scholarship, announced during <strong>June 2027</strong> for the class commencing in autumn 2027.</li>
        <li>Plan the remaining 25% of tuition and your Boston living costs separately — this scholarship does not cover them — and plan the two-month Monaco internship for the summer between your two MBA years.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Boustany Harvard MBA Scholarship fully funded?',
  'No. It covers 75% of Harvard MBA tuition fees, plus travel, food and accommodation for the two-month Monaco internship. The remaining 25% of tuition and all Boston living costs are yours to fund. Aggregator pages calling it fully funded are wrong.'),
 ('Can I apply before I am admitted to Harvard Business School?',
  'No. The Foundation states that candidates may apply only after receiving an offer of admission from the Harvard MBA programme. Secure the offer first, then apply for the scholarship.'),
 ('What is the deadline for the 2027 cycle?',
  '31 May 2027 for the submission of candidacy, for the class commencing in autumn 2027. The scholarship is awarded during June 2027.'),
 ('How often is the scholarship awarded?',
  'Once every two years, to a single candidate. The 2027 cycle is the current cycle; missing it means waiting for the next biennial round.'),
 ('Do I need to be of Lebanese descent?',
  'No. Candidates of any nation may apply. Priority is given to candidates of Lebanese descent, but the award is not restricted to them.'),
 ('What documents do I need?',
  'A curriculum vitae with a photograph, your GMAT scores, and your Harvard Business School acceptance letter, submitted through the Foundation’s online application form. Incomplete applications are not considered.'),
 ('Is the Monaco internship paid?',
  'The internship itself is unpaid, but the Foundation covers travel, food and accommodation expenses connected to it. Dates are set case by case with the scholar.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the Boustany Foundation's own Harvard MBA Scholarship page (boustany-foundation.org: excellent academic background and considerable promise; apply only after receiving an offer of admission from the Harvard MBA programme; any nation, priority to candidates of Lebanese descent; online application form including CV with a photograph, GMAT scores and acceptance letter; incomplete applications not considered; if shortlisted, one or more interviews and one candidate awarded; deadline 31 May 2027; awarded June 2027; two-month unpaid summer internship in Monaco with travel, food and accommodation covered; project set on day one, scholar interests considered) plus multiple aggregator guides agreeing on 75% of tuition, one award every two years, class commencing autumn 2027, and the older email submission route. CONFLICTS: (1) Aggregator 'Fully Funded' labels are REJECTED - the award is 75% of tuition plus internship costs only. (2) The Foundation's own page does not restate a dollar total for 2027 in the text checked, so the article leads with the confirmed 75% and reports the aggregator $102,200 total only as aggregator arithmetic, not as the official figure. (3) Older aggregator pages direct applicants to email documents to the Foundation; the Foundation's current page directs applicants to its online application form, and the article follows the form. (4) One aggregator describes the MBA as a 12-month programme; Harvard's MBA is a two-year programme and the article uses two years.</p>''',
 dl_long='31 May 2027 (for the class commencing autumn 2027; award announced June 2027)',
 offlinks=[('Boustany Foundation — Harvard University MBA Scholarship (official)', 'https://boustany-foundation.org/scholarships/programs/harvard-university-mba-scholarship/'),
           ('Bright Scholarship — Harvard University MBA Scholarship 2027', 'https://brightscholarship.com/harvard-university-mba-scholarship-2027/'),
           ('ScholarPositions — Harvard University MBA Scholarship 2027', 'https://scholarpositions.com/harvard-university-mba-scholarship-2027/')],
 related_titles=['unicaf-2026', 'unhcr-2026', 'umdearborn-2026', 'fes-2026'])),

# ---------------------------------------------------------------- 3. UNHCR Internship
A.append(dict(
 slug='unhcr-internship-2026-online-apply',
 title='UNHCR Internship Programme 2026 (Rolling Applications Worldwide)',
 meta='UNHCR Internship Programme 2026: rolling 2-6 month humanitarian internships at UNHCR headquarters, global service centres and field offices for current students and recent graduates. No programme-wide deadline — each vacancy has its own closing date; support is an allowance, not a salary.',
 short='UNHCR Internship 2026', kicker='Worldwide · Internship · Rolling', mono='UNH',
 prov_short='UNHCR', prov_cat='United Nations · Worldwide',
 h1='UNHCR Internship Programme 2026 (Rolling Applications Worldwide)',
 sub='Two corrections before anything else, because aggregator pages get both wrong. First, this is not a single programme with a single deadline: UNHCR internships are offered on an ongoing basis throughout the year, and each advertised vacancy carries its own closing date — there is no programme-wide deadline to quote, and any page that invents one is guessing. Second, this is not a salaried job and not “fully funded” in the usual sense: interns who receive no external financial support may receive a food and local transport allowance set as a percentage of a UN salary scale at the duty station, plus return travel reimbursement in some cases, while visa costs and medical and evacuation insurance remain the intern’s responsibility. What the programme genuinely offers is two to six months inside the UN refugee agency — at headquarters in Geneva, a global service centre, or a field office — doing real protection, policy, communications or operations work.',
 facts=facts([
  ('Provider', 'United Nations High Commissioner for Refugees (UNHCR)'),
  ('Award', 'Allowance, not a salary: interns without external funding may receive a food and local transport allowance (70% of GS-3 Step 1 net salary at most duty stations, 50% at hardship stations; part-time at 50% of the applicable rate); return travel reimbursed in some cases; visa and insurance costs are the intern’s own'),
  ('Level', 'Internship — current students and recent graduates (2-6 months, extendable within cumulative limits)'),
  ('Deadline', 'Rolling — no programme-wide deadline; each vacancy has its own closing date'),
  ('Eligibility', 'Current student or recent graduate (within 2 years) from a UNESCO-accredited institution; at least 2 years of undergraduate study completed; English B2 minimum; no immediate relatives working for UNHCR'),
 ]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>UNHCR, the UN Refugee Agency, offers internships across its global operations: headquarters in Geneva, global service centres in Amman, Budapest and Copenhagen, and country and field offices on every continent, with remote or telework arrangements possible where the manager approves. Interns work on a project that benefits both them and the office — in refugee protection and legal work, international relations, administration, communications, programme and policy management, fundraising, research and data, or emergency and field operations. Placements normally last between two and six months, can begin at any time of year depending on office needs, and may be extended within strict cumulative limits: up to eight months in total for full-time internships and up to twelve months for part-time internships, including any prior UNHCR internships.</p>
      <p>The application route is vacancy by vacancy, not a single annual call. UNHCR’s own UK frequently-asked-questions page states that internships are offered on an ongoing basis throughout the year depending on the availability of meaningful assignments, and that there is no deadline for sending in an application form — meaning no central deadline, not that individual vacancies stay open forever. In practice you register on UNHCR’s recruitment platform, watch for internship requisitions that match your education and skills, and apply to each one before its stated closing date. An internship creates no expectation of employment with UNHCR afterwards, and UNHCR charges no fee at any stage of recruitment — any request for payment is a fraud signal, not a normal step.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Real humanitarian experience:</strong> hands-on work on refugee protection and displacement response, under experienced staff, in a global, multicultural organisation — the core value of the placement, and the reason it is competitive.</li>
        <li><strong>Food and local transport allowance:</strong> interns who do not receive financial support from an outside party (for example a university stipend) may receive an allowance to partially cover food and local transport. Current vacancy guidance sets it at 70% of the GS-3 Step 1 net salary at most duty stations and 50% at hardship-category stations, with part-time interns at 50% of the applicable rate. The amount therefore varies by duty station and is not a fixed monthly salary.</li>
        <li><strong>Return travel reimbursement in some cases:</strong> if you are recruited from outside the duty-station country, UNHCR may reimburse return travel by the most economical route. Visa costs are not reimbursed.</li>
        <li><strong>Remote options:</strong> some offices offer remote or telework internships if the manager approves, and current guidance states remote internships are also paid on the same allowance basis.</li>
        <li><strong>What is not covered:</strong> you must arrange your own medical insurance covering accidents, illness and emergency evacuation before starting, and you are responsible for your legal stay, housing and visa costs. Older UNHCR guidance stating that no financial support is provided at all is outdated against current vacancy terms — but equally, no vacancy guarantees the allowance regardless of your funding position, so read each posting’s financial terms before applying.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Student or recent graduate:</strong> a current student in a graduate or undergraduate programme, or a recent graduate — defined as having completed studies within two years of applying — from a university or higher-education institution accredited by UNESCO.</li>
        <li><strong>Two years of undergraduate study:</strong> undergraduate applicants must have completed at least two years of study in a field relevant to, or of interest to, the work of the organisation.</li>
        <li><strong>English at B2 minimum:</strong> proficiency in English at a minimum B2 level is required; other UN languages such as French, Arabic or Spanish are an advantage depending on the duty station. No IELTS certificate is specifically required — proficiency, not a test score, is the stated rule.</li>
        <li><strong>No immediate relatives at UNHCR:</strong> applicants must not have immediate relatives (father, mother, brother or sister) working for UNHCR as staff on any contract type or as an affiliate at the time of application.</li>
        <li><strong>Cumulative limits not exhausted:</strong> you must not have already used up the maximum cumulative internship period with UNHCR (eight months full-time, twelve months part-time, including prior internships).</li>
        <li><strong>All nationalities:</strong> internships are open to applicants of all nationalities, subject to the vacancy’s location, language and visa conditions. UNHCR states it particularly encourages applications from women, refugees, stateless people and candidates from underrepresented regions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>An online profile and application on UNHCR’s recruitment platform</strong> — applications must be submitted in English, and only fully completed applications are accepted. Individual vacancies state their own required fields and files, and there is no verified universal document package that replaces the vacancy instructions.</li>
        <li><strong>A CV and a tailored letter of interest</strong> for the specific vacancy, explaining your availability (full-time or part-time), your relevant education and skills, and why that office’s work fits you. Some vacancies also request a short writing sample.</li>
        <li><strong>Proof of student or recent-graduate status and academic background</strong> as the vacancy requires, plus evidence of English proficiency where the posting asks for it.</li>
        <li>Do not send applications by email unless a specific vacancy instructs it: the standard route is the online portal, and only shortlisted candidates are contacted.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Register and complete your profile on UNHCR’s official recruitment platform, linked from the UNHCR careers pages.</li>
        <li>Search current internship requisitions (vacancies) by location, office and field, and shortlist only those matching your education, languages and availability.</li>
        <li>Read each vacancy in full before applying: its closing date, its duty station, its full-time or part-time pattern, its language requirements, and its financial terms — especially whether an allowance applies to your situation.</li>
        <li>Submit the portal application in English before that vacancy’s closing date, with your CV, letter of interest and any writing sample or document the posting requests. Save your draft regularly and keep the system confirmation.</li>
        <li>Arrange your own medical and evacuation insurance and check your visa and legal-stay requirements for the duty station while you wait. Only shortlisted candidates are contacted, so keep applying to suitable vacancies rather than waiting on one.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the UNHCR internship paid?',
  'It is not a salary. Interns without external funding may receive a food and local transport allowance — 70% of the GS-3 Step 1 net salary at most duty stations, 50% at hardship stations, part-time at half the applicable rate — plus return travel reimbursement in some cases. Visa costs and medical and evacuation insurance are your own responsibility.'),
 ('What is the deadline for the UNHCR Internship Programme 2026?',
  'There is no programme-wide deadline. Internships are offered on an ongoing basis all year, and each vacancy has its own closing date. Apply to individual vacancies before their stated dates.'),
 ('How long does an internship last?',
  'Normally two to six months, extendable within cumulative limits of eight months for full-time and twelve months for part-time internships, including any prior UNHCR internships.'),
 ('Who can apply?',
  'Current students or recent graduates (within two years) from a UNESCO-accredited institution, with at least two years of undergraduate study completed, English at B2 minimum, and no immediate relatives working for UNHCR. All nationalities may apply.'),
 ('Where can I intern?',
  'At UNHCR headquarters in Geneva, global service centres in Amman, Budapest and Copenhagen, or country and field offices worldwide. Some offices offer remote internships with manager approval. Not every office offers internships regularly, and some cannot for security reasons.'),
 ('Does an internship lead to a UNHCR job?',
  'No. An internship creates no expectation or entitlement to employment with UNHCR at its conclusion, although the experience is valued for later UN applications.'),
 ('Do I need IELTS?',
  'No specific IELTS score is stated. English proficiency at a minimum B2 level is required, and other UN languages are an advantage depending on the duty station.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against UNHCR's own UK internship FAQ (unhcr.org/uk: internships normally no less than two months and no more than six months; offered on an ongoing basis throughout the year with no central deadline; headquarters and family duty stations in the field; work depends on unit needs) plus current vacancy guidance and programme guides agreeing on: recent graduate or current student from a UNESCO-accredited institution, at least two years of undergraduate study, no immediate relatives at UNHCR, cumulative limits of 8 months full-time / 12 months part-time, English B2 minimum, allowance of 70% GS-3 Step 1 (50% hardship stations, part-time at 50% of the applicable rate), return travel reimbursement where recruited from outside the duty-station country, intern's own visa and medical/evacuation insurance, no recruitment fee, and no expectation of employment. CONFLICTS: (1) The older UNHCR UK FAQ line 'UNHCR does not provide any financial support for interns' conflicts with current vacancy guidance on the food and local transport allowance; the article follows current vacancy terms and states the allowance as conditional on having no external funding. (2) Aggregator 'Fully Funded' labels are REJECTED - this is an allowance, not full funding. (3) A single vacancy listing's $1,642.75 monthly figure is a duty-station-specific posting amount, not a universal rate, and is not stated as the programme rate. (4) No fixed document checklist is published programme-wide; the article states the vacancy-specific position honestly.</p>''',
 dl_long='Rolling — no programme-wide deadline (each vacancy has its own closing date)',
 offlinks=[('UNHCR — Internships: Frequently Asked Questions (official)', 'https://www.unhcr.org/uk/publications/internships-unhcr-frequently-asked-questions'),
           ('UNHCR — Careers (official portal route)', 'https://www.unhcr.org/careers'),
           ('Bright Scholarship — UNHCR Internship 2026 Online Apply', 'https://brightscholarship.com/unhcr-internship-2026-online-apply/')],
 related_titles=['unicaf-2026', 'harvard-mba-2027', 'umdearborn-2026', 'fes-2026'])),

# ---------------------------------------------------------------- 4. Michigan-Dearborn
A.append(dict(
 slug='university-of-michigan-dearborn-scholarship-2026-usa',
 title='University of Michigan-Dearborn Scholarship 2026 in USA (Funded)',
 meta='University of Michigan-Dearborn Scholarship 2026: merit awards of $5,000-$12,500 a year for international and non-resident undergraduates, set by GPA at admission and automatically considered on admission. Deadline 15 November 2026.',
 short='Michigan-Dearborn 2026', kicker='USA · Undergraduate · Merit', mono='UMD',
 prov_short='University of Michigan-Dearborn', prov_cat='University · USA',
 h1='University of Michigan-Dearborn Scholarship 2026 in USA (Funded)',
 sub='Do not budget on the single figure most aggregator pages repeat. There is no flat $10,000 award here, and there is certainly no $50,000 award for every recipient — $50,000 is only the four-year total at the very top tier. The University of Michigan-Dearborn’s non-resident undergraduate merit awards are a four-step ladder set by your GPA at admission: $5,000 a year at GPA 3.00-3.24, $7,500 at 3.25-3.49, $10,000 at 3.50-3.99, and $12,500 at 4.00 or higher, renewable for up to eight semesters for freshmen if you keep a 3.0 GPA and complete 24 credits a year. The good news is procedural: eligible applicants are automatically considered when they apply for admission — there is no separate scholarship form. The deadline most guides report for international merit awards is 15 November 2026, so an application still in draft in late October is genuinely urgent.',
 facts=facts([
  ('Provider', 'University of Michigan-Dearborn, Michigan, USA'),
  ('Award', 'Non-resident undergraduate merit award by GPA at admission: $5,000/year (3.00-3.24), $7,500 (3.25-3.49), $10,000 (3.50-3.99), $12,500 (4.00+); renewable up to 8 semesters (freshmen) / 6 semesters (transfers)'),
  ('Level', 'Undergraduate — first-year and transfer students, full-time degree-seeking'),
  ('Deadline', '15 November 2026 (reported deadline for most international merit-based undergraduate scholarships)'),
  ('Eligibility', 'International or out-of-state students with GPA 3.0+ at admission; English proficiency (IELTS 6.5 / TOEFL iBT 80 in older international criteria); automatically considered on admission'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The University of Michigan-Dearborn, part of the University of Michigan system in the Detroit metropolitan area, offers merit scholarships that reduce tuition for non-resident students, including international students. The central award for this article is the undergraduate non-resident scholarship for incoming first-year students: a merit ladder published in the university’s 2026-2027 scholarship information and corroborated by several independent guides. Your award is set by the GPA on your record at the time of admission, not by a later application or interview, and it is reviewed automatically when you apply — which is why the admission deadline effectively is the scholarship deadline.</p>
      <p>Two neighbouring awards are often confused with this one, so keep them separate. The Great Lakes Scholarship gives eligible non-resident students from Illinois, Indiana, Minnesota, New York, Ohio, Pennsylvania, Wisconsin or Ontario (Canada) in-state tuition — it is a residency-based award, not available to most international students outside that region. The tuition-differential scholarship covers Michigan residents initially classified as out-of-state. Neither is the international merit ladder in this article, and neither should be quoted as its value.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>GPA 4.00 or higher:</strong> $12,500 a year, $50,000 over four years — the only route to the $50,000 total some aggregator pages quote for everyone.</li>
        <li><strong>GPA 3.50-3.99:</strong> $10,000 a year, $40,000 over four years — the figure most aggregator pages present as the single award.</li>
        <li><strong>GPA 3.25-3.49:</strong> $7,500 a year, $30,000 over four years.</li>
        <li><strong>GPA 3.00-3.24:</strong> $5,000 a year, $20,000 over four years — the entry tier, and the reason a GPA just below 3.25 or 3.50 is worth real money to improve before applying.</li>
        <li><strong>Renewal:</strong> renewable for up to eight semesters for freshmen or six semesters for transfer students, or until bachelor’s degree completion, provided you maintain at least a 3.0 cumulative GPA and complete 24 credit hours per academic year (fall and winter semesters).</li>
        <li><strong>Automatic consideration:</strong> for the listed undergraduate merit awards, the university states that students do not need a separate scholarship application — eligible applicants are automatically reviewed on residency and academic information supplied during admission.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>First-year or transfer undergraduates:</strong> international or out-of-state students admitted to a full-time, degree-seeking undergraduate programme at UM-Dearborn.</li>
        <li><strong>GPA of 3.0 or higher</strong> on a 4.0 scale at admission — the minimum for the ladder, with the award level set by the exact band above. The GPA used is the one at the time of admission.</li>
        <li><strong>English proficiency:</strong> the older international criteria list IELTS 6.5, TOEFL iBT 80 (CBT 213, PBT 550) or MELAB 76. The university now operates a test-optional policy for most undergraduate courses, so confirm the current English and test requirements for your programme on the university’s admissions pages rather than treating the older list as the only route.</li>
        <li><strong>Test scores where submitted:</strong> the older international criteria also list a combined SAT score of at least 1020 (or ACT composite 20) for freshmen, and a GPA of 3.5 for transfer students, with fewer than 24 transfer credits also requiring the SAT/ACT and high-school transcripts. Under test-optional admissions these scores are not the universal gate they once were — confirm before assuming you must sit a test.</li>
        <li><strong>Full-time enrolment and progress:</strong> maintain a 3.0 cumulative GPA and 24 credits a year to renew. Changes in residency status may affect eligibility.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>The undergraduate admission application</strong> itself, with accurate permanent-address and residency information — this is the document the automatic scholarship review runs on, so errors here cost money.</li>
        <li><strong>Official academic transcripts</strong> (high-school transcripts for freshmen, and college transcripts for transfer students) showing the GPA the award band is set from.</li>
        <li><strong>English proficiency evidence</strong> where required for your programme (IELTS, TOEFL or an accepted equivalent).</li>
        <li><strong>SAT or ACT scores where submitted</strong> under the older criteria or where your programme still asks for them, plus any programme-specific documents the admissions pages list.</li>
        <li>Some guides also list a recommendation letter, personal statement and financial support letter for the wider international application; the merit award itself is automatic on admission, so treat those as admission documents, not a separate scholarship file.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to an undergraduate programme at the University of Michigan-Dearborn as a first-year or transfer student, through the university’s application portal, before <strong>15 November 2026</strong> — the reported deadline for most international merit-based undergraduate scholarships.</li>
        <li>Supply complete transcripts and residency information, and respond promptly if the university asks for additional documentation to verify eligibility.</li>
        <li>There is no separate scholarship application for the listed merit awards: eligible applicants are automatically reviewed. Do not wait for a scholarship form that does not exist.</li>
        <li>Check your offer and award letter for the exact tier (your GPA band) and the renewal terms, and confirm the current test and English requirements for your programme before making financial commitments.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Michigan-Dearborn Scholarship 2026?',
  '15 November 2026, the date reported by multiple guides — and confirmed in substance by a study-abroad guide — as the last date for most international merit-based undergraduate scholarships. Complete your admission application by this date, since the merit review runs on admission.'),
 ('How much is the scholarship worth?',
  'It depends on your GPA at admission: $5,000 a year at GPA 3.00-3.24, $7,500 at 3.25-3.49, $10,000 at 3.50-3.99, and $12,500 at 4.00 or higher. Over four years that is $20,000, $30,000, $40,000 or $50,000 respectively. There is no flat $10,000 or flat $50,000 award for everyone.'),
 ('Is there a separate scholarship application?',
  'No, for the listed undergraduate merit awards. Eligible applicants are automatically reviewed on the residency and academic information in their admission application.'),
 ('Do I need SAT or ACT scores?',
  'The older international criteria list SAT 1020 or ACT 20, but the university now operates a test-optional policy for most undergraduate courses. Confirm the current requirement for your programme rather than assuming a test is mandatory.'),
 ('What English score do I need?',
  'The older international criteria list IELTS 6.5, TOEFL iBT 80, or MELAB 76. Confirm the current English requirement for your programme on the university’s admissions pages, since requirements vary by course.'),
 ('How do I keep the scholarship?',
  'Maintain at least a 3.0 cumulative GPA and complete 24 credit hours per academic year. The award renews for up to eight semesters for freshmen or six for transfer students, or until you complete your bachelor’s degree.'),
 ('Does the Great Lakes Scholarship apply to international students?',
  'Generally no. The Great Lakes Scholarship gives in-state tuition to non-residents from listed neighbouring states and Ontario, Canada. It is a separate, residency-based award from the international merit ladder in this article.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against three independent guides corroborating the university's published 2026-2027 information: the GPA tier table ($12,500 at 4.00+ / $50,000 over four years; $10,000 at 3.50-3.99 / $40,000; $7,500 at 3.25-3.49 / $30,000; $5,000 at 3.00-3.24 / $20,000; renewal at 3.0 GPA and 24 credits a year, up to 8 semesters freshmen / 6 semesters transfers; automatic review on admission, no separate application) plus the older international criteria (freshmen GPA 3.0, SAT 1020 / ACT 20; transfers GPA 3.5; IELTS 6.5 / TOEFL iBT 80 / MELAB 76) and the 15 November 2026 deadline reported by multiple guides and confirmed in substance for most international merit undergraduate scholarships. CONFLICTS: (1) Aggregator pages quoting a flat $10,000 a year (or a flat $50,000 total) for every recipient are REJECTED - the award is the four-tier GPA ladder above. (2) A $50,000 total on some pages alongside a $10,000 annual figure is arithmetically inconsistent ($10,000 x 4 = $40,000); the $50,000 total belongs only to the $12,500 top tier. (3) Older SAT/ACT and English lists conflict with the university's current test-optional policy for most undergraduate courses; the article states both and directs applicants to confirm current programme requirements. (4) No official UM-Dearborn scholarship page was surfaced by search for direct quotation, so the article relies on three corroborating guides and flags that limitation; the deadline and tier figures agree across all three.</p>''',
 dl_long='15 November 2026 (reported deadline for most international merit-based undergraduate scholarships)',
 offlinks=[('Bright Scholarship — University of Michigan Dearborn Scholarship 2026', 'https://brightscholarship.com/university-of-michigan-dearborn-scholarship-2026/'),
           ('ScholarshipsEdge — UM-Dearborn Undergraduate Scholarships 2026', 'https://scholarshipsedge.com/university-of-michigan-dearborn-undergraduate-scholarships/'),
           ('ScholarsAfrica — UM-Dearborn Scholarships 2026-2027', 'https://scholarsafrica.org/university-of-michigan-dearborn-scholarships-2026-2027-eligibility-benefits-and-how-to-apply/')],
 related_titles=['unicaf-2026', 'harvard-mba-2027', 'unhcr-2026', 'fes-2026'])),

# ---------------------------------------------------------------- 5. Friedrich Ebert Foundation
A.append(dict(
 slug='friedrich-ebert-foundation-scholarship-2026-germany',
 title='Friedrich Ebert Foundation Scholarship 2026 in Germany (Fully Funded)',
 meta='Friedrich Ebert Foundation (FES) Scholarship 2026 for international students in Germany: a monthly stipend (EUR 992 a month in the latest guide), health insurance and family allowance, for students from the Global South and eastern Europe with strong academics and social commitment. Master’s winter deadline 30 November 2026.',
 short='Friedrich Ebert 2026', kicker='Germany · Bachelor’s, Master’s & PhD · Fully Funded', mono='FES',
 prov_short='Friedrich Ebert Foundation', prov_cat='Foundation · Germany',
 h1='Friedrich Ebert Foundation Scholarship 2026 in Germany (Fully Funded)',
 sub='This scholarship is narrower, and more demanding, than its “fully funded” label suggests — and that narrowness is exactly why it is worth understanding properly. The Friedrich-Ebert-Stiftung (FES) funds international students who are already studying in Germany, not applicants still sitting at home hoping for a ticket: guides summarising the programme state that you must already be in Germany, that you must not have been in Germany longer than 15 months when you apply (with exemptions), and that flights are not covered. The award itself is generous — a monthly stipend, health insurance costs, and a child allowance, with nothing to repay — but the selection weighs something most scholarships ignore: proven social and political commitment to the values of social democracy, alongside outstanding academic merit. And the deadline in this article, 30 November 2026, is specifically the Master’s deadline for the winter semester; Bachelor’s and doctoral applicants follow different timing rules, not this date.',
 facts=facts([
  ('Provider', 'Friedrich-Ebert-Stiftung (FES), Germany'),
  ('Award', 'Monthly stipend EUR 992/month for students (latest guide; older pages list EUR 934, EUR 850 or EUR 750); doctoral candidates EUR 1,500/month (latest guide); health insurance costs covered for students; child allowance EUR 255/month (German programme page) or EUR 276 (English summary); nothing repayable; flights NOT covered'),
  ('Level', 'Bachelor’s, Master’s, Diplom, Staatsexamen and doctorate, at any state or state-recognised university or Fachhochschule in Germany'),
  ('Deadline', '30 November 2026 for Master’s (winter semester); 31 May 2027 for Master’s (summer semester); Bachelor’s and doctoral applicants follow timing rules instead of a fixed calendar date'),
  ('Eligibility', 'International students from the Global South, former CIS states and eastern/south-eastern Europe (OECD nationals excluded); outstanding merit plus social/political commitment to social-democratic values; German B2; not longer than 15 months in Germany at application (exemptions apply)'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The Friedrich-Ebert-Stiftung, founded in 1925, is Germany’s oldest political foundation, and its scholarship programme is one of the country’s most established routes for talented students who combine academic excellence with social engagement. The international programme — Grundförderung and Promotionsförderung für Ausländer:innen — supports students from Africa, Asia, Latin America, the former CIS states and eastern and south-eastern Europe, at any state or state-recognised university or Fachhochschule in Germany, in any subject. Around 40 international scholarships are awarded each year according to current guides, from thousands of applicants, so this is a highly competitive award where the motivation and engagement evidence matter as much as grades.</p>
      <p>The programme’s design explains its unusual rules. Because FES scholars join a seminar programme and a network, and are expected to take part in the Foundation’s life, the Foundation looks for people already embedded in Germany: applicants are expected to be studying in Germany already, and the 15-month residency limit at application (with exemptions) keeps the cohort at a similar stage. The application itself is in German only, and German at B2 is required even if your degree programme or dissertation is in English — a rule that surprises many applicants who assumed an English-taught Master’s would exempt them. It does not.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend:</strong> EUR 992 a month for students, flat and not means-tested, in the latest guide. Older pages list EUR 934, EUR 850 (Master’s) and EUR 750 (Bachelor’s) — the article leads with the current EUR 992 figure and reports the older figures as superseded, not as alternatives you can choose between.</li>
        <li><strong>Doctoral funding:</strong> EUR 1,500 a month in the latest guide, normally for three and a half years, extendable in justified exceptional cases to the final examination at the latest.</li>
        <li><strong>Health insurance:</strong> health insurance costs are covered for students, with a contribution towards statutory insurance for doctoral candidates.</li>
        <li><strong>Child allowance:</strong> EUR 255 a month on the German programme page, EUR 276 on the English summary page — the article states both and tells you to confirm the current figure on the official page, since the two published figures disagree.</li>
        <li><strong>No repayment, no tuition line:</strong> the scholarship does not have to be repaid. Tuition fees are not listed among what FES covers — but most German public universities charge no tuition, only a semester contribution, so the stipend plus insurance is effectively full living-cost funding for most recipients.</li>
        <li><strong>Seminar programme and mentoring:</strong> scholars join a comprehensive seminar programme, receive mentoring, and are expected to submit a semester report on academic performance and social participation each term.</li>
        <li><strong>What is not covered:</strong> flights to Germany are not covered, and you must already be in Germany to fit the programme’s design. Any income above EUR 400 a month is credited against the stipend.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Region:</strong> international students from the Global South (Asia, Africa, Latin America), the former CIS states, and eastern and south-eastern European states. Nationals of OECD states — including the United States, Australia, New Zealand and Japan — are excluded from this international route.</li>
        <li><strong>Already studying in Germany:</strong> the programme is designed for students already enrolled at a German university or Fachhochschule, who have not been in Germany longer than 15 months at the time of application, with exemptions. If you are still in your home country, this is not the right FES route.</li>
        <li><strong>Outstanding academic merit:</strong> strong school or university results, with first graded proofs of academic achievement where required.</li>
        <li><strong>Social and political commitment:</strong> proven social and political involvement and commitment to the values of social democracy — freedom, justice and social cohesion — plus responsible, motivated and reliable character and willingness to engage with the Foundation’s network. This is a scored criterion, not a formality.</li>
        <li><strong>German at B2:</strong> sufficient German is required even if your courses are in English, and the application itself is in German only. Other guides cite higher certificates (DSH Level 2, TestDaF Level 4, Goethe C1) — the article states B2 as the programme’s stated minimum and warns you to confirm the certificate actually accepted for your case on the official page.</li>
        <li><strong>Degree levels:</strong> Bachelor’s, Master’s, Diplom, Staatsexamen and doctorate. Doctoral applicants need an unconditional admission to doctoral study at a German university.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>The online application form first:</strong> FES operates a two-stage process. You complete the online application form; if you are eligible, the Foundation requests additional documents from you by email. Do not assemble a full file before that screening step and do not expect a single published checklist to replace the Foundation’s request.</li>
        <li><strong>Academic records</strong> — transcripts and certificates showing your outstanding merit, with first graded proofs where required — requested at the document stage.</li>
        <li><strong>Evidence of social and political engagement</strong> — the material that proves your commitment to social-democratic values and your involvement in your community or organisations.</li>
        <li><strong>Proof of enrolment at a German university</strong> and, for doctoral applicants, unconditional admission to doctoral study, plus German-language evidence at the required level.</li>
        <li><strong>A motivation account</strong> setting out your academic path, your engagement, and why FES’s programme fits you — the document on which the engagement criterion is largely judged.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm you fit the international route: eligible region, already studying in Germany within the 15-month limit (or an exemption), German at B2, and genuine social and political engagement to evidence.</li>
        <li>Complete the online application form on the FES website (in German) for the correct deadline: <strong>30 November 2026</strong> for a Master’s scholarship for the winter semester, or <strong>31 May 2027</strong> for the summer semester. Bachelor’s and doctoral applicants follow the programme’s timing rules instead of these fixed dates — check the official page for your category.</li>
        <li>Wait for the Foundation’s response. If you are eligible, FES requests additional documents by email; the full review can take several weeks to a few months, and shortlisted candidates are invited to an interview (in person or by video).</li>
        <li>If selected, accept the scholarship and follow the acceptance instructions, including the semester reporting duty and seminar participation.</li>
        <li>There is no application fee. If anyone asks you to pay to apply for FES funding, it is not the Foundation.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Friedrich Ebert Foundation Scholarship 2026?',
  '30 November 2026 for Master’s scholarships for the winter semester, and 31 May 2027 for the summer semester. PhD candidates may apply at any time, and Bachelor’s applicants follow timing rules rather than a single fixed date — check the official page for your category.'),
 ('How much does the FES Scholarship pay?',
  'EUR 992 a month for students in the latest guide, and EUR 1,500 a month for doctoral candidates, plus health insurance costs and a child allowance (EUR 255 on the German page, EUR 276 in the English summary). Older figures of EUR 934, EUR 850 and EUR 750 appear on older pages and are superseded. Nothing is repayable, and income above EUR 400 a month is credited against the stipend.'),
 ('Can I apply from my home country?',
  'Not on this international route as summarised in current guides: the programme is designed for students already studying in Germany, not longer than 15 months in Germany at application (with exemptions), and flights are not covered.'),
 ('Do I need German if my degree is in English?',
  'Yes. German at B2 is required even if your programme or dissertation is in English, and the application itself is in German only. Some guides cite higher certificates, so confirm the accepted evidence on the official page.'),
 ('Who cannot apply?',
  'Nationals of OECD states, including the United States, Australia, New Zealand and Japan, are excluded from this international route. German students apply through a separate FES route.'),
 ('Is there an application fee?',
  'No. The FES scholarship application is free of charge.'),
 ('How competitive is it?',
  'Highly competitive: current guides report up to 40 international scholars selected annually from thousands of applicants. Strong academics, authentic social engagement and a compelling motivation account are what distinguish winners.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the latest programme guide (Master's deadlines 30 Nov 2026 winter / 31 May 2027 summer; Bachelor's and doctoral timing rules instead of a fixed date; students EUR 992/month flat, doctoral EUR 1,500/month, 3.5 years as a rule; health insurance covered for students; child allowance EUR 255 German page vs EUR 276 English summary; German B2 accepted without a certificate, application in German only; residency not longer than 15 months with exemptions; income above EUR 400/month credited; Global South, former CIS and eastern/south-eastern Europe eligible, OECD excluded; flights not covered; no repayment) plus the Bright Scholarship page and other guides agreeing on the 30 Nov 2026 winter deadline, any state/state-recognised university or Fachhochschule, all subjects, up to 40 awards a year, and the online-form-then-documents-by-email route. CONFLICTS: (1) Stipend figures conflict across vintages (EUR 992 current vs EUR 934 / EUR 850 / EUR 750 older) - the article leads with the current figure and labels the rest superseded. (2) Child allowance is EUR 255 on the German page but EUR 276 in the English summary - both are stated. (3) German evidence conflicts (B2 minimum vs DSH 2 / TestDaF 4 / Goethe C1 in other guides) - the article states B2 as the programme minimum and warns applicants to confirm. (4) One aggregator claims the programme is 'run by DAAD' - rejected; FES is an independent foundation, and DAAD does not run it. (5) 'Fully funded' is used in the title as the queue title, but the article clarifies the precise scope: stipend plus insurance, no tuition line published, no flights, and a semester contribution may still apply.</p>''',
 dl_long='30 November 2026 for Master’s (winter semester); 31 May 2027 for Master’s (summer semester); Bachelor’s and doctoral applicants follow timing rules instead',
 offlinks=[('Friedrich-Ebert-Stiftung — Scholarship Application (official)', 'https://www.fes.de/studienfoerderung/bewerbung'),
           ('Bright Scholarship — Friedrich Ebert Foundation Scholarship 2026', 'https://brightscholarship.com/friedrich-ebert-foundation-scholarship-2026/'),
           ('OpportunitiesNexus — Friedrich Ebert Foundation Scholarship 2027', 'https://opportunitiesnexus.com/friedrich-ebert-foundation-scholarship-2027/')],
 related_titles=['unicaf-2026', 'harvard-mba-2027', 'unhcr-2026', 'umdearborn-2026'])),

DPILLS = {
 'unicaf-online-scholarship-program-2026': 'Rolling · no fixed deadline published',
 'harvard-university-mba-scholarship-2027-usa': 'Deadline 31 May 2027 · %d days left' % dl_left('2027-05-31'),
 'unhcr-internship-2026-online-apply': 'Rolling · per-vacancy deadlines',
 'university-of-michigan-dearborn-scholarship-2026-usa': 'Deadline 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
 'friedrich-ebert-foundation-scholarship-2026-germany': 'Deadline 30 Nov 2026 · %d days left' % dl_left('2026-11-30'),
}

for a in A:
    a['dpill'] = DPILLS[a['slug']]
    _split_verify(a)
    n = build_article(BASE, OUT, a, CARDS)
    print('built', a['slug'], n)

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

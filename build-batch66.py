#!/usr/bin/env python3
"""Batch 66 (cron run 66, 29 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
- U of Manitoba Scholarships 2026 - SKIPPED: umbrella, not a single scheme;
  Bright "fully funded" claims rejected (main entrance award is a partial
  CAD 1,000-3,000 award, not tuition plus stipend plus housing).
- UI GREAT Scholarship 2026 - SKIPPED: deadline passed 4 May 2026.
- UTS RTP Scholarships 2026 - SKIPPED: latest official round closed 23 Sep 2026.
- Croatian Government Scholarship 2026 - SKIPPED: deadline passed 10 Apr 2026.
- Humboldt Research Fellowship 2026 - WRITTEN with corrected framing: current
  call closed at its 800-application cap; next call opens 15 Nov 2026.
- University of Winnipeg Scholarship 2026 - SKIPPED: umbrella, 2026-27 cycle closed.
- University of Rochester iScholar 2026 - SKIPPED: deadline passed 23 Jan 2026
  (aggregator 1 Dec 2026 date is wrong for the 2026 cycle).
- Google Summer of Code GSoC 2026 - SKIPPED: contributor deadline passed
  31 Mar 2026.
- WTO Young Trade Leaders Program 2026 - SKIPPED: deadline passed 1 May 2026;
  also unpaid, so "fully funded" labels are misleading.
- IFAD Internship Program 2026 - WRITTEN (rolling, monthly allowance, amount
  not published on the official page).
- Abu Dhabi University Scholarships 2026 - SKIPPED: umbrella (many schemes);
  the only 100% scheme is closed to international students.
- University of Alberta Scholarships 2026 - SKIPPED: umbrella, no single
  deadline or award; "fully funded" label not supported.
- CERN Short Term Internship 2026 - WRITTEN (deadline 1 Nov 2026, CHF 1,593/month).
- Salford International Excellence Scholarship 2026 - SKIPPED: aggregator
  14 Jul 2026 date passed; official award is the automatic Global Gold
  Excellence Scholarship, with no separate application.
- University of Trento Scholarships 2026 - SKIPPED: umbrella; main 2026/27
  deadlines passed (MISS/MEIS 4 Mar 2026, FUTURA 30 Mar 2026).
- University of Hamburg Merit Scholarships 2026 - SKIPPED: official page
  states no further calls are planned.
- MS, PhD Scholarships in Australia 2026 - SKIPPED: listicle.
- Bellagio Center Residency Program 2027 - SKIPPED: deadline passed 20 Mar 2026.
- WIPO Roster Internship 2026 - SKIPPED: 2026 roster closed 3-4 Jul 2026.
- Canada ASEAN Scholarships 2026 - SKIPPED: deadline passed 24 Mar 2026.
- Scholarships in Czech Republic Without IELTS 2026 - SKIPPED: listicle.
- New York University Stern Fellowship 2026 - SKIPPED: deadline passed
  20 Apr 2026 (real scheme is the Climate Economics Journalism Fellowship,
  not a PhD fellowship).
- ScottishPower Masters Scholarship 2026 - SKIPPED: deadline passed 29 Mar 2026.
- Korea University SK Global Scholarship 2026 - SKIPPED: deadline passed
  31 Mar 2026.
- Study in Albania Without IELTS 2026 - SKIPPED: listicle.
- University of Huddersfield Scholarships 2026 - WRITTEN with reframing:
  automatic merit tuition discounts, no separate scholarship application;
  January 2027 entry, Early Payment Discount 31 Oct 2026.
- Universities in Canada with Low Tuition 2026 - SKIPPED: listicle.
- BTU STIBET I Scholarship Program 2026 - SKIPPED: deadline passed 31 Jul 2026.
- Summer Programs in Europe 2026 - SKIPPED: listicle.
- New Zealand Universities Without IELTS 2026 - SKIPPED: listicle.
- TUM International Student Scholarship 2026 - SKIPPED: latest 2026 window
  closed 15 Oct 2026.
- Fully Funded Masters Degree Scholarships in Canada 2026 - SKIPPED: listicle.
- ICIQ Summer Fellowship Program 2026 - SKIPPED: deadline passed 22 Mar 2026.
- University of Malta Scholarships 2026 - CHECKED, NOT MARKED: single
  postgraduate fee-waiver scheme (40-100% tuition), but deadlines conflict
  across sources (31 Jan / 30 Apr / 31 Oct) with no official-page confirmation
  of a live 31 Oct 2026 round; left unmarked for next run to re-check.
- EEML Summer School 2026 - SKIPPED: deadline passed 31 Mar 2026.
- Armament and Disarmament Summer School 2026 - SKIPPED: deadline passed
  16 Mar 2026.
- CNIO Summer Training Program 2026 - SKIPPED: deadline passed 31 Mar 2026.
- Asian Future Leaders Scholarship 2026 - SKIPPED as titled: 2026 cycle closed
  10 Apr 2026; the April 2027 Kyoto cycle (4-13 Nov 2026) is a retitle for a
  future run, not written here.
- Einstein Forum Fellowship 2026 - SKIPPED: deadline passed 15 May 2026.
- ADB-JSP Japan Scholarship 2026 - SKIPPED as titled: umbrella with
  per-institution deadlines, no single programme deadline.
- HENNGE Global Internship Program 2026 - WRITTEN with corrections: rolling
  batches, unpaid with subsidies (not "fully funded"), no subsidy amount
  published, no batch calendar published.
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
 'ifad-2026': {'mono': 'IFAD', 'title': 'IFAD Internship Programme 2026 (Rolling Applications Worldwide)',
   'href': 'ifad-internship-program-2026.html',
   'dpill': 'Rolling · no fixed deadline published',
   'award': 'A 6-month internship at IFAD headquarters in Rome or a country or regional office, with a monthly allowance. Interns from developing countries who must travel to their duty station receive a higher allowance towards housing and travel. The exact allowance amount is not published on the official programme page, so none is stated.',
   'elig': 'Aged 30 or younger, enrolled in an accredited university or graduate school (at least two years of undergraduate study completed, courses attended in the last 24 months) or having finished undergraduate or postgraduate studies within the last 24 months, fluent in English, in a field relevant to IFAD work.',
   'tags': [('Internship', 'blue'), ('Worldwide', 'teal')]},
 'humboldt-2026': {'mono': 'HUM', 'title': 'Humboldt Research Fellowship in Germany (Next Call Opens 15 November 2026)',
   'href': 'humboldt-research-fellowship-2026-germany.html',
   'dpill': 'Next call opens 15 Nov 2026',
   'award': 'A research fellowship in Germany of 6 to 24 months for postdoctoral researchers (EUR 3,000 a month) or 6 to 18 months for experienced researchers (EUR 3,600 a month), plus language training, family benefits, health-insurance subsidy, travel allowances and a host research-cost subsidy.',
   'elig': 'Researchers of all nationalities except Germany, all disciplines, with above-average qualifications: postdoctoral researchers within 4 years of the doctorate, experienced researchers within 12 years with a strong publication record, plus a German host and two expert reviews.',
   'tags': [('Fellowship', 'purple'), ('Germany', 'teal')]},
 'cern-stag-2026': {'mono': 'CERN', 'title': 'CERN Short Term Internship 2026 in Switzerland (Paid)',
   'href': 'cern-short-term-internship-2026-switzerland.html',
   'dpill': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
   'award': 'A 1 to 6 month full-time internship at CERN in Geneva, paid CHF 1,593 net a month for a full month (pro-rated for partial months), with paid leave for contracts of 4 months or more and CERN health insurance.',
   'elig': 'Nationals of a CERN Member State or Associate Member State (with current ceiling exclusions), aged 18 or over, full-time students throughout the internship on a technical or administrative diploma, Bachelor or Master course, whose university requires or encourages practical training. PhD students are not eligible.',
   'tags': [('Internship', 'blue'), ('Switzerland', 'teal')]},
 'huddersfield-2026': {'mono': 'HUD', 'title': 'University of Huddersfield International Merit Scholarships 2026 in UK (Automatic Tuition Discounts)',
   'href': 'university-of-huddersfield-international-scholarships-2026-uk.html',
   'dpill': 'Automatic · January 2027 entry',
   'award': 'Automatic tuition-fee discounts for self-funded international students: up to GBP 4,000 a year for undergraduates (AAB equivalent) or GBP 2,000 a year at general entry, and up to GBP 4,000 for taught postgraduates (First-class equivalent) or GBP 2,000 at general entry, plus a GBP 5,000 progression award and a GBP 1,000 early-payment discount.',
   'elig': 'International fee-paying, self-funded students on a full-time taught undergraduate or postgraduate course at Huddersfield, meeting the academic entry requirements for their tier. No separate scholarship application exists.',
   'tags': [('Undergraduate & Master’s', 'blue'), ('UK', 'teal')]},
 'hennge-2026': {'mono': 'HEN', 'title': 'HENNGE Global Internship Program in Japan (Rolling Batches, Unpaid with Subsidies)',
   'href': 'hennge-global-internship-program-2026-japan.html',
   'dpill': 'Rolling · batches fill first-come, first-served',
   'award': 'A 4 to 6 week on-site internship in Shibuya, Tokyo, in Full-Stack or Front-End development. The programme is unpaid, with subsidies covering a monthly subsidy (amount not published), round-trip airfare, visa guidance, medical insurance, a Japanese mobile phone with data, office facilities and cultural events.',
   'elig': 'Third-year Bachelor students or above (Bachelor, Master, PhD or recent graduates) in Computer Science or a related field, or with equivalent technical experience, fluent in English (no Japanese required), with Linux, macOS or Unix-like knowledge and an interest in open source.',
   'tags': [('Internship', 'blue'), ('Japan', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)
A = []

# ---------------------------------------------------------------- 1. IFAD
A.append(dict(
 slug='ifad-internship-program-2026',
 title='IFAD Internship Programme 2026 (Rolling Applications Worldwide)',
 meta='IFAD Internship Programme 2026: a 6-month internship at the International Fund for Agricultural Development in Rome or a country or regional office, with a monthly allowance. Rolling applications, age 30 or under, for students and recent graduates in fields relevant to rural development.',
 short='IFAD Internship 2026', kicker='Internship · Worldwide · Rolling', mono='IFAD',
 prov_short='IFAD', prov_cat='United Nations · International',
 h1='IFAD Internship Programme 2026 (Rolling Applications Worldwide)',
 sub='Read the funding label with care, because aggregator pages routinely call this opportunity fully funded. It is not a full-funding package. The International Fund for Agricultural Development, a United Nations agency fighting rural poverty and hunger, runs a rolling internship programme of six months, with a monthly allowance and, for interns from developing countries who must travel to their duty station, a higher allowance towards housing and travel. There is no single closing date: you apply to a specific vacancy on the IFAD careers portal, and vacancies are filled as they arise. The exact allowance amount is not published on the official programme page, so this article states none. If you are 30 or under, studying or recently graduated in a field that touches IFAD work, and you can work in Rome or in a country or regional office, this is a genuine route into the United Nations system. If you need every cost covered in advance, check the vacancy terms before you apply, because the official page promises an allowance, not full funding.',
 facts=facts([
  ('Provider', 'International Fund for Agricultural Development (IFAD), a United Nations specialised agency'),
  ('Award', '6-month internship (with the possibility of one further 6-month internship in a different area); monthly allowance, higher for interns from developing countries who must travel to their duty station. Exact allowance amount not published on the official programme page'),
  ('Level', 'Undergraduate (at least 2 years completed), postgraduate, and recent graduates'),
  ('Deadline', 'Rolling — no fixed deadline published; apply to a specific vacancy, filled as it arises'),
  ('Eligibility', 'Aged 30 or younger; enrolled in an accredited university or graduate school with courses attended in the last 24 months, or having completed undergraduate or postgraduate studies within the last 24 months; fluent in English; field relevant to IFAD mission'),
 ]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>IFAD invests in rural people. Its mandate is to help poor rural communities in developing countries raise their incomes and food security, and its internship programme is built to bring students and recent graduates into that work, rather than to run a classroom course. Interns are placed where the work actually sits: at headquarters in Rome, or in a country or regional office around the world. That placement matters more than the city in the queue title. The title says Italy, because headquarters is in Rome, but a vacancy in a country office is just as much an IFAD internship, and applicants should search the whole vacancy list rather than waiting for a Rome posting.</p>
      <p>The programme is deliberately open-ended. There is no annual competition with one deadline and one intake. Vacancies appear through the year, each with its own description, duty station and requirements, and each is filled when a suitable candidate is found. That is why this article gives no closing date and no batch calendar: inventing one would mislead readers into waiting for, or missing, a real vacancy. The practical rule is the opposite of a fixed-deadline scholarship. Check the portal regularly, and apply when a vacancy matches your field and your availability, because a good vacancy can close once it is filled.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>A six-month placement, extendable once:</strong> the standard internship lasts six months, and the official programme page allows one additional six-month internship in a different area. It is a substantial placement, not a short visit, and it is long enough to complete a real piece of work.</li>
        <li><strong>A monthly allowance:</strong> interns receive a monthly allowance from IFAD. The official programme page does not publish the amount, so this article does not quote one. Any page that gives you a precise figure for this programme is quoting an aggregator or an old vacancy, not the current official page, and you should confirm the figure in the vacancy itself before relying on it.</li>
        <li><strong>A higher allowance where travel is required:</strong> interns from developing countries who must travel to their duty station receive a higher monthly allowance, contributing to housing and travel costs. This is the programme's main equalising feature, and it is worth checking in the vacancy terms if you would need to relocate.</li>
        <li><strong>United Nations experience in rural development:</strong> work in areas such as agriculture, rural finance, climate adaptation, nutrition, gender, or project design, depending on the host team. That experience, and the references that come with it, carry weight for later United Nations, development-bank and non-governmental roles.</li>
        <li><strong>What it does not promise:</strong> the official page does not promise full funding of all costs, a salary, or a job at the end. Do not budget as if the allowance covered everything, and do not treat selection as a route to employment: the internship is a learning placement, and any further role would need a separate application.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Age 30 or younger:</strong> the official programme page sets an upper age limit of 30. If you are over 30, this programme is closed to you, however strong your profile.</li>
        <li><strong>Enrolled, or recently finished:</strong> you must be enrolled in an accredited university or graduate school, having completed at least two years of undergraduate study and attended courses in the last 24 months, or you must have completed undergraduate or postgraduate studies within the last 24 months. Aggregator pages that say 12 months are wrong: the official window is 24 months.</li>
        <li><strong>English fluency:</strong> fluency in English is required. Knowledge of another IFAD official language, Arabic, French or Spanish, is an asset, and for some country-office posts it may be required by the vacancy itself. Check the language line in each vacancy, not just the programme page.</li>
        <li><strong>A field relevant to IFAD work:</strong> your studies or experience should connect to IFAD's mission, whether that is agriculture, economics, development studies, environment, finance, communications, or a related discipline. A vacancy in a technical team will also carry its own subject requirements.</li>
        <li><strong>Available for the full placement:</strong> internships are full-time placements at a duty station or, where the vacancy says so, in a hybrid arrangement. Confirm the working pattern in the vacancy before applying, and do not assume a fully remote option exists.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>The official programme page does not publish a document checklist,</strong> so this article does not invent one. Aggregator lists of a CV, motivation letter, transcripts and proof of enrolment or graduation are plausible portal requirements, but they are not confirmed on the official programme page and they will vary by vacancy.</li>
        <li><strong>Prepare the standard set in advance:</strong> an up-to-date CV, a motivation letter tailored to the specific vacancy and team, academic transcripts, and proof of enrolment or of recent graduation. Having these ready matters because vacancies fill as they arise.</li>
        <li><strong>Tailor, do not recycle:</strong> because you apply to a specific team, your motivation letter should name the work that team does and the skills you bring to it. A generic United Nations letter is the weakest application this programme receives.</li>
        <li><strong>No application fee is charged:</strong> consistent with United Nations practice, secondary sources confirm no fee. Any page asking for payment to apply for an IFAD internship is not IFAD.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the IFAD careers portal and search for internship vacancies, filtering by the programme name. Do not apply through an aggregator link that promises a generic form: there is no single generic application form.</li>
        <li>Read the vacancy in full: duty station, team, duration, language requirements and any allowance or travel terms stated for that post. If a term you need is not stated, treat it as unconfirmed rather than assuming it.</li>
        <li>Create a profile on the portal, complete the application for that specific vacancy, and upload the documents the portal asks for. Keep a copy of everything you submit.</li>
        <li>Apply as soon as a suitable vacancy appears, rather than waiting for a deadline that does not exist. Rolling programmes reward early, well-matched applications.</li>
        <li>If you are shortlisted, expect the host team to assess fit for its own work. Prepare to discuss, concretely, what you would do in the first weeks of the placement.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a deadline for the IFAD Internship Programme?',
  'No single deadline is published. The programme is rolling: you apply to a specific vacancy on the IFAD careers portal, and vacancies are filled as they arise. Check the portal regularly and apply when a vacancy matches you.'),
 ('How much is the monthly allowance?',
  'The exact amount is not published on the official programme page, so this article states none. Interns from developing countries who must travel to their duty station receive a higher allowance towards housing and travel. Confirm the figure in the vacancy itself before relying on any number quoted elsewhere.'),
 ('Is the internship only in Rome?',
  'No. Headquarters is in Rome, but internships also sit in IFAD country and regional offices worldwide. Search the whole vacancy list, not only Rome postings.'),
 ('Am I eligible if I graduated more than two years ago?',
  'No, on the official rule. You must be enrolled with courses attended in the last 24 months, or have completed undergraduate or postgraduate studies within the last 24 months. Aggregator pages saying 12 months are wrong.'),
 ('How long does the internship last?',
  'Six months, with the possibility of one additional six-month internship in a different area.'),
 ('Is this a paid job or a route to IFAD employment?',
  'Neither, in the strict sense. It is an internship with a monthly allowance, not a salary and not a job offer. Any later role would need a separate application.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against IFAD's official internship programme page (ifad.org/en/work-with-us/internship-programmes: 6 months with one further 6 months possible, age 30 or younger, enrolled with at least two years of undergraduate study and courses in the last 24 months or completed studies within the last 24 months, fluent in English, monthly allowance with a higher allowance for interns from developing countries travelling to their duty station, apply through the careers portal to a specific vacancy) plus Opportunities Radar and Prosple vacancy summaries (same duration, age and allowance structure). CONFLICTS: (1) Aggregator "fully funded" labels are REJECTED - the official page promises an allowance, not full funding of all costs, and no allowance amount is published there, so none is stated. (2) The 12-month post-graduation window in some aggregators is REJECTED in favour of the official 24 months. (3) "Italy only" in the queue title is corrected - headquarters is Rome, but country and regional offices also host interns. (4) No document checklist is published on the official programme page, so the article states none and flags aggregator lists as unconfirmed portal requirements.</p>''',
 dl_long='Rolling — no fixed deadline published (vacancies filled as they arise)',
 offlinks=[('IFAD — Internship Programmes (official)', 'https://www.ifad.org/en/work-with-us/internship-programmes'),
           ('Bright Scholarship — IFAD Internship Program 2026', 'https://brightscholarship.com/ifad-internship-program-2026-in-italy/')],
 related_titles=['humboldt-2026', 'cern-stag-2026', 'huddersfield-2026', 'hennge-2026'])),

# ---------------------------------------------------------------- 2. Humboldt
A.append(dict(
 slug='humboldt-research-fellowship-2026-germany',
 title='Humboldt Research Fellowship in Germany (Next Call Opens 15 November 2026)',
 meta='Humboldt Research Fellowship: EUR 3,000 a month for postdoctoral researchers and EUR 3,600 for experienced researchers, for 6 to 24 months in Germany. The current call is closed at its 800-application cap; the next call opens 15 November 2026 for the July 2027 selection meeting.',
 short='Humboldt Research Fellowship', kicker='Fellowship · Germany · Research', mono='HUM',
 prov_short='Alexander von Humboldt Foundation', prov_cat='Foundation · Germany',
 h1='Humboldt Research Fellowship in Germany (Next Call Opens 15 November 2026)',
 sub='Do not apply today, and do not trust the deadline lists that say you can. The Alexander von Humboldt Foundation, one of Germany most respected research funders, has capped its current Humboldt Research Fellowship call at 800 applications, and that cap has been reached: no new applications can be created at present. The next call opens on 15 November 2026, for the selection meeting in July 2027, with the earliest fellowship start in September 2027. That single fact changes how this opportunity should be read. It is not a rolling open door, and it is not a fixed annual deadline in March, July and November, as aggregator pages claim. It is a competitive, capped call that you prepare for now and submit when it opens. The award itself is substantial: EUR 3,000 a month for postdoctoral researchers and EUR 3,600 a month for experienced researchers, plus language training, family benefits, a health-insurance subsidy, travel allowances and a subsidy for the host research costs. If you are a researcher with a strong record, a German host, and a project that needs time in Germany, the wait until 15 November is preparation time, not dead time.',
 facts=facts([
  ('Provider', 'Alexander von Humboldt Foundation'),
  ('Award', 'EUR 3,000 a month (postdoctoral researchers) or EUR 3,600 a month (experienced researchers), plus language course, family benefits, health-insurance subsidy, travel allowances and host research-cost subsidy'),
  ('Level', 'Postdoctoral and experienced researchers, all disciplines'),
  ('Deadline', 'Next call opens 15 November 2026 (July 2027 selection meeting; earliest start September 2027). Current call closed at its 800-application cap'),
  ('Eligibility', 'All nationalities except Germany (narrow exceptions for Germans long resident or working abroad); postdocs within 4 years of the doctorate, experienced researchers within 12 years with a strong publication record; German host and two expert reviews required; not lived in Germany more than 90 days in the 18 months before applying'),
 ]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The Humboldt Research Fellowship is a fellowship for researchers, not a scholarship for students. It funds a research stay at a university or research institution in Germany, hosted by an established German academic who mentors the fellow and provides research facilities. The Foundation, based in Bonn, has run the programme for decades, and its alumni network is one of the reasons the award carries weight far beyond the monthly stipend. Selection is competitive, with an expected approval rate of 20 to 25 percent, and the process takes months: applications are reviewed formally, expert reviews are collected, a selection committee meets, and the outcome arrives about five weeks after the selection decision. Applicants should therefore plan on a four to eight month process from submission to decision, and should not build a move to Germany around a start date the Foundation has not confirmed.</p>
      <p>The cap is the newest feature, and it is the reason this article leads with a warning rather than a deadline. The official page states that the current call has reached its maximum of 800 applications and that no new applications can be created at present. Older aggregator pages, which list three deadlines a year in March, July and November, are now stale: they describe the old rhythm, not the capped call. The next call opens on 15 November 2026. The practical consequence is simple. Use the weeks before 15 November to secure your host, your mentoring agreement, your research outline and your two expert reviewers, so that you can submit promptly when the call opens, rather than starting that work after it opens and risking a second cap.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>EUR 3,000 a month for postdoctoral researchers, EUR 3,600 a month for experienced researchers:</strong> these are the current official rates. Older aggregator figures of EUR 2,670, EUR 2,700 and EUR 3,200 are outdated and should not be used. The fellowship is a living stipend, not a salary, and it is paid for the duration of the stay.</li>
        <li><strong>Duration with flexibility:</strong> postdoctoral fellowships run 6 to 24 months, experienced-researcher fellowships 6 to 18 months. Either can be divided into up to three stays within three years, which matters for researchers who cannot relocate for one continuous block.</li>
        <li><strong>Language training:</strong> an intensive language course for the fellow and partner before the fellowship begins, so that daily life in Germany does not depend on arriving fluent.</li>
        <li><strong>Family benefits and health-insurance subsidy:</strong> family benefits where applicable, and a subsidy for private full health insurance, both of which change the real value of the stipend for researchers moving with a partner or children.</li>
        <li><strong>Travel allowances and host research costs:</strong> travel allowances for the fellow, and a subsidy to the host for research costs, so that the host institution is supported as well as the fellow.</li>
        <li><strong>Personal support and the Humboldt network:</strong> personal support during the fellowship and, afterwards, membership of a worldwide alumni network that remains a professional asset long after the stay ends.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Nationality:</strong> researchers of all nationalities except Germany, with narrow exceptions for German nationals who have lived and worked abroad for a long time. If you are German and based in Germany, this fellowship is not for you; the Foundation directs alumni and other routes to different programmes.</li>
        <li><strong>Postdoctoral track:</strong> a doctorate or equivalent completed within the last four years, or to be completed before the envisaged selection meeting, with a written summary of findings. Aggregator pages that invert this rule, saying the doctorate must be at least four years old, are wrong.</li>
        <li><strong>Experienced-researcher track:</strong> a doctorate within the last twelve years, an extensive publication list including lead-author papers, and a leadership-level position. An alternative route exists for researchers up to sixteen years after a master or postgraduate degree where a doctorate is not possible or uncommon, with a commensurate publication record.</li>
        <li><strong>German host required:</strong> you must have a host at a German research institution who provides a mentoring agreement, confirmation of research facilities, and a detailed review of your project. An application without a committed host is not a complete application.</li>
        <li><strong>Two expert reviews:</strong> two independent expert reviews, uploaded directly by the reviewers, are required. Line up reviewers early: a late review is a common reason for delay.</li>
        <li><strong>Residence rule:</strong> you must not have lived in Germany for more than 90 days in total in the eighteen months before applying. Good German or English is required, depending on the field, and previous direct Humboldt sponsorship disqualifies an applicant from this fellowship.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Curriculum vitae, maximum two pages,</strong> and a research outline of maximum five pages. Brevity is a requirement here, not a suggestion: overlong documents are a formal weakness.</li>
        <li><strong>Complete publication list, a list of selected key publications, and the key publications themselves,</strong> so that reviewers can judge the record, not just the claim.</li>
        <li><strong>Doctoral certificate, or proof of successful completion,</strong> or confirmation that completion will occur before the selection meeting, plus a German language certificate if required, and publisher acceptance notifications or translations where required.</li>
        <li><strong>Host statement and confirmation of research facilities,</strong> with the detailed host review, and the two expert reviews uploaded directly by the reviewers.</li>
        <li><strong>Online submission only:</strong> applications go online to the Foundation. Incomplete or inaccurate applications are formally rejected or postponed, so check every field and attachment before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Secure a German host first. Agree the project, the mentoring arrangement and the research facilities, and confirm that the host will provide the detailed statement and review.</li>
        <li>Prepare the research outline (maximum five pages), the two-page CV, the publication lists and the key publications, and the doctoral evidence. Keep to the page limits exactly.</li>
        <li>Ask your two expert reviewers early, and confirm they will upload their reviews directly. Do not leave this to the week the call opens.</li>
        <li>When the call opens on 15 November 2026, submit online to the Foundation, complete and accurate, for the July 2027 selection meeting. Expect a decision about five weeks after that meeting, with the earliest start in September 2027.</li>
        <li>Do not confuse this fellowship with the separate CAPES-Humboldt programme for Brazil, which has its own rules and deadlines. It is a different scheme.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I apply right now?',
  'No. The current call has reached its 800-application cap and no new applications can be created at present. The next call opens 15 November 2026, for the July 2027 selection meeting, with the earliest start in September 2027.'),
 ('How much does the fellowship pay?',
  'EUR 3,000 a month for postdoctoral researchers and EUR 3,600 a month for experienced researchers, plus language training, family benefits, a health-insurance subsidy, travel allowances and a host research-cost subsidy. Older figures of EUR 2,670 or EUR 2,700 are outdated.'),
 ('How long can the fellowship last?',
  'Postdoctoral fellowships 6 to 24 months, experienced-researcher fellowships 6 to 18 months, each divisible into up to three stays within three years.'),
 ('Do I need a German host before applying?',
  'Yes. A German host providing a mentoring agreement, confirmation of research facilities and a detailed review is required, along with two expert reviews.'),
 ('Am I eligible if I have lived in Germany recently?',
  'Only if your total stay in Germany in the eighteen months before applying is 90 days or less. Longer residence disqualifies you under the residence rule.'),
 ('What are my chances?',
  'The Foundation expects an approval rate of 20 to 25 percent. A strong publication record, a clear research outline and a committed host are the factors you control.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the Alexander von Humboldt Foundation official fellowship page (humboldt-foundation.de/en/apply/sponsorship-programmes/humboldt-research-fellowship, fetched 29 Oct 2026: current call at its 800-application maximum with no new applications creatable, next call opens 15 Nov 2026 for the July 2027 selection meeting with earliest start September 2027, EUR 3,000 postdoctoral and EUR 3,600 experienced-researcher monthly rates, 6-24 and 6-18 month durations divisible into up to three stays, 20-25 percent approval expectation) plus Collegedunia and OpportunitiesFeed summaries. CONFLICTS: (1) Bright's "deadline: March, July, and November" is REJECTED as stale - it omits the cap and the closed current call. (2) Bright's EUR 2,670 figure and older EUR 2,700 and EUR 3,200 figures are REJECTED as outdated; the article uses the current official EUR 3,000 and EUR 3,600. (3) Bright's eligibility line inverting the postdoctoral rule is REJECTED - postdocs must be within 4 years of the doctorate, experienced researchers within 12 years. (4) The CAPES-Humboldt programme (Brazil only) is a separate scheme and is excluded.</p>''',
 dl_long='Next call opens 15 November 2026 (July 2027 selection meeting; earliest fellowship start September 2027; current call closed at its 800-application cap)',
 offlinks=[('Alexander von Humboldt Foundation — Humboldt Research Fellowship (official)', 'https://www.humboldt-foundation.de/en/apply/sponsorship-programmes/humboldt-research-fellowship'),
           ('Bright Scholarship — Humboldt Research Fellowship 2026', 'https://brightscholarship.com/humboldt-research-fellowship-2026/')],
 related_titles=['ifad-2026', 'cern-stag-2026', 'huddersfield-2026', 'hennge-2026'])),

# ---------------------------------------------------------------- 3. CERN
A.append(dict(
 slug='cern-short-term-internship-2026-switzerland',
 title='CERN Short Term Internship 2026 in Switzerland (Paid)',
 meta='CERN Short Term Internship 2026: a 1 to 6 month paid internship at CERN in Geneva, CHF 1,593 net a month, for full-time students from CERN Member States and Associate Member States. Deadline 1 November 2026, 23:59 Geneva time.',
 short='CERN Short Term Internship 2026', kicker='Internship · Switzerland · Paid', mono='CERN',
 prov_short='CERN', prov_cat='Research Organisation · Switzerland',
 h1='CERN Short Term Internship 2026 in Switzerland (Paid)',
 sub='This is the most urgent article in this batch, and the deadline is the point. The CERN Short Term Internship, known as STAG 2026, closes on 1 November 2026 at 23:59 Geneva time, three days after this article was written. It is a one to six month, fully on-site internship at CERN in Geneva, paid at CHF 1,593 net a month for a full month, pro-rated for partial months. It is open to full-time students on technical and administrative courses, but it is not open to everyone: you must be a national of a CERN Member State or Associate Member State, with current ceiling exclusions, and PhD students are not eligible. If you meet those two gates and you can be in Geneva, apply now, because departments select on a rolling basis through the year and this is the final 2026 cutoff. If you are not a Member State national, or you are a PhD student, this internship is closed to you however strong your application, and no aggregator claim of open to all countries changes that.',
 facts=facts([
  ('Provider', 'CERN (European Organization for Nuclear Research), Geneva'),
  ('Award', 'CHF 1,593 net a month for a full month (pro-rated for partial months); paid leave for contracts of 4 months or more; CERN comprehensive health insurance, with a contribution deducted from the allowance'),
  ('Level', 'Full-time students on a technical or administrative diploma, Bachelor or Master course; PhD students not eligible'),
  ('Deadline', '1 November 2026, 23:59 Geneva time (final 2026 cutoff)'),
  ('Eligibility', 'National of a CERN Member State or Associate Member State (with current ceiling exclusions); aged 18 or over; full-time student throughout the internship; university requires or encourages practical training; good working knowledge of English or French'),
 ]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>CERN is the European particle-physics laboratory on the Swiss-French border near Geneva, home to the Large Hadron Collider and to thousands of physicists, engineers and technicians. The Short Term Internship is its short placement route: a one to six month, fully on-site internship in a CERN team, distinct from the longer technical and doctoral student programmes. Departments use it to fill a defined piece of work, which is why selection runs through the year rather than in one annual intake, and why the vacancy, not a generic programme page, is the real application. You state your availability period in the application, and a department that needs someone in that window can take you on. That rolling model is also why the 1 November cutoff matters: it is the last date for 2026 applications, not a rolling date you can safely ignore.</p>
      <p>The fields are wider than particle physics alone. Technical fields include applied physics, computing, mathematics, engineering, instrumentation, safety and surveying, and administrative fields include translation, human resources, accounting, legal work, logistics and related support functions. The common requirement is not a physics degree: it is that you are a full-time student on a relevant course, that your university requires or encourages a practical training period, and that you can work in English or French. If your course has no practical-training element at all, check with your university before applying, because the requirement is part of the eligibility rule, not a preference.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CHF 1,593 net a month for a full month,</strong> pro-rated for partial months. Older listings quoting CHF 1,587 are superseded: use the current vacancy figure. This is an allowance, not a salary, and it is the figure to budget against for Geneva, which is an expensive city.</li>
        <li><strong>Paid leave for longer placements:</strong> contracts of four months or more carry paid leave. Shorter placements do not carry the same leave entitlement, so factor that into a one or two month plan.</li>
        <li><strong>CERN health insurance:</strong> interns are covered by CERN comprehensive health insurance, with a contribution deducted from the allowance. Confirm the deduction in your offer, because it changes your net monthly amount.</li>
        <li><strong>On-site experience at a world laboratory:</strong> a CERN placement, even a short one, puts real project work and a CERN reference on a CV in a way that a remote placement cannot match. It is also a realistic route to discovering whether a longer CERN programme, or a technical career in large-scale research infrastructure, suits you.</li>
        <li><strong>What is not confirmed:</strong> a travel allowance or supplement is not confirmed in the current call, and this article does not promise one. Older vacancy text mentions an insurance contribution and, in some versions, travel support, but the current vacancy snippets confirm the allowance and paid leave only. Do not budget for a travel payment that the current call does not state.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Nationality gate, read first:</strong> you must be a national of a CERN Member State or Associate Member State. Recent vacancy summaries also list current ceiling exclusions, for example Pakistani, Lithuanian, Latvian, Cypriot, Croatian and Turkish nationals currently cannot be considered. Aggregator claims of open to all countries are wrong. Check your nationality against the current vacancy before spending time on the application.</li>
        <li><strong>Age 18 or over,</strong> and a full-time student throughout the internship. You must remain a student for the whole placement: graduating before the placement ends breaks the condition.</li>
        <li><strong>On a technical or administrative course:</strong> a diploma, Bachelor or Master course in a field relevant to the team you apply to, where your university requires or encourages practical training as part of the course.</li>
        <li><strong>PhD students are not eligible:</strong> this is an explicit exclusion. Doctoral researchers should look at CERN doctoral student programmes instead, not at this short-term route.</li>
        <li><strong>Language:</strong> a good working knowledge of English or French. No IELTS score is required, and no application fee is charged.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>A CV in English or French, in PDF format,</strong> is the document the current vacancy asks for, plus any other documents you consider relevant to your application. That is a lighter requirement than older listings suggested.</li>
        <li><strong>Older requirements are superseded:</strong> older listings demanding a transcript and a mandatory professor reference letter conflict with the current vacancy, which asks for the CV plus anything else you consider relevant. Follow the current vacancy, not an old aggregator checklist.</li>
        <li><strong>Prepare a targeted CV:</strong> because the CV carries most of the weight, tailor it to the team and field you want, list relevant coursework and practical work plainly, and state your availability period clearly. A generic CV is the weakest application this programme receives.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the CERN Careers posting for Short-Term Internship 2026 (STAG 2026) and check the nationality and student-status conditions against your own situation before starting.</li>
        <li>Complete the online application, which takes about fifteen minutes, and state your availability period honestly. Departments select during the year against the periods they need.</li>
        <li>Upload your CV in English or French as a PDF, plus any other document you consider relevant. Do not wait for a reference letter the current vacancy does not ask for.</li>
        <li>Submit before 1 November 2026, 23:59 Geneva time. This is the final 2026 cutoff, and a late application is not considered.</li>
        <li>If you are selected, confirm the insurance deduction, the paid-leave position for your contract length, and any travel terms in your offer before accepting, because those details are not all stated in the public vacancy.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline?',
  '1 November 2026, 23:59 Geneva time. It is the final 2026 cutoff for the Short Term Internship, and departments select on a rolling basis through the year.'),
 ('How much does it pay?',
  'CHF 1,593 net a month for a full month, pro-rated for partial months. The older CHF 1,587 figure is superseded. Paid leave applies to contracts of four months or more, and CERN health insurance is provided with a contribution deducted from the allowance.'),
 ('Can PhD students apply?',
  'No. PhD students are explicitly not eligible for this short-term route. It is for diploma, Bachelor and Master students who remain full-time students throughout the placement.'),
 ('Is it open to all nationalities?',
  'No. You must be a national of a CERN Member State or Associate Member State, subject to current ceiling exclusions (recent vacancy summaries list Pakistani, Lithuanian, Latvian, Cypriot, Croatian and Turkish nationals as currently unable to be considered).'),
 ('Do I need IELTS or a reference letter?',
  'No IELTS score is required, and the current vacancy asks for a CV in English or French plus anything else you consider relevant. Older transcript and mandatory reference-letter requirements are superseded.'),
 ('Is the internship remote?',
  'No. It is fully on-site in Geneva. You must be able to be in Geneva for the whole placement.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the official CERN Careers posting for Short-Term Internship 2026 (jobs.smartrecruiters.com/CERN/744000085340717-short-term-internship-2026: deadline 1 Nov 2026, 23:59 Geneva time, CHF 1,593 net a month, 1-6 months, fully on-site, full-time student throughout, Member State or Associate Member State nationality, PhD students not eligible, CV in English or French) plus OpportunitiesFeed (22 Oct 2026) and CareerAidHub vacancy summaries. CONFLICTS: (1) CHF 1,587 in older listings is REJECTED in favour of the current CHF 1,593. (2) Aggregator "open to all countries" claims are REJECTED - nationality is restricted, with current ceiling exclusions. (3) Older transcript plus mandatory professor reference-letter requirements are REJECTED in favour of the current vacancy (CV plus anything else considered relevant). (4) A travel allowance or supplement is NOT confirmed in the current call and is not promised in this article.</p>''',
 dl_long='1 November 2026, 23:59 Geneva time (final 2026 cutoff)',
 offlinks=[('CERN Careers — Short-Term Internship 2026 (official posting)', 'https://jobs.smartrecruiters.com/CERN/744000085340717-short-term-internship-2026'),
           ('Bright Scholarship — CERN Short Term Internship 2026', 'https://brightscholarship.com/cern-short-term-internship-2026-switzerland/')],
 related_titles=['ifad-2026', 'humboldt-2026', 'huddersfield-2026', 'hennge-2026'])),

# ---------------------------------------------------------------- 4. Huddersfield
A.append(dict(
 slug='university-of-huddersfield-international-scholarships-2026-uk',
 title='University of Huddersfield International Merit Scholarships 2026 in UK (Automatic Tuition Discounts)',
 meta='University of Huddersfield International Merit Scholarships: automatic tuition-fee discounts up to GBP 4,000 a year for self-funded international students, with no separate scholarship application. January 2027 entry; Early Payment Discount deadline 31 October 2026.',
 short='Huddersfield Merit Scholarships', kicker='UK · Undergraduate & Master’s · Automatic', mono='HUD',
 prov_short='University of Huddersfield', prov_cat='University · United Kingdom',
 h1='University of Huddersfield International Merit Scholarships 2026 in UK (Automatic Tuition Discounts)',
 sub='The most useful fact about this opportunity is also the one most aggregator pages get wrong: there is no scholarship application to fill in. The University of Huddersfield, a university in West Yorkshire, England, assesses self-funded international students for merit tuition discounts automatically, on the strength of their course application, and tells successful applicants in their offer letter. There is therefore no single scholarship deadline to miss, and no separate essay, form or interview to prepare. What does have a deadline is a separate, smaller discount: the Early Payment Discount of GBP 1,000 for the first year, for January 2027 intake, closes on 31 October 2026. The live angle for a reader in late October 2026 is January 2027 entry, not September 2026, which has already begun. The awards themselves are partial tuition discounts, up to GBP 4,000 a year, not full funding, and this article keeps that distinction in the title, in the award table, and in every benefit claim.',
 facts=facts([
  ('Provider', 'University of Huddersfield'),
  ('Award', 'Automatic tuition-fee discount: undergraduates up to GBP 4,000 a year (AAB equivalent) or GBP 2,000 a year (general entry); taught postgraduates up to GBP 4,000 (First-class equivalent) or GBP 2,000 (general entry), each year except a placement year; plus GBP 5,000 progression award and GBP 1,000 early-payment discount'),
  ('Level', 'Full-time taught undergraduate and postgraduate (Master) courses'),
  ('Deadline', 'No separate scholarship deadline — automatic on course application. Early Payment Discount: 31 October 2026 for January 2027 intake'),
  ('Eligibility', 'International fee-paying, self-funded students on a full-time taught course, meeting the academic entry requirements for their tier; cannot be combined with another university or external scholarship'),
 ]),
 body='''
      <h2 id="about">About the awards</h2>
      <p>Huddersfield international scholarships are best understood as a fee-discount system, not as a competition. When you apply for an eligible full-time taught undergraduate or postgraduate course, the university looks at your academic record against its published tiers and, if you qualify, applies the discount to your tuition fees and states it in your offer letter. There is no separate scholarship committee, no shortlist, and no second application to track. That simplicity is the point of the design, and it is also why aggregator pages that describe a scholarship form, personal statement and recommendation letters are misleading: they describe a process the official page explicitly says does not exist. The official page states that there is no specific application process for these awards.</p>
      <p>Two cautions belong in the same paragraph as the good news. First, the September 2026 intake is past, so a reader applying now is realistically aiming at January 2027 entry, where the same automatic system applies. Second, the discounts are partial. Even the top tier, GBP 4,000 a year, leaves most of the international tuition fee, plus living costs, accommodation, travel and visa costs, to be funded by the student. Any page calling this funded, in the sense of full funding, is overstating it, and any budget built on that reading will fall short.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Undergraduate discounts, up to GBP 4,000 a year:</strong> GBP 4,000 a year for applicants with an AAB A-Level equivalent, or GBP 2,000 a year at general entry requirements, applied each year except a placement year. The discount follows the student through the course, not just the first year.</li>
        <li><strong>Taught postgraduate discounts, up to GBP 4,000:</strong> GBP 4,000 for applicants with a First-class Honours equivalent, or GBP 2,000 at general entry requirements, for taught Master courses. A GBP 3,000 middle tier appears on some aggregator and comparison pages, but it is not on the current official page, which lists only GBP 4,000 and GBP 2,000, so this article omits it rather than repeating an unverified tier.</li>
        <li><strong>Progression Scholarship, GBP 5,000:</strong> a separate award for students who completed a Huddersfield undergraduate degree in 2026 and progress immediately to a taught postgraduate course. This is the largest single discount in the bundle, and it rewards staying at the same university.</li>
        <li><strong>Early Payment Discount, GBP 1,000:</strong> GBP 1,000 off the first year for students who pay the full deposit by the stated deadline. For January 2027 intake, that deadline is 31 October 2026, two days after this article was written. This is the only dated item on the official page, and it must not be presented as the scholarship deadline: the scholarship itself has no separate deadline.</li>
        <li><strong>What is not covered:</strong> living costs, accommodation, travel, visa and insurance are not covered by these discounts. Only one university scholarship or discount applies at a time in the usual rule: you cannot stack these awards with another university or external scholarship to reach full funding.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>International fee-paying, self-funded students</strong> on a full-time taught undergraduate or postgraduate course. If your fees are paid by a sponsor, government or employer, the self-funded condition needs checking against the course page before you assume eligibility.</li>
        <li><strong>Academic tier:</strong> the GBP 4,000 undergraduate tier requires an AAB A-Level equivalent, and the GBP 4,000 postgraduate tier requires a First-class Honours equivalent. The GBP 2,000 tiers apply at general entry requirements. Aggregator claims of a minimum 2:1 for all applicants are wrong: the general-entry tier does not carry that bar.</li>
        <li><strong>Cannot be combined</strong> with another university or external scholarship. If you hold another award, the university will apply the applicable rule, and you should confirm which award survives before accepting an offer.</li>
        <li><strong>Exclusions need course-page checking:</strong> corroborating sources list exclusions including MA TESOL with Placement, Huddersfield Business School Master courses with placement, Master by Research, and applicants with refugee, asylum or indefinite-leave status. These exclusions are not on the current official page snippet checked, so this article flags them as needing confirmation on the course page rather than stating them as official-page facts.</li>
        <li><strong>Standard course entry requirements still apply:</strong> academic qualifications and English language requirements for the course itself are the real gates. The scholarship discount does not waive them.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>No separate scholarship documents are published,</strong> because there is no separate scholarship application. This article therefore does not invent a scholarship checklist, and readers should ignore aggregator lists of a scholarship form, personal statement and recommendation letters for this award.</li>
        <li><strong>Standard course-application documents apply:</strong> academic transcripts and certificates, English language evidence where required, a passport, and any course-specific requirements stated on the course page. Those documents are what the university actually assesses, for admission and for the discount tier.</li>
        <li><strong>Get the discount in writing:</strong> the offer letter is the document that matters. If a discount is awarded, it should appear there. If it does not, ask the international enquiries team before accepting, rather than assuming it will be added later.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose an eligible full-time taught undergraduate or postgraduate course at Huddersfield, and check the course page for entry requirements, fees and any exclusion that applies to that course.</li>
        <li>Apply for the course through the normal route. There is no separate scholarship form, essay or interview to complete.</li>
        <li>If you qualify, the university will state the discount in your offer letter. Read the offer carefully: the tier, the years it applies to, and any placement-year exception should all be visible.</li>
        <li>If you are aiming for January 2027 entry and want the GBP 1,000 Early Payment Discount, pay the full deposit by 31 October 2026. That discount is first-year only and is separate from the merit discount.</li>
        <li>For questions, contact the university international enquiries team at international.enquirers@hud.ac.uk, as given on the official page, rather than relying on an aggregator contact form.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there a scholarship application form for Huddersfield?',
  'No. The official page states there is no specific application process. You are automatically considered on your course application, and any discount is stated in your offer letter.'),
 ('Is there a scholarship deadline?',
  'No separate scholarship deadline exists. The only dated item on the official page is the Early Payment Discount: 31 October 2026 for January 2027 intake. Do not confuse that discount deadline with a scholarship deadline.'),
 ('How much is the discount?',
  'Up to GBP 4,000 a year for undergraduates (AAB equivalent) or GBP 2,000 a year at general entry, and up to GBP 4,000 for taught postgraduates (First-class equivalent) or GBP 2,000 at general entry, each year except a placement year. A GBP 5,000 progression award and a GBP 1,000 early-payment discount are separate.'),
 ('Is this fully funded?',
  'No. These are partial tuition-fee discounts. Living costs, accommodation, travel, visa and insurance are not covered, and the discount cannot be combined with another university or external scholarship.'),
 ('Can I still apply for September 2026?',
  'September 2026 intake is past. The live angle in late October 2026 is January 2027 entry, with the Early Payment Discount deadline on 31 October 2026.'),
 ('Does the GBP 3,000 middle tier exist?',
  'It appears on comparison sites, but it is not on the current official page, which lists only GBP 4,000 and GBP 2,000 tiers. This article omits it rather than repeating an unverified tier.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against the University of Huddersfield official international scholarships page (hud.ac.uk/international/scholarships: no specific application process, automatic consideration with the award stated in the offer letter, GBP 4,000 and GBP 2,000 tiers for undergraduates and taught postgraduates, GBP 5,000 progression award, GBP 1,000 Early Payment Discount with a 31 Oct 2026 deadline for January 2027 intake, contact international.enquirers@hud.ac.uk) plus CollegeDunia, Scholarship Union and GlobalScholarships summaries. CONFLICTS: (1) Bright's separate scholarship application form, personal statement and recommendation-letter steps are REJECTED - the official page says there is no specific application process. (2) Bright's "minimum 2:1 for all" is REJECTED - the GBP 2,000 tier is general entry. (3) The GBP 3,000 middle tier on comparison sites is OMITTED - it is not on the current official page. (4) The 28 June 2026 date on one aggregator is REJECTED - it is not on the official page and conflicts with the automatic scheme. (5) "Funded" in the queue title is corrected to partial tuition discounts, and the article is framed for January 2027 entry, not September 2026. Exclusions listed by corroborating sources are flagged as needing course-page confirmation, since they are not on the official page snippet checked.</p>''',
 dl_long='No separate scholarship deadline — automatic on course application; Early Payment Discount deadline 31 October 2026 for January 2027 intake',
 offlinks=[('University of Huddersfield — International Scholarships (official)', 'https://www.hud.ac.uk/international/scholarships/'),
           ('Bright Scholarship — University of Huddersfield Scholarships 2026', 'https://brightscholarship.com/university-of-huddersfield-scholarships-2026/')],
 related_titles=['ifad-2026', 'humboldt-2026', 'cern-stag-2026', 'hennge-2026'])),

# ---------------------------------------------------------------- 5. HENNGE
A.append(dict(
 slug='hennge-global-internship-program-2026-japan',
 title='HENNGE Global Internship Program in Japan (Rolling Batches, Unpaid with Subsidies)',
 meta='HENNGE Global Internship Program: a 4 to 6 week on-site internship in Shibuya, Tokyo, in Full-Stack or Front-End development. Rolling batches, first-come first-served, unpaid with subsidies including airfare, insurance and a monthly subsidy (amount not published).',
 short='HENNGE Global Internship', kicker='Internship · Japan · Rolling', mono='HEN',
 prov_short='HENNGE', prov_cat='Technology Company · Japan',
 h1='HENNGE Global Internship Program in Japan (Rolling Batches, Unpaid with Subsidies)',
 sub='The first correction to make about this programme is the funding label, because it changes the whole decision. HENNGE, a Tokyo cloud-security company, describes its Global Internship Program plainly on its official recruitment page: the programme is unpaid, with comprehensive subsidies. Aggregator pages that call it fully funded are therefore wrong in a way that matters to a student budgeting for Tokyo. What HENNGE does provide is substantial: a monthly subsidy, round-trip airfare, visa guidance, medical insurance, a Japanese mobile phone with data, office facilities and cultural events, for a four to six week, on-site internship in Shibuya, Tokyo, in Full-Stack or Front-End development. The second correction is the calendar. There is no single deadline and no reliable batch calendar to publish: batches run through the year, applications are reviewed first-come, first-served, and a batch closes when its slots fill. Most 2026 batches are already past, and the programme is already being advertised for 2027, so the honest framing is rolling batches with the live official page as the only reliable source for current dates. If you are a computing student who wants real product work in Tokyo and you can afford an unpaid placement with subsidies, this is a genuine route. If you need a salary, it is not.',
 facts=facts([
  ('Provider', 'HENNGE (cloud-security company, Tokyo)'),
  ('Award', 'Unpaid internship with subsidies: monthly subsidy (amount not published), round-trip airfare, visa guidance, medical insurance, Japanese mobile phone with data, office facilities and refreshments, cultural events. Possible full-time offer for outstanding participants, not guaranteed'),
  ('Level', 'Third-year Bachelor students or above, including Master, PhD and recent graduates, in Computer Science or a related field'),
  ('Deadline', 'Rolling — no fixed deadline published; batches close when slots fill, reviewed first-come, first-served'),
  ('Eligibility', 'Third-year Bachelor or above, or equivalent technical experience; fluent English, no Japanese required; Linux, macOS or Unix-like knowledge; interest in open source and the tech community; Full-Stack or Front-End pathway'),
 ]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>HENNGE is a Japanese software company best known for HENNGE One, a cloud-security service, and its Global Internship Program brings international students into its Shibuya office in Tokyo for four to six weeks of real development work. Interns work Monday to Friday, 10:00 to 19:00 Japan time, on-site, in one of two pathways: Full-Stack or Front-End. The work is product work, not a classroom simulation, and the programme is explicit that outstanding participants may receive a full-time offer. That offer is a possibility, not a promise, and applicants should not treat the internship as a guaranteed job route. The value of the placement, for most participants, is the experience itself: shipping code in a Japanese technology company, working in English in a Tokyo office, and building a portfolio and references that carry weight for later roles in Japan or elsewhere.</p>
      <p>The rolling, first-come, first-served model is the part of the programme most often misunderstood. Because batches run through the year and close when slots fill, there is no annual deadline to plan around, and aggregator batch calendars disagree with each other: one lists June, August and November batches for 2026, another lists March, June and August batches, and neither can be treated as authoritative. The official recruitment page is the only reliable source for current batches, and applicants should check it, choose a batch they can actually attend, and apply early rather than waiting for a deadline that does not exist. A batch that looks open on an aggregator page may already be full on the official page.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Real product experience in Tokyo:</strong> four to six weeks on-site in Shibuya, working on Full-Stack or Front-End development in a live product team, during normal working hours. That is a stronger signal to future employers than a short remote project.</li>
        <li><strong>A monthly subsidy, amount not published:</strong> HENNGE provides a monthly subsidy, but its official page does not publish the amount, so this article states none. Any precise figure quoted by an aggregator for this subsidy is unverified, and you should confirm it with HENNGE before relying on it for a Tokyo budget.</li>
        <li><strong>Round-trip airfare and visa guidance:</strong> airfare to Japan and guidance on the visa process are included in the subsidy package, which removes two of the largest practical barriers to a short Tokyo placement.</li>
        <li><strong>Medical insurance and a Japanese phone with data:</strong> medical insurance is provided, and interns receive a Japanese mobile phone with data, so that daily life and work in Tokyo do not depend on roaming or on buying a local plan on arrival.</li>
        <li><strong>Office facilities, refreshments and cultural events:</strong> office facilities and refreshments during the working day, plus cultural events, are part of the package, and they matter for a short placement: they are how an intern settles into a Tokyo office quickly.</li>
        <li><strong>A possible full-time offer, not a guarantee:</strong> outstanding participants may be offered a full-time role. Treat that as a possibility to work towards, not as part of the award, and do not decline other opportunities on the assumption that it will happen.</li>
        <li><strong>What it is not:</strong> it is not a paid internship and it is not fully funded. The official wording is unpaid with subsidies, and this article uses that wording throughout, because a student who budgets for a salary will run short in Tokyo.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Third-year Bachelor students or above:</strong> Bachelor students in their third year or later, Master and PhD students, and recent graduates are eligible. First and second year undergraduates should wait until they meet the year requirement.</li>
        <li><strong>Computer Science or a related degree, or equivalent technical experience:</strong> a computing degree is the normal route, but equivalent experience, such as an internship or a bootcamp with real technical work, is also accepted. The coding challenge, not the degree title alone, is the practical test.</li>
        <li><strong>Fluent English, no Japanese required:</strong> the working language is English, and Japanese is not required. That is a genuine advantage for international applicants, and it is confirmed on the official page.</li>
        <li><strong>Linux, macOS or Unix-like knowledge:</strong> familiarity with a Unix-like environment is expected, reflecting the development environment at HENNGE. Applicants without that familiarity should build it before the coding challenge.</li>
        <li><strong>Interest in open source and the tech community:</strong> an interest in open-source work and in the wider technology community is part of the profile HENNGE looks for, and it should show in the cover letter, not just in the CV.</li>
        <li><strong>Choose one pathway, or apply separately for both:</strong> Full-Stack and Front-End are separate pathways, and separate applications are required if you apply to both. Do not submit one combined application and expect it to cover both.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV and cover letter,</strong> submitted with the pathway coding challenge and your batch preferences. The coding challenge has no time limit, which is unusual and useful: take the time to do it well rather than rushing it.</li>
        <li><strong>The completed coding challenge:</strong> this is the central document of the application, more important than any transcript. Register and verify your email, complete the pathway challenge, and upload the CV and cover letter with your batch preferences.</li>
        <li><strong>Unverified extras are not stated as requirements:</strong> a GitHub link, passport and enrolment proof appear in a secondary source, but they are not confirmed on the official page, so this article does not present them as official requirements. Have a GitHub profile ready if you have one, because it helps a technical application, but do not treat it as a stated rule.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the official HENNGE recruitment page for the Global Internship Program and check the current batches on that page, not on an aggregator calendar. Choose a batch you can attend in full, on-site in Tokyo.</li>
        <li>Register and verify your email, then complete the coding challenge for your chosen pathway. There is no time limit on the challenge, so use that time to produce clean, working code.</li>
        <li>Upload your CV and cover letter, and select your batch preferences. If you want both pathways, submit separate applications for each.</li>
        <li>Shortlisted candidates receive a phone screening, followed by an online interview. Prepare to discuss your coding challenge work concretely, and your interest in open source and in working in Tokyo.</li>
        <li>Apply early for the batch you want, because applications are reviewed first-come, first-served and batches close when slots fill. Waiting for a deadline that does not exist is the most common way to miss a batch.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the HENNGE internship paid?',
  'No. The official page describes it as unpaid, with comprehensive subsidies: a monthly subsidy (amount not published), round-trip airfare, visa guidance, medical insurance, a Japanese mobile phone with data, office facilities and cultural events. Aggregator "fully funded" labels are wrong.'),
 ('Is there an application deadline?',
  'No fixed deadline is published. Batches run through the year, applications are reviewed first-come, first-served, and a batch closes when its slots fill. Check the official recruitment page for current batches and apply early.'),
 ('Do I need Japanese?',
  'No. The working language is English, and Japanese is not required.'),
 ('How long is the internship and where is it?',
  'Four to six weeks, on-site at HENNGE in Shibuya, Tokyo, Monday to Friday, 10:00 to 19:00 Japan time. It is not a remote internship.'),
 ('Who can apply?',
  'Third-year Bachelor students or above (Bachelor, Master, PhD or recent graduates) in Computer Science or a related field, or with equivalent technical experience, fluent in English, with Linux, macOS or Unix-like knowledge.'),
 ('Will I get a job at HENNGE afterwards?',
  'Possibly, but not guaranteed. Outstanding participants may receive a full-time offer. Treat that as a possibility, not as part of the award.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against HENNGE's official recruitment page (recruit.hennge.com/en/gip: unpaid with comprehensive subsidies, monthly subsidy, round-trip airfare, visa guidance, medical insurance, Japanese mobile phone with data, office facilities and refreshments, cultural events, 4-6 weeks on-site in Shibuya, Tokyo, Mon-Fri 10:00-19:00 JST, Full-Stack and Front-End pathways, third-year Bachelor or above, fluent English with no Japanese required, Linux, macOS or Unix-like knowledge, CV plus cover letter plus coding challenge with no time limit, phone screening then online interview, first-come first-served review) plus Bright Scholarship (queue source) and DAADScholarship.org summaries, and OYA Opportunities for the 2027 advertising. CONFLICTS: (1) Bright and aggregator "fully funded" labels are REJECTED in favour of the official "unpaid with subsidies" wording. (2) Batch calendars disagree across aggregators (Bright: Jun, Aug, Nov 2026; DAAD: Mar, Jun, Aug 2026) and a November batch appears in Bright only and is unverified - the article publishes no batch calendar and directs readers to the live official page. (3) No monthly subsidy amount is published on the official page, so none is stated. (4) GitHub link, passport and enrolment proof appear only in a secondary source and are not presented as official requirements. (5) The 2026 cycle is effectively superseded by 2027 advertising, so the article is framed as rolling batches, not as a 2026 cycle.</p>''',
 dl_long='Rolling — no fixed deadline published (batches close when slots fill, reviewed first-come, first-served)',
 offlinks=[('HENNGE — Global Internship Program (official recruitment page)', 'https://recruit.hennge.com/en/gip/'),
           ('Bright Scholarship — HENNGE Global Internship Program 2026', 'https://brightscholarship.com/hennge-global-internship-program-2026/')],
 related_titles=['ifad-2026', 'humboldt-2026', 'cern-stag-2026', 'huddersfield-2026'])),

DPILLS = {
 'ifad-internship-program-2026': 'Rolling · no fixed deadline published',
 'humboldt-research-fellowship-2026-germany': 'Next call opens 15 Nov 2026',
 'cern-short-term-internship-2026-switzerland': 'Deadline 1 Nov 2026 · %d days left' % dl_left('2026-11-01'),
 'university-of-huddersfield-international-scholarships-2026-uk': 'Automatic · January 2027 entry',
 'hennge-global-internship-program-2026-japan': 'Rolling · batches fill first-come, first-served',
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

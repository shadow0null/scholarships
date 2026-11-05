#!/usr/bin/env python3
"""Batch 62 (cron run 62, 28 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Wang Gungwu Visiting Fellowship 2026 in Singapore - SKIPPED: 2027
   cycle closed 4 Aug 2026 per the official ISEAS brochure (a later
   brochure gives 28 Aug 2026 - conflicting); next cycle not announced.
2. Unilever Future Leaders Programme 2026 - VERIFIED (rolling,
   per-country deadlines; 3-year salaried rotational programme).
3. Japan Study Support Scholarship 2026 - SKIPPED: deadline passed
   31 May 2026 (brightscholarship, scholarsworld, jobandscholarshipnews).
4. MOFA Taiwan Fellowship 2026 - SKIPPED: 2027 cycle closed 30 Jun 2026
   (official taiwanfellowship.ncl.edu.tw); next cycle opens May 2027.
5. Bond University Leadership Scholarships 2026 - SKIPPED: deadline
   passed 31 Aug 2026 ("Applications have now closed", bond.edu.au).
6. Milan University Excellence Scholarship 2026-27 - SKIPPED: deadline
   passed 15 Jun 2026 (one source says 31 May 2026; either way passed).
7. Islamic University of Madinah Scholarship 2026 - VERIFIED
   (applications accepted year-round; fully funded).
8. Malaysian Government MTCP Scholarship 2026-27 - SKIPPED: deadline
   passed 12 Jun 2026 (official MTCP guidelines, mtcp.kln.gov.my).
9. METI Japanese Internship Program 2026 - SKIPPED: deadline passed
   30 Jun 2026 (official internshipprogram.go.jp).
10. University of Birmingham Scholarships 2026 - SKIPPED: family/
    umbrella label, no single scheme; the named 2026 awards closed
    (Future Skills 30 Apr 2026; India PG Chancellor's 31 May 2026).
11. Colombia Government Scholarship 2026-27 - SKIPPED: deadline passed
    5 Jun 2026 (official ICETEX call, via DHET South Africa / esteri.it).
12. Wonju Literature Residency Program 2026 - SKIPPED: deadline passed
    31 May 2026.
13. List of Scholarships in Asia Without IELTS 2026 - SKIPPED: listicle,
    not a single scheme.
14. The Farm Residency Program 2027 - SKIPPED: deadline passed
    1 Jun 2026 (official The Farm Margaret River call).
15. SWJTU Silk Road Scholarship 2026 - SKIPPED: deadline passed
    15 Jun 2026.
16. ANU International Research Scholarships 2026 - VERIFIED (Round 1
    international closed 31 Aug 2026; Round 2 closes 15 Apr 2027).
17. University of Trieste PhD Scholarships 2027 - SKIPPED: 42nd cycle
    closed 31 Aug 2026; next-cycle dates conflicting/not published
    (30 Jun 2027 vs 25 May 2026 vs "not specified").
18. NATO Young Professionals Program 2026 - SKIPPED: deadline passed
    31 May 2026 (nato.int: "no longer accepting applications in 2026").
19. Tsinghua International Summer School 2026 - SKIPPED: 2026 programmes
    closed (deadlines 10 May / 15 May / 10 Jun / 12 Jun 2026); the queue
    title is a guide to several separate summer schools, not one scheme.
20. Just Tech Fellowship 2027 - SKIPPED: deadline passed 28 Jun 2026
    (SSRC; fellows notified Nov 2026).
21. University of Melbourne Human Rights Scholarship 2027 - VERIFIED
    (deadline 31 Oct 2026; AUD 44,500/year 2026 rate).
22. Heinrich Boll Foundation Scholarships 2027 - VERIFIED (next
    deadline 1 Mar 2027; official boell.de; EUR 992/month Master's,
    EUR 1,500/month PhD).
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
 'uflp-2026': {'mono': 'UL', 'title': 'Unilever Future Leaders Programme 2026 Apply Online',
   'href': 'unilever-future-leaders-programme-2026.html',
   'dpill': 'Rolling · varies by country',
   'award': 'A full-time salaried 3-year rotational graduate programme (typically 4 rotations) across Marketing, Finance, Supply Chain, Customer Development, R&D and more, with a mentor, formal training and a route to a first management role. Salary varies by country; no single global figure is published.',
   'elig': 'Recent graduates (UK: graduated within the last 5 years; other countries cap experience at 2–5 years); a Bachelor’s or Master’s degree by the start date; eligible to work in the country of application; fluent English; geographically mobile.',
   'tags': [('Graduate Programme', 'blue'), ('Global', 'teal')]},
 'madinah-2026': {'mono': 'IM', 'title': 'Islamic University of Madinah Scholarship 2026 in Saudi Arabia (Fully Funded)',
   'href': 'islamic-university-of-madinah-scholarship-2026-saudi-arabia.html',
   'dpill': 'Year-round · no single closing date',
   'award': 'Fully funded: full tuition, a monthly stipend (amount not published in the sources checked), free furnished accommodation for unmarried students, healthcare, free return airfare on admission and at the end of each academic year, transport to the Prophet’s Mosque and organised Umrah trips.',
   'elig': 'International Muslim male students (non-Saudi, living outside the Kingdom); undergraduate applicants aged 17–25 with a high-school certificate from the last 5 years; Master’s applicants need a Bachelor’s degree; good conduct and medical fitness; programmes are mainly in Arabic.',
   'tags': [('Undergraduate & Master’s', 'blue'), ('Saudi Arabia', 'teal')]},
 'anu-2026': {'mono': 'ANU', 'title': 'ANU International Research Scholarships 2026 in Australia (Fully Funded)',
   'href': 'anu-international-research-scholarships-2026-australia.html',
   'dpill': 'Deadline 15 Apr 2027 · %d days left' % dl_left('2027-04-15'),
   'award': 'Australian Government Research Training Program (AGRTP) Stipend Scholarship / ANU University Research Scholarship: a stipend of AUD $39,069 a year (2026 rate) for up to 3.5 years plus a 6-month extension, tuition fee offset, travel and removal allowances, thesis allowance, dependent child allowance for international students and paid leave.',
   'elig': 'Domestic and international students in a Master’s by Research or PhD at ANU with First Class Honours (H1) or equivalent, a qualified supervisor and English language requirements met; Industry PhD candidates on a full-time salary are not eligible.',
   'tags': [('Master’s & PhD', 'blue'), ('Australia', 'teal')]},
 'melb-hr-2027': {'mono': 'UM', 'title': 'University of Melbourne Human Rights Scholarship 2027 in Australia (Fully Funded)',
   'href': 'university-of-melbourne-human-rights-scholarship-2027-australia.html',
   'dpill': 'Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': 'Fully funded graduate research award: a living allowance of AUD $44,500 a year (2026 rate), a full tuition fee offset (up to 2 years for a Master’s, 4 years for a PhD), a relocation grant of AUD $2,000–$3,000 and OSHC for international students who need a visa. Total package up to AUD $94,200.',
   'elig': 'Domestic and international students applying for a Master’s by Research or PhD at the University of Melbourne starting in 2027, whose research is in human rights; must not have completed a research degree at the same or higher level or previously held a similar graduate research scholarship.',
   'tags': [('Master’s & PhD', 'blue'), ('Australia', 'teal')]},
 'boell-2027': {'mono': 'HB', 'title': 'Heinrich Boll Foundation Scholarships 2027 in Germany (Funded)',
   'href': 'heinrich-boll-foundation-scholarships-2027-germany.html',
   'dpill': 'Next deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
   'award': 'A monthly stipend of €992 for Master’s students and €1,500 for PhD students, plus possible additional allowances, for the standard period of study at a state or state-recognised German university. Funded by the Federal Ministry of Education and Research and the Federal Foreign Office.',
   'elig': 'International students (priority to applicants from DAC countries not yet living in Germany) who completed their first degree abroad and apply before starting a Master’s in Germany, or PhD applicants with a graduate degree from abroad; strong academics, social and political engagement, and German at B2 / DSH 1 level.',
   'tags': [('Master’s & PhD', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Unilever UFLP 2026
A.append(dict(
 slug='unilever-future-leaders-programme-2026',
 title='Unilever Future Leaders Programme 2026 Apply Online',
 meta='Unilever Future Leaders Programme (UFLP) 2026: a full-time salaried 3-year rotational graduate programme across Marketing, Finance, Supply Chain, Customer Development and R&D, with a mentor and a route to a first management role. Deadlines are rolling and vary by country — check Unilever Careers.',
 short='Unilever Future Leaders Programme 2026', kicker='Global · Graduate Programme · Salaried', mono='UL',
 prov_short='Unilever', prov_cat='Company · Global',
 h1='Unilever Future Leaders Programme 2026 Apply Online',
 sub='Read this first, because there is no single UFLP deadline to circle on a calendar — and any page that prints one is guessing. The Unilever Future Leaders Programme is a full-time, salaried, 3-year rotational graduate programme run separately in each country, so every country sets its own window: the UK intake for 2026 opened on 15 September 2025 and closes on a rolling basis once places fill, the Netherlands R&D window ran 2–21 March 2026, and the South Africa Marketing window closed on 29 February 2026. What is the same everywhere is the shape of the programme: about four rotations over three years, real responsibility from day one, a mentor, formal training, and a first management role at the end of it.',
 dpill='Rolling · varies by country',
 facts=facts([('Award', 'A full-time salaried graduate programme lasting 3 years (36 months), typically with 4 rotations. Trainees are hired into one function — Marketing, Finance, Supply Chain, Customer Development/Sales, Research & Development, Human Resources or Unilever Food Solutions — and rotate across teams in that function, with one rotation often outside it. The first assignment is usually a retail experience, learning the business at the point of sale. Each trainee gets a mentor, a personal development plan, formal training through Unilever’s academies, and exposure to senior leaders. Pay is a competitive salary that varies by country; no single global salary figure is published.'),
              ('Eligible', 'Recent graduates and young professionals. The UK route is for people who graduated within the last 5 years; the Philippines route is open to students graduating in 2026 and professionals with at most 2 years of work experience; the Netherlands route recommends at most 5 years of experience. You need a Bachelor’s or Master’s degree (or equivalent) by the programme start date, eligibility to work in the country you apply in, fluency in English (and Dutch where the role requires it), and willingness to be geographically mobile for rotations. Some functions ask for a relevant degree — Supply Chain looks for STEM or supply-chain-related qualifications, R&D for science or engineering.'),
              ('How', '1) Go to Unilever Careers and search for "Future Leaders" in the country you want to work in. 2) Complete the online application — in several countries you can import your details from LinkedIn. 3) Complete the online assessment (a personality/profile assessment plus a cognitive assessment) and the digital interview. 4) Shortlisted candidates are invited to an assessment centre or Discovery Centre. 5) Successful candidates start on the country’s start date — 1 September 2026 in the Netherlands, April 2026 in South Africa.'),
              ('Deadline', 'Rolling — varies by country; there is no single global deadline. The UK intake opened 15 September 2025 and closes on a rolling basis once application numbers are reached. The Netherlands R&D window (2–21 March 2026) and the South Africa Marketing window (29 February 2026) have closed. Listings for the Vietnam 2026 intake were still showing applications open at the time of checking. Check Unilever Careers for the country you want.'),
              ('Fine print', 'UFLP is a job, not a scholarship: you are a full-time Unilever employee from day one, so the usual graduate-scheme rules apply — you can generally only apply for one track, the first you applied for, and you cannot hold a search-year/orientation-year visa in the Netherlands (EU nationals and R&D talents excepted). Unilever does not charge an application fee. Third-party pages that call the programme "fully funded" are describing the salaried package, not a scholarship grant.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Unilever Future Leaders Programme (UFLP)</strong> is Unilever’s flagship graduate scheme: a <strong>full-time, salaried, 3-year (36-month) rotational leadership programme</strong> that hires top graduates into one function and develops them, through live projects, into readiness for a first management role. You are a Unilever employee from day one, working on real business challenges across a company whose brands reach 3.4 billion people a day in more than 190 countries.</p>
      <p>The programme is built around <strong>rotations</strong> — typically <strong>four over three years</strong> — inside your chosen function, with the chance of one rotation outside it. Marketing trainees rotate across brand management, innovation, digital marketing, media and consumer insights; Finance trainees work across accounting, reporting and analysis; Supply Chain trainees work across planning, procurement, logistics and manufacturing; Customer Development trainees work across sales, key account management, e-commerce and category management; R&D trainees rotate across up to four R&D roles and may work internationally. The <strong>first assignment is usually a retail experience</strong> — learning the heart of the business at the point of sale. Along the way you get a <strong>mentor</strong>, a personal development plan, formal training through Unilever’s academies, and exposure to senior leaders.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>recent graduate or young professional</strong>. The UK route is for people who <strong>graduated within the last 5 years</strong>; the Philippines route is open to students <strong>graduating in 2026</strong> and professionals with at most <strong>2 years of work experience</strong>; the Netherlands route recommends at most <strong>5 years of experience</strong>.</li>
        <li>A <strong>Bachelor’s or Master’s degree (or equivalent)</strong> by the programme start date.</li>
        <li><strong>Eligible to work in the country</strong> you apply in before the start date — Unilever cannot sponsor a visa for most UFLP roles.</li>
        <li><strong>Fluent in English</strong> (and in Dutch where the role requires it).</li>
        <li><strong>Geographically mobile</strong> — the programme includes rotations in different locations.</li>
        <li>Some functions ask for a relevant degree: <strong>Supply Chain</strong> looks for STEM or supply-chain-related qualifications; <strong>R&amp;D</strong> looks for science or engineering.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>A full-time salary</strong> from day one — this is a job, not a scholarship grant. The amount varies by country and is not published as a single global figure.</li>
        <li><strong>3 years of rotations</strong> (typically 4) across your function, with real responsibility and real projects from the start.</li>
        <li>A <strong>mentor</strong> and a personal development plan, plus formal training through Unilever’s academies.</li>
        <li><strong>Exposure to senior leaders</strong> and a route to a first management role on successful completion.</li>
        <li>Benefits reported for the programme include <strong>insurance, health and wellness support, leave arrangements and a subsidised onsite shop</strong> (the exact package varies by country).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>CV or résumé</strong> — in several countries you can import your details from <strong>LinkedIn</strong> when you apply.</li>
        <li>Proof of your <strong>degree or expected graduation date</strong>, and of your <strong>right to work</strong> in the country you apply in.</li>
        <li>No separate scholarship-style document list is published — the programme is applied for as a job, through Unilever Careers.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to <strong>Unilever Careers</strong> and search for <strong>"Future Leaders"</strong> in the country you want to work in.</li>
        <li>Complete the <strong>online application</strong> — in several countries you can import your details from LinkedIn.</li>
        <li>Complete the <strong>online assessment</strong> (a personality/profile assessment plus a cognitive assessment) and the <strong>digital interview</strong> (in the Netherlands this is the SOVA interview, completed in English).</li>
        <li>Shortlisted candidates are invited to an <strong>assessment centre or Discovery Centre</strong>.</li>
        <li>Successful candidates start on the country’s start date — <strong>1 September 2026</strong> in the Netherlands, <strong>April 2026</strong> in South Africa.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Unilever Future Leaders Programme 2026?',
  'There is no single global deadline — it varies by country and closes on a rolling basis. The UK intake opened 15 September 2025 and closes once application numbers are reached. The Netherlands R&D window (2–21 March 2026) and the South Africa Marketing window (29 February 2026) have closed, while Vietnam 2026 listings were still showing applications open. Check Unilever Careers for your country.'),
 ('Is the Unilever Future Leaders Programme a scholarship?',
  'No. It is a full-time salaried job — a 3-year rotational graduate programme. Third-party pages that call it "fully funded" are describing the salaried package, not a scholarship grant.'),
 ('How long is the Unilever Future Leaders Programme?',
  'Three years (36 months), typically with four rotations inside your chosen function, plus formal training, a mentor and a personal development plan.'),
 ('Who can apply for UFLP?',
  'Recent graduates and young professionals — in the UK, people who graduated within the last 5 years; in the Philippines, students graduating in 2026 and professionals with at most 2 years of experience; in the Netherlands, applicants with at most 5 years of experience are recommended. You need a degree by the start date, the right to work in the country, fluent English and willingness to relocate for rotations.'),
 ('What functions can I join in UFLP?',
  'Marketing, Finance, Supply Chain, Customer Development/Sales, Research & Development, Human Resources and Unilever Food Solutions, depending on the country.'),
 ('What is the selection process for UFLP?',
  'An online application, an online assessment (personality/profile plus cognitive tests), a digital interview, and then an assessment centre or Discovery Centre for shortlisted candidates. In the Netherlands the process runs on a first-come, first-served basis, so early application matters.'),
 ('Do I need a specific degree for UFLP?',
  'Not for most functions — Unilever says personality sets applicants apart in Marketing, for example. Supply Chain prefers STEM or supply-chain-related degrees, and R&D looks for science or engineering.'),
 ('Can I apply for more than one UFLP track?',
  'No — your application is considered for one track, the first you applied for, so choose the function you want most.')]) + '''
      <p class="verify">Verified 28 Oct 2026 from Unilever's own careers material and live job postings — the Unilever UK & Ireland Early Careers brochure 2026 (tbcdn.talentbrew.com; UFLP "open once a year, typically around Q3", "close on a rolling basis"), Bright Network (UK applications opened Monday 15 September 2025; 3-year programme; graduated within the last 5 years), Adzuna Netherlands listings for the 2026 intake (start 1 September 2026; Master's/Bachelor's required; max 5 years experience recommended; Dutch and English fluency), the Netherlands R&D posting (online application 2–21 March 2026, first-come first-served; SOVA digital interview in English), the Philippines Supply Chain posting (open to students graduating in 2026 and professionals with max 2 years experience), WayUp/Prosple programme descriptions (36-month programme, 4 rotations, first assignment a retail experience, mentor, formal training) and Built In Vietnam (UFLP 2026 applications officially open) — plus corroboration from Scholarship Union: programme details and structure; duration 3 years; no single global deadline (deadlines differ per job); no application fee. CONFLICTS: (1) Third-party pages that call UFLP "fully funded" are describing the salaried package, not a scholarship grant — the article states this plainly. (2) Salary: one job board lists €52.7k/year for the Netherlands R&D track; no single global salary figure is published, so none is stated. (3) The UK brochure and Bright Network give the 15 September 2025 opening for the 2026 intake; the Netherlands and South Africa windows for the same intake have already closed — the article lists each country's window separately rather than printing one deadline.</p>''',
 dl_long='Rolling — varies by country (no single global deadline; UK opened 15 Sep 2025, closes when places fill)',
 offlinks=[('Unilever Careers — UK & Ireland Early Careers (official brochure)', 'https://tbcdn.talentbrew.com/company/34155/cms/early-careers/early-careers-uk-and-ireland/Unilever_UK-EC_Brochure_2026.pdf'),
           ('Bright Network — Unilever Future Leaders Programme (UK)', 'https://www.brightnetwork.co.uk/graduate-jobs/unilever/unilever-future-leaders-programme-register-your-interest?search_id=beb88dbcde437f2708b5a5224f90199f&search_position=1'),
           ('WayUp — UFLP Supply Chain programme description', 'https://www.wayup.com/i-Consumer-Goods-j-Supply-Chain-Unilever-Future-Leaders-Program-UFLP-Unilever-714078376611116/'),
           ('Bright Scholarship — Unilever Future Leaders Programme 2026', 'https://brightscholarship.com/unilever-future-leaders-programme-2026/')],
 related_titles=['adidas-internships-2027', 'ista-internships-2027', 'fbi-honors-2027', 'claude-corps-2027'])),

# ---------------------------------------------------------------- 2. Islamic University of Madinah Scholarship 2026
A.append(dict(
 slug='islamic-university-of-madinah-scholarship-2026-saudi-arabia',
 title='Islamic University of Madinah Scholarship 2026 in Saudi Arabia (Fully Funded)',
 meta='Islamic University of Madinah Scholarship 2026: fully funded study in Saudi Arabia for international Muslim male students — full tuition, monthly stipend, free accommodation, healthcare and return airfare. Applications accepted year-round.',
 short='Islamic University of Madinah Scholarship 2026', kicker='Saudi Arabia · Undergraduate & Master’s · Fully Funded', mono='IM',
 prov_short='Islamic University of Madinah', prov_cat='University · Saudi Arabia',
 h1='Islamic University of Madinah Scholarship 2026 in Saudi Arabia (Fully Funded)',
 sub='Read this first, because the dates floating around for this scholarship disagree with each other — and the university itself does not publish one fixed closing date. Secondary sources report a 2026 undergraduate deadline of 14 June 2026 (others say 21 May 2026), while the university’s own pattern is to accept applications year-round, and a 2027 guide reports the 1447 AH entry as open now. Treat the programme as open and check the official portal for the current intake, rather than trusting any single date on an aggregator page. What is not in doubt is the package: a fully funded place at the Islamic University of Madinah for international Muslim male students, covering tuition, a monthly stipend, free furnished accommodation, healthcare and return airfare.',
 dpill='Year-round · no single closing date',
 facts=facts([('Award', 'Fully funded by the Government of the Kingdom of Saudi Arabia: full tuition fee coverage for the whole programme; a monthly stipend (the amount is not published in the sources checked); free furnished accommodation for unmarried students; free healthcare at the university hospital; a free return air ticket on admission and at the end of each academic year; free daily transport to and from the Prophet’s Mosque; regular organised Umrah trips; an extra allowance for students with excellent grades; meals at the university restaurant for a small monthly fee; and access to social, training and sports facilities.'),
              ('Eligible', 'International Muslim male students from all countries (non-Saudi nationals residing outside the Kingdom). Undergraduate applicants must be aged 17–25 and hold a high-school diploma or equivalent (12 years of education) from within the last 5 years. Master’s applicants need a Bachelor’s degree — one source reports a minimum GPA of 3.75 out of 5. All applicants must be of good conduct and in good physical and medical health, and must follow the university’s rules. No IELTS is required for undergraduate entry; postgraduate applicants are assessed on Arabic proficiency, since most programmes are taught in Arabic.'),
              ('How', '1) Apply online through the university’s official scholarship portal (the "My Scholarships at the Islamic University of Madinah" page) or through the Saudi government’s Study in Saudi Arabia portal (studyinsaudi.sa). 2) Upload the required documents, attested by the Saudi Embassy or a recognised authority, in Arabic or English. 3) Correct any errors in the original documents before submission. 4) Wait for the university’s decision — successful applicants receive an admission letter and a free air ticket.'),
              ('Deadline', 'Applications are accepted year-round, according to several secondary sources; the university does not publish one fixed closing date. Secondary sources report a 2026 undergraduate deadline of 14 June 2026 (one source says 21 May 2026) and a 31 October 2026 date for another track — these conflict and are not confirmed on the official site. A 2027 guide reports the 1447 AH entry as open now. Check the official portal for the current intake.'),
              ('Fine print', 'The university was founded in 1961 by royal decree and hosts students from more than 170 countries. Programmes span Islamic sciences (Shariah, Quran, Hadith, Arabic language, Da’wah) and modern disciplines (engineering, computer science, sciences). The scholarship is for male students only. The stipend amount is not published in the sources checked, so no figure is stated here.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Islamic University of Madinah Scholarship</strong> is a <strong>fully funded</strong> government scholarship for <strong>international Muslim male students</strong> to study at the <strong>Islamic University of Madinah</strong> in Saudi Arabia — an institution founded in <strong>1961</strong> by royal decree, in one of Islam’s most significant cities, which today hosts students from <strong>more than 170 countries</strong>. It covers <strong>undergraduate, Master’s and PhD</strong> study across the university’s colleges: Shariah, the Holy Quran, Hadith, Arabic Language, Da’wah and Fundamentals of Religion, alongside the Colleges of Science, Engineering, and Computer and Information Systems.</p>
      <p>The package is comprehensive: <strong>full tuition</strong>, a <strong>monthly stipend</strong>, <strong>free furnished accommodation</strong> for unmarried students, <strong>healthcare</strong> at the university hospital, a <strong>free return air ticket</strong> on admission and at the end of each academic year, <strong>free daily transport to the Prophet’s Mosque</strong>, regular <strong>organised Umrah trips</strong>, and meals at the university restaurant for a small monthly fee. An <strong>extra allowance</strong> is paid to students with excellent grades. Study is conducted primarily in <strong>Arabic</strong>, so postgraduate applicants are assessed on language proficiency as part of selection.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Muslim male students</strong> from any country — non-Saudi nationals residing outside the Kingdom.</li>
        <li><strong>Undergraduate:</strong> aged <strong>17–25</strong>, with a <strong>high-school diploma or equivalent</strong> (12 years of education) from within the <strong>last 5 years</strong>.</li>
        <li><strong>Master’s:</strong> a <strong>Bachelor’s degree</strong> (16 years of education); one source reports a minimum GPA of <strong>3.75 out of 5</strong>.</li>
        <li><strong>Good conduct</strong> and <strong>good physical and medical health</strong>.</li>
        <li><strong>No IELTS</strong> is required for undergraduate entry. Postgraduate applicants are assessed on <strong>Arabic proficiency</strong>, since most programmes are taught in Arabic.</li>
        <li>Applicants must be willing to follow the university’s rules and regulations.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee coverage</strong> for the entire programme.</li>
        <li>A <strong>monthly stipend</strong> to cover living expenses (the amount is not published in the sources checked).</li>
        <li><strong>Free furnished accommodation</strong> for unmarried students.</li>
        <li><strong>Free healthcare</strong> at the university hospital.</li>
        <li>A <strong>free return air ticket</strong> on admission and at the end of each academic year.</li>
        <li><strong>Free daily transport</strong> to and from the Prophet’s Mosque and regular <strong>organised Umrah trips</strong>.</li>
        <li>An <strong>extra allowance</strong> for students with excellent grades.</li>
        <li>Meals at the university restaurant for a <strong>small monthly fee</strong>, plus access to social, training and sports facilities.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Passport</strong> (valid).</li>
        <li><strong>Birth certificate.</strong></li>
        <li><strong>High-school transcripts and certificates</strong> (and degree certificates for postgraduate applicants).</li>
        <li><strong>Testimony of conduct</strong> / character reference, plus a <strong>recommendation letter</strong> from religious leaders or a recognised Islamic authority (reported by secondary sources).</li>
        <li>A <strong>medical report</strong> confirming fitness.</li>
        <li>All documents in <strong>Arabic or English</strong>, with originals <strong>attested by the Saudi Embassy or a recognised authority</strong>. Correct any errors in the original documents before submission.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the <strong>official Islamic University of Madinah scholarship portal</strong> — the "My Scholarships at the Islamic University of Madinah" page at iu.edu.sa — or apply through the Saudi government’s <strong>Study in Saudi Arabia portal</strong> (studyinsaudi.sa).</li>
        <li>Complete the <strong>online application form</strong> and upload the required documents.</li>
        <li>Make sure all original documents are <strong>attested by the Saudi Embassy or a recognised authority</strong>, and correct any errors before submission.</li>
        <li>Wait for the university’s decision. Successful applicants receive an <strong>admission letter</strong> and a free air ticket.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Islamic University of Madinah Scholarship fully funded?',
  'Yes. It covers full tuition, a monthly stipend, free furnished accommodation for unmarried students, healthcare, a free return air ticket on admission and at the end of each academic year, transport to the Prophet’s Mosque and organised Umrah trips.'),
 ('Who can apply for the Islamic University of Madinah Scholarship?',
  'International Muslim male students from any country (non-Saudi nationals living outside the Kingdom). Undergraduate applicants must be aged 17–25 with a high-school certificate from the last 5 years; Master’s applicants need a Bachelor’s degree. Applicants must be of good conduct and medically fit.'),
 ('What is the deadline for the Islamic University of Madinah Scholarship 2026?',
  'The university does not publish one fixed closing date — several sources report that applications are accepted year-round. Secondary sources give conflicting 2026 dates (14 June 2026, 21 May 2026 and 31 October 2026 for different tracks), none of which is confirmed on the official site. A 2027 guide reports the 1447 AH entry as open now. Check the official portal for the current intake.'),
 ('Is IELTS required for the Islamic University of Madinah Scholarship?',
  'No, IELTS is not required for undergraduate entry. Postgraduate applicants are assessed on Arabic proficiency, since most programmes are taught in Arabic.'),
 ('What does the Madinah scholarship cover?',
  'Full tuition, a monthly stipend (amount not published in the sources checked), free furnished accommodation for unmarried students, healthcare, a free return air ticket on admission and at the end of each academic year, daily transport to the Prophet’s Mosque, organised Umrah trips, and an extra allowance for excellent grades.'),
 ('Can female students apply for the Islamic University of Madinah Scholarship?',
  'No. The scholarship is for male students only.'),
 ('Which programmes can I study at the Islamic University of Madinah?',
  'Undergraduate, Master’s and PhD programmes across Shariah, Quran, Hadith, Arabic Language, Da’wah, Science, Engineering and Computer and Information Systems — including Civil, Electrical and Mechanical Engineering, Physics, Mathematics, Chemistry, Renewable Energy, Mechatronics and Robotics.'),
 ('How do I apply for the Islamic University of Madinah Scholarship?',
  'Apply online through the university’s official scholarship portal at iu.edu.sa, or through the Saudi government’s Study in Saudi Arabia portal (studyinsaudi.sa), uploading attested documents in Arabic or English.')]) + '''
      <p class="verify">Verified 28 Oct 2026 from multiple independent secondary sources agreeing on the core facts — ScholarWaka (deadline 14 June 2026; fully funded; tuition, accommodation, monthly allowance, flights, healthcare; Muslim male; founded 1961; students from 130+ countries; study mainly in Arabic), EngineersJob (deadline 21 May 2026; UG 17–25, high-school certificate within last 5 years; Master's GPA 3.75/5; documents — passport, birth certificate, transcripts, testimony of conduct, attested by the Saudi Embassy; benefits list), StudyCorner (fully funded; Muslim male only; no IELTS; applications year-round; deadline listed as 14 June 2026 / 31 Oct 2026; official site iu.edu.sa), PakAdmissions (UG deadline 14 June 2026; Master's year-round; 170+ countries), OpportunitiesNexus 2027 guide (OPEN — 1447 AH entry applications now accepted; apply through studyinsaudi.sa/en; contact care@iu.edu.sa; information verified from iu.edu.sa/en-us, fetched live 22 September 2026) and FutureHelpPortal (benefits list; colleges list) — plus the queue's Bright Scholarship listing. CONFLICTS: (1) The 2026 deadline is reported as 21 May 2026 (EngineersJob), 14 June 2026 (ScholarWaka, PakAdmissions), 14 June / 31 Oct 2026 (StudyCorner) and "year-round" (StudyCorner FAQ, PakAdmissions for Master's) — none confirmed on the official site, so the article states year-round acceptance and lists the conflict rather than printing one date. (2) The monthly stipend amount is not published in any source checked, so no figure is stated. (3) The Master's GPA of 3.75/5 comes from one secondary source and is presented as reported. (4) The "arrival cash reward" appears in one secondary source only and is not stated as confirmed.</p>''',
 dl_long='Applications accepted year-round (no single published closing date; check the official portal for the current intake)',
 offlinks=[('Islamic University of Madinah — official website', 'https://iu.edu.sa'),
           ('Study in Saudi Arabia — official government portal', 'https://studyinsaudi.sa/en'),
           ('ScholarWaka — Islamic University of Madinah Scholarship 2026', 'https://scholarwaka.com/islamic-university-madinah-scholarship/'),
           ('Bright Scholarship — Islamic University of Madinah Scholarship 2026', 'https://brightscholarship.com/islamic-university-of-madinah-scholarships/')],
 related_titles=['qatar-gov-2027', 'alqasimi-foundation-2026', 'hokkaido-mext-2027', 'tsukuba-mext-2027'])),

# ---------------------------------------------------------------- 3. ANU International Research Scholarships 2026
A.append(dict(
 slug='anu-international-research-scholarships-2026-australia',
 title='ANU International Research Scholarships 2026 in Australia (Fully Funded)',
 meta='ANU International Research Scholarships 2026: the Australian Government Research Training Program (AGRTP) Stipend Scholarship at the Australian National University — AUD $39,069 a year (2026 rate), tuition fee offset, up to 3.5 years. Round 2 closes 15 April 2027; no separate application.',
 short='ANU International Research Scholarships 2026', kicker='Australia · Master’s & PhD · Fully Funded', mono='ANU',
 prov_short='Australian National University', prov_cat='University · Australia',
 h1='ANU International Research Scholarships 2026 in Australia (Fully Funded)',
 sub='Read this first, because the deadline in the listing title — "April 2026" — is last year’s Round 2 date, not the live one. The Australian National University runs its research scholarships in two rounds a year: Round 1 for international students closed on 31 August 2026, and Round 2, for international and domestic students, closes on 15 April 2027. The award is the Australian Government Research Training Program (AGRTP) Stipend Scholarship alongside the ANU University Research Scholarship: a stipend of AUD $39,069 a year at the 2026 rate, a tuition fee offset, and up to 3.5 years of funding. And there is no separate scholarship form for new applicants — you are automatically considered when you apply for a research degree.',
 dpill='Deadline 15 Apr 2027 · %d days left' % dl_left('2027-04-15'),
 facts=facts([('Award', 'The AGRTP Stipend Scholarship (and the ANU University Research Scholarship) pays a stipend of AUD $39,069 per annum at the 2026 full-time rate, paid fortnightly, for up to 3.5 years full-time, with a 6-month extension available. It also covers the tuition fee offset, travel and removal allowances for students relocating to Canberra, a thesis allowance, a dependent child allowance (international students only) and paid medical, maternity and parental leave. One secondary source gives AUD $40,475 per annum — that appears to be the 2027 rate; this article uses the 2026 rate.'),
              ('Eligible', 'Domestic and international students enrolled in, or applying for, an accredited Higher Degree by Research (Master’s by Research or PhD) at the Australian National University. You need First Class Honours (H1) or an H1 equivalent in your prior studies, and you must meet the academic and English-language requirements for the HDR programme. Industry PhD candidates receiving a full-time salary are not eligible. Selection is a competitive ranking on academic record, research potential, supervisor support, referee reports, English competency and comparison with other applications in the same round. A qualified supervisor is essential — without one, an application has little realistic chance.'),
              ('How', '1) Apply for admission to a Higher Degree by Research programme at ANU. 2) In the admission application, select the scholarships you want to be considered for, including the University Research Scholarship and the AGRTP Stipend Scholarship — there is no separate application form for new candidates. 3) Submit by the round deadline, ideally 2–3 weeks early so referee reports can arrive. 4) Current ANU HDR students (typically with less than one year of full-time equivalent study completed) use the "Request for a current ANU student to be considered for a HDR scholarship" form.'),
              ('Deadline', 'Round 2 (international and domestic) closes 15 April 2027, for commencement by 31 August 2027. Round 1 international closed 31 August 2026 and Round 1 domestic closes 31 October 2026, for commencement between 1 January and 31 March 2027.'),
              ('Fine print', 'The queue title’s "April 2026" was the Round 2 date for the 2026 cycle; the live Round 2 is 15 April 2027. The stipend figure is the 2026 rate; the 2027 rate is reported as AUD $40,475 by one secondary source and is not stated as confirmed. Some secondary pages describe the application as "rolling" — the official rounds are fixed (31 August / 31 October / 15 April), so this article uses the round dates.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>ANU International Research Scholarships</strong> are the Australian National University’s research awards for domestic and international students in a <strong>Higher Degree by Research</strong> — a Master’s by Research or a PhD — in Canberra. The two main awards are the <strong>Australian Government Research Training Program (AGRTP) Stipend Scholarship</strong> and the <strong>ANU University Research Scholarship</strong>, both awarded through the same admission process.</p>
      <p>The package is <strong>fully funded</strong>: a <strong>stipend of AUD $39,069 a year</strong> at the 2026 full-time rate, paid fortnightly, for up to <strong>3.5 years</strong> (with a 6-month extension available), plus a <strong>tuition fee offset</strong>, <strong>travel and removal allowances</strong> for relocating to Canberra, a <strong>thesis allowance</strong>, a <strong>dependent child allowance</strong> for international students, and <strong>paid medical, maternity and parental leave</strong>. ANU is Australia’s top-ranked university, and the scholarship is awarded by competitive ranking in two rounds a year.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>domestic or international student</strong> enrolled in, or applying for, an accredited <strong>Higher Degree by Research</strong> (Master’s by Research or PhD) at ANU.</li>
        <li><strong>First Class Honours (H1) or an H1 equivalent</strong> in your prior studies.</li>
        <li>You must meet the <strong>academic and English-language requirements</strong> for the HDR programme (one guide reports IELTS 6.5 overall, no subscore below 6.0).</li>
        <li><strong>Industry PhD candidates receiving a full-time salary are not eligible.</strong></li>
        <li>Selection is competitive, based on <strong>academic record, research potential, supervisor support, referee reports, English competency</strong> and comparison with other applications in the same round. A <strong>qualified supervisor is essential</strong> — without one, an application has little realistic chance.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>stipend of AUD $39,069 a year</strong> (2026 full-time rate, paid fortnightly) for up to <strong>3.5 years</strong>, with a <strong>6-month extension</strong> available.</li>
        <li>A <strong>tuition fee offset</strong> covering the cost of the research degree.</li>
        <li><strong>Travel and removal allowances</strong> for students relocating to Canberra.</li>
        <li>A <strong>thesis allowance</strong> and a <strong>dependent child allowance</strong> for international students.</li>
        <li><strong>Paid medical, maternity and parental leave.</strong></li>
        <li><strong>No separate scholarship application</strong> — you are automatically considered on your HDR admission application.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>HDR admission application</strong>, in which you select the scholarships you want to be considered for.</li>
        <li><strong>Academic transcripts</strong> and a <strong>research proposal</strong>, a <strong>CV</strong>, and <strong>letters of recommendation</strong> (referee reports are part of the ranking).</li>
        <li>Proof of <strong>English language proficiency</strong>.</li>
        <li>Contact <strong>3–5 potential supervisors</strong> per field before applying — supervisor support is part of the selection criteria.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Find and contact a <strong>qualified supervisor</strong> at ANU in your research area — supervisor support is essential.</li>
        <li>Apply for admission to a <strong>Higher Degree by Research programme</strong> at ANU.</li>
        <li>In the admission application, <strong>select the scholarships</strong> you want to be considered for, including the University Research Scholarship and the AGRTP Stipend Scholarship. There is <strong>no separate application form</strong> for new candidates.</li>
        <li>Submit by the round deadline — <strong>15 April 2027</strong> for Round 2 — ideally <strong>2–3 weeks early</strong> so referee reports can arrive.</li>
        <li>Current ANU HDR students (typically with less than one year of full-time equivalent study completed) use the <strong>"Request for a current ANU student to be considered for a HDR scholarship"</strong> form.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the ANU International Research Scholarships 2026?',
  'Round 2 (international and domestic) closes 15 April 2027, for commencement by 31 August 2027. Round 1 international closed 31 August 2026 and Round 1 domestic closes 31 October 2026, for commencement between 1 January and 31 March 2027. The "April 2026" date in the listing title was the Round 2 date for the 2026 cycle.'),
 ('How much is the ANU research scholarship stipend?',
  'AUD $39,069 per annum at the 2026 full-time rate, paid fortnightly, for up to 3.5 years (with a 6-month extension available). One secondary source gives AUD $40,475 per annum, which appears to be the 2027 rate and is not stated as confirmed.'),
 ('Do I need a separate application for the ANU research scholarship?',
  'No, for new candidates. You are automatically considered when you apply for admission to a Higher Degree by Research programme — just select the scholarships you want to be considered for in the admission application. Current ANU HDR students use a separate request form.'),
 ('Who can apply for the ANU International Research Scholarships?',
  'Domestic and international students in, or applying for, a Master’s by Research or PhD at ANU, with First Class Honours (H1) or equivalent, who meet the academic and English-language requirements. Industry PhD candidates receiving a full-time salary are not eligible.'),
 ('Is a supervisor required for the ANU research scholarship?',
  'Effectively yes. Selection depends on supervisor support and available space and resources in a research area aligned with ANU’s research strategy, and guides advise contacting 3–5 potential supervisors per field.'),
 ('What does the ANU AGRTP scholarship cover?',
  'A stipend of AUD $39,069 a year (2026 rate), a tuition fee offset, travel and removal allowances, a thesis allowance, a dependent child allowance for international students, and paid medical, maternity and parental leave.'),
 ('How long does ANU research scholarship funding last?',
  'Up to 3.5 years full-time, with a 6-month extension available, subject to satisfactory academic progress.'),
 ('Is IELTS required for the ANU research scholarship?',
  'You must meet ANU’s English language requirements for the HDR programme. One guide reports IELTS 6.5 overall with no subscore below 6.0.')]) + '''
      <p class="verify">Verified 28 Oct 2026 from multiple independent sources agreeing on the rounds, the stipend and the automatic-consideration route — the AGRTP Stipend Scholarship round table (o4af.com: 2026 Round 1 International 31 August 2026, Round 1 Australian 31 October 2026, Round 2 15 April 2027; AUD $40,475 per annum; travel/removal stipends, thesis allowance, dependent child allowance, paid leave), IDP's ANU University Research Scholarship listing (H1 or equivalent; no separate application — automatic consideration on the HDR admission application; Round 1 International closing 31 August each year; Round 2 closing 15 April each year; award deadline 31 Aug 2026), CoursMooc (AUD $39,069 per annum, 2026 rate; 3.5 years; 6-month extension; rounds 31 August / 31 October / 15 April; apply 2–3 weeks early for referee reports), AfterSchoolAfrica (AUD $39,069 per annum, 2026 full-time base rate; 3.5 years; 6-month extension; apply for HDR admission, indicate interest, no separate application) and ScholarshipsFuture (Round 1 31 August 2026, Round 2 15 April 2027; AUD 38,950 tax-free stipend — an older figure). CONFLICTS: (1) The stipend is reported as AUD $39,069 (2026 rate, two sources), AUD $40,475 (o4af, appears to be the 2027 rate) and AUD $38,950 (ScholarshipsFuture, older figure) — the article uses the 2026 rate of $39,069 and notes the $40,475 figure. (2) ScholarshipsFuture describes applications as "rolling" — the official rounds are fixed (31 August / 31 October / 15 April), so the article uses the round dates. (3) The queue's "April 2026" deadline was the Round 2 date for the 2026 cycle; the live Round 2 is 15 April 2027.</p>''',
 dl_long='15 April 2027 (Round 2, international and domestic; Round 1 international closed 31 August 2026)',
 offlinks=[('IDP — ANU University Research Scholarships (official ANU listing via IDP)', 'https://www.idp.com/scholarship/the-australian-national-university/anu-university-research-scholarships/116503/?lang=km'),
           ('O4af — AGRTP Stipend Scholarship round table', 'https://o4af.com/opportunity/australian-government-research-training-program-stipend-scholarship/?sector_cat=social-science&ajax_filter=true'),
           ('AfterSchoolAfrica — ANU AGRTP Stipend Scholarship 2026', 'https://www.afterschoolafrica.com/114891/anu-australian-government-research-training-program/'),
           ('Bright Scholarship — ANU International Research Scholarships 2026', 'https://brightscholarship.com/anu-international-research-scholarships-2026/')],
 related_titles=['melbourne-grs-2027', 'rtp-2027', 'macquarie-2027', 'vuw-2027'])),

# ---------------------------------------------------------------- 4. Melbourne Human Rights Scholarship 2027
A.append(dict(
 slug='university-of-melbourne-human-rights-scholarship-2027-australia',
 title='University of Melbourne Human Rights Scholarship 2027 in Australia (Fully Funded)',
 meta='University of Melbourne Human Rights Scholarship 2027: fully funded graduate research in human rights — AUD $44,500 a year living allowance (2026 rate), full tuition fee offset, relocation grant and OSHC. Deadline 31 October 2026.',
 short='Melbourne Human Rights Scholarship 2027', kicker='Australia · Master’s & PhD · Fully Funded', mono='UM',
 prov_short='University of Melbourne', prov_cat='University · Australia',
 h1='University of Melbourne Human Rights Scholarship 2027 in Australia (Fully Funded)',
 sub='Read this first, because the deadline is three days away — 31 October 2026 — and this is a research scholarship, not a taught Master’s award. The University of Melbourne Human Rights Scholarship funds graduate research in human rights: a living allowance of AUD $44,500 a year at the 2026 rate, a full tuition fee offset, a relocation grant and Overseas Student Health Cover for international students. It is open to domestic and international students applying for a Master’s by Research or a PhD starting in 2027, and it asks for something most scholarships do not: evidence of a commitment to human rights beyond your academic study, through voluntary work or professional experience.',
 dpill='Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'Fully funded: a living allowance of AUD $44,500 per annum (2026 rate, full-time, pro-rata) — up to 2 years for a Master’s by Research or 3.5 years for a PhD — plus a full tuition fee offset (up to 2 years for a Master’s, 4 years for a PhD), a relocation grant of AUD $2,000 for students moving from within Australia or AUD $3,000 for international students, and single Overseas Student Health Cover for international students who need a student visa. The total package is valued at up to AUD $94,200. One secondary source gives AUD $43,500 a year — that is the 2025 rate; this article uses the 2026 rate.'),
              ('Eligible', 'Domestic and international students. You must apply for, and meet the entry requirements of, a Master’s by Research or PhD at the University of Melbourne starting in 2027, and your proposed research must be in the area of human rights. You must not have completed a research degree at the same or higher level, and must not have previously received a similar graduate research scholarship. You should be able to show a commitment to the peaceful advancement of respect for human rights beyond academic study — voluntary work or professional experience are given as examples.'),
              ('How', '1) Apply for a graduate research degree at the University of Melbourne and receive an offer for a degree commencing in the scholarship year. 2) Submit the scholarship application through the University of Melbourne Scholarships Portal by 31 October 2026. 3) Outcomes are expected by email in February 2027. Applicants for graduate research courses are reported to be exempt from the university’s international application fee.'),
              ('Deadline', '31 October 2026 (applications opened 1 April 2026). Outcomes are expected by email in February 2027.'),
              ('Fine print', 'This is a research scholarship — taught Master’s programmes are not eligible. The living allowance figure differs across sources (AUD $44,500 for 2026, AUD $43,500 for 2025); the article uses the 2026 rate. English requirements follow the course: Melbourne accepts evidence of English proficiency through previous English-medium study or an approved English test, depending on the course requirements.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Melbourne Human Rights Scholarship</strong> exists to foster research in the field of human rights and to encourage work that advances and protects human rights at national and international level. It funds <strong>graduate research</strong> — a <strong>Master’s by Research or a PhD</strong> — for students whose proposed research sits in the human rights field, and it is open to <strong>domestic and international students</strong> alike.</p>
      <p>The package is <strong>fully funded</strong>: a <strong>living allowance of AUD $44,500 a year</strong> at the 2026 rate, a <strong>full tuition fee offset</strong>, a <strong>relocation grant</strong> of AUD $2,000 for students moving from within Australia or AUD $3,000 for international students, and <strong>single Overseas Student Health Cover</strong> for international students who need a student visa. The total package is valued at up to <strong>AUD $94,200</strong>. What sets this award apart is its selection focus: alongside academic excellence and research potential, the university looks for a <strong>demonstrated commitment to human rights beyond academic study</strong>, through voluntary work or professional experience.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Domestic and international students</strong> of all nationalities.</li>
        <li>Apply for, and meet the entry requirements of, a <strong>Master’s by Research or PhD</strong> at the University of Melbourne <strong>starting in 2027</strong>.</li>
        <li>Your proposed research must be in the <strong>area of human rights</strong>.</li>
        <li>You must <strong>not have completed a research degree at the same or higher level</strong>.</li>
        <li>You must <strong>not have previously received a similar graduate research scholarship</strong>.</li>
        <li>You should be able to show a <strong>commitment to the peaceful advancement of respect for human rights beyond academic study</strong> — voluntary work or professional experience are given as examples.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>living allowance of AUD $44,500 a year</strong> (2026 rate, full-time, pro-rata), for up to <strong>2 years</strong> (Master’s by Research) or <strong>3.5 years</strong> (PhD), including paid leave.</li>
        <li>A <strong>full tuition fee offset</strong> — up to 2 years (Master’s) or 4 years (PhD).</li>
        <li>A <strong>relocation grant</strong> of AUD $2,000 (within Australia) or AUD $3,000 (international).</li>
        <li><strong>Single Overseas Student Health Cover</strong> for international students who need a student visa.</li>
        <li>Total package valued at up to <strong>AUD $94,200</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>graduate research course application</strong> and the <strong>scholarship application</strong> through the University of Melbourne Scholarships Portal.</li>
        <li>Secondary sources report the course application needs <strong>academic transcripts, proof of language proficiency, a personal statement, a valid passport and a CV</strong> — treat this as a secondary-source list, not an officially confirmed checklist.</li>
        <li>Evidence of your <strong>commitment to human rights</strong> beyond academic study (voluntary work or professional experience).</li>
        <li>English proficiency: Melbourne accepts evidence through <strong>previous English-medium study or an approved English test</strong>, depending on the course requirements — do not assume an IELTS waiver applies to you.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for a <strong>graduate research degree</strong> (Master’s by Research or PhD) at the University of Melbourne in the human rights field, and <strong>receive an offer</strong> for a degree commencing in the scholarship year.</li>
        <li>Submit the <strong>scholarship application</strong> through the <strong>University of Melbourne Scholarships Portal</strong> by <strong>31 October 2026</strong>.</li>
        <li>Outcomes are expected by <strong>email in February 2027</strong>. Individual feedback is not provided to unsuccessful applicants.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Melbourne Human Rights Scholarship 2027?',
  '31 October 2026. Applications opened 1 April 2026, and outcomes are expected by email in February 2027.'),
 ('How much is the Melbourne Human Rights Scholarship worth?',
  'A living allowance of AUD $44,500 a year (2026 rate), a full tuition fee offset, a relocation grant of AUD $2,000–$3,000 and single OSHC for international students who need a visa — a total package valued at up to AUD $94,200.'),
 ('Who can apply for the Melbourne Human Rights Scholarship?',
  'Domestic and international students applying for a Master’s by Research or PhD at the University of Melbourne starting in 2027, whose research is in human rights, who have not completed a research degree at the same or higher level and have not previously held a similar graduate research scholarship.'),
 ('Is the Human Rights Scholarship for taught Master’s degrees?',
  'No. It is for graduate research degrees only — a Master’s by Research or a PhD. Taught Master’s programmes are not eligible.'),
 ('Do I need an admission offer before applying for the Human Rights Scholarship?',
  'Yes. The eligibility rules state you must have received an offer for a graduate research degree commencing in the scholarship year.'),
 ('Does my research have to be called "Human Rights"?',
  'Not necessarily, but the proposed research must genuinely fall within the field of human rights — your application should make that connection explicit rather than assuming the selection panel will infer it.'),
 ('Is professional or volunteer experience required?',
  'The university asks applicants to address their commitment to human rights beyond academic study, giving voluntary and work experience as examples. In practice, you should provide concrete evidence of that commitment wherever possible.'),
 ('Is there an application fee for the Melbourne Human Rights Scholarship?',
  'Applicants for graduate research courses are reported to be exempt from the university’s international application fee.')]) + '''
      <p class="verify">Verified 28 Oct 2026 from multiple independent sources agreeing on the deadline, the package and the research-only scope — EngineersJob (deadline 31 October 2026; living allowance $43,500/year; full fee offset up to 2 years Master's / 4 years PhD; relocation $2,000–$3,000; OSHC; no previous graduate research scholarship; must not have completed a research degree at the same or higher level), Olainfo (applications open 1 April 2026; deadline 31 October 2026; value up to $94,200; living allowance $43,500/year at 2025 rates; Master's 2 years / PhD 3.5 years), LegalMaestros (living allowance $44,500 per annum, 2026 rate; full tuition fee offset up to 2 years Master's / 4 years PhD; deadline 31 October 2026; commitment to human rights beyond academic study), Scholarship Union (deadline 31 October 2026; $43,500/year; relocation $2,000/$3,000; OSHC; fully funded), DAADScholarship (deadline 31 October 2026; outcomes by email February 2027; offer required; research must genuinely fall within human rights; commitment evidence expected) and a YouTube guide (living allowance AUD $44,500/year; deadline 31 October 2026; research scholarship not a taught Master's; graduate research applicants exempt from the international application fee; English via previous English-medium study or an approved test). CONFLICTS: (1) The living allowance is reported as AUD $44,500 (2026 rate, LegalMaestros quoting the official page and the YouTube guide) and AUD $43,500 (2025 rate, EngineersJob, Olainfo, Scholarship Union) — the article uses the 2026 rate of $44,500. (2) The fee-offset duration is 4 years for a PhD (LegalMaestros, EngineersJob) while the living allowance runs 3.5 years for a PhD — both are stated separately in the article. (3) The official Melbourne scholarships page was not fetched verbatim this run; the official-page wording is quoted via LegalMaestros.</p>''',
 dl_long='31 October 2026 (outcomes by email in February 2027)',
 offlinks=[('EngineersJob — University of Melbourne Human Rights Scholarship 2027', 'https://engineersjob.in/university-of-melbourne-human/'),
           ('LegalMaestros — Human Rights Scholarship 2027 (quotes the official page)', 'https://legalmaestros.com/opportunities/fellowships/university-of-melbourne-human-rights-scholarship-2027-fully-funded-opportunity-for-graduate-research-students/'),
           ('DAADScholarship — Human Rights Scholarship 2027', 'https://daadscholarship.com/university-of-melbourne-human-rights-scholarship-2027-allow-foreign-students/'),
           ('Bright Scholarship — University of Melbourne Human Rights Scholarship 2027', 'https://brightscholarship.com/university-of-melbourne-human-rights-scholarship-2027/')],
 related_titles=['melbourne-grs-2027', 'rtp-2027', 'ucl-impact-2027', 'glasgow-leadership-2027'])),

# ---------------------------------------------------------------- 5. Heinrich Boll Foundation Scholarships 2027
A.append(dict(
 slug='heinrich-boll-foundation-scholarships-2027-germany',
 title='Heinrich Boll Foundation Scholarships 2027 in Germany (Funded)',
 meta='Heinrich Böll Foundation Scholarships 2027: funded Master’s and PhD study in Germany — €992 a month for Master’s students, €1,500 a month for PhD students, plus allowances. Next deadline 1 March 2027 (portal opens 15 January 2027); German B2 required.',
 short='Heinrich Böll Foundation Scholarships 2027', kicker='Germany · Master’s & PhD · Funded', mono='HB',
 prov_short='Heinrich Böll Foundation', prov_cat='Foundation · Germany',
 h1='Heinrich Boll Foundation Scholarships 2027 in Germany (Funded)',
 sub='Read this first, because the next window has not opened yet — and that is the point. The Heinrich Böll Foundation’s international graduate scholarships run in two windows a year: the Spring 2027 portal opens on 15 January 2027 and closes on 1 March 2027, and the Fall 2027 window runs 15 July to 1 September 2027. The award supports Master’s and PhD study at any state or state-recognised university in Germany — €992 a month for Master’s students and €1,500 a month for PhD students, plus possible additional allowances — and it is aimed at academically strong, socially engaged students, with priority to applicants from DAC countries who have not yet moved to Germany. The hard requirement to plan around now is German: B2 level, or DSH 1.',
 dpill='Next deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
 facts=facts([('Award', 'A monthly stipend of €992 for Master’s students and €1,500 for PhD students, plus possible additional allowances, for the standard period of study, with a possible one-semester extension. Around 1,500 scholarships are awarded every year across all disciplines (plus about 200 doctoral awards). The programme is funded by the Federal Ministry of Education and Research (BMBF) and the Federal Foreign Office (AA). Tuition is not the issue in Germany — most public universities charge no tuition — so the stipend is the core of the award.'),
              ('Eligible', 'International students from EU and non-EU countries, with priority given to applicants from DAC countries who have not yet taken up residence in Germany at the time of application. Master’s applicants must have completed their first degree abroad and apply before starting a Master’s programme in Germany. PhD applicants must have completed a graduate degree abroad and apply for a PhD programme in Germany. Applicants need a strong academic record, social commitment and political interest aligned with the foundation’s values — democracy, ecology, human rights, participation and social responsibility — and German language skills at B2 level or DSH 1. There is no published numerical age limit and no application fee.'),
              ('How', '1) Prepare during the preparation window: German-language certification (B2 / DSH 1), university admission, academic references and evidence of social or political engagement. 2) Apply online through the Foundation’s scholarship portal when it opens — Spring 2027: 15 January to 1 March 2027; Fall 2027: 15 July to 1 September 2027. 3) Use the official information flyer and the programme-specific checklists to confirm the full requirements before applying.'),
              ('Deadline', 'Spring 2027: 15 January to 1 March 2027. Fall 2027: 15 July to 1 September 2027. Both windows are published on the Foundation’s own scholarships page.'),
              ('Fine print', 'One aggregator gives the window as "15 January 2027 to September 1, 2027" — that conflates the two separate windows; the official page lists Spring (15 January–1 March 2027) and Fall (15 July–1 September 2027) separately, and this article follows the official page. Some secondary pages list the stipend as €934–€1,450 a month; the figures used here (€992 Master’s / €1,500 PhD) come from the most recent 2027 guides.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Heinrich Böll Foundation Scholarships</strong> — the Foundation’s <strong>"Tailwind for Talents"</strong> programme for graduates and PhD students — support international students who want to do a <strong>Master’s degree or a PhD in Germany</strong>, at any <strong>state or state-recognised university</strong>, in <strong>any academic discipline</strong>. The Foundation awards around <strong>1,500 scholarships a year</strong> (plus about 200 doctoral awards), funded by the <strong>Federal Ministry of Education and Research (BMBF)</strong> and the <strong>Federal Foreign Office (AA)</strong>.</p>
      <p>The award is a <strong>monthly stipend</strong>: <strong>€992 for Master’s students</strong> and <strong>€1,500 for PhD students</strong>, plus possible additional allowances, for the <strong>standard period of study</strong> with a possible one-semester extension. Since most German public universities charge no tuition, the stipend is the core of the award. The Foundation is the green political foundation close to the German Green Party, and it looks for applicants whose academic work and social engagement line up with its values: <strong>democracy, ecology, human rights, participation and social responsibility</strong>. Priority goes to applicants from <strong>DAC countries</strong> who have <strong>not yet taken up residence in Germany</strong> when they apply.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International students</strong> from EU and non-EU countries; <strong>priority</strong> to applicants from <strong>DAC countries</strong> who have <strong>not yet taken up residence in Germany</strong> at the time of application.</li>
        <li><strong>Master’s applicants:</strong> you must have <strong>completed your first degree abroad</strong> and apply <strong>before starting</strong> a Master’s programme in Germany.</li>
        <li><strong>PhD applicants:</strong> you must have <strong>completed a graduate degree abroad</strong> and apply for a PhD programme in Germany.</li>
        <li>A <strong>strong academic record</strong> plus <strong>social commitment and political interest</strong> aligned with the Foundation’s values.</li>
        <li><strong>German language skills at B2 level or DSH 1</strong> — this is the requirement to plan around now, since certification takes time.</li>
        <li>There is <strong>no published numerical age limit</strong> and <strong>no application fee</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly stipend of €992</strong> for Master’s students and <strong>€1,500</strong> for PhD students.</li>
        <li><strong>Possible additional allowances</strong> on top of the stipend.</li>
        <li>Funding for the <strong>standard period of study</strong>, with a possible <strong>one-semester extension</strong>.</li>
        <li>Study at any <strong>state or state-recognised university in Germany</strong>, in any discipline.</li>
        <li>Access to the Foundation’s <strong>seminars, networks and professional development</strong> (reported by secondary sources).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>German-language certification</strong> at B2 level or DSH 1.</li>
        <li><strong>University admission</strong> (or evidence of application) for the Master’s or PhD programme in Germany.</li>
        <li><strong>Academic references</strong> and <strong>evidence of social or political engagement</strong>.</li>
        <li>The Foundation publishes <strong>programme-specific checklists</strong> — use the official information flyer and checklist for your applicant group to confirm the full requirements before applying. No definitive document list is stated here because the official page points applicants to those checklists.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Use the preparation window now: obtain your <strong>German-language certification (B2 / DSH 1)</strong>, secure <strong>university admission</strong>, and gather <strong>academic references and evidence of social or political engagement</strong>.</li>
        <li>When the portal opens, apply online through the <strong>Foundation’s scholarship portal</strong> — <strong>Spring 2027: 15 January to 1 March 2027</strong>; <strong>Fall 2027: 15 July to 1 September 2027</strong>.</li>
        <li>Check the official <strong>information flyer and programme-specific checklists</strong> on the Foundation’s scholarships page before submitting.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Heinrich Böll Foundation Scholarships 2027?',
  'There are two windows: Spring 2027 runs 15 January to 1 March 2027, and Fall 2027 runs 15 July to 1 September 2027. Both are published on the Foundation’s own scholarships page.'),
 ('How much is the Heinrich Böll Foundation Scholarship worth?',
  '€992 a month for Master’s students and €1,500 a month for PhD students, plus possible additional allowances, for the standard period of study with a possible one-semester extension.'),
 ('Who can apply for the Heinrich Böll Foundation Scholarship?',
  'International students from EU and non-EU countries, with priority to applicants from DAC countries who have not yet taken up residence in Germany. Master’s applicants must have completed their first degree abroad and apply before starting the Master’s in Germany; PhD applicants need a graduate degree from abroad.'),
 ('Do I need German to apply for the Heinrich Böll Foundation Scholarship?',
  'Yes — German language skills at B2 level or DSH 1 are required for international graduate applicants.'),
 ('Is there an age limit for the Heinrich Böll Foundation Scholarship?',
  'No numerical age limit is published.'),
 ('What does the Heinrich Böll Foundation look for in applicants?',
  'Academic strength plus social commitment and political interest aligned with the Foundation’s values — democracy, ecology, human rights, participation and social responsibility.'),
 ('Is there an application fee for the Heinrich Böll Foundation Scholarship?',
  'No — there is no application fee.'),
 ('Which universities can I study at with the Böll Scholarship?',
  'Any state or state-recognised university in Germany, in any academic discipline.')]) + '''
      <p class="verify">Verified 28 Oct 2026 against the Foundation's own page — boell.de/en/scholarships (checked via search, crawled 4 hours ago: "Tailwind for Talents: Scholarships for Graduates and PhD students"; priority to DAC-country applicants not yet resident in Germany; "Our next application deadlines: Spring 2027: 15 January 2027 until 1 March 2027; Fall 2027: 15 July 2027 until 1 September 2027"; funded by BMBF and the Federal Foreign Office; contact studienwerk@boell.de) — plus corroboration from Careeraidhub (Spring 2027 portal opens 15 January 2027, closes 1 March 2027; second window 15 July–1 September 2027; German B2/DSH; Master's €992), DAADScholarship (status announced, applications open 15 January 2027; Master's €992/month plus allowances; PhD €1,500/month plus allowances; German B2 or DSH 1; no age limit; no fees; Spring deadline 1 March 2027; Fall deadline 1 September 2027; verified 20 September 2026), GlobalScholarshipsHub (up to €992/month for non-EU students; deadlines 1 March and 1 September annually) and AfterSchoolAfrica (deadline 15 January 2027 to 1 September 2027 — see conflict note). CONFLICTS: (1) AfterSchoolAfrica prints the window as "15 January 2027 to September 1, 2027" — that conflates the two separate windows; the official page lists Spring (15 January–1 March 2027) and Fall (15 July–1 September 2027) separately, and the article follows the official page. (2) Some secondary pages list the stipend as €934–€1,450 a month; the figures used here (€992 Master's / €1,500 PhD) come from the most recent 2027 guides (Careeraidhub, DAADScholarship). (3) GlobalScholarshipsHub gives the second window as "1 March to 1 September 2027" — the official page gives 15 July to 1 September 2027, and the article follows the official page.</p>''',
 dl_long='1 March 2027 (Spring 2027 window: 15 January – 1 March 2027; Fall 2027 window: 15 July – 1 September 2027)',
 offlinks=[('Heinrich Böll Foundation — Scholarships (official)', 'https://www.boell.de/en/scholarships'),
           ('CareerAidHub — Heinrich Böll Scholarship 2027: Opens 15 January', 'https://careeraidhub.com/heinrich-boll-foundation-scholarships-for-masters-students/'),
           ('DAADScholarship — Heinrich Boll Foundation Scholarships 2027', 'https://daadscholarship.com/germany-heinrich-boll-foundation-scholarships-2027-9-application-submission-steps/'),
           ('Bright Scholarship — Heinrich Boll Foundation Scholarships 2027', 'https://brightscholarship.com/heinrich-boll-foundation-scholarships-2027/')],
 related_titles=['gottingen-daad-2027', 'sbw-berlin-2027', 'glasgow-leadership-2027', 'ucl-impact-2027'])),

for a in A:
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

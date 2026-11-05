#!/usr/bin/env python3
"""Batch 21 (cron run 21, 19 Oct 2026): articles 1-2 — beVisioneers Fellowship 2027, Tampere University Scholarships 2027.

1. beVisioneers: The Mercedes-Benz Fellowship 2027 (Cohort 5). Applications open
   21 Sep 2026 -> 31 Jan 2027 (23:59:59 CET). Two-year programme: 12-month
   Foundation Year (min 24 hrs/month, hybrid + Local Hubs + Regional/Global
   Summits) then Acceleration Year. Project scholarships up to EUR 15,000,
   fully funded summit travel, needs-based cost-of-living support. Eligibility:
   18-28 on the deadline, resident in an eligible country (EU, India, Indonesia,
   Kenya, Malaysia, Mexico, Rwanda, South Africa, Tanzania, Uganda, US,
   Zimbabwe) for the fellowship duration, good English, an environmental project
   or strong idea, entrepreneurial spirit; not employed by Mercedes-Benz (and no
   parent/guardian there). Verified across the official site, official
   application portal, the programme's official LinkedIn (Cohort 5 = 250
   fellows) and 6 independent trackers, all consistent.
2. Tampere University Scholarships 2027 (Finland). 50% tuition-fee scholarship
   for non-EU/EEA/Switzerland fee-paying students in English-taught Bachelor's
   and Master's programmes; limited number, awarded at admission, covers the
   normative degree duration. Master's: 14 Dec 2026 - 7 Jan 2027 (attachments
   by 14 Jan 2027); Bachelor's joint application: 7-21 Jan 2027. Tuition
   EUR 10,000/yr (bachelor's) / EUR 12,000/yr (master's); EUR 2,000 Early Bird
   first-year reduction; EUR 2,000 graduation scholarship into the master's.
   Verified on the official tuni.fi 2027 admissions pages + 3 trackers.
   Honesty: explicitly partial (tuition-only), not fully funded.
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'bevisioneers2027': dict(mono='BV', title='beVisioneers: The Mercedes-Benz Fellowship 2027 (Funded)', href='bevisioneers-mercedes-benz-fellowship-2027.html',
              dpill='31 Jan 2027 · 104 days to go', award='Project scholarships up to €15,000 + training, mentoring, fully funded summit travel', elig='Age 18–28; resident in an eligible country (India included); an environmental project or strong idea; good English.',
              tags=[('Fellowship', 'purple'), ('Worldwide', 'teal')]),
 'tampere2027': dict(mono='TA', title='Tampere University Scholarships 2027 in Finland (Funded)', href='tampere-university-scholarships-2027-finland.html',
              dpill='7 Jan 2027 · 80 days to go', award='50% tuition fee scholarship for the full degree (limited number, awarded at admission)', elig='Non-EU/EEA fee-paying applicants to English-taught Bachelor’s/Master’s programmes.',
              tags=[('Bachelor’s', 'blue'), ('Master’s', 'blue'), ('Finland', 'teal')]),
 'kuas2027': dict(mono='KU', title='Kyoto University of Advanced Science Scholarships 2027 in Japan (Funded)', href='kyoto-university-of-advanced-science-scholarships-2027-japan.html',
              dpill='26 Feb 2027 · 130 days to go', award='Super KUAS-E: 100% tuition + admission fee + ¥1.2M/year stipend; KUAS-E: 100/50/20% reductions', elig='International students applying to KUAS international (English-track) programmes.',
              tags=[('Bachelor’s', 'blue'), ('Master’s', 'blue'), ('Japan', 'teal')]),
 'nims2026': dict(mono='NI', title='NIMS Internship Program in Japan (Fully Funded)', href='nims-internship-program-japan.html',
              dpill='Opens Dec 2026', award='Daily allowance + accommodation for selected interns (up to 90 days research)', elig='Current undergraduate or graduate students worldwide; materials-science-related fields.',
              tags=[('Internship', 'green'), ('Japan', 'teal')]),
 'waikato2027': dict(mono='WA', title='University of Waikato Vice-Chancellor’s International Excellence Scholarship 2027 (Funded)', href='university-of-waikato-vice-chancellors-international-excellence-scholarship-2027.html',
              dpill='30 Nov 2026 · 42 days to go', award='Up to NZD 15,000 (UG) / NZD 10,000 (PG) tuition credit for the first year', elig='New international students with an offer of place; B+ GPA equivalency or better.',
              tags=[('Bachelor’s', 'blue'), ('Master’s', 'blue'), ('New Zealand', 'teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 1. beVisioneers
ARTICLES.append(dict(
 slug='bevisioneers-mercedes-benz-fellowship-2027',
 title='beVisioneers: The Mercedes-Benz Fellowship 2027 (Funded) | StudyDesk Scholarships',
 meta='beVisioneers: The Mercedes-Benz Fellowship 2027 — a two-year environmental fellowship for 18–28-year-olds with innovation training, mentorship, and project scholarships up to €15,000. India is eligible. Applications close 31 January 2027.',
 short='beVisioneers Mercedes-Benz Fellowship 2027',
 kicker='Worldwide · Fellowship',
 mono='BV', prov_short='Mercedes-Benz × The DO School', prov_cat='Corporate Foundation · Fellowship',
 h1='beVisioneers: The Mercedes-Benz Fellowship 2027 (Funded)',
 sub='A two-year fellowship that turns young environmental ideas into real projects. beVisioneers — funded by Mercedes-Benz and run by The DO School Fellowships — gives 18–28-year-olds innovation training, 1:1 venture coaching and mentoring, a global peer network, and the chance to win project scholarships of up to €15,000. Cohort 5 is recruiting now, and applications close 31 January 2027.',
 dpill='31 Jan 2027 · 104 days to go', dl_long='31 January 2027 at 23:59:59 CET. Applications opened 21 September 2026; shortlisted applicants complete an online activity in March 2027, selection happens in April 2027, and the 12-month Foundation Year begins in June 2027.',
 facts=facts([('Award','Project scholarships up to €15,000 <small>Competitive project scholarships after year one; a needs-based cost-of-living stipend is available in the Acceleration Year, and travel, accommodation and expenses are covered for the Regional and Global Summits</small>'),
              ('Who it is for','Environmental innovators 18–28 <small>Resident in an eligible country (India included) for the duration of the fellowship; good command of English; an environmental problem identified plus an existing project or a strong idea; committed to positive environmental change with an entrepreneurial mindset</small>'),
              ('Structure','Two years <small>Year 1: intensive 12-month Foundation Year (minimum 24 hours/month) — online innovation training, Local Hub gatherings, Regional and Global Summits, 1:1 venture coaching and mentoring. Year 2: Acceleration Year to scale the venture</small>'),
              ('Cohort size','250 fellows <small>Per the programme’s official LinkedIn announcement for Cohort 5 (2027). Older aggregator posts about “1000 fellows” refer to earlier cohorts’ targets, not the 2027 call</small>'),
              ('Countries','13 eligible <small>EU countries, India, Indonesia, Kenya, Malaysia, Mexico, Rwanda, South Africa, Tanzania, Uganda, the United States, and Zimbabwe. Applicants must live in an eligible country for the fellowship duration and implement their project there</small>')]),
 body='''<h2 id="about">About the fellowship</h2>
<p><strong>beVisioneers: The Mercedes-Benz Fellowship</strong> is a two-year programme that supports young people building solutions to environmental challenges. It is funded by <strong>Mercedes-Benz</strong> and designed and implemented by <strong>The DO School Fellowships</strong>; the programme launched in 2023 and the 2027 call is its <strong>fifth cohort</strong>.</p>
<p>The programme is built for early-stage eco-innovation — climate, sustainability, circular economy, clean energy, waste, biodiversity, agriculture, mobility and related areas — including projects that are still at the idea or prototype stage. Selection focuses on three things: genuine dedication to environmental change, an entrepreneurial mindset (persistence, resilience, determination), and a project that is genuinely planet-positive. Grades, degrees and money already raised are not the criteria.</p>
<p><strong>Cohort note:</strong> the programme’s official LinkedIn announcement says Cohort 5 (2027) is looking for <strong>250 fellows</strong>. Some aggregator pages mention “1000 fellows” — that figure comes from earlier cohorts’ messaging, not the 2027 call.</p>
<h2 id="benefits">What fellows get</h2>
<ul>
<li><strong>Project scholarships of up to €15,000</strong> — competitive awards to develop fellows’ environmental projects after the first year.</li>
<li><strong>Innovation training</strong> designed to fit around work or university, plus <strong>1:1 venture coaching</strong> and <strong>1:1 mentoring</strong> from experts.</li>
<li><strong>Community and summits:</strong> three Local Hub gatherings with nearby fellows, Regional Summits and a Global Summit — with <strong>travel, accommodation and expenses covered</strong>.</li>
<li><strong>Acceleration Year (year two):</strong> a needs-based <strong>cost-of-living stipend</strong>, support to scale the venture, and introductions to investors, accelerators and climate scientists.</li>
<li><strong>Needs-based participation support:</strong> if a laptop or a stable internet connection stands between an applicant and the programme, the beVisioneers team can help.</li>
<li>The programme is <strong>hybrid</strong> (online learning plus in-person activities) and run in <strong>English</strong>.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Age:</strong> 18 to 28 years old at the time of applying (the programme states applicants must be 18–28 on the 31 January 2027 closing date).</li>
<li><strong>Residency:</strong> resident in one of the eligible countries or territories for the duration of the fellowship, and the project must be implemented in that same country.</li>
<li><strong>Eligible countries for 2027:</strong> European Union countries, India, Indonesia, Kenya, Malaysia, Mexico, Rwanda, South Africa, Tanzania, Uganda, the United States, and Zimbabwe.</li>
<li><strong>Language:</strong> a good command of English.</li>
<li><strong>Project:</strong> an identified environmental problem you want to solve, with an existing project or a strong idea for a planet-positive project. <strong>No previous entrepreneurial experience or formal technical training is required.</strong></li>
<li><strong>Mindset:</strong> commitment to positive environmental change and a demonstrably entrepreneurial spirit.</li>
<li><strong>Exclusions:</strong> you must not work for Mercedes-Benz, and must not have a parent or guardian who works there.</li>
</ul>
<h2 id="documents">What the application involves</h2>
<p>The application is built to understand your potential, not your background, and takes roughly <strong>30–45 minutes</strong>:</p>
<ul>
<li><strong>Written section</strong> — personal details, the environmental problem and your solution, your progress so far, and your motivation.</li>
<li><strong>Video component</strong> — a recorded video interview. Treat this as essential: earlier cohorts’ guidance states applications without the video are not considered.</li>
<li><strong>Financial-support section (optional)</strong> — for applicants who need assistance to participate; financial assistance is also available during the application process itself if needed.</li>
<li>Your application can be <strong>saved and completed later</strong> on the portal.</li>
<li><strong>No application fee</strong> is published for this programme.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Check eligibility</strong> — age, country of residence, English, and your environmental project or idea.</li>
<li><strong>Create an account</strong> on the official beVisioneers application portal and start the Cohort 5 application.</li>
<li><strong>Describe your environmental problem, your solution and the progress you have made</strong> — clearly and honestly.</li>
<li><strong>Record your video interview</strong> and upload it with the application.</li>
<li><strong>Submit before 31 January 2027 at 23:59:59 CET</strong> — that is 04:29 IST on 1 February.</li>
<li><strong>If shortlisted:</strong> complete the online activity in <strong>March 2027</strong>; selection runs through <strong>April 2027</strong>.</li>
</ol>
<p>Published timeline: applications opened <strong>21 September 2026</strong> → deadline <strong>31 January 2027</strong> → shortlisted online activity <strong>March 2027</strong> → selection <strong>April 2027</strong> → Foundation Year begins <strong>June 2027</strong>.</p>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('How many fellows are selected in 2027?','The programme’s official LinkedIn announcement says Cohort 5 is looking for 250 young people. Figures of “1000 fellows” seen on some older aggregator pages refer to earlier cohorts’ messaging, not the 2027 call.'),
 ('Is the fellowship fully funded?','Summit participation is fully funded (travel, accommodation and expenses), and fellows can compete for project scholarships of up to €15,000 plus needs-based support in the Acceleration Year. There is no published monthly salary during the Foundation Year.'),
 ('Can I apply from India?','Yes — India is explicitly on the 2027 eligible-country list, alongside EU countries, Indonesia, Kenya, Malaysia, Mexico, Rwanda, South Africa, Tanzania, Uganda, the US and Zimbabwe.'),
 ('Do I need a finished project to apply?','No. The programme targets early-stage eco-innovation, including projects at the idea or prototype stage. What matters is a real environmental problem and a genuine idea for solving it.'),
 ('What is the age rule exactly?','You must be between 18 and 28 years old at the time of applying; the programme phrases it as 18–28 on the 31 January 2027 application closing date.'),
 ('How much time does it take?','A minimum of 24 hours per month during the 12-month Foundation Year — designed to fit around work or university.'),
 ('Do I need to speak German?','No. The programme is run in English; what matters is a good command of written and spoken English.'),
 ('Who runs it?','Designed and implemented by The DO School Fellowships and funded by Mercedes-Benz. It is not a government programme.'),
]),
 verify='Verified 19 Oct 2026 against the programme’s official site (bevisioneers.world), the official application portal (applications.bevisioneers.world — Cohort 5 application), the programme’s official LinkedIn (Cohort 5, 250 fellows, deadline 31 January 2027) and six independent opportunity trackers, all consistent on the 31 January 2027 23:59:59 CET deadline, the 21 September 2026 opening, project scholarships of up to €15,000, the 18–28 age window, the eligible-country list including India, and the Foundation-Year/Acceleration-Year structure. The 2027 call is Cohort 5 (not the “2026” label on the queue entry); the “1000 fellows” figure seen on some aggregators refers to earlier cohort messaging, not the 2027 call.',
 offlinks=[('beVisioneers — official website','https://bevisioneers.world/'),
           ('Official application portal (Cohort 5)','https://applications.bevisioneers.world/courses/course/11-bevisioneers-mercedes-benz-fellowship')],
 related_titles=['mopga','aixbio','wb-gaf'],
))

# ---------------------------------------------------------------- 2. Tampere
ARTICLES.append(dict(
 slug='tampere-university-scholarships-2027-finland',
 title='Tampere University Scholarships 2027 in Finland | StudyDesk Scholarships',
 meta='Tampere University Scholarships 2027: 50% tuition-fee scholarships for non-EU/EEA students in English-taught Bachelor’s and Master’s programmes. Master’s applications 14 Dec 2026–7 Jan 2027; Bachelor’s joint application 7–21 Jan 2027.',
 short='Tampere University Scholarships 2027',
 kicker='Finland · University',
 mono='TA', prov_short='Tampere University', prov_cat='Public University · Finland',
 h1='Tampere University Scholarships 2027 in Finland (Funded)',
 sub='Finland’s second-largest university funds a share of its best international applicants. Tampere University awards <strong>50% tuition-fee scholarships</strong> — granted at admission to a limited number of exceptionally qualified fee-paying students — across its English-taught Bachelor’s and Master’s programmes. Master’s applications run 14 December 2026 to 7 January 2027; Bachelor’s joint applications run 7–21 January 2027.',
 dpill='7 Jan 2027 · 80 days to go', dl_long='Master’s programmes: 14 December 2026 (08:00, UTC+2) – 7 January 2027 (23:59, UTC+2); all attachments by 14 January 2027; admission results 23 March 2027. Bachelor’s programmes: national joint application 7–21 January 2027.',
 facts=facts([('Award','50% tuition fee scholarship <small>Granted at admission to a limited number of exceptionally qualified fee-paying applicants; covers the normative duration of the degree (3 years bachelor’s, 2 years master’s). Very limited in number — in the 2026 admission round, nine tuition-fee scholarships were awarded across all programmes</small>'),
              ('Tuition 2027','€10,000/year bachelor’s · €12,000/year master’s <small>Indicative annual tuition for international fee-paying students in English-taught programmes; exact fees vary by programme and should be confirmed on the university’s official tuition pages</small>'),
              ('Early Bird offer','€2,000 first-year reduction <small>Accept your study place and pay the reduced first-year tuition fee within 21 days of receiving admission information to claim it</small>'),
              ('Graduation scholarship','€2,000 master’s reduction <small>Students who complete a Tampere University bachelor’s degree within three academic years can claim a €2,000 reduction on the first-year tuition of a master’s programme at the university</small>'),
              ('Who it is for','Non-EU/EEA/Switzerland applicants <small>International students from outside the EU, EEA and Switzerland who are subject to tuition fees and applying to an English-taught bachelor’s or master’s programme at Tampere University</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>Tampere University</strong> (TAU) is Finland’s second-largest multidisciplinary university, with campuses in Tampere at the city centre, Hervanta and Kauppi. For fee-paying international students in its English-taught degree programmes, the university offers <strong>tuition fee scholarships covering 50% of tuition</strong> — awarded at admission to a limited number of exceptionally qualified applicants.</p>
<p>There is <strong>no separate scholarship application</strong>: you are considered automatically when you apply for admission during the application window. But read this plainly — this is <strong>partial funding only</strong>. The scholarship covers half the tuition for the degree; living costs (estimated around €800/month by independent trackers) and all other expenses are yours to fund.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>50% tuition fee scholarship</strong> for the normative duration of the degree — three academic years for a bachelor’s, two for a master’s — for the small number of fee-paying applicants the university selects.</li>
<li><strong>Early Bird offer:</strong> a <strong>€2,000 reduction</strong> on the first-year tuition fee — claim it by accepting your study place and paying the reduced first-year tuition within 21 days of receiving admission information.</li>
<li><strong>Graduation scholarship:</strong> students who complete a Tampere University bachelor’s degree within three academic years are eligible for a <strong>€2,000 reduction</strong> on first-year master’s tuition at Tampere.</li>
<li><strong>What it does not cover:</strong> accommodation, living expenses, travel, or insurance — plan to self-fund these, as the scholarship is tuition-only.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Fee status:</strong> you must be a non-EU/EEA/Switzerland national subject to tuition fees.</li>
<li><strong>Programme:</strong> applying to an English-taught bachelor’s or master’s programme at Tampere University.</li>
<li><strong>Merit:</strong> awarded to exceptionally qualified applicants at the university’s discretion — the bar is high and the number of awards very small.</li>
<li><strong>Doctoral applicants:</strong> this admission-linked scheme is for bachelor’s and master’s programmes; it is not a general fully funded PhD scholarship route.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Apply through the national <strong>Studyinfo.fi</strong> portal during the application period and upload all required attachments by the attachment deadline:</p>
<ul>
<li>Educational certificates and transcripts (with grading-scale explanations where relevant).</li>
<li>Proof of English proficiency (programme-specific requirements apply).</li>
<li>Programme-specific documents — portfolios, work experience evidence, or other items where required.</li>
<li>Passport or national ID.</li>
<li>Pay the <strong>€100 application fee</strong> by the deadline given in the Studyinfo.fi email — an unpaid application is deactivated. (Master’s 2027 round; check the portal for bachelor’s-round fee rules.)</li>
<li>You may apply to <strong>up to two programmes</strong> at a time.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Check eligibility</strong> — fee status, programme fit, and English-language requirements.</li>
<li><strong>Prepare documents early</strong> — the attachment deadline falls just a week after the master’s application window closes.</li>
<li><strong>Submit on Studyinfo.fi</strong> during the application period (master’s: 14 Dec 2026–7 Jan 2027; bachelor’s: 7–21 Jan 2027) and pay the application fee.</li>
<li><strong>Upload all attachments by 14 January 2027</strong> (master’s round) — missing documents lead to rejection.</li>
<li><strong>Await admission results (23 March 2027)</strong> — scholarship decisions come with the admission offer.</li>
<li><strong>If awarded:</strong> accept your study place by <strong>31 May 2027</strong> to take advantage of the scholarship, and consider the Early Bird (€2,000 off) by acting within 21 days of the admission information.</li>
</ol>
<p>Official 2027 timeline (master’s): application 14 Dec 2026 → attachments 14 Jan 2027 → results 23 Mar 2027 → accept place for scholarship 31 May 2027 → tuition fee payment 31 Jul 2027 → studies start autumn 2027.</p>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is the Tampere scholarship fully funded?','No. It is a 50% tuition-fee scholarship — tuition only, no stipend, no travel or living-cost support. Budget accommodation, food and insurance yourself.'),
 ('How many scholarships are awarded?','A very limited number at the university’s discretion. In the 2026 admission round, nine tuition-fee scholarships were awarded across all bachelor’s and master’s programmes (per an independent tracker).'),
 ('Is there a separate scholarship application?','No. Fee-paying applicants are considered automatically when they apply for admission — but the application itself must be complete and submitted within the window.'),
 ('What does the Early Bird offer do?','It cuts €2,000 off the first-year tuition fee if you accept your study place and pay the reduced fee within 21 days of receiving admission information.'),
 ('Can I apply to more than one programme?','Yes — you may apply to up to two programmes at the same time in the master’s round.'),
 ('Does the scholarship cover a PhD?','No. This scheme covers English-taught bachelor’s and master’s programmes; doctoral funding runs through separate routes.'),
 ('When do I pay tuition if admitted?','Per the official 2027 timeline, the full tuition fee is due by 31 July 2027 (with the Early Bird reduction applied if claimed within 21 days of the admission information).'),
]),
 verify='Verified 19 Oct 2026 on Tampere University’s official 2027 admissions pages (tuni.fi): the master’s application window 14 December 2026–7 January 2027 (08:00/23:59 UTC+2), the €100 application fee rule, the 14 January 2027 attachment deadline, the 23 March 2027 results date, and the 31 May / 13 July / 31 July 2027 acceptance and tuition dates. The 7–21 January 2027 bachelor’s joint-application window, the 50% tuition-fee scholarship terms, the €10,000/€12,000 annual tuition figures, the €2,000 Early Bird reduction and the €2,000 graduation scholarship are consistent across three independent trackers and are used with that framing. The award is explicitly tuition-only and is presented here as partial funding, not fully funded.',
 offlinks=[('Applying to Tampere Master’s programmes — official 2027 timeline','https://www.tuni.fi/en/tau/masters-programmes/applying'),
           ('Tampere Master’s programmes (official)','https://www.tuni.fi/en/tau/masters-programmes')],
 related_titles=['aalto','daad','fulbright-dk'],
))

# ---------------------------------------------------------------- 3. KUAS
ARTICLES.append(dict(
 slug='kyoto-university-of-advanced-science-scholarships-2027-japan',
 title='Kyoto University of Advanced Science Scholarships 2027 in Japan (Funded) | StudyDesk Scholarships',
 meta='KUAS Scholarships 2027: Super KUAS-E covers 100% tuition + admission fee + a ¥1,200,000/year stipend; KUAS-E offers 100/50/20% reductions. International students apply 1 Oct 2026–26 Feb 2027 for September 2027 entry.',
 short='KUAS Scholarships 2027',
 kicker='Japan · University',
 mono='KU', prov_short='Kyoto University of Advanced Science', prov_cat='Private University · Japan',
 h1='Kyoto University of Advanced Science Scholarships 2027 in Japan (Funded)',
 sub='Kyoto’s English-taught engineering university puts serious money behind international students. Kyoto University of Advanced Science (KUAS) offers two scholarship tiers for 2027 entrants: the <strong>Super KUAS-E Scholarship</strong> — full tuition, full admission fee, plus a <strong>¥1,200,000-per-year stipend</strong> — and the <strong>KUAS-E Scholarship</strong> with 100%, 50% or 20% tuition and admission-fee reductions. Applications for September 2027 entry run 1 October 2026 to 26 February 2027.',
 dpill='26 Feb 2027 · 130 days to go', dl_long='1 October 2026 – 26 February 2027 (must arrive by this date) for September 2027 entry to the English-track programmes, per Japan Student Services Organization data. Applications go through the TAO online portal.',
 facts=facts([('Super KUAS-E','Fully funded <small>100% tuition fee + 100% admission fee + a stipend for personal expenses worth ¥1,200,000 per year. Awarded to academically excellent international students; express your intent on the TAO application</small>'),
              ('KUAS-E Scholarship','Full or partial reduction <small>100%, 50% or 20% tuition reduction plus a matching 100%, 50% or 20% admission-fee reduction, depending on category and level (bachelor’s and master’s)</small>'),
              ('2027 costs','¥1,022,500/year tuition (engineering) <small>Published projected amounts for September 2027 entrants: ¥1,022,500 annual tuition + ¥200,000 admission fee + ¥49,500 other expenses, subject to change. The scholarship is awarded together with — or shortly after — the admission offer, so you know your funding before enrolment</small>'),
              ('Who it is for','All international applicants <small>Any international student applying to KUAS’ international (English-taught) programmes can apply for both scholarship tiers; eligibility is academic-excellence based</small>'),
              ('How it works','Indicate intent on TAO <small>A separate scholarship step in addition to the university admission: express your intent to receive the scholarship on the TAO application, following the university’s published procedure</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>Kyoto University of Advanced Science (KUAS)</strong> is a private university in Kyoto offering engineering programmes taught <strong>entirely in English</strong> — undergraduate and postgraduate — in a city famous as a college town. For international students, KUAS runs two scholarship tiers, and both can be applied for during the admission application itself.</p>
<p>The flagship <strong>Super KUAS-E Scholarship</strong> is the genuinely fully funded option: full tuition, full admission fee, and a yearly living stipend. The <strong>KUAS-E Scholarship</strong> covers the remaining ground with tiered reductions of 100%, 50% or 20% on tuition and admission fees.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>Super KUAS-E Scholarship:</strong> <strong>100% of tuition fees</strong> + <strong>100% of the admission fee</strong> + a <strong>stipend for personal expenses worth ¥1,200,000 per year</strong> (about ¥100,000 per month).</li>
<li><strong>KUAS-E Scholarship:</strong> <strong>tuition reduction of 100%, 50% or 20%</strong> with a matching <strong>admission-fee reduction of 100%, 50% or 20%</strong>, by category — available to bachelor’s and master’s students.</li>
<li><strong>Funding arrives with the admission decision:</strong> scholarship results are announced together with the admission offer (or a few weeks after), so you can plan your finances before you enrol.</li>
<li><strong>Published 2027 costs for reference:</strong> engineering programmes — annual tuition <strong>¥1,022,500</strong>, admission fee <strong>¥200,000</strong>, other expenses ¥49,500 (the university’s projected amounts for September 2027 entrants, subject to change).</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Nationality:</strong> all international applicants — the scholarships are open to every international student applying to KUAS’ international programmes.</li>
<li><strong>Level:</strong> bachelor’s and master’s students (Super KUAS-E; the KUAS-E reduction tiers also span both levels).</li>
<li><strong>Academic standing:</strong> awarded on <strong>academic excellence</strong> — the single stated criterion.</li>
<li><strong>Track:</strong> applicants to the university’s English-taught international programmes (notably engineering).</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Applications go through the <strong>TAO (The Admissions Office) online portal</strong>. Prepare the standard international-admissions pack:</p>
<ul>
<li>Academic transcripts and graduation certificates.</li>
<li>Passport copy and other identification documents.</li>
<li>English proficiency evidence (programmes are English-taught).</li>
<li>Any programme-specific documents listed in the entrance examination guidelines.</li>
<li><strong>Application fee: ¥5,000</strong> for the English-based admission track (2027 school year, per JASSO data).</li>
<li><strong>Scholarship step:</strong> express your intent to receive the Super KUAS-E and/or KUAS-E Scholarship on the TAO application, per the university’s published procedure.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Read the entrance examination guidelines</strong> for the 2027 English-track admission on the official KUAS admissions pages.</li>
<li><strong>Prepare your documents</strong> — transcripts, certificates, ID, and proof of English proficiency.</li>
<li><strong>Submit your application on the TAO portal</strong> between <strong>1 October 2026 and 26 February 2027</strong> (documents must arrive by the deadline).</li>
<li><strong>Indicate your scholarship intent</strong> on the TAO application for the Super KUAS-E and/or KUAS-E Scholarship.</li>
<li><strong>Await the combined result</strong> — admission and scholarship notifications arrive together (or a few weeks apart).</li>
</ol>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is the Super KUAS-E Scholarship really fully funded?','Yes — it covers 100% of tuition, 100% of the admission fee, and adds a ¥1,200,000-per-year stipend for personal expenses. It is the top tier for academically excellent international students.'),
 ('What does the KUAS-E Scholarship cover?','A tuition reduction of 100%, 50% or 20% plus a matching admission-fee reduction (100%, 50% or 20%), depending on your category — for bachelor’s and master’s students.'),
 ('Do I apply for admission and the scholarship separately?','A separate scholarship step exists in addition to the university admission — you express your intent to receive the scholarship on the TAO application and follow the university’s published procedure.'),
 ('When will I know about funding?','Scholarship results come with your admission offer, or a few weeks after, so your funding plan is settled before enrolment.'),
 ('What does it cost without a scholarship?','The university’s projected 2027 figures for engineering entrants: ¥1,022,500 annual tuition, ¥200,000 admission fee, and ¥49,500 in other expenses — subject to change.'),
 ('Can international students really study in English at KUAS?','Yes — the engineering programmes for international students are taught entirely in English, and the university’s International Admissions Office supports applications from outside Japan.'),
]),
 verify='Verified 19 Oct 2026 via Japan Student Services Organization (JASSO) JPSS data for Kyoto University of Advanced Science: the 1 October 2026–26 February 2027 application window for September 2027 entry, the Super KUAS-E terms (100% tuition + 100% admission fee + ¥1,200,000/year stipend), the KUAS-E reduction tiers (100/50/20%), the ¥5,000 English-track application fee, and the published 2027 fee figures — corroborated by three independent scholarship trackers. The fee figures are the university’s published projected amounts for September 2027 entrants, subject to change, and are stated as such here. The official KUAS scholarship page URL is given as the primary source.',
 offlinks=[('KUAS — official scholarship page','https://www.kuas.ac.jp/en/admission/scholarship/'),
           ('KUAS on JPSS (JASSO) — engineering','http://www.jpss.jp/en/univ/480/4301/')],
 related_titles=['honjo','iuj','science-tokyo'],
))

# ---------------------------------------------------------------- 4. NIMS
ARTICLES.append(dict(
 slug='nims-internship-program-japan',
 title='NIMS Internship Program in Japan (Fully Funded) | StudyDesk Scholarships',
 meta='NIMS Internship Program Japan: hands-on materials-science research internships of up to 90 days for current undergraduate and graduate students worldwide. The 2026 round is closed; the next application round opens December 2026.',
 short='NIMS Internship Program',
 kicker='Japan · Research Internship',
 mono='NI', prov_short='National Institute for Materials Science', prov_cat='National Research Institute · Japan',
 h1='NIMS Internship Program in Japan (Fully Funded)',
 sub='<strong>Prepare now — the 2026 round is closed and the next round opens in December 2026.</strong> The National Institute for Materials Science (NIMS) in Tsukuba, Japan, takes about <strong>100 students a year</strong> from universities around the world for hands-on research internships of up to <strong>90 days</strong> in cutting-edge materials science. Selected interns receive a <strong>daily allowance plus accommodation</strong> while working directly with NIMS researchers.',
 dpill='Opens Dec 2026', dl_long='The 2026 round is closed (per the official NIMS internship page, updated 3 February 2026). The next application round is scheduled to open in December 2026. Internships for the coming round must be completed by the end of March 2027.',
 facts=facts([('Support','Daily allowance + accommodation <small>For selected students: a daily allowance and accommodation fees (excluding utilities). NIMS explicitly notes this does not guarantee acceptance of all applicants’ internship or financial support</small>'),
              ('Who it is for','Current students only <small>Only students currently enrolled as undergraduates or graduates at domestic or international universities — in materials science and related technical fields. NIMS is widely open to the world, with researchers and students from many countries</small>'),
              ('Duration','Up to 90 consecutive days <small>Internships run up to 90 consecutive calendar days and must be completed by the end of March 2027. Longer requests are possible only by arrangement with the host researcher</small>'),
              ('Scale','~100 interns a year <small>NIMS accepts about one hundred students from around the world every year — a selective, well-networked programme</small>'),
              ('What is honest here','Airfare not stated by NIMS <small>The official NIMS page lists the daily allowance and accommodation only. Some aggregator pages claim round-trip airfare is covered — NIMS itself does not say this, so budget travel yourself unless the December 2026 call states otherwise</small>')]),
 body='''<h2 id="about">About the internship</h2>
<p>The <strong>National Institute for Materials Science (NIMS)</strong>, based in Tsukuba, Japan, runs a long-standing internship programme that gives <strong>undergraduate and graduate students</strong> practical, hands-on experience of cutting-edge research in materials science. Interns work directly with NIMS researchers on real projects — not classroom exercises — and the programme also feeds into the institute’s Joint Graduate School Program visibility.</p>
<p>About <strong>100 students a year</strong> from universities around the world take part, and the institute is known for its strongly international research community. If you are studying science, engineering, physics, chemistry, materials science, nanotechnology or a related technical field, this is one of the most respected research internships in Asia.</p>
<p><strong>Timing status (read this first):</strong> the <strong>2026 round is closed</strong>. The next application round is scheduled to <strong>open in December 2026</strong>. Use the waiting time to identify the researcher you want to work with and prepare your materials — applications move fast once the round opens.</p>
<h2 id="benefits">What the funding covers</h2>
<p>Straight from the official NIMS internship page — this is what is published, and only this:</p>
<ul>
<li><strong>Daily allowance</strong> for selected students.</li>
<li><strong>Accommodation fees</strong> (excluding utilities) for selected students.</li>
<li><strong>No internship or financial support is guaranteed</strong> — NIMS states explicitly that the programme does not guarantee acceptance of all applicants’ internship requests or financial support.</li>
<li><strong>Not published by NIMS:</strong> round-trip airfare. Several aggregator sites claim flights are covered; NIMS’ own page does not say this. <strong>Budget your own travel</strong> unless the December 2026 call explicitly adds it.</li>
<li>If you hold a Japanese government-funded scholarship (MEXT, JSPS, JST), check with your scholarship provider about eligibility before applying.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Only current undergraduate and graduate students</strong> at domestic or international universities — graduates and non-students are not eligible.</li>
<li><strong>Fields:</strong> materials science and related technical areas — science, engineering, physics, chemistry, nanotechnology and adjacent disciplines.</li>
<li><strong>Nationality:</strong> the programme is open to the world; NIMS hosts many international researchers and students.</li>
<li>You will be attached to a <strong>specific researcher and project</strong> — your application should align with ongoing NIMS research.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>The exact document list will be published with the December 2026 call. Based on the programme’s established pattern, prepare:</p>
<ul>
<li>An updated <strong>CV/resume</strong>.</li>
<li><strong>Academic transcripts</strong>.</li>
<li>A clear <strong>research-interest statement</strong> naming the NIMS researcher and group you want to join.</li>
<li>Proof of current <strong>enrolment</strong> at your university.</li>
<li>Identification documents (passport).</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>From now until December:</strong> study the NIMS research groups, identify 2–3 researchers whose work matches yours, and read their recent publications.</li>
<li><strong>Prepare your pack</strong> — CV, transcripts, enrolment proof, and a focused research-interest statement.</li>
<li><strong>When the round opens (December 2026):</strong> apply through the official NIMS internship page promptly.</li>
<li><strong>Plan a window of up to 90 consecutive days</strong> that finishes by the end of March 2027.</li>
<li><strong>If you hold MEXT/JSPS/JST funding:</strong> confirm with your scholarship provider that you may take part.</li>
</ol>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is the NIMS internship fully funded?','Selected interns receive a daily allowance and accommodation fees (excluding utilities). NIMS does not publish airfare coverage — do not count on flights being paid unless the new call says so.'),
 ('Who can apply?','Only students currently enrolled as undergraduates or graduates, from domestic or international universities, in materials science or related technical fields.'),
 ('When do applications open?','The 2026 round is closed. Per the official NIMS page, the next application round is scheduled to open in December 2026.'),
 ('How long is the internship?','Up to 90 consecutive calendar days, and it must be completed by the end of March 2027.'),
 ('Do I need to know Japanese?','The programme’s working context is research under NIMS scientists; English is the working language of the international research community there. No Japanese test is published as a requirement.'),
 ('Is acceptance guaranteed?','No. NIMS states the programme does not guarantee acceptance of all applicants’ internship or financial-support requests — selection applies.'),
 ('Can I extend beyond 90 days?','Only by arrangement: the official page says internship requests exceeding 90 days should be discussed with the researcher you wish to apply to.'),
]),
 verify='Verified 19 Oct 2026 on the official NIMS internship page (nims.go.jp, updated 3 February 2026): the 2026 round is closed, the next round opens December 2026, eligibility is restricted to current undergraduate and graduate students, the published financial support is a daily allowance plus accommodation fees excluding utilities, the programme accepts about 100 students a year, internships run up to 90 consecutive days and must be completed by the end of March 2027, and acceptance/financial support is not guaranteed. Aggregator claims of covered round-trip airfare are not from NIMS and are explicitly not repeated here.',
 offlinks=[('NIMS Internship Program — official page','https://www.nims.go.jp/eng/hr-development/internship.html')],
 related_titles=['kaust-vsrp','epfl-summer','stowers2027'],
))

# ---------------------------------------------------------------- 5. Waikato
ARTICLES.append(dict(
 slug='university-of-waikato-vice-chancellors-international-excellence-scholarship-2027',
 title='University of Waikato Vice-Chancellor’s International Excellence Scholarship 2027 (Funded) | StudyDesk Scholarships',
 meta='University of Waikato Vice-Chancellor’s International Excellence Scholarship 2027: up to NZD 15,000 tuition credit for first-time international students. Rolling monthly review — 30 Nov 2026 for Trimester A 2027 offers of place.',
 short='Waikato Vice-Chancellor’s International Excellence Scholarship 2027',
 kicker='New Zealand · University',
 mono='WA', prov_short='University of Waikato', prov_cat='Public University · New Zealand',
 h1='University of Waikato Vice-Chancellor’s International Excellence Scholarship 2027 (Funded)',
 sub='New Zealand’s University of Waikato rewards talented first-time international students with a <strong>tuition credit of up to NZD 15,000</strong> for undergraduates and <strong>up to NZD 10,000</strong> for postgraduates. The Vice-Chancellor’s International Excellence Scholarship is reviewed <strong>monthly on a rolling basis</strong> — with the next consideration date <strong>30 November 2026</strong> for Trimester A 2027 offers of place.',
 dpill='30 Nov 2026 · 42 days to go', dl_long='Reviewed monthly on a rolling basis — the university notes the closing dates do not apply as hard deadlines, but applications must be received by 30 November 2026 (A Trimester 2027 offers), 31 May 2027 (B Trimester), 31 August 2027 (C Trimester), or 31 October 2027 (H/X Trimester).',
 facts=facts([('Award','Up to NZD 15,000 (UG) / NZD 10,000 (PG) <small>Tuition-fee credit in NZD for the first year of full-time study, awarded to applicants who demonstrate excellent academic achievement. Successful applicants may also be called on as global ambassadors for the university</small>'),
              ('Who it is for','New international students <small>Applying to enrol full-time in an undergraduate or taught postgraduate programme as a new international student to the University of Waikato — with a conditional or unconditional offer of place and a minimum B+ GPA equivalency in the entrance qualification</small>'),
              ('Study level','UG + taught PG <small>All subject areas: Arts, Business & Management, Computer Science, Mathematics, Education, Health, Engineering, Law, Māori & Indigenous Studies, Science, Social Sciences. Face-to-face study — online students are not eligible</small>'),
              ('How to apply','Apply to enrol first <small>You must complete an application to enrol BEFORE you can access the scholarship application; then apply via the Scholarships tab in MyWaikato. Read the official regulations first</small>'),
              ('Not eligible','Several exclusions <small>Currently enrolled students; anyone who has paid fees or applied for a visa at application time; arrivals via sponsoring bodies, Guaranteed Credit Arrangements, or study-abroad/exchange agreements; limited-place programmes (e.g. Master of Nursing Practice, Master of Pharmacy Practice) and postgraduate teaching programmes (e.g. Master of Teaching and Learning)</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The <strong>Vice-Chancellor’s International Excellence Scholarship</strong> — known before 2023 as the University of Waikato International Excellence Scholarship — was established in <strong>2015</strong> to promote educational opportunities and support talented international applicants enrolling as new students at the <strong>University of Waikato</strong> in Hamilton and Tauranga, New Zealand.</p>
<p>Unlike many scholarships with a single annual deadline, this one is <strong>reviewed monthly on a rolling basis</strong>. The university explicitly notes the published trimester dates are consideration dates rather than hard closing dates — but you must still have your application in by the date tied to your trimester’s offer of place, and applying early improves your chances.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>Up to NZD 15,000</strong> as a tuition-fee credit for <strong>undergraduate</strong> study.</li>
<li><strong>Up to NZD 10,000</strong> as a tuition-fee credit for <strong>postgraduate (taught)</strong> study.</li>
<li>The credit applies to your <strong>first year of full-time study</strong>; it is paid in NZD against tuition fees — <strong>not a cash stipend</strong>, and it does not cover living costs, travel or accommodation.</li>
<li>Recipients may be called upon to serve as <strong>global ambassadors</strong> for the University of Waikato.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<p>Per the university’s published regulations, applicants must meet <strong>all</strong> of the following:</p>
<ul>
<li><strong>New international student</strong> applying to enrol <strong>full-time</strong> in an undergraduate or postgraduate (taught) programme at the University of Waikato.</li>
<li>Hold a <strong>conditional or unconditional offer of place</strong> from the university.</li>
<li>Have a <strong>minimum GPA equivalency of B+</strong> in the qualification used to gain entrance.</li>
<li>Not be eligible for one of the country/region-specific Vice-Chancellor’s International Excellence Scholarships (if your region has its own version, apply to that one).</li>
</ul>
<p>You are <strong>ineligible</strong> if you: are currently enrolled at the university or its college; have already paid fees or applied for a visa; are coming via a sponsoring body, a Guaranteed Credit Arrangement, or a study-abroad/exchange agreement; or intend to enrol in a limited-places programme (e.g. Master of Nursing Practice, Master of Pharmacy Practice) or a postgraduate teaching programme (e.g. Master of Teaching and Learning). <strong>Online-only students are not eligible</strong> — study must be face-to-face.</p>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>Academic <strong>transcripts</strong> and qualification certificates (for the B+ equivalency assessment).</li>
<li>Your <strong>offer of place</strong> from the University of Waikato.</li>
<li>Proof of <strong>English proficiency</strong> (as required for admission).</li>
<li>Passport/ID.</li>
<li>The university’s <strong>scholarship regulations</strong> — read them in full before applying.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply to enrol</strong> at the University of Waikato first — you cannot access the scholarship application until you have an account. (This is not a commitment to study; it can be withdrawn.)</li>
<li><strong>Log in to MyWaikato</strong> and open the <strong>‘Scholarships’</strong> tab to find the Vice-Chancellor’s International Excellence Scholarship.</li>
<li><strong>Complete and submit</strong> the scholarship application with your documents.</li>
<li><strong>Meet the consideration date</strong> for your trimester’s offer of place: <strong>30 November 2026</strong> (A Trimester 2027) → <strong>31 May 2027</strong> (B) → <strong>31 August 2027</strong> (C) → <strong>31 October 2027</strong> (H/X).</li>
<li><strong>Await the monthly review</strong> — decisions are made on a rolling basis.</li>
</ol>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is this scholarship fully funded?','No. It is a tuition-fee credit only — up to NZD 15,000 for undergraduates or NZD 10,000 for postgraduates, applied in the first year. Living costs, travel and accommodation are not covered.'),
 ('When is the deadline?','There is no single hard deadline; applications are reviewed monthly. But you must apply by the consideration date for your trimester’s offer of place — 30 November 2026 for Trimester A 2027, 31 May 2027 for B, 31 August 2027 for C, and 31 October 2027 for H/X.'),
 ('Do I need an admission offer before applying?','Yes — you must hold a conditional or unconditional offer of place from the University of Waikato, and you must apply to enrol before you can even access the scholarship application.'),
 ('What GPA do I need?','A minimum GPA equivalency of B+ in the qualification used for admission.'),
 ('Can I apply if I already study at Waikato?','No — the scholarship is for students enrolling for the first time. Currently enrolled students are explicitly ineligible.'),
 ('Can online students apply?','No. The scholarship requires face-to-face study in New Zealand.'),
 ('Is it available for all subjects?','Yes — all areas of study: Arts, Business & Management, Computer Science, Mathematics, Education, Health, Engineering, Law, Māori & Indigenous Studies, Science and Social Sciences.'),
 ('How much is New Zealand tuition without it?','Independent trackers put international tuition at roughly NZD 30,000–40,000 per year — the credit offsets a meaningful share of year one. Confirm current fees on the university’s pages.'),
]),
 verify='Verified 19 Oct 2026 on the University of Waikato’s official scholarship page (waikato.ac.nz): rolling monthly review, the four trimester consideration dates (30 Nov 2026 for A Trimester 2027 offers; 31 May / 31 Aug / 31 Oct 2027 for B/C/H-X), the up-to-NZD-15,000 value, the enrol-before-applying rule and the MyWaikato application route. The NZD 15,000-undergraduate / NZD 10,000-postgraduate split, the B+ GPA equivalency, the offer-of-place requirement, the face-to-face requirement and the full exclusion list are from the university’s published 2026 scholarship regulations (the current published regulations document) — flagged as such. Aggregator claims of a fixed single deadline are not from the university and are not repeated.',
 offlinks=[('Vice-Chancellor’s International Excellence Scholarship — official page','https://www.waikato.ac.nz/study/scholarships/find-a-scholarship/vice-chancellors-international-excellence-scholarship/'),
           ('Scholarship regulations 2026 (PDF, official)','https://www.waikato.ac.nz/assets/Uploads/Study-with-us/Scholarships/Find-a-Scholarship/VCIES-2026-all-other-countries-v2.pdf')],
 related_titles=['auckland','adelaide2027','melbourne2027'],
))

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# validate
import html.parser
class P(html.parser.HTMLParser):
    def error(self, m): raise Exception(m)
for slug, _ in built:
    src = OUT.joinpath(slug + '.html').read_text()
    P().feed(src)
    for bad in ['AICTE Pragati', 'Lorem', '#']:
        assert bad not in src, (slug, bad)
    print('validated', slug)

#!/usr/bin/env python3
"""Batch 20 (cron run 20, 18 Oct 2026): first 3 of 5 verified articles.

Written (queue order):
1. Adelaide University Research Scholarships 2027 (Australia) — re-scoped from the
   stale queue title "University of South Australia Research Scholarships 2026".
   UniSA no longer exists under that name: it merged with the University of
   Adelaide to form Adelaide University (2026). Research scholarships are now
   the university-funded AURS and the government-funded RTPS. GRTS Round 1 is
   OPEN now for 2027 commencements (no exact close published); Round 2 mid-Feb
   to late Mar 2027; Round 3 mid-Jul to mid-Aug 2027; CSC-Adelaide partnership
   1 Oct 2026 - 1 Feb 2027. Stipend A$36,500/yr (2026 rate, indexed), 100%
   tuition waiver, OSHC + relocation allowances confirmed but figures unconfirmed.
2. Unilever Internships 2027 — honest guide. No single global programme with one
   deadline exists (aggregator "Submit Applications" framing rejected); roles are
   posted per country on careers.unilever.com and reviewed on a rolling basis.
   Summer 2026 roles closed. Currently open: Singapore ULIP Jan-Jun 2027 and UK
   & Ireland Industrial Placements 2027. Eligibility = enrolled students only,
   fresh graduates explicitly ineligible. Pay not published on official postings.
3. Stowers Summer Scholars Program 2027 (USA) — official pages confirm: open now,
   deadline 11:59 pm ET 17 Jan 2027, rolling within window; $5,000 salary +
   round-trip travel + accommodation; 8 weeks 7 Jun-30 Jul 2027; one year of UG
   completed, 18+, life/physical sciences + computing/engineering/maths, domestic
   + international; apply via GradCAS portal; two recommendation letters.
4-5. (added after deep-dive wave — GEM + DENSYS 2027, see build-batch20b.py)
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'adelaide2027': dict(mono='AU', title='Adelaide University Research Scholarships 2027 in Australia (Fully Funded)', href='adelaide-university-research-scholarships-2027-australia.html',
              dpill='Round 1 open now', award='A$36,500/yr stipend + 100% tuition waiver (PhD up to 3.5 yrs)', elig='PhD/MPhil applicants, domestic + international; all disciplines; merit-based.',
              tags=[('PhD', 'blue'), ('Australia', 'teal')]),
 'unilever2027': dict(mono='U', title='Unilever Internships 2027 — How to Apply (Rolling, Country-Wise)', href='unilever-internships-2027-guide.html',
              dpill='Rolling admissions', award='Paid roles (per market; figures not published on official postings)', elig='Enrolled bachelor’s/master’s students; fresh graduates ineligible; per-listing regions.',
              tags=[('Internship', 'blue'), ('Global', 'teal')]),
 'stowers2027': dict(mono='S', title='Stowers Summer Scholars Program 2027 in USA (Fully Funded)', href='stowers-summer-scholars-program-2027-usa.html',
              dpill='17 Jan 2027 · 91 days to go', award='$5,000 salary + round-trip travel + accommodation (8 weeks)', elig='Completed 1 year of UG; 18+; life/physical sciences, computing, engineering, maths; domestic + international.',
              tags=[('Research internship', 'blue'), ('USA', 'teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 1. Adelaide
ARTICLES.append(dict(
 slug='adelaide-university-research-scholarships-2027-australia',
 title='Adelaide University Research Scholarships 2027 in Australia (Fully Funded) | StudyDesk Scholarships',
 meta='Adelaide University Research Scholarships 2027: A$36,500/yr stipend, 100% tuition fee waiver, OSHC and relocation support for PhD and MPhil students. GRTS Round 1 open now; Round 2 mid-Feb–late Mar 2027; Round 3 mid-Jul–mid-Aug 2027; CSC partnership closes 1 Feb 2027.',
 short='Adelaide University Research Scholarships 2027',
 kicker='Australia · Research Scholarships',
 mono='AU', prov_short='Adelaide University', prov_cat='University · Australia',
 h1='Adelaide University Research Scholarships 2027 in Australia (Fully Funded)',
 sub='Australia\u2019s newest university is funding its research future. Adelaide University — formed in 2026 by the merger of the University of Adelaide and the University of South Australia — runs its research scholarships as the university-funded Adelaide University Research Scholarship (AURS) and the Australian Government\u2019s Research Training Program Scholarship (RTPS): a stipend of A$36,500 a year, a full tuition fee waiver, and OSHC and relocation support. The Graduate Research Talent Scheme\u2019s first 2027 round is open now.',
 dpill='Round 1 open now', dl_long='Graduate Research Talent Scheme Round 1 is open now for 2027 commencements (the official page publishes no exact closing date — check before applying). Round 2 runs mid-February to late March 2027; Round 3 runs mid-July to mid-August 2027. The CSC\u2013Adelaide University Partnership (PhD, Chinese nationals) is open 1 October 2026 to 1 February 2027.',
 facts=facts([('Award','A$36,500 per year stipend <small>2026 full-time rate, indexed annually; up to 3.5 years for a PhD, 2 years for an MPhil. Higher rate for Aboriginal and Torres Strait Islander scholars (exact figure not published)</small>'),
              ('Tuition','100% fee waiver <small>For the duration of the award — up to 4 years for a PhD, 2 years for an MPhil, 1.5 years for an MRes. OSHC and a relocation allowance are also included, though the official page publishes no fixed figures for them</small>'),
              ('Who it is for','PhD and MPhil applicants <small>Domestic and international students across every discipline; awarded competitively on academic merit, research experience and strategic alignment</small>'),
              ('Key rounds','GRTS Rounds 1–3 <small>Round 1 open now for 2027 starts (domestic + international applicants holding an Australian/New Zealand qualification). Out-of-round awards run year-round</small>'),
              ('CSC partnership','1 Oct 2026 – 1 Feb 2027 <small>China Scholarship Council partnership for Chinese nationals doing a PhD; must hold an unconditional admission offer by the closing date</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>A naming warning first, because stale tracker pages will confuse you: <strong>there is no longer a \u201cUniversity of South Australia research scholarship\u201d</strong> under that name. The University of South Australia and the University of Adelaide merged in 2026 to form <strong>Adelaide University</strong>, and the research scholarships moved with it. What trackers still list as \u201cUniSA RTPi\u201d or \u201cUPS\u201d are the old labels — the current awards are the <strong>Adelaide University Research Scholarship (AURS, university-funded)</strong> and the <strong>Research Training Program Scholarship (RTPS, Australian Government\u2013funded)</strong>. Apply for research admission and you are automatically considered for the scholarship rounds; there is no separate scholarship form.</p>
<p>The headline package is genuinely strong: a living stipend, a complete tuition fee waiver, and additional allowances for overseas health cover and relocation. The catch is competition — these are merit-based awards, and each round also weighs your research experience and, for some awards, how your project fits the university\u2019s strategic research goals.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>Stipend:</strong> <strong>A$36,500 per annum</strong> (the 2026 full-time rate, indexed annually), for up to 3.5 years on a PhD and up to 2 years on an MPhil. The official listing values the package at about A$127,750 in total over a PhD. Aboriginal and Torres Strait Islander scholars receive a higher stipend rate — the exact figure is not published on the official page.</li>
<li><strong>Tuition:</strong> a <strong>100% tuition fee waiver</strong> for the duration of the award (up to 4 years for a PhD, 2 years for an MPhil, 1.5 years for an MRes).</li>
<li><strong>Health cover:</strong> the official page confirms additional allowances covering <strong>Overseas Student Health Cover</strong> for international scholars where applicable. The detail of single-versus-family policies is not published on official channels — treat tracker specifics with scepticism.</li>
<li><strong>Relocation:</strong> a relocation allowance is confirmed on the official page, but no official figure is published. Trackers quote figures between A$1,000 and A$2,000; those are unconfirmed.</li>
</ul>
<p>Ignore outdated tracker figures such as A$32,500 or A$35,200 — those belong to the pre-merger years. A$36,500 is the confirmed 2026 rate.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Study level:</strong> PhD and MPhil (research) across every discipline.</li>
<li><strong>Nationality:</strong> open to <strong>domestic and international</strong> applicants.</li>
<li><strong>Merit:</strong> awards are competitive — academic record, research experience, and (for some awards) alignment with the university\u2019s strategic research goals decide.</li>
<li><strong>GRTS Round 1 restriction — important:</strong> Round 1 of the Graduate Research Talent Scheme is open only to <strong>domestic applicants, plus international applicants who have completed a relevant Australian or New Zealand qualification</strong>. International applicants without an Australian or New Zealand qualification cannot use this round — wait for a later round.</li>
<li><strong>CSC partnership:</strong> Chinese nationals applying for a PhD must meet PhD entry and English requirements by the closing date and hold an <strong>unconditional offer of admission</strong>.</li>
<li><strong>Out-of-round awards:</strong> Aboriginal and Torres Strait Islander PhD/MPhil candidates are assessed at any time, alongside top-up, internship, travel and externally funded awards.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>The official scholarships page does not publish a single fixed document checklist — so treat aggregator checklists as guidance, not gospel. Across the official page and independent sources, a complete application typically includes:</p>
<ul>
<li>Your research degree application through the university\u2019s official portal (this is the scholarship application — there is no separate form).</li>
<li>Official academic transcripts, including the grading scheme.</li>
<li>Evidence of English-language proficiency meeting the university\u2019s requirement.</li>
<li>A CV prepared on the university\u2019s structured CV template.</li>
<li>A research proposal on the university\u2019s template — you can propose your own project or select one from the \u201cFind a research project\u201d listings.</li>
<li>Written support from a prospective supervisor.</li>
</ul>
<p>The exact CV and proposal templates live on the official scholarships page; download those rather than improvising.</p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Find your project.</strong> Browse the university\u2019s \u201cFind a research project\u201d listings, or draft your own proposal on the university\u2019s template.</li>
<li><strong>Contact a supervisor.</strong> Line up written supervisor support — applications without a willing supervisor go nowhere.</li>
<li><strong>Submit your research degree application</strong> through the official scholarships/admissions portal before your round closes. Round 1 is open now with no published close date, so do not leave this late.</li>
<li><strong>Upload everything the portal asks for</strong> (transcripts, English evidence, templated CV and proposal) and verify the submission is complete.</li>
<li><strong>CSC applicants:</strong> secure your unconditional admission offer before 1 February 2027 and apply for the CSC partnership in parallel.</li>
</ol>
<p>Keep track of the round dates: Round 1 (open now), Round 2 (mid-February to late March 2027), Round 3 (mid-July to mid-August 2027).</p>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is the old UniSA RTPi/UPS scholarship still available?','No — the University of South Australia merged with the University of Adelaide in 2026 to form Adelaide University. The current equivalents are the Adelaide University Research Scholarship (AURS) and the Research Training Program Scholarship (RTPS). Tracker pages using the old names are stale.'),
 ('What is the stipend in 2026/2027?','The confirmed 2026 rate is A$36,500 per year, indexed annually. Ignore older tracker figures such as A$32,500 or A$35,200.'),
 ('Is there a separate scholarship application form?','No. You apply for admission to a research degree and are automatically considered for the scholarship rounds.'),
 ('I am an international student without an Australian qualification. Which round can I use?','Not GRTS Round 1 — it is restricted to domestic applicants and internationals holding an Australian or New Zealand qualification. Use a later round or an out-of-round award.'),
 ('Does the scholarship cover my family\u2019s health insurance?','The official page confirms OSHC support for international scholars \u201cwhere applicable\u201d; the single-versus-family detail is not published officially. Confirm with the university before relying on it.'),
 ('What does the China Scholarship Council partnership require?','Chinese nationals applying for a PhD: meet PhD entry and English requirements by 1 February 2027 and hold an unconditional offer of admission. The application window is 1 October 2026 to 1 February 2027.'),
]),
 verify='Verified 18 Oct 2026 against the official Adelaide University research scholarships page (adelaide.edu.au/graduate-research/scholarships — GRTS Rounds 1–3, CSC partnership 1 Oct 2026–1 Feb 2027, AURS/RTPS naming) and the official RTPS listing page (A$36,500/yr stipend, ~A$127,750 total value, 100% fee waiver, OSHC and relocation allowances). Relocation and OSHC single-policy figures are tracker-sourced and deliberately not repeated as facts; the GRTS document checklist is per trackers and marked as typical, not official. The UniSA-merger framing follows the university\u2019s own pages; old UniSA scholarship labels and stale stipend figures were rejected as outdated.',
 offlinks=[('Research scholarships — official page','https://www.adelaide.edu.au/graduate-research/scholarships'),
           ('RTPS scholarship listing (stipend & value)','https://www.adelaide.edu.au/study/scholarships/research-training-program-scholarship/'),
           ('Conditions of award','https://www.adelaide.edu.au/graduate-research/scholarships/conditions-of-award')],
 related_titles=['melbourne2027','singa2027','griffith-vc'],
))

# ---------------------------------------------------------------- 2. Unilever
ARTICLES.append(dict(
 slug='unilever-internships-2027-guide',
 title='Unilever Internships 2027 — How to Apply (Rolling, Country-Wise) | StudyDesk Scholarships',
 meta='Unilever internships 2027: no single global programme or deadline — roles are posted per country on careers.unilever.com and reviewed on a rolling basis. Currently open: Singapore ULIP (Jan–Jun 2027) and UK & Ireland Industrial Placements 2027. Enrolled students only; fresh graduates ineligible.',
 short='Unilever Internships 2027',
 kicker='Global · Internships Guide',
 mono='U', prov_short='Unilever', prov_cat='Company · Global',
 h1='Unilever Internships 2027 — How to Apply (Rolling, Country-Wise)',
 sub='There is no single \u201cUnilever Summer Internship\u201d with one deadline, whatever aggregator blogs claim. Unilever posts internships as individual country- and function-specific roles on its official careers portal, reviewed on a rolling basis until enough applications are in. The summer 2026 intake is closed; the live opportunities are the Singapore ULIP (January–June 2027) and the UK & Ireland Industrial Placements 2027. Here is how the system actually works.',
 dpill='Rolling admissions', dl_long='No single deadline — internships are posted per country and function on careers.unilever.com and reviewed on a rolling basis; each role closes once enough applications are received, so apply early. Currently open: Singapore ULIP Customer Development (internship period 11 January – 30 June 2027) and the UK & Ireland Industrial Placements 2027 (12 months from June 2027). Summer 2026 roles are closed.',
 facts=facts([('How it works','Per-country, per-function postings <small>No global intake, no single deadline: each role is a separate job listing on careers.unilever.com, reviewed on a rolling basis until filled</small>'),
              ('Open now','2027 intakes <small>Singapore ULIP (Jan–Jun 2027, Customer Development) and UK & Ireland Industrial Placements 2027 (12 months from June 2027)</small>'),
              ('Who it is for','Enrolled students only <small>Singapore ULIP requires current enrolment in a bachelor\u2019s or master\u2019s programme — fresh graduates are explicitly ineligible. UK placements require penultimate-year students returning to university afterwards</small>'),
              ('Pay','Not published on official postings <small>Third-party guides describe the programme as paid; one cites £27,898 per annum for a UK Technology placement — treat as reported, not officially confirmed</small>'),
              ('Honest framing','Not one programme <small>Ignore aggregator pages presenting this as a single global \u201cSubmit Applications\u201d scheme open to all nationalities — the official postings are per-listing, with their own regions, functions and timelines</small>')]),
 body='''<h2 id="about">About the internship programme</h2>
<p>Unilever does not run one global summer internship. What it runs is a <strong>per-market early-careers system</strong>: marketing, supply chain, technology, finance, R&D, human resources and customer-development internships are posted as <strong>individual job listings for individual countries</strong> on <strong>careers.unilever.com</strong>. Each listing carries its own location, function, duration, eligibility and start date — and applications are reviewed on a <strong>rolling basis</strong>, meaning a role closes as soon as Unilever has enough strong applicants. There is no published master deadline to work toward; the working rule is <strong>apply as soon as a role matching your profile appears</strong>.</p>
<p>The most structured tracks are the <strong>Unilever Leadership Internship Programme (ULIP)</strong> in markets like Singapore and the <strong>Industrial Placements</strong> in the UK & Ireland — year-long placements embedded in degree programmes.</p>
<h2 id="benefits">What the internship offers</h2>
<ul>
<li><strong>Duration:</strong> varies by market and role — about 6 months for Singapore ULIP, 12 months for UK Industrial Placements, and shorter summer slots in markets like Belgium.</li>
<li><strong>Real projects:</strong> ULIP Singapore projects include route-to-market and partner-onboarding work; UK placements sit in functions from technology to supply chain.</li>
<li><strong>Pay:</strong> <strong>not published</strong> on the official posting pages reviewed for this article. Third-party guides describe the programme as paid, and one cites £27,898 per annum for a UK Technology Industrial Placement 2027 (job ref R-1188417) — treat that as reported, not officially confirmed.</li>
<li><strong>Conversion:</strong> internship performance feeds into graduate hiring, though no official conversion guarantee is published — do not treat the internship as a job offer.</li>
<li><strong>Time commitment:</strong> Singapore ULIP asks for a minimum of 3 days a week, with full-time preferred; UK placements are full-time.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Enrolled students, not fresh graduates:</strong> Singapore ULIP explicitly requires applicants to be enrolled in a bachelor\u2019s or master\u2019s degree programme — <strong>fresh graduates are ineligible</strong>. UK Industrial Placements require students to have <strong>completed their penultimate year</strong> and be returning to university after the placement.</li>
<li><strong>Regions are per-listing:</strong> the Singapore posting is for candidates able to work in Singapore; UK roles sit at sites like Port Sunlight, Leeds, Burton and Kingston and expect relocation. Aggregator claims of \u201call nationalities welcome\u201d are not supported by the official postings.</li>
<li><strong>Functions differ per market:</strong> Customer Development, Human Resources, Consumer Marketing / Digital Marketing, Supply Chain, Technology, Finance and R&D appear across the live postings — check each listing.</li>
<li><strong>One application per market:</strong> the UK page asks applicants to apply for <strong>only one function</strong> — only the first application is considered.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Each posting lists its own requirements, but across the official pages the consistent asks are:</p>
<ul>
<li>A <strong>CV</strong> — always.</li>
<li>Academic transcripts and certificates for some roles (e.g. finance internships).</li>
<li>Evidence of your right to work in the posting\u2019s country, where applicable.</li>
</ul>
<p>Check the specific posting\u2019s \u201cWhat we need\u201d section rather than relying on a generic checklist.</p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Go to careers.unilever.com</strong> and search for internship / early-careers roles, filtering by country and function.</li>
<li><strong>Open a specific posting</strong> (for example, the Singapore ULIP Customer Development role, ref R-1187705) and read the whole listing — eligibility, dates and process are listing-specific.</li>
<li><strong>Create an account and click \u201cApply Online\u201d</strong> — early. Rolling review means the best roles can fill weeks before any nominal closing date.</li>
<li><strong>Complete the assessments.</strong> The Singapore ULIP process runs: online application → SOVA blended assessments → phone interview → virtual interview with the hiring manager → offer.</li>
<li><strong>Respect the one-function rule</strong> on the UK & Ireland hub — apply to one function only, or only your first application counts.</li>
</ol>
<p>For the US Summer Intern Program, third-party guides expect postings on Unilever\u2019s Workday portal between September and November 2026 for summer 2027 — as of early October 2026 no US intern postings were live, so verify directly on careers.unilever.com.</p>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is there one global Unilever Summer Internship application?','No. Unilever posts internships as individual country- and function-specific roles on careers.unilever.com. There is no single programme, no single deadline, and no single eligibility list — every listing stands alone.'),
 ('Are summer 2026 internships still open?','No. The summer 2026 postings found (e.g. Belgium digital marketing starting July–September 2026, Singapore ULIP roles running 13 July–31 December 2026) have passed. The open intakes are for 2027.'),
 ('Can fresh graduates apply?','For the flagship tracks, no. Singapore ULIP explicitly requires current enrolment and lists fresh graduates as ineligible; UK Industrial Placements require penultimate-year students returning to their degree.'),
 ('Is the internship paid?','Unilever\u2019s own posting pages do not publish pay figures. Third-party sources describe the programme as paid — one cites £27,898 per annum for a UK Technology placement — but that is reported, not officially confirmed.'),
 ('What is the selection process?','Typically: online application, SOVA blended assessments, phone interview, then a virtual interview with the hiring manager. Steps vary by market — read the posting.'),
 ('How do deadlines work with rolling review?','There are no fixed deadlines on most postings. Roles are reviewed as applications arrive and close once filled, so applying early materially improves your chances.'),
]),
 verify='Verified 18 Oct 2026 against the official Unilever careers portal (careers.unilever.com): the Singapore ULIP Customer Development posting (published 2026-09-01, internship period 11 Jan–30 Jun 2027, eligibility, selection steps — page read directly), the UK & Ireland early-careers industrial placements hub ("2027 Industrial Placement Opportunities Are Now Open!"), and the Belgium digital-marketing internship posting (summer 2026, now past). The "no single global programme" framing follows the official postings; aggregator blogs presenting one global scheme with generic eligibility were rejected. Pay figures: not published on the official postings viewed; third-party figures marked as reported, not confirmed.',
 offlinks=[('Unilever careers portal — internship roles','https://careers.unilever.com/en/'),
           ('UK & Ireland early careers & industrial placements','https://careers.unilever.com/en/uk-and-ireland-early-careers-industrial-placements')],
 related_titles=['oecd','epfl-summer','kaust-vsrp'],
))

# ---------------------------------------------------------------- 3. Stowers
ARTICLES.append(dict(
 slug='stowers-summer-scholars-program-2027-usa',
 title='Stowers Summer Scholars Program 2027 in USA (Fully Funded) | StudyDesk Scholarships',
 meta='Stowers Summer Scholars Program 2027: $5,000 salary, round-trip travel and accommodation for an 8-week research internship at the Stowers Institute, Kansas City (7 Jun–30 Jul 2027). Deadline 17 Jan 2027, 11:59 pm ET. Open to domestic and international undergraduates via GradCAS.',
 short='Stowers Summer Scholars 2027',
 kicker='USA · Summer Research',
 mono='S', prov_short='Stowers Institute for Medical Research', prov_cat='Research Institute · USA',
 h1='Stowers Summer Scholars Program 2027 in USA (Fully Funded)',
 sub='Eight weeks of real biomedical research in Kansas City — paid. The Stowers Institute for Medical Research opens its 2027 Summer Scholars Program to undergraduates worldwide: a $5,000 salary, round-trip travel and accommodation, an independent research project under a principal investigator, weekly seminars and a closing poster session, running 7 June to 30 July 2027. Applications are open now and close 17 January 2027 at 11:59 pm Eastern Time.',
 dpill='17 Jan 2027 · 91 days to go', dl_long='11:59 pm Eastern Time on 17 January 2027. Applications opened 1 October 2026 and are reviewed on a rolling basis within the window — submit early, and note that an application cannot be altered after submission. The programme itself runs 7 June – 30 July 2027.',
 facts=facts([('Award','$5,000 salary <small>No application fee and no participation fee. Round-trip transportation between your school and Kansas City, plus accommodation near the Stowers campus, are provided</small>'),
              ('Duration','8 weeks <small>7 June – 30 July 2027 (brief delay exceptions possible for school calendars, by email inquiry). Full-time availability required</small>'),
              ('Who it is for','Undergraduates worldwide <small>Completed one year of undergraduate study by the programme start; 18 or older; enrolled in or just graduated from a degree-granting undergraduate programme in biology, biochemistry, molecular biology, genetics, chemistry, physics, computing, engineering, mathematics or a related field</small>'),
              ('How to apply','GradCAS portal <small>Online application via the official "Apply now" link, plus two letters of recommendation uploaded by the recommenders. Unofficial transcripts at application stage; official ones only after acceptance</small>'),
              ('International students','Welcome <small>Accepted international scholars are supported by Stowers Immigration Services on the visa process — confirmed on both the programme page and the FAQ</small>')]),
 body='''<h2 id="about">About the program</h2>
<p>The <strong>Stowers Summer Scholars Program</strong> is the Stowers Institute for Medical Research\u2019s annual undergraduate summer research program in Kansas City, USA. Selected scholars spend <strong>eight weeks</strong> working on an <strong>independent research project under a principal investigator</strong>, attend weekly scientific seminars, join weekly lunches with Stowers scientists, and present at a closing all-Institute poster session. Group activities around the Kansas City area round out the experience.</p>
<p>What sets it apart from most summer programs: it is <strong>fully funded with a salary rather than a stipend waiver</strong> — $5,000 for the eight weeks — plus travel and housing, with no fees at any stage. Applications for the 2027 cohort are <strong>open now</strong> on a rolling basis.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>$5,000 salary</strong> for the eight-week program (confirmed on the program page and in the FAQ).</li>
<li><strong>Round-trip transportation</strong> between your school and Kansas City.</li>
<li><strong>Accommodation</strong> near the Stowers campus.</li>
<li><strong>Group activities</strong> around the Kansas City area.</li>
<li><strong>No fees:</strong> no application fee and no participation fee.</li>
</ul>
<p>The 2027 cohort size is not published — treat any figure you see online as unconfirmed. The notification timeline for the 2027 cycle is likewise not published; the FAQ still carries stale 2026-cycle text in two spots (a January 2026 deadline and March 2026 offer dates), so rely on the main 2027 page for all dates.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Full-time availability</strong> from 7 June to 30 July 2027 (brief delay exceptions are possible for school calendars — ask by email first).</li>
<li><strong>Completed one year of undergraduate studies</strong> by the program start.</li>
<li><strong>18 years of age or older</strong> before the program start date.</li>
<li><strong>Field:</strong> enrolled in or just graduated from a degree-granting undergraduate program in <strong>biology, biochemistry, molecular biology, genetics, chemistry, physics, computing, engineering, mathematics, or a related field</strong>.</li>
<li><strong>Nationality:</strong> open to <strong>domestic and international students</strong>; Stowers Immigration Services supports accepted international scholars with the visa process.</li>
<li><strong>Open to previous Summer Scholars</strong> — returning applicants are welcome.</li>
<li><strong>Not eligible:</strong> anyone enrolled in or beginning a master\u2019s, medical, or PhD program in Fall 2026. Combined BS/MS students must be within the first four years (equivalent to a US undergraduate program).</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Everything goes through the <strong>GradCAS portal</strong>:</p>
<ul>
<li>The completed <strong>GradCAS application</strong>: biographical information, a previous laboratory experience essay (including school projects), a statement of interest in Stowers research laboratories, and an optional personal statement.</li>
<li><strong>Unofficial transcript(s)</strong> uploaded to the application — official transcripts are requested only after acceptance.</li>
<li><strong>Two letters of recommendation</strong>, uploaded by the recommenders themselves through GradCAS (a third letter is optional).</li>
</ul>
<p>Submit early: once submitted, the application <strong>cannot be altered</strong>.</p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Confirm your eligibility</strong> — one year of undergraduate study completed, 18+ by the start date, right field, and no graduate program starting in Fall 2026.</li>
<li><strong>Draft your essays</strong> — the laboratory-experience essay and the statement of interest carry real weight; name the Stowers laboratories whose research genuinely interests you.</li>
<li><strong>Line up two recommenders early</strong> — they upload the letters themselves through GradCAS, and late letters sink applications.</li>
<li><strong>Apply online through the GradCAS portal</strong> via the \u201cApply now\u201d button on the official Summer Scholars page (the 2027 portal runs on the GradCAS system).</li>
<li><strong>Watch your email after the deadline</strong> — every applicant is contacted with the outcome. Questions: summerscholars@stowers.edu.</li>
</ol>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('Is the Stowers Summer Scholars Program really fully funded?','Yes. The 2027 program pays a $5,000 salary, covers round-trip travel to Kansas City and accommodation near the campus, and charges no application or participation fee.'),
 ('Can international students apply?','Yes. The program is explicitly open to domestic and international students, and Stowers Immigration Services supports accepted international scholars with the visa process.'),
 ('I will graduate in spring 2027. Am I eligible?','Yes — students who have just graduated from a degree-granting undergraduate program are eligible, as long as you are not enrolled in or beginning a master\u2019s, medical, or PhD program in Fall 2026.'),
 ('Can I change my application after submitting?','No. GradCAS submissions cannot be altered after submission, so review everything before you hit submit.'),
 ('Are previous Summer Scholars allowed to reapply?','Yes — the official eligibility rules explicitly welcome previous Summer Scholars.'),
 ('When will I hear back?','The 2027 notification timeline is not published. The FAQ\u2019s March dates refer to the 2026 cycle and are stale — ignore them.'),
]),
 verify='Verified 18 Oct 2026 against the official Stowers Institute pages: the 2027 Summer Scholars page (stowers.org/gradschool/summer-scholars — "Applications are now open", Key Dates: applications 1 Oct 2026 – 17 Jan 2027 11:59 pm ET, program 7 Jun – 30 Jul 2027, $5,000 salary, travel and accommodation, eligibility, GradCAS requirements) and the companion FAQ page (fees, salary, age-18 rule, international eligibility). The FAQ\u2019s two stale 2026-cycle date lines were deliberately ignored; the 2027 cohort size and notification timeline are not published and are not stated as facts.',
 offlinks=[('Summer Scholars 2027 — official page','https://www.stowers.org/gradschool/summer-scholars'),
           ('Summer Scholars FAQ','https://www.stowers.org/gradschool/summer-scholars-faq')],
 related_titles=['kaust-vsrp','epfl-summer','oecd'],
))

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

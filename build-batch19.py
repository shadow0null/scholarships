#!/usr/bin/env python3
"""Batch 19 (cron run 19): 5 verified articles. Verified 18 Oct 2026.

Written this run:
1. Kaunas University of Technology Scholarships 2027 (Lithuania) — written
   for the OPEN 2027 intake (admissions opened 15 Oct 2026, deadline 31 May
   2027). KTU's own scheme = full/partial tuition waiver, automatic
   consideration, no separate form; explicitly NOT fully funded (tuition only).
   Lithuanian state grants (€592/mo + full tuition, 70 grants, master's, listed
   nationalities) covered as the fully-funded route.
2. Türkiye Burslari Scholarships 2027 (Turkey) — written as a 2027 preparation
   guide: the 2027 call is NOT yet formally published (as of 18 Oct 2026); the
   10 Jan–20 Feb 2027 window is the official standing annual calendar, flagged
   as "expected". Stipends per official sources: TL 4,500/6,500/9,000 per
   level; aggregator 6,500/9,500/13,000 figures rejected as unconfirmed.
3–5. (added after second verification wave — see below)

SKIPPED this run (coordinator-verified, 18 Oct 2026): CUMT CSC 2026 (closed
10 Mar 2026; no 2027 announced; stipend figures contradictory across
aggregators); University of Szeged Hungarian Scholarships 2026 (Stipendium
Hungaricum 2026/27 closed 15 Jan 2026; 2027/28 call not yet published —
re-queue once Tempus publishes, expected ~mid-Nov 2026); AScI International
Summer Program 2026 (2026 edition ran, window 7–31 Jan 2026 closed; 2027
edition announced with applications 7–31 Jan 2027 — premature to write now,
re-queue Dec 2026–Jan 2027).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'ktu2027': dict(mono='KTU', title='Kaunas University of Technology Scholarships 2027 in Lithuania (Funded)', href='kaunas-university-of-technology-scholarships-2027-lithuania.html',
              dpill='31 May 2027 · 225 days to go', award='Full or partial tuition fee waiver (merit-based)', elig='International applicants to English-taught bachelor’s/master’s; outstanding academic results.',
              tags=[('Undergraduate', 'blue'), ('Lithuania', 'teal')]),
 'turkiye2027': dict(mono='TB', title='Türkiye Burslari Scholarships 2027 in Turkey (Fully Funded)', href='turkiye-burslari-scholarships-2027-turkey.html',
              dpill='Expected Jan 2027 · 84 days to go', award='Full tuition + TL 4,500–9,000/mo + housing + flights', elig='Citizens of all countries except Türkiye; 70%/75%/90% grade minimums; age caps per level.',
              tags=[('Undergraduate', 'blue'), ('Turkey', 'teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 1. KTU 2027
ARTICLES.append(dict(
 slug='kaunas-university-of-technology-scholarships-2027-lithuania',
 title='Kaunas University of Technology Scholarships 2027 in Lithuania (Funded) | StudyDesk Scholarships',
 meta='KTU Scholarships 2027: full or partial tuition fee waivers for international students at Kaunas University of Technology, Lithuania — automatic consideration with your admission application by 31 May 2027. Plus Lithuanian state grants (€592/month + full tuition) for master’s students.',
 short='KTU Scholarships 2027',
 kicker='Lithuania · University Scholarships',
 mono='KTU', prov_short='Kaunas University of Technology', prov_cat='University · Lithuania',
 h1='Kaunas University of Technology Scholarships 2027 in Lithuania (Funded)',
 sub='Kaunas University of Technology has opened admissions for the September 2027 intake — and with it, its merit-based tuition scholarships for international students. There is no separate scholarship form: every applicant through apply.ktu.edu is automatically considered for a full or partial tuition fee waiver. Separately, Lithuanian state grants worth €592 a month plus full tuition are available for master’s students from selected countries.',
 dpill='31 May 2027 · 225 days to go', dl_long='31 May 2027 — KTU’s published application deadline for the September 2027 intake. Scholarship consideration is automatic with your admission application (no separate form); scholarship receivers are announced by mid-July.',
 facts=facts([('Award','Full or partial tuition fee waiver <small>KTU’s own merit-based scheme for candidates with outstanding results, varying by study programme; automatic consideration — no separate application</small>'),
              ('State grant route','€592/month + full tuition <small>70 Lithuanian state grants for full-time master’s students from selected nationalities — the genuinely fully-funded route at KTU</small>'),
              ('Who it is for','International applicants <small>English-taught bachelor’s and master’s programmes; must meet the programme’s academic and English-language entry requirements</small>'),
              ('How you are considered','Automatic <small>Apply for admission via apply.ktu.edu and you are automatically a scholarship candidate — receivers notified by mid-July</small>'),
              ('Honest framing','Tuition only, not living costs <small>KTU’s own waiver covers tuition fees — budget separately for living costs in Kaunas unless you hold the state grant</small>'),
              ('Admissions status','2027 intake open <small>Applications opened 15 October 2026; the 2026 cycle (deadline 1 June 2026) is closed</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>Kaunas University of Technology (KTU)</strong> — Lithuania’s leading technological university, founded in 1922 — offers <strong>merit-based tuition scholarships</strong> to international applicants for its English-taught bachelor’s and master’s programmes. The award takes the form of a <strong>full or partial tuition fee waiver</strong> for candidates with outstanding academic results, with the exact coverage depending on the chosen study programme.</p>
<p>The single most convenient feature: <strong>there is no separate scholarship application</strong>. Everyone who applies for admission through KTU’s official application portal, apply.ktu.edu, automatically becomes a scholarship candidate. KTU publishes the scholarship receivers by <strong>mid-July</strong>.</p>
<p>Read the framing carefully: KTU’s own scheme covers <strong>tuition fees only</strong> — it does not pay living costs. Trackers that label this a "fully funded" scholarship are overclaiming. The genuinely fully-funded route at KTU is the separate <strong>Lithuanian state grant</strong> programme described below.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>KTU tuition waiver:</strong> full or partial waiver of tuition fees for candidates with outstanding results, awarded per programme. No living stipend is attached to this scheme.</li>
<li><strong>Lithuanian state grants (master’s):</strong> <strong>70 grants</strong> offering <strong>€592 per month plus full tuition fee coverage</strong> — open to full-time master’s students from a listed set of nationalities: Armenia, Azerbaijan, China (including Taiwan), Georgia, Indonesia, Israel, Japan, Kazakhstan, Moldova, New Zealand, Philippines, South Korea, Ukraine, USA, Uzbekistan, Vietnam, plus foreign citizens of Lithuanian origin from non-EU/EFTA countries.</li>
</ul>
<p>The state-grant route is competitive and separate from KTU’s automatic waiver — check the official KTU state-scholarship page for its own application rules and deadlines (the 2026-cycle state-grant deadline was 20 April 2026).</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Nationality:</strong> international applicants — open to students from all countries (the state grant additionally restricts by nationality as listed above).</li>
<li><strong>Study level:</strong> English-taught bachelor’s or master’s programmes at KTU starting September 2027.</li>
<li><strong>Academic standing:</strong> "outstanding results" — selection is merit-based. (Tracker-reported fixed grade thresholds are not confirmed on KTU’s official pages and are not repeated here.)</li>
<li><strong>Entry requirements:</strong> you must meet the programme’s academic entry requirements <strong>and</strong> its English-language requirements.</li>
<li><strong>Admission first:</strong> the waiver can only be held alongside an actual KTU study place.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Because scholarship consideration is automatic, your <strong>admission application documents</strong> are your scholarship documents. Across KTU and independent sources, these consistently include:</p>
<ul>
<li>Completed online application form (via apply.ktu.edu).</li>
<li>Academic transcripts and degree certificate / proof of previous education.</li>
<li>Valid passport (identity document).</li>
<li>Proof of English proficiency meeting the programme requirement.</li>
</ul>
<p>Some trackers additionally mention a motivation letter, CV or recommendation letters — these appear only on the aggregator page and are <strong>unconfirmed</strong>; follow the document list the official application portal asks for.</p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Pick your programme</strong> from KTU’s English-taught bachelor’s and master’s offerings and read its entry requirements carefully.</li>
<li><strong>Apply for admission through apply.ktu.edu</strong> before 31 May 2027 — this one application doubles as your scholarship application.</li>
<li><strong>Upload your documents</strong> exactly as the portal requests (transcripts, passport, English proof).</li>
<li><strong>State-grant route:</strong> if you are a full-time master’s applicant from a listed nationality, follow the separate Lithuanian state-grant process on KTU’s official state-scholarship page.</li>
<li><strong>Wait for mid-July</strong>, when KTU announces the scholarship receivers.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is the KTU scholarship fully funded?','No — and this is the key honesty point. KTU’s own scheme is a full or partial tuition fee waiver; it does not cover living costs. The fully-funded option at KTU is the Lithuanian state grant (€592/month + full tuition), available only to full-time master’s students from selected nationalities.'),
 ('Is there really no separate scholarship form?','Correct. KTU states that all applicants through apply.ktu.edu automatically become scholarship candidates — receivers are announced by mid-July.'),
 ('What are the deadlines?','Admissions for the September 2027 intake close 31 May 2027. The 2026-cycle scholarship deadlines (1 June 2026 for tuition waivers, 20 April 2026 for state grants) are long closed.'),
 ('Which nationalities qualify for the Lithuanian state grant?','Per KTU’s official page: Armenia, Azerbaijan, China (including Taiwan), Georgia, Indonesia, Israel, Japan, Kazakhstan, Moldova, New Zealand, Philippines, South Korea, Ukraine, USA, Uzbekistan, Vietnam, and foreign citizens of Lithuanian origin from non-EU/EFTA countries.'),
 ('What does the state grant pay?','€592 per month plus full tuition fee coverage — 70 grants in the programme.'),
 ('Do I need Lithuanian language?','No — the scholarships target English-taught programmes, but you must meet the programme’s English-language entry requirement.'),
]),
 verify='Verified 18 Oct 2026 against official KTU pages: apply.ktu.edu/news/archive (admissions for international students opened 15 Oct 2026; "apply by 31 May" for the September 2027 start), en.ktu.edu/events/2992162/ (merit-based scholarships and tuition fee waivers for eligible applicants; no separate application), en.ktu.edu/news/study-masters-at-ktu-with-a-state-scholarship/ (70 Lithuanian state grants; €592/month + full tuition; master’s; listed nationalities). Deliberately framed as tuition-only funding, not "fully funded"; tracker-only figures (fixed grade thresholds, "fully funded" labels, motivation-letter requirements) omitted or flagged as unconfirmed.',
 offlinks=[('KTU admissions for international students (official news archive)','https://apply.ktu.edu/news/archive'),
           ('KTU merit scholarships & tuition waivers (official event page)','https://en.ktu.edu/events/2992162/'),
           ('Lithuanian state grants for master’s at KTU (official)','https://en.ktu.edu/news/study-masters-at-ktu-with-a-state-scholarship/')],
 related_titles=['sabanci','ceu-hungary','eiffel'],
))

# ---------------------------------------------------------------- 2. Türkiye Burslari 2027
ARTICLES.append(dict(
 slug='turkiye-burslari-scholarships-2027-turkey',
 title='Türkiye Burslari Scholarships 2027 in Turkey (Fully Funded) | StudyDesk Scholarships',
 meta='Türkiye Burslari 2027: the Turkish government’s fully funded scholarship — full tuition, TL 4,500–9,000/month stipend, free housing, flights and a Turkish language course. Applications expected 10 January–20 February 2027 via TBBS; here is the preparation guide while the 2027 call is being published.',
 short='Türkiye Burslari 2027',
 kicker='Turkey · Government Scholarship',
 mono='TB', prov_short='Türkiye Burslari', prov_cat='Government of Turkey',
 h1='Türkiye Burslari Scholarships 2027 in Turkey (Fully Funded)',
 sub='Türkiye’s flagship government scholarship covers full tuition, a monthly stipend of up to TL 9,000, free accommodation, health insurance, flights and a one-year Turkish language course — one free application for up to 12 university programmes. One honest caveat: the 2027 call has not yet been formally published as of October 2026, so this is a preparation guide based on the official annual calendar — the application window is expected from 10 January to 20 February 2027.',
 dpill='Expected Jan 2027 · 84 days to go', dl_long='EXPECTED: 10 January – 20 February 2027. This is the fixed annual General Application Period published in Türkiye Scholarships’ official calendar (the 2026 window ran 10 Jan – 20 Feb 2026). The 2027 call itself has not yet been formally announced as of 18 October 2026 — confirm the dates on turkiyeburslari.gov.tr when the call is published.',
 facts=facts([('Award','Full tuition + placement <small>One application places you at a Turkish university and department — you rank up to 12 programmes; no separate university application or fee</small>'),
              ('Monthly stipend','TL 4,500–9,000/month <small>Associate’s/bachelor’s TL 4,500, master’s TL 6,500, PhD TL 9,000 (official 2026 figures; merit-track scholars receive 2×)</small>'),
              ('Housing + insurance','Free dormitory + health cover <small>Free accommodation, general health insurance, and a once-off flight ticket on arrival plus a return ticket at graduation</small>'),
              ('Language course','1-year Turkish course <small>Compulsory free Turkish language year for awardees without a C1 Turkish certificate, before the degree starts</small>'),
              ('Who it is for','All countries except Türkiye <small>70% associate’s/bachelor’s, 75% master’s/PhD, 90% for Medicine/Dentistry/Pharmacy; age under 21 / 30 / 35 at the application deadline</small>'),
              ('Application','Free via TBBS <small>One centralized online application — no intermediaries, no agents, no application fee; shortlisted candidates are interviewed</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>Türkiye Burslari (Türkiye Scholarships)</strong> is the Turkish government’s international scholarship programme for full-time associate’s, bachelor’s, master’s and PhD study at Turkish universities. It is one of the genuinely fully-funded government scholarships in the world: <strong>tuition, a monthly stipend, accommodation, health insurance and flights</strong> are all covered, and the whole process runs through a <strong>single free online application</strong> — there is no application fee, no agents, and no separate university application.</p>
<p><strong>The honesty note first:</strong> the 2027 call has <strong>not yet been formally announced</strong> as of 18 October 2026. Türkiye Scholarships runs a fixed annual calendar — the 2026 window was 10 January to 20 February 2026, and the standing calendar keeps that same General Application Period every year — so the 2027 window is <strong>expected from 10 January to 20 February 2027</strong>. Treat every date below as "expected until published" and confirm on turkiyeburslari.gov.tr when the 2027 call goes live. (Several aggregators already advertise "2027 applications announced" — that claim is extrapolated, not backed by a published official call.)</p>
<h2 id="benefits">What the scholarship pays</h2>
<ul>
<li><strong>Full tuition fee coverage</strong> — plus university and department placement: you rank up to 12 programmes in your single application.</li>
<li><strong>Monthly stipend:</strong> <strong>TL 4,500/month</strong> (associate’s/bachelor’s), <strong>TL 6,500/month</strong> (master’s), <strong>TL 9,000/month</strong> (PhD) — per the official benefits figures (2026), with merit-track scholars receiving <strong>2× the standard stipend</strong>.</li>
<li><strong>Free accommodation</strong> (university dormitory housing).</li>
<li><strong>General health insurance.</strong></li>
<li><strong>Flights:</strong> a once-off flight ticket on arrival in Türkiye and a return ticket upon graduation.</li>
<li><strong>Free 1-year Turkish language course</strong> — compulsory for all awardees without a C1 Turkish certificate, completed before the degree programme begins.</li>
</ul>
<p>A note on stipend figures: two aggregator sites claim higher amounts (TL 6,500/9,500/13,000) with no official citation. This article uses the <strong>official 4,500/6,500/9,000 figures</strong>, independently confirmed by the University of St. Gallen’s funding database (updated January 2026).</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Citizenship:</strong> citizens of <strong>all countries except Türkiye</strong>. Dual nationals holding Turkish citizenship are <strong>not eligible</strong>. You must not already be enrolled in a Turkish university at the same study level, and you cannot apply for a level you have already studied in Türkiye.</li>
<li><strong>Graduation:</strong> already graduated, or due to graduate before the award year.</li>
<li><strong>Academic minimums:</strong> <strong>70%</strong> for associate’s/bachelor’s, <strong>75%</strong> for master’s and PhD, <strong>90%</strong> for Medicine, Dentistry and Pharmacy.</li>
<li><strong>Age limits (at the application deadline):</strong> bachelor’s <strong>under 21</strong>, master’s <strong>under 30</strong>, PhD <strong>under 35</strong>, research track <strong>under 45</strong> (per the official criteria page; some aggregators vary on the research-track figure).</li>
<li><strong>Researchers and academics</strong> are eligible for the research track.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>From the official "Application in 5 Steps" page:</p>
<ul>
<li>Valid identity document / ID card / passport.</li>
<li>A photograph taken within the last 1 year.</li>
<li>National exam results (if any).</li>
<li>Diploma or temporary graduation certificate.</li>
<li>Official transcript.</li>
<li>International exam results (GRE, GMAT, SAT, etc.) — if required by your chosen university/programme.</li>
<li>International language test results (TOEFL, DELF, etc.) — if required by your chosen programme.</li>
<li>For PhD applicants: a research-topic proposal and a written example of research you have carried out.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Watch turkiyeburslari.gov.tr</strong> for the 2027 call — expected to open around 10 January 2027.</li>
<li><strong>Register in TBBS</strong> (the Türkiye Scholarships Application System at tbbs.turkiyeburslari.gov.tr) — it is free, and there are no legitimate intermediaries or agents.</li>
<li><strong>Complete the single centralized application:</strong> personal details, academic background, documents, and your ranking of up to <strong>12 programmes/universities</strong>.</li>
<li><strong>Submit within the window</strong> — the system closes when the General Application Period ends; late applications are not accepted.</li>
<li><strong>Attend the interview</strong> if shortlisted (evaluation March–April, interviews April–June per the official calendar).</li>
<li><strong>Results</strong> are published in early August, with transfers to Türkiye in September — awardees without C1 Turkish then begin the compulsory language year.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is the 2027 call actually open yet?','Not yet, as of 18 October 2026. The 10 January–20 February 2027 window is expected based on the official standing annual calendar (the 2026 window ran 10 Jan–20 Feb 2026). Confirm on turkiyeburslari.gov.tr when the call is published.'),
 ('Is the application really free?','Yes — TBBS is free and Türkiye Scholarships states there are no intermediaries or agents. Anyone asking for a fee in its name is running a scam.'),
 ('What does "fully funded" cover here?','Full tuition, a TL 4,500–9,000/month stipend by level, free dormitory housing, health insurance, a once-off arrival flight plus return at graduation, and the free Turkish language year.'),
 ('Can I apply if I already study in Türkiye?','Only if you are applying for a higher level than you currently hold — you cannot be enrolled at the same study level, and you cannot repeat a level already studied in Türkiye.'),
 ('Do I need to know Turkish?','No — awardees without a C1 certificate complete a free compulsory 1-year Turkish course before their degree starts.'),
 ('Why do some sites show higher stipends?','Two aggregators claim TL 6,500/9,500/13,000 with no official citation. The official figures — independently confirmed by the University of St. Gallen funding database — are TL 4,500/6,500/9,000.'),
]),
 verify='Verified 18 Oct 2026 against turkiyeburslari.gov.tr: the official 2026 call announcement (10 Jan–20 Feb 2026 window, one period for international students from all countries), the official annual calendar (General Application Period Jan 10–Feb 20; evaluation Mar–Apr; interviews Apr–Jun; results early Aug; transfers Sep), the "Application in 5 Steps" page (document list, mandatory 1-year Turkish course), and the official eligibility criteria page (70%/75%/90% minimums; age under 21 UG / 30 master’s / 35 PhD / 45 research; all countries except Türkiye; no dual Turkish citizens). Stipend figures 4,500/6,500/9,000 TL from the official benefits page, independently confirmed by the University of St. Gallen funding database (updated 12.01.2026). 2027 dates explicitly framed as expected (call not yet published); aggregator "2027 announced" claims and higher stipend figures rejected as unconfirmed.',
 offlinks=[('Türkiye Scholarships — official homepage','https://turkiyeburslari.gov.tr'),
           ('Official application calendar','https://www.turkiyeburslari.gov.tr/calendar'),
           ('Application in 5 Steps — documents & process (official)','https://www.turkiyeburslari.gov.tr/applysteps'),
           ('TBBS — Türkiye Scholarships Application System','https://tbbs.turkiyeburslari.gov.tr')],
 related_titles=['sabanci','gks2027','iuj'],
))

# ---------------------------------------------------------------- 3. SINGA 2027
ARTICLES.append(dict(
 slug='singapore-international-graduate-award-singa-2027',
 title='Singapore International Graduate Award (SINGA) 2027 \u2014 Fully Funded PhD in Singapore | StudyDesk Scholarships',
 meta='SINGA 2027: the Singapore International Graduate Award offers a fully funded PhD \u2014 full tuition for 4 years, S$2,700\u2013S$3,200/month stipend, airfare and settling-in allowance, no bond. August 2027 intake applications close 1 December 2026 via the A*STAR portal.',
 short='SINGA 2027',
 kicker='Singapore \u00b7 PhD Scholarship',
 mono='SA', prov_short='A*STAR, NUS, NTU, SUTD', prov_cat='Research · Singapore',
 h1='Singapore International Graduate Award (SINGA) 2027 \u2014 Fully Funded PhD in Singapore',
 sub='A fully funded PhD route into Singapore\u2019s research ecosystem: the Singapore International Graduate Award, a collaboration between A*STAR and Singapore\u2019s universities (NTU, NUS, SUTD), pays full tuition for up to four years, a monthly stipend of up to S$3,200, airfare and a settling-in allowance \u2014 with no service bond. Applications for the August 2027 intake close 1 December 2026.',
 dpill='1 Dec 2026 \u00b7 44 days to go', dl_long='1 December 2026, 23:59 (GMT+8) \u2014 for the August 2027 intake. A second intake (January 2028, at A*STAR and NTU only) closes 1 June 2027. Dates are consistently published across independent sources; A*STAR\u2019s dedicated SINGA page is currently unavailable, so re-confirm on the official A*STAR scholarships page before applying.',
 facts=facts([('Award','Full tuition for up to 4 years <small>Full tuition fees for the whole PhD at NTU, NUS, SUTD (or A*STAR research institutes)</small>'),
              ('Monthly stipend','S$2,700 \u2192 S$3,200 <small>S$2,700/month, rising to S$3,200/month after passing the PhD Qualifying Examination</small>'),
              ('Travel + settling-in','S$1,500 + S$1,000 <small>One-time airfare grant of up to S$1,500 and a one-time S$1,000 settling-in allowance</small>'),
              ('Bond','None <small>No service bond — and priority on-campus accommodation for first-year scholars</small>'),
              ('Who it is for','International graduates <small>Open to all international graduates with excellent academic results; Singapore citizens, PRs and those who previously studied in Singapore are NOT eligible</small>'),
              ('Application','A*STAR portal <small>Entirely online: register, select SINGA, rank up to 3 preferred research projects/supervisors, and ensure 2 referee reports arrive before the deadline</small>')]),
 body='''<h2 id="about">About the award</h2>
<p>The <strong>Singapore International Graduate Award (SINGA)</strong> is a collaboration between the <strong>Agency for Science, Technology and Research (A*STAR)</strong> and Singapore\u2019s universities \u2014 the Nanyang Technological University (NTU), the National University of Singapore (NUS) and the Singapore University of Technology and Design (SUTD) \u2014 for international students pursuing a <strong>PhD in science and engineering</strong> in Singapore.</p>
<p>It is one of the rare genuinely bond-free, fully-funded PhD routes: tuition, living costs, travel and settling-in are all covered, and scholars simply research. Note the naming honesty point behind this article: the queue source called it "Singapore Government Scholarships 2026" \u2014 that is a vague aggregator title, not a real scheme. The real scheme is SINGA, the 2026 cycle is closed, and the live cycle is the <strong>August 2027 intake</strong>.</p>
<h2 id="benefits">What the award pays</h2>
<ul>
<li><strong>Full tuition fees</strong> for up to <strong>4 years</strong> of PhD study.</li>
<li><strong>Monthly stipend of S$2,700</strong>, rising to <strong>S$3,200/month</strong> after passing the PhD Qualifying Examination.</li>
<li><strong>One-time airfare grant of up to S$1,500.</strong></li>
<li><strong>One-time settling-in allowance of S$1,000.</strong></li>
<li><strong>Priority for on-campus accommodation</strong> in the first year.</li>
<li><strong>No service bond.</strong></li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Nationality:</strong> open to <strong>all international graduates</strong> with a passion for research and excellent academic results. Singapore citizens, Singapore permanent residents, and applicants who have previously studied in Singapore are <strong>not eligible</strong>.</li>
<li><strong>Study level:</strong> graduates applying for PhD programmes in biomedical sciences, physical sciences, engineering, or computing and information sciences.</li>
<li><strong>Language:</strong> a good command of written and spoken English.</li>
<li><strong>References:</strong> good reports from academic referees (two recommendation reports are mandatory).</li>
<li><strong>Fields:</strong> research-oriented PhD tracks across the sciences and engineering.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>Copy of a valid passport or national ID.</li>
<li>Recent passport-size photograph.</li>
<li>Bachelor\u2019s and/or master\u2019s academic transcripts and certificates (with certified English translations where needed).</li>
<li>CV/r\u00e9sum\u00e9 and a statement of purpose or research proposal.</li>
<li><strong>Two recommendation letters</strong>, submitted online by the referees themselves before the deadline (applications with fewer than two reports are not considered).</li>
<li>GRE/TOEFL/IELTS/GATE scores are optional — but the host university may request them at the admission stage.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Confirm the intake on A*STAR\u2019s official scholarships page</strong> before you start (the dedicated SINGA URL is currently unavailable — use the A*STAR scholarships home page linked below).</li>
<li><strong>Register an account</strong> on the A*STAR applicant portal and select the "Singapore International Graduate Award (SINGA)".</li>
<li><strong>Browse the research projects and rank up to 3 preferred projects/supervisors</strong> — this ranking is part of the application.</li>
<li><strong>Complete the application form</strong> and upload all documents.</li>
<li><strong>Line up your referees early</strong> and make sure both reports are submitted online <strong>before 1 December 2026, 23:59 (GMT+8)</strong>.</li>
<li><strong>Submit and track</strong> — no hard-copy mailing is accepted; everything is online.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is SINGA really fully funded?','Yes — full tuition for up to 4 years, a S$2,700–S$3,200/month stipend, up to S$1,500 in airfare and a S$1,000 settling-in allowance, with no service bond.'),
 ('Who is not eligible?','Singapore citizens, Singapore permanent residents, and anyone who has previously studied in Singapore.'),
 ('What does "August 2027 intake" mean?','PhD studies commence in August 2027; the application deadline is 1 December 2026. There is also a January 2028 intake (A*STAR and NTU only) with a 1 June 2027 deadline.'),
 ('Do I need GRE or IELTS?','Not for the SINGA application itself — but the host university may request test scores during admission, so keep them ready if you have them.'),
 ('How many supervisors can I choose?','You browse the listed research projects and rank up to 3 preferred projects/supervisors in the application.'),
 ('Why can\u2019t I find the official SINGA page?','A*STAR restructured its site and the old dedicated SINGA URL returns a 404. The scheme is confirmed as live on A*STAR\u2019s BII graduate-research page and its scholarships home page — start there.'),
]),
 verify='Verified 18 Oct 2026: SINGA\u2019s existence confirmed live on official A*STAR pages (a-star.edu.sg/bii/join-us/graduate-research lists SINGA as a collaboration between A*STAR, NTU, NUS and SUTD; a-star.edu.sg/ime/careers lists it under International Students > Graduate). The widely-quoted dedicated SINGA URL returned HTTP 404 today, so all benefit and deadline figures (full tuition up to 4 years; S$2,700 rising to S$3,200 after the Qualifying Examination; S$1,500 airfare; S$1,000 settling-in; no bond; deadlines 1 Dec 2026 / 1 Jun 2027) are corroborated across 5+ independent sources and explicitly flagged as third-party-published — readers are told to re-confirm on the official A*STAR site. The queue\u2019s "Singapore Government Scholarships 2026" title was a vague aggregator label, not a real scheme — the article is honestly titled for SINGA.',
 offlinks=[('A*STAR scholarships — official home','https://www.a-star.edu.sg/scholarships/home/scholarships'),
           ('SINGA collaboration — A*STAR BII graduate research (official)','https://www.a-star.edu.sg/bii/join-us/graduate-research')],
 related_titles=['oecd','kaust-vsrp','science-tokyo'],
))

# ---------------------------------------------------------------- 4. META4.0 2027
ARTICLES.append(dict(
 slug='erasmus-mundus-meta4-0-scholarship-2027',
 title='Erasmus Mundus META4.0 Scholarship 2027 (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus META4.0 2027–2029: a fully funded 2-year joint master in intelligent and sustainable manufacturing across France, Slovenia, Norway, Germany and Italy — €1,400/month for 24 months, full participation costs and insurance. Applications open 15 Nov 2026; deadline 15 Feb 2027.',
 short='Erasmus Mundus META4.0 2027',
 kicker='Europe · Erasmus Mundus',
 mono='M4', prov_short='META4.0 Consortium (Erasmus Mundus)', prov_cat='European Union · Master’s',
 h1='Erasmus Mundus META4.0 Scholarship 2027 (Fully Funded)',
 sub='A two-year, fully English-taught joint master in manufacturing by intelligent and sustainable technologies, run by six European universities and funded by Erasmus Mundus: €1,400 a month for 24 months, full participation costs and insurance — plus multiple national master’s degrees. The 2027–2029 call opens 15 November 2026 and closes 15 February 2027.',
 dpill='15 Feb 2027 · 120 days to go', dl_long='15 February 2027, 23:59 (Paris time) — the programme’s published recurring annual deadline (Nov 15 – Feb 15 window) for the 2027–2029 intake. Applications open 15 November 2026. The date is carried by three independent sources matching the official annual window; the official site states the window without a year-specific date.',
 facts=facts([('Award','€1,400/month × 24 months <small>Full Erasmus Mundus lump sum for subsistence, travel and accommodation — up to ~€51,600 total value</small>'),
              ('Participation costs','100% covered <small>Tuition, library, lab and mandatory costs across all 4 semesters, plus the EACEA insurance package</small>'),
              ('Degrees','Multiple national master’s <small>Two years, 120 ECTS, fully taught in English, with international mobility across the consortium</small>'),
              ('Consortium','6 universities, 5 countries <small>Coordinated by ENISE / École Centrale de Lyon; Mines Saint-Étienne, Politecnico di Torino, University of Ljubljana, NTNU, TU Chemnitz</small>'),
              ('Who it is for','Engineering graduates <small>BSc/BEng (180 ECTS) in mechanical engineering, materials science or mechatronics; average grade B or higher; all nationalities</small>'),
              ('Standout requirement','Motivation VIDEO <small>Instead of a written cover letter: a ≤3-minute MP4 motivation video (≤70 MB), plus a mandatory 12-question questionnaire</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>META4.0</strong> is a genuine EU-funded <strong>Erasmus Mundus Joint Master</strong> — a two-year (120 ECTS), fully English-taught master’s degree in <strong>manufacturing by intelligent and sustainable technologies</strong>. It is run by a consortium of six universities across five countries, coordinated by <strong>ENISE (École Centrale de Lyon)</strong>, with Mines Saint-Étienne, Politecnico di Torino, the University of Ljubljana, NTNU and TU Chemnitz. Around <strong>90 scholarships are funded across the programme’s four cohorts</strong>, per TU Chemnitz’s official press release.</p>
<p>The honesty note: the queue source framed this as "2026" — that intake’s deadline (15 February 2026) has passed. The next cycle is the <strong>2027–2029 intake</strong>, starting early September 2027, with applications opening <strong>15 November 2026</strong> and closing <strong>15 February 2027</strong>.</p>
<h2 id="benefits">What the scholarship pays</h2>
<ul>
<li><strong>€1,400 per month for 24 months</strong> — the standard Erasmus Mundus lump sum covering subsistence, travel and accommodation (total value around €51,600).</li>
<li><strong>Full coverage of participation costs</strong> for all four semesters — tuition, library, laboratory and mandatory costs.</li>
<li><strong>Insurance package</strong> (health cover under EACEA rules).</li>
<li><strong>Multiple national master’s degrees</strong> from the consortium universities, plus structured international mobility.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<p>From the official application page (master-meta4-0.eu/application):</p>
<ul>
<li><strong>Degree:</strong> Bachelor of Science or Engineering (180 ECTS equivalent), with an <strong>average grade of B or higher</strong>.</li>
<li><strong>Field:</strong> at least 3 years of study in <strong>mechanical engineering, materials science & engineering</strong>, or potentially mechatronics.</li>
<li><strong>Mathematics:</strong> documented minimum of <strong>135 face-to-face hours</strong> of mathematics or related subjects.</li>
<li><strong>English (not older than 2 years):</strong> IELTS 6.5 (≥6.0 in each band), TOEFL 95 iBT (or ~600 paper), Cambridge FCE grade A/B, or TOEIC 800. Graduates of English-medium programmes in listed countries (including India) may be exempt with an official university letter.</li>
<li><strong>Final-year students</strong> may apply conditionally — graduation must be confirmed before 31 July of the call year.</li>
<li><strong>Nationality:</strong> all nationalities are eligible.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>Europass CV, passport-type photo and passport ID-page copy.</li>
<li>Degree certificates/diplomas with English translation (or an official letter if the degree is not yet delivered).</li>
<li>Academic transcripts <strong>with grading-scale information</strong>.</li>
<li>English proficiency evidence (or exemption letter).</li>
<li>Mathematics-level evidence (the 135-hour documentation).</li>
<li>Proof of residence less than 3 months old, in English.</li>
<li>The <strong>mandatory META4.0 questionnaire</strong> — 12 questions including 4 scenario questions.</li>
<li><strong>One recommendation letter</strong> on institutional letterhead (submitted by the student).</li>
<li><strong>A motivation video</strong> — ≤3 minutes, MP4, ≤70 MB. Written cover letters are <strong>not accepted</strong>.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Read the official application page</strong> (master-meta4-0.eu/application) in full — the eligibility and document bar is specific and strict.</li>
<li><strong>Record your motivation video early</strong> — it is the document most applicants will find unusual; plan and keep it under 3 minutes / 70 MB.</li>
<li><strong>Gather the mathematics evidence and grading-scale documents</strong> — these are the items most likely to delay an application.</li>
<li><strong>Apply online</strong> via the consortium’s dedicated application platform (linked from the official application page) after 15 November 2026.</li>
<li><strong>Register for the official admissions webinar</strong> if one is announced for this call.</li>
<li><strong>Know the selection funnel:</strong> eligibility check → pre-score → top-100 shortlist with two independent evaluators (at most 10 students of the same nationality) → possible March interviews → main and reserve lists; results by 24 March, confirmation 25 March – 1 April.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is META4.0 really an Erasmus Mundus programme?','Yes — it is an EU-funded Erasmus Mundus Joint Master running from 2022 to 2028, with around 90 scholarships across four cohorts, coordinated by ENISE (École Centrale de Lyon).'),
 ('When is the 2027–2029 deadline?','15 February 2027, 23:59 Paris time — the programme’s recurring annual deadline, published by three independent sources matching the official Nov 15 – Feb 15 window.'),
 ('What English scores are needed?','IELTS 6.5 (≥6.0 each), TOEFL 95 iBT, Cambridge FCE A/B, or TOEIC 800, not older than 2 years — or an official exemption letter for English-medium graduates in listed countries.'),
 ('What is the motivation video about?','A maximum 3-minute MP4 video (≤70 MB) replacing the traditional cover letter — treat it as your pitch, not a formality.'),
 ('Can final-year students apply?','Yes, conditionally — but your graduation must be confirmed before 31 July of the call year (2027).'),
 ('How many students are shortlisted?','The top 100 applications go to two independent evaluators, with a maximum of 10 students per nationality, before possible March interviews.'),
]),
 verify='Verified 18 Oct 2026 against the official META4.0 site (master-meta4-0.eu: real 2-year English-taught joint master; 6 universities in France, Slovenia, Norway, Germany, Italy; recurring Nov 15 – Feb 15 application window) and its official application page (full eligibility, document list, selection funnel, webinar), plus TU Chemnitz’s official press release (consortium, EU funding, 90 scholarships over 4 cohorts). The 15 Feb 2027 deadline is the published recurring deadline carried by three independent sources; benefit figures (€1,400/month × 24, ~€51,600 total) corroborated across multiple sources against the standard EMJM structure.',
 offlinks=[('META4.0 — official programme site','https://www.master-meta4-0.eu/'),
           ('Application page (official: timeline, eligibility, documents)','https://www.master-meta4-0.eu/application/'),
           ('TU Chemnitz press release on META4.0 (official)','https://www.tu-chemnitz.de/tu/pressestelle/aktuell/12129')],
 related_titles=['eiffel','globed','glocal'],
))

# ---------------------------------------------------------------- 5. KAS 2027
ARTICLES.append(dict(
 slug='kas-international-talent-development-scholarship-2027-germany',
 title='KAS International Talent Development Scholarship 2027 in Germany (Fully Funded) | StudyDesk Scholarships',
 meta='Konrad Adenauer Stiftung International Scholarship 2027: up to €992/month (bachelor’s/master’s) or €1,400/month (PhD) plus allowances for international students and doctoral candidates at German universities. Deadline 15 July 2027 — funded by the German Federal Foreign Office.',
 short='KAS Scholarship 2027',
 kicker='Germany · Foundation Scholarship',
 mono='KAS', prov_short='Konrad Adenauer Stiftung', prov_cat='Foundation · Germany',
 h1='KAS International Talent Development Scholarship 2027 in Germany (Fully Funded)',
 sub='Germany’s Konrad Adenauer Stiftung — funded by the Federal Foreign Office — supports international bachelor’s, master’s and doctoral students at German universities with up to €992 a month (€1,400 for doctoral candidates), plus health, family and research-travel allowances. The 2027 domestic deadline is 15 July 2027; applicants abroad apply through participating KAS foreign offices.',
 dpill='15 Jul 2027 · 270 days to go', dl_long='15 July 2027, 12:00 noon (CET) — the annual deadline for the domestic (in-Germany) selection procedure. Applicants from abroad apply via participating KAS foreign offices, which set their own office-specific deadlines.',
 facts=facts([('Monthly stipend','Up to €992/month <small>Bachelor’s, master’s and postgraduate students, standard funding period 2 years; doctoral candidates up to €1,400/month for 3 years</small>'),
              ('Allowances','Health + family + travel <small>Health insurance up to €120/month; family €276/month; child €250; research-travel grants; tuition-fee reimbursement up to €750/semester in exceptional cases</small>'),
              ('Language','German B2 required <small>Seminars and mentoring run in German — minimum B2 (Goethe-Institut certificate, DSH or TestDaF)</small>'),
              ('Who it is for','International students in Germany <small>Primarily non-EU bachelor’s, master’s and doctoral candidates at German universities (incl. HAW/FH); no age limit; no medicine/state-exam programmes</small>'),
              ('Beyond money','Full development programme <small>Seminars, personal mentoring, local university groups, international alumni network, specialized research colleges for doctoral students</small>'),
              ('Application','Two routes <small>In Germany: upload via the KAS Campus Portal; abroad: apply through a participating KAS foreign office in your home country/region</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The <strong>International Talent Development</strong> programme of the <strong>Konrad Adenauer Stiftung (KAS)</strong> — officially funded by the German Federal Foreign Office — is one of Germany’s established foundation scholarships for <strong>international students and doctoral candidates at German universities</strong> (including universities of applied sciences, HAW/FH). It combines a generous monthly stipend with a full development programme of seminars, mentoring and an international alumni network.</p>
<p>The honesty note: the queue source framed this as "2026" — that cycle’s deadline (15 July 2026) has passed. The programme runs <strong>annually</strong>, and the next domestic deadline is <strong>15 July 2027, 12:00 noon CET</strong>. Applicants from abroad follow a separate route through KAS foreign offices.</p>
<h2 id="benefits">What the scholarship pays</h2>
<p>Figures confirmed on the official KAS page and in the DAAD scholarship database:</p>
<ul>
<li><strong>Up to €992/month</strong> for bachelor’s, master’s and postgraduate students (standard funding period 2 years).</li>
<li><strong>Up to €1,400/month</strong> for doctoral candidates (standard funding period 3 years; full admission to a German doctoral programme required).</li>
<li><strong>Health insurance</strong> up to €120/month on request.</li>
<li><strong>Family allowance</strong> €276/month (spouse in Germany for more than 3 months); <strong>child allowance</strong> €250 per child.</li>
<li><strong>Research-travel grants</strong> abroad (conference visits excluded).</li>
<li><strong>Tuition-fee reimbursement</strong> up to €750/semester in exceptional cases. Enrolment/re-registration and semester fees are <strong>not</strong> covered.</li>
</ul>
<p>Non-financial benefits: a seminar programme, personal mentoring, local university groups, an international alumni network of over 3,000, and specialized research colleges for doctoral students.</p>
<h2 id="eligibility">Eligibility</h2>
<p>From the official KAS page:</p>
<ul>
<li><strong>Status:</strong> international students and doctoral candidates <strong>enrolled at German universities</strong> — primarily non-EU applicants.</li>
<li><strong>German language:</strong> minimum <strong>B2</strong> (Goethe-Institut certificate, DSH or TestDaF) — seminars run in German.</li>
<li><strong>Master’s applicants:</strong> must intend to enrol in a <strong>four-semester</strong> master’s programme.</li>
<li><strong>Bachelor’s applicants:</strong> at least <strong>two semesters</strong> of a bachelor’s programme at a German university completed.</li>
<li><strong>Doctoral applicants:</strong> full admission to a PhD programme at a German university.</li>
<li><strong>Minimum funding period:</strong> 4 semesters.</li>
<li><strong>Exclusions:</strong> human medicine, dentistry (state-exam programmes), medical specializations; programmes of only 3 semesters (e.g. some LL.M.); no postdoctoral funding and no bridge/follow-up funding.</li>
<li><strong>Values:</strong> academic excellence plus social/voluntary engagement and alignment with democratic values.</li>
<li><strong>Age:</strong> no age limit.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>The definitive checklist is the German-language <strong>"Notes on Applying for the International Scholarship Program"</strong> and Guidelines documents linked on the official KAS page. The general requirements include:</p>
<ul>
<li>Completed online application (via the KAS Campus Portal for the domestic route).</li>
<li>CV and motivation letter.</li>
<li>Academic transcripts and degree certificates.</li>
<li>German language certificate (B2 or higher).</li>
<li>Recommendation letters.</li>
</ul>
<p>Because the full official checklist sits in the German "Notes" document, treat the English FAQ as indicative and work from the official document for your final submission.</p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Choose your route:</strong> if you are already in Germany, apply through the <strong>domestic selection procedure</strong>; if abroad, contact the <strong>KAS foreign office</strong> responsible for your home country/region (only selected offices run the procedure each year).</li>
<li><strong>Read the official "Notes on Applying"</strong> document — it is the binding checklist, in German.</li>
<li><strong>Secure your German B2 certificate early</strong> if you do not have one — it is a hard requirement, not a nice-to-have.</li>
<li><strong>Prepare the Campus Portal upload</strong> (domestic route): application form, CV, motivation letter, transcripts, language certificate, recommendations.</li>
<li><strong>Submit before 15 July 2027, 12:00 noon CET</strong> (domestic). Office-abroad deadlines are set per office — ask your KAS office.</li>
<li><strong>For portal problems:</strong> campus.fachadmin@kas.de; general questions: stipendium-if@kas.de.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Who funds this scholarship?','The German Federal Foreign Office, via the Konrad Adenauer Stiftung — one of Germany’s official political-foundation scholarship programmes.'),
 ('How much does it pay?','Up to €992/month for bachelor’s, master’s and postgraduate students (2 years) and up to €1,400/month for doctoral candidates (3 years), plus health, family, child and research-travel allowances.'),
 ('Is there an age limit?','No age limit — but the study-level requirements (e.g. full PhD admission for doctoral funding) apply.'),
 ('Do I need German?','Yes: minimum B2, because the seminar and mentoring programme runs in German.'),
 ('Can I apply from my home country?','Yes — via a participating KAS foreign office in your country/region. Only selected offices run the procedure each year, so check with yours.'),
 ('What can’t it fund?','Medicine, dentistry and state-exam programmes; 3-semester programmes; postdoctoral research; bridge or follow-up funding. Enrolment and semester fees are also excluded.'),
]),
 verify='Verified 18 Oct 2026 against the official KAS page (kas.de/en/web/begabtenfoerderung-und-kultur/international-talent-development: €992/€1,400 monthly figures; allowance details; B2 requirement; exclusions; annual 15 July deadline at 12:00 noon CET; Campus Portal and foreign-office routes; contact emails) and corroborated by the DAAD scholarship database (detail 10000108). Written for the 2027 intake (2026 cycle closed 15 July 2026). Document checklist explicitly attributed to the official German "Notes" document, not invented from aggregators.',
 offlinks=[('KAS International Talent Development — official page','https://www.kas.de/en/web/begabtenfoerderung-und-kultur/international-talent-development'),
           ('DAAD scholarship database entry (official)','https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?detail=10000108')],
 related_titles=['daad','eiffel','hanns-seidel'],
))

ARTICLES_TWO = ARTICLES[:3]
ARTICLES_ALL = ARTICLES_TWO + ARTICLES[3:]
CARDINFO_ALL = dict(CARDINFO, **{
 'singa2027': dict(mono='SA', title='Singapore International Graduate Award (SINGA) 2027 — Fully Funded PhD in Singapore', href='singapore-international-graduate-award-singa-2027.html',
              dpill='1 Dec 2026 · 44 days to go', award='Full tuition (4 yrs) + S$2,700–3,200/month + airfare', elig='International graduates; not SG citizens/PRs or prior SG students.',
              tags=[('PhD', 'blue'), ('Singapore', 'teal')]),
 'meta40': dict(mono='M4', title='Erasmus Mundus META4.0 Scholarship 2027 (Fully Funded)', href='erasmus-mundus-meta4-0-scholarship-2027.html',
              dpill='15 Feb 2027 · 120 days to go', award='€1,400/month × 24 months + full participation costs', elig='BSc/BEng (180 ECTS) in mechanical/materials engineering; grade B+; all nationalities.',
              tags=[('Master’s', 'blue'), ('Europe', 'teal')]),
 'kas2027': dict(mono='KAS', title='KAS International Talent Development Scholarship 2027 in Germany (Fully Funded)', href='kas-international-talent-development-scholarship-2027-germany.html',
              dpill='15 Jul 2027 · 270 days to go', award='Up to €992/month (bachelor’s/master’s), €1,400/month (PhD) + allowances', elig='International students/doctoral candidates at German universities; German B2; no age limit.',
              tags=[('Postgraduate', 'blue'), ('Germany', 'teal')]),
})


if __name__ == '__main__':
    ok = 0
    for a in ARTICLES_TWO:
        assert a['slug'] not in [x['slug'] for x in ARTICLES_TWO[:ok]], a['slug'] + ' duplicated'
        sz = build_article(BASE, OUT, a, CARDINFO)
        ok += 1
        print('built', a['slug'], sz, 'bytes')
    import html.parser as hp
    for a in ARTICLES_TWO:
        path = OUT / (a['slug'] + '.html')
        src = path.read_text()
        p = hp.HTMLParser(); p.feed(src)
        for bad in ('AICTE Pragati', 'Lorem'):
            if bad in src:
                raise AssertionError((a['slug'], 'leftover', bad))
        print('validated', a['slug'])


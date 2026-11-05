#!/usr/bin/env python3
"""Batch 18 (cron run 18): 5 verified articles. Verified 18 Oct 2026.

Written this run:
1. University of Melbourne Research Scholarships 2027 (Australia) — 2027 cycle
   OPEN, Round 1 closes 31 Oct 2026. Official figures used throughout
   (A$41,100/yr 2027 stipend, 100% fee remission, up to A$138,000, 350 awards,
   automatic consideration); tracker "600 awards"/"$39,500 (2026 rate)" figures
   deliberately replaced.
2. Study in Canada Without IELTS 2026 — guide. Corroborated university list
   (Winnipeg, Brock, Memorial, Concordia, Regina, Saskatchewan, Guelph,
   Carleton, Trent, Manitoba, UNB, Brandon) + accepted alternatives
   (Duolingo 105-120, TOEFL iBT, PTE, CAEL, MOI waiver, internal ELP).
   Framed honestly: no IELTS != no English proof.
3. Webster University Vienna Scholarships 2027 (Austria) — Spring 2027 window
   open 1 Oct–30 Nov 2026; partial awards €3,000–€12,000/yr (official range);
   explicitly NOT fully funded.
4. Tiffin University Dragon Flight Fellowship 2027 (USA) — real honors
   fellowship in drone tech, annual deadline 1 Feb; no cash award published on
   the official page — framed honestly as experiential.
5. NUS International Undergraduate Scholarship 2027-28 (Singapore) — AY2027/28
   window opens 16 Dec 2026, closes mid-Feb 2027. Official nus.edu.sg figures:
   100% subsidised tuition after MOE Tuition Grant + S$5,800 living +
   S$1,750 computer + S$5,000 accommodation; automatic consideration via
   admission application; MOE TG (mandatory) carries a 3-year Singapore work
   obligation. Queue title said "2026" — written for the open 2027-28 cycle.
SKIPPED this run (coordinator-verified, 18 Oct 2026): Renmin CSC 2026 (closed
15 Feb 2026); New York Bloomberg Fellowship (Bloomberg journalism programme,
2026 cycle closed 28 Feb 2026); Top-25-without-IELTS (listicle); Bilateral
State Scholarships Hungary (Stipendium Hungaricum closed 15 Jan 2026); FuSEP
2026 (closed 22 Mar 2026); King Salman (disability-research prize, not a study
scholarship; 2026 round closed 31 Mar 2026); Luxembourg 2026 (closed 24 Mar
2026); KNB 2026 (closed 31 Mar 2026); British Turing (UK students only);
Killam (closed 20 Feb 2026); Kärnten Healthcare and Nursing 2026 (closed 15 Mar
2026; programme started Sep 2026; 2027 call not announced); Bader (closed 19
Feb 2026); EMMBIOME (unverifiable); Stanford summer (closed 3 Feb 2026);
Soochow CSC (closed 28 Feb 2026); Oslo (ISS window closed 1 Feb 2026); TIPP
2026 (closed 23 Feb 2026); Yale Hoffleit (closed 15 Feb 2026); Tsinghua CSC
(closed 28 Feb 2026); Fulbright Indigenous (Indigenous Australians only);
Arab-countries (listicle); KAIST-X (closed 15 Feb 2026); Ocean Leaders
(closed 15 Feb 2026); AIT ADB (closed 31 Mar 2026); IDEX Grenoble (closed 5 May
2026); Alaska Safety (closed 30 Apr 2026); Research Academy Ruhr (closed 15 Feb
2026); World Bank Graduate (duplicate of joint-japan-world-bank-graduate-
scholarship-2027); First-Year-Canada (listicle); Niskanen (closed 27 Feb
2026); GB-without-IELTS (listicle); IAPS (closed 2 Feb 2026); no-GRE/GMAT USA
(listicle); InteRussia (closed 1 Sep 2026); Cadieux Léger (Canadians only);
Uppsala (closed 2 Feb 2026); Wuhan YoE (closed 31 Mar 2026); AYFN Japan
(closed 20 Apr 2026); Kuwait-without-IELTS (listicle); Reuters (closed 13 Feb
2026); NCKU (closed 20 Jan 2026); Anhui Medical CSC (closed 25 Feb 2026);
World Bank Legal Internship (closed 14 Feb 2026; "(Paid)" label now wrong);
HAN 2026 (window closes 19 Oct 2026 — no shelf life, skipped on practical
grounds); HKU summer (closed 9 Feb 2026); AIIB internship (closed 28 Feb
2026); NKUST (closed 23 Jan 2026); Southern Denmark (closed 1 Sep 2026).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'melbourne2027': dict(mono='UM', title='University of Melbourne Research Scholarships 2027 in Australia (Fully Funded)', href='university-of-melbourne-research-scholarships-2027-australia.html',
              dpill='31 Oct 2026 · 13 days to go', award='Up to A$138,000 · 100% tuition fee remission', elig='Master’s by Research / PhD applicants; domestic + international; high academic achievement.',
              tags=[('PhD', 'blue'), ('Australia', 'teal')]),
 'canada-noielts': dict(mono='CA', title='Study in Canada Without IELTS 2026 – Universities, Tests and Waivers', href='study-in-canada-without-ielts-2026.html',
              dpill='Open routes · no single deadline', award='Admission routes without IELTS', elig='International students; English proof via Duolingo/TOEFL/PTE/MOI or pathway programmes.',
              tags=[('Guide', 'blue'), ('Canada', 'teal')]),
 'webster2027': dict(mono='WV', title='Webster University Vienna Scholarships 2027 in Austria (Partially Funded)', href='webster-university-vienna-scholarships-2027-austria.html',
              dpill='30 Nov 2026 · 43 days to go', award='€3,000–€12,000/year partial tuition award', elig='Newly admitted bachelor’s/master’s; 3.0 GPA; financial need; all nationalities.',
              tags=[('Undergraduate', 'blue'), ('Austria', 'teal')]),
 'tiffin2027': dict(mono='TU', title='Tiffin University Dragon Flight Fellowship 2027 in USA', href='tiffin-university-dragon-flight-fellowship-2027-usa.html',
              dpill='1 Feb 2027 · 106 days to go', award='Experiential fellowship — certifications + industry projects (no cash award published)', elig='Tiffin UG/graduate students; weekly in-person participation required.',
              tags=[('Fellowship', 'blue'), ('USA', 'teal')]),
 'nus2027': dict(mono='NUS', title='National University of Singapore Scholarships 2027-28 in Singapore (Fully Funded)', href='national-university-of-singapore-scholarships-2027-28-singapore.html',
              dpill='Opens 16 Dec 2026', award='100% subsidised tuition + S$5,800 living + S$5,000 accommodation', elig='International freshmen (all countries except Singapore); outstanding results, leadership, CCA.',
              tags=[('Undergraduate', 'blue'), ('Singapore', 'teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 1. Melbourne
ARTICLES.append(dict(
 slug='university-of-melbourne-research-scholarships-2027-australia',
 title='University of Melbourne Research Scholarships 2027 in Australia (Fully Funded) | StudyDesk Scholarships',
 meta='Melbourne Research Scholarships 2027: 350 fully funded awards for Master\u2019s by Research and PhD at the University of Melbourne \u2014 A$41,100/year stipend (2027 rate), full tuition fee offset, relocation grant and OSHC. Automatic consideration; Round 1 closes 31 October 2026.',
 short='Melbourne Research Scholarships 2027',
 kicker='Australia \u00b7 Research Scholarships',
 mono='UM', prov_short='University of Melbourne', prov_cat='University \u00b7 Australia',
 h1='University of Melbourne Research Scholarships 2027 in Australia (Fully Funded)',
 sub='One of Australia\u2019s largest fully funded research scholarship rounds \u2014 around 350 Melbourne Research Scholarships for 2027, each combining a full tuition fee offset with a A$41,100-a-year living stipend, a relocation grant and health cover. New applicants are considered automatically when they apply for their research degree; the main international round closes 31 October 2026.',
 dpill='31 Oct 2026 \u00b7 13 days to go', dl_long='31 October 2026 \u2014 Round 1 deadline for the 2027 intake. New applicants are automatically considered for the scholarship when they apply for an eligible graduate research degree; students already enrolled (or holding a deferred offer) should check the official page for the separate scholarship form, which closes on the same date.',
 facts=facts([('Award value','Up to A$138,000 (official) <small>100% tuition fee remission plus a living stipend; around 350 Melbourne Research Scholarships, alongside Australian Government RTP awards</small>'),
              ('Living stipend','A$41,100/year (2027 full-time rate) <small>Paid fortnightly, tax-free; up to 2 years for Master\u2019s by Research, up to 3.5 years for PhD; indexed annually; includes limited paid sick, parental and partner leave</small>'),
              ('Tuition cover','100% fee offset <small>Full fee remission for up to 2 years (Master\u2019s) or up to 4 years (doctoral); domestic students receive an RTP fee offset with their course offer</small>'),
              ('Relocation + health','A$2,000\u2013$3,000 + OSHC <small>One-off A$2,000 for interstate movers, A$3,000 for international arrivals; single Overseas Student Health Cover for student-visa holders</small>'),
              ('Who it is for','Domestic + international <small>High-achieving applicants enrolling in a Master\u2019s by Research or PhD across all research fields</small>'),
              ('Application','Automatic consideration <small>No separate scholarship form for new applicants \u2014 applying for the research degree by the round deadline puts you in the running</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The Melbourne Research Scholarship is the University of Melbourne\u2019s flagship award for graduate researchers, offered to high-achieving domestic and international students enrolling in a <strong>Master\u2019s by Research or a PhD</strong>. It sits alongside the Australian Government Research Training Program (RTP) scholarships \u2014 trackers often lump the two together into a "\u2248600 scholarships" headline, but the university\u2019s official listing puts the Melbourne Research Scholarship itself at <strong>around 350 awards</strong>, with RTP awards made separately. Both routes are fully funded in the true sense: tuition, living costs, relocation and health cover are all addressed.</p>
<p>The scheme is unusually applicant-friendly: for new applicants there is <strong>no separate scholarship application</strong>. You apply for the research degree, and the university automatically assesses you for scholarship funding.</p>
<h2 id="benefits">What the scholarship pays</h2>
<ul>
<li><strong>Full tuition fee offset</strong> \u2014 100% fee remission for up to 2 years (Master\u2019s by Research) or up to 4 years (doctoral).</li>
<li><strong>Living stipend of A$41,100 per year</strong> (2027 full-time rate, paid fortnightly) \u2014 for up to 2 years (Master\u2019s) or 3.5 years (PhD), indexed annually, with limited paid sick, parental and partner leave.</li>
<li><strong>Relocation grant</strong> \u2014 a one-off A$2,000 for students moving from other Australian states/territories, or A$3,000 for students arriving from outside Australia.</li>
<li><strong>Overseas Student Health Cover (OSHC)</strong> \u2014 single membership for international students who need a student visa.</li>
<li>The official listing values the combined package at <strong>up to A$138,000</strong>.</li>
</ul>
<p>A note on figures you may see elsewhere: several trackers still quote A$39,500 (the 2026 rate) and a "600 awards" total. The university\u2019s current official page lists the 2027 stipend rate (A$41,100) and 350 Melbourne Research Scholarships \u2014 this article uses the official figures.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Study level:</strong> applicants for a Master\u2019s by Research or doctoral degree at the University of Melbourne, in any research field.</li>
<li><strong>Nationality:</strong> open to domestic and international students from all countries.</li>
<li><strong>Academic standing:</strong> high-achieving applicants \u2014 the university selects on academic merit and research potential. (Tracker claims of a fixed "75\u201380% WAM" cut-off are not on the official page and are not repeated here.)</li>
<li><strong>Stage:</strong> both future (commencing) and current graduate researchers are eligible.</li>
<li><strong>Course entry requirements:</strong> you must meet the entry requirements of the research degree itself, including English language requirements.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Because new applicants are assessed automatically, there is no separate scholarship dossier \u2014 your <strong>course application is your scholarship application</strong>. That application typically includes:</p>
<ul>
<li>Academic transcripts and degree certificates.</li>
<li>A research proposal or statement of research interest.</li>
<li>Curriculum vitae and (usually two) referee reports.</li>
<li>English language test results (e.g. IELTS/TOEFL) meeting the course requirement.</li>
<li>Identification documents for the student-visa process (international applicants).</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Choose your research degree and check entry requirements</strong> on the University of Melbourne\u2019s graduate research pages, including English requirements for your faculty.</li>
<li><strong>Line up a supervisor (strongly advised):</strong> contacting a potential supervisor in your field before applying materially improves a research application.</li>
<li><strong>Apply for the course through the official portal by 31 October 2026</strong> \u2014 this is the Round 1 deadline for the 2027 intake and the main international round, when most scholarships are awarded.</li>
<li><strong>No separate scholarship form is needed</strong> if you are a new applicant \u2014 your course application puts you in the scholarship pool automatically.</li>
<li><strong>Already enrolled or holding a deferred offer?</strong> Scholarship trackers report a separate online scholarship form with the same 31 October deadline \u2014 confirm the current process on the official award page before the date passes.</li>
<li><strong>Await the outcome:</strong> scholarship offers are made with or shortly after course offers; the official status page currently reads "Open for automatic consideration".</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is there really no separate scholarship application?','Correct \u2014 for new applicants. The university automatically considers every eligible graduate-research course application for scholarship funding. Only students who are already enrolled (or holding a deferred offer) use a separate form, per scholarship trackers; confirm the current rule on the official page.'),
 ('What does \u201cfully funded\u201d actually cover here?','Full tuition fee remission, a A$41,100/year living stipend, a A$2,000\u2013$3,000 relocation grant and single OSHC for international students \u2014 the official combined value is up to A$138,000.'),
 ('How many scholarships are there \u2014 350 or 600?','The university\u2019s official listing shows around 350 Melbourne Research Scholarships. The "600" figure quoted by trackers bundles in Australian Government RTP awards made alongside them.'),
 ('Are there later application rounds?','Trackers report secondary rounds closing 31 January 2027 and 15 May 2027, with most awards made in Round 1. These later dates are not confirmed on the official award page \u2014 treat 31 October 2026 as your real deadline and verify any later round on the official site.'),
 ('Do I need a first-class honours degree?','The official criterion is "high-achieving" with strong research potential; there is no published fixed cut-off. A first-class honours (or a master\u2019s with a strong thesis component) is the typical profile of winners.'),
 ('Which fields are covered?','All of them \u2014 the scholarship spans every graduate research discipline at the university, from engineering and medicine to arts, law and education.'),
]),
 verify='Verified 18 Oct 2026 against the official University of Melbourne award page (scholarships.unimelb.edu.au/awards/melbourne-research-scholarship: status "Open for automatic consideration"; 100% fee remission; stipend A$41,100/year pro rata (2027 full-time rate), up to 2 yrs Master\u2019s / 3.5 yrs doctoral; relocation A$2,000/A$3,000; OSHC single membership; quantity 350; value up to A$138,000), with the 31 October 2026 Round 1 deadline corroborated by multiple scholarship trackers. Tracker-only figures (A$39,500 2026-rate stipend, "600 awards" aggregate, fixed 75\u201380% WAM cut-off, "10 business day" notification claims) deliberately omitted or flagged.',
 offlinks=[('Melbourne Research Scholarship \u2014 official award page','https://scholarships.unimelb.edu.au/awards/melbourne-research-scholarship'),
           ('Graduate research scholarships \u2014 official overview','https://scholarships.unimelb.edu.au/awards/graduate-research-scholarships')],
 related_titles=['griffith-vc','anz-summer','swiss-phd'],
))

# ---------------------------------------------------------------- 2. Canada without IELTS guide
ARTICLES.append(dict(
 slug='study-in-canada-without-ielts-2026',
 title='Study in Canada Without IELTS 2026 \u2013 Universities, Tests and Waivers | StudyDesk Scholarships',
 meta='Study in Canada without IELTS in 2026: the verified list of Canadian universities that accept Duolingo, TOEFL, PTE, CAEL or a medium-of-instruction waiver instead of IELTS \u2014 plus typical score requirements and how to apply.',
 short='Study in Canada Without IELTS 2026',
 kicker='Canada \u00b7 Country Guide',
 mono='CA', prov_short='Canadian Universities', prov_cat='Country Guide \u00b7 Canada',
 h1='Study in Canada Without IELTS in 2026: Universities, Accepted Tests and Waivers',
 sub='\u201cWithout IELTS\u201d does not mean \u201cwithout any English proof\u201d \u2014 but in 2026 a solid list of Canadian universities will admit international students on the strength of the Duolingo English Test, TOEFL, PTE, CAEL, a medium-of-instruction certificate, or their own pathway programmes. This guide maps the verified routes, the typical scores each university asks for, and exactly how to apply.',
 dpill='Open routes \u00b7 no single deadline', dl_long='No single deadline \u2014 each university follows its own admission calendar for the 2026 and 2027 intakes. English-proficiency rules also vary by programme and faculty, so always confirm the current requirement on the university\u2019s official admissions page before you apply.',
 facts=facts([('What \u201cwithout IELTS\u201d means','Alternative English proof <small>Canadian universities set their own language rules \u2014 most accept other tests or waive the requirement for students educated in English</small>'),
              ('Universities on the list','12 verified institutions <small>Winnipeg, Brock, Memorial, Concordia, Regina, Saskatchewan, Guelph, Carleton, Trent, Manitoba, New Brunswick, Brandon \u2014 requirements differ per university</small>'),
              ('Accepted alternatives','Duolingo \u00b7 TOEFL \u00b7 PTE \u00b7 CAEL <small>Typical minimums: Duolingo 105\u2013120, TOEFL iBT 80\u201390, PTE Academic 58\u201360, CAEL 50\u201360 \u2014 higher for competitive programmes</small>'),
              ('The no-test route','MOI / English-medium waiver <small>Several universities waive testing entirely if your previous schooling or degree was taught in English (medium-of-instruction certificate)</small>'),
              ('Backup route','Pathway / ELP programmes <small>Most listed universities run their own English Language / ESL pathway \u2014 complete it and enter the degree without an external test</small>'),
              ('Deadlines','Per-university calendars <small>Fall (September) is the main intake; winter and summer intakes exist at many institutions</small>')]),
 body='''<h2 id="about">The honest picture</h2>
<p>Canada has no national rule forcing international applicants to take IELTS. Each university sets its own English-proficiency policy, and a growing number of them accept alternatives or grant waivers. That is what "study in Canada without IELTS" actually means in 2026: <strong>you still prove your English, just not necessarily with IELTS</strong>. Be sceptical of any list that promises "no English test at all, guaranteed" \u2014 every route below requires either an alternative test score, documented English-medium education, or completion of a pathway programme.</p>
<h2 id="universities">Canadian universities that admit without IELTS (2026)</h2>
<p>Requirements below are the typical published minimums for undergraduate admission, corroborated across four independent 2025/26 guides. Graduate and competitive programmes usually ask for more.</p>
<ul>
<li><strong>University of Winnipeg</strong> \u2014 Duolingo, TOEFL, or completion of its English Language Program (ELP); waiver possible with prior English-medium study.</li>
<li><strong>Brock University</strong> \u2014 TOEFL iBT 88 (21 speaking), PTE 60, or its Intensive English Language Program (IELP); prior English study may suffice.</li>
<li><strong>Memorial University of Newfoundland</strong> \u2014 IELTS waiver possible with a previous degree in English; alternative tests and its own language programme accepted. Also among Canada\u2019s most affordable options.</li>
<li><strong>Concordia University</strong> \u2014 Duolingo 105, TOEFL, PTE 58, CAEL; waives the requirement with about 3 years of English-medium education.</li>
<li><strong>University of Regina</strong> \u2014 TOEFL, CAEL, PTE, Duolingo, CanTEST, or completion of internal ESL/EAP programmes instead of IELTS.</li>
<li><strong>University of Saskatchewan</strong> \u2014 TOEFL iBT 86, PTE 60, Duolingo 110; waiver for students with English-medium education.</li>
<li><strong>University of Guelph</strong> \u2014 Duolingo 105, PTE 58, TOEFL iBT 89, CAEL, or its English Language Certificate Program (ELCP).</li>
<li><strong>Carleton University</strong> \u2014 Duolingo 105, TOEFL iBT 86, PTE 58; waiver for prior English-medium study.</li>
<li><strong>Trent University</strong> \u2014 Duolingo 105, TOEFL iBT 83, PTE 58; waiver possible.</li>
<li><strong>University of Manitoba</strong> \u2014 Duolingo 105, TOEFL iBT 86, PTE 58; waiver with English-medium background.</li>
<li><strong>University of New Brunswick</strong> \u2014 Duolingo 105, TOEFL iBT 90, PTE 59; waiver with English-medium education.</li>
<li><strong>Brandon University</strong> \u2014 PTE, CanTEST, CAEL, CAE/CPE or TOEFL iBT instead of IELTS.</li>
</ul>
<h2 id="alternatives">The alternatives, explained</h2>
<ul>
<li><strong>Duolingo English Test (DET):</strong> the cheapest and fastest option (about an hour, online, results in 48 hours). Canadian universities that accept it typically ask for <strong>105\u2013120</strong>.</li>
<li><strong>TOEFL iBT:</strong> the most widely accepted alternative; typical minimums run <strong>80\u201390</strong> overall, sometimes with per-section floors.</li>
<li><strong>PTE Academic:</strong> typical minimums of <strong>58\u201360</strong> at the universities above.</li>
<li><strong>CAEL:</strong> the Canadian-designed test; typical minimums of <strong>50\u201360</strong>.</li>
<li><strong>Medium-of-instruction (MOI) certificate:</strong> an official letter from your school or university confirming your education was in English. Several universities waive all testing on this basis \u2014 Indian CBSE/ICSE students should ask their institution for one on letterhead.</li>
<li><strong>Pathway / ELP programmes:</strong> the university\u2019s own English course. Finish it (usually one or two terms) and progress to the degree with no external test.</li>
</ul>
<h2 id="how">How to apply without IELTS</h2>
<ol class="steps-list">
<li><strong>Shortlist 3\u20134 universities</strong> from the list above whose programmes match your goals \u2014 and open each university\u2019s official admissions page to confirm the current rule for your exact programme.</li>
<li><strong>Pick your proof:</strong> book Duolingo/TOEFL/PTE, request your MOI certificate, or apply for the pathway programme \u2014 whichever the university accepts.</li>
<li><strong>Apply through the university\u2019s online portal</strong> for the intake you want (Fall/September is the main one), uploading transcripts, your English proof, SOP and references.</li>
<li><strong>Apply for scholarships in parallel</strong> \u2014 language waivers do not reduce scholarship eligibility; automatic entrance awards (for example at Ottawa) are assessed on grades, not on which English test you took.</li>
<li><strong>Apply for the study permit</strong> once admitted; include your letter of acceptance and financial proof as IRCC requires.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Can I really study in Canada with zero English tests?','Only via two narrow routes: a medium-of-instruction waiver (your previous education was in English) or a university pathway programme. Every other "no IELTS" route substitutes a different test such as Duolingo or TOEFL.'),
 ('Is Duolingo accepted for a Canadian study permit?','The study permit itself is issued by IRCC, which does not mandate IELTS specifically \u2014 the language requirement comes from the university. If your university admits you on a Duolingo score, that satisfies the admission side of the process.'),
 ('Does skipping IELTS hurt my scholarship chances?','No. Entrance scholarships are awarded on academic merit (grades, sometimes leadership). The English test you used for admission does not enter the calculation.'),
 ('Which is the cheapest good option without IELTS?','Memorial University of Newfoundland and Brandon University are consistently the most affordable on this list, with some undergraduate tuition around CAD 11,000\u201315,000 a year \u2014 verify current fees on the official pages.'),
 ('Do I need IELTS for the visa interview?','Canada does not routinely interview study-permit applicants, and IRCC\u2019s published document checklist does not require IELTS. Strong finances and a genuine study plan matter more.'),
 ('What if my chosen university changes its policy?','Policies do change between intakes \u2014 the single most important step in this guide is re-checking the official admissions page of your shortlisted universities before you pay any application fee.'),
]),
 verify='Verified 18 Oct 2026 across four independent 2025/26 guides that agree on the university list and the accepted alternatives: MMS Global (Winnipeg, Brock, Memorial, Concordia, Regina, Saskatchewan, Guelph, Carleton, Trent, Manitoba, UNB with per-university test tables), Leverage Edu (DET/PTE/TOEFL/MOI pathways), Careers360 (QS-2026-referenced list with score bands: Duolingo 105\u2013120, TOEFL 80\u201390, PTE 58\u201360, CAEL 50\u201360), and Nigeria Private Schools 2025/26 list. Per-university minimums vary by programme and intake \u2014 stated as typical undergraduate minimums with an explicit re-check instruction. No invented "guaranteed admission" or visa claims.',
 offlinks=[('MMS Global \u2014 Study in Canada Without IELTS (2026 university table)','https://mmsglobal.io/blog/study-in-canada-without-ielts/'),
           ('Leverage Edu \u2014 Study in Canada Without IELTS','https://leverageedu.com/learn/study-in-canada-without-ielts/'),
           ('Careers360 \u2014 Study in Canada without IELTS 2026','https://studyabroad.careers360.com/articles/study-in-canada-without-ielts')],
 related_titles=['ottawa','griffith-vc','iuj'],
))

# ---------------------------------------------------------------- 4. Webster Vienna
ARTICLES.append(dict(
 slug='webster-university-vienna-scholarships-2027-austria',
 title='Webster University Vienna Scholarships 2027 in Austria (Partially Funded) | StudyDesk Scholarships',
 meta='Webster Vienna Private University Scholarships 2027: partial merit- and need-based awards of \u20ac3,000\u2013\u20ac12,000 per academic year for newly admitted bachelor\u2019s and master\u2019s students. Spring 2027 entry window: 1 October \u2013 30 November 2026.',
 short='Webster Vienna Scholarships 2027',
 kicker='Austria \u00b7 University Scholarships',
 mono='WV', prov_short='Webster Vienna Private University', prov_cat='University \u00b7 Austria',
 h1='Webster University Vienna Scholarships 2027 in Austria (Partially Funded)',
 sub='An American-accredited university in Vienna offering newly admitted bachelor\u2019s and master\u2019s students multiyear, merit- and need-based tuition awards of \u20ac3,000 to \u20ac12,000 per academic year. The Spring 2027 entry window is open now and closes 30 November 2026 \u2014 but read the fine print: these are partial scholarships, not full rides.',
 dpill='30 Nov 2026 \u00b7 43 days to go', dl_long='30 November 2026, 13:00 CET \u2014 Spring semester 2027 entry (application period 1 October \u2013 30 November 2026). The Fall 2026 window closed 31 May 2026. Apply for admission first, then request the scholarship form from the Admissions Office.',
 facts=facts([('Award','\u20ac3,000\u2013\u20ac12,000/year (official range) <small>Multiyear partial tuition awards; trackers report Distinction/Merit/Honors tiers (bachelor\u2019s up to \u20ac12,000, master\u2019s up to \u20ac8,000 per year)</small>'),
              ('Who it is for','Newly admitted degree students <small>Bachelor\u2019s and master\u2019s, all nationalities; minimum 3.0 GPA (US 4-point scale); proven financial need; English B2\u2013C1</small>'),
              ('Duration','Multiyear, renewable <small>Up to 4 years (bachelor\u2019s) or 2 years (master\u2019s), renewable with full-time enrolment and a 3.0 GPA each semester</small>'),
              ('How you apply','Admission first <small>Apply for admission, receive your acceptance letter, then request the scholarship form from Admissions and submit before the deadline</small>'),
              ('Honest framing','Partial funding only <small>These awards reduce tuition \u2014 they do not cover full tuition plus living costs. Budget for the remainder</small>'),
              ('Extras','Alumni + legacy discounts <small>Webster alumni get an automatic 20% master\u2019s tuition discount; legacy grants of 10% for close family</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>Webster Vienna Private University \u2014 the Austrian campus of the American-accredited Webster University network \u2014 offers <strong>partial, merit- and need-based scholarships</strong> to incoming undergraduate and graduate students. The flagship <strong>WVPU New Student Scholarships</strong> are multiyear tuition awards for newly admitted bachelor\u2019s and master\u2019s degree students, with amounts set by academic merit and demonstrated financial need.</p>
<p>Two things to get straight before you apply: these awards are <strong>partial</strong> (the university\u2019s own admissions page describes them as "partial, merit- and need-based scholarships and tuition grants"), and they are only for <strong>newly admitted full-degree students</strong> \u2014 certificate and English-preparation programmes are not eligible.</p>
<h2 id="benefits">What the scholarship pays</h2>
<ul>
<li><strong>WVPU New Student Scholarships:</strong> <strong>\u20ac3,000 to \u20ac12,000 per academic year</strong> (official range), awarded for multiple years. Scholarship trackers break this into Distinction, Merit and Honors tiers \u2014 roughly <strong>up to \u20ac12,000/year for bachelor\u2019s and up to \u20ac8,000/year for master\u2019s</strong> at the top tier \u2014 but the university\u2019s official figure is the \u20ac3,000\u2013\u20ac12,000 range.</li>
<li><strong>Borealis Social Scholarship / Borealis Excellence Award:</strong> separate named awards reported by trackers at up to \u20ac21,000 and \u20ac10,000 per academic year respectively \u2014 confirm availability with the Admissions Office, as these are not detailed on the main admissions page.</li>
<li><strong>Webster Alumni Graduate Discount:</strong> an automatic 20% tuition discount for Webster University alumni entering any master\u2019s programme.</li>
<li><strong>Webster Vienna Legacy Grant:</strong> 10% tuition reduction for students whose parent or sibling attends or graduated within the Webster network.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Status:</strong> newly admitted to a full bachelor\u2019s or master\u2019s degree programme at Webster Vienna (not certificate or English-prep tracks).</li>
<li><strong>Nationality:</strong> all nationalities, including international students.</li>
<li><strong>Academics:</strong> minimum GPA of 3.0 on the American 4-point scale, plus exceptional academic achievement for the higher tiers.</li>
<li><strong>Financial need:</strong> demonstrated significant financial need \u2014 this is a need-aware award.</li>
<li><strong>English:</strong> advanced or native-level proficiency (B2 to C1).</li>
<li><strong>Renewal:</strong> full-time enrolment and a minimum 3.0 GPA each semester.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>The completed scholarship application form (requested from the Admissions Office after admission).</li>
<li>Academic transcripts and proof of GPA.</li>
<li>Evidence of financial need (financial documents).</li>
<li>Proof of English proficiency (B2\u2013C1).</li>
<li>Essays as requested on the scholarship form (trackers mention reflective essay prompts).</li>
<li>Acceptance letter from Webster Vienna (you apply for the scholarship after admission).</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply for admission</strong> to your chosen bachelor\u2019s or master\u2019s programme at Webster Vienna.</li>
<li><strong>Receive your acceptance letter</strong> \u2014 only admitted students can proceed.</li>
<li><strong>Request the scholarship form</strong> from the Admissions Office (scholarship@webster.ac.at, per trackers).</li>
<li><strong>Prepare your financial and academic documents</strong> plus the required essays.</li>
<li><strong>Submit everything before 30 November 2026, 13:00 CET</strong> for Spring 2027 entry (the window runs 1 October \u2013 30 November).</li>
<li><strong>Note the visa timeline:</strong> international students needing an Austrian student residence permit should start early \u2014 processing can take 4\u20137 months, and you must show proof of financial capability beyond the scholarship.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Are Webster Vienna scholarships fully funded?','No \u2014 and this matters. They are partial awards of \u20ac3,000\u2013\u20ac12,000 per academic year against tuition. You must cover the remaining tuition plus living costs in Vienna, and show proof of financial capability for the residence permit.'),
 ('Who can apply?','Newly admitted bachelor\u2019s and master\u2019s degree students of any nationality, with at least a 3.0 GPA, B2\u2013C1 English, and demonstrated financial need.'),
 ('What are the deadlines?','Two windows a year: 31 May (13:00 CET) for fall entry and 30 November (13:00 CET) for spring entry. The currently open window is Spring 2027 entry, closing 30 November 2026.'),
 ('Do I apply for the scholarship before admission?','No \u2014 admission comes first. You request the scholarship form from the Admissions Office after receiving your acceptance letter.'),
 ('Can the award be renewed?','Yes, for up to 4 years (bachelor\u2019s) or 2 years (master\u2019s), provided you stay enrolled full-time and keep a 3.0 GPA each semester.'),
 ('I am a Webster alumnus \u2014 anything for me?','Yes: Webster University alumni receive an automatic 20% tuition discount on any master\u2019s programme, no separate application.'),
]),
 verify='Verified 18 Oct 2026 against the official Webster Vienna admissions page (webster.ac.at/admissions: "partial, merit- and need-based scholarships and tuition grants"; WVPU New Student Scholarships \u2014 incoming bachelor\u2019s/master\u2019s with minimum 3.0 GPA and proven financial need; multiyear awards \u20ac3,000\u2013\u20ac12,000/academic year; deadlines 31 May for fall entry, 30 Nov for spring entry), with the Spring window dates (1 Oct\u201330 Nov, 13:00 CET), tier breakdowns and document list corroborated by three trackers (o4af.com, scholarshipsads.com, zaupdates.co.za). Framed explicitly as partial funding; "fully funded" aggregator claims deliberately contradicted in-article.',
 offlinks=[('Webster Vienna admissions \u2014 tuition, financial aid and housing (official)','https://www.webster.ac.at/admissions/index.php')],
 related_titles=['daad','hanns-seidel','eiffel'],
))

# ---------------------------------------------------------------- 5. Tiffin Dragon Flight
ARTICLES.append(dict(
 slug='tiffin-university-dragon-flight-fellowship-2027-usa',
 title='Tiffin University Dragon Flight Fellowship 2027 in USA | StudyDesk Scholarships',
 meta='Tiffin University\u2019s Dragon Flight Fellowship: a four-year honors fellowship in drone technology with FAA engagement, industry projects and professional certifications. Annual application deadline 1 February; open to Tiffin undergraduate and graduate students.',
 short='Tiffin Dragon Flight Fellowship 2027',
 kicker='USA \u00b7 Fellowship',
 mono='TU', prov_short='Tiffin University', prov_cat='University \u00b7 USA',
 h1='Tiffin University Dragon Flight Fellowship 2027 in USA',
 sub='A four-year honors fellowship that turns Tiffin University students into drone-technology leaders \u2014 real flight time, FAA engagement, industry projects and professional certifications across sectors from public safety to filmmaking. Read this carefully first: it is an experiential fellowship, not a cash scholarship, and the official page publishes no monetary award.',
 dpill='1 Feb 2027 \u00b7 106 days to go', dl_long='1 February (annual) \u2014 the official programme page sets the application deadline at 1 February each year; the next occurrence is 1 February 2027. Confirm the cycle year on the official page before applying.',
 facts=facts([('What it is','Honors fellowship in drone tech <small>Four-year applied programme: drone operations, FAA engagement, industry projects, capstone and mentorship</small>'),
              ('Who it is for','Tiffin University students <small>Open to online and on-campus undergraduate and graduate students; weekly in-person participation is required</small>'),
              ('What you gain','Certifications + experience <small>Specialized certifications (thermal imaging, photogrammetry), FAA compliance work, agency internships, conference presentations \u2014 no cash award is published</small>'),
              ('Honest framing','Not a cash scholarship <small>The official page lists no monetary award. Treat this as a career-building fellowship, not funding for tuition</small>'),
              ('Eligibility steer','3.0 GPA benchmark (trackers) <small>Scholarship trackers report a 3.0 GPA requirement; the official page does not publish one \u2014 confirm with admissions</small>'),
              ('Application','Annual 1 February deadline <small>Apply via Tiffin admission + fellowship interest, essay and possible interview</small>')]),
 body='''<h2 id="about">About the fellowship</h2>
<p>The <strong>Dragon Flight Fellowship</strong> is Tiffin University\u2019s honors experience for students who want to lead in drone and aerial technology. It is structured as a <strong>four-year journey</strong> that grows with you: Year 1 covers drone operations, safety and regulations; Year 2 builds technical skill and teamwork; Year 3 moves into applied research and leadership in specialized areas; Year 4 is capstone projects, mentorship and a professional launch.</p>
<p>Fellows work on real missions with real partners \u2014 public-safety agencies, companies and community organizations \u2014 across sectors including environmental monitoring, public safety and emergency response, agriculture, construction and surveying, healthcare logistics, media and filmmaking, and autonomous systems.</p>
<h2 id="benefits">What fellows actually get</h2>
<ul>
<li><strong>Real flight time and real missions</strong> with industry and public-sector partners.</li>
<li><strong>Direct FAA engagement</strong> \u2014 compliance reports, safety initiatives and regulatory reviews.</li>
<li><strong>Specialized certifications</strong> such as thermal imaging and photogrammetry.</li>
<li><strong>Internships</strong> with state and local agencies.</li>
<li><strong>Research exposure</strong> \u2014 presenting at conferences or in professional publications.</li>
<li><strong>Leadership and mentorship</strong> \u2014 leading teams and mentoring junior fellows in the final year.</li>
</ul>
<p>What you do <strong>not</strong> get, as far as the official page states: a published cash award. Trackers label the programme "funded", but the university\u2019s own page describes an honors experience, not a scholarship cheque. If tuition funding is what you need, look at Tiffin\u2019s separate merit scholarships instead.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Enrolment:</strong> you must be a Tiffin University student \u2014 the programme is open to both online and on-campus undergraduate and graduate students.</li>
<li><strong>In-person commitment:</strong> weekly in-person participation is required, so online students must be able to attend regularly in Ohio.</li>
<li><strong>Academics:</strong> the official page publishes no GPA cut-off; scholarship trackers report a 3.0 GPA benchmark (high school for entry, college GPA to continue) \u2014 treat this as tracker-reported and confirm with admissions.</li>
<li><strong>Nationality:</strong> trackers describe it as open to students worldwide; international applicants must additionally meet Tiffin\u2019s admission requirements (including English proficiency).</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>Tiffin University admission application (undergraduate or graduate, as applicable).</li>
<li>Academic transcripts.</li>
<li>A short personal essay on why you want to join the fellowship and how drone technology fits your goals.</li>
<li>CV/r\u00e9sum\u00e9 and a valid passport (for international applicants).</li>
<li>Any supporting documents the admissions counsellor requests; an interview may follow.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply for admission to Tiffin University</strong> and indicate your interest in fellowship opportunities.</li>
<li><strong>Write the fellowship essay</strong> after submitting your application, outlining your interest in the programme.</li>
<li><strong>Speak with your admissions counsellor</strong> and complete any interview the university requests.</li>
<li><strong>Meet the 1 February deadline</strong> \u2014 the official page sets the fellowship application deadline at 1 February each year.</li>
<li><strong>If selected, accept the fellowship terms</strong> (active participation in fellowship events and programme regulations) to confirm your place.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is this a scholarship that pays money?','No \u2014 not according to the official page. It is an honors fellowship: the value is certifications, FAA and industry experience, internships and mentorship. Do not expect a tuition cheque.'),
 ('Who can join?','Tiffin University undergraduate and graduate students, on-campus or online \u2014 but weekly in-person participation is mandatory, so you need to be reachable for regular on-site sessions.'),
 ('When is the deadline?','1 February each year, per the official programme page. The next occurrence is 1 February 2027.'),
 ('Is there a GPA requirement?','The official page does not state one. Scholarship trackers report a 3.0 GPA benchmark for entry and continuation \u2014 confirm with the admissions office.'),
 ('Can international students apply?','Trackers describe the fellowship as open worldwide; you must first meet Tiffin University\u2019s international admission requirements.'),
 ('What do fellows do day to day?','Hands-on drone operations across sectors \u2014 thermal imaging for firefighting, mapping and surveying, FAA compliance work, agency internships, and a final-year capstone with real stakeholders.'),
]),
 verify='Verified 18 Oct 2026 against the official Tiffin University programme page (tiffin.edu/academics/dragon-flight-fellowship-program/: "honors experience"; application deadline February 1 (annual); open to online and on-campus undergraduate and graduate students with weekly in-person participation required; four-year structure \u2014 certifications including thermal imaging/photogrammetry, FAA engagement, agency internships, capstone and mentorship), corroborated by three trackers (scholarshipunion.com, brightscholarship.com, daadscholarship.com). No monetary award is published on the official page \u2014 framed as an experiential fellowship, not a cash scholarship; the 3.0 GPA benchmark is tracker-reported and flagged as such.',
 offlinks=[('Dragon Flight Fellowship \u2014 official programme page','https://www.tiffin.edu/academics/dragon-flight-fellowship-program/')],
 related_titles=['oecd','kaust-vsrp','epfl-summer'],
))


# ---------------------------------------------------------------- 5. NUS (next open in queue order after Tiffin)
ARTICLES.append(dict(
 slug='national-university-of-singapore-scholarships-2027-28-singapore',
 title='National University of Singapore Scholarships 2027-28 in Singapore (Fully Funded) | StudyDesk Scholarships',
 meta='NUS International Undergraduate Scholarship 2027-28: 100% subsidised tuition plus S$5,800 living, S$5,000 accommodation and S$1,750 computer allowances at the National University of Singapore. Automatic consideration with your admission application; window opens 16 December 2026.',
 short='NUS Scholarships 2027-28',
 kicker='Singapore \u00b7 Undergraduate Scholarships',
 mono='NUS', prov_short='National University of Singapore', prov_cat='University \u00b7 Singapore',
 h1='National University of Singapore Scholarships 2027-28 in Singapore (Fully Funded)',
 sub='NUS\u2019s flagship International Undergraduate Scholarship covers 100% of subsidised tuition fees plus annual living and accommodation allowances \u2014 and there is no separate scholarship form. You are automatically considered when you apply for undergraduate admission; the AY2027/28 window opens 16 December 2026.',
 dpill='Opens 16 Dec 2026', dl_long='AY2027/28 undergraduate applications open 16 December 2026; the international-qualification window closes in mid-February 2027 (the exact date varies by qualification route). Scholarship consideration is automatic with your admission application \u2014 shortlisted candidates may be invited to a selection interview.',
 facts=facts([('Award','100% subsidised tuition + allowances <small>Full coverage of subsidised undergraduate tuition fees (after the MOE Tuition Grant) for the normal candidature period</small>'),
              ('Living allowance','S$5,800/year <small>Annual living allowance for the duration of the scholarship</small>'),
              ('Accommodation','S$5,000/year <small>Annual accommodation allowance, plus a one-time S$1,750 computer allowance on enrolment</small>'),
              ('Who it is for','International freshmen <small>Citizens of all countries except Singapore, applying for a first full-time undergraduate degree at NUS; transfer applicants are not eligible</small>'),
              ('How you are considered','Automatic <small>No separate scholarship application \u2014 candidates are considered and shortlisted through their undergraduate admission application</small>'),
              ('The key condition','MOE Tuition Grant required <small>Recipients must take up the MOE Tuition Grant, which carries a 3-year work obligation in Singapore after graduation</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The <strong>NUS International Undergraduate Scholarship</strong> is the National University of Singapore\u2019s flagship award for outstanding international freshmen. It is a university-level, merit-based scholarship open to citizens of <strong>all countries except Singapore</strong> who are applying for admission to a full-time undergraduate degree programme at NUS \u2014 including Double Degree and Joint Degree programmes (coverage applies to the undergraduate portion). Transfer applicants from local or overseas universities are not eligible.</p>
<p>The defining feature: <strong>there is no separate scholarship application</strong>. Every eligible international applicant is considered automatically through the undergraduate admission application, and shortlisted candidates are invited for scholarship selection interviews.</p>
<h2 id="benefits">What the scholarship pays</h2>
<ul>
<li><strong>100% coverage of subsidised undergraduate tuition fees</strong> \u2014 i.e. the tuition that remains after the MOE Tuition Grant \u2014 for the normal candidature period, transferable across programmes.</li>
<li><strong>S$5,800 annual living allowance.</strong></li>
<li><strong>S$5,000 annual accommodation allowance.</strong></li>
<li><strong>S$1,750 one-time computer allowance</strong> upon enrolment.</li>
</ul>
<p>"Subsidised" is doing real work in that first bullet: the scholarship sits on top of the MOE Tuition Grant (see below), which is why the combined package is genuinely close to full funding.</p>
<h2 id="moe">The MOE Tuition Grant \u2014 read this carefully</h2>
<p>The scholarship itself carries <strong>no bond</strong>. But recipients <strong>must take up the MOE Tuition Grant</strong> to receive the scholarship \u2014 and the grant does carry an obligation: international students (and Singapore PRs) who accept it must <strong>work for a Singapore-registered company for three years immediately after graduation</strong>. Separate, longer service obligations apply to Medicine and Dentistry. Go in with your eyes open: this is a superb deal if you are happy to start your career in Singapore, and a deal-breaker if you are not.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Nationality:</strong> citizens of all countries except Singapore (Singapore Permanent Residents have a separate route).</li>
<li><strong>Study level:</strong> applying for admission to a full-time undergraduate degree programme at NUS (first degree).</li>
<li><strong>Academics:</strong> outstanding high-school results.</li>
<li><strong>Beyond grades:</strong> strong leadership qualities and potential, plus an outstanding co-curricular activities record.</li>
<li><strong>Not eligible:</strong> transfer applicants from local or overseas universities.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>Because consideration is automatic, the "scholarship documents" are your <strong>admission application documents</strong>, which vary by qualification route (Indian Class XII, IB, A-Levels, etc.):</p>
<ul>
<li>Academic transcripts and certificates for your qualifying examinations.</li>
<li>Passport / identification documents.</li>
<li>Records of co-curricular activities, leadership roles and achievements.</li>
<li>Any additional documents the NUS admissions portal requests for your qualification group.</li>
<li>Shortlisted candidates should be ready for a <strong>scholarship selection interview</strong>.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Check your qualification route\u2019s window:</strong> AY2027/28 undergraduate applications open <strong>16 December 2026</strong>; international-qualification windows close in <strong>mid-February 2027</strong> (the exact date depends on your qualification).</li>
<li><strong>Submit the NUS undergraduate admission application</strong> through the official Office of Admissions portal before your route\u2019s deadline \u2014 this single application doubles as your scholarship application.</li>
<li><strong>Make the application strong on leadership and CCA</strong>, not just grades \u2014 the scholarship explicitly rewards both.</li>
<li><strong>Watch for the interview invitation</strong> if you are shortlisted.</li>
<li><strong>If offered, accept the MOE Tuition Grant</strong> as part of the package \u2014 the scholarship cannot be held without it.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is there really no separate scholarship form?','Correct. The official NUS page states that candidates "will be considered and shortlisted for the scholarship through their application for undergraduate admission to NUS." One application covers both.'),
 ('Is the scholarship bonded?','The scholarship itself has no bond \u2014 but you must take up the MOE Tuition Grant, and that grant obliges international recipients to work for a Singapore-registered company for three years after graduation.'),
 ('What does the scholarship not cover?','It covers subsidised tuition plus the stated allowances. Anything outside the normal candidature period, or costs beyond the allowances, is on you \u2014 and the award cannot be combined with another scholarship without the university\u2019s prior approval (per the published terms).'),
 ('Can I apply for Medicine or Dentistry?','You can apply for admission, but note that Medicine and Dentistry carry separate, longer service obligations under the MOE framework \u2014 check the official pages for those programmes specifically.'),
 ('When exactly does my window close?','It depends on your qualification: the main international-qualification window closes in mid-February 2027 (reported as 17 February 2027 for international qualifications; other routes differ). Confirm your exact date on the NUS admissions site.'),
 ('I am a Singapore Permanent Resident \u2014 is this for me?','No. This scholarship is for international students; PRs have separate NUS scholarship routes (e.g. the ASEAN Undergraduate Scholarship).'),
]),
 verify='Verified 18 Oct 2026 against the official NUS page "NUS International Undergraduate Scholarship" (nus.edu.sg: eligibility \u2014 citizens of all countries except Singapore; strong leadership; outstanding CCA record; outstanding high-school results; full-time UG degree; transfer applicants ineligible; benefits \u2014 100% subsidised tuition after MOE Tuition Grant, S$5,800 living, S$1,750 computer, S$5,000 accommodation; automatic consideration via the admission application; no bond on the scholarship itself but the mandatory MOE Tuition Grant carries a 3-year Singapore work obligation). AY2027/28 window (opens 16 Dec 2026, closes mid-Feb 2027, date varies by qualification) per Laplace Apply and Collegedunia admission trackers. Not confused with the Singapore-citizen-only NUS Global Merit Scholarship.',
 offlinks=[('NUS International Undergraduate Scholarship \u2014 official page','https://www.nus.edu.sg/oam/scholarships/scholarships-for-freshmen-(international-students)/nus-international-undergraduate-scholarship')],
 related_titles=['iuj','gks2027','science-tokyo'],
))


if __name__ == '__main__':
    ok = 0
    for a in ARTICLES:
        assert a['slug'] not in [x['slug'] for x in ARTICLES[:ok]], a['slug'] + ' duplicated'
        sz = build_article(BASE, OUT, a, CARDINFO)
        ok += 1
        print('built', a['slug'], sz, 'bytes')
    import html.parser as hp
    for a in ARTICLES:
        path = OUT / (a['slug'] + '.html')
        src = path.read_text()
        p = hp.HTMLParser(); p.feed(src)
        for bad in ('AICTE Pragati', 'Lorem'):
            if bad in src:
                raise AssertionError((a['slug'], 'leftover', bad))
        print('validated', a['slug'])

#!/usr/bin/env python3
"""Batch 17 (cron run 17): 5 verified articles. Verified 18 Oct 2026.

Notes:
- Italy guide: route-by-route guide for 2026-27. 2026/27 calls for MAECI, IYT,
  Padua, Bologna, SNS are CLOSED (closed Mar-May 2026); DSU Toscana PhD window
  (25 Sep - 16 Nov 2026) and EDISU Piemonte PhD window (28 Oct - 27 Nov 2026)
  are open; Polimi 2027-28 merit call is live (form by 15 Dec 2026). No
  "guaranteed fully funded" framing - DSU/EDISU amounts vary by ISEE bracket.
- GKS-U 2027: official NIIED 2027 guidelines. Embassy Track closed 30 Sep 2026;
  University Track open Sep-Nov 2026 per university. Framed for the open
  University Track; graduate (GKS-G 2027) marked not yet published.
- KAUST VSRP: live year-round rolling (vsrp.kaust.edu.sa), $1,000/mo + airfare
  + housing. Visa/insurance not on the official benefits list - omitted.
- OECD Internship: current vacancy window closes 31 Dec 2026; rolling. Framed
  as a paid allowance (EUR 1,000/mo), NOT a scholarship; no travel/insurance.
- EM GLOBED: Edition XI closed; article written for Edition 2027-2029 (call
  details due Nov 2026) as a preparation guide. Official consortium:
  UAB / Bremen / Cyprus / Glasgow.
SKIPPED this run (15): GMP 2026 (closed 20 Feb 2026); JINR START Summer 2026
(closed 2 Mar 2026); HIAS 2027/28 call (closed 2 Mar 2026); Jiangnan CSC 2026
(closed 20 Feb 2026); Rotary Peace 2027-28 (closed 15 May 2026); YTB-IsDB 2026
(closed 20 Feb 2026); Latvia 2026/27 (closed 1 Apr 2026); Australia Awards 2027
intake (closed 30 Apr 2026, 2028 dates not announced); UNESCO WH 2027 (closed
28 Feb 2026); Paris-Saclay 2026 (closed 31 Mar 2026, 2027-28 call not
published); McCain 2026 (closed 15 Mar 2026, no 2027 call); Dubai Business
Associates 12th cohort (closed 1 Mar 2026, 13th not announced); British Council
Women in STEM 2026-27 (closed, 2027-28 not announced); Sakharov 2026 (closed
15 Feb 2026); Fudan STEM Elite 2026 (closed 28 Feb 2026).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'italy-guide': dict(mono='IT', title='How to Get Fully Funded Scholarships in Italy 2026-27', href='how-to-get-fully-funded-scholarships-in-italy-2026-27.html',
              dpill='16 Nov 2026 · 29 days to go', award='€10,800 (MAECI) · €10k + waiver (Polimi) · €8k + waiver (Padua) · regional grants', elig='International students; routes by merit or financial need; some windows open now.',
              tags=[('Guide','blue'),('Italy','teal')]),
 'gks2027': dict(mono='GKS', title='Korean Government GKS Scholarship 2027 in Korea (Fully Funded)', href='korean-government-gks-scholarship-2027-korea.html',
              dpill='University Track open — check each university', award='₩1.13M–1.2M/month + tuition (up to ₩5M/sem) + airfare', elig='Under 25; non-Korean; 80%+/CGPA 2.64+; Embassy Track closed 30 Sep 2026.',
              tags=[("Undergraduate",'blue'),('South Korea','teal')]),
 'kaust-vsrp': dict(mono='KAUST', title='KAUST VSRP Internship Program 2026 in Saudi Arabia (Fully Funded)', href='kaust-vsrp-internship-program-2026-saudi-arabia.html',
              dpill='Rolling — apply anytime', award='$1,000/month + round-trip airfare + on-campus housing', elig='3rd-year+ bachelor’s / master’s in STEM; GPA 3.5/4.0; strong English.',
              tags=[('Research internship','blue'),('Saudi Arabia','teal')]),
 'oecd': dict(mono='OECD', title='OECD Internship Program 2026 in France (Paid Internship)', href='oecd-internship-program-2026-france.html',
              dpill='31 Dec 2026 · 74 days to go', award='€1,000/month living contribution; 1–6 months in Paris', elig='Enrolled bachelor’s/master’s/PhD; fluent English or French.',
              tags=[('Internship','blue'),('France','teal')]),
 'globed': dict(mono='GL', title='Erasmus Mundus GLOBED Scholarship 2027 in Europe (Fully Funded)', href='erasmus-mundus-globed-scholarship-2027.html',
              dpill='2027–2029 call info due Nov 2026', award='€1,400/month × 2 years + insurance (up to 24 awards)', elig='180-ECTS bachelor’s in education/social sciences; IELTS 7.0/TOEFL 90.',
              tags=[("Master's",'blue'),('Europe','teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 1. Italy guide
ARTICLES.append(dict(
 slug='how-to-get-fully-funded-scholarships-in-italy-2026-27',
 title='How to Get Fully Funded Scholarships in Italy 2026-27 | StudyDesk Scholarships',
 meta='Nine verified routes to study in Italy with full or near-full funding for 2026-27: MAECI government grants, Invest Your Talent, regional DSU scholarships, and university awards at Polimi, Padua, Bologna, Bocconi and SNS.',
 short='Fully Funded Scholarships in Italy 2026-27',
 kicker="Italy · Government + Regional + University Routes",
 mono='IT', prov_short='Italy · Study in Italy', prov_cat='Country Guide · Europe',
 h1='How to Get Fully Funded Scholarships in Italy in 2026-27: The 9 Verified Routes',
 sub='Italy is one of the few European countries where international students can genuinely study on a full grant in 2026-27 — but the money is spread across government, regional and university schemes with very different rules. This guide maps the nine verifiable routes, states honestly which 2026-27 calls are already closed and which are still open, and lists exactly what each one pays.',
 dpill='16 Nov 2026 · 29 days to go', dl_long='Several 2026-27 deadlines. Still open now: DSU Toscana PhD window (25 Sep – 16 Nov 2026) and EDISU Piemonte PhD window (28 Oct – 27 Nov 2026); Politecnico di Milano 2027-28 merit call — scholarship form by 15 Dec 2026. Closed for 2026-27: MAECI (26 Mar 2026), Invest Your Talent (11 May 2026), DSU/EDISU Bachelor/Master windows, Padua, Bologna, Bocconi 2026-27 rounds, SNS PhD.',
 facts=facts([('What this guide covers','9 verified routes <small>Italian government grants, regional right-to-study scholarships, and university merit awards</small>'),
              ('Typical funding','€8,000 – €12,000/year <small>Plus tuition exemptions, meals and housing on some routes — amounts vary by scheme and income bracket</small>'),
              ('Who can apply','International students <small>Routes exist for Bachelor’s, Master’s, PhD, AFAM and research programmes; some are country-restricted</small>'),
              ('How awards work','Merit or need <small>Government and university awards are mostly merit-based; regional DSU grants are need-based via an ISEE income assessment</small>'),
              ('Open windows now','PhD regional + Polimi 2027-28 <small>DSU Toscana PhD to 16 Nov 2026; EDISU Piemonte PhD 28 Oct – 27 Nov 2026; Polimi scholarship form by 15 Dec 2026</small>'),
              ('Provider','Italian institutions <small>MAECI, Invest Your Talent, regional DSU/EDISU agencies, and partner universities</small>')]),
 body='''<h2 id="about">The honest picture for 2026-27</h2>
<p>Italy does not have one big "fully funded" national scholarship that covers everything. Instead, funding comes in three layers: <strong>government grants</strong> (MAECI and Invest Your Talent), <strong>regional right-to-study scholarships</strong> (DSU/EDISU agencies, which can combine cash, free meals and housing), and <strong>university merit awards</strong> (Polimi, Padua, Bologna, Bocconi, SNS). Be cautious of trackers that list these as always-open "fully funded" awards — as of October 2026 most 2026-27 calls have closed, so this guide separates what is still open from what to prepare for in 2027-28.</p>
<h2 id="routes">The 9 verified routes</h2>
<h3>1. MAECI Italian Government Scholarships (2026/27)</h3>
<p>The Ministry of Foreign Affairs' official programme paid <strong>€10,800 over 9 months</strong> for 2026/27 (three instalments), plus health insurance and a tuition/enrolment fee exemption at participating universities — you still pay the regional tax of about €140 plus stamp duty. Eligibility: Master's (under 28), PhD (under 30) or AFAM/research (under 40), with B2-level English or Italian, studying on-site. The 2026/27 call <strong>closed 26 March 2026</strong>; the next call typically opens in January–February 2027. Ignore trackers quoting €9,000 or a May 2026 deadline — both are wrong.</p>
<h3>2. Invest Your Talent in Italy (2026/27)</h3>
<p>A combined scholarship-plus-internship route: <strong>€1,200/month for 9 months</strong> from 1 October 2026, tuition exemption, and a mandatory internship with Italian companies. It does <strong>not</strong> cover travel or accommodation, and it cannot be combined with any other Italian public scholarship. Open to bachelor's graduates under 28 with B2 English from 23 partner countries, including India. The 2026/27 call <strong>closed 11 May 2026</strong>.</p>
<h3>3. DSU Toscana regional scholarships (2026/27) — PhD window still open</h3>
<p>Tuscany's right-to-study agency offers cash grants of up to about <strong>€6,800 plus tuition exemption, free canteen meals and accommodation</strong>, scaled to your income bracket (ISEE/ISPE) and whether you live at home, commute or are off-site. The Bachelor's/Master's window closed 7 September 2026, but the <strong>PhD/specialisation window runs 25 September – 16 November 2026 — still open</strong>. International students must convert family income documents into an ISEE Parificato at a CAF centre after arriving in Italy, with sworn translations and apostille/legalisation.</p>
<h3>4. EDISU Piemonte (Turin) 2026/27 — PhD window still open</h3>
<p>Piedmont's agency supports students at the University of Turin, Politecnico di Torino and the University of Eastern Piedmont with roughly <strong>€1,873–€8,097/year</strong> depending on ISEE bracket and residency, plus free meals and possible housing for off-site students. The Bachelor's/Master's window closed 4 September 2026; the <strong>PhD/specialisation window opens 28 October and closes 27 November 2026</strong>. First-year students must earn 20 university credits (CFU) by 10 August 2027 to receive the second half of the grant.</p>
<h3>5. Politecnico di Milano merit scholarships — 2027-28 call live</h3>
<p>Polimi offers international Master's students a <strong>full tuition waiver</strong> (winners pay only about €170 in admin fees), with top-ranked awardees receiving <strong>up to €10,000/year gross</strong> on top (Platinum/Gold tiers). The 2026/27 call is over, but the <strong>2027-28 call is now live</strong>: apply for MSc admission between 1 October and 1 December 2026, then submit the separate scholarship form via Polimi Online Services by <strong>15 December 2026, 12:00 Italian time</strong>. Note that most tiers are waiver-only — the cash allowance is for top awardees, and the grant can be combined with DSU Lombardia.</p>
<h3>6. University of Bologna — Unibo Action 1 + Action 2</h3>
<p>Bologna's route for first-year international students has two branches: <strong>Action 1 (100% tuition waiver)</strong> and <strong>Action 2 (a study grant of about €11,000 gross/year)</strong> — you cannot hold both. They require applicants under 30 with SAT (Bachelor's) or GRE (Master's) scores. Bologna's separate International Talents @Unibo (€6,500/year + full tuition exemption, 30 awards) closed 30 May 2026 for 2026/27; the 2027-28 call is not yet published.</p>
<h3>7. Bocconi Merit Awards (2026/27)</h3>
<p>Bocconi awards top-profile first-year Bachelor's and Master's applicants a <strong>full tuition waiver worth roughly €12,000–14,000/year, plus possible free accommodation</strong> in Bocconi residences, renewable on academic progress. Consideration is automatic — no separate application; awards follow the admission rounds. Do not confuse these merit awards with Bocconi's need-based ISU support, which is a separate income-based scheme.</p>
<h3>8. University of Padua — International Excellence Scholarship</h3>
<p>Padua's excellence scheme offers <strong>€8,000/year plus a full tuition-fee waiver</strong> for up to 2 years (Master's) or 3 years (Bachelor's), with about 69 Excellence and 30 departmental awards; only the regional tax and stamp duty remain payable. Open to non-Italian citizens not resident in Italy. The 2026/27 calls ran February–May 2026 and are closed; the next intake is expected to open around late February 2027.</p>
<h3>9. Scuola Normale Superiore PhD positions (2026-27, 42nd cycle)</h3>
<p>SNS Pisa offers PhD positions with a <strong>PhD scholarship plus free accommodation and free canteen meals</strong>, open to all nationalities. Eligibility requires a Master's obtained no earlier than 5 years before the call deadline (or to be obtained by 31 October 2026) and no prior Italian PhD. The 2026/27 sessions closed in early 2026; the new 2027-28 call is expected in early 2027.</p>
<h2 id="eligibility">Eligibility at a glance</h2>
<ul>
<li><strong>Age limits:</strong> MAECI under 28 (Master's)/under 30 (PhD)/under 40 (research); IYT under 28; Bologna under 30; Padua none stated; Polimi and SNS rules vary by call.</li>
<li><strong>Language:</strong> B2 English or Italian for MAECI and IYT; English-taught programmes at Polimi, Padua and Bologna require the university's standard English evidence.</li>
<li><strong>Country rules:</strong> IYT is restricted to citizens of 23 partner countries including India; regional DSU grants and most university awards are open to all nationalities.</li>
<li><strong>Income:</strong> regional DSU/EDISU grants are means-tested — you need documented family income and assets converted to an ISEE Parificato; merit awards ignore income.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<ul>
<li>Valid passport/ID and degree certificate plus transcripts with grades.</li>
<li>Europass CV, motivation letter, and English B2 certificate (IYT also asks for a 59-second motivation video and a one-page CV).</li>
<li>SAT/GRE for Bologna's Unibo Actions; research project proposal for SNS PhD (max 20,000 characters).</li>
<li>For regional DSU grants: family income, bank-balance, property and household-composition certificates with sworn Italian translations plus apostille or consular legalisation, then an ISEE Parificato from a CAF centre.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Pick your route first:</strong> government (MAECI/IYT), regional DSU, or university merit — the portals and timelines are completely separate, and IYT cannot be combined with other public aid.</li>
<li><strong>Apply to the university in parallel:</strong> several routes (Padua, Bocconi) assess you automatically on admission; Polimi and SNS need separate scholarship steps.</li>
<li><strong>Register on the right portal:</strong> studyinitaly.esteri.it for MAECI, the IYT application portal for Invest Your Talent, DSU Toscana's Student Help Desk or EDISU Piemonte's online sportello for regional grants.</li>
<li><strong>For DSU grants, prepare the income paperwork early:</strong> get 2024 tax-year family documents translated, legalised and converted to ISEE Parificato before the PhD windows close (16 Nov / 27 Nov 2026).</li>
<li><strong>Submit before the call's exact time:</strong> Italian calls use Italian time (CET) — Polimi's 15 December 2026 form closes at 12:00 Italian time.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Are any Italian 2026-27 scholarship calls still open in October 2026?','Yes, two: the DSU Toscana PhD/specialisation window (until 16 November 2026) and the EDISU Piemonte PhD window (28 October – 27 November 2026). The Politecnico di Milano 2027-28 merit call is also live (scholarship form by 15 December 2026). All other 2026-27 calls listed in this guide are closed.'),
 ('Is DSU Toscana a guaranteed full scholarship?','No. It is a need-based regional grant: the cash portion (up to about €6,800) depends on your ISEE income bracket and living arrangement, and first-year students must earn 20 credits by 10 August 2027 to get the second half. Meals, tuition exemption and housing add real value, but nothing is guaranteed.'),
 ('Do I need Italian to study on these scholarships?','Not necessarily. MAECI accepts B2 English or Italian, and Polimi, Padua, Bologna and Bocconi all run English-taught programmes. IYT requires B2 English. Regional DSU applications can be done in Italian or with translated documents.'),
 ('Can I combine Invest Your Talent with a regional scholarship?','No. IYT is explicitly incompatible with any other Italian public scholarship, so choose one route.'),
 ('Does the MAECI grant cover flights to Italy?','The official 2026/27 MAECI terms cover a €10,800 grant over 9 months, health insurance and tuition exemption — travel to Italy is not listed among the covered items.'),
 ('How far in advance should I prepare for the 2027-28 calls?','Start now: gather and legalise family income documents for DSU, prepare English certificates, and watch the Polimi 2027-28 call (live now) plus Padua and SNS, whose 2027-28 calls are expected around late February / early 2027.'),
]),
 verify='Verified 18 Oct 2026 against official pages: studyinitaly.esteri.it and esteri.it network announcements (MAECI 2026/27 €10,800, closed 26 Mar 2026), conscalcutta.esteri.it (Invest Your Talent 2026/27), dsu.toscana.it (PhD window 25 Sep – 16 Nov 2026), edisu.piemonte.it (PhD window 28 Oct – 27 Nov 2026), Politecnico di Milano 2027-28 merit call (form by 15 Dec 2026), bandi.unibo.it (Unibo Action 1/2), unibocconi.it (Bocconi Graduate Merit Awards 2026-27), University of Padua English scholarship pages, sns.it (42nd-cycle PhD call). Stale/wrong tracker figures (€9,000 MAECI, "guaranteed" DSU sums) deliberately omitted.',
 offlinks=[('MAECI scholarships portal (studyinitaly.esteri.it)','https://studyinitaly.esteri.it'),
           ('DSU Toscana 2026/27 calls','https://www.dsu.toscana.it'),
           ('EDISU Piemonte 2026/27 calls','https://www.edisu.piemonte.it/en'),
           ('Bocconi Graduate Merit Awards 2026-27','https://www.unibocconi.it/en/applying-bocconi/master-science-and-ma-programs/funding/bocconi-graduate-merit-awards-ay-2026-27'),
           ('Scuola Normale Superiore PhD admission competition','https://www.sns.it/en/phd-admission-competition')],
 related_titles=['daad','eiffel','each'],
))

# ---------------------------------------------------------------- 2. GKS-U 2027
ARTICLES.append(dict(
 slug='korean-government-gks-scholarship-2027-korea',
 title='Korean Government GKS Scholarship 2027 in Korea (Fully Funded) | StudyDesk Scholarships',
 meta='GKS-U 2027 (Korean Government Scholarship, undergraduate): ₩1.2 million/month, full tuition and airfare. Embassy Track closed 30 Sep 2026 — University Track is still open through November 2026. Eligibility and how to apply.',
 short='Korean Government GKS Scholarship 2027',
 kicker="South Korea · Undergraduate · Fully Funded",
 mono='GKS', prov_short='National Institute for International Education (NIIED)', prov_cat='Government of Korea',
 h1='Korean Government GKS Scholarship 2027: Fully Funded Undergraduate Study in Korea',
 sub='The 2027 Korean Government Scholarship for undergraduate degrees (GKS-U 2027) is now running under NIIED\u2019s official guidelines. The Embassy Track closed on 30 September 2026, but the University Track stays open through November 2026 with each university setting its own deadline — so this article is written for applicants who can still apply. It covers the exact award, eligibility, the seven official forms, and the mistakes aggregators make about this scheme.',
 dpill='University Track open — check each university', dl_long='Embassy Track: 15 – 30 September 2026 (closed). University Track: September – November 2026 — deadlines are set by each participating university, so confirm the date on your chosen university\u2019s announcement. The graduate GKS-G 2027 guidelines have not been published yet (expected around February).',
 facts=facts([('Award','₩1,200,000/month <small>₩1,130,000/month during the 1-year Korean language programme; the monthly allowance is all-inclusive — living, housing, insurance</small>'),
              ('Tuition & airfare','Full tuition + round-trip airfare <small>Tuition up to ₩5,000,000/semester paid by NIIED (the university covers any excess); one economy round-trip ticket</small>'),
              ('Eligibility','Under 25, non-Korean <small>Born on/after 1 Mar 2002; neither applicant nor parents may hold Korean citizenship; graduating high school by 31 Dec 2026</small>'),
              ('Academic bar','80%+ or CGPA 2.64/4.0+ <small>One of: 80%+ on a 100-point scale, top 20% of class, or CGPA ≥ 2.64/4.0, 2.80/4.3, 2.91/4.5, 3.23/5.0</small>'),
              ('Quota','286 awards <small>Embassy Track 156 (incl. 61 regional R-GKS); University Track 130 (UIC programme 100 + associate 30)</small>'),
              ('Provider','NIIED <small>National Institute for International Education, Ministry of Education, Korea</small>')]),
 body='''<h2 id="about">About the GKS-U 2027 cycle</h2>
<p>The Global Korea Scholarship undergraduate cycle for 2027 entry (GKS-U 2027) was announced by NIIED in September 2026. It funds bachelor's and associate degrees plus one year of Korean language training. There are two application tracks: the <strong>Embassy Track</strong> (apply via your country's Korean embassy, choosing up to 3 universities) and the <strong>University Track</strong> (apply directly to one university and one department). Because the Embassy Track closed on 30 September 2026, this page focuses on the <strong>University Track, which remains open through November 2026</strong> — but each university sets its own deadline, so check your chosen university's notice now.</p>
<h2 id="benefits">Benefits (official 2027 guidelines)</h2>
<ul>
<li><strong>Monthly allowance:</strong> ₩1,130,000/month during the 1-year Korean language programme and <strong>₩1,200,000/month</strong> during the degree — explicitly "all-inclusive": it bundles living expenses, accommodation, health insurance, settlement costs, TOPIK fees and completion grants. Do not believe trackers quoting ₩900,000/month (outdated) or separate settlement/medical figures (they are folded into the allowance in 2027).</li>
<li><strong>Tuition:</strong> full tuition up to ₩5,000,000 per semester paid by NIIED; the host university covers any amount above that, plus the admission fee.</li>
<li><strong>Korean language training:</strong> 1 year fully funded (₩5,200,000/year); TOPIK Level 5–6 holders skip it and receive proficiency grants.</li>
<li><strong>Airfare:</strong> one round-trip economy ticket — not provided if you already reside in Korea at the final announcement or enter from a country other than your own.</li>
<li><strong>Duration:</strong> bachelor's 5–7 years (language year + degree); associate degree 3–4 years.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Nationality:</strong> citizen of an NIIED-invited country; neither you nor your parents may hold Korean citizenship (dual holders of Korean nationality are ineligible). The UIC programme under the University Track is open to all countries.</li>
<li><strong>Age:</strong> under 25 — born on or after <strong>1 March 2002</strong>.</li>
<li><strong>Education:</strong> graduated, or expected to graduate by <strong>31 December 2026</strong>, from high school; bachelor's-degree holders cannot apply; graduates of Korean high schools/international schools are ineligible.</li>
<li><strong>Grades:</strong> at least one of 80%+ on a 100-point scale, top 20% of class, or CGPA ≥ 2.64/4.0 (equivalents for 4.3, 4.5, 5.0 scales listed officially).</li>
<li><strong>Language:</strong> no mandatory TOPIK/IELTS at application; TOPIK Level 3+ earns bonus points, as do science/engineering applicants.</li>
<li><strong>Disqualifications:</strong> previous Korean government degree-scholarship recipients cannot apply; duplicate applications across tracks cancel your candidacy.</li>
</ul>
<h2 id="documents">Documents required</h2>
<p>NIIED's official checklist requires <strong>seven forms</strong>: Application Form, Personal Statement, Study Plan, Recommendation Letter (issued within 1 year of the deadline, from a principal or teacher), GKS Applicant Agreement, Personal Medical Assessment, and Consent to Collect and Use Personal Information. Plus: proof of citizenship for you and your parents with family-relationship proof, high school graduation certificate (or expected-graduation certificate with a stated date), transcripts, optional TOPIK/English score reports and up to 5 award/activity certificates. Round 1 is scanned uploads; round 2 requires one original set with apostille or consular confirmation.</p>
<h2 id="how">How to apply (University Track)</h2>
<ol class="steps-list">
<li><strong>Pick ONE university and ONE department:</strong> unlike the Embassy Track, the University Track allows only a single university/department application.</li>
<li><strong>Find that university's deadline:</strong> the track runs September–November 2026, but each university sets its own date — check its international admissions notice immediately.</li>
<li><strong>Prepare the seven NIIED forms</strong> plus citizenship, graduation and transcript documents listed above.</li>
<li><strong>Apply through the university's channel</strong> as stated in its GKS-U 2027 announcement (the Embassy Track used studyinkorea.go.kr; the University Track follows each university).</li>
<li><strong>Track the rounds:</strong> 1st-round results arrive in November 2026 (university), 2nd round (NIIED review) in December, final announcement expected <strong>7 January 2027</strong>; entry to Korea starts around March 2027.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Can I still apply for GKS-U 2027?','The Embassy Track closed on 30 September 2026. The University Track is still open (September–November 2026), but each university sets its own deadline — apply through your chosen university\u2019s announcement now. The graduate cycle (GKS-G 2027) guidelines have not been published yet.'),
 ('Is accommodation free?','No. The official 2027 guidelines do not promise free accommodation — housing is covered inside the all-inclusive monthly allowance (₩1.13M during language training, ₩1.2M during the degree). Treat "free dormitory" claims as aggregator invention.'),
 ('Do I need TOPIK or IELTS?','Not mandatory at application. But TOPIK Level 3+ earns bonus evaluation points, and science/engineering applicants get an extra bonus. English proficiency reports are optional supporting documents.'),
 ('What are the monthly allowance figures I should trust?','The official 2027 NIIED figures: ₩1,130,000/month during the language programme and ₩1,200,000/month during the degree. The widely quoted ₩900,000/month is an outdated figure from older cycles — do not use it.'),
 ('Can I apply through both tracks?','No. Duplicate applications across tracks or programmes lead to cancellation of your candidacy. If you failed Embassy Track round 1, you may re-apply through the University Track.'),
 ('Is there a separate settlement allowance?','Not in 2027. Settlement, medical insurance and proficiency grants are folded into the all-inclusive monthly allowance — separate figures on aggregator sites are carried over from older cycles.'),
]),
 verify='Verified 18 Oct 2026 against the official NIIED GKS-U 2027 Application Guidelines PDF via the Study in Korea portal (monthly allowance ₩1,130,000/₩1,200,000 all-inclusive, tuition cap ₩5,000,000/semester, quota 286, age born on/after 1 Mar 2002, seven official forms, Embassy Track 15–30 Sep 2026, University Track Sep–Nov 2026, final results 7 Jan 2027), plus the Korean Cultural Centre South Africa GKS-U 2027 call. GKS-G 2027 graduate guidelines not yet published — marked as such in-article.',
 offlinks=[('Study in Korea — GKS notices','https://www.studyinkorea.go.kr/en/plan/scholarship.do'),
           ('Official GKS-U 2027 guidelines PDF (NIIED)','https://www.studyinkorea.go.kr/cmm/fms/FileDown.do?atchFileId=FILE_000000000673717&fileSn=1'),
           ('Korean Cultural Centre SA — GKS-U 2027 call','http://sa.korean-culture.org/en/1356/board/1050/read/148115')],
 related_titles=['knu','science-tokyo','each'],
))

# ---------------------------------------------------------------- 3. KAUST VSRP
ARTICLES.append(dict(
 slug='kaust-vsrp-internship-program-2026-saudi-arabia',
 title='KAUST VSRP Internship Program 2026 in Saudi Arabia (Fully Funded) | StudyDesk Scholarships',
 meta='KAUST VSRP: a fully funded 2–6 month research internship in Saudi Arabia. $1,000/month stipend, round-trip airfare and housing. Open year-round with rolling applications — eligibility, benefits and how to apply.',
 short='KAUST VSRP Internship Program 2026',
 kicker="Saudi Arabia · Research Internship · Fully Funded",
 mono='KAUST', prov_short='King Abdullah University of Science and Technology', prov_cat='University · Saudi Arabia',
 h1='KAUST VSRP Internship Program 2026: Fully Funded Research in Saudi Arabia',
 sub='The King Abdullah University of Science and Technology\u2019s Visiting Student Research Program (VSRP) is a fully funded 2–6 month research internship on KAUST\u2019s campus at Thuwal, Saudi Arabia — with a $1,000 monthly stipend, round-trip airfare and on-campus housing. Unlike most schemes on this site, it runs year-round with rolling applications and no fixed deadline. This page covers the official benefits, the 3.5/4.0 GPA bar, and the one-project-at-a-time application process.',
 dpill='Rolling — apply anytime', dl_long='No fixed deadline — the VSRP accepts applications year-round on a rolling basis with flexible start and end dates. Apply well before your preferred start date; decisions are issued as they are made.',
 facts=facts([('Award','$1,000/month stipend <small>Plus private on-campus bedroom and bathroom, round-trip airfare, and social and cultural activities; no application fee</small>'),
              ('Duration','2 – 6 months <small>Most projects run 3–6 months; flexible start and end dates, on-site at KAUST Thuwal</small>'),
              ('Eligibility','STEM undergrads & master\u2019s <small>3rd year or above of a bachelor\u2019s, or enrolled in a master\u2019s in a STEM field; strong English</small>'),
              ('Academic bar','GPA 3.5/4.0+ <small>Minimum GPA of 3.5/4.0 (or 14/20 ECTS B equivalent); recommended English TOEFL iBT 79 or IELTS 6.0–6.5 — you may apply without a test score</small>'),
              ('Projects','100+ active <small>Choose one faculty-led research project across KAUST\u2019s STEM disciplines; only one application at a time</small>'),
              ('Provider','KAUST <small>King Abdullah University of Science and Technology, Saudi Arabia</small>')]),
 body='''<h2 id="about">About the VSRP</h2>
<p>The Visiting Student Research Program at KAUST places you inside a faculty-led research project for 2–6 months (most projects run 3–6 months), with access to core laboratories and major research and community facilities. With 100+ active projects across STEM fields and flexible start dates, it is one of the few genuinely rolling, fully funded research internships in the world — and the official page confirms it is accepting applications now.</p>
<h2 id="benefits">Benefits (official)</h2>
<ul>
<li><strong>USD $1,000 monthly stipend</strong> — paid during the internship.</li>
<li><strong>Round-trip airfare</strong> to and from KAUST.</li>
<li><strong>On-campus housing:</strong> a private bedroom and bathroom (the official wording — not a full apartment).</li>
<li><strong>Social and cultural activities</strong> and access to core laboratories and community facilities.</li>
<li><strong>No application fee.</strong></li>
</ul>
<p><em>Note: some third-party listings claim visa fees and health insurance as VSRP benefits, but these do not appear on the current official benefits page — they are not stated officially and are omitted here. The official page also does not promise tuition coverage or a furnished apartment.</em></p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Degree:</strong> 3rd year or above of a bachelor's programme, or currently enrolled in a master's programme, in a STEM field. Students who graduated within one year of the internship start date are also eligible.</li>
<li><strong>Grades:</strong> minimum GPA of <strong>3.5/4.0</strong> (or 14/20 ECTS B equivalent).</li>
<li><strong>English:</strong> strong verbal and written English; official materials recommend around TOEFL iBT 79 or IELTS 6.0 (some newer sources quote 6.5 — confirm the current minimum on the official page). You may apply <strong>without</strong> an English test score; official scores are only required if your application succeeds. Exemptions apply for in-person degrees from the US, Canada, UK, Ireland, Australia or New Zealand.</li>
<li><strong>Not eligible:</strong> current PhD candidates, current KAUST students, and KAUST alumni.</li>
<li><strong>Passport:</strong> valid for at least 6 months.</li>
</ul>
<h2 id="documents">Documents required</h2>
<ul>
<li>Official transcripts in English (current and previous institutions).</li>
<li>One faculty recommendation — KAUST contacts your recommender through the portal; you do not upload the letter yourself.</li>
<li>Valid passport; CV and statement of purpose as listed by the project/portal.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Browse the research project listings</strong> on vsrp.kaust.edu.sa and choose <strong>one</strong> project aligned with your background — only one application to KAUST at a time.</li>
<li><strong>Apply online</strong> through the KAUST admissions portal and upload your documents.</li>
<li><strong>Faculty review:</strong> complete applications are reviewed, and shortlisted candidates may be contacted by the faculty member for a Zoom interview about their research background.</li>
<li><strong>Admissions interview:</strong> progressed candidates have a second Zoom interview with the Office of Admissions (about life at KAUST).</li>
<li><strong>Acceptance:</strong> approved candidates receive an email acceptance letter, and a travel advisor assists with relocation.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is there a deadline for the KAUST VSRP?','No fixed deadline. The programme runs year-round on a rolling basis with flexible start and end dates, so you can apply any time. Because selection is ongoing, apply well before your preferred start date.'),
 ('Does the VSRP cover visa and health insurance?','These appear on some third-party listings, but the current official benefits page lists only the stipend, housing, airfare, activities and lab access — so visa and insurance are not stated officially and should not be counted on.'),
 ('What English score do I need?','Official KAUST materials describe recommended levels (TOEFL iBT 79 or IELTS around 6.0–6.5); newer sources quote IELTS 6.5 overall. You can apply without a test score — official scores are only required if your application succeeds.'),
 ('Can PhD students or KAUST alumni apply?','No. Current PhD candidates, current KAUST students and KAUST alumni are explicitly not eligible.'),
 ('How much does the internship pay?','A USD $1,000 monthly stipend, plus round-trip airfare and private on-campus housing with bathroom.'),
 ('Can I apply to multiple projects?','No. The official process allows only one application to KAUST at a time — pick the single project that best matches your background.'),
]),
 verify='Verified 18 Oct 2026 against the live official pages at vsrp.kaust.edu.sa (programme page + internships FAQ: $1,000/month stipend, private bedroom and bathroom, round-trip airfare, social/cultural activities, lab access, no application fee; eligibility: 3rd-year+ bachelor\u2019s / master\u2019s in STEM, GPA 3.5/4.0, recommended TOEFL iBT 79 or IELTS 6.0; rolling year-round applications; one application at a time; PhD candidates, current KAUST students and alumni ineligible). Visa/insurance benefits claimed by third-party listings are not on the official page and are omitted.',
 offlinks=[('KAUST VSRP programme page','https://vsrp.kaust.edu.sa/')],
 related_titles=['oecd','epfl-summer','each'],
))

# ---------------------------------------------------------------- 4. OECD Internship
ARTICLES.append(dict(
 slug='oecd-internship-program-2026-france',
 title='OECD Internship Program 2026 in France (Paid Internship) | StudyDesk Scholarships',
 meta='OECD Internship Programme in Paris: €1,000/month for 1–6 months, open to all nationalities of enrolled students. Current vacancy window closes 31 Dec 2026. Eligibility, documents and how to apply.',
 short='OECD Internship Program 2026',
 kicker="France · Internship · Paid",
 mono='OECD', prov_short='Organisation for Economic Co-operation and Development', prov_cat='International Organisation · France',
 h1='OECD Internship Program 2026: A Paid Internship in Paris',
 sub='The OECD Internship Programme places enrolled students inside the Organisation\u2019s Paris headquarters for 1–6 months (renewable to 12), supporting policy analysts with research, data work and event support. It pays a €1,000/month living-expense contribution — it is a paid internship, not a scholarship. The current vacancy window closes 31 December 2026, and recruitment is rolling, so early applications have the advantage.',
 dpill='31 Dec 2026 · 74 days to go', dl_long='The current programme-level vacancy closes 31 December 2026; a new vacancy is then published. Recruitment is rolling year-round — apply well before your preferred start date, since the selection process can take up to three months.',
 facts=facts([('Award','€1,000/month <small>Living-expense contribution per full calendar month worked (Paris-based interns); 2.5 days annual leave per full month; not a salary, not a scholarship</small>'),
              ('Duration','1 – 6 months <small>Normally full-time (40 hrs/week); renewable up to 12 months total; part-time (20 hrs/week) only in exceptional cases</small>'),
              ('Location','Paris, France <small>Mainly at OECD headquarters; in-person, hybrid or fully remote depending on the hiring team\u2019s needs</small>'),
              ('Eligibility','Enrolled students, all nationalities <small>Full-time bachelor\u2019s, master\u2019s or PhD enrolment for the internship\u2019s entire duration; fluent English or French</small>'),
              ('Deadline','31 Dec 2026 (rolling) <small>Current vacancy closes 31 December 2026; candidates not contacted within six months may update and reapply</small>'),
              ('Provider','OECD <small>Organisation for Economic Co-operation and Development</small>')]),
 body='''<h2 id="about">About the programme</h2>
<p>OECD interns work alongside policy analysts or in corporate functions: preparing studies, collecting and analysing data, drafting notes and technical annexes, attending meetings and supporting events. Internships are primarily allocated to nationals of OECD member countries, but <strong>non-member-country nationals are also eligible</strong> for specific programmes and projects — including affiliated bodies such as the IEA, NEA, FATF and ITF.</p>
<h2 id="benefits">What you get (official)</h2>
<ul>
<li><strong>€1,000/month</strong> contribution to living expenses per full calendar month worked (Paris-based interns).</li>
<li><strong>2.5 days of annual leave</strong> per full month worked (for internships longer than 2 full-time months), plus OECD-observed French public holidays.</li>
<li>The allowance can be paid to bank accounts inside or outside the Eurozone — a French bank account is not mandatory.</li>
</ul>
<p><em>Honest limits, straight from the official FAQ: the OECD does <strong>not</strong> reimburse travel to or from Paris, public transport, or accommodation, and provides <strong>no medical insurance</strong> — interns must show proof of their own insurance before starting. Ignore aggregator pages inflating this into a "fully funded scholarship."</em></p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Enrolment:</strong> full-time enrolment in an accredited degree programme (bachelor's, master's or PhD) for the <strong>entire duration</strong> of the internship, in a field related to OECD work. Online or non-degree programmes are not recognised. (Some aggregators claim "graduated within 12 months" — this is not stated on the official page.)</li>
<li><strong>Availability:</strong> at least one month; four or more months encouraged.</li>
<li><strong>Languages:</strong> excellent command of one OECD official language (English or French), plus working knowledge of — or willingness to learn — the other.</li>
<li><strong>Skills:</strong> good quantitative and IT skills, drafting and communication skills, and the ability to thrive in a multicultural team.</li>
<li><strong>Nationality:</strong> majority of places go to OECD member-country nationals; non-member nationals eligible for specific programmes and projects.</li>
</ul>
<h2 id="documents">Documents required</h2>
<ul>
<li>Online application with personal data and academic/work history (at least one entry each under Experience and Education), plus eligibility screening questions.</li>
<li>Résumé attached; a cover letter in the "Message to Hiring Manager" box (max 4,000 characters) covering motivation, contribution and career goals.</li>
<li>Before taking up duty: passport copy, proof of full-time enrolment, proof of medical insurance, visa/work permit if applicable, and bank details.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply online</strong> on the OECD careers platform (SmartRecruiters) before the current vacancy closes on <strong>31 December 2026</strong>.</li>
<li><strong>Write a strong 4,000-character cover letter</strong> explaining your motivation, what you would contribute, and your career goals — this is the main document the hiring teams read.</li>
<li><strong>Wait for shortlisting:</strong> the Internship Office pre-screens and shares shortlists with Directorates; only shortlisted candidates are contacted.</li>
<li><strong>Interview/test:</strong> hiring teams may invite shortlisted candidates to an interview and/or a written test.</li>
<li><strong>Sign the agreement:</strong> selected candidates sign a tripartite internship agreement (OECD + intern + university). The OECD does not sign universities' own agreement templates.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is the OECD internship fully funded?','No. It is a paid internship with a €1,000/month living-expense contribution — not a salary and not a scholarship. Travel to Paris, accommodation, transport and medical insurance are not covered.'),
 ('Can non-OECD-country nationals apply?','Yes, for specific programmes and projects — though most places go to member-country nationals. Affiliated bodies like the IEA, NEA, FATF and ITF also host interns.'),
 ('Do I need to be a current student?','Yes. The official requirement is full-time enrolment in an accredited degree programme for the internship\u2019s entire duration. Online and non-degree programmes are not recognised.'),
 ('Can the internship be remote?','It depends on the hiring team\u2019s needs — the official page lists in-person, hybrid and fully remote arrangements.'),
 ('When should I apply?','The current vacancy closes 31 December 2026 and recruitment is rolling, with selection taking up to three months — apply as early as possible before your preferred start date.'),
 ('Is the €1,000 paid every month?','It is paid per full calendar month worked, for Paris-based interns. The FAQ for the Trento Centre lists a different figure (€982.26) — that is a separate centre; use €1,000 for the Paris programme.'),
]),
 verify='Verified 18 Oct 2026 against the official OECD internship pages (oecd.org/en/about/careers/internships.html and the official Internship FAQ PDF: €1,000/month contribution for Paris-based interns, 1–6 months renewable to 12, 2.5 days leave per month, no travel/accommodation/insurance reimbursement; eligibility: full-time enrolment for the internship\u2019s duration, fluent English or French; current SmartRecruiters vacancy closes 31 Dec 2026; rolling recruitment). "Graduated within 12 months" and "fully funded scholarship" aggregator claims deliberately not repeated.',
 offlinks=[('OECD internships programme page','https://www.oecd.org/en/about/careers/internships.html'),
           ('OECD Internship FAQ (official PDF)','https://www.oecd.org/content/dam/oecd/en/about/careers/internship/OECD-Internship-FAQS.pdf'),
           ('OECD internship application portal','https://careers.smartrecruiters.com/OECD/internships---en')],
 related_titles=['kaust-vsrp','epfl-summer','anz-summer'],
))

# ---------------------------------------------------------------- 5. GLOBED 2027
ARTICLES.append(dict(
 slug='erasmus-mundus-globed-scholarship-2027',
 title='Erasmus Mundus GLOBED Scholarship 2027 in Europe (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus GLOBED 2027–2029 (Education Policies for Global Development): €1,400/month for 2 years across Barcelona, Bremen, Cyprus and Glasgow. Next call details due November 2026 — how to prepare now.',
 short='Erasmus Mundus GLOBED Scholarship 2027',
 kicker="Europe · Master's · Fully Funded",
 mono='GL', prov_short='Erasmus Mundus GLOBED (UAB)', prov_cat='European Union · Master\u2019s',
 h1='Erasmus Mundus GLOBED Scholarship 2027: €1,400/Month Across Four Universities',
 sub='GLOBED — the Erasmus Mundus Joint Master in Education Policies for Global Development — is a 2-year, 120-ECTS master\u2019s taught across the Universitat Autònoma de Barcelona, the University of Bremen, the University of Cyprus and the University of Glasgow. The 2026 (Edition XI) scholarship call is closed; the official site states the Edition 2027–2029 call details will be published in November 2026. This page is written as an honest preparation guide for that next call: the real award terms, the official eligibility bar, and the documents to start assembling now.',
 dpill='2027–2029 call info due Nov 2026', dl_long='The Edition XI (2026–2028) scholarship call (12 Jan – 12 Feb 2026) is closed. The Edition 2027–2029 call details will be published in November 2026 — expected to follow the same pattern (open around November/January, closing early/mid-February). Prepare your documents now; do not treat aggregator-projected 2027 dates as official.',
 facts=facts([('Award','€1,400/month × 2 years <small>Up to 24 Erasmus Mundus scholarships per edition; covers subsistence, mobility, installation, registration at all four universities, and worldwide health insurance</small>'),
              ('Programme','120 ECTS, 4 semesters <small>Barcelona → Bremen → Cyprus → Glasgow; 10 self-funded places also available per edition</small>'),
              ('Eligibility','180-ECTS bachelor\u2019s + C1 English <small>Bachelor\u2019s (min 180 ECTS) in education or related social sciences; IELTS 7.0 (writing ≥6.5) / TOEFL 90 (writing ≥24) / Cambridge C1</small>'),
              ('Grades','7/10 or GPA 2.75/4 <small>Minimum 7 out of 10 (or equivalent C) or GPA 2.75/4.0</small>'),
              ('Special-needs awards','2 reserved <small>Two scholarships reserved for students with special needs, with additional support available</small>'),
              ('Provider','GLOBED consortium <small>UAB (coordinator, Spain), Bremen (Germany), Cyprus, Glasgow (UK); co-funded under Erasmus+ 2023–2029</small>')]),
 body='''<h2 id="about">About GLOBED</h2>
<p>GLOBED is the Erasmus Mundus Joint Master in Education Policies for Global Development, run by four universities: the <strong>Universitat Autònoma de Barcelona</strong> (coordinator), the <strong>University of Bremen</strong>, the <strong>University of Cyprus</strong>, and the <strong>University of Glasgow</strong>. Students spend four semesters across the consortium studying how education policy shapes global development. The programme has secured Erasmus+ funding for the 2023–2029 period, and its scholarship calls follow the standard Erasmus Mundus Joint Masters terms.</p>
<h2 id="benefits">Benefits (official Finance page)</h2>
<ul>
<li><strong>€1,400/month for the full 2-year programme</strong> for all scholarship holders, regardless of residence or nationality.</li>
<li>Covers subsistence, mobility and installation costs, <strong>registration at all four universities</strong>, and <strong>worldwide health insurance</strong>.</li>
<li><strong>Up to 24 Erasmus Mundus scholarships</strong> per edition, including regional scholarships and two reserved for students with special needs (with additional support available).</li>
<li>10 self-funded places per edition are also available (participation costs include registration and 24-month insurance).</li>
</ul>
<h2 id="eligibility">Eligibility (official)</h2>
<ul>
<li><strong>Degree:</strong> bachelor's in Educational Sciences or a relevant field (preferably Sociology, Social/Cultural Anthropology, Political Sciences, Human Geography, International Relations), lasting at least 3 years = <strong>180 ECTS minimum</strong>.</li>
<li><strong>Grades:</strong> minimum <strong>7/10</strong> (or equivalent C) or GPA <strong>2.75/4.0</strong>.</li>
<li><strong>English (SELT only, exact official figures):</strong> TOEFL ≥ 90 (writing ≥ 24), Cambridge Advanced Certificate ≥ C1, or IELTS Academic ≥ 7.0 with ≥ 6.0 in each element and ≥ 6.5 in writing. Waivers are possible for eligible profiles — check the official English-language list. (Some trackers quote IELTS 5.5 / TOEFL 72 — wrong; the official figures above apply.)</li>
<li><strong>Nationality:</strong> open to <strong>all nationalities</strong>; prior EMJM scholarship recipients are barred under standard EMJM rules.</li>
</ul>
<h2 id="documents">Documents to prepare now</h2>
<ul>
<li>Valid passport; <strong>Europass CV</strong> (other formats are not accepted).</li>
<li>Bachelor's diploma plus transcripts with ECTS/hours and grades (original language, with English or Spanish translations); final-year students may submit transcripts only.</li>
<li>Official English certificate (or waiver/late-submission form) meeting the exact thresholds above.</li>
<li><strong>Motivation letter</strong> (maximum 1 page, Times New Roman 11, 1.5 spacing) — a strict format; prepare it to spec.</li>
<li>A PDF with contact details of <strong>two recommenders</strong> (letters are not accepted — they are contacted only if you are shortlisted).</li>
<li>Erasmus Sworn Declaration (scholarship applicants only). All PDFs ≤ 4 MB.</li>
</ul>
<h2 id="how">How the application works (from the official how-to-apply page)</h2>
<ol class="steps-list">
<li><strong>Wait for the November 2026 update:</strong> the Edition 2027–2029 call details (including the exact deadline) will be published on globed.eu in November 2026. Scholarship and self-funded calls are separate windows with separate appeal periods.</li>
<li><strong>Obtain a UAB ID number</strong> (via web01.uab.es) and select "MU Erasmus Mundus in Education Policies for Global Development" in the UAB application portal once the window opens.</li>
<li><strong>Fill in details and upload documents</strong> in the formats above, then download the confirmation document (no confirmation email is sent — keep the downloaded copy).</li>
<li><strong>Track appeals:</strong> scholarship and self-funded calls each have their own appeal periods (for Edition XI these ran late April and late May–June respectively).</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is the GLOBED 2027 application open?','Not yet. The official site says the Edition 2027–2029 call details will be published in November 2026. The Edition XI (2026–2028) scholarship call closed on 12 February 2026. Use this page to prepare your documents now.'),
 ('What exactly does the scholarship pay?','€1,400 per month for the full 2 years, covering subsistence, mobility, installation, registration at all four consortium universities and worldwide health insurance — up to 24 scholarships per edition.'),
 ('What English score is really required?','The official requirement is strict: IELTS Academic 7.0 (≥6.0 each element, ≥6.5 writing), TOEFL 90 (writing ≥24), or Cambridge Advanced C1. Aggregator claims of IELTS 5.5 / TOEFL 72 are wrong.'),
 ('Do I write an essay on a Board-set topic?','No — a "short essay on an Academic Board topic" appears only on aggregator sites and is not in the official how-to-apply list. The official writing requirement is the 1-page motivation letter in the exact specified format.'),
 ('Can self-funded students also apply?','Yes — 10 self-funded places per edition are available through a separate call window (Edition XI ran 13 Feb – 15 May 2026).'),
 ('Which universities will I study at?','The current consortium is UAB (Barcelona, coordinator), Bremen (Germany), Cyprus, and Glasgow (UK) — four semesters across the programme. Earlier editions included Oslo and Malta, but the current list applies.'),
]),
 verify='Verified 18 Oct 2026 against the official globed.eu pages (homepage, admission-selection, how-to-apply, Finance): Edition XI scholarship call 12 Jan – 12 Feb 2026 closed; Edition 2027–2029 call details due November 2026; award €1,400/month × 2 years, up to 24 scholarships incl. 2 special-needs, all four universities\u2019 registration + insurance; eligibility: 180-ECTS bachelor\u2019s, 7/10 or 2.75/4.0, IELTS 7.0/TOEFL 90/Cambridge C1; documents: Europass CV only, 1-page motivation letter to spec, two recommender contacts. Wrong tracker figures (IELTS 5.5, Board essay, 2026 applications "open") deliberately omitted.',
 offlinks=[('GLOBED official homepage','https://globed.eu/'),
           ('Admission & selection (official)','https://globed.eu/admission-selection/'),
           ('How to apply (official)','https://globed.eu/how-to-apply/')],
 related_titles=['emabg','each','eiffel'],
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
        for bad in ('AICTE Pragati', 'Lorem', '#'):
            if bad in src:
                raise AssertionError((a['slug'], 'leftover', bad))
        print('validated', a['slug'])

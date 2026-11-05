#!/usr/bin/env python3
"""Batch 20b (cron run 20, 18 Oct 2026): articles 4–5 — Erasmus Mundus GEM and DENSYS 2027.

4. Erasmus Mundus GEM Scholarship 2027 (Geo-Information Science and Earth
   Observation for Environmental Modelling and Management). 2027-2029 intake:
   applications 1 Oct 2026 – 15 Jan 2027 (23:59 CET), automatic scholarship
   consideration. ~17-18 scholarships: full tuition + insurance + EUR 1,400/mo
   x 24 months. Coordinator University of Twente (ITC); partners Lund,
   UCLouvain, Tartu. 4 tracks with mobility pairings; double degree.
   Eligibility: 180-ECTS bachelor's, First Class/Upper Second (2.1; 2.2
   rejected), university in Webometrics top 10,000; English test before the
   deadline (IELTS 6.5 / 6.0 per section per multiple sources). Documents per
   official apply page incl. 2-page GEM CV template rule; no motivation or
   reference letters. Recorded interview gates the scholarship. Verified
   directly on gem-msc.eu (apply page, finances page, homepage).
5. Erasmus Mundus DENSYS Scholarship 2027 (Decentralized Smart Energy Systems).
   2027 intake: applications 12 Oct 2026 – 27 Jan 2027 (KTH official page);
   EUR 1,400/mo x 24 months + participation costs covered (tuition, insurance,
   summer schools, Liège immersive week). Coordinator Université de Lorraine
   (Nancy); semester-3 tracks at KTH Stockholm / Politecnico di Torino / UPC
   Barcelona; double degree. Eligibility: engineering bachelor's (mechanical/
   aeronautical, chemical, electrical, energy) or 180-credit technical degree
   with required courses; effectively CGPA 3.0/4.0; English TOEFL iBT 92 or
   IELTS 6.5. Documents: Europass CV, 1-page motivation letter, 3-5 min video,
   notarised degree/transcripts, 2 referee-uploaded letters, photo, ID, English
   cert. Apply on eMundus. Verified on densys.univ-lorraine.fr + KTH page.
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'gem2027': dict(mono='GE', title='Erasmus Mundus GEM Scholarship 2027 (Fully Funded)', href='erasmus-mundus-gem-scholarship-2027.html',
              dpill='15 Jan 2027 · 89 days to go', award='€1,400/month × 24 months + full tuition + insurance (~17–18 awards)', elig='180-ECTS bachelor’s, First Class/2.1; English test before deadline; all nationalities.',
              tags=[('Master’s', 'blue'), ('Europe', 'teal')]),
 'densys2027': dict(mono='DE', title='Erasmus Mundus DENSYS Scholarship 2027 (Fully Funded)', href='erasmus-mundus-densys-scholarship-2027.html',
              dpill='27 Jan 2027 · 101 days to go', award='€1,400/month × 24 months + participation costs fully covered', elig='Engineering bachelor’s (180 ECTS); CGPA 3.0/4.0; English TOEFL 92 / IELTS 6.5; all nationalities.',
              tags=[('Master’s', 'blue'), ('Europe', 'teal')]),
})

ARTICLES = []

# ---------------------------------------------------------------- 4. GEM
ARTICLES.append(dict(
 slug='erasmus-mundus-gem-scholarship-2027',
 title='Erasmus Mundus GEM Scholarship 2027 (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus GEM Scholarship 2027: €1,400/month for 24 months plus full tuition and insurance for the Geo-Information Science and Earth Observation master\u2019s (2027–2029). Deadline 15 Jan 2027; applications via the University of Twente portal; ~17–18 scholarships across 4 tracks.',
 short='Erasmus Mundus GEM Scholarship 2027',
 kicker='Europe · Erasmus Mundus',
 mono='GE', prov_short='GEM Consortium (Erasmus Mundus)', prov_cat='European Union · Master\u2019s',
 h1='Erasmus Mundus GEM Scholarship 2027 (Fully Funded)',
 sub='Two years, four European universities, one of the strongest geo-science funding packages in Europe. The Erasmus Mundus GEM master\u2019s — Geo-Information Science and Earth Observation for Environmental Modelling and Management — pays about 17–18 scholars \u20ac1,400 a month for up to 24 months, covers all tuition and insurance, and awards a double degree across partners in the Netherlands, Sweden, Belgium and Estonia. The 2027–2029 intake is open now and closes 15 January 2027.',
 dpill='15 Jan 2027 · 89 days to go', dl_long='15 January 2027, 23:59 CET — the single deadline for scholarship and self-funded applicants (final certified graduation documents due 31 July 2027). Results by 31 March 2027; tuition payment 1 May 2027; programme starts September 2027.',
 facts=facts([('Award','€1,400/month × up to 24 months <small>Full tuition fee waiver + comprehensive student insurance (medical, dental, accident, liability, repatriation) paid directly by the programme; ~17–18 scholarships for the 2027–2029 intake across the four tracks</small>'),
              ('What it covers','Tuition + living + insurance <small>The monthly allowance is meant to cover accommodation, travel, visa and residence-permit costs, study materials and personal expenses — travel and visa costs are NOT paid separately, and there is no family/partner support</small>'),
              ('Who it is for','180-ECTS bachelor\u2019s holders <small>First Class or Upper Second (2.1) or equivalent — 2.2 does not qualify; degree from a university ranked in the Webometrics top 10,000; all nationalities; no age limit; final-year students may apply with expected-graduation proof</small>'),
              ('How scholarships work','Automatic <small>No separate scholarship application: complete applications submitted before the deadline are automatically considered. Recorded online interview for roughly the top 25 per track (Feb–Mar) — only interviewed applicants remain eligible for the scholarship</small>'),
              ('Tracks','4 mobility paths <small>Geospatial Planner (Tartu → Twente/ITC), Analyst (Tartu → UCLouvain), Developer (Lund → Twente/ITC), Modeller (Lund → UCLouvain). One track only; it cannot be changed after admission</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>GEM</strong> — <strong>Geo-Information Science and Earth Observation for Environmental Modelling and Management</strong> — is an Erasmus Mundus Joint Master run by a four-university consortium coordinated by the <strong>University of Twente\u2019s Faculty ITC (Netherlands)</strong>, with <strong>Lund University (Sweden)</strong>, <strong>UCLouvain (Belgium)</strong> and the <strong>University of Tartu (Estonia)</strong>. It is a fully English-taught, two-year (120 ECTS) programme, co-funded by Erasmus+, that ends with a <strong>double degree</strong>: two separate degree certificates, one from each host university.</p>
<p>A naming warning: this is <strong>not</strong> the separate Erasmus Mundus \u201cMSc in Geospatial Technologies\u201d run by NOVA Lisbon, M\u00fcnster and Jaume I — a distinct programme with its own call. Confirm you are on gem-msc.eu before applying.</p>
<p>The scholarship structure is the standard Erasmus Mundus package at its most generous: roughly 17–18 scholarships for this intake, covering the whole two years, with selection that is academic first — a recorded online interview gates the final scholarship list.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>\u20ac1,400 per month for up to 24 months</strong> (maximum \u20ac33,600), paid to the scholar.</li>
<li><strong>Full tuition fee waiver</strong> and <strong>comprehensive student insurance</strong> — emergency assistance, medical and dental, accidents, social and medical repatriation, liability, legal assistance, home contents and luggage — paid directly by the programme.</li>
<li>The monthly allowance is intended to cover accommodation, travel, visa and residence-permit costs, study materials, a laptop and personal expenses. <strong>Budget carefully:</strong> travel and visa costs are not paid separately, and the scholarship does <strong>not</strong> cover a spouse or family.</li>
<li><strong>No application fee.</strong></li>
<li>The programme includes an internship within the two years and a common one-week joint event after year one.</li>
</ul>
<p>Note the capacity constraint the consortium publishes: up to 100 candidates can be provisionally admitted per track, but <strong>a maximum of 8 students per track can ultimately enrol</strong> — the interview round is the real bottleneck.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Degree:</strong> a bachelor\u2019s degree equivalent to at least <strong>180 ECTS or three years</strong> of full-time study in a discipline related to the course — geography, geoinformatics, GIS, remote sensing, environmental/earth sciences, ecology, agriculture, forestry, planning, civil/environmental engineering, computer science or data science.</li>
<li><strong>Grade:</strong> <strong>First Class or Upper Second (2.1) or equivalent</strong> — a 2.2 does not qualify and there are no waivers. Country-specific minimum grades also apply.</li>
<li><strong>University standing:</strong> your degree must come from a <strong>recognised university ranked in the top 10,000 of the Webometrics Ranking</strong>.</li>
<li><strong>Final-year students:</strong> may apply with a university letter confirming status and expected graduation plus the current transcript; the final degree and transcript must be uploaded by <strong>31 July 2027</strong>.</li>
<li><strong>English:</strong> the test must be completed <strong>before the 15 January 2027 deadline</strong> — results obtained afterwards are not accepted. Multiple independent sources citing the consortium\u2019s requirements give <strong>IELTS Academic 6.5 overall with at least 6.0 in each section</strong>, with alternatives including TOEFL iBT, Cambridge C1 Advanced/C2 Proficiency, PTE Academic and LANGUAGECERT Academic. Country exemptions exist for some English-speaking countries. An English-medium-instruction certificate alone is not enough unless your country is on the exempted list.</li>
<li><strong>Nationality:</strong> open worldwide; no age limit; work experience not required. The standard Erasmus+ mobility rule applies — your two study countries must differ from your country of residence at enrolment.</li>
<li>Previous Erasmus Mundus scholarship recipients are ineligible for a second GEM award.</li>
<li>You apply to <strong>one track only</strong>, and the track cannot be changed after admission. For the Developer and Modeller tracks, at least 15 ECTS in GIS/remote sensing is strongly recommended.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>The official apply page is precise — and unusually, it is a list of what to bring <em>and what not to</em>:</p>
<ul>
<li>Bachelor\u2019s degree certificate (First Class or Upper Second or equivalent), official transcripts, certified English translations where applicable; additional degree certificates/transcripts if applicable.</li>
<li>Valid <strong>English-language test certificate</strong> (test completed before the deadline).</li>
<li>Copy of a <strong>valid passport</strong>.</li>
<li><strong>CV in the official GEM CV template, maximum 2 pages</strong> — the wrong template or an over-length CV makes the application inadmissible.</li>
<li>Financial-information fields completed in the form <strong>in euros</strong> — no separate financial-plan document or proof of funds is required.</li>
<li><strong>Not required:</strong> motivation letter, reference letters, or a provisional research topic. <strong>Do not upload unrequested documents.</strong></li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Check eligibility</strong> on the official Admission and Eligibility page — including the grade rule, the Webometrics top-10,000 rule and the English-test-before-deadline rule.</li>
<li><strong>Pick one track</strong> (Planner, Analyst, Developer or Modeller) and study its year-1/year-2 mobility pairing.</li>
<li><strong>Prepare all documents first</strong> — including the CV in the official 2-page GEM template and your English test results.</li>
<li><strong>Submit through the online application portal</strong> (run by the University of Twente) by <strong>15 January 2027, 23:59 CET</strong>.</li>
<li><strong>If shortlisted:</strong> the recorded online interview (roughly the top 25 per track, February–March) is the gateway to the scholarship — only interviewed applicants remain eligible.</li>
<li><strong>Await the ranking</strong> — outcomes: admitted with scholarship, provisionally admitted without scholarship (possible reserve list), or not admitted.</li>
</ol>
<p>Key 2027 dates from the official apply page: portal opened 1 October 2026 → deadline 15 January 2027 → results 31 March 2027 → tuition payment 1 May 2027 → final certified graduation documents 31 July 2027 → programme starts September 2027.</p>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('What does GEM stand for?','Geo-Information Science and Earth Observation for Environmental Modelling and Management — an Erasmus Mundus Joint Master coordinated by the University of Twente\u2019s Faculty ITC, with Lund, UCLouvain and Tartu. It is distinct from the separate Erasmus Mundus MSc in Geospatial Technologies (NOVA Lisbon / M\u00fcnster / Jaume I).'),
 ('How much is the GEM scholarship?','\u20ac1,400 per month for up to 24 months, plus a full tuition waiver and comprehensive insurance. Travel, visa and family costs are not paid separately — they come out of the monthly allowance.'),
 ('Do I need a separate scholarship application?','No. Applicants who submit a complete application before the deadline are automatically considered for an Erasmus Mundus Joint Master Scholarship. No separate form exists.'),
 ('Is a motivation letter or references required?','No — the official FAQ explicitly says motivation letters, reference letters and provisional research topics are not required, and you should not upload unrequested documents.'),
 ('What is the minimum grade?','First Class or Upper Second (2.1) or equivalent, from a university in the Webometrics top 10,000. A 2.2 does not qualify and there are no waivers.'),
 ('When must I take my English test?','It must be completed before the 15 January 2027 application deadline — results obtained after the deadline are not accepted.'),
 ('How many scholarships are available?','About 17–18 for the 2027–2029 intake across the four tracks (70 across four intakes overall), with a possible limited regional allocation per European Commission funding provisions.'),
 ('Do I get two degrees?','Yes — a double degree: two separate English-language degree certificates, one from each host university.'),
]),
 verify='Verified 18 Oct 2026 against the official consortium site gem-msc.eu — the apply page (deadline 15 Jan 2027 23:59 CET, eligibility, documents incl. the 2-page GEM CV template rule, automatic scholarship consideration, interview gate, 2027 timeline), the finances page (~17–18 scholarships for 2027–2029, \u20ac1,400/month \u00d7 24 months, full tuition + insurance), and the homepage (four tracks and mobility pairings, double degree, co-funding by Erasmus+). The IELTS 6.5/6.0-per-section figure and the accepted alternative tests are consistent across multiple independent sources citing the consortium\u2019s requirements and are used with that framing. The exact DreamApply portal URL was not captured from the official pages — the article directs readers to the official apply page instead of printing a link.',
 offlinks=[('GEM — official consortium site','https://www.gem-msc.eu'),
           ('Apply to GEM — official apply page','https://www.gem-msc.eu/apply-to-gem/'),
           ('Finances — scholarship details','https://www.gem-msc.eu/apply-to-gem/finances/')],
 related_titles=['meta40','globed','eiffel'],
))

# ---------------------------------------------------------------- 5. DENSYS
ARTICLES.append(dict(
 slug='erasmus-mundus-densys-scholarship-2027',
 title='Erasmus Mundus DENSYS Scholarship 2027 (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus DENSYS Scholarship 2027: €1,400/month for 24 months plus fully covered participation costs for the Decentralized Smart Energy Systems master\u2019s. Deadline 27 Jan 2027 via eMundus. Engineering bachelor\u2019s, all nationalities.',
 short='Erasmus Mundus DENSYS Scholarship 2027',
 kicker='Europe · Erasmus Mundus',
 mono='DE', prov_short='DENSYS Consortium (Erasmus Mundus)', prov_cat='European Union · Master\u2019s',
 h1='Erasmus Mundus DENSYS Scholarship 2027 (Fully Funded)',
 sub='A two-year energy master\u2019s across four countries with one of Europe\u2019s best funding packages. Erasmus Mundus DENSYS — Decentralized Smart Energy Systems, coordinated by the Universit\u00e9 de Lorraine in Nancy — pays scholars \u20ac1,400 a month for the full 24 months, covers all participation costs (tuition, insurance, summer schools, the Li\u00e8ge immersive week), and ends with a double degree. The 2027 intake opened 12 October 2026 and closes 27 January 2027.',
 dpill='27 Jan 2027 · 101 days to go', dl_long='27 January 2027. Applications opened 12 October 2026 (per KTH\u2019s official programme page); the two-year programme starts in September 2027. Two recommendation letters must be uploaded by your referees before you can submit — start that process early, as the consortium flags it as the main last-minute blocker.',
 facts=facts([('Award','€1,400/month × 24 months <small>Plus participation costs fully covered by the EU: tuition, health/accident insurance, lab courses, excursions, visits, two summer schools and the Li\u00e8ge immersive week. Travel, housing and living expenses are excluded from the covered costs — those come from the monthly allowance</small>'),
              ('Who it is for','Engineering graduates <small>180-ECTS bachelor\u2019s (or final-year students who will hold it by early-September enrolment) in mechanical/aeronautical, chemical, electrical or energy engineering — or another technical/natural-science degree with required courses in applied thermodynamics, heat transfer, fluid dynamics, mathematics and numerical methods. Effectively CGPA 3.0/4.0. All nationalities, no age limit</small>'),
              ('English','TOEFL iBT 92 / IELTS 6.5 <small>TOEFL iBT 92/120 with writing ≥ 22 (or 4.5/6 on the new January-2026 scale with writing ≥ 4.5); IELTS Academic 6.5 overall with writing ≥ 5.5; CAE/CPE grade C. Medium-of-instruction letters and Duolingo explicitly not accepted; waivers only in narrow published cases</small>'),
              ('How to apply','eMundus platform <small>Create an account and an application for DENSYS on eMundus; referees upload their two letters directly via an email link and must do so before you can submit. Evaluation: 100-point scoring by two reviewers, then the Admission Board assigns EMJM scholarship, partial reduction, self-funded or rejection</small>'),
              ('Mobility','Nancy → KTH / Politecnico di Torino / UPC <small>Year 1 at Universit\u00e9 de Lorraine (Nancy, France); semester-3 specialisation track at KTH Stockholm, Politecnico di Torino or UPC Barcelona; semester 4 internship or thesis — ending with a double master\u2019s degree</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p><strong>DENSYS</strong> — <strong>Decentralized Smart Energy Systems</strong> — is a two-year (120 ECTS) Erasmus Mundus Joint Master coordinated by the <strong>Universit\u00e9 de Lorraine (Nancy, France)</strong>, with <strong>KTH Royal Institute of Technology (Sweden)</strong>, <strong>Politecnico di Torino (Italy)</strong> and <strong>Universitat Polit\u00e8cnica de Catalunya (Spain)</strong>. It trains engineers for decentralised energy systems — the technologies behind the energy transition — and awards a <strong>double master\u2019s degree</strong>: from UL and the university where the third semester is completed.</p>
<p>The funding package is the standard Erasmus Mundus top tier: \u20ac1,400 a month for the full two years, with tuition and programme costs covered by the EU. Applications go through the <strong>eMundus</strong> platform, and the 2027 intake is open now.</p>
<h2 id="benefits">What the funding covers</h2>
<ul>
<li><strong>\u20ac1,400 per month for the full 2-year programme</strong> for EMJM scholarship holders.</li>
<li><strong>Participation costs fully covered by the EU:</strong> tuition fees, health and accident insurance, lab courses, excursions, visits, <strong>two summer schools</strong> (including the ESADE Barcelona business/entrepreneurship school) and the <strong>immersive week at the University of Li\u00e8ge</strong> on AI for energy networks.</li>
<li><strong>Challenge-based multidisciplinary projects</strong> and, in semester 4, an internship or master\u2019s thesis — typically with industry or research partners such as Vattenfall, Scania, the IEA, ArcelorMittal, Snam or Sener.</li>
<li>Also possible: admission with a <strong>partial scholarship</strong> (reduced participation costs, for a few students per cohort) or as a <strong>self-funded</strong> student. There is a published cost-of-living breakdown per country (updated March 2026) on the official fees page to help self-funded applicants budget.</li>
<li><strong>No published travel or installation allowance figure</strong> — participation costs explicitly <em>exclude</em> travel, housing and living expenses, which come from the monthly allowance. Any site quoting a separate travel/installation sum for this call is inventing it.</li>
</ul>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Degree:</strong> a bachelor\u2019s degree (or final-year status — you must hold the degree by enrolment in early September) in <strong>science, engineering, or a technical bachelor\u2019s in mechanical/aeronautical, chemical, electrical, or energy engineering</strong>. Other 180-credit technical or natural-science degrees are accepted only with the required courses: <strong>applied thermodynamics, heat transfer, fluid dynamics, mathematics, numerical methods</strong>.</li>
<li><strong>Grades:</strong> effectively <strong>CGPA 3.0/4.0</strong> — below that the requirements \u201cmay be assessed as not fulfilled.\u201d</li>
<li><strong>English (official page):</strong> TOEFL iBT <strong>92/120 with writing ≥ 22</strong> (or 4.5/6 on the new January-2026 scale with writing ≥ 4.5); <strong>IELTS Academic 6.5 overall with writing ≥ 5.5</strong>; CAE/CPE grade C (B2 First/FCE not accepted). A waiver applies only to students instructed in English for at least 60 ECTS during their bachelor\u2019s from the EU/EEA, Switzerland, listed English-speaking countries or listed African countries. <strong>Medium-of-instruction letters and Duolingo are explicitly not accepted.</strong></li>
<li><strong>Nationality:</strong> open to all nationalities, no age limit. Prior EMJM scholarship recipients cannot receive a second EMJM award (they may apply as self-funded).</li>
<li><strong>Track competition warning:</strong> the consortium notes about three-quarters of applicants pick the KTH track — competition for Stockholm is the toughest.</li>
</ul>
<h2 id="documents">Documents you will need</h2>
<p>All documents in English, submitted via eMundus (per the official application page):</p>
<ul>
<li>Europass-format CV (PDF).</li>
<li>Motivation letter (maximum 1 page, 11pt).</li>
<li><strong>3–5 minute self-introduction video</strong>, shared via a link that stays accessible without login through the end of March.</li>
<li><strong>Notarised copy</strong> of your degree and transcripts — or enrolment proof plus transcripts if not yet graduated; translated and notarised if not in English.</li>
<li><strong>Two reference letters, uploaded directly by the referees via an email link</strong> — the consortium flags this as the main last-minute blocker, because you cannot submit until both letters are in.</li>
<li>Proof of employment if relevant; copy of ID card or passport; <strong>English test certificate</strong>; an ID/passport-style photo.</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Lock in your two referees first.</strong> They receive the upload link by email and must submit before you can finalize — chase this a month early, not a week.</li>
<li><strong>Prepare the document pack</strong> — Europass CV, one-page motivation letter, notarised degree/transcripts, the 3–5 minute self-introduction video, English certificate, ID and photo.</li>
<li><strong>Create an account and an application for DENSYS on eMundus.</strong> The application can be completed progressively, and everything is editable after submission <em>except referee contact details</em>.</li>
<li><strong>Pick your semester-3 track</strong> — KTH Stockholm (decentralised energy systems in a global energy system), Politecnico di Torino (Power-to-X / energy storage pathways), or UPC Barcelona (thermal energy management). Remember the KTH track draws about three-quarters of applicants.</li>
<li><strong>Submit by 27 January 2027.</strong> Evaluation: two consortium reviewers score your file out of 100 (degree/field/marks 45; references and video 20; motivation, experience and potential 25; English 10), and the Admission Board then assigns the EMJM scholarship, a partial reduction, self-funded status — or rejection. Results are emailed in early March.</li>
</ol>
<h2 id="faqs">Frequently asked questions</h2>
''' + faqs([
 ('What is the DENSYS scholarship worth?','\u20ac1,400 per month for the full two years, plus all participation costs covered by the EU: tuition, health and accident insurance, lab courses, excursions, two summer schools and the Li\u00e8ge immersive week. Travel, housing and living expenses are not covered separately — budget those from the monthly allowance.'),
 ('Which universities do I study at?','Year 1 is at the Universit\u00e9 de Lorraine in Nancy, France. For semester 3 you choose a specialisation track: KTH in Stockholm, Politecnico di Torino, or UPC in Barcelona. Semester 4 is an internship or master\u2019s thesis. You graduate with a double master\u2019s degree.'),
 ('Do I need an English test?','In almost all cases, yes: TOEFL iBT 92 (writing ≥ 22) or IELTS 6.5 overall (writing ≥ 5.5) are the published thresholds. Medium-of-instruction letters and Duolingo are explicitly not accepted; waivers apply only in narrow published cases.'),
 ('Can I apply without an engineering degree?','Only if your 180-credit technical or natural-science degree included the required courses: applied thermodynamics, heat transfer, fluid dynamics, mathematics and numerical methods. Otherwise the degree requirement will not be fulfilled.'),
 ('Is the KTH track more competitive?','Yes — the consortium itself notes that about three-quarters of applicants choose KTH Stockholm, so that track\u2019s selection is the toughest.'),
 ('When are results announced?','Results are emailed to applicants in early March, following the published evaluation pattern; the exact 2027 notification date is not published.'),
 ('Is there a parallel funding route?','The official site names the Eiffel scholarship as a parallel French-government route for candidates interested in studying in France.'),
]),
 verify='Verified 18 Oct 2026 against the official consortium site densys.univ-lorraine.fr — the application page (eligibility, English scores, all nine documents, eMundus process, referee-upload rule), the fees-and-scholarships page (\u20ac1,400/month \u00d7 24 months, participation-cost coverage, cost-of-living breakdown, partial/self-funded options, Eiffel mention) — and KTH\u2019s official programme page (application window 12 Oct 2026 – 27 Jan 2027, September 2027 start, double degree). Any travel or installation allowance figure is deliberately not published (not on the official site); the exact 2027 notification date and the number of 2027 EMJM awards are not published and are not stated as facts. The direct eMundus application URL is not printed — the article directs readers to the consortium\u2019s application page.',
 offlinks=[('DENSYS — official consortium site','https://densys.univ-lorraine.fr'),
           ('Application & admissions','https://densys.univ-lorraine.fr/application/'),
           ('Fees and scholarships','https://densys.univ-lorraine.fr/fees-and-scholarships/'),
           ('KTH programme page','https://www.kth.se/en/studies/master/decentralized-smart-energy-systems/')],
 related_titles=['meta40','globed','eiffel'],
))

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

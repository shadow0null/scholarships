#!/usr/bin/env python3
"""Batch 13 (cron run 13): 5 verified international articles. Verified 17 Oct 2026.

Notes:
- Denmark Fulbright 2027: two tracks run on different clocks. The Danish-applicant
  (Denmark->USA) student-grant deadline is 17 Feb 2027 noon and is OPEN. The
  American-applicant (USA->Denmark) 2027/28 window closed 6 Oct 2026 -- stated
  honestly instead of pretending both are open.
- EACH 2027: the official consortium page (each.ut.ee) corrects third-party blogs:
  Admission Period 2 is 1-15 Feb 2027 (not 7 Jan-5 Feb) and carries NO Erasmus
  Mundus scholarship -- scholarship consideration requires Period 1 (by 5 Jan 2027).
- Keio ADB 2027: deadline 1 Nov 2026 per all published guides; monthly stipend is
  quoted at the Japanese Government Scholarship rate -- no JPY figure published in
  verified sources, so none is stated.
- Ursinus Gateway International: $35,000/year international track; the college's
  larger domestic merit awards (e.g. Zacharias) are flagged as separate so readers
  do not confuse the figures.
- Auckland 2027: written as the scholarship family around the official 2027
  International Student Excellence Scholarship (master's, invitation route,
  25% of one year's tuition, supplementary form due 4 Nov 2026).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'fulbright-dk': dict(mono='FD', title='Denmark Fulbright Program 2027 (Fully Funded)', href='denmark-fulbright-program-2027.html',
              dpill='123 days to go', award='Grants advertised DKK 50k–100k (recent cycles; varies by grant)', elig='Danish citizens → USA (open) / Americans → Denmark (closed for 2027/28).',
              tags=[("Students & Scholars",'blue'),('Denmark','teal')]),
 'each': dict(mono='EACH', title='Erasmus Mundus EACH Scholarships 2027 in Europe', href='erasmus-mundus-each-scholarships-2027-europe.html',
              dpill='80 days to go', award='€1,400/month + participation costs (standard EMJM rate)', elig="Bachelor's with 60 ECTS chemistry; Period 1 only for scholarship.",
              tags=[("Master's",'blue'),('Europe','teal')]),
 'keio-adb': dict(mono='Keio', title='Keio University ADB Scholarship 2027 in Japan (Fully Funded)', href='keio-university-adb-scholarship-2027-japan.html',
              dpill='15 days to go', award='Full tuition + admission fee + stipend + airfare + insurance', elig='ADB borrowing-country nationals; ≤35; ≥2 yrs work experience.',
              tags=[("Master's",'blue'),('Japan','teal')]),
 'ursinus': dict(mono='UG', title='Ursinus Gateway International Scholarship 2027 in USA', href='ursinus-gateway-international-scholarship-2027-usa.html',
              dpill='15 days to go', award='$35,000/year, renewable up to 4 years', elig='First-year international undergrads; SAT 1250+/ACT 28+/GPA 3.85.',
              tags=[('Undergraduate','blue'),('USA','teal')]),
 'auckland': dict(mono='UoA', title='University of Auckland Scholarship 2027 in New Zealand', href='university-of-auckland-scholarship-2027-new-zealand.html',
              dpill='18 days to go', award="25% of one year's tuition (Excellence, master's)", elig='New international students; invitation + supplementary form by 4 Nov 2026.',
              tags=[("Bachelor's/Master's",'blue'),('New Zealand','teal')]),
})

ARTICLES = [

# ---------------------------------------------------------------- 1. Fulbright Denmark
dict(
 slug='denmark-fulbright-program-2027',
 title='Denmark Fulbright Program 2027 (Fully Funded) | StudyDesk Scholarships',
 meta="Fulbright Denmark 2027 grants for Danish students, scholars and artists heading to the USA, and Americans heading to Denmark. Danish-applicant deadline: 17 Feb 2027. Track-by-track guide.",
 short='Denmark Fulbright 2027', kicker='Denmark ⇄ USA · Students, scholars & artists',
 mono='FD', prov_short='Fulbright Denmark', prov_long='Fulbright Denmark — the binational Fulbright Commission (Fulbright Center, Copenhagen)',
 h1='Denmark Fulbright Program 2027',
 sub='Fulbright Denmark runs one of the classic two-way exchanges: Danish citizens can take grants to the United States, and Americans can take grants to Denmark. The catch that most guides bury is that the two directions run on different clocks — one is open, one has already closed for 2027/28.',
 dpill='123 days to go', dl_long='17 Feb 2027, 12:00 noon (Danish applicants — student grants for Fall 2027 / Spring 2028)',
 facts=facts([('Award','Grants (vary by award)<small>Recent Danish cycles advertised DKK 50,000–100,000; amounts differ by grant type</small>'),
              ('Two directions','Denmark ⇄ USA<small>Danish nationals → US study/research; Americans → Denmark study/research</small>'),
              ('Who','Students, scholars, artists<small>Danish: MSc/PhD, visiting scholars, artistic projects; Americans: master’s/PhD study in Denmark</small>'),
              ('Open window','Danish applicants — 17 Feb 2027<small>The American 2027/28 student window closed 6 Oct 2026</small>'),
              ('How to apply','Official portals<small>Danish applicants via the IIE Slate portal; Americans via the Fulbright U.S. Student site</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Fulbright Program</strong> is the world's best-known government-backed academic exchange, and its Danish arm — administered by the independent <strong>binational Fulbright Commission</strong> from the Fulbright Center in Copenhagen — runs grants in both directions across the Atlantic. Danish citizens can win support for graduate and postgraduate study, academic research, visiting-scholar stays, artistic and creative projects, and specialised academic exchanges in the United States. In the other direction, American students and scholars can take grants for graduate-level study and research in Denmark, including the ten-month core student grant. Beyond the money, grantees get professional advising and mentorship, entry to the global Fulbright alumni network, and the commission's advisory services in Copenhagen.</p>
      <p><strong>The honest headline:</strong> there is no single Fulbright Denmark deadline. Each grant category runs on its own clock, and for the 2027/28 cycle the two main clocks disagree. The <strong>Danish-applicant student-grant deadline is Wednesday 17 February 2027 at noon</strong> (for Fall 2027 and Spring 2028 stays) and is still open. The <strong>American-applicant 2027/28 student window closed on 6 October 2026</strong>, and the US scholar window closed on 15 September 2026 — those tracks will not reopen until the next cycle. If you are an American reading this, treat the Denmark-bound grants as a next-year plan, not a 2027 application.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Denmark → USA track:</strong> Danish citizens applying for study, research, visiting-scholar or artistic stays in the United States. The commission's guidance is aimed at graduate-level applicants — Master's and PhD students — plus established scholars and artists/musicians.</li>
        <li><strong>USA → Denmark track:</strong> American citizens applying for graduate-level study and/or research in Denmark. Applicants can apply before being accepted by a Danish university, but need a strong letter of affiliation from the Danish host institution; recent graduates and graduating seniors must attend Master's-level classes there.</li>
        <li><strong>Stay timing:</strong> the Danish-side grants expect the US stay to last at least one semester (4–6 months) and not to have begun at the time of application.</li>
        <li><strong>Category rules vary:</strong> each grant category (student, scholar, artist) carries its own eligibility and paperwork — confirm the exact rules for your category in the official application system rather than relying on a summary.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Grant funding that varies by award:</strong> recent Danish cycles have advertised grants of <strong>DKK 50,000–100,000</strong> for study or research stays, typically put toward tuition, living costs and study-related expenses. Treat published figures as the previous cycle's range, not a promise for your grant.</li>
        <li><strong>Advising and mentorship</strong> through the Fulbright Center in Copenhagen.</li>
        <li><strong>Global Fulbright alumni network</strong> — the long-run value of the award for many grantees.</li>
        <li><strong>International collaboration and cultural-engagement opportunities</strong> attached to the programme.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>The commission publishes the document list below for Danish student-grant applicants; uploads are in English through the Slate portal.</em></p>
      <ol>
        <li>Applicant commitments form (download, fill, upload)</li><li>Budget form (download, fill, upload)</li>
        <li>Two essays, max one page each: Study/Research Objective and Personal Statement</li>
        <li>CV, max two pages</li>
        <li>Academic transcripts/grades from universities</li>
        <li>Two recommendations — must be uploaded by the recommenders themselves by the deadline</li>
        <li>Official letter of acceptance/invitation (or correspondence if not yet accepted)</li>
        <li>Copy of the passport ID page</li>
        <li>PhD students: documentation from the Danish university confirming academic and financial support during the US stay</li>
        <li>Artists/musicians: relevant portfolio (photos, catalogues, performances)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick your direction first.</strong>Danish citizens heading to the USA and Americans heading to Denmark use different portals, different rules and different deadlines — make sure you are reading the guidance for your own track.</li>
        <li><strong>Danish applicants: apply through the IIE Slate portal</strong>by <strong>Wednesday 17 February 2027, 12:00 noon</strong>. Read the Danish-applicant instructions before you start — not every section of the worldwide Slate form applies to Danish applicants.</li>
        <li><strong>American applicants: use the Fulbright U.S. Student site</strong>(or your university's Fulbright process, which closes earlier). Note the 2027/28 window closed on 6 October 2026 — plan for the following cycle.</li>
        <li><strong>Get recommendations in early:</strong> referees upload directly, and a late referee means a late application. Chase them a month before the deadline, not the week of it.</li>
        <li><strong>Secure your affiliation letter early</strong>if you are heading to Denmark — the commission flags a strong host letter as a decisive document.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is 17 February 2027 the deadline for everyone?","No. That is the Danish-applicant student-grant deadline for Fall 2027 / Spring 2028. The American-applicant 2027/28 student and scholar windows closed on 6 October and 15 September 2026 respectively. Each grant category sets its own date — always check the official application system for your track."),
 ("How much funding does Fulbright Denmark give?","It varies by grant. Recent Danish cycles advertised grants of DKK 50,000–100,000 toward tuition, living and study costs. The commission describes amounts as subject to revision, so treat figures as indicative until your award letter arrives."),
 ("Can artists and musicians apply, or is it only researchers?","Artists and musicians are explicitly included on the Danish side — they apply with a portfolio of photos, catalogues or performances instead of a purely academic file."),
 ("Can I apply before I have been accepted by a US or Danish university?","On the American-to-Denmark track, yes — you may apply before acceptance, but you need a strong letter of affiliation from the Danish host institution."),
]),
 offlinks=[('Apply — Fulbright Denmark (Danish student grants, official)','https://fulbrightcenter.dk/go-to-the-us/fulbright-grants-for-danish-students/apply/'),
           ('Fulbright grants for US students — Fulbright Denmark (official)','https://fulbrightcenter.dk/grantsforamericans/fulbright-for-students/')],
 related_titles=['daad','hanns-seidel','yale-wf'],
 verify='Verified 17 Oct 2026 via the official Fulbright Denmark Apply page (Danish student-grant deadline Wed 17 Feb 2027 12:00; full document list; Slate portal route) and the official US-student page (2027/28 deadline 6 Oct 2026 — closed before publish; affiliation-letter requirement; graduate-level study rule), corroborated by independent trackers on the two-track structure and the DKK 50,000–100,000 recent grant range. Grant counts and per-grant amounts beyond the published range are not stated here.'),

# ---------------------------------------------------------------- 2. EACH
dict(
 slug='erasmus-mundus-each-scholarships-2027-europe',
 title='Erasmus Mundus EACH Scholarships 2027 in Europe (Fully Funded) | StudyDesk Scholarships',
 meta="EACH (Excellence in Analytical Chemistry) 2027: 2-year Erasmus Mundus joint master's across Estonia, Sweden, France and Finland. €1,400/month for Period-1 applicants. Scholarship deadline 5 Jan 2027.",
 short='EACH 2027', kicker='Europe · Master’s · Analytical chemistry',
 mono='EACH', prov_short='EACH Consortium', prov_long='EACH Consortium — University of Tartu (coordinator), Uppsala, UCBL Lyon 1, Åbo Akademi',
 h1='Erasmus Mundus EACH Scholarships 2027 in Europe',
 sub='EACH — Excellence in Analytical Chemistry — is a two-year Erasmus Mundus joint master’s across four European universities. The money follows a strict rule most blogs misstate: only Period 1 applications are considered for the Erasmus Mundus scholarship.',
 dpill='80 days to go', dl_long='5 Jan 2027 (Admission Period 1 — the only round considered for the Erasmus Mundus scholarship)',
 facts=facts([('Award','€1,400/month + participation costs<small>Standard Erasmus Mundus rate for the study period; tuition-waiver track covers participation costs only</small>'),
              ('Programme','2-year joint Master’s (120 ECTS)<small>Year 1: University of Tartu; Year 2: Uppsala, Lyon 1 or Åbo Akademi</small>'),
              ('Two periods','Period 1: 5 Nov 2026 – 5 Jan 2027<small>Period 2 (1–15 Feb 2027): tuition-waiver / fee-based ONLY — no scholarship</small>'),
              ('Eligibility',"Bachelor’s + 60 ECTS chemistry<small>+ 20 ECTS maths/physics; ≥66% of max grade average; English required</small>"),
              ('Decisions','By 9 April 2027<small>Applications via the EACH DreamApply system</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>EACH — Excellence in Analytical Chemistry</strong> — is an Erasmus Mundus Joint Master’s run by a four-university consortium: the <strong>University of Tartu</strong> in Estonia (coordinator), <strong>Uppsala University</strong> in Sweden, <strong>Université Claude Bernard Lyon 1</strong> in France, and <strong>Åbo Akademi University</strong> in Finland. The two-year, 120-ECTS programme starts with the first year at Tartu and continues with a second year at one of the three partner universities — the Year-2 placement is competitive, decided on your stated preference and your first-semester academic performance. The degree targets in-depth analytical chemistry: instrumental analysis, laboratory technique, measurement and data analysis, metrology and quality management, plus a mandatory internship placement with an approved international company.</p>
      <p><strong>The funding rule you must not get wrong:</strong> the consortium accepts 2027-intake applications in two periods, but they are not equal. <strong>Admission Period 1 (5 Nov 2026 – 5 Jan 2027)</strong> is open to candidates applying for the <strong>Erasmus Mundus scholarship</strong>, tuition-waiver places and fee-based places. <strong>Admission Period 2 (1 – 15 Feb 2027)</strong> is for <strong>tuition-waiver and fee-based places only — the Erasmus Mundus scholarship is not available in Period 2.</strong> If you want the funded route, Period 1 is your only shot; a Period-2 application is effectively a self-funded (or waiver-only) application. Note that several third-party blogs print a wrong Period-2 window (7 Jan – 5 Feb); the consortium's own admission page is the authority.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Bachelor’s degree (or equivalent)</strong> containing <strong>at least 60 ECTS in chemistry or chemical engineering</strong> and <strong>20 ECTS in mathematics and/or physics</strong>. These prerequisites are <strong>mandatory</strong> and are checked after you submit the full application in DreamApply — a chemistry-light degree will not clear this bar.</li>
        <li><strong>Minimum 66% of the maximum grade available</strong>, averaged across all courses on your transcript (the admissions committee handles any conversion to percentages itself).</li>
        <li><strong>English language requirements</strong> per the consortium's official language-test list — check the EACH admission page for the accepted tests, not a blog's summary.</li>
        <li>Applicants considering the <strong>Uppsala study track</strong> may face additional Swedish national requirements depending on the diploma-issuing country — read the Uppsala-specific notes on the EACH site.</li>
        <li>All nationalities may apply; note the consortium publishes specific restrictions for citizens of the Russian Federation.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Erasmus Mundus scholarship holders receive €1,400 per month</strong> for the relevant study period under the standard Erasmus+ rules, plus coverage of participation (tuition) costs.</li>
        <li>The scholarship package is designed to cover <strong>living expenses, travel, visa costs and installation costs</strong> — budget inside the monthly contribution rather than expecting separate allowances on top.</li>
        <li><strong>Tuition-waiver study places</strong> (no monthly stipend) are available in both periods for strong applicants who miss the scholarship.</li>
        <li>An <strong>internship with an approved international company</strong> is built into the curriculum — a direct pipeline into R&amp;D departments, chemical and pharmaceutical labs, and health, consumer and environmental agencies.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Bachelor’s degree certificate</li><li>Academic transcripts</li>
        <li>Curriculum Vitae (CV)</li><li>Motivation letter</li>
        <li>Proof of English language proficiency</li>
      </ol>
      <p><em>An admission test may also be required. Prepare documents before the Period-1 window opens — the 60-ECTS chemistry prerequisite is verified from your transcript after submission.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the prerequisites against your transcript first</strong>— 60 ECTS chemistry/chemical engineering plus 20 ECTS maths/physics, and the 66% average. If you do not clear these, the rest of the application is wasted effort.</li>
        <li><strong>Create an account on the EACH DreamApply application system</strong>once Period 1 opens on 5 November 2026, and upload all documents there.</li>
        <li><strong>Submit before 5 January 2027</strong>if you want Erasmus Mundus scholarship consideration — Period 2 (1–15 Feb 2027) cannot carry the scholarship.</li>
        <li><strong>Complete any admission test</strong>the consortium sets, without prohibited assistance.</li>
        <li><strong>Wait for results by 9 April 2027</strong>, announced by the consortium for both periods.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I win the Erasmus Mundus scholarship if I apply in Period 2?","No. The consortium is explicit: Period 2 (1–15 Feb 2027) is for tuition-waiver and fee-based places only. Scholarship consideration requires a Period-1 application by 5 January 2027."),
 ("What does the €1,400 per month actually cover?","It is the standard Erasmus Mundus monthly contribution for the study period, meant to cover living, travel, visa and installation costs, with participation (tuition) costs covered separately. Do not budget as if travel and visa are extra guaranteed allowances."),
 ("Where do I study each year?","Year 1 is at the University of Tartu. Year 2 is at Uppsala, Lyon 1 or Åbo Akademi, assigned competitively on your preference and first-semester results."),
 ("My degree is in a related science, not pure chemistry — can I apply?","Only if your transcript shows at least 60 ECTS in chemistry/chemical engineering and 20 ECTS in maths/physics. The prerequisite is mandatory and verified after submission, so count your credits honestly before applying."),
]),
 offlinks=[('Admission information — EACH consortium (official)','https://each.ut.ee/EACH/admission-requirements/')],
 related_titles=['emmir','glocal','daad'],
 verify='Verified 17 Oct 2026 via the official EACH consortium admission page (Period 1: 5 Nov 2026–5 Jan 2027 with scholarship; Period 2: 1–15 Feb 2027 waiver/fee-based only; 60 ECTS chemistry + 20 ECTS maths/physics; 66% grade floor; results by 9 Apr 2027; Tartu/Uppsala/Lyon 1/Åbo Akademi consortium), corroborated by independent trackers on the €1,400/month EMJM rate, the DreamApply route and the document list. The wrong Period-2 window printed by some blogs (7 Jan–5 Feb) is not used.'),

# ---------------------------------------------------------------- 3. Keio ADB
dict(
 slug='keio-university-adb-scholarship-2027-japan',
 title='Keio University ADB Scholarship 2027 in Japan (Fully Funded) | StudyDesk Scholarships',
 meta="Keio University ADB–Japan Scholarship 2027: full tuition, admission fee, monthly stipend, health insurance and airfare for master's students from ADB borrowing countries. Deadline 1 Nov 2026.",
 short='Keio ADB 2027', kicker='Japan · Master’s · ADB–Japan Scholarship Program',
 mono='Keio', prov_short='Keio University', prov_long='Keio University, Tokyo (Asian Development Bank–Japan Scholarship Program)',
 h1='Keio University ADB Scholarship 2027 in Japan',
 sub='Keio is one of Japan’s designated universities for the ADB–Japan Scholarship Program: full master’s funding for development-minded professionals from ADB borrowing countries. There is no standalone scholarship form — you enter through Keio’s graduate admission.',
 dpill='15 days to go', dl_long='1 Nov 2026 (published application closing date for the 2027 intake)',
 facts=facts([('Award','Fully funded (ADB-JSP)<small>Full tuition + admission fee remission, monthly stipend, health insurance, round-trip airfare</small>'),
              ('Level & duration',"Master’s, up to 2 years<small>Four eligible graduate schools: Science & Technology, Economics, System Design & Management, Business & Commerce</small>"),
              ('Who','ADB borrowing-country nationals<small>Bachelor’s + strong record; ≥2 years post-degree work experience; ≤35 at application</small>'),
              ('Key condition','Return-home commitment<small>Scholars agree to return and contribute to their home country’s development</small>'),
              ('Deadline','1 Nov 2026<small>Published closing date across guides; apply via Keio graduate admission</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Asian Development Bank–Japan Scholarship Program (ADB-JSP)</strong> funds postgraduate study for citizens of ADB borrowing member countries, and <strong>Keio University</strong> — Japan's oldest private university, based in Tokyo — is one of its designated host institutions. The award is aimed squarely at working professionals: it wants people with a degree, a strong academic record, and at least two years of full-time professional experience, who will return home after the master's and put the training to work for their country's development. Four Keio graduate schools take ADB-JSP scholars: <strong>Science and Technology</strong>, <strong>Economics</strong>, <strong>System Design and Management</strong>, and <strong>Business and Commerce</strong>.</p>
      <p><strong>How the route works:</strong> you do not apply for the scholarship as a standalone award. You apply for admission to a Keio master's programme in one of the eligible schools during the application window (roughly September–November), and admitted candidates are considered for the ADB-JSP nomination through the admission process. An application fee applies to the admission application and cannot be waived.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>national of an ADB borrowing member country</strong> (nationals of countries that no longer borrow from ADB are not eligible).</li>
        <li>A <strong>bachelor’s degree or equivalent with an outstanding academic record</strong>.</li>
        <li><strong>At least 2 years of full-time professional working experience</strong> acquired after the university degree.</li>
        <li><strong>Proficiency in oral and written English</strong> — mandatory.</li>
        <li><strong>No more than 35 years old</strong> at the time of application.</li>
        <li><strong>In good health</strong>, and willing to <strong>return to the home country after completing studies</strong> and contribute to its development.</li>
        <li><strong>Excluded:</strong> ADB executive directors, alternate directors, management and staff, consultants and their relatives; applicants living or working outside their home country (applicants from another ADB developing member country may still be considered).</li>
        <li>The scholarship <strong>does not sponsor</strong> undergraduate study, distance learning, short-term training, conferences, seminars, thesis writing or research projects.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full remission of tuition fees</strong> for the programme.</li>
        <li><strong>Full remission of the admission/entrance fee.</strong></li>
        <li><strong>Monthly stipend</strong> at the Japanese Government Scholarship rate, plus allowances for study materials and research.</li>
        <li><strong>Health insurance.</strong></li>
        <li><strong>Round-trip economy-class airfare</strong> between the home country and Japan.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>The list below is the standard set cited consistently across the published guides for this award — confirm the current checklist on Keio's admissions pages before uploading.</em></p>
      <ol>
        <li>Online application form (Keio graduate admission)</li><li>Academic transcripts</li>
        <li>Degree certificate</li><li>Up-to-date CV/resume</li>
        <li>Two recommendation letters</li><li>Valid passport or ID</li>
        <li>Proof of professional work experience</li><li>English-language documentation where required; ADB-JSP application form where applicable</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose one of the four eligible Keio graduate schools</strong>and check its programme page for the 2027 admission guide.</li>
        <li><strong>Submit the Keio graduate admission application online</strong>during the application window (published guides place the 2027-intake closing date at <strong>1 November 2026</strong>). There is an application fee that cannot be waived.</li>
        <li><strong>Signal your ADB-JSP interest</strong>through the admission process — admitted candidates are the pool from which scholars are nominated.</li>
        <li><strong>Prepare the return-home narrative early:</strong> the programme's development mission means your post-study contribution plan matters; generic study plans undersell the application.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate ADB scholarship application form?","No standalone route is published. You apply for admission to Keio's graduate programme first, and scholarship consideration runs through the admission process — admitted candidates form the nomination pool."),
 ("What is the monthly stipend amount?","Published guides describe it as a monthly allowance at the Japanese Government Scholarship rate. No exact yen figure was confirmed in two verified sources for this cycle, so none is quoted here — check Keio's current admissions pages."),
 ("I am 36 — can I still apply?","The official eligibility caps applicants at 35 years old at the time of application. Above that, this award is closed to you."),
 ("Can I apply if I currently work outside my home country?","No — applicants living or working outside their home country are not eligible, though applications from another ADB developing member country may be considered."),
]),
 offlinks=[('ADB–Japan Scholarship Program — Keio University (official)','https://www.keio.ac.jp/en/st/admissions-en/scholarships/adb/')],
 related_titles=['honjo','jj-wbgsp','u-tokyo-mext'],
 verify='Verified 17 Oct 2026 via the official Keio University ADB-JSP page (full eligibility list: ADB borrowing-country national, bachelor’s + outstanding record, ≥2 yrs post-degree experience, English mandatory, ≤35, good health, return-home commitment, ADB-staff exclusion) and multiple independent guides on the 1 Nov 2026 closing date, the four eligible graduate schools and the benefit package. The exact yen stipend figure is one-source only and is not quoted.'),

# ---------------------------------------------------------------- 4. Ursinus
dict(
 slug='ursinus-gateway-international-scholarship-2027-usa',
 title='Ursinus Gateway International Scholarship 2027 in United States (Funded) | StudyDesk Scholarships',
 meta="Ursinus Gateway International Scholarship 2027: $35,000/year for up to 4 years for first-year international undergrads at Ursinus College, Pennsylvania. Automatic consideration. Intakes: 1 Nov, 1 Dec 2026, 1 Feb 2027.",
 short='Ursinus Gateway 2027', kicker='USA · Undergraduate · Ursinus College, Pennsylvania',
 mono='UG', prov_short='Ursinus College', prov_long='Ursinus College — private liberal arts college, Pennsylvania',
 h1='Ursinus Gateway International Scholarship 2027 in the United States',
 sub='A $35,000-a-year merit award for first-year international undergraduates at Ursinus College — awarded automatically with admission, no separate essay, across three intakes. Read it as serious tuition relief, not a full ride.',
 dpill='15 days to go', dl_long='1 Nov 2026 (Intake 1; further intakes 1 Dec 2026 and 1 Feb 2027)',
 facts=facts([('Award','$35,000/year, up to 4 years<small>Merit award toward tuition; renewable with good academic standing</small>'),
              ('Who','First-year international undergrads<small>Any nationality; full-time bachelor’s students; nearly all majors</small>'),
              ('Academic bar','SAT 1250+ / ACT 28+ / GPA 3.85<small>Published thresholds for the guaranteed award</small>'),
              ('Application','Automatic consideration<small>No separate scholarship essay — assessed through the admission application</small>'),
              ('Intakes','1 Nov 2026 · 1 Dec 2026 · 1 Feb 2027<small>Three rounds; earlier rounds leave more room in the pool</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Ursinus College</strong> is a private liberal-arts college in Pennsylvania, founded in 1869, and its <strong>Gateway International Scholarship</strong> is the international-student version of the college's guaranteed merit awards. For the 2027 intake it offers <strong>$35,000 per year for up to four years</strong> to first-year, full-time international undergraduate students — students of any nationality, across nearly every academic major the college offers. The defining feature is simplicity: <strong>every international applicant is automatically considered</strong> through the admission application, with selection based on SAT/ACT scores or GPA. There is no separate scholarship essay and no separate form.</p>
      <p><strong>Keep the numbers straight.</strong> Ursinus runs several merit awards side by side — the published guides also mention the Zacharias Honors Scholarship (a larger award, roughly $40,000/year) and the domestic Gateway Scholarship. This article covers only the <strong>international Gateway track at $35,000/year</strong>; do not mix the figures when comparing offers. Also be clear-eyed about coverage: $35,000 a year is major tuition relief at a US private college, but it is <strong>not a full ride</strong> — housing, meals, books, insurance and personal costs sit outside it, and you should budget for them before accepting.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student of any nationality</strong>, applying as a <strong>first-year, full-time undergraduate</strong> (not a transfer student).</li>
        <li>Admitted to a bachelor's programme at Ursinus College.</li>
        <li>The published academic bar for the guaranteed award: <strong>SAT 1250+, ACT 28+, or an unweighted GPA of 3.85 or higher on a 4.0 scale</strong> at the time of application (guides note GPAs between 3.5 and 3.84 may be considered alongside a rigorous curriculum).</li>
        <li><strong>High-school diploma or equivalent</strong>, with certified English translation of transcripts where needed.</li>
        <li><strong>English proficiency evidence</strong> (TOEFL, IELTS or equivalent) unless exempt.</li>
        <li>Demonstrated academic merit and leadership potential strengthen the file.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$35,000 per year</strong> toward tuition and academic costs, for <strong>up to four years</strong> of the bachelor's degree.</li>
        <li><strong>Renewable</strong> each year provided you maintain good academic performance.</li>
        <li><strong>No separate application burden</strong> — consideration is automatic with admission.</li>
        <li>Recipients may also be considered for <strong>additional need-based financial aid</strong>, further lowering the net cost.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Ursinus College undergraduate application (Common Application or Coalition Application)</li><li>High-school transcripts (certified English translation if not in English)</li>
        <li>SAT or ACT scores (where available)</li><li>Proof of English proficiency (TOEFL/IELTS or equivalent)</li>
        <li>Copy of valid passport</li><li>Letters of recommendation</li>
        <li>Personal statement / CV as required by the admission application</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for undergraduate admission to Ursinus College</strong>through the Common Application (or Coalition) for your chosen intake — <strong>1 November 2026, 1 December 2026 or 1 February 2027</strong>. Earlier intakes are the safer bet.</li>
        <li><strong>Nothing extra to file for the scholarship:</strong> admitted international applicants are automatically evaluated for the Gateway award on academic merit.</li>
        <li><strong>Receive the admission and scholarship decision together</strong>— successful candidates get both confirmations.</li>
        <li><strong>Confirm enrolment</strong>by the college's reply deadline and proceed with the F-1 student-visa process (including the SEVIS fee).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need to write a separate scholarship essay?","No. The Gateway International Scholarship is assessed automatically from your admission application on SAT/ACT scores or GPA — there is no separate scholarship application or essay."),
 ("Is the $35,000 a full scholarship?","No — it is a large partial award toward tuition, renewable for up to four years. Housing, meals, books, insurance and personal expenses are not covered by it, so plan the remaining costs before committing."),
 ("Can transfer students apply?","No — this track is for first-year, full-time bachelor's students only."),
 ("What if my GPA is 3.6 — am I out?","The published guaranteed-award bar is 3.85 unweighted (or SAT 1250+/ACT 28+), but guides note GPAs of 3.5–3.84 can be considered with a rigorous curriculum. Apply in an early intake and let the college assess the full file."),
]),
 offlinks=[('Ursinus Gateway Scholarship — official page','https://www.ursinus.edu/offices/student-financial-services/grants-scholarships-loans/ursinus-gateway-scholarship/')],
 related_titles=['dayton-merit','yale-wf','heyning'],
 verify='Verified 17 Oct 2026 via multiple independent trackers (the $35,000/year international figure, up-to-4-years renewability, first-year full-time international undergrad scope, automatic consideration, three intakes 1 Nov / 1 Dec 2026 / 1 Feb 2027, SAT 1250+/ACT 28+/GPA 3.85 bar) and the official Ursinus gateway-scholarship page. The larger Zacharias/domestic figures are separate awards and are flagged as such, not mixed into the international track.'),

# ---------------------------------------------------------------- 5. Auckland
dict(
 slug='university-of-auckland-scholarship-2027-new-zealand',
 title='University of Auckland Scholarship 2027 in New Zealand (Funded) | StudyDesk Scholarships',
 meta="University of Auckland 2027 scholarships for international students: Excellence Scholarship (25% of one year's tuition, master's, invitation route, 4 Nov 2026) plus India, ASEAN and School Leaver awards up to NZ$20,000.",
 short='Auckland 2027', kicker='New Zealand · Bachelor’s & Master’s · University of Auckland',
 mono='UoA', prov_short='University of Auckland', prov_long='The University of Auckland — New Zealand’s top-ranked university',
 h1='University of Auckland Scholarship 2027 in New Zealand',
 sub='Auckland funds international students through a family of tuition awards rather than one mega-scholarship — and the flagship 2027 award works by invitation, not by direct application. Understand the mechanism and you will not miss the window.',
 dpill='18 days to go', dl_long='4 Nov 2026 (supplementary form — International Student Excellence Scholarship, master’s)',
 facts=facts([('Flagship award','25% of one year’s tuition<small>International Student Excellence Scholarship — new international master’s students, one-year tenure</small>'),
              ('Mechanism','Invitation only<small>Master’s offer for Semester 1 / Quarter 2 2027 by 20 Oct 2026 → invited 21 Oct → supplementary form by 4 Nov 2026</small>'),
              ('Companion awards','Up to NZ$20,000<small>India High Achievers (up to NZ$20,000); ASEAN High Achievers (up to NZ$10,000); International School Leaver (up to NZ$20,000)</small>'),
              ('Who','New international students<small>Any nationality; admission offer required; English proficiency required</small>'),
              ('Coverage','Partial — tuition only<small>These are tuition-fee awards, not full funding; plan living costs separately</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Auckland</strong> — New Zealand's highest-ranked university — funds international students through a <strong>family of tuition-fee scholarships</strong> rather than a single award. The flagship for 2027 is the <strong>International Student Excellence Scholarship</strong>: for new international <strong>master's</strong> students, worth <strong>25% of one year's tuition fees</strong> for one year, offered twice a year with the number of awards varying by round. Around it sit three companion awards: the <strong>India High Achievers Scholarship</strong> (up to <strong>NZ$20,000</strong> toward tuition for new Indian students in undergraduate, PGDip or master's study), the <strong>ASEAN High Achievers Scholarship</strong> (up to <strong>NZ$10,000</strong> for new students from ASEAN countries), and the <strong>International School Leaver Scholarship</strong> (up to <strong>NZ$20,000</strong> for international students finishing secondary school in New Zealand).</p>
      <p><strong>The mechanism is the part most applicants miss.</strong> For the 2027 master's Excellence Scholarship there is <strong>no direct application</strong>: eligible new international master's students who hold a conditional or unconditional programme offer for <strong>Semester One or Quarter Two 2027 by 20 October 2026</strong> are <strong>invited on 21 October 2026</strong> to complete a supplementary application form, which must be submitted online by <strong>4 November 2026</strong>. No offer by 20 October, no invitation — the admission timeline <em>is</em> the scholarship timeline.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>New international students</strong> — the awards target students commencing study, not those already enrolled.</li>
        <li><strong>Excellence Scholarship (master's):</strong> hold a conditional or unconditional master's programme offer for Semester 1 or Quarter 2 2027 by <strong>20 October 2026</strong>; invitation to the supplementary form follows automatically for eligible students.</li>
        <li><strong>India High Achievers:</strong> new international students from <strong>India</strong> enrolling full-time in undergraduate, PGDip or master's degrees.</li>
        <li><strong>ASEAN High Achievers:</strong> new international students from <strong>ASEAN member countries</strong> entering bachelor's, master's or postgraduate diplomas.</li>
        <li><strong>International School Leaver:</strong> international students completing secondary schooling in New Zealand (published guides place its closing date at 21 October 2026 — only days away at the time of writing).</li>
        <li><strong>English proficiency</strong> per the university's admission requirements; academic merit decides the awards.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>25% of one year's tuition fees</strong> (International Student Excellence Scholarship, master's) — credited against tuition.</li>
        <li><strong>Up to NZ$20,000</strong> toward tuition (India High Achievers; International School Leaver).</li>
        <li><strong>Up to NZ$10,000</strong> toward tuition (ASEAN High Achievers).</li>
        <li>Study at <strong>New Zealand's top-ranked university</strong> across almost all fields — engineering, computer science and AI, business, law, health sciences, arts and more.</li>
      </ul>
      <p><em>These are partial, tuition-only awards. None of them covers living costs, and none is a full ride — budget Auckland living expenses separately.</em></p>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>University of Auckland programme application (the admission offer is the gateway)</li><li>Academic transcripts and degree certificates</li>
        <li>Up-to-date CV/resume</li><li>Copy of passport</li>
        <li>Valid English test result (e.g. IELTS)</li><li>Scholarship application / supplementary form where the award route requires it</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for your Auckland programme first</strong>— the Excellence Scholarship invitation depends on holding a Semester 1 / Quarter 2 2027 master's offer by <strong>20 October 2026</strong>.</li>
        <li><strong>Watch for the invitation on 21 October 2026</strong>and complete the supplementary application form online by <strong>4 November 2026</strong>.</li>
        <li><strong>For the India, ASEAN and School Leaver awards,</strong>use the dedicated scholarship pages linked from the university's scholarship finder — these follow their own application routes and dates.</li>
        <li><strong>Check the regulations PDF</strong>on each official scholarship page before submitting — award counts and exact criteria are set there.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I apply directly for the International Student Excellence Scholarship?","No. The 2027 master's version is invitation-only: you need the programme offer by 20 October 2026, receive the invitation on 21 October, and submit the supplementary form by 4 November 2026."),
 ("Is this a fully funded scholarship?","No. The flagship award covers 25% of one year's tuition, and the companion awards top out at NZ$20,000 toward tuition. They are tuition-fee awards — living costs in Auckland are on you."),
 ("I am an undergraduate — which Auckland award fits me?","The 2027 Excellence Scholarship page is master's-only. Undergraduates should look at the India High Achievers (up to NZ$20,000), ASEAN High Achievers (up to NZ$10,000) or International School Leaver (up to NZ$20,000) awards instead."),
 ("What happens if my programme offer arrives after 20 October 2026?","Then you miss this Excellence round — the invitation list is drawn from students holding offers by that date. The scholarship runs twice a year, so check the official page for the next round."),
]),
 offlinks=[('International Student Excellence Scholarship — University of Auckland (official)','https://www.auckland.ac.nz/en/study/scholarships-and-awards/find-a-scholarship/university-of-auckland-international-student-excellence-scholarship-844-all.html')],
 related_titles=['dayton-merit','maastricht','heyning'],
 verify='Verified 17 Oct 2026 via the official University of Auckland scholarship page (master’s Excellence: 25% of one year’s tuition, invitation route, offer by 20 Oct 2026, invitations 21 Oct, supplementary form due 4 Nov 2026) and independent trackers on the India (NZ$20,000), ASEAN (NZ$10,000) and School Leaver (NZ$20,000) companion awards. The School Leaver 21 Oct 2026 closing is tracker-sourced and flagged as such.'),

]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

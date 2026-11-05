#!/usr/bin/env python3
"""Batch 16 (cron run 16): 5 verified international articles. Verified 17 Oct 2026.

Notes:
- QMUL 2027: real scheme - four September 2027 awards (UG Global Talent £5k/yr up
  to £20k, automatic; PGT Global Excellence £8k, Global Talent £6k, Global Merit
  £5k, one form). Rolling, no fixed deadline; PGT form opens Oct 2026, awards
  continue to Apr 2027. Explicitly NOT fully funded - framed honestly.
- UChicago 2027: need-based aid meets full demonstrated need with grants, no
  loans; free tuition under $250k family income from Autumn 2027 (announced
  May 2026), full cost under $125k; merit from $2k automatic; First Phoenix
  $20k min; Odyssey grant-based support. Deadlines follow admission plan:
  ED I/EA 2 Nov 2026, ED II/RD 4 Jan 2027. Bright's CSS Profile/RaiseMe claims
  are stale - draft built from official pages.
- EMABG 2027: Erasmus Mundus Joint Master "European Master in Animal Biodiversity
  and Genomics" (emabg.eu). 3rd intake 15 Sep 2026 - 15 Jan 2027; EUR 1,400/month,
  participation costs covered; BSc 180 ECTS animal science; TOEFL 92 / IELTS 7.
- uOttawa: admission scholarships are AUTOMATIC, no deadline. UG $1k/$2k/$3k at
  85-89.9/90-94.9/95-100%; doctoral min $72k/4 yrs ($9k/yr component, 8.0/10+).
  Bright's "30 Apr 2026" deadline and Master/PhD "$7,500/yr" framing are
  aggregator inventions - flagged honestly in-article.
- IUJ: written for the OPEN September 2027 intake (all 2026 rounds closed).
  Nakayama tiers, ADB-JSP (nominated by IUJ), MEXT (yen144,000/mo, 1st intake
  only). ADB-JSP stipend yen amount omitted (not stated in official guidelines,
  third-party figures conflict). Master's round dates not republished officially
  - article tells readers to confirm on iuj.ac.jp; dpill kept neutral ("Now
  open") rather than tracker-derived "54 days".
SKIPPED this run (4): ADB YPP 2027 (deadline 30 Sep 2026 - passed); UST Korea
(Spring 2027 intake closed 6 Oct 2026, Fall 2027 dates not announced); ADB
Internship 2026 (official adb.org shows "no open opportunities"); Airbus GGP
2027 (official airbus.com: 2027 intake closed, 2028 opens Sep 2027).
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'qmul': dict(mono='QM', title='Queen Mary University Scholarships 2027 in UK (Funded)', href='queen-mary-university-scholarships-2027-uk.html',
              dpill='Rolling', award='£5,000–£8,000; UG up to £20,000', elig='Overseas fee status; offer for September 2027 entry; UG Global Talent is automatic.',
              tags=[('UK','blue'),('International','teal')]),
 'uchicago': dict(mono='UChi', title='University of Chicago Undergraduate Scholarships 2027 in USA (Funded)', href='university-of-chicago-undergraduate-scholarships-2027-usa.html',
              dpill='4 Jan 2027 · 79 days to go', award='Full need met, no loans; free tuition under $250k income', elig='First-year fall 2027 applicants; need-aware for internationals; aid requested at admission.',
              tags=[('Undergraduate','blue'),('USA','teal')]),
 'emabg': dict(mono='EM', title='Erasmus Mundus EMABG Scholarship 2027 (Fully Funded)', href='erasmus-mundus-emabg-scholarship-2027.html',
              dpill='90 days to go', award='€1,400/month + tuition + insurance', elig='BSc (180 ECTS) in animal science; all nationalities; IELTS 7 / TOEFL 92.',
              tags=[("Master's",'blue'),('Europe','teal')]),
 'ottawa': dict(mono='UO', title='University of Ottawa Admission Scholarship 2026 in Canada (Funded)', href='university-of-ottawa-admission-scholarship-2026.html',
              dpill='Automatic on admission', award='$1,000–$3,000 (UG); min $72,000/4 yrs (PhD)', elig='UG: 85–100% admission average; PhD: 8.0/10+; no separate form.',
              tags=[('Canada','blue'),('Automatic','teal')]),
 'iuj': dict(mono='IUJ', title='International University of Japan Scholarship 2027 in Japan (Fully Funded)', href='international-university-of-japan-scholarship-2027.html',
              dpill='Now open', award='Full tuition + monthly stipend (ADB-JSP / MEXT / Nakayama)', elig='Master’s, September 2027; ADB-JSP: age ≤35, 2 yrs work experience; apply in 1st/2nd intake.',
              tags=[("Master's",'blue'),('Japan','teal')]),
})

ARTICLES = [

# ---------------------------------------------------------------- 1. Queen Mary
dict(
 slug='queen-mary-university-scholarships-2027-uk',
 title='Queen Mary University Scholarships 2027 UK | StudyDesk Scholarships',
 meta='Queen Mary University of London offers tuition scholarships of £5,000–£8,000 for September 2027 entry, plus an undergraduate award worth up to £20,000. Check eligibility and how to apply.',
 short='Queen Mary University Scholarships 2027',
 kicker="UK · Undergraduate/Master's · Funded",
 mono='QM', prov_short='Queen Mary University of London', prov_cat='University · United Kingdom',
 h1='Queen Mary University of London Scholarships 2027: Up to £20,000 for International Students',
 sub='Queen Mary University of London has published its international scholarship line-up for September 2027 entry. There is no single "funded" award — instead, eligible offer holders can receive tuition-fee reductions of £5,000 to £8,000 on master\u2019s programmes, or up to £20,000 across an undergraduate degree. This page covers the four confirmed September 2027 awards, who qualifies, and how to be considered.',
 dpill='Rolling', dl_long='No fixed deadline — awards are allocated on a rolling basis. The Global Excellence postgraduate award is unlimited until April 2027, and its application form opens in October 2026.',
 facts=facts([('Award value','£5,000–£8,000<small>Undergraduate Global Talent: up to £20,000 total (£5,000 per year)</small>'),
              ('Study level',"Undergraduate & Master's<small>Full-time courses starting September 2027</small>"),
              ('Eligibility','Overseas fee status<small>First-class honours for Global Excellence; above-offer grades for undergraduate Global Talent</small>'),
              ('How awards are made','Offer + scholarship form<small>Undergraduate Global Talent is automatic — no separate application</small>'),
              ('Deadline','Rolling<small>Global Excellence applications open October 2026; awards continue until April 2027</small>'),
              ('Provider','Queen Mary University of London<small>Russell Group university in London, UK</small>')]),
 body='''<h2 id="about">About these scholarships</h2>
<p>For September 2027 entry, Queen Mary University of London lists four international scholarships in its official scholarship database. At undergraduate level, the <strong>Global Talent Scholarship</strong> is worth <strong>£5,000 per academic year</strong> — up to <strong>£20,000</strong> over a standard four-year degree — and is awarded automatically to eligible offer holders.</p>
<p>At postgraduate taught level, three tuition-fee awards are confirmed: the <strong>Global Excellence Scholarship (£8,000)</strong>, the <strong>Global Talent Scholarship (£6,000)</strong> and the <strong>Global Merit Scholarship (£5,000)</strong>. All are tuition-fee deductions, not full scholarships, and one scholarship application form considers you for all three postgraduate awards. Queen Mary also lists Global Excellence and Global Talent awards of £5,000–£7,000 for January 2027 postgraduate entry.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Global Talent – Undergraduate (September 2027):</strong> hold an offer for an eligible full-time undergraduate programme starting September 2027, have confirmed overseas fee status, be fully self-funded, and <strong>exceed</strong> your course offer (for example, an AAB offer requires AAA at A-level, or 36 IB points with HL 665) — or hold the overseas equivalent.</li>
<li><strong>Global Excellence – Postgraduate Taught (September 2027):</strong> achieve (or be on course to achieve) a first-class honours bachelor\u2019s degree or overseas equivalent, hold an offer for an eligible full-time master\u2019s programme starting September 2027, and have overseas fee status confirmed by Queen Mary.</li>
<li><strong>Global Talent / Global Merit – Postgraduate Taught (September 2027):</strong> the university\u2019s scholarship database lists these at £6,000 and £5,000 respectively for postgraduate taught offer holders joining in September 2027; detailed grade thresholds beyond \u201chigh achieving\u201d are not published in the official listings.</li>
<li>Applicants must remain overseas for fee purposes for the whole programme, must not hold any other University scholarship or a full-fee scholarship from another source, and must be able to finance the remainder of tuition fees and living costs.</li>
<li>Excluded from the schemes are advanced (year-two) entry, foundation and pre-master\u2019s programmes, distance learning, MRes, PG Diploma/Certificate courses, study-abroad/exchange programmes, and named programmes including medicine, dentistry and certain MSc/apprenticeship courses.</li>
</ul>
<h2 id="benefits">Benefits</h2>
<ul>
<li><strong>£5,000 per year, up to £20,000</strong> for undergraduate Global Talent scholars, deducted directly from tuition fees each year — renewable annually provided you achieve at least a 65% average.</li>
<li><strong>£8,000 tuition-fee deduction</strong> for Global Excellence postgraduate scholars, applied when you enrol.</li>
<li><strong>£6,000 tuition-fee deduction</strong> for Global Talent postgraduate scholars and <strong>£5,000</strong> for Global Merit postgraduate scholars.</li>
<li><strong>Unlimited awards</strong> for both the undergraduate Global Talent scheme and the Global Excellence postgraduate scheme (the latter until April 2027), open to students of <strong>all nationalities</strong>.</li>
<li><strong>One application covers all three postgraduate awards</strong> — you complete a single scholarship form and Queen Mary considers you for Global Talent, Global Merit and Global Excellence together.</li>
<li>The undergraduate award requires <strong>no separate application</strong>: eligible students are assessed automatically and notified via their applicant portal when their status becomes unconditional firm.</li>
</ul>
<h2 id="documents">Documents required</h2>
<p><em>Queen Mary has not published a separate documents checklist for these scholarships. You will need the standard documents for your course application (academic transcripts, English-language evidence where required, and a passport for fee-status assessment); the postgraduate scholarship form is emailed to you after you receive a course offer. Contact <strong>globalengagement@qmul.ac.uk</strong> for scheme-specific queries.</em></p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply for your course:</strong> submit an application for an eligible full-time Queen Mary undergraduate or master\u2019s programme for September 2027 entry (undergraduate applicants go through UCAS).</li>
<li><strong>Receive your offer:</strong> undergraduate candidates who exceed their offer grades are assessed automatically — there is no scholarship form to complete.</li>
<li><strong>Complete the scholarship form (postgraduate):</strong> once you hold a master\u2019s offer, Queen Mary emails you the scholarship application form when applications open in <strong>October 2026</strong>. One form covers Global Talent, Global Merit and Global Excellence.</li>
<li><strong>Awards are allocated on a rolling basis:</strong> apply early, since funding is distributed until places run out (Global Excellence postgraduate awards continue until April 2027).</li>
<li><strong>Confirm at enrolment:</strong> the scholarship is confirmed when your admissions status becomes \u2018unconditional firm\u2019 and you enrol; the award is then deducted directly from your tuition fees.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Are the Queen Mary 2027 scholarships fully funded?','No. These are partial tuition-fee reductions (£5,000–£8,000 for postgraduate awards, and up to £20,000 over an undergraduate degree). You must be fully self-funded and able to pay the remaining tuition fees and living costs.'),
 ('Is there a separate deadline for the undergraduate Global Talent Scholarship?','No. There is no application, registration process, or scholarship deadline for the undergraduate award — eligible international students are assessed automatically based on their final results and notified through their applicant portal.'),
 ('What grades do I need for the postgraduate awards?','The official page for Global Excellence requires a first-class honours degree or overseas equivalent. For Global Talent and Global Merit at postgraduate level, Queen Mary only states \u201chigh achieving\u201d — exact thresholds are not published, and the Admissions Office makes the final decision on overseas equivalences.'),
 ('Do I need to apply separately for each postgraduate scholarship?','No. One scholarship application form — emailed to you after you receive a master\u2019s offer — considers you for Global Talent, Global Merit and Global Excellence together. Applications open in October 2026.'),
 ('Can I hold this scholarship alongside another award?','No. You must not be in receipt of any other University scholarship, tuition-fee discount (including the alumni or partner-university discounts) or a full-fee scholarship from another source.'),
 ('Do the scholarships renew each year?','The undergraduate Global Talent award renews annually at £5,000 per year provided you maintain at least a 65% average. The postgraduate awards are one-off tuition-fee deductions. None of the awards can be deferred to a later year.'),
]),
 offlinks=[('Global Talent Scholarship – Undergraduate (September 2027), QMUL','https://www.qmul.ac.uk/scholarships/items/global-talent-scholarship---undergraduate-september-2027.html'),
           ('Global Excellence Scholarship – Postgraduate Taught (September 2027), QMUL','https://www.qmul.ac.uk/scholarships/items/global-excellence-scholarship--postgraduate-taught-september-2027.html'),
           ('QMUL scholarship database','https://www.qmul.ac.uk/scholarships/database/')],
 related_titles=['eiffel','clarendon','daad'],
 verify='Verified 17 Oct 2026 via official QMUL scholarship pages (Global Talent Undergraduate Sept 2027: £5,000/yr up to £20,000, automatic assessment, unlimited awards; Global Excellence PGT Sept 2027: £8,000, rolling allocation until April 2027, applications open Oct 2026, one form covers all three PGT awards) and the QMUL scholarship database (Global Merit PGT Sept 2027 £5,000; Global Talent PGT Sept 2027 £6,000).'),

# ---------------------------------------------------------------- 2. UChicago
dict(
 slug='university-of-chicago-undergraduate-scholarships-2027-usa',
 title='University of Chicago Undergraduate Scholarships 2027 in USA (Funded) | StudyDesk Scholarships',
 meta='UChicago undergraduate aid for 2027 entry: need-based grants with no loans, free tuition under $250k family income, Odyssey support, plus automatic merit consideration.',
 short='UChicago Undergraduate 2027',
 kicker='USA · Undergraduate · Need-based + merit',
 mono='UChi', prov_short='University of Chicago', prov_cat='University · United States',
 h1='University of Chicago Undergraduate Scholarships 2027 in USA (Funded)',
 sub='The University of Chicago funds undergraduate study mainly through need-based financial aid that meets full demonstrated need with grants, not loans — and from Autumn 2027 families earning under $250,000 pay no tuition. Alongside aid, UChicago runs several named awards, including the Odyssey Scholarship Program for under-resourced and first-generation students, and merit scholarships for which every first-year applicant is considered automatically.',
 dpill='4 Jan 2027 · 79 days to go',
 dl_long='Financial-aid consideration follows your admission plan: Early Decision I / Early Action by 2 November 2026; Early Decision II / Regular Decision by 4 January 2027 (fall 2027 entry).',
 facts=facts([('Coverage','Need-based grants, no loans <small>UChicago meets full demonstrated need with grants only; aid packages contain no student loans</small>'),
              ('Free-tuition guarantee','Under $250,000 family income <small>from Autumn 2027: free tuition with typical assets; under $125,000 also covers housing, meals and fees</small>'),
              ('Merit awards','From $2,000 <small>all first-year applicants are automatically considered for merit scholarships; no separate application, winners notified through April</small>'),
              ('International students','Eligible for need-based aid <small>need-aware admission; aid must be requested with the admission application — it cannot be added later</small>'),
              ('Named programmes','Odyssey, First Phoenix, Neubauer <small>Odyssey supports under-resourced/first-gen students; First Phoenix guarantees at least $20,000 over four years</small>'),
              ('Deadline','4 January 2027 <small>ED II / Regular Decision for fall 2027 entry; 2 Nov 2026 for ED I / Early Action</small>')]),
 body='''<h2 id="about">About this opportunity</h2>
<p>The University of Chicago does not run a single "2027 scholarship" with one form and one deadline. Instead, undergraduate funding flows through two channels: need-based financial aid and merit scholarships, both decided alongside the admission application for fall 2027 entry.</p>
<p>The need-based route is the main one. UChicago meets the full demonstrated financial need of admitted students with grants rather than loans, so an aid package contains no debt. In May 2026 the university went further, announcing that from Autumn 2027 students from families earning under $250,000 a year (with typical assets) will pay no tuition, while those from families under $125,000 will also have housing, meals and university fees covered.</p>
<p>Alongside aid, UChicago offers merit scholarships — most of them automatic. Every first-year applicant is considered without a separate application; awards start at $2,000 and can run for four years of study or fund summer opportunities. Only winners are notified, on a rolling basis through the end of April.</p>
<h2 id="eligibility">Eligibility</h2>
<ul>
<li><strong>Level:</strong> first-year undergraduate applicants entering UChicago's College in fall 2027; all nationalities may apply.</li>
<li><strong>Need-based aid:</strong> awarded on demonstrated financial need. International students are eligible but admission is need-aware, and aid must be requested during the admission process — a student admitted without aid cannot claim it in a later year.</li>
<li><strong>Free-tuition guarantee (Autumn 2027 onwards):</strong> family income under $250,000 with typical assets for tuition; under $125,000 for tuition plus housing, meals and fees. The guarantee previously sat at $125,000 for tuition and $60,000 for full cost.</li>
<li><strong>Merit scholarships:</strong> decided by an admissions committee on academic achievement, leadership and community commitment, without regard to financial need. Transfer students are not eligible for merit awards.</li>
<li><strong>First Phoenix Scholarship:</strong> for students first in their family to attend college — a minimum of $20,000 across four years, automatic consideration.</li>
<li><strong>Odyssey Scholarship Program:</strong> enhanced support for students from under-resourced families and first-generation students, including grants instead of loans, study-abroad funding, a paid summer internship opportunity and paid student health insurance.</li>
<li><strong>Admission:</strong> UChicago is test-optional under its "No Harm" policy; non-native English speakers demonstrate proficiency (e.g. TOEFL iBT 100, IELTS Academic 7.0 or Duolingo 135).</li>
</ul>
<h2 id="benefits">Benefits</h2>
<ul>
<li>Full demonstrated need met through grants — no loans in any aid package.</li>
<li>Free tuition for families under $250,000 (Autumn 2027 onwards); full cost of attendance for families under $125,000.</li>
<li>Odyssey Scholars receive grant-based aid, study-abroad funding, a paid first-summer internship opportunity, career mentorship and health insurance paid by Odyssey funds.</li>
<li>Merit awards starting at $2,000, renewable for four years of undergraduate study or usable for summer research and internship funding; the First Phoenix Scholarship guarantees at least $20,000 over four years.</li>
<li>Named scholarships exist for specific groups, including the Neubauer Family Adelante Program, the National Police and Fire Scholarship, Chicago Public Schools awards and the Evans Scholarship.</li>
</ul>
<h2 id="documents">Documents required</h2>
<p><em>A standalone scholarship document checklist is not published in the official notification; funding is assessed through the admission and financial-aid applications. International aid applicants complete the UChicago Financial Aid Worksheet through their UChicago Account (the CSS Profile and FAFSA are not used for international applicants), and all applicants submit the standard admission materials with their chosen application platform.</em></p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply for admission</strong> for fall 2027 entry through the Common Application, Coalition Application or UChicago's own application, selecting an admission plan (Early Decision I, Early Action, Early Decision II or Regular Decision).</li>
<li><strong>Request financial aid with your application.</strong> Indicate your intent to apply for aid at the same time you apply — international students who do not request aid at this stage cannot receive it later.</li>
<li><strong>Complete the UChicago Financial Aid Worksheet</strong> through your UChicago Account if you are an international (non-US citizen/permanent resident) aid applicant; US applicants complete the FAFSA.</li>
<li><strong>Submit proof of family income and assets</strong> as instructed in your applicant portal (translated tax documents or employer/bank evidence where applicable).</li>
<li><strong>Merit consideration is automatic.</strong> No separate merit application exists for first-year applicants; scholarship winners are notified on a rolling basis through the end of April.</li>
<li><strong>Meet your plan's deadline:</strong> 2 November 2026 for ED I / Early Action; 4 January 2027 for ED II / Regular Decision.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is this a fully funded scholarship for international students?','UChicago meets full demonstrated need for admitted students — including international students — with grants and no loans, which can amount to a full award. But admission is need-aware for international applicants, and you must request aid when you apply; you cannot add it later.'),
 ('What is the $250,000 free-tuition announcement?','Announced in May 2026, from Autumn 2027 UChicago guarantees free tuition for undergraduates from families earning under $250,000 with typical assets, and covers tuition, housing, meals and fees for families under $125,000.'),
 ('Do I need a separate application for merit scholarships?','No. Every first-year applicant is automatically considered for all available merit scholarships through the admission application. Transfer students are not eligible for merit awards.'),
 ('What is the Odyssey Scholarship Program?','Odyssey is UChicago\u2019s enhanced aid programme for students from under-resourced families and first-generation students: grants instead of loans, study-abroad and paid-internship funding, career mentorship and paid student health insurance.'),
 ('What are the deadlines for 2027 entry?','For fall 2027: Early Decision I and Early Action close 2 November 2026; Early Decision II and Regular Decision close 4 January 2027. Financial-aid consideration follows the same plan you apply under.'),
 ('Do I submit the CSS Profile for UChicago aid?','International applicants do not submit the CSS Profile or FAFSA — they complete the UChicago Financial Aid Worksheet in their UChicago Account. US applicants use the FAFSA.'),
]),
 offlinks=[('UChicago Scholarships (official admissions page)','https://collegeadmissions.uchicago.edu/cost-aid/scholarships/odyssey-scholarships'),
           ('UChicago announces free tuition under $250k (Chicago Maroon)','https://chicagomaroon.com/52351/news/uchicago-to-offer-free-undergraduate-tuition-for-families-making-less-than-250000-per-year/')],
 related_titles=['yale-wf','um-bright','ursinus'],
 verify='Verified 17 Oct 2026 via official UChicago admissions scholarships page (merit from $2,000, automatic first-year consideration, First Phoenix $20k minimum, Odyssey grant-based support, health insurance, paid internship; winners notified through April) + Chicago Maroon reporting of the 13 May 2026 announcement (free tuition under $250k from Autumn 2027; full cost under $125k; prior thresholds $125k/$60k since 2018; ~$225m annual aid) + international-aid guides (need-aware; aid must be requested at admission; Financial Aid Worksheet not CSS Profile/FAFSA for international applicants) + multiple deadline sources (ED I/EA 2 Nov 2026; ED II/RD 4 Jan 2027 for fall 2027 entry)'),

# ---------------------------------------------------------------- 3. EMABG
dict(
 slug='erasmus-mundus-emabg-scholarship-2027',
 title='Erasmus Mundus EMABG Scholarship 2027 (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus EMABG Scholarship 2027: fully funded 2-year master\u2019s in Animal Biodiversity and Genomics across 6 European universities. \u20ac1,400/month. Deadline 15 Jan 2027.',
 short='Erasmus Mundus EMABG Scholarship 2027',
 kicker='Europe · Master\u2019s · Fully Funded',
 mono='EM', prov_short='Erasmus Mundus (European Commission)', prov_cat='European Union · Master\u2019s',
 h1='Erasmus Mundus EMABG Scholarship 2027 (Fully Funded)',
 sub='The European Master in Animal Biodiversity and Genomics (EMABG), an Erasmus Mundus Joint Master, is inviting applications for its 2027 intake. Selected scholars receive full funding — tuition covered plus a monthly allowance of \u20ac1,400 — while studying animal breeding, biodiversity and genomics across six European universities over two years.',
 dpill='90 days to go',
 dl_long='15 January 2027 — application deadline for Erasmus Mundus scholarship consideration (applications open 15 September 2026)',
 facts=facts([('Level',"Master's · 2 years · taught in English"),
              ('Award','€1,400/month <small>monthly allowance; participation costs and insurance covered for scholarship holders</small>'),
              ('Deadline','15 January 2027 <small>scholarship round; self-paying deadlines differ</small>'),
              ('Open to','All nationalities <small>applications accepted worldwide</small>'),
              ('Study countries','Austria · France · Germany · Netherlands · Norway · Sweden <small>two of six consortium universities</small>'),
              ('Application route','Single online application <small>via the EMABG central application database — no separate university applications</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The European Master in Animal Biodiversity and Genomics — known by its acronym EMABG — is an Erasmus Mundus Joint Master funded by the European Union. It is a two-year master's course, taught entirely in English, built around the science and practice of animal breeding, biodiversity and genomics. The field has been transformed in the last decade by high-throughput genomic markers and large-scale phenotypic recording, and this programme trains graduates to work directly with that kind of data.</p>
<p>EMABG is run by a consortium of six leading European universities, and every student studies at two of them in two different countries. There are five areas of specialisation to choose from: conservation genomics for rare and endangered breeds and species; designing breeding programmes for small populations; bioinformatics applied to biodiversity and genomics; One Health — health and welfare in humans and animals; and understanding biodiversity through integrative biology. The study tracks are offered as pairs beginning at the Norwegian University of Life Sciences, for example NMBU–SLU, NMBU–WUR, NMBU–APT, NMBU–UGOE and NMBU–BOKU.</p>
<p>Applying for the programme automatically puts you in consideration for the Erasmus Mundus scholarship — there is no separate scholarship form. The application round for the 2027 intake runs from 15 September 2026 to 15 January 2027.</p>
<h2 id="eligibility">Eligibility criteria</h2>
<ul>
<li><strong>Academic degree:</strong> a Bachelor of Science degree of at least 180 ECTS in animal science. Graduates of other relevant bachelor's programmes can also be considered, provided they can demonstrate knowledge and skills in the basics of agricultural sciences and animal production — mathematics, biostatistics or bioinformatics; zoology, anatomy or physiology of farm animals; biodiversity and breeding; and genetics and genomics. Applicants who already hold a master's degree in a similar field cannot be accepted at the University of Göttingen.</li>
<li><strong>Nationality:</strong> open to applicants from all countries. The consortium distinguishes Programme Country and Partner Country applicants for scholarship-pool purposes, but candidates worldwide are welcome to apply.</li>
<li><strong>English proficiency:</strong> one of the following, taken no more than two years before the application deadline — TOEFL iBT with a score of at least 92 (minimum 23 in speaking; paper-based and ITP versions are not accepted); Academic IELTS with a score of at least 7 (minimum 6.5 in speaking; the online test and One Skill Retake are not accepted); Cambridge C1 Advanced (180–210, Grade C) or C2 Proficiency (180–230, Grade C).</li>
<li><strong>English exemption:</strong> applicants who completed their bachelor's or master's degree entirely in English, on campus, in Australia, Ireland, Canada (except Quebec universities), New Zealand, the United Kingdom or the United States do not need to submit a language certificate.</li>
<li><strong>Final-year students:</strong> may apply. Non-EU students must graduate by 15 March and EU students by 1 July of the intake year, and must upload a university letter, signed and stamped, confirming they will finish in time.</li>
</ul>
<h2 id="benefits">Scholarship benefits</h2>
<ul>
<li><strong>Monthly allowance of €1,400</strong> paid throughout the study period to support living costs.</li>
<li><strong>Participation costs fully covered</strong> for scholarship holders — no tuition or registration fees at any partner university.</li>
<li><strong>Health and accident insurance</strong> included for the duration of the programme.</li>
<li><strong>Mobility across Europe:</strong> study and research at two consortium universities in two different countries, earning a joint or double master's degree.</li>
<li><strong>One application, two outcomes:</strong> the same application is assessed both for admission to the master's programme and for the Erasmus Mundus scholarship.</li>
</ul>
<h2 id="documents">Documents required</h2>
<p>The official programme guidance lists the following. Only complete applications submitted through the application database are assessed, and all documents must be uploaded in the required format before the deadline.</p>
<ul>
<li>Completed online application form in the EMABG application database</li>
<li>Academic degree certificate and transcript of records (plus an official English translation if the originals are in another language)</li>
<li>Two letters of recommendation, addressed to the coordinators of the European Master in Animal Biodiversity and Genomics</li>
<li>Curriculum vitae, following the Europass format as closely as possible</li>
<li>Copy of a valid passport</li>
<li>Certificate of residence in English, issued within 12 months before the application deadline</li>
<li>Official English language certificate, unless you qualify for the exemption</li>
<li>Passport-style photograph</li>
<li>Letter stating your preferred study tracks (for example NMBU–SLU, NMBU–WUR, NMBU–APT) and explaining your reasons — this is not a generic motivation letter</li>
<li>Short motivation video (1–2 minutes, MP4, maximum 50 MB), titled only with your application number, explaining why you want to join the programme</li>
</ul>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Open the official EMABG website</strong> (emabg.eu) and read the programme and admission-requirements pages so you understand the study tracks and language rules.</li>
<li><strong>Choose your three preferred study tracks</strong> and write the required study-track letter explaining your choices.</li>
<li><strong>Record your motivation video</strong> and gather all documents — transcripts, passport, residence certificate, CV, recommendation letters and language certificate.</li>
<li><strong>Register in the EMABG central application database</strong> once the application period opens (15 September 2026) and upload every document. This single application covers both programme admission and the Erasmus Mundus scholarship.</li>
<li><strong>Submit the complete application by 15 January 2027.</strong> Do not send applications or documents directly to the partner universities or by email — only submissions through the database are considered, and hard copies should only be sent if the consortium asks for them.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('What is the application deadline for the 2027 EMABG intake?','15 January 2027 for candidates who want to be considered for the Erasmus Mundus scholarship. Self-paying applicants have later cut-offs: 15 February for non-EU students and 15 April for EU students. The application period opens on 15 September 2026.'),
 ('What exactly does the EMABG scholarship cover?','Scholarship holders receive a monthly allowance of €1,400, full coverage of participation (tuition) costs at every partner university, and health and accident insurance for the duration of the programme. The award is meant to cover food, accommodation, travel and visa costs across the two years of study.'),
 ('Which universities will I study at?','The consortium has six partners: the Norwegian University of Life Sciences (NMBU), Wageningen University & Research (Netherlands), the University of Göttingen (Germany), AgroParisTech (France), the University of Natural Resources and Life Sciences Vienna (BOKU, Austria), and the Swedish University of Agricultural Sciences (SLU). You study at two of them in two different countries, following a study track such as NMBU–SLU or NMBU–WUR.'),
 ('Can I apply if I am still finishing my bachelor\u2019s degree?','Yes. You can apply with a stamped and signed letter from your university confirming you will graduate in time — by 15 March for non-EU students and by 1 July for EU students. Upload the letter before the application deadline; no exceptions are made.'),
 ('Do I need to apply to each partner university separately?','No. One application in the EMABG central application database is enough — it is assessed for both admission to the master\u2019s programme and the Erasmus Mundus scholarship. The consortium explicitly asks applicants not to submit additional applications to individual consortium members.'),
 ('What English test scores are required?','Accepted tests are TOEFL iBT (at least 92 overall, minimum 23 in speaking), Academic IELTS (at least 7 overall, minimum 6.5 in speaking), or Cambridge C1 Advanced / C2 Proficiency. Certificates must be no older than two years at the application deadline. Graduates of on-campus English-medium programmes in Australia, Ireland, Canada (except Quebec), New Zealand, the UK or the USA are exempt.'),
]),
 offlinks=[('EMABG official site — Programme','https://www.emabg.eu/programme/'),
           ('EMABG official site — FAQ (deadlines, scholarships, application)','https://www.emabg.eu/faq/'),
           ('EMABG official site — Admission requirements','https://www.emabg.eu/application/admission-requirements/')],
 related_titles=['emmir','eiffel','daad'],
 verify='Verified 17 Oct 2026 via emabg.eu (official programme page: full name "European Master in Animal Biodiversity and Genomics", Erasmus Mundus Joint Master, 2-year English course, 3rd-intake window 15 Sep 2026–15 Jan 2027; FAQ: €1,400/month scholarship with participation costs covered, single database application covers programme + scholarship, final-year rules; admission page: BSc 180 ECTS in animal science, TOEFL 92 / IELTS 7 / Cambridge scores, exemption countries), ScholarshipsTab (full six-university consortium list, €1,400 × 24 months, 15 Jan 2027 scholarship deadline), BrightScholarship (15 Jan 2027 deadline, eligibility and documents corroboration)'),

# ---------------------------------------------------------------- 4. uOttawa
dict(
 slug='university-of-ottawa-admission-scholarship-2026',
 title='University of Ottawa Admission Scholarship 2026 | StudyDesk Scholarships',
 meta='University of Ottawa Admission Scholarship 2026: automatic awards of $1,000–$3,000 for undergraduates and up to $72,000 for doctoral students. No application needed.',
 short='uOttawa Admission Scholarship',
 kicker='Canada · Undergraduate · Automatic',
 mono='UO', prov_short='University of Ottawa', prov_cat='University · Canada',
 h1='University of Ottawa Admission Scholarship 2026 in Canada',
 sub='The University of Ottawa automatically considers newly admitted students for admission scholarships, with no separate form to file. Undergraduate awards range from $1,000 to $3,000 based on the admission average, while doctoral students can receive funding worth a minimum of $72,000 over four years. Here is exactly how the awards work, who qualifies, and what to do to be considered.',
 dpill='Automatic on admission',
 dl_long='There is no separate scholarship application and uOttawa publishes no application deadline for these awards — consideration happens automatically with an admission application. The 30 April 2026 date seen on aggregator listings is not published by the university as a scholarship deadline.',
 facts=facts([('Award (undergraduate)','$1,000 – $3,000 <small>single admission award, sized by admission average</small>'),
              ('Award (doctoral)','Minimum $72,000 <small>over four years; admission-scholarship component of $9,000 per year</small>'),
              ('Application','No separate application <small>automatically considered with your admission application</small>'),
              ('UG average bands','85–89.9%: $1,000 · 90–94.9%: $2,000 · 95–100%: $3,000 <small>doctoral admission scholarships need 8.0/10 or higher</small>'),
              ('Level','Undergraduate & doctoral <small>direct-entry undergraduate faculties and doctoral programmes</small>'),
              ('International students','Doctoral: eligible <small>international doctoral students with 8.0/10 or higher can qualify; undergraduate general criteria are framed around Canadian citizens, permanent residents, and protected/refugee status</small>')]),
 body='''<h2 id="about">About the scholarship</h2>
<p>The University of Ottawa Admission Scholarship is an entrance award granted on the strength of the marks used to admit a student. It comes in two forms: a one-time payment for entering undergraduates, scaled to the admission average, and a multi-year funding package for doctoral students. Both are automatic — the university assesses every eligible admission file and informs recipients with their admission offer. The 2026–2027 award details are currently published on the university's official scholarships pages.</p>
<p>It is worth noting that several scholarship-aggregation websites describe this award incorrectly, attaching invented deadlines or mismatched amounts to it. The university itself runs no application round and sets no application deadline for the admission scholarship, so treat any "last date" posted elsewhere with caution and rely on uottawa.ca.</p>
<h2 id="eligibility">Eligibility</h2>
<p>For the undergraduate Admission Scholarship, you must be enrolled full time for the first time in a university undergraduate programme, studying in a direct-entry faculty or in the Faculty of Law, Civil Law Section, with an admission average between 85% and 100%. Mature applicants and university transfers are not eligible for this award. The general undergraduate criteria describe eligibility for Canadian citizens, permanent residents, and those with protected-person or refugee status, with exceptions noted per award.</p>
<p>For the graduate (doctoral) Admission Scholarship, eligible candidates include Canadian students, permanent residents, protected persons, members of a diplomatic corps, and international students admitted into doctoral programmes, with an admission average of 8.0/10 or higher. Certain programmes are excluded from the doctoral award — the university's published list includes the MBA, MHA, MPH, MEd, MEng, Engineering Management, MCom, and MCI.</p>
<h2 id="benefits">Benefits</h2>
<p>Undergraduate recipients receive a single award of $1,000 (admission average 85–89.9%), $2,000 (90–94.9%), or $3,000 (95–100%). Doctoral recipients receive funding with a minimum total value of $72,000 over four years: the admission-scholarship component pays $9,000 per year in $3,000 instalments per term across 12 consecutive terms of full-time enrolment, with additional funding making up the rest of the package. Doctoral recipients must remain enrolled full time without interruption for the full duration of the scholarship.</p>
<h2 id="documents">Documents required</h2>
<p><em>Not published in the official notification. Because consideration is automatic, there are no scholarship-specific documents to prepare; the university uses the academic records and supporting materials already included in your admission application.</em></p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li><strong>Apply for admission.</strong> Submit your application for an eligible undergraduate or doctoral programme at the University of Ottawa through the normal admission channel.</li>
<li><strong>Secure your uoAccess ID.</strong> Once admitted, you can use your uoAccess ID and password to access university services, including the Online Scholarships and Bursaries tool for other awards that do need applications.</li>
<li><strong>Wait for the offer.</strong> No separate scholarship form exists. Eligible students are automatically considered at admission and are informed if they receive the award.</li>
<li><strong>Check the official page.</strong> Before relying on any deadline or amount posted on a third-party site, confirm the current terms on the university's official scholarships pages linked below.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is there a separate application for the Admission Scholarship?','No. The University of Ottawa states that no application is required — every eligible admission file is automatically considered, and recipients are informed if they receive the award.'),
 ('What admission average do I need?','For the undergraduate award: 85–89.9% earns $1,000, 90–94.9% earns $2,000, and 95–100% earns $3,000. For the doctoral award, the published minimum is an admission average of 8.0/10.'),
 ('Can international students receive it?','International students admitted into doctoral programmes are explicitly listed as eligible for the doctoral admission scholarship (8.0/10 average or higher). For the undergraduate award, the general criteria are framed around Canadian citizens, permanent residents, and protected/refugee status, with exceptions noted per award — international undergraduates have separate dedicated awards at the university.'),
 ('What is the 30 April 2026 deadline on some websites?','That date appears only on scholarship-aggregation websites and is not published by the University of Ottawa as a deadline for the admission scholarship. Since consideration is automatic with admission, there is no application round to close — be guided by the university\u2019s own admission deadlines instead.'),
 ('Is the undergraduate award renewable?','Not published in the official notification. The university describes it as a single admission award of $1,000 to $3,000; the doctoral component runs across 12 consecutive terms of full-time enrolment.'),
]),
 offlinks=[('University of Ottawa — Admission scholarship (graduate studies)','https://www.uottawa.ca/study/graduate-studies/funding-financing/awards/admission-scholarship'),
           ('University of Ottawa — Scholarships and awards overview (undergraduate)','https://www.uottawa.ca/study/fees-financial-support/scholarships-awards-overview')],
 related_titles=['oise-toronto','bcdi2030','dundee-ge'],
 verify='Verified 17 Oct 2026 via uOttawa official undergraduate scholarships page (automatic UG award: $1,000/$2,000/$3,000 bands at 85–89.9%/90–94.9%/95–100%; updated 24 Sep 2026; citizenship/transfer restrictions) and uOttawa official graduate admission-scholarship page (doctoral: 8.0/10 average minimum, $72,000 minimum over 4 years, $9,000/year component, automatic offer, international doctoral students eligible, excluded programmes list). Bright Scholarship listing used only as a lead; its 30 Apr 2026 deadline and Master/PhD "$7,500/$9,000 per year" framing are not corroborated by the official pages.'),

# ---------------------------------------------------------------- 5. IUJ 2027
dict(
 slug='international-university-of-japan-scholarship-2027',
 title='International University of Japan Scholarship 2027 in Japan (Fully Funded) | StudyDesk Scholarships',
 meta='IUJ Japan scholarship 2027: fully funded master\u2019s routes (ADB-JSP, MEXT, Nakayama) for September 2027 entry — eligibility, benefits, deadlines and how to apply.',
 short='IUJ Scholarship 2027',
 kicker='Japan · Master\u2019s · Fully Funded',
 mono='IUJ', prov_short='International University of Japan', prov_cat='University · Japan',
 h1='International University of Japan Scholarship 2027 in Japan (Fully Funded)',
 sub='The International University of Japan is accepting applications for September 2027 entry, and its official 2027 scholarship guidelines map out every funded route — from the university\u2019s own Nakayama awards to IUJ-nominated ADB-JSP and MEXT places. Fully funded options cover full tuition plus monthly stipends; ADB-JSP targets working professionals from ADB developing member countries, while the MEXT university-recommendation track is open only to first-intake applicants. IUJ strongly advises applying in the first or second intake — late applicants are extremely unlikely to secure full funding.',
 dpill='Now open',
 dl_long='Applications for September 2027 entry are open now — apply in the 1st intake for the strongest scholarship chances. Confirm the exact round deadlines on iuj.ac.jp before applying.',
 facts=facts([('Funding','Fully funded <small>ADB-JSP: full tuition + monthly stipend incl. housing (amount not stated in IUJ\u2019s 2027 guidelines); MEXT: full tuition + ¥144,000/month; Nakayama Premium: full tuition + ¥100,000/month</small>'),
              ('Intake','September 2027 <small>IUJ confirms online applications for the 2027 admissions cycle are now open</small>'),
              ('Levels','Master\u2019s programmes <small>GSIR: IRP, IDP, PMPP, JGDP (MA), IPPP (1-year); GSIM: MBA, JGDP (MBA), IMBA, DXP (1-year)</small>'),
              ('Who can apply','Citizens of ADB developing member countries <small>India, Bangladesh, Pakistan, Nepal, Sri Lanka, the Philippines, Vietnam and others are on IUJ\u2019s published list</small>'),
              ('Experience & age','ADB-JSP: 35 or younger <small>with at least 2 years of full-time work experience after the bachelor\u2019s degree</small>'),
              ('Strategy','1st or 2nd intake <small>3rd-intake applicants are extremely unlikely to be nominated for a full scholarship</small>')]),
 body='''<h2 id="about">About the IUJ scholarship routes</h2>
<p>The International University of Japan, based in Niigata, admits graduate students once a year, in September. For the September 2027 intake it publishes one set of scholarship guidelines for non-Japanese master\u2019s applicants, covering three paths. Category A is awarded directly by IUJ at the time of admission — the S. Nakayama Memorial Scholarships, which range from a 30% tuition exemption up to the Premium tier with full tuition and a monthly stipend. Category B is nominated by IUJ\u2019s admissions committee after you pass the admissions screening; this includes the ADB-Japan Scholarship Program, the AEON Scholarship, the JERA Asia Scholarship, the Marubeni Scholarship, the Konosuke Matsushita Memorial Foundation award and the MEXT University Recommendation (Special). Category C is applied for directly with the provider — JICA programmes, the Japan-IMF Scholarship Program for Asia and MEXT by embassy recommendation — where you simply name IUJ as your chosen school. Most awards require you to hold a Japan student visa, which IUJ helps successful applicants obtain.</p>
<h2 id="eligibility">Eligibility</h2>
<p>For the Nakayama awards, IUJ looks for newly enrolling international students with excellent academic records who will take part in campus and local-community life; recipients are expected to live in the IUJ dormitories in principle. The ADB-JSP is open to citizens of ADB developing member countries who do not hold dual citizenship of a developed country. You must gain admission to an approved IUJ master\u2019s course, hold a bachelor\u2019s degree with a superior academic record, and have at least two years of full-time work experience gained after the degree, in either the public or private sector. You must be 35 or younger at the time of application, in good health, proficient in written and spoken English, and be living and working in your home country when you apply. In principle you should not already hold a master\u2019s or PhD or be enrolled in a degree programme, and you must agree to return to your home country for at least two years after completing the degree. ADB staff, their close relatives and staff of the designated institutions are excluded. IUJ notes that preference goes to applicants with lesser financial capacity and to women. For MEXT (University Recommendation), only international applicants from the 1st intake can be considered; you must be born on or after 2 April 1992, come from a country with diplomatic relations with Japan, hold a student visa, never have received a MEXT scholarship before, and be available for an online interview with IUJ faculty.</p>
<h2 id="benefits">Benefits</h2>
<p>The Nakayama Premium waives ¥250,000 of the ¥300,000 admissions fee, exempts full tuition — ¥3,200,000 per year for two-year programmes and ¥3,900,000 for one-year programmes — and pays ¥100,000 per month; Nakayama 100 gives a full tuition exemption, and Nakayama 90, 70, 50 and 30 give partial exemptions of 90%, 70%, 50% and 30%. These are one-year awards that can be extended to the second year on a commendable record, and the Premium and 100 tiers are reserved for the most capable candidates. Under ADB-JSP, the scholar pays ¥50,000 of the admissions fee upfront (reimbursed after enrolment) and receives full tuition, a monthly stipend including a housing allowance, a books and instructional-materials allowance, medical and accident insurance, a thesis or research allowance, and two one-way economy air tickets between the home country and Japan. The award runs for one year and may be extended if academic performance stays satisfactory; scholars may not take paid work that needs a work permit, though paid TA, RA or facilitator roles are possible with prior ADB approval. The MEXT university-recommendation award covers full tuition, a monthly stipend of ¥144,000 (subject to change), and airfare between the home country and Japan; successful nominees pay ¥50,000 of the admissions fee upfront and are reimbursed after enrolment. The award runs September 2027 to June 2029 for two-year programmes and to August 2028 for one-year programmes.</p>
<h2 id="documents">Documents required</h2>
<p><em>IUJ\u2019s 2027 scholarship guidelines do not publish a standalone documents list — everything is collected inside the online application. IUJ\u2019s 2027 admissions guidelines list the usual items: the online application form, a personal statement, scanned transcripts and graduation certificates, two recommendation letters, an English test score (TOEFL, IELTS or TOEIC), the application fee, and a passport copy. Confirm the master\u2019s checklist in the portal before you start.</em></p>
<h2 id="how">How to apply</h2>
<ol class="steps-list">
<li>Read the 2027 Scholarship Guidelines and the programme pages on iuj.ac.jp, and choose the master\u2019s programme that fits your goals.</li>
<li>Register on IUJ\u2019s online application site, complete Phase 1 (admission) and then Phase 2 (the scholarship application), answering every question directly in the form.</li>
<li>Submit in the 1st or, at latest, the 2nd intake — IUJ says 3rd-intake applicants are extremely unlikely to be nominated for a full scholarship, and only 1st-intake applicants can be considered for MEXT.</li>
<li>Upload all required documents and make sure the application fee reaches IUJ by the round deadline.</li>
<li>For Category C routes (JICA, Japan-IMF/JISPA, MEXT by embassy recommendation), apply directly to the provider and name IUJ as your graduate school.</li>
<li>Wait for the admissions and scholarship decisions — IUJ nominates candidates to ADB, which makes the final ADB-JSP selection around July; MEXT nominees must submit extra materials on a short deadline set by IUJ.</li>
</ol>
<h2 id="faqs">FAQs</h2>
'''+faqs([
 ('Is there a separate scholarship form at IUJ?','No — the scholarship application is Phase 2 of the same online admission application. You first complete the degree-application sections, then continue to the scholarship part and select the awards you want to be considered for.'),
 ('Do I apply to ADB directly for the ADB-JSP?','No. There is no direct application to ADB. IUJ\u2019s admissions committee nominates candidates from successful admission applicants, and ADB makes the final selection, informing IUJ around July.'),
 ('Can I apply in the 3rd intake and still get a full scholarship?','IUJ\u2019s official guidelines say applicants in the 3rd intake are extremely unlikely to be nominated for a full scholarship. Apply in the 1st or 2nd intake to be seriously considered.'),
 ('What are the age limits?','ADB-JSP applicants must be 35 or younger at the time of application, with at least two years of full-time post-degree work experience. For MEXT (University Recommendation), you must have been born on or after 2 April 1992.'),
 ('Do I need to know Japanese?','No — Japanese is not an admission requirement. Some partner awards add their own language terms: AEON asks for JLPT N3 or above, and JERA strongly encourages learning Japanese toward JLPT N2 during the degree.'),
 ('How long does ADB-JSP funding last?','The award is granted for one year and may be extended for the second year of a two-year programme, conditional on maintaining satisfactory academic performance as judged by IUJ.'),
]),
 offlinks=[('IUJ 2027 Scholarship Guidelines – Master\u2019s (PDF)','https://www2.iuj.ac.jp/admission/pdf/2027/Sch_Instructions_M_E.pdf'),
           ('IUJ: Online Applications Now Open for 2027 Admissions','https://www.iuj.ac.jp/news/news/20260915/726/'),
           ('IUJ Online Application Site','https://www.iuj.ac.jp/admis/online/')],
 related_titles=['apu-adb','keio-adb','science-tokyo'],
 verify='Verified 17 Oct 2026 via IUJ 2027 Scholarship Guidelines (Master\u2019s) PDF on iuj.ac.jp (scholarship categories, ADB-JSP eligibility and conditions, Nakayama tiers and amounts, MEXT ¥144,000 stipend and 1st-intake-only rule, Phase 1/Phase 2 application process), IUJ news page “Online Applications Now Open for 2027 Admissions” (2027 cycle open), and IUJ 2027 PhD Admissions Guidelines PDF (intake deadlines 16 Nov 2026 / 16 Feb 2027 / 16 Apr 2027, document checklist)'),

]

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

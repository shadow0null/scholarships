#!/usr/bin/env python3
"""Batch 12 (cron run 12): 5 verified international articles. Verified 16 Oct 2026.

Notes: CIEL Internship Program (Spring 2027, Geneva) researched but SKIPPED —
its application deadline is 16 Oct 2026 11:59pm CET (deadline day; closed before
publish). KNU International Graduate Scholarship substituted from the queue.
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'mbzuai': dict(mono='MB', title='MBZUAI Postgraduate Scholarships 2027 in UAE', href='mbzuai-postgraduate-scholarships-2027-uae.html',
              dpill='60 days to go', award='Tuition waiver + AED 15.5k–43.5k/month + airfare', elig="STEM Master's/PhD; PhD centrally funded; MSc via assistantship/merit.",
              tags=[("Master's/PhD",'blue'),('UAE','teal')]),
 'maastricht': dict(mono='UM', title='Maastricht NL-High Potential Scholarship 2027-28', href='maastricht-nl-high-potential-scholarship-2027.html',
              dpill='108 days to go', award='€20,150–€38,750 + tuition/visa at cost', elig="Non-EU Master's; GPA 7.5/10; ≤35; never studied in NL.",
              tags=[("Master's",'blue'),('Netherlands','teal')]),
 'heyning': dict(mono='HR', title='Heyning-Roelli Foundation Scholarship (Switzerland)', href='heyning-roelli-foundation-scholarship-2027.html',
              dpill='4 days to go', award='Need-based exchange grant (no fixed amount)', elig='Exchange students at Swiss universities; demonstrated financial need.',
              tags=[('Exchange','blue'),('Switzerland','teal')]),
 'daad': dict(mono='DAAD', title='DAAD University Summer Courses 2027 in Germany', href='daad-university-summer-courses-2027-germany.html',
              dpill='14 days to go', award='Course fees + accommodation + €475 + travel + insurance', elig='18+; non-German university; B1 German; 2+ years of study.',
              tags=[('Language course','blue'),('Germany','teal')]),
 'knu': dict(mono='KNU', title='KNU International Graduate Scholarship 2027 (Korea)', href='knu-international-graduate-scholarship-2027-korea.html',
              dpill='14 days to go', award='100% or 50% tuition waiver (reviewed each semester)', elig="Non-Korean; KNU Master's/PhD admission; no separate scholarship form.",
              tags=[("Master's/PhD",'blue'),('South Korea','teal')]),
})

ARTICLES = [
dict(
 slug='mbzuai-postgraduate-scholarships-2027-uae',
 title='MBZUAI Postgraduate Scholarships 2027 in UAE | StudyDesk Scholarships',
 meta="MBZUAI scholarships 2027: funded PhD and assistantship/merit-funded MSc at Abu Dhabi's AI university. Tuition waived, AED 15,500–43,500/month stipends, annual airfare. Deadline 15 Dec 2026.",
 short='MBZUAI Scholarships 2027', kicker='UAE · Master’s & PhD · AI / STEM',
 mono='MB', prov_short='MBZUAI', prov_long='Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi (graduate admissions)',
 h1='MBZUAI Postgraduate Scholarships 2027 in the UAE',
 sub='Abu Dhabi’s dedicated AI university funds postgraduate AI study — but read the fine print first: PhD students are centrally funded, while MSc students are admitted fee-paying unless they earn an assistantship or merit award.',
 dpill='60 days to go', dl_long='15 Dec 2026, 5:00 PM GST (most programmes; Computational Biology: 22 Jan 2027)',
 facts=facts([('Award','Fully funded (for funded students)<small>Tuition waiver + monthly stipend + annual airfare + insurance + UAE visa</small>'),
              ('Who can apply',"Master’s & PhD in AI<small>STEM graduates; open to all nationalities</small>"),
              ('Stipend','AED 15,500–43,500/month<small>AED 15.5k MSc / 17.5k PhD (international); higher for UAE nationals</small>'),
              ('Funding model','PhD centrally funded in Year 1<small>MSc: fee-paying unless assistantship / merit award</small>'),
              ('Deadline','15 Dec 2026, 5 PM GST<small>Decisions by 31 Mar 2027; respond by 15 Apr 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)</strong> in Abu Dhabi is the world's first graduate-level, research-based university dedicated to AI, and for the <strong>Fall 2027 intake</strong> it continues its generous but often-misunderstood funding model. Many blogs headline this as "fully funded" without qualification — the honest version is: <strong>PhD students are centrally funded by the university in Year 1</strong> (moving to faculty-advisor funding from Year 2, subject to a confirmed match and satisfactory progress), while <strong>MSc students are admitted fee-paying by default</strong> and only funded via a faculty-sponsored research or teaching assistantship, an approved UAE government scholarship, or a merit-based award considered during admission review. The Master in Applied AI (MAAI) is a fee-based programme and is <strong>not</strong> eligible for funding.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>STEM degree</strong> — computer science, electrical/computer engineering, mathematics, physics or a related science/engineering field — from an accredited university recognised by the UAE Ministry of Education.</li>
        <li><strong>CGPA of 3.0 or 3.5 on a 4.0 scale</strong>, depending on the programme.</li>
        <li>Final-year students may apply with current transcripts; degrees need UAE attestation or a Certificate of Recognition (for non-UAE degrees) within the first semester.</li>
        <li><strong>English proficiency is required</strong> (the official page's exact score table was not verifiable in two sources — check the admissions page for current minimums).</li>
        <li><strong>All nationalities welcome:</strong> the official pages publish no nationality restriction, and international students apply alongside UAE nationals.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver</strong> for funded students.</li>
        <li><strong>Monthly stipend</strong> — official rates: <strong>AED 15,500 (MSc) / 17,500 (PhD)</strong> for international students; <strong>AED 37,500 (MSc) / 43,500 (PhD)</strong> for UAE nationals.</li>
        <li><strong>One return airfare</strong> to the home country per year.</li>
        <li><strong>Health insurance</strong> for the funding period, plus a <strong>university-sponsored UAE residence visa and Emirates ID</strong>.</li>
        <li><strong>No free accommodation promise:</strong> accommodation is not on the official benefits list — third-party blogs claiming "free housing" are not supported by the university's own pages.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>The official page's document checklist did not render for verification; the list below is the standard set cited consistently across third-party guides — confirm against the official admissions page before uploading.</em></p>
      <ol>
        <li>CV and official transcripts + degree certificates</li><li>Statement of purpose (roughly 500–1,000 words) and research statement (PhD)</li>
        <li>Two referee nominations (MSc) / three (PhD)</li><li>English proficiency test evidence</li>
        <li>Passport copy and a recent photograph</li>
        <li>UAE nationals/residents: Emirates ID, family book, and national-service letter where applicable</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Submit one online application per admission cycle</strong>via the university's graduate application portal (linked from the official admissions pages). There is <strong>no separate scholarship form</strong> — funding is assessed through the admission process itself.</li>
        <li><strong>Pay the AED 200 application fee</strong>after submission (waived at ≥75% screening-exam score; refunded on enrolment) — per third-party guides; confirm on the official portal.</li>
        <li><strong>Complete the technical screening exam</strong></li>
        <li><strong>Attend a faculty interview</strong>if shortlisted; decisions arrive by 31 March 2027 and offers must be answered by 15 April 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is every admitted MSc student fully funded?","No. MSc students are admitted fee-paying by default; funding comes only via a faculty assistantship, an approved UAE government scholarship, or a merit award considered during review."),
 ("Is accommodation covered?","Accommodation is not on the official benefits list, so do not count on it."),
 ("Is the MAAI (Master in Applied AI) covered?","No — the MAAI is a fee-based programme and is not eligible for scholarship funding."),
 ("When will I know the decision?","The official timeline says decisions by 31 March 2027, with offer responses due by 15 April 2027."),
]),
 offlinks=[('MBZUAI graduate MSc admissions (official)','https://mbzuai.ac.ae/admissions/graduate-masters-admissions/'),('MBZUAI PhD admissions (official)','https://mbzuai.ac.ae/admissions/graduate-phd-admissions/')],
 related_titles=['qassim','yale-wf','monash-rtp'],
 verify='Verified 16 Oct 2026 via mbzuai.ac.ae (official admissions pages) and multiple independent trackers (deadlines 15 Dec 2026 / 22 Jan 2027; official funding model — PhD centrally funded, MSc fee-paying unless assistantship/merit; stipend figures; accommodation not on the official benefits list; documents/fee/exam steps from third-party consensus).'),

dict(
 slug='maastricht-nl-high-potential-scholarship-2027',
 title='Maastricht University NL-High Potential Scholarship 2027-28 | StudyDesk Scholarships',
 meta="Maastricht NL-High Potential scholarship 2027-28: €20,150–€38,750 living costs, tuition and visa paid at cost for a non-EU master's in the Netherlands. Deadline 1 Feb 2027, 23:59 CET.",
 short='Maastricht NL-High Potential 2027', kicker='Netherlands · Master’s · Non-EU students',
 mono='UM', prov_short='Maastricht University', prov_long='Maastricht University, the Netherlands (Scholarship Fund + Dutch NL Scholarship)',
 h1='Maastricht University NL-High Potential Scholarship 2027-28',
 sub='The Netherlands’ flagship master’s award combines UM funding with the Dutch NL Scholarship — living costs, insurance, tuition and visa covered, but only for the top-ranked non-EU applicants.',
 dpill='108 days to go', dl_long='1 Feb 2027, 23:59 CET (scholarship form; master’s admission via Studielink by 10 Dec 2026)',
 facts=facts([('Award','€20,150–€38,750 living costs<small>13- or 25-month programme; tuition, visa, insurance paid at cost</small>'),
              ('Who can apply',"Non-EU/EEA master's students<small>Never studied in the NL; GPA 7.5/10; ≤35 on 1 Sep 2027</small>"),
              ('Tuition & visa','Paid at cost by UM<small>Health + liability insurance (€700) arranged by UM</small>'),
              ('Admission first','Studielink by 10 Dec 2026<small>A UM student ID is needed for the scholarship form</small>'),
              ('Deadline','1 Feb 2027, 23:59 CET<small>One application per person; no changes after submission</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Maastricht University NL-High Potential scholarship</strong> is the combined form of two awards: the <strong>UM High Potential Scholarship</strong> (funded by the Maastricht University Scholarship Fund) and the <strong>NL Scholarship</strong> (financed by the Dutch Ministry of Education, Culture and Science). A note on naming: the national component was formerly called the "Holland Scholarship" and many aggregators still use that label, but <strong>"Holland Scholarship" is not the official UM name</strong>. The award is highly selective — UM itself notes only about 2% of applicants are awarded. The two-week <strong>Pre-Academic Training</strong> starting the first week of August 2027 is a mandatory part of the programme.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A national of a country <strong>outside the EU/EEA, Switzerland and Surinam</strong>; must qualify for a Dutch entry visa/residence permit (MVV); no dual EU/EEA or Swiss nationality.</li>
        <li>Applied to a <strong>participating full-time UM master's for 2027-28</strong> with a complete admission file via Studielink by <strong>10 December 2026</strong>, meeting that programme's requirements.</li>
        <li><strong>Never</strong> participated in a degree-seeking higher-education programme in the Netherlands (exchange programmes are fine).</li>
        <li><strong>GPA of at least 7.5 out of 10</strong> on the latest transcript (equivalents: 75% of the maximum grade, or 3 out of 4).</li>
        <li><strong>Not older than 35 on 1 September 2027</strong>; preference for candidates without a prior master's degree.</li>
        <li>Willing to act as a UM NL-High Potential ambassador; only <strong>one scholarship application per person</strong>, and documents cannot be changed after submission.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Living expenses: €20,150</strong> for a 13-month programme or <strong>€38,750</strong> for a 25-month programme (the official page gives a line-item breakdown, e.g. housing €960/month).</li>
        <li><strong>Health and liability insurance (€700)</strong>, arranged and paid by UM.</li>
        <li><strong>Tuition fees, visa application costs and Pre-Academic Training costs paid at cost</strong> by UM.</li>
        <li>A <strong>room is allocated</strong> as a mandatory part of the award until <strong>16 July 2028</strong> — accepting the scholarship means accepting the room (not suitable for partners, children or pets); two-year awardees arrange their own second-year housing.</li>
        <li><strong>Not covered:</strong> air tickets and an upfront cleaning fee of about €75.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>All uploaded as .doc/.docx/PDF via the scholarship form, in one go:</em></p>
      <ol>
        <li>CV (max two A4 pages; include awards/prizes and job experience)</li><li>Letter of motivation using <strong>UM's template</strong></li>
        <li>Proof of academic excellence: university transcript with the most recent GPA <strong>plus a document explaining the grading system</strong></li>
        <li>Personal statement of financial needs (describe financial difficulty, caretaking, disability, refugee status, etc.)</li>
        <li>A reference letter <strong>uploaded by the applicant</strong> (former professor/lecturer/employer — not family; must follow UM's reference guidelines; dated no earlier than February 2026; UM may verify it)</li>
        <li>Contact details of one referee (relationship, work phone with country code, <strong>institutional/work email</strong> — personal-email references are rejected)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for a participating master's via Studielink</strong>Submit your complete admission file by 10 December 2026 and receive a UM student ID.</li>
        <li><strong>Log in with your UM account and complete the scholarship form</strong>before 1 February 2027, 23:59 CET. (UM warned the portal would be down 22–26 October during an upgrade.)</li>
        <li><strong>Wait for the selection timeline</strong>completeness check after the deadline; faculties rank their top 5 in March; interviews late March; decisions in April; final status (selected / waitlisted / rejected) by early May 2027.</li>
        <li><strong>Attend Pre-Academic Training</strong>a mandatory two-week component starting the first week of August 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the award automatic with admission?","No — the scholarship is a separate, highly competitive application; UM notes only about 2% of applicants are awarded."),
 ("What about the 'top 5%' rule some sites mention?","It is not on the official UM page. The official academic bar is a GPA of at least 7.5/10."),
 ("Can I bring my partner or children?","The allocated room is part of the award and is not suitable for partners, children or pets."),
 ("Can I apply for more than one scholarship?","Only one scholarship application per person may be submitted, and documents cannot be changed after submission."),
]),
 offlinks=[('Maastricht University NL-High Potential scholarship (official)','https://www.maastrichtuniversity.nl/studeren/toelating-inschrijving/financing-your-studies/scholarships/maastricht-university-nl-high')],
 related_titles=['eiffel','sabanci','unil'],
 verify='Verified 16 Oct 2026 via maastrichtuniversity.nl (official award amounts, deadlines, eligibility, documents, selection timeline) and independent 2027-28 guides. The "top 5%" criterion and award counts are not published on the official page — omitted.'),

dict(
 slug='heyning-roelli-foundation-scholarship-2027',
 title='Heyning-Roelli Foundation Scholarship 2027 (Switzerland, Exchange Students) | StudyDesk Scholarships',
 meta="Heyning-Roelli Foundation scholarship: need-based grants for exchange students at Swiss universities, covering documented travel and living-cost shortfalls. Next deadline 20 Oct 2026 (Spring 2027 round).",
 short='Heyning-Roelli Scholarship', kicker='Switzerland · Exchange · Bachelor’s & Master’s',
 mono='HR', prov_short='Heyning-Roelli Foundation', prov_long='Heyning-Roelli Stiftung, Zurich (independent foundation)',
 h1='Heyning-Roelli Foundation Scholarship for Exchange Students (Switzerland)',
 sub='A Zurich foundation that plugs the budget gap for economically disadvantaged students on official exchanges at Swiss universities — need-based, no fixed amount, and nothing like a full degree scholarship.',
 dpill='4 days to go', dl_long='20 Oct 2026 (Spring 2027 round; next round 20 Apr 2027)',
 facts=facts([('Award','Need-based grant<small>No fixed amount — covers the documented travel/living-cost shortfall</small>'),
              ("Who can apply","Exchange students only<small>Bachelor's & Master's on an official exchange at a Swiss university</small>"),
              ('Not covered','No tuition waiver published<small>Other scholarships you hold count against the grant</small>'),
              ('Deadlines','20 Apr (autumn) / 20 Oct (spring)<small>Decisions: end Nov for the spring round</small>'),
              ('Administered by','Independent foundation<small>Not ETH-administered; applications go to the foundation directly</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Heyning-Roelli Stiftung</strong>, founded in Zurich on <strong>15 February 2010 by Eduard C. Heyning</strong>, supports talented but economically disadvantaged students who take part in <strong>official exchange programmes</strong> at Swiss universities. Get the framing right: the foundation <strong>does not award full scholarships</strong>. It pays grants that cover a documented budget shortfall, decided case-by-case by its Board of Trustees based on need, destination and duration — and other scholarships you hold are counted against the award. It is an <strong>independent foundation</strong> (administration runs through the Zurich law firm Blum &amp; Grob), not administered by ETH Zurich, and the grant is open to exchange students at <strong>any</strong> Swiss university.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Bachelor's and Master's students</strong> taking part in an <strong>official exchange programme</strong> (the Swiss-European Mobility Programme, or bilateral agreements between Swiss and foreign universities) for one or two semesters at a partner university.</li>
        <li>Incoming route: students at foreign universities with an <strong>approved exchange placement at a Swiss institution</strong>, remaining enrolled at their home university; Swiss students invited to write their Bachelor's/Master's thesis abroad are also covered.</li>
        <li><strong>Excluded:</strong> double-degree students, students who have already completed an exchange, and retrospective applications (exchange already started).</li>
        <li><strong>Nationality is open</strong> — no official source restricts this to developing countries; that framing appears only on some blogs.</li>
        <li>You must be <strong>economically disadvantaged</strong> with a documented budget shortfall.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>grant sized to your documented shortfall</strong>, covering travel and living/subsistence costs during the exchange, plus other exchange-connected costs — decided individually by the Board of Trustees.</li>
        <li><strong>There is no fixed lump sum:</strong> blog figures such as "CHF 8,800 per semester" are not supported by any source, and a dated university document's "up to CHF 5,000" cap contradicts the foundation's current no-fixed-amount policy.</li>
        <li><strong>No tuition waiver</strong> is mentioned anywhere in the foundation's materials.</li>
        <li>Grants from other sources reduce the award — the foundation only covers the remaining gap.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p><em>Officially named by the foundation: motivation letter (no template) and proof of financial need (bank documents, tax returns, letters from relatives, etc.). Independent guides consistently add:</em></p>
      <ol>
        <li>One-page motivation letter (no template)</li><li>Bachelor's/Master's transcripts and GPA calculation result</li>
        <li>Confirmation/nomination from the host university (preliminary proof, e.g. an email confirmation, is accepted; formal admission can follow)</li>
        <li>Proof of financial need — bank documents, tax returns, letters from relatives</li><li>CV</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure your exchange placement</strong>through your home university's official exchange programme first (nomination/confirmation from the host Swiss university).</li>
        <li><strong>Apply online through the foundation's website</strong>— email applications are no longer accepted. Respect the cutoff: 24:00 CET on 20 October for the spring round.</li>
        <li><strong>Sign the declaration of commitment</strong>after arrival in Switzerland (submitted to the administration email); payout happens once it is received, at the earliest one month before the exchange starts.</li>
        <li><strong>Decisions are emailed by end of November</strong>for the spring round (end of July for the autumn round).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a fixed amount, like CHF 8,800 per semester?","No. There is no fixed lump sum — blogs quoting CHF 8,800 or CHF 25,000 per year are unsupported or contradicted. The grant is sized to your documented shortfall."),
 ("Does it waive tuition fees?","No tuition waiver appears anywhere in the foundation's materials — the grant covers travel and living-cost shortfalls."),
 ("Is it only for students from developing countries?","No — nationality is open. The developing-country restriction is a blog invention."),
 ("Is it administered by ETH Zurich?","No. It is an independent foundation administered through Blum & Grob in Zurich; ETH Zurich only lists it as an external scholarship."),
]),
 offlinks=[('Heyning-Roelli Foundation (official)','https://heyning-roelli-stiftung.ch/en/')],
 related_titles=['swiss-phd','epfl-summer','unil'],
 verify='Verified 16 Oct 2026 via heyning-roelli-stiftung.ch (official foundation site) and ETH Zurich mobility materials. No fixed award amount exists; CHF 8,800/CHF 25,000 blog figures are unsupported or contradicted; no tuition waiver; not ETH-administered; nationality is open.'),

dict(
 slug='daad-university-summer-courses-2027-germany',
 title='DAAD University Summer Courses 2027 in Germany (Funded) | StudyDesk Scholarships',
 meta="DAAD University Summer Courses 2027: funded 4-week German-language courses in Germany — course fees, accommodation, €475 allowance, travel subsidy and insurance. Deadline 30 Oct 2026, 23:59 CET.",
 short='DAAD Summer Courses 2027', kicker='Germany · Language courses · UG & PG',
 mono='DAAD', prov_short='DAAD', prov_long='German Academic Exchange Service (DAAD), Germany',
 h1='DAAD University Summer Courses 2027 in Germany',
 sub='A funded four-week German language course in Germany — fees covered, accommodation arranged, a €475 allowance plus travel subsidy and insurance, for students and graduates worldwide.',
 dpill='14 days to go', dl_long='30 Oct 2026, 23:59 CET (applications open 1 Sep 2026)',
 facts=facts([('Award','Course fees + accommodation + €475<small>Country-specific travel allowance + health/accident/liability insurance</small>'),
              ('Who can apply','Students & graduates, any subject<small>18+; enrolled at a university outside Germany</small>'),
              ('German level','B1 minimum<small>A2 accepted for non-humanities applicants (official call)</small>'),
              ('Study bar','2+ years of university completed<small>Final-year undergrads eligible if starting PG right after; one-time award</small>'),
              ('Deadline','30 Oct 2026, 23:59 CET<small>PDF-only uploads; portal closes at midnight</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DAAD University Summer Courses</strong> (<em>Hochschulsommerkurse</em>) are four-week, intensive German-language courses held at German universities <strong>June to September</strong>, funded by the German Federal Foreign Office. Courses are taught <strong>exclusively in German</strong>, in person only, with at least 25 teaching hours per week (maximum five days per week). A warning on figures: several aggregators still quote the old amounts of €1,134 / €1,309 and a 1 December deadline from earlier cycles — those are outdated for this programme. The <strong>official 2027 listing</strong> gives a <strong>€475 one-off allowance</strong> and a <strong>30 October</strong> closing date.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>At least 18</strong> when the course starts.</li>
        <li>Enrolled at a university in a programme-related country (<strong>not Germany</strong>) both at application time and throughout the scholarship period; simultaneous enrolment at a German university disqualifies.</li>
        <li>Students and graduates in <strong>any subject area</strong>.</li>
        <li>Bachelor's/undergraduate applicants must have completed <strong>at least two academic years</strong> by the time funding begins (final-year undergraduates are eligible only if they intend to start postgraduate studies immediately after graduating).</li>
        <li><strong>German: minimum B1</strong> on the official listing, with an <strong>A2 floor for applicants from non-humanities subjects</strong> in a country-variant listing (exception: Moscow and St. Petersburg).</li>
        <li>Funding from this programme can be claimed <strong>only once</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full coverage of the language-course fees.</strong></li>
        <li><strong>Accommodation arranged</strong> by the course provider for the course duration (single room — student dormitory, shared flat or private household).</li>
        <li><strong>One-time allowance of €475</strong>, paid through the course provider in cash on site (not transferred abroad).</li>
        <li><strong>Country-specific travel allowance</strong> (amount varies by home country — check the DAAD subsidies table; an India-specific figure was not confirmed).</li>
        <li><strong>Health, accident and personal liability insurance.</strong></li>
        <li>Grants are <strong>not extendable</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application form</li><li>Complete tabular CV <strong>in German</strong></li>
        <li>Letter of motivation <strong>in German</strong></li>
        <li>Transcripts of all university examinations from the <strong>last two consecutive years</strong> with individual grades — original plus German or English translation (if study is under two years: current achievements plus school-leaving certificate)</li>
        <li>For graduates: last degree certificate with final grades, original plus translation</li>
        <li>Language certificates with German/English translation where applicable (accepted: onSET-Deutsch, TestDaF, Goethe-Institut, DSD, DSH, telc Deutsch, ÖSD; certificate no older than <strong>one year</strong>, B2/TDN3-in-all-parts up to two years)</li>
        <li>Other supporting documents where relevant (internships, employment certificates)</li>
      </ol>
      <p><em>Uncertified copies are accepted at submission; DAAD may request certified copies later. All uploads must be PDF.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register and apply online through the DAAD application portal</strong>during 1 September – 30 October. Prepare documents, translate where needed and scan to PDF.</li>
        <li><strong>Name three preferred course locations</strong>preferences cannot be changed after submission, and DAAD may assign a different course if capacity is full. The course list (dates, levels, focus areas) is published as a spreadsheet on the call page.</li>
        <li><strong>Upload the complete application before the deadline</strong>only complete applications uploaded by 30 October 2026, 23:59 CET are considered; the portal closes at midnight.</li>
        <li><strong>Selection is by a committee</strong>on your academic record and motivation letter.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is 1 December the deadline?","No — that figure circulates on some guides but is outdated for this programme. The official 2027 closing date is 30 October 2026, 23:59 CET."),
 ("Can I choose my course?","You name three preferred course locations, but preferences cannot be changed after submission and DAAD may assign a different course if capacity is full."),
 ("Is the grant renewable or repeatable?","No — the grant is not extendable and funding from this programme can be claimed only once."),
 ("Can I apply with A2 German?","The official floor is B1, but A2 is accepted for non-humanities subject applicants per the official call."),
]),
 offlinks=[('DAAD scholarship database — University Summer Courses (official)','https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?origin=179&status=1&subjectGrps=&daad=&q=&page=2&detail=50035295')],
 related_titles=['hanns-seidel','ieg-mainz','ustc'],
 verify='Verified 16 Oct 2026 via the official DAAD scholarship database (deadline 30 Oct 2026; €475 allowance for 2027; B1 floor with the A2 non-humanities exception; portal rules) and independent trackers. Older €1,134/€1,309 amounts and the 1 December date are from earlier cycles — not used.'),

dict(
 slug='knu-international-graduate-scholarship-2027-korea',
 title='KNU International Graduate Scholarship 2027 in South Korea | StudyDesk Scholarships',
 meta="KNU KINGS scholarship 2027: 100% or 50% tuition waivers for international master's and PhD students at Kyungpook National University, Daegu. Spring 2027 deadline 30 Oct 2026, 6 PM KST.",
 short='KNU Graduate Scholarship 2027', kicker='South Korea · Master’s & PhD · KNU Daegu',
 mono='KNU', prov_short='KNU', prov_long='Kyungpook National University, Daegu (Office of International Affairs)',
 h1='KNU International Graduate Scholarship 2027 in South Korea',
 sub='Kyungpook National University’s KINGS programme waives 50–100% of tuition for newly admitted international master’s and PhD students — but note: it is tuition-only, and there is no separate scholarship form.',
 dpill='14 days to go', dl_long='30 Oct 2026, 6:00 PM KST (Spring 2027 intake)',
 facts=facts([('Award','100% or 50% tuition waiver<small>Reviewed every semester; tuition only — no living stipend</small>'),
              ('Who can apply',"International master's/PhD<small>Non-Korean; admitted via normal KNU graduate admission</small>"),
              ('Duration','Up to 4 semesters<small>8 semesters for the combined master’s–PhD</small>'),
              ('No separate form','Department recommendation<small>Departments rank admitted candidates for KINGS</small>'),
              ('Deadline','30 Oct 2026, 6 PM KST<small>Interviews 18–27 Nov 2026; results 6 Jan 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>KINGS — the KNU International Graduate Scholarship</strong> — is Kyungpook National University's own programme for newly admitted international master's and PhD students at its Daegu campus. It comes in <strong>two tiers: 100% or 50% tuition waiver</strong>, reviewed every semester, so continuation is not guaranteed. New students compete in a budget of roughly <strong>70 full-tuition equivalents</strong>; enrolled students draw from a larger pool (around 210), normally needing at least a B0 grade from the prior semester. Support lasts up to <strong>4 semesters</strong> (master's or PhD) or <strong>8 semesters</strong> (combined master's–PhD). The key structural fact: there is <strong>no separate scholarship application</strong> — departments screen admitted candidates and recommend them in ranked order for KINGS.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International (non-Korean) students</strong> admitted to KNU master's, PhD or combined master's–PhD programmes, with the prior degree completed (expected graduation acceptable).</li>
        <li>No separate scholarship eligibility round — you compete on the strength of your admission: <strong>departments recommend admitted international students in ranked order</strong>.</li>
        <li>The <strong>"Excellent KINGS" top tier</strong> (full waiver for the first semester, around 30 students) is reserved for candidates who graduated from a <strong>THE/QS top-500 overseas university</strong>, are qualifying KNU graduates continuing their studies, or hold strong language scores (<strong>TOPIK 6 / TOEFL iBT 100 / IELTS 7.0 / CEFR C1 / New TEPS 392</strong>).</li>
        <li><strong>No age limits</strong> are published anywhere.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% or 50% tuition waiver</strong>, tiered and reviewed each semester.</li>
        <li><strong>Tuition only:</strong> the majority of sources state living costs, flights and insurance are <strong>not</strong> covered. One low-quality source claims monthly stipends of KRW 700,000–1,200,000 plus dormitory and health coverage — this contradicts the majority and is <strong>not used here</strong>.</li>
        <li>Continued funding depends on academic performance (enrolled students normally need <strong>≥B0</strong> from the prior semester).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Application form, statement of purpose and study plan</li><li>Recommendation letter (directly from the professor or sealed)</li>
        <li>Degree certificate (or expected-graduation certificate) and official transcripts</li>
        <li>Language proficiency results (TOPIK / IELTS / TOEFL etc.)</li>
        <li>Passport copy and birth/family register; portfolio for fine-arts/design programmes</li>
      </ol>
      <p><em>One-source items (not confirmed in two sources): a USD 18,000 bank-balance certificate and a KRW 60,000 online application fee — confirm on the official admission guide.</em></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply through KNU's normal international graduate admission process</strong>for your chosen department and the Spring 2027 semester — there is no separate scholarship form.</li>
        <li><strong>Submit online 12–30 October 2026, 6:00 PM KST</strong>the department screens your admission file; interviews run 18–27 November 2026.</li>
        <li><strong>Scholarship selection happens before the semester begins</strong>results announced 6 January 2027; your department's ranking decides your tier.</li>
        <li><strong>Find the official guide on the KNU site</strong>the exact 2027 graduate admission-guide URL was not locatable in verification, so use the official KNU homepage and Office of International Affairs pages and search for the "Spring 2027 graduate admission guide" — do not trust deep links copied from blogs.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a monthly stipend?","The majority of sources say no — KINGS is tuition-only. A single low-quality source claiming KRW 700,000–1,200,000 monthly stipends contradicts the rest and should not be relied on."),
 ("Do I apply for the scholarship separately?","No. There is no separate scholarship form — departments recommend admitted international students for KINGS in ranked order."),
 ("What about the Fall 2027 intake?","A 30 April 2027 Fall deadline appears in only one source and is unconfirmed — check the official KNU pages."),
 ("Where is the official admission guide?","The exact 2027 guide URL could not be located in two sources; use the official KNU homepage and its Office of International Affairs pages and search for the Spring 2027 graduate admission guide."),
]),
 offlinks=[('Kyungpook National University (official)', 'https://www.knu.ac.kr/')],
 related_titles=['yeungnam','sabanci','monash-rtp'],
 verify='Verified 16 Oct 2026 via Korea JoongAng Daily (sourced per-university, published 4 Oct 2026) and multiple independent trackers (30 Oct 2026 deadline; 100%/50% tuition tiers; department-recommended, no separate form; tuition-only). Official knu.ac.kr 2027 guide URL not located — homepage linked; bank-certificate and fee figures are one-source; stipend claims contradicted — omitted.'),

]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

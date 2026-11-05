#!/usr/bin/env python3
"""Batch 25 (cron run 25, 20 Oct 2026): 5 verified articles.

All prose original. Verification completed 20 Oct 2026 across 5 waves.

WRITTEN this run:
- Holland NL Scholarship 2026 (verified open; per-institution deadlines, no single deadline)
- UAE University Undergraduate Scholarship 2026 (verified; open intake window;
  deadline + document list not published in official notification -> honest-notes)
- UNICEF Internship Program 2026 (verified open; rolling vacancies, no fixed deadline;
  stipend varies by duty station -> figure omitted)
- British Airways Summer Internship 2027 (re-scoped: 2026 cycle closed 19 Nov 2025;
  2027 cycle open, deadline 4 Nov 2026, GBP 26,000 pro rata)
- Erasmus Mundus MemBioMed Scholarship 2027 (re-scoped: 2026-28 cohort closed;
  2027-29 cohort opens 1 Dec 2026; closing date not yet published -> flagged)

SKIPS this run (deadline passed / closed 2026 cycles):
- USTB CSC 2026 (Type B deadline 15 Mar 2026; second announcement 15 May 2026 — past)
- NASA LPI Summer Internship 2026 (application period ended 12 Dec 2025; 2027 edition separate)
- CERN OPENLAB Summer Student Program 2026 (deadline 26 Jan 2026 — past)
- Amazon Future Engineer 2026 (deadline 22 Jan 2026; recipients already announced)
- Jonkoping University Scholarships 2026 (deadline 2 May 2026 — past; open window is 2027 intake)
- CERN Summer Student Programme 2026 (deadline 26 Jan 2026 — past)
- Rockefeller SURF 2026 (deadline 1 Feb 2026 — past)
- Erasmus Mundus EMLE 2026 (deadline 15 Jan 2026 — past; 2027/28 intake open separately)
- Sheffield GEMS 2026 (deadline 19 Feb 2026 — past; 2027 cycle live separately)
- Zhejiang University CSC 2026 (deadline 31 Dec 2025 — past)
- MCW Young Leaders Fellowship 2026 (deadline 3 Dec 2025 — past; 2026 programme concluded)
- RIKEN CBS Summer Internship 2026 (deadline 7 Jan 2026 — past; 2027 call not yet posted)
- CUFE CSC 2026 (deadline 6 Mar 2026 — past)
- Tianjin University CSC 2026 (deadline 18 Feb 2026 — past; 2027 call not published)
- Harbin Institute of Technology CSC 2026 (window 1 Nov 2025 - 20 Feb 2026 — closed)
- Stipendium Hungaricum 2026 (deadline 15 Jan 2026 — past; 2027/28 call opens Nov 2026)
- University of Pecs Hungarian Scholarships 2026 (deadline 15 Jan 2026 — past; Stipendium Hungaricum track)
- KAIST Visual AI Winter Internship 2026 (deadline 15 Nov 2025 — past; winter 2026-27 call not posted)
- Edinburgh Mastercard Foundation 2026 (2026/27 intake closed; open 2027/28 cycle is
  gated behind closed info sessions -> not writable as apply-now)
- British Airways Summer Internship 2026 -> re-scoped to the open 2027 cycle
- Erasmus Mundus MemBioMed 2026 -> re-scoped to the 2027-2029 cohort
SKIPS (failed verification / umbrellas):
- University of York Masters Scholarship 2026: no single genuine scheme (stale mashup of
  discontinued York Management School awards, Chevening, GREAT) — skip permanently
- UK GREAT Scholarships 2026: umbrella across 60+ institutions, no single deadline/amount
- Indorama Ventures Internship 2026: "fully funded" package blog-only, contradicted by
  official partner page (students pay own airfare); no official 2026 cycle or apply URL
- Chinese Government Scholarships 2026 Complete Guide: guide, not a single scheme
- Best Scholarships in Norway 2026 (BS, MS, PhD): umbrella listicle, no single scheme
- 5000 Fully Funded Scholarships in Germany 2026: umbrella listicle, no single scheme
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'nl-2026': dict(mono='NL', title='Holland NL Scholarship 2026 in Holland (Funded)', href='holland-nl-scholarship-2026-holland.html',
              dpill='Varies by university', award='\u20ac5,000 one-off (first year only)', elig='Non-EEA; full-time bachelor\u2019s/master\u2019s; no prior Dutch degree.',
              tags=[('Government','blue'),('Netherlands','teal')]),
 'uaeu-2026': dict(mono='UAEU', title='UAE University Undergraduate Scholarship 2026 (Funded)', href='uae-university-undergraduate-scholarship-2026.html',
              dpill='Open \u2014 Sep\u2013Nov intake', award='100% tuition (Grade 12 \u226598%); 75% (\u226595%)', elig='New undergrads incl. international; UAEU admission requirements.',
              tags=[('University','blue'),('UAE','teal')]),
 'unicef-2026': dict(mono='UN', title='UNICEF Internship Program 2026 (Paid)', href='unicef-internship-program-2026.html',
              dpill='Rolling \u2014 no fixed deadline', award='Monthly stipend (varies by duty station)', elig='18+; enrolled or graduated within 2 years.',
              tags=[('Internship','blue'),('Worldwide','teal')]),
 'ba-2027': dict(mono='BA', title='British Airways Summer Internship 2027 in UK (Paid)', href='british-airways-summer-internship-2027-uk.html',
              dpill='4 Nov 2026 \u00b7 15 days to go', award='\u00a326,000 pro rata', elig='First/second-year uni students; 2:2 predicted; right to work in UK.',
              tags=[('Internship','blue'),('UK','teal')]),
 'membiomed-2027': dict(mono='MB', title='Erasmus Mundus MemBioMed Scholarship 2027 in Europe (Fully Funded)', href='erasmus-mundus-membiomed-scholarship-2027.html',
              dpill='Opens 1 Dec 2026', award='\u20ac1,400/month \u00d7 24 + full tuition', elig='All nationalities; 180 ECTS bachelor\u2019s in biology/life sciences.',
              tags=[('Master\u2019s','blue'),('Europe','teal')]),
})

ARTICLES = [
dict(
 slug='holland-nl-scholarship-2026-holland',
 title='Holland NL Scholarship 2026 in Holland (Funded) | StudyDesk Scholarships',
 meta='NL Scholarship (formerly Holland Scholarship) 2026: a \u20ac5,000 one-off grant for non-EEA students in their first year of a full-time bachelor\u2019s or master\u2019s at participating Dutch universities. Per-institution deadlines, eligibility, and how to apply.',
 short='Holland NL Scholarship 2026', kicker='Government Scholarship \u00b7 Netherlands',
 mono='NL', prov_short='Nuffic', prov_long='Nuffic / Dutch Ministry of Education, Culture and Science, The Hague, Netherlands', prov_cat='Government \u00b7 Netherlands',
 h1='Holland NL Scholarship 2026',
 sub='\u20ac5,000 towards your first year of study in the Netherlands: the NL Scholarship (previously the Holland Scholarship) helps non-EEA bachelor\u2019s and master\u2019s students cover the costs of a full-time degree at participating Dutch research universities and universities of applied sciences.',
 dpill='Varies by university', dl_long='Per institution \u2014 no single published deadline (2026-27 examples: some closed, some open)',
 facts=facts([('Award','\u20ac5,000 one-off grant<small>First year of study only \u2014 not renewable</small>'),
              ('Who can apply','Non-EEA students<small>Full-time bachelor\u2019s/master\u2019s; no prior Dutch degree</small>'),
              ('Deadline','Set per institution<small>No central deadline exists</small>'),
              ('Level','Bachelor\u2019s & master\u2019s<small>First year at a participating institution</small>'),
              ('Apply via','Your chosen university<small>No central application \u2014 admission first</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>NL Scholarship</strong> \u2014 still widely known by its former name, the <strong>Holland Scholarship</strong> \u2014 is a grant for students from outside the European Economic Area (EEA) who are starting a full-time bachelor\u2019s or master\u2019s programme in the Netherlands. It is financed by the <strong>Dutch Ministry of Education, Culture and Science</strong> and the participating institutions themselves, and it is administered jointly with <strong>Nuffic</strong>, the Dutch organisation for internationalisation in education. The programme was renamed from Holland Scholarship to NL Scholarship in 2023.</p>
      <div class="honest-note"><strong>No single deadline:</strong> there is no central NL Scholarship deadline. Each participating university sets its own closing date for the 2026-27 cycle \u2014 some have already passed (e.g. May 2026 closes), while others remain open (a round that began 1 October 2026 at Aeres University; Saxion\u2019s 2027 close of 1 May 2027). <strong>Check the deadline on your chosen university\u2019s own page</strong> \u2014 any single \u201c2026 deadline\u201d quoted by a third-party site should be treated with suspicion.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-EEA nationality</strong> (the EEA covers the EU plus Iceland, Liechtenstein and Norway; some institutions also exclude Switzerland or students already entitled to the statutory tuition fee).</li>
        <li>Applying for \u2014 and admitted to \u2014 a <strong>full-time bachelor\u2019s or master\u2019s programme</strong> at a <strong>participating Dutch research university or university of applied sciences</strong>.</li>
        <li><strong>No degree previously obtained from a Dutch institution</strong> (some institutions extend this to no prior enrolment in the Netherlands).</li>
        <li>You must meet the <strong>institution\u2019s own admission and selection requirements</strong> \u2014 GPA thresholds, English-language scores and an admission offer are typically part of the picture.</li>
        <li>The scholarship can <strong>generally be awarded only once</strong> per student.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac5,000 one-off grant</strong>, paid in the <strong>first year of study</strong>.</li>
      </ul>
      <div class="honest-note"><strong>What it is not:</strong> the NL Scholarship is not full tuition and not a full scholarship \u2014 it is a single \u20ac5,000 grant for the first year, and it is not renewed. Living costs, housing and the balance of tuition remain your responsibility.</div>
      <h2 id="documents">Documents required</h2>
      <p>No standardized document list is published for the scheme as a whole \u2014 <strong>not published in the official notification</strong> as a single list; each institution defines its own. Examples seen on university pages include an application form, a motivation letter or essay, transcripts and diplomas, an English-language test result, and passport or identity proof. Follow the checklist of the institution you apply to.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose a participating Dutch institution and programme</strong>Check that it runs the NL Scholarship for 2026-27 and note its own deadline.</li>
        <li><strong>Apply for admission first</strong>The scholarship is tied to an admission offer \u2014 secure your place at the institution before anything else.</li>
        <li><strong>Follow the institution\u2019s scholarship instructions</strong>Each university has its own application route, selection criteria and required documents.</li>
        <li><strong>Meet that institution\u2019s deadline</strong>There is no central safety net \u2014 a missed university deadline is a missed scholarship.</li>
      </ol>
      <div class="honest-note"><strong>Apply through the university, not to Nuffic:</strong> Nuffic provides the official programme information on the Study in NL site, but applications are submitted through the admissions or scholarship office of your chosen institution.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the Holland NL Scholarship 2026?","The NL Scholarship \u2014 the Holland Scholarship renamed in 2023 \u2014 is a Dutch-government co-funded grant of \u20ac5,000 for non-EEA students in their first year of a full-time bachelor\u2019s or master\u2019s at participating Dutch universities and universities of applied sciences."),
 ("When is the NL Scholarship 2026 deadline?","There is no single deadline: each participating institution sets its own. Some 2026-27 deadlines have already passed and some remain open \u2014 always check your chosen university\u2019s own scholarship page."),
 ("How much does the NL Scholarship pay?","\u20ac5,000 as a one-off grant in the first year of study. It is not full tuition and it is not renewed for later years."),
 ("Who can apply?","Students with non-EEA nationality who have no prior degree from a Dutch institution and who are applying for a full-time bachelor\u2019s or master\u2019s at a participating institution, meeting that institution\u2019s admission requirements."),
 ("How do I apply for the NL Scholarship?","Secure admission at a participating Dutch institution first, then follow that institution\u2019s own scholarship application route. There is no central NL Scholarship application form."),
]),
 verify='Verified 20 Oct 2026 against multiple official Dutch institutional pages (Radboud University, Rotterdam University of Applied Sciences and others) plus Nuffic\u2019s Study in NL programme information: renamed Holland Scholarship \u2192 NL Scholarship in 2023; \u20ac5,000 one-off grant for the first year of study only (not full tuition, not renewable); bachelor\u2019s/master\u2019s scope; non-EEA targeting; no-prior-Dutch-degree rule; typically awarded once; no central deadline and no central application \u2014 each institution sets its own deadline and process. Per-institution deadline caution stated in-article; document list stated as not published as a single scheme-wide list.',
 offlinks=[('Nuffic \u2014 NL Scholarship programme information (official)','https://www.studyinholland.nl/plan-your-stay/scholarships/nl-scholarship'),
           ('Nuffic \u2014 internationalisation in education (official)','https://www.nuffic.nl/en')],
 related_titles=['uaeu-2026','ba-2027','unicef-2026'],
),
dict(
 slug='uae-university-undergraduate-scholarship-2026',
 title='UAE University Undergraduate Scholarship 2026 (Funded) | StudyDesk Scholarships',
 meta='UAE University undergraduate scholarships 2026: 100% tuition discount for Grade 12 \u226598% and 75% for \u226595% \u2014 open to international students. Intake windows, eligibility, renewal rules, and how to apply.',
 short='UAE University Undergraduate Scholarship 2026', kicker='University Scholarship \u00b7 UAE',
 mono='UAEU', prov_short='United Arab Emirates University', prov_long='UAEU, Al Ain, United Arab Emirates', prov_cat='University \u00b7 UAE',
 h1='UAE University Undergraduate Scholarship 2026',
 sub='Study at the UAE\u2019s flagship national university on a merit-based tuition discount \u2014 up to 100% for top Grade 12 achievers, including international students \u2014 with a clear path to renew it every year.',
 dpill='Open \u2014 Sep\u2013Nov intake', dl_long='Not published in the official notification; intake windows: May\u2013Jul (first semester), Sep\u2013Nov (second semester)',
 facts=facts([('Award','100% / 75% tuition discount<small>Grade 12 \u226598% \u2192 100%; \u226595% \u2192 75%</small>'),
              ('Who can apply','New undergraduates<small>Including international students</small>'),
              ('Deadline','Not published<small>Apply within the intake window</small>'),
              ('Renewal','GPA 3.6\u20133.8 + 15 credit hours<small>Per-semester merit requirement</small>'),
              ('Not covered','Housing & admission fees<small>Tuition discount only</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>United Arab Emirates University (UAEU)</strong>, the country\u2019s oldest national research university based in Al Ain, offers <strong>merit-based undergraduate scholarships</strong> that discount tuition fees for high-achieving new students. Students with a Grade 12 average of <strong>98% or above receive a 100% tuition discount</strong>, and those with <strong>95% or above receive 75%</strong>. The scheme is <strong>open to international students</strong>, not only UAE nationals.</p>
      <div class="honest-note"><strong>No fixed deadline published:</strong> UAEU\u2019s official scholarship page does not publish a single application deadline. Admissions run in intake windows \u2014 <strong>May to July for the first semester</strong> and <strong>September to November for the second semester</strong> (the September\u2013November window is open as of 20 October 2026). The official document checklist is also not published; apply through the UAEU admissions office and follow its instructions.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>New undergraduate students</strong> at UAEU, including <strong>international applicants</strong>.</li>
        <li><strong>100% tuition discount:</strong> Grade 12 average of <strong>98% or above</strong>. <strong>75% discount:</strong> <strong>95% or above</strong>.</li>
        <li>Meet <strong>UAEU\u2019s admission requirements</strong> for the chosen college.</li>
        <li><strong>English proficiency:</strong> IELTS 7.5 or 6.5 bands (depending on college) or the equivalent TOEFL score.</li>
        <li><strong>Mathematics proficiency:</strong> SAT-MATH 730 or 660 for colleges that are not otherwise exempt.</li>
        <li><strong>Arabic proficiency</strong> is required for the <strong>College of Law</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% or 75% tuition-fee discount</strong>, depending on the Grade 12 average.</li>
        <li><strong>Renewable:</strong> keep a GPA of <strong>3.6\u20133.8</strong> and complete <strong>15 credit hours</strong> per term to retain the award.</li>
      </ul>
      <div class="honest-note"><strong>Tuition only:</strong> the discount covers tuition fees. <strong>Housing and admission fees are excluded</strong>, and it is not a full-ride scholarship \u2014 plan for accommodation and living costs separately.</div>
      <h2 id="documents">Documents required</h2>
      <p>The official scholarship document list is <strong>not published in the official notification</strong> \u2014 only aggregator-compiled lists exist, which this article does not present as official. Apply through UAEU\u2019s undergraduate admissions and supply whatever the admissions office asks for.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check your Grade 12 average against the tiers</strong>98%+ for full tuition, 95%+ for three-quarters.</li>
        <li><strong>Meet the college\u2019s entry tests</strong>English (IELTS/TOEFL), mathematics (SAT-MATH) and Arabic (Law) where required.</li>
        <li><strong>Apply for undergraduate admission within the intake window</strong>May\u2013July (first semester) or September\u2013November (second semester), via UAEU\u2019s official admissions route.</li>
        <li><strong>Ask the admissions office about the scholarship step</strong>The official page points applicants to the university\u2019s scholarship information; confirm how the discount is attached to your admission.</li>
        <li><strong>Keep your grades up to renew</strong>Aim for a 3.6\u20133.8 GPA and 15 credit hours per term.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much does the UAE University scholarship cover?","A 100% tuition discount for students with a Grade 12 average of 98% or above, and 75% for 95% or above. Housing and admission fees are not covered."),
 ("Can international students apply?","Yes \u2014 UAEU\u2019s merit scholarships are open to new undergraduate students including internationals."),
 ("What is the application deadline?","No fixed deadline is published. UAEU admits in intake windows: May to July for the first semester and September to November for the second semester \u2014 the latter is open as of 20 October 2026."),
 ("How do I keep the scholarship?","Meet the per-term renewal bar: a GPA of roughly 3.6\u20133.8 and 15 credit hours completed."),
 ("What entry tests are needed?","English (IELTS/TOEFL), mathematics (SAT-MATH) for non-exempt colleges, and Arabic for the College of Law \u2014 on top of UAEU\u2019s general admission requirements."),
]),
 verify='Verified 20 Oct 2026 on UAEU\u2019s official undergraduate-scholarships page (uaeu.ac.ae) plus two corroborating trackers: 100% tuition discount at Grade 12 \u226598%, 75% at \u226595%; new undergraduates including international students; excludes housing and admission fees; renewal at GPA 3.6\u20133.8 with 15 credit hours; English IELTS 7.5/6.5 or TOEFL equivalents; SAT-MATH 730/660 for non-exempt colleges; Arabic for Law. No fixed application deadline and no official document list published \u2014 intake windows May\u2013Jul / Sep\u2013Nov stated; both gaps flagged in-article rather than filled from aggregators.',
 offlinks=[('UAEU \u2014 Undergraduate scholarships (official)','https://uaeu.ac.ae/en/admission/undergraduate-scholarships.shtml')],
 related_titles=['nl-2026','membiomed-2027','unicef-2026'],
),
dict(
 slug='unicef-internship-program-2026',
 title='UNICEF Internship Program 2026 (Paid) | StudyDesk Scholarships',
 meta='UNICEF Internship Programme 2026: rolling paid internships (6\u201326 weeks) for enrolled students and recent graduates \u2014 monthly stipend, in-person, remote or hybrid. Eligibility, documents, and how to apply on the UNICEF Careers portal.',
 short='UNICEF Internship Program 2026', kicker='Internship \u00b7 Worldwide',
 mono='UN', prov_short='UNICEF', prov_long='United Nations Children\u2019s Fund, worldwide', prov_cat='UN \u00b7 Worldwide',
 h1='UNICEF Internship Program 2026',
 sub='A paid internship inside the world\u2019s largest children\u2019s organisation: 6 to 26 weeks of hands-on work at UNICEF offices around the globe \u2014 in person, remote or hybrid \u2014 for students and recent graduates.',
 dpill='Rolling \u2014 no fixed deadline', dl_long='Rolling \u2014 each vacancy sets its own closing date',
 facts=facts([('Stipend','Paid monthly<small>Varies by duty station; amount not in official notice</small>'),
              ('Duration','6\u201326 weeks<small>Typical programme length</small>'),
              ('Who can apply','18+ students & recent grads<small>Enrolled, or graduated within 2 years</small>'),
              ('Mode','In-person / remote / hybrid<small>Depends on the vacancy</small>'),
              ('Application fee','None<small>Apply free on UNICEF Careers</small>')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>UNICEF Internship Programme</strong> gives students and recent graduates direct work experience inside the <strong>United Nations Children\u2019s Fund</strong> \u2014 supporting programmes for children\u2019s health, education, nutrition, protection and emergency response. Internships run <strong>6 to 26 weeks</strong>, are <strong>paid with a monthly stipend</strong>, and are offered <strong>in person, remotely or hybrid</strong> depending on the office and role. There is <strong>no single 2026 deadline</strong>: vacancies are advertised year-round and each carries its own closing date, so the programme is effectively rolling.</p>
      <div class="honest-note"><strong>Stipend figures:</strong> UNICEF pays a monthly stipend that varies by duty station, and the official notification pages do not publish a single figure \u2014 third-party guides quote up to USD 1,700/month at major headquarters locations, which this article does not present as official. Check the stipend line in each vacancy before applying. A one-time lump sum towards travel or visa costs may also be granted for some placements.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>At least 18 years old</strong> at the time of application.</li>
        <li><strong>Currently enrolled</strong> in an undergraduate, graduate or PhD programme, <strong>or graduated within the past two years</strong>.</li>
        <li><strong>Strong academic performance</strong> in a relevant field.</li>
        <li><strong>Proficient in at least one UNICEF working language:</strong> English, French or Spanish.</li>
        <li><strong>No immediate relatives</strong> working with UNICEF, and no relatives in the intern\u2019s reporting line.</li>
        <li>Some positions are <strong>nationals-only</strong>; others are open <strong>internationally</strong> \u2014 check each vacancy.</li>
        <li><strong>No prior professional work experience required.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend</strong> (amount varies by duty station).</li>
        <li><strong>Possible one-time lump sum</strong> towards travel or visa costs for some placements.</li>
        <li><strong>Flexible modes:</strong> in-person, remote or hybrid depending on the vacancy.</li>
        <li><strong>No application fee.</strong></li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Applications go through UNICEF\u2019s online recruitment portal: build your <strong>UNICEF Careers profile</strong> and attach a <strong>CV/r\u00e9sum\u00e9</strong> and a <strong>cover letter tailored to the specific role</strong>. Individual vacancies may add their own items \u2014 read the vacancy notice, not a generic checklist.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Browse open internships</strong>Search current internship vacancies on the official UNICEF Careers portal (jobs.unicef.org).</li>
        <li><strong>Check the vacancy\u2019s own closing date</strong>There is no global 2026 deadline \u2014 each posting closes on its own date.</li>
        <li><strong>Create your UNICEF Careers profile</strong>Complete the online recruitment profile carefully.</li>
        <li><strong>Attach a CV and a role-specific cover letter</strong>Tailor both to the team and the work described.</li>
        <li><strong>Submit before that vacancy\u2019s deadline</strong>There is no application fee at any stage.</li>
      </ol>
      <div class="honest-note"><strong>Competition is real:</strong> UNICEF internships attract applicants from every region. Apply to several fitting vacancies rather than waiting on one posting, and never pay anyone who promises a UNICEF placement \u2014 applications are free.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the UNICEF internship paid?","Yes \u2014 interns receive a monthly stipend that varies by duty station. UNICEF does not publish a single official figure; check the vacancy notice for the location-specific amount."),
 ("What is the UNICEF Internship 2026 deadline?","There is no single deadline. Vacancies are advertised year-round on the UNICEF Careers portal, each with its own closing date."),
 ("Who can apply for a UNICEF internship?","Applicants aged 18+ who are enrolled in an undergraduate, graduate or PhD programme \u2014 or graduated within the past two years \u2014 with strong academics and proficiency in English, French or Spanish."),
 ("Can I do the internship remotely?","Yes \u2014 UNICEF offers in-person, remote and hybrid internships depending on the vacancy. The posting states the mode."),
 ("How do I apply?","Through the official UNICEF Careers portal (jobs.unicef.org): build your profile, attach a CV and a tailored cover letter, and submit before the vacancy\u2019s own closing date."),
]),
 verify='Verified 20 Oct 2026 via UNICEF\u2019s official Careers portal (jobs.unicef.org, linked from unicef.org/careers) plus two corroborating guides: rolling vacancies year-round with per-vacancy closing dates (no single 2026 deadline); 6\u201326 week duration; 18+; enrolled or graduated within 2 years; strong academics; English/French/Spanish proficiency; no-relatives rule; nationals-only vs international per vacancy; monthly stipend (duty-station-dependent \u2014 exact figure not in the official notification, so the \u201cUSD 1,700/month\u201d third-party figure is omitted as official fact); possible travel/visa lump sum; no application fee.',
 offlinks=[('UNICEF Careers \u2014 internship vacancies (official)','https://jobs.unicef.org/'),
           ('UNICEF \u2014 internships overview (official)','https://www.unicef.org/about-unicef/internships')],
 related_titles=['ba-2027','nl-2026','membiomed-2027'],
),
dict(
 slug='british-airways-summer-internship-2027-uk',
 title='British Airways Summer Internship 2027 in UK (Paid) | StudyDesk Scholarships',
 meta='British Airways Summer Internship 2027: paid internship at Heathrow on \u00a326,000 pro rata. Deadline 4 November 2026. Open to first/second-year university students with a predicted 2:2, returning to study. How to apply.',
 short='British Airways Summer Internship 2027', kicker='Paid Internship \u00b7 UK',
 mono='BA', prov_short='British Airways', prov_long='British Airways, Heathrow, London, UK', prov_cat='Corporate \u00b7 UK',
 h1='British Airways Summer Internship 2027',
 sub='Spend your summer inside one of the world\u2019s best-known airlines: a paid internship at Heathrow on \u00a326,000 pro rata \u2014 part of British Airways\u2019 Emerging Talent programme for students still working towards their degree.',
 dpill='4 Nov 2026 \u00b7 15 days to go', dl_long='4 Nov 2026',
 facts=facts([('Pay','\u00a326,000 pro rata<small>Per official careers.ba.com listing</small>'),
              ('Who can apply','First/second-year students<small>Predicted 2:2 or above; returning to study</small>'),
              ('Deadline','4 Nov 2026<small>Application + online tests by the deadline</small>'),
              ('Location','Heathrow, London<small>Emerging Talent programme</small>'),
              ('Applications','One Emerging Talent scheme only<small>Only your first application is considered</small>')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>British Airways Summer Internship 2027</strong> is a paid summer placement at <strong>Heathrow</strong> within the airline\u2019s <strong>Emerging Talent</strong> portfolio \u2014 the same family of programmes that includes BA\u2019s graduate schemes and business placements. The internship pays <strong>\u00a326,000 pro rata</strong> per BA\u2019s official careers listing, and the 2027 recruitment window is open now with a <strong>4 November 2026</strong> deadline.</p>
      <div class="honest-note"><strong>Which BA programme is this?</strong> This article covers the <strong>Summer Internship</strong> (students, summer 2027). BA also runs Graduate Programmes, 11-month Business Placements (\u00a326,000 at Heathrow) and Engineering placements \u2014 do not mix their eligibility rules. The 2026 internship cycle closed on 19 November 2025; this article is written for the currently open 2027 cycle.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>university student in your first or second year</strong> at the time of the internship.</li>
        <li><strong>Returning to university</strong> after the internship to complete your studies.</li>
        <li>A <strong>minimum predicted 2:2</strong> (any subject).</li>
        <li><strong>Right to work in the UK</strong> \u2014 no visa sponsorship is offered.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Paid at \u00a326,000 pro rata</strong> for the internship period.</li>
        <li><strong>Graduate network and community</strong> access, with chances to learn from former graduates across BA\u2019s schemes.</li>
        <li><strong>Discounted flights</strong> to travel the world, plus a generous annual-leave entitlement.</li>
        <li>Options to keep going after the summer as a <strong>Campus Ambassador</strong>.</li>
        <li>Community investment and volunteering opportunities, including the <strong>Flying Proud</strong> and <strong>BeMe</strong> networks.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No official document checklist is published \u2014 <strong>not published in the official notification</strong>. The application is submitted through BA\u2019s careers portal with online tests; every section of the application, including all online tests, must be complete by the deadline.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply through BA\u2019s careers portal</strong>Submit your application for the Summer Internship via careers.ba.com (graduates, placements and interns).</li>
        <li><strong>Complete every section plus the online tests</strong>All parts of the application \u2014 including all online tests \u2014 must be finished by the deadline given.</li>
        <li><strong>Video interview</strong>If your online tests go well, you are invited to a short video interview within a set timeframe.</li>
        <li><strong>Submit by 4 November 2026</strong>Missed deadlines mean automatic withdrawal \u2014 applications failing any stage by its deadline are removed.</li>
      </ol>
      <div class="honest-note"><strong>One application only:</strong> because of application volumes, you may apply to only one graduate/Emerging Talent programme \u2014 only your first application will be considered. Read the scheme descriptions before choosing. Also note BA\u2019s recruitment pages encourage preparing your application early rather than waiting for the last evening.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What does the British Airways summer internship pay?","\u00a326,000 pro rata, per BA\u2019s official careers listing for the Summer Internship."),
 ("When is the BA Summer Internship 2027 deadline?","4 November 2026 \u2014 applications and all online tests must be complete by the deadline."),
 ("Who can apply?","University students in their first or second year, returning to study afterwards, with a predicted 2:2 or above (any subject) and the right to work in the UK."),
 ("Where is the internship based?","Heathrow, London, as part of British Airways\u2019 Emerging Talent programme."),
 ("Can international students apply?","Only if you have the right to work in the UK \u2014 BA offers no visa sponsorship for the internship."),
]),
 verify='Verified 20 Oct 2026 on BA\u2019s official careers portal (careers.ba.com, graduates/BPS/interns) plus BA\u2019s Bright Network partner page (crawled 1 hour before this run): Summer Internship 2027, Heathrow, \u00a326,000 pro rata, deadline 4 Nov 2026 (currently open); first/second-year university students returning to study; minimum predicted 2:2 any subject; UK right to work, no visa sponsorship; one-application rule (only first application considered); application + online tests complete by deadline; video interview for those who clear the tests. The 2026 cycle (closed 19 Nov 2025) is superseded \u2014 article is written for the open 2027 cycle. Document checklist not published in the official notification \u2014 stated as such.',
 offlinks=[('British Airways careers \u2014 graduates, placements and interns (official)','https://careers.ba.com/graduates-bps-and-interns'),
           ('British Airways on Bright Network (official partner page)','https://www.brightnetwork.co.uk/graduate-employer-company/british-airways/')],
 related_titles=['unicef-2026','uaeu-2026','nl-2026'],
),
dict(
 slug='erasmus-mundus-membiomed-scholarship-2027',
 title='Erasmus Mundus MemBioMed Scholarship 2027 in Europe (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus MemBioMed Scholarship 2027: \u20ac1,400/month for 24 months plus full tuition for the \u201cFrom Membrane Biology to Neuroscience and Experimental Medicine\u201d master\u2019s \u2014 15 scholarships per cohort. Applications open 1 December 2026. Eligibility, documents, how to apply.',
 short='Erasmus Mundus MemBioMed 2027', kicker='Erasmus Mundus \u00b7 Europe',
 mono='MB', prov_short='MemBioMed consortium (Universit\u00e9 C\u00f4te d\u2019Azur)', prov_long='MemBioMed consortium: Universit\u00e9 C\u00f4te d\u2019Azur (France), University of Genoa (Italy), Osnabr\u00fcck University (Germany)', prov_cat='Erasmus Mundus \u00b7 Europe',
 h1='Erasmus Mundus MemBioMed Scholarship 2027',
 sub='Two years of fully funded neuroscience master\u2019s study across France, Italy and Germany: \u20ac1,400 a month for 24 months plus full tuition \u2014 open to students from every country.',
 dpill='Opens 1 Dec 2026', dl_long='Applications open 1 Dec 2026; closing date not yet published',
 facts=facts([('Award','\u20ac1,400/month \u00d7 24<small>\u20ac33,600 total + full tuition</small>'),
              ('Scholarships','15 per cohort<small>Erasmus Mundus Joint Master</small>'),
              ('Opens','1 Dec 2026<small>2027\u20132029 cohort</small>'),
              ('Who can apply','All nationalities<small>180 ECTS bachelor\u2019s in biology/life sciences</small>'),
              ('Route','France \u2192 Italy \u2192 Germany<small>2-year joint master\u2019s</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>MemBioMed</strong> is an <strong>Erasmus Mundus Joint Master</strong> \u2014 officially titled <strong>\u201cFrom Membrane Biology to Neuroscience and Experimental Medicine\u201d</strong> \u2014 co-funded by the European Union. Three partner universities drive the programme: <strong>Universit\u00e9 C\u00f4te d\u2019Azur</strong> in France (the coordinator), the <strong>University of Genoa</strong> in Italy, and <strong>Osnabr\u00fcck University</strong> in Germany. Each cohort has <strong>15 Erasmus Mundus scholarships</strong>, each worth <strong>\u20ac1,400 per month for 24 months</strong> plus <strong>full tuition</strong>. Applications for the <strong>2027\u20132029 cohort open on 1 December 2026</strong>.</p>
      <div class="honest-note"><strong>Not \u201cbiomedical engineering\u201d:</strong> many third-party blogs mislabel this as a biomedical engineering scholarship. The official programme is a neuroscience and experimental-medicine master\u2019s built around biomembranes \u2014 apply only if that is the field you actually want to study. Also note the 2026\u20132028 cohort is closed; this article is written for the newly announced 2027\u20132029 cycle.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>All nationalities</strong> may apply.</li>
        <li>A <strong>bachelor\u2019s degree worth 180 ECTS</strong> in <strong>biology, life sciences or a related field</strong>.</li>
        <li><strong>English at B2 level</strong> or above (e.g. IELTS 6.5, TOEFL iBT 93 or equivalent).</li>
      </ul>
      <div class="honest-note"><strong>Closing date not yet published:</strong> the official consortium page confirms the 1 December 2026 opening but has not announced the 2027\u20132029 application deadline. Do not trust a closing date from a third-party site \u2014 watch the official page and prepare your documents now so you can apply the week it opens.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac1,400 per month for 24 months</strong> (\u20ac33,600 total living support).</li>
        <li><strong>Full tuition coverage.</strong></li>
        <li>Study mobility across <strong>three European countries</strong> (France, Italy, Germany).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the official consortium guidance: the <strong>online application form</strong>; a <strong>Europass CV</strong>; a <strong>motivation letter</strong>; <strong>transcripts and your bachelor\u2019s diploma with an English translation</strong>; a <strong>course list with grades</strong>; <strong>two recommendation letters</strong>; <strong>proof of English proficiency</strong>; and a <strong>passport or ID copy</strong>. Apply through the consortium\u2019s e-candidat portal.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the official consortium page</strong>Confirm the 2027\u20132029 call details on life.univ-cotedazur.eu/international/membiomed.</li>
        <li><strong>Prepare your documents early</strong>Transcripts with English translations and two recommendation letters take the longest \u2014 start now.</li>
        <li><strong>Apply through the e-candidat portal</strong>Once applications open on <strong>1 December 2026</strong>, submit the online form and upload everything.</li>
        <li><strong>Watch for the closing date</strong>It has not been announced yet \u2014 do not wait for a reminder; set your own early target.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When do MemBioMed 2027 applications open?","1 December 2026, for the 2027\u20132029 cohort. The closing date has not been announced yet on the official page."),
 ("What does the MemBioMed scholarship cover?","\u20ac1,400 per month for 24 months (\u20ac33,600) plus full tuition \u2014 15 Erasmus Mundus scholarships are available per cohort."),
 ("What is MemBioMed, exactly?","An Erasmus Mundus Joint Master titled \u201cFrom Membrane Biology to Neuroscience and Experimental Medicine\u201d \u2014 a two-year neuroscience master\u2019s run by Universit\u00e9 C\u00f4te d\u2019Azur (coordinator), the University of Genoa and Osnabr\u00fcck University. It is not a biomedical engineering programme."),
 ("Who can apply?","Students of all nationalities with a 180-ECTS bachelor\u2019s in biology, life sciences or a related field, and English at B2 level or above."),
 ("How do I apply?","Through the consortium\u2019s e-candidat portal (linked from the official MemBioMed page at life.univ-cotedazur.eu), with a Europass CV, motivation letter, transcripts and diploma with English translations, course list with grades, two recommendation letters, English proof and passport/ID."),
]),
 verify='Verified 20 Oct 2026 on the official MemBioMed consortium pages (life.univ-cotedazur.eu/international/membiomed + official October 2026 EMJM brochure, univ-cotedazur.fr), independently re-checked this run via search: programme title \u201cFrom Membrane Biology to Neuroscience and Experimental Medicine\u201d (blogs mislabeling it \u201cBiomedical Engineering\u201d corrected); coordinator Universit\u00e9 C\u00f4te d\u2019Azur with University of Genoa and Osnabr\u00fcck University; 15 Erasmus Mundus scholarships per cohort at \u20ac1,400/month for 2 years + full tuition; 2027\u20132029 cohort applications open 1 Dec 2026 (2026\u20132028 cohort closed); all nationalities; 180-ECTS bachelor\u2019s in biology/life sciences or related; English B2 (IELTS 6.5 / TOEFL iBT 93); documents per official guidance; e-candidat portal. Closing deadline not yet published on official pages \u2014 flagged in-article, not invented.',
 offlinks=[('MemBioMed consortium \u2014 official page (Universit\u00e9 C\u00f4te d\u2019Azur)','https://life.univ-cotedazur.eu/international/membiomed'),
           ('MemBioMed \u2014 official EMJM brochure, Oct 2026 (PDF)','https://univ-cotedazur.fr/medias/fichier/brochure-emjm-membiomed-web-oct2026_1791564750403-pdf')],
 related_titles=['uaeu-2026','unicef-2026','nl-2026'],
),
]

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# registry appends
import io
reg = pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').read_text()
assert "'membiomed-2027'" not in reg, 'registry already has batch 25 cards'
newcards = """\
 'nl-2026': {'mono': 'NL', 'title': 'Holland NL Scholarship 2026 in Holland (Funded)', 'href': 'holland-nl-scholarship-2026-holland.html',
              'dpill': 'Varies by university', 'award': '\\u20ac5,000 one-off (first year only)', 'elig': 'Non-EEA; full-time bachelor\\u2019s/master\\u2019s; no prior Dutch degree.',
              'tags': [('Government', 'blue'), ('Netherlands', 'teal')]},
 'uaeu-2026': {'mono': 'UAEU', 'title': 'UAE University Undergraduate Scholarship 2026 (Funded)', 'href': 'uae-university-undergraduate-scholarship-2026.html',
              'dpill': 'Open \\u2014 Sep\\u2013Nov intake', 'award': '100% tuition (Grade 12 \\u226598%); 75% (\\u226595%)', 'elig': 'New undergrads incl. international; UAEU admission requirements.',
              'tags': [('University', 'blue'), ('UAE', 'teal')]},
 'unicef-2026': {'mono': 'UN', 'title': 'UNICEF Internship Program 2026 (Paid)', 'href': 'unicef-internship-program-2026.html',
              'dpill': 'Rolling \\u2014 no fixed deadline', 'award': 'Monthly stipend (varies by duty station)', 'elig': '18+; enrolled or graduated within 2 years.',
              'tags': [('Internship', 'blue'), ('Worldwide', 'teal')]},
 'ba-2027': {'mono': 'BA', 'title': 'British Airways Summer Internship 2027 in UK (Paid)', 'href': 'british-airways-summer-internship-2027-uk.html',
              'dpill': '4 Nov 2026 \\u00b7 15 days to go', 'award': '\\u00a326,000 pro rata', 'elig': 'First/second-year uni students; 2:2 predicted; right to work in UK.',
              'tags': [('Internship', 'blue'), ('UK', 'teal')]},
 'membiomed-2027': {'mono': 'MB', 'title': 'Erasmus Mundus MemBioMed Scholarship 2027 in Europe (Fully Funded)', 'href': 'erasmus-mundus-membiomed-scholarship-2027.html',
              'dpill': 'Opens 1 Dec 2026', 'award': '\\u20ac1,400/month \\u00d7 24 + full tuition', 'elig': 'All nationalities; 180 ECTS bachelor\\u2019s in biology/life sciences.',
              'tags': [('Master\\u2019s', 'blue'), ('Europe', 'teal')]},
"""
reg = reg.rstrip()
assert reg.endswith('}')
reg = reg[:-1] + newcards + '}\n'
pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').write_text(reg)
print('registry appended')

# logos INFO appends
logof = pathlib.Path('/home/hatch/workspace/scholarships-17k/add-logos.py')
lt = logof.read_text()
add = """\
 'holland-nl-scholarship-2026-holland': ('Nuffic', 'Government \\u00b7 Netherlands', 'nuffic'),
 'uae-university-undergraduate-scholarship-2026': ('UAE University', 'University \\u00b7 UAE', 'uaeu'),
 'unicef-internship-program-2026': ('UNICEF', 'UN \\u00b7 Worldwide', 'unicef'),
 'british-airways-summer-internship-2027-uk': ('British Airways', 'Corporate \\u00b7 UK', 'ba'),
 'erasmus-mundus-membiomed-scholarship-2027': ('MemBioMed consortium', 'Erasmus Mundus \\u00b7 Europe', 'membiomed'),
"""
m = lt.find("\n}\n", lt.find('INFO = {'))
assert m != -1, 'INFO dict end not found'
lt = lt[:m] + "\n" + add.rstrip("\n") + lt[m:]
logof.write_text(lt)
print('add-logos INFO appended')

# validate HTML
from html.parser import HTMLParser
class P(HTMLParser):
    def error(self, message): raise ValueError(message)
for a in ARTICLES:
    p = P(); p.feed(pathlib.Path(OUT / (a['slug'] + '.html')).read_text())
    print('validated', a['slug'])

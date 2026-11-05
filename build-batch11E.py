#!/usr/bin/env python3
"""Batch 11E: 9 verified international articles. Verified 16 Oct 2026. (Assas Eiffel skipped: same program as Eiffel Excellence.)"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'oise-toronto': dict(mono='UT', title='University of Toronto OISE Graduate Funding 2027', href='toronto-oise-graduate-funding-2027.html',
              dpill='Open now', award='Up to CAD $40,000 (PhD)', elig='Full-time PhD/SJD or non-professional MA at OISE; funded cohort.',
              tags=[('Master\u2019s/PhD','blue'),('Canada','teal')]),
 'ubd-grad': dict(mono='UBD', title='UBD Graduate Scholarship 2027, Brunei (Fully Funded)', href='ubd-graduate-scholarship-2027-brunei.html',
              dpill='15 days to go', award='Full tuition + BND 1,200\u20132,200/month', elig='First-class bachelor\u2019s (master\u2019s) / master\u2019s (PhD); research proposal.',
              tags=[('Master\u2019s/PhD','blue'),('Brunei','teal')]),
 'ceu-hungary': dict(mono='CEU', title='Central European University Scholarships 2027, Hungary', href='ceu-scholarships-2027-hungary.html',
              dpill='109 days to go', award='Up to 100% tuition + \u20ac1,000/month', elig='UG/PG/PhD applicants; English proficiency; academic merit.',
              tags=[('UG/PG/PhD','blue'),('Hungary','teal')]),
 'aixbio': dict(mono='AX', title='AIxBio Research Fellowship 2027, Cambridge UK', href='aixbio-research-fellowship-2027.html',
              dpill='3 days to go', award='\u00a310,000 stipend + travel/visa', elig='18+; any background; no formal research experience needed.',
              tags=[('Fellowship','blue'),('UK','teal')]),
 'yeungnam': dict(mono='YU', title='Yeungnam University PSPS Scholarship 2027, South Korea', href='yeungnam-psps-scholarship-2027-korea.html',
              dpill='7 days to go', award='Full tuition + KRW 1,000,000/month \u00d7 12', elig='International; bachelor\u2019s degree; IELTS 5.5 or MOI.',
              tags=[('Master\u2019s','blue'),('South Korea','teal')]),
 'glocal': dict(mono='EM', title='Erasmus Mundus GLOCAL Scholarship 2027', href='erasmus-mundus-glocal-scholarship-2027.html',
              dpill='90 days to go', award='\u20ac1,400/month + full tuition', elig='Bachelor\u2019s; Glasgow offer; no prior EMJM; all nationalities.',
              tags=[('Master\u2019s','blue'),('Europe','teal')]),
 'eiffel': dict(mono='EF', title='France Excellence Eiffel Scholarship 2027', href='eiffel-excellence-scholarship-2027-france.html',
              dpill='82 days to go', award='\u20ac1,200/month (Master\u2019s) · \u20ac2,100/month (PhD)', elig='International; nominated by French institution; age limits apply.',
              tags=[('Master\u2019s/PhD','blue'),('France','teal')]),
 'justcool': dict(mono='JC', title='JUSTCOOL PhD Scholarship 2027, China', href='justcool-phd-scholarship-2027-china.html',
              dpill='29 days to go', award='Fellowship + tuition waiver + housing', elig='Non-Chinese bachelor\u2019s; top 20% rank; Maths/Physics/Chem/Bio.',
              tags=[('PhD','blue'),('China','teal')]),
 'ippa-ws': dict(mono='IP', title='IPPA Chiang Mai Winter School 2026, Thailand', href='ippa-chiang-mai-winter-school-2026.html',
              dpill='4 days to go', award='Funded 5-day training (selected)', elig='Early-career public-policy researchers; all nationalities.',
              tags=[('Winter School','blue'),('Thailand','teal')]),
}

ARTICLES = [
dict(
 slug='toronto-oise-graduate-funding-2027',
 title='University of Toronto OISE Graduate Funding 2027 | StudyDesk Scholarships',
 meta='OISE graduate funding 2027: up to CAD $40,000 for PhD and at least CAD $26,892 for first-year MA students at the University of Toronto. No separate application.',
 short='OISE Graduate Funding 2027', kicker='Canada \u00b7 Master\u2019s/PhD \u00b7 International',
 mono='UT', prov_short='University of Toronto \u2014 OISE', prov_long='Ontario Institute for Studies in Education, University of Toronto',
 prov_cat='University',
 h1='University of Toronto OISE Graduate Funding 2027',
 sub='Up to CAD $40,000 a year for PhD students \u2014 automatic funding packages for eligible OISE graduate students.',
 dpill='Open now', dl_long='Rolling \u2014 no fixed deadline',
 facts=facts([('Award','Up to CAD $40,000 / year<small>PhD/SJD base funding</small>'),
              ('MA funding','At least CAD $26,892.39<small>Year-1 MA, 2026\u201327</small>'),
              ('Who can apply','Full-time PhD/SJD + MA<small>OISE funded cohort</small>'),
              ('Application','No separate form<small>Assessed with admission</small>'),
              ('Extras','UHIP for internationals<small>+ GA/TA positions</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Ontario Institute for Studies in Education (OISE)</strong> at the <strong>University of Toronto</strong> provides <strong>graduate funding packages</strong> to eligible students in full-time doctoral programmes and non-professional Master of Arts (MA) programmes. There is <strong>no separate application</strong>: eligible students are assessed automatically and receive their funding details with the admission offer.</p>
      <p>For 2026\u201327, the base funding commitment is <strong>CAD $40,000 for PhD/SJD students</strong> (inclusive of tuition and incidental fees), and <strong>at least CAD $26,892.39 for first-year MA students</strong>. International students get additional support for the mandatory University Health Insurance Plan (UHIP).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Admitted to a <strong>full-time PhD/SJD programme</strong> at OISE, or a <strong>non-professional MA programme</strong> (funded cohort).</li>
        <li>Meet the <strong>terms and conditions of funding each year</strong> to stay in the funded cohort.</li>
        <li>Students eligible for <strong>Graduate Assistantships (GA)</strong> must apply for and accept those positions as part of the package.</li>
        <li>All nationalities, including international students.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>PhD/SJD:</strong> base funding package of <strong>CAD $40,000</strong>, inclusive of tuition and incidental fees.</li>
        <li><strong>MA (year 1):</strong> funding package of <strong>at least CAD $26,892.39</strong>.</li>
        <li><strong>UHIP support</strong> for eligible international students.</li>
        <li>Packages may combine <strong>fellowships, grants, awards, scholarships and paid GA/TA employment</strong>.</li>
        <li>Students can also apply for external awards such as the <strong>Ontario Graduate Scholarship (OGS)</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>OISE graduate admission application (online)</li><li>Academic transcripts</li><li>Statement of intent / research interests</li>
        <li>Letters of reference</li><li>CV</li><li>English proficiency proof (if required)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to OISE</strong>Choose your PhD or MA programme and submit the graduate application.</li>
        <li><strong>You are assessed automatically</strong>There is no separate funding application \u2014 eligible students get funding details with the offer.</li>
        <li><strong>Accept GA/TA positions if offered</strong>These form part of the package; declining forfeits that component.</li>
      </ol>
      <div class="honest-note"><strong>Not a cash handout:</strong> the package value includes tuition and fees \u2014 it is not necessarily paid out as a lump-sum stipend. Read the funding letter carefully.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate application?","No \u2014 eligible students are assessed automatically with their admission application."),
 ("How much is the PhD funding?","The base commitment is CAD $40,000 per year, inclusive of tuition and incidental fees."),
 ("Do international students get health insurance?","Yes \u2014 the package value is increased to cover the mandatory UHIP for eligible international students."),
 ("Is there a deadline?","Funding follows the admission cycle; there is no separate published deadline for the package itself."),
]),
 verify='Verified 16 Oct 2026 against the official OISE graduate funding page (CAD $40,000 PhD/SJD base from Fall 2025; at least CAD $26,892.39 year-1 MA 2026\u201327; UHIP top-up; no separate application) and Bright Scholarship + GlobalSouthOpportunities listings (same figures).',
 offlinks=[('OISE Graduate Funding (official)','https://www.oise.utoronto.ca/home/registrar-students/grad-funding')],
 related_titles=['griffith-vc','hanns-seidel','swiss-phd'],
),

dict(
 slug='ubd-graduate-scholarship-2027-brunei',
 title='UBD Graduate Scholarship 2027, Brunei (Fully Funded) | StudyDesk Scholarships',
 meta='UBD Graduate Scholarship 2027: full tuition waiver, monthly subsistence allowance, free accommodation and airfare at Universiti Brunei Darussalam. Deadline 31 Oct 2026.',
 short='UBD Graduate Scholarship 2027', kicker='Brunei \u00b7 Master\u2019s/PhD \u00b7 International',
 mono='UBD', prov_short='Universiti Brunei Darussalam', prov_long='Universiti Brunei Darussalam (UBD), Bandar Seri Begawan',
 prov_cat='University',
 h1='UBD Graduate Scholarship 2027, Brunei (Fully Funded)',
 sub='Full tuition waiver, monthly living allowance and free accommodation \u2014 for the February 2027 intake at Brunei\u2019s top university.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','Full tuition waiver<small>+ monthly allowance</small>'),
              ('Allowance','BND 1,200\u20132,200 / month<small>Up to 36 months</small>'),
              ('Who can apply','Master\u2019s / PhD applicants<small>All nationalities</small>'),
              ('Deadline','31 Oct 2026<small>Feb 2027 intake</small>'),
              ('Extras','Free housing + airfare<small>+ research funding</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>UBD Graduate Research Scholarship (UGRS)</strong> at <strong>Universiti Brunei Darussalam</strong> \u2014 Brunei\u2019s leading university, ranked in the QS top 300 \u2014 funds <strong>Master\u2019s and PhD</strong> study for the <strong>February 2027 intake</strong>. It is open to <strong>Brunei citizens and international students</strong>, with <strong>no application fee</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>all nationalities</strong> (Brunei and non-Brunei).</li>
        <li>Master\u2019s: <strong>first-class bachelor\u2019s degree</strong> (or equivalent).</li>
        <li>PhD: <strong>master\u2019s degree</strong> in a relevant field.</li>
        <li><strong>High-quality research proposal</strong> in the chosen area.</li>
        <li>Meet UBD\u2019s <strong>English language requirements</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver</strong>, including registration and acceptance fees.</li>
        <li><strong>Monthly subsistence allowance</strong> (UBD\u2019s published graduate terms list BND 1,200\u20132,200 per month, up to 36 months, depending on the award).</li>
        <li><strong>Free on-campus accommodation.</strong></li>
        <li><strong>Return economy airfare</strong> for candidates outside Brunei.</li>
        <li><strong>Research/conference funding</strong> and visa fee coverage.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online admission application (OASys)</li><li>Degree certificates + transcripts</li><li>Research proposal</li>
        <li>CV</li><li>Passport copy</li><li>English proficiency proof</li><li>Reference letters</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply through UBD\u2019s Online Admission System (OASys)</strong>Scholarship consideration is part of the admission application.</li>
        <li><strong>Upload all documents</strong>Incomplete applications are not entertained.</li>
        <li><strong>Submit before 31 October 2026</strong>For the February 2027 intake.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What does it cover?","Tuition waiver, monthly subsistence allowance, free on-campus accommodation, return airfare and research funding."),
 ("Who can apply?","Brunei citizens and international students for Master\u2019s and PhD programmes."),
 ("Is there an application fee?","No \u2014 applications are free."),
 ("When is the deadline?","31 October 2026 for the February 2027 graduate intake."),
]),
 verify='Verified 16 Oct 2026 against the official UBD UGRS page (tuition waiver; BND 1,200/month subsistence; free accommodation; airfare; OASys route) and Bright Scholarship + OpportunityPortal listings (31 Oct 2026 deadline; BND 2,200 figure on the broader graduate scheme; Feb 2027 intake).',
 offlinks=[('UBD Graduate Research Scholarship (official)','https://ubd.edu.bn/admission/graduate/graduate-fees-funding/ugrs/')],
 related_titles=['griffith-vc','hanns-seidel','swiss-phd'],
),

dict(
 slug='ceu-scholarships-2027-hungary',
 title='Central European University Scholarships 2027, Hungary | StudyDesk Scholarships',
 meta='CEU Scholarships 2027: up to 100% tuition + \u20ac1,000/month master\u2019s stipends and doctoral fellowships in Hungary. Next deadline 2 Feb 2027.',
 short='CEU Scholarships 2027', kicker='Hungary \u00b7 UG/PG/PhD \u00b7 International',
 mono='CEU', prov_short='Central European University', prov_long='Central European University (CEU), Vienna\u2013Budapest',
 prov_cat='University',
 h1='Central European University Scholarships 2027, Hungary',
 sub='Up to 100% tuition plus monthly stipends \u2014 for Bachelor\u2019s, Master\u2019s and PhD study at CEU.',
 dpill='109 days to go', dl_long='2 Feb 2027',
 facts=facts([('Award','Up to 100% tuition<small>+ monthly stipend</small>'),
              ('Master\u2019s stipend','\u20ac500\u2013\u20ac1,000 / month<small>By merit tier</small>'),
              ('Who can apply','UG / Master\u2019s / PhD<small>All nationalities</small>'),
              ('Deadline','2 Feb 2027<small>Round 2</small>'),
              ('Language','All courses in English<small>Budapest + Vienna</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Central European University (CEU)</strong> \u2014 an international graduate university with campuses in <strong>Vienna and Budapest</strong> \u2014 awards <strong>merit-based scholarships</strong> across its Bachelor\u2019s, Master\u2019s and PhD programmes. Over 80% of CEU students receive some form of financial aid. Awards combine <strong>tuition coverage (up to 100%)</strong> with <strong>monthly stipends and health insurance</strong>.</p>
      <div class="honest-note"><strong>Round 1 closed 15 October 2026.</strong> The next window is <strong>Round 2, closing 2 February 2027</strong> (financial aid open in Round 2; applicants from visa-sensitive countries should check eligibility for later rounds).</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying to a <strong>CEU Bachelor\u2019s, Master\u2019s or PhD programme</strong>.</li>
        <li><strong>Strong academic record</strong> \u2014 scholarships are awarded on merit (and need, for some tiers).</li>
        <li><strong>English proficiency</strong> (exemptions for prior English-taught degrees from listed countries).</li>
        <li>PhD: <strong>master\u2019s degree</strong> required.</li>
        <li>All nationalities welcome.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition:</strong> up to <strong>100% coverage</strong>.</li>
        <li><strong>Master\u2019s stipends:</strong> \u20ac1,000/month (Excellence), \u20ac750/month (Distinction), \u20ac500/month (Master\u2019s Scholarship).</li>
        <li><strong>Doctoral fellowship:</strong> monthly stipend plus health insurance.</li>
        <li><strong>Health insurance</strong> and housing/living support.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application form</li><li>Degree certificates + transcripts</li><li>CV</li>
        <li>Statement of purpose</li><li>Recommendation letters</li><li>Research proposal (PhD / some master\u2019s)</li><li>English proficiency proof</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Create an account on CEU\u2019s online application portal</strong>Pick your programme and check its requirements.</li>
        <li><strong>Submit the application + documents</strong>Pay the \u20ac30 application fee.</li>
        <li><strong>Meet the 2 February 2027 Round 2 deadline</strong>Scholarship consideration is automatic with admission.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the next deadline?","Round 2 closes 2 February 2027. Round 1 (15 Oct 2026) has closed."),
 ("How much can I get?","Up to 100% tuition plus \u20ac500\u2013\u20ac1,000/month for master\u2019s students; doctoral fellowships for PhD students."),
 ("Are courses in English?","Yes \u2014 all CEU programmes are taught in English."),
 ("Is there a separate scholarship form?","No \u2014 you are considered for financial aid through the admission application."),
]),
 verify='Verified 16 Oct 2026 via OpportunityPortal (Round 1: 15 Oct 2026; Round 2: 2 Feb 2027; aid open in Rounds 1\u20132), ScholarshipForPhD (stipend tiers \u20ac500\u2013\u20ac1,000; doctoral stipend) and the official CEU admissions page (online application; \u20ac30 fee).',
 offlinks=[('CEU Admissions (official)','https://ceu.edu/admissions')],
 related_titles=['hanns-seidel','griffith-vc','epfl-summer'],
),
]
ARTICLES += [
dict(
 slug='aixbio-research-fellowship-2027',
 title='AIxBio Research Fellowship 2027, Cambridge UK | StudyDesk Scholarships',
 meta='AIxBio Research Fellowship 2027: \u00a310,000 stipend for 10 weeks in Cambridge, UK on AI and biosecurity. No formal research experience required. Deadline 19 Oct 2026.',
 short='AIxBio Fellowship 2027', kicker='UK \u00b7 Fellowship \u00b7 International',
 mono='AX', prov_short='ERA + Cambridge Biosecurity Hub', prov_long='ERA, in partnership with the Cambridge Biosecurity Hub',
 prov_cat='Research Organisation',
 h1='AIxBio Research Fellowship 2027, Cambridge UK',
 sub='\u00a310,000 for 10 weeks in Cambridge \u2014 work on AI and biosecurity with expert mentors. No formal research background required.',
 dpill='3 days to go', dl_long='19 Oct 2026',
 facts=facts([('Award','\u00a310,000 stipend<small>10-week programme</small>'),
              ('Who can apply','Aged 18+<small>Any background; worldwide</small>'),
              ('When','18 Jan \u2013 26 Mar 2027<small>In person, Cambridge</small>'),
              ('Deadline','19 Oct 2026<small>Rolling review \u2014 apply early</small>'),
              ('Extras','Travel + visa + meals<small>+ mentors, workspace</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>AIxBio Research Fellowship (Winter 2027)</strong>, run by <strong>ERA in partnership with the Cambridge Biosecurity Hub</strong>, is a <strong>10-week, full-time, in-person programme in Cambridge, UK</strong> for people working at the intersection of <strong>advanced AI and biosecurity</strong>. Around <strong>10\u201315 fellows</strong> are selected for research, placement or founding tracks, each producing a written output such as a policy brief or technical report.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>18 or older</strong> by 18 January 2027.</li>
        <li>Open to <strong>all nationalities and backgrounds</strong> \u2014 students, engineers, policy professionals, founders.</li>
        <li><strong>No formal research experience required</strong> \u2014 what matters is reasoning ability and commitment to the mission.</li>
        <li>Available <strong>full-time, in person in Cambridge</strong> for the whole 10 weeks (remote participation generally not possible).</li>
        <li>Valid passport for international fellows (visa sponsorship available for most countries).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u00a310,000 total stipend</strong> for the programme.</li>
        <li><strong>Travel to/from Cambridge and visa costs</strong> covered.</li>
        <li><strong>Meals during working hours</strong>, dedicated workspace, project funding.</li>
        <li><strong>Expert mentors + dedicated research managers</strong>, talks and workshops.</li>
        <li>Support letters for employers/institutions if you need leave.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online written application (background, interests, reasoning)</li><li>CV (as requested in the form)</li><li>References (if shortlisted)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the fellowship and FAQ pages</strong>Pick your track: Research, Placement or Founding.</li>
        <li><strong>Submit the written application</strong>Through the official form \u2014 quality of reasoning matters more than polish.</li>
        <li><strong>Interview + possible work tests</strong>Shortlisted candidates meet the ERA team.</li>
        <li><strong>Apply before 19 October 2026</strong>Review is rolling, so earlier is better.</li>
      </ol>
      <div class="honest-note"><strong>Not a University of Cambridge scholarship.</strong> AIxBio is run by ERA with the Cambridge Biosecurity Hub \u2014 accommodation is not provided (guidance on shared housing is offered).</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need research experience?","No \u2014 it is helpful but not required. Strong reasoning and a clear problem focus matter most."),
 ("Is it remote?","No \u2014 it is full-time and in person in Cambridge, with exceptions only for exceptional candidates."),
 ("What are the tracks?","Research, Placement (with a biosecurity team) and Founding (testing whether a gap needs a new organisation)."),
 ("When does it run?","18 January to 26 March 2027."),
]),
 verify='Verified 16 Oct 2026 against the official AIxBio fellowship + FAQ pages (\u00a310,000; 19 Oct 2026; 18 Jan\u201326 Mar 2027; 18+; no formal experience required; visa sponsorship; ~10\u201315 fellows) and Al-Khwarizmi + OpportunitiesRadar listings (same dates and terms).',
 offlinks=[('AIxBio Fellowship (official)','https://www.aixbiosecurity.com/fellowship')],
 related_titles=['nasa-hubble','epfl-summer','wb-gaf'],
),

dict(
 slug='yeungnam-psps-scholarship-2027-korea',
 title='Yeungnam University PSPS Scholarship 2027, South Korea | StudyDesk Scholarships',
 meta='Yeungnam PSPS Scholarship 2027: full tuition for 4 semesters + KRW 1,000,000/month living allowance for international master\u2019s students. Deadline 23 Oct 2026.',
 short='Yeungnam PSPS Scholarship 2027', kicker='South Korea \u00b7 Master\u2019s \u00b7 International',
 mono='YU', prov_short='Yeungnam University \u2014 PSPS', prov_long='Park Chung Hee School of Policy and Saemaul, Yeungnam University',
 prov_cat='University',
 h1='Yeungnam University PSPS Scholarship 2027, South Korea',
 sub='Full tuition for all four semesters plus KRW 1,000,000 a month \u2014 for international master\u2019s students at PSPS, Spring 2027.',
 dpill='7 days to go', dl_long='23 Oct 2026',
 facts=facts([('Award','Full tuition \u00d7 4 semesters<small>+ living allowance</small>'),
              ('Allowance','KRW 1,000,000 / month<small>12 months, Mar 2027\u2013Feb 2028</small>'),
              ('Who can apply','International students<small>Bachelor\u2019s degree holders</small>'),
              ('Deadline','23 Oct 2026<small>Docs by 30 Oct</small>'),
              ('Language','English-taught programmes<small>IELTS 5.5 or MOI</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>PSPS General Scholarship</strong> at the <strong>Park Chung Hee School of Policy and Saemaul (PSPS), Yeungnam University</strong>, South Korea, is awarded to <strong>every admitted international student</strong> for the <strong>Spring 2027</strong> intake. PSPS shares Korea\u2019s development experience through English-taught master\u2019s programmes in public policy, public administration, and forest and environmental policy.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Korean citizen</strong> (neither applicant nor parents may be Korean citizens).</li>
        <li><strong>Bachelor\u2019s degree</strong> comparable to a four-year Korean degree.</li>
        <li><strong>English proficiency:</strong> IELTS 5.5, TOEFL iBT 71, TOEIC 750, CEFR B2 \u2014 or an official medium-of-instruction statement if the bachelor\u2019s was taught in English.</li>
        <li>Good health; able to attend daytime classes in Korea.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver for all four semesters.</strong></li>
        <li><strong>Admission fee waiver.</strong></li>
        <li><strong>KRW 1,000,000 per month living allowance</strong> for 12 months (March 2027 \u2013 February 2028).</li>
        <li>Certificate of Admission + Scholarship for the <strong>D-2 student visa</strong>.</li>
        <li>Maintain a <strong>GPA of 3.0/4.5</strong> with no F grades to keep funding.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed application form</li><li>Degree certificate + transcripts</li><li>CV</li>
        <li>Personal statement</li><li>English proof (or MOI statement)</li><li>Recommendation letters</li>
        <li>Passport; parents\u2019 nationality proof; birth certificate</li><li>Application fee payment receipt (KRW 100,000 / USD 80)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Fill the forms on the PSPS admissions page</strong>Select your degree and major; print and sign where required.</li>
        <li><strong>Pay the non-refundable fee</strong>KRW 100,000 (or USD 80) by <strong>23 Oct 2026, 2 PM KST</strong>.</li>
        <li><strong>Email scanned documents</strong>To the PSPS admissions email by <strong>30 Oct 2026</strong>; watch for interview requests.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What exactly is covered?","Full tuition for four semesters, admission fee waiver, and KRW 1,000,000/month for the first 12 months."),
 ("Do I need IELTS?","Not necessarily \u2014 an official statement that your bachelor\u2019s was taught in English is accepted."),
 ("What are the deadlines?","Application + fee by 23 October 2026 (2 PM KST); documents by 30 October 2026."),
 ("How do I keep the scholarship?","Maintain a cumulative GPA of at least 3.0/4.5 with no failing grades."),
]),
 verify='Verified 16 Oct 2026 via Bright Scholarship (23 Oct 2026; full tuition \u00d74 semesters; KRW 1,000,000/month \u00d712; KRW 100,000 fee; docs by 30 Oct) and FellowshipsGuide + Gradualin listings (same deadlines, amounts and MOI rule).',
 offlinks=[('Yeungnam University (official)','https://www.yu.ac.kr/')],
 related_titles=['griffith-vc','hanns-seidel','swiss-phd'],
),

dict(
 slug='erasmus-mundus-glocal-scholarship-2027',
 title='Erasmus Mundus GLOCAL Scholarship 2027 | StudyDesk Scholarships',
 meta='GLOCAL Erasmus Mundus 2027: \u20ac1,400/month + full tuition for a 2-year joint master\u2019s across 7 universities in Europe, Colombia and Japan. Deadline 14 Jan 2027.',
 short='GLOCAL Erasmus Mundus 2027', kicker='Europe \u00b7 Master\u2019s \u00b7 International',
 mono='EM', prov_short='GLOCAL Consortium (EU)', prov_long='Erasmus Mundus GLOCAL Consortium, led by the University of Glasgow',
 prov_cat='International Consortium',
 h1='Erasmus Mundus GLOCAL Scholarship 2027',
 sub='\u20ac1,400 a month plus full tuition \u2014 a two-year joint master\u2019s across seven universities on four continents.',
 dpill='90 days to go', dl_long='14 Jan 2027',
 facts=facts([('Award','\u20ac1,400 / month<small>24 months + full tuition</small>'),
              ('Who can apply','Bachelor\u2019s holders<small>All nationalities</small>'),
              ('Route','Via University of Glasgow<small>Offer needed first</small>'),
              ('Deadline','14 Jan 2027, 13:00 UK<small>Scholarship form</small>'),
              ('Results','April 2027<small>Enrolment Sep 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>GLOCAL (Global Markets, Local Creativities)</strong> is a two-year <strong>Erasmus Mundus Joint Master\u2019s</strong> funded by the <strong>European Union</strong>, delivered by seven universities: <strong>Glasgow (lead), Uppsala, Barcelona, G\u00f6ttingen, Rotterdam, Los Andes (Colombia) and Kyoto (Japan)</strong>. Students study at <strong>three partner universities</strong> across the two years. Up to 60 regular scholarships are awarded across four intakes, plus targeted-region awards.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Bachelor\u2019s degree</strong> with an acceptable academic background for the chosen track.</li>
        <li>Apply for <strong>admission through the University of Glasgow</strong> and hold a <strong>conditional or unconditional offer</strong> before the scholarship deadline.</li>
        <li><strong>Never received an Erasmus Mundus Joint Master\u2019s scholarship</strong> before.</li>
        <li>Meet the <strong>English language</strong> entry requirements.</li>
        <li>All nationalities; max six regular scholarships per nationality across intakes.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and participation fees</strong> covered.</li>
        <li><strong>\u20ac1,400/month living allowance</strong> for 24 months \u2014 or <strong>\u20ac1,275/month plus \u20ac1,000 \u00d7 3</strong> travel/installation payments.</li>
        <li><strong>Full insurance</strong> coverage.</li>
        <li><strong>No application fee.</strong></li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Glasgow admission application + offer</li><li>Europass CV</li><li>Two references on headed paper</li>
        <li>Transcripts + degree certificates</li><li>English proficiency proof</li><li>Passport scan</li><li>Personal statement</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your track and partner universities</strong>Check the acceptable academic backgrounds.</li>
        <li><strong>Apply to Glasgow early</strong>Your offer must be final (not \u201cholding for documents\u201d) before the scholarship deadline.</li>
        <li><strong>Submit the Erasmus Mundus scholarship form</strong>By <strong>14 January 2027, 13:00 UK time</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Ranking matters:</strong> selection weights the personal statement at 40%, academic merit 30%, references 10% and other experience 20%. Put real effort into the statement.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the stipend?","\u20ac1,400/month for two years, or \u20ac1,275/month plus three \u20ac1,000 travel payments."),
 ("Do I apply separately for the scholarship?","You apply for admission via Glasgow first, then complete the Erasmus Mundus scholarship form \u2014 one coordinated process."),
 ("Can I apply if I had an Erasmus Mundus scholarship before?","No \u2014 previous EMJM recipients are ineligible."),
 ("When are results announced?","April 2027, for September 2027 enrolment."),
]),
 verify='Verified 16 Oct 2026 against the official GLOCAL Erasmus Mundus scholarship page (14 Jan 2027, 13:00 UK; Glasgow offer required; no prior EMJM; results April 2027) and ScholarInfo + WorldOpportunitiesHub listings (\u20ac1,400/month; full tuition; 7 universities).',
 offlinks=[('GLOCAL Erasmus Mundus (official)','https://globallocal-erasmusmundus.eu/erasmus-mundus-scholarship/')],
 related_titles=['hanns-seidel','griffith-vc','swiss-phd'],
),
]
ARTICLES += [
dict(
 slug='eiffel-excellence-scholarship-2027-france',
 title='France Excellence Eiffel Scholarship 2027 | StudyDesk Scholarships',
 meta='Eiffel Excellence Scholarship 2027: \u20ac1,200/month (master\u2019s) and \u20ac2,100/month (PhD) from the French government. Nomination only via French universities. Deadline 6 Jan 2027.',
 short='Eiffel Excellence Scholarship 2027', kicker='France \u00b7 Master\u2019s/PhD \u00b7 International',
 mono='EF', prov_short='French Government (Campus France)', prov_long='French Ministry for Europe and Foreign Affairs, via Campus France',
 prov_cat='Government',
 h1='France Excellence Eiffel Scholarship 2027',
 sub='\u20ac1,200\u2013\u20ac2,100 a month from the French government \u2014 for outstanding international master\u2019s and PhD students, by university nomination.',
 dpill='82 days to go', dl_long='6 Jan 2027',
 facts=facts([('Award','\u20ac1,200 / month (Master\u2019s)<small>\u20ac2,100 / month (PhD)</small>'),
              ('Who can apply','International students<small>Nominated by a French institution</small>'),
              ('Age limit','29 (Master\u2019s) · 35 (PhD)<small>At application</small>'),
              ('Deadline','6 Jan 2027<small>Institutional submission</small>'),
              ('Note','No tuition cover<small>Travel + insurance included</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>France Excellence Eiffel Scholarship</strong>, established by the <strong>French Ministry for Europe and Foreign Affairs</strong> and managed by <strong>Campus France</strong>, is France\u2019s flagship award for outstanding international students. It funds <strong>Master\u2019s (12\u201336 months) and PhD (12\u201336 months)</strong> study across seven priority fields \u2014 from biology and engineering to law and economics \u2014 training future decision-makers for the public and private sectors.</p>
      <div class="honest-note"><strong>You cannot apply directly.</strong> Only French higher-education institutions can nominate candidates to Campus France. Each university sets its own earlier internal deadline \u2014 for example, <strong>Universit\u00e9 Paris-Panth\u00e9on-Assas\u2019s 2027 Eiffel campaign runs 19 October \u2013 5 November 2026</strong> (dossiers due 5 Nov, 15:00 Paris time).</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student</strong> (non-French nationality).</li>
        <li><strong>Nominated by a French higher-education institution</strong> \u2014 direct applications are ineligible.</li>
        <li>Enrolling in an <strong>accredited master\u2019s, engineering or doctoral programme</strong> in one of the seven eligible fields.</li>
        <li><strong>Age:</strong> 29 or under for master\u2019s, 35 or under for PhD.</li>
        <li><strong>Not holding</strong> another French government, Erasmus+ or AUF scholarship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly allowance:</strong> \u20ac1,200 (master\u2019s) / \u20ac2,100 (PhD).</li>
        <li><strong>Return international flight</strong> and travel within France.</li>
        <li><strong>Health insurance</strong>, housing assistance and cultural activities.</li>
        <li><strong>Tuition fees are NOT covered</strong> \u2014 check whether your institution waives them for Eiffel scholars.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>University nomination dossier (per institution\u2019s checklist)</li><li>Academic transcripts + degree certificates</li><li>CV</li>
        <li>Career/professional plan</li><li>Passport</li><li>Language evidence</li><li>Thesis proposal + expert evaluations (PhD)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick a French university and programme</strong>In one of the seven eligible fields.</li>
        <li><strong>Check that university\u2019s internal Eiffel deadline</strong>These fall between mid-October and late November 2026 \u2014 far earlier than January.</li>
        <li><strong>Apply to the university and request Eiffel consideration</strong>The international office nominates shortlisted candidates.</li>
        <li><strong>The university submits to Campus France</strong>By <strong>6 January 2027</strong>; results week of 12 April 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I apply directly to Campus France?","No \u2014 only French institutions can submit nominations. You must be selected by a university first."),
 ("What is the real deadline?","6 January 2027 is the institutional submission date; your university\u2019s internal deadline is earlier (often October\u2013November 2026)."),
 ("Does it cover tuition?","No \u2014 the Eiffel covers the monthly allowance, travel, insurance and housing help, not tuition fees."),
 ("What are the age limits?","29 for master\u2019s candidates and 35 for PhD candidates."),
]),
 verify='Verified 16 Oct 2026 via OpportunityLab + CareersHelpdesk + Pathfinderly (call opened Oct 2026; \u20ac1,200/\u20ac2,100; nomination-only; 6 Jan 2027 institutional deadline; results week of 12 Apr 2027) and Assas/Eiffel listings (Assas window 19 Oct\u20135 Nov 2026; same national programme).',
 offlinks=[('Campus France (official)','https://www.campusfrance.org/en')],
 related_titles=['hanns-seidel','swiss-phd','griffith-vc'],
),

dict(
 slug='justcool-phd-scholarship-2027-china',
 title='JUSTCOOL PhD Scholarship 2027, China | StudyDesk Scholarships',
 meta='JUSTCOOL PhD 2027: direct PhD after bachelor\u2019s at Fudan, Shanghai Jiao Tong and Tongji \u2014 fellowship, tuition waiver, housing. Deadline 14 Nov 2026.',
 short='JUSTCOOL PhD 2027', kicker='China \u00b7 PhD \u00b7 International',
 mono='JC', prov_short='JUSTCOOL (Fudan/SJTU/Tongji)', prov_long='JUSTCOOL programme \u2014 Fudan University, Shanghai Jiao Tong University, Tongji University',
 prov_cat='University Consortium',
 h1='JUSTCOOL PhD Scholarship 2027, China',
 sub='Direct PhD straight after your bachelor\u2019s \u2014 at Fudan, Shanghai Jiao Tong or Tongji, with fellowship, housing and tuition waiver.',
 dpill='29 days to go', dl_long='14 Nov 2026',
 facts=facts([('Award','Fellowship + tuition waiver<small>+ free accommodation</small>'),
              ('Who can apply','Non-Chinese bachelor\u2019s<small>Top 20% class rank</small>'),
              ('Subjects','Maths · Physics<small>Chemistry · Biology</small>'),
              ('Deadline','14 Nov 2026<small>24:00 Beijing time</small>'),
              ('Route','5-year English PhD<small>Written exam 12 Dec</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>JUSTCOOL: PhD</strong> is a joint doctoral programme of three leading Shanghai universities \u2014 <strong>Fudan University, Shanghai Jiao Tong University and Tongji University</strong> \u2014 offering international students <strong>direct PhD entry straight after a bachelor\u2019s degree</strong> (no master\u2019s required). The five-year, <strong>English-taught</strong> PhD covers <strong>Mathematics, Physics, Chemistry and Biology</strong>, with a fellowship, tuition waiver, free accommodation and medical insurance.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizen</strong> holding (or about to hold) a bachelor\u2019s degree.</li>
        <li><strong>Top 20% of class</strong> academically; graduation date must fit the programme rules.</li>
        <li>Applying for <strong>Mathematics, Physics, Chemistry or Biology</strong>.</li>
        <li><strong>English proficiency:</strong> English-medium education or an accepted test (IELTS not strictly compulsory).</li>
        <li>Prepared to sit the <strong>written examinations (12 Dec 2026)</strong> and interviews.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>PhD fellowship</strong> plus <strong>research/teaching assistantship</strong> support (exact stipend not stated on the official site).</li>
        <li><strong>Tuition waiver</strong> and <strong>free university accommodation</strong>.</li>
        <li><strong>Medical insurance</strong> coverage.</li>
        <li>Cross-university course access across the three partners.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application on the JUSTCOOL portal</li><li>Bachelor\u2019s degree certificate + transcripts</li><li>CV</li>
        <li>Personal statement / study plan</li><li>English proficiency proof</li><li>Passport copy</li><li>Recommendation letters</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply on the official portal</strong>apply.justcoolphd.cn \u2014 choose your subject first (university choice comes after interview).</li>
        <li><strong>Submit before 14 Nov 2026, 24:00 Beijing time</strong>Application window: 28 Sep \u2013 14 Nov 2026.</li>
        <li><strong>Written exam 12 Dec 2026, interviews January 2027</strong>Admission notices in February 2027; enrolment spring/autumn 2027.</li>
      </ol>
      <div class="honest-note"><strong>Stipend amount not published:</strong> the official site confirms a fellowship and assistantship but does not state the monthly figure \u2014 verify your award letter before accepting.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I need a master\u2019s degree?","No \u2014 JUSTCOOL admits directly after a bachelor\u2019s degree."),
 ("Which universities take part?","Fudan University, Shanghai Jiao Tong University and Tongji University."),
 ("What subjects are offered?","Mathematics, Physics, Chemistry and Biology."),
 ("Is there an entrance exam?","Yes \u2014 written examinations on 12 December 2026, then interviews in January 2027."),
]),
 verify='Verified 16 Oct 2026 via ScholarshipClaude (apply.justcoolphd.cn; 14 Nov 2026; subject-first, university-after-interview) and GS/DAADScholarship listings (Fudan/SJTU/Tongji; direct-after-bachelor\u2019s; 4 subjects; written exam 12 Dec 2026; fellowship + waiver + housing; stipend not stated).',
 offlinks=[('JUSTCOOL application portal (official)','https://apply.justcoolphd.cn/')],
 related_titles=['swiss-phd','nasa-hubble','zonta-ae'],
),

dict(
 slug='ippa-chiang-mai-winter-school-2026',
 title='IPPA Chiang Mai Winter School 2026, Thailand | StudyDesk Scholarships',
 meta='IPPA Chiang Mai Winter School 2026: funded 5-day public-policy training in Thailand for early-career researchers worldwide. Deadline 20 Oct 2026.',
 short='IPPA Winter School 2026', kicker='Thailand \u00b7 Winter School \u00b7 International',
 mono='IP', prov_short='IPPA', prov_long='International Public Policy Association (IPPA)',
 prov_cat='Academic Association',
 h1='IPPA Chiang Mai Winter School 2026, Thailand',
 sub='Five funded days of public-policy training in Chiang Mai \u2014 for early-career researchers worldwide.',
 dpill='4 days to go', dl_long='20 Oct 2026',
 facts=facts([('Award','Funded 5-day training<small>Selected participants</small>'),
              ('Who can apply','Early-career researchers<small>Public policy; all nationalities</small>'),
              ('Where','Chiang Mai, Thailand<small>In person</small>'),
              ('Deadline','20 Oct 2026<small>Apply online</small>'),
              ('Format','Lectures + workshops<small>+ research feedback</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>IPPA Chiang Mai Winter School 2026</strong>, organised by the <strong>International Public Policy Association (IPPA)</strong>, is a <strong>five-day intensive training programme in Chiang Mai, Thailand</strong> for up-and-coming public-policy researchers. Selected participants learn from eminent international academics through <strong>lectures on policy theory, specialised courses, case-study workshops and research presentation sessions</strong> with faculty feedback.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Early-career researchers</strong> working in public policy or related fields.</li>
        <li>Open to <strong>all nationalities</strong>.</li>
        <li>Able to attend <strong>in person in Chiang Mai</strong> for the full five days.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Funded participation</strong> for selected candidates in the winter school programme.</li>
        <li>Lectures by <strong>leading international policy academics</strong>.</li>
        <li><strong>Feedback on your own research</strong> from faculty and peers.</li>
        <li>Workshops, case studies and a <strong>global academic network</strong>.</li>
      </ul>
      <div class="honest-note"><strong>Funding scope:</strong> listings describe the school as funded for selected participants, but <strong>travel and accommodation coverage was not published</strong> in the listings checked \u2014 confirm with IPPA before booking travel.</div>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application form</li><li>CV</li><li>Brief research description / motivation</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the official winter school page</strong>Review courses, fees and accommodation details.</li>
        <li><strong>Complete the online application</strong>Before <strong>20 October 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it really funded?","Listings describe it as funded for selected participants; exact coverage of travel/accommodation was not published \u2014 confirm with IPPA."),
 ("Who should apply?","Early-career researchers in public policy from any country."),
 ("How long is it?","Five days, in person in Chiang Mai, Thailand."),
 ("When is the deadline?","20 October 2026."),
]),
 verify='Verified 16 Oct 2026 via Bright Scholarship (IPPA; 5 days; funded; all nationalities; 20 Oct 2026) and ScholarInfo (same deadline; advises checking the official winter school page for fees/accommodation). No official IPPA page URL was confirmed in the sources checked.',
 offlinks=[('Bright Scholarship listing (corroborating source)','https://brightscholarship.com/ippa-chiang-mai-winter-school-in-thailand/')],
 related_titles=['wb-gaf','bloomberg-harvard','epfl-summer'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')
print('ALL DONE:', len(ARTICLES))

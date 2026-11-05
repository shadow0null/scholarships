#!/usr/bin/env python3
"""Batch 23 (cron run 23, 19 Oct 2026): 5 verified articles.

All prose original. Verification completed the afternoon of 19 Oct 2026.

Skips this run (all deadline-passed, verified before writing):
- ZJUT CSC Graduate Scholarship 2026 (deadline 31 Dec 2025) -> re-scoped to 2027 if announced
- Broad Summer Research Program 2026 (deadline 11 Jan 2026; summer 2026 concluded) -> REWRITTEN as the officially announced 2027 cycle (deadline 10 Jan 2027)
- University of Saskatchewan Scholarships 2026 (deadline 1 May 2026) -> re-scoped to 2027 if announced
- Xiamen University CSC Scholarships 2026 (deadline 15 Feb 2026) -> re-scoped to 2027 if announced
- Reagan Fascell Democracy Fellowship 2026 (deadline 31 Dec 2025; no 2027-28 call found) -> skipped outright
- Erasmus Mundus EMINENT 2026 (deadline 1 Mar 2026; 2027 call not announced) -> skipped outright
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'bsrp-2027': dict(mono='B', title='Broad Summer Research Program 2027 in USA (Fully Funded)', href='broad-summer-research-program-2027-usa.html',
              dpill='Opens late Oct 2026', award='$5,400 stipend + housing + travel', elig='US college undergrads; 3.2+ GPA; graduation Dec 2027+.',
              tags=[('Internship','blue'),('International','teal')]),
 'saitama-mext-2027': dict(mono='S', title='Saitama University MEXT Scholarship 2027 in Japan (Fully Funded)', href='saitama-university-mext-scholarship-2027-japan.html',
              dpill='8 Jan 2027 \u00b7 81 days to go', award='\u00a5148,000/month + tuition waiver + airfare', elig='Master\u2019s holders under 35; GPA 2.30+; doctoral-level Special Programs.',
              tags=[('Government','blue'),('Japan','teal')]),
 'xiamen-csc-2027': dict(mono='X', title='Xiamen University CSC Scholarships 2027 in China (Fully Funded)', href='xiamen-university-csc-scholarships-2027-china.html',
              dpill='20 Feb 2027 \u00b7 124 days to go', award='Full tuition + stipend CNY 2,500\u20133,500/month + dormitory', elig='Non-Chinese citizens; bachelor\u2019s/master\u2019s/doctoral; HSK or IELTS/TOEFL.',
              tags=[('Government','blue'),('China','teal')]),
 'trent-2027': dict(mono='T', title='Trent University International Scholarships 2027 in Canada (Funded)', href='trent-university-international-scholarships-2027-canada.html',
              dpill='15 Feb 2027 \u00b7 119 days to go', award='Up to CAD 15,000/year (prestigious) / CAD 2,500\u20135,500 entrance', elig='International UG applicants; 80%+ average; study permit.',
              tags=[('University','blue'),('Canada','teal')]),
 'warwick-2027': dict(mono='W', title="Warwick Chancellor's International Scholarships 2027 in UK (Fully Funded)", href='warwick-chancellors-international-scholarships-2027-uk.html',
              dpill='10 Dec 2026 \u00b7 52 days to go', award='Full fees + UKRI stipend 3.5 yrs + \u00a35,000 grant', elig='PGR applicants, any nationality; Oct 2027 PhD start.',
              tags=[('PhD','blue'),('UK','teal')]),
})

ARTICLES = [
dict(
 slug='broad-summer-research-program-2027-usa',
 title='Broad Summer Research Program 2027, USA | StudyDesk Scholarships',
 meta='Broad Summer Research Program 2027: applications open late October 2026 and close 10 January 2027. Nine weeks of mentored biomedical research in Boston with a $5,400 stipend, paid housing and travel. Eligibility and how to apply.',
 short='Broad Summer Research Program', kicker='Research Internship \u00b7 USA',
 mono='B', prov_short='Broad Institute', prov_long='Broad Institute of MIT and Harvard, Cambridge, Massachusetts, USA',
 h1='Broad Summer Research Program 2027',
 sub='Nine weeks of mentored biomedical research in Boston \u2014 a $5,400 stipend, paid housing, travel to Boston and a national conference, and a weekly science-communication course.',
 dpill='Opens late Oct 2026', dl_long='10 Jan 2027, 11:59 PM ET',
 facts=facts([('Award','$5,400 stipend<small>Housing + travel + conference sponsorship</small>'),
              ('Who can apply','US college undergrads<small>Graduation Dec 2027 or later; 3.2+ GPA</small>'),
              ('Deadline','10 Jan 2027, 11:59 PM ET<small>Recommendations due 11 Jan; decisions by mid-Mar</small>'),
              ('Duration','9 weeks<small>Summer 2027, arriving Boston 7 June</small>'),
              ('Fields','Biomedical research<small>Physical, biological & computer sciences, engineering, maths</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Broad Summer Research Program (BSRP) 2027</strong>, run by the <strong>Broad Institute of MIT and Harvard</strong> in Cambridge, Massachusetts, gives undergraduates <strong>nine weeks of mentored research</strong> in one of the world\u2019s leading biomedical research institutes. Participants work on real projects, take a <strong>weekly science-communication course</strong>, attend leadership and career-development sessions, and join team-building and social activities through the summer.</p>
      <div class="honest-note"><strong>Not open yet:</strong> applications for the summer 2027 cycle open in <strong>late October 2026</strong> on the official BSRP page (a notify-me form is live now). The deadline is <strong>10 January 2027, 11:59 PM ET</strong>, with letters of recommendation due the next day and decisions announced by <strong>mid-March 2027</strong>.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Enrolled in a four-year college in the United States</strong> for the Fall 2026 semester.</li>
        <li><strong>Graduating in December 2027 or later</strong> \u2014 the program is for non-graduating students; seniors graduating in 2027 cannot take part.</li>
        <li>Majoring in the <strong>physical, biological or computer sciences, engineering or mathematics</strong>.</li>
        <li><strong>Minimum 3.2 GPA</strong> on a 4.0 scale.</li>
        <li><strong>Legally authorized to work in the United States</strong> \u2014 the Broad Institute does not sponsor work authorization for this program.</li>
        <li><strong>Strong interest in graduate school</strong> (Ph.D. or M.D./Ph.D.) and in biomedical research, demonstrated through coursework such as general chemistry and biology.</li>
        <li><strong>No prior research experience required</strong> \u2014 first-time researchers are welcome.</li>
        <li>Available for the <strong>entire nine weeks</strong> \u2014 no concurrent courses, other programs, MCAT preparation or outside employment.</li>
      </ul>
      <div class="honest-note"><strong>Note on eligibility claims:</strong> some aggregator sites describe this program as open to all nationalities. The official Broad Institute criteria require enrollment at a <strong>U.S. college</strong> plus <strong>U.S. work authorization</strong>, so international students without those are not eligible.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>$5,400 stipend</strong> for the nine weeks.</li>
        <li><strong>Paid housing</strong> at partner university facilities in Boston.</li>
        <li><strong>Domestic air and ground travel</strong> to and from Boston.</li>
        <li><strong>Sponsorship to travel and present</strong> your summer research at a national scientific conference.</li>
        <li><strong>Meals during program events</strong>.</li>
        <li>Mentored research, the weekly science-communication course, leadership and career sessions, and team-building activities.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Completed online application</strong> on the official BSRP page once it opens.</li>
        <li><strong>Five short essay responses</strong> (prompts in the application).</li>
        <li><strong>Unofficial transcript(s)</strong> \u2014 combined into <strong>one PDF</strong> per the official FAQ.</li>
        <li><strong>CV or resume.</strong></li>
        <li><strong>Two letters of recommendation</strong> from mentors, faculty members or teachers \u2014 not friends or family. Due <strong>11 January 2027</strong>.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Sign up for the notify-me form</strong>On the official BSRP page so you are alerted when applications open in late October 2026.</li>
        <li><strong>Prepare your documents early</strong>Draft the five essays, merge your transcripts into one PDF, and polish your CV.</li>
        <li><strong>Ask your recommenders now</strong>Give your two mentors or teachers the January 11 deadline well in advance \u2014 late letters sink applications.</li>
        <li><strong>Submit before 10 January 2027, 11:59 PM ET</strong>Apply through the official BSRP application portal.</li>
        <li><strong>Watch for the decision</strong>Notifications go out by mid-March 2027. Questions: bsrp@broadinstitute.org.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When do BSRP 2027 applications open?","In late October 2026 on the official Broad Institute BSRP page. Only a notify-me form is available right now."),
 ("What is the BSRP 2027 deadline?","10 January 2027 at 11:59 PM Eastern Time. Letters of recommendation are due on 11 January 2027."),
 ("Is the Broad Summer Research Program paid?","Yes \u2014 a $5,400 stipend, paid housing in Boston, domestic travel, meals at program events, and sponsorship to present at a national scientific conference."),
 ("Can international students apply?","Only if they are enrolled at a four-year college in the United States and are legally authorized to work in the U.S. The Broad Institute does not provide work-authorization sponsorship."),
 ("Do I need previous research experience?","No \u2014 none is required. What matters is a strong interest in biomedical research and graduate school, shown through your coursework and essays."),
]),
 verify='Verified 19 Oct 2026 on the two official Broad Institute pages (BSRP program page + BSRP FAQ, broadinstitute.org/bsrp): application deadline 10 Jan 2027, 11:59 PM ET; recommendation deadline 11 Jan; decisions by mid-March 2027; applications open "end of October" (notify-me form live); $5,400 stipend, paid housing at partner university facilities, domestic air/ground travel, conference travel sponsorship, meals at program events; 9-week program arriving Boston 7 June 2027. Eligibility from the official FAQ: US four-year college enrollment for Fall 2026, graduation Dec 2027 or later, science/engineering/maths major, 3.2+ GPA, US work authorization (no sponsorship), PhD/MD-PhD interest, no prior research required, full 9-week availability. Aggregator claim of "all nationalities" contradicts the official site and is flagged in the article. 2027 program end date not stated officially.',
 offlinks=[('Broad Summer Research Program \u2014 official FAQ','https://www.broadinstitute.org/bsrp/frequently-asked-questions-about-bsrp'),
           ('Broad Summer Research Program \u2014 official program page','https://www.broadinstitute.org/bsrp/broad-summer-research-program-bsrp')],
 related_titles=['stowers2027','hzdr-2027','utrip-2027'],
),

dict(
 slug='saitama-university-mext-scholarship-2027-japan',
 title='Saitama University MEXT Scholarship 2027, Japan | StudyDesk Scholarships',
 meta='Saitama University MEXT Scholarship 2027 (University Recommendation): October 2027 enrollment through three Special Programs. \u00a5148,000/month stipend, tuition exemption, round-trip airfare. Applications close 8 January 2027.',
 short='Saitama University MEXT Scholarship', kicker='Government Scholarship \u00b7 Japan',
 mono='S', prov_short='Saitama University', prov_long='Saitama University, Saitama, Japan',
 h1='Saitama University MEXT Scholarship 2027',
 sub='A fully funded doctoral scholarship at Saitama University for October 2027 enrollment \u2014 a \u00a5148,000 monthly stipend, full tuition exemption and round-trip airfare, through the MEXT University Recommendation track.',
 dpill='8 Jan 2027', dl_long='8 Jan 2027',
 facts=facts([('Award','Fully funded doctoral scholarship<small>\u00a5148,000/month + tuition exemption + airfare</small>'),
              ('Who can apply','Master\u2019s holders<small>Under 35; GPA 2.30+; outside Japan</small>'),
              ('Deadline','8 Jan 2027<small>SSED program; each program sets its own schedule</small>'),
              ('Enrollment','October 2027<small>Doctoral level; 3 years</small>'),
              ('Programs','3 Special Programs<small>Civil & Environmental, ESITI, SSED</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Saitama University MEXT Scholarship 2027</strong> is Japan\u2019s government-funded <strong>University Recommendation</strong> track for <strong>October 2027 enrollment</strong> at the <strong>Graduate School of Science and Engineering, Saitama University</strong>. It funds a full doctoral program with a monthly stipend, complete exemption from university fees and round-trip airfare between your home country and Japan.</p>
      <div class="honest-note"><strong>Important change for 2027:</strong> MEXT has discontinued the <strong>General Program</strong> of university recommendation at Saitama for 2027+ enrollment. Applications are accepted <strong>only through three Special Programs</strong>: the International Graduate Program on Civil and Environmental Engineering, the International Graduate Program on Energy System \u2013 Information Technology Innovation (<strong>ESITI</strong>), and the International Graduate Program on Stable socio-economic development through sustainable resource management (<strong>SSED</strong>). You apply through the program, not through Saitama\u2019s general admissions or MEXT directly.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Nationality of a country that has <strong>diplomatic relations with Japan</strong>, residing <strong>outside Japan</strong> at the time of application; <strong>Japanese nationals are not eligible</strong>.</li>
        <li><strong>Under 35 years old as of 1 April of the application year</strong> \u2014 born on or after 2 April 1992 for the 2027 cycle.</li>
        <li>Hold, or expect to hold before enrollment, a <strong>master\u2019s degree</strong> (these are doctoral-level programs).</li>
        <li><strong>GPA of 2.30 or higher</strong> (on the MEXT 3.0-scale formula) over the past two years, with academic performance to be maintained during the scholarship.</li>
        <li><strong>English proficiency:</strong> IELTS 5.5 or higher in all four skills, or TOEFL iBT 72 or higher (CEFR B2) taken within the past two years \u2014 or proof that your most recent degree was taught in English. Alternatively, <strong>JLPT N2 or above</strong>.</li>
        <li>Good mental and physical health.</li>
        <li>Must <strong>not have been a MEXT scholarship awardee</strong> in the past three years.</li>
        <li>Must be able to <strong>arrive at Saitama University by 1 October 2027</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend of \u00a5148,000</strong> for doctoral students, including the \u00a53,000 monthly regional supplement (official figures).</li>
        <li><strong>Full exemption</strong> from application, admission and tuition fees.</li>
        <li><strong>Round-trip airfare</strong> between your home country and Japan \u2014 at enrollment and upon program completion.</li>
        <li>Funding for <strong>up to 3 years</strong>, subject to satisfactory academic progress (not extendable).</li>
        <li>ESITI states a quota of <strong>8 doctoral scholars</strong> through University Recommendation.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>MEXT application form</strong> (the program notes the 2027 form was marked \u201cfor reference\u201d while submissions were not yet open \u2014 use the current version from the program site).</li>
        <li><strong>Copy of your passport.</strong></li>
        <li><strong>Official academic transcript(s)</strong> and <strong>certificate of graduation or expected graduation</strong>.</li>
        <li><strong>Research plan.</strong></li>
        <li><strong>Recommendation letter</strong> issued by your home university (SSED asks for two recommenders, sent directly to the program office).</li>
        <li><strong>Abstract of your graduation thesis</strong> plus a list of publications.</li>
        <li><strong>Proof of language skills</strong> (IELTS/TOEFL/JLPT or medium-of-instruction certificate).</li>
        <li>Program <strong>application checklist</strong>. All documents in <strong>PDF</strong>, uploaded through the program\u2019s online submission form.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your Special Program</strong>Pick one of the three: Civil and Environmental Engineering, ESITI, or SSED \u2014 read its admission page fully before starting.</li>
        <li><strong>Contact a prospective supervisor</strong>Supervisor or provisional acceptance is part of Saitama\u2019s screening \u2014 line this up early.</li>
        <li><strong>Prepare your documents in PDF</strong>Application form, passport copy, transcripts, graduation certificate, research plan, thesis abstract and language proof.</li>
        <li><strong>Arrange your recommenders</strong>They must send their letters <strong>directly to the program office</strong> \u2014 you cannot submit them yourself.</li>
        <li><strong>Submit before 8 January 2027</strong>The SSED program\u2019s published deadline; check your chosen program\u2019s page for its exact schedule.</li>
        <li><strong>Screening and nomination</strong>Saitama sends its final nominee list to MEXT in February 2027; final MEXT approval comes around July 2027 for October 2027 enrollment.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the Saitama University MEXT 2027 deadline?","The SSED program\u2019s published deadline is 8 January 2027. Each of the three Special Programs publishes its own schedule \u2014 confirm on your chosen program\u2019s admission page."),
 ("Can I apply through the MEXT General Program at Saitama?","No \u2014 for 2027+ enrollment Saitama accepts MEXT University Recommendation applications only through its three Special Programs (Civil & Environmental Engineering, ESITI, SSED)."),
 ("How much is the Saitama MEXT stipend?","\u00a5148,000 per month for doctoral students, including the \u00a53,000 regional supplement, plus full fee exemption and round-trip airfare."),
 ("What are the age and GPA requirements?","Under 35 as of 1 April of the application year, and a GPA of 2.30 or higher on the MEXT formula over the past two years."),
 ("Do I need Japanese?","No \u2014 JLPT N2+ is one option, but IELTS 5.5+ / TOEFL iBT 72+ (or proof your last degree was taught in English) is accepted instead."),
]),
 verify='Verified 19 Oct 2026 on the official Saitama University pages: the MEXT University Recommendation overview (en.saitama-u.ac.jp/studentlife/mextscholarship_university/ \u2014 confirms 2027 Special Programs only, General Program discontinued) and the SSED admission pages (park.saitama-u.ac.jp/~ssed/admision.html and appli_docs.html \u2014 deadline 8 Jan 2027, screening timeline, eligibility, documents) plus the ESITI admission page (park.saitama-u.ac.jp/~rese/admission.html \u2014 benefits, 8-scholar quota, eligibility) and the official MEXT stipend page (FY2025 figures). Stipend stated as \u00a5148,000/month doctoral including the \u00a53,000 regional supplement; SSED cites a 147,000\u2013148,000 range, given as a range in facts. SSED submission link marked "Not Yet Open" at crawl time.',
 offlinks=[('Saitama University \u2014 MEXT University Recommendation overview','https://en.saitama-u.ac.jp/studentlife/mextscholarship_university/'),
           ('SSED Program \u2014 admission information','https://park.saitama-u.ac.jp/~ssed/admision.html'),
           ('ESITI Program \u2014 admission information','http://park.saitama-u.ac.jp/~rese/admission.html')],
 related_titles=['science-tokyo','u-tokyo-mext','nims2026'],
),

dict(
 slug='xiamen-university-csc-scholarships-2027-china',
 title='Xiamen University CSC Scholarships 2027, China | StudyDesk Scholarships',
 meta='Xiamen University CSC Scholarships 2027: Chinese Government Scholarship (Type B) applications run 1 December 2026 \u2013 20 February 2027. Full tuition, dormitory, monthly stipend and insurance. Eligibility, documents and how to apply.',
 short='Xiamen University CSC Scholarships', kicker='Government Scholarship \u00b7 China',
 mono='X', prov_short='Xiamen University', prov_long='Xiamen University, Xiamen, Fujian, China',
 h1='Xiamen University CSC Scholarships 2027',
 sub='Fully funded bachelor\u2019s, master\u2019s and doctoral study at Xiamen University \u2014 full tuition, free dormitory, a monthly stipend and medical insurance under the Chinese Government Scholarship (Type B).',
 dpill='20 Feb 2027 \u00b7 124 days to go', dl_long='20 Feb 2027',
 facts=facts([('Award','Fully funded<small>Tuition + dormitory + monthly stipend + insurance</small>'),
              ('Who can apply','Non-Chinese citizens<small>Bachelor\u2019s / master\u2019s / doctoral; autumn 2027 intake</small>'),
              ('Deadline','1 Dec 2026 \u2013 20 Feb 2027<small>Beijing time; late applications not considered</small>'),
              ('Stipend','CNY 2,500\u20133,500/month<small>By level; CSC national standard (see note)</small>'),
              ('How to apply','Two online applications<small>CSC system (Type B, agency 10384) + XMU portal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Xiamen University CSC Scholarships 2027</strong> offer the <strong>Chinese Government Scholarship \u2013 University Program (Type B)</strong> at <strong>Xiamen University</strong>, a leading 211/985/Double First-Class university in Fujian. The scholarship covers full tuition fees, a free university dormitory or accommodation subsidy, a monthly living stipend and comprehensive medical insurance, for bachelor\u2019s, master\u2019s and doctoral programs starting in <strong>autumn 2027</strong>.</p>
      <div class="honest-note"><strong>Not open yet:</strong> the 2027 application window runs <strong>1 December 2026 \u2013 20 February 2027</strong> (Beijing time), per Xiamen University\u2019s official 2027 admission guides. The standalone 2027 CSC guide had not been published when this article was verified \u2014 figures marked below as the CSC national standard come from the 2026 CSC guide and apply unless the 2027 CSC notice changes them.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizens</strong> in good physical and mental health, holding a valid regular passport.</li>
        <li><strong>Degree requirements:</strong> bachelor\u2019s applicants need a high-school diploma or equivalent; master\u2019s applicants need a bachelor\u2019s degree (or be graduating); doctoral applicants need a master\u2019s degree (or be graduating).</li>
        <li><strong>Age limits (as of 1 September 2027, per the 2027 admission guides):</strong> bachelor\u2019s generally 18\u201330; master\u2019s generally under 45; doctoral generally under 50. CSC scholarship applicants must <strong>also meet the CSC\u2019s own age limits</strong> \u2014 the 2026 CSC guide set under 25/35/40 by level, but the 2027 CSC limits are not yet published, so confirm against the 2027 CSC notice.</li>
        <li><strong>Language:</strong> Chinese-medium programs \u2014 HSK 5 with score 210 or above (humanities, economics, management, law, arts) or HSK 4 with 210 or above (sciences, engineering, medicine, physical education). English-medium programs \u2014 TOEFL iBT 80 (XMU DI code C310) or IELTS Academic 6.0, an equivalent certificate, or proof your previous degree was taught in English.</li>
        <li>Bachelor\u2019s applicants must submit a <strong>CSCA score report</strong>.</li>
        <li>CSC awardees may <strong>not hold another Chinese government or university scholarship</strong> at the same time.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for the program duration.</li>
        <li><strong>Free university dormitory</strong> or an accommodation subsidy.</li>
        <li><strong>Monthly stipend:</strong> CNY 2,500 (bachelor\u2019s), CNY 3,000 (master\u2019s), CNY 3,500 (doctoral) \u2014 the CSC national standard (2026 guide; to be confirmed for 2027).</li>
        <li><strong>Comprehensive medical insurance</strong> of CNY 800 per person per year \u2014 the CSC national standard.</li>
        <li>Quota of around <strong>50 awards</strong> (2026 figure, subject to CSC approval for 2027).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Passport scan</strong> (valid through 31 October 2027), <strong>birth certificate</strong> and <strong>parents\u2019 identity documents</strong>.</li>
        <li><strong>Degree certificate and full academic transcripts</strong> (notarized if issued outside mainland China).</li>
        <li><strong>Language proficiency certificate</strong> (HSK, TOEFL, IELTS or medium-of-instruction proof).</li>
        <li><strong>Two recommendation letters</strong> from associate professors or above.</li>
        <li><strong>Personal statement</strong> of at least 1,000 words, plus a <strong>CV</strong>.</li>
        <li><strong>Physical examination record</strong> (valid 6 months) and a <strong>no-criminal-record report</strong> (issued within 6 months).</li>
        <li><strong>Financial support guarantee statement</strong> \u2014 scholarship applicants are not exempt.</li>
        <li><strong>Pre-acceptance letter</strong> from an XMU supervisor (optional, but gives admission priority for postgraduates); art applicants must submit portfolios.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply on the CSC Information System</strong>Complete your application at studyinchina.csc.edu.cn: Program Category <strong>Type B</strong>, Xiamen University Agency No. <strong>10384</strong>. Print and sign the CSC application form.</li>
        <li><strong>Apply on the XMU Online Application System</strong>Upload the signed CSC application form at application.xmu.edu.cn and pay the non-refundable application fee of <strong>RMB 400</strong> online.</li>
        <li><strong>Line up a supervisor</strong>Postgraduate CSC applicants ideally secure a pre-acceptance letter from an XMU supervisor for admission priority.</li>
        <li><strong>Submit within the window</strong>Both applications must be completed between <strong>1 December 2026 and 20 February 2027</strong> (Beijing time). No hard copies need to be mailed.</li>
        <li><strong>Wait for results</strong>Results are published on admissions.xmu.edu.cn in <strong>July\u2013August 2027</strong>. Contact: admissions@xmu.edu.cn, +86 (0)592 2184792/2188375.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When do Xiamen University CSC 2027 applications open?","1 December 2026. Both the CSC system and the XMU portal applications must be completed by 20 February 2027 (Beijing time)."),
 ("What does the Xiamen CSC scholarship cover?","Full tuition, a free dormitory or accommodation subsidy, a monthly stipend (CNY 2,500\u20133,500 by level) and medical insurance \u2014 the CSC national standard, pending the 2027 CSC notice."),
 ("What is Xiamen University\u2019s CSC agency number?","10384, under Program Category Type B (Chinese Government Scholarship \u2013 University Program)."),
 ("Is there an application fee?","Yes \u2014 RMB 400, paid online through the XMU application system. It is non-refundable."),
 ("Do I need to mail hard copies?","No \u2014 both applications are completed online; no hard copies need to be mailed."),
]),
 verify='Verified 19 Oct 2026 on the official Xiamen University 2027 admission guides (admissions.xmu.edu.cn): master\u2019s guide (Admissions/Master_s_Students.htm \u2014 window 1 Dec 2026 \u2013 20 Feb 2027, documents), doctoral guide (info/1061/4640.htm \u2014 CSC Type B, agency 10384), bachelor\u2019s guide (Admissions/Undergraduate_Students.htm \u2014 Type B window, CSCA score). Benefits and quota figures are the CSC national standard from the 2026 CSC guide (stipends CNY 2,500/3,000/3,500, insurance CNY 800/yr, ~50 quota) \u2014 not yet re-published for 2027 and flagged as such. 2027 admission-guide age ceilings (18\u201330 / under 45 / under 50 as of 1 Sep 2027) published; 2026 CSC age ceilings (25/35/40) not presented as 2027-confirmed.',
 offlinks=[('Xiamen University \u2014 2027 master\u2019s admission guide','https://admissions.xmu.edu.cn/Admissions/Master_s_Students.htm'),
           ('Xiamen University \u2014 2027 doctoral admission guide (CSC Type B)','https://admissions.xmu.edu.cn/info/1061/4640.htm'),
           ('Xiamen University \u2014 2027 bachelor\u2019s admission guide','https://admissions.xmu.edu.cn/Admissions/Undergraduate_Students.htm')],
 related_titles=['justcool','saitama-mext-2027','science-tokyo'],
),

dict(
 slug='trent-university-international-scholarships-2027-canada',
 title='Trent University International Scholarships 2027, Canada | StudyDesk Scholarships',
 meta='Trent University International Scholarships 2027: automatic entrance awards of CAD 2,500\u20135,500 plus competitive prestigious scholarships up to CAD 15,000/year. Prestigious applications close 15 February 2027. Eligibility and how to apply.',
 short='Trent University International Scholarships', kicker='University Scholarship \u00b7 Canada',
 mono='T', prov_short='Trent University', prov_long='Trent University, Peterborough, Ontario, Canada',
 h1='Trent University International Scholarships 2027',
 sub='Automatic entrance awards of CAD 2,500\u20135,500 a year for international undergraduates \u2014 plus competitive prestigious scholarships worth up to CAD 15,000 a year for the 2027 intakes.',
 dpill='15 Feb 2027 \u00b7 119 days to go', dl_long='15 Feb 2027, 11:59 p.m. EST',
 facts=facts([('Award','Up to CAD 15,000/year<small>Prestigious awards; entrance CAD 2,500\u20135,500 automatic</small>'),
              ('Who can apply','International UG students<small>80%+ average; study permit; Trent offer</small>'),
              ('Deadline','15 Feb 2027, 11:59 p.m. EST<small>Prestigious scholarships; entrance has no separate deadline</small>'),
              ('Renewable','Yes, up to 4 years<small>Reapply yearly; maintain 80%+ full course load</small>'),
              ('Campus','Peterborough & Durham GTA<small>Ontario, Canada</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Trent University International Scholarships 2027</strong> support international students starting an undergraduate degree at <strong>Trent University</strong> in Peterborough, Ontario. Every admitted international student is <strong>automatically considered</strong> for an International Entrance Scholarship based on grades, while high-achieving students can apply separately for competitive <strong>International Prestigious Scholarships & Awards</strong> worth up to CAD 15,000 a year.</p>
      <div class="honest-note"><strong>Partial funding:</strong> these are tuition and ancillary-fee awards, not full cost-of-living packages. Trent pairs entrance and prestigious awards \u2014 you can hold both \u2014 but plan for living costs separately.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An <strong>international student paying international tuition fees</strong>, studying in Canada on a <strong>study permit</strong>.</li>
        <li>Applied to an <strong>undergraduate degree</strong> at Trent \u2014 postgraduate students are not eligible for these awards.</li>
        <li>A <strong>Canadian-equivalent high-school average of 80% or higher</strong>.</li>
        <li>Meet Trent\u2019s <strong>admission and English-language proficiency</strong> requirements.</li>
        <li>Fulfil your <strong>offer conditions</strong>, register for courses and pay your first-year fees.</li>
        <li>Prestigious awards additionally require you to <strong>start in the spring, summer or fall term</strong> \u2014 Winter (January) starters are not eligible for the prestigious tier.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>International Entrance Scholarship (automatic):</strong> CAD 2,500\u20135,500 per academic year by average \u2014 $5,500 for 95\u2013100%, $4,500 for 90\u201394.9%, $3,500 for 85\u201389.9%, $2,500 for 80\u201384.9%. Renewable each year (reapply and maintain 80%+ on a full course load), worth up to <strong>CAD 22,000 over four years</strong>.</li>
        <li><strong>International Prestigious Scholarships & Awards (application required):</strong> up to <strong>CAD 15,000 per year</strong>, up to <strong>CAD 60,000 over four years</strong> \u2014 competitive, based on academics, community service and leadership, with some consideration of financial need.</li>
        <li><strong>Moore Family International Scholarship:</strong> up to CAD 12,000 per year, up to CAD 48,000 over four years \u2014 for students from outside North America.</li>
        <li><strong>Justin Chiu International Scholarship:</strong> up to CAD 15,000 per year, up to CAD 60,000 over four years \u2014 for international students from Asia.</li>
        <li><strong>Daniel Powell Scholarship:</strong> renewable award for Latin American students entering Trent, intended for Global Development Studies majors (amount not published on the awards page).</li>
        <li>You can <strong>combine entrance and prestigious awards</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Trent\u2019s official scholarships page does not publish a separate documents checklist \u2014 the prestigious-award application is completed inside the <strong>Trent Applicant Portal</strong> (Finances tab &gt; International), which will show the fields it needs. Your admission application file (transcripts, English proficiency) forms the basis of the automatic entrance award.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to Trent</strong>You are automatically considered for the International Entrance Scholarship \u2014 no separate form.</li>
        <li><strong>Open the prestigious application from 1 November</strong>Prestigious scholarship applications open each year on 1 November inside the Trent Applicant Portal (Finances tab &gt; International). One application covers all the prestigious awards you are eligible for.</li>
        <li><strong>Submit by 15 February 2027, 11:59 p.m. EST</strong>The deadline for International Prestigious Scholarships applications.</li>
        <li><strong>Fulfil your offer conditions</strong>Register for courses and pay first-year fees to secure your awards.</li>
      </ol>
      <p>Questions: <strong>international@trentu.ca</strong>.</p>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is the Trent entrance scholarship automatic?","Yes \u2014 every international undergraduate applicant is automatically considered for the International Entrance Scholarship based on their admission average. No separate form is needed."),
 ("What is the deadline for Trent\u2019s prestigious scholarships?","15 February 2027 at 11:59 p.m. Eastern Time. Applications open on 1 November 2026."),
 ("How much can I get?","Entrance awards run CAD 2,500\u20135,500 a year (renewable); competitive prestigious awards go up to CAD 15,000 a year. The two can be combined."),
 ("Are January (winter) starters eligible?","They can receive automatic entrance awards, but they are not eligible for the International Prestigious Scholarships."),
 ("Are postgraduate students eligible?","No \u2014 these international awards are for undergraduate degrees only."),
]),
 verify='Verified 19 Oct 2026 on Trent University\u2019s official international scholarships page (trentu.ca/international/discover-trent/tuition-scholarships/scholarships), live-read this run: 2027-intake cycle open; International Prestigious Scholarships deadline 15 Feb 2027, 11:59 p.m. EST, applications open 1 Nov; automatic entrance CAD 2,500\u20135,500 by grade bands (renewable to CAD 22,000/4 yrs at 80%+); prestigious up to CAD 15,000/yr (CAD 60,000/4 yrs); Moore Family up to CAD 12,000/yr (outside North America); Justin Chiu up to CAD 15,000/yr (Asia); Daniel Powell for Latin American Global Development Studies entrants (amount not published); eligibility (international fees, study permit, UG only, 80%+ average, spring/summer/fall start for prestigious). 2026-intake deadlines (1 Feb / 1 Apr 2026) confirmed closed via canamgroup and scholarshiptab. Partial awards \u2014 "Fully Funded" deliberately not used. No documents checklist published \u2014 stated, not invented.',
 offlinks=[('Trent University \u2014 international scholarships (official)','https://www.trentu.ca/international/discover-trent/tuition-scholarships/scholarships')],
 related_titles=['waikato2027','kuas2027','griffith-vc'],
),

dict(
 slug='warwick-chancellors-international-scholarships-2027-uk',
 title="Warwick Chancellor's International Scholarships 2027, UK | StudyDesk Scholarships",
 meta="Warwick Chancellor's International Scholarships 2027: fully funded PhD study from October 2027 \u2014 full fees, UKRI-rate stipend for 3.5 years and a \u00a35,000 research grant. Course applications close 7 December 2026; scholarship applications 10 December 2026.",
 short="Warwick Chancellor's International Scholarships", kicker='PhD Scholarship \u00b7 UK',
 mono='W', prov_short='University of Warwick', prov_long='University of Warwick (Warwick Doctoral College), Coventry, UK',
 h1="Warwick Chancellor's International Scholarships 2027",
 sub='Fully funded PhD study at the University of Warwick from October 2027 \u2014 full tuition, a tax-free maintenance stipend for 3.5 years and a \u00a35,000 research, training and support grant.',
 dpill='10 Dec 2026 \u00b7 52 days to go', dl_long='10 Dec 2026, 16:59 GMT',
 facts=facts([('Award','Fully funded PhD<small>Full fees + UKRI stipend (3.5 yrs) + \u00a35,000 grant</small>'),
              ('Who can apply','PGR applicants, any nationality<small>PhD / MPhil-PhD / EngD from Oct 2027</small>'),
              ('Deadlines','Course: 7 Dec 2026<small>Scholarship: 10 Dec 2026, 16:59 GMT; refs 21 Dec</small>'),
              ('Awards','Up to 80 scholarships<small>Six streams incl. Chancellors & CSC</small>'),
              ('Results','By 5 Mar 2027<small>Mid-stage notification 25 Jan 2027</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Warwick Chancellor\u2019s International Scholarships 2027</strong> are the University of Warwick\u2019s flagship doctoral awards, run through the <strong>Warwick Doctoral College</strong> for <strong>October 2027 entry</strong>. The 2027/28 competition offers <strong>up to 80 postgraduate research scholarships across six streams</strong> \u2014 including Faculty Chancellors, Interdisciplinary Chancellors, AHRC Doctoral, Doctoral Access, and China Scholarship Council streams \u2014 each covering full fees, a tax-free maintenance stipend and a <strong>\u00a35,000 research, training and support grant</strong>.</p>
      <div class="honest-note"><strong>Two deadlines, not one:</strong> you must first submit your <strong>course application by 7 December 2026, 16:59 GMT</strong>, then your <strong>scholarship application by 10 December 2026, 16:59 GMT</strong>, with references due 21 December 2026. Late applications are not accepted. <strong>One scholarship application covers every stream you are eligible for</strong>, and awards cannot be deferred.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Have applied for an <strong>eligible Warwick postgraduate research course</strong> starting <strong>October 2027</strong> \u2014 PhD, MPhil/PhD, EngD, or the PhD stage of a Masters+PhD route (such as 1+3 or 2+4).</li>
        <li><strong>Any nationality and any fee status</strong> can enter the Chancellors streams \u2014 the International/Chancellors competition is aimed squarely at overseas-fee applicants.</li>
        <li><strong>Current Warwick PGR students are not eligible.</strong></li>
        <li>Awards are made on <strong>academic excellence</strong> against Warwick\u2019s PGR Scholarship Competency-Based Assessment Criteria.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full payment of academic fees</strong> at UK or international fee level.</li>
        <li><strong>Tax-free maintenance stipend</strong> at the UKRI rate for <strong>3.5 years</strong> (Chancellors streams).</li>
        <li><strong>\u00a35,000 Research, Training and Support Grant (RTSG)</strong> for conferences, fieldwork, equipment and training.</li>
        <li><strong>Paid leave</strong> for family or medical reasons, plus up to <strong>8 weeks of annual leave</strong>.</li>
        <li><strong>Support towards UK visa and immigration costs</strong> for eligible international applicants (application-based).</li>
        <li><strong>Full-time or part-time</strong> options (part-time = 60% funding over a longer period), study-suspension option, and disability support.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The official competition page does not publish a single bullet-point document list \u2014 it directs applicants to the <strong>Applicant Guidance Notes</strong> and the ITS scholarships portal for exact requirements. Corroborated from the application process: a completed <strong>course application</strong>; academic <strong>transcripts and degree certificates</strong>; a <strong>research proposal or statement of interest</strong>; typically <strong>two academic references</strong>; and <strong>English-language proficiency proof</strong> where applicable. Confirm the scheme-specific list in the guidance notes before submitting.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the official criteria and guidance notes</strong>Study the PGR Scholarship Competency-Based Assessment Criteria and Applicant Guidance Notes on the competition page.</li>
        <li><strong>Submit your course application by 7 December 2026</strong>Apply for your Warwick PGR course through the university\u2019s PGR application system by <strong>16:59 GMT</strong>.</li>
        <li><strong>Get your 7-digit applicant ID</strong>It arrives by email after your course application \u2014 allow 48 hours.</li>
        <li><strong>Register an ITS applicant account</strong>Then complete the scholarship application and upload your documents on the scholarships portal (scholarships.warwick.ac.uk).</li>
        <li><strong>Submit by 10 December 2026, 16:59 GMT</strong>References are due <strong>21 December 2026</strong>. Results are emailed by <strong>5 March 2027</strong> (mid-stage notification 25 January 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the Warwick Chancellor\u2019s International Scholarship deadline?","Two parts: the course application closes 7 December 2026 and the scholarship application closes 10 December 2026, both at 16:59 GMT. References are due 21 December 2026."),
 ("What does the Warwick Chancellor\u2019s scholarship cover?","Full tuition fees, a tax-free maintenance stipend at the UKRI rate for 3.5 years, and a \u00a35,000 research, training and support grant \u2014 plus leave, and visa-cost support for eligible international applicants."),
 ("How many scholarships are available?","Up to 80 postgraduate research scholarships across six streams in the 2027/28 competition \u2014 including Faculty Chancellors (up to 30), Interdisciplinary Chancellors (up to 12) and the CSC stream (up to 30)."),
 ("Can current Warwick PhD students apply?","No \u2014 current Warwick PGR students are not eligible. The competition is for new October 2027 starters."),
 ("Can I defer the award?","No \u2014 the scholarship cannot be deferred to a later year."),
]),
 verify='Verified 19 Oct 2026 on the official Warwick Doctoral College competition page (warwick.ac.uk/services/dc/schols_fund/applicants/competitions/), live-read this run: Autumn 2027 entry call opened 5 Oct 2026; course application deadline 7 Dec 2026 16:59 GMT; scholarship application deadline 10 Dec 2026 16:59 GMT; references 21 Dec 2026; mid-stage notification 25 Jan 2027; offers 5 Mar 2027; full fees + UKRI-rate tax-free stipend for 3.5 years (Chancellors streams) + \u00a35,000 RTSG + paid family/medical leave + up to 8 weeks annual leave + visa-cost support (application-based) + full/part-time options; up to 80 PGR scholarships across six streams (Faculty Chancellors \u226430, Interdisciplinary \u226412, AHRC \u22643, Doctoral Access-Pathway \u22643, Sanctuary \u22642, CSC \u226430); one application covers all eligible schemes; not deferrable. Secondary-source conflicts resolved in favor of the official page (10 Dec vs 11 Dec; up to 80 vs 42). Contact email not verified on the official page \u2014 omitted. 2026/27 cycle (course 8 Dec 2025 / scholarship 11 Dec 2025, results March 2026) confirmed closed.',
 offlinks=[('University of Warwick \u2014 2027/28 PGR scholarship competition (official)','https://warwick.ac.uk/services/dc/schols_fund/applicants/competitions/')],
 related_titles=['swiss-phd','hanns-seidel','zonta-ae'],
),
]

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# validate
import html.parser, re
class P(html.parser.HTMLParser):
    def error(self, m): raise Exception(m)
for slug, _ in built:
    src = OUT.joinpath(slug + '.html').read_text()
    P().feed(src)
    # leftover template text = 'AICTE Pragati', 'Lorem', and template anchors like href="#"/src="#"
    # (CSS hex colours such as #fff in the design system are not template leftovers;
    #  the single href="#" in the dead 'Remind me' button is a known base-template
    #  artifact that postprocess-articles.py (step 5) converts into a WhatsApp CTA)
    for bad in ['AICTE Pragati', 'Lorem', 'src="#"', "href='#'"]:
        assert bad not in src, (slug, bad)
    n_dead = len(re.findall(r'href="#"', src))
    assert n_dead <= 1 and ('Remind me' in src or n_dead == 0), (slug, 'unexpected href="#"', n_dead)
    print('validated', slug)


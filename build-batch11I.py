#!/usr/bin/env python3
"""Batch 11I: final 4 verified articles to reach 50 new. Verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'uq-arc-ft27': dict(mono='UQ', title='University of Queensland ARC Future Fellowships 2027', href='uq-arc-future-fellowships-2027-australia.html',
              dpill='21 days to go', award='4-yr salary + up to A$60,000/yr project funding', elig='Mid-career researchers; PhD awarded 2012–2022; all nationalities.',
              tags=[('Fellowship','blue'),('Australia','teal')]),
 'apu-adb': dict(mono='APU', title='Asia Pacific University ADB Scholarship 2027', href='apu-adb-scholarship-2027-japan.html',
              dpill='20 days to go', award='Full tuition + ¥144,000/month + airfare', elig='ADB-country citizens incl. India; 2 yrs work exp; ≤35; Master’s.',
              tags=[('Master’s','blue'),('Japan','teal')]),
 'monash-rtp': dict(mono='MU', title='Monash University Research Scholarships 2027', href='monash-university-research-scholarships-2027-australia.html',
              dpill='135 days to go', award='A$41,100/yr stipend + tuition + relocation', elig='Research Master’s/PhD; First Class Honours; all nationalities.',
              tags=[('Research','blue'),('Australia','teal')]),
 'honjo': dict(mono='HISF', title='Honjo International Scholarship 2027 in Japan', href='honjo-international-scholarship-2027-japan.html',
              dpill='15 days to go', award='¥180,000–230,000/month', elig='Master’s/PhD at Japanese grad school; ≤30/35; basic Japanese.',
              tags=[('Master’s/PhD','blue'),('Japan','teal')]),
})

ARTICLES = [
dict(
 slug='uq-arc-future-fellowships-2027-australia',
 title='University of Queensland ARC Future Fellowships 2027 | StudyDesk Scholarships',
 meta='ARC Future Fellowships 2027 at the University of Queensland: 4 years of research salary plus up to A$60,000 a year in project funding. ARC closes 6 Nov 2026.',
 short='UQ ARC Future Fellowships 2027', kicker='Australia · Fellowship · All nationalities',
 mono='UQ', prov_short='University of Queensland', prov_long='The University of Queensland, Brisbane (ARC administering organisation)',
 h1='University of Queensland ARC Future Fellowships 2027 in Australia',
 sub='Four years of research salary plus up to A$60,000 a year — for mid-career researchers ready to lead.',
 dpill='21 days to go', dl_long='6 Nov 2026',
 facts=facts([('Award','4-year fellowship salary<small>+ up to A$60,000/year project funding</small>'),
              ('Who can apply','Mid-career researchers<small>PhD awarded 1 Mar 2012 – 1 Mar 2022</small>'),
              ('Route','Via an Australian university<small>UQ is an eligible administering organisation</small>'),
              ('Deadline','6 Nov 2026<small>ARC closing date</small>'),
              ('Attempts','Max 3 submissions<small>Check your history first</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Australian Research Council (ARC) Future Fellowships</strong> scheme funds outstanding mid-career researchers to build an independent research career after doctoral training. The <strong>University of Queensland (UQ)</strong> — one of Australia's Group of Eight research universities — acts as an eligible administering organisation, supporting international candidates through its Research Office with information sessions, templates and internal review.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>PhD or equivalent research higher degree</strong>, awarded on or between <strong>1 March 2012 and 1 March 2022</strong> (allowable career interruptions can extend this window; an Eligibility Exemption Request may be needed).</li>
        <li>Demonstrate a <strong>strong research record</strong> with evidence of leadership, supervision or mentoring appropriate to the fellowship level.</li>
        <li>Show capacity to build <strong>national and international research collaborations</strong>.</li>
        <li>Apply through an <strong>eligible Australian administering organisation</strong> (such as UQ) — you cannot apply directly to the ARC.</li>
        <li>Researchers nominated for a Future Fellowship on <strong>three previous occasions</strong> cannot submit again during the eligible period.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Four years of full-time fellowship salary</strong> at one of the ARC's Future Fellowship salary levels, with salary-related on-costs.</li>
        <li><strong>Up to A$60,000 per year</strong> (up to A$240,000 over four years) in non-salary project funding: research personnel, equipment, consumables, fieldwork, computing, publications, workshops and collaboration.</li>
        <li>Project travel of up to <strong>A$100,000 across the project period</strong>, subject to ARC rules.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Full application in the ARC Research Management System (RMS)</li><li>Application Certification Form</li><li>UQ Pending and Newly Funded ARC grants form</li>
        <li>Evidence for any Eligibility Exemption (career interruptions)</li><li>Host organisation endorsement via UQ Research Office</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Contact UQ's Research Office early</strong>uq.edu.au — the internal Notice of Intent and eligibility-exemption deadline was 7 Oct 2026.</li>
        <li><strong>Prepare the application in RMS</strong>Allow time for internal review before the Research Office deadline.</li>
        <li><strong>ARC closing date: 6 Nov 2026</strong>Rejoinder period follows in Mar–Apr 2027; outcomes expected Oct–Nov 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this a student scholarship?","No — it is a research fellowship for established mid-career researchers, not for Master's or PhD study."),
 ("Can international researchers apply?","Yes — through an eligible Australian administering organisation such as UQ."),
 ("What is the PhD award window?","1 March 2012 to 1 March 2022 inclusive; career interruptions can extend eligibility."),
 ("How long is the fellowship?","Four years full time, with grant commencement expected 1 July 2027."),
]),
 offlinks=[('University of Queensland — research office','https://www.uq.edu.au/'),('ARC Future Fellowships — scheme info','https://www.arc.gov.au/funding/grant-opportunities')],
 related_titles=['nasa-hubble','bloomberg-harvard','wb-gaf'],
 verify='Verified 16 Oct 2026 via scholarshipunion.com, careeraidhub.com and brightscholarship.com (ARC closing 6 Nov 2026; PhD window 1 Mar 2012 – 1 Mar 2022; 4-year salary + up to A$60,000/yr project funding).'),

dict(
 slug='apu-adb-scholarship-2027-japan',
 title='Asia Pacific University ADB Scholarship 2027 in Japan | StudyDesk Scholarships',
 meta='ADB-Japan Scholarship at Ritsumeikan Asia Pacific University 2027: full tuition, ¥144,000/month, airfare. First deadline 5 Nov 2026; second 8 Jan 2027.',
 short='APU ADB Scholarship 2027', kicker='Japan · Master’s · ADB countries incl. India',
 mono='APU', prov_short='Ritsumeikan APU', prov_long='Ritsumeikan Asia Pacific University, Beppu (ADB-JSP)',
 h1='Asia Pacific University ADB Scholarship 2027 in Japan',
 sub='Full tuition, ¥144,000 a month and airfare — for development professionals from ADB member countries.',
 dpill='20 days to go', dl_long='5 Nov 2026 (first round)',
 facts=facts([('Award','Full tuition + ¥144,000/month<small>+ airfare, books, medical insurance</small>'),
              ('Who can apply','ADB borrowing-country citizens<small>India included; 2 yrs work experience; ≤35</small>'),
              ('Level','Master’s, September 2027 intake<small>Development-related fields</small>'),
              ('Deadlines','5 Nov 2026 / 8 Jan 2027<small>Two rounds</small>'),
              ('Route','Apply through APU first<small>No direct ADB application</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>ADB–Japan Scholarship Program (ADB-JSP)</strong> at <strong>Ritsumeikan Asia Pacific University (APU)</strong>, Beppu, funds a <strong>Master's degree</strong> for professionals from ADB developing member countries. The goal is to train people who will contribute to the economic and social development of their home countries. You apply through APU — there is no direct application to the ADB.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Citizen of an <strong>eligible ADB borrowing member country</strong> (India is included); must not hold dual citizenship of a developed country.</li>
        <li><strong>Living and working in your home country</strong> at the time of application.</li>
        <li><strong>Bachelor's degree</strong> plus at least <strong>two years of full-time work experience</strong> after graduation.</li>
        <li><strong>35 years old or younger</strong> at the time of application.</li>
        <li><strong>Strong English communication skills</strong>; secure admission to an approved APU Master's programme.</li>
        <li><strong>Not</strong> currently enrolled in a graduate degree, and <strong>not</strong> applying for a second Master's.</li>
        <li>Family income ≤ US$50,000/year; personal income ≤ US$25,000/year (income certificate may be required).</li>
        <li>Agree to <strong>return home</strong> after completing the degree.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full admission fee and full tuition</strong> at APU.</li>
        <li><strong>Monthly allowance of ¥144,000</strong> (including housing; subject to adjustment).</li>
        <li><strong>Books and instructional materials</strong>, <strong>medical insurance</strong>.</li>
        <li><strong>Economy airfare</strong> from home country to APU and back.</li>
        <li>Initial grant for one year, extendable to a second year on satisfactory academic performance.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Passport / national ID</li><li>Bachelor's degree certificate + transcripts</li><li>Employment certificate(s) with dates and salary (or income tax return)</li>
        <li>Statement of purpose / motivation letter</li><li>English proficiency proof</li><li>Family income certification</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to APU's graduate school</strong>through the APU online application system for the September 2027 intake.</li>
        <li><strong>Upload ADB-JSP documents</strong>Employment certificates, income proof, SOP and English evidence via the portal.</li>
        <li><strong>Meet the deadlines</strong><strong>5 Nov 2026 (first round) or 8 Jan 2027 (second round)</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is India eligible?","Yes — India is an eligible ADB borrowing member country."),
 ("Can I apply directly to the ADB?","No — ADB-JSP applications go through APU."),
 ("What does the monthly allowance cover?","¥144,000 per month including housing support."),
 ("How long does the scholarship last?","Initially one year, extendable to a second year on good academic performance."),
]),
 offlinks=[('Ritsumeikan Asia Pacific University','https://www.apu.ac.jp/home/'),('ADB-Japan Scholarship Program','https://www.adb.org/work-with-us/careers/japan-scholarship-program')],
 related_titles=['swiss-phd','nasa-hubble','wb-gaf'],
 verify='Verified 16 Oct 2026 via daadscholarship.com, fellowshipsguide.com, opportunitiesradar.com, scholarshipsedge.com and brightscholarship.com (deadlines 5 Nov 2026 / 8 Jan 2027; full tuition + ¥144,000/month; India eligible; 2 yrs experience; ≤35).'),

dict(
 slug='monash-university-research-scholarships-2027-australia',
 title='Monash University Research Scholarships 2027 in Australia | StudyDesk Scholarships',
 meta='Monash University Research Scholarships 2027: A$41,100/year stipend, tuition coverage, relocation allowance. Automatic consideration via myApp Portal.',
 short='Monash Research Scholarships 2027', kicker='Australia · Research Master’s/PhD · International',
 mono='MU', prov_short='Monash University', prov_long='Monash University, Melbourne',
 h1='Monash University Research Scholarships 2027 in Australia',
 sub='A$41,100 a year plus tuition — automatic consideration for research-degree applicants.',
 dpill='135 days to go', dl_long='28 Feb 2027',
 facts=facts([('Award','A$41,100/year stipend (2027 rate)<small>+ tuition, relocation, OSHC</small>'),
              ('Who can apply','Research Master’s / PhD applicants<small>First Class Honours; all nationalities</small>'),
              ('Route','Automatic consideration<small>No separate scholarship form</small>'),
              ('Deadline','28 Feb 2027<small>Primary international round</small>'),
              ('Basis','Academic excellence + research outputs<small>Highly competitive</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Monash University</strong>, Melbourne, considers every graduate research applicant <strong>automatically for all available research scholarships</strong> — including the Australian Government <strong>Research Training Program (RTP) Stipend</strong> — when you apply for your course through the <strong>myApp Portal</strong>. There is no separate scholarship form; one application covers admission and funding.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying for (or enrolled in) a <strong>graduate research degree</strong> — Master by Research, PhD or Doctorate — at Monash.</li>
        <li>Hold a <strong>Bachelor's degree with First Class Honours</strong> or equivalent qualification.</li>
        <li>Demonstrate <strong>strong research capability</strong>: publications, research projects or a thesis where available.</li>
        <li>Meet Monash's <strong>English language proficiency</strong> and competitive scholarship selection requirements.</li>
        <li>Open to <strong>domestic and international students</strong> worldwide.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Living allowance of A$41,100 per year</strong> (2027 rate; tax-free, indexed).</li>
        <li><strong>Full tuition fee coverage</strong> for eligible international students (RTP fee offset for domestic).</li>
        <li><strong>Relocation allowance</strong> for eligible students moving to Melbourne.</li>
        <li><strong>Single Overseas Student Health Cover (OSHC)</strong> for international students.</li>
        <li>Paid sick, maternity and parental leave; research and thesis allowances.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic transcripts and degree certificates</li><li>CV</li><li>Research proposal</li>
        <li>Evidence of research experience; publications list</li><li>English proficiency test results</li><li>Passport copy (international applicants)</li><li>Referee reports / recommendation letters</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for your research degree</strong>via Monash's myApp Portal — scholarship consideration is automatic.</li>
        <li><strong>Attach all research evidence</strong>Publications, thesis and experience strengthen a competitive file.</li>
        <li><strong>Meet the international round deadline</strong><strong>28 Feb 2027</strong> for the primary international round.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate scholarship form?","No — eligible applicants are automatically considered when they apply for the research degree."),
 ("What is the stipend for 2027?","A$41,100 per year (2027 rate), tax-free and indexed."),
 ("Are international students eligible?","Yes — domestic and international students are considered."),
 ("What do I need academically?","First Class Honours or equivalent, plus demonstrated research capability."),
]),
 offlinks=[('Monash University — graduate research','https://www.monash.edu/graduate-research'),('RTP — Australian Government','https://www.education.gov.au/research-training-program')],
 related_titles=['griffith-vc','nasa-hubble','swiss-phd'],
 verify='Verified 16 Oct 2026 via idp.com, stlresulttoday.one, opportunitiespedia.com and daadscholarship.com (A$41,100/yr 2027 RTP rate; automatic consideration via myApp; 28 Feb 2027 primary international round).'),

dict(
 slug='honjo-international-scholarship-2027-japan',
 title='Honjo International Scholarship 2027 in Japan | StudyDesk Scholarships',
 meta='Honjo International Scholarship 2027: ¥180,000–230,000/month for Master’s and PhD at Japanese graduate schools. Deadline 31 Oct 2026.',
 short='Honjo International Scholarship 2027', kicker='Japan · Master’s/PhD · All nationalities',
 mono='HISF', prov_short='Honjo Foundation', prov_long='Honjo International Scholarship Foundation (HISF)',
 h1='Honjo International Scholarship 2027 in Japan',
 sub='Up to ¥230,000 a month — for foreign Master’s and PhD students committed to their home countries.',
 dpill='15 days to go', dl_long='31 Oct 2026',
 facts=facts([('Award','¥180,000–230,000/month<small>By degree length; non-repayable</small>'),
              ('Who can apply','Foreign Master’s / PhD students<small>All nationalities; all research fields</small>'),
              ('Age','Master’s ≤30; PhD ≤35<small>No exceptions</small>'),
              ('Deadline','31 Oct 2026<small>Online application</small>'),
              ('Awards','About 10 students<small>Direct application, no nomination</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Honjo International Scholarship Foundation (HISF)</strong> funds foreign students pursuing a <strong>Master's or doctoral degree at a Japanese graduate school</strong>. Around <strong>10 students from all countries</strong> are selected each year. You apply <strong>directly to the foundation</strong> — no university nomination is needed. The award is a <strong>monthly allowance you do not repay</strong>.</p>
      <div class="note-box"><strong>Honest note:</strong> the scholarship covers the monthly allowance (plus possible conference support). It does <strong>not</strong> cover university tuition fees or initial travel/airfare to Japan — plan those separately.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Not a Japanese citizen</strong>; any nationality and any research field may apply.</li>
        <li>Enrolled in, or applying to, a <strong>Master's or doctoral programme at a Japanese graduate school</strong> (admission or acceptance letter needed).</li>
        <li>Start the Master's course <strong>by age 30</strong>, or the PhD course <strong>by age 35</strong> — the foundation states no exceptions.</li>
        <li>More than <strong>12 months remaining</strong> until graduation.</li>
        <li><strong>Basic conversational Japanese</strong> — the interview is conducted in Japanese.</li>
        <li><strong>Strong commitment to serving your home country</strong> in your future career.</li>
        <li>Professional graduate school students are generally ineligible unless submitting a research plan.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>¥230,000/month</strong> for 1–2 year degrees.</li>
        <li><strong>¥210,000/month</strong> for 3-year degrees.</li>
        <li><strong>¥180,000/month</strong> for 4–5 year degrees.</li>
        <li>Paid for the <strong>minimum period required to complete the degree</strong>.</li>
        <li>Possible financial assistance for <strong>international conference attendance</strong> under the foundation's rules.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic transcripts (undergraduate + graduate if applicable; in Japanese or English)</li><li>Research proposal on the official template, written in Japanese</li>
        <li>Recommendation letter from current/previous academic supervisor</li><li>Proof of admission / certificate of enrollment</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Prepare documents</strong>Transcripts, the Japanese research proposal template, recommendation letter and admission proof.</li>
        <li><strong>Submit online</strong>Complete the application form on the HISF website — no physical documents need mailing.</li>
        <li><strong>Deadline: 31 Oct 2026</strong>Document screening results 31 Jan 2027; interviews 9 Feb 2027; final results 31 Mar 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Does it cover tuition?","No — the scholarship is a monthly living allowance; tuition and airfare are not covered."),
 ("Do I need Japanese?","Yes — basic conversational ability; the interview is in Japanese and the research proposal is written in Japanese."),
 ("How many are selected?","About 10 students from all countries each year."),
 ("Do I need my university to nominate me?","No — you apply directly to the foundation."),
]),
 offlinks=[('Honjo International Scholarship Foundation','https://www.hisf.or.jp/')],
 related_titles=['swiss-phd','nasa-hubble','zonta-ae'],
 verify='Verified 16 Oct 2026 via greatpaktimes.com.pk, propakistani.pk, techstour.com, opforall.com and bloompakistan.com (deadline 31 Oct 2026; ¥180,000–230,000/month; ~10 awards; tuition/airfare not covered).'),
]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

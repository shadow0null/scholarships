#!/usr/bin/env python3
"""Batch 24 (cron run 24, 19 Oct 2026): 5 verified articles.

All prose original. Verification completed 19 Oct 2026.

Skips this run:
- Study in France without IELTS 2026 -> umbrella listicle, no single verifiable scheme
- Warwick Chancellor's International Scholarship 2026 -> 2026/27 cycle closed;
  superseded by the 2027/28 article already written in batch 23
  (warwick-chancellors-international-scholarships-2027-uk.html)
- University of Tokyo Summer Internship (UTSIP) 2026 -> 2026 closed (1 Feb 2026 deadline
  passed; programme May-Jul 2026 concluded); 2027 call not announced on the official
  GSFS page (expected late Nov 2026). Note: third-party "270,000 JPY stipend + airfare"
  claims describe Amgen Scholars, a different programme.
- BIS PhD Fellowship Program 2026 -> re-scoped to the officially announced 2027 PhD
  Fellowship Programme (deadline 6 Nov 2026, 23:59 CET; placements Apr-Dec 2027)
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'eth-esop-2027': dict(mono='E', title='ETH Zurich Excellence Scholarship (ESOP) 2027 in Switzerland (Fully Funded)', href='eth-zurich-excellence-scholarship-2027-switzerland.html',
              dpill='Opens 1 Nov 2026', award='CHF 13,500/semester + full tuition waiver', elig='Top-10% bachelor\u2019s graduates applying to an ETH master\u2019s (no MAS).',
              tags=[('Master\u2019s','blue'),('Switzerland','teal')]),
 'hust-csc-2027': dict(mono='H', title='HUST CSC Scholarship Program 2027 in China (Fully Funded)', href='hust-csc-scholarship-program-2027-china.html',
              dpill='25 Feb 2027 \u00b7 129 days to go', award='Full CSC: tuition + accommodation + stipend + insurance', elig='Non-Chinese postgraduates; master\u2019s <35, doctoral <40.',
              tags=[('Government','blue'),('China','teal')]),
 'msrp-2027': dict(mono='M', title='MIT Summer Research Program (MSRP) 2027 in USA (Fully Funded)', href='mit-summer-research-program-msrp-2027-usa.html',
              dpill='19 Jan 2027 \u00b7 92 days to go', award='Weekly stipend + travel + housing + food subsidy', elig='US-college sophomores/juniors/non-graduating seniors; 3.5+ GPA.',
              tags=[('Internship','blue'),('USA','teal')]),
 'taiwanicdf-2027': dict(mono='T', title='TaiwanICDF International Higher Education Scholarship 2027 in Taiwan (Fully Funded)', href='taiwanicdf-international-higher-education-scholarship-2027-taiwan.html',
              dpill='Opens 1 Dec 2026', award='Airfare + housing + tuition + NT$15,000\u201320,000/month', elig='Citizens of TaiwanICDF partner countries (2027 list pending).',
              tags=[('Government','blue'),('Taiwan','teal')]),
 'bis-phd-2027': dict(mono='BIS', title='BIS PhD Fellowship Programme 2027 in Switzerland (Funded)', href='bis-phd-fellowship-programme-2027-switzerland.html',
              dpill='6 Nov 2026 \u00b7 18 days to go', award='Competitive salary + benefits + relocation support', elig='PhD candidates (3rd\u20135th year) in economics/finance.',
              tags=[('PhD','blue'),('Switzerland','teal')]),
})

ARTICLES = [
dict(
 slug='eth-zurich-excellence-scholarship-2027-switzerland',
 title='ETH Zurich Excellence Scholarship (ESOP) 2027 in Switzerland (Fully Funded) | StudyDesk Scholarships',
 meta='ETH Zurich Excellence Scholarship & Opportunity Programme (ESOP) 2027: applications open 1 November 2026 and close 30 November 2026, 11:59 MEZ. CHF 13,500 per semester plus a full tuition waiver for outstanding master\u2019s applicants. Eligibility, documents and how to apply.',
 short='ETH Zurich Excellence Scholarship 2027', kicker='Master\u2019s Scholarship \u00b7 Switzerland',
 mono='E', prov_short='ETH Zurich', prov_long='ETH Zurich, Zurich, Switzerland', prov_cat='University \u00b7 Switzerland',
 h1='ETH Zurich Excellence Scholarship (ESOP) 2027',
 sub='A fully funded route into one of the world\u2019s top universities: CHF 13,500 per semester for living and study costs plus a full tuition-fee waiver, mentorship, and access to the ETH Foundation network \u2014 for outstanding master\u2019s applicants across all disciplines.',
 dpill='Opens 1 Nov 2026', dl_long='30 Nov 2026, 11:59 MEZ (application window 1\u201330 Nov 2026)',
 facts=facts([('Award','CHF 13,500 per semester<small>From HS27 (CHF 12,000 before) + full tuition waiver</small>'),
              ('Who can apply','Top-10% bachelor\u2019s graduates<small>Applying to an ETH Zurich master\u2019s (MAS excluded)</small>'),
              ('Deadline','30 Nov 2026, 11:59 MEZ<small>First application window only \u2014 submit via eApply</small>'),
              ('Duration','3 or 4 semesters<small>Regular duration of your master\u2019s programme</small>'),
              ('Awards','~60 for 2027/28<small>Subject to available funding</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Excellence Scholarship &amp; Opportunity Programme (ESOP)</strong> is ETH Zurich\u2019s flagship funding scheme for outstanding incoming master\u2019s students. It pays a scholarship covering <strong>living and study expenses \u2014 CHF 12,000 per semester, rising to CHF 13,500 per semester from the autumn semester 2027 (HS27)</strong> \u2014 plus a <strong>full tuition-fee waiver</strong>, and adds <strong>mentorship and access to the network of the ETH Foundation</strong>. Funding runs for the regular duration of your master\u2019s programme: three or four semesters depending on the degree.</p>
      <div class="honest-note"><strong>Window not open yet:</strong> applications for the 2027/28 academic year are accepted <strong>1\u201330 November 2026, 11:59 MEZ</strong>, for a master\u2019s start in autumn 2027. ETH runs a separate later window (1\u201330 April) that is only for Swiss bachelor\u2019s graduates \u2014 <strong>ESOP applications are only possible in the November window</strong>, so international applicants must use November.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Very good bachelor\u2019s results</strong> \u2014 in roughly the <strong>top 10% of your bachelor\u2019s degree programme (grade A)</strong>; this is a self-assessment.</li>
        <li>Applying to an eligible <strong>consecutive ETH Zurich master\u2019s programme</strong> (Master of Advanced Studies / MAS programmes are excluded).</li>
        <li>You must <strong>not already be enrolled in an ETH Zurich master\u2019s</strong> and must <strong>not already hold a master\u2019s degree</strong>.</li>
        <li>Open to <strong>all nationalities</strong> \u2014 the November window is mandatory for students with a bachelor\u2019s from outside Switzerland.</li>
        <li>You must meet the <strong>admission requirements of your chosen master\u2019s programme</strong> (academic and language requirements).</li>
        <li><strong>Only ETH bachelor\u2019s students may start the ESOP-funded master\u2019s with a leave of absence.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CHF 13,500 per semester</strong> for living and study expenses from autumn 2027 (CHF 12,000 for earlier cohorts).</li>
        <li><strong>Full tuition-fee waiver</strong> for the regular duration of the programme.</li>
        <li><strong>Mentorship</strong> and access to the <strong>ETH Foundation network</strong>.</li>
        <li>Funding for <strong>three or four semesters</strong>, matching the regular length of your master\u2019s programme.</li>
      </ul>
      <div class="honest-note"><strong>~60 awards planned:</strong> ETH states approximately 60 ESOP scholarships will be assigned for the 2027/28 academic year \u2014 the exact number depends on available funding. Applications are evaluated by the admissions committees of the master\u2019s programmes, and the final decision rests with the Rector of ETH Zurich.</div>
      <h2 id="documents">Documents required</h2>
      <p>In addition to the standard master\u2019s admission documents, ESOP applicants must upload a <strong>pre-proposal for the master\u2019s thesis</strong> \u2014 developed by yourself, following established scientific citation practice. <strong>Plagiarism or misinformation leads to exclusion</strong> from the admission process, or later revocation of admission and the scholarship. If your study programme does not itself ask for references, you must name <strong>two reference persons (professors)</strong>, who upload their letters after receiving the system\u2019s email invitation. Keep the <strong>telephone number in your CV current</strong>: the selection process may include a phone or video interview in February.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose an eligible ETH Zurich master\u2019s programme</strong>Check its admission profile, deadlines and language requirements.</li>
        <li><strong>Prepare your admission documents plus the ESOP pre-proposal</strong>Draft an original thesis pre-proposal with proper scientific citations, following ETH\u2019s published pre-proposal guidelines.</li>
        <li><strong>Arrange your two professor referees</strong>Ask them early if your programme does not already require references; they upload letters after ETH\u2019s system email.</li>
        <li><strong>Apply through eApply in the November window</strong>ESOP applications are supplied via ETH\u2019s online master application system, eApply \u2014 there is no separate scholarship application.</li>
        <li><strong>Submit by 30 November 2026, 11:59 MEZ</strong>Keep your phone reachable for a possible February interview. Decisions are communicated <strong>by the end of March 2027</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Deadline caution:</strong> ETH states the close as 11:59 MEZ, which reads as midday (not midnight) Swiss time \u2014 and sources differ on the exact interpretation. Do not leave submission to the last evening; set your own target well before 30 November.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When does the ETH Excellence Scholarship 2027 application open?","Applications for the 2027/28 intake open 1 November 2026 and close 30 November 2026 at 11:59 MEZ, through ETH\u2019s eApply system \u2014 there is no separate scholarship application."),
 ("What does the ESOP scholarship cover?","A living-and-study grant of CHF 13,500 per semester from autumn 2027 (CHF 12,000 before), a full tuition-fee waiver for the regular duration of the master\u2019s (three or four semesters), mentorship, and access to the ETH Foundation network."),
 ("Who is eligible for ESOP?","Bachelor\u2019s graduates in roughly the top 10% of their programme (grade A, self-assessed), applying to an eligible ETH Zurich consecutive master\u2019s programme \u2014 not MAS \u2014 who are not already enrolled in an ETH master\u2019s and do not already hold a master\u2019s degree."),
 ("How many ESOP scholarships are awarded?","Approximately 60 for the 2027/28 academic year, subject to available funding. Applications are assessed by the master\u2019s programmes\u2019 admissions committees; the final decision rests with the Rector of ETH Zurich."),
 ("Can I apply in the April window?","No \u2014 ESOP is only available in the first application window (November). The April window is for Swiss bachelor\u2019s graduates without ESOP eligibility."),
]),
 verify='Verified 19 Oct 2026 on the official ETH Zurich ESOP page (ethz.ch/students/en/studies/financial/scholarships/excellencescholarship.html), live-read this run: window 1\u201330 Nov 2026, 11:59 MEZ, for HS27 master\u2019s start; CHF 13,500/semester from HS27 (CHF 12,000 before) + full tuition waiver for the regular 3- or 4-semester programme; ~60 awards for 2027/28 subject to funding; decisions by end of March; top-10%/grade-A bachelor\u2019s (self-assessed); no MAS; not enrolled at ETH / no existing master\u2019s; self-developed thesis pre-proposal with scientific citation (plagiarism = exclusion); two professor referees where the programme does not require them; possible phone/VC interview in February; only ETH bachelor\u2019s students may start with a leave of absence. Deadline-time ambiguity flagged (11:59 MEZ \u2014 noon vs midnight disputed across secondary sources); article advises early submission. Financial Aid Office contact published on the official page: Dr. Barbara E. Hellermann, +41 44 632 20 23 / +41 44 632 20 88.',
 offlinks=[('ETH Zurich \u2014 Excellence Scholarship & Opportunity Programme (official)','https://ethz.ch/students/en/studies/financial/scholarships/excellencescholarship.html'),
           ('ETH Zurich \u2014 Master\u2019s admissions (official)','https://mtec.ethz.ch/studies/prospectives/admissions.html')],
 related_titles=['warwick-2027','qecs-2027-28','utrip-2027'],
),
dict(
 slug='hust-csc-scholarship-program-2027-china',
 title='HUST CSC Scholarship Program 2027 in China (Fully Funded) | StudyDesk Scholarships',
 meta='HUST CSC Scholarship Program 2027: Huazhong University of Science and Technology opens its Chinese Government Scholarship window 15 October 2026. Type B deadline 25 February 2027 (agency 10487). Full tuition, accommodation, stipend and insurance. Eligibility, documents and how to apply.',
 short='HUST CSC Scholarship Program 2027', kicker='Government Scholarship \u00b7 China',
 mono='H', prov_short='Huazhong University of Science and Technology', prov_long='HUST, Wuhan, Hubei, China', prov_cat='University \u00b7 China',
 h1='HUST CSC Scholarship Program 2027',
 sub='A fully funded Chinese Government Scholarship route into one of China\u2019s leading research universities: full tuition waiver, accommodation, a monthly stipend and medical insurance for master\u2019s and doctoral study in Wuhan.',
 dpill='25 Feb 2027 \u00b7 129 days to go', dl_long='25 Feb 2027 (Type B Chinese University Program; window opens 15 Oct 2026)',
 facts=facts([('Award','Full CSC package<small>Tuition + accommodation + stipend + insurance</small>'),
              ('Who can apply','Non-Chinese postgraduates<small>Master\u2019s: under 35; doctoral: under 40</small>'),
              ('Deadline','25 Feb 2027<small>Type B window: 15 Oct 2026 \u2013 25 Feb 2027</small>'),
              ('Duration','Programme length<small>Master\u2019s / doctoral tracks</small>'),
              ('Apply via','HUST portal + CSC system<small>Agency number 10487 (Type B)</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>HUST CSC Scholarship Program 2027</strong> is the <strong>Chinese Government Scholarship</strong> track run by the <strong>Huazhong University of Science and Technology (HUST)</strong> in Wuhan \u2014 one of China\u2019s flagship science-and-engineering research universities. The full scholarship covers <strong>tuition, accommodation, a monthly stipend and medical insurance</strong>. HUST\u2019s 2027 scholarship information page confirms the <strong>Type B (Chinese University Program) application window opens 15 October 2026</strong>, with a <strong>25 February 2027 deadline</strong> for master\u2019s and doctoral applicants.</p>
      <div class="honest-note"><strong>2027 detail still arriving:</strong> HUST has published its 2027 overview page; the detailed 2027 guide and 2027 programme lists are not yet out. Where the article gives eligibility and document detail, it is the best-available published information (HUST\u2019s 2025 guide / 2026 FAQ) \u2014 always confirm against the 2027 materials before applying.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizens</strong> in good health with no criminal record.</li>
        <li><strong>Type B Chinese University Program:</strong> postgraduate only \u2014 master\u2019s applicants hold a bachelor\u2019s degree and are <strong>under 35</strong>; doctoral applicants hold a master\u2019s degree and are <strong>under 40</strong>. Excellent academic record (published benchmark: GPA 3.0/4, 3.75/5, or 75%+).</li>
        <li><strong>Type B Silk Road Program:</strong> bachelor\u2019s, master\u2019s and doctoral applicants from the <strong>10 designated countries</strong> (Russia, Malaysia, Mongolia, Laos, Indonesia, Cambodia, Thailand, Bangladesh, Vietnam, Pakistan) \u2014 in 5 specialties: Architecture or Software Engineering (bachelor\u2019s, Chinese-medium); Computer Science and Technology, Civil Engineering or Chemistry (master\u2019s/doctoral, English-medium).</li>
        <li><strong>Language proof:</strong> English-medium \u2014 TOEFL 80+, GRE 310+, IELTS 6.0+, or a previous degree taught in English; Chinese-medium \u2014 HSK 4 \u2265180 (science/engineering/medicine) or HSK 5 \u2265180 (other fields). Bachelor\u2019s Silk Road: HSK 4 \u2265180.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver.</strong></li>
        <li><strong>Accommodation</strong> (university housing).</li>
        <li><strong>Monthly stipend</strong> for the study period.</li>
        <li><strong>Comprehensive medical insurance.</strong></li>
      </ul>
      <div class="honest-note"><strong>Stipend amounts not published:</strong> HUST\u2019s 2027 page does not state exact monthly stipend figures, and the Silk Road track\u2019s benefit details are not published at all \u2014 the article does not assume they match the standard CSC rates. Do not plan around a figure that is not yet announced.</div>
      <h2 id="documents">Documents required</h2>
      <p>The published document list (best-available 2025 guide; no 2027-specific list yet): <strong>degree certificate or enrollment proof, transcripts, personal statement, a 60-second introduction video</strong> (English or Chinese), <strong>CV, study plan/research proposal</strong> (over 1,000 words), <strong>writing sample, language proficiency certificate, two recommendation letters</strong> from professors or associate professors, and a <strong>supervisor acceptance letter</strong> where your chosen programme requires one \u2014 plus <strong>passport, physical examination form, police certificate of no criminal record</strong>, and the printed CSC application form.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply on the HUST Online Application System</strong>Log in at HUST\u2019s admission portal, click \u201cApply for Admission\u201d, submit your academic documents and pay the <strong>800 CNY non-refundable application fee</strong>.</li>
        <li><strong>Pass the review and get the pre-admission letter</strong>Clear the online language test and academic review; HUST issues a pre-admission letter.</li>
        <li><strong>Complete the CSC application</strong>Apply on the Chinese Government Scholarship Information System (campuschina.org) as <strong>Type B with HUST agency number 10487</strong>.</li>
        <li><strong>Upload non-academic documents and wait</strong>Upload them to the HUST system; nomination results are communicated by email.</li>
      </ol>
      <div class="honest-note"><strong>Type A is different:</strong> the Bilateral Program (Type A) runs <strong>late November to early April</strong> and goes only through the dispatching authority in your home country (embassy education office etc.) \u2014 do not apply to HUST or CSC directly for that track, and no HUST application fee applies there.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When is the HUST CSC 2027 deadline?","Type B (Chinese University Program) applications run 15 October 2026 to 25 February 2027 for master\u2019s and doctoral applicants. Silk Road bachelor\u2019s runs to 30 April 2027. Type A (Bilateral) follows your home-country dispatching authority\u2019s own deadline."),
 ("What does the HUST CSC scholarship cover?","A full CSC package: tuition waiver, accommodation, a monthly stipend and medical insurance. Exact 2027 stipend amounts are not yet published on HUST\u2019s pages."),
 ("Who can apply for HUST CSC 2027?","Non-Chinese citizens in good health: master\u2019s applicants under 35 with a bachelor\u2019s degree, doctoral applicants under 40 with a master\u2019s degree, plus strong academics and the required language proof."),
 ("What is HUST\u2019s CSC agency number?","Type B applications use HUST agency number 10487 on campuschina.org. (Type A applicants get their agency number from their home-country dispatching authority.)"),
 ("Is there an application fee?","Yes \u2014 800 CNY, non-refundable, for direct (Type B) applications through the HUST portal. Type A (Bilateral) applicants pay no HUST fee."),
]),
 verify='Verified 19 Oct 2026 on HUST\u2019s official 2027 Scholarship Information page (iso.hust.edu.cn/Scholarships/Scholarship_Information_and_Tips.htm), live-read this run: Type B window opens 15 Oct 2026; deadline 25 Feb 2027 (master\u2019s/doctoral); Silk Road 25 Feb 2027 (master\u2019s/doctoral) and 30 Apr 2027 (bachelor\u2019s); Type A late-Nov to early-Apr via home-country dispatching authority; 800 CNY application fee (rose from 600 CNY in the 2025 guide). Eligibility/document/process detail is the best-available published information (2025 guide / 2026 FAQ) \u2014 the detailed 2027 guide and programme lists are not yet published. Stipend amounts and Silk Road benefit details not published \u2014 omitted as unverifiable. No time-of-day/timezone stated for deadlines.',
 offlinks=[('HUST \u2014 2027 Scholarship Information and Tips (official)','https://iso.hust.edu.cn/Scholarships/Scholarship_Information_and_Tips.htm'),
           ('HUST \u2014 Chinese University Program guide (official)','https://iso.hust.edu.cn/Scholarships/Chinese_University_Program_CUP_.htm')],
 related_titles=['xiamen-csc-2027','saitama-mext-2027','trent-2027'],
),
dict(
 slug='mit-summer-research-program-msrp-2027-usa',
 title='MIT Summer Research Program (MSRP) 2027 in USA (Fully Funded) | StudyDesk Scholarships',
 meta='MIT Summer Research Program 2027: applications open 29 September 2026 and close 19 January 2027, 11:59 PM ET. Nine weeks of mentored research at MIT (7 Jun \u2013 7 Aug 2027) with a weekly stipend, travel, housing and food subsidy. Eligibility and how to apply.',
 short='MIT Summer Research Program 2027', kicker='Summer Research Program \u00b7 USA',
 mono='M', prov_short='Massachusetts Institute of Technology', prov_long='MIT, Cambridge, Massachusetts, USA', prov_cat='University \u00b7 USA',
 h1='MIT Summer Research Program (MSRP) 2027',
 sub='Nine weeks of mentored research at the Massachusetts Institute of Technology \u2014 paired with faculty across all five MIT Schools plus the Schwarzman College of Computing, with a weekly stipend, round-trip travel, housing and graduate-school preparation.',
 dpill='19 Jan 2027 \u00b7 92 days to go', dl_long='19 Jan 2027, 11:59 PM ET (applications open 29 Sep 2026)',
 facts=facts([('Award','Weekly stipend + travel + housing<small>Food subsidy; zero participation cost</small>'),
              ('Who can apply','US-college undergrads<small>Sophomore/junior/non-graduating senior; 3.5+ GPA</small>'),
              ('Deadline','19 Jan 2027, 11:59 PM ET<small>All materials incl. recommendations due then</small>'),
              ('Duration','9 weeks<small>7 Jun \u2013 7 Aug 2027, on-site at MIT</small>'),
              ('Outcome','Research + grad prep<small>Faculty mentorship, workshops, final symposium</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>MIT Summer Research Program (MSRP) 2027</strong>, run by MIT\u2019s Office of Graduate Education, gives undergraduates <strong>nine weeks of mentored research</strong> at the Massachusetts Institute of Technology \u2014 <strong>7 June to 7 August 2027, on-site</strong>. Participants are paired with faculty across <strong>all five MIT Schools plus the Schwarzman College of Computing</strong>, and the programme adds <strong>professional-development and graduate-school preparation workshops</strong>, ending in a <strong>final research symposium</strong>. There is <strong>zero participation cost</strong>: a weekly stipend, round-trip travel to MIT, university housing for the full nine weeks, a food subsidy plus several programme meals per week, and subsidized access to athletic activities are all covered.</p>
      <div class="honest-note"><strong>Biology applicants take a different track:</strong> students in biology, biomedical or neuroscience fields must apply through the separate <strong>MSRP Biology/BCS track</strong> (run via biology.mit.edu), which has its <strong>own deadline of 30 January 2027</strong> (opens 20 November 2026) and requires prior research experience plus three science-faculty references. Do not mix the two tracks\u2019 deadlines or requirements.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Enrolled full-time</strong> in a degree-granting programme at a <strong>U.S. institution or territory</strong> \u2014 MIT students are excluded; satellite campuses abroad, study-abroad programmes and hybrid instruction outside the U.S. do not qualify.</li>
        <li><strong>Sophomore, junior or non-graduating senior</strong>, with at least two academic years of college coursework completed (high-school college credit excluded) \u2014 <strong>not graduating before December 2027</strong>.</li>
        <li><strong>Minimum 3.5 overall or major GPA</strong> on a 4.0 scale.</li>
        <li><strong>U.S. citizens, permanent residents, DACA recipients, or international students with appropriate visa/work authorization</strong> \u2014 F-1 students need CPT/OPT approval from their home institution by 15 May 2027.</li>
        <li><strong>Genuine interest in a graduate degree in an MIT programme</strong> (Sloan professional programmes excluded) and a career in academic research or teaching.</li>
      </ul>
      <div class="honest-note"><strong>Who this is not for:</strong> full-time enrollment at a U.S. institution is mandatory, so students studying in India are not eligible unless they are enrolled full-time at a U.S. college with work authorization. (This is a different programme from the Broad Institute\u2019s BSRP and from MIT Lincoln Laboratory\u2019s Summer Research Program \u2014 the latter has different citizenship and clearance rules.)</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Weekly stipend</strong> for the nine weeks.</li>
        <li><strong>Round-trip travel</strong> to MIT.</li>
        <li><strong>University housing</strong> for the full nine weeks.</li>
        <li><strong>Food subsidy</strong> (food not fully covered) plus several programme meals per week.</li>
        <li><strong>Subsidized access to athletic activities.</strong></li>
        <li>Faculty mentorship, graduate-prep workshops and a final research symposium.</li>
      </ul>
      <div class="honest-note"><strong>Stipend amount not published:</strong> MIT\u2019s official 2027 pages confirm a weekly stipend but do not state the dollar figure \u2014 this article does not repeat older-cycle amounts from third-party sites, which are stale and unverified for 2027.</div>
      <h2 id="documents">Documents required</h2>
      <p>Per MIT\u2019s official 2027 application page: <strong>essay questions</strong> (your academic journey, barriers overcome, research interests, and how MSRP accelerates your graduate path); a <strong>CV (1\u20132 pages)</strong>; <strong>unofficial transcripts from all institutions attended</strong> \u2014 they must be <strong>unlocked, not password-protected</strong>; <strong>two letters of recommendation</strong> (at least one from a faculty member whose classes you took or with whom you did research; if you have prior research experience, one from a research supervisor) \u2014 no more than two letters; and your <strong>top three research preferences</strong> (department, faculty member and research area). <strong>All materials, including recommendations, are due by the 19 January deadline \u2014 no exceptions.</strong></p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Confirm your eligibility</strong>Check the official page against the criteria above \u2014 especially the U.S.-enrollment and graduation-timing rules.</li>
        <li><strong>Apply online once the window opens (29 Sep 2026)</strong>Complete the application at oge.mit.edu/msrp/application.</li>
        <li><strong>Enter recommender details early</strong>They receive the submission link from the system \u2014 follow up with them before the deadline.</li>
        <li><strong>Upload everything and list your research preferences</strong>CV, unlocked transcripts, essays, top-three department/faculty/research-area choices. Do not contact faculty directly.</li>
        <li><strong>Submit by 19 January 2027, 11:59 PM ET</strong>Notifications go out by 31 March; respond to any offer by the date in your acceptance letter.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When is the MIT MSRP 2027 deadline?","19 January 2027 at 11:59 PM ET. Applications open 29 September 2026. Every component \u2014 including the two recommendation letters \u2014 must be in by the deadline, with no exceptions."),
 ("What does MSRP cover?","A weekly stipend, round-trip travel to MIT, university housing for nine weeks, a food subsidy plus several programme meals weekly, and subsidized athletic access \u2014 there is no participation cost. The exact stipend figure is not published on the official 2027 page."),
 ("Who can apply for MSRP 2027?","Full-time undergraduates at U.S. institutions or territories (sophomore, junior or non-graduating senior; not graduating before December 2027) with a 3.5+ GPA \u2014 U.S. citizens, permanent residents, DACA recipients, or international students with appropriate work authorization. MIT students are excluded."),
 ("When does the programme run?","7 June to 7 August 2027, nine weeks on-site at MIT, ending with a research symposium. (One MIT page mentions 8 June; the programme\u2019s dates table says 7 June \u2013 7 August \u2014 plan on the table\u2019s dates.)"),
 ("How is MSRP different from the biology track?","Biology, biomedical and neuroscience applicants must use the separate MSRP Biology/BCS track at biology.mit.edu: deadline 30 January 2027, applications open 20 November 2026, prior research experience required, three science-faculty references."),
]),
 verify='Verified 19 Oct 2026 on MIT\u2019s official 2027 pages (oge.mit.edu/msrp/application/ + FAQ), live-read this run: window 29 Sep 2026 \u2013 19 Jan 2027, 11:59 PM ET; programme 7 Jun \u2013 7 Aug 2027, 9 weeks on-site; zero participation cost (weekly stipend \u2014 amount not published; round-trip travel; housing; food subsidy; several programme meals; subsidized athletics; workshops; final symposium); full-time U.S.-institution enrollment (MIT excluded; no satellite/study-abroad/hybrid-outside-U.S.); sophomore/junior/non-graduating senior, \u22652 years coursework, not graduating before Dec 2027; 3.5+ GPA; citizens/PR/DACA or internationals with work authorization (F-1: CPT/OPT by 15 May 2027); grad-degree intent excluding Sloan professional programmes; essays + 1\u20132-page CV + unlocked unofficial transcripts + exactly two LORs (all due by deadline, no exceptions); top-three research preferences; no direct faculty contact; notification by 31 Mar. Separate MSRP Biology/BCS track: deadline 30 Jan 2027, opens 20 Nov 2026, requires prior research + three science-faculty references. Audience caveat stated: students studying in India ineligible without full-time U.S. enrollment + work authorization. Minor official-page inconsistencies noted (Dec 2027 vs Dec 2026 graduation wording; 7 vs 8 June start).',
 offlinks=[('MIT \u2014 MSRP application 2027 (official)','https://oge.mit.edu/msrp/application/'),
           ('MIT \u2014 MSRP FAQ (official)','https://oge.mit.edu/msrp/frequently-asked-questions/')],
 related_titles=['bsrp-2027','nims2026','hzdr-2027'],
),
dict(
 slug='taiwanicdf-international-higher-education-scholarship-2027-taiwan',
 title='TaiwanICDF International Higher Education Scholarship 2027 in Taiwan (Fully Funded) | StudyDesk Scholarships',
 meta='TaiwanICDF International Higher Education Scholarship 2027: applications open 1 December 2026 and close 15 March 2027. Full scholarship \u2014 airfare, housing, tuition, insurance, textbooks and NT$15,000\u201320,000/month living allowance. Eligibility, documents and how to apply.',
 short='TaiwanICDF Scholarship 2027', kicker='Government Scholarship \u00b7 Taiwan',
 mono='T', prov_short='TaiwanICDF', prov_long='International Cooperation and Development Fund, Taiwan', prov_cat='Government \u00b7 Taiwan',
 h1='TaiwanICDF International Higher Education Scholarship 2027',
 sub='A full scholarship for partner-country students to study in Taiwan: round-trip airfare, housing, tuition and credit fees, insurance, approved textbooks, and a monthly living allowance \u2014 for bachelor\u2019s, master\u2019s and PhD programmes.',
 dpill='Opens 1 Dec 2026', dl_long='15 Mar 2027 (application window 1 Dec 2026 \u2013 15 Mar 2027)',
 facts=facts([('Award','Fully funded<small>Airfare + housing + tuition + NT$15,000\u201320,000/month</small>'),
              ('Who can apply','Partner-country citizens<small>2027 country list pending \u2014 check the guidebook</small>'),
              ('Deadline','15 Mar 2027<small>Window opens 1 Dec 2026; no cutoff time published</small>'),
              ('Duration','Up to 4 / 2 / 4 years<small>Bachelor\u2019s / master\u2019s / PhD maximum</small>'),
              ('Apply via','TaiwanICDF portal + ROC mission<small>Scholarship \u2260 university admission</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>TaiwanICDF International Higher Education Scholarship 2027</strong>, offered by Taiwan\u2019s <strong>International Cooperation and Development Fund</strong>, is a full scholarship for students from TaiwanICDF\u2019s <strong>partner/beneficiary countries</strong> to pursue <strong>bachelor\u2019s, master\u2019s or PhD study</strong> at Taiwanese universities. It is a <strong>fall (September-semester) intake with no spring admission and no deferral</strong>. The 2027 cycle is officially announced: <strong>applications open 1 December 2026 and close 15 March 2027</strong>.</p>
      <div class="honest-note"><strong>2027 guidebook not yet published:</strong> TaiwanICDF\u2019s official page still hosts the 2026 guidebook PDFs. The 2027 country list, TICA programme list and detailed document checklist are pending \u2014 this article does not quote the 2026 lists as 2027 facts. Confirm everything against the 2027 guidebook when it appears.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Citizen of an eligible TaiwanICDF partner/beneficiary country</strong> \u2014 the exact 2027 country list is cycle-specific and not yet published.</li>
        <li><strong>Not a Taiwan national or overseas Taiwanese student.</strong></li>
        <li>Meet the <strong>admission requirements of the chosen TICA programme</strong> and satisfy <strong>visa/ARC requirements</strong>.</li>
        <li><strong>Cannot hold another ROC/Taiwan government scholarship</strong> for the same academic year where prohibited; no prior revoked Taiwan government scholarship; must not have been expelled from a Taiwanese university.</li>
        <li>Bachelor\u2019s, master\u2019s and PhD levels \u2014 historically, undergraduate programmes have accepted applicants only from countries maintaining diplomatic relations with Taiwan (to be confirmed in the 2027 guidebook).</li>
        <li><strong>No general age limit</strong> is stated in the current FAQ.</li>
        <li><strong>Language:</strong> TaiwanICDF itself sets no universal English test requirement \u2014 host universities/programmes may require TOEFL/IELTS or other proof.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Round-trip economy-class airfare.</strong></li>
        <li><strong>University accommodation</strong> (housing).</li>
        <li><strong>Tuition fees and credit fees.</strong></li>
        <li><strong>Insurance.</strong></li>
        <li><strong>Approved textbook costs.</strong></li>
        <li><strong>Monthly living allowance:</strong> NT$15,000 (bachelor\u2019s), NT$18,000 (master\u2019s), NT$20,000 (PhD) \u2014 confirmed by four independent sources.</li>
      </ul>
      <div class="honest-note"><strong>Funding limits:</strong> the maximum funded duration is up to 4 years (bachelor\u2019s), 2 years (master\u2019s) and 4 years (PhD) \u2014 there is <strong>no extension of the funded period</strong>. TaiwanICDF charges no scholarship application fee; universities may charge their own admission/application fees.</div>
      <h2 id="documents">Documents required</h2>
      <p>The standard package (confirmed across sources; the full 2027 checklist is pending the guidebook): a <strong>signed printed copy of the completed online application form</strong>; <strong>passport/nationality proof</strong>; <strong>certified copies of the highest diploma and complete transcripts</strong>; <strong>proof of English proficiency</strong> (TOEFL/IELTS or English-medium-of-instruction certificate, unless your official national language is English); an <strong>itemised CV/resume</strong>; plus whatever your chosen TICA university requires for admission (study plan, recommendation letters \u2014 TaiwanICDF itself does not generally require recommendation letters). Some embassies add their own items, such as medical-exam forms or document certification rules \u2014 <strong>country-specific instructions apply</strong>.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Wait for the 2027 guidebook</strong>Confirm your nationality and chosen programme are eligible for the 2027 cycle.</li>
        <li><strong>Select exactly one approved TICA programme</strong>One programme at one partner university per application year \u2014 it <strong>cannot be changed after submission</strong>.</li>
        <li><strong>Apply online via the TaiwanICDF system (1 Dec 2026 \u2013 15 Mar 2027)</strong>Complete the online application, then print and sign the finished form.</li>
        <li><strong>Complete the partner university\u2019s own admission process separately</strong>The scholarship application is not university admission \u2014 you only become a recipient on receiving the official TaiwanICDF acceptance letter.</li>
        <li><strong>Submit everything to your ROC mission</strong>Hand the signed printed application and all documents to the <strong>ROC (Taiwan) Embassy, Consulate General or Representative Office</strong> serving your country. The mission conducts the first review/interview and forwards its recommended list to TaiwanICDF.</li>
        <li><strong>Two-stage selection</strong>Second review by the partner university\u2019s academic committee together with TaiwanICDF, then the scholarship decision and formal notification \u2014 arrive before the autumn (September) semester.</li>
      </ol>
      <div class="honest-note"><strong>No cutoff time published:</strong> no source gives an exact time-of-day for the 15 March 2027 close. Submit well before the final day rather than gambling on a timezone assumption.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When is the TaiwanICDF 2027 deadline?","Applications open 1 December 2026 and close 15 March 2027. No exact cutoff time is published, so submit well before the final day."),
 ("What does the TaiwanICDF scholarship cover?","Round-trip economy airfare, university accommodation, tuition and credit fees, insurance, approved textbooks, and a monthly living allowance of NT$15,000 (bachelor\u2019s), NT$18,000 (master\u2019s) or NT$20,000 (PhD). No extension of the funded period is allowed."),
 ("Who can apply?","Citizens of TaiwanICDF partner/beneficiary countries (the exact 2027 country list is not yet published) who are not Taiwan nationals, meet their chosen TICA programme\u2019s admission requirements, and do not hold a conflicting Taiwan government scholarship."),
 ("Do I apply to TaiwanICDF or the university first?","Both, separately. You apply online through TaiwanICDF\u2019s system and complete the partner university\u2019s own admission process \u2014 then submit the signed printed application to your country\u2019s ROC (Taiwan) Embassy, Consulate General or Representative Office, which conducts the first review."),
 ("Is there an application fee?","TaiwanICDF charges no scholarship application fee. Universities may charge their own admission or application fees."),
]),
 verify='Verified 19 Oct 2026 against TaiwanICDF\u2019s official 2027 announcement page (icdf.org.tw, announcing the 2027 cycle) plus four independent trackers: window 1 Dec 2026 \u2013 15 Mar 2027; full package (economy airfare, housing, tuition + credit fees, insurance, textbooks, NT$15,000/18,000/20,000 per month by degree level); maximum funded durations 4/2/4 years; partner-country citizens only (2027 list pending \u2014 2026 lists NOT quoted as 2027 facts); no Taiwan nationals; separate scholarship-vs-university-admission decisions; one TICA programme per year, unchangeable after submission; fall intake only, no deferral, no extension; embassy first-review then joint university/TaiwanICDF second review; no TaiwanICDF application fee. Unverifiable and flagged in-article: exact deadline cutoff time/timezone; results notification date; 2027 guidebook, country list, TICA programme list and full document checklist. Embassy-specific extras vary by country \u2014 not presented as universal.',
 offlinks=[('TaiwanICDF \u2014 2027 scholarship announcement (official)','https://www.icdf.org.tw/wSite/ct?xItem=12505&ctNode=31280&mp=2')],
 related_titles=['qecs-2027-28','xiamen-csc-2027','warwick-2027'],
),
dict(
 slug='bis-phd-fellowship-programme-2027-switzerland',
 title='BIS PhD Fellowship Programme 2027 in Switzerland (Funded) | StudyDesk Scholarships',
 meta='BIS PhD Fellowship Programme 2027: the Bank for International Settlements invites PhD candidates in economics and finance for a 3-month research fellowship in Basel. Deadline 6 November 2026, 23:59 CET. Competitive salary, relocation support, hybrid working. Eligibility and how to apply.',
 short='BIS PhD Fellowship Programme 2027', kicker='PhD Fellowship \u00b7 Switzerland',
 mono='BIS', prov_short='Bank for International Settlements', prov_long='BIS, Basel, Switzerland', prov_cat='International Organisation \u00b7 Switzerland',
 h1='BIS PhD Fellowship Programme 2027',
 sub='Three months inside the \u201cbank for central banks\u201d: do policy-oriented research in the Monetary and Economic Department in Basel, work with BIS economists, and join the seminar series \u2014 with a competitive salary, relocation support and hybrid working.',
 dpill='6 Nov 2026 \u00b7 18 days to go', dl_long='6 Nov 2026, 23:59 CET (Swiss time)',
 facts=facts([('Award','Competitive salary + benefits<small>Relocation support; hybrid working</small>'),
              ('Who can apply','PhD candidates in economics/finance<small>Preferably 3rd\u20135th year; all nationalities</small>'),
              ('Deadline','6 Nov 2026, 23:59 CET<small>Current call; apply via bis.org/careers</small>'),
              ('Duration','3 months<small>Placement start between Apr 2027 \u2013 Dec 2027</small>'),
              ('Location','Basel, Switzerland<small>Embedded in the Monetary and Economic Department</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>BIS PhD Fellowship Programme 2027</strong> is run by the <strong>Bank for International Settlements (BIS)</strong> in <strong>Basel, Switzerland</strong> \u2014 the institution that supports central banks\u2019 pursuit of monetary and financial stability and acts as a bank for central banks. The programme gives PhD students the chance to <strong>contribute to BIS economic research and analysis</strong>, working with expert economists and research analysts in the <strong>Monetary and Economic Department (MED)</strong>. Fellows gain <strong>first-hand insight into BIS research and policy work</strong>, access the BIS <strong>seminar series</strong> and visiting research fellows, and benefit from <strong>flexible, hybrid working</strong> \u2014 a blend of on-site work at the Basel office and home office.</p>
      <div class="honest-note"><strong>Which BIS fellowship is this?</strong> BIS runs several fellowship lines. This article covers only the <strong>PhD Fellowship Programme</strong> (current PhD students). It is <strong>not</strong> the BIS Research Fellowship (established academics; deadline 31 March), the Central Bank Research Fellowship (member central-bank nominees), the Lamfalussy Senior Research Fellowship, or the BIS Innovation Hub programmes.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Currently enrolled in a PhD programme</strong> (preferably in the <strong>3rd\u20135th year</strong>) in <strong>economics, finance or related fields</strong>.</li>
        <li><strong>Expertise in conducting research</strong> in financial, macro and monetary economics.</li>
        <li><strong>Ability to apply economic-analysis tools</strong> \u2014 such as Python, MATLAB, Stata or EViews \u2014 to a range of topics.</li>
        <li><strong>Familiarity with major financial/monetary databases</strong> is beneficial.</li>
        <li><strong>All nationalities welcome</strong> \u2014 BIS hires globally and offers relocation support for the successful candidate. BIS\u2019s corporate language is English.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Competitive compensation and benefits package.</strong></li>
        <li><strong>Relocation support</strong> for the successful candidate.</li>
        <li><strong>Hybrid working</strong>: on-site in Basel plus home-office and working-from-abroad days.</li>
        <li>Embedding in the <strong>Monetary and Economic Department</strong> with regular interaction with staff.</li>
        <li>Access to BIS <strong>research activities, seminar series and visiting research fellows</strong> from leading academic institutions.</li>
        <li>An international working environment \u2014 BIS staff come from <strong>over 66 countries</strong>.</li>
      </ul>
      <div class="honest-note"><strong>No salary figure published:</strong> BIS describes the package as \u201ccompetitive compensation and benefits\u201d without stating an amount \u2014 this article does not invent one.</div>
      <h2 id="documents">Documents required</h2>
      <p>No official document checklist is published for this fellowship \u2014 <strong>not published in the official notification</strong>. Apply through the vacancy on <strong>bis.org/careers</strong> while the call is open and follow the application portal\u2019s own instructions.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the 2027 PhD Fellowship vacancy</strong>Find the listing on BIS\u2019s official careers/vacancies page.</li>
        <li><strong>Check your fit</strong>Current PhD enrollment (economics, finance or related), research expertise in financial/macro/monetary economics, and economic-analysis tool skills.</li>
        <li><strong>Apply through bis.org/careers before the deadline</strong>Submit your application by <strong>Friday 6 November 2026, 23:59 CET (Swiss time)</strong>.</li>
      </ol>
      <div class="honest-note"><strong>Note on duration:</strong> the current 2027 vacancy text states a <strong>three-month</strong> placement (start between April and December 2027). An older BIS programme flyer described three-to-eleven-month placements \u2014 the current vacancy\u2019s figure applies.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("When is the BIS PhD Fellowship 2027 deadline?","Friday 6 November 2026, 23:59 CET (Swiss time), per the official vacancy on bis.org/careers. Placement start dates fall between April and December 2027."),
 ("Who can apply for the BIS PhD Fellowship?","Students currently enrolled in a PhD programme (preferably 3rd\u20135th year) in economics, finance or related fields, with research expertise in financial, macro and monetary economics and the ability to apply economic-analysis tools. All nationalities are welcome."),
 ("What does the fellowship offer?","A three-month research placement embedded in the Monetary and Economic Department in Basel: a competitive salary and benefits package, relocation support, hybrid working, and access to BIS seminars and visiting research fellows. No exact salary figure is published."),
 ("Where is the fellowship based?","Basel, Switzerland, with hybrid working options blending on-site work and home office."),
 ("Is this the same as the BIS Research Fellowship?","No. The PhD Fellowship Programme is for current PhD students. The BIS Research Fellowship is for established academics (deadline 31 March), and there are separate Central Bank Research and Lamfalussy Senior Research fellowships."),
]),
 verify='Verified 19 Oct 2026 on BIS\u2019s official vacancy page (bis.org/vacancy/jr100516 \u2014 \u201c2027 PhD Fellowship Programme\u201d), live-read this run: deadline Friday 6 Nov 2026, 23:59 CET (Swiss time); three-month placement; start Apr\u20132027\u2013Dec 2027; Basel-based with hybrid working; enrolled PhD candidates (preferably 3rd\u20135th year) in economics, finance or related fields; expertise in financial/macro/monetary economics research; Python/MATLAB/Stata/EViews-type tools; database familiarity beneficial; all nationalities welcome; relocation support; competitive compensation and benefits package; English is the corporate language; MED embedding with seminars. Official BIS fellowship overview page (bis.org/about/careers/fellowship-programmes) confirms the programme\u2019s existence and MED placement; the other BIS fellowship lines (Research, Central Bank Research, Lamfalussy) are distinct and not covered here. Salary figure not published \u2014 not invented. Official document checklist not published \u2014 stated as such.',
 offlinks=[('BIS \u2014 2027 PhD Fellowship Programme vacancy (official)','https://www.bis.org/vacancy/jr100516'),
           ('BIS \u2014 Fellowship programmes overview (official)','https://www.bis.org/about/careers/fellowship-programmes')],
 related_titles=['swiss-phd','warwick-2027','qecs-2027-28'],
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
    # leftover template text = 'AICTE Pragati', 'Lorem', and template anchors like src="#"/href='#'
    # (CSS hex colours such as #fff in the design system are not template leftovers;
    #  the single href="#" in the dead 'Remind me' button is a known base-template
    #  artifact that postprocess-articles.py (step 5) converts into a WhatsApp CTA)
    for bad in ['AICTE Pragati', 'Lorem', 'src="#"', "href='#'"]:
        assert bad not in src, (slug, bad)
    n_dead = len(re.findall(r'href="#"', src))
    assert n_dead <= 1 and ('Remind me' in src or n_dead == 0), (slug, 'unexpected href="#"', n_dead)
    print('validated', slug)

#!/usr/bin/env python3
"""Batch 27 (cron run 27, 20 Oct 2026): 5 verified articles.

All prose original. Verification completed 20 Oct 2026 across 12 search waves.

WRITTEN this run:
- Taiwan International Graduate Program (TIGP) 2027 (re-scoped: 2026 closed;
  2027 window 1 Nov 2026 - 1 Feb 2027 23:59 GMT+8 on official application
  system; central FAQ NT$34,000/month first-year, extendable; some programme
  pages quote NT$40,000/month; tuition payable at domestic rate, not waived)
- Deakin Vice-Chancellor's International Scholarship 2027 (re-scoped; official
  deakin.edu.au: 100%/50% tuition for normal degree duration; 85% average
  incl. 85% in CBSE/ICSE/State Board Year 12; separate application with
  personal statement + 2 references; VCPEP required; no single deadline)
- Deutsche Welle DW Journalism Traineeship 2028/29 (re-scoped; 2026 cycle long
  closed; current call: apply 13 Oct - 17 Nov 2026 12pm CET; 18 months
  3 Jan 2028 - Jun 2029; EUR 2,196/2,374/2,473 per month; global; language
  profiles incl. Hindi/Urdu/Bengali/Tamil native speakers)
- Erasmus Mundus NOHA Scholarship 2027-2029 (re-scoped; applications opened
  1 Oct 2026; scholarship deadline 15 Dec 2026 23:59 GMT; EUR 1,400/month x 24;
  16 scholarships; 8 universities incl. Deusto coordinator; all nationalities)
- CrossCulture Programme (CCP) Fellowships 2027 (re-scoped; official
  applications-ccp.ifa.de: applications currently accepted; India eligible;
  50-60 fellows, 2-3 months May-Nov 2027; EUR 650/month + airfare + housing +
  insurance; 23+, 2 yrs civil-society experience; deadline 8 Dec 2026)

SKIPS this run (duplicates/closed cycles/umbrellas/unverified):
- NUS Amgen Scholars Program 2026, HKU ADB Scholarship 2026, Dalian UoT CSC
  2026, Erasmus Mundus MIPDaL 2026, NPU International Scholarships 2026
  (duplicates: batch 26 wrote the 2027 cycles of all five; 2026 cycles closed)
- Jiangsu University CSC 2026 (2026 intakes closed Jan/Jun 2026; no official
  2027 CSC call announced - only tracker dates)
- USTC International Scholarship 2026 (2026 closed; 2027 CSC call not verified
  on official USTC pages this run; Winter Camp 2027 already written)
- Queen Sofia Spanish Institute Scholarship 2026 (closed 31 Mar 2026; 2027
  not announced; US citizens/permanent residents only)
- Cambridge ERA AI Fellowship 2026 (2026 concluded; Winter 2027 cohort
  applications closed 13 Sep 2026)
- RISE Germany 2026 (2026 concluded; 2027 call not verified this run)
- Erasmus Mundus CYBERMACS 2026 (no verified 2027 call; CYBERUS project ends
  Dec 2027; successor CYBERSURE is a different programme)
- ENS International Selection 2026, Georg Arnhold Senior Fellowship 2026,
  Kohli Foundation Postdoctoral Fellowship 2026 (not verified this run)
- Listicles/umbrellas: BS/MS/PhD Scholarships in Germany 2026, Scholarships
  for Graduate Students in Canada 2026-27, Bachelor/Master/PhD Scholarships in
  France 2026, Canadian Scholarships for Nigerian Students 2026, 5,000 Fully
  Funded Scholarships in Canada, European Government Scholarships 2026
  Without IELTS, List of Chinese Universities Offering CSC Scholarships 2026
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'tigp-2027': dict(mono='TI', title='Taiwan International Graduate Program (TIGP) 2027 in Taiwan (Fully Funded)', href='taiwan-international-graduate-program-2027-taiwan.html',
              dpill='1 Feb 2027 \u00b7 103 days to go', award='NT$34,000/month tax-free (first year); extendable', elig='B.S./M.Sc. holders; English proficiency; apply to one programme.',
              tags=[('PhD','blue'),('Taiwan','teal')]),
 'deakin-vc-2027': dict(mono='D', title="Deakin Vice-Chancellor's International Scholarship 2027 in Australia (Funded)", href='deakin-vice-chancellors-international-scholarship-2027-australia.html',
              dpill='Rolling \u00b7 no fixed deadline', award='100% or 50% tuition for normal degree duration', elig='New international students; \u226585% average (CBSE/ICSE/State Board 85% accepted).',
              tags=[('UG/PG','blue'),('Australia','teal')]),
 'dw-2028': dict(mono='DW', title='Deutsche Welle DW Journalism Traineeship 2028/29 in Germany (Paid)', href='deutsche-welle-dw-traineeship-2028-29-germany.html',
              dpill='17 Nov 2026 \u00b7 28 days to go', award='\u20ac2,196\u2013\u20ac2,473/month salary for 18 months', elig='Completed degree; English + German (profiles vary); journalism experience.',
              tags=[('Traineeship','blue'),('Germany','teal')]),
 'noha-2027': dict(mono='NO', title='Erasmus Mundus NOHA Scholarship 2027\u20132029 in Europe (Fully Funded)', href='erasmus-mundus-noha-scholarship-2027-29-europe.html',
              dpill='15 Dec 2026 \u00b7 56 days to go', award='\u20ac1,400/month \u00d7 24 (\u20ac33,600) + participation costs', elig='All nationalities; bachelor\u2019s in a relevant field; humanitarian experience valued.',
              tags=[('Master\u2019s','blue'),('Europe','teal')]),
 'ccp-2027': dict(mono='CCP', title='CrossCulture Programme (CCP) Fellowships 2027 in Germany (Fully Funded)', href='crossculture-programme-ccp-fellowships-2027-germany.html',
              dpill='8 Dec 2026 \u00b7 49 days to go', award='\u20ac650/month + airfare + housing + insurance', elig='India eligible; 23+; 2 yrs civil-society experience; not students.',
              tags=[('Fellowship','blue'),('Germany','teal')]),
})

ARTICLES = [
dict(
 slug='taiwan-international-graduate-program-2027-taiwan',
 title='Taiwan International Graduate Program (TIGP) 2027 in Taiwan (Fully Funded) | StudyDesk Scholarships',
 meta='TIGP 2027: fully funded PhD at Academia Sinica, Taiwan, deadline 1 February 2027. Monthly stipend, tuition rules, eligibility, documents, and how to apply to one of 14 programmes.',
 short='Taiwan International Graduate Program 2027', kicker='PhD Scholarship \u00b7 Taiwan',
 mono='TI', prov_short='Academia Sinica', prov_long='Academia Sinica (Taiwan International Graduate Program)', prov_cat='Research Institute \u00b7 Taiwan',
 h1='Taiwan International Graduate Program (TIGP) 2027',
 sub='Do your PhD in the labs of Academia Sinica \u2014 Taiwan\u2019s national research academy \u2014 with a tax-free monthly stipend, no application fee, and your degree conferred by a top Taiwanese partner university.',
 dpill='1 Feb 2027 \u00b7 103 days to go', dl_long='1 February 2027, 23:59 GMT+8 (application window 1 November 2026 \u2013 1 February 2027 on the official TIGP online application system)',
 facts=facts([('Funding','NT$34,000/month tax-free, first year<small>Extended 2\u20133 more years on good performance; some programme pages quote NT$40,000/month</small>'),
              ('Degree','PhD across 14 programmes<small>Partner universities (e.g. NTU, NTHU) confer the PhD; Academia Sinica issues a joint certificate</small>'),
              ('Deadline','1 February 2027<small>Portal opens 1 Nov 2026 \u00b7 one programme per round</small>'),
              ('Tuition','Payable at the domestic rate<small>Academia Sinica subsidises the international premium for 5 years \u2014 tuition is NOT waived</small>'),
              ('Fee','No application fee<small>Apply free at tigp.apps.sinica.edu.tw</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Taiwan International Graduate Program (TIGP)</strong> is the doctoral programme of <strong>Academia Sinica</strong>, Taiwan\u2019s national academy and premier research institution, run together with leading Taiwanese universities. For the <strong>Fall 2027 intake</strong>, the official online application system confirms a window of <strong>1 November 2026 to 1 February 2027 (23:59 GMT+8)</strong>. TIGP is not one degree course but <strong>14 separate PhD programmes</strong> \u2014 from nano science and molecular medicine to bioinformatics and social networks \u2014 each with its own page, partner universities, and slightly different requirements, so you apply to exactly <strong>one programme per round</strong>.</p>
      <div class="honest-note"><strong>Stipend figure, explained:</strong> Academia Sinica\u2019s central TIGP FAQ states a fellowship of <strong>NT$34,000/month (approx. US$1,130)</strong> for the first year, extendable for a further 2\u20133 years on good performance, with advisor funding after that. Some individual programme pages (e.g. Nano Science and Technology) quote <strong>NT$40,000/month</strong> \u2014 a breakdown seen on tracker pages describes it as NT$34,000 tax-free plus NT$6,000. Treat NT$34,000/month as the confirmed central figure and NT$40,000 as programme-specific wording until you confirm on your programme\u2019s page.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>bachelor\u2019s and/or master\u2019s degree</strong> in science, arts, or a related discipline \u2014 most programmes accept applicants holding <strong>only a B.S.</strong> (a few require a master\u2019s; check your programme\u2019s page).</li>
        <li><strong>English proficiency</strong> is required for non-native speakers (TOEFL, IELTS or GEPT); it can be exempted if your university certifies that English was your primary language of instruction \u2014 exemption rules vary by programme.</li>
        <li><strong>GRE scores are optional</strong>, but applicants who skip them are encouraged to submit other evidence of research potential (thesis, publications, research description).</li>
        <li>You may apply to <strong>only one TIGP programme per round</strong>, and each year\u2019s cycle is for the <strong>fall semester</strong> only.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>full fellowship of NT$34,000/month tax-free for the first year</strong>, extended 2\u20133 years on good performance (central FAQ); after the stipend period, funding comes from the thesis advisor.</li>
        <li><strong>No application fee</strong> \u2014 applying through the TIGP portal is entirely free.</li>
        <li><strong>Tuition subsidised to the domestic rate:</strong> Academia Sinica partially subsidises international students\u2019 tuition for five consecutive years, so you pay the Taiwanese domestic rate rather than the full international rate. Note this is a <strong>subsidy, not a waiver</strong> \u2014 tuition is still payable each semester.</li>
        <li>Training in Academia Sinica\u2019s advanced labs, coursework at partner universities, and a PhD conferred by the partner university plus a certificate jointly signed by the Academia Sinica president and the TIGP director.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the official programme pages (the Nano programme page is the most detailed public checklist; confirm against your chosen programme):</p>
      <ul>
        <li><strong>Degree certificates</strong> (bachelor\u2019s and master\u2019s, in English).</li>
        <li><strong>Academic transcripts</strong> with an explanation of any non-standard grading system.</li>
        <li><strong>English proficiency certificate</strong> (or registrar\u2019s certification of English-medium instruction, where your programme allows exemption).</li>
        <li><strong>Three recommendation letters</strong> \u2014 some programmes require one to come from your academic advisor.</li>
        <li><strong>CV</strong>, <strong>statement of purpose / plan for graduate study</strong>, and (where required) an <strong>abstract of your thesis</strong> with advisor details.</li>
        <li>Shortlisted applicants may be asked to send <strong>official transcripts and original language-test scores by post</strong>.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick one TIGP programme</strong> that matches your research interest \u2014 read its admission page carefully, since reference counts and degree rules differ between programmes.</li>
        <li><strong>Apply online</strong> at <strong>tigp.apps.sinica.edu.tw</strong> between <strong>1 November 2026 and 1 February 2027, 23:59 GMT+8</strong>. There is no application fee.</li>
        <li><strong>Upload all documents</strong> marked with an asterisk in the system before submitting; no materials are returned once submitted.</li>
        <li><strong>Wait for review:</strong> committees and partner universities review applications from February to April 2027, with admission offers typically announced in May\u2013June 2027 for autumn entry.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> this page covers the announced Fall 2027 intake. Also note two official-programme realities that differ from most tracker write-ups: <strong>tuition is not waived</strong> (it is subsidised to the domestic rate), and fellows <strong>may not take outside work</strong> \u2014 on or off campus, part-time or full-time, including paid summer internships.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is TIGP 2027?","The Taiwan International Graduate Program is Academia Sinica\u2019s PhD programme in Taipei, run with partner universities such as National Taiwan University and National Tsing Hua University. The Fall 2027 intake accepts applications from 1 November 2026 to 1 February 2027 (23:59 GMT+8) across 14 separate PhD programmes."),
 ("When is the 2027 deadline?","1 February 2027 at 23:59 GMT+8, per the official TIGP online application system. The window opens 1 November 2026; the central FAQ describes the cycle generally as November to February each year."),
 ("How much is the stipend?","The central TIGP FAQ states NT$34,000/month (about US$1,130) for the first year, extendable 2\u20133 years on good performance, with advisor support afterwards. Some programme pages quote NT$40,000/month \u2014 treat NT$34,000 as the confirmed central figure."),
 ("Is tuition free?","No. Tuition is payable each semester, but Academia Sinica subsidises the international premium for five years so international students pay the Taiwanese domestic rate."),
 ("Who can apply?","Holders of a bachelor\u2019s and/or master\u2019s degree in a relevant discipline \u2014 most programmes accept applicants with only a B.S. English proficiency (TOEFL/IELTS/GEPT) is required unless your university certifies English-medium instruction. You may apply to only one TIGP programme per round."),
 ("How do I apply?","Apply free of charge at tigp.apps.sinica.edu.tw within the window, choosing one programme and uploading all required documents (degree certificates, transcripts, English proof, three recommendation letters, CV, statement of purpose). Shortlisted candidates may be asked to post official transcripts and original test scores."),
]),
 verify='Verified 20 Oct 2026 against the official TIGP FAQ (tigp.sinica.edu.tw \u2014 NT$34,000/month first-year fellowship, up-to-3-year funding + advisor support, November-to-February window, no application fee, one programme per round, fall semester only), the official Nano programme admission page (NT$40,000/month figure, ~NT$58,000/semester tuition before subsidy, 5-year subsidy rule, three references, statement of purpose, PhD conferred by NTU/NTHU), and the TIGP central online application system\u2019s stated 2027 window (1 Nov 2026 \u2013 1 Feb 2027, 23:59 GMT+8). The tuition-not-waived fact and the outside-work prohibition are per the programme\u2019s own stated rules. The 2026 cycle was re-scoped to the announced Fall 2027 intake.',
 offlinks=[('TIGP FAQ \u2014 fellowship, fees, how to apply (official, Academia Sinica)','https://tigp.sinica.edu.tw/posts/166309'),
           ('TIGP Nano programme \u2014 admission requirements (official)','https://tigpnano.rcas.sinica.edu.tw/admission.html'),
           ('TIGP biodiversity programme \u2014 admission (official)','https://tigp-biodiv.biodiv.tw/index.php/admission/')],
 related_titles=['taiwanicdf-2027','ustc','npu-2027','dut-2027'],
),
dict(
 slug='deakin-vice-chancellors-international-scholarship-2027-australia',
 title="Deakin Vice-Chancellor's International Scholarship 2027 in Australia (Funded) | StudyDesk Scholarships",
 meta="Deakin Vice-Chancellor's International Scholarship 2027: 100% or 50% tuition for international students. Eligibility (85% average, CBSE/ICSE accepted), documents, and how to apply.",
 short="Deakin Vice-Chancellor's International Scholarship 2027", kicker='University Scholarship \u00b7 Australia',
 mono='D', prov_short='Deakin University', prov_long='Deakin University (Australia)', prov_cat='University \u00b7 Australia',
 h1="Deakin Vice-Chancellor's International Scholarship 2027",
 sub='Deakin\u2019s most prestigious international award covers all or half of your tuition for the whole degree \u2014 for high-achieving students from every country, including India.',
 dpill='Rolling \u00b7 no fixed deadline', dl_long='No single deadline \u2014 apply at least one month before your course starts (scholarship applications are assessed alongside admission; check Deakin\u2019s regional Trimester 1 2027 closing dates for your country)',
 facts=facts([('Funding','100% or 50% of tuition fees<small>For the normal duration of your program; extra or repeated units not covered</small>'),
              ('Who can apply','New international students<small>Coursework degrees (UG + PG); Doctor of Medicine (H911) excluded</small>'),
              ('Grades','At least 85% average<small>85% in Year 12 (CBSE/ICSE/State Board) or 80% overall in an undergraduate degree</small>'),
              ('Deadline','Rolling \u2014 per intake<small>No fixed date; apply \u22651 month before course commencement</small>'),
              ('Extra','VCPEP membership<small>Participation in the Vice-Chancellor\u2019s Professional Excellence Program is required + priority on-campus accommodation</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>Deakin University calls this its <strong>most prestigious scholarship for international students</strong>. The <strong>Vice-Chancellor\u2019s International Scholarship</strong> pays <strong>100% or 50% of your tuition fees</strong> for the <strong>normal duration of your program</strong>, for undergraduate and postgraduate <strong>coursework</strong> degrees. Beyond the fee reduction, scholars join the <strong>Vice-Chancellor\u2019s Professional Excellence Program (VCPEP)</strong> \u2014 a personal and professional development program with career coaching and academic mentoring \u2014 and get <strong>priority access to on-campus accommodation</strong> (at their own cost, subject to availability). A <strong>separate scholarship application is required</strong>; the 25% Excellence and 20% Merit scholarships are assessed automatically, but this one is not.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>new international student</strong> enrolling in a <strong>Deakin coursework degree</strong> (undergraduate or postgraduate).</li>
        <li><strong>Meet the entry requirements</strong> for your program, including <strong>English language requirements</strong>.</li>
        <li>Have achieved <strong>at least an 85% average (or equivalent)</strong> in previous studies. Deakin\u2019s official examples: <strong>85% overall in Year 12 (CBSE, ICSE or State Board)</strong> for undergraduates, or <strong>80% overall in an undergraduate degree</strong> (or in the first four semesters) for postgraduates. GCSE/A Level and IBDP equivalents are also listed.</li>
        <li><strong>Not available</strong> to international students in the <strong>Doctor of Medicine (H911)</strong> program.</li>
        <li>Meeting the minimum does <strong>not guarantee selection</strong> \u2014 Deakin says competition is strong and higher results may be required.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>100% or 50% tuition fee reduction</strong> for the normal duration of the degree (the outcome determines the band).</li>
        <li>Membership of the <strong>VCPEP</strong> \u2014 Deakin describes it as an exclusive program preparing students for future careers and community contribution.</li>
        <li><strong>Priority access to on-campus accommodation</strong> (you pay the accommodation cost yourself; availability permitting).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the official Deakin scholarship page and tracker summaries of the process:</p>
      <ul>
        <li>Your <strong>Deakin course application</strong> (the scholarship sits on top of admission \u2014 apply for admission first).</li>
        <li>A <strong>separate scholarship application form</strong> with a <strong>personal statement</strong>.</li>
        <li><strong>Two letters of reference</strong> highlighting leadership skills and community engagement.</li>
        <li><strong>Academic transcripts</strong> evidencing the 85%+ average.</li>
        <li>An <strong>interview</strong> may be required by the university.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission</strong> to a Deakin coursework degree \u2014 you must meet the program\u2019s entry and English requirements.</li>
        <li><strong>Submit the separate Vice-Chancellor\u2019s International Scholarship application</strong> with your personal statement, two references and transcripts.</li>
        <li><strong>Apply at least one month before your course starts</strong> \u2014 there is no single scholarship deadline; scholarship decisions are made alongside admission for each trimester. Deakin publishes <strong>regional closing dates for Trimester 1 2027</strong> (e.g. Pakistan 20 Nov 2026, Africa 4 Dec 2026, SE/NE Asia 22 Jan 2027) \u2014 check the date for your country before applying.</li>
        <li>If shortlisted, <strong>attend the interview</strong> if Deakin requests one.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> this page covers the open 2027 scholarship. Note there is <strong>no fixed closing date</strong> \u2014 do not trust tracker pages that invent one; the official rule is to apply with your course application, at least a month before you start studying. Living costs, the visa charge and OSHC are <strong>not covered</strong>.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What does the Deakin Vice-Chancellor\u2019s International Scholarship cover?","100% or 50% of tuition fees for the normal duration of your undergraduate or postgraduate coursework degree, depending on the scholarship outcome. It does not cover extra or repeated units, living costs, accommodation, the visa charge, or health cover."),
 ("Who is eligible?","New international students enrolling in a Deakin coursework degree who meet the program\u2019s entry requirements (including English) and have at least an 85% average \u2014 Deakin accepts 85% in Year 12 under CBSE/ICSE/State Boards, or 80% overall in an undergraduate degree for postgraduates. The Doctor of Medicine (H911) is excluded."),
 ("Is there a deadline?","No single deadline. Deakin has no fixed closing date for this scholarship \u2014 applications are assessed alongside admission for each trimester. The official guidance is to apply at least one month before your course starts, and to check Deakin\u2019s published regional closing dates for your intake."),
 ("How do I apply?","Apply for admission to Deakin first, then submit the separate scholarship application with a personal statement, two reference letters (leadership and community engagement) and academic transcripts. An interview may be required."),
 ("What is the VCPEP?","The Vice-Chancellor\u2019s Professional Excellence Program is a personal and professional development program that all scholars must participate in \u2014 Deakin describes career coaching and academic mentoring as part of it."),
 ("Is it automatic?","No. Unlike Deakin\u2019s 25% Excellence and 20% Merit scholarships (assessed automatically from your course application), the Vice-Chancellor\u2019s International Scholarship needs a separate application, and meeting the minimum criteria does not guarantee selection."),
]),
 verify='Verified 20 Oct 2026 against the official Deakin Vice-Chancellor\u2019s International Scholarship page (deakin.edu.au \u2014 100%/50% tuition for normal degree duration; VCPEP requirement; priority on-campus accommodation; new international student + coursework degree + English + \u226585% average with CBSE/ICSE/State Board, GCSE/A Level, IBDP and UG-degree equivalents; Doctor of Medicine H911 excluded; competitive selection; separate application; extra/repeated units not covered) and the official Deakin Trimester 1 2027 closing-dates page (regional dates; no India-specific date listed \u2014 not invented). The \u201cno single deadline / apply one month before commencement\u201d rule is per the official and tracker consensus. The 2026 cycle was re-scoped to the open 2027 scholarship.',
 offlinks=[("Deakin Vice-Chancellor\u2019s International Scholarship (official)","https://www.deakin.edu.au/study/fees-and-scholarships/scholarships/find-a-scholarship/deakin-vice-chancellors-international-scholarship"),
           ("Deakin international scholarships guide (official PDF)","https://www.deakin.edu.au/__data/assets/pdf_file/0014/312422/deakin-international-scholarship-guide.pdf")],
 related_titles=['griffith-vc','monash-rtp','melbourne2027','adelaide2027'],
),
dict(
 slug='deutsche-welle-dw-traineeship-2028-29-germany',
 title='Deutsche Welle DW Journalism Traineeship 2028/29 in Germany (Paid) | StudyDesk Scholarships',
 meta='DW Journalism Traineeship 2028/29: 18-month paid journalism training in Bonn and Berlin, salary \u20ac2,196\u2013\u20ac2,473/month. Deadline 17 November 2026. Eligibility, languages, and how to apply.',
 short='Deutsche Welle DW Traineeship 2028/29', kicker='Paid Traineeship \u00b7 Germany',
 mono='DW', prov_short='Deutsche Welle', prov_long='Deutsche Welle (DW), Germany\u2019s international broadcaster', prov_cat='Broadcaster \u00b7 Germany',
 h1='Deutsche Welle DW Journalism Traineeship 2028/29',
 sub='Eighteen months of paid multimedia journalism training at Germany\u2019s international broadcaster \u2014 seminars in Bonn and Berlin, newsroom placements at home and abroad, and a monthly training salary.',
 dpill='17 Nov 2026 \u00b7 28 days to go', dl_long='17 November 2026, 12:00 p.m. CET (application window: 13 October 2026, 12:00 p.m. CEST \u2013 17 November 2026, 12:00 p.m. CET)',
 facts=facts([('Salary','\u20ac2,196\u2013\u20ac2,473/month<small>Months 1\u20136: \u20ac2,196 \u00b7 7\u201312: \u20ac2,374 \u00b7 13\u201318: \u20ac2,473 (before tax)</small>'),
              ('Duration','18 months<small>3 January 2028 \u2013 June 2029 \u00b7 Bonn and Berlin + foreign bureaus</small>'),
              ('Cohort','About 12 trainees<small>Highly competitive international intake</small>'),
              ('Who can apply','All nationalities<small>Completed degree or apprenticeship + language profile + initial journalism experience</small>'),
              ('Languages','German + English required<small>Exact profile depends on your native language (see eligibility)</small>')]),
 body='''
      <h2 id="about">About the traineeship</h2>
      <p>The <strong>Deutsche Welle (DW) Journalism Traineeship</strong> is one of Germany\u2019s most prestigious paid journalism training programmes. The <strong>2028/29 cohort</strong> runs for <strong>18 months, from 3 January 2028 to June 2029</strong>, combining six months of theory and practice-oriented seminar modules (in German and English), nine months of placements with DW editorial departments in <strong>Bonn and Berlin</strong> and one of DW\u2019s <strong>foreign bureaus</strong> (including Delhi, Jakarta, Washington D.C., Brussels, Riga and Jerusalem), plus a one-month elective. Around <strong>twelve trainees</strong> are selected per cycle, and DW notes that successful completion carries a <strong>genuine prospect of ongoing employment</strong> at the broadcaster. The current application window is <strong>13 October to 17 November 2026 (12:00 p.m. CET)</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Education:</strong> a completed <strong>university degree, college qualification or vocational apprenticeship</strong> before the traineeship begins \u2014 a journalism degree is <strong>not</strong> required. DW explicitly welcomes career changers from fields such as <strong>IT, science, politics, economics, law and medicine</strong>, provided they meet the other requirements.</li>
        <li><strong>Languages</strong> \u2014 one of three profiles: (a) <strong>native speaker of a DW broadcast language</strong> (the list includes Hindi, Urdu, Bengali and Tamil, plus 30 others) with <strong>excellent English (C1/C2)</strong> and <strong>good German (B1/B2)</strong>; (b) <strong>native English speaker</strong> with <strong>good German</strong>; or (c) <strong>native German speaker</strong> with <strong>excellent English</strong>.</li>
        <li><strong>Initial journalism experience:</strong> you do not need to be a professional journalist, but you must show reporting-related experience \u2014 published work, student media, podcasts, video reports or researched multimedia stories \u2014 plus <strong>social media expertise</strong>.</li>
        <li><strong>No language certificates</strong> need to be uploaded; DW asks for an honest self-assessment (certificates are welcome if you have them), but journalists from DW\u2019s language departments test your languages at the assessment centre.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly training salary for the full 18 months</strong>: \u20ac2,196 (months 1\u20136), \u20ac2,374 (months 7\u201312), \u20ac2,473 (months 13\u201318), before tax.</li>
        <li><strong>World-class multimedia journalism seminars</strong> and hands-on newsroom placements in Germany and at DW foreign bureaus.</li>
        <li>Training across <strong>TV, radio and online</strong> \u2014 digital storytelling, data journalism, TV moderation, and emerging tools including AI in journalism.</li>
        <li><strong>Prospect of ongoing DW employment</strong> after successful completion.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the published selection-process descriptions for this cycle:</p>
      <ul>
        <li><strong>Online application form</strong> with a detailed background <strong>questionnaire</strong>.</li>
        <li>A <strong>mandatory custom video application</strong> (completed as one of the application tasks).</li>
        <li><strong>Up to three work samples</strong> \u2014 video, audio, text or social-media posts.</li>
        <li><strong>Digital certificates</strong> of education/professional training; <strong>CV</strong>; <strong>motivation letter</strong>; language self-assessment.</li>
        <li>Passport copy; residency permit (for non-EU citizens living in the EU). Internship certificates and employment references welcome.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register your email</strong> on the official DW online application portal (opened 13 October 2026) \u2014 you will receive the application tasks by email.</li>
        <li><strong>Complete all mandatory tasks</strong> \u2014 questionnaire, application video, work samples, documents \u2014 before <strong>17 November 2026, 12:00 p.m. CET</strong>.</li>
        <li><strong>Selection stages:</strong> shortlisted applicants (about 50\u201360) are invited to an <strong>online assessment centre</strong> (timed writing test, guided discussion, camera/TikTok task), conducted in German and English; around 20 reach the <strong>final round</strong>, where DW management makes the decision.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> the 2026 traineeship has long concluded. This page covers the <strong>open 2028/29 call</strong> (programme Jan 2028 \u2013 Jun 2029). Note that good <strong>German is genuinely required</strong> for all three language profiles \u2014 this is not an English-only programme \u2014 and that the 12 places make it one of Germany\u2019s most competitive media traineeships.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the DW Journalism Traineeship 2028/29?","An 18-month paid journalism training programme at Deutsche Welle, Germany\u2019s international broadcaster: six months of seminars in German and English, nine months of placements in Bonn, Berlin and a DW foreign bureau, and a one-month elective. It runs 3 January 2028 to June 2029 with about 12 trainees."),
 ("When is the deadline?","17 November 2026 at 12:00 p.m. CET. The application window opened 13 October 2026 at 12:00 p.m. CEST, and all mandatory tasks must be completed in the online portal by the deadline."),
 ("How much does it pay?","A monthly training salary of \u20ac2,196 for months 1\u20136, \u20ac2,374 for months 7\u201312, and \u20ac2,473 for months 13\u201318, before tax."),
 ("Who can apply?","Applicants of all nationalities with a completed university degree, college qualification or apprenticeship. You need one of three language profiles (native DW broadcast language + excellent English + good German; native English + good German; or native German + excellent English), plus initial journalism experience and social media expertise."),
 ("Do I need a journalism degree?","No. DW explicitly encourages applicants from non-journalism fields such as IT, science, politics, economics, law and medicine \u2014 but you must demonstrate initial reporting experience and submit up to three work samples."),
 ("How are trainees selected?","Through the online application (form, questionnaire, video application, work samples), then an online assessment centre for about 50\u201360 shortlisted candidates, then a final round for around 20, with DW management making the final decision."),
]),
 verify='Verified 20 Oct 2026 against 7 independent tracker pages, all mutually consistent on the current call (application window 13 Oct \u2013 17 Nov 2026 12 p.m. CET; 18-month programme 3 Jan 2028 \u2013 Jun 2029; salary bands \u20ac2,196/\u20ac2,374/\u20ac2,473; ~12 trainees; Bonn/Berlin + foreign bureaus incl. Delhi and Jakarta; three language profiles incl. Hindi/Urdu/Bengali/Tamil broadcast languages; initial journalism experience; up-to-3 work samples; mandatory video application; no certificates required; selection via assessment centre and final round). The 2026 cycle was re-scoped to this open 2028/29 call. Apply through the official DW careers portal (dw.com careers section) \u2014 the portal link is published on DW\u2019s own careers pages; confirm it there before applying.',
 offlinks=[],
 related_titles=['unicef-2026','unu-junior-fellows-2027','ba-2027','wb-gaf'],
),
dict(
 slug='erasmus-mundus-noha-scholarship-2027-29-europe',
 title='Erasmus Mundus NOHA Scholarship 2027\u20132029 in Europe (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus NOHA Scholarship 2027\u20132029: \u20ac1,400/month for a two-year Joint Master\u2019s in International Humanitarian Action across 8 European universities. Deadline 15 December 2026.',
 short='Erasmus Mundus NOHA Scholarship 2027\u20132029', kicker='Master\u2019s Scholarship \u00b7 Europe',
 mono='NO', prov_short='NOHA Network on Humanitarian Action', prov_long='NOHA Network on Humanitarian Action (coordinated by the University of Deusto)', prov_cat='Erasmus Mundus \u00b7 Europe',
 h1='Erasmus Mundus NOHA Scholarship 2027\u20132029',
 sub='Study humanitarian action across Europe \u2014 a two-year joint master\u2019s delivered by eight universities, with Erasmus Mundus scholarships worth \u20ac1,400 a month.',
 dpill='15 Dec 2026 \u00b7 56 days to go', dl_long='15 December 2026, 23:59 GMT (Erasmus Mundus scholarship deadline; applications opened 1 October 2026 \u2014 do not wait for the later self-funded deadlines)',
 facts=facts([('Funding','\u20ac1,400/month for 24 months<small>Maximum \u20ac33,600 \u00b7 participation costs covered \u00b7 only 16 scholarships for 2027\u20132029</small>'),
              ('Degree','Joint Master\u2019s, 120 ECTS<small>International Humanitarian Action \u00b7 8 universities \u00b7 mobility in at least 2 countries</small>'),
              ('Deadline','15 December 2026<small>23:59 GMT \u00b7 self-funded: 1 Apr 2027 (central) / 1 Jul 2027 (non-EU without residence permit)</small>'),
              ('Who can apply','All nationalities<small>Bachelor\u2019s in a relevant field; humanitarian experience strongly valued</small>'),
              ('Languages','Mainly English<small>French or Spanish required for specific universities</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>NOHA Erasmus Mundus Joint Master\u2019s Degree in International Humanitarian Action</strong> is delivered by the <strong>Network on Humanitarian Action (NOHA)</strong> \u2014 eight European universities in <strong>France</strong> (Aix-Marseille), <strong>Germany</strong> (Ruhr-Bochum), <strong>Ireland</strong> (University College Dublin), <strong>Malta</strong>, the <strong>Netherlands</strong> (Groningen), <strong>Poland</strong> (Warsaw), <strong>Spain</strong> (University of Deusto, the coordinator) and <strong>Sweden</strong> (Uppsala) \u2014 with regional training options at partner institutions on other continents. The degree is <strong>120 ECTS over two years (four semesters)</strong>, with compulsory international mobility: you study in <strong>at least two European countries</strong>, can do regional training or a work placement in the third semester, and write your master\u2019s thesis in the fourth. Applications for the <strong>2027\u20132029 intake opened 1 October 2026</strong>, and the <strong>Erasmus Mundus scholarship deadline is 15 December 2026 at 23:59 GMT</strong>.</p>
      <div class="honest-note"><strong>Extremely competitive:</strong> only <strong>16 Erasmus Mundus scholarships</strong> are available for the 2027\u20132029 intake (4 for Programme-Country candidates, 8 for Partner-Country candidates, 4 for targeted regions \u2014 with no more than 10% to any single nationality). NOHA states that successful candidates generally combine <strong>exceptional academic performance with prior humanitarian-action experience</strong>.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>A <strong>bachelor\u2019s degree</strong> in a relevant field \u2014 law, social sciences, medical sciences, engineering or humanities (completed, or on track to complete, by 15 December 2026).</li>
        <li><strong>All nationalities</strong> may apply; you select a preferred home university for the first semester and host universities for the second, so check each university\u2019s <strong>academic and language requirements</strong> before ranking preferences.</li>
        <li><strong>Language:</strong> the programme is mainly in English, but <strong>French or Spanish</strong> are required for specific universities.</li>
        <li>You must <strong>not have previously held an Erasmus Mundus Joint Master\u2019s scholarship</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac1,400 per month for up to 24 months</strong> \u2014 a maximum of <strong>\u20ac33,600</strong> \u2014 as a contribution to travel, visa, installation and living costs, plus <strong>coverage of participation costs</strong> for scholarship holders.</li>
        <li>A <strong>joint master\u2019s degree</strong> delivered by eight European universities with built-in international mobility and a 3,500+-strong international alumni community.</li>
        <li>Options for <strong>regional training or a work placement</strong> in the third semester.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the published 2027\u20132029 application checklists (confirm against the official NOHA application form, which may vary by home university):</p>
      <ul>
        <li><strong>Passport copy</strong> and <strong>proof of residence</strong> (required for the Erasmus Mundus scholarship route).</li>
        <li><strong>Bachelor\u2019s diploma</strong> (or official proof of completion) and <strong>academic transcripts</strong>.</li>
        <li><strong>CV in English</strong> and a <strong>statement of motivation</strong> showing your humanitarian experience and commitment.</li>
        <li><strong>Two signed and dated reference letters</strong> and a <strong>required language certificate</strong>.</li>
        <li>Publications, where applicable.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Review the programme</strong> \u2014 participating universities, specialisations, and each university\u2019s national admission and language requirements \u2014 on the official NOHA site (nohanet.org).</li>
        <li><strong>Choose your home and host university preferences</strong> for the first and second semesters.</li>
        <li><strong>Apply online</strong> through the official NOHA application system (apply.nohanet.org) \u2014 there is <strong>no separate Erasmus Mundus scholarship form</strong>; you tick the scholarship option in the joint application.</li>
        <li><strong>Submit the complete application by 15 December 2026, 23:59 GMT</strong> for scholarship consideration. Do not wait for the later self-funded deadlines (1 April 2027 central; 1 July 2027 for applicants without EU citizenship or a valid EU residence permit) \u2014 those are for non-scholarship applicants only.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> this page covers the announced <strong>2027\u20132029 intake</strong> (applications opened 1 October 2026). Scholarship selection results are expected by the end of March 2027. Always confirm the document checklist on the official NOHA application system before submitting, since university-specific requirements can differ.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the NOHA Erasmus Mundus Scholarship 2027\u20132029?","A fully funded Erasmus Mundus Joint Master\u2019s in International Humanitarian Action: a 120-ECTS, two-year degree delivered by eight European universities (France, Germany, Ireland, Malta, the Netherlands, Poland, Spain and Sweden) with compulsory mobility in at least two countries, coordinated by the University of Deusto."),
 ("When is the deadline?","15 December 2026 at 23:59 GMT for Erasmus Mundus scholarship consideration. Self-funded applicants have later deadlines (1 April 2027 central; 1 July 2027 for applicants without EU citizenship or a valid EU residence permit) \u2014 but those do not carry the scholarship."),
 ("How much is the scholarship worth?","\u20ac1,400 per month for up to 24 months \u2014 a maximum of \u20ac33,600 \u2014 plus coverage of participation costs. Only 16 scholarships are awarded for the 2027\u20132029 intake, and no more than 10% may go to one nationality."),
 ("Who can apply?","All nationalities with a bachelor\u2019s in a relevant field (law, social sciences, medical, engineering, humanities). The programme is mainly in English, with French or Spanish required at specific universities. Prior humanitarian experience is strongly valued, and you must not have held an Erasmus Mundus Joint Master\u2019s scholarship before."),
 ("How do I apply?","Apply online through the official NOHA application system (apply.nohanet.org) \u2014 there is no separate scholarship form; you select the Erasmus Mundus scholarship option in the joint application and submit everything by 15 December 2026, 23:59 GMT."),
]),
 verify='Verified 20 Oct 2026 against 8 independent tracker pages, all mutually consistent on the 2027\u20132029 intake (applications opened 1 Oct 2026; scholarship deadline 15 Dec 2026 23:59 GMT; \u20ac1,400/month \u00d7 24 = \u20ac33,600; 16 scholarships with the 4/8/4 country-group split and 10% nationality cap; 120 ECTS; the eight universities; mobility in \u22652 countries; no prior EMJM scholarship rule; self-funded deadlines 1 Apr 2027 / 1 Jul 2027; selection criteria incl. humanitarian experience; results by end March 2027). The official network site (nohanet.org) and application portal (apply.nohanet.org) are cited by the trackers as the authoritative sources. The 2026 cycle was re-scoped to the announced 2027\u20132029 intake.',
 offlinks=[],
 related_titles=['mipdal-2027','membiomed-2027','each','gem2027'],
),
dict(
 slug='crossculture-programme-ccp-fellowships-2027-germany',
 title='CrossCulture Programme (CCP) Fellowships 2027 in Germany (Fully Funded) | StudyDesk Scholarships',
 meta='CCP Fellowships 2027: fully funded 2\u20133 month professional exchange in Germany for civil-society professionals. \u20ac650/month stipend, deadline 8 December 2026. Eligibility and how to apply.',
 short='CrossCulture Programme (CCP) Fellowships 2027', kicker='Fellowship \u00b7 Germany',
 mono='CCP', prov_short='ifa (Institut f\u00fcr Auslandsbeziehungen)', prov_long='ifa \u2013 Institut f\u00fcr Auslandsbeziehungen (funded by the German Federal Foreign Office)', prov_cat='Cultural Institute \u00b7 Germany',
 h1='CrossCulture Programme (CCP) Fellowships 2027',
 sub='Spend two to three months working with a host organisation in Germany \u2014 fully funded, for civil-society professionals and volunteers from India and 40+ other countries.',
 dpill='8 Dec 2026 \u00b7 49 days to go', dl_long='8 December 2026 (application window opened October 2026 on the official CCP portal; confirm the exact time-of-day on the official page)',
 facts=facts([('Funding','\u20ac650/month stipend<small>Plus round-trip airfare, accommodation, health insurance, local transport, visa-fee reimbursement</small>'),
              ('Duration','2\u20133 months<small>Fellowship period May\u2013November 2027 \u00b7 50\u201360 fellows from 40+ countries</small>'),
              ('Deadline','8 December 2026<small>Applications currently accepted on the official portal</small>'),
              ('Who can apply','Civil-society professionals + volunteers<small>23+; \u22652 yrs experience; solid English; registered students NOT eligible</small>'),
              ('Fields','Policy, media, human rights, climate<small>Policy & society \u00b7 media & culture \u00b7 human rights & peace \u00b7 sustainable development & climate justice</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>CrossCulture Programme (CCP)</strong>, run by <strong>ifa (Institut f\u00fcr Auslandsbeziehungen)</strong> and funded by the <strong>German Federal Foreign Office</strong>, funds <strong>50\u201360 professionals and volunteers</strong> from <strong>over 40 countries</strong> each year. Fellows spend <strong>two to three months</strong> working with host organisations <strong>in Germany or in CCP partner countries</strong>, joining cross-cultural workshops, networking events and professional meetings \u2014 then take the experience back into their home organisations. The <strong>2027 fellowships</strong> run in the <strong>May\u2013November 2027</strong> period as on-site fellowships (digital participation is possible in individual cases, subject to funding). Applications for 2027 are <strong>currently accepted</strong> on the official CCP portal, and <strong>India is on the official list of eligible countries</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Nationality/residence:</strong> applications are currently accepted from the listed countries, which include <strong>India</strong>, Bangladesh, Nepal, Pakistan, Sri Lanka, Indonesia, the Philippines, Thailand, Vietnam and others (full list on the official programme page).</li>
        <li><strong>Age 23 or older</strong> at the time of application.</li>
        <li><strong>At least two years of proven professional experience or volunteer work</strong> in a <strong>civil society organisation</strong> in your home country.</li>
        <li><strong>Solid command of written and spoken English</strong> (German is an advantage, not a requirement).</li>
        <li>Able to undertake a <strong>prolonged stay abroad</strong> (health-wise).</li>
        <li><strong>Registered students are not eligible.</strong></li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly stipend of \u20ac650</strong>.</li>
        <li><strong>Round-trip airfare</strong> and <strong>accommodation</strong>.</li>
        <li><strong>Health insurance</strong>, a <strong>monthly public-transportation ticket</strong> for your city of residence, and <strong>reimbursement of visa fees</strong>.</li>
        <li>Professional <strong>mentorship, workshops and international networking</strong> through the CCP, plus access to the CCP alumni community.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the published 2027 application guidance (prepare these before the portal closes):</p>
      <ul>
        <li><strong>Completed online application form</strong> on the official CCP portal.</li>
        <li><strong>CV in English.</strong></li>
        <li><strong>Motivation letter</strong> using the <strong>official CCP template</strong>.</li>
        <li><strong>Recommendation letter</strong> in the <strong>prescribed format</strong>.</li>
        <li><strong>Proof of relevant professional/volunteer experience</strong> and any additional documents the programme requests.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the official programme page</strong> (applications-ccp.ifa.de) to confirm your country\u2019s eligibility and the current call details.</li>
        <li><strong>Prepare your documents</strong> \u2014 write the motivation letter and get the recommendation letter in the <strong>official templates</strong>, and prepare your CV in English.</li>
        <li><strong>Complete the online application form</strong> on the official portal and <strong>upload all documents</strong>.</li>
        <li><strong>Submit before 8 December 2026</strong> (the deadline announced across the 2027 call coverage; confirm the exact cut-off time on the official portal).</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> this page covers the open <strong>2027 fellowships</strong> (May\u2013November 2027). The 8 December 2026 deadline is per the 2027 call announcements and the official \u201capplications currently accepted\u201d status \u2014 always verify the cut-off on the official portal before submitting. Fellowships are awarded principally to people working in policy &amp; society, media &amp; culture, human rights &amp; peace, or sustainable development &amp; climate justice.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the CCP Fellowship 2027?","The CrossCulture Programme (run by ifa, funded by the German Federal Foreign Office) funds 50\u201360 professionals and volunteers from 40+ countries for 2\u20133-month placements with host organisations in Germany or CCP partner countries, during May\u2013November 2027."),
 ("When is the deadline?","8 December 2026, per the 2027 call announcements. Applications are currently accepted on the official CCP portal \u2014 confirm the exact cut-off time there before submitting."),
 ("What does it cover?","A \u20ac650 monthly stipend, round-trip airfare, accommodation, health insurance, a monthly local public-transport ticket, and reimbursement of visa fees."),
 ("Who can apply?","People aged 23+ from the listed countries (including India) with at least two years of proven professional or volunteer experience in a civil society organisation in their home country, a solid command of English, and the ability to stay abroad. Registered students cannot apply."),
 ("How do I apply?","Through the official CCP online application portal: complete the form, upload your English CV, and submit the motivation letter and recommendation letter in the programme\u2019s official templates before the deadline."),
]),
 verify='Verified 20 Oct 2026 against the official ifa CrossCulture Programme page (applications-ccp.ifa.de \u2014 50\u201360 professionals/volunteers from 40+ countries; 2\u20133 months with host organisations in Germany or partner countries; on-site 2027 fellowships; India on the eligible-country list; 23+; \u22652 years civil-society experience; solid English; health requirement) and 6 independent call announcements, mutually consistent (fellowship period May\u2013November 2027; \u20ac650/month stipend + airfare + accommodation + insurance + local transport + visa reimbursement; deadline 8 December 2026; fields: policy & society, media & culture, human rights & peace, sustainable development & climate justice; motivation/recommendation templates). The 2026 cycle was re-scoped to the open 2027 call.',
 offlinks=[('CrossCulture Programme \u2014 about the programme (official, ifa)','https://applications-ccp.ifa.de/about-the-program.html')],
 related_titles=['wb-gaf','unicef-2026','unu-junior-fellows-2027'],
),
]

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# registry appends
reg = pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').read_text()
assert "'tigp-2027'" not in reg, 'registry already has batch 27 cards'
newcards = """\\
 'tigp-2027': {'mono': 'TI', 'title': 'Taiwan International Graduate Program (TIGP) 2027 in Taiwan (Fully Funded)', 'href': 'taiwan-international-graduate-program-2027-taiwan.html',
              'dpill': '1 Feb 2027 \\\\u00b7 103 days to go', 'award': 'NT$34,000/month tax-free (first year); extendable', 'elig': 'B.S./M.Sc. holders; English proficiency; apply to one programme.',
              'tags': [('PhD', 'blue'), ('Taiwan', 'teal')]},
 'deakin-vc-2027': {'mono': 'D', 'title': "Deakin Vice-Chancellor's International Scholarship 2027 in Australia (Funded)", 'href': 'deakin-vice-chancellors-international-scholarship-2027-australia.html',
              'dpill': 'Rolling \\\\u00b7 no fixed deadline', 'award': '100% or 50% tuition for normal degree duration', 'elig': 'New international students; \\\\u226585% average (CBSE/ICSE/State Board 85% accepted).',
              'tags': [('UG/PG', 'blue'), ('Australia', 'teal')]},
 'dw-2028': {'mono': 'DW', 'title': 'Deutsche Welle DW Journalism Traineeship 2028/29 in Germany (Paid)', 'href': 'deutsche-welle-dw-traineeship-2028-29-germany.html',
              'dpill': '17 Nov 2026 \\\\u00b7 28 days to go', 'award': '\\\\u20ac2,196\\\\u2013\\\\u20ac2,473/month salary for 18 months', 'elig': 'Completed degree; English + German (profiles vary); journalism experience.',
              'tags': [('Traineeship', 'blue'), ('Germany', 'teal')]},
 'noha-2027': {'mono': 'NO', 'title': 'Erasmus Mundus NOHA Scholarship 2027\\\\u20132029 in Europe (Fully Funded)', 'href': 'erasmus-mundus-noha-scholarship-2027-29-europe.html',
              'dpill': '15 Dec 2026 \\\\u00b7 56 days to go', 'award': '\\\\u20ac1,400/month \\\\u00d7 24 (\\\\u20ac33,600) + participation costs', 'elig': 'All nationalities; bachelor\\\\u2019s in a relevant field; humanitarian experience valued.',
              'tags': [('Master\\\\u2019s', 'blue'), ('Europe', 'teal')]},
 'ccp-2027': {'mono': 'CCP', 'title': 'CrossCulture Programme (CCP) Fellowships 2027 in Germany (Fully Funded)', 'href': 'crossculture-programme-ccp-fellowships-2027-germany.html',
              'dpill': '8 Dec 2026 \\\\u00b7 49 days to go', 'award': '\\\\u20ac650/month + airfare + housing + insurance', 'elig': 'India eligible; 23+; 2 yrs civil-society experience; not students.',
              'tags': [('Fellowship', 'blue'), ('Germany', 'teal')]},
"""
reg = reg.rstrip()
assert reg.endswith('}')
reg = reg[:-1] + newcards + '}\n'
pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').write_text(reg)
print('registry appended')

# logos INFO appends
logof = pathlib.Path('/home/hatch/workspace/scholarships-17k/add-logos.py')
lt = logof.read_text()
add = """\\
 'taiwan-international-graduate-program-2027-taiwan': ('Academia Sinica', 'Research Institute \\\\u00b7 Taiwan', 'tigp'),
 'deakin-vice-chancellors-international-scholarship-2027-australia': ('Deakin University', 'University \\\\u00b7 Australia', 'deakin'),
 'deutsche-welle-dw-traineeship-2028-29-germany': ('Deutsche Welle', 'Broadcaster \\\\u00b7 Germany', 'dw'),
 'erasmus-mundus-noha-scholarship-2027-29-europe': ('NOHA Network on Humanitarian Action', 'Erasmus Mundus \\\\u00b7 Europe', 'noha'),
 'crossculture-programme-ccp-fellowships-2027-germany': ('ifa (Institut f\u00fcr Auslandsbeziehungen)', 'Cultural Institute \\\\u00b7 Germany', 'ifa'),
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
    for needle in ['AICTE Pragati', 'Lorem', 'data:image']:
        assert needle not in pathlib.Path(OUT / (a['slug'] + '.html')).read_text(), (a['slug'], needle)
    print('validated', a['slug'])

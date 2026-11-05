#!/usr/bin/env python3
"""Batch 26 (cron run 26, 20 Oct 2026): 5 verified articles.

All prose original. Verification completed 20 Oct 2026 across 9 waves.

WRITTEN this run:
- NUS Amgen Scholars Program 2027 (re-scoped: 2026 cycle closed 1 Feb 2026; 2027
  deadline 1 Feb 2027 on official amgenscholars.com; 2027 funding/dates not published)
- HKU ADB Scholarship 2027 (re-scoped: 2026 cycle closed; 2027 deadline 29 Jan 2027
  noon HK time on official HKU Faculty of Architecture page; exact amounts not published)
- Dalian University of Technology CSC Scholarship 2027 (re-scoped: 2026 Type B window
  closed 15 Feb 2026; 2027 Type B notice published 23 Sep 2026, window 1 Nov 2026 - 15 Feb 2027,
  agency 10141; official DUT page not directly fetchable in-session - corroborated from
  5 independent trackers quoting the notice, flagged as such)
- NPU International Scholarships 2027 (re-scoped: 2026 closed; official 2027 admission
  season published 13 Oct 2026 - President Scholarship tiers + CSC Type B; document list
  and CSC stipend figures not on official pages - omitted)
- Erasmus Mundus MIPDaL Scholarship 2027 (re-scoped: 2026 closed 15 Jan 2026; 2027 portal
  opened 1 Oct 2026, scholarship deadline 15 Jan 2027; aggregator 1400/month and 2-year
  claims contradicted by official 1-year programme - not used)

SKIPS this run (deadline passed / closed cycles / not announced):
- RIPS Summer Internship 2026 (2026 cycle closed Feb 2026; 2027 not announced; official
  FAQ excludes foreign students not studying in the US)
- Erasmus Mundus PROMISE 2026 (2026 intake officially cancelled by consortium;
  2027 prospective only, conditional on Summer 2027 grant decision)
- Caltech SURF 2026 (deadline 22 Feb 2026 - past; 2027 not announced; "fully funded"
  framing misleading - it is a stipend, not full-cost coverage)
- University of Debrecen Hungarian Scholarships 2026 (Stipendium Hungaricum 2026/27
  closed 15 Jan 2026; 2027/28 call not yet published by Tempus - expected ~Nov 2026)
- HZB International Summer Program 2026 (2026 cycle closed, official deadline 14 Dec 2025;
  2027 not announced anywhere)
- University of Bradford Scholarship 2026 (aggregator umbrella - 33+ separate named
  awards with different deadlines; no single official scheme by that name)
"""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'amgen-2027': dict(mono='AM', title='NUS Amgen Scholars Program 2027 in Singapore (Fully Funded)', href='nus-amgen-scholars-program-2027-singapore.html',
              dpill='1 Feb 2027 \u00b7 104 days to go', award='Full package (2027 figures not published)', elig='Asia undergrads; 1st year done; not graduating before programme.',
              tags=[('Internship','blue'),('Singapore','teal')]),
 'adbhku-2027': dict(mono='ADB', title='HKU ADB Scholarship 2027 in Hong Kong (Fully Funded)', href='hku-adb-scholarship-2027-hong-kong.html',
              dpill='29 Jan 2027 \u00b7 101 days to go', award='Full tuition + allowances (amounts not published)', elig='ADB member-country citizens; master\u2019s; \u226435; 2 yrs work experience.',
              tags=[('Master\u2019s','blue'),('Hong Kong','teal')]),
 'dut-2027': dict(mono='DUT', title='Dalian University of Technology CSC Scholarship 2027 in China (Fully Funded)', href='dalian-university-csc-scholarship-2027-china.html',
              dpill='15 Feb 2027 \u00b7 118 days to go', award='Tuition waiver + CNY 3,000\u20133,500/month', elig='Non-Chinese; master\u2019s <35; doctoral <40.',
              tags=[('Master\u2019s','blue'),('China','teal')]),
 'npu-2027': dict(mono='NPU', title='NPU International Scholarships 2027 in China: President Scholarship + CSC', href='npu-international-scholarships-2027-china.html',
              dpill='Batches \u00b7 final 30 Apr 2027', award='Tiers: tuition+housing waiver + RMB 1,500\u20132,500/mo \u00d710', elig='Non-Chinese; UG <23; master\u2019s <30; PhD <35.',
              tags=[('UG/PG/PhD','blue'),('China','teal')]),
 'mipdal-2027': dict(mono='MIP', title='Erasmus Mundus MIPDaL Scholarship 2027 (Fully Funded)', href='erasmus-mundus-mipdal-scholarship-2027.html',
              dpill='15 Jan 2027 \u00b7 87 days to go', award='EMJM scholarship: no tuition + monthly expense funding', elig='All nationalities; \u2265240 ECTS law degree; English C1.',
              tags=[('Master\u2019s','blue'),('Europe','teal')]),
})

ARTICLES = [
dict(
 slug='nus-amgen-scholars-program-2027-singapore',
 title='NUS Amgen Scholars Program 2027 in Singapore (Fully Funded) | StudyDesk Scholarships',
 meta='NUS Amgen Scholars Program 2027: 8-week paid summer research at the National University of Singapore, deadline 1 February 2027. Eligibility for Asia undergraduates, English requirements, documents, and how to apply.',
 short='NUS Amgen Scholars Program 2027', kicker='Research Internship \u00b7 Singapore',
 mono='AM', prov_short='Amgen Foundation', prov_long='Amgen Foundation (Amgen Scholars Program, Asia Program)', prov_cat='Foundation \u00b7 Singapore',
 h1='NUS Amgen Scholars Program 2027',
 sub='Spend eight weeks doing full-time scientific research in a lab at the National University of Singapore \u2014 the Amgen Scholars Asia Program gives undergraduate science students hands-on research experience, with a stipend, housing arranged, and a travel grant, at one of five Asia host institutions.',
 dpill='1 Feb 2027 \u00b7 104 days to go', dl_long='1 February 2027 (official Amgen Scholars Asia Program deadline; 2027 time-of-day not published; the 2026 cycle closed 18:00 SGT)',
 facts=facts([('Funding','Full package for 2027 not yet published<small>2026 NUS package: SG$6,000 stipend, housing arranged, travel grant up to SG$1,500 \u2014 for context only, not the 2027 offer</small>'),
              ('Who can apply','Undergraduates enrolled in Asia<small>First year completed; not graduating before the programme</small>'),
              ('Deadline','1 February 2027<small>Apply separately per host \u2014 NUS runs its own process</small>'),
              ('Programme','8-week summer lab research<small>2026 ran 2 Jun \u2013 31 Jul plus the Asia Symposium in Tokyo</small>'),
              ('Host','National University of Singapore<small>One of five Amgen Scholars Asia host institutions</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p>The <strong>Amgen Scholars Program</strong>, run by the <strong>Amgen Foundation</strong>, places undergraduate science students in university laboratories for a full-time summer of research. In Asia, the programme runs at <strong>five host institutions</strong> \u2014 including the <strong>National University of Singapore (NUS)</strong> \u2014 and the 2027 cycle has been officially announced with an application deadline of <strong>1 February 2027</strong>. The 2026 cycle (deadline 1 February 2026) is closed and its programme ran in June\u2013July 2026, followed by the Asia Symposium in Tokyo.</p>
      <div class="honest-note"><strong>2027 details are still being published:</strong> the official Amgen Scholars Asia page confirms the 1 February 2027 deadline, but the 2027 funding package, exact programme dates, and the opening date of the NUS application are <strong>not published in the official notification</strong> yet. Figures from the 2026 cycle below are marked as past-cycle context and are not the 2027 offer.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Enrolled undergraduate</strong> at a degree-awarding college or university <strong>in Asia</strong> (the programme uses the UN DESA Asia region \u2014 which includes India and countries across Eastern, South-Eastern, Central, Southern and Western Asia). Your <strong>nationality</strong> does not have to be Asian; your university must be in Asia.</li>
        <li>Must have <strong>completed at least the first year</strong> of undergraduate study by the time the programme begins.</li>
        <li><strong>Not graduating before the programme begins</strong>, and you must <strong>resume undergraduate studies for at least one semester or quarter</strong> after the programme ends.</li>
        <li>A <strong>strong record of academic performance</strong> and a genuine interest in pursuing a <strong>PhD in science or biotechnology</strong> research.</li>
        <li><strong>English proficiency:</strong> non-native speakers need TOEFL iBT 72, IELTS 5.5, Cambridge English FCE, TOEIC 1095 (or TOEIC L&amp;R 785 / S&amp;W 310) \u2014 <strong>or</strong> a letter from your university stating that the medium of instruction is fully in English.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Eight weeks of <strong>full-time supervised laboratory research</strong> at NUS.</li>
        <li>Stipend, <strong>arranged accommodation</strong>, and a <strong>travel grant</strong> \u2014 exact 2027 figures are <strong>not published</strong>. For context, the 2026 NUS package was an SG$6,000 stipend, accommodation arranged by NUS, a travel grant of up to SG$1,500 for international scholars, and visa/TEP fees covered; scholars arranged their own health and travel insurance.</li>
        <li>Participation in the <strong>Amgen Scholars Asia Symposium</strong> with scholars from the other Asia host institutions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the official NUS host-page checklist (2026 pattern; confirm against the 2027 portal once it opens):</p>
      <ul>
        <li>Completed <strong>online application form</strong>.</li>
        <li><strong>Academic transcripts</strong> (foreign-language transcripts must be accompanied by English translations).</li>
        <li><strong>Proof of English proficiency</strong> or a university letter confirming English-medium instruction.</li>
        <li>Current <strong>CV</strong> and <strong>personal identification</strong>.</li>
        <li>At least <strong>two referee nominations</strong> (referees must use professional email addresses; they receive a two-week submission window and are not notified to you on receipt).</li>
        <li>Documents collated in <strong>one ZIP folder labelled with your full name</strong>; there are <strong>three extra days after the deadline</strong> for document uploads.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply separately to each Asia host \u2014</strong> there is no single Asia-wide application form. If you want NUS, apply through the <strong>NUS application process</strong>.</li>
        <li><strong>Complete the online application</strong> on the NUS Amgen Scholars outreach page (hosted by the Department of Biological Sciences).</li>
        <li><strong>Nominate at least two referees</strong> and assemble all documents <strong>before</strong> submitting \u2014 then upload the ZIP folder within the three days after the deadline.</li>
        <li><strong>Meet the 1 February 2027 deadline</strong> (the 2026 deadline was 18:00 SGT; no 2027 time-of-day is published \u2014 do not assume a midnight cut-off).</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> the 2026 application cycle closed on 1 February 2026 and that programme has already run. This page covers the <strong>announced 2027 cycle</strong> with its confirmed 1 February 2027 deadline; funding figures and programme dates for 2027 have not yet been published officially.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the NUS Amgen Scholars Program 2027?","The Amgen Scholars Program (Asia), run by the Amgen Foundation, offers undergraduates eight weeks of full-time summer laboratory research at one of five Asia host institutions, including the National University of Singapore. The 2027 cycle is announced with a 1 February 2027 deadline."),
 ("When is the 2027 deadline?","1 February 2027, per the official Amgen Scholars Asia Program page. The 2026 cycle closed on 1 February 2026 and has already run."),
 ("How much does the programme pay?","The 2027 funding package is not published yet. For context, the 2026 NUS package was an SG$6,000 stipend, arranged accommodation, a travel grant of up to SG$1,500 for international scholars, and covered visa/TEP fees \u2014 those are past-cycle figures, not the 2027 offer."),
 ("Who is eligible?","Undergraduates enrolled at a degree-awarding college or university in Asia who have completed their first year, are not graduating before the programme, and will resume studies for at least one semester afterwards \u2014 with a strong academic record and an interest in a science or biotechnology PhD. Nationality need not be Asian."),
 ("How do I apply to the NUS host?","Applications are made separately to each Asia host \u2014 there is no single Asia-wide form. Complete the NUS online application, nominate at least two referees, collate documents in one ZIP folder labelled with your full name, and upload within three days after the deadline."),
]),
 verify='Verified 20 Oct 2026 against the official Amgen Scholars Asia Program page (amgenscholars.com/asia-program \u2014 1 Feb 2027 deadline for all five Asia hosts, Asia-region eligibility, PhD-orientation) and the NUS Department of Biological Sciences Amgen Scholars outreach page (2026 package SG$6,000 stipend + arranged housing + up to SG$1,500 travel grant; English-test thresholds or English-medium letter; \u22652 referees; ZIP-folder upload with 3 extra days; separate application per host). 2027 funding package, 2027 programme dates and 2027 portal opening date are not published in the official notification \u2014 omitted, with 2026 figures labelled as past-cycle context only. The 2026 cycle (closed 1 Feb 2026) was re-scoped to the announced 2027 cycle.',
 offlinks=[('Amgen Scholars Asia Program (official) \u2014 eligibility, 2027 deadline','https://amgenscholars.com/asia-program/'),
           ('NUS Department of Biological Sciences \u2014 Amgen Scholars page (official)','https://www.dbs.nus.edu.sg/outreach/amgen-scholars-program/')],
 related_titles=['adbhku-2027','dut-2027','npu-2027','mipdal-2027'],
),
dict(
 slug='hku-adb-scholarship-2027-hong-kong',
 title='HKU ADB Scholarship 2027 in Hong Kong (Fully Funded) | StudyDesk Scholarships',
 meta='HKU ADB Scholarship 2027: the Asian Development Bank\u2013Japan Scholarship Program at the University of Hong Kong. Deadline 29 January 2027 (noon HK time), eligibility, funding package, designated programmes, and how to apply.',
 short='HKU ADB Scholarship 2027', kicker='Government-Funded Scholarship \u00b7 Hong Kong',
 mono='ADB', prov_short='Asian Development Bank', prov_long='Asian Development Bank (ADB), funded by the Government of Japan', prov_cat='Multilateral \u00b7 Hong Kong',
 h1='HKU ADB Scholarship 2027',
 sub='Study a master\u2019s at the University of Hong Kong with full tuition, living allowances, travel and insurance covered \u2014 the ADB\u2013Japan Scholarship Program, funded by the Government of Japan since 1988, is open for the 2027 intake with applications closing 29 January 2027.',
 dpill='29 Jan 2027 \u00b7 101 days to go', dl_long='29 January 2027, 12:00 noon Hong Kong time (published on HKU Faculty of Architecture ADB-JSP page; the 2026 cycle is closed)',
 facts=facts([('Award','Full tuition + allowances<small>Tuition, monthly subsistence (incl. housing), books, insurance, travel \u2014 exact amounts not published</small>'),
              ('Who can apply','Citizens of ADB borrowing member countries<small>Approved master\u2019s; superior bachelor\u2019s record; 2 years work experience; \u226435</small>'),
              ('Deadline','29 January 2027, noon HK time<small>Apply through HKU \u2014 never directly to ADB</small>'),
              ('Programmes','Urban Planning & Urban Design tracks<small>Designated ADB-JSP fields at HKU; admission via HKU portal</small>'),
              ('Funded by','Government of Japan via ADB<small>Programme established April 1988</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>ADB\u2013Japan Scholarship Program (ADB-JSP)</strong> is funded by the <strong>Government of Japan</strong> and administered by the <strong>Asian Development Bank</strong> (established April 1988). It sends citizens of ADB\u2019s developing member countries to designated partner institutions across Asia and the Pacific for postgraduate study. At the <strong>University of Hong Kong (HKU)</strong>, the programme is hosted by the <strong>Faculty of Architecture</strong>, with applications routed through HKU\u2019s own admissions portal. The <strong>2027 intake</strong> is announced, with a deadline of <strong>29 January 2027 at 12:00 noon (Hong Kong time)</strong>; the 2026 cycle is closed.</p>
      <div class="honest-note"><strong>Apply through HKU, not to ADB:</strong> ADB\u2019s official pages state that applications are made through the designated partner institutions only \u2014 ADB does not accept applications directly.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>National of an ADB borrowing member country</strong> that is eligible for Japanese ODA scholarships (ADB lists around 41 countries/areas, including Afghanistan, Bangladesh, Bhutan, Cambodia, India, Indonesia, Nepal, Pakistan, the Philippines, Sri Lanka and Viet Nam).</li>
        <li><strong>No dual citizenship</strong> of any developed country.</li>
        <li>Gained <strong>admission to an approved master\u2019s course</strong> at a designated institution \u2014 for HKU, the designated fields are <strong>Urban Planning and Urban Design</strong> (HKU routes applicants through the <strong>Master of Urban Design \u2014 for ADB\u2013Japan Scholarship Programme applicants</strong> admissions portal).</li>
        <li><strong>Bachelor\u2019s degree or equivalent with a superior academic record</strong>.</li>
        <li>At least <strong>two years of full-time professional working experience</strong> after the university degree.</li>
        <li><strong>Proficiency in oral and written English</strong>.</li>
        <li><strong>Not more than 35 years old</strong> at the time of application (waivable only in exceptional cases with the expressed endorsement of the Government of Japan).</li>
        <li>In <strong>good health</strong>, and agree to <strong>return and work in your home country for at least two years</strong> after completing the programme.</li>
        <li>Not an ADB Executive Director, alternate, management, staff or consultant \u2014 or a close relative of one; not staff of an ADB-JSP designated institution; <strong>not living or working in a country other than your home country</strong>; not already enrolled in a graduate degree programme.</li>
        <li><strong>HKU adds:</strong> applicants <strong>from Hong Kong and Mainland China are ineligible</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong>.</li>
        <li><strong>Monthly subsistence allowance</strong>, including housing.</li>
        <li><strong>Books and instructional materials</strong>.</li>
        <li><strong>Medical insurance</strong>.</li>
        <li><strong>Travel expenses</strong>.</li>
        <li>For research scholars, a <strong>special grant for thesis preparation</strong> may be available; computer-literacy or preparatory language courses may be covered in special circumstances.</li>
      </ul>
      <div class="honest-note"><strong>No exact monthly figures are published</strong> on the official ADB pages \u2014 this article states only the categories the programme covers.</div>
      <h2 id="documents">Documents required</h2>
      <p>The official pages mention the required application documents <strong>\u201cincluding the ADB\u2013Japan Scholarship Program information sheet\u201d</strong>, submitted to the partner institution \u2014 the full document list is <strong>not published on the official pages</strong>. Follow the document checklist on the HKU admissions portal exactly; do not rely on a generic list from a third-party site.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to the designated HKU master\u2019s programme</strong> (Master of Urban Design \u2014 for ADB\u2013Japan Scholarship Programme applicants) through the <strong>HKU tpg-admissions portal</strong>, indicating your ADB-JSP interest.</li>
        <li><strong>Complete the required application documents</strong> (including the ADB\u2013Japan Scholarship Program information sheet) and submit them to HKU per its portal instructions.</li>
        <li><strong>HKU evaluates and shortlists</strong> candidates; the <strong>final selection of scholars is made by ADB</strong>.</li>
        <li><strong>Await the evaluation results</strong> from HKU \u2014 and do not submit anything to ADB directly.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> the 2026 cycle is closed (aggregators recorded its deadline as 30 January 2026). This page covers the announced <strong>2027 intake</strong>, whose 29 January 2027 (noon, Hong Kong time) deadline is published on HKU\u2019s Faculty of Architecture ADB-JSP page.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the HKU ADB Scholarship 2027?","The ADB\u2013Japan Scholarship Program at the University of Hong Kong, funded by the Government of Japan: full tuition, subsistence, books, insurance and travel for an approved master\u2019s in the designated fields (Urban Planning, Urban Design). The 2027 intake closes 29 January 2027 at noon Hong Kong time."),
 ("Can I apply to ADB directly?","No. ADB\u2019s official pages state that applications go through the designated partner institutions only \u2014 for HKU, through the university\u2019s own admissions portal."),
 ("Who is eligible?","Nationals of ADB borrowing member countries eligible for Japanese ODA (no developed-country dual citizenship), with a superior bachelor\u2019s record, at least two years of full-time professional experience, English proficiency, aged not more than 35, who will return and work in their home country for at least two years afterwards."),
 ("Can Hong Kong or Mainland China residents apply?","HKU states that applicants from Hong Kong and Mainland China are ineligible for this scholarship."),
 ("How much is the scholarship worth?","The official ADB pages list the coverage categories (tuition, monthly subsistence including housing, books, medical insurance, travel) but publish no exact monthly figures \u2014 this page states only what the official pages state."),
]),
 verify='Verified 20 Oct 2026 against the official HKU Faculty of Architecture ADB-JSP page (arch.hku.hk \u2014 29 Jan 2027, 12:00 noon HK-time deadline; Hong Kong/Mainland China ineligibility note; HKU tpg-admissions portal route for the Master of Urban Design \u2014 for ADB-JSP applicants) and the official ADB JSP pages (adb.org \u2014 full eligibility list verbatim, funding categories, 41 eligible countries/areas, \u201cthe institution, not ADB\u201d application route, August 2026 brochure). Exact monthly amounts are not published on the official ADB pages \u2014 omitted. The full document list is not published on the official pages \u2014 flagged, with the portal named as the authority. The 2026 cycle is closed (re-scoped to the announced 2027 intake).',
 offlinks=[('HKU Faculty of Architecture \u2014 ADB-JSP page (official, 2027 deadline)','https://www.arch.hku.hk/programmes/upad/master-of-urban-design/scholarship/'),
           ('ADB Japan Scholarship Program (official) \u2014 eligibility, funding, application','https://www.adb.org/work-with-us/careers/japan-scholarship-program'),
           ('ADB-JSP brochure, August 2026 (official PDF)','https://www.adb.org/sites/default/files/publication/29268/jsp-brochure.pdf')],
 related_titles=['amgen-2027','dut-2027','npu-2027','mipdal-2027'],
),
dict(
 slug='dalian-university-csc-scholarship-2027-china',
 title='Dalian University of Technology CSC Scholarship 2027 in China (Fully Funded) | StudyDesk Scholarships',
 meta='Dalian University of Technology CSC Scholarship 2027: Chinese Government Scholarship Type B (agency 10141) for master\u2019s and PhD. Window 1 Nov 2026 \u2013 15 Feb 2027. Stipend, eligibility, documents, and how to apply.',
 short='Dalian CSC Scholarship 2027', kicker='Government Scholarship \u00b7 China',
 mono='DUT', prov_short='Dalian University of Technology', prov_long='Dalian University of Technology (DUT), Dalian, China \u2014 Chinese Government Scholarship, Ministry of Education, P.R.C.', prov_cat='University \u00b7 China',
 h1='Dalian University of Technology CSC Scholarship 2027',
 sub='A fully funded Chinese Government Scholarship at Dalian University of Technology for master\u2019s and doctoral students \u2014 full tuition waiver, free on-campus accommodation, a monthly stipend, and medical insurance, with applications open 1 November 2026 to 15 February 2027.',
 dpill='15 Feb 2027 \u00b7 118 days to go', dl_long='15 February 2027 (Type B window: 1 November 2026 \u2013 15 February 2027; time-of-day not published \u2014 do not assume a midnight cut-off)',
 facts=facts([('Award','Full tuition waiver + CNY 3,000\u20133,500/month<small>Master\u2019s CNY 3,000/month; doctoral CNY 3,500/month; free on-campus housing; insurance</small>'),
              ('Who can apply','Non-Chinese citizens \u2014 master\u2019s & PhD only<small>Master\u2019s: bachelor\u2019s + under 35; doctoral: master\u2019s + under 40</small>'),
              ('Deadline','15 February 2027<small>Window opens 1 Nov 2026; apply in BOTH the CSC and DUT systems (agency 10141, Type B)</small>'),
              ('Not covered','International travel<small>Travel to/from China is self-funded</small>'),
              ('Language','HSK 4/5 or English tests<small>Science/engineering: HSK 4 (180+); humanities: HSK 5 (180+); or TOEFL 80+ / IELTS 5.5+ / Duolingo 100+</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Chinese Government Scholarship (CSC)</strong> is run by the <strong>Ministry of Education of the People\u2019s Republic of China</strong>. At <strong>Dalian University of Technology (DUT)</strong>, the scholarship is offered through the <strong>High-Level Postgraduate Program and the Silk Road Program</strong> \u2014 known as <strong>Type B</strong> (CSC agency number <strong>10141</strong>). The 2027 call was published by DUT\u2019s School of International Education on <strong>23 September 2026</strong>, with applications running from <strong>1 November 2026 to 15 February 2027</strong> for <strong>master\u2019s and doctoral applicants only</strong> \u2014 this is not a bachelor\u2019s award. The 2026 window (1 November 2025 \u2013 15 February 2026) is closed.</p>
      <div class="honest-note"><strong>Source note:</strong> DUT\u2019s official notice page could not be fetched directly in this session, so every fact below is corroborated from <strong>multiple independent trackers citing the official 23 September 2026 notice</strong> \u2014 where they disagreed, the detail was omitted. The time of day for the 15 February 2027 closing is <strong>not published</strong>; do not assume a midnight Beijing-time cut-off.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizen</strong> in good health.</li>
        <li><strong>Master\u2019s applicants:</strong> hold a bachelor\u2019s degree and be <strong>under 35</strong>.</li>
        <li><strong>Doctoral applicants:</strong> hold a master\u2019s degree and be <strong>under 40</strong>.</li>
        <li><strong>Language requirements:</strong> for <strong>Chinese-taught programmes</strong> \u2014 science, engineering, economics and management majors: new <strong>HSK Level 4 with a minimum score of 180</strong>; humanities and foreign-language majors: new <strong>HSK Level 5 with a minimum score of 180</strong>. For <strong>English-taught programmes</strong>: TOEFL 80+, IELTS 5.5+ or Duolingo 100+ \u2014 or a certificate that previous instruction was in English, or exemption for applicants from countries where English is an official language.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver</strong>.</li>
        <li><strong>Free on-campus accommodation</strong>.</li>
        <li><strong>Monthly stipend:</strong> CNY 3,000 for master\u2019s students; CNY 3,500 for doctoral students.</li>
        <li><strong>CSC comprehensive medical insurance</strong>.</li>
        <li><strong>International travel is self-funded.</strong></li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Per the cited 2027 notice (corroborated across trackers; confirm against the official notice if in doubt):</p>
      <ul>
        <li>CSC application form (<strong>printed and signed</strong>) and the DUT application form.</li>
        <li><strong>Notarized highest diploma</strong> (plus notarized Chinese or English translations) and sealed academic transcripts.</li>
        <li><strong>Study-plan proposal</strong> of at least 1,000 words (in Chinese or English), <strong>signed by a DUT supervisor</strong> \u2014 note that a supervisor\u2019s acceptance letter is optional, but the study plan itself needs the supervisor\u2019s signature, so contact academics early.</li>
        <li><strong>Two recommendation letters</strong> from professors or associate professors.</li>
        <li><strong>Foreigner Physical Examination Form</strong> (valid for 6 months) plus a <strong>blood test report</strong> (HIV, syphilis, HBsAg, HCV).</li>
        <li><strong>Passport photo page and blank visa page</strong> copies; language proficiency certificates; <strong>Certificate of No Criminal Conviction</strong> (valid for 6 months).</li>
        <li>Optional: supervisor acceptance letter, employment certificate, passport-sized photo.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply on the CSC portal</strong> (campuschina.org) \u2014 select Type B with DUT agency number <strong>10141</strong>; print and sign the completed form.</li>
        <li><strong>Submit the DUT online application</strong> at iso.dlut.edu.cn, selecting the <strong>\u201cScholarship\u201d project</strong> \u2014 an application number is generated for your submission.</li>
        <li><strong>Complete both systems before 15 February 2027.</strong></li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> the 2026 Type B window closed on 15 February 2026. This page covers the announced <strong>2027 intake</strong> per DUT\u2019s 23 September 2026 notice; the window opens 1 November 2026. Note: the CNY 800 figure seen on some trackers is the separate self-funded admission fee, not a CSC-route charge.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the DUT CSC Scholarship 2027?","The Chinese Government Scholarship at Dalian University of Technology, offered as Type B (High-Level Postgraduate + Silk Road Programmes, agency number 10141) for master\u2019s and PhD study. The 2027 window runs 1 November 2026 to 15 February 2027."),
 ("Is it really fully funded?","The package covers full tuition, free on-campus housing, a monthly stipend (CNY 3,000 master\u2019s / 3,500 doctoral) and CSC medical insurance. International travel is self-funded."),
 ("Who can apply?","Non-Chinese citizens in good health: bachelor\u2019s holders under 35 for master\u2019s programmes, master\u2019s holders under 40 for doctoral programmes. It is master\u2019s and PhD only \u2014 not for bachelor\u2019s applicants."),
 ("What language scores do I need?","For Chinese-taught programmes: HSK 4 (score 180+) for science, engineering, economics and management; HSK 5 (180+) for humanities. For English-taught programmes: TOEFL 80+, IELTS 5.5+ or Duolingo 100+, or proof of prior English-medium instruction (exemptions for English-official-language countries)."),
 ("How do I apply?","In two systems: (1) the CSC portal (campuschina.org), Type B, agency 10141 \u2014 print and sign the form; (2) the DUT online application at iso.dlut.edu.cn, selecting the \u201cScholarship\u201d project. Both must be completed by 15 February 2027."),
]),
 verify='Verified 20 Oct 2026: DUT\u2019s 2027 Type B notice (High-Level Postgraduate + Silk Road Programmes) published 23 Sep 2026 per DUT\u2019s School of International Education, with window 1 Nov 2026 \u2013 15 Feb 2027, agency 10141, master\u2019s/PhD only, tuition waiver + free on-campus accommodation + CNY 3,000 (master\u2019s) / 3,500 (doctoral) monthly stipend + CSC insurance, travel self-funded \u2014 corroborated from five independent trackers citing the notice (cscpath.com, daadscholarship.com, scholarshipunion.com, scholarshipsland.com, scholarshipforphd.com), cross-checked for consistency. sie.dlut.edu.cn could not be fetched directly in this session \u2014 this is stated in-article. Disputed or single-source claims omitted (2027 time-of-day, 800 RMB CSC-route fee, bachelor\u2019s eligibility). The 2026 window (closed 15 Feb 2026) was re-scoped to the announced 2027 intake.',
 offlinks=[('Chinese Government Scholarship portal (official) \u2014 campuschina.org','http://www.campuschina.org/'),
           ('DUT online application \u2014 iso.dlut.edu.cn (official)','http://iso.dlut.edu.cn/')],
 related_titles=['amgen-2027','adbhku-2027','npu-2027','mipdal-2027'],
),
dict(
 slug='npu-international-scholarships-2027-china',
 title='NPU International Scholarships 2027 in China: President Scholarship + CSC | StudyDesk Scholarships',
 meta='NPU International Scholarships 2027: Northwestern Polytechnical University\u2019s President Scholarship (four tiers, announced 13 Oct 2026) and CSC University Program Type B for the 2027 admission season. Tiers, deadlines, eligibility, and how to apply.',
 short='NPU International Scholarships 2027', kicker='University Scholarships \u00b7 China',
 mono='NPU', prov_short='Northwestern Polytechnical University', prov_long='Northwestern Polytechnical University (NPU), Xi\u2019an, China', prov_cat='University \u00b7 China',
 h1='NPU International Scholarships 2027',
 sub='Northwestern Polytechnical University in Xi\u2019an has opened its 2027 admission season with two genuine international scholarship routes: the tiered NPU President Scholarship and the Chinese Government Scholarship (University Program, Type B) \u2014 with four application batches running from November 2026.',
 dpill='Batches \u00b7 final 30 Apr 2027', dl_long='Four batches from 1 November 2026; final deadline 30 April 2027 17:00 (postgrad) / 20 May 2027 (undergrad); CSC batches close 31 Dec 2026 and 28 Feb 2027 (GMT+8)',
 facts=facts([('Award','President Scholarship tiers + CSC Type B<small>Elite: tuition + housing waiver + RMB 1,500\u20132,500/mo \u00d7 10; First level: full tuition; Second: 50%; Third: 25%</small>'),
              ('Who can apply','Non-Chinese citizens<small>Undergrad: high-school diploma, under 23; Master\u2019s: bachelor\u2019s, under 30; PhD: master\u2019s, under 35</small>'),
              ('Deadline','Batch system \u2014 final 30 Apr 2027 (PG) / 20 May 2027 (UG)<small>Batch 1 closes 31 Dec 2026; CSC routes close 28 Feb 2027</small>'),
              ('Review','Freshman scholarship \u2014 first year only<small>Annual comprehensive review; the award can be downgraded or terminated</small>'),
              ('Apply via','NPU Online Application System<small>Follow the official 2027 bachelor\u2019s and master/PhD guides</small>')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Northwestern Polytechnical University (NPU)</strong> in Xi\u2019an offers two genuine international scholarship routes for its <strong>2027 admission season</strong> \u2014 officially published for 2027 on <strong>13 October 2026</strong>: the <strong>NPU President Scholarship</strong> and the <strong>Chinese Government Scholarship (University Program, Type B)</strong>. The 2026 cycles are closed. (An aggregator page mashes these together as one scheme \u2014 they are separate routes with separate deadlines, described accurately below.)</p>
      <h2 id="president">NPU President Scholarship 2027 \u2014 four tiers</h2>
      <ul>
        <li><strong>Elite:</strong> tuition waiver + accommodation waiver + living allowance \u2014 <strong>RMB 1,500/month \u00d7 10 months (UG)</strong>, <strong>RMB 2,000 \u00d7 10 (master\u2019s)</strong>, <strong>RMB 2,500 \u00d7 10 (PhD)</strong>.</li>
        <li><strong>First level:</strong> full tuition waiver.</li>
        <li><strong>Second level:</strong> 50% tuition waiver.</li>
        <li><strong>Third level:</strong> 25% tuition waiver.</li>
      </ul>
      <div class="honest-note"><strong>First year only:</strong> the President Scholarship is a freshman award covering the first academic year, with an annual comprehensive review \u2014 it can be <strong>downgraded or terminated</strong>, and there is <strong>no upward adjustment</strong>.</div>
      <h2 id="csc">CSC University Program (Type B) 2027 at NPU</h2>
      <p>The CSC route is open to <strong>master\u2019s and PhD applicants only</strong>, with NPU\u2019s agency number <strong>10699</strong>. Applications must go <strong>through NPU first</strong> \u2014 other channels are not accepted. Two CSC batches run: <strong>1 November \u2013 31 December 2026 (17:00 GMT+8)</strong> and <strong>1 January \u2013 28 February 2027 (17:00 GMT+8)</strong>.</p>
      <div class="honest-note"><strong>Exact CSC stipend figures</strong> (tuition, accommodation, the national 3,000\u20133,500 CNY/month rates, insurance) were <strong>not confirmed on NPU\u2019s official CSC page</strong> in this check \u2014 they are omitted here rather than filled in from aggregators. The 600 RMB application fee seen on some sites is likewise not on the official pages.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Non-Chinese citizen</strong> with a valid passport, in good health (special nationality rules apply for former Chinese citizens).</li>
        <li><strong>Undergraduate:</strong> high-school diploma, <strong>under 23 before 1 September 2027</strong>, with CSCA results (SAT, A-Level or IB accepted as supplementary).</li>
        <li><strong>Master\u2019s:</strong> bachelor\u2019s degree, <strong>under 30</strong>, with an average score of <strong>75% or above</strong>.</li>
        <li><strong>PhD:</strong> master\u2019s degree, <strong>under 35</strong>.</li>
        <li>Chinese or English proficiency meeting NPU\u2019s admission criteria.</li>
        <li>All majors offered to international students are covered.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The <strong>document list is not published on the President Scholarship page itself</strong> \u2014 applicants must pull the checklist from NPU\u2019s official 2027 application guides (bachelor\u2019s guide and master\u2019s/PhD guide, linked in the official sources). <strong>Contacts:</strong> admission-ug@nwpu.edu.cn (undergraduate), admission-pg@nwpu.edu.cn (postgraduate), tel 86-29-88494381.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply through the NPU Online Application System</strong> in your batch \u2014 undergraduate batches: <strong>1 Nov \u2013 31 Dec 2026</strong>, <strong>1 Jan \u2013 28 Feb 2027</strong>, <strong>1 Mar \u2013 15 Apr 2027</strong>, <strong>16 Apr \u2013 20 May 2027</strong> (September intake only); postgraduate batches: <strong>1 Nov \u2013 31 Dec 2026 (17:00)</strong>, <strong>1 Jan \u2013 28 Feb 2027</strong>, <strong>1 Mar \u2013 31 Mar 2027</strong>, <strong>1 Apr \u2013 30 Apr 2027</strong>. Submissions after <strong>30 April 2027 17:00</strong> are automatically void.</li>
        <li><strong>For the CSC route:</strong> apply through NPU first (agency 10699, Type B) within the CSC batch windows above.</li>
        <li><strong>Prepare documents per the official 2027 guides</strong> linked on NPU\u2019s page \u2014 do not rely on a generic aggregator checklist.</li>
        <li><strong>Apply as early as possible:</strong> the President Scholarship is a freshman award and later batches compete for fewer remaining places.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What are the NPU International Scholarships 2027?","Two separate genuine routes at Northwestern Polytechnical University, Xi\u2019an, for the officially announced 2027 admission season: the tiered NPU President Scholarship and the Chinese Government Scholarship (University Program, Type B)."),
 ("How much does the President Scholarship cover?","The Elite tier waives tuition and accommodation and adds a living allowance (RMB 1,500/month \u00d7 10 for undergraduates, 2,000 for master\u2019s, 2,500 for PhD). First level waives full tuition; second level 50%; third level 25%. It covers the first year only, subject to annual review."),
 ("When is the deadline?","Applications run in four batches from 1 November 2026. The final deadlines are 30 April 2027 17:00 (postgraduate) and 20 May 2027 (undergraduate). The two CSC batches close 31 December 2026 and 28 February 2027."),
 ("Who can apply?","Non-Chinese citizens: undergraduates under 23 with a high-school diploma, master\u2019s applicants under 30 (average \u226575%), and PhD applicants under 35 \u2014 meeting NPU\u2019s Chinese/English proficiency requirements."),
 ("How do I apply for the CSC route?","Through NPU first (agency number 10699, Type B) \u2014 other channels are not accepted. Complete the NPU online application within the CSC batch windows."),
]),
 verify='Verified 20 Oct 2026 against official NPU International College pages (studyat.nwpu.edu.cn): the President Scholarship page headed \u201cUpdated and published on 2026.10.13 for 2027 ADMISSION SEASON\u201d (Elite/First/Second/Third tiers with exact RMB figures; freshman-only status; annual review; \u226523/\u226530/\u226535 age limits; \u226575% PG average; CSCA/SAT/A-Level/IB note; four UG and four PG batch windows; 30 Apr 2027 17:00 hard cut-off) and the CSC-University Program page (Type B, master\u2019s/PhD only, agency 10699, apply-through-NPU-first, two 2027 batches). CSC stipend figures and the 600 RMB fee were not confirmed on official NPU pages \u2014 omitted as not published. The document checklist is not published on the scholarship page \u2014 the official 2027 guides are linked instead. The 2026 cycles are closed (re-scoped to the announced 2027 season).',
 offlinks=[('NPU President Scholarship 2027 (official) \u2014 tiers, eligibility, batches','https://studyat.nwpu.edu.cn/info/1011/2120.htm'),
           ('CSC-University Program at NPU (official) \u2014 categories, batches','https://studyat.nwpu.edu.cn/info/1009/10571.htm'),
           ('NPU 2027 bachelor\u2019s application guide (official)','https://studyat.nwpu.edu.cn/info/1184/3541.htm'),
           ('NPU 2027 master\u2019s/PhD application guide (official)','https://studyat.nwpu.edu.cn/info/1313/8831.htm')],
 related_titles=['amgen-2027','adbhku-2027','dut-2027','mipdal-2027'],
),
dict(
 slug='erasmus-mundus-mipdal-scholarship-2027',
 title='Erasmus Mundus MIPDaL Scholarship 2027 (Fully Funded) | StudyDesk Scholarships',
 meta='Erasmus Mundus MIPDaL Scholarship 2027: the Master of Intellectual Property Law and Data Law (1-year dual degree, TU Dresden + 5 partners). Deadline 15 January 2027. Eligibility, funding, documents, and how to apply.',
 short='Erasmus Mundus MIPDaL 2027', kicker='Master\u2019s Scholarship \u00b7 Europe',
 mono='MIP', prov_short='MIPDaL consortium (TU Dresden)', prov_long='Erasmus Mundus MIPDaL consortium, coordinated by TU Dresden, Germany', prov_cat='Erasmus Mundus \u00b7 Europe',
 h1='Erasmus Mundus MIPDaL Scholarship 2027',
 sub='A one-year dual master\u2019s in intellectual property law and data law across six universities in five countries \u2014 the Erasmus Mundus MIPDaL programme awards up to 12 scholarships a year covering tuition and living costs, with the 2027 portal open now and the scholarship deadline on 15 January 2027.',
 dpill='15 Jan 2027 \u00b7 87 days to go', dl_long='15 January 2027 (Erasmus Mundus scholarship; portal opened 1 October 2026; self-funded deadline 15 March 2027; late applications to 15 June 2027)',
 facts=facts([('Award','Erasmus Mundus scholarship \u2014 up to 12/year<small>No tuition fees, no UK top-up fees, plus funding for monthly living expenses (exact monthly amount not published)</small>'),
              ('Who can apply','All nationalities \u2014 law graduates<small>Job-qualifying degree \u2265240 ECTS in law or law-related fields; top-level academic performance</small>'),
              ('Deadline','15 January 2027<small>Scholarship applications; portal opened 1 Oct 2026</small>'),
              ('Programme','1-year dual degree (60 ECTS)<small>Three specialisations: IT & Data Law, Creative Industries, Industrial Property Law</small>'),
              ('Language','English C1 required<small>French C1 for Strasbourg tracks; Spanish B2 for Madrid tracks</small>')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p><strong>MIPDaL</strong> \u2014 the <strong>Master of Intellectual Property Law and Data Law</strong> \u2014 is an Erasmus Mundus Joint Master coordinated by <strong>Technische Universit\u00e4t Dresden (TU Dresden), Germany</strong>, with five partner universities: the <strong>University of Strasbourg/CEIPI (France)</strong>, <strong>Tallinn University of Technology (Estonia)</strong>, <strong>Universidad Carlos III de Madrid (Spain)</strong>, the <strong>University of Exeter (UK)</strong> and <strong>Queen Mary University of London (UK)</strong>. It is a <strong>one-year programme (60 ECTS)</strong> with a <strong>dual-degree structure</strong> \u2014 one degree from each of the two partner universities you study at. The 2026 cycle (scholarship deadline 15 January 2026; late applications to 15 June 2026) is closed; the <strong>2027 intake</strong> portal opened on <strong>1 October 2026</strong>, with the <strong>Erasmus Mundus scholarship deadline on 15 January 2027</strong>.</p>
      <div class="honest-note"><strong>Correction to aggregator claims:</strong> several third-party pages describe MIPDaL as a two-year programme paying \u20ac1,400/month. The official consortium site confirms it is a <strong>one-year</strong> programme, and the official pages publish <strong>no exact monthly stipend figure</strong> \u2014 neither claim is used here.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>All nationalities</strong> are eligible (no published nationality restriction).</li>
        <li>A <strong>job-qualifying degree of at least 240 ECTS</strong> (four years) in <strong>law or law-related fields</strong> (e.g. criminology, jurisprudence), recognised in all partner countries.</li>
        <li>Your <strong>two study countries must differ</strong> from your country of residence at the time of enrolment.</li>
        <li><strong>Top-level academic performance</strong> (equivalent to UK Upper Second Class honours; for the scholarship, in practice First Class results plus C1 English are needed).</li>
        <li><strong>English at C1 (CEFR)</strong>; <strong>French C1</strong> for the Strasbourg tracks; <strong>Spanish B2</strong> for the Madrid tracks. Official language certificates are required: the test must be <strong>under two years old</strong> (IELTS, TOEFL, PTE etc.) or <strong>under five years</strong> (WAEC).</li>
        <li>A <strong>strong motivation statement</strong>; no explicit age limit is published.</li>
      </ul>
      <div class="honest-note"><strong>Highly competitive:</strong> up to 12 Erasmus Mundus scholarships are awarded per year (60 across five years), with geographic balance (a maximum of 10% of scholarships to one country over the funding period) \u2014 the 2026/27 intake drew roughly 541 scholarship applications for about 12 places.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Scholarship holders pay <strong>no tuition fees</strong> and <strong>no UK top-up fees</strong> (the official site quotes top-up fees of \u00a320,050 at QMUL and \u00a312,000 at Exeter \u2014 waived for scholarship holders).</li>
        <li><strong>Funding to cover monthly expenses</strong> for accommodation, travel and living costs (exact monthly amount <strong>not published</strong> on the official pages).</li>
        <li>For context on self-funded costs: published tuition is <strong>\u20ac9,990</strong> for European (EU + UK) students and <strong>\u20ac11,990</strong> for non-European students.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Curriculum vitae</strong> (Europass recommended) and a copy of your <strong>ID card</strong>.</li>
        <li><strong>Degree certificates</strong> for all university studies, plus an <strong>officially certified transcript of records</strong> with an <strong>official English translation</strong>.</li>
        <li><strong>Proof of language proficiency</strong> (certified copy; English, plus French or Spanish where required by your tracks).</li>
        <li><strong>Statement of purpose</strong> (official template recommended, not mandatory).</li>
        <li><strong>Academic reference letter</strong> on institutional letterhead with a signature \u2014 a professional reference is allowed if you have been out of university for three years or more.</li>
        <li>Uploads as <strong>PDF</strong> are preferred.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check eligibility and language requirements</strong> on the official admission pages (mipdal.eu/admission).</li>
        <li><strong>Prepare your documents</strong> (PDF uploads preferred); use the official templates for the Statement of Purpose and the Reference Letter.</li>
        <li><strong>Apply online</strong> via the official application portal: <strong>application.mipdal.eu</strong>.</li>
        <li><strong>For scholarship consideration, the complete application must be submitted by 15 January 2027.</strong> Self-funded or other applicants: deadline 15 March 2027; late applications accepted until 15 June 2027. No application fee is mentioned on the official pages.</li>
      </ol>
      <div class="honest-note"><strong>Re-scoped from the 2026 cycle:</strong> the 2026 scholarship deadline (15 January 2026) has passed. This page covers the announced <strong>2027 intake</strong>, whose portal opened 1 October 2026 with the scholarship deadline of 15 January 2027 \u2014 both confirmed on the official consortium site.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the Erasmus Mundus MIPDaL Scholarship 2027?","The Erasmus Mundus Joint Master in Intellectual Property Law and Data Law \u2014 a one-year (60 ECTS) dual-degree master\u2019s coordinated by TU Dresden with five partner universities in France, Estonia, Spain and the UK. Up to 12 Erasmus Mundus scholarships are awarded each year; the 2027 scholarship deadline is 15 January 2027."),
 ("When is the 2027 deadline?","15 January 2027 for Erasmus Mundus scholarship consideration (portal opened 1 October 2026). Self-funded applicants: 15 March 2027; late applications until 15 June 2027."),
 ("How much is the scholarship worth?","Scholarship holders pay no tuition and no UK top-up fees, and receive funding for monthly living expenses. The exact monthly amount is not published on the official pages. Self-funded tuition is \u20ac9,990 (EU + UK) or \u20ac11,990 (non-European)."),
 ("Who can apply?","All nationalities with a job-qualifying degree of at least 240 ECTS in law or law-related fields, top-level academic performance, and English at C1 level (French C1 for Strasbourg tracks; Spanish B2 for Madrid tracks). The two study countries must differ from your country of residence."),
 ("How do I apply?","Apply online at application.mipdal.eu after checking eligibility on mipdal.eu/admission. Upload PDFs (CV, degree certificates, certified transcripts with English translation, language certificates, statement of purpose, academic reference). Use the official templates for the statement of purpose and reference letter."),
]),
 verify='Verified 20 Oct 2026 against the official MIPDaL consortium site (mipdal.eu \u2014 programme structure, six partners, dual degree, one-year 60 ECTS, specialisations, fee tables, 2027 portal-opened-1-Oct-2026 and 15 Jan 2027 scholarship deadline) plus its admission page (\u2265240 ECTS law degree, country-of-residence rule, language thresholds and certificate ages, official document checklist, application.mipdal.eu portal). Aggregator claims of \u20ac1,400/month and a two-year programme are contradicted by the official site \u2014 not used. Exact monthly stipend amount and any application-fee claim are not published \u2014 omitted. The 2026 cycle (closed 15 Jan 2026) was re-scoped to the announced 2027 intake.',
 offlinks=[('MIPDaL programme (official consortium site)','https://mipdal.eu/'),
           ('MIPDaL admission \u2014 eligibility, documents, deadlines (official)','https://mipdal.eu/admission/'),
           ('MIPDaL application portal (official)','https://application.mipdal.eu/')],
 related_titles=['amgen-2027','adbhku-2027','dut-2027','npu-2027'],
),
]

built = []
for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    built.append((a['slug'], n))
    print('built', a['slug'], n)

# registry appends
reg = pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').read_text()
assert "'amgen-2027'" not in reg, 'registry already has batch 26 cards'
newcards = """\\
 'amgen-2027': {'mono': 'AM', 'title': 'NUS Amgen Scholars Program 2027 in Singapore (Fully Funded)', 'href': 'nus-amgen-scholars-program-2027-singapore.html',
              'dpill': '1 Feb 2027 \\\\u00b7 104 days to go', 'award': 'Full package (2027 figures not published)', 'elig': 'Asia undergrads; 1st year done; not graduating before programme.',
              'tags': [('Internship', 'blue'), ('Singapore', 'teal')]},
 'adbhku-2027': {'mono': 'ADB', 'title': 'HKU ADB Scholarship 2027 in Hong Kong (Fully Funded)', 'href': 'hku-adb-scholarship-2027-hong-kong.html',
              'dpill': '29 Jan 2027 \\\\u00b7 101 days to go', 'award': 'Full tuition + allowances (amounts not published)', 'elig': 'ADB member-country citizens; master\\\\u2019s; \\\\u226435; 2 yrs work experience.',
              'tags': [('Master\\\\u2019s', 'blue'), ('Hong Kong', 'teal')]},
 'dut-2027': {'mono': 'DUT', 'title': 'Dalian University of Technology CSC Scholarship 2027 in China (Fully Funded)', 'href': 'dalian-university-csc-scholarship-2027-china.html',
              'dpill': '15 Feb 2027 \\\\u00b7 118 days to go', 'award': 'Tuition waiver + CNY 3,000\\\\u20133,500/month', 'elig': 'Non-Chinese; master\\\\u2019s <35; doctoral <40.',
              'tags': [('Master\\\\u2019s', 'blue'), ('China', 'teal')]},
 'npu-2027': {'mono': 'NPU', 'title': 'NPU International Scholarships 2027 in China: President Scholarship + CSC', 'href': 'npu-international-scholarships-2027-china.html',
              'dpill': 'Batches \\\\u00b7 final 30 Apr 2027', 'award': 'Tiers: tuition+housing waiver + RMB 1,500\\\\u20132,500/mo \\\\u00d710', 'elig': 'Non-Chinese; UG <23; master\\\\u2019s <30; PhD <35.',
              'tags': [('UG/PG/PhD', 'blue'), ('China', 'teal')]},
 'mipdal-2027': {'mono': 'MIP', 'title': 'Erasmus Mundus MIPDaL Scholarship 2027 (Fully Funded)', 'href': 'erasmus-mundus-mipdal-scholarship-2027.html',
              'dpill': '15 Jan 2027 \\\\u00b7 87 days to go', 'award': 'EMJM scholarship: no tuition + monthly expense funding', 'elig': 'All nationalities; \\\\u2265240 ECTS law degree; English C1.',
              'tags': [('Master\\\\u2019s', 'blue'), ('Europe', 'teal')]},
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
 'nus-amgen-scholars-program-2027-singapore': ('Amgen Foundation', 'Foundation \\\\u00b7 Singapore', 'amgen'),
 'hku-adb-scholarship-2027-hong-kong': ('Asian Development Bank', 'Multilateral \\\\u00b7 Hong Kong', 'adb'),
 'dalian-university-csc-scholarship-2027-china': ('Dalian University of Technology', 'University \\\\u00b7 China', 'dut'),
 'npu-international-scholarships-2027-china': ('Northwestern Polytechnical University', 'University \\\\u00b7 China', 'npu'),
 'erasmus-mundus-mipdal-scholarship-2027': ('MIPDaL consortium (TU Dresden)', 'Erasmus Mundus \\\\u00b7 Europe', 'mipdal'),
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

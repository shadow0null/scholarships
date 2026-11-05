#!/usr/bin/env python3
"""Batch 55 (cron run 55, 27 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Emirates Group Internship 2027 - SKIPPED: deadline passed 28 Sep 2026
   (Emirates Group Elevate Internship, 6 months, start 11 Jan 2027).
   Bright's AED 4,000/month conflicts with the official AED 5,000/month;
   Bright's page is a 7-employer roundup, not one programme.
2. CWAJ Graduate Scholarships 2027 - SKIPPED: deadline passed 5 Oct 2026,
   22:00 JST. Provider is CWAJ itself, not Institute of Science Tokyo.
   Yen 2.0 million one-time grant for non-Japanese women PhD students
   already in Japan.
3. Albukhary University Scholarships 2027 - SKIPPED: deadline passed
   31 Jul 2026. Foundation/Bachelor's only, age 17-20, household
   income <= USD 300/month; "fully funded" overstates it (EMGS/pass
   charges ~RM 3,500 etc. paid by the student).
4. Dongguan University of Technology Scholarships 2027 - VERIFIED:
   deadline NOT yet announced by DGUT (aggregators' 30 Jun 2027
   unconfirmed). Official award: Guangdong provincial scholarship
   RMB 20,000 one-off + DGUT tuition scholarships of 75%/50%/25%.
   Aggregator "freshman package" (RMB 20,000/yr + living RMB 10,000)
   is NOT in the official 2026 guide. Master's is 3 years, not 2.
5. Qatar Government Scholarships 2027 - VERIFIED (composite, Qatari
   nationals only): MoEHE plan. Phase 1 (overseas) closed 15 Aug 2026;
   Phase 2 (domestic) 15 Nov - 30 Dec 2026. Stipends QAR 4,000-10,000/
   month by field. Bright's "All Nationalities" is wrong.
6. SBW Berlin International Scholarships 2027 - VERIFIED: no fixed
   deadline (rolling, year-round). EUR 480/month + furnished shared
   flat + tuition support, up to 48 months, ~20 places. Age 18-30,
   non-profit/social-sector experience required.
7. United Nations Nippon Foundation Fellowship 2027 - SKIPPED:
   deadline passed 13 Sep 2026 (un.org).
8. The Gates Scholarship 2027 - SKIPPED: deadline passed 15 Sep 2026.
   Unresolved ethnicity-eligibility conflict flagged.
9. Milano Bicocca University Scholarship 2027 - SKIPPED: deadline
   passed 22 Jul 2026 (42nd-cycle PhD call, Session II). "130" figure
   not confirmed by the institution.
10. Macquarie University Research Scholarship 2026-27 - VERIFIED:
    main international round closed 31 Jul 2026; open round is the
    International Road to Research Scholarship, closing 31 Oct 2026,
    11pm AEDT, AUD $40,900 for one year, onshore-in-Australia only.
11. Abertay University Scholarships 2026 - VERIFIED (family): Abertay
    International Scholarship up to GBP 3,000/year, max 4 years,
    automatic on admission, no separate deadline. "Fully funded" is
    false; it is a partial tuition discount.
12. Florida State University Scholarships 2027 - VERIFIED (family,
    NOT written this run - spare for next run): operative deadline
    1 Dec 2026; Presidential $42,000 + $73,808 waiver; Vires $16,000;
    Benacquisto ~$91,808.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 27)
def dl_left(ymd):
    y, m, d = map(int, ymd.split('-'))
    return (date(y, m, d) - TODAY).days

def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'dgut-2027': {'mono': 'DG', 'title': 'Dongguan University of Technology Scholarships 2027 in China (Funded)',
   'href': 'dongguan-university-of-technology-scholarships-2027-china.html',
   'dpill': 'Deadline not yet announced',
   'award': 'Guangdong Provincial Government Scholarship of RMB 20,000 (one-off) for postgraduates, plus DGUT tuition scholarships covering 75%, 50% or 25% of the year’s tuition (RMB 20,000 a year). No confirmed deadline for the 2027 cycle yet.',
   'elig': 'Non-Chinese citizens with a bachelor’s degree applying for a 3-year master’s taught in Chinese; HSK Level 4 (score 180+) required for science and engineering majors.',
   'tags': [('Master’s', 'blue'), ('China', 'teal')]},
 'qatar-gov-2027': {'mono': 'QA', 'title': 'Qatar Government Scholarships 2027 (Funded)',
   'href': 'qatar-government-scholarships-2027.html',
   'dpill': 'Phase 2 opens 15 Nov 2026 · %d days to go' % dl_left('2026-11-15'),
   'award': 'Fully funded for Qatari nationals: full tuition plus a monthly stipend of QAR 4,000–10,000 depending on field (medicine QAR 10,000, engineering QAR 8,000, arts QAR 6,000). Phase 1 (overseas) closed 15 August 2026; Phase 2 (domestic) runs 15 November – 30 December 2026.',
   'elig': 'Qatari nationals only (Qatari passport and QID); apply to MoEHE-approved universities and specialisations only.',
   'tags': [('Qatari nationals', 'blue'), ('Qatar', 'teal')]},
 'sbw-berlin-2027': {'mono': 'SB', 'title': 'SBW Berlin International Scholarships 2027 in Germany (Fully Funded)',
   'href': 'sbw-berlin-international-scholarships-2027-germany.html',
   'dpill': 'No fixed deadline · Rolling',
   'award': 'Fully funded: a furnished room in a shared student flat in Berlin, €480 a month living allowance and tuition support, for up to 48 months. Only about 20 places in total.',
   'elig': 'Foreign nationals aged 18–30 from countries in particular need of development support, with non-profit or social-sector experience, a relatively low income and a German grade of 2.0 or better.',
   'tags': [('Bachelor’s/Master’s', 'blue'), ('Germany', 'teal')]},
 'macquarie-2027': {'mono': 'MQ', 'title': 'Macquarie University Research Scholarship 2026-27 in Australia (Funded)',
   'href': 'macquarie-university-research-scholarship-2026-27-australia.html',
   'dpill': 'Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
   'award': 'International Road to Research Scholarship: a tuition-fee offset plus a living stipend of AUD $40,900 for one year (2027 rate) for an MRes starting January 2027. The main international round closed 31 July 2026.',
   'elig': 'International students already onshore in Australia, commencing a full-time MRes in January 2027 with supervisor confirmation; Australian and New Zealand citizens and permanent residents are not eligible.',
   'tags': [('MRes/PhD', 'blue'), ('Australia', 'teal')]},
 'abertay-2026': {'mono': 'AB', 'title': 'Abertay University Scholarships 2026 in UK (Funded)',
   'href': 'abertay-university-scholarships-2026-uk.html',
   'dpill': 'No fixed deadline · Assessed on admission',
   'award': 'Abertay International Scholarship: up to £3,000 a year off tuition, for up to four years; combined with the Principal’s Excellence Scholarship it reaches £7,000 a year. Assessed automatically on your application for study — no separate form.',
   'elig': 'New international (Overseas fee status) students on a full-time on-campus undergraduate or postgraduate taught course; postgraduate taught needs a UK 2:1 equivalent or better.',
   'tags': [('Undergraduate & Taught Master’s', 'blue'), ('United Kingdom', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Dongguan University of Technology
A.append(dict(
 slug='dongguan-university-of-technology-scholarships-2027-china',
 title='Dongguan University of Technology Scholarships 2027 in China (Funded)',
 meta='Dongguan University of Technology Scholarships 2027: the official award is a Guangdong provincial scholarship of RMB 20,000 plus DGUT tuition scholarships of 75%, 50% or 25%. The 2027 deadline has not been announced yet — eligibility, documents, how to apply and FAQs.',
 short='Dongguan University of Technology Scholarships 2027', kicker='China · Master’s · Funded', mono='DG',
 prov_short='Dongguan University of Technology', prov_cat='University · China',
 h1='Dongguan University of Technology Scholarships 2027 in China (Funded)',
 sub='Read this first, because the listings get this one wrong in two places. First, the 2027 deadline has not been announced by Dongguan University of Technology (DGUT) — the 30 June 2027 date on aggregator pages is unconfirmed, so this article does not present it as fact. Second, the “fully funded” package quoted on those same pages — a freshman scholarship of RMB 20,000 a year plus a living allowance and accommodation — does not appear in DGUT’s official 2026 International Student Enrollment Guide. What the official guide actually offers is a Guangdong Provincial Government Scholarship of RMB 20,000 (one-off) for international postgraduates, plus DGUT tuition scholarships covering 75%, 50% or 25% of the year’s tuition. The master’s is three years, taught in Chinese, starting each September — not two years, as the aggregators say.',
 dpill='Deadline not yet announced',
 facts=facts([('Award', 'Officially: (a) the Guangdong Provincial Government Scholarship for international postgraduates — RMB 20,000 one-off, bachelor’s degree required, age 40 or under, application before 1 September each year; (b) the DGUT Scholarship for international students — 75% (First Prize, 10% quota), 50% (Second Prize, 20% quota) or 25% (Third Prize, 30% quota) of the year’s tuition. Tuition is RMB 20,000 per academic year for postgraduate courses; registration fee RMB 450 (non-refundable). NOT officially confirmed: the aggregator “freshman package” of RMB 20,000 a year plus a RMB 10,000 living allowance, RMB 1,500–3,000 accommodation and ~RMB 800 medical insurance.'),
              ('Eligible', 'Non-Chinese citizens holding a valid foreign passport, in good health, with a bachelor’s degree equivalent to a Chinese university degree. For science and engineering majors taught in Chinese, HSK Level 4 with a score of 180 or above (otherwise Chinese-language study first). Provincial scholarship applicants must be 40 or under. Ethnic-Chinese applicants must meet the 4-year naturalisation / 2-year residence rule.'),
              ('How', 'Email the completed application form and supporting documents to gjc@dgut.edu.cn, or apply through the official WeChat student consultation account “studyatDGUT”. Then document verification and interview, admission letter and visa documents (JW202), then a student visa application.'),
              ('Deadline', 'Not yet announced by DGUT for the 2027 cycle. Aggregators list 30 June 2027, but ScholarshipsAds itself states the 2027 deadline has not been announced and no 2027 DGUT admission notice was found — so do not plan around 30 June 2027. The official guide’s current-cycle master’s application deadline is before 25 December 2026; that is the 2026 guide’s date, not the 2027 deadline.'),
              ('Fine print', 'The master’s is 3 years, full-time, starting each September, taught in Chinese — aggregators saying 2 years are wrong. Do not confuse DGUT with GDUT (Guangdong University of Technology) — a different university whose admissions pages polluted several searches. Airfare, daily meals, visa fees, residence permit fees and personal expenses are not covered.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Dongguan University of Technology (DGUT)</strong> is a public university in Dongguan, Guangdong Province, China, and its scholarships for international master’s students come in two official parts. The first is the <strong>Guangdong Provincial Government Scholarship</strong> for international postgraduates: <strong>RMB 20,000, one-off</strong>, for students with a bachelor’s degree who are 40 or under. The second is the <strong>DGUT Scholarship</strong> for international students, which pays <strong>75%, 50% or 25% of the year’s tuition</strong> — First, Second and Third Prize, with quotas of 10%, 20% and 30% of recipients. Tuition itself is <strong>RMB 20,000 per academic year</strong> for postgraduate courses, and the registration fee is <strong>RMB 450</strong> (non-refundable).</p>
      <p>That is the official picture, from DGUT’s own 2026 International Student Enrollment Guide. It is deliberately narrower than the “fully funded” package quoted on aggregator sites — a freshman scholarship of RMB 20,000 a year, a living allowance of RMB 10,000 a year, accommodation of RMB 1,500–3,000 a year and medical insurance of about RMB 800 a year — which does not appear in the official guide at all. It may reflect a newer cycle, but it is not officially confirmed, so this article does not present it as the award. The master’s programmes are <strong>three years, full-time, starting each September, taught in Chinese</strong>, and cover engineering and related fields: Software Engineering, Communication Engineering, Control Engineering, Optoelectronic Information Engineering, Electrical Engineering, Civil and Hydraulic Engineering, Environmental Engineering, Energy and Power Engineering, Mechanical Engineering, Materials and Chemical Engineering, New-Generation Electronic Information Technology, Integrated Circuit Engineering, Biology and Medicine, Food and Nutrition, International Business, Digital Economy and Social Work.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>non-Chinese citizen</strong> holding a <strong>valid foreign passport</strong>, in <strong>good health</strong>.</li>
        <li>Hold a <strong>bachelor’s degree equivalent to a Chinese university degree</strong> (fresh graduates may submit a pre-graduation certificate).</li>
        <li>For science and engineering majors taught in Chinese: <strong>HSK Level 4 with a score of 180 or above</strong> — otherwise Chinese-language study first.</li>
        <li>For the Guangdong Provincial Government Scholarship: be <strong>40 or under</strong> and apply <strong>before 1 September</strong> each year.</li>
        <li><strong>Ethnic-Chinese applicants</strong> must meet the <strong>4-year naturalisation / 2-year residence rule</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Guangdong Provincial Government Scholarship:</strong> <strong>RMB 20,000, one-off</strong>, for international postgraduates.</li>
        <li><strong>DGUT Scholarship:</strong> <strong>75% / 50% / 25% of the year’s tuition</strong> (First / Second / Third Prize).</li>
        <li><strong>Tuition:</strong> RMB 20,000 per academic year for postgraduate courses; registration fee RMB 450 (non-refundable).</li>
        <li><strong>Not covered:</strong> airfare, daily meals, visa fees, residence permit fees and personal expenses.</li>
        <li><strong>Not officially confirmed:</strong> the aggregator “freshman package” (RMB 20,000 a year + RMB 10,000 living allowance + accommodation + medical insurance) — do not budget around it.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>valid passport</strong> (plus the current visa/residence permit page if already in mainland China).</li>
        <li>A <strong>bachelor’s degree certificate</strong> (a pre-graduation certificate is acceptable for fresh graduates).</li>
        <li>A <strong>complete undergraduate transcript</strong>.</li>
        <li>A <strong>language proficiency certificate</strong> (HSK for Chinese-taught majors).</li>
        <li><strong>Reference letters signed by two professors or associate professors</strong>.</li>
        <li>A <strong>study and research plan in China</strong>.</li>
        <li><strong>Proof of financial status</strong>.</li>
        <li>A <strong>health examination report</strong>.</li>
        <li>A <strong>letter of commitment</strong> and other supporting materials as required.</li>
        <li>Documents must be in <strong>Chinese or English</strong> (notarised translations otherwise).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Prepare the <strong>application form and supporting documents</strong> listed above.</li>
        <li><strong>Email them to gjc@dgut.edu.cn</strong>, or apply through the official WeChat student consultation account <strong>“studyatDGUT”</strong>.</li>
        <li>Go through <strong>document verification and interview</strong>.</li>
        <li>Receive the <strong>admission letter and visa documents (JW202)</strong>.</li>
        <li>Apply for a <strong>student visa</strong>.</li>
        <li>Note the <strong>application fee of about RMB 450</strong> after pre-admission (per Bright; the official guide’s registration fee is RMB 450).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for DGUT Scholarships 2027?',
  'It has not been announced by DGUT for the 2027 cycle. Aggregators list 30 June 2027, but ScholarshipsAds itself states the 2027 deadline has not been announced and no 2027 DGUT admission notice was found. Do not plan around 30 June 2027; watch the official DGUT channels.'),
 ('Is the DGUT scholarship fully funded?',
  'Not on the official evidence. The official award is a Guangdong provincial scholarship of RMB 20,000 (one-off) plus a DGUT tuition scholarship of 75%, 50% or 25%. The “fully funded” freshman package quoted by aggregators (RMB 20,000 a year plus a living allowance and accommodation) is not in the official 2026 guide.'),
 ('How long is the master’s at DGUT?',
  'Three years, full-time, starting each September and taught in Chinese — aggregators saying two years are wrong.'),
 ('What Chinese level do I need?',
  'For science and engineering majors taught in Chinese, HSK Level 4 with a score of 180 or above; otherwise you study Chinese first.'),
 ('How do I apply to DGUT?',
  'Email the completed application form and supporting documents to gjc@dgut.edu.cn, or apply through the official WeChat account “studyatDGUT”. Then comes document verification and an interview, then the admission letter and JW202 visa documents.'),
 ('Is DGUT the same as GDUT?',
  'No. DGUT is Dongguan University of Technology; GDUT is Guangdong University of Technology — a different university. Several searches mix the two up, so check the domain (dgut.edu.cn) before you apply.')]) + '''
      <p class="verify">Verified 27 Oct 2026: DGUT official 2026 International Student Enrollment Guide, reproduced in full at wentchina.com/dongguan-university-of-technology-international (images hosted on gjc.dgut.edu.cn) — Guangdong Provincial Government Scholarship RMB 20,000 one-off (bachelor’s required, age 40 or under, apply before 1 September), DGUT Scholarship 75%/50%/25% of the year’s tuition (quotas 10%/20%/30%), tuition RMB 20,000 per academic year, registration fee RMB 450, master’s 3 years full-time starting September taught in Chinese, HSK Level 4 score 180+, documents (passport, degree certificate, transcript, language certificate, two reference letters, study/research plan, financial proof, health examination, letter of commitment), application by email to gjc@dgut.edu.cn or WeChat "studyatDGUT", current-cycle master’s deadline before 25 December 2026; Bright Scholarship, Ehsas Kafaalat, ScholarshipsAds, ScholarshipBob — corroboration, including the 30 June 2027 aggregator date and the programme list. CONFLICTS: (1) the 2027 deadline is NOT yet announced — Bright/Ehsas Kafaalat list 30 June 2027, but ScholarshipsAds explicitly states it has not been announced; the article states "not yet announced". (2) the aggregator "freshman package" (RMB 20,000/year + RMB 10,000 living allowance + accommodation + insurance) does NOT appear in the official guide and is not presented as the award; Bright also double-counts the RMB 20,000 as both a freshman scholarship and the tuition fee. (3) aggregators say the master’s is 2 years; the official guide says 3 years. The DGUT official site itself (dgut.edu.cn) could not be opened directly in this check — no DGUT URL is cited that was not verified here. Do not confuse DGUT with GDUT.</p>''',
 dl_long='Not yet announced by DGUT for the 2027 cycle (aggregators suggest 30 June 2027 — unconfirmed)',
 offlinks=[('Dongguan University of Technology — 2026 International Student Enrollment Guide (official, via WentChina)', 'https://wentchina.com/dongguan-university-of-technology-international'),
           ('Bright Scholarship — Dongguan University of Technology Scholarships 2027', 'https://brightscholarship.com/dongguan-university-of-technology-scholarships/')],
 related_titles=['gxnu-csc-2027', 'xiamen-csc-2027', 'hust-csc-2027', 'nju-csc-2027'])),

# ---------------------------------------------------------------- 2. Qatar Government Scholarships
A.append(dict(
 slug='qatar-government-scholarships-2027',
 title='Qatar Government Scholarships 2027 (Funded)',
 meta='Qatar Government Scholarships 2027: the Ministry of Education’s Government Scholarship Plan for Qatari nationals — full tuition plus QAR 4,000–10,000 a month. Phase 1 (overseas) closed 15 August 2026; Phase 2 (domestic) opens 15 November 2026 — eligibility, documents, how to apply and FAQs.',
 short='Qatar Government Scholarships 2027', kicker='Qatar · Bachelor’s/Master’s/PhD · Funded', mono='QA',
 prov_short='Ministry of Education and Higher Education, Qatar', prov_cat='Government · Qatar',
 h1='Qatar Government Scholarships 2027 (Funded)',
 sub='Read this first, because the listings get this one wrong in two ways. First, this is not one scholarship with one deadline: it is the Qatar Ministry of Education and Higher Education’s Government Scholarship Plan 2026–2027, made of several tracks — the Amiri Scholarship, Overseas (Abroad) Scholarships, Education City scholarships and Domestic/Local scholarships (including the Tomouh programme) — and each track has its own rules and dates. Second, it is for Qatari nationals only. Bright Scholarship’s claim of “All Nationalities” is contradicted by the official-plan reporting and must not be believed: international students should not apply until the portal confirms their nationality is accepted. The overseas phase closed on 15 August 2026, but the domestic phase opens on 15 November 2026 — so if you are a Qatari student, this is still live.',
 dpill='Phase 2 opens 15 Nov 2026 · %d days to go' % dl_left('2026-11-15'),
 facts=facts([('Award', 'Fully funded for Qatari nationals: full tuition plus a monthly stipend that depends on the field of study — medicine, education and paramedic studies QAR 10,000 a month; engineering, computer science and health sciences QAR 8,000 a month; applied sciences and arts QAR 6,000 a month; professional diploma QAR 4,000 a month (MoEHE, via The Peninsula / MENAFN). Aggregators cite a range of QAR 4,000–12,000 a month including overseas tracks — the “up to QAR 12,000” figure is aggregator-only and not in the domestic reporting. “Business class flights” (one aggregator) is unconfirmed — do not rely on it.'),
              ('Eligible', 'Qatari nationals only — a Qatari passport and QID are required (confirmed by The Peninsula/Zawya reporting of the MoEHE plan). Apply only to MoEHE-approved universities and specialisations (about 98 approved specialisations, about 60 accredited universities, 79 countries). Aggregator-only and unverified: age limits typically 25 or under for a bachelor’s abroad, 45 for a master’s, 40 for a PhD; a service bond to work in the public sector for a period equal to the study duration.'),
              ('How', 'Apply online on the official Government Scholarship Platform at scholarship.edu.gov.qa — create an account with your Qatari national ID, select your track (Amiri / Abroad / Local–Tomouh), complete your profile, upload your documents and rank your university choices.'),
              ('Deadline', 'Two phases. Phase 1 (external/overseas, Education City, private universities): 1 July – 15 August 2026 — CLOSED. Phase 2 (domestic — Qatar University and other public universities): 15 November – 30 December 2026 — not yet open as of 27 October 2026. The queue’s “August 2026” deadline is only Phase 1.'),
              ('Fine print', 'This is a composite plan, not a single scheme — eligibility, amounts and deadlines differ by track. Bright’s “All Nationalities” and its single “deadline 15 August 2026” are both wrong/incomplete. The document list below is the aggregator set — the official portal requires a Qatari national ID to create an account, and requirements differ by track, so do not treat the list as official. Age limits, the IELTS 6.0 rule and the service bond are aggregator-only.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>Qatar Government Scholarships</strong> are the <strong>Ministry of Education and Higher Education (MoEHE)</strong> Government Scholarship Plan for <strong>2026–2027</strong>, announced in April 2026. It is a single national plan with several tracks: the <strong>Amiri Scholarship</strong>, <strong>Overseas (Abroad) Scholarships</strong>, <strong>Education City scholarships</strong> and <strong>Domestic/Local scholarships</strong> (including the <strong>Tomouh programme</strong>). The plan covers about <strong>98 approved specialisations</strong> at about <strong>60 accredited universities</strong> across <strong>79 countries</strong>, and it is <strong>fully funded</strong>: full tuition plus a monthly stipend that depends on your field — <strong>QAR 10,000 a month</strong> for medicine, education and paramedic studies, <strong>QAR 8,000</strong> for engineering, computer science and health sciences, <strong>QAR 6,000</strong> for applied sciences and arts, and <strong>QAR 4,000</strong> for a professional diploma.</p>
      <p>The one hard rule is nationality: this plan is for <strong>Qatari nationals only</strong>. The Peninsula and Zawya reporting of the MoEHE press conference describe it as support for Qatari students, and Fully-FundedScholarships.com explicitly warns international students not to apply until the portal confirms their nationality is accepted. If you are not Qatari, this is not your route — look instead at Qatar University, HBKU or Qatar Foundation awards, which run their own international schemes. The plan runs in <strong>two phases</strong>: Phase 1 (overseas) ran 1 July – 15 August 2026 and is closed; Phase 2 (domestic — Qatar University and other public universities) runs <strong>15 November – 30 December 2026</strong> and has not opened yet.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>Qatari national</strong> — a <strong>Qatari passport and QID</strong> are required.</li>
        <li>Apply only to <strong>MoEHE-approved universities and specialisations</strong> (about 98 specialisations, 60 accredited universities, 79 countries).</li>
        <li>Hold a <strong>high-school diploma or a higher degree</strong>, depending on the track (aggregator-reported).</li>
        <li><strong>Age limits are aggregator-only and unverified:</strong> typically 25 or under for a bachelor’s abroad, 45 for a master’s, 40 for a PhD.</li>
        <li><strong>A service bond is aggregator-only and unverified:</strong> recipients are reported to sign a bond to work in the public sector for a period equal to their study duration.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition</strong> at an MoEHE-approved university.</li>
        <li><strong>Monthly stipend by field:</strong> medicine, education and paramedic studies <strong>QAR 10,000</strong>; engineering, computer science and health sciences <strong>QAR 8,000</strong>; applied sciences and arts <strong>QAR 6,000</strong>; professional diploma <strong>QAR 4,000</strong>.</li>
        <li><strong>Travel</strong> is reported as covered for overseas tracks (aggregator-only).</li>
        <li><strong>Not confirmed:</strong> the “up to QAR 12,000 a month” figure (aggregator-only) and “business class flights” (one aggregator only).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>Qatari national ID</strong> to create your account on the official portal.</li>
        <li>The <strong>completed application form</strong> on the portal.</li>
        <li>A <strong>degree certificate</strong> and <strong>academic transcript</strong>.</li>
        <li>A <strong>valid passport</strong>.</li>
        <li>An updated <strong>CV / résumé</strong>.</li>
        <li><strong>Other supporting documents</strong> as the track requires.</li>
        <li>Note that this list is the <strong>aggregator set, not officially confirmed</strong> — requirements differ by track, so check the portal for your track.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the official Government Scholarship Platform, <strong>scholarship.edu.gov.qa</strong>.</li>
        <li><strong>Create an account</strong> with your Qatari national ID.</li>
        <li>Select your track — <strong>Amiri, Abroad, or Local–Tomouh</strong>.</li>
        <li><strong>Complete your profile</strong> and upload your documents.</li>
        <li><strong>Rank your university choices</strong> from the MoEHE-approved list and submit.</li>
        <li>For Phase 2 (domestic), apply between <strong>15 November and 30 December 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can international students apply for Qatar Government Scholarships 2027?',
  'No — not on the evidence available. The plan is for Qatari nationals only (Qatari passport and QID). Bright Scholarship’s “All Nationalities” claim is contradicted by the official-plan reporting. International students should look at Qatar University, HBKU or Qatar Foundation awards instead.'),
 ('What is the deadline for Qatar Government Scholarships 2027?',
  'There are two phases. Phase 1 (overseas, Education City, private universities) ran 1 July – 15 August 2026 and is closed. Phase 2 (domestic — Qatar University and other public universities) runs 15 November – 30 December 2026 and has not opened yet.'),
 ('How much is the Qatar Government Scholarship stipend?',
  'QAR 10,000 a month for medicine, education and paramedic studies; QAR 8,000 for engineering, computer science and health sciences; QAR 6,000 for applied sciences and arts; QAR 4,000 for a professional diploma. The “up to QAR 12,000” figure on aggregators is not in the domestic reporting.'),
 ('What is the Tomouh programme?',
  'Tomouh is the domestic/local track of the MoEHE Government Scholarship Plan, covering study at Qatar University and other public universities in Qatar. It opens in Phase 2, 15 November – 30 December 2026.'),
 ('Where do I apply?',
  'On the official Government Scholarship Platform at scholarship.edu.gov.qa. You need a Qatari national ID to create an account. The portal page itself is JavaScript-only and could not be read by text fetch, so track details should be confirmed on the portal.'),
 ('Is there a service bond?',
  'Aggregators report that recipients must sign a service bond to work in the public sector for a period equal to their study duration, but this is not confirmed in the official-plan reporting — treat it as unverified.')]) + '''
      <p class="verify">Verified 27 Oct 2026: The Peninsula, "Education Ministry launches expanded 2026-27 scholarship plan", thepeninsulaqatar.com/article/22/04/2026/education-ministry-launches-expanded-2026-27-scholarship-plan — MoEHE Government Scholarship Plan 2026-27, Qatari nationals, two phases (Phase 1: 1 July - 15 August 2026 external/overseas, Education City, private universities; Phase 2: 15 November - 30 December 2026 domestic, Qatar University and other public universities), about 98 approved specialisations, 60 accredited universities, 79 countries; Zawya, zawya.com/en/world/middle-east/qatars-ministry-launches-expanded-2026-27-scholarship-plan-347867 — same plan and phases; MENAFN/The Peninsula domestic stipend report, menafn.com/1111291264/Qatar-Expands-Scholarships-For-Priority-Fields — QAR 10,000/month medicine/education/paramedic, QAR 8,000 engineering/computer science/health sciences, QAR 6,000 applied sciences/arts, QAR 4,000 professional diploma; Bright Scholarship, brightscholarship.com/qatar-government-scholarships-2027-funded/ — corroboration only; official portal: scholarship.edu.gov.qa (JavaScript-only page, could not be read by text fetch). CORRECTIONS: Bright's "All Nationalities" is wrong — Qatari nationals only. Bright's single "deadline 15 August 2026" is incomplete — Phase 2 runs 15 November - 30 December 2026. NOT CONFIRMED officially: the QAR 12,000 figure, age limits (25/45/40), IELTS 6.0, the service bond, "business class flights", and the document list (aggregator set only).</p>''',
 dl_long='Phase 2 (domestic): 15 November – 30 December 2026 — Phase 1 (overseas) closed 15 August 2026',
 offlinks=[('Ministry of Education and Higher Education, Qatar — Government Scholarship Platform (official)', 'https://scholarship.edu.gov.qa'),
           ('The Peninsula — Education Ministry launches expanded 2026-27 scholarship plan', 'http://thepeninsulaqatar.com/article/22/04/2026/education-ministry-launches-expanded-2026-27-scholarship-plan'),
           ('Bright Scholarship — Qatar Government Scholarships 2027', 'https://brightscholarship.com/qatar-government-scholarships-2027-funded/')],
 related_titles=['doha-2027', 'griffith-vc', 'deakin-vc-2027', 'lincoln-nz-2027'])),

# ---------------------------------------------------------------- 3. SBW Berlin
A.append(dict(
 slug='sbw-berlin-international-scholarships-2027-germany',
 title='SBW Berlin International Scholarships 2027 in Germany (Fully Funded)',
 meta='SBW Berlin International Scholarships 2027: fully funded for students from countries in particular need of development support — a furnished flat in Berlin, €480 a month and tuition support for up to 48 months. No fixed deadline, applications year-round — eligibility, documents, how to apply and FAQs.',
 short='SBW Berlin International Scholarships 2027', kicker='Germany · Bachelor’s/Master’s · Fully Funded', mono='SB',
 prov_short='SBW Berlin', prov_cat='Foundation · Germany',
 h1='SBW Berlin International Scholarships 2027 in Germany (Fully Funded)',
 sub='This is one of the rare genuinely fully funded scholarships with no deadline at all: SBW Berlin accepts applications year-round, because it awards its roughly 20 places as vacancies arise. What it pays is concrete — a furnished room in a shared student flat in Berlin, €480 a month in living allowance and tuition support, for up to 48 months. What it asks for in return is also concrete, and it catches applicants off guard: you must be 18 to 30, from a country in particular need of development support, with real professional or volunteer experience in the non-profit or social sector — and you must run a social project in your home country (2 to 8 hours a week) for the whole time you are funded. If you stop studying, stop the project, or stay in Germany afterwards, a repayment plan starts three months later. And one warning: some aggregators invent a “31 December 2026” deadline. There is no fixed deadline — do not plan around one.',
 dpill='No fixed deadline · Rolling',
 facts=facts([('Award', 'Fully funded: a furnished room in a shared student apartment in Berlin, a living allowance of €480 a month, and tuition support (subject to the scholarship rules), plus in some cases a travel contribution to and from Germany. Up to 48 months (the regular programme duration), reviewed periodically. The €480 figure is corroborated by LeapScholar, DAADScholarship.com, GreatYop, Careerical and ScholarHunter; the official page itself does not state the amount (it refers readers to the guidelines). Health insurance is NOT included — you arrange and pay mandatory public health insurance yourself (about €120–140 a month, per aggregators).'),
              ('Eligible', 'Foreign nationals from countries in particular need of development support (see the guidelines); age 18–30; professional or volunteer experience in the non-profit or social sector, supported by letters of recommendation from the social institution; not resided in Germany for more than 18 months before applying; university entrance qualification; average grade equivalent to a German 2.0 or better; proven relatively low net income; no first-degree family members permanently residing in Germany; apply before starting studies or while enrolled in the 1st, 2nd or at most 3rd semester at a state-recognised university, or for a master’s shortly before or after a bachelor’s; intention to work at least 18 months in the home country after graduation or engage in charitable activities in Germany until the repayment plan is fulfilled. A separate university application to a Berlin or Potsdam university is required. Only about 20 scholarship places in total.'),
              ('How', 'Apply through SBW Berlin’s official site — start at sbw.berlin/en/sbw-berlin-scholarship/ and follow the linked guidelines and application process on that page. The recommendation letter from the non-profit comes first (two-step process, per aggregators). No application fee. No fixed deadline — apply any time, but apply early: university admission, uni-assist, language testing and the visa take months.'),
              ('Deadline', 'No fixed deadline — applications are accepted year-round / rolling. The official SBW Berlin page states no deadline anywhere, and multiple independent aggregators confirm it. The “31 December 2026” / “15 November to 31 December” dates on some aggregator sites are not official — one source calls 31 December 2026 only a practical planning target, not a fixed closing date. The “2027” label is an aggregator construct; the scholarship is evergreen (guidelines last updated 9 April 2025, still current July 2026).'),
              ('Fine print', 'Recipients must run a social project (2–8 hours a week) with a non-profit in their home country during their studies, attend SBW Berlin project meetings and workshops, write project reports and give presentations. If studies or the project are discontinued, or the recipient stays in Germany, a repayment plan starts 3 months after the end of studies or funding, in 12 monthly instalments. One aggregator’s claim of “medical and health insurance coverage” conflicts with other aggregators saying health insurance is NOT included — do not claim insurance is covered. Some sites say “open to all countries”; the official criteria restrict it to nationals of countries in particular need of development support.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>SBW Berlin Scholarship</strong> is run by <strong>SBW Berlin gemeinnützige GmbH</strong>, a non-profit that supports talented young people from countries in particular need of development support to study in Berlin — and then to take what they learned back home. It is <strong>fully funded</strong>: a <strong>furnished room in a shared student flat in Berlin</strong>, a living allowance of <strong>€480 a month</strong> and <strong>tuition support</strong>, for up to <strong>48 months</strong> (the regular programme duration), plus in some cases a <strong>travel contribution</strong> to and from Germany. There are only about <strong>20 places</strong> in total, awarded as vacancies arise — which is why there is no fixed deadline and applications are accepted <strong>year-round</strong>.</p>
      <p>What makes SBW Berlin different from an ordinary scholarship is the deal attached to it. You are not just funded; you are expected to <strong>run a social project in your home country</strong> — 2 to 8 hours a week with a non-profit — for the whole time you are funded, to attend <strong>SBW Berlin project meetings and workshops</strong>, and to report and present on your project. After graduation you are expected to <strong>work at least 18 months in your home country</strong> or engage in charitable activities in Germany until the repayment plan is fulfilled. And if you discontinue your studies or your project, or you stay in Germany, a <strong>repayment plan starts three months later</strong>, in 12 monthly instalments. Apply only if that deal suits you — and apply early, because university admission, uni-assist, language testing and the visa take months even without a deadline to chase.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a <strong>foreign national from a country in particular need of development support</strong> (see the SBW Berlin guidelines).</li>
        <li>Be aged <strong>18–30</strong>.</li>
        <li>Have <strong>professional or volunteer experience in the non-profit or social sector</strong>, supported by <strong>letters of recommendation from the social institution</strong>.</li>
        <li><strong>Not have resided in Germany for more than 18 months</strong> before applying.</li>
        <li>Hold a <strong>university entrance qualification</strong>, with an <strong>average grade equivalent to a German 2.0 or better</strong>.</li>
        <li>Have a <strong>proven relatively low net income</strong>.</li>
        <li>Have <strong>no first-degree family members permanently residing in Germany</strong>.</li>
        <li>Apply <strong>before starting studies</strong> or while enrolled in the <strong>1st, 2nd or at most 3rd semester</strong> at a state-recognised university — or for a master’s <strong>shortly before or after a bachelor’s</strong>.</li>
        <li>Intend to <strong>work at least 18 months in your home country after graduation</strong>, or engage in charitable activities in Germany until the repayment plan is fulfilled.</li>
        <li>Apply separately to a <strong>Berlin or Potsdam university</strong> — the scholarship does not include admission.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>furnished room in a shared student apartment in Berlin</strong>.</li>
        <li>A <strong>living allowance of €480 a month</strong>.</li>
        <li><strong>Tuition support</strong> (subject to the scholarship rules).</li>
        <li>In some cases, a <strong>travel contribution</strong> to and from Germany.</li>
        <li>Funding for up to <strong>48 months</strong>, reviewed periodically.</li>
        <li><strong>Not included:</strong> health insurance — you arrange and pay mandatory public health insurance yourself (about €120–140 a month, per aggregators).</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>valid passport</strong>.</li>
        <li>A <strong>German student visa</strong>.</li>
        <li><strong>Proof of admission</strong> to a Berlin or Potsdam university.</li>
        <li><strong>Academic certificates and transcripts</strong>.</li>
        <li>A <strong>CV</strong>.</li>
        <li>A <strong>language proficiency certificate</strong>.</li>
        <li>A <strong>letter of recommendation from a previous tutor or academic supervisor</strong>.</li>
        <li>A <strong>description of a social or development project</strong>.</li>
        <li><strong>Proof of financial need</strong> (bank statement).</li>
        <li><strong>Evidence of previous work or professional experience</strong>.</li>
        <li>Note that this list is <strong>aggregator-sourced, not officially confirmed</strong> — the official page does not list the documents in full, so check the guidelines on the SBW Berlin site.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Go to the official page, <strong>sbw.berlin/en/sbw-berlin-scholarship/</strong>, and read the <strong>guidelines</strong> linked there.</li>
        <li>Secure the <strong>recommendation letter from your non-profit or social institution first</strong> — the application is two-step (per aggregators).</li>
        <li>Apply separately for <strong>admission to a Berlin or Potsdam university</strong>.</li>
        <li>Submit the <strong>SBW Berlin application</strong> with your documents — there is <strong>no application fee</strong> and <strong>no fixed deadline</strong>.</li>
        <li>Apply early: <strong>admission, uni-assist, language testing and the visa take months</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the SBW Berlin Scholarship 2027?',
  'There is no fixed deadline. Applications are accepted year-round and places are awarded as vacancies arise. The “31 December 2026” dates on some aggregator sites are not official — do not plan around them.'),
 ('How much does the SBW Berlin Scholarship pay?',
  'A furnished room in a shared student flat in Berlin, €480 a month in living allowance and tuition support, for up to 48 months, plus in some cases a travel contribution. Health insurance is not included.'),
 ('Who can apply for the SBW Berlin Scholarship?',
  'Foreign nationals aged 18–30 from countries in particular need of development support, with non-profit or social-sector experience, a relatively low income and a German grade of 2.0 or better — who have not lived in Germany for more than 18 months and who apply before or early in their studies at a Berlin or Potsdam university.'),
 ('What is the social project requirement?',
  'Recipients must run a social project (2–8 hours a week) with a non-profit in their home country during their studies, attend SBW Berlin project meetings and workshops, write project reports and give presentations.'),
 ('Do I have to pay the money back?',
  'Only if you discontinue your studies or your project, or you stay in Germany after graduation. Then a repayment plan starts three months after the end of studies or funding, in 12 monthly instalments.'),
 ('Is health insurance covered?',
  'No — on the aggregator evidence, health insurance is not included. You arrange and pay mandatory public health insurance yourself (about €120–140 a month). One aggregator claims otherwise, but that claim conflicts with the others and is not used here.')]) + '''
      <p class="verify">Verified 27 Oct 2026: sbw.berlin/en/sbw-berlin-scholarship/ (official SBW Berlin page, opened and read) — eligibility (foreign nationals from countries in particular need of development support; age 18-30; non-profit/social-sector experience with letters of recommendation; not resided in Germany more than 18 months; university entrance qualification; grade equivalent to German 2.0 or better; relatively low net income; no first-degree family members permanently residing in Germany; apply before starting studies or in the 1st, 2nd or max 3rd semester, or for a master's shortly before/after a bachelor's; intention to work at least 18 months in the home country after graduation or engage in charitable activities in Germany); no deadline stated anywhere on the official page; LeapScholar, leapscholar.com/blog/sbw-berlin-scholarship-in-germany/ — €480/month, furnished shared flat, tuition support, up to 48 months, ~20 places, social project 2-8 hours/week, repayment plan 3 months after end of studies in 12 instalments, guidelines last updated 9 April 2025 still current July 2026; DAADScholarship.com, GreatYop, ScholarHunter, Careerical — corroboration of the €480 figure, rolling applications and eligibility; Talk2SamAfrica — aggregator document list. CONFLICTS: "31 December 2026" / "15 November to 31 December" deadlines on KAIST Scholarship and AlexandraGrants are not official — Fully-FundedScholarships.com says 31 December 2026 is only a practical planning target, not a fixed closing date. Some sites say "open to all countries"; the official criteria restrict it to countries in particular need of development support. Talk2SamAfrica's "medical and health insurance coverage" conflicts with other aggregators saying health insurance is NOT included — not claimed here. The €480 figure is widely reported but not stated on the official page read (it refers readers to the guidelines).</p>''',
 dl_long='No fixed deadline — applications accepted year-round',
 offlinks=[('SBW Berlin — Scholarship (official)', 'https://sbw.berlin/en/sbw-berlin-scholarship/'),
           ('Bright Scholarship — SBW Berlin International Scholarships 2027', 'https://brightscholarship.com/sbw-berlin-international-scholarships-2027/')],
 related_titles=['stuttgart-2027', 'hanns-seidel', 'daad', 'ceepus-2027'])),

# ---------------------------------------------------------------- 4. Macquarie University Research Scholarship
A.append(dict(
 slug='macquarie-university-research-scholarship-2026-27-australia',
 title='Macquarie University Research Scholarship 2026-27 in Australia (Funded)',
 meta='Macquarie University Research Scholarship 2026-27: the main international round closed 31 July 2026, but the International Road to Research Scholarship closes 31 October 2026 — AUD $40,900 for one year for an MRes starting January 2027, onshore in Australia only. Eligibility, how to apply and FAQs.',
 short='Macquarie University Research Scholarship 2026-27', kicker='Australia · MRes/PhD · Funded', mono='MQ',
 prov_short='Macquarie University', prov_cat='University · Australia',
 h1='Macquarie University Research Scholarship 2026-27 in Australia (Funded)',
 sub='Read this first, because the headline is misleading. The main International Research Scholarship Round (iRTP / iMQRES, for MRes and PhD) closed on 31 July 2026 — it is gone. What is still open, and what this article is actually about, is the International Road to Research Scholarship (iR2R), which closes on 31 October 2026 at 11pm AEDT: a tuition-fee offset plus a living stipend of AUD $40,900 for one year, for an MRes commencing January 2027. And it has a hard limit the aggregators bury: you must already be onshore in Australia when you apply, and you must intend to live in Sydney. Offshore applicants cannot use this round — do not apply from abroad and expect it to work.',
 dpill='Deadline 31 Oct 2026 · %d days left' % dl_left('2026-10-31'),
 facts=facts([('Award', 'International Road to Research Scholarship (iR2R): a tuition-fee offset for a maximum of one year plus a living allowance stipend of AUD $40,900 for one year (2027 rate), for an MRes commencing January 2027 (Session 1 2027). The three-year MRes-to-PhD progression scholarship is also $40,900 a year in 2027 (official graduate research scholarships page). A Graduate Diploma of Research scholarship is $5,000 per session. NOT used: several aggregators quote $39,700 a year from 1 January 2027 — that conflicts with the official $40,900 on both mq.edu.au pages read. “Fully funded” overstates it: the open round covers one year only, not a full multi-year package.'),
              ('Eligible', 'International students (not Australian or New Zealand citizens or permanent residents) who are onshore in Australia at the time of application and intend to reside in Sydney; commencing an MRes full-time in January 2027; meeting the English language and MRes admission criteria; with confirmation of supervision from an eligible Macquarie researcher (compulsory for FMHHS, desirable for other faculties); holding a valid Student Visa (or an alternative visa permitting full-time study until the end of June 2028). Excluded: current Macquarie graduate research students, holders of another equivalent or major award, those who have already completed a research degree at the same or a higher level, and Session 2 2027 starters. Selection is by academic merit (WAM/GPA ranking).'),
              ('How', 'Combined course and scholarship application through Macquarie’s online application system — the official R2R page links “Online applications”. Contact: gr.applications@mq.edu.au, +61 (2) 9850 4741.'),
              ('Deadline', 'International Road to Research Scholarship: 31 October 2026 at 11pm AEDT, for MRes commencing January 2027. The main International Research Scholarship Round (iRTP/iMQRES) closed 31 July 2026 at 11pm. Bright’s vague “October 2026” hides that the main round is already closed and the open round is onshore-only.'),
              ('Fine print', 'No full document list is published on the official iR2R page — this article says so rather than presenting an aggregator list as official. Aggregator claims of OSHC and visa-cost coverage for iRTP/iMQRES were not confirmed on the official pages read and are omitted. The official pages are mq.edu.au — the R2R page and the graduate research scholarships overview.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Macquarie University</strong> in Sydney runs its international research scholarships in rounds, and the round that matters right now is the <strong>International Road to Research Scholarship (iR2R)</strong>. It is for international students who are <strong>already onshore in Australia</strong> and about to start a <strong>Master of Research (MRes) in January 2027</strong>: a <strong>tuition-fee offset for up to one year</strong> plus a living stipend of <strong>AUD $40,900 for one year</strong> (the 2027 rate). It is the on-ramp to the three-year <strong>MRes-to-PhD progression scholarship</strong>, which is also $40,900 a year in 2027 — but the iR2R itself is one year, so “fully funded” is an overstatement for it.</p>
      <p>The main <strong>International Research Scholarship Round (iRTP / iMQRES)</strong> for MRes and PhD — the round most listings describe — <strong>closed on 31 July 2026 at 11pm</strong>. If you are offshore, that round is gone and the iR2R does not help you either: it requires you to be <strong>onshore in Australia at the time of application</strong> and to intend to <strong>reside in Sydney</strong>. Selection is by <strong>academic merit (WAM/GPA ranking)</strong>, and you need <strong>confirmation of supervision</strong> from an eligible Macquarie researcher — compulsory for the Faculty of Medicine, Health and Human Sciences, desirable for other faculties.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> — not an Australian or New Zealand citizen or permanent resident.</li>
        <li>Be <strong>onshore in Australia at the time of application</strong> and intend to <strong>reside in Sydney</strong>.</li>
        <li>Be <strong>commencing an MRes full-time in January 2027</strong> (Session 1 2027).</li>
        <li>Meet the <strong>English language and MRes admission criteria</strong>.</li>
        <li>Have <strong>confirmation of supervision</strong> from an eligible Macquarie researcher (compulsory for FMHHS, desirable for other faculties).</li>
        <li>Hold a <strong>valid Student Visa</strong> (or an alternative visa permitting full-time study until the end of June 2028).</li>
        <li><strong>Excluded:</strong> current Macquarie graduate research students, holders of another equivalent or major award, those who have already completed a research degree at the same or a higher level, and Session 2 2027 starters.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>tuition-fee offset for a maximum of one year</strong>.</li>
        <li>A <strong>living allowance stipend of AUD $40,900 for one year</strong> (2027 rate).</li>
        <li>A pathway to the <strong>three-year MRes-to-PhD progression scholarship</strong>, also $40,900 a year in 2027.</li>
        <li>A <strong>Graduate Diploma of Research scholarship of $5,000 per session</strong> (separate route).</li>
        <li><strong>Not confirmed:</strong> OSHC and visa-cost coverage claimed by aggregators for iRTP/iMQRES — not on the official pages read.</li>
        <li><strong>Not used:</strong> the $39,700 a year figure quoted by several aggregators — the official 2027 rate is $40,900.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>No full document list is published on the official iR2R page — this article does not invent one.</li>
        <li><strong>Confirmation of supervision</strong> from an eligible Macquarie researcher is officially required (compulsory for FMHHS).</li>
        <li>Aggregators list a <strong>CV, two academic referee reports, academic transcripts, proof of English proficiency, a research proposal and a passport copy</strong> — treat that list as aggregator-only, not officially confirmed.</li>
        <li>Your <strong>course application</strong> itself is combined with the scholarship application in Macquarie’s online system.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm <strong>supervision</strong> with an eligible Macquarie researcher.</li>
        <li>Submit the <strong>combined course and scholarship application</strong> through Macquarie’s online application system (the official R2R page links “Online applications”).</li>
        <li>Apply by <strong>31 October 2026 at 11pm AEDT</strong> for an MRes commencing January 2027.</li>
        <li>For questions: <strong>gr.applications@mq.edu.au</strong>, <strong>+61 (2) 9850 4741</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Macquarie University Research Scholarship 2026-27?',
  'The open round — the International Road to Research Scholarship — closes 31 October 2026 at 11pm AEDT, for an MRes commencing January 2027. The main international round (iRTP/iMQRES) closed 31 July 2026.'),
 ('Can I apply from outside Australia?',
  'Not for the open round. The iR2R requires you to be onshore in Australia at the time of application and to intend to reside in Sydney. Offshore applicants should wait for the next international round.'),
 ('How much is the Macquarie research scholarship?',
  'AUD $40,900 for one year (the 2027 rate), plus a tuition-fee offset for up to one year. The three-year MRes-to-PhD progression scholarship is also $40,900 a year. Aggregators quoting $39,700 are wrong.'),
 ('Is the Macquarie scholarship fully funded?',
  'Not for the open round: it covers one year (tuition offset plus stipend), not a full multi-year package. The “fully funded” label overstates it.'),
 ('Do I need a supervisor before I apply?',
  'Yes — confirmation of supervision from an eligible Macquarie researcher is officially required, and it is compulsory for the Faculty of Medicine, Health and Human Sciences.'),
 ('What documents do I need?',
  'No full document list is published on the official iR2R page. Aggregators list a CV, two referee reports, transcripts, English proof, a research proposal and a passport copy, but that list is not officially confirmed — check the official page and your supervisor’s requirements.')]) + '''
      <p class="verify">Verified 27 Oct 2026: mq.edu.au official pages — Road to Research Scholarship page (mq.edu.au/research/phd-and-research-degrees/how-to-apply/scholarship-opportunities/scholarship-search/road-to-research-scholarship), graduate research scholarships overview, and the closed International Scholarship Round page — iR2R closes 31 October 2026 at 11pm AEDT for MRes commencing January 2027 (Session 1 2027); main international round (iRTP/iMQRES, MRes + PhD) closed 31 July 2026 at 11pm; iR2R award is a tuition-fee offset for a maximum of one year plus a living stipend of AUD $40,900 for one year (2027 rate); three-year MRes-to-PhD progression scholarship $40,900 p.a. in 2027; Graduate Diploma of Research scholarship $5,000 per session; eligibility (onshore in Australia at time of application, intend to reside in Sydney, commencing MRes full-time January 2027, English and MRes admission criteria, supervisor confirmation compulsory for FMHHS and desirable for other faculties, valid Student Visa or alternative visa permitting full-time study until end of June 2028; exclusions: current Macquarie graduate research students, holders of another equivalent/major award, those who already completed a research degree at same/higher level, Session 2 2027 starters); selection by academic merit (WAM/GPA ranking); contact gr.applications@mq.edu.au, +61 (2) 9850 4741; scholarships.af and scholarshiptab.com — corroboration of both deadlines, the $40,900 figure and the onshore requirement. CORRECTIONS: Bright's vague "October 2026" deadline hides that the main international round is already closed and the open round is onshore-only. NOT USED: the $39,700 p.a. figure quoted by several aggregators (conflicts with the official $40,900); aggregator claims of OSHC and visa-cost coverage (not confirmed on the official pages read); the aggregator document list (CV, referees, transcripts, English proof, research proposal, passport) is aggregator-only — no full document list is published on the official iR2R page.</p>''',
 dl_long='31 October 2026, 11pm AEDT (International Road to Research Scholarship; main international round closed 31 July 2026)',
 offlinks=[('Macquarie University — Road to Research Scholarship (official)', 'https://www.mq.edu.au/research/phd-and-research-degrees/how-to-apply/scholarship-opportunities/scholarship-search/road-to-research-scholarship'),
           ('Macquarie University — Graduate Research Scholarships (official)', 'https://www.mq.edu.au/research/phd-and-research-degrees/how-to-apply/scholarship-opportunities'),
           ('Bright Scholarship — Macquarie University Research Scholarship 2026-27', 'https://brightscholarship.com/macquarie-university-research-scholarship-2026-27-in-australia/')],
 related_titles=['griffith-vc', 'deakin-vc-2027', 'lincoln-nz-2027', 'ubc-2027'])),

# ---------------------------------------------------------------- 5. Abertay University
A.append(dict(
 slug='abertay-university-scholarships-2026-uk',
 title='Abertay University Scholarships 2026 in UK (Funded)',
 meta='Abertay University Scholarships 2026: the Abertay International Scholarship pays up to £3,000 a year off tuition for up to four years — £7,000 a year combined with the Principal’s Excellence Scholarship — assessed automatically on your application for study, with no separate deadline. Eligibility, how to apply and FAQs.',
 short='Abertay University Scholarships 2026', kicker='United Kingdom · Undergraduate & Taught Master’s · Funded', mono='AB',
 prov_short='Abertay University', prov_cat='University · United Kingdom',
 h1='Abertay University Scholarships 2026 in UK (Funded)',
 sub='This one is refreshingly simple — and the listings still manage to get it wrong. The Abertay International Scholarship pays up to £3,000 a year off your tuition, for up to four years, and there is no separate application and no separate deadline: you are assessed for it automatically when you apply for study. Combined with the Principal’s Excellence Scholarship it reaches £7,000 a year. That is the whole scheme. It is not “fully funded” — it is a partial tuition discount — and the intake deadlines (15 December, 30 April, 31 August) on Bright Scholarship’s page do not appear on the official scholarship pages and could not be confirmed, so this article does not use them. Abertay is in Dundee, Scotland — not Austria, as one aggregator claims.',
 dpill='No fixed deadline · Assessed on admission',
 facts=facts([('Award', 'Abertay International Scholarship — up to £3,000 a year, maximum four years, deducted from tuition fees, for new international undergraduate and postgraduate taught students. Combinable: with the Principal’s Excellence Scholarship – Global it reaches £7,000 a year combined (£3,000 + £4,000); with the Partner Excellence Scholarship it reaches £5,000 a year combined (£3,000 + £2,000). NOT officially confirmed: a Dean’s Scholarship at £5,000 a year, which appears only on aggregators (collegedunia, shiksha) — no official Abertay page for it was found.'),
              ('Eligible', 'Classified as international (Overseas) fee status; met all academic conditions of the admission offer; a new full-time on-campus undergraduate or postgraduate taught student; for postgraduate taught, a UK 2:1 bachelor’s equivalent or better (about 60%+). Advanced Entry into Year 2 or above is also eligible. Contact: international@abertay.ac.uk.'),
              ('How', 'Apply for admission to Abertay University — no separate scholarship form. You are assessed for the scholarship based on your application for study (official Abertay page).'),
              ('Deadline', 'No fixed scholarship deadline is published. The official Abertay International Scholarship page states: "No separate application form is required, and you will be assessed for the scholarship based on your application for study." Do not use Bright’s intake deadlines (15 December / 30 April / 31 August) — they do not appear on the official scholarship pages and could not be confirmed.'),
              ('Fine print', 'Bright calls this "Fully Funded" — false; it is a partial tuition-fee discount of £3,000 a year. Bright’s "up to £12,000" is only the four-year cumulative total of £3,000 a year, not a lump sum. Bright’s "leadership/extracurricular" eligibility criteria are not on the official International Scholarship page. Abertay University is in Dundee, Scotland, UK — one aggregator wrongly says "Austria".')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Abertay University</strong> in <strong>Dundee, Scotland</strong>, keeps its international funding simple: the <strong>Abertay International Scholarship</strong> pays <strong>up to £3,000 a year</strong> off your tuition fees, for up to <strong>four years</strong>, for new international undergraduate and postgraduate taught students. There is <strong>no separate application form and no separate deadline</strong> — the university assesses you for the scholarship automatically, based on your application for study. And it stacks: combined with the <strong>Principal’s Excellence Scholarship – Global</strong> it reaches <strong>£7,000 a year</strong> (£3,000 + £4,000), and combined with the <strong>Partner Excellence Scholarship</strong> it reaches <strong>£5,000 a year</strong> (£3,000 + £2,000).</p>
      <p>Be clear about what this is: a <strong>partial tuition discount</strong>, not full funding. The “fully funded” label on aggregator pages is false, and the “up to £12,000” figure is only the four-year cumulative total of £3,000 a year, not a lump sum. A <strong>Dean’s Scholarship at £5,000 a year</strong> appears on aggregators (collegedunia, shiksha), but no official Abertay page for it was found, so it is not presented as confirmed here. If you are applying, the only thing that matters is your application for study — meet all the academic conditions of your offer, and the scholarship follows.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be classified as <strong>international (Overseas) fee status</strong>.</li>
        <li>Have <strong>met all academic conditions</strong> of your admission offer.</li>
        <li>Be a <strong>new full-time on-campus undergraduate or postgraduate taught student</strong>.</li>
        <li>For <strong>postgraduate taught</strong> study: a <strong>UK 2:1 bachelor’s equivalent or better</strong> (about 60%+).</li>
        <li><strong>Advanced Entry into Year 2 or above</strong> is also eligible.</li>
        <li>Contact: <strong>international@abertay.ac.uk</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Abertay International Scholarship:</strong> up to <strong>£3,000 a year</strong> off tuition, for up to <strong>four years</strong>.</li>
        <li><strong>Combined with the Principal’s Excellence Scholarship – Global:</strong> <strong>£7,000 a year</strong> combined (£3,000 + £4,000).</li>
        <li><strong>Combined with the Partner Excellence Scholarship:</strong> <strong>£5,000 a year</strong> combined (£3,000 + £2,000).</li>
        <li><strong>Not officially confirmed:</strong> a Dean’s Scholarship at £5,000 a year (aggregator-only).</li>
        <li><strong>Not full funding:</strong> this is a partial tuition discount — living costs, travel and the rest of the tuition are yours.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>None separate</strong> — the scholarship is assessed from your <strong>application for study</strong> (official).</li>
        <li>Do not list Bright’s generic document list as official — it is not on the official scholarship page.</li>
        <li>Prepare the normal <strong>admission application documents</strong> for your course (transcripts, qualifications, English proof where required).</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission</strong> to Abertay University for a full-time on-campus undergraduate or postgraduate taught course.</li>
        <li>Meet <strong>all academic conditions</strong> of your offer.</li>
        <li>There is <strong>no separate scholarship form</strong> — you are assessed automatically on your application for study.</li>
        <li>For questions: <strong>international@abertay.ac.uk</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Abertay University Scholarship fully funded?',
  'No. It is a partial tuition discount of up to £3,000 a year, for up to four years. The “fully funded” label on aggregator pages is false.'),
 ('What is the deadline for Abertay University Scholarships 2026?',
  'There is no separate scholarship deadline. You are assessed automatically when you apply for study, so the only dates that matter are the course application deadlines. Bright’s intake deadlines (15 December / 30 April / 31 August) do not appear on the official scholarship pages and could not be confirmed.'),
 ('How much is the Abertay International Scholarship?',
  'Up to £3,000 a year off tuition, for up to four years — £12,000 in total across four years. Combined with the Principal’s Excellence Scholarship it reaches £7,000 a year.'),
 ('Do I need a separate application for the scholarship?',
  'No. The official page states: "No separate application form is required, and you will be assessed for the scholarship based on your application for study."'),
 ('Who is eligible?',
  'New international (Overseas fee status) students on a full-time on-campus undergraduate or postgraduate taught course who have met all the academic conditions of their offer. Postgraduate taught students need a UK 2:1 equivalent or better.'),
 ('Where is Abertay University?',
  'In Dundee, Scotland, in the United Kingdom. One aggregator wrongly says "Austria" — it is not.')]) + '''
      <p class="verify">Verified 27 Oct 2026: abertay.ac.uk official pages — Abertay International Scholarship page (admin.abertay.ac.uk/study-apply/money-fees-and-funding/scholarships/abertay-international-scholarship/) — up to £3,000 per year, maximum four years, deducted from tuition fees, for new international undergraduate and postgraduate taught students; "No separate application form is required, and you will be assessed for the scholarship based on your application for study"; combinable with Dean's and Principal's Excellence; Principal's Excellence Scholarship – Global page (abertay.ac.uk/study-apply/money-fees-and-funding/scholarships/principals-excellence-scholarship-global/) — combined values £7,000/year with International (£3,000 + £4,000) and £5,000/year with Partner Excellence (£3,000 + £2,000); eligibility (international/Overseas fee status, met all academic conditions of the offer, new full-time on-campus UG or PG taught, PG taught UK 2:1 equivalent or better, Advanced Entry Year 2+ eligible); contact international@abertay.ac.uk; afterschoolafrica.com — corroboration (£3,000/year, max four years, no separate deadline, automatic assessment); collegedunia.com / shiksha.com — corroboration of the £3,000/year figure and tiered awards. CORRECTIONS: Bright's "Fully Funded" is false — partial tuition discount only. Bright's "up to £12,000" is the four-year cumulative total, not a lump sum. Bright's intake deadlines (15 Dec / 30 Apr / 31 Aug) are unconfirmed by the official source. Bright's "leadership/extracurricular" criteria are not on the official page. NOT CONFIRMED: the Dean's Scholarship at £5,000/year (aggregator-only; no official Abertay page found). One aggregator (zaupdates.co.za) wrongly says the university is in "Austria" — it is in Dundee, Scotland, UK.</p>''',
 dl_long='No separate scholarship deadline — assessed with your application for study',
 offlinks=[('Abertay University — International Scholarship (official)', 'https://admin.abertay.ac.uk/study-apply/money-fees-and-funding/scholarships/abertay-international-scholarship/'),
           ('Abertay University — Principal’s Excellence Scholarship – Global (official)', 'https://www.abertay.ac.uk/study-apply/money-fees-and-funding/scholarships/principals-excellence-scholarship-global/'),
           ('Bright Scholarship — Abertay University Scholarships 2026', 'https://brightscholarship.com/abertay-university-scholarships-2026-in-uk/')],
 related_titles=['dundee-ge', 'gates-cam-2027', 'neukom-2027', 'ubc-2027'])),

# ---------------------------------------------------------------- build + validate
for a in A:
    _split_verify(a)
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']

sizes = {}
for a in A:
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch55_built.json','w'))

class _P(html.parser.HTMLParser):
    def error(self, msg): raise ValueError(msg)

for a in A:
    p = OUT / (a['slug'] + '.html')
    assert p.exists(), a['slug']
    _P().feed(p.read_text())
    t = p.read_text()
    assert 'AICTE Pragati' not in t, a['slug']
    assert 'Lorem' not in t, a['slug']
    assert '#' not in a['slug']
    assert 'wa.me/919905166009' in t, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

# write new cards into the registry for the next run
reg = pathlib.Path('cards_registry.py').read_text()
assert reg.rstrip().endswith('}')
add = ''
for k, v in NEW_CARDS.items():
    add += " '%s': %s,\n" % (k, repr(v))
reg = reg.rstrip()[:-1] + add + '}\n'
pathlib.Path('cards_registry.py').write_text(reg)
print('registry updated, now', len(CARDS), 'cards')

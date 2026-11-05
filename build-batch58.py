#!/usr/bin/env python3
"""Batch 58 (cron run 58, 27 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order), 36 scanned:
1. HUGO Lab PhD positions (U South Carolina) - VERIFIED (Fall 2027: 1 May 2027
   international / 15 May 2027 domestic; fully funded, stipend not published;
   no official sc.edu page found - two aggregators agree exactly).
2. Messina 42nd Cycle PhD - SKIPPED: deadline passed 24 Jul 2026.
3. RMIT PhD positions - SKIPPED: no deadline published anywhere; June 2026
   listing, open status cannot be confirmed.
4. Camerino 42nd Cycle PhD - SKIPPED: deadline passed 24 Jul 2026 (later
   calls also closed, last 22 Oct 2026).
5. TDTU International Graduate Scholarship 2027 - VERIFIED (deadline
   6 Nov 2026 per official-calendar-sourced greatyop, updated 6 Oct 2026;
   other aggregators list 15 Nov as the recurring annual date).
6. Kent Future Students Global Scholarships 2026 - SKIPPED: deadline passed
   31 Jul 2026.
7. University of London Scholarships 2027 - SKIPPED: deadline conflict
   unresolvable (queue source says 8 Sep 2026, passed; StudyQA 17 Jul 2027
   is recycled from the 2020 cycle; official page states no deadline).
8. Frankfurt Universities offering Scholarships 2027 - SKIPPED: listicle.
9. Trento 42nd Cycle PhD - SKIPPED: deadline passed 20 Jul 2026 (second
   calls also closed, last 2 Sep 2026).
10. Max Planck Summer Internship 2026 - SKIPPED: titled 2026 but the
    1 Nov 2026 deadline is for summer 2027 internships; 2026 cycle closed
    1 Nov 2025.
11. King Fahd University Scholarships 2026 - SKIPPED: deadline passed
    (latest claimed date 11 Jul 2026).
12. UCL IMPACT Scholarship 2027 - VERIFIED (official UCL page, 2027/28
    cycle: deadline 30 Jun 2027, 11:59pm BST; up to GBP 20,500; two
    bursaries; Bright's 30 Jun 2026 was the 2026/27 cycle).
13. ISTA Postdoctoral Fellowships 2026 - SKIPPED: deadline passed
    8 Sep 2026.
14. Simon Fraser University Scholarships 2027 - SKIPPED: listicle/family
    (USES flagship facts recorded: CAD 140,000, deadline 15 Dec 2026).
15. Royal Society Entrepreneur in Residence 2026 - SKIPPED: deadline passed
    19 Aug 2026.
16. DAAD Scholarships 2027-28 - SKIPPED: listicle (~30 EPOS courses).
17. Mexico Government Scholarship 2026 - SKIPPED: deadline passed
    22 Jun 2026; no 2027 call published.
18. GIST International Scholarships 2027 - SKIPPED: deadline passed
    7 Oct 2026 (Spring intake); Fall intake opens 9 Mar 2027.
19. Greater Manchester Excellence Scholarship 2027 - SKIPPED: deadline
    passed (14/20 Aug 2026, sources conflict); no 2027 deadline published.
20. P&G Korea Summer Internship 2026 - SKIPPED: deadline passed
    17 Apr 2026; internship ran 29 Jun-28 Aug 2026, already over.
21. TMU Southbound Policy Elite Program 2026 - SKIPPED: deadline passed
    30 Jun 2026.
22. Anthropic Claude Corps Fellowships 2027 - VERIFIED as Cohort 3
    (deadline 31 Jan 2027, starts late Aug 2027; queue's Jul 2026 date was
    Cohort 1, closed 17 Jul 2026).
23. Gottingen DAAD Scholarship 2027 - VERIFIED as DAAD EPOS MSc
    Development Economics only (deadline 15 Nov 2026, 23:59 CET; Global
    South only; stipend not published officially, aggregators conflict
    EUR 934 vs EUR 992).
24. Walsh Scholars PhD Program 2026 - SKIPPED: deadline passed
    3 Jul 2026 (one single project closes 28 Oct 2026).
25. Al Qasimi Foundation Scholarships 2026 - VERIFIED as a spare
    (overseas categories open to 29 Dec 2026; RAK nationals only; four
    categories; domestic closed 30 Jun 2026). NOT written this run; stays
    in the queue for the next run.
26. Kochi University Special Scholarship 2027 - SKIPPED: deadline passed
    16 Oct 2026 (Oct 2027 second deadline 9 Apr 2027 still open).
27. Bolton Excellence Scholarships 2026 - SKIPPED: deadline passed
    Aug 2026; same scheme as Greater Manchester (pos 19).
28. NPGH Global Health Fellowship 2027 - SKIPPED: deadline passed
    15 Sep 2026.
29. York University Scholarships 2026 - VERIFIED as a spare, retitled to
    the President's International Scholarship of Excellence, Fall 2027
    entry (deadline 27 Jan 2027; $45,000/year). NOT written this run; stays
    in the queue for the next run.
30. AAUW American Short Term Scholarship 2027 - SKIPPED: deadline passed
    30 Sep 2026.
31. CSIS Internships 2026 - SKIPPED: rolling family of vacancies, no
    single scheme or deadline.
32. Moroccan Government Scholarship 2026-27 - SKIPPED: deadline passed
    (all country streams, latest 27 Jul 2026).
33. Council of Europe Traineeship 2026 - SKIPPED: deadline passed
    17 Jun 2026; call closed.
34. Portugal Government Scholarships 2027 - SKIPPED: deadline passed
    30 Sep 2026; no single official programme verified.
35. 12 Best NGO Scholarships for Nigerian Students 2026 - SKIPPED:
    listicle.
36. University of Florida Scholarships 2027 - SKIPPED: family/listicle;
    "fully funded" is false for the schemes listed.

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
 'hugo-lab-2027': {'mono': 'HU', 'title': 'Two Fully Funded PhD Positions in HUGO Lab at the University of South Carolina, Columbia',
   'href': 'hugo-lab-phd-positions-2027.html',
   'dpill': 'Deadline 1 May 2027 · %d days left' % dl_left('2027-05-01'),
   'award': 'Fully funded PhD positions in Human Factors: full tuition waiver, a monthly living stipend and guaranteed funding for the first two years. The stipend amount is not published.',
   'elig': 'All nationalities; TOEFL iBT 80+ or IELTS 6.5+ for international applicants; apply by email to the lab director.',
   'tags': [('PhD', 'blue'), ('USA', 'teal')]},
 'tdtu-2027': {'mono': 'TD', 'title': 'TDTU International Graduate Scholarship 2027 in Vietnam (Funded)',
   'href': 'tdtu-international-graduate-scholarship-2027-vietnam.html',
   'dpill': 'Deadline 6 Nov 2026 · %d days left' % dl_left('2026-11-06'),
   'award': 'Full Scholarship: 100% tuition waiver plus free accommodation. Partial Scholarship: 50% tuition and 50% accommodation. No cash stipend is published.',
   'elig': 'All nationalities; a Bachelor’s degree for a Master’s, a Master’s degree for a PhD; IELTS 5.5+ or TDTU’s own English assessment.',
   'tags': [('Master’s & PhD', 'blue'), ('Vietnam', 'teal')]},
 'ucl-impact-2027': {'mono': 'UC', 'title': 'The IMPACT Scholarship 2027 at UCL in UK (Funded)',
   'href': 'ucl-impact-scholarship-2027-uk.html',
   'dpill': 'Deadline 30 Jun 2027 · %d days left' % dl_left('2027-06-30'),
   'award': 'Up to £20,500 per recipient, applied first to tuition fees of the UCL online Public Health MPH. Two bursaries for 2027/28.',
   'elig': 'Lived experience of inequality; meets the MPH admissions criteria; has applied for the MPH starting 2027/28; home and overseas fee status both eligible.',
   'tags': [('Master’s', 'blue'), ('UK', 'teal')]},
 'claude-corps-2027': {'mono': 'AC', 'title': 'Anthropic Claude Corps Fellowships 2027 (Stipend $85,000)',
   'href': 'anthropic-claude-corps-fellowships-2027.html',
   'dpill': 'Deadline 31 Jan 2027 · %d days left' % dl_left('2027-01-31'),
   'award': '$85,000 annual salary plus benefits for a year at a US nonprofit using AI for public good; up to $2,500 in Claude API credits and relocation support. No degree required.',
   'elig': 'Aged 18+; under 2 years of full-time work experience; authorised to work in the US for the full 12 months without visa sponsorship; early-career.',
   'tags': [('Fellowship', 'blue'), ('USA', 'teal')]},
 'gottingen-daad-2027': {'mono': 'UG', 'title': 'Fully Funded University of Gottingen DAAD Scholarship 2027 in Germany',
   'href': 'university-of-gottingen-daad-scholarship-2027-germany.html',
   'dpill': 'Deadline 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
   'award': 'DAAD EPOS award for the MSc Development Economics at Göttingen: monthly stipend (not published on the official page; aggregators cite €934 or €992), insurance and travel allowance. Only 6–7 places a year.',
   'elig': 'Nationals of developing / Global South countries with a Bachelor’s degree and at least 2 years of relevant professional experience after the first degree.',
   'tags': [('Master’s', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. HUGO Lab PhD positions
A.append(dict(
 slug='hugo-lab-phd-positions-2027',
 title='Two Fully Funded PhD Positions in HUGO Lab at the University of South Carolina, Columbia',
 meta='Two fully funded PhD positions in the HUGO Lab at the University of South Carolina for Fall 2027: full tuition waiver, a monthly living stipend and guaranteed funding for the first two years. International deadline 1 May 2027.',
 short='HUGO Lab PhD Positions 2027', kicker='USA · PhD · Fully Funded', mono='HU',
 prov_short='University of South Carolina', prov_cat='University · USA',
 h1='Two Fully Funded PhD Positions in HUGO Lab at the University of South Carolina, Columbia',
 sub='Read this first, because these are not general University of South Carolina scholarships — they are two named PhD positions inside one research lab, the HUGO Lab, and you apply by emailing the lab director, not through a university portal. For Fall 2027 the lab is recruiting two PhD students to work on Human-AI Interaction, Human-Robot Interaction and related Human Factors topics. The positions are fully funded: a full tuition waiver, a monthly living stipend and guaranteed funding for the first two years, with continued funding subject to satisfactory performance. The catch is that the stipend amount is not published anywhere, and there is no official university page for the positions — the two aggregator sources that list them agree exactly on the dates and terms, and this article uses only what they agree on.',
 dpill='Deadline 1 May 2027 · %d days left' % dl_left('2027-05-01'),
 facts=facts([('Award', 'Fully funded: full tuition waiver, a monthly living stipend and guaranteed funding for the first two years, with continued funding subject to satisfactory performance. The stipend amount is not published in any source — do not plan around a figure.'),
              ('Eligible', 'All nationalities. International applicants need TOEFL iBT 80+ or IELTS 6.5+. Research areas: Human-AI Interaction, Human-Machine Interaction, Human-Robot Interaction, Human Factors and Ergonomics, Industrial Safety, Vehicle Ergonomics, Human Variability, Digital Twin Systems, Human-Centered Design.'),
              ('How', 'Email your documents to Dr. Jangwoon Park at Jangwoon.park@sc.edu. Only shortlisted candidates are contacted for interview. There is no online portal for these positions.'),
              ('Deadline', 'Fall 2027: 1 May 2027 for international applicants, 15 May 2027 for domestic applicants. The Spring 2027 deadlines (1 October / 15 October 2026) have already passed — do not apply for Spring.'),
              ('Fine print', 'No official sc.edu HUGO Lab page for these positions could be found — the facts here rest on two aggregator sources that agree exactly. One of those pages also carries generic filler about a "December deadline" and a "Fall 2026 window" in its prose; its deadline table matches the other source exactly, and only the table dates are used here.')]),
 body='''
      <h2 id="about">About the positions</h2>
      <p>The <strong>HUGO Lab</strong> at the <strong>University of South Carolina, Columbia</strong>, is recruiting <strong>two PhD students for Fall 2027</strong> to work on Human Factors and Human-AI Interaction research. The lab works across <strong>Human-AI Interaction, Human-Machine Interaction, Human-Robot Interaction, Human Factors and Ergonomics, Industrial Safety, Vehicle Ergonomics, Human Variability, Digital Twin Systems and Human-Centered Design</strong> — so the positions suit applicants whose background sits at the intersection of engineering, computer science, psychology or design, and who want to work on how people and intelligent systems work together.</p>
      <p>The funding is genuinely <strong>fully funded</strong>: a <strong>full tuition waiver</strong>, a <strong>monthly living stipend</strong> and <strong>guaranteed funding for the first two years</strong>, with continued funding subject to satisfactory performance. What is missing is the number: <strong>no source publishes the stipend amount</strong>, so this article does not state one. The other thing to know is that these positions are filled by the lab itself — you apply by <strong>emailing the lab director</strong>, and only shortlisted candidates are contacted for interview. There is no university application portal for them.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to applicants of <strong>all nationalities</strong>.</li>
        <li>International applicants need <strong>TOEFL iBT 80+</strong> or <strong>IELTS 6.5+</strong>.</li>
        <li>A background suited to the lab’s research areas: <strong>Human-AI Interaction, Human-Machine Interaction, Human-Robot Interaction, Human Factors and Ergonomics, Industrial Safety, Vehicle Ergonomics, Human Variability, Digital Twin Systems, Human-Centered Design</strong>.</li>
        <li>Applying for a <strong>PhD starting Fall 2027</strong> — the Spring 2027 deadlines have already passed.</li>
        <li>Note: there is <strong>no official sc.edu HUGO Lab page</strong> for these positions; the facts here rest on two aggregator sources that agree exactly on the dates and terms.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition waiver</strong>.</li>
        <li><strong>Monthly living stipend</strong> — the amount is <strong>not published</strong> in any source.</li>
        <li><strong>Guaranteed funding for the first two years</strong>, with continued funding subject to satisfactory performance.</li>
        <li>PhD research in the HUGO Lab at the University of South Carolina, Columbia, across Human Factors and Human-AI Interaction topics.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>one-page cover letter</strong>.</li>
        <li>Your <strong>CV</strong>.</li>
        <li>A <strong>one-page statement of research interests</strong>.</li>
        <li><strong>Official academic transcripts</strong>.</li>
        <li><strong>Three letters of recommendation</strong>.</li>
        <li>A <strong>personal statement</strong>.</li>
        <li>English-proficiency evidence (<strong>TOEFL iBT 80+</strong> or <strong>IELTS 6.5+</strong>) if you are an international applicant.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Prepare the documents listed above — cover letter, CV, statement of research interests, transcripts, three recommendation letters and personal statement.</li>
        <li><strong>Email your documents to Dr. Jangwoon Park at Jangwoon.park@sc.edu</strong>.</li>
        <li>Apply for the <strong>Fall 2027</strong> intake: <strong>1 May 2027</strong> for international applicants, <strong>15 May 2027</strong> for domestic applicants.</li>
        <li>Wait to hear back — <strong>only shortlisted candidates are contacted</strong> for interview.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the HUGO Lab PhD positions 2027?',
  'Fall 2027: 1 May 2027 for international applicants and 15 May 2027 for domestic applicants. The Spring 2027 deadlines (1 October / 15 October 2026) have already passed.'),
 ('Are the HUGO Lab PhD positions fully funded?',
  'Yes — a full tuition waiver, a monthly living stipend and guaranteed funding for the first two years, with continued funding subject to satisfactory performance. The stipend amount is not published in any source.'),
 ('How much is the HUGO Lab PhD stipend?',
  'Not published. No source states the monthly stipend amount, so do not plan around a figure — ask the lab director when you apply.'),
 ('How do I apply for the HUGO Lab PhD positions?',
  'By email, not through a portal. Send your cover letter, CV, statement of research interests, transcripts, three recommendation letters and personal statement to Dr. Jangwoon Park at Jangwoon.park@sc.edu. Only shortlisted candidates are contacted for interview.'),
 ('What research does the HUGO Lab do?',
  'Human Factors and Human-AI Interaction: Human-AI Interaction, Human-Machine Interaction, Human-Robot Interaction, Human Factors and Ergonomics, Industrial Safety, Vehicle Ergonomics, Human Variability, Digital Twin Systems and Human-Centered Design.'),
 ('What English score do I need for the HUGO Lab PhD?',
  'International applicants need TOEFL iBT 80+ or IELTS 6.5+.'),
 ('Is there an official University of South Carolina page for these positions?',
  'No official sc.edu HUGO Lab page for these positions could be found. The facts in this article rest on two aggregator sources (Scholarship Union and edu.mspro.site) that agree exactly on the dates and terms.')]) + '''
      <p class="verify">Verified 27 Oct 2026 (light re-confirm of batch 57 spare verification): scholarshipunion.com/hugo-lab-phd-scholarship/ and edu.mspro.site/fully-funded-phd-positions-in-hugo/ agree exactly — Fall 2027 deadlines 1 May 2027 (international) / 15 May 2027 (domestic); fully funded (full tuition waiver, monthly living stipend, guaranteed funding first two years, continued funding subject to satisfactory performance); stipend amount not published in any source; all nationalities; TOEFL iBT 80+ or IELTS 6.5+ for international applicants; apply by email to Dr. Jangwoon Park at Jangwoon.park@sc.edu; documents: one-page cover letter, CV, one-page statement of research interests, official transcripts, three letters of recommendation, personal statement; only shortlisted candidates contacted for interview. CONFLICTS: the edu.mspro.site page contains generic filler about a "December deadline" / "Fall 2026 window" in its prose, but its deadline table matches Scholarship Union exactly — only the table dates are used. No official sc.edu HUGO Lab page found (same as batch 57). Spring 2027 deadlines (1 Oct / 15 Oct 2026) have passed.</p>''',
 dl_long='Fall 2027 — 1 May 2027 (international) / 15 May 2027 (domestic)',
 offlinks=[('Scholarship Union — HUGO Lab PhD Scholarship', 'https://scholarshipunion.com/hugo-lab-phd-scholarship/'),
           ('edu.mspro.site — Fully Funded PhD Positions in HUGO Lab', 'https://edu.mspro.site/fully-funded-phd-positions-in-hugo/'),
           ('Bright Scholarship — PhD Positions in HUGO Lab', 'https://brightscholarship.com/phd-positions-in-hugo-lab-at-university-of-south-carolina/')],
 related_titles=['jsps-2027', 'fsu-2027', 'gem-usa-2027', 'yale-2027'])),

# ---------------------------------------------------------------- 2. TDTU International Graduate Scholarship
A.append(dict(
 slug='tdtu-international-graduate-scholarship-2027-vietnam',
 title='TDTU International Graduate Scholarship 2027 in Vietnam (Funded)',
 meta='TDTU International Graduate Scholarship 2027: a full scholarship (100% tuition waiver plus free accommodation) or a partial scholarship (50% tuition and 50% accommodation) for Master’s and PhD study at Ton Duc Thang University, Vietnam. Deadline 6 November 2026.',
 short='TDTU International Graduate Scholarship 2027', kicker='Vietnam · Master’s & PhD · Funded', mono='TD',
 prov_short='Ton Duc Thang University', prov_cat='University · Vietnam',
 h1='TDTU International Graduate Scholarship 2027 in Vietnam (Funded)',
 sub='Read this first, because the TDTU International Graduate Scholarship has two dates floating around online and only one of them is the real deadline for this cycle. Most aggregators list 15 November 2026, but that is the recurring annual date repeated from older pages. The official TDTU admissions calendar, quoted by the most recently updated source (6 October 2026), ends the submission period on 6 November 2026, with results on 8 December and enrolment on 18–19 December. Apply by 6 November to be safe. The scholarship itself is straightforward: a Full Scholarship covers 100% of tuition plus free accommodation, a Partial Scholarship covers 50% of each, and a Research Scholarship rewards outstanding publications and contributions. There is no cash stipend — the award is tuition and housing, not a salary.',
 dpill='Deadline 6 Nov 2026 · %d days left' % dl_left('2026-11-06'),
 facts=facts([('Award', 'Full Scholarship: 100% tuition fee waiver plus free accommodation. Partial Scholarship: 50% tuition fee coverage plus 50% accommodation fee support. Research Scholarship for outstanding research publications and academic contributions. No cash stipend amount is published.'),
              ('Eligible', 'All nationalities. Master’s applicants need a Bachelor’s degree; PhD applicants need a Master’s degree. English: IELTS 5.5+ (or TOEFL iBT 50 / TOEIC 600 / Cambridge PET-FCE 160) or pass TDTU’s own English Language Proficiency assessment. Master’s fields include Accounting, Applied Mathematics, Computer Science and Business Administration; PhD fields include Accounting, Business Administration, Computer Science, Civil Engineering, Computational Science and Electrical Engineering.'),
              ('How', 'First secure admission through TDTU’s graduate admissions portal. Then submit the scholarship application package by email to graduate-scholarship@tdtu.edu.vn, through the online admissions portal, or in person at the School of Graduate Studies, 19 Nguyen Huu Tho Street, District 7, Ho Chi Minh City.'),
              ('Deadline', '6 November 2026 (application submission period ends). Admission results 8 December 2026; enrolment 18–19 December 2026. Several aggregators list 15 November 2026 — that is the recurring annual date, not the current cycle’s calendar date.'),
              ('Fine print', 'TDTU accepts applications in two annual cycles: the Fall semester deadline is 15 May each year and the Spring semester deadline is 15 November in the recurring calendar. This cycle’s official calendar overrides the recurring date with 6 November 2026. The longer document list quoted on some sources (including a health fitness report) could not be fully verified against the official page.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Ton Duc Thang University (TDTU)</strong> in Ho Chi Minh City, Vietnam, offers its <strong>International Graduate Scholarship</strong> to international students for <strong>Master’s and PhD</strong> study. The award comes in three tiers. The <strong>Full Scholarship</strong> covers <strong>100% of tuition fees plus free accommodation</strong>. The <strong>Partial Scholarship</strong> covers <strong>50% of tuition plus 50% of accommodation fees</strong>. A <strong>Research Scholarship</strong> is awarded to students who demonstrate outstanding academic contributions and publish research relevant to the university’s strategic priorities. Note what the award is not: there is <strong>no cash stipend</strong> — it is tuition and housing support, not a monthly salary.</p>
      <p>The deadline needs care. TDTU runs <strong>two annual cycles</strong> — the Fall semester deadline is 15 May each year and the Spring semester deadline is 15 November in the recurring calendar — which is why most aggregator pages say 15 November 2026. But the <strong>official admissions calendar for this cycle</strong>, quoted by the most recently updated source (6 October 2026), ends the submission period on <strong>6 November 2026</strong>, with results on <strong>8 December 2026</strong> and enrolment on <strong>18–19 December 2026</strong>. This article uses 6 November as the operative deadline: apply by then, and the 15 November date cannot hurt you.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to applicants of <strong>all nationalities</strong>.</li>
        <li>For a <strong>Master’s</strong>: hold a <strong>Bachelor’s degree</strong>. For a <strong>PhD</strong>: hold a <strong>Master’s degree</strong>.</li>
        <li>English: <strong>IELTS 5.5+</strong> (or TOEFL iBT 50 / TOEIC 600 / Cambridge PET-FCE 160), or pass <strong>TDTU’s own English Language Proficiency assessment</strong>. Applicants who completed their degree in English may be exempt — confirm with TDTU.</li>
        <li>Master’s fields include <strong>Accounting, Applied Mathematics, Computer Science and Business Administration</strong>; PhD fields include <strong>Accounting, Business Administration, Computer Science, Civil Engineering, Computational Science and Electrical Engineering</strong>.</li>
        <li>For the <strong>Research Scholarship</strong>: outstanding research publications and academic contributions relevant to TDTU’s strategic priorities.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full Scholarship:</strong> <strong>100% tuition fee waiver</strong> plus <strong>free accommodation</strong>.</li>
        <li><strong>Partial Scholarship:</strong> <strong>50% tuition fee coverage</strong> plus <strong>50% accommodation fee support</strong>.</li>
        <li><strong>Research Scholarship:</strong> awarded for outstanding research publications and academic contributions.</li>
        <li>Study at a research-focused university in Ho Chi Minh City, Vietnam.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li><strong>Online application form</strong>.</li>
        <li>An updated <strong>CV</strong>.</li>
        <li><strong>Certified true copies of degree certificates and transcripts</strong> (with English translation if the originals are in another language) — Bachelor’s documents for a Master’s application, Master’s documents for a PhD application.</li>
        <li>A <strong>statement of purpose (500 words)</strong>.</li>
        <li>A valid copy of your <strong>passport</strong>.</li>
        <li><strong>Reference letter(s)</strong> (if any).</li>
        <li>A <strong>photograph (3×4 cm)</strong>.</li>
        <li><strong>Health fitness report</strong> (not older than 6 months) — listed by the aggregators; the full official list could not be verified directly, so confirm the exact checklist with TDTU.</li>
        <li><strong>Evidence of English proficiency</strong> if your previous degree was not in English.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Secure admission first</strong> — apply through TDTU’s graduate admissions portal for your Master’s or PhD programme.</li>
        <li>Prepare the scholarship application package with the documents above.</li>
        <li>Submit the package <strong>by email to graduate-scholarship@tdtu.edu.vn</strong>, through the <strong>online admissions portal</strong>, or <strong>in person</strong> at the School of Graduate Studies, 19 Nguyen Huu Tho Street, District 7, Ho Chi Minh City.</li>
        <li>Submit before <strong>6 November 2026</strong> — results are announced <strong>8 December 2026</strong> and enrolment runs <strong>18–19 December 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the TDTU International Graduate Scholarship 2027?',
  '6 November 2026, per the official TDTU admissions calendar quoted by the most recently updated source (6 October 2026). Results are announced 8 December 2026 and enrolment runs 18–19 December 2026. Several aggregators list 15 November 2026 — that is the recurring annual date, not this cycle’s calendar date — so apply by 6 November to be safe.'),
 ('Is the TDTU scholarship fully funded?',
  'The Full Scholarship covers 100% of tuition plus free accommodation. There is no cash stipend published, so it is funded rather than a full living-cost package. A Partial Scholarship (50% tuition, 50% accommodation) and a Research Scholarship are also available.'),
 ('Who can apply for the TDTU Graduate Scholarship?',
  'Students of all nationalities. Master’s applicants need a Bachelor’s degree and PhD applicants need a Master’s degree, with English at IELTS 5.5+ (or TOEFL iBT 50 / TOEIC 600) or a pass in TDTU’s own English assessment.'),
 ('How do I apply for the TDTU scholarship?',
  'Secure admission through TDTU’s graduate admissions portal first, then submit the scholarship package by email to graduate-scholarship@tdtu.edu.vn, through the online portal, or in person at the School of Graduate Studies in Ho Chi Minh City.'),
 ('What documents do I need for the TDTU scholarship?',
  'The online application form, CV, certified degree certificates and transcripts (with English translation if needed), a 500-word statement of purpose, a passport copy, reference letter(s), a 3×4 cm photograph, a health fitness report not older than 6 months, and English-proficiency evidence if your previous degree was not in English.'),
 ('Does TDTU require IELTS?',
  'Non-English speaking applicants need IELTS 5.5 or above (or TOEFL iBT 50 / TOEIC 600 / Cambridge PET-FCE 160), or they can pass TDTU’s own English Language Proficiency assessment test.')]) + '''
      <p class="verify">Verified 27 Oct 2026: brightscholarship.com/tdtu-international-graduate-scholarship-2027/, scholarshipunion.com/tdtu-graduate-scholarship-2027-vietnam/, scholarshipforphd.com/tdtu-scholarship/, townflex.com/fully-funded-tdtu-graduate-scholarship-2027-in-vietnam/, nspscholarships.com/tdtu-international-graduate-scholarship/ and greatyop.com/tdtu-scholarship-international-students/ (updated 6 Oct 2026, quoting the official TDTU admissions calendar) — Full Scholarship 100% tuition + free accommodation, Partial 50% tuition + 50% accommodation, Research Scholarship for publications/contributions; all nationalities; Master's needs Bachelor's, PhD needs Master's; IELTS 5.5+ (or TOEFL iBT 50 / TOEIC 600 / Cambridge PET-FCE 160) or TDTU's own English assessment; apply via graduate admissions portal first, then email graduate-scholarship@tdtu.edu.vn, online portal, or in person at School of Graduate Studies, 19 Nguyen Huu Tho Street, District 7, Ho Chi Minh City. CONFLICT — deadline: most aggregators list 15 November 2026 (the recurring annual "15 Nov each year" date, from June 2026 pages); greatyop, quoting the official admissions calendar, states the submission period ends 6 November 2026, results 8 December 2026, enrolment 18-19 December 2026. The article uses 6 November 2026 as the operative deadline and notes the 15 November figure. The greatyop page itself would not open (bot-check wall), so the official TDTU page could not be read directly. The longer document list (including the health fitness report) is aggregator-sourced and could not be fully verified against the official page.</p>''',
 dl_long='6 November 2026 (other aggregators list 15 November as the recurring annual date — apply by 6 November)',
 offlinks=[('Bright Scholarship — TDTU International Graduate Scholarship 2027', 'https://brightscholarship.com/tdtu-international-graduate-scholarship-2027/'),
           ('Scholarship Union — TDTU Graduate Scholarship 2027', 'https://scholarshipunion.com/tdtu-graduate-scholarship-2027-vietnam/'),
           ('Scholarship for PhD — TDTU Graduate Scholarships 2027', 'https://scholarshipforphd.com/tdtu-scholarship/'),
           ('GreatYOP — TDTU Scholarship for International Students', 'https://greatyop.com/tdtu-scholarship-international-students/')],
 related_titles=['szu-phd-2027', 'dgut-2027', 'qatar-gov-2027', 'vuw-2027'])),

# ---------------------------------------------------------------- 3. UCL IMPACT Scholarship
A.append(dict(
 slug='ucl-impact-scholarship-2027-uk',
 title='The IMPACT Scholarship 2027 at UCL in UK (Funded)',
 meta='The IMPACT Scholarship 2027 at UCL: up to £20,500 towards the online Public Health MPH for students with lived experience of inequality. Two bursaries for 2027/28. Applications open 1 March 2027, deadline 30 June 2027.',
 short='The IMPACT Scholarship 2027 at UCL', kicker='UK · Master’s · Funded', mono='UC',
 prov_short='UCL', prov_cat='University · United Kingdom',
 h1='The IMPACT Scholarship 2027 at UCL in UK (Funded)',
 sub='Read this first, because the IMPACT Scholarship is not a general UCL award — it is two bursaries for one specific degree, the online Master of Public Health (MPH), and it is awarded on lived experience of inequality, not on grades alone. Each bursary is worth up to £20,500, applied first to the MPH tuition fees, for students starting in 2027/28. Applications open on 1 March 2027 and close on 30 June 2027 at 11:59pm BST. If you see a 30 June 2026 deadline online, that was the 2026/27 cycle — the official UCL page has been updated to the 2027/28 cycle, and this article uses the new dates.',
 dpill='Deadline 30 Jun 2027 · %d days left' % dl_left('2027-06-30'),
 facts=facts([('Award', 'Up to £20,500 per recipient, applied first to tuition fees of the UCL online Public Health MPH (full-time; pro rata for part-time or modular-flexible study). Two bursaries are available for 2027/28.'),
              ('Eligible', 'Lived experience of inequality (income, ethnicity, gender, sexual orientation, carer responsibilities, adverse childhood experiences, social exclusion, disability — a non-exhaustive list). Meets the admissions criteria for the UCL online MPH. Has submitted an admissions application for the MPH starting in 2027/28. Home and overseas fee status both eligible; full-time, part-time and modular-flexible study all eligible.'),
              ('How', '1) Apply for admission to the UCL online Public Health MPH for 2027/28. 2) From 1 March 2027, complete the IMPACT Scholarship online application before 30 June 2027, 11:59pm BST. 3) Write a personal statement covering three points: how lived experience of inequality shaped your drive to study Public Health; why you need the scholarship and how it will help you personally; how you will use the MPH and scholarship to make a difference to population health. 4) Two independent assessors score each application; the two highest-ranked applicants are awarded.'),
              ('Deadline', 'Applications open 1 March 2027 and close 30 June 2027 (Wednesday), 11:59pm BST. Results are notified in early August 2027.'),
              ('Fine print', 'Bright Scholarship and other aggregators still show 30 June 2026 — that was the 2026/27 cycle. The official UCL page lists no document checklist beyond the online application with a personal statement; the document lists on aggregators (degree certificate, medical certificate, CV and so on) are generic template filler, not from UCL — do not rely on them.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>University College London (UCL)</strong> offers the <strong>IMPACT Scholarship</strong> for its <strong>online Master of Public Health (MPH)</strong>. It is a small, targeted award: <strong>two bursaries</strong> for the 2027/28 intake, each worth <strong>up to £20,500</strong>, applied first to the MPH tuition fees (pro rata for part-time or modular-flexible study). What makes it different from most scholarships is the selection basis: it is for students with <strong>lived experience of inequality</strong> — the official page names income, ethnicity, gender, sexual orientation, carer responsibilities, adverse childhood experiences, social exclusion and disability as examples, and stresses the list is not exhaustive. Academic merit matters through the MPH admissions criteria, but the scholarship itself is judged on your story and your purpose.</p>
      <p>The timeline is generous: applications <strong>open 1 March 2027</strong> and close on <strong>30 June 2027 at 11:59pm BST</strong>, with results in <strong>early August 2027</strong>. Two independent assessors score each application, and the <strong>two highest-ranked applicants</strong> are awarded. If you find a 30 June 2026 deadline on an aggregator page, ignore it — that was the 2026/27 cycle, and the official UCL page has moved on to 2027/28.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Have <strong>lived experience of inequality</strong> — for example income, ethnicity, gender, sexual orientation, carer responsibilities, adverse childhood experiences, social exclusion or disability (the official list is non-exhaustive).</li>
        <li>Meet the <strong>admissions criteria for the UCL online Master of Public Health (MPH)</strong>.</li>
        <li>Have <strong>submitted an admissions application for the MPH starting in 2027/28</strong>.</li>
        <li><strong>Home and overseas fee status</strong> are both eligible.</li>
        <li><strong>Full-time, part-time and modular-flexible</strong> study are all eligible.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to £20,500</strong> per recipient, applied first to <strong>tuition fees</strong> of the UCL online Public Health MPH.</li>
        <li><strong>Two bursaries</strong> available for 2027/28.</li>
        <li>Pro rata support for <strong>part-time or modular-flexible</strong> study.</li>
        <li>A fully <strong>online MPH</strong> — study from anywhere.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>MPH admissions application</strong> for 2027/28 (submitted first).</li>
        <li>The <strong>IMPACT Scholarship online application</strong> (from 1 March 2027).</li>
        <li>A <strong>personal statement</strong> covering: (a) how your lived experience of inequality shaped your drive to study Public Health; (b) why you need the scholarship and how it will help you personally; (c) how you will use the MPH and the scholarship to make a difference to population health.</li>
        <li>Note: the official page lists <strong>no document checklist</strong> beyond the online application with a personal statement. Aggregator lists (degree certificate, medical certificate, CV and so on) are generic template filler, not from UCL.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Apply for admission to the UCL online Public Health MPH</strong> for 2027/28.</li>
        <li>From <strong>1 March 2027</strong>, complete the <strong>IMPACT Scholarship online application</strong> on the official UCL page.</li>
        <li>Write your <strong>personal statement</strong> covering the three points above — lived experience, need, and the difference you will make.</li>
        <li>Submit before <strong>30 June 2027, 11:59pm BST</strong>.</li>
        <li><strong>Two independent assessors</strong> score each application; the <strong>two highest-ranked applicants</strong> are awarded, with results in <strong>early August 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the UCL IMPACT Scholarship 2027?',
  'Applications open 1 March 2027 and close 30 June 2027 (Wednesday), 11:59pm BST. Results are notified in early August 2027. The 30 June 2026 date on aggregator pages was the 2026/27 cycle.'),
 ('How much is the UCL IMPACT Scholarship worth?',
  'Up to £20,500 per recipient, applied first to tuition fees of the UCL online Public Health MPH (pro rata for part-time or modular-flexible study). Two bursaries are available for 2027/28.'),
 ('Who can apply for the UCL IMPACT Scholarship?',
  'Students with lived experience of inequality (income, ethnicity, gender, sexual orientation, carer responsibilities, adverse childhood experiences, social exclusion, disability — a non-exhaustive list) who meet the MPH admissions criteria and have applied for the MPH starting in 2027/28. Home and overseas fee status are both eligible.'),
 ('Is the UCL IMPACT Scholarship only for the online MPH?',
  'Yes — it is specifically for the UCL online Master of Public Health (MPH), full-time, part-time or modular-flexible.'),
 ('What should the personal statement cover?',
  'Three things: how your lived experience of inequality shaped your drive to study Public Health; why you need the scholarship and how it will help you personally; and how you will use the MPH and the scholarship to make a difference to population health.'),
 ('How are IMPACT Scholarship winners chosen?',
  'Two independent assessors score each application, and the two highest-ranked applicants are awarded.'),
 ('What documents do I need for the IMPACT Scholarship?',
  'The official page lists no document checklist beyond the online application with a personal statement. Aggregator document lists (degree certificate, medical certificate, CV and so on) are generic template filler, not from UCL.')]) + '''
      <p class="verify">Verified 27 Oct 2026: ucl.ac.uk/population-health-sciences/epidemiology-health-care/study/scholarships-and-funding/impact-scholarship (official UCL page, opened and read; updated to the 2027/28 cycle) — deadline 30 June 2027 (Wednesday), 11:59pm BST; applications open 1 March 2027; results notified early August 2027; up to £20,500 per recipient applied first to tuition fees of the UCL online Public Health MPH (full-time; pro rata part-time/modular-flexible); two bursaries for 2027/28; lived experience of inequality (income, ethnicity, gender, sexual orientation, carer responsibilities, adverse childhood experiences, social exclusion, disability — non-exhaustive); must meet MPH admissions criteria and have submitted an MPH application for 2027/28; home and overseas fee status both eligible; two independent assessors score each application, two highest-ranked awarded; personal statement covering (a) how lived experience shaped the drive to study Public Health, (b) why the scholarship is needed and how it will help personally, (c) how the MPH and scholarship will be used to make a difference to population health. CONFLICTS: Bright Scholarship and aggregators say deadline 30 June 2026 — that was the 2026/27 cycle; the official page governs. The official page lists no document checklist beyond the online application with a personal statement — Bright's document list (degree certificate, medical certificate, CV etc.) is generic template filler, not from UCL, and is not used.</p>''',
 dl_long='30 June 2027, 11:59pm BST (applications open 1 March 2027)',
 offlinks=[('UCL — IMPACT Scholarship (official)', 'https://www.ucl.ac.uk/population-health-sciences/epidemiology-health-care/study/scholarships-and-funding/impact-scholarship'),
           ('Bright Scholarship — The IMPACT Scholarship 2027 at UCL', 'https://brightscholarship.com/the-impact-scholarship-2027-at-ucl/')],
 related_titles=['abertay-2026', 'bleumink-2027', 'ceepus-2027', 'emhrpp-2027'])),

# ---------------------------------------------------------------- 4. Anthropic Claude Corps Fellowships
A.append(dict(
 slug='anthropic-claude-corps-fellowships-2027',
 title='Anthropic Claude Corps Fellowships 2027 (Stipend $85,000)',
 meta='Anthropic Claude Corps Fellowships 2027 (Cohort 3): an $85,000 annual salary plus benefits for a year at a US nonprofit using AI for public good. No degree required. Deadline 31 January 2027.',
 short='Anthropic Claude Corps Fellowships 2027', kicker='USA · Fellowship · $85,000', mono='AC',
 prov_short='Anthropic / CodePath', prov_cat='Fellowship · USA',
 h1='Anthropic Claude Corps Fellowships 2027 (Stipend $85,000)',
 sub='Read this first, because the Anthropic Claude Corps Fellowship is not a scholarship and not a student programme — it is a paid, full-time, year-long job at a US nonprofit, for early-career people who already use AI tools in their daily life and work. Cohort 3 starts in late August 2027 and pays an $85,000 annual salary plus benefits, with up to $2,500 in Claude API credits and relocation support. There is no degree requirement and no visa sponsorship — you must already be authorised to work in the US for the full 12 months. The queue’s July 2026 date was Cohort 1, which closed on 17 July 2026. This article is about Cohort 3, whose deadline is 31 January 2027.',
 dpill='Deadline 31 Jan 2027 · %d days left' % dl_left('2027-01-31'),
 facts=facts([('Award', '$85,000 annual salary plus benefits (health, dental, vision, 401(k), paid time off); up to $2,500 in Claude API credits; relocation support; a CodePath mentor. Host nonprofits receive a $10,000 implementation grant. 1,000 fellows across 3 cohorts; 400+ host nonprofits. Anthropic committed $150M; partners: Anthropic (funds), CodePath (employer of record), Social Finance (measurement).'),
              ('Eligible', 'Aged 18+ by the start date; under 2 years of full-time work experience; authorised to work in the US for the full 12 months without visa sponsorship; no degree required; early-career (finishing school, leaving military service, first full-time job); already uses AI tools in daily life/work; willing to relocate if needed; full-time, in-person at a US host nonprofit.'),
              ('How', '1) Complete the free AI Fluency and Claude 101 modules on Skilljar — required before submitting. 2) Apply online at anthropic.com/claude-corps/fellow — personal details, cohort choice, relocation availability, CV and two short answers (community impact; learning from a setback). 3) Take-home assessment if shortlisted. 4) 25-minute conversation. 5) Final round of two interviews. 6) Interviews with 2–3 host nonprofits, then matching.'),
              ('Deadline', 'Cohort 3, starting late August 2027. Applications are reviewed on a rolling basis, with a deadline of 31 January 2027 for consideration. The queue’s July 2026 date was Cohort 1 (closed 17 July 2026, started October 2026).'),
              ('Fine print', 'One early TechTimes piece (June 2026) estimated "approx. mid-May 2027" for the August 2027 start — superseded by the official 31 January 2027 deadline now posted. One aggregator says "no fixed deadline, rolling" — incomplete; the official posting gives 31 January 2027. One secondary source mentions a 500-word project proposal for Cohort 2 — not in the official posting, so it is not stated here as a requirement.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Claude Corps Fellowship</strong>, run by <strong>Anthropic</strong> with <strong>CodePath</strong> and <strong>Social Finance</strong>, places early-career people in <strong>full-time, in-person roles at US nonprofits</strong> for a year, doing work that uses AI — specifically Claude — for public good. Anthropic funds the programme (a <strong>$150M commitment</strong>), CodePath is the employer of record, and Social Finance handles measurement. Across the three cohorts there will be <strong>1,000 fellows</strong> at <strong>400+ host nonprofits</strong>, and each host nonprofit also receives a <strong>$10,000 implementation grant</strong>.</p>
      <p>The money is a salary, not a scholarship: <strong>$85,000 a year plus benefits</strong> (health, dental, vision, 401(k), paid time off), <strong>up to $2,500 in Claude API credits</strong> and <strong>relocation support</strong>, plus a <strong>CodePath mentor</strong>. The unusual part is who can apply: there is <strong>no degree requirement</strong> and no minimum qualification beyond being early-career — finishing school, leaving military service, or starting a first full-time job — and <strong>already using AI tools in daily life or work</strong>. The hard limits are experience (under 2 years of full-time work) and work authorisation (you must already be authorised to work in the US for the full 12 months, with <strong>no visa sponsorship</strong>).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Aged <strong>18+</strong> by the start date.</li>
        <li>Under <strong>2 years of full-time work experience</strong>.</li>
        <li><strong>Authorised to work in the US</strong> for the full 12 months <strong>without visa sponsorship</strong>.</li>
        <li><strong>No degree required</strong>.</li>
        <li>Early-career: finishing school, leaving military service, or starting a first full-time job.</li>
        <li><strong>Already uses AI tools</strong> in daily life or work.</li>
        <li>Willing to <strong>relocate</strong> if needed; the role is <strong>full-time, in-person</strong> at a US host nonprofit.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>$85,000 annual salary</strong> plus benefits (health, dental, vision, 401(k), paid time off).</li>
        <li>Up to <strong>$2,500 in Claude API credits</strong>.</li>
        <li><strong>Relocation support</strong>.</li>
        <li>A <strong>CodePath mentor</strong>.</li>
        <li>Host nonprofits receive a <strong>$10,000 implementation grant</strong>.</li>
        <li>A year of full-time, in-person work at a US nonprofit using AI for public good.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Completion of the free <strong>AI Fluency</strong> and <strong>Claude 101</strong> modules on Skilljar — <strong>required before submitting</strong> the application.</li>
        <li>Your <strong>CV</strong>.</li>
        <li><strong>Two short answers</strong>: community impact, and learning from a setback.</li>
        <li>Personal details, <strong>cohort choice</strong> and <strong>relocation availability</strong> in the online form.</li>
        <li>Note: one secondary source mentions a 500-word project proposal for Cohort 2 — it is <strong>not in the official posting</strong> and is not stated here as a requirement.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete the free <strong>AI Fluency</strong> and <strong>Claude 101</strong> modules on Skilljar first — they are required before you can submit.</li>
        <li>Apply online at <strong>anthropic.com/claude-corps/fellow</strong> — personal details, cohort choice, relocation availability, CV and the two short answers.</li>
        <li>If shortlisted, complete the <strong>take-home assessment</strong>.</li>
        <li>Take part in a <strong>25-minute conversation</strong>, then a <strong>final round of two interviews</strong>.</li>
        <li>Interview with <strong>2–3 host nonprofits</strong>, then matching. Cohort 3 starts in <strong>late August 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Anthropic Claude Corps Fellowships 2027?',
  '31 January 2027 for Cohort 3, which starts in late August 2027. Applications are reviewed on a rolling basis. The July 2026 date in the queue was Cohort 1, which closed on 17 July 2026.'),
 ('How much does the Claude Corps Fellowship pay?',
  '$85,000 annual salary plus benefits (health, dental, vision, 401(k), paid time off), up to $2,500 in Claude API credits and relocation support. Host nonprofits also receive a $10,000 implementation grant.'),
 ('Do I need a degree for the Claude Corps Fellowship?',
  'No — there is no degree requirement. The fellowship is for early-career people (finishing school, leaving military service, or starting a first full-time job) who already use AI tools in daily life or work.'),
 ('Can international students apply for the Claude Corps Fellowship?',
  'Only if you are already authorised to work in the US for the full 12 months without visa sponsorship. There is no visa sponsorship.'),
 ('What is the Claude Corps Fellowship?',
  'A year-long, full-time, in-person fellowship at a US nonprofit using AI (Claude) for public good, run by Anthropic with CodePath and Social Finance. There are 1,000 fellows across 3 cohorts at 400+ host nonprofits.'),
 ('What do I need to do before applying?',
  'Complete the free AI Fluency and Claude 101 modules on Skilljar — they are required before you can submit the application. Then apply online with your CV and two short answers (community impact; learning from a setback).'),
 ('What is the selection process for Claude Corps?',
  'Online application, then a take-home assessment if shortlisted, a 25-minute conversation, a final round of two interviews, and interviews with 2–3 host nonprofits before matching.')]) + '''
      <p class="verify">Verified 27 Oct 2026: job-boards.greenhouse.io/claudecorps/jobs/4402649009 (CodePath official job board posting, mirrored verbatim by Harvard FAS and Morehouse career pages) — "third cohort which will start late August 2027. Applications are reviewed on a rolling basis, with a deadline of January 31, 2027 for consideration"; anthropic.com/claude-corps/fellow (programme/apply page); contact recruiting@claudecorps.org. Award: $85,000 annual salary + benefits (health, dental, vision, 401(k), paid time off); up to $2,500 in Claude API credits; relocation support; CodePath mentor; host nonprofits receive a $10,000 implementation grant; 1,000 fellows across 3 cohorts; 400+ host nonprofits; Anthropic committed $150M; partners Anthropic (funds), CodePath (employer of record), Social Finance (measurement). Eligibility: aged 18+ by start date; under 2 years of full-time work experience; authorised to work in the US for the full 12 months without visa sponsorship; no degree required; early-career (finishing school, leaving military service, first full-time job); already uses AI tools in daily life/work; willing to relocate; full-time, in-person at a US host nonprofit. Steps: free AI Fluency and Claude 101 modules on Skilljar (required before submitting); online application (personal details, cohort choice, relocation availability, CV, two short answers — community impact; learning from a setback); take-home assessment if shortlisted; 25-minute conversation; final round of two interviews; interviews with 2-3 host nonprofits, then matching. CONFLICTS: the queue's July 2026 date was Cohort 1 only (closed 17 July 2026, started Oct 2026) — this article is about Cohort 3. An early TechTimes piece (June 2026) estimated "approx. mid-May 2027" for the Aug 2027 start — superseded by the official 31 Jan 2027 deadline. One aggregator says "no fixed deadline, rolling" — incomplete. One secondary source mentions a 500-word project proposal for Cohort 2 — not in the official posting, not stated as a requirement.</p>''',
 dl_long='31 January 2027 (Cohort 3, starts late August 2027)',
 offlinks=[('Anthropic — Claude Corps Fellowship (official)', 'https://www.anthropic.com/claude-corps/fellow'),
           ('CodePath — Claude Corps Fellowship, Cohort 3 (official job board)', 'https://job-boards.greenhouse.io/claudecorps/jobs/4402649009'),
           ('Bright Scholarship — Anthropic Claude Corps Fellowships 2027', 'https://brightscholarship.com/anthropic-claude-corps-fellowships-2027/')],
 related_titles=['gem-usa-2027', 'kpmg-gip-2026', 'unicef-2027', 'ieee-gov-2027'])),

# ---------------------------------------------------------------- 5. Gottingen DAAD EPOS
A.append(dict(
 slug='university-of-gottingen-daad-scholarship-2027-germany',
 title='Fully Funded University of Gottingen DAAD Scholarship 2027 in Germany',
 meta='University of Göttingen DAAD Scholarship 2027: a DAAD EPOS award for the MSc Development Economics, for students from developing countries with at least 2 years of professional experience. Deadline 15 November 2026.',
 short='University of Gottingen DAAD Scholarship 2027', kicker='Germany · Master’s · Fully Funded', mono='UG',
 prov_short='University of Göttingen', prov_cat='University · Germany',
 h1='Fully Funded University of Gottingen DAAD Scholarship 2027 in Germany',
 sub='Read this first, because the University of Göttingen DAAD Scholarship is narrower than its name suggests — it is one DAAD EPOS award for one degree, the MSc Development Economics, for students from developing countries who already have at least two years of professional experience. There is no PhD route at Göttingen under this call, and "All Nationalities" is wrong: EPOS is for Global South countries only. There are only 6–7 scholarships a year, and the application window is 1 October to 15 November 2026, with the programme starting in October 2027. One more honest gap: the official Göttingen page does not publish a stipend figure, and aggregators disagree on it — this article states the conflict instead of picking a number.',
 dpill='Deadline 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
 facts=facts([('Award', 'DAAD EPOS award for the MSc Development Economics: a monthly stipend (not published on the official Göttingen page — aggregators cite €934/month or €992/month, a conflict; confirm with DAAD), plus health, accident and liability insurance, a travel allowance, and a possible rent subsidy and family allowance. Only 6–7 scholarships per year.'),
              ('Eligible', 'National of a developing / Global South country; a Bachelor’s degree; at least 2 years of relevant professional experience after the first degree; a strong academic record; commitment to sustainable development; English or German proficiency per the programme requirements. Must also meet the MSc Development Economics general admission requirements.'),
              ('How', 'One single application via the Göttingen application portal (1 October – 15 November 2026): create an account, complete your profile, choose "Regular Procedure" and select "Development Economics with DAAD EPOS SCHOLARSHIP", complete the 3-step process and upload the programme and DAAD documents. Late or incomplete applications are rejected.'),
              ('Deadline', '15 November 2026, 23:59 CET. Interviews January–March 2027; decisions mid-March 2027; intensive German course August–September 2027; programme starts October 2027.'),
              ('Fine print', 'This is the DAAD EPOS route for the MSc Development Economics only — the official page covers no PhD route at Göttingen, so the "Master’s, PhD" framing on aggregators is misleading. Aggregators saying "All Nationalities" are wrong: EPOS is for students from Global South / developing countries only.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Göttingen</strong> in Germany offers a <strong>DAAD EPOS (Development-Related Postgraduate Courses)</strong> scholarship for its <strong>MSc Development Economics</strong>, starting in <strong>October 2027</strong>. EPOS is DAAD’s programme for professionals from developing countries: it funds a full Master’s in Germany for people who already have work experience and want to take that expertise home. Göttingen awards only <strong>6–7 of these scholarships a year</strong>, which makes it one of the more competitive EPOS places — the application window runs <strong>1 October to 15 November 2026</strong>.</p>
      <p>Two corrections matter before you apply. First, this call is for the <strong>MSc Development Economics only</strong> — the official Göttingen page covers no PhD route, whatever aggregators say about "Master’s, PhD". Second, it is <strong>not open to all nationalities</strong>: EPOS is for students from <strong>Global South / developing countries</strong> only. And one honest gap: the official page does <strong>not publish a stipend figure</strong>. Aggregators cite <strong>€934 a month</strong> (the current DAAD EPOS Master’s rate) or <strong>€992 a month</strong> (a more recent figure) — the two disagree, so this article reports both and tells you to confirm with DAAD rather than presenting either as official.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be a national of a <strong>developing / Global South country</strong> — EPOS is not open to all nationalities.</li>
        <li>Hold a <strong>Bachelor’s degree</strong> and meet the <strong>MSc Development Economics general admission requirements</strong>.</li>
        <li>Have at least <strong>2 years of relevant professional experience after your first degree</strong> (the standard DAAD EPOS rule).</li>
        <li>Have a <strong>strong academic record</strong>.</li>
        <li>Show a <strong>commitment to sustainable development</strong>.</li>
        <li>Meet the <strong>English or German proficiency</strong> requirements of the programme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>monthly stipend</strong> — the amount is <strong>not published on the official Göttingen page</strong>; aggregators cite <strong>€934/month</strong> or <strong>€992/month</strong> (confirm with DAAD).</li>
        <li><strong>Health, accident and liability insurance</strong>.</li>
        <li>A <strong>travel allowance</strong>.</li>
        <li>A possible <strong>rent subsidy</strong> and <strong>family allowance</strong>.</li>
        <li>An <strong>intensive German course</strong> in August–September 2027 before the programme starts.</li>
        <li>Only <strong>6–7 scholarships</strong> are awarded per year.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>The <strong>online application form</strong> (Göttingen portal).</li>
        <li>Your <strong>CV</strong>.</li>
        <li>A <strong>motivation letter</strong>.</li>
        <li><strong>Two recommendation letters</strong>.</li>
        <li>Proof of <strong>English or German proficiency</strong>.</li>
        <li><strong>Academic transcripts and degree certificates</strong>.</li>
        <li>A valid <strong>passport or ID</strong>.</li>
        <li>Note: the official page links to separate programme and DAAD-EPOS document lists — check both before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the <strong>Göttingen application portal</strong> (1 October – 15 November 2026) and <strong>create an account</strong>.</li>
        <li>Complete your profile and choose <strong>"Regular Procedure"</strong>, then select <strong>"Development Economics with DAAD EPOS SCHOLARSHIP"</strong>.</li>
        <li>Complete the <strong>3-step process</strong> and upload the programme documents and the DAAD documents.</li>
        <li>Submit before <strong>15 November 2026, 23:59 CET</strong> — successful submission shows "Application Submitted". <strong>Late or incomplete applications are rejected.</strong></li>
        <li>Interviews run <strong>January–March 2027</strong>; decisions come in <strong>mid-March 2027</strong>; the intensive German course runs <strong>August–September 2027</strong> and the programme starts in <strong>October 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Göttingen DAAD Scholarship 2027?',
  '15 November 2026, 23:59 CET. The application window is 1 October – 15 November 2026. Interviews run January–March 2027, decisions come in mid-March 2027, and the programme starts in October 2027.'),
 ('How much is the Göttingen DAAD Scholarship stipend?',
  'The official Göttingen page does not publish a stipend figure. Aggregators cite €934 a month (the current DAAD EPOS Master’s rate) or €992 a month — the two disagree, so confirm the current rate with DAAD before relying on either figure. Insurance, a travel allowance and a possible rent subsidy and family allowance are also included.'),
 ('Who can apply for the Göttingen DAAD Scholarship?',
  'Nationals of developing / Global South countries with a Bachelor’s degree, at least 2 years of relevant professional experience after the first degree, a strong academic record and a commitment to sustainable development, who meet the MSc Development Economics admission requirements.'),
 ('Is the Göttingen DAAD Scholarship open to all nationalities?',
  'No — aggregators saying "All Nationalities" are wrong. DAAD EPOS is for students from Global South / developing countries only.'),
 ('Does the Göttingen DAAD Scholarship cover a PhD?',
  'No — this call is the DAAD EPOS route for the MSc Development Economics only. The official Göttingen page covers no PhD route, so the "Master’s, PhD" framing on aggregators is misleading.'),
 ('How many Göttingen DAAD EPOS scholarships are there?',
  'Only 6–7 scholarships per year.'),
 ('How do I apply for the Göttingen DAAD Scholarship?',
  'Through one single application on the Göttingen portal: create an account, choose "Regular Procedure", select "Development Economics with DAAD EPOS SCHOLARSHIP", complete the 3-step process and upload the programme and DAAD documents before 15 November 2026, 23:59 CET.')]) + '''
      <p class="verify">Verified 27 Oct 2026: uni-goettingen.de/en/572462.html (official University of Göttingen DAAD EPOS page) — confirms the scheme, the 1 Oct – 15 Nov 2026 window, interviews Jan–Mar 2027, intensive German course Aug–Sep 2027, decisions mid-March 2027, programme starts October 2027, only 6-7 scholarships per year. CORRECTIONS: (a) this is the DAAD EPOS route for the MSc Development Economics only — the official page covers no PhD route at Göttingen, so the "Master's, PhD" framing is misleading; (b) aggregators say "All Nationalities" — wrong: EPOS is for students from Global South / developing countries only. Eligibility: meet the MSc Development Economics general admission requirements plus DAAD EPOS criteria — national of a developing/Global South country; Bachelor's degree; at least 2 years of relevant professional experience after the first degree (standard DAAD EPOS rule, confirmed by multiple secondary sources); strong academic record; commitment to sustainable development; English or German proficiency per programme requirements. CONFLICT — stipend: not published on the official Göttingen page; aggregators conflict — most cite €934/month (Master's) and €1,300/month (PhD, other DAAD routes); one recent source cites €992/month for Master's and advises confirming with DAAD. The article states the €934 vs €992 conflict and does not present either as official. Also included: health/accident/liability insurance, travel allowance, possible rent subsidy and family allowance. Documents (per aggregators; official page links to separate programme and DAAD-EPOS document lists): online application form, CV, motivation letter, two recommendation letters, proof of English/German proficiency, academic transcripts and degree certificates, valid passport/ID. How to apply: one single application via the Göttingen portal — create account, complete profile, choose "Regular Procedure" → select "Development Economics with DAAD EPOS SCHOLARSHIP", complete the 3-step process, upload programme + DAAD documents, submit; successful submission shows "Application Submitted"; late/incomplete applications are rejected.</p>''',
 dl_long='15 November 2026, 23:59 CET',
 offlinks=[('University of Göttingen — DAAD EPOS, MSc Development Economics (official)', 'https://uni-goettingen.de/en/572462.html'),
           ('Bright Scholarship — University of Gottingen DAAD Scholarship 2027', 'https://brightscholarship.com/university-of-gottingen-daad-scholarship-2027/')],
 related_titles=['daad-reinvitation-2027', 'sbw-berlin-2027', 'stuttgart-2027', 'emhrpp-2027'])),

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
    json.dump(sizes, open('/tmp/batch58_built.json','w'))

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

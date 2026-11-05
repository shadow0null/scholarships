#!/usr/bin/env python3
"""Batch 46 (cron run 46, 24 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Ritsumeikan APU Rotary Yoneyama Scholarship 2027 — SKIPPED: APU
   application deadlines passed (15 Sep 2026 September intake; 7 Oct 2026
   April intake); the foundation's October window cannot be entered without
   the APU application step.
2. University of St Andrews Postgraduate Scholarships 2027 — VERIFIED:
   St Leonard's Masters (international), closes 3 Feb 2027, plus the
   World-Leading Doctoral route, closes 20 Jan 2027. Official
   st-andrews.ac.uk catalogue page confirms the master's scheme.
3. UBC Killam Fellowship 2027 — VERIFIED (official postdocs.ubc.ca):
   CAD 60,000/year up to 2 years, 4-6 new awards; department nominations
   due 6 Nov 2026 4pm PT. Article warns that applicants face earlier
   departmental internal deadlines (typically October; several already
   closed, e.g. Okanagan 5 Oct 2026).
4. RMIT Scholarship 2027 — SKIPPED: the "fully funded" RMIT route is the
   Research Stipend Scholarship; its international full-application
   deadline was 30 Sep 2026 (passed).
5. Sophia University Scholarship 2027 — VERIFIED: New Student Scholarship
   (1/3, 1/2 or full first-year tuition) + Adachi Scholarship (full tuition
   + education enhancement fee, international students only); live windows
   11 Nov-11 Dec 2026 and 10 Mar-7 Apr 2027.
6. University of Macau Scholarships 2027 — SKIPPED: deadline 23 Oct 2026
   passed (yesterday).
7-28. Twenty-two further 2019/2020-edition queue entries — SKIPPED as stale
   editions (deadlines in 2019/2020, or 2019 internship postings).
8. Loyola University Maryland Undergraduate Merit Scholarships — VERIFIED
   (official loyola.edu): Presidential $41,000-$45,000, Dean's
   $39,000-$40,000, Loyola $37,000-$38,000 for 2027-28; automatic with the
   admission application; Early Action 15 Nov 2026, Regular Decision
   15 Jan 2027. Official page confirms international students are eligible.
9-151. A further 123 stale 2019/2020/2021-edition entries — SKIPPED
   (same stale-edition reason; full list in queue-progress.json).
10. KAUST MEWC Winter Camp 2027 — SKIPPED: deadline 24 Sep 2026 passed.
11. University of Vechta PhD Scholarships 2027 — VERIFIED (official
    uni-vechta.de call + boeckler.de): up to 3 Hans Boeckler-funded PhD
    scholarships, EUR 1,650/month up to 3 years, deadline 2 Nov 2026.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 24)
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
 'st-andrews-pg-2027': {'mono': 'SA', 'title': 'University of St Andrews Postgraduate Scholarships 2027 in Scotland (Funded)',
   'href': 'university-of-st-andrews-postgraduate-scholarships-2027-scotland.html',
   'dpill': 'PhD 20 Jan 2027 · Master\u2019s 3 Feb 2027',
   'award': 'St Leonard\u2019s Master\u2019s awards from 25% of tuition up to full tuition + \u00a318,000; up to 6 fully funded doctoral awards (full tuition + annual stipend).',
   'elig': 'Overseas fee-status applicants for eligible full-time taught/research master\u2019s or PhD programmes starting 2027; one application covers many awards.',
   'tags': [('Master\u2019s & PhD', 'blue'), ('Scotland', 'teal')]},
 'ubc-killam-2027': {'mono': 'UB', 'title': 'UBC Killam Fellowship 2027 in Canada (Funded)',
   'href': 'ubc-killam-fellowship-2027-canada.html',
   'dpill': 'Dept nominations 6 Nov 2026 · %d days left' % dl_left('2026-11-06'),
   'award': 'CAD 60,000 per year for up to two years for 4\u20136 new postdoctoral fellows; a research travel allowance is also listed in secondary summaries.',
   'elig': 'Recent PhD holders (PhD completed within 24 months of start) who did not do their PhD at UBC, with no tenure-track post, nominated by a UBC department.',
   'tags': [('Postdoc & research', 'purple'), ('Canada', 'teal')]},
 'sophia-2027': {'mono': 'SO', 'title': 'Sophia University Scholarship 2027 in Japan (Funded)',
   'href': 'sophia-university-scholarship-2027-japan.html',
   'dpill': 'Next window 11 Dec 2026 · %d days left' % dl_left('2026-12-11'),
   'award': 'New Student Scholarship: 1/3, 1/2 or full first-year tuition. Adachi Scholarship (international students): full first-year tuition + education enhancement fee.',
   'elig': 'New or transfer applicants to Sophia\u2019s English-taught undergraduate or graduate programmes for 2027 entry, with excellent grades, financial hardship, and Sophia as first choice.',
   'tags': [('Bachelor\u2019s & Master\u2019s', 'blue'), ('Japan', 'teal')]},
 'loyola-merit-2027': {'mono': 'LM', 'title': 'Undergraduate Merit Scholarships at Loyola University Maryland USA',
   'href': 'loyola-university-maryland-undergraduate-merit-scholarships-usa.html',
   'dpill': 'Early Action 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
   'award': '2027-28 merit awards: Presidential $41,000\u2013$45,000, Dean\u2019s $39,000\u2013$40,000, Loyola $37,000\u2013$38,000 per year, renewable for up to 4 years (tuition only).',
   'elig': 'First-year and transfer undergraduates admitted to Loyola University Maryland, including international students; automatic consideration, no separate application.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'vechta-phd-2027': {'mono': 'UV', 'title': 'University of Vechta PhD Scholarships 2027 in Germany (Stipend \u20ac1,650)',
   'href': 'university-of-vechta-phd-scholarships-2027-germany.html',
   'dpill': 'Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
   'award': '\u20ac1,650 per month (\u20ac1,550 stipend + \u20ac100 research allowance) for up to 3 years, plus up to \u20ac100/month health insurance contribution and possible family allowance.',
   'elig': 'Doctoral researchers in sustainability, justice and rural transformation themes, for the PK 060 doctoral college at the University of Vechta.',
   'tags': [('PhD', 'purple'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. St Andrews
A.append(dict(
 slug='university-of-st-andrews-postgraduate-scholarships-2027-scotland',
 title='University of St Andrews Postgraduate Scholarships 2027 in Scotland (Funded)',
 meta='University of St Andrews Postgraduate Scholarships 2027: the St Leonard\u2019s Master\u2019s scheme for international students (25% of tuition up to full tuition + \u00a318,000) and up to 6 fully funded World-Leading Doctoral awards. Deadlines 20 January and 3 February 2027 — eligibility, documents, how to apply and FAQs.',
 short='University of St Andrews Postgraduate Scholarships 2027', kicker='Scotland · Master\u2019s & PhD · Funded', mono='SA',
 prov_short='University of St Andrews', prov_cat='University · Scotland',
 h1='University of St Andrews Postgraduate Scholarships 2027 in Scotland (Funded)',
 sub='The University of St Andrews Postgraduate Scholarships 2027 are really two routes under one umbrella: the St Leonard\u2019s Master\u2019s Scholarship for international students, which can pay anything from a quarter of your tuition up to full tuition plus an \u00a318,000 living allowance, and the St Leonard\u2019s College World-Leading Doctoral Scholarships, up to six fully funded PhD awards. The doctoral route closes on 20 January 2027 and the master\u2019s route on 3 February 2027, and a single scholarship application puts you in the running for many awards at once.',
 dpill='PhD 20 Jan 2027 · Master\u2019s 3 Feb 2027',
 facts=facts([('Award', 'Master\u2019s route (St Leonard\u2019s Master\u2019s Scholarship, international students): tiered awards — Global Widening Participation covers full tuition plus \u00a318,000 towards living costs; Leadership covers 75% of tuition plus up to \u00a32,000 for approved career activities; Excellence covers 25% or 50% of tuition. Doctoral route (World-Leading Doctoral Scholarships): up to 6 awards covering full tuition plus an annual stipend (the 2026/27 reference stipend quoted in secondary summaries is \u00a320,467 — confirm the 2027/28 figure on st-andrews.ac.uk). Master\u2019s funding lasts one year; for eligible longer research programmes it covers the first year only.'),
              ('Eligible', 'Master\u2019s: students with Overseas fee status applying for eligible full-time one-year taught master\u2019s degrees, one-year research master\u2019s, and some two-year research master\u2019s with a taught first year, starting in September 2027 (January 2028, or August 2027 for the Master of Public Policy, where applicable). Doctoral: PhD applicants in any field, with no topic limits across the qualifying schools; you must not already hold a doctorate or be enrolled in a doctoral programme elsewhere. Assessment is on academic excellence, wider achievement, leadership and financial need — not on financial need alone.'),
              ('How', 'Apply for your St Andrews course first, then submit one scholarship application through the university\u2019s My Application portal. That single application automatically considers you for the other awards inside the St Leonard\u2019s scheme, and for any further awards added to the scheme after you apply.'),
              ('Deadline', 'Doctoral route: 20 January 2027. Master\u2019s route (international): 3 February 2027. The master\u2019s application period opened 17 August 2026; results are expected in the week beginning 22 March 2027.'),
              ('Fine print', 'The largest master\u2019s award also reserves a standard room for you, but the room is not free — you pay for accommodation from your living-cost allowance or other funds. Doctoral applicants whose proposed research advances one of the university\u2019s world-leading strategic topics are the ones considered for the World-Leading Doctoral Scholarships.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of St Andrews</strong>, Scotland\u2019s oldest university, runs its most prestigious postgraduate funding through <strong>St Leonard\u2019s College</strong>, its postgraduate college. For 2027 entry the scheme is deliberately designed as one door into many rooms: instead of applying separately to a dozen small funds, you submit a single scholarship application and the panel considers you for every award in the scheme you qualify for — including named awards such as the R&amp;A Ransome Scholarship and the Valerie Graeme Smith Scholarship, with more added during the cycle.</p>
      <p>That matters because the two routes are genuinely different in scale. The master\u2019s route is a tiered fee-waiver scheme: most winners get a slice of their tuition, while the top Global Widening Participation tier is effectively a full ride plus a living allowance. The doctoral route is much smaller and much deeper — up to six fully funded PhD places a year, aimed at research the university classes as world-leading.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Master\u2019s route:</strong> hold <strong>Overseas fee status</strong> and an application (or offer) for an eligible full-time taught or research master\u2019s starting in 2027 — one-year taught degrees, one-year research degrees, and some two-year research degrees with a taught first year. Only the first year of a two-year research master\u2019s is funded.</li>
        <li><strong>Doctoral route:</strong> be applying for a <strong>PhD at St Andrews</strong>; you must not already hold a doctorate or be enrolled in a doctoral programme elsewhere. There are no topic limits across the qualifying schools.</li>
        <li>Meet <strong>at least one</strong> of the scheme\u2019s criteria — you do not need to meet all of them. The panel weighs academic excellence, wider achievement, leadership, financial need, disability, minority background and other contextual factors.</li>
        <li>For the doctoral route, research that advances one of the university\u2019s <strong>world-leading strategic topics</strong> is what the World-Leading awards target.</li>
        <li>Course admission comes first: you apply for the degree, then for the scholarship, through the same <strong>My Application</strong> portal.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Global Widening Participation (master\u2019s):</strong> full tuition fees plus <strong>\u00a318,000</strong> towards living costs, plus a reserved standard room (paid for by you, not free).</li>
        <li><strong>Leadership (master\u2019s):</strong> 75% of tuition fees plus up to <strong>\u00a32,000</strong> for approved career-development activities.</li>
        <li><strong>Excellence (master\u2019s):</strong> 25% or 50% of tuition fees.</li>
        <li><strong>World-Leading Doctoral:</strong> up to <strong>6 awards</strong> covering full tuition plus an annual stipend.</li>
        <li>One application covers many named awards inside the scheme — and any awards added after you apply.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your St Andrews <strong>course application</strong> (submitted first) and any offer you hold.</li>
        <li><strong>Degree certificate</strong> and academic <strong>transcripts</strong>.</li>
        <li>A <strong>CV or r\u00e9sum\u00e9</strong> and a <strong>cover letter / personal statement</strong> setting out your achievements, leadership and any financial need.</li>
        <li>A <strong>research proposal</strong> where your school asks for one for course admission; where it does not, an appropriate personal statement may be used instead.</li>
        <li>A valid <strong>passport</strong> and any other supporting documents the scholarship form requests.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for an <strong>eligible St Andrews postgraduate course</strong> for 2027 entry.</li>
        <li>Open the <strong>St Leonard\u2019s scholarship application</strong> in the My Application portal (the master\u2019s window opened 17 August 2026).</li>
        <li>Complete the single scholarship application — it automatically considers you for the other awards in the scheme.</li>
        <li>Submit by <strong>20 January 2027</strong> (doctoral) or <strong>3 February 2027</strong> (master\u2019s, international students).</li>
        <li>Expect results in the week beginning <strong>22 March 2027</strong> for the master\u2019s route (doctoral results are also expected in late March 2027).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is there one application for all St Andrews postgraduate scholarships?',
  'For the St Leonard\u2019s scheme, yes. You submit one scholarship application through My Application and are automatically considered for the other awards in the scheme, including any added after you apply.'),
 ('What is the biggest master\u2019s award?',
  'The Global Widening Participation award: full tuition fees plus \u00a318,000 towards living costs. Note the reserved standard room that comes with it is not free — you pay for it from your allowance or other funds.'),
 ('Can a two-year research master\u2019s be fully funded?',
  'No. Only the first year of an eligible two-year research master\u2019s is funded under the master\u2019s route.'),
 ('Do I need a separate application for the doctoral scholarships?',
  'The doctoral route has its own deadline (20 January 2027) and is aimed at research advancing the university\u2019s world-leading strategic topics. Apply for your PhD first, then follow the doctoral scholarship route on st-andrews.ac.uk.'),
 ('When will I hear back?',
  'Master\u2019s results are expected in the week beginning 22 March 2027; doctoral results are also expected in late March 2027.')]) + '''
      <p class="verify">Verified 24 Oct 2026: st-andrews.ac.uk/study/scholarships/scholarships-catalogue/postgraduate-scholarships/st-leonards-masters-scholarship-international/ (official) — application period opens 17 Aug 2026, closes 3 Feb 2027, notification week commencing 22 Mar 2027, single application covering many awards, at least one criterion needed, ambassador sharing expectation; daadscholarship.com/ms-phd-scholarships-2027-at-university-of-st-andrews-process-for-international-students/ — master\u2019s tiers 25%/50%/75%/full + \u00a318,000, doctoral up to 6 fully funded awards, stipend reference \u00a320,467 (2026/27), deadlines 3 Feb 2027 master\u2019s / 20 Jan 2027 doctoral, late-March results; pontly.africa/blog/st-leonards-masters-scholarship-international-students-2027-university-of-st-andrews — tier names, September 2027 / January 2028 / August 2027 (MPP) intakes, 3 Feb 2027 deadline; thescholarshipbrief.substack.com/p/study-in-scotland-st-andrews-is-offering — full tuition + \u00a318,000 top tier, 75% + \u00a32,000 leadership tier, 25%/50% excellence tier, one-year funding, reserved room not free.</p>''',
 dl_long='20 January 2027 (doctoral route) and 3 February 2027 (master\u2019s route, international students)',
 offlinks=[('University of St Andrews — St Leonard\u2019s Masters Scholarship, International Students (official)', 'https://www.st-andrews.ac.uk/study/scholarships/scholarships-catalogue/postgraduate-scholarships/st-leonards-masters-scholarship-international/'),
           ('Bright Scholarship — University of St Andrews Postgraduate Scholarships 2027', 'https://brightscholarship.com/university-of-st-andrews-postgraduate-scholarships/')],
 related_titles=['cardiff-vc-2027', 'stirling-vc-2027', 'rgu-vc-2027', 'glos-merit-2027'])),

# ---------------------------------------------------------------- 2. UBC Killam
A.append(dict(
 slug='ubc-killam-fellowship-2027-canada',
 title='UBC Killam Fellowship 2027 in Canada (Funded)',
 meta='UBC Killam Fellowship 2027: the Izaak Walton Killam Memorial Postdoctoral Research Fellowship at the University of British Columbia pays CAD 60,000 a year for up to two years. Department nominations close 6 November 2026 — eligibility, documents, the internal-deadline trap, how to apply and FAQs.',
 short='UBC Killam Fellowship 2027', kicker='Canada · Postdoctoral Fellowship · Funded', mono='UB',
 prov_short='University of British Columbia (UBC)', prov_cat='University · Canada',
 h1='UBC Killam Fellowship 2027 in Canada (Funded)',
 sub='The UBC Killam Fellowship 2027 — formally the Izaak Walton Killam Memorial Postdoctoral Research Fellowship — brings outstanding early-career researchers from around the world to the University of British Columbia for one to two years, on a stipend of CAD 60,000 a year. Four to six new fellowships are awarded each year. The date that matters most is not the one on the poster: UBC departments must lodge their nominations by 6 November 2026 at 4:00 p.m. PT, but applicants apply to departments, and most departmental internal deadlines fall in October — several have already closed.',
 dpill='Dept nominations 6 Nov 2026 · %d days left' % dl_left('2026-11-06'),
 facts=facts([('Award', 'An annual stipend of CAD 60,000 for a maximum of two years (subject to a satisfactory progress review after the first 12 months). Secondary summaries also list a research travel allowance of up to CAD 4,000 over two years — confirm the current figure with your department, as the official page checked leads with the stipend. Four to six new fellowships are awarded each year across both UBC campuses.'),
              ('Eligible', 'You must have completed all requirements of your PhD no more than 24 months before the anticipated fellowship start date (fellowships in this competition must start between 1 May 2027 and 2 January 2028). You must not have pursued PhD-level studies at any UBC campus, and must not currently hold a tenure-track or continuing faculty position (temporary, term or non-tenure-track appointments are fine). You must be able to contribute fresh intellectual insights to UBC and will work under a continuing faculty member with a tenure-track appointment. Career interruptions for childrearing, illness or health-related family responsibilities can extend the 24-month window by up to one year, with justification in a Special Circumstances attachment.'),
              ('How', 'You do not apply to UBC centrally. You apply to your proposed UBC department or academic unit, which vets applications, convenes a review committee, and may forward one nomination (Vancouver campus; Okanagan may forward four in total) to the Killam committee via Graduate and Postdoctoral Studies by 6 November 2026 at 4:00 p.m. PT.'),
              ('Deadline', '6 November 2026 at 4:00 p.m. PT — that is the department/unit nomination deadline, not an applicant deadline. Applicants must meet their proposed department\u2019s internal deadline, typically in October: UBC Okanagan closed 5 October 2026, SPPGA closed 7 October 2026, and Land & Food Systems closed 9 October 2026. If your department\u2019s internal deadline has passed, you cannot be nominated in this cycle.'),
              ('Fine print', 'If you have already started a postdoctoral appointment at UBC, you must provide a rationale for continuing it (in the Special Circumstances document). The fellowship is for most fields of research; each eligible Vancouver department may forward only one nomination, so internal competition is intense.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Killam Postdoctoral Research Fellowships</strong> come from the Izaak Walton Killam Memorial Fund for Advanced Studies, created through the will of Dorothy Johnston Killam in memory of her husband. Their stated purpose is to bring scholars to UBC who are likely to contribute to the advancement of learning or win distinction in a profession — in Dorothy Killam\u2019s words, scholars who are not one-sided, with special distinction of intellect founded on sound character.</p>
      <p>At UBC the fellowship is the university\u2019s flagship postdoctoral award: <strong>CAD 60,000 a year for up to two years</strong>, open across most fields of research, with only <strong>four to six new fellows a year</strong>. That scarcity is why the route matters as much as the money — you are not competing against the world, you are competing to become your department\u2019s single nominee.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Have completed <strong>all requirements of your PhD</strong> (defence, corrections, thesis deposit — not the convocation date) <strong>no more than 24 months</strong> before the anticipated fellowship start date.</li>
        <li>Be able to start between <strong>1 May 2027 and 2 January 2028</strong>.</li>
        <li><strong>Not have pursued PhD-level studies</strong> at any campus of the University of British Columbia.</li>
        <li><strong>Not currently hold</strong> a tenure-track or continuing faculty position; temporary, term or non-tenure-track appointments are eligible.</li>
        <li>Have a proposed supervisor who is a <strong>continuing faculty member with a tenure-track appointment</strong> at UBC.</li>
        <li>Be able to show your work brings <strong>fresh intellectual insights</strong> to UBC and fits the department\u2019s research programmes.</li>
        <li>Career interruptions for <strong>childrearing, illness or health-related family responsibilities</strong> after the PhD can extend the 24-month window by up to one year, with justification in the Special Circumstances attachment.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>CAD 60,000 annual stipend</strong> for up to two years (progress review after year one).</li>
        <li>A research travel allowance is listed in secondary summaries at up to <strong>CAD 4,000 over two years</strong> — confirm it with your department.</li>
        <li>Research across <strong>most fields</strong> at UBC Vancouver or UBC Okanagan, with mentorship from a senior faculty supervisor.</li>
        <li>One of only <strong>4–6 new fellowships</strong> a year — a strong signal on an academic CV.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A completed <strong>application form</strong> (per the department\u2019s nomination guide).</li>
        <li>A <strong>research proposal</strong> showing innovative, ground-breaking work and fit with the department.</li>
        <li>A <strong>curriculum vitae</strong> with publications.</li>
        <li><strong>References</strong> and supporting documents as required by the department.</li>
        <li>A <strong>Special Circumstances</strong> document if you are requesting an eligibility-window extension or justifying a continuing UBC postdoctoral appointment.</li>
        <li>Any additional materials your proposed department specifies.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li><strong>Contact your proposed UBC department or unit immediately</strong> and ask for its internal Killam deadline — this is the deadline that decides whether you can apply at all.</li>
        <li>Line up a <strong>continuing tenure-track faculty supervisor</strong> in that department who will support your nomination.</li>
        <li>Prepare the application package to the department\u2019s nomination guide (proposal, CV, references, Special Circumstances if needed).</li>
        <li>Submit to the department by its internal deadline. The department vets, reviews and may forward <strong>one nomination</strong> (Vancouver) to Graduate and Postdoctoral Studies.</li>
        <li>Department nominations must reach UBC by <strong>6 November 2026 at 4:00 p.m. PT</strong>. Enquiries: killam.fellowships@ubc.ca.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can I apply directly to UBC for the Killam Fellowship?',
  'No. Applicants apply to a UBC department or academic unit; the department nominates. The 6 November 2026 date is the departments\u2019 nomination deadline, and your real deadline is your department\u2019s internal one, typically in October.'),
 ('Is the Okanagan competition still open?',
  'No. The UBC Okanagan applicant deadline was 5 October 2026 at 5:00 p.m. PDT and that competition is now closed. Vancouver departments set their own internal deadlines — check yours at once.'),
 ('Can I apply if I did my PhD at UBC?',
  'No. Applicants must not have pursued PhD-level studies at any campus of the University of British Columbia.'),
 ('How long after my PhD can I apply?',
  'You must have completed all PhD requirements no more than 24 months before the fellowship start date, with up to one extra year for documented career interruptions such as childrearing or illness.'),
 ('How many fellowships are awarded?',
  'Four to six new fellowships a year across UBC, each worth CAD 60,000 a year for up to two years.')]) + '''
      <p class="verify">Verified 24 Oct 2026: postdocs.ubc.ca/award/killam-postdoctoral-research-fellowship (official) — CAD 60,000/year max 2 years, 4–6 new awards, Award Status Open, department/unit nomination deadline 6 Nov 2026 4:00 PM PT, applicants check department internal deadline (typically October), enquiries killam.fellowships@ubc.ca; postdocs.ubc.ca 2027-2028 nomination guide (official PDF) — same 6 Nov 2026 4:00 pm PT deadline, one nomination per Vancouver unit, Okanagan four total; gradstudies.ok.ubc.ca (official) — Okanagan applicant deadline 5 Oct 2026 5:00pm PDT, Award Status Closed, start window 1 May 2027–2 Jan 2028, 24-month rule and extension terms; landfood.ubc.ca (official) — internal LFS deadline 9 Oct 2026; sppga.ubc.ca (official) — SPPGA internal deadline 7 Oct 2026; scholarshiproar.com — CAD 60,000 stipend, CAD 4,000 travel research allowance over two years, no UBC PhD, no tenure-track post.</p>''',
 dl_long='6 November 2026 at 4:00 p.m. PT (department/unit nomination deadline; applicants must meet their department\u2019s earlier internal deadline, typically in October)',
 offlinks=[('UBC Postdoctoral Fellows Office — Killam Postdoctoral Research Fellowship (official)', 'https://www.postdocs.ubc.ca/award/killam-postdoctoral-research-fellowship'),
           ('Bright Scholarship — UBC Killam Fellowship in Canada', 'https://brightscholarship.com/ubc-killam-fellowship-in-canada-funded/')],
 related_titles=['harvard-env-2027', 'neukom-2027', 'elevate-2027', 'hawaii-ewc'])),

# ---------------------------------------------------------------- 3. Sophia
A.append(dict(
 slug='sophia-university-scholarship-2027-japan',
 title='Sophia University Scholarship 2027 in Japan (Funded)',
 meta='Sophia University Scholarship 2027: the New Student Scholarship (one-third, one-half or full first-year tuition) and the Adachi Scholarship (full first-year tuition + education enhancement fee) for English-taught programmes in Tokyo. Next window 11 November–11 December 2026 — eligibility, programmes, how to apply and FAQs.',
 short='Sophia University Scholarship 2027', kicker='Japan · Bachelor\u2019s & Master\u2019s · Funded', mono='SO',
 prov_short='Sophia University', prov_cat='University · Japan',
 h1='Sophia University Scholarship 2027 in Japan (Funded)',
 sub='The Sophia University Scholarship 2027 funds the first year of English-taught undergraduate and graduate study in Tokyo through two awards: the New Student Scholarship, which covers one-third, one-half or all of first-year tuition, and the Adachi Scholarship, which covers full first-year tuition plus the education enhancement fee for international students. Both are awarded at admission-application time to students with excellent grades and genuine financial hardship who have chosen Sophia as their first choice. The next application window runs from 11 November to 11 December 2026.',
 dpill='Next window 11 Dec 2026 · %d days left' % dl_left('2026-12-11'),
 facts=facts([('Award', 'Two awards, both for the first year only. New Student Scholarship (Japanese and international students): one-third, one-half or full tuition fee. Adachi Scholarship, formally the Sophia University Benefactors\u2019 (Adachi) Scholarship (international students only): full tuition fee plus the education enhancement fee. Neither covers living costs, and neither is a cash payment — both are tuition reductions. Once enrolled, you can apply for Sophia\u2019s continuing tuition-reduction programmes for later years.'),
              ('Eligible', 'New students or transfer candidates applying for 2027 entrance to an English-taught undergraduate or graduate programme at Sophia University. You must show excellent academic performance and demonstrated financial hardship, and you must have chosen Sophia University as your first-choice institution. You must meet the entrance and English-language requirements of your programme.'),
              ('How', 'Scholarship applications are accepted at the time of your admission application — there is no separate later scholarship round. Apply for admission to an eligible English-taught programme inside the scholarship application period for your entry term, and the scholarship decision follows the admission process.'),
              ('Deadline', 'Next window: 11 November–11 December 2026 — that is the second application for Spring 2027 undergraduate entry (first-year students) and the first application for Autumn 2027 entry (undergraduate first-year students and SPSF). The following window is 10 March–7 April 2027 (Autumn 2027 second application; graduate Autumn 2027 entry). Graduate Spring 2027 February-examination programmes run 15 December 2026–8 January 2027. Earlier 2027 windows (September 2026) have closed.'),
              ('Fine print', '“Fully funded” in some listings overstates this award: it covers first-year tuition (and, for Adachi, the education enhancement fee) only. Budget separately for the admission fee, housing in Tokyo, living costs and later years\u2019 tuition, and note that scholarship eligibility follows the programme and entry term exactly — check the period for your faculty, not a general deadline.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Sophia University</strong>, a private Jesuit university in central Tokyo founded in 1913, teaches a large share of its international intake in English. Its two entrance scholarships exist for one specific situation: a student with strong grades who has picked Sophia first but would struggle to study there without help. That combination — academic excellence plus financial hardship plus first-choice commitment — is the whole selection test, and it is assessed when you apply for admission, not afterwards.</p>
      <p>Understanding the two awards keeps expectations honest. The <strong>New Student Scholarship</strong> is a sliding tuition cut (one-third, one-half or full) open to Japanese and international students. The <strong>Adachi Scholarship</strong> is the stronger international award: full tuition plus the education enhancement fee for year one. Neither pays rent or living costs in Tokyo, and neither extends beyond the first year on its own — but enrolled students can chase continuing tuition-reduction support for later years.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be applying for <strong>2027 entrance</strong> to an <strong>English-taught undergraduate or graduate programme</strong> at Sophia University, as a new student or a transfer candidate.</li>
        <li>Demonstrate <strong>excellent academic performance</strong> and <strong>financial hardship</strong> — both are required, not either/or.</li>
        <li>Have chosen <strong>Sophia University as your first-choice institution</strong>.</li>
        <li>Meet the <strong>entrance requirements</strong> of your programme, including its <strong>English-language requirements</strong> as an international student.</li>
        <li>Apply inside the <strong>scholarship application period for your programme and entry term</strong> — periods differ by faculty and by spring/autumn entry.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>New Student Scholarship:</strong> one-third, one-half or <strong>full first-year tuition</strong> (Japanese and international students).</li>
        <li><strong>Adachi Scholarship:</strong> <strong>full first-year tuition plus the education enhancement fee</strong> (international students only).</li>
        <li>Awarded at admission time, so you know your first-year tuition position before you commit.</li>
        <li>Continuing <strong>tuition-reduction programmes</strong> are available to apply for once enrolled, for later years.</li>
      </ul>
      <h2 id="eligible-programmes">Eligible programmes</h2>
      <ul>
        <li><strong>Undergraduate:</strong> Faculty of Liberal Arts; Faculty of Science and Technology (Green Science &amp; Engineering courses, including Digital Green Technology); Sophia Program for Sustainable Futures (SPSF).</li>
        <li><strong>Graduate:</strong> Graduate Program in Global Studies; Graduate Program in Global Environment Studies; Green Science/Engineering courses (Graduate School of Science and Technology); Graduate Program in Linguistics (TESOL); Graduate Program in Education; Master\u2019s in International Cooperation Studies.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>admission application</strong> for the eligible English-taught programme (the scholarship is assessed with it).</li>
        <li>Academic <strong>transcripts and certificates</strong> showing excellent performance.</li>
        <li><strong>English-language evidence</strong> meeting your programme\u2019s requirements.</li>
        <li>Evidence of <strong>financial hardship</strong> as the admission/scholarship instructions specify.</li>
        <li>A valid <strong>passport</strong> (international applicants) and any programme-specific documents.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Pick an <strong>eligible English-taught programme</strong> and entry term (spring/April or autumn/September 2027).</li>
        <li>Check the <strong>scholarship application period for your faculty and entry</strong> — the live window is <strong>11 November–11 December 2026</strong> for Spring 2027 undergraduate second applications and Autumn 2027 first applications.</li>
        <li>Submit your <strong>admission application together with the scholarship application</strong> inside that window — the scholarship is not a separate later step.</li>
        <li>If you miss the December window, the next window is <strong>10 March–7 April 2027</strong> for Autumn 2027 entry (second application; graduate Autumn 2027 entry).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Sophia University Scholarship fully funded?',
  'Not in the full sense. The Adachi Scholarship covers full first-year tuition plus the education enhancement fee, and the New Student Scholarship covers one-third, one-half or full first-year tuition. Living costs, housing and later years are not covered.'),
 ('Do I apply for the scholarship separately?',
  'No. Scholarship applications are accepted at the time of your admission application, inside the scholarship application period for your programme and entry term.'),
 ('Which window is live right now?',
  '11 November–11 December 2026: the second application for Spring 2027 undergraduate entry (first-year students) and the first application for Autumn 2027 entry. The next window after that is 10 March–7 April 2027.'),
 ('Can transfer students apply?',
  'Yes. New students and transfer candidates are both eligible, subject to the programme, grades, hardship and first-choice conditions.'),
 ('Do I need Japanese language skills?',
  'These are English-taught programmes, and the published conditions centre on programme entrance and English-language requirements. Check your programme\u2019s own language requirements on sophia.ac.jp.')]) + '''
      <p class="verify">Verified 24 Oct 2026: scholarshipunion.com/sophia-university-scholarship-2027/ — New Student Scholarship 1/3, 1/2 or full first-year tuition, Adachi full tuition + education enhancement fee for international students, excellent grades + financial hardship + first choice, English-taught programmes spring/autumn 2027; medjouel.com/jobs/sophia-university-scholarship-2027-in-japan-fully-funded/ — full window table: UG Spring 2027 second application 11 Nov–11 Dec 2026, UG Autumn 2027 first application 11 Nov–11 Dec 2026, UG Autumn 2027 second application 10 Mar–7 Apr 2027, graduate Autumn 2027 10 Mar–7 Apr 2027, graduate Spring Feb exam 15 Dec 2026–8 Jan 2027, earlier September 2026 windows closed; ajiraforum.com/sophia-university-scholarship-2027-in-japan-funded-study-opportunity-for-international-students/ — same award split, programme lists, window dates; youthexpat.com/2026/09/07/sophia-university-undergraduate-graduate-scholarship-programs-2027/ — scholarship applications accepted at admission-application time, first-choice + hardship + excellent grades conditions.</p>''',
 dl_long='11 December 2026 (application window 11 November–11 December 2026; next window 10 March–7 April 2027)',
 offlinks=[('Sophia University — Scholarships for International Students (official site)', 'https://www.sophia.ac.jp/'),
           ('Bright Scholarship — Sophia University Scholarship 2027', 'https://brightscholarship.com/sophia-university-scholarship-2027-in-japan/')],
 related_titles=['apu-adb', 'utokyo-adb-2027', 'hkpfs-2027', 'kaist-grad-2027'])),

# ---------------------------------------------------------------- 4. Loyola
A.append(dict(
 slug='loyola-university-maryland-undergraduate-merit-scholarships-usa',
 title='Undergraduate Merit Scholarships at Loyola University Maryland USA',
 meta='Undergraduate Merit Scholarships at Loyola University Maryland: Presidential $41,000–$45,000, Dean\u2019s $39,000–$40,000 and Loyola $37,000–$38,000 per year for 2027-28, renewable for up to four years. Automatic consideration with your admission application — Early Action 15 November 2026, Regular Decision 15 January 2027.',
 short='Undergraduate Merit Scholarships at Loyola University Maryland', kicker='USA · Undergraduate · Funded', mono='LM',
 prov_short='Loyola University Maryland', prov_cat='University · USA',
 h1='Undergraduate Merit Scholarships at Loyola University Maryland USA',
 sub='Loyola University Maryland\u2019s undergraduate merit scholarships are refreshingly simple: there is no separate scholarship application at all. Every student who completes an application for admission — first-year, transfer and international — is automatically considered, and the award is notified with the admission decision. For the 2027-28 academic year the first-year awards run from $37,000 to $45,000 a year, renewable for up to four years. Apply by Early Action on 15 November 2026 or Regular Decision on 15 January 2027.',
 dpill='Early Action 15 Nov 2026 · %d days left' % dl_left('2026-11-15'),
 facts=facts([('Award', 'First-year merit awards for the 2027-28 academic year: Presidential Scholarship $41,000–$45,000 per year; Dean\u2019s Scholarship $39,000–$40,000 per year; Loyola Scholarship $37,000–$38,000 per year. Transfer students: Loyola Transfer Scholarship $35,000–$41,000 per year. Awards are renewable for up to four academic years (8 semesters) of full-time undergraduate study, provided you stay enrolled full-time (12 credits) with a minimum cumulative GPA of 2.0. Awards apply to tuition charges only, split equally between fall and spring semesters.'),
              ('Eligible', 'All students who apply for undergraduate admission to Loyola University Maryland — first-year, transfer and international students are all explicitly eligible for merit-based scholarships on the university\u2019s own financial-aid page. First-year awards are based on GPA, course selection and test scores if submitted (Loyola is test-optional: SAT/ACT scores are not required but are reviewed if provided). Transfer awards are competitive, based on strong academic records.'),
              ('How', 'No separate application: complete your application for admission to Loyola University Maryland and you are automatically considered for merit scholarship funding; you are notified of your award at the time of admission.'),
              ('Deadline', 'Early Action: 15 November 2026. Regular Decision: 15 January 2027. (Knott Scholarships, a separate full-tuition route for the most deserving first-year students, also require applying for admission by 15 January.)'),
              ('Fine print', 'These are partial tuition awards, not full rides — even the top Presidential award leaves a large share of Loyola\u2019s total cost to fund, and room, board and fees are not covered. The separate Knott Scholarships cover full tuition for four years but require a 3.0 GPA each semester, an annual Scholar Profile and participation in Knott events; Maguire and Hyman/Empowered Scholars routes are restricted to specific schools or majors and, for Maguire, FAFSA-based need.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>Loyola University Maryland</strong> is a Jesuit liberal-arts university in Baltimore. Its merit scholarships work differently from most of the awards on this site: instead of a scholarship form, an essay contest or a nomination, the university simply reads your admission application and attaches a merit award to your offer. The official financial-aid page is explicit that <strong>all students — first-year, transfer and international — are eligible</strong> for merit-based scholarships, and that every student who completes an application for admission is automatically considered.</p>
      <p>The amounts are substantial by US standards — up to $45,000 a year at the Presidential tier — but they are tuition-only and partial. Treat them as a large discount on a private-university bill, not as a full scholarship, and plan the remaining cost (room, board, fees and later years) before you accept.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Apply for <strong>undergraduate admission</strong> to Loyola University Maryland as a first-year or transfer student — <strong>international students are explicitly eligible</strong>.</li>
        <li>First-year awards are based on <strong>GPA, course selection and test scores if submitted</strong>. Loyola is test-optional: SAT/ACT scores are not required for merit consideration but are reviewed if you provide them.</li>
        <li>Transfer awards are made on a <strong>competitive basis</strong> to students with strong academic records.</li>
        <li>To keep an award you must stay enrolled <strong>full-time (12 credits)</strong> with a minimum <strong>cumulative GPA of 2.0</strong>.</li>
        <li>No separate scholarship application, essay or interview is required for the three main first-year tiers or the transfer award.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Presidential Scholarship:</strong> $41,000–$45,000 per year (2027-28).</li>
        <li><strong>Dean\u2019s Scholarship:</strong> $39,000–$40,000 per year (2027-28).</li>
        <li><strong>Loyola Scholarship:</strong> $37,000–$38,000 per year (2027-28).</li>
        <li><strong>Loyola Transfer Scholarship:</strong> $35,000–$41,000 per year (2027-28).</li>
        <li>Renewable for up to <strong>four academic years (8 semesters)</strong> of full-time study, subject to the GPA and enrolment conditions.</li>
        <li>Awarded <strong>with your admission decision</strong> — no waiting for a separate scholarship round.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>application for admission</strong> to Loyola University Maryland (the only application that matters for these awards).</li>
        <li>Secondary-school <strong>transcripts</strong> and records showing GPA and course selection.</li>
        <li><strong>SAT/ACT scores if you choose to submit them</strong> (optional; reviewed if provided).</li>
        <li>For international applicants: the usual admission documents, including <strong>English-language evidence</strong> and a valid <strong>passport</strong> for visa purposes.</li>
        <li>Transfer applicants: <strong>college transcripts</strong> showing a strong academic record.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Submit your <strong>application for admission</strong> to Loyola University Maryland by <strong>Early Action (15 November 2026)</strong> or <strong>Regular Decision (15 January 2027)</strong>.</li>
        <li>Include your transcripts and, if you wish, test scores — these drive the merit decision.</li>
        <li>There is <strong>nothing else to file</strong> for the Presidential, Dean\u2019s, Loyola or Transfer awards: consideration is automatic.</li>
        <li>Your merit award is <strong>notified with your admission decision</strong>.</li>
        <li>If you want the separate <strong>Knott full-tuition scholarships</strong>, note they need an admission application by 15 January plus a Knott application, a 3.0 semester GPA, an annual Scholar Profile and event participation.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Do international students get Loyola merit scholarships?',
  'Yes. Loyola\u2019s own financial-aid page states that all students — first-year, transfer and international — are eligible for merit-based scholarships, with automatic consideration on admission application.'),
 ('Is there a separate scholarship application?',
  'No, not for the Presidential, Dean\u2019s, Loyola or Transfer awards. The only separate routes are named awards such as the Knott Scholarships (full tuition, with its own application and 3.0 GPA condition).'),
 ('Do the awards cover room and board?',
  'No. Merit awards can only be applied toward tuition charges, split equally between fall and spring semesters. Room, board, fees and other costs remain yours.'),
 ('Can I lose the scholarship?',
  'Yes, if you drop below full-time enrolment (12 credits) or below a 2.0 cumulative GPA. The awards are renewable for up to four academic years while you meet those conditions.'),
 ('Is Loyola test-optional for merit awards?',
  'Yes. SAT/ACT scores are not required for merit consideration, but if you submit them they are reviewed as part of the GPA, course-selection and test-score assessment.')]) + '''
      <p class="verify">Verified 24 Oct 2026: loyola.edu/department/financial-aid/undergraduate/programs/scholarships.html (official, read 24 Oct 2026) — "All students (first-year, transfer, and international) are eligible to receive merit-based scholarships, and every student who completes an application for admission is automatically considered", 2027-28 ranges Presidential $41,000–$45,000, Dean\u2019s $39,000–$40,000, Loyola $37,000–$38,000, Transfer $35,000–$41,000, retention full-time 12 credits + CGPA 2.0, tuition-only split fall/spring, Knott full-tuition route with 15 January admission deadline and 3.0 GPA condition; catalogue.loyola.edu (official) — Early Action 15 November, Regular Decision 15 January for first-year international applicants; globalscholarships.com/scholarships/merit-based-scholarships-for-first-year-students/ — same three tiers (older ranges $38,000–$40,000 / $35,000–$36,000 / $30,000–$33,000), automatic consideration, November 15 admission deadline. Official 2027-28 figures used in the article.</p>''',
 dl_long='15 November 2026 (Early Action; Regular Decision 15 January 2027)',
 offlinks=[('Loyola University Maryland — Scholarships, Office of Financial Aid (official)', 'https://www.loyola.edu/department/financial-aid/undergraduate/programs/scholarships.html'),
           ('Bright Scholarship — Undergraduate Merit Scholarships at Loyola University Maryland', 'https://brightscholarship.com/undergraduate-merit-scholarships-at-loyola-university-maryland-usa/')],
 related_titles=['glos-merit-2027', 'rgu-vc-2027', 'cardiff-vc-2027', 'stirling-vc-2027'])),

# ---------------------------------------------------------------- 5. Vechta
A.append(dict(
 slug='university-of-vechta-phd-scholarships-2027-germany',
 title='University of Vechta PhD Scholarships 2027 in Germany (Stipend \u20ac1,650)',
 meta='University of Vechta PhD Scholarships 2027: up to three Hans B\u00f6ckler Foundation doctoral scholarships at the University of Vechta on justice, sustainability and rural transformation, paying \u20ac1,650 a month for up to three years. Deadline 2 November 2026 — eligibility, documents, how to apply and FAQs.',
 short='University of Vechta PhD Scholarships 2027', kicker='Germany · PhD · Funded', mono='UV',
 prov_short='University of Vechta', prov_cat='University · Germany',
 h1='University of Vechta PhD Scholarships 2027 in Germany (Stipend \u20ac1,650)',
 sub='The University of Vechta PhD Scholarships 2027 offer up to three doctoral researchers a fully funded place in the doctoral college on the justice dimensions of sustainability-oriented transformation in rural areas, funded by the Hans B\u00f6ckler Foundation. Winners receive \u20ac1,650 a month for up to three years, with a health-insurance contribution and a possible family allowance on top, and start between June and September 2027. Applications close on 2 November 2026, and you apply through the foundation\u2019s online portal with a ten-page expos\u00e9.',
 dpill='Deadline 2 Nov 2026 · %d days left' % dl_left('2026-11-02'),
 facts=facts([('Award', '\u20ac1,650 per month, made up of a \u20ac1,550 basic stipend plus a \u20ac100 lump sum for research costs. In addition, a health-insurance contribution of up to \u20ac100 per month is paid where applicable, and a family allowance may be paid if applicable. Funding runs for a maximum of three years (extendable in justified cases) and decisions follow BMBF guidelines and Hans B\u00f6ckler Foundation selection criteria.'),
              ('Eligible', 'Doctoral researchers whose planned project fits the doctoral college PK 060 — "Justice Dimensions of Sustainability-Oriented Transformation Processes in Rural Areas" — at the Vechta Institute of Sustainability Transformation in Rural Areas (VISTRA). Relevant fields include sustainability science, geography, social sciences, ethics, economics, psychology and related disciplines. The call summary lists German B2 and English C1 language requirements, with the thesis possible in English — confirm the exact language evidence in the official call. Applicants are expected to contact the college\u2019s professors in advance to discuss their project.'),
              ('How', 'Apply exclusively via the Hans B\u00f6ckler Foundation\u2019s online application portal, with the required documents and an expos\u00e9 (maximum 10 pages) outlining the planned project and classifying it within the doctoral college\u2019s research programme. Promising applicants are supported by the college\u2019s academic leadership in revising the expos\u00e9 to fit the topic and requirements.'),
              ('Deadline', '2 November 2026. Winners are announced in May 2027 and fellowships begin between June and September 2027.'),
              ('Fine print', 'Only up to three scholarships are available, so this is a small, competitive call — the advance discussion with the named professors (Prof. Dr. Jana Zscheischler and Prof. Dr. John Oliver Engler) is part of the published process, not an optional extra. The standard three-year funding period may be extended only in justified cases.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of Vechta</strong>, in Lower Saxony, hosts the <strong>Vechta Institute of Sustainability Transformation in Rural Areas (VISTRA)</strong> and its doctoral college <strong>PK 060</strong>, which asks an unfashionable but important question: when regions transform for sustainability — new energy systems, changing land use, shifting economies — who gains, who loses, and what counts as fair? The college studies those justice dimensions through comparative case studies, with several doctoral projects building one shared theoretical framework.</p>
      <p>The <strong>Hans B\u00f6ckler Foundation</strong>, the scholarship foundation close to the German trade-union movement, funds up to three doctoral scholarships in this college. At \u20ac1,650 a month for up to three years, with health-insurance and possible family support, it is a genuine full doctoral stipend — but with only three places, the fit of your expos\u00e9 to the college\u2019s programme matters as much as your grades.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold (or be about to hold) a degree qualifying you for <strong>doctoral study</strong> in a field relevant to the college — sustainability science, geography, social sciences, ethics, economics, psychology or a related discipline.</li>
        <li>Propose a project that fits the college theme: <strong>justice dimensions of sustainability-oriented transformation processes in rural areas</strong> — social justice, inequality, risk and uncertainty, energy justice, climate action, rural resilience, spatial justice or social inclusion.</li>
        <li>Meet the language expectations in the call summary — <strong>German B2 and English C1</strong>, with the thesis possible in English — and confirm the exact evidence required in the official call.</li>
        <li>Be ready to <strong>contact the college\u2019s professors in advance</strong> (Prof. Dr. Jana Zscheischler and Prof. Dr. John Oliver Engler) to discuss your project before submitting.</li>
        <li>Be able to start between <strong>June and September 2027</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac1,650 per month</strong> (\u20ac1,550 basic stipend + \u20ac100 research-cost lump sum).</li>
        <li><strong>Up to \u20ac100 per month</strong> health-insurance contribution where applicable.</li>
        <li><strong>Family allowance</strong> where applicable.</li>
        <li>Funding for up to <strong>three years</strong> (extendable in justified cases).</li>
        <li>Methodological and thematic workshops, academic supervision, interdisciplinary research and international collaboration inside the VISTRA doctoral college.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>An <strong>expos\u00e9 (maximum 10 pages)</strong> outlining the planned project and classifying it within the doctoral college\u2019s research programme.</li>
        <li>The <strong>required documents</strong> specified in the official call and the Hans B\u00f6ckler Foundation portal (degree certificates, transcripts, CV).</li>
        <li><strong>Language evidence</strong> as the call requires (German B2 and English C1 per the call summary).</li>
        <li>Records of your <strong>advance discussion with the college professors</strong> about your project.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official call and the <strong>PK 060 doctoral college programme</strong> (uni-vechta.de/vistra/promotionskolleg).</li>
        <li><strong>Contact Prof. Dr. Jana Zscheischler and Prof. Dr. John Oliver Engler in advance</strong> to discuss your project — the published process expects this.</li>
        <li>Draft your <strong>expos\u00e9 (max. 10 pages)</strong>, classifying your project within the college\u2019s research programme.</li>
        <li>Submit <strong>exclusively via the Hans B\u00f6ckler Foundation\u2019s online application portal</strong> by <strong>2 November 2026</strong>.</li>
        <li>Promising applicants are supported by the college\u2019s academic leadership in revising the expos\u00e9; winners are announced in <strong>May 2027</strong> and start between <strong>June and September 2027</strong>. Questions on the process: bewerbung@boeckler.de.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How many Vechta PhD scholarships are there?',
  'Up to three, all in the PK 060 doctoral college on justice dimensions of sustainability-oriented transformation in rural areas.'),
 ('What exactly does \u20ac1,650 a month consist of?',
  '\u20ac1,550 basic stipend plus a \u20ac100 lump sum for research costs, with up to \u20ac100 a month towards health insurance where applicable and a possible family allowance.'),
 ('Do I have to write my thesis in German?',
  'No — the call summary lists German B2 and English C1 requirements with the thesis possible in English. Confirm the exact language evidence in the official call.'),
 ('Must I contact the professors before applying?',
  'The published process says to contact Prof. Dr. Jana Zscheischler and Prof. Dr. John Oliver Engler in advance to discuss your project, and promising applicants are then supported in revising their expos\u00e9. Treat it as part of the application.'),
 ('When do the fellowships start?',
  'Between June and September 2027, with winners announced in May 2027. Funding runs for a maximum of three years.')]) + '''
      <p class="verify">Verified 24 Oct 2026: uni-vechta.de official call for applications (PDF, English) — deadline 2 Nov 2026, \u20ac1,650 stipend (\u20ac1,550 + \u20ac100), health insurance up to \u20ac100, family allowance if applicable, max 3 years, fellowships June–September 2027, winners May 2027, expos\u00e9 max 10 pages, apply exclusively via Hans B\u00f6ckler Foundation online portal, contact Profs. Zscheischler and Engler in advance, BMBF guidelines + HBS criteria, bewerbung@boeckler.de; boeckler.de same official call PDF; scholarshipforphd.com/uni-vechta-phd/ — up to 3 scholarships, PK 060 college, Hans B\u00f6ckler funding, \u20ac1,650/month, 2 Nov 2026 deadline, social justice/sustainability/rural themes; gradualin.com/university-of-vechta-phd-scholarship-germany-2027/ — German B2 + English C1, thesis in English possible, May 2027 results, June–September 2027 start, up to 3 years.</p>''',
 dl_long='2 November 2026',
 offlinks=[('University of Vechta — Call for applications for scholarships, PK 060 (official PDF)', 'https://www.uni-vechta.de/fileadmin/user_upload/VISTRA/Stellenangebote/26-11_Promo_Stipendien_pk60_final_engl.pdf'),
           ('Hans B\u00f6ckler Foundation — Call for applications (official PDF)', 'https://www.boeckler.de/data/downloads/Stufoe/Promo_Stipendien_pk60_final_engl.pdf')],
 related_titles=['potsdam-2027', 'neukom-2027', 'harvard-env-2027', 'elevate-2027'])),

for a in A: _split_verify(a)
sizes = {}
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch46_built.json','w'))

class P(html.parser.HTMLParser):
    def error(self, message): raise AssertionError(message)
for a in A:
    pth = OUT / (a['slug'] + '.html')
    assert pth.exists(), a['slug']
    P().feed(pth.read_text())
    txt = pth.read_text()
    assert 'AICTE Pragati' not in txt, a['slug']
    assert 'Lorem' not in txt, a['slug']
    assert '#' not in a['slug']
    assert 'wa.me/919905166009' in txt, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

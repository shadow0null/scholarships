#!/usr/bin/env python3
"""Batch 35, article 7: High Point University Scholarships in the USA.

HONESTY CALLS (22 Oct 2026, Asia/Kolkata):
- Queue title "High Point University Scholarships 2026 in USA (Funded)" was
  stale/misleading. The 2026 intake deadline (15 Nov 2025) is long past. The
  live call on highpoint.edu is the 2026-27 admissions cycle for FALL 2027
  entry (Class of 2031), with the priority Early Action/merit deadline of
  15 November 2026. Article retitled to the 2027 intake.
- NOT "fully funded" as a blanket label: only the top Presidential merit
  candidates can reach full tuition; the published merit band is
  $5,000 - full tuition, with most other awards $500-$5,000/yr. Marketed as
  "(Partially Funded)".
- The $40,000 "Presidential Founders" tiers on one third-party page could
  not be confirmed on highpoint.edu and are NOT repeated (only the
  officially published figures are used: Merit $5,000-full tuition;
  Scout $1,000; Honors $3,000/yr; Fellows $3,000/yr; Performing Arts
  $500-$2,000; Marching Panther $5,000/yr; ROTC tuition+books+$100/mo).
- International students: officially, the admission application IS the
  scholarship application and merit awards are considered for all entering
  freshmen; need-based/local awards (shift_ed, First Generation, alumni)
  are US-citizen/resident oriented. ROTC requires US citizenship. The article
  says exactly this and does not promise awards that are US-only.
- Slug kept as assigned: high-point-university-scholarships-2026-usa.

Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'highpoint': {'mono': 'HPU', 'title': 'High Point University Scholarships 2027 in USA (Partially Funded)',
   'href': 'high-point-university-scholarships-2026-usa.html',
   'dpill': 'Priority deadline 15 Nov 2026 \u00b7 24 days left',
   'award': 'Merit scholarships $5,000/yr up to full tuition; Honors & Fellows $3,000/yr each; Marching Panther $5,000/yr; Performing Arts $500\u2013$2,000; Scout awards $1,000.',
   'elig': 'Entering freshmen (domestic + international) admitted for Fall 2027; outstanding high-school achievement, leadership and citizenship; separate auditions/interviews for talent awards.',
   'tags': [("Bachelor\u2019s", 'blue'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='high-point-university-scholarships-2026-usa',
 title='High Point University Scholarships 2027 in USA (Partially Funded)',
 meta='High Point University Scholarships 2027: merit awards from $5,000/yr up to full tuition for entering freshmen (including international students), plus $3,000/yr Honors and Fellows awards, talent awards, and ROTC. Admission application doubles as the scholarship application. Priority deadline 15 Nov 2026.',
 short='High Point University Scholarships', kicker='USA \u00b7 Bachelor\u2019s \u00b7 Partially Funded', mono='HPU',
 prov_short='High Point University', prov_cat='University \u00b7 USA',
 h1='High Point University Scholarships 2027 in USA (Partially Funded)',
 sub='Merit awards from $5,000 a year up to full tuition for the entering class \u2014 your admission application is automatically your scholarship application, no extra essay needed.',
 dpill='Priority deadline 15 Nov 2026 \u00b7 24 days left',
 facts=facts([('Award', 'Merit scholarships $5,000 per year up to full tuition (highly selective; top candidates are invited to Presidential Scholarship Interview Weekends). Stackable additions: Honors Scholars $3,000/yr, Fellows $3,000/yr, Marching Panther $5,000/yr, Performing Arts $500-$2,000, Scout awards $1,000. ROTC scholarships cover tuition and books plus $100/month.'),
              ('Eligible', 'Entering freshmen admitted to High Point University for Fall 2027 (Class of 2031), domestic and international. Merit awards reward outstanding achievement, good citizenship, strong leadership and exceptional scholarship in high school; SAT/ACT submission is optional (test-optional). Talent awards require audition/interview/recruitment.'),
              ('How', 'No separate scholarship form for merit awards: your undergraduate admission application IS the scholarship application. Honors/Fellows need a supplemental application on PantherPage; performing-arts awards need an audition; marching band needs an interview; athletics need coach recruitment.'),
              ('Deadline', 'Priority deadline 15 November 2026 (Early Action - also the priority date for full merit consideration; decision by 15 Dec 2026). Fellows/Honors: priority 15 January, final 1 March. Regular Decision: 1 February 2027, but merit funds are largely committed earlier.'),
              ('Renewal', 'Most awards are renewable for up to four years (eight semesters) provided students meet the GPA, programme participation and good-standing requirements stated in HPU\'s Financial Planning Policies.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p><strong>High Point University (HPU)</strong>, a private university in High Point, North Carolina (founded 1924), runs its undergraduate scholarships on a refreshingly simple principle: <strong>your admission application is also your scholarship application</strong>. There is no extra essay or separate form for the main merit awards \u2014 the admissions team evaluates every applicant for scholarships as part of the admissions review.</p>
      <p>A word of honesty before you read on: some listing sites market HPU scholarships as \u201cfully funded\u201d for everyone. That is not what the university publishes. The official merit band runs from <strong>$5,000 a year up to full tuition</strong>, and only the very top candidates reach the full-tuition ceiling \u2014 most awards are meaningful partial reductions. This article describes the awards exactly as HPU publishes them.</p>
      <p>The live cycle is the <strong>2026-27 admissions round for Fall 2027 entry</strong> (the Class of 2031). The priority deadline \u2014 and the date for full consideration for all merit awards \u2014 is <strong>15 November 2026</strong>, 24 days from today (22 October 2026).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>entering freshman admitted to High Point University for Fall 2027</strong> \u2014 both US and <strong>international applicants</strong> are evaluated for merit awards.</li>
        <li>Show <strong>outstanding achievement, good citizenship, strong leadership and exceptional scholarship</strong> during high school \u2014 these are HPU\u2019s stated criteria for merit awards.</li>
        <li><strong>SAT/ACT scores are optional</strong> (HPU is test-optional); submitted scores are superscored.</li>
        <li>For <strong>Honors Scholars and Fellows</strong>: submit the supplemental application on PantherPage after your admission application (priority 15 Jan, final 1 Mar).</li>
        <li>For <strong>talent awards</strong>: complete an audition (Theatre, Dance, Music departments), an interview (Marching Panther band), or be recruited by a coach (NCAA Division I athletics).</li>
        <li>For <strong>Scout awards</strong>: hold Eagle Scout rank (Boy Scouts of America) or a Gold Award (Girl Scouts of the USA) and send a copy of your certificate to your admissions counsellor.</li>
        <li>Note honestly: <strong>ROTC scholarships require US citizenship</strong>, and need-based/local awards (shift_ed, First Generation, Alumni Association Merit Scholarships \u2014 the latter also requires FAFSA) are aimed at US students. International applicants should focus on the merit, Fellows, Honors, performing-arts, marching-band and athletic tracks.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Merit scholarships: $5,000 per year up to full tuition.</strong> The top recipients are invited to the <strong>Presidential Scholarship Interview Weekends</strong> in February, where interviews and activities can raise their award. Awarded at three levels and <strong>renewable over four years</strong>.</li>
        <li><strong>Honors Scholars Program: $3,000 per year</strong>, renewable with continued participation.</li>
        <li><strong>Fellows Scholarships: $3,000 per year</strong> across nine discipline-specific fellowship programmes \u2014 this stacks <strong>on top of</strong> the Presidential, Presidential Fellowship or High Point Scholarship.</li>
        <li><strong>Marching Panther Scholarship: $5,000 per year</strong> for wind, drum line, colour guard and majorette performers (requires Band Camp attendance over the summer).</li>
        <li><strong>Performing Arts Scholarships: $500\u2013$2,000</strong> for entering music majors (audition-based, offered by the Theatre, Dance and Music Departments).</li>
        <li><strong>Scout Awards: $1,000</strong> for Eagle Scouts and Gold Award holders.</li>
        <li><strong>ROTC scholarships: full tuition and books, plus $100 per month</strong> for personal expenses (US Army/Air Force; three- or four-year awards).</li>
        <li><strong>Athletic scholarships:</strong> talent-based awards across all varsity sports under NCAA Division I rules (amounts vary).</li>
        <li><strong>Renewable:</strong> most awards run up to four years provided GPA and programme requirements are met.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>The <strong>undergraduate admission application</strong> itself (Common App or HPU application) with the standard admission materials \u2014 this is the only paperwork needed for merit-award consideration.</li>
        <li><strong>Official SAT/ACT scores</strong> (optional under test-optional admissions; HPU superscores).</li>
        <li><strong>PantherPage supplemental application</strong> for the Honors Scholars or any Fellows Programme.</li>
        <li><strong>Copy of Eagle Scout certificate or Gold Award certificate</strong> (Scout awards) \u2014 submitted to your admissions counsellor.</li>
        <li><strong>Audition / interview / recruitment materials</strong> for performing-arts, marching-band and athletic awards (programme-specific).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Submit your admission application</strong>Apply for undergraduate admission to High Point University (via the Common App or HPU\u2019s application) by <strong>15 November 2026</strong>. This application automatically doubles as your scholarship application \u2014 no separate form or extra essay.</li>
        <li><strong>Add supplemental applications</strong>If you want the Honors Scholars Programme or a Fellows Programme, complete the matching application on your PantherPage (priority deadline 15 January).</li>
        <li><strong>Audition or interview for talent awards</strong>Contact the Music/Theatre/Dance departments for auditions, the Marching Band for an interview, or work with a coach for athletics.</li>
        <li><strong>Send Scout certificates</strong>Eagle Scouts and Gold Award holders send a copy of the certificate to their admissions counsellor.</li>
        <li><strong>Interview for top merit tiers</strong>Top merit candidates are invited to the Presidential Scholarship Interview Weekends in February, which can increase their award.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the High Point University scholarship fully funded?',
  'Not for everyone. The published merit band is $5,000 a year up to full tuition \u2014 full tuition goes only to the very top Presidential candidates selected at the interview weekends. Treat it as a strong partial award unless you are at the top of the pool.'),
 ('Do international students qualify?',
  'Yes. Merit scholarships, Honors, Fellows, performing-arts, marching-band and athletic awards are all evaluated from the admission application regardless of nationality. Only US-only tracks (ROTC, need-based/local grants, FAFSA-based awards) are off the table for international applicants.'),
 ('Is there a separate scholarship application?',
  'No for the main merit awards \u2014 your admission application is the scholarship application. Yes for Honors/Fellows (a PantherPage supplement), performing arts (audition), marching band (interview) and athletics (coach recruitment).'),
 ('What is the deadline?',
  '15 November 2026 is the priority Early Action deadline and the date HPU gives for full consideration for all merit awards (decisions by 15 December 2026). Honors/Fellows run to a priority date of 15 January with a final deadline of 1 March. Regular Decision (1 February 2027) is late for merit funding.'),
 ('How do I keep the scholarship?',
  'Awards are typically renewable for up to four years as long as you meet the GPA, programme-participation and good-standing requirements published in HPU\u2019s Financial Planning Policies. Fellows must also meet programme-specific professionalism requirements.'),
 ('Can awards be combined?',
  'Yes \u2014 the Fellows $3,000/yr scholarship is explicitly stated to stack on top of the Presidential, Presidential Fellowship or High Point Scholarship.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official highpoint.edu page "Admissions Scholarships at HPU" (merit band $5,000\u2013full tuition, priority deadline Nov 15, Scout $1,000, Honors $3,000/yr, Fellows $3,000/yr, performing arts $500\u2013$2,000, Marching Panther $5,000/yr, athletics vary, ROTC tuition+books+$100/mo, admission application = scholarship application) and the official highpoint.edu pages "Scholarship Awards Programs" (three Presidential levels, renewable 4 years, interview weekends, test-optional, apply by Nov 15) and "Academic Fellowship Programs & Honors Scholars" ($3,000/yr renewable, stackable, PantherPage application, priority Jan 15 / final Mar 1) plus the official admissions page (Early Action deadline 15 Nov 2026). Corroborated by CollegeData/Peterson's (Nov 15, 2026 deadline; three award levels; $5k\u2013$10k High Point Scholar band) and CollegeDunia (2027-cycle award lineup). Queue title "2026 (Funded)" was stale: the 2026 intake deadline passed on 15 Nov 2025, so the article covers the Fall 2027 cycle and is marketed as Partially Funded, not fully funded. The $40k "Presidential Founders" tier on one third-party page could not be confirmed on highpoint.edu and is omitted. US-only awards (ROTC, need-based/local) are flagged as such; no invented GPA/SAT cut-offs are given \u2014 HPU publishes none for the main awards.</p>
''',
 dl_long='Priority deadline: 15 November 2026 (Early Action - full consideration for all merit awards; 24 days from 22 Oct 2026). Honors/Fellows: priority 15 January, final 1 March. Regular Decision: 1 February 2027 (late for merit funding).',
 offlinks=[('Admissions Scholarships at HPU \u2014 official page', 'https://www.highpoint.edu/admissions/scholarships-and-grants/'),
           ('Scholarship Awards Programs (Presidential) \u2014 official page', 'https://www.highpoint.edu/admissions/tuition-fees/presidential-scholarship-program/'),
           ('Academic Fellowship Programs & Honors Scholars \u2014 official page', 'https://www.highpoint.edu/admissions/academic-fellowship-programs/'),
           ('Undergraduate Admissions \u2014 official page', 'https://www.highpoint.edu/admissions/')],
 related_titles=['dayton-merit', 'ursinus', 'msu-oos', 'uchicago', 'tiffin2027'],
))

import re as _re
def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)

if __name__ == '__main__':
    for a in A: _split_verify(a)
    built = []
    for a in A:
        n = build_article(BASE, OUT, a, CARDS)
        built.append((a['slug'], n))
    class P(html.parser.HTMLParser):
        def error(self, m): raise ValueError(m)
        def __init__(self):
            super().__init__(); self.errs = []
    bad = []
    for slug, _ in built:
        t = OUT.joinpath(slug + '.html').read_text()
        for token in ('AICTE Pragati', 'Lorem', '{{', 'data:image'):
            if token in t: bad.append((slug, 'template leftover / forbidden token: ' + token))
        # flag '#' only when used as a placeholder link (href="#"), not in-page anchors (#about) or CSS hex colors
        for mm in re.finditer(r'href=["\']#["\']', t):
            bad.append((slug, 'suspicious placeholder: ' + mm.group(0)))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

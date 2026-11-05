#!/usr/bin/env python3
"""Batch 35-5 build: DCSE Global Talent Scholarship 2026 (Universitas Gadjah Mada).

Verification: official DCSE scholarship page (dcse.fmipa.ugm.ac.id/en/scholarship/,
"Global Talent Scholarship 2026" call) + official UGM admission post
(admission.ugm.ac.id/2025/09/01/dcse-global-talent-scholarship-2025/) +
agreeing trackers (scholarshipunion, brightscholarship, mucuruzi, scholarshipsfuture)
on documents/steps/coverage.

Honesty calls baked into the article:
- Queue title said "2025 ... (Fully Funded)". The 2025 cycle closed 3 Oct 2025.
  The live official call is the 2026 cycle, and this article is framed on it.
- Fall 2026 intake (Aug-Dec 2026) registration closed 14 Apr 2026; the Spring
  intake (Feb-Jun 2027) application dates are TBA. Deadline is presented as-is.
- NOT marketed as "fully funded": Type A = tuition waiver + IDR 2.5M/month
  living allowance + research support; Type B = tuition waiver + research
  support. Airfare, visa/immigration, health insurance are borne by the student.
- Slug keeps the parent's predefined identifier (dcse-global-talent-scholarship-2025).

Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'dcse-gts': {'mono': 'DCSE', 'title': 'DCSE Global Talent Scholarship 2026 in Indonesia (Funded)',
   'href': 'dcse-global-talent-scholarship-2025.html',
   'dpill': 'Fall intake closed 14 Apr 2026 \u00b7 Spring intake dates TBA',
   'award': 'Full tuition waiver + IDR 2.5M/month living allowance (Type A); tuition + research funding (Type B)',
   'elig': 'Non-Indonesian citizens; bachelor\u2019s (master\u2019s) or master\u2019s (PhD) in CS/electronics; GPA \u22653.25/3.5; IELTS 6 / TOEFL 550.',
   'tags': [('Scholarship', 'blue'), ('Indonesia', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='dcse-global-talent-scholarship-2025',
 title='DCSE Global Talent Scholarship 2026 in Indonesia (Funded)',
 meta='DCSE Global Talent Scholarship 2026: UGM\u2019s Department of Computer Science and Electronics funds international Master\u2019s and PhD research students with a full tuition waiver, IDR 2.5M/month living allowance (Type A) and research support. Fall intake closed 14 Apr 2026; Spring intake dates TBA.',
 short='DCSE Global Talent Scholarship 2026', kicker='Indonesia \u00b7 Master\u2019s/PhD \u00b7 Funded', mono='DCSE',
 prov_short='Department of Computer Science and Electronics (DCSE), Universitas Gadjah Mada', prov_cat='University Department \u00b7 Indonesia',
 h1='DCSE Global Talent Scholarship 2026 in Indonesia (Funded)',
 sub='Research-based Master\u2019s and PhD places at Universitas Gadjah Mada\u2019s Department of Computer Science and Electronics \u2014 tuition waived, a monthly living allowance on the Type A award, and publication support for overseas students.',
 dpill='Fall 2026 intake: registration closed 14 April 2026 \u00b7 Spring intake (Feb\u2013Jun 2027): dates to be announced',
 facts=facts([('Award', 'GTS Type A: full tuition waiver + IDR 2.5 million/month living allowance + research support funding for publication. GTS Type B: full tuition waiver + research support funding. Up to six scholarships per intake.'),
              ('Eligible', 'Non-Indonesian citizens applying from abroad; bachelor\u2019s degree for the Master\u2019s route (max age 35, GPA \u22653.25/4.00) or master\u2019s degree for the doctoral route (max age 40, GPA \u22653.5/4.00) in CS, electronics or instrumentation; ASEAN applicants preferred; TOEFL 550 / IELTS 6 / IBT 70'),
              ('Programmes', 'Master in Computer Science, Master in Artificial Intelligence, Master in Electronics and Instrumentation, and the Doctoral Program in Computer Science \u2014 all by research'),
              ('How', 'Register in UGM\u2019s admission system, set Financial Sponsor to "Scholarship" + "DCSE Global Talent Scholarship 2026", upload the documents, then email the full set to dep-ike.mipa@ugm.ac.id quoting your application number'),
              ('Deadline', 'The 2025 cycle closed 3 Oct 2025. Under the live 2026 call, the Fall intake (Aug\u2013Dec 2026) closed 14 Apr 2026; Spring intake (Feb\u2013Jun 2027) application dates are TBA on the official page.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>DCSE Global Talent Scholarship</strong> is offered by the <strong>Department of Computer Science and Electronics (DCSE)</strong> of <strong>Universitas Gadjah Mada (UGM)</strong> in Yogyakarta, Indonesia, to overseas students who want to pursue a <strong>research-based Master\u2019s or doctoral degree</strong> and can demonstrate financial need. UGM runs a fresh call each year \u2014 the page currently live is the <strong>Global Talent Scholarship 2026</strong> call, and that is what this article covers. The 2025 cycle (deadline 3 October 2025) is closed.</p>
      <p><strong>Up to six scholarships</strong> are awarded per intake across four programmes: the <strong>Master Program in Computer Science</strong>, the <strong>Master Program in Artificial Intelligence</strong>, the <strong>Master Program in Electronics and Instrumentation</strong>, and the <strong>Doctoral Program in Computer Science</strong>. Awards run for 3 semesters for a Master\u2019s and 6 semesters for a doctorate, with one additional semester allowed.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Must hold <strong>citizenship other than Indonesian</strong> and apply <strong>from abroad</strong>. Degrees must be from a registered/official university in the country of origin \u2014 applicants from <strong>ASEAN countries are preferred</strong>, but other nationalities may still apply.</li>
        <li><strong>Master\u2019s route:</strong> hold a bachelor\u2019s degree in computer science, electronics or instrumentation areas with a <strong>minimum GPA of 3.25 out of 4.00</strong> from a reputable university; <strong>maximum age 35</strong>; applicants who already hold a master\u2019s degree are not eligible for this route.</li>
        <li><strong>Doctoral route:</strong> hold a master\u2019s degree in the same fields with a <strong>minimum GPA of 3.5 out of 4.00</strong>; <strong>maximum age 40</strong>; applicants who already hold a doctoral degree are not eligible for this route.</li>
        <li><strong>English proficiency:</strong> TOEFL 550, IELTS 6.0, or IBT 70 (required for applicants from non-English-speaking countries).</li>
        <li>Must present a <strong>research proposal</strong> with a timeline of about <strong>1.5 years for a Master\u2019s</strong> and <strong>3 years for a doctorate</strong>, discussed with a potential supervisor at DCSE UGM.</li>
        <li>In good health (health certificate), <strong>willing to purchase health insurance</strong> for the study duration, and committed to all aspects of the programme upon nomination.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>GTS Type A:</strong> full tuition fee waiver, a <strong>living allowance of IDR 2.5 million per month</strong>, and research support funding for publication.</li>
        <li><strong>GTS Type B:</strong> full tuition fee waiver and research support funding for publication.</li>
        <li>All international students are <strong>exempt from admission fees</strong>.</li>
      </ul>
      <p>Stated plainly, this is <strong>not an all-expenses award</strong>: there is no family allowance, benefits are prorated by the awardee\u2019s actual presence in Indonesia, and the student bears round-trip airfare, health insurance, immigration and visa fees, and other personal costs.</p>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Valid passport</strong> (colour scan of cover and personal-information pages).</li>
        <li><strong>Passport-sized photograph</strong> with a red background.</li>
        <li><strong>Certified degree certificate and academic transcript</strong> (bachelor\u2019s for the Master\u2019s route; master\u2019s for the doctoral route) <strong>in English</strong>.</li>
        <li><strong>English proficiency certificate</strong> (TOEFL/IELTS) for applicants from non-English-speaking countries.</li>
        <li><strong>Curriculum vitae</strong> and a <strong>personal statement / motivation letter</strong>.</li>
        <li><strong>Research proposal</strong>, discussed with a potential DCSE UGM supervisor.</li>
        <li><strong>Financial support statement</strong> and a <strong>good health statement</strong> from a doctor, in English.</li>
        <li><strong>Academic recommendation letter</strong> from professors or potential supervisors (required for the doctoral route).</li>
        <li><strong>Proof of completed registration</strong> in the UGM admission system (admission ID).</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Register online</strong>Create an account in the UGM admission system at admission.ugm.ac.id/registration and select the Master\u2019s or Doctoral programme in the DCSE Global Talent Scholarship track.</li>
        <li><strong>Mark the funding source</strong>In the \u201cStudy Planning in Universitas Gadjah Mada\u201d section, set the <strong>Financial Sponsor</strong> to \u201cScholarship\u201d and enter <strong>\u201cDCSE Global Talent Scholarship 2026\u201d</strong>.</li>
        <li><strong>Upload the documents</strong>Fill in your data and upload every document listed above in good quality. Note that the scholarship application and the admission process are separate procedures \u2014 the admission step must also be completed, and you will need your admission ID.</li>
        <li><strong>Email the package</strong>Send all uploaded documents to <strong>dep-ike.mipa@ugm.ac.id</strong> with the subject <strong>\u201cDCSE Global Talent Scholarship 2026\u201d</strong>, mentioning your application number. Late submissions are not considered.</li>
        <li><strong>Screening and interview</strong>After the deadline, shortlisted applicants go through document screening and an interview; results follow the official intake timeline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the 2025 cycle still open?',
  'No. The 2025 call closed on 3 October 2025. The current live call on the official DCSE page is the Global Talent Scholarship 2026, and this article covers that cycle.'),
 ('Can I still apply for the Fall 2026 intake?',
  'No \u2014 its registration window (1\u201314 April 2026) has closed and results were announced in May 2026 for the August\u2013December 2026 semester. Watch the official page for the Spring intake (Feb\u2013Jun 2027) application dates, which are still TBA.'),
 ('Is this scholarship fully funded?',
  'Not completely. Tuition is fully waived, Type A adds IDR 2.5 million/month plus research support, and admission fees are exempt \u2014 but airfare, visa/immigration fees, health insurance and living costs beyond the allowance are yours to cover.'),
 ('Who may apply?',
  'Non-Indonesian citizens applying from abroad, preferably from ASEAN countries. Master\u2019s applicants need a relevant bachelor\u2019s with GPA \u22653.25/4.00 and must be under 36; doctoral applicants need a relevant master\u2019s with GPA \u22653.5/4.00 and must be 40 or under.'),
 ('What English scores are required?',
  'TOEFL 550, IELTS 6.0, or IBT 70 \u2014 stated for applicants from non-English-speaking countries.'),
 ('Do I need to contact a supervisor first?',
  'The research proposal should be discussed with a potential supervisor in DCSE UGM (the page links the department\u2019s lecturer directory), so yes \u2014 line that up before applying.'),
 ('Does the scholarship cover family members?',
  'No. Every award is for a single person only, and benefits are prorated according to the awardee\u2019s presence in Indonesia.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official DCSE scholarship page (dcse.fmipa.ugm.ac.id/en/scholarship/: the live 2026 call \u2014 up to six awards, Type A/B coverage, master\u2019s/doctoral eligibility, Fall 2026 timeline with 14 Apr 2026 registration deadline, Spring intake dates TBA, email application step) + the official UGM admission announcement for the 2025 call (admission.ugm.ac.id/2025/09/01/dcse-global-talent-scholarship-2025/: programmes, main requirements, English scores, coverage) + agreeing third-party trackers (scholarshipunion, brightscholarship, mucuruzi, scholarshipsfuture) on the document set, steps and coverage terms. The 2025 cycle closed 3 Oct 2025; the article is deliberately framed on the 2026 call with the Fall intake shown as closed and the Spring intake as TBA, and it is not marketed as \u201cfully funded\u201d.</p>
''',
 dl_long='Under the live 2026 call: Fall intake (semester Aug\u2013Dec 2026) \u2014 registration 1\u201314 April 2026, closed. Spring intake (semester Feb\u2013Jun 2027) \u2014 application dates to be announced on the official DCSE page.',
 offlinks=[('Scholarship page \u2014 DCSE, Universitas Gadjah Mada (official)', 'https://dcse.fmipa.ugm.ac.id/en/scholarship/'),
           ('DCSE Global Talent Scholarship 2025 announcement \u2014 UGM Admission (official)', 'https://admission.ugm.ac.id/2025/09/01/dcse-global-talent-scholarship-2025/')],
 related_titles=['singa2027', 'nanyang-2027', 'saitama-mext-2027', 'brunei-2027-28', 'uiii'],
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
        for token in ('AICTE Pragati', 'Lorem'):
            if token in t: bad.append((slug, 'template leftover: ' + token))
        if 'href="#"' in t: bad.append((slug, 'dead anchor'))
        if 'data:image' in t: bad.append((slug, 'embedded data image'))
        if '{{' in t: bad.append((slug, 'unrendered template braces'))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

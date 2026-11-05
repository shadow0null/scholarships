#!/usr/bin/env python3
"""Batch 35, article 1: UIC Barcelona International Excellence Scholarship.

HONESTY CALLS (22 Oct 2026, Asia/Kolkata):
- Queue title "UIC Barcelona University Scholarship 2026 in Spain (Funded)"
  was stale/misleading. The real, officially published scheme is UIC
  Barcelona's "International Excellence Scholarships (International
  students)". The prior (2026) call resolved at the end of May 2026 and is
  closed; the article covers the CURRENT edition, framed for the 2027
  intake, with the academic year stated explicitly.
- NOT "fully funded": the grant covers exactly 20% of tuition fees across
  all years (up to 20% wording on the grants index). Marketed as
  "(Partially Funded)".
- NO single published application deadline. The grant is tied to the
  admission calendar: entrance exam sittings in November, January and
  April; final grant resolution announced at the end of May. Stated as
  such; no date invented.
- Slug kept as assigned: uic-barcelona-university-scholarship-2026.

Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'uic-barcelona': {'mono': 'UIC', 'title': 'UIC Barcelona International Excellence Scholarship 2027 in Spain (Partially Funded)',
   'href': 'uic-barcelona-university-scholarship-2026.html',
   'dpill': 'Exam sittings Nov 2026\u2013Apr 2027 \u00b7 resolution end of May',
   'award': '20% tuition-fee reduction across all years of the bachelor\u2019s degree (except Dentistry/Medicine)',
   'elig': 'International students; average mark of 8 (Spanish scale); pass UIC admission + specific exam; place reserved.',
   'tags': [("Bachelor\u2019s", 'blue'), ('Spain', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='uic-barcelona-university-scholarship-2026',
 title='UIC Barcelona International Excellence Scholarship 2027 in Spain (Partially Funded)',
 meta='UIC Barcelona International Excellence Scholarship 2027: international students get a 20% tuition-fee reduction across all years of a bachelor\u2019s degree (except Dentistry/Medicine). No single published deadline \u2014 the grant follows the admission calendar (exam sittings in Nov, Jan, Apr; decision end of May).',
 short='UIC Barcelona International Excellence Scholarship', kicker='Spain \u00b7 Bachelor\u2019s \u00b7 Partially Funded', mono='UIC',
 prov_short='Universitat Internacional de Catalunya (UIC Barcelona)', prov_cat='University \u00b7 Spain',
 h1='UIC Barcelona International Excellence Scholarship 2027 in Spain (Partially Funded)',
 sub='A 20% tuition-fee reduction across every year of your bachelor\u2019s degree at a private university in Barcelona \u2014 for international students with a strong academic record who pass the UIC entrance exam.',
 dpill='No single published deadline \u00b7 exam sittings Nov 2026\u2013Apr 2027 \u00b7 grant resolution end of May',
 facts=facts([('Award', '20% reduction of the tuition fees across all years of the degree (the grants index states "up to 20%"). Supported by the UIC Barcelona grant fund. Dentistry and Medicine bachelor\u2019s degrees are excluded.'),
              ('Eligible', 'International students admitted to study the entire bachelor\u2019s programme at UIC Barcelona, with an average mark of 8 from the first year of upper secondary education (marks converted to the Spanish system by UIC\u2019s Promotions and Admissions Department), who pass the UIC Barcelona specific entrance exam and have paid to reserve their place'),
              ('How', 'Apply online for admission via the personal admission portal, submit the requested documentation, take the online entrance exam, and qualify for the grant call'),
              ('Deadline', 'No single published deadline \u2014 tied to the admission calendar: three entrance-exam sittings (November, January, April); the final grant resolution is announced at the end of May. Apply early for the 2027 intake.'),
              ('Renewal', 'Pass all subjects each year with an average mark of 7, plus 15 hours per year of departmental tasks assigned by your department')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>International Excellence Scholarships</strong> are UIC Barcelona\u2019s flagship award for <strong>international students</strong>: a <strong>20% reduction of tuition fees across all years</strong> of a bachelor\u2019s degree. The programme is funded by the university\u2019s own grant fund and is aimed at talented students with a clear vocation for one of UIC Barcelona\u2019s degree programmes.</p>
      <p>A word of caution before you read on: some third-party listing sites market this as a \u201cfully funded\u201d scholarship. It is not \u2014 the official university page states a <strong>20% tuition-fee reduction</strong>, not a full ride. This article describes the award exactly as UIC Barcelona publishes it.</p>
      <p>The current edition is open to international students entering for the <strong>2027 intake</strong>; the previous call\u2019s final resolution was announced at the end of May 2026 and is closed.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student</strong> intending to study the <strong>entire bachelor\u2019s degree programme</strong> at UIC Barcelona.</li>
        <li>Hold an <strong>average mark of 8</strong> from the first year of upper secondary education (your marks are converted to the Spanish system by UIC\u2019s Promotions and Admissions Department).</li>
        <li><strong>Pass the UIC Barcelona specific entrance exam</strong> (taken online) and <strong>pass the university admission process</strong>.</li>
        <li>Once admitted, <strong>pay to reserve your place</strong> \u2014 this is a condition for qualifying for the grant.</li>
        <li>Meeting these requirements allows you to enter the call, but <strong>does not guarantee the award</strong> \u2014 the number of grants is limited and the final resolution rests solely with UIC Barcelona.</li>
        <li>Note: the grant <strong>cannot be applied to the bachelor\u2019s degrees in Dentistry and Medicine</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>20% reduction of tuition fees</strong> for every year of the degree programme.</li>
        <li><strong>Renewable annually</strong>: pass all subjects and reach an average mark of 7 to keep it in the following year.</li>
        <li><strong>15 hours per year of departmental tasks</strong> accompany the grant \u2014 these can be concentrated on specific activities or spread through the year.</li>
        <li><strong>No financial requirements</strong> beyond admission: unlike some UIC grants, family income is not a criterion for this call.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Academic certificate</strong> for the school year equivalent to the first year of the baccalaureate (grades are converted to the Spanish system by UIC Barcelona).</li>
        <li>The <strong>documentation requested in the personal admission portal</strong> as part of the online admission application (programme-specific admission documents vary \u2014 check the portal for your degree).</li>
        <li><strong>Payment proof for reserving your place</strong> once admitted.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose an eligible programme</strong>Pick one of the listed bachelor\u2019s degrees \u2014 Audiovisual Communication, Journalism, Advertising and Public Relations, Business Administration and Management, Law, Architecture, Humanities, Nursing, Physiotherapy, Bioengineering, Biomedicine, Psychology or Education. Dentistry and Medicine are excluded.</li>
        <li><strong>Apply for admission</strong>Fill in the online application for admission and submit the requested documentation via the personal admission portal.</li>
        <li><strong>Take the entrance exam</strong>Sit the UIC Barcelona specific exam, which is taken online. Three exam sittings are scheduled: November, January and April.</li>
        <li><strong>Complete admission</strong>Pass the admission process and pay to reserve your place \u2014 this qualifies you for the grant call.</li>
        <li><strong>Await the resolution</strong>The final resolution of the International Grants for Academic Excellence is announced by UIC Barcelona at the end of May.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the UIC Barcelona International Excellence Scholarship fully funded?',
  'No. It covers 20% of the tuition fees across all years of the degree \u2014 a genuine but partial reduction. Third-party sites calling it \u201cfully funded\u201d are overstating the official offer.'),
 ('Which degrees are excluded?',
  'The bachelor\u2019s degrees in Dentistry and Medicine cannot receive this grant. Eligible programmes include Architecture, Law, Business, Nursing, Psychology, Biomedicine and others \u2014 the official list is on the university page.'),
 ('What is the application deadline?',
  'There is no single published deadline. The grant follows the admission calendar: three entrance-exam sittings in November, January and April, with the final resolution announced at the end of May. Apply early in the cycle.'),
 ('Do I need to be fluent in Spanish?',
  'The official grant page does not state a language requirement; language demands come from the degree programme itself, so check the programme you apply to.'),
 ('What happens if I meet all the requirements?',
  'Meeting the academic, exam and admission requirements allows you to enter the call, but the number of grants is limited and awarding is not guaranteed \u2014 the final decision is UIC Barcelona\u2019s alone.'),
 ('How do I renew the grant each year?',
  'Pass all subjects, achieve an average mark of 7, and complete the 15 hours per year of departmental tasks.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official uic.es page "International Excellence Scholarships (International students)" (20% tuition-fee reduction across all years; edition offered to international students; average-of-8 requirement with Spanish-system conversion; UIC specific exam; admission + place reservation; Dentistry/Medicine excluded; eligible degree list; resolution at end of May; renewal: pass all subjects, average 7, 15 hours/year) and the official uic.es "Grants for degrees offered by UIC Barcelona" index ("up to 20%", no financial requirements, documentation: academic certificate, three exam sittings in Nov/Jan/Apr, contact admisiones@uic.es) + corroborating third-party trackers (globalscholarshipshub, scholarshipunion, thetechiest) on the programme details. Queue title "2026" was stale (that call resolved end of May 2026) and "fully funded" was an overstatement \u2014 the article is retitled for the 2027 intake and marketed as Partially Funded. No single application deadline is published; the article states this explicitly instead of inventing one.</p>
''',
 dl_long='No single published deadline \u2014 tied to the admission calendar for the 2027 intake: entrance-exam sittings in November, January and April; final grant resolution announced at the end of May.',
 offlinks=[('International Excellence Scholarships (International students) \u2014 official page', 'http://www.uic.es/en/estudis/beques/international-excellence-scholarships-international-students'),
           ('Grants for degrees offered by UIC Barcelona \u2014 official index', 'https://www.uic.es/en/admissions/grants-financial-aid-and-funding/grants-degrees-offered-uic-barcelona')],
 related_titles=['polimi-2027', 'daad', 'eiffel', 'ceu-hungary', 'aalto'],
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
        for token in ('AICTE Pragati', 'Lorem', '#', '{{', 'data:image'):
            if token in t: bad.append((slug, 'template leftover / forbidden token: ' + token))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

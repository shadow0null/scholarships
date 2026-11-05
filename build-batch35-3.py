#!/usr/bin/env python3
"""Batch 35-3: DAAD Study Scholarships - Postgraduate Studies (Germany).
Queue title 'DAAD International Postgraduate Scholarship 2026 in Germany
(Fully Funded)' is stale in two ways: the source page lists 2025 deadlines,
and the programmes it covers (Architecture / Music / Fine Art, Design,
Visual Communication & Film) all closed their fall 2026 calls (23 Sep,
24 Sep, 15 Oct 2026) per the official DAAD scholarship database and the
German Federal Foreign Office. The article is honestly retitled, states the
calls are closed, does NOT market it as fully funded (DAAD confirms tuition
is not covered), and points readers at the expected Sep/Oct 2027 calls.
Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'daad-pg-2026': {'mono': 'DA', 'title': 'DAAD Study Scholarships \u2013 Postgraduate Studies in Germany (Creative Fields)',
   'href': 'daad-international-postgraduate-scholarship-2026.html',
   'dpill': '15 Oct 2026 \u00b7 fall 2026 call closed',
   'award': '\u20ac992/month stipend + travel, insurance & study allowances + funded German language course',
   'elig': 'Creative-field graduates; degree \u22646 yrs old; \u226415 months prior residence in Germany; country checks apply; portfolio central.',
   'tags': [('Scholarship', 'blue'), ('Germany', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='daad-international-postgraduate-scholarship-2026',
 title='DAAD Study Scholarships \u2013 Postgraduate Studies in Germany (Fine Art, Design, Music & Architecture)',
 meta='DAAD Study Scholarships \u2013 Postgraduate Studies: \u20ac992/month for creative-field graduates doing postgraduate or continuing studies in Germany. Fall 2026 calls (Architecture, Music, Fine Art/Design/Visual Communication/Film) closed; next calls expected Sep\u2013Oct 2027.',
 short='DAAD Postgraduate Study Scholarships (Creative Fields)', kicker='Germany \u00b7 Postgraduate \u00b7 \u20ac992/month', mono='DA',
 prov_short='German Academic Exchange Service (DAAD)', prov_cat='Government \u00b7 Germany',
 h1='DAAD Study Scholarships \u2013 Postgraduate Studies in Germany (Fine Art, Design, Music & Architecture)',
 sub='\u20ac992 a month for creative-field graduates to continue their artistic training in Germany \u2014 the fall 2026 calls have closed; the next round is expected in Sep\u2013Oct 2027.',
 dpill='Fall 2026 calls closed (23 Sep \u2013 15 Oct 2026) \u00b7 next expected Sep\u2013Oct 2027',
 facts=facts([('Award', '\u20ac992/month stipend + travel allowance + one-off study allowance + health, accident and personal liability insurance + possible rent/family subsidies + funded German language course (2, 4 or 6 months). Tuition fees are NOT covered.'),
              ('Eligible', 'Graduates in fine art, design, visual communication, film, music or architecture; first degree not older than 6 years at the deadline; not resided in Germany more than 15 months; programme open only to specified countries \u2014 check the DAAD page for your country'),
              ('What is funded', 'A Master\u2019s/postgraduate degree course (10\u201324 months) OR a one-year complementary course without a final qualification at a state or state-recognised German university'),
              ('How', 'Apply online via the DAAD scholarship portal (scholarship database / funding-guide.de); selection is by DAAD; the portfolio/work samples are the central selection material'),
              ('Deadlines', 'Fall 2026 calls closed: Architecture 23 Sept 2026, Music 24 Sept 2026, Fine Art/Design/Visual Communication/Film 15 Oct 2026. Next calls expected in the same period of 2027 (applications open from 1 Sept each year).')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The German Academic Exchange Service (DAAD) runs <strong>Study Scholarships \u2013 Postgraduate Studies</strong> specifically for <strong>creative disciplines</strong>: fine art, design, visual communication and film, music, and architecture. They let graduates continue their artistic training in Germany \u2014 either through a <strong>Master\u2019s or postgraduate degree course (10 to 24 months)</strong> or a <strong>one-year complementary course</strong> that does not lead to a final qualification.</p>
      <p>An important status note: the <strong>fall 2026 application calls have closed</strong> \u2014 Architecture on 23 September 2026, Music on 24 September 2026, and Fine Art/Design/Visual Communication/Film on 15 October 2026 (all per the official DAAD scholarship database, confirmed by the German Federal Foreign Office\u2019s fall-scholarship listing). If you found pages advertising \u201c2026\u201d deadlines, they are showing the <strong>2025 cycle dates</strong> and are out of date. DAAD updates these deadlines annually in the same period, so the <strong>next call is expected in Sep\u2013Oct 2027</strong>, with applications possible from 1 September each year.</p>
      <p>A second honesty note: third-party sites call this \u201cfully funded\u201d. DAAD itself states the <strong>scholarship does not cover tuition fees</strong> \u2014 it is a generous living-cost package (stipend, insurance, travel, allowances, language course), not a full-fee award.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>first university degree</strong> in the relevant field \u2014 fine art, design, visual communication, film, music or architecture (by the start of the funded programme at the latest).</li>
        <li>The degree should <strong>not be older than 6 years</strong> at the time of the application deadline.</li>
        <li>Must <strong>not have resided in Germany for more than 15 months</strong> prior to the application deadline.</li>
        <li>Funding <strong>cannot be granted for a degree programme that has already started</strong> in Germany.</li>
        <li>The programme is <strong>restricted to specified countries</strong> \u2014 check the DAAD programme page for whether applicants from your country are accepted.</li>
        <li>By the start of the scholarship, you should have <strong>sufficient knowledge of the language of instruction</strong> of the chosen programme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend of \u20ac992</strong> covering basic living costs.</li>
        <li><strong>Travel allowance</strong> for the journey to and from Germany.</li>
        <li><strong>One-off study allowance</strong> for books, materials and study-related costs.</li>
        <li><strong>Health, accident and personal liability insurance</strong> contributions.</li>
        <li><strong>Monthly rent subsidy</strong> and <strong>allowances for accompanying spouses/children</strong> under certain conditions.</li>
        <li><strong>Funded German language course</strong> (2, 4 or 6 months) before the programme where needed, plus payment of TestDaF/DSH exam fees.</li>
        <li>Tuition fees are <strong>not</strong> covered by the scholarship.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>CV</strong> in tabular form.</li>
        <li><strong>Letter of motivation</strong> (up to 3 pages).</li>
        <li><strong>Letter of admission</strong> to the chosen German study programme \u2014 this can be submitted later, before the scholarship-supported programme begins, if it is not available at application time.</li>
        <li><strong>Portfolio / work samples</strong> in your discipline \u2014 the central selection material for these creative-field programmes.</li>
        <li><strong>Language certificate</strong> proving sufficient knowledge of the programme\u2019s language of instruction.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick your programme</strong>Confirm your field matches one of the three calls (Architecture; Music; Fine Art, Design, Visual Communication and Film) and that your country is eligible on the official DAAD page.</li>
        <li><strong>Prepare the portfolio first</strong>For these creative programmes the artistic work samples carry the most weight \u2014 start well before the autumn call.</li>
        <li><strong>Apply via the DAAD portal</strong>Submit the application through the DAAD scholarship database / funding-guide.de portal once the call opens (applications possible from 1 September each year).</li>
        <li><strong>Secure admission</strong>Arrange admission to the German university; the admission letter may be submitted after the scholarship application if unavailable in time.</li>
        <li><strong>Await selection</strong>Selections are made in spring (e.g. Architecture in January, Music in February, Fine Art in April), with funding beginning in autumn 2027 for the last cycle.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this scholarship still open?',
  'No. The fall 2026 calls closed on 23 Sept 2026 (Architecture), 24 Sept 2026 (Music) and 15 Oct 2026 (Fine Art, Design, Visual Communication & Film). The next calls are expected in the same period of 2027.'),
 ('Is it really fully funded?',
  'Not fully. DAAD states the scholarship does not cover tuition fees. What it does cover is generous: \u20ac992/month, travel, a study allowance, insurance, possible rent and family subsidies, and a German language course.'),
 ('Who can apply?',
  'Graduates in the creative fields named above whose first degree is no more than 6 years old at the deadline, who have not lived in Germany for more than 15 months, and who come from a country accepted for the programme.'),
 ('Do I need to be admitted to a German university before I apply?',
  'No. The admission letter can be submitted later \u2014 before the scholarship-supported programme begins \u2014 if it is not available at the time of application.'),
 ('Can it fund a degree I have already started in Germany?',
  'No. Funding for a Master\u2019s or postgraduate programme that has already started in Germany cannot be granted.'),
 ('When will the next call open?',
  'DAAD updates these deadlines at least once a year, in most cases in the same period as the previous year; applications are possible from 1 September each year, so expect the next call around Sep\u2013Oct 2027.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official DAAD scholarship database on daad.de (fall 2026 deadlines: Architecture 23.09.2026, Music 24.09.2026, Fine Art/Design/VC/Film 15.10.2026; selection dates; 6-year degree and 15-month residence rules; applications possible from 1 September each year) + the German Federal Foreign Office\u2019s \u201cFall Scholarships Now Open\u201d listing confirming the same dates + two agreeing trackers (scholarships.af, House of Europe) on the \u20ac992 stipend, allowances, insurance, tuition exclusion, duration (10\u201324 months) and documents (CV, motivation letter, admission letter). The queue title\u2019s \u201c2026\u201d/\u201cFully Funded\u201d framing was downgraded: the fall 2026 calls are closed and DAAD confirms tuition is not covered.</p>
''',
 dl_long='Fall 2026 calls closed \u2014 Architecture 23 Sept 2026, Music 24 Sept 2026, Fine Art/Design/Visual Communication/Film 15 Oct 2026. Next calls expected Sep\u2013Oct 2027 (applications open from 1 Sept each year).',
 offlinks=[('DAAD Scholarship Database (official) \u2014 search the postgraduate studies programmes', 'https://www2.daad.de/deutschland/stipendium/datenbank/en/21148-scholarship-database/?status=&origin=9&subjectGrps=&intention=&daad=1&q=&page=2&target=&back=1'),
           ('German Federal Foreign Office: DAAD Fall Scholarships Now Open (deadline list)', 'https://canada.diplo.de/ca-en/about-us/vancouver/2780968-2780968')],
 related_titles=['daad', 'kas2027', 'ccp-2027', 'dw-2028', 'hanns-seidel'],
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
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

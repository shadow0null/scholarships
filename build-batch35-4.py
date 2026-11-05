#!/usr/bin/env python3
"""Batch 35 writer 4: Leiden University Mandela Scholarship Fund (batch 35,
22 Oct 2026). Queue title said "2026" but both 2026-cycle deadlines have
closed; the fund runs on a fixed twice-yearly pattern, so this article is
framed for the live next window (September 2027 intake, 1 April 2027) and
retitled to 2027. NOT marketed as fully funded: official page lists only a
monthly living allowance + insurance.
Run from /home/hatch/workspace/scholarships-17k/."""
import json, pathlib, html.parser, re
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'leiden-mandela': {'mono': 'L', 'title': 'Leiden University Mandela Scholarship Fund 2027 (Netherlands Exchange)',
   'href': 'leiden-university-mandela-scholarship-2026.html',
   'dpill': '1 Apr 2027 \u00b7 161 days to go',
   'award': '\u20ac625\u2013\u20ac1,250/month living allowance + Aon student insurance (5 or 10 months)',
   'elig': 'Enrolled at Stellenbosch, UCT, Pretoria or UWC; pre-selected by home university; Leiden exchange admission.',
   'tags': [('Exchange', 'blue'), ('Netherlands', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

A.append(dict(
 slug='leiden-university-mandela-scholarship-2026',
 title='Leiden University Mandela Scholarship Fund 2027 (Netherlands Exchange)',
 meta='Leiden University Mandela Scholarship Fund: a living-stipend exchange scholarship (\u20ac625\u2013\u20ac1,250/month + Aon insurance) for students of Stellenbosch, UCT, Pretoria and UWC to study at Leiden University in the Netherlands. Next deadline: 1 April 2027 (September 2027 intake).',
 short='Leiden Mandela Scholarship Fund 2027', kicker='Netherlands \u00b7 Exchange \u00b7 Partially Funded', mono='L',
 prov_short='Leiden University (Mandela Scholarship Fund)', prov_cat='University \u00b7 Netherlands',
 h1='Leiden University Mandela Scholarship Fund 2027 (Netherlands Exchange)',
 sub='A one- or two-semester exchange at Leiden University for students of four South African partner universities \u2014 a monthly living allowance plus insurance, named for Nelson Mandela.',
 dpill='1 April 2027 \u00b7 161 days to go',
 facts=facts([('Award', 'Monthly living allowance for the exchange: \u20ac1,250/month for students of the University of Cape Town, University of Pretoria and University of the Western Cape; \u20ac625/month for Stellenbosch University students \u2014 plus Aon Student Insurance for the duration (5 or 10 months)'),
              ('Eligible', 'Bachelor\u2019s or Master\u2019s students enrolled at Stellenbosch University, University of Cape Town, University of Pretoria or University of the Western Cape; pre-selected by the home university; meeting Leiden\u2019s exchange/student-abroad admission requirements; open to all nationalities enrolled at those universities'),
              ('Duration', 'One semester (up to 5 months) or two semesters (up to 10 months), depending on the allocation each university uses'),
              ('How', 'Apply to your home university first (it runs its own nomination process), then submit an online application for admission to an exchange/study-abroad course at Leiden University'),
              ('Deadline', 'Leiden\u2019s rolling deadline is 15 October for programmes starting in February and 1 April for programmes starting in September. Next live window: 1 April 2027 (September 2027 intake). Home universities set earlier internal deadlines \u2014 apply through yours well in advance.')]),
 body='''
      <h2 id="about">About the fund</h2>
      <p>The <strong>Mandela Scholarship Fund</strong> at <strong>Leiden University</strong> in the Netherlands supports exchange students from four South African partner universities \u2014 <strong>Stellenbosch University, University of Cape Town, University of Pretoria and the University of the Western Cape</strong> \u2014 who want to spend one or two semesters studying in Leiden. It was founded to mark President Nelson Mandela receiving an <strong>Honorary Doctorate from Leiden University on 12 March 1999</strong>, and the Leiden University Fund (LUF) is the fund\u2019s key sponsor.</p>
      <p>The fund works on a <strong>fixed twice-yearly rhythm</strong>: a 15 October deadline for programmes starting in February, and a 1 April deadline for programmes starting in September. Both 2026-cycle windows have closed, so this guide is written for the <strong>live next window: the September 2027 intake (deadline 1 April 2027)</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Enrolled at one of the four partner universities</strong>: Stellenbosch University, University of Cape Town, University of Pretoria or University of the Western Cape.</li>
        <li><strong>Pre-selected for the scholarship by your home university</strong> \u2014 each university runs its own internal nomination process.</li>
        <li><strong>Meet Leiden University\u2019s admission requirements</strong> for exchange/study-abroad students.</li>
        <li>The official page lists the fund as open to <strong>students of all nationalities</strong> \u2014 the requirement is enrolment at one of the four universities, not South African citizenship.</li>
        <li><strong>Cannot be combined with an Erasmus+ ICM scholarship.</strong></li>
        <li>Eligible fields span Archaeology, Humanities, Medicine/LUMC, Governance and Global Affairs, Law, Social and Behavioural Sciences, Science, ICLON (teacher training), the African Studies Centre and the International Institute for Asian Studies.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>University of Cape Town, University of Pretoria, University of the Western Cape:</strong> one scholarship per university for a two-semester exchange (up to 10 months), OR two scholarships per university for a one-semester exchange (up to 5 months) \u2014 each with a <strong>\u20ac1,250/month living allowance</strong> plus <strong>Aon Student Insurance</strong> for the exchange duration.</li>
        <li><strong>Stellenbosch University:</strong> two scholarships for a two-semester exchange (up to 10 months), OR four scholarships for a one-semester exchange (up to 5 months) \u2014 each with a <strong>\u20ac625/month living allowance</strong> plus <strong>Aon Student Insurance</strong>.</li>
      </ul>
      <p>A plain note on the money: this is <strong>not a fully funded scholarship</strong>. It covers a living allowance and insurance; Leiden\u2019s page does not include airfare, visa fees, orientation costs or housing deposits \u2014 partner-university guidance notes these remain the student\u2019s responsibility, so budget for them before you apply.</p>
      <h2 id="documents">Documents required</h2>
      <p>Leiden University\u2019s official page does <strong>not publish a fixed document checklist</strong> for the fund: the scholarship application goes through your <strong>home university\u2019s exchange office</strong>, and the Leiden application is the standard online exchange-admission form. Each home university sets its own nomination requirements and internal deadline, so the document list varies. Contact your university\u2019s exchange coordinator (contact emails are on the official fund page) to get the current checklist for your intake.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply through your home university</strong>Submit the scholarship application to your own university\u2019s exchange/international office first \u2014 this is where the nomination happens. Check its internal deadline, which is earlier than Leiden\u2019s.</li>
        <li><strong>Apply for exchange admission at Leiden</strong>Submit the online application for admission to an exchange or study-abroad course at Leiden University by <strong>1 April 2027</strong> for the September 2027 start.</li>
        <li><strong>Nomination is sent to Leiden</strong>The four South African universities review all applications and send the names of their selected students to Leiden University\u2019s Scholarships Team.</li>
        <li><strong>Await the outcome</strong>Within two weeks of admission to a Leiden exchange programme, the Scholarships Team notifies the selected candidates with further instructions.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is this really fully funded?',
  'No. The fund pays a monthly living allowance (\u20ac625 or \u20ac1,250 depending on your home university) plus Aon Student Insurance for the exchange period. Airfare, visa fees, orientation and housing-deposit costs are not included, so treat it as a partially funded exchange.'),
 ('Which students can apply?',
  'Bachelor\u2019s and Master\u2019s students enrolled at Stellenbosch University, University of Cape Town, University of Pretoria or the University of the Western Cape, of any nationality, who are pre-selected by their home university.'),
 ('Do I apply to Leiden first or my home university first?',
  'Your home university first \u2014 it runs the nomination process and has its own earlier internal deadline. Leiden\u2019s exchange-admission application comes after nomination.'),
 ('What is the deadline for the 2027 intake?',
  'Leiden\u2019s fixed pattern is 15 October (February start) and 1 April (September start). As of this writing, the next live window is 1 April 2027 for the September 2027 intake.'),
 ('How many scholarships are available?',
  'UCT, UP and UWC each offer either one two-semester or two one-semester scholarships; Stellenbosch offers either two two-semester or four one-semester scholarships.'),
 ('Can I combine it with an Erasmus+ scholarship?',
  'No \u2014 the fund cannot be combined with an Erasmus+ ICM scholarship.'),
]) + '''
      <p class="verify">Verified 22 Oct 2026 via the official Leiden University Mandela Scholarship Fund page (deadline pattern 15 Oct / 1 April, four partner universities, all-nationalities eligibility, pre-selection requirement, Erasmus+ exclusion, \u20ac1,250/\u20ac625 allowance split, Aon insurance, two-step application process, contact persons) + corroborating trackers (afterschoolafrica, scholyhub) on the allowance figures and the 2026-cycle closure + University of Pretoria\u2019s official news on the internal nomination process and student-borne costs. Honesty calls: retitled from the stale \u201c2026\u201d label to the live 2027 window, and the fund is presented as partially funded (living stipend + insurance), not fully funded. The official page publishes no fixed document checklist \u2014 the article says so instead of inventing one.</p>
''',
 dl_long='1 April 2027 \u2014 September 2027 intake (the 15 October 2026 deadline for the February 2027 start has passed; home universities set earlier internal deadlines \u2014 apply through yours first).',
 offlinks=[('Mandela Scholarship Fund \u2014 official page (Leiden University)', 'https://www.universiteitleiden.nl/en/scholarships/sea/mandela-scholarship-fund'),
           ('Leiden University scholarships overview', 'https://www.universiteitleiden.nl/en/scholarships?incoming=incoming')],
 related_titles=['maastricht', 'tue-excellence', 'uva-merit-2027', 'tudelft-excellence-2027', 'tilburg-rm'],
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
        for token in ('AICTE Pragati', 'Lorem', 'data:image', '{{'):
            if token in t: bad.append((slug, 'leftover: ' + token))
        if 'href="#"' in t: bad.append((slug, 'dead anchor'))
        P().feed(t)
    print('validation issues:', bad if bad else 'none')
    for slug, _ in built:
        p = OUT.joinpath(slug + '.html')
        print('size', slug, p.stat().st_size)
    print('--- NEW_CARDS ---')
    print(json.dumps(NEW_CARDS, ensure_ascii=False, indent=1))

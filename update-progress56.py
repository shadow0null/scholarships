#!/usr/bin/env python3
"""Batch 56 queue-progress update (27 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch56.py, items 1-29):
  file-order positions 1-27, PLUS VUW (pos 30) and JSPS (pos 34),
  checked out of strict file order by the parallel verification waves.
  Positions 28 (Brandtech) and 29 (UCLouvain) were NOT scanned this run.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

# unscanned entries in file order
pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 563, len(pending)
assert p['runs'] == 55, p['runs']

# scanned = positions 1..27 + VUW (pos 30) + JSPS (pos 34)
scanned = pending[:27]
vuw = 'Victoria University of Wellington Scholarships 2027 in New Zealand (Funded)'
jsps = '120 JSPS Postdoctoral Fellowship 2027 in Japan (Fully Funded)'
assert pending[29] == vuw, pending[29]
assert pending[33] == jsps, pending[33]
scanned = scanned + [vuw, jsps]
assert len(scanned) == 29, len(scanned)

DONE_TITLES = {
    'Florida State University Scholarships 2027 in USA (Funded)',
    # NOTE: exact queue title carries a literal '| Scholarships Available' suffix
    [t for t in scanned if t.startswith('Shenzhen University Graduate Research Opportunities')][0],
    'Yale University Scholarships 2027 in USA (Fully Funded)',
    jsps,
    vuw,
}
assert DONE_TITLES <= set(scanned), DONE_TITLES - set(scanned)

KPMG = 'KPMG Global Internship Program 2026 (Fully Funded)'
assert KPMG in scanned, 'KPMG missing from scanned list'

REASONS = {
    'KWI Institute Fellowship 2027 in Germany (Fully Funded)':
        'deadline passed (17 Aug 2026)',
    'List of Universities to Study in Ireland Without IELTS 2027':
        'listicle, not a single scheme',
    'Merck International Research Scholarship 2026 in Germany (Funded)':
        'deadline passed (31 Aug 2026)',
    'Top 40 Europe Scholarships for 2027 Without IELTS':
        'listicle, not a single scheme',
    'Bond University HDR Scholarship 2027 in Australia (Fully Funded)':
        'deadline passed (30 Sep 2026)',
    'Zayed University Merit Scholarship 2026 in UAE (Funded)':
        '2026 cycle closed; no open application window verified',
    'US Fulbright Student Program 2027 in USA (Fully Funded)':
        'deadline passed (6 Oct 2026)',
    'PSU Research Internship at CABI-SEA 2026 in Thailand (Fully Funded)':
        'deadline passed (20 Jul 2026)',
    'University of Florence PEGASO Scholarships 2026 (Award €16,243)':
        'deadline passed (6 Aug 2026)',
    'Discover Canada Winter Edition 2026 in Quebec City, Canada | Cultural Exchange Program':
        'deadline passed (30 Aug 2026)',
    'Malaysian International Scholarship MIS 2026 in Malaysia (Fully Funded)':
        'deadline passed (3 Apr 2026)',
    'Ireland Kader Asmal Fellowships 2027 (Fully Funded)':
        'deadline passed (27 Jul 2026)',
    'Max Planck Doucet Scholarship 2027 in Germany (Fully Funded)':
        'deadline passed (15 Sep 2026)',
    'Jiangxi Province Government Scholarship 2027 in China (Funded)':
        'deadline passed (20 Aug 2026)',
    'Climate Tech Fellowship 2026 in USA (Fully Funded)':
        'deadline passed (1 Aug 2026)',
    'IKEA Internship Program 2026 | IKEA Career Opportunities (Paid)':
        'no single verified scheme; IKEA India states it offers no internships',
    'University of Silesia Scholarship 2026-27 in Poland (Funded)':
        'deadline passed (30 Sep 2026)',
    'International Student Festival 2027 in Norway (Fully Funded)':
        'deadline passed (2 Aug 2026)',
    'Charles Darwin University RTP Scholarship 2027 in Australia (Fully Funded)':
        'deadline passed (30 Sep 2026, international)',
    '11 Universities offering Entrance Scholarships in Canada 2027 (Funded)':
        'listicle, not a single scheme',
    'Singapore AI Safety Fellowship 2026 (Fully Funded)':
        'deadline passed (10 Jul 2026)',
    'Yale Emerging Climate Leaders Fellowship 2027 in USA, France (Fully Funded)':
        'deadline passed (30 Jul 2026)',
    'Europe Scholarships for International Students 2027 | Study Free in EU':
        'listicle, not a single scheme',
}
assert set(REASONS) == set(scanned) - DONE_TITLES - {KPMG}, \
    set(REASONS) ^ (set(scanned) - DONE_TITLES - {KPMG})

for t in DONE_TITLES:
    p['done'].append(t)
for t, r in REASONS.items():
    p['skipped'].append({'title': t, 'reason': r})
p['runs'] = 56

json.dump(p, open(QP, 'w'), indent=2, ensure_ascii=False)
print('updated: runs 55 -> 56; done %d -> %d; skipped %d -> %d' % (
    326, len(p['done']), 981, len(p['skipped'])))
print('queue len:', len(q), '| pending after run:',
      len([e for e in q if e['title'] not in set(p['done'])
           and e['title'] not in set(s['title'] for s in p['skipped'])]))

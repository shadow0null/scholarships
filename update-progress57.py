#!/usr/bin/env python3
"""Batch 57 queue-progress update (27 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch57.py, items 1-24):
  file-order pending positions 1..24. Position 23 (HUGO Lab PhD) was
  VERIFIED as a spare but NOT written - it stays pending for the next run.
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
assert len(pending) == 535, len(pending)
assert p['runs'] == 56, p['runs']

scanned = pending[:24]
assert len(scanned) == 24, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0] == 'KPMG Global Internship Program 2026 (Fully Funded)', scanned[0]
assert scanned[3] == 'University Of Idaho Scholarships 2027 in USA (Funded)', scanned[3]
assert scanned[6] == 'Cape Breton University Scholarships 2027 in Canada (Funded)', scanned[6]
assert scanned[14] == 'IEEE USA Government Fellowship Program 2027 (Funding $100,000)', scanned[14]
assert scanned[20] == 'Australian Government Research Scholarship 2026-27 (Fully Funded)', scanned[20]
assert scanned[22].startswith('Two Fully Funded PhD Positions in HUGO Lab'), scanned[22]

DONE_TITLES = {
    scanned[0],
    scanned[3],
    scanned[6],
    scanned[14],
    scanned[20],
}

REASONS = {
    scanned[1]: 'deadline passed (2 Aug 2026)',
    scanned[2]: 'deadline passed (23 Sep 2026)',
    scanned[4]: 'deadline passed (15 Jul 2026)',
    scanned[5]: 'deadline passed (30 Sep 2026)',
    scanned[7]: 'deadline passed (21 Sep 2026)',
    scanned[8]: 'listicle, not a single scheme',
    scanned[9]: 'deadline passed (30 Aug 2026, international EOI; 30 Sep 2026 full application)',
    scanned[10]: 'listicle, not a single scheme',
    scanned[11]: 'deadline passed (26 Jul 2026)',
    scanned[12]: 'deadline passed (12 Oct 2026)',
    scanned[13]: 'deadline passed (17 Sep 2026)',
    scanned[15]: 'deadline passed (9 Jul 2026)',
    scanned[16]: 'deadline passed (31 Jul 2026)',
    scanned[17]: 'deadline passed (31 Jul 2026; some sources 29 Jun 2026)',
    scanned[18]: 'listicle/guide, not a single scheme',
    scanned[19]: 'deadline passed (15 Sep 2026)',
    scanned[21]: 'deadline passed (28 Aug 2026)',
    scanned[23]: 'deadline passed (28 Jun 2026)',
}
assert len(REASONS) == 18, len(REASONS)
assert set(REASONS) | DONE_TITLES == set(scanned) - {scanned[22]}, 'scan coverage mismatch'
assert scanned[22] not in DONE_TITLES and scanned[22] not in REASONS, 'HUGO spare must stay pending'

# nothing already recorded
assert not (DONE_TITLES & done), DONE_TITLES & done
assert not (set(REASONS) & skip), set(REASONS) & skip

for t in scanned:
    if t in DONE_TITLES:
        p['done'].append(t)
    elif t in REASONS:
        p['skipped'].append({'title': t, 'reason': REASONS[t]})
p['runs'] += 1
json.dump(p, open(QP, 'w'), indent=2)
print('runs:', p['runs'], 'done:', len(p['done']), 'skipped:', len(p['skipped']))
print('pending now:', len(q) - len(p['done']) - len(p['skipped']))

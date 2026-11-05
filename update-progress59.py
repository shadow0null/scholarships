#!/usr/bin/env python3
"""Batch 59 queue-progress update (28 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch59.py, items 1-19):
  file-order pending positions 1..19.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 478, len(pending)
assert p['runs'] == 58, p['runs']

scanned = pending[:19]
assert len(scanned) == 19, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0].startswith('Al Qasimi Foundation Scholarships 2026'), scanned[0]
assert scanned[1].startswith('York University Scholarships 2026'), scanned[1]
assert scanned[2].startswith('IUSS Pavia PhD Scholarship 2027'), scanned[2]
assert scanned[5].startswith('Apply for University of Tsukuba MEXT'), scanned[5]
assert scanned[10].startswith('UK Embassy Paid Internships 2026'), scanned[10]
assert scanned[16].startswith('EPFL CYD Fellowship 2027'), scanned[16]
assert scanned[18].startswith('Duke University Karsh Scholarship 2026'), scanned[18]

DONE_TITLES = {
    scanned[0],
    scanned[1],
    scanned[5],
    scanned[16],
    scanned[18],
}

REASONS = {
    scanned[2]: 'deadline passed (16 Jun 2026, 42nd cycle; no later 2027 call published)',
    scanned[3]: 'expired aggregator umbrella label, not a single SNU scheme; last date 9 Jul 2026 passed; no verifiable current open call',
    scanned[4]: 'deadline passed (2026 cohort closed; assessments Jul 2026, programme started Oct 2026); no 2027 call announced; no exact closing date ever published',
    scanned[6]: 'deadline passed (real deadline 12 Jul 2026; queue\'s "January 2027" is wrong)',
    scanned[7]: 'listicle, not a single scheme',
    scanned[8]: 'deadline passed (10 Jul 2026)',
    scanned[9]: 'deadline passed (1 Oct 2026); UiA offers no scholarships for 2027/28',
    scanned[10]: 'rolling family of vacancies, no single scheme or deadline',
    scanned[11]: 'deadline passed (1 Oct 2026, funding from Apr 2027); next round 1 Oct 2027',
    scanned[12]: 'no official source or deadline verifiable — aggregator-only label; deadline not published',
    scanned[13]: 'umbrella label, not a single scheme; every scheme with a published 2026 deadline already closed',
    scanned[14]: 'deadline passed (17 Jun 2026, PBEEE pre-selection); no new call found',
    scanned[15]: 'deadline passed (30 Jun 2026); no 2028 call published',
    scanned[17]: 'deadline passed (31 Jul 2026, WIPO-KDI MIPD Spring 2027 intake); no new call',
}
assert len(REASONS) == 14, len(REASONS)
assert set(REASONS) | DONE_TITLES == set(scanned), 'scan coverage mismatch'

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
done2 = set(p['done']); skip2 = set(s['title'] for s in p['skipped'])
print('pending now:', len([e for e in q if e['title'] not in done2 and e['title'] not in skip2]))

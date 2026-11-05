#!/usr/bin/env python3
"""Batch 60 queue-progress update (28 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch60.py, items 1-34):
  file-order pending positions 1..34.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 459, len(pending)
assert p['runs'] == 59, p['runs']

scanned = pending[:34]
assert len(scanned) == 34, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0].startswith('Alexander Rave Foundation Scholarship 2027'), scanned[0]
assert scanned[2].startswith('Scholarships in Japan 2026'), scanned[2]
assert scanned[6].startswith('IST Austria Scientific Internships 2027'), scanned[6]
assert scanned[12].startswith('Adidas Internships 2026'), scanned[12]
assert scanned[20].startswith('NSP National Scholarship Program 2027'), scanned[20]
assert scanned[27].startswith('University of Miami Bachelors Scholarship 2026'), scanned[27]
assert scanned[33].startswith('University of Pisa Scholarship 2027'), scanned[33]

DONE_TITLES = {
    scanned[6],
    scanned[12],
    scanned[20],
    scanned[27],
    scanned[33],
}

REASONS = {
    scanned[0]: 'deadline passed (30 Jun 2026)',
    scanned[1]: 'deadline passed (31 Aug 2026)',
    scanned[2]: 'listicle, not a single scheme',
    scanned[3]: 'deadline passed (6 Oct 2026, 1:00 PM PT)',
    scanned[4]: 'deadline passed (30 Jun 2026)',
    scanned[5]: 'deadline passed (11 Jun 2026)',
    scanned[7]: 'deadline passed (22 Jun 2026)',
    scanned[8]: 'deadline passed (all constituencies closed, latest USA 7 Oct 2026)',
    scanned[9]: 'aggregator umbrella label, mixes US state of Georgia awards with country Georgia — no single scheme',
    scanned[10]: 'deadline passed (12 Jun 2026)',
    scanned[11]: 'deadline passed (9 Jun 2026, XLII cycle, 104 positions)',
    scanned[13]: 'deadline passed (15 Sep 2026)',
    scanned[14]: 'deadline passed (30 Jun 2026)',
    scanned[15]: 'deadline passed (31 Jul 2026)',
    scanned[16]: 'named 2027 award (Global Sustainability Leaders) closed 3 Sep 2026; other Reading awards are separate schemes',
    scanned[17]: 'listicle, not a single scheme',
    scanned[18]: 'deadline passed (15 Jun 2026)',
    scanned[19]: 'deadline passed (country groups 31 Aug / 3 Sep / 24 Sep / 30 Sep / 21 Oct 2026)',
    scanned[21]: 'deadline passed (6 Jul 2026, 11:59 PM BRT)',
    scanned[22]: 'deadline passed (7 Jun 2026)',
    scanned[23]: 'deadline passed (13 Jun 2026; one source says 16 Jun, either way passed)',
    scanned[24]: 'deadline passed (12 Jun 2026, 2:00 PM Romanian time)',
    scanned[25]: 'listicle, not a single scheme',
    scanned[26]: 'deadline passed (30 Sep 2026; one source says 1 Oct, either way passed)',
    scanned[28]: 'June 2026 window passed (April 2027 intake); November 2026 window for Oct 2027 intake has no published exact date',
    scanned[29]: 'rolling family of vacancies, no single scheme or deadline',
    scanned[30]: 'rolling family of vacancies, no single scheme or deadline',
    scanned[31]: 'listicle, not a single scheme',
    scanned[32]: 'rolling family of vacancies, no single scheme or deadline',
}
assert len(REASONS) == 29, len(REASONS)
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

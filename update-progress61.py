#!/usr/bin/env python3
"""Batch 61 queue-progress update (28 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch61.py, items 1-35):
  file-order pending positions 1..35.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 425, len(pending)
assert p['runs'] == 60, p['runs']

scanned = pending[:35]
assert len(scanned) == 35, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0].startswith('Rowland Fellowships 2027'), scanned[0]
assert scanned[11].startswith('FBI Honors Internships 2027'), scanned[11]
assert scanned[15].startswith('Eric Bleumink Fellowship 2027'), scanned[15]
assert scanned[17].startswith('University of Glasgow Global Leadership'), scanned[17]
assert scanned[18].startswith('600 Graduate Research Scholarships 2027'), scanned[18]
assert scanned[21].startswith('Hokkaido University MEXT Scholarships 2027'), scanned[21]
assert scanned[28].startswith('Boston University Presidential Scholarship 2026'), scanned[28]
assert scanned[34].startswith('UAL International Masters Scholarship 2026'), scanned[34]

DONE_TITLES = {
    scanned[11],
    scanned[17],
    scanned[18],
    scanned[21],
    scanned[28],
}

REASONS = {
    scanned[0]: 'deadline passed (1 Aug 2026)',
    scanned[1]: 'deadline passed (1 Sep 2026)',
    scanned[2]: 'listicle, not a single scheme; underlying MEXT 2026 cycle closed (India deadline 13 May 2026)',
    scanned[3]: '2026 cycle closed (internships ran May-Aug 2026); rolling listings, no single deadline or confirmed 2027 call',
    scanned[4]: 'deadline passed (EMEA cycle closed 11 Oct 2026; US window closed Mar 2026)',
    scanned[5]: 'deadline passed (31 Aug 2026)',
    scanned[6]: 'listicle, not a single scheme',
    scanned[7]: 'deadline passed (1 Oct 2026)',
    scanned[8]: 'listicle, not a single scheme',
    scanned[9]: 'family/umbrella label, no single fully funded scheme (closest single scheme: McGill Major Entrance Scholarships, deadline 21 Jan 2027, partial award — spare for a future run)',
    scanned[10]: 'deadline passed (international round 23 Aug 2026; domestic round 25 Oct 2026)',
    scanned[12]: 'listicle, not a single scheme',
    scanned[13]: 'deadline passed (21 May 2026); other tracks conflict, no single current deadline',
    scanned[14]: 'deadline passed for new students (30 Jun 2026); no official source; award amounts conflict (5,000 vs 10,000 RMB/year)',
    scanned[15]: 'duplicate of already-published Eric Bleumink Scholarship 2027 article (same scheme)',
    scanned[16]: 'family/umbrella label, no single scheme',
    scanned[19]: '2026 cycle closed (Summer 27 Feb 2026; Fall 22 May 2026); next open session Summer 2027, deadline 1 Mar 2027 — spare for a 2027 retitle',
    scanned[20]: 'deadline passed (21 Jun 2026)',
    scanned[22]: 'listicle, not a single scheme',
    scanned[23]: 'rolling programme, no single deadline (per-vacancy deadlines) — verified as spare',
    scanned[24]: 'deadline passed (1 Jun 2026)',
    scanned[25]: 'deadline passed (5 Jun 2026)',
    scanned[26]: 'deadline passed (14 Jun 2026)',
    scanned[27]: 'deadline passed (31 Aug 2026)',
    scanned[29]: 'deadline passed (17 May 2026)',
    scanned[30]: 'listicle, not a single scheme',
    scanned[31]: 'deadline passed (30 Jun 2026)',
    scanned[32]: 'deadline passed (2026 round closed 7 Jun 2026)',
    scanned[33]: '2026 sessions closed (Summer 5 Jan 2026; Fall 6 Apr 2026); next session Summer 2027, deadline 4 Jan 2027, unpaid — spare for a 2027 retitle',
    scanned[34]: '2026 rounds closed (27 Mar / 26 Jun 2026); live official cycle is 2027/28 (23 Mar / 18 May 2027) — spare for a 2027/28 retitle',
}
assert len(REASONS) == 30, len(REASONS)
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

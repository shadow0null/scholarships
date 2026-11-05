#!/usr/bin/env python3
"""Batch 58 queue-progress update (27 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch58.py, items 1-36):
  file-order pending positions 1..36. Positions 25 (Al Qasimi) and 29
  (York PISE) were VERIFIED as spares but NOT written - they stay pending
  for the next run.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 512, len(pending)
assert p['runs'] == 57, p['runs']

scanned = pending[:36]
assert len(scanned) == 36, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0].startswith('Two Fully Funded PhD Positions in HUGO Lab'), scanned[0]
assert scanned[4] == 'TDTU International Graduate Scholarship 2027 in Vietnam (Funded)', scanned[4]
assert scanned[11] == 'The IMPACT Scholarship 2027 at UCL in UK (Funded)', scanned[11]
assert scanned[21] == 'Anthropic Claude Corps Fellowships 2027 (Stipend $85,000)', scanned[21]
assert scanned[22] == 'Fully Funded University of Gottingen DAAD Scholarship 2027 in Germany', scanned[22]
assert scanned[24] == 'Al Qasimi Foundation Scholarships 2026 in UAE (Tuition Fee, Stipend)', scanned[24]
assert scanned[28] == 'York University Scholarships 2026 in Canada (Funded)', scanned[28]

DONE_TITLES = {
    scanned[0],
    scanned[4],
    scanned[11],
    scanned[21],
    scanned[22],
}

REASONS = {
    scanned[1]: 'deadline passed (24 Jul 2026)',
    scanned[2]: 'no deadline published; open status cannot be confirmed (June 2026 listing)',
    scanned[3]: 'deadline passed (24 Jul 2026; later calls also closed, last 22 Oct 2026)',
    scanned[5]: 'deadline passed (31 Jul 2026)',
    scanned[6]: 'deadline conflict unresolvable (queue source says 8 Sep 2026, passed)',
    scanned[7]: 'listicle, not a single scheme',
    scanned[8]: 'deadline passed (20 Jul 2026; second calls also closed, last 2 Sep 2026)',
    scanned[9]: 'titled 2026 but the 1 Nov 2026 deadline is for summer 2027 internships; 2026 cycle closed 1 Nov 2025',
    scanned[10]: 'deadline passed (latest claimed date 11 Jul 2026)',
    scanned[12]: 'deadline passed (8 Sep 2026)',
    scanned[13]: 'listicle/family, not a single scheme',
    scanned[14]: 'deadline passed (19 Aug 2026)',
    scanned[15]: 'listicle, not a single scheme',
    scanned[16]: 'deadline passed (22 Jun 2026); no 2027 call published',
    scanned[17]: 'deadline passed (7 Oct 2026, Spring intake); Fall intake opens 9 Mar 2027',
    scanned[18]: 'deadline passed (14/20 Aug 2026, sources conflict); no 2027 deadline published',
    scanned[19]: 'deadline passed (17 Apr 2026); internship ran 29 Jun-28 Aug 2026',
    scanned[20]: 'deadline passed (30 Jun 2026)',
    scanned[23]: 'deadline passed (3 Jul 2026)',
    scanned[25]: 'deadline passed (16 Oct 2026; Oct 2027 second deadline 9 Apr 2027)',
    scanned[26]: 'deadline passed (Aug 2026); same scheme as Greater Manchester Excellence',
    scanned[27]: 'deadline passed (15 Sep 2026)',
    scanned[29]: 'deadline passed (30 Sep 2026)',
    scanned[30]: 'rolling family of vacancies, no single scheme or deadline',
    scanned[31]: 'deadline passed (all country streams, latest 27 Jul 2026)',
    scanned[32]: 'deadline passed (17 Jun 2026); call closed',
    scanned[33]: 'deadline passed (30 Sep 2026); no single official programme verified',
    scanned[34]: 'listicle, not a single scheme',
    scanned[35]: 'family/listicle; "fully funded" is false for the schemes listed',
}
assert len(REASONS) == 29, len(REASONS)
assert set(REASONS) | DONE_TITLES == set(scanned) - {scanned[24], scanned[28]}, 'scan coverage mismatch'
assert scanned[24] not in DONE_TITLES and scanned[24] not in REASONS, 'Al Qasimi spare must stay pending'
assert scanned[28] not in DONE_TITLES and scanned[28] not in REASONS, 'York PISE spare must stay pending'

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

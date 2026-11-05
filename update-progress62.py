#!/usr/bin/env python3
"""Batch 62 queue-progress update (28 Oct 2026).

Derives exact queue titles from inventory/queue.json itself (file order),
so literal '|' separators and punctuation are preserved verbatim.
Scanned this run (docstring in build-batch62.py, items 1-22):
  file-order pending positions 1..22.
"""
import json

QP = 'inventory/queue-progress.json'
Q = 'inventory/queue.json'

q = json.load(open(Q))
p = json.load(open(QP))
done = set(p['done'])
skip = set(s['title'] for s in p['skipped'])

pending = [e['title'] for e in q if e['title'] not in done and e['title'] not in skip]
assert len(pending) == 390, len(pending)
assert p['runs'] == 61, p['runs']

scanned = pending[:22]
assert len(scanned) == 22, len(scanned)

# spot-check positions so a queue-order drift fails loudly
assert scanned[0].startswith('Wang Gungwu Visiting Fellowship'), scanned[0]
assert scanned[1].startswith('Unilever Future Leaders Programme'), scanned[1]
assert scanned[6].startswith('Islamic University of Madinah'), scanned[6]
assert scanned[15].startswith('ANU International Research Scholarships'), scanned[15]
assert scanned[20].startswith('University of Melbourne Human Rights'), scanned[20]
assert scanned[21].startswith('Heinrich Boll Foundation'), scanned[21]

DONE_TITLES = {
    scanned[1],
    scanned[6],
    scanned[15],
    scanned[20],
    scanned[21],
}

REASONS = {
    scanned[0]: '2027 cycle closed 4 Aug 2026 per the official ISEAS brochure (a later brochure gives 28 Aug 2026 - conflicting); next cycle not announced',
    scanned[2]: 'deadline passed (31 May 2026)',
    scanned[3]: '2027 cycle closed 30 Jun 2026 (official taiwanfellowship.ncl.edu.tw); next cycle opens May 2027',
    scanned[4]: 'deadline passed (31 Aug 2026; "Applications have now closed", bond.edu.au)',
    scanned[5]: 'deadline passed (15 Jun 2026; one source says 31 May 2026, either way passed)',
    scanned[7]: 'deadline passed (12 Jun 2026; official MTCP guidelines)',
    scanned[8]: 'deadline passed (30 Jun 2026; official internshipprogram.go.jp)',
    scanned[9]: 'family/umbrella label, no single scheme; named 2026 awards closed (Future Skills 30 Apr 2026; India PG Chancellor\'s 31 May 2026)',
    scanned[10]: 'deadline passed (5 Jun 2026; official ICETEX call)',
    scanned[11]: 'deadline passed (31 May 2026)',
    scanned[12]: 'listicle, not a single scheme',
    scanned[13]: 'deadline passed (1 Jun 2026; official The Farm Margaret River call)',
    scanned[14]: 'deadline passed (15 Jun 2026)',
    scanned[16]: '42nd cycle closed 31 Aug 2026; next-cycle dates conflicting/not published (30 Jun 2027 vs 25 May 2026 vs "not specified")',
    scanned[17]: 'deadline passed (31 May 2026; nato.int: "no longer accepting applications in 2026")',
    scanned[18]: '2026 programmes closed (deadlines 10 May / 15 May / 10 Jun / 12 Jun 2026); queue title is a guide to several separate summer schools, not one scheme',
    scanned[19]: 'deadline passed (28 Jun 2026; SSRC)',
}
assert len(REASONS) == 17, len(REASONS)
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

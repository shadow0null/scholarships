#!/usr/bin/env python3
"""Scholarships MOBILE fix (5 Nov 2026) - CORPUS-side patch.

Applies, in the corpus (~/workspace/scholarships-17k/), the fixes from the
live mobile-UX check of 5 Nov 2026. Backups of every pre-edit file are in
backups/mobile-fix-2026-11-05/ (taken before this script first ran).

  1. Min-award input bug: `.togrow input{width:20px...}` (meant for the
     Show-closed checkbox) also shrinks the #minAward number input to a
     ~25px sliver. Scope it to input[type="checkbox"] and give #minAward
     min-width:140px. (build-homepage-v9.py NEW_CSS + articles/index.html)
  2. Humboldt: current call capped at 800 applications, no new
     applications creatable; next call opens 15 Nov 2026. dl 2026-11-15
     made the site show "Closes 15 Nov" - an opening date as a deadline.
     Follow the dl-null pattern (cf. Eastman): dl/days -> null,
     closed stays false, dlRaw + verified updated, article file mirrors
     the dl-null shape (data-dl="", JSON-LD applicationDeadline removed,
     meta row "Date not confirmed", alert carries the new dlRaw).
     Verified 5 Nov 2026 against the official Humboldt Foundation page.
  3. Swiss duplicate cards: PhD article (India route) title clarified to
     "... 2027-28 — India" in site-data.json, the homepage DATA block,
     the article file (<title>/h1/JSON-LD name/body) and every related
     card linking to it. The global umbrella article is NOT merged.
  4. Guide TOCs: Canada gains #universities + #alternatives (real h2
     texts) and its "How to apply" label becomes the real h2 text;
     Italy gains #routes. Unilever was verified complete (6/6) - untouched.
  5-7. Detail CSS rules (build-detail-v9.py SD_CSS + template.php
     fallback CSS + every corpus article file, before </style>):
       .facts:has(>.fact:nth-child(6):last-child) -> 3-col grid
       ins.adsbygoogle[data-ad-status="unfilled"]{display:none!important}
       .abody table{display:block;overflow-x:auto;max-width:100%}

NOT touched here (out of scope, see the delivery report): the live
fix-pass D1 gating (corpus article files never received it - that is a
separate corpus/live drift issue, and the reason the deploy zip must NOT
be rebuilt from the corpus yet), test/lovr removal, Super 50 Apply
policy, Vylor whoLine fallback, "Closing soon in India" copy.

Run:  python3 mobile-fix-corpus-2026-11-05.py   (idempotent: re-run exits 0)
"""
import glob
import json
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(ROOT, 'articles')
MARKER = '/* Mobile fix 2026-11-05 */'

NEW_DLRAW_HUMBOLDT = ('Next call opens 15 November 2026 (July 2027 selection; '
                      'earliest start September 2027). Current call closed at '
                      'its 800-application cap \u2014 no new applications can '
                      'be created at present.')
OLD_DLRAW_HUMBOLDT = ('Next call opens 15 November 2026 (July 2027 selection '
                      'meeting; earliest fellowship start September 2027; '
                      'current call closed at its 800-application cap)')
NEW_TITLE_SWISS = ('Swiss Government Excellence Scholarships '
                   '2027\u201328 \u2014 India')
OLD_TITLE_SWISS = 'Swiss Government Excellence Scholarships 2027\u201328'

CSS_RULES = (MARKER + '\n'
             '/* 6-cell fact grids (e.g. Canada guide) wrap in a 5-col grid; '
             '3 cols fits exactly. Exact-6 only: 7/8-cell grids untouched. */\n'
             '.facts:has(>.fact:nth-child(6):last-child)'
             '{grid-template-columns:repeat(3,1fr)}\n'
             '/* Unfilled AdSense slots leave a ~150-200px blank band; hide '
             'only the unfilled ones, AdSense itself stays. */\n'
             'ins.adsbygoogle[data-ad-status="unfilled"]'
             '{display:none!important}\n'
             '/* Bare tables (e.g. Super 50 exam pattern) can overflow narrow '
             'screens; let them scroll instead. Markup untouched. */\n'
             '.abody table{display:block;overflow-x:auto;max-width:100%}\n')

problems = []


def check(path, text, old, expect=1):
    n = text.count(old)
    if n != expect:
        problems.append('%s: expected %dx, found %dx: %.70r'
                        % (path, expect, n, old))
        return False
    return True


def replace(text, old, new, count=1):
    return text.replace(old, new, count) if count == 1 else text.replace(old, new)


def main():
    # ---- 1. build-homepage-v9.py (NEW_CSS, once)
    p = os.path.join(ROOT, 'build-homepage-v9.py')
    t = open(p, encoding='utf-8').read()
    old = '.togrow input{width:20px;height:20px;accent-color:var(--navy)}'
    if check(p, t, old):
        t = t.replace(
            old,
            '.togrow input[type="checkbox"]{width:20px;height:20px;'
            'accent-color:var(--navy)}\n'
            '#minAward{min-width:140px;flex:none}')
        open(p, 'w', encoding='utf-8').write(t)
        print('build-homepage-v9.py: min-award CSS scoped to checkboxes')
    else:
        print('build-homepage-v9.py: anchor mismatch, skipped (see problems)')

    # ---- 2. build-detail-v9.py (SD_CSS, once)
    p = os.path.join(ROOT, 'build-detail-v9.py')
    t = open(p, encoding='utf-8').read()
    old = '.sd-guide-note{margin-top:10px}\n"""'
    if check(p, t, old) and MARKER not in t:
        t = t.replace(old, '.sd-guide-note{margin-top:10px}\n' + CSS_RULES + '"""')
        open(p, 'w', encoding='utf-8').write(t)
        print('build-detail-v9.py: SD_CSS gains the 3 mobile rules')
    elif MARKER in t:
        print('build-detail-v9.py: already patched')
    else:
        print('build-detail-v9.py: anchor mismatch, skipped (see problems)')

    # ---- 3. template.php fallback CSS (v2 tree)
    p = os.path.expanduser(
        '~/workspace/scholarships-admin-panel-v2/admin/lib/template.php')
    t = open(p, encoding='utf-8').read()
    old = (". '.facts{display:grid;gap:12px}.fact{border:1px solid #ddd;"
           "border-radius:12px;padding:12px}'")
    if check(p, t, old) and MARKER not in t:
        add = (". '.facts:has(>.fact:nth-child(6):last-child)"
               "{grid-template-columns:repeat(3,1fr)}'"
               " . 'ins.adsbygoogle[data-ad-status=\"unfilled\"]"
               "{display:none!important}'"
               " . '.abody table{display:block;overflow-x:auto;"
               "max-width:100%}'")
        t = t.replace(old, old + '\n        ' + add)
        open(p, 'w', encoding='utf-8').write(t)
        print('template.php: fallback CSS gains the 3 mobile rules')
    elif MARKER in t:
        print('template.php: already patched')
    else:
        print('template.php: anchor mismatch, skipped (see problems)')

    # ---- 4. site-data.json (Humboldt + Swiss title)
    p = os.path.join(ROOT, 'site-data.json')
    recs = json.load(open(p, encoding='utf-8'))
    by_id = {r['id']: r for r in recs}
    hum = by_id['humboldt-research-fellowship-2026-germany']
    if (hum['dl'], hum['days'], hum['closed'], hum['dlRaw'],
            hum['verified']) == ('2026-11-15', 14, False,
                                 OLD_DLRAW_HUMBOLDT, '29 Oct 2026'):
        hum['dl'] = None
        hum['days'] = None
        hum['closed'] = False
        hum['dlRaw'] = NEW_DLRAW_HUMBOLDT
        hum['verified'] = '5 Nov 2026'
        print('site-data.json: Humboldt -> dl null, verified 5 Nov 2026')
    elif (hum['dl'], hum['days'], hum['dlRaw'], hum['verified']) == (
            None, None, NEW_DLRAW_HUMBOLDT, '5 Nov 2026'):
        print('site-data.json: Humboldt already patched')
    else:
        problems.append('site-data.json: Humboldt record unexpected: %r'
                        % ((hum['dl'], hum['days'], hum['dlRaw'],
                            hum['verified']),))
    sw = by_id['swiss-government-excellence-phd-scholarships-2027-28']
    if sw['title'] == OLD_TITLE_SWISS:
        sw['title'] = NEW_TITLE_SWISS
        print('site-data.json: Swiss PhD title -> "%s"' % NEW_TITLE_SWISS)
    elif sw['title'] == NEW_TITLE_SWISS:
        print('site-data.json: Swiss title already patched')
    else:
        problems.append('site-data.json: Swiss title unexpected: %r'
                        % (sw['title'],))
    if not problems:
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(recs, fh, ensure_ascii=False, indent=1)
        # round-trip guard: the file must re-serialise byte-identically
        # apart from the two records we just changed.
        print('site-data.json: written (indent=1, as before)')

    # ---- 5. articles/index.html: homepage CSS + DATA block
    p = os.path.join(ART, 'index.html')
    t = open(p, encoding='utf-8').read()
    old = '.togrow input{width:20px;height:20px;accent-color:var(--navy)}'
    n = t.count(old)
    if n >= 1:
        t = t.replace(
            old,
            '.togrow input[type="checkbox"]{width:20px;height:20px;'
            'accent-color:var(--navy)}')
        print('articles/index.html: scoped %d togrow-input rule(s)' % n)
    else:
        print('articles/index.html: togrow rule already scoped or missing')
    if '#minAward{min-width:140px;flex:none}' not in t:
        if t.count('</style>') != 1:
            problems.append('articles/index.html: </style> count != 1')
        else:
            t = t.replace('</style>',
                          '#minAward{min-width:140px;flex:none}\n</style>', 1)
            print('articles/index.html: #minAward min-width rule added')
    # DATA block
    s = t.find('[{"id":')
    e = t.find('}];</script>', s)
    if s < 0 or e < 0:
        problems.append('articles/index.html: DATA block not found')
    else:
        raw = t[s:e + 2]
        recs = json.loads(raw)
        by_id = {r['id']: r for r in recs}
        hum = by_id['humboldt-research-fellowship-2026-germany']
        if (hum['dl'], hum['days'], hum['dlRaw'], hum['verified']) == (
                '2026-11-15', 14, OLD_DLRAW_HUMBOLDT, '29 Oct 2026'):
            hum['dl'] = None
            hum['days'] = None
            hum['closed'] = False
            hum['dlRaw'] = NEW_DLRAW_HUMBOLDT
            hum['verified'] = '5 Nov 2026'
            print('articles/index.html DATA: Humboldt flipped to dl null')
        sw = by_id['swiss-government-excellence-phd-scholarships-2027-28']
        if sw['title'] == OLD_TITLE_SWISS:
            sw['title'] = NEW_TITLE_SWISS
            print('articles/index.html DATA: Swiss title clarified')
        new_raw = json.dumps(recs, ensure_ascii=False).replace('</', '<\\/')
        t = t[:s] + new_raw + t[e + 2:]
    open(p, 'w', encoding='utf-8').write(t)

    # ---- 6. Humboldt article file
    p = os.path.join(ART, 'humboldt-research-fellowship-2026-germany.html')
    t = open(p, encoding='utf-8').read()
    reps = [
        ('      "applicationDeadline": "2026-11-15",\n', ''),
        ('<span class="sd-status st-open" data-dl="2026-11-15">Closes 15 Nov'
         '</span>',
         '<span class="sd-status st-warn" data-dl="">Date not confirmed'
         '</span>'),
        ('<span class="sd-date">Deadline: 15 Nov</span>',
         '<span class="sd-date">Date not confirmed</span>'),
        ('<div class="meta-row" data-dl="2026-11-15">',
         '<div class="meta-row" data-dl="">'),
        ('<span class="dline">Deadline: 15 Nov</span>',
         '<span class="dline">Date not confirmed</span>'),
        ('<span class="status">Closes 15 Nov</span>',
         '<span class="status">Date not confirmed</span>'),
        ('<h3>Deadline: ' + OLD_DLRAW_HUMBOLDT + '</h3>',
         '<h3>Deadline: ' + NEW_DLRAW_HUMBOLDT + '</h3>'),
        ('<div class="v">Next call opens 15 November 2026 (July 2027 '
         'selection meeting; earliest start September 2027). Current call '
         'closed at its 800-application cap</div>',
         '<div class="v">' + NEW_DLRAW_HUMBOLDT + '</div>'),
        ('Updated 16 Oct 2026', 'Updated 5 Nov 2026'),
        ('Verified 29 Oct 2026 against the Alexander von Humboldt Foundation',
         'Verified 5 Nov 2026 against the Alexander von Humboldt Foundation'),
        ('fetched 29 Oct 2026', 're-checked 5 Nov 2026'),
    ]
    # WhatsApp href: the old dlRaw, URL-encoded, inside the wa.me text.
    old_enc = urllib.parse.quote(OLD_DLRAW_HUMBOLDT, safe='')
    new_enc = urllib.parse.quote(NEW_DLRAW_HUMBOLDT, safe='')
    reps.append((old_enc, new_enc))
    ok = True
    for old, new in reps:
        if not check(p, t, old):
            ok = False
    if ok:
        for old, new in reps:
            t = t.replace(old, new, 1)
        open(p, 'w', encoding='utf-8').write(t)
        print('Humboldt article: dl-null shape applied (%d replacements)'
              % len(reps))
    else:
        print('Humboldt article: SKIPPED, anchor mismatch (see problems)')

    # ---- 7. Swiss PhD article: en-dash title first (5x), then the
    # related-card/hyphen title (which also fixes this file's <title>).
    p = os.path.join(ART,
                     'swiss-government-excellence-phd-scholarships-2027-28.html')
    t = open(p, encoding='utf-8').read()
    if check(p, t, OLD_TITLE_SWISS, 5):
        t = t.replace(OLD_TITLE_SWISS, NEW_TITLE_SWISS)
        print('Swiss PhD article: 5x en-dash title -> India title')
    old2 = 'Swiss Government Excellence PhD Scholarships 2027-28'
    if check(p, t, old2, 1):
        t = t.replace(old2, NEW_TITLE_SWISS, 1)
        print('Swiss PhD article: <title> -> India title')
    open(p, 'w', encoding='utf-8').write(t)

    # ---- 8. Related cards in every other article file (43 occurrences
    # in 42 files incl. the Swiss PhD <title> handled above).
    total = 0
    for f in sorted(glob.glob(os.path.join(ART, '*.html'))):
        base = os.path.basename(f)
        if base in ('index.html',
                    'swiss-government-excellence-phd-scholarships-2027-28.html'):
            continue
        if base.startswith('pilot-'):
            continue
        tt = open(f, encoding='utf-8').read()
        n = tt.count(old2)
        if n:
            tt = tt.replace(old2, NEW_TITLE_SWISS)
            open(f, 'w', encoding='utf-8').write(tt)
            total += n
    print('Related cards: %d Swiss PhD title(s) clarified' % total)

    # ---- 9. Guide TOCs
    p = os.path.join(ART, 'study-in-canada-without-ielts-2026.html')
    t = open(p, encoding='utf-8').read()
    a = '<li><a href="#about">The honest picture</a></li>'
    if check(p, t, a):
        t = t.replace(
            a,
            a + '\n          <li><a href="#universities">Canadian '
            'universities that admit without IELTS (2026)</a></li>\n'
            '          <li><a href="#alternatives">The alternatives, '
            'explained</a></li>')
    b = '<li><a href="#how">How to apply</a></li>'
    if check(p, t, b):
        t = t.replace(b, '<li><a href="#how">How to apply without IELTS'
                         '</a></li>')
    open(p, 'w', encoding='utf-8').write(t)
    print('Canada guide: TOC gains universities + alternatives, '
          'How label fixed')
    p = os.path.join(ART,
                     'how-to-get-fully-funded-scholarships-in-italy-2026-27.html')
    t = open(p, encoding='utf-8').read()
    a = ('<li><a href="#about">The honest picture for 2026-27</a></li>')
    if check(p, t, a):
        t = t.replace(
            a,
            a + '\n          <li><a href="#routes">The 9 verified routes'
            '</a></li>')
        open(p, 'w', encoding='utf-8').write(t)
        print('Italy guide: TOC gains #routes')
    # Unilever verified complete (6 h2s, 6 TOC links) - untouched.
    p = os.path.join(ART, 'unilever-internships-2027-guide.html')
    t = open(p, encoding='utf-8').read()
    h2s = re.findall(r'<h2 id="([^"]+)">', t)
    toc = re.findall(r'<li><a href="#([^"]+)">', t)
    print('Unilever guide: h2s=%s toc=%s (complete, untouched)'
          % (h2s, toc))

    # ---- 10. The 3 CSS rules into every corpus article file.
    n_done = n_skip = 0
    for f in sorted(glob.glob(os.path.join(ART, '*.html'))):
        if os.path.basename(f) == 'index.html':
            continue
        if os.path.basename(f).startswith('pilot-'):
            continue
        tt = open(f, encoding='utf-8').read()
        if MARKER in tt:
            n_skip += 1
            continue
        if tt.count('</style>') != 1:
            problems.append('%s: </style> count != 1' % f)
            continue
        tt = tt.replace('</style>', CSS_RULES + '</style>', 1)
        open(f, 'w', encoding='utf-8').write(tt)
        n_done += 1
    print('Detail CSS rules: %d files patched, %d already had them'
          % (n_done, n_skip))

    if problems:
        print('\nPROBLEMS (%d):' % len(problems))
        for pr in problems:
            print('  - ' + pr)
        sys.exit(1)
    print('\nCorpus patch complete, no anchor problems.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Regenerate the scholarships sitemap from the same file list that
generates the HTML (v9, 2 Nov 2026 spec).

Locs (418 = homepage + 416 articles + privacy page):
  https://scholarships.studydesk.fun/
  https://scholarships.studydesk.fun/<article>.html   (root-style, == canonical)
  https://scholarships.studydesk.fun/privacy.html
Excluded: pilot-*.html drafts, articles/index.html (a homepage copy whose
canonical is the root URL — no separate loc), admin URLs, 404s, anchors.
lastmod: the listing's verified date (YYYY-MM-DD), or the file mtime
capped at today (2026-11-02); never a future date.
Output: articles/sitemap.xml (the bundle builder copies it byte-identical
to the zip root, so both sitemap copies stay identical as the panel's
verify expects). UTF-8, no BOM, valid urlset XML.
"""
import json
import os
import pathlib
import re
import xml.etree.ElementTree as ET
from datetime import date
from xml.sax.saxutils import escape

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'
OUT = ART / 'sitemap.xml'
BASE = 'https://scholarships.studydesk.fun'
TODAY = date(2026, 11, 2)
MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
          'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def parse_verified(s):
    """'30 Oct 2026' -> date, or None when unparseable."""
    m = re.match(r'(\d{1,2}) ([A-Za-z]{3}) (\d{4})', (s or '').strip())
    if not m:
        return None
    d, mon, y = int(m.group(1)), MONTHS.get(m.group(2)), int(m.group(3))
    if not mon:
        return None
    try:
        return date(y, mon, d)
    except ValueError:
        return None


def file_lastmod(path, fallback):
    try:
        d = date.fromtimestamp(os.path.getmtime(path))
    except OSError:
        return fallback
    return min(d, TODAY)


def main():
    sd = json.load(open(ROOT / 'site-data.json', encoding='utf-8'))
    by_file = {r['file']: r for r in sd}
    entries = []
    # Homepage (file mtime, capped at today).
    entries.append((BASE + '/', file_lastmod(ART / 'index.html', TODAY)))
    # Articles, sorted by file (all 416; pilot drafts and index excluded).
    files = sorted(p.name for p in ART.glob('*.html')
                   if p.name != 'index.html'
                   and not p.name.startswith('pilot-'))
    assert len(files) == 416, f'expected 416 articles, found {len(files)}'
    missing = [f for f in files if f not in by_file]
    assert not missing, f'articles without DATA record: {missing}'
    for f in files:
        rec = by_file[f]
        lm = parse_verified(rec.get('verified')) or \
            file_lastmod(ART / f, TODAY)
        lm = min(lm, TODAY)
        entries.append((f'{BASE}/{f}', lm))
    # Privacy page (file mtime, capped at today).
    assert (ROOT / 'privacy.html').exists(), 'privacy.html missing'
    entries.append((BASE + '/privacy.html',
                    file_lastmod(ROOT / 'privacy.html', TODAY)))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lm in entries:
        lines.append('  <url>')
        lines.append(f'    <loc>{escape(loc)}</loc>')
        lines.append(f'    <lastmod>{lm.isoformat()}</lastmod>')
        lines.append('  </url>')
    lines.append('</urlset>')
    data = ('\n'.join(lines) + '\n').encode('utf-8')
    assert not data.startswith(b'\xef\xbb\xbf'), 'BOM must not be written'
    OUT.write_bytes(data)
    # Self-check: parses, 418 locs, all on host, no trailing slash on
    # files, no query strings.
    root = ET.fromstring(data)
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs = [e.text for e in root.findall('s:url/s:loc', ns)]
    assert len(locs) == 418, f'expected 418 locs, got {len(locs)}'
    assert all(u.startswith(BASE + '/') or u == BASE + '/' for u in locs)
    assert all('?' not in u and '#' not in u for u in locs)
    assert all(not (u != BASE + '/' and u.endswith('/')) for u in locs)
    print(f'wrote {OUT} ({len(locs)} locs, {len(data)} bytes)')


if __name__ == '__main__':
    main()

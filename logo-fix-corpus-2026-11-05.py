#!/usr/bin/env python3
"""Logo fix 2026-11-05 — CORPUS patch (one-shot, not idempotent).

Root cause (verified 5 Nov 2026 from actual file sizes):
- 82 DATA records use logos whose smaller side is <48px (36 at 16-20px,
  43 at 21-32px, 3 at 33-47px; 61 distinct files), mostly 16/32px favicons
  displayed at 34px (cards) / 46-64px (mastheads) = upscaled 2-3x = blurry.
- 26 records have aspect ratio >= 2; homepage cards use object-fit:cover
  in a 34px circle, cropping them to a sliver = broken look.
- Detail mastheads ALREADY use object-fit:contain (verified in article CSS),
  so their blur is upscaling only, not cropping.
- 8 tiny logos have a >=68px same-stem sibling on disk; swap those.
- Remaining 53 distinct tiny logos have no bigger version: render the
  monogram letter fallback instead (existing no-logo path). No re-fetching.
- Header StudyDesk logo is fine (192px source, 40x40 display) - untouched.

What this does (backups under backups/logo-fix-2026-11-05/):
1. site-data.json: apply the 8 logo swaps.
2. articles/index.html DATA block: same 8 swaps (DATA block is NOT
   identical to site-data.json for Cologne/BA/Auckland - preserve each
   file's own other values; touch logo values only).
3. build-homepage-v9.py: card .plogo img cover -> contain + white bg +
   3px padding; add TINY_LOGOS const (post-swap, from real file sizes);
   cardHTML skips <img> for tiny logos (monogram letter stays).
4. admin/lib/template.php: TINY_LOGOS array + three-way masthead logo
   block (tiny -> monogram, else img, else monogram); fallback CSS gets a
   contain rule. (Panel CSS is normally copied from an existing article,
   so the fallback is a belt-and-braces case only.)
5. All articles/*.html: masthead + related-card <img> inside .plogo spans:
   swap src for the 8, remove <img> + drop has-logo/dark classes for tiny.
   (Dropping has-logo matters: has-logo forces a white background, which
   would make the white monogram letter invisible.)
6. build-detail-v9.py: NO change needed - detail .plogo img already
   contain + white. (Verified, not assumed.)
7. articles/index.html (homepage copy): patched IN PLACE with the same
   CSS/JS edits as the live script (4x cover rule, TINY_LOGOS insert,
   2x logo guard) - do NOT re-run build-homepage-v9.py to regenerate
   it: the builder appends NEW_CSS on every run and the copy already
   carries it 4x, so a re-run would make it 5x. (Applied 5 Nov via an
   inline patch after this script ran; both inline scripts pass
   node --check.)

Run from ~/workspace/scholarships-17k. Exits non-zero on any anchor miss.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKUP = os.path.join(ROOT, 'backups', 'logo-fix-2026-11-05')

SWAPS = {
    'logos/fav-hanns-seidel.png': 'logos/hanns-seidel.png',
    'logos/fav-hust.png': 'logos/hust.png',
    'logos/fav-icdf.png': 'logos/icdf.png',
    'logos/fav-mota.png': 'logos/mota.png',
    'logos/fav-msje.png': 'logos/msje.png',
    'logos/fav-sakal.png': 'logos/sakal.png',
    'logos/fav-vidyadhan.png': 'logos/vidyadhan.png',
    'logos/fav-wb.png': 'logos/wb.png',
}

from PIL import Image


def post_swap(logo):
    return SWAPS.get(logo, logo)


def compute_tiny(records):
    """Post-swap tiny set from REAL file sizes: min side < 48px."""
    tiny = set()
    for r in records:
        lg = r.get('logo')
        if not lg:
            continue
        lg = post_swap(lg)
        p = os.path.join(ROOT, 'articles', lg)
        w, h = Image.open(p).size
        if min(w, h) < 48:
            tiny.add(lg)
    return tiny


def backup():
    os.makedirs(BACKUP, exist_ok=True)
    for rel in ['site-data.json', 'build-homepage-v9.py',
                'build-detail-v9.py']:
        src = os.path.join(ROOT, rel)
        dst = os.path.join(BACKUP, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    # template.php lives outside the corpus tree
    tpl = os.path.expanduser('~/workspace/scholarships-admin-panel-v2'
                             '/admin/lib/template.php')
    dst = os.path.join(BACKUP, 'template.php.bak')
    shutil.copy2(tpl, dst)
    shutil.copytree(os.path.join(ROOT, 'articles'),
                    os.path.join(BACKUP, 'articles'), dirs_exist_ok=True)
    print('backup ->', BACKUP)


def patch_site_data(tiny):
    path = os.path.join(ROOT, 'site-data.json')
    raw = open(path, encoding='utf-8').read()
    data = json.loads(raw)
    # round-trip check first: dump must reproduce the file (indent=1)
    rt = json.dumps(data, ensure_ascii=False, indent=1)
    if rt != raw.rstrip('\n') and rt + '\n' != raw:
        print('WARN: site-data.json does not round-trip byte-identical;'
              ' refusing to rewrite it blindly')
        print('  raw tail:', repr(raw[-40:]), 'dump tail:', repr(rt[-40:]))
        sys.exit(1)
    n = 0
    for r in data:
        if r.get('logo') in SWAPS:
            r['logo'] = SWAPS[r['logo']]
            n += 1
    out = json.dumps(data, ensure_ascii=False, indent=1)
    if not raw.endswith('\n'):
        open(path, 'w', encoding='utf-8').write(out)
    else:
        open(path, 'w', encoding='utf-8').write(out + '\n')
    print(f'site-data.json: {n} logo swaps')
    return n


def patch_index_data():
    path = os.path.join(ROOT, 'articles', 'index.html')
    s = open(path, encoding='utf-8').read()
    m = re.search(r'(var DATA = \[.*?\]);', s, re.S)
    assert m, 'DATA block not found in articles/index.html'
    block = m.group(1)
    new = block
    n = 0
    for old, newlogo in SWAPS.items():
        old_s = '"logo": "%s"' % old
        cnt = new.count(old_s)
        n += cnt
        new = new.replace(old_s, '"logo": "%s"' % newlogo)
    assert n == 26, f'expected 26 logo swaps in DATA block, got {n}'
    s = s[:m.start(1)] + new + s[m.end(1):]
    open(path, 'w', encoding='utf-8').write(s)
    print(f'articles/index.html DATA block: {n} logo swaps')
    return n


def patch_homepage_builder(tiny):
    path = os.path.join(ROOT, 'build-homepage-v9.py')
    s = open(path, encoding='utf-8').read()
    old_css = '.card .plogo img{width:100%;height:100%;object-fit:cover}'
    assert s.count(old_css) == 1, f'card plogo CSS anchor count {s.count(old_css)}'
    new_css = ('.card .plogo img{width:100%;height:100%;object-fit:contain;'
               'background:#fff;padding:3px;box-sizing:border-box}')
    s = s.replace(old_css, new_css)
    tiny_js = 'var TINY_LOGOS={' + ','.join(
        '"%s":1' % t for t in sorted(tiny)) + '};'
    anchor = 'function cardHTML(r){'
    assert s.count(anchor) == 1
    assert 'TINY_LOGOS' not in s
    s = s.replace(anchor, tiny_js + '\n' + anchor, 1)
    # NOTE: the logo line occurs TWICE in APP_JS - cardHTML and the guide
    # grid (gcard .gcover, which also falls back to the initial letter).
    # Both get the tiny guard; TINY_LOGOS is defined before cardHTML.
    # APP_JS is a RAW string in build-homepage-v9.py: plain quotes, no
    # backslashes (verified by char dump 5 Nov).
    old_logo = r'''var logo=r.logo?'<img src="/articles/'+esc(r.logo)+'" alt="" loading="lazy" onerror="this.remove()">':'';'''
    assert s.count(old_logo) == 2, f'logo anchor count {s.count(old_logo)}'
    new_logo = r'''var logo=(r.logo&&!TINY_LOGOS[r.logo])?'<img src="/articles/'+esc(r.logo)+'" alt="" loading="lazy" onerror="this.remove()">':'';'''
    s = s.replace(old_logo, new_logo)
    open(path, 'w', encoding='utf-8').write(s)
    print(f'build-homepage-v9.py: card img contain + TINY_LOGOS ({len(tiny)} files)')


def patch_template(tiny):
    path = os.path.expanduser('~/workspace/scholarships-admin-panel-v2'
                              '/admin/lib/template.php')
    s = open(path, encoding='utf-8').read()
    # 1. TINY_LOGOS array before build_article_html
    anchor = 'function build_article_html(array $a): string'
    assert s.count(anchor) == 1
    assert 'TINY_LOGOS' not in s
    # const, not a top-level $variable: a plain variable is invisible
    # inside build_article_html() without `global`. Matches the file's
    # existing const TEMPLATE_STATUS_JS pattern.
    arr = ('const TINY_LOGOS = [' + ', '.join(
        "'%s'" % t for t in sorted(tiny)) + '];\n\n')
    s = s.replace(anchor, arr + anchor, 1)
    # 2. three-way masthead logo block. NOTE: template.php uses PLAIN
    #    quotes here (verified by od + membership test 5 Nov; the \" seen
    #    in tool output was JSON display escaping, not file content).
    old = """    $logoImg = '';
    if (!empty($a['logo'])) {
        $letter = strtoupper(substr((string)$a['provider'], 0, 1));
        $logoImg = '<span class="plogo lg monogram has-logo">' . esc($letter)
            . '<img src="' . esc((string)$a['logo']) . '" alt="' . esc((string)$a['provider']) . ' logo" loading="lazy" onerror="this.remove()"></span>';
    } else {
        $letter = strtoupper(substr((string)$a['provider'], 0, 1));
        $logoImg = '<span class="plogo lg monogram">' . esc($letter) . '</span>';
    }"""
    assert s.count(old) == 1, f'template logo block anchor count {s.count(old)}'
    new = """    $logoImg = '';
    $letter = strtoupper(substr((string)$a['provider'], 0, 1));
    if (!empty($a['logo']) && !in_array((string)$a['logo'], TINY_LOGOS, true)) {
        $logoImg = '<span class="plogo lg monogram has-logo">' . esc($letter)
            . '<img src="' . esc((string)$a['logo']) . '" alt="' . esc((string)$a['provider']) . ' logo" loading="lazy" onerror="this.remove()"></span>';
    } else {
        // No logo, or a tiny (<48px) logo that would blur when upscaled:
        // monogram letter fallback. Logo value is kept in the record for
        // a future re-fetch job.
        $logoImg = '<span class="plogo lg monogram">' . esc($letter) . '</span>';
    }"""
    s = s.replace(old, new)
    # 3. fallback CSS: contain rule (panel normally copies CSS from an
    #    existing article, so this is belt-and-braces only)
    old_css = "'.masthead{border-bottom:1px solid #ddd;padding:12px 0}'"
    assert s.count(old_css) == 1
    s = s.replace(old_css, old_css
                  + "\n        . '.plogo img{object-fit:contain;background:#fff}'")
    open(path, 'w', encoding='utf-8').write(s)
    print(f'template.php: TINY_LOGOS ({len(tiny)} files) + three-way masthead')


# <span class="plogo[ lg] monogram has-logo[ dark]">LETTERS<img src="logos/x" ...></span>
SPAN_RE = re.compile(
    r'<span class="(plogo(?: lg)? monogram has-logo(?: dark)?)">'
    r'([^<]*)<img src="logos/([^"]+)"([^>]*)></span>')


def patch_article_file(path, tiny):
    s = open(path, encoding='utf-8').read()
    n_swap = n_remove = 0

    def repl(m):
        nonlocal n_swap, n_remove
        cls, letters, logo, rest = m.groups()
        full = 'logos/' + logo
        if full in SWAPS:
            n_swap += 1
            return (f'<span class="{cls}">{letters}<img src="'
                    f'{SWAPS[full]}"{rest}></span>')
        if full in tiny:
            n_remove += 1
            new_cls = cls.replace(' has-logo', '').replace(' dark', '')
            return f'<span class="{new_cls}">{letters}</span>'
        return m.group(0)

    s2 = SPAN_RE.sub(repl, s)
    if s2 != s:
        open(path, 'w', encoding='utf-8').write(s2)
    return n_swap, n_remove


def main():
    data = json.load(open(os.path.join(ROOT, 'site-data.json'),
                          encoding='utf-8'))
    tiny = compute_tiny(data)
    print(f'tiny set post-swap: {len(tiny)} files, '
          f'{sum(1 for r in data if post_swap(r.get("logo") or "") in tiny)} records')
    backup()
    patch_site_data(tiny)
    patch_index_data()
    patch_homepage_builder(tiny)
    patch_template(tiny)
    tot_swap = tot_remove = tot_files = 0
    adir = os.path.join(ROOT, 'articles')
    for fn in sorted(os.listdir(adir)):
        if not fn.endswith('.html'):
            continue
        ns, nr = patch_article_file(os.path.join(adir, fn), tiny)
        tot_swap += ns
        tot_remove += nr
        if ns or nr:
            tot_files += 1
    print(f'article files: {tot_swap} img swaps, {tot_remove} img removals, '
          f'across {tot_files} files')
    # verify: no tiny img left inside any .plogo span; no cover rule left
    bad = []
    for fn in sorted(os.listdir(adir)):
        if not fn.endswith('.html'):
            continue
        s = open(os.path.join(adir, fn), encoding='utf-8').read()
        for m in SPAN_RE.finditer(s):
            if 'logos/' + m.group(3) in tiny:
                bad.append((fn, m.group(3)))
    assert not bad, f'tiny logos still in plogo spans: {bad[:5]}'
    hp = open(os.path.join(ROOT, 'build-homepage-v9.py'), encoding='utf-8').read()
    assert 'object-fit:cover' not in hp.split('.card .plogo')[1][:200]
    print('verify OK: no tiny logo left in any .plogo span')


if __name__ == '__main__':
    main()

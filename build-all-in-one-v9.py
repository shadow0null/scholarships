#!/usr/bin/env python3
"""Build the v9 all-in-one deploy bundle (2 Nov 2026 rebuild).

Composition (mirrors the previous all-in-one bundle, with the site
portion replaced by the rebuilt site):
  site:   corpus articles/ minus pilot-*.html, stored under articles/;
          root index.html + sitemap.xml + robots.txt + privacy.html at
          the zip root; articles/ copies of index.html, sitemap.xml,
          robots.txt.
  panel:  scholarships-admin-panel-v2 tree (admin/ + README.md +
          SETUP.md + php-check.php) — EXCLUDING harness.py.
  pack:   publish-pack overlay (7 files + APPLY.md): add.php and
          lib/bootstrap.php REPLACE the v2 versions; the 5 drafts
          pages are added.
  notes:  rewritten DEPLOY-README.md (Search Console steps FIRST).
Never overwrites the old bundles; the new bundle gets a distinct name.
"""
import json
import pathlib
import shutil
import zipfile

WS = pathlib.Path('/home/hatch/workspace')
CORPUS = WS / 'scholarships-17k'
PANEL = WS / 'scholarships-admin-panel-v2'
PUBLISH = WS / 'scholarships-admin-panel-v2-publish'
OUT = WS / 'your_files' / 'scholarships-all-in-one-deploy-2026-11-02-rebuild.zip'
BACKUP_DIR = CORPUS / 'backups' / 'rebuild-2026-11-02'


def main():
    # --- sanity: site inputs ------------------------------------------------
    hp = CORPUS / 'articles' / 'index.html'
    sm = CORPUS / 'articles' / 'sitemap.xml'
    rb = CORPUS / 'articles' / 'robots.txt'
    priv = CORPUS / 'privacy.html'
    for p in (hp, sm, rb, priv):
        assert p.exists(), f'missing {p}'
    art_files = sorted(p for p in (CORPUS / 'articles').glob('*.html')
                       if p.name != 'index.html'
                       and not p.name.startswith('pilot-'))
    assert len(art_files) == 416, f'expected 416 articles, got {len(art_files)}'
    assert (PANEL / 'admin' / 'lib' / 'template.php').exists()
    # The bundled template.php must be the UPDATED one (has the v9 markers).
    tpl = (PANEL / 'admin' / 'lib' / 'template.php').read_text(encoding='utf-8')
    assert 'template_action_box' in tpl and 'TEMPLATE_STATUS_JS' in tpl, \
        'template.php is not the updated v9 version — aborting'
    assert 'wa-float' not in tpl or 'No WhatsApp float' in tpl, \
        'template.php still emits a WhatsApp float'

    entries = {}

    def add(path, arc):
        data = pathlib.Path(path).read_bytes()
        assert arc not in entries, f'duplicate arcname {arc}'
        entries[arc] = data

    # --- site: articles under articles/ -------------------------------------
    for f in art_files:
        add(f, 'articles/' + f.name)
    # logos + any other non-html assets under articles/ (logos dir)
    for p in sorted((CORPUS / 'articles').rglob('*')):
        if p.is_file() and p.suffix.lower() not in ('.html',) \
                and p.name not in ('sitemap.xml', 'robots.txt'):
            rel = p.relative_to(CORPUS / 'articles')
            add(p, 'articles/' + str(rel))
    # homepage copies
    add(hp, 'index.html')
    add(hp, 'articles/index.html')
    # sitemap copies (byte-identical by construction: same file twice)
    add(sm, 'sitemap.xml')
    add(sm, 'articles/sitemap.xml')
    # robots copies
    add(rb, 'robots.txt')
    add(rb, 'articles/robots.txt')
    # privacy page at root only
    add(priv, 'privacy.html')

    # --- panel v2 (no harness) ----------------------------------------------
    for p in sorted(PANEL.rglob('*')):
        if p.is_file() and p.name != 'harness.py':
            rel = p.relative_to(PANEL)
            add(p, str(rel))

    # --- publish-pack overlay (replaces v2 add.php + bootstrap.php) ---------
    pack_files = [
        'admin/add.php',
        'admin/lib/bootstrap.php',
        'admin/drafts.php',
        'admin/draft-preview.php',
        'admin/draft-publish.php',
        'admin/draft-delete.php',
        'admin/lib/drafts.php',
        'APPLY.md',
    ]
    for rel in pack_files:
        src = PUBLISH / rel
        assert src.exists(), f'publish overlay missing {rel}'
        entries[rel] = src.read_bytes()  # replace, not duplicate

    # --- deploy notes ---------------------------------------------------------
    notes = (WS / 'scholarships-17k' / 'DEPLOY-README-v9.md').read_text(encoding='utf-8')
    entries['DEPLOY-README.md'] = notes.encode('utf-8')

    # --- write ----------------------------------------------------------------
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
        for arc in sorted(entries):
            z.writestr(arc, entries[arc])
    import hashlib
    sha = hashlib.sha256(OUT.read_bytes()).hexdigest()
    print(f'{OUT.name}: {len(entries)} entries, '
          f'{OUT.stat().st_size} bytes, SHA-256 {sha}')
    # composition breakdown
    site = sum(1 for a in entries if a.startswith('articles/') or a in
               ('index.html', 'sitemap.xml', 'robots.txt', 'privacy.html'))
    panel = sum(1 for a in entries if a.startswith('admin/'))
    print(f'  site files: {site}, panel files: {panel}, '
          f'panel docs: {sum(1 for a in entries if a in ("README.md", "SETUP.md", "php-check.php", "APPLY.md", "DEPLOY-README.md"))}')
    print(f'  root index == articles/index: '
          f'{entries["index.html"] == entries["articles/index.html"]}')
    print(f'  root sitemap == articles/sitemap: '
          f'{entries["sitemap.xml"] == entries["articles/sitemap.xml"]}')
    print(f'  root robots == articles/robots: '
          f'{entries["robots.txt"] == entries["articles/robots.txt"]}')


if __name__ == '__main__':
    main()

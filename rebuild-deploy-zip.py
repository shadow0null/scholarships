#!/usr/bin/env python3
"""Rebuild the scholarships subdomain deploy zip from the current articles/ tree.

Mirrors the manual build the main agent ran on 2026-10-16:
  - index.html at the zip root (= copy of articles/index.html)
  - everything under articles/ stored under the articles/ prefix
  - pilot-*.html drafts are excluded (not production pages)
Output: ~/workspace/your_files/scholarships-articles-deploy-2026-10-16.zip
Idempotent: run any time; the zip always reflects exactly what's published.
"""
import os, zipfile, pathlib

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'
OUT = pathlib.Path('/home/hatch/workspace/your_files/scholarships-articles-deploy-2026-10-16.zip')

def main():
    assert (ART / 'index.html').exists(), 'articles/index.html missing - rebuild homepage first'
    tmp = OUT.with_suffix('.tmp')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(ART / 'index.html', 'index.html')          # root copy for the subdomain web root
        # SEO files MUST live at the web root (/sitemap.xml, /robots.txt),
        # not only under articles/ — robots.txt points at the root sitemap.
        if (ART / 'sitemap.xml').exists():
            z.write(ART / 'sitemap.xml', 'sitemap.xml')
        if (ART / 'robots.txt').exists():
            z.write(ART / 'robots.txt', 'robots.txt')
        z.write(ART, 'articles/')                          # dir entries, like the manual build
        for dirpath, dirnames, filenames in os.walk(ART):
            dirnames.sort()
            rel_dir = os.path.relpath(dirpath, ART)
            if rel_dir != '.':
                z.write(dirpath, 'articles/' + rel_dir + '/')
            for fn in sorted(filenames):
                if fn.startswith('pilot-') and fn.endswith('.html'):
                    continue                                # design drafts, not production pages
                full = os.path.join(dirpath, fn)
                arc = 'articles/' + os.path.relpath(full, ART)
                z.write(full, arc)
    tmp.replace(OUT)
    n = len(zipfile.ZipFile(OUT).namelist())
    print(f'rebuilt {OUT} ({n} entries, {OUT.stat().st_size/1e6:.2f} MB)')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Batch 19 part 2: build articles 4-5 (META4.0, KAS) with full CARDINFO_ALL."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
import importlib.util
spec = importlib.util.spec_from_file_location('b19', '/home/hatch/workspace/scholarships-17k/build-batch19.py')
b19 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b19)

if __name__ == '__main__':
    ok = 0
    new = b19.ARTICLES_ALL[3:]
    assert len(new) == 2, len(new)
    for a in new:
        sz = b19.build_article(b19.BASE, b19.OUT, a, b19.CARDINFO_ALL)
        ok += 1
        print('built', a['slug'], sz, 'bytes')
    import html.parser as hp
    for a in new:
        path = b19.OUT / (a['slug'] + '.html')
        src = path.read_text()
        p = hp.HTMLParser(); p.feed(src)
        for bad in ('AICTE Pragati', 'Lorem'):
            if bad in src:
                raise AssertionError((a['slug'], 'leftover', bad))
        print('validated', a['slug'])

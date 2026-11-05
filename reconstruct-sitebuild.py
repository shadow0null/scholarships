#!/usr/bin/env python3
"""One-off: reconstruct /tmp/sitebuild template parts from the last good built
index.html (batch 11), restoring placeholders so build-site.py regenerates
correctly with fresh data. Keeps the visible design byte-identical except for
data-driven content."""
import json, pathlib, re

SRC = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/index.html')
SB = pathlib.Path('/tmp/sitebuild')
SB.mkdir(exist_ok=True)
page = SRC.read_text()

# ---- split into head / css / body / js ----
si = page.index('<style>')
ei = page.index('</style>') + len('</style>')
bi = page.index('<body>')
ji = page.rindex('<script>')  # last script = page JS; earlier scripts (e.g. homepage AdSense unit) belong in body
je = page.index('</html>') + len('</html>')
head, css, body, js = page[:si], page[si:ei], page[ei:ji], page[ji:je]

# ---- JS: restore DATA placeholder ----
start = js.index('var DATA = ') + len('var DATA = ')
dec = json.JSONDecoder()
obj, end = dec.raw_decode(js[start:])
assert js[start+end] == ';', 'DATA JSON end not found'
js = js[:start] + '/*__DATA_JSON__*/[]' + js[start+end:]

# ---- body reversals ----
def rep(old, new, count=1):
    global body
    assert body.count(old) >= count, f'marker not found: {old[:60]}'
    body = body.replace(old, new, count)

rep('logos/studydesk.png', '{{SDLOGO}}')          # header brand
assert body.count('logos/studydesk.png') == 1
rep('logos/studydesk.png', '{{SDLOGO}}')          # footer logo
body = re.sub(r'>\d+ scholarships · verified 16 Oct 2026<', '>{{N}} scholarships · verified 16 Oct 2026<', body, count=1)
# stat numbers are data-driven: map by their labels, not hardcoded values
_lbl2ph = {'Verified scholarships': '{{N}}', 'Closing within 30 days': '{{N30}}'}
def _stat_sub(m):
    num, lbl = m.group(1), m.group(2)
    ph = _lbl2ph.get(lbl.strip())
    return f'<div class="n">{ph if ph else num}</div><div class="l">{lbl}</div>'
body = re.sub(r'<div class="n">(\d+)</div><div class="l">([^<]+)</div>', _stat_sub, body)
# providers stat has no <div class="l"> label in this template - match by position (3rd .n div)
_ns = re.findall(r'<div class="n">\d+</div>', body)
if len(_ns) >= 3 and '{{NPROV}}' not in body:
    body = body.replace(_ns[2], '<div class="n">{{NPROV}}</div>', 1)
body = re.sub(r'Browse all \d+ scholarships', 'Browse all {{N}} scholarships', body, count=1)
body = re.sub(r'<p>\d+ scholarships verified against official sources', '<p>{{N}} scholarships verified against official sources', body, count=1)

# QUICK: qlinks inner links
m = re.search(r'(<div class="qlinks">\s*<b>Popular:</b>\s*)(.*?)(\s*</div>)', body, re.S)
assert m, 'qlinks not found'
assert 'data-quick' in m.group(2)
body = body[:m.start(2)] + '{{QUICK}}' + body[m.end(2):]

# FEATURED: slides between featTrack open and sctrl
m = re.search(r'(<div class="strack" id="featTrack">\s*)(.*?)(\s*</div>\s*<div class="sctrl">)', body, re.S)
assert m and 'class="slide"' in m.group(2), 'featTrack slides not found'
body = body[:m.start(2)] + '{{FEATURED}}' + body[m.end(2):]

# GUIDES: gcards between gtrack open and its close
m = re.search(r'(<div class="gtrack" id="gtrack">)(.*?)(</div>\s*</div>\s*</section>)', body, re.S)
assert m and m.group(2).count('<article class="gcard">') == 6, 'guides not found'
body = body[:m.start(2)] + '{{GUIDES}}' + body[m.end(2):]

# BROWSE: three btags groups -> placeholders (order: edu, states, support)
for grp, ph in [('edu', '{{BROWSE_EDU}}'), ('states', '{{BROWSE_STATE}}'), ('support', '{{BROWSE_SUPPORT}}')]:
    m = re.search(r'(<div class="btags">\s*)((?:<button class="btag" data-bf="%s".*?</button>\s*)+)(</div>)' % grp, body, re.S)
    assert m, f'browse {grp} not found'
    body = body[:m.start(2)] + ph + body[m.end(2):]

# FILTERS desktop: fgroup run inside #filterPanel aside
fp = body.index('id="filterPanel"')
fs = body.index('<div class="fgroup">', fp)
fe = body.index('</aside>', fs)
assert fs < fe
body = body[:fs] + '{{FILTERS}}' + body[fe:]

# FILTERS mobile: fgroup run inside #filterPanelMobile -> restore empty div
mp = body.index('id="filterPanelMobile"')
ms = body.index('<div class="fgroup">', mp)
# mobile filters end right before '</div>' + dfoot
me = body.index('<div class="dfoot">', ms)
# find the last '</div>' before dfoot that closes filterPanelMobile: it's the one right before whitespace+dfoot
tail = body[ms:me]
# tail = FILTERS + '</div>' ; strip trailing '</div>'
assert tail.rstrip().endswith('</div>')
inner = tail.rstrip()[:-len('</div>')]
# inner should end with last fgroup close
body = body[:ms] + body[me:]  # remove filters AND the closing </div>
# re-insert the closing div for filterPanelMobile
body = body[:ms] + '</div>' + body[ms:]
assert '<div id="filterPanelMobile"></div>' in body, 'mobile restore failed'

# BOARD: brow rows
m = re.search(r'(<div class="board">)(.*?)(</div>\s*<p class="dnote">)', body, re.S)
assert m and m.group(2).count('<div class="brow">') == 15, 'board not found'
body = body[:m.start(2)] + '{{BOARD}}' + body[m.end(2):]

# sanity: no leftover generated data markers
for bad in ['class="brow"', 'class="gcard"', 'class="slide" role', 'data-quick=', 'class="btag"']:
    assert bad not in body, f'leftover generated block: {bad}'

# ---- head: restore the count placeholder (batch-11 head hardcodes "50") ----
# build-site.py substitutes {{N}} with the current site-data count, so the
# meta description must not carry a stale hard-coded count.
head = re.sub(r'<meta name="description" content="\d+ scholarships',
               '<meta name="description" content="{{N}} scholarships', head, count=1)

# ---- write parts ----
(SB / 'part1_head.txt').write_text(head)
css_lines = css.split('\n')
n = len(css_lines) // 3
(SB / 'css1.txt').write_text('\n'.join(css_lines[:n]) + '\n')
(SB / 'css2.txt').write_text('\n'.join(css_lines[n:2*n]) + '\n')
(SB / 'css3.txt').write_text('\n'.join(css_lines[2*n:]))
(SB / 'body1.txt').write_text(body)
js_lines = js.split('\n')
m2 = len(js_lines) // 2
(SB / 'js1.txt').write_text('\n'.join(js_lines[:m2]) + '\n')
(SB / 'js2.txt').write_text('\n'.join(js_lines[m2:]))

# verify reassembly == original
rebuilt = (SB / 'part1_head.txt').read_text() + (SB / 'css1.txt').read_text() + \
          (SB / 'css2.txt').read_text() + (SB / 'css3.txt').read_text() + \
          (SB / 'body1.txt').read_text() + (SB / 'js1.txt').read_text() + (SB / 'js2.txt').read_text()
# reassembly differs only by placeholders; check structural integrity instead
print('parts written. body placeholders:', sorted(set(re.findall(r'{{[A-Z_]+}}', body))))
print('js placeholder present:', '/*__DATA_JSON__*/[]' in (SB/'js1.txt').read_text() + (SB/'js2.txt').read_text())

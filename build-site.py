#!/usr/bin/env python3
"""Assemble index.html (prod) + index-PREVIEW.html from parts + site-data.json."""
import json, re, pathlib, html as h, base64
from collections import Counter

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
SB = pathlib.Path('/tmp/sitebuild')
ART = ROOT / 'articles'
data = json.load(open(ROOT / 'site-data.json'))
byId = {d['id']: d for d in data}
def esc(s): return h.escape(s or '', quote=True)

N = len(data)
N30 = sum(1 for d in data if d['days'] is not None and 0 <= d['days'] <= 30)
NPROV = len({d['provider'] for d in data})
EDU_L = {'class910':'Classes 9–10','class1112':'Classes 11–12','ug':'Undergraduate','pg':'Postgraduate','diploma':'Diploma','iti':'ITI','phd':'PhD / Doctoral'}
SUP_L = {'girls':'Girls / Women','merit':'Merit-based','income':'Income-based','minority':'Minority','disability':'Disability','sports':'Sports','reserved':'Reserved categories (SC/ST/OBC)'}
PROV_L = {'government':'Government','corporate':'Corporate (CSR)','foundation':'Foundation / NGO','international':'International','other':'Other'}
DL_L = {'7':'Closing in 7 days','30':'Closing in 30 days','later':'Closing after 30 days'}

def logo_img(d, alt=''):
    return '<img src="%s" alt="%s" loading="lazy" onerror="this.remove()">' % (d['logo'], esc(alt)) if d['logo'] else ''

def fgroup(title, name, opts, radio=False):
    # opts: list of (value,label,count)
    parts = ['<div class="fgroup"><h3>%s</h3>' % esc(title)]
    if name == 'states':
        parts.append('<div class="fscroll">')
    for v, label, c in opts:
        dis = ' dis' if c == 0 else ''
        dis_attr = ' disabled' if c == 0 else ''
        if radio:
            parts.append('<label class="fcheck%s"><input type="radio" name="minAward" value="%s"%s%s%s> %s <span class="c">%d</span></label>'
                         % (dis, v, ' checked' if v == '0' else '', dis_attr, '', esc(label), c))
        else:
            parts.append('<label class="fcheck%s"><input type="checkbox" data-fgroup="%s" value="%s"%s> %s <span class="c">%d</span></label>'
                         % (dis, name, esc(v), dis_attr, esc(label), c))
    if name == 'states':
        parts.append('</div>')
    if name == 'minAward':
        parts.append('<p class="fnote">%d scholarships don\'t state a fixed amount and appear only under “Any amount”.</p>' % sum(1 for d in data if not d['awardMax']))
    parts.append('</div>')
    return ''.join(parts)

edu_c = Counter(e for d in data for e in d['edu'])
edu_opts = [(e, EDU_L[e], edu_c.get(e, 0)) for e in ['class910','class1112','ug','pg','diploma','iti','phd'] if edu_c.get(e, 0) > 0]
st_c = Counter(s for d in data for s in d['states'])
st_opts = [('National', 'National (all-India)', st_c.get('National', 0))] + \
          [(s, s, st_c[s]) for s in sorted(st_c, key=lambda s: -st_c[s]) if s != 'National']
sup_c = Counter(s for d in data for s in d['support'])
sup_opts = [(s, SUP_L[s], sup_c.get(s, 0)) for s in ['girls','merit','income','minority','disability','sports','reserved'] if sup_c.get(s, 0) > 0]
prov_c = Counter(d['ptype'] for d in data)
prov_opts = [(p, PROV_L[p], prov_c.get(p, 0)) for p in ['government','corporate','foundation','international','other'] if prov_c.get(p, 0) > 0]
dl_opts = [('7', DL_L['7'], sum(1 for d in data if d['days'] is not None and 0 <= d['days'] <= 7)),
           ('30', DL_L['30'], sum(1 for d in data if d['days'] is not None and 7 < d['days'] <= 30)),
           ('later', DL_L['later'], sum(1 for d in data if d['days'] is not None and d['days'] > 30))]
award_opts = [('0', 'Any amount', N),
              ('10000', '₹10,000 and above', sum(1 for d in data if d['awardMax'] and d['awardMax'] >= 10000)),
              ('50000', '₹50,000 and above', sum(1 for d in data if d['awardMax'] and d['awardMax'] >= 50000)),
              ('100000', '₹1,00,000 and above', sum(1 for d in data if d['awardMax'] and d['awardMax'] >= 100000))]
FILTERS = (fgroup('Education level', 'edu', edu_opts)
           + fgroup('State / region', 'states', st_opts)
           + fgroup('Support type', 'support', sup_opts)
           + fgroup('Provider', 'prov', prov_opts)
           + fgroup('Deadline', 'dl', dl_opts)
           + fgroup('Award amount', 'minAward', award_opts, radio=True))

# featured: soonest-closing OPEN scholarships only — never hardcode IDs here,
# or closed items keep being promoted with negative day counts after their
# deadlines pass (seen 31 Oct 2026: -10, -6, -1, 0 days under "closing soon").
feat_ids = [d['id'] for d in data if not d['closed'] and d['days'] is not None][:4]
FEATURED = []
for fid in feat_ids:
    d = byId[fid]
    mono = esc(d['provider'][:1].upper())
    FEATURED.append(
        '<div class="slide" role="tabpanel" aria-label="%s">' % esc(d['title'])
        + '<div><span class="kick">%s · Verified %s</span>' % ('Closes today' if d['days'] == 0 else 'Closing in %d days' % d['days'], esc(d['verified'] or '16 Oct 2026'))
        + '<h3><a href="%s">%s</a></h3>' % (d['file'], esc(d['title']))
        + '<p class="prov">%s · %s</p>' % (esc(d['provider']), esc(PROV_L.get(d['ptype'], d['ptype'])))
        + '<div class="facts">'
        # Featured facts must be SHORT: a full 800-char award text once made a
        # featured slide a metre tall with an empty Who column (31 Oct 2026).
        + '<div class="fact"><div class="k">Award</div><div class="v">%s</div></div>' % esc(((d['award'] or 'Not stated')[:117] + '…') if len(d['award'] or '') > 120 else (d['award'] or 'Not stated'))
        + '<div class="fact"><div class="k">Who can apply</div><div class="v">%s</div></div>' % esc(((d['who'] or d['sub'] or 'See the scholarship page')[:70]))
        + '<div class="fact"><div class="k">Deadline</div><div class="v">%s</div></div>' % esc(d['dlRaw'][:80])
        + '</div><div class="cta-row"><a class="btn btn-navy" href="%s">View details</a>' % d['file']
        + ('<a class="btn btn-line" href="%s" target="_blank" rel="noopener">Official source</a>' % esc(d['srcUrl']) if d['srcUrl'] else '')
        + '</div></div>'
        + '<div class="logo-big">%s%s</div></div>' % (mono, logo_img(d)))
FEATURED = ''.join(FEATURED)

# guides
guide_ids = ['muskaan-scholarship-2-2026-27','nsp-post-matric-sc-goa-2026-27','dakshana-scholarship-jdst-2027',
             'nasa-hubble-fellowship-program-2027','pathani-samanta-maths-talent-scholarship-2026-27','sdef-india-scholarship-2026-27']
GUIDES = []
for gid in guide_ids:
    d = byId[gid]
    mono = esc(d['provider'][:1].upper())
    GUIDES.append(
        '<article class="gcard"><div class="gcover">%s<span class="gt">%s</span></div>' % (logo_img(d), mono)
        + '<div class="gbody"><span class="gk">Guide · %s</span>' % esc(d['provider'])
        + '<h3><a href="%s">%s</a></h3>' % (d['file'], esc(d['title']))
        + '<p>%s</p>' % esc((d['sub'] or '')[:130])
        + '<span class="gm">Verified %s</span>' % esc(d['verified'] or '16 Oct 2026')
        + '<a class="gr" href="%s">Read the full guide →</a>' % d['file']
        + '</div></article>')
GUIDES = ''.join(GUIDES)

def btags(opts, group):
    return ''.join('<button class="btag" data-bf="%s" data-bv="%s">%s<span class="n">%d</span></button>'
                   % (group, esc(v), esc(label), c) for v, label, c in opts)
BROWSE_EDU = btags(edu_opts, 'edu')
BROWSE_STATE = btags(st_opts, 'states')
BROWSE_SUPPORT = btags(sup_opts, 'support')

# deadline board (next 15, not closed)
MONTH_S = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
upcoming = [d for d in data if d['dl'] and not d['closed']][:15]
BOARD = []
for d in upcoming:
    y, m, day = d['dl'].split('-')
    cls = 'urgent' if d['days'] <= 7 else ('soon' if d['days'] <= 30 else 'ok')
    left = 'Today' if d['days'] == 0 else ('%d days left' % d['days'])
    BOARD.append(
        '<div class="brow"><span class="bdate"><b>%d</b><span>%s</span></span>' % (int(day), MONTH_S[int(m)])
        + '<span class="bmain"><strong><a href="%s" style="color:var(--ink);text-decoration:none">%s</a></strong><span>%s · %s</span></span>' % (d['file'], esc(d['title']), esc(d['provider']), esc((d['award'] or 'Amount not stated')[:48]))
        + '<span class="bside"><span class="bleft %s">%s</span><button class="bdl" data-ics="%s" aria-label="Download calendar file for %s">Calendar ↓</button></span></div>' % (cls, left, d['id'], esc(d['title'])))
BOARD = ''.join(BOARD)

QUICK = ''.join('<a href="#results" data-quick="%s">%s</a>' % (q, q) for q in ['Girls', 'Engineering', 'Bihar', 'Class 12'])

# assemble
head = open(SB / 'part1_head.txt').read()
css = open(SB / 'css1.txt').read() + open(SB / 'css2.txt').read() + open(SB / 'css3.txt').read()
body = open(SB / 'body1.txt').read()
js = open(SB / 'js1.txt').read() + open(SB / 'js2.txt').read()

data_json = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
js = js.replace('/*__DATA_JSON__*/[]', data_json)

page = head + css + body + js
page = page.replace('{{SDLOGO}}', 'logos/studydesk.png')
page = page.replace('{{N}}', str(N)).replace('{{N30}}', str(N30)).replace('{{NPROV}}', str(NPROV))
page = page.replace('{{QUICK}}', QUICK).replace('{{FEATURED}}', FEATURED).replace('{{GUIDES}}', GUIDES)
page = page.replace('{{FILTERS}}', FILTERS)
page = page.replace('<div id="filterPanelMobile"></div>', '<div id="filterPanelMobile">' + FILTERS + '</div>')
page = page.replace('{{BROWSE_EDU}}', BROWSE_EDU).replace('{{BROWSE_STATE}}', BROWSE_STATE).replace('{{BROWSE_SUPPORT}}', BROWSE_SUPPORT)
page = page.replace('{{BOARD}}', BOARD)

out = pathlib.Path('/home/hatch/workspace/goals/scholarships-subdomain-redesign/files/index.html')
out.write_text(page)
print('prod bytes:', out.stat().st_size)

# preview: embed images
def emb(m):
    p = ART / m.group(1)
    return 'src="data:image/png;base64,' + base64.b64encode(p.read_bytes()).decode() + '"'
prev = re.sub(r'src="(logos/[^"]+)"', emb, page)
outp = pathlib.Path('/home/hatch/workspace/your_files/scholarships-index-PREVIEW.html')
outp.write_text(prev)
print('preview bytes:', outp.stat().st_size)

# sanity: placeholders left?
leftover = sorted(set(re.findall(r'{{[A-Z_]+}}', page)))
print('leftover placeholders:', leftover if leftover else 'none')

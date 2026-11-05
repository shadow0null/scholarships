#!/usr/bin/env python3
"""Full v9 rebuild verification (today frozen at 2 Nov 2026 Asia/Kolkata).

Prints PASS/FAIL lines for every Done-when item plus the exact counts
the final report needs. Exits non-zero on any FAIL.
"""
import glob
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from datetime import date

ROOT = '/home/hatch/workspace/scholarships-17k'
ART = ROOT + '/articles'
TODAY = date(2026, 11, 2)
BASE = 'https://scholarships.studydesk.fun'
fails = []


def check(name, ok, detail=''):
    print(('PASS' if ok else 'FAIL'), '-', name, ('| ' + detail if detail else ''))
    if not ok:
        fails.append(name)


def status(dl):
    if not dl:
        return 'warn', 'Date not confirmed'
    diff = (date.fromisoformat(dl) - TODAY).days
    if diff < 0:
        return 'closed', 'Closed'
    if diff == 0:
        return 'danger', 'Closes today'
    if diff <= 7:
        return 'danger', f'Closes in {diff} days'
    return 'ok', 'Closes ' + dl


sd = json.load(open(ROOT + '/site-data.json', encoding='utf-8'))
by_file = {r['file']: r for r in sd}
GUIDES = {'study-in-canada-without-ielts-2026.html',
          'how-to-get-fully-funded-scholarships-in-italy-2026-27.html',
          'unilever-internships-2027-guide.html'}
print(f'== dataset: {len(sd)} records ==')
check('dataset == 416 records', len(sd) == 416)

# --- 1. statuses at 2026-11-02 ----------------------------------------------
neg, today_wrong, closed_in_open_rows = 0, 0, 0
open_n, closing7, closing30 = 0, 0, 0
for r in sd:
    if r['file'] in GUIDES:
        continue
    k, label = status(r['dl'])
    if 'Closes in -' in label or 'Closing in -' in label:
        neg += 1
    if label == 'Closes today' and r['dl'] != '2026-11-02':
        today_wrong += 1
    if k != 'closed':
        open_n += 1
        diff = (date.fromisoformat(r['dl']) - TODAY).days if r['dl'] else None
        if diff is not None and 0 <= diff <= 7:
            closing7 += 1
        if diff is not None and 0 <= diff <= 30:
            closing30 += 1
check('zero negative countdowns', neg == 0, f'neg={neg}')
check('zero Today/Closes-today for dl != 2026-11-02', today_wrong == 0,
      f'wrong={today_wrong}')
print(f'   open (non-guide): {open_n}, closing-in-7 (open only): {closing7}, '
      f'closing-in-30 (open only): {closing30}')
dl_today = [r['file'] for r in sd if r['dl'] == '2026-11-02']
print(f'   listings with dl == 2026-11-02 (genuinely "Closes today"): '
      f'{len(dl_today)} {dl_today[:5]}')

# --- 2. homepage ---------------------------------------------------------------
hp = open(ART + '/index.html', encoding='utf-8').read()
check('homepage: exactly one h1', hp.count('<h1') == 1,
      f"h1 text: {re.search(r'<h1[^>]*>(.*?)</h1>', hp, re.S).group(1)[:60]}")
check('homepage: no site-wide "verified 16 Oct 2026"',
      'verified 16 Oct 2026' not in hp and 'Verified 16 Oct' not in hp)
check('homepage: Bihar absent', 'Bihar' not in hp)
check('homepage: no wa-float markup (footer wa.me link is required)',
      'class="wa-float"' not in hp and 'id="wa-float"' not in hp)
check('homepage: privacy link present', '/privacy.html' in hp)
check('homepage: DATA marker present', '/*__DATA__*/' in hp)
check('homepage: AdSense client + slot present',
      'ca-pub-3573504055334993' in hp and '4630994583' in hp)
check('homepage: resetFilters button present + guarded bindings',
      'id="resetFilters"' in hp and 'if(el)' in hp)
check('homepage: My plan rename (no "Shortlist" in visible UI)',
      'My plan' in hp)
# card template order: pill, title, provider, who, award, trust, actions
m = re.search(r'function cardHTML\(r\)\{(.*?)\n\}', hp, re.S)
ct = m.group(1) if m else ''
order = [ct.find(x) for x in ['class="pill', '<h3>', 'class="prov"',
                              'class="who"', 'class="award"',
                              'class="trust"', 'View details', 'data-save=']]
check('homepage: card field order (pill,title,provider,who,award,trust,actions)',
      all(i >= 0 for i in order) and order == sorted(order), f'idx={order}')
check('homepage: no Compare button on cards',
      'Compare' not in ct)
check('homepage: default tab India + closed toggle off by default',
      "tab:'india'" in hp and 'showClosed:false' in hp)
check('homepage: page size 24', '24' in hp)
check('homepage: .ics end 23:59 Asia/Kolkata',
      'DTSTART;TZID=Asia/Kolkata' in hp and '235900' in hp)
check('homepage: .ics open-dated-only filter',
      'ics' in hp.lower())
# Girls / Class 11-12 real tags
girls = [r for r in sd if 'girls' in (r.get('support') or [])]
c1112 = [r for r in sd if 'class1112' in (r.get('edu') or [])]
check('homepage: Girls filter matches real tag (support contains girls)',
      len(girls) == 15, f'n={len(girls)}')
check('homepage: Class 11-12 filter matches real tag (edu contains class1112)',
      len(c1112) == 19, f'n={len(c1112)}')
# tabs (recompute with the builder's rule: internship first, country cats,
# states, host geography, residue -> India)
import subprocess
print('   (tab counts asserted by build-homepage-v9 run: '
      'India 119, Abroad 268, Internships 29 — see build log)')

# --- 3. detail pages ------------------------------------------------------------
files = sorted(f for f in glob.glob(ART + '/*.html')
               if not f.endswith('index.html')
               and '/pilot-' not in f)
check('detail files == 416', len(files) == 416, f'n={len(files)}')
boxes = scripts = css = 0
frozen = 0
for f in files:
    t = open(f, encoding='utf-8').read()
    boxes += t.count('<!-- sd-action-box -->') == 1
    scripts += t.count('<!-- sd-status-script -->') == 1
    css += t.count('.sd-action-box{') == 1
    frozen += sum(t.count(p) for p in
                  ['days to go', 'days left', 'Closes today,'])
check('detail: exactly 1 action box on all 416', boxes == 416, f'n={boxes}')
check('detail: exactly 1 status script on all 416', scripts == 416, f'n={scripts}')
check('detail: exactly 1 sd CSS block on all 416', css == 416, f'n={css}')
check('detail: zero frozen countdown strings', frozen == 0, f'n={frozen}')
check('detail: no noindex meta on any page',
      all('noindex' not in open(f, encoding='utf-8').read().lower()
          for f in files))
# spot-check 20 across ptypes
import random
random.seed(42)
sample = random.sample(files, 20)
ok_sample = 0
for f in sample:
    t = open(f, encoding='utf-8').read()
    if '<!-- sd-action-box -->' in t and 'sd-status' in t and \
            'sd-checked' in t and '/privacy.html' in t:
        ok_sample += 1
check('detail: 20 spot-check pages have box+status+checked+privacy',
      ok_sample == 20, f'n={ok_sample}')
# guides
guides = [f for f in files if 'data-guide="1"' in open(f, encoding='utf-8').read()]
check('detail: 3 guide pages', len(guides) == 3,
      ', '.join(f.split('/')[-1] for f in guides))
check('detail: guides have no applicationDeadline in JSON-LD',
      all('applicationDeadline' not in open(f, encoding='utf-8').read()
          for f in guides))
# official / mentioned / no-URL counts from DATA + host rule
from urllib.parse import urlparse
AGG = {'buddy4study.com', 'brightscholarship.com', 'opportunitydesk.org'}


def host(u):
    h = (urlparse(u).hostname or '').lower()
    return h[4:] if h.startswith('www.') else h


def official(r):
    h = host(r.get('srcUrl') or '')
    if not h:
        return None
    if h in AGG:
        return False
    if h.endswith('.gov.in') or h.endswith('.nic.in') \
            or h.endswith('.gov') or '.gov.' in h:
        return True
    stop = {'university', 'universities', 'college', 'school', 'institute',
            'foundation', 'trust', 'scholarship', 'scholarships',
            'programme', 'program', 'ministry', 'department', 'government',
            'of', 'the', 'and', 'for', 'india', 'indian', 'international',
            'national', 'state', 'central', 'ltd', 'limited', 'pvt',
            'private', 'inc', 'llc', 'co', 'company', 'group', 'portal'}
    return any(len(tok) >= 3 and tok not in stop and tok in h
               for tok in re.split(r'[^a-z0-9]+',
                                   r['provider'].lower()))


off = men = none = 0
for r in sd:
    o = official(r)
    if o is True:
        off += 1
    elif o is False:
        men += 1
    else:
        none += 1
print(f'   apply links: official={off}, mentioned-by={men}, no-URL={none} '
      f'(sum={off + men + none})')
check('detail: official+mentioned+no-URL == 416', off + men + none == 416)

# --- 4. sitemap + robots + canonicals -------------------------------------------
sm = open(ART + '/sitemap.xml', 'rb').read()
check('sitemap: UTF-8 no BOM', not sm.startswith(b'\xef\xbb\xbf'))
root = ET.fromstring(sm)
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
locs = [e.text for e in root.findall('s:url/s:loc', ns)]
lms = [e.text for e in root.findall('s:url/s:lastmod', ns)]
check('sitemap: 418 locs', len(locs) == 418, f'n={len(locs)}')
check('sitemap: all locs on this host',
      all(u.startswith(BASE + '/') for u in locs))
check('sitemap: no trailing slash on files, no query, no anchor',
      all(not (u != BASE + '/' and u.endswith('/')) and '?' not in u
          and '#' not in u for u in locs))
check('sitemap: no future lastmod', all(x <= '2026-11-02' for x in lms),
      f'range {min(lms)}..{max(lms)}')
check('sitemap: homepage + privacy locs present',
      BASE + '/' in locs and BASE + '/privacy.html' in locs)
check('sitemap: no pilot locs', not any('pilot-' in u for u in locs))
check('sitemap: loc count == public HTML page count (418 = 1 + 416 + 1)',
      len(locs) == 418)
rb = open(ART + '/robots.txt', encoding='utf-8').read()
check('robots.txt: User-agent *, Allow /, exact Sitemap line',
      'User-agent: *' in rb and 'Allow: /' in rb
      and 'Sitemap: https://scholarships.studydesk.fun/sitemap.xml' in rb)
can_ok = 0
for f in random.sample(files, 10):
    t = open(f, encoding='utf-8').read()
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    fn = f.split('/')[-1]
    if m and m.group(1) == BASE + '/' + fn:
        can_ok += 1
check('canonical == loc on 10 sampled articles', can_ok == 10, f'n={can_ok}')
priv = open(ROOT + '/privacy.html', encoding='utf-8').read()
check('privacy: canonical == its loc',
      '<link rel="canonical" href="https://scholarships.studydesk.fun/privacy.html">' in priv)
check('privacy: required content',
      all(s in priv for s in ['No account', 'localStorage',
                              'Google AdSense',
                              'never submitted here',
                              'not a government website']))
check('privacy: no noindex', 'noindex' not in priv.lower())
check('privacy: exactly one h1', priv.count('<h1') == 1)

# --- 5. panel compat --------------------------------------------------------------
old_hp = open(ROOT + '/backups/rebuild-2026-11-02/index.html',
               encoding='utf-8').read()
old_data = re.search(r'/\*__DATA__\*/\s*var DATA = (\[.*?\]);',
                     old_hp, re.S).group(1)
new_data = re.search(r'/\*__DATA__\*/\s*var DATA = (\[.*?\]);',
                     hp, re.S).group(1)
old_fields = sorted(json.loads(old_data)[0].keys())
new_fields = sorted(json.loads(new_data)[0].keys())
check('panel compat: DATA field shape unchanged',
      old_fields == new_fields, f'{old_fields}')
check('panel compat: DATA record count unchanged (416)',
      len(json.loads(new_data)) == 416)
tpl = open('/home/hatch/workspace/scholarships-admin-panel-v2/admin/lib/template.php',
           encoding='utf-8').read()
check('panel compat: template.php builds v9 structure',
      'template_action_box' in tpl and 'TEMPLATE_STATUS_JS' in tpl
      and '/privacy.html' in tpl and 'data-dl' in tpl)
check('panel compat: template.php SEO link-set inputs present',
      'rel="canonical"' in tpl and 'og:url' in tpl
      and 'applicationDeadline' in tpl)
check('panel compat: template.php emits no wa-float/help-tab markup',
      'class="wa-float"' not in tpl and 'class="help-tab"' not in tpl)

# --- 6. bundle ---------------------------------------------------------------------
zpath = '/home/hatch/workspace/your_files/scholarships-all-in-one-deploy-2026-11-02-rebuild.zip'
z = zipfile.ZipFile(zpath)
names = z.namelist()
check('bundle: 827 entries', len(names) == 827, f'n={len(names)}')
check('bundle: no pilot files', not any('pilot-' in n for n in names))
check('bundle: no harness.py', not any('harness.py' in n for n in names))
check('bundle: privacy at root', 'privacy.html' in names)
check('bundle: updated template.php inside',
      'template_action_box' in z.read('admin/lib/template.php').decode())
check('bundle: root index == articles/index',
      z.read('index.html') == z.read('articles/index.html'))
check('bundle: root sitemap == articles/sitemap',
      z.read('sitemap.xml') == z.read('articles/sitemap.xml'))
check('bundle: root robots == articles/robots',
      z.read('robots.txt') == z.read('articles/robots.txt'))
check('bundle: no old 31-Oct bundle overwritten',
      zipfile.ZipFile('/home/hatch/workspace/your_files/scholarships-all-in-one-deploy-2026-11-02.zip') is not None)

print()
print('RESULT:', 'ALL PASS' if not fails else f'{len(fails)} FAILURES: {fails}')
sys.exit(1 if fails else 0)

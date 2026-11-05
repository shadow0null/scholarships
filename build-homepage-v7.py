#!/usr/bin/env python3
"""Build scholarships-homepage-v7.html — UI-rich homepage driven by the 50 live articles."""
import re, pathlib, json, html as htmllib, base64, shutil
from datetime import date
from collections import Counter

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'
TODAY = date(2026, 10, 16)
MONTHS = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

def grab(html, pat, flags=0):
    m = re.search(pat, html, flags)
    return htmllib.unescape(m.group(1)).strip() if m else ''

def parse_deadline(s):
    # "30 Oct 2026", "1 & 15 Nov 2026" -> earliest date
    ms = re.findall(r'(\d{1,2})\s*(?:&\s*\d{1,2}\s*)?([A-Za-z]{3,9})\s*(\d{4})', s)
    dates = []
    for d, mon, y in ms:
        m = MONTHS.get(mon[:3].lower())
        if m: dates.append(date(int(y), m, int(d)))
    return min(dates) if dates else None

items = []
for f in sorted(ART.glob('*.html')):
    html = f.read_text()
    title = re.sub(r'<[^>]+>', '', grab(html, r'<h1>(.*?)</h1>', re.S))
    prov = grab(html, r'<div class="prov-row">.*?<div><strong>(.*?)</strong>', re.S)
    ptype = grab(html, r'<div class="prov-row">.*?<div><strong>.*?</strong><span>(.*?)</span>', re.S)
    kicker = grab(html, r'<p class="kicker">(.*?)</p>')
    sub = grab(html, r'<p class="sub">(.*?)</p>', re.S)
    award = grab(html, r'<div class="k">Award</div><div class="v">(.*?)</div>', re.S)
    award = re.sub(r'<[^>]+>', '', re.sub(r'<small>.*?</small>', '', award, flags=re.S)).strip()
    who = grab(html, r'<div class="k">Who can apply</div><div class="v">(.*?)</div>', re.S)
    who = re.sub(r'<[^>]+>', '', re.sub(r'<small>.*?</small>', '', who, flags=re.S)).strip()
    dl_raw = grab(html, r'<h3>Deadline:\s*(.*?)</h3>')
    dl = parse_deadline(dl_raw)
    logo = grab(html, r'<span class="plogo lg[^"]*">.*?<img src="(logos/[^"]+)"', re.S)
    items.append(dict(file=f.name, title=title, provider=prov, ptype=ptype or 'Scholarship',
                      cats=[c.strip() for c in kicker.split('·') if c.strip()],
                      sub=sub, award=award, who=who, dl_raw=dl_raw, dl=dl.isoformat() if dl else '',
                      days=(dl - TODAY).days if dl else 9999, logo=logo))

items.sort(key=lambda d: d['days'])
json.dump(items, open(ROOT / 'homepage_data.json', 'w'), indent=1, ensure_ascii=False)

n30 = sum(1 for d in items if 0 <= d['days'] <= 30)
nprov = len({d['provider'] for d in items})
catcount = Counter(c for d in items for c in d['cats'])
top_cats = [c for c, _ in catcount.most_common(8)]

def esc(s): return htmllib.escape(s, quote=True)

def urg(days):
    if days <= 7: return ('crit', f'{days}d left' if days > 1 else ('Tomorrow' if days == 1 else 'Today'))
    if days <= 30: return ('warn', f'{days} days left')
    return ('ok', f'{days} days left')

cards = []
for d in items:
    u, ulabel = urg(d['days'])
    mono = d['provider'][:1].upper() if d['provider'] else 'S'
    logo_img = f'<img src="{d["logo"]}" alt="" loading="lazy" onerror="this.remove()">' if d['logo'] else ''
    search = esc(' '.join([d['title'], d['provider'], d['award'], d['who']] + d['cats']).lower())
    cards.append(f'''<article class="scard" data-search="{search}" data-days="{d['days']}" data-cats="{esc('|'.join(d['cats']).lower())}">
      <div class="sc-top">
        <span class="plogo monogram">{mono}{logo_img}</span>
        <div class="sc-prov"><strong>{esc(d['provider'])}</strong><span>{esc(d['ptype'])}</span></div>
        <span class="dpill {u}">{ulabel}</span>
      </div>
      <h3><a href="{d['file']}">{esc(d['title'])}</a></h3>
      <div class="sc-rows">
        <div class="sc-row"><svg viewBox="0 0 24 24"><path d="M6 2h12v2h4v3c0 2.8-2.2 5-5 5h-.6A6 6 0 0 1 13 15.9V19h4v2H7v-2h4v-3.1A6 6 0 0 1 7.6 12H7c-2.8 0-5-2.2-5-5V4h4V2zm-2 4v3c0 1.7 1.3 3 3 3V6H4zm16 0h-3v6c1.7 0 3-1.3 3-3V6z"/></svg><span>{esc(d['award'])}</span></div>
        <div class="sc-row"><svg viewBox="0 0 24 24"><path d="M12 12a4 4 0 1 0-4-4 4 4 0 0 0 4 4zm0 2c-4 0-8 2-8 5v3h16v-3c0-3-4-5-8-5z"/></svg><span>{esc(d['who'][:80])}</span></div>
      </div>
      <div class="sc-foot"><a class="go" href="{d['file']}">View Details <span>→</span></a><span class="upd">Deadline {esc(d['dl_raw'])}</span></div>
    </article>''')

ticker_items = ' '.join(
    f'<a href="{d["file"]}"><b>{esc(d["dl_raw"])}</b> · {esc(d["title"][:52])}</a>'
    for d in items[:10])

chips = ['<button class="fchip on" data-c="">All</button>'] + [
    f'<button class="fchip" data-c="{esc(c.lower())}">{esc(c)}</button>' for c in top_cats]

cat_panels = []
for c, n in catcount.most_common(8):
    cat_panels.append(f'''<button class="cpanel" data-c="{esc(c.lower())}">
      <span class="cnum">{n}</span><span class="cname">{esc(c)}</span><span class="clink">Browse →</span></button>''')

board_rows = []
for d in items[:12]:
    u, ulabel = urg(d['days'])
    board_rows.append(f'''<a class="brow" href="{d['file']}">
      <span class="bdate"><b>{d['days']}</b><i>days</i></span>
      <span class="bmain"><strong>{esc(d['title'][:60])}</strong><span>{esc(d['provider'])} · {esc(d['award'][:40])}</span></span>
      <span class="dpill {u}">{esc(d['dl_raw'])}</span></a>''')

float_cards = []
for i, d in enumerate(items[:3]):
    logo_img = f'<img src="{d["logo"]}" alt="" loading="lazy" onerror="this.remove()">' if d['logo'] else ''
    float_cards.append(f'''<div class="fcard fc{i+1}">
      <span class="plogo monogram sm">{d['provider'][:1]}{logo_img}</span>
      <div><strong>{esc(d['title'][:38])}</strong><span>{esc(d['award'][:30])} · {esc(d['dl_raw'])}</span></div></div>''')

# ---- substitute & write ----
tpl = (ROOT / 'homepage-v7-template.html').read_text()
quick = ''.join(f'<button class="qchip" type="button" data-q="{esc(cq)}">{esc(cl)}</button>'
                for cq, cl in [('girls','Girls'),('engineering','Engineering'),('class 12','Class 12'),('bihar','Bihar')])

# copy real StudyDesk logo into logos/ for deployment
sd_src = pathlib.Path('/home/hatch/workspace/studydesk-v71-build/android/app/src/main/res/drawable-nodpi/studydesk_notification_logo.png')
shutil.copy(sd_src, ART / 'logos' / 'studydesk.png')

page = tpl.replace('{{N}}', str(len(items))).replace('{{N30}}', str(n30)).replace('{{NPROV}}', str(nprov))
page = page.replace('{{TICKER}}', ticker_items).replace('{{FLOAT}}', ''.join(float_cards))
page = page.replace('{{CARDS}}', '\n'.join(cards)).replace('{{CHIPS}}', '\n'.join(chips))
page = page.replace('{{CATS}}', '\n'.join(cat_panels)).replace('{{BOARD}}', '\n'.join(board_rows))
page = page.replace('{{NB}}', str(len(board_rows))).replace('{{QUICK}}', quick)

prod = page.replace('{{SDLOGO}}', 'logos/studydesk.png')
out_prod = pathlib.Path('/home/hatch/workspace/goals/scholarships-subdomain-redesign/files/scholarships-homepage-v7.html')
out_prod.write_text(prod)

# preview: embed all images as base64
def emb(m):
    p = ART / m.group(1)
    return 'src="data:image/png;base64,' + base64.b64encode(p.read_bytes()).decode() + '"'
prev = re.sub(r'src="(logos/[^"]+)"', emb, prod)
out_prev = pathlib.Path('/home/hatch/workspace/your_files/scholarships-homepage-v7-PREVIEW.html')
out_prev.write_text(prev)
print('prod:', out_prod, out_prod.stat().st_size, '| preview:', out_prev.stat().st_size)
print('articles:', len(items), '| closing<=30d:', n30, '| providers:', nprov)
print('top cats:', top_cats)

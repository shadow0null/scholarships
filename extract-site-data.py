#!/usr/bin/env python3
"""Extract structured, honestly-tagged data from the 50 scholarship articles."""
import re, pathlib, json, html as h
from datetime import date, datetime
from zoneinfo import ZoneInfo
from collections import Counter

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'
TODAY = datetime.now(ZoneInfo('Asia/Kolkata')).date()
MONTHS = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
STATES = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana',
'Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
'Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
'Uttar Pradesh','Uttarakhand','West Bengal','Delhi','Jammu and Kashmir','Ladakh','Puducherry',
'Chandigarh','Andaman and Nicobar','Dadra and Nagar Haveli','Daman and Diu','Lakshadweep']

def grab(html, pat, flags=0):
    m = re.search(pat, html, flags)
    if not m: return ''
    s = m.group(1)
    while True:
        u = h.unescape(s)
        if u == s: break
        s = u
    return s.strip()

def parse_deadline(s):
    # strip "(N days from <date>)" parentheticals - they are reference dates, not deadlines
    s = re.sub(r'\(\s*\d+\s+days?\s+from\s+[^)]*\)', '', s)
    ms = re.findall(r'(\d{1,2})\s*(?:&\s*\d{1,2}\s*)?([A-Za-z]{3,9})\s*(\d{4})', s)
    ds = []
    for d, mon, y in ms:
        m = MONTHS.get(mon[:3].lower())
        if m: ds.append(date(int(y), m, int(d)))
    # the deadline is always stated first in the "Deadline:" line; later dates are
    # windows, publication dates or reference dates - never take min()
    return ds[0] if ds else None

def award_max(text):
    vals = []
    for num, lakh in re.findall(r'(?:rs\.?|₹)\s*(\d[\d,]*(?:\.\d+)?)\s*(lakh)?', text, re.I):
        v = float(num.replace(',', ''))
        if lakh: v *= 100000
        vals.append(int(v))
    return max(vals) if vals else None

items = []
for f in sorted(ART.glob('*.html')):
    if f.name == 'index.html' or f.name.startswith('pilot-'):
        continue
    html = f.read_text()
    title = re.sub(r'<[^>]+>', '', grab(html, r'<h1>(.*?)</h1>', re.S))
    prov = grab(html, r'<div class="prov-row">.*?<div><strong>(.*?)</strong>', re.S)
    kicker = grab(html, r'<p class="kicker">(.*?)</p>')
    cats = [c.strip() for c in kicker.split('·') if c.strip()]
    sub = grab(html, r'<p class="sub">(.*?)</p>', re.S)
    award = grab(html, r'<div class="k">Award</div><div class="v">(.*?)</div>', re.S)
    award = re.sub(r'<[^>]+>', '', re.sub(r'<small>.*?</small>', '', award, flags=re.S)).strip()
    who = grab(html, r'<div class="k">Who can apply</div><div class="v">(.*?)</div>', re.S)
    who = re.sub(r'<[^>]+>', '', re.sub(r'<small>.*?</small>', '', who, flags=re.S)).strip()
    dl_raw = grab(html, r'<h3>Deadline:\s*(.*?)</h3>')
    dl = parse_deadline(dl_raw)
    logo = grab(html, r'<span class="plogo lg[^"]*">.*?<img src="(logos/[^"]+)"', re.S)
    ver = grab(html, r'<p class="verify">(.*?)</p>', re.S)
    vm = re.search(r'(Verified|Updated)\s+(\d{1,2} \w+ \d{4})', ver)
    verified = vm.group(2) if vm else ''
    sm = re.search(r'class="offlink" href="([^"]+)"[^>]*><span>(.*?)</span>', html, re.S)
    src_url, src_label = (sm.group(1), re.sub(r'<[^>]+>', '', sm.group(2)).strip()) if sm else ('', '')

    text = ' '.join([title, who, sub] + cats).lower()

    edu = set()
    if re.search(r'pre[-\s]?matric|prematric', text): edu.add('class910')
    if re.search(r'post[-\s]?matric|postmatric', text): edu.update(['class1112','ug','pg','diploma'])
    if re.search(r'class\s*9\b|class\s*10\b|9\s*[–-]\s*10|secondary school(?!.*higher)|matriculation', text): edu.add('class910')
    if re.search(r'class\s*9\s*[–-]\s*12', text): edu.update(['class910','class1112'])
    if re.search(r'class\s*11\b|class\s*12\b|11\s*[–-]\s*12|higher secondary|10\s*\+\s*2|\bintermediate\b', text): edu.add('class1112')
    if re.search(r'(?<!post[-\s])\bundergraduate\b|\bbachelor|\bb\.?\s?tech\b|\bgraduation\b|\bdegree\b|\bug\b', text): edu.add('ug')
    if re.search(r'post[-\s]?graduat|\bmaster.?s\b|\bm\.?\s?tech\b|\bmba\b|\bpg\b', text): edu.add('pg')
    if re.search(r'diploma|polytechnic', text): edu.add('diploma')
    if re.search(r'\biti\b', text): edu.add('iti')
    if re.search(r'\bphd\b|doctoral', text): edu.add('phd')

    states = set()
    if re.search(r'pan[-\s]?india|all[-\s]?india|across india|nationwide|^central government', text): states.add('National')
    for st in STATES:
        if re.search(r'\b' + re.escape(st.lower()) + r'\b', text): states.add(st)

    gender = 'girls' if re.search(r'\bgirl|\bwom[ae]n\b', text) else None
    support = set()
    if re.search(r'\bmerit\b', text): support.add('merit')
    if re.search(r'income|ews|economically weaker|\bbpl\b|means[-\s]?based', text): support.add('income')
    if re.search(r'minorit', text): support.add('minority')
    if re.search(r'disab|divyang|\bpwd\b|persons with disabilities', text): support.add('disability')
    if re.search(r'\bsport', text): support.add('sports')
    if re.search(r'\bsc\b|\bst\b|\bobc\b|scheduled (caste|tribe)|backward class|dnt\b', text): support.add('reserved')
    if gender: support.add('girls')

    t0 = cats[0].lower() if cats else ''
    pl = prov.lower()
    if t0 in ('nasa','harvard','switzerland','germany','australia') or any(k in pl for k in ['nasa','harvard']):
        ptype = 'international'
    elif 'csr' in t0 or t0 == 'private':
        ptype = 'corporate'
    elif 'private foundation' in t0 or t0 == 'trust' or any(k in pl for k in ['foundation','trust','ngo']):
        ptype = 'foundation'
    elif 'government' in t0 or t0 in ('odisha','himachal pradesh','west bengal','chhattisgarh') or \
         any(k in pl for k in ['ministry','aicte','icar','iit ','isi ','government']):
        ptype = 'government'
    elif 'international' in text and 'national' not in t0:
        ptype = 'international'
    else:
        ptype = 'other'

    days = (dl - TODAY).days if dl else None
    items.append(dict(
        id=f.stem, file=f.name, title=title, provider=prov, ptype=ptype,
        cats=cats, award=award, awardMax=award_max(award), who=who,
        dlRaw=dl_raw, dl=dl.isoformat() if dl else None, days=days,
        closed=days is not None and days < 0, logo=logo,
        verified=verified, srcUrl=src_url, srcLabel=src_label, sub=sub,
        edu=sorted(edu), states=sorted(states), gender=gender, support=sorted(support),
    ))

items.sort(key=lambda d: (d['days'] is None, d['days'] if d['days'] is not None else 0))
json.dump(items, open(ROOT / 'site-data.json', 'w'), indent=1, ensure_ascii=False)

print('total:', len(items))
print('closed already:', sum(1 for d in items if d['closed']))
print('no deadline:', sum(1 for d in items if d['dl'] is None))
print('edu coverage:', dict(Counter(e for d in items for e in d['edu'])))
print('states found:', sorted({s for d in items for s in d['states'] if s != 'National'}))
print('national:', sum(1 for d in items if 'National' in d['states']), '| no state:', sum(1 for d in items if not d['states']))
print('support:', dict(Counter(s for d in items for s in d['support'])))
print('ptype:', dict(Counter(d['ptype'] for d in items)))
print('awardMax parsed:', sum(1 for d in items if d['awardMax']))

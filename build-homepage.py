#!/usr/bin/env python3
"""Build the deploy-ready scholarships.studydesk.fun homepage (index.html)
from the 50 written article files.

Rerun whenever new batches land:
    python3 build-homepage.py

Outputs:
  - ../news-redesign/schol-home-v6.html (template refreshed with real data)
  - ../your_files/scholarships-subdomain-deploy-2026-10-16.zip
      (index.html + 50 articles + logos/ — unzip into the subdomain web root)

Honest rules baked in:
  - every stat, count, ticker item and notice-board entry comes from the
    actual article files; nothing from the old 111-finder catalog
  - deadline pills are recomputed by page JS on load from data-deadline,
    so they never go stale
"""
import re, glob, html as ihtml, json, zipfile, os, sys
from datetime import date

ART = os.path.join(os.path.dirname(__file__), "articles")
TPL = os.path.expanduser("~/workspace/news-redesign/schol-home-v6.html")
OUT_ZIP = os.path.expanduser("~/workspace/your_files/scholarships-subdomain-deploy-2026-10-16.zip")
TODAY = date(2026, 10, 16)

sys.path.insert(0, os.path.dirname(__file__))
from cards_registry import CARDS

MONTHS = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,
          "jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}

SPECIAL_DEADLINES = {
    "dakshana-scholarship-jdst-2027.html": ("2026-11-30", "30 Nov 2026"),
    "epfl-summer-internship-2027.html": ("2026-11-01", "1 & 15 Nov 2026"),
    "super-50-by-aayam-neet-jee-2026-27.html": ("2026-11-05", "5 Nov 2026"),
}

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()

def parse_deadline(txt):
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3,9})\s+(\d{4})", txt)
    if not m:
        return None
    d, mon, y = int(m.group(1)), MONTHS[m.group(2).lower()[:3]], int(m.group(3))
    try:
        return date(y, mon, d)
    except ValueError:
        return None

def pill_days(dl):
    n = (dl - TODAY).days
    if n < 0:   return "Closed"
    if n == 0:  return "Closes today"
    if n == 1:  return "1 day to go"
    return f"{n} days to go"

def short_title(t):
    # card titles like Buddy4Study: short name + year
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    return t

items = []
for f in sorted(glob.glob(os.path.join(ART, "*.html"))):
    slug = os.path.basename(f)
    src = open(f, encoding="utf-8").read()

    # article nav: fix the /#closing anchor to match the homepage section id
    if 'href="/#closing"' in src:
        src = src.replace('href="/#closing"', 'href="/#scholarships"')
        open(f, "w", encoding="utf-8").write(src)

    h1 = strip_tags(re.search(r"<h1>(.*?)</h1>", src, re.S).group(1))
    mp = re.search(r'<div><strong>([^<]+)</strong><span>', src)
    provider = mp.group(1).strip() if mp else "StudyDesk"
    lg = re.search(r'plogo lg monogram[^"]*">(.*?)</span>', src, re.S)
    lg_inner = lg.group(1) if lg else ""
    limg = re.search(r'<img src="([^"]+)"', lg_inner)
    logo = limg.group(1) if limg else None
    mono = re.sub(r"<[^>]+>", "", lg_inner).strip() or provider[0]

    dm = re.search(r'<div class="k">Deadline</div><div class="v">(.*?)<small>', src, re.S)
    dl_txt = strip_tags(dm.group(1)) if dm else None
    if slug in SPECIAL_DEADLINES:
        dl_iso, dl_txt = SPECIAL_DEADLINES[slug]
        dl = date(*map(int, dl_iso.split("-")))
    else:
        dl = parse_deadline(dl_txt or "")
        dl_iso = dl.isoformat() if dl else "9999-12-31"
    am = re.search(r'<div class="k">Award</div><div class="v">(.*?)<small>', src, re.S)
    award = strip_tags(am.group(1)) if am else ""
    am_full = re.search(r'<div class="k">Award</div><div class="v">(.*?)</div>', src, re.S)
    award_full = strip_tags(am_full.group(1)) if am_full else award
    em = re.search(r'<div class="k">Who can apply</div><div class="v">(.*?)<small>', src, re.S)
    elig = strip_tags(em.group(1)) if em else ""
    em_full = re.search(r'<div class="k">Who can apply</div><div class="v">(.*?)</div>', src, re.S)
    elig_full = strip_tags(em_full.group(1)) if em_full else elig
    um = re.search(r"Updated (\d{1,2} \w+ \d{4})", src)
    upd_txt = um.group(1) if um else "16 Oct 2026"
    d, mo, y = upd_txt.split()
    upd_iso = f"{y}-{MONTHS[mo.lower()[:3]]:02d}-{int(d):02d}"
    fm = re.search(r'<div class="facts rv">(.*?)</div>\s*<div class="alayout">', src, re.S)
    facts_text = strip_tags(fm.group(1)) if fm else ""
    h2m = re.findall(r"<h2[^>]*>([^<]+)</h2>", src)
    full_text = " ".join([h1] + [facts_text])

    tags = []
    for key, c in CARDS.items():
        if c.get("href") == slug:
            tags = [t for t, _ in c.get("tags", [])]
            break
    search = " ".join([h1, provider, award_full, elig_full] + tags)
    items.append(dict(slug=slug, title=h1, provider=provider, logo=logo, mono=mono,
                      dl=dl, dl_iso=dl_iso, dl_txt=dl_txt or "See official portal",
                      award=award, elig=elig, elig_full=elig_full, award_full=award_full,
                      upd_iso=upd_iso, upd_txt=upd_txt, full=full_text,
                      search=search))

items.sort(key=lambda x: x["dl_iso"])
open_now = [i for i in items if i["dl"] and i["dl"] >= TODAY]
closed = [i for i in items if i["dl"] and i["dl"] < TODAY]
closing30 = [i for i in items if i["dl"] and 0 <= (i["dl"] - TODAY).days <= 30]
print(f"parsed {len(items)} articles; open now {len(open_now)}; closing<=30d {len(closing30)}; already closed {len(closed)}")
for i in closed:
    print("  CLOSED:", i["slug"], i["dl_iso"], i["dl_txt"])

# ---------- card html ----------
TROPHY = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
          'stroke-linecap="round" stroke-linejoin="round"><path d="M7 4h10v5a5 5 0 0 1-10 0V4z"/>'
          '<path d="M7 5.5H4.5a3 3 0 0 0 3.2 4.8M17 5.5h2.5a3 3 0 0 1-3.2 4.8M12 14v3.5M8.5 21h7M9.5 17.5h5"/></svg>')
PERSON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
          'stroke-linecap="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.8 20a7.2 7.2 0 0 1 14.4 0"/></svg>')

def esc(s):
    return ihtml.escape(ihtml.unescape(s or ""), quote=True)

def card(it):
    pill = pill_days(it["dl"]) if it["dl"] else "See official portal"
    pill_cls = 'dpill check' if (it["dl"] and it["dl"] < TODAY) else 'dpill'
    if it["logo"]:
        logo_html = (f'<span class="plogo"><img src="{esc(it["logo"])}" alt="{esc(it["provider"])} logo" '
                     f'loading="lazy" onerror="this.parentNode.classList.add(\'monofb\');this.remove()">{esc(it["mono"])}</span>')
    else:
        logo_html = f'<span class="plogo monofb">{esc(it["mono"])}</span>'
    return (f'<article class="scard" data-search="{esc(it["search"].lower())}" '
            f'data-deadline="{it["dl_iso"].replace("-", "")}" data-updated="{it["upd_iso"]}">\n'
            f'  <div class="scard-top">\n    {logo_html}\n'
            f'    <span class="{pill_cls}" data-d="{it["dl_iso"]}">{esc(pill)}</span>\n  </div>\n'
            f'  <h3><a href="{esc(it["slug"])}">{esc(short_title(it["title"]))}</a></h3>\n'
            f'  <div class="spec">\n'
            f'    <div class="spec-row"><span class="spec-ic" aria-hidden="true">{TROPHY}</span>'
            f'<div><strong>Award</strong><p>{esc(it["award"])}</p></div></div>\n'
            f'    <div class="spec-row"><span class="spec-ic" aria-hidden="true">{PERSON}</span>'
            f'<div><strong>Eligibility</strong><p>{esc(it["elig"])}</p></div></div>\n'
            f'  </div>\n'
            f'  <div class="scard-foot">\n'
            f'    <a class="view" href="{esc(it["slug"])}">View Details <span aria-hidden="true">&rarr;</span></a>\n'
            f'    <small><span class="vdot"></span>Last Updated On {it["upd_iso"][8:]}-{it["upd_iso"][5:7]}-{it["upd_iso"][:4]}</small>\n'
            f'  </div>\n</article>')

cards_html = "\n".join(card(i) for i in items)

# ---------- browse counts (heuristic, from real article text) ----------
def has(rx, t): return bool(re.search(rx, t, re.I))
def blob(i): return " ".join([i["title"], i["full"]])

by_class = [
    ("Class 9\u201310", lambda i: has(r"class 9|class 10|pre-?matric|classes? 9", blob(i))),
    ("Class 11\u201312", lambda i: has(r"class 11|class 12|post-?matric|higher secondary|class 12 science", blob(i))),
    ("Undergraduate", lambda i: has(r"\bug\b|undergraduate|bachelor|mbbs|bds|b\.?tech|engineering|graduation", blob(i))),
    ("Postgraduate", lambda i: has(r"\bpg\b|postgraduate|master'?s|m\.?phil|ph\.?d|phd|mba|llm", blob(i))),
    ("Diploma / ITI", lambda i: has(r"diploma|iti\b|polytechnic", blob(i))),
]
STATES = ["Bihar","Uttar Pradesh","Maharashtra","West Bengal","Odisha","Sikkim","Meghalaya",
          "Goa","Chhattisgarh","Chandigarh","Himachal Pradesh","Madhya Pradesh","Punjab",
          "Rajasthan","Karnataka","Tamil Nadu","Kerala","Assam","Jharkhand","Gujarat",
          "Haryana","Telangana","Andhra Pradesh","Manipur","Tripura"]
def states_of(i):
    b = blob(i)
    found = [s for s in STATES if re.search(r"\b"+re.escape(s)+r"\b", b, re.I)]
    return found or ["All India"]
by_cat = [
    ("Girls / Women", lambda i: has(r"\bgirl|women|female|daughter", blob(i))),
    ("Merit based", lambda i: has(r"merit|talent|\d+%|topper|rank", blob(i))),
    ("Income based", lambda i: has(r"income|ews|economically", blob(i))),
    ("SC / ST / OBC", lambda i: has(r"\bsc\b|\bst\b|\bobc\b|scheduled|minority", blob(i))),
    ("Disability", lambda i: has(r"disab|pwd|benchmark", blob(i))),
]
class_counts = [(n, sum(1 for i in items if fn(i))) for n, fn in by_class]
from collections import Counter
sc = Counter()
for i in items:
    for s in states_of(i): sc[s] += 1
state_top = [(s, c) for s, c in sc.most_common() if s != "All India"][:4]
state_counts = state_top + [("All India", sc.get("All India", 0))]
cat_counts = [(n, sum(1 for i in items if fn(i))) for n, fn in by_cat]
print("class:", class_counts); print("state:", state_counts); print("cat:", cat_counts)

# ---------- ticker / notice board ----------
near = [i for i in open_now if i["dl"]]
ticker = near[:4]
notice = near[:6]

def ticker_html(it):
    n = (it["dl"] - TODAY).days
    return (f'<a href="{esc(it["slug"])}"><b>{it["dl"].day} {it["dl"].strftime("%b")}</b> '
            f'\u00b7 {esc(short_title(it["title"]))} closes in {n} days</a>')

def notice_html(it):
    d = it["dl"]
    return (f'<a href="{esc(it["slug"])}"><span class="nt">{esc(short_title(it["title"]))}</span>'
            f'<span class="nd">{d.day} {d.strftime("%b")} {d.year}</span></a>')

# ---------- assemble (idempotent: every region is re-replaced on each run) ----------
tpl = open(TPL, encoding="utf-8").read()
n = len(items)

def sub1(rx, repl, s):
    ns, cnt = re.subn(rx, repl, s, count=1, flags=re.S)
    return ns

# --- cards ---
cards_html = "\n".join(card(i) for i in items)
if "<!--CARDS-->" in tpl:
    tpl = sub1(r"<!--CARDS-->.*?<!--/CARDS-->",
               "<!--CARDS-->\n" + cards_html + "\n<!--/CARDS-->", tpl)
else:
    tpl = sub1(r'(<div class="cards" id="cards">)\s*.*?(<p class="empty" id="empty">)',
               r"\1\n<!--CARDS-->\n" + cards_html + r"\n<!--/CARDS-->\n    \2", tpl)

# --- counts / copy ---
tpl = sub1(r'<title>StudyDesk Scholarships 2026\u201327: [^<]*</title>',
           f'<title>StudyDesk Scholarships 2026\u201327: {n} Verified Scholarships for Indian Students</title>', tpl)
tpl = sub1(r'<meta name="description" content="\d+ scholarships verified against official sources[^"]*">',
           f'<meta name="description" content="{n} scholarships verified against official sources. Real deadlines, real eligibility, official application links. No account needed.">', tpl)
tpl = sub1(r'<span class="pill"><span class="dot"></span>\d+ scholarships \u00b7 verified',
           f'<span class="pill"><span class="dot"></span>{n} scholarships \u00b7 verified', tpl)
tpl = sub1(r'<div class="n">\d+</div><div class="l">Verified scholarships</div>',
           f'<div class="n">{n}</div><div class="l">Verified scholarships</div>', tpl)
tpl = sub1(r'<div class="n"><em>\d+</em></div><div class="l">Open now</div>',
           f'<div class="n"><em>{len(open_now)}</em></div><div class="l">Open now</div>', tpl)
tpl = sub1(r'<div class="n"><em>\d+</em></div><div class="l">Closing in 30 days</div>',
           f'<div class="n"><em>{len(closing30)}</em></div><div class="l">Closing in 30 days</div>', tpl)
tpl = sub1(r'Not from a list of \d+ names\.',
           f'Not from a list of {n} names.', tpl)
tpl = sub1(r'Showing <strong>\d+</strong> of \d+',
           f'Showing <strong>{n}</strong> of {n}', tpl)
by_oct31 = [i for i in near if i["dl"] <= date(2026, 10, 31)]
tpl = sub1(r'(Four major scholarships close on 31 October|\d+ scholarships close by 31 October)\.?[^<]*',
           f'{len(by_oct31)} scholarships close by 31 October. Check the official portal and apply in time.', tpl)

# --- ticker: real nearest deadlines ---
tick = '<div class="track" id="tickerTrack">\n      ' + "\n      ".join(ticker_html(i) for i in ticker) + "\n    </div>"
tpl = sub1(r'<div class="track" id="tickerTrack">.*?</div>\s*</div>', tick + "\n  </div>", tpl)

# --- notice board: real nearest deadlines ---
notices = "\n        ".join(notice_html(i) for i in notice)
tpl = sub1(r'<div class="notice-list">.*?</div>\s*</div>\s*</section>',
           '<div class="notice-list">\n        ' + notices + "\n      </div>\n    </div>\n  </section>", tpl)

# --- browse panels: real counts, wired to search ---
def panel(name, counts, queries):
    lis = "\n          ".join(
        f'<li><a href="#scholarships" data-q="{esc(q)}">{esc(nm)} <span class="cnt">{c}</span></a></li>'
        for (nm, c), q in zip(counts, queries))
    return f"<!--{name}-->\n        <ul>\n          {lis}\n        </ul>\n        <!--/{name}-->"
panels = [
    ("BROWSE-CLASS", class_counts, ["class 9", "class 11", "undergraduate", "postgraduate", "diploma"]),
    ("BROWSE-STATE", state_counts, [s.lower() for s, _ in state_counts]),
    ("BROWSE-CAT", cat_counts, ["girls", "merit", "income", "sc", "disability"]),
]
sec_m = re.search(r'<section class="sec tint" id="browse">.*?</section>', tpl, re.S)
if sec_m:
    sec = sec_m.group(0)
    uls = list(re.finditer(r"(?:<!--BROWSE-\w+-->\s*)?<ul>.*?</ul>(?:\s*<!--/BROWSE-\w+-->)?", sec, re.S))
    assert len(uls) == 3, f"expected 3 browse ULs, found {len(uls)}"
    new_sec = sec
    for (name, counts, queries), um in zip(panels, reversed(uls)):
        new_sec = new_sec[:um.start()] + panel(name, counts, queries) + new_sec[um.end():]
    tpl = tpl.replace(sec, new_sec)

# --- footer / header dead links -> honest targets (once) ---
if '<a href="#">About</a>' in tpl:
    tpl = tpl.replace('<a href="#">About</a><a href="#">Editorial policy</a><a href="#">Corrections</a><a href="#">Contact</a>',
                      '<a href="https://studydesk.fun/about/">About</a><a href="https://wa.me/919905166009">Contact</a>')
if '<a href="#">Privacy</a>' in tpl:
    tpl = tpl.replace('<a href="#">Privacy</a><a href="#">Terms of use</a><a href="#">Cookies</a>',
                      '<a href="https://studydesk.fun/privacy.php">Privacy</a><a href="https://studydesk.fun/privacy.php">Terms &amp; Cookies</a>')
if '<a class="btn btn-amber" href="#">Get deadline alerts</a>' in tpl:
    tpl = tpl.replace('<a class="btn btn-amber" href="#">Get deadline alerts</a>',
                      '<a class="btn btn-amber" href="#alerts">Get deadline alerts</a>')

# --- JS: category links drive search; pills recompute on load (guarded) ---
CAT_JS = '''Array.prototype.forEach.call(document.querySelectorAll(".cat a[data-q]"), function(link){
    link.addEventListener("click", function(){ q.value = link.getAttribute("data-q"); applyAll(); });
  });
  '''
if 'cat a[data-q]' not in tpl:
    tpl = tpl.replace('''Array.prototype.forEach.call(document.querySelectorAll(".qchip"), function(chip){''',
                      CAT_JS + '''Array.prototype.forEach.call(document.querySelectorAll(".qchip"), function(chip){''')
PILL_JS = '''  var today = new Date(); today.setHours(0,0,0,0);
  Array.prototype.forEach.call(document.querySelectorAll(".dpill[data-d]"), function(p){
    var parts = p.getAttribute("data-d").split("-");
    if(parts[0] === "9999") return;
    var d = new Date(+parts[0], +parts[1]-1, +parts[2]);
    var n = Math.round((d - today) / 86400000);
    p.textContent = n < 0 ? "Closed" : n === 0 ? "Closes today" : n === 1 ? "1 day to go" : n + " days to go";
    if(n < 0) p.classList.add("check");
  });
'''
if 'dpill[data-d]' not in tpl:
    tpl = tpl.replace('''  var wa = document.querySelector(".wa-float");''',
                      PILL_JS + '''  var wa = document.querySelector(".wa-float");''')
tpl = tpl.replace(".plogo img{max-width:100%;max-height:100%;object-fit:contain}",
                  ".plogo img{max-width:100%;max-height:100%;object-fit:contain}\n"
                  ".plogo.monofb{font-weight:800;color:var(--navy);font-size:18px}") \
    if ".plogo.monofb" not in tpl else tpl

open(TPL, "w", encoding="utf-8").write(tpl)
print("template written:", TPL, os.path.getsize(TPL), "bytes")

# ---------- deploy zip: index.html + articles + logos ----------
with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(TPL, "index.html")
    for f in sorted(glob.glob(os.path.join(ART, "**"), recursive=True)):
        rel = os.path.relpath(f, ART)
        if os.path.isfile(f):
            z.write(f, rel)
print("zip written:", OUT_ZIP, os.path.getsize(OUT_ZIP), "bytes")

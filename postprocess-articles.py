#!/usr/bin/env python3
"""Idempotent post-processing for all articles:
1. provider names + logos (via add-logos.py)
2. real StudyDesk logo in masthead wordmark
3. 'Get alerts' #alerts -> #deadline-alert
4. dead 'Remind me' button -> working WhatsApp CTA
5. subdomain nav links (/scholarships/ -> /, footer cats -> /#browse, /about/ -> main site)
6. canonical link (idempotent; pilot drafts skipped; homepage -> site root)
7. Google AdSense "articles" unit (idempotent; article pages only — pilots
   and the homepage are skipped; unit placed after the intro <p class="sub">,
   so it sits in article content, not on policy/404/app pages)
8. strip the old "Design prototype, not the live page" footer line
   (baked into the BASE template; must never ship on a live page)
9. correct the status badge: "Closed" (red) when site-data says the deadline
   has passed or the deadline pill says Closed — never "Open" on a closed page
10. mobile UI fixes (31 Oct 2026): masthead fits a 390px screen (no clipped
    "Get alerts" button) and the vertical "Need Help?" tab is hidden on mobile
    (it overlapped body text; the WhatsApp float already covers help there)
11. validation
"""
import re, pathlib, subprocess, sys, html as htmllib, urllib.parse
from html.parser import HTMLParser

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'

# 1. provider names + logos
print('== add-logos.py ==')
r = subprocess.run([sys.executable, str(ROOT / 'add-logos.py')], capture_output=True, text=True, cwd=str(ROOT))
print(r.stdout[-500:] if r.stdout else '', r.stderr[-300:] if r.stderr else '')

n_wm = n_alerts = n_remind = n_nav = n_status = 0
# 9. status badge source: site-data.json closed flag (deadline vs today)
import json as _json
_closed = {}
try:
    for _d in _json.load(open(ROOT / 'site-data.json')):
        if _d.get('closed'):
            _closed[_d['id']] = True
except Exception:
    _closed = {}
for f in sorted(ART.glob('*.html')):
    html = f.read_text()
    # 2. wordmark logo
    old_wm = '<a class="wordmark" href="/">StudyDesk <em>Scholarships</em></a>'
    if old_wm in html:
        html = html.replace(old_wm,
            '<a class="wordmark" href="/"><img src="logos/studydesk.png" alt="StudyDesk" width="34" height="34">StudyDesk <em>Scholarships</em></a>', 1)
        n_wm += 1
    old_css = '.wordmark{font-family:var(--serif);font-weight:700;font-size:22px;letter-spacing:-.01em;color:var(--ink);white-space:nowrap;text-decoration:none}'
    if old_css in html:
        html = html.replace(old_css,
            '.wordmark{display:inline-flex;align-items:center;gap:10px;font-family:var(--serif);font-weight:700;font-size:22px;letter-spacing:-.01em;color:var(--ink);white-space:nowrap;text-decoration:none}'
            '.wordmark img{width:34px;height:34px;border-radius:9px;box-shadow:0 4px 10px -4px rgba(79,70,229,.5)}', 1)
    # 3. alerts anchor
    if 'href="#alerts"' in html:
        html = html.replace('href="#alerts"', 'href="#deadline-alert"')
        n_alerts += 1
    # 4. remind-me CTA
    old_rm = '<p>Get a reminder 7 days and 1 day before this deadline, by browser notification or email.</p>\n        <a class="btn" href="#">Remind me</a>'
    if old_rm in html:
        h1 = re.sub(r'<[^>]+>', '', re.search(r'<h1>(.*?)</h1>', html, re.S).group(1)).strip()
        dl = re.search(r'<h3>Deadline: (.*?)</h3>', html).group(1)
        msg = 'Hi StudyDesk, please remind me about the %s deadline (%s).' % (htmllib.unescape(h1), dl)
        url = 'https://wa.me/919905166009?text=' + urllib.parse.quote(msg)
        html = html.replace(old_rm,
            '<p>Want a nudge before this deadline? Tap below and send us the message — we\'ll remind you on WhatsApp.</p>\n        <a class="btn" href="%s">Remind me on WhatsApp</a>' % url, 1)
        n_remind += 1
    # 5. subdomain nav
    c1 = len(re.findall(r'href="/scholarships/"', html)); html = re.sub(r'href="/scholarships/"', 'href="/"', html)
    c2 = len(re.findall(r'href="/scholarships/[a-z0-9-]+/"', html)); html = re.sub(r'href="/scholarships/[a-z0-9-]+/"', 'href="/#browse"', html)
    c3 = len(re.findall(r'href="/about/"', html)); html = re.sub(r'href="/about/"', 'href="https://studydesk.fun/about/"', html)
    n_nav += (c1 + c2 + c3)
    # fix double-encoded entities in titles
    html = html.replace('&amp;amp;', '&amp;')
    # 8. strip "Design prototype" footer (never ship on a live page)
    html = html.replace('© 2026 StudyDesk Scholarships · Design prototype, not the live page',
                        '© 2026 StudyDesk Scholarships')
    # 9. status badge: Closed when the deadline has passed
    if f.name != 'index.html' and not f.name.startswith('pilot-'):
        _dl = re.search(r'<span class="dline">(.*?)</span>', html)
        _is_closed = _closed.get(f.stem) or (_dl and 'losed' in _dl.group(1))
        _cur = re.search(r'<span class="status(?: closed)?">([^<]*)</span>', html)
        if _is_closed and _cur and _cur.group(1) != 'Closed':
            html = html.replace(_cur.group(0), '<span class="status closed">Closed</span>', 1)
            n_status += 1
        if _is_closed and '.status.closed{' not in html and '</style>' in html:
            html = html.replace('</style>', '.status.closed{color:#b91c1c;background:#fee2e2}\n</style>', 1)
    # 10. mobile UI fixes: masthead fits 390px, vertical help tab hidden on mobile
    if f.name != 'index.html' and not f.name.startswith('pilot-'):
        if '.help-tab{display:none}' not in html:
            html = html.replace('@media(max-width:860px){.masthead nav{display:none}}',
                '@media(max-width:860px){.masthead nav{display:none}.masthead-in{gap:12px;padding:0 16px}.wordmark{font-size:19px}.shell{padding:0 16px}.help-tab{display:none}}', 1)
    # 7. AdSense articles unit (article pages only; homepage/pilots skipped)
    if (not f.name.startswith('pilot-') and f.name != 'index.html'
            and 'adsbygoogle' not in html):
        m_sub = re.search(r'(<p class="sub">.*?</p>)', html, re.S)
        if m_sub:
            unit = ('\n<!-- Google AdSense articles unit -->\n'
                    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3573504055334993"\n'
                    '     crossorigin="anonymous"></script>\n'
                    '<ins class="adsbygoogle"\n'
                    '     style="display:block"\n'
                    '     data-ad-client="ca-pub-3573504055334993"\n'
                    '     data-ad-slot="4630994583"\n'
                    '     data-ad-format="auto"\n'
                    '     data-full-width-responsive="true"></ins>\n'
                    '<script>\n'
                    '     (adsbygoogle = window.adsbygoogle || []).push({});\n'
                    '</script>')
            html = html[:m_sub.end()] + unit + html[m_sub.end():]
    # 6. canonical (pilot drafts are not production pages, so skip them)
    if not f.name.startswith('pilot-'):
        canon = ('https://scholarships.studydesk.fun/' if f.name == 'index.html'
                 else 'https://scholarships.studydesk.fun/' + f.name)
        tag = '<link rel="canonical" href="%s">' % canon
        if re.search(r'<link rel="canonical"[^>]*>', html):
            html = re.sub(r'<link rel="canonical"[^>]*>', tag, html, count=1)
        elif '<meta name="description"' in html:
            html = html.replace('<meta name="description"', tag + '\n<meta name="description"', 1)
        elif '</head>' in html:
            html = html.replace('</head>', tag + '\n</head>', 1)
    f.write_text(html)

print('wordmark: %d | alerts: %d | remind: %d | nav: %d | status-fixed: %d' % (n_wm, n_alerts, n_remind, n_nav, n_status))

# 6. validation
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack = []; self.bad = False
    def handle_starttag(self, t, a):
        if t not in ('meta','link','br','img','input','hr','source'): self.stack.append(t)
    def handle_endtag(self, t):
        if self.stack and self.stack[-1] == t: self.stack.pop()
        else: self.bad = True
problems = []
for f in sorted(ART.glob('*.html')):
    h = f.read_text(); p = P(); p.feed(h)
    issues = []
    if p.stack or p.bad: issues.append('parse')
    if 'wa.me/919905166009' not in h: issues.append('no-whatsapp')
    if 'href="#"' in h: issues.append('dead-link')
    if 'AICTE Pragati' in h and 'pragati' not in f.name: issues.append('template-text')
    if issues: problems.append((f.name, issues))
print('validated %d articles, problems: %s' % (len(list(ART.glob('*.html'))), problems if problems else 'none'))

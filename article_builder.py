import re
import html as htmllib
TROPHY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4h10v5a5 5 0 0 1-10 0V4z"/><path d="M7 5.5H4.5a3 3 0 0 0 3.2 4.8M17 5.5h2.5a3 3 0 0 1-3.2 4.8M12 14v3.5M8.5 21h7M9.5 17.5h5"/></svg>'
PERSON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.8 20a7.2 7.2 0 0 1 14.4 0"/></svg>'

def scard(mono, title, href, dpill, award, elig, tags):
    taghtml = ''.join(f'<span class="tag {c}">{t}</span>' for t, c in tags)
    return f'''<article class="scard rv">
        <div class="scard-top">
          <span class="plogo monogram">{mono}</span>
          <span class="dpill ">{dpill}</span>
        </div>
        <h3><a href="{href}">{title}</a></h3>
        <div class="spec">
          <div class="spec-row"><span class="spec-ic" aria-hidden="true">{TROPHY}</span><div><strong>Award</strong><p>{award}</p></div></div>
          <div class="spec-row"><span class="spec-ic" aria-hidden="true">{PERSON}</span><div><strong>Eligibility</strong><p>{elig}</p></div></div>
        </div>
        <div class="tags">{taghtml}</div>
        <div class="scard-foot">
          <a class="view" href="{href}">View details →</a>
          <small><span class="verified">✓ Verified</span> · 16 Oct 2026</small>
        </div>
      </article>'''

def facts(items):
    return ''.join(
        f'<div class="fact"><div class="k">{k}</div><div class="v">{v}</div></div>'
        for k, v in items)

def faqs(pairs):
    return ''.join(
        f'<div class="faq"><div class="q">{q}</div><p>{a}</p></div>'
        for q, a in pairs)


MONO_CSS = ('.plogo.monogram{background:linear-gradient(135deg,#1a2145,#2e4a8f);color:#fff;'
            'font-weight:800;font-size:15px;letter-spacing:.02em;padding:0;border:0}'
            '.plogo.monogram.lg{font-size:20px}')

def build_article(BASE, OUT, a, CARDINFO):
    page = BASE
    page = re.sub(r'<title>.*?</title>', f"<title>{htmllib.escape(a['title'])}</title>", page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content=".*?">',
                  f'<meta name="description" content="{htmllib.escape(a["meta"])}">', page, count=1)
    page = page.replace('</style>', MONO_CSS + '.status.closed{color:#b91c1c;background:#fee2e2}' + '\n</style>', 1)
    page = re.sub(r'(<p class="crumbs">.*?<span>/</span>)AICTE Pragati Scholarship 2026\u201327</p>',
                  r'\g<1>' + htmllib.escape(a['short']) + '</p>', page, count=1, flags=re.S)
    page = re.sub(r'<p class="kicker">.*?</p>', f'<p class="kicker">{a["kicker"]}</p>', page, count=1, flags=re.S)
    page = re.sub(r'<span class="plogo lg"><img src="data:image/[^"]*"[^>]*></span>',
                  f'<span class="plogo lg monogram">{a["mono"]}</span>', page, count=1)
    page = re.sub(r'(<div class="prov-row">.*?</span>\s*<div>\s*<strong>).*?(</strong>)',
                  r'\g<1>' + htmllib.escape(a['prov_short']) + r'\g<2>', page, count=1, flags=re.S)
    page = re.sub(r'(<div class="prov-row">.*?</strong>\s*<span>).*?(</span>\s*</div>\s*</div>)',
                  r'\g<1>' + htmllib.escape(a.get('prov_cat', 'Scholarship Provider')) + r'\g<2>', page, count=1, flags=re.S)
    page = re.sub(r'<h1>.*?</h1>', f"<h1>{htmllib.escape(a['h1'])}</h1>", page, count=1, flags=re.S)
    page = re.sub(r'<p class="sub">.*?</p>', f'<p class="sub">{a["sub"]}</p>', page, count=1, flags=re.S)
    # Status badge must match the deadline pill — never hardcode "Open" again
    # (closed articles shipped with "Closed <date>" + an "Open" badge, 31 Oct 2026).
    _dp = a["dpill"].lower()
    _status = 'Closed' if 'closed' in _dp else ('Closes today' if 'today' in _dp else 'Open')
    _cls = ' class="status closed"' if _status == 'Closed' else ' class="status"'
    newmeta = (f'<div class="meta-row">\n      <span class="dline">{a["dpill"]}</span>\n'
               f'      <span{_cls}>{_status}</span>\n      <span>Updated 16 Oct 2026</span>\n'
               f'      <span>By {htmllib.escape(a["prov_short"])}</span>\n    </div>')
    page = re.sub(r'<div class="meta-row">.*?</div>', newmeta, page, count=1, flags=re.S)
    page = re.sub(r'<div class="facts rv">.*?</div>\s*(?=<div class="alayout">)',
                  f'<div class="facts rv">\n{a["facts"]}\n    </div>\n    ', page, count=1, flags=re.S)
    start = page.find('<article class="abody">')
    end = page.find('</article>', start)
    newbody = '<article class="abody">\n' + a['body'] + '\n      <p class="verify">' + a['verify'] + '</p>\n    '
    page = page[:start] + newbody + page[end:]
    page = re.sub(r'(<div class="acard alert-card rv"[^>]*>\s*<h3>)Deadline: .*?(</h3>)',
                  r'\g<1>Deadline: ' + a['dl_long'] + r'\g<2>', page, count=1, flags=re.S)
    links = ''.join(
        f'<a class="offlink" href="{u}" rel="noopener"><span>{htmllib.escape(t)}</span><span>\u2192</span></a>'
        for t, u in a['offlinks'])
    page = re.sub(r'(<div class="acard offcard rv">.*?<p>Always confirm details on the official portal before applying\.</p>).*?(</div>\s*</aside>)',
                  r'\g<1>\n        ' + links + r'\n      \g<2>', page, count=1, flags=re.S)
    cards = '\n'.join(scard(**CARDINFO[k]) for k in a['related_titles'])
    page = re.sub(r'(<section class="related">.*?<div class="cards">).*?(</div>\s*</section>)',
                  r'\g<1>\n' + cards + r'\n    \g<2>', page, count=1, flags=re.S)
    page = page.replace('<a class="wa-float" href="#"',
                        '<a class="wa-float" href="https://wa.me/919905166009"', 1)
    assert 'AICTE Pragati' not in page, a['slug']
    assert 'data:image' not in page, a['slug'] + ' still has embedded images'
    assert '{{' not in page
    OUT.joinpath(a['slug'] + '.html').write_text(page)
    return len(page)

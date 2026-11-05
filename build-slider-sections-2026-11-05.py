#!/usr/bin/env python3
"""Slider + missing sections 2026-11-05 — CORPUS patch (one-shot).

Wires the featured slider that exists as an empty shell in the homepage
(#featured / #featSlider / #featTrack / featPrev / featNext / featDots)
and adds the sections Buddy4Study has that we honestly can: a fraud
warning banner and browse-by-state/level/type columns, plus a Terms of
Use page and footer links. Also makes homepage + article links relative
so the same files work at the domain root (live) and under
/scholarships-preview/ (GitHub Pages preview).

Root causes (verified 5 Nov 2026):
- The slider is empty because renderFeatured() only picks
  indiaClosing7() (Indian gov/corp/foundation closing within 7 days),
  which is currently empty, so the whole #featured section hides.
  It also has no auto-play (no setInterval anywhere) and its slides
  carry no logo even though the CSS designs a 200px .logo-big slot.
- The homepage has no fraud warning, no browse columns, no Terms page,
  and its footer has only a Privacy link.
- Absolute paths (/articles/logos/..., /privacy.html, href="/",
  href="/#...") break under the /scholarships-preview/ subpath.

What this does (backups under backups/slider-sections-2026-11-05/):
1. build-homepage-v9.py (builder) AND articles/index.html (live copy)
   get the SAME edits (logo-fix pattern — never regenerate index.html
   from the builder here: it appends NEW_CSS on every run):
   - NEW_CSS += fraud-bar, browse-column and slide-logo rules.
   - Fraud banner inserted under the header.
   - Featured section sub-text updated to the new selection.
   - Browse-columns section inserted after Guides, before How-it-works.
   - Footer: Privacy link relative + Terms + Sitemap links added.
   - Header/footer StudyDesk logo src /articles/... -> articles/...
   - Card/guide logo prefix '/articles/' -> 'articles/'.
   - renderFeatured(): 5 open scholarships closing soonest (ALL tabs,
     not India-only), each slide with monogram-or-logo (.logo-big,
     TINY_LOGOS respected), auto-play 5s with pause on hover/focus
     and on prefers-reduced-motion, prev/next + dots as before.
   - New: featStart/featStop, openCountWhere/bestTab,
     renderBrowseCols (State / Level / Type from real DATA with
     open-only counts), applyBrowse via the existing filter state
     (new S.ptype field, same pattern as edu/states/support), init
     calls renderBrowseCols and binds slider pause; [data-browse]
     click branch reuses resetAll + filterPanelHTML + render.
2. build-detail-v9.py: footer Privacy insert -> relative; the
   Bihar-drop regex matches the new index.html#browse form too; the
   footer-exists check now matches 'privacy.html' either form so a
   re-run cannot duplicate the Privacy link.
3. admin template.php: wordmark/nav/crumbs/footer hrefs -> relative
   (index.html, index.html#..., privacy.html). Canonical/og/srcUrl
   untouched (absolute live URLs by design).
4. All 418 article files (everything in articles/*.html except
   index.html, which is patched in step 1): href="/" -> index.html,
   href="/#x" -> index.html#x, href="/privacy.html" -> privacy.html.
   Canonical/og/srcUrl/sitemap untouched (different patterns).
5. privacy.html (corpus root): same relative-link pass + footer copy
   line gains Terms + Sitemap links (same as the homepage footer).
6. NEW terms.html at the corpus root, same pattern as privacy.html
   (standalone file, inline CSS, relative links throughout).

Deliberately NOT built: partner logo strip (no partners), testimonials
(no real scholar stories), predictor/loans/stream-selector tools
(no such tools — a fake control violates the product rule).

Run from ~/workspace/scholarships-17k. Exits non-zero on any anchor
miss. After it runs: node --check the touched inline JS (extracted),
grep counts, then rebuild the preview from the fixed corpus.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKUP = os.path.join(ROOT, 'backups', 'slider-sections-2026-11-05')
TPL = os.path.expanduser('~/workspace/scholarships-admin-panel-v2'
                         '/admin/lib/template.php')

NEW_RULES = """
/* ---- slider + browse columns + fraud banner (5 Nov 2026) ---- */
.fraudbar{background:#fff8e1;border-bottom:1px solid #f0d48a;color:#5b4300;font-size:14px}
.fraudbar-in{max-width:1220px;margin:0 auto;padding:10px 24px}
.fraudbar strong{color:#7a5200}
.slide .logo-big img{object-fit:contain;background:#fff;padding:10px;box-sizing:border-box}
.bcols{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:18px}
.bcol{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.bcol h3{font-size:17px;margin-bottom:8px}
.bcol ul{list-style:none}
.bcol li a{display:flex;gap:8px;align-items:baseline;padding:7px 0;color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.bcol li:last-child a{border-bottom:0}
.bcol li a:hover{color:var(--blue);text-decoration:underline}
.bcol a .c{margin-left:auto;color:var(--mut);font-size:13px;flex:none}
@media(max-width:900px){.bcols{grid-template-columns:1fr}}"""

FRAUD_HTML = '''<div class="fraudbar" role="note"><div class="fraudbar-in"><strong>Beware of fake scholarships.</strong> StudyDesk never asks for a fee, and applications always happen on the provider's official website — never here and never through an agent.</div></div>'''

BROWSE_HTML = '''<section class="browsecols" id="browseCols" aria-label="Browse scholarships by category"><div class="sec-kick">Browse</div><h2 class="sec-title">Browse scholarships by state, level and type</h2><p class="sec-sub">Counts show open scholarships only, recomputed daily from each listing's own deadline.</p><div class="bcols" id="browseColsGrid"></div></section>'''

TERMS_HTML = """<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Terms of Use — StudyDesk Scholarships</title>
<link rel="canonical" href="https://scholarships.studydesk.fun/terms.html">
<meta name="description" content="Terms of Use for StudyDesk Scholarships: a free listing guide — no account, applications happen on official sites, deadlines must be confirmed on the official portal.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--navy:#141d45;--navy2:#1e2a63;--amber:#f5a524;--bg:#f3f1f9;--card:#ffffff;--ink:#1b1936;--mut:#5f5b7c;--line:#e3e0f1;--serif:'Fraunces',Georgia,'Times New Roman',serif;--sans:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);background:var(--bg);color:var(--ink);line-height:1.62;-webkit-font-smoothing:antialiased}
a{color:#2456e0}
:focus-visible{outline:3px solid #2456e0;outline-offset:2px;border-radius:6px}
.wrap{max-width:820px;margin:0 auto;padding:0 24px}
.hdr{background:rgba(255,255,255,.96);border-bottom:1px solid var(--line)}
.hdr-in{max-width:1220px;margin:0 auto;padding:0 24px;height:66px;display:flex;align-items:center;gap:11px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;color:var(--ink);font-family:var(--serif);font-weight:700;font-size:22px}
.brand img{width:34px;height:34px}
.brand small{display:block;font-family:var(--sans);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
main{padding:40px 0 60px}
h1{font-family:var(--serif);font-size:clamp(30px,4.5vw,44px);line-height:1.22;margin:8px 0 10px}
h2{font-family:var(--serif);font-size:22px;margin:28px 0 8px}
p{margin:0 0 12px}
ul{margin:0 0 12px 22px}
li{margin-bottom:6px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin:20px 0}
footer{border-top:1px solid var(--line);padding:26px 0}
.foot-in{max-width:1220px;margin:0 auto;padding:0 24px;display:flex;gap:28px;flex-wrap:wrap;justify-content:space-between}
.naff-line{max-width:1220px;margin:18px auto 0;padding:0 24px;color:var(--mut);font-size:14px}
.copy{max-width:1220px;margin:10px auto 0;padding:0 24px;display:flex;gap:18px;flex-wrap:wrap;font-size:14px;color:var(--mut)}
</style>
</head>
<body>
<header class="hdr"><div class="hdr-in"><a class="brand" href="index.html"><img src="articles/logos/studydesk.png" alt="StudyDesk logo"><span>StudyDesk<small>Scholarships</small></span></a></div></header>
<main><div class="wrap">
<h1>Terms of Use</h1>
<p>StudyDesk Scholarships is a free listing guide. These terms state plainly what this site is, what it does, and what it does not do.</p>

<h2>What this site is</h2>
<p>A guide to scholarships, fellowships and internships for Indian students and students applying abroad. Every listing is checked against the provider's own notification, portal or press release before publication, and each page shows the date it was checked. There is no account, no sign-in, and no profile on this site.</p>

<h2>Free to use</h2>
<p>There is nothing to pay for here. We never ask for a fee, and no one acting for us will ask for one either. Saving a scholarship to My plan stores it in your browser on your own device; nothing is uploaded.</p>

<h2>Applications happen elsewhere</h2>
<p>Applications always happen on the provider's own website or portal — never on StudyDesk Scholarships. We do not collect application forms, documents, or personal details for any scholarship. A link is called “Official source” only when it goes to the provider or a government portal; aggregator pages are labelled “Mentioned by”, never “Official source”.</p>

<h2>Accuracy and no guarantees</h2>
<p>Deadlines, amounts and eligibility change. We re-check listings against official sources, and deadlines on this site are recomputed daily from each listing's own date — but we cannot guarantee that a listing is current at the moment you read it. Always confirm the deadline, amount and eligibility on the official portal before applying. If you spot an error, tell us at <a href="mailto:scholarships@studydesk.fun">scholarships@studydesk.fun</a> and we will check it against the official source.</p>

<h2>Advertising</h2>
<p>Ads may be served by Google AdSense. Google may use cookies to serve ads on this site. We do not control Google's cookies; you can manage ad personalisation in your Google account settings and by clearing cookies in your browser.</p>

<div class="card">
<h2 style="margin-top:0">Not a government website</h2>
<p style="margin-bottom:0">StudyDesk is an independent education guide — not a government website and not affiliated with any provider listed here. Always confirm details on the official portal before applying.</p>
</div>

<h2>Contact</h2>
<p>Questions about these terms: <a href="mailto:scholarships@studydesk.fun">scholarships@studydesk.fun</a> or WhatsApp <a href="https://wa.me/919905166009">+91 99051 66009</a>.</p>
<p><a href="index.html">← Back to scholarships</a></p>
</div></main>
<footer><div class="foot-in"><div><a class="brand" href="index.html"><img src="articles/logos/studydesk.png" alt="StudyDesk logo"><span>StudyDesk<small>Scholarships</small></span></a></div><div><a href="index.html">All scholarships</a></div><div><a href="mailto:scholarships@studydesk.fun">scholarships@studydesk.fun</a></div></div><p class="naff-line">StudyDesk is an independent education guide — not a government website and not affiliated with any provider listed here.</p><div class="copy"><span>© 2026 StudyDesk</span><span>Shortlists are stored only in your browser. <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="sitemap.xml">Sitemap</a></span></div></footer>
</body>
</html>
"""


def rep(s, old, new, expect, label):
    n = s.count(old)
    assert n == expect, f'{label}: expected {expect}, got {n} for {old[:70]!r}'
    return s.replace(old, new)


def backup():
    os.makedirs(BACKUP, exist_ok=True)
    for rel in ['build-homepage-v9.py', 'build-detail-v9.py',
                'privacy.html']:
        src = os.path.join(ROOT, rel)
        dst = os.path.join(BACKUP, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    shutil.copy2(TPL, os.path.join(BACKUP, 'template.php.bak'))
    shutil.copytree(os.path.join(ROOT, 'articles'),
                    os.path.join(BACKUP, 'articles'), dirs_exist_ok=True)
    print('backup ->', BACKUP)

# ---------- JS blocks (builder APP_JS and index.html app JS are identical
# here — verified by the logo fix — so the same replacements work twice) ----------

OLD_RENDER_FEATURED = """function renderFeatured(){
  var sec=document.getElementById('featured'); if(!sec) return;
  featSlides=indiaClosing7().slice(0,4); featIdx=0;
  if(!featSlides.length){ sec.hidden=true; return; }
  sec.hidden=false;
  var track=document.getElementById('featTrack'); if(!track) return;
  track.innerHTML=featSlides.map(function(r,i){ var st=statusFor(r.dl); return '<div class="slide"'+(i===0?' role="tabpanel"':' hidden')+' aria-label="'+esc(cleanTitle(r.title))+'"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><h3><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></h3><p class="prov">'+esc(r.provider)+'</p><p class="saward">'+esc(awardShort(r))+'</p><p class="trust">Checked '+esc(r.verified)+'</p><div class="cta-row"><a class="btn btn-navy" href="'+esc(r.file)+'">View details</a></div></div>'; }).join('');
  var dots=document.getElementById('featDots'); if(dots) dots.innerHTML=featSlides.map(function(r,i){ return '<button type="button" role="tab" aria-selected="'+(i===0?'true':'false')+'" aria-label="Go to slide '+(i+1)+'" data-slide="'+i+'"></button>'; }).join('');
}"""

NEW_RENDER_FEATURED = """function renderFeatured(){
  var sec=document.getElementById('featured'); if(!sec) return;
  featSlides=DATA.filter(function(r){ return openDated(r); }).sort(soonestCmp).slice(0,5); featIdx=0;
  if(!featSlides.length){ sec.hidden=true; return; }
  sec.hidden=false;
  var track=document.getElementById('featTrack'); if(!track) return;
  track.innerHTML=featSlides.map(function(r,i){ var st=statusFor(r.dl); var initial=esc((r.provider||'S').trim().charAt(0).toUpperCase()); var logo=(r.logo&&!TINY_LOGOS[r.logo])?'<img src="articles/'+esc(r.logo)+'" alt="" loading="lazy" onerror="this.remove()">':''; return '<div class="slide"'+(i===0?' role="tabpanel"':' hidden')+' aria-label="'+esc(cleanTitle(r.title))+'"><div class="slide-main"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><h3><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></h3><p class="prov">'+esc(r.provider)+'</p><p class="saward">'+esc(awardShort(r))+'</p><p class="trust">Checked '+esc(r.verified)+'</p><div class="cta-row"><a class="btn btn-navy" href="'+esc(r.file)+'">View details</a></div></div><span class="logo-big">'+initial+logo+'</span></div>'; }).join('');
  var dots=document.getElementById('featDots'); if(dots) dots.innerHTML=featSlides.map(function(r,i){ return '<button type="button" role="tab" aria-selected="'+(i===0?'true':'false')+'" aria-label="Go to slide '+(i+1)+'" data-slide="'+i+'"></button>'; }).join('');
  featStart();
}"""

# Timer, pause, browse-column helpers, browse click handler. Inserted
# before renderBoard() so the function declarations are defined before
# init() runs (and featStart/featStop are also used by featGo).
NEW_JS_HELPERS = """var featTimer=null;
function featStart(){ if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return; featStop(); featTimer=setInterval(function(){ featGo(featIdx+1); },5000); }
function featStop(){ if(featTimer){ clearInterval(featTimer); featTimer=null; } }
function openCountWhere(tab,pred){ var n=0; DATA.forEach(function(r){ if(isGuide(r)) return; if(tabOf(r)!==tab) return; if(!isOpenR(r)) return; if(pred(r)) n++; }); return n; }
function bestTab(pred){ var tabs=['india','abroad','internships'], best='india', bn=-1; tabs.forEach(function(t){ var n=openCountWhere(t,pred); if(n>bn){ bn=n; best=t; } }); return {tab:best,count:bn}; }
function renderBrowseCols(){
  var grid=document.getElementById('browseColsGrid'); if(!grid) return;
  function item(label,tab,count,browse){ return {label:label,tab:tab,count:count,browse:browse}; }
  var states=STATE_LIST.map(function(s){ return item(s,'india',openCountWhere('india',function(r){ return (r.states||[]).indexOf(s)>=0; }),'state:'+s); }).filter(function(x){ return x.count>0; }).sort(function(a,b){ return b.count-a.count; }).slice(0,12);
  var edu=Object.keys(EDU_L).map(function(tag){ var b=bestTab(function(r){ return (r.edu||[]).indexOf(tag)>=0; }); return item(EDU_L[tag],b.tab,b.count,'edu:'+tag); }).filter(function(x){ return x.count>0; });
  var types=[['government','Government','india'],['corporate','Corporate','india'],['foundation','Foundation','india'],['international','International','abroad']].map(function(t){ return item(t[1],t[2],openCountWhere(t[2],function(r){ return r.ptype===t[0]; }),'ptype:'+t[0]); }).filter(function(x){ return x.count>0; });
  var ob=bestTab(function(r){ return r.ptype==='other'; }); if(ob.count>0) types.push(item('Other',ob.tab,ob.count,'ptype:other'));
  var ic=openCountWhere('internships',function(r){ return true; }); if(ic>0) types.push(item('Internships','internships',ic,'tab:internships'));
  function col(title,items){ var h='<div class="bcol"><h3>'+esc(title)+'</h3><ul>'; items.forEach(function(it){ h+='<li><a href="#results" data-browse="'+esc(it.browse)+'" data-tab="'+esc(it.tab)+'">'+esc(it.label)+' <span class="c">'+it.count+'</span></a></li>'; }); return h+'</ul></div>'; }
  grid.innerHTML=col('By state',states)+col('By level',edu)+col('By type',types);
}
"""


def patch_app_js(s, where):
    """JS edits shared by the builder APP_JS and the live index.html."""
    s = rep(s, "'<img src=\"/articles/'+esc(r.logo)+'\" alt=\"\" loading=\"lazy\" onerror=\"this.remove()\">'",
            "'<img src=\"articles/'+esc(r.logo)+'\" alt=\"\" loading=\"lazy\" onerror=\"this.remove()\">'",
            2, where + ' logo prefix')
    s = rep(s, "var DEF = {tab:'india',edu:[],states:[],support:[],need:'',q:'',sort:'soonest',showClosed:false,minAward:''};",
            "var DEF = {tab:'india',edu:[],states:[],support:[],need:'',q:'',sort:'soonest',showClosed:false,minAward:'',ptype:''};",
            1, where + ' DEF')
    s = rep(s, "var SUP_L = {girls:'Girls',reserved:'SC/ST/OBC (Reserved)',income:'Income-based',disability:'Disability',minority:'Minority',merit:'Merit-based',sports:'Sports'};",
            "var SUP_L = {girls:'Girls',reserved:'SC/ST/OBC (Reserved)',income:'Income-based',disability:'Disability',minority:'Minority',merit:'Merit-based',sports:'Sports'};\nvar PTYPE_L = {government:'Government',corporate:'Corporate',foundation:'Foundation',international:'International',other:'Other'};",
            1, where + ' PTYPE_L')
    s = rep(s, "  if(S.support.length && !S.support.some(function(t){ return (r.support||[]).indexOf(t)>=0; })) return false;",
            "  if(S.support.length && !S.support.some(function(t){ return (r.support||[]).indexOf(t)>=0; })) return false;\n  if(S.ptype && r.ptype!==S.ptype) return false;",
            1, where + ' passFilters ptype')
    s = rep(s, "  if(S.need) h+=chipHTML('need',S.need,{fees:'Fees',stipend:'Stipend',coaching:'Coaching'}[S.need]);",
            "  if(S.need) h+=chipHTML('need',S.need,{fees:'Fees',stipend:'Stipend',coaching:'Coaching'}[S.need]);\n  if(S.ptype) h+=chipHTML('ptype',S.ptype,PTYPE_L[S.ptype]||S.ptype);",
            1, where + ' chip ptype')
    s = rep(s, " } else if(g==='minAward'){ S.minAward=''; } else {",
            " } else if(g==='minAward'){ S.minAward=''; } else if(g==='ptype'){ S.ptype=''; } else {",
            1, where + ' unchip ptype')
    s = rep(s, OLD_RENDER_FEATURED, NEW_RENDER_FEATURED, 1,
            where + ' renderFeatured')
    s = rep(s, "b.setAttribute('aria-selected', j===featIdx?'true':'false'); }); }",
            "b.setAttribute('aria-selected', j===featIdx?'true':'false'); }); featStart(); }",
            1, where + ' featGo timer restart')
    s = rep(s, "function renderBoard(){",
            NEW_JS_HELPERS + "function renderBoard(){", 1,
            where + ' new helpers')
    s = rep(s, "  syncFilterUI(); render(); renderClosing(); renderFeatured(); renderBoard(); renderGuides();",
            "  syncFilterUI(); render(); renderClosing(); renderFeatured(); renderBoard(); renderGuides(); renderBrowseCols();",
            1, where + ' init renderBrowseCols')
    s = rep(s, "  bind('featNext','click',function(){ featGo(featIdx+1); });",
            "  bind('featNext','click',function(){ featGo(featIdx+1); });\n  var fs=document.getElementById('featSlider'); if(fs){ fs.addEventListener('mouseenter',featStop); fs.addEventListener('mouseleave',featStart); fs.addEventListener('focusin',featStop); fs.addEventListener('focusout',featStart); }",
            1, where + ' slider pause binds')
    s = rep(s, "    var tb=e.target.closest?e.target.closest('[data-tab]'):null;",
            "    var br=e.target.closest?e.target.closest('[data-browse]'):null;\n    if(br){ var parts=br.dataset.browse.split(':'), k=parts[0], v=parts.slice(1).join(':'); resetAll(); if(k==='state'){ S.tab='india'; S.states=[v]; } else if(k==='edu'){ S.tab=br.dataset.tab||'india'; S.edu=[v]; } else if(k==='ptype'){ S.tab=br.dataset.tab||'india'; S.ptype=v; } else if(k==='tab'){ S.tab=v; } visible=24; var fp=el('filterPanel'); if(fp) fp.innerHTML=filterPanelHTML(); var fpm=el('filterPanelMobile'); if(fpm) fpm.innerHTML=filterPanelHTML(); syncFilterUI(); render(); var rr=el('results'); if(rr) rr.scrollIntoView(); return; }\n    var tb=e.target.closest?e.target.closest('[data-tab]'):null;",
            1, where + ' data-browse branch')
    return s


def patch_body_html(s, where):
    """Body/template edits shared by build-homepage-v9.py's HTML_TEMPLATE
    and the live articles/index.html."""
    s = rep(s, 'src="/articles/logos/studydesk.png"',
            'src="articles/logos/studydesk.png"', 2, where + ' logo src')
    s = rep(s, '</aside>\n\n<main class="wrap" id="top">',
            '</aside>\n\n' + FRAUD_HTML + '\n\n<main class="wrap" id="top">',
            1, where + ' fraud banner')
    s = rep(s, '<h2 class="sec-title">Deadlines approaching fast</h2><p class="sec-sub">Open Indian government, corporate and foundation schemes closing in the next 7 days, soonest first.</p>',
            '<h2 class="sec-title">Deadlines approaching fast</h2><p class="sec-sub">Open scholarships closing soonest — across India, abroad and internships.</p>',
            1, where + ' feat sub')
    s = rep(s, '<section class="how wrap" id="how">',
            BROWSE_HTML + '\n\n<section class="how wrap" id="how">',
            1, where + ' browse section')
    s = rep(s, '<span>Shortlists are stored only in your browser. <a href="/privacy.html">Privacy</a></span>',
            '<span>Shortlists are stored only in your browser. <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="sitemap.xml">Sitemap</a></span>',
            1, where + ' footer links')
    return s


def patch_builder():
    p = os.path.join(ROOT, 'build-homepage-v9.py')
    s = open(p).read()
    # NEW_CSS: append once at its end (the sticky-tabs @media is its last
    # rule; builder duplicates NEW_CSS 4x into the page already, so this
    # keeps one canonical copy here, same as the logo fix did).
    s = rep(s, '@media(max-width:700px){.tabs,.togrow{position:sticky;top:66px;z-index:40;background:var(--bg);padding:8px 0}}',
            '@media(max-width:700px){.tabs,.togrow{position:sticky;top:66px;z-index:40;background:var(--bg);padding:8px 0}}' + NEW_RULES,
            1, 'builder NEW_CSS')
    s = patch_body_html(s, 'builder template')
    s = patch_app_js(s, 'builder APP_JS')
    open(p, 'w').write(s)
    print('patched build-homepage-v9.py')


def patch_index():
    p = os.path.join(ROOT, 'articles', 'index.html')
    s = open(p).read()
    # Style block: append the same rules once, right before </style>.
    s = rep(s, '</style>', NEW_RULES + '\n</style>', 1, 'index style')
    s = patch_body_html(s, 'index.html')
    s = patch_app_js(s, 'index.html app JS')
    open(p, 'w').write(s)
    print('patched articles/index.html')


def patch_detail_builder():
    p = os.path.join(ROOT, 'build-detail-v9.py')
    s = open(p).read()
    s = rep(s, "re.sub(r'<a href=\"/#browse\">Bihar</a>', '', page, count=1)",
            "re.sub(r'<a href=\"(?:/#browse|index\\.html#browse)\">Bihar</a>', '', page, count=1)",
            1, 'detail Bihar regex')
    s = rep(s, "if fb and '/privacy.html' not in fb.group(0):",
            "if fb and 'privacy.html' not in fb.group(0):",
            1, 'detail footer-exists guard')
    s = rep(s, "'>Contact</a> · <a href=\"/privacy.html\">Privacy</a> · '",
            "'>Contact</a> · <a href=\"privacy.html\">Privacy</a> · '",
            1, 'detail footer insert')
    open(p, 'w').write(s)
    print('patched build-detail-v9.py')


def patch_template():
    s = open(TPL).read()
    s = rep(s, 'href="/"><img src="logos/studydesk.png"',
            'href="index.html"><img src="logos/studydesk.png"',
            1, 'template wordmark')
    s = rep(s, '<a href="/#closing">Scholarships</a><a href="/#deadlines">Deadline watch</a><a href="/#browse">Browse</a><a href="/#why">Why StudyDesk</a>',
            '<a href="index.html#closing">Scholarships</a><a href="index.html#deadlines">Deadline watch</a><a href="index.html#browse">Browse</a><a href="index.html#why">Why StudyDesk</a>',
            1, 'template nav')
    s = rep(s, '<a href="/">Home</a><span>/</span><a href="/">Scholarships</a>',
            '<a href="index.html">Home</a><span>/</span><a href="index.html">Scholarships</a>',
            1, 'template crumbs')
    s = rep(s, '<a href="/">All scholarships</a> · <a href="/privacy.html">Privacy</a>',
            '<a href="index.html">All scholarships</a> · <a href="privacy.html">Privacy</a>',
            1, 'template footer')
    open(TPL, 'w').write(s)
    print('patched admin template.php')


def patch_article_files():
    """Mechanical relative-link pass over the 418 article files (index.html
    is patched separately by patch_index()). Returns counts."""
    counts = {'href="/"' : 0, 'href="/#': 0, 'href="/privacy.html"': 0}
    files = 0
    art = os.path.join(ROOT, 'articles')
    for name in sorted(os.listdir(art)):
        if not name.endswith('.html') or name == 'index.html':
            continue
        p = os.path.join(art, name)
        s = open(p).read()
        n1, n2, n3 = (s.count('href="/"'), s.count('href="/#'),
                      s.count('href="/privacy.html"'))
        if not (n1 or n2 or n3):
            continue
        s = s.replace('href="/privacy.html"', 'href="privacy.html"')
        s = s.replace('href="/#', 'href="index.html#')
        s = s.replace('href="/"', 'href="index.html"')
        open(p, 'w').write(s)
        counts['href="/"'] += n1
        counts['href="/#'] += n2
        counts['href="/privacy.html"'] += n3
        files += 1
    print('article files patched:', files, counts)
    return counts


def patch_privacy():
    p = os.path.join(ROOT, 'privacy.html')
    s = open(p).read()
    s = rep(s, 'src="/articles/logos/studydesk.png"',
            'src="articles/logos/studydesk.png"', 2, 'privacy logo src')
    s = rep(s, 'href="/privacy.html"', 'href="privacy.html"', 1,
            'privacy self link')
    s = rep(s, 'href="/"', 'href="index.html"', 4, 'privacy home links')
    s = rep(s, '<span>Shortlists are stored only in your browser. <a href="privacy.html">Privacy</a></span>',
            '<span>Shortlists are stored only in your browser. <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="sitemap.xml">Sitemap</a></span>',
            1, 'privacy footer links')
    open(p, 'w').write(s)
    print('patched privacy.html')


def write_terms():
    p = os.path.join(ROOT, 'terms.html')
    assert not os.path.exists(p), 'terms.html already exists — refusing to overwrite'
    open(p, 'w').write(TERMS_HTML)
    print('wrote terms.html', len(TERMS_HTML), 'bytes')


def verify_static():
    """Static grep checks after the patch. Raises on any failure."""
    art = os.path.join(ROOT, 'articles')
    bad = []
    for name in sorted(os.listdir(art)):
        if not name.endswith('.html'):
            continue
        s = open(os.path.join(art, name)).read()
        for pat in ('src="/articles/', 'href="/privacy.html"', 'href="/#',
                    'href="/"'):
            if pat in s:
                bad.append((name, pat, s.count(pat)))
    assert not bad, f'absolute link left: {bad[:10]}'
    idx = open(os.path.join(art, 'index.html')).read()
    for must in ('id="featSlider"', 'id="browseCols"', 'id="browseColsGrid"',
                 'class="fraudbar"', 'href="terms.html"',
                 'href="sitemap.xml"', 'renderBrowseCols()', 'featStart()',
                 'openCountWhere', 'data-browse', 'S.ptype',
                 'src="articles/logos/studydesk.png"'):
        assert must in idx, f'index.html missing {must}'
    assert "'/articles/'" not in idx, 'index.html still has absolute logo prefix'
    # No tiny-logo img inside any .plogo span (logo-fix invariant):
    # normal logos DO render as imgs there; only TINY_LOGOS files must
    # never appear as an img (they render as monogram letters instead).
    import glob
    builder = open(os.path.join(ROOT, 'build-homepage-v9.py')).read()
    m = re.search(r"var TINY_LOGOS\s*=\s*(\{[^;]*\});", builder)
    assert m, 'TINY_LOGOS not found in builder'
    tiny_set = set(json.loads(m.group(1)).keys())
    tiny = 0
    plogo_re = re.compile(r'<span class="plogo[^"]*">.*?</span>', re.S)
    img_re = re.compile(r'<img[^>]+src="([^"]+)"')
    for f in glob.glob(os.path.join(art, '*.html')):
        s = open(f).read()
        for pm in plogo_re.finditer(s):
            for im in img_re.finditer(pm.group(0)):
                if im.group(1) in tiny_set:
                    tiny += 1
    assert tiny == 0, f'tiny-logo imgs in .plogo spans: {tiny}'
    # Canonical / og:url / srcUrl stay absolute (by design).
    assert 'rel="canonical" href="https://scholarships.studydesk.fun/' in idx
    print('static verify OK: no absolute src/href left in articles/, '
          '0 tiny-logo imgs in .plogo spans, canonical absolute kept')


def main():
    backup()
    patch_builder()
    patch_index()
    patch_detail_builder()
    patch_template()
    patch_article_files()
    patch_privacy()
    write_terms()
    verify_static()
    print('DONE — now run node --check on the touched inline JS, '
          'the Node harness for slider + browse counts, then rebuild '
          'the preview.')


if __name__ == '__main__':
    main()

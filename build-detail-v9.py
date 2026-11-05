#!/usr/bin/env python3
"""Transform all 416 scholarships detail pages (v9, 2 Nov 2026 spec).

For every articles/*.html except index.html and pilot-* drafts:
- insert ONE action box after </h1> (status + exact date from dl, computed
  for 2 Nov 2026 at build time AND recomputed in the browser from data-dl)
- "You can apply if": up to 3 bullets from the page's own Eligibility
  list (never invented); "You cannot apply if": only when the page states
  an exclusion; Documents: short list only when the page lists them
- apply button labelled with the official hostname ONLY when the srcUrl
  host is official (government portal or provider host); otherwise a
  plain "No official application URL on file" line + Mentioned-by link
- offcard heading "Official source" -> "Mentioned by" when the srcUrl
  host is not official (the old heading mislabelled aggregators)
- meta-row: dline becomes the exact date, status becomes the computed
  label; the meta-row div carries data-dl (or data-guide) so the browser
  script recomputes both spans on every view (panel edits that rewrite
  frozen text are self-healing at view time). Panel regexes target the
  spans themselves, which keep their exact class attributes.
- related-card dpills: frozen "N days to go" / "Closes today, 31 Oct"
  text replaced with a computed label + data-dl for browser recompute
- guide pages (3): Guide label, no single deadline, no fake apply
  button; applicationDeadline removed from their JSON-LD
- footer: Bihar link removed (0 tagged listings); Privacy + WhatsApp
  links added (footer-only contact); fixed wa-float + help-tab removed
  (their trailing script is replaced by reveal + status script)

Panel safety: no .fact/.dline/.status element shapes change (only text),
no section ids change, no canonical/JSON-LD urls change (except removing
a fake single deadline from guide LD). Idempotent: re-running replaces
the previously inserted box/script instead of duplicating them.

Run: python3 build-detail-v9.py
"""
import html
import json
import pathlib
import re
from datetime import date

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
ART = ROOT / 'articles'
TODAY = date(2026, 11, 2)
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
GUIDES = {
    'study-in-canada-without-ielts-2026.html',
    'how-to-get-fully-funded-scholarships-in-italy-2026-27.html',
    'unilever-internships-2027-guide.html',
}
AGGREGATORS = {'buddy4study.com', 'brightscholarship.com',
               'opportunitydesk.org'}
STOP = {'university', 'universities', 'college', 'school', 'institute',
        'foundation', 'trust', 'scholarship', 'scholarships', 'programme',
        'program', 'ministry', 'department', 'government', 'of', 'the',
        'and', 'for', 'india', 'indian', 'international', 'national',
        'state', 'central', 'ltd', 'limited', 'pvt', 'private', 'inc',
        'llc', 'co', 'company', 'group', 'portal'}


def esc(s):
    return html.escape(str(s or ''), quote=True)


def word_cut(s, n):
    s = re.sub(r'\s+', ' ', str(s or '')).strip()
    if len(s) <= n:
        return s
    c = s[:n]
    i = c.rfind(' ')
    if i > 40:
        c = c[:i]
    return c + '…'


def clean_text(raw):
    t = re.sub(r'<[^>]+>', ' ', raw or '')
    t = html.unescape(t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s+([.,;:!?%])', r'\1', t)
    return t


def fmt_dl(dl):
    if not dl:
        return ''
    y, m, d = dl.split('-')
    s = f'{int(d)} {MONTHS[int(m) - 1]}'
    if int(y) != TODAY.year:
        s += f' {y}'
    return s


def status_for(dl):
    """(key, label) for today=2026-11-02. Never a negative number."""
    if not dl:
        return ('warn', 'Date not confirmed')
    y, m, d = map(int, dl.split('-'))
    diff = (date(y, m, d) - TODAY).days
    if diff < 0:
        return ('closed', 'Closed')
    if diff == 0:
        return ('urgent', 'Closes today')
    if diff <= 7:
        return ('urgent', f'Closes in {diff} day{"s" if diff != 1 else ""}')
    return ('open', f'Closes {fmt_dl(dl)}')


def host_of(u):
    m = re.match(r'https?://([^/:?#]+)', u or '')
    return m.group(1).replace('www.', '') if m else ''


def is_official(rec):
    host = host_of(rec.get('srcUrl') or '')
    if not host:
        return False
    bare = host.replace('www.', '')
    if bare in AGGREGATORS:
        return False
    if re.search(r'\.gov(\.|$)|\.gov\.in$|\.nic\.in$', bare):
        return True
    toks = re.split(r'[^a-z0-9]+', (rec.get('provider') or '').lower())
    for t in toks:
        if len(t) >= 3 and t not in STOP and t in bare:
            return True
    return False


def section_items(page, heading_prefixes):
    """<li> texts of the first <ul>/<ol> after an <h2> whose text starts
    with any of heading_prefixes (case-insensitive). [] when absent."""
    if isinstance(heading_prefixes, str):
        heading_prefixes = (heading_prefixes,)
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', page, re.S):
        head = clean_text(m.group(1))
        if any(head.lower().startswith(p.lower())
               for p in heading_prefixes):
            rest = page[m.end():]
            lm = re.search(r'<(ul|ol)[^>]*>(.*?)</\1>', rest, re.S)
            if not lm:
                return []
            nxt = rest[:lm.start()]
            if '<h2' in nxt:
                return []
            return [clean_text(li) for li in
                    re.findall(r'<li[^>]*>(.*?)</li>', lm.group(2), re.S)]
    return []


def find_exclusion(page, elig_items):
    """One exclusion line only when the page states one, else None."""
    for it in elig_items:
        if re.match(r'\s*(not eligible|you (are )?not eligible|'
                    r'candidates (who )?are not|excluded)\b', it, re.I):
            return it
    for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', page, re.S):
        head = clean_text(m.group(1))
        if re.search(r'cannot|not eligible|exclusion', head, re.I):
            rest = page[m.end():]
            lm = re.search(r'<li[^>]*>(.*?)</li>', rest, re.S)
            if lm:
                return clean_text(lm.group(1))
            sm = re.search(r'<p[^>]*>(.*?)</p>', rest, re.S)
            if sm:
                s = clean_text(sm.group(1))
                mm = re.match(r'^[^.!?]+[.!?]', s)
                return mm.group(0) if mm else s
    # Prose exclusion inside the Eligibility / Who-can-apply section:
    # first sentence that itself states "not eligible".
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', page, re.S):
        head = clean_text(m.group(1))
        if head.lower().startswith(('eligibility', 'who can apply')):
            rest = page[m.end():]
            nxt = rest.find('<h2')
            sect = rest if nxt < 0 else rest[:nxt]
            text = clean_text(sect)
            for sent in re.split(r'(?<=[.!?])\s+', text):
                if 'not eligible' in sent.lower():
                    return sent.strip()
            break
    return None


SD_CSS = """
/* sd-action-box (v9) */
.sd-action-box{border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:18px 0;background:var(--surface)}
.sd-action-box h3{font-size:16px;margin:14px 0 6px}
.sd-action-box h3:first-child{margin-top:0}
.sd-status-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.sd-status{display:inline-block;padding:4px 11px;border-radius:999px;font-weight:700;font-size:14px}
.sd-status.st-open{background:var(--good-soft);color:var(--good)}
.sd-status.st-urgent{background:var(--urgent-soft);color:var(--urgent)}
.sd-status.st-closed{background:#eef2f8;color:var(--muted)}
.sd-status.st-warn{background:#fdf0dc;color:#b45309}
.sd-status.st-guide{background:#e9effe;color:#173da8}
.sd-date{font-weight:600}
.sd-action-box ul{margin:6px 0 0 20px}
.sd-action-box li{margin-bottom:4px}
.sd-cannot{margin-top:12px}
.sd-apply{display:inline-block;background:var(--accent);color:var(--accent-ink);padding:11px 22px;border-radius:999px;text-decoration:none;font-weight:700;margin-top:12px;min-height:44px;line-height:22px}
.sd-apply:hover{text-decoration:underline}
.sd-noapply{margin-top:12px;font-weight:600}
.sd-checked{margin-top:14px;font-size:14px;color:var(--muted)}
.sd-guide-note{margin-top:10px}
/* Mobile fix 2026-11-05 */
/* 6-cell fact grids (e.g. Canada guide) wrap in a 5-col grid; 3 cols fits exactly. Exact-6 only: 7/8-cell grids untouched. */
.facts:has(>.fact:nth-child(6):last-child){grid-template-columns:repeat(3,1fr)}
/* Unfilled AdSense slots leave a ~150-200px blank band; hide only the unfilled ones, AdSense itself stays. */
ins.adsbygoogle[data-ad-status="unfilled"]{display:none!important}
/* Bare tables (e.g. Super 50 exam pattern) can overflow narrow screens; let them scroll instead. Markup untouched. */
.abody table{display:block;overflow-x:auto;max-width:100%}
"""

STATUS_JS = """<!-- sd-status-script -->
<script>
(function(){
  "use strict";
  var MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var TODAY; try{ TODAY=new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Kolkata'}).format(new Date()); }catch(e){ var d=new Date(); TODAY=d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2); }
  function fmtDL(dl){ var p=dl.split('-'); var s=parseInt(p[2],10)+' '+MONTHS[parseInt(p[1],10)-1]; if(parseInt(p[0],10)!==parseInt(TODAY.slice(0,4),10)) s+=' '+p[0]; return s; }
  function statusFor(dl){
    if(!dl) return {key:'warn',label:'Date not confirmed'};
    var diff=Math.round((Date.parse(dl+'T00:00:00Z')-Date.parse(TODAY+'T00:00:00Z'))/86400000);
    if(diff<0) return {key:'closed',label:'Closed'};
    if(diff===0) return {key:'urgent',label:'Closes today'};
    if(diff<=7) return {key:'urgent',label:'Closes in '+diff+' day'+(diff===1?'':'s')};
    return {key:'open',label:'Closes '+fmtDL(dl)};
  }
  function setPill(el,st){ el.textContent=st.label; el.className=el.className.replace(/\\bst-(open|urgent|closed|warn|guide)\\b/g,'').trim()+' st-'+st.key; }
  document.querySelectorAll('.sd-status[data-dl]').forEach(function(el){ setPill(el, statusFor(el.getAttribute('data-dl')||'')); });
  document.querySelectorAll('.dpill[data-dl]').forEach(function(el){ var dl=el.getAttribute('data-dl')||''; var st=statusFor(dl); el.textContent = dl ? (fmtDL(dl)+' · '+st.label) : st.label; });
  document.querySelectorAll('.meta-row').forEach(function(row){
    var dl=row.getAttribute('data-dl'), guide=row.getAttribute('data-guide');
    var dlEl=row.querySelector('.dline'), stEl=row.querySelector('.status');
    if(guide){ if(dlEl) dlEl.textContent='Guide'; if(stEl) stEl.textContent='Guide'; return; }
    if(dl){ var st=statusFor(dl); if(dlEl) dlEl.textContent='Deadline: '+fmtDL(dl); if(stEl) stEl.textContent=st.label; }
    else { if(dlEl) dlEl.textContent='Date not confirmed'; if(stEl) stEl.textContent='Date not confirmed'; }
  });
  // Fix pass 2026-11-03: a closed listing must not offer Apply or a WhatsApp
  // reminder, and a guide (no single deadline) must not offer one either.
  // Status is recomputed here from data-dl, so the gating stays right as
  // deadlines pass without any rebuild.
  (function(){
    var pageClosed=false, pageGuide=false;
    document.querySelectorAll('.meta-row').forEach(function(row){
      if(row.getAttribute('data-guide')) pageGuide=true;
      var dl=row.getAttribute('data-dl');
      if(dl && statusFor(dl).key==='closed') pageClosed=true;
    });
    document.querySelectorAll('.sd-action-box').forEach(function(box){
      var pill=box.querySelector('.sd-status[data-dl]');
      if(pill && statusFor(pill.getAttribute('data-dl')||'').key==='closed'){
        var ap=box.querySelector('.sd-apply'); if(ap) ap.style.display='none';
      }
    });
    if(pageClosed||pageGuide){
      var ac=document.getElementById('deadline-alert'); if(ac) ac.style.display='none';
      var gal=document.querySelector('a[href="#deadline-alert"]'); if(gal) gal.style.display='none';
    }
  })();
  function sectionItemsAny(prefixes){
    var heads=document.querySelectorAll('h2'); for(var i=0;i<heads.length;i++){
      var txt=heads[i].textContent.trim().toLowerCase();
      for(var k=0;k<prefixes.length;k++){
        if(txt.indexOf(prefixes[k])===0){
          var el=heads[i].nextElementSibling;
          while(el && el.tagName!=='UL' && el.tagName!=='OL' && el.tagName!=='H2') el=el.nextElementSibling;
          if(el && (el.tagName==='UL'||el.tagName==='OL')) return Array.prototype.map.call(el.querySelectorAll('li'), function(li){ return li.textContent.replace(/\\s+/g,' ').trim(); });
        }
      }
    }
    return [];
  }
  function sectionItems(headingStart){ return sectionItemsAny([headingStart]); }
  function wordCut(s,n){ s=String(s||'').replace(/\\s+/g,' ').trim(); if(s.length<=n) return s; var c=s.slice(0,n); var i=c.lastIndexOf(' '); if(i>40) c=c.slice(0,i); return c+'…'; }
  document.querySelectorAll('.sd-can[data-from]').forEach(function(ul){
    var items=sectionItemsAny(['eligibility','who can apply']); if(!items.length) return;
    ul.innerHTML=items.slice(0,3).map(function(t){ return '<li>'+t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')+'</li>'; }).join('');
  });
  document.querySelectorAll('.sd-docs[data-from]').forEach(function(ul){
    var items=sectionItems('documents'); if(!items.length) return;
    ul.innerHTML=items.slice(0,6).map(function(t){ return '<li>'+wordCut(t,100).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')+'</li>'; }).join('');
  });
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rvEls=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window && !reduce){
    var io=new IntersectionObserver(function(entries){ entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {threshold:.1});
    rvEls.forEach(function(el){ io.observe(el); });
  } else { rvEls.forEach(function(el){ el.classList.add('in'); }); }
})();
</script>
"""

def first_sentence(s):
    s = re.sub(r'\s+', ' ', str(s or '')).strip()
    if not s:
        return ''
    m = re.match(r'^[^.!?]+[.!?]', s)
    return (m.group(0) if m else s).strip()


def build_action_box(page, rec):
    """Returns (box_html, info_dict)."""
    info = {}
    dl = rec.get('dl')
    verified = rec.get('verified') or ''
    src_url = rec.get('srcUrl') or ''
    host = host_of(src_url)
    official = is_official(rec)
    src_label = rec.get('srcLabel') or host or ''
    if rec['file'] in GUIDES:
        cover = word_cut(first_sentence(rec.get('sub') or ''), 160)
        if official and src_url:
            src_html = (f'<a class="sd-apply" href="{esc(src_url)}" '
                        f'rel="noopener">Visit official source: '
                        f'{esc(host)}</a>')
            checked_src = f'Official source: {esc(src_label)}'
        elif src_url:
            src_html = (f'<p class="sd-mentioned">Mentioned by '
                        f'<a href="{esc(src_url)}" rel="noopener">'
                        f'{esc(host)}</a></p>')
            checked_src = f'Mentioned by: {esc(src_label)}'
        else:
            src_html = ('<p class="sd-noapply">No official application '
                        'URL on file.</p>')
            checked_src = ''
        checked = (f'Checked {esc(verified)} against {checked_src}'
                   if checked_src else
                   f'Checked {esc(verified)} — no source URL on file.')
        box = ('<!-- sd-action-box -->\n'
               '<div class="sd-action-box sd-guide">\n'
               '  <div class="sd-status-row">'
               '<span class="sd-status st-guide">Guide</span>'
               '<span class="sd-date">No single deadline</span></div>\n'
               + (f'  <p class="sd-guide-note">{esc(cover)}</p>\n'
                  if cover else '')
               + '  <p class="sd-guide-note">This guide covers several '
               'options with different deadlines — there is no single '
               'deadline for this page.</p>\n'
               f'  {src_html}\n'
               f'  <p class="sd-checked">{checked}</p>\n'
               '</div>\n<!-- /sd-action-box -->')
        info['guide'] = True
        return box, info
    key, label = status_for(dl)
    date_line = f'Deadline: {fmt_dl(dl)}' if dl else 'Date not confirmed'
    elig = section_items(page, ('Eligibility', 'Who can apply'))
    excl = find_exclusion(page, elig)
    can = [it for it in elig
           if not (excl and it == excl)][:3]
    docs = section_items(page, ('Documents',))[:6]
    parts = ['<!-- sd-action-box -->',
             '<div class="sd-action-box">',
             '  <div class="sd-status-row">'
             f'<span class="sd-status st-{key}" data-dl="{esc(dl or "")}">'
             f'{esc(label)}</span>'
             f'<span class="sd-date">{esc(date_line)}</span></div>']
    if can:
        parts.append('  <h3>You can apply if</h3>')
        parts.append('  <ul class="sd-can" data-from="eligibility">')
        parts += [f'    <li>{esc(word_cut(it, 140))}</li>' for it in can]
        parts.append('  </ul>')
        info['can'] = len(can)
    if excl:
        parts.append(f'  <p class="sd-cannot"><strong>You cannot apply '
                     f'if:</strong> {esc(word_cut(excl, 200))}</p>')
        info['cannot'] = True
    if docs:
        parts.append('  <h3>Documents</h3>')
        parts.append('  <ul class="sd-docs" data-from="documents">')
        parts += [f'    <li>{esc(word_cut(it, 100))}</li>' for it in docs]
        parts.append('  </ul>')
        info['docs'] = len(docs)
    if official and src_url:
        parts.append(f'  <a class="sd-apply" href="{esc(src_url)}" '
                     f'rel="noopener">Apply on {esc(host)}</a>')
        checked_src = f'Official source: {esc(src_label)}'
        info['apply'] = 'official'
    else:
        parts.append('  <p class="sd-noapply">No official application '
                     'URL on file.</p>')
        if src_url:
            parts.append(f'  <p class="sd-mentioned">Mentioned by '
                         f'<a href="{esc(src_url)}" rel="noopener">'
                         f'{esc(host)}</a></p>')
            checked_src = f'Mentioned by: {esc(src_label)}'
            info['apply'] = 'mentioned'
        else:
            checked_src = ''
            info['apply'] = 'none'
    checked = (f'Checked {esc(verified)} against {checked_src}'
               if checked_src else
               f'Checked {esc(verified)} — no source URL on file.')
    parts.append(f'  <p class="sd-checked">{checked}</p>')
    parts.append('</div>')
    parts.append('<!-- /sd-action-box -->')
    return '\n'.join(parts) + '\n', info


def strip_old_box(page):
    a = page.find('<!-- sd-action-box -->')
    if a < 0:
        return page
    b = page.find('<!-- /sd-action-box -->', a)
    if b < 0:
        return page
    return page[:a] + page[b + len('<!-- /sd-action-box -->'):]


def strip_old_script(page):
    a = page.find('<!-- sd-status-script -->')
    if a < 0:
        return page
    b = page.find('</script>', a)
    if b < 0:
        return page
    return page[:a] + page[b + len('</script>'):]


def transform(page, rec, by_file):
    """Returns (new_page, info)."""
    info = {}
    page = strip_old_box(page)
    page = strip_old_script(page)
    box, binfo = build_action_box(page, rec)
    info.update(binfo)
    if '</h1>' not in page:
        info['miss'] = 'no-h1'
        return page, info
    page = page.replace('</h1>', '</h1>\n' + box, 1)
    # ---- CSS (exactly one copy) ----
    page = page.replace(SD_CSS, '')
    page = page.replace('</style>', SD_CSS + '</style>', 1)
    info['css'] = True
    # ---- meta-row ----
    dl = rec.get('dl')
    is_guide = rec['file'] in GUIDES
    m = re.search(r'<div class="meta-row"[^>]*>(.*?)</div>', page, re.S)
    if m:
        block = m.group(0)
        block = re.sub(r'\sdata-dl="[^"]*"', '', block)
        block = re.sub(r'\sdata-guide="[^"]*"', '', block)
        if is_guide:
            block = block.replace('<div class="meta-row"',
                                  '<div class="meta-row" data-guide="1"', 1)
            new_dline, new_status = 'Guide', 'Guide'
        elif dl:
            block = block.replace('<div class="meta-row"',
                                  f'<div class="meta-row" data-dl="{dl}"',
                                  1)
            key, label = status_for(dl)
            new_dline, new_status = f'Deadline: {fmt_dl(dl)}', label
        else:
            new_dline = new_status = 'Date not confirmed'
        block = re.sub(r'<span class="dline">.*?</span>',
                       f'<span class="dline">{esc(new_dline)}</span>',
                       block, count=1)
        block = re.sub(r'<span class="status">.*?</span>',
                       f'<span class="status">{esc(new_status)}</span>',
                       block, count=1)
        page = page[:m.start()] + block + page[m.end():]
        info['meta'] = True
    else:
        info['miss'] = 'no-meta-row'
    # ---- related dpills (only after the Related heading) ----
    rel = page.find('Related scholarships')
    if rel >= 0:
        head, tail = page[:rel], page[rel:]
        fixed, unmapped = 0, 0

        def fix_pill(m):
            nonlocal fixed, unmapped
            after = tail[m.end():m.end() + 800]
            hm = re.search(r'<a href="([^"]+\.html)"', after)
            if not hm:
                unmapped += 1
                return ''
            target = by_file.get(hm.group(1))
            if target is None:
                unmapped += 1
                return ''
            tdl = target.get('dl')
            if tdl:
                key, label = status_for(tdl)
                text = f'{fmt_dl(tdl)} · {label}'
            else:
                key, label = 'warn', 'Date not confirmed'
                text = label
            fixed += 1
            return (f'<span class="dpill" data-dl="{tdl or ""}">'
                    f'{esc(text)}</span>')

        tail = re.sub(r'<span class="dpill[^"]*"[^>]*>(.*?)</span>',
                      fix_pill, tail)
        page = head + tail
        info['dpills'] = fixed
        info['dpills_unmapped'] = unmapped
    # ---- offcard heading ----
    if not is_official(rec) and rec.get('srcUrl'):
        oc = re.search(r'<div class="acard offcard.*?</div>', page, re.S)
        if oc and '<h3>Official source</h3>' in oc.group(0):
            new_oc = oc.group(0).replace('<h3>Official source</h3>',
                                         '<h3>Mentioned by</h3>', 1)
            page = page[:oc.start()] + new_oc + page[oc.end():]
            info['offcard'] = True
    # ---- footer: drop Bihar, add Privacy + WhatsApp ----
    if '>Bihar</a>' in page:
        page = re.sub(r'<a href="/#browse">Bihar</a>', '', page, count=1)
        info['bihar_dropped'] = True
    fb = re.search(r'<div class="foot-bar">.*?</div>', page, re.S)
    if fb and '/privacy.html' not in fb.group(0):
        new_fb = fb.group(0).replace(
            '>Contact</a>',
            '>Contact</a> · <a href="/privacy.html">Privacy</a> · '
            '<a href="https://wa.me/919905166009">WhatsApp</a>', 1)
        page = page[:fb.start()] + new_fb + page[fb.end():]
        info['footer'] = True
    # ---- wa-float + help-tab removal ----
    if 'wa-float' in page:
        page = re.sub(r'<a class="wa-float"[^>]*>.*?</a>', '', page,
                      count=1, flags=re.S)
        info['wa_removed'] = True
    if 'help-tab' in page:
        page = re.sub(r'<button class="help-tab"[^>]*>.*?</button>', '',
                      page, count=1, flags=re.S)
    # ---- trailing script -> reveal + status script ----
    # (Re-run safe: the old status script was stripped above, so if no
    # wa-float script remains, insert fresh before </body>.)
    done = False
    for m in re.finditer(r'<script>(.*?)</script>', page, re.S):
        if 'wa-float' in m.group(1):
            page = page[:m.start()] + STATUS_JS + page[m.end():]
            done = True
            break
    if not done and '</body>' in page:
        page = page.replace('</body>', STATUS_JS + '</body>', 1)
        done = True
    info['script'] = done
    # ---- guide JSON-LD: drop a fake single deadline ----
    if is_guide:
        before = page
        page = re.sub(r'[ \t]*"applicationDeadline":\s*"[^"]*",\n', '',
                      page, count=1)
        if page == before:
            page = re.sub(r',\n[ \t]*"applicationDeadline":\s*"[^"]*"',
                          '', page, count=1)
        info['ld_fixed'] = page != before
    return page, info


def main():
    sd = json.load(open(ROOT / 'site-data.json', encoding='utf-8'))
    by_file = {r['file']: r for r in sd}
    files = sorted(p for p in ART.glob('*.html')
                   if p.name != 'index.html'
                   and not p.name.startswith('pilot-'))
    print(f'{len(files)} detail files')
    agg = {'can': 0, 'cannot': 0, 'docs': 0, 'apply_official': 0,
           'apply_mentioned': 0, 'apply_none': 0, 'offcard': 0,
           'dpills': 0, 'dpills_unmapped': 0, 'wa_removed': 0,
           'script': 0, 'footer': 0, 'bihar_dropped': 0, 'css': 0,
           'meta': 0, 'guides': 0, 'ld_fixed': 0}
    misses = []
    no_can, no_docs = [], []
    for p in files:
        rec = by_file.get(p.name)
        if rec is None:
            misses.append((p.name, 'no-DATA-record'))
            continue
        page = p.read_text(encoding='utf-8')
        new, info = transform(page, rec, by_file)
        if 'miss' in info:
            misses.append((p.name, info['miss']))
            continue
        if new != page:
            p.write_text(new, encoding='utf-8')
        agg['can'] += 1 if info.get('can') else 0
        agg['cannot'] += 1 if info.get('cannot') else 0
        agg['docs'] += 1 if info.get('docs') else 0
        agg['apply_official'] += 1 if info.get('apply') == 'official' else 0
        agg['apply_mentioned'] += 1 if info.get('apply') == 'mentioned' else 0
        agg['apply_none'] += 1 if info.get('apply') == 'none' else 0
        agg['offcard'] += 1 if info.get('offcard') else 0
        agg['dpills'] += info.get('dpills', 0)
        agg['dpills_unmapped'] += info.get('dpills_unmapped', 0)
        agg['wa_removed'] += 1 if info.get('wa_removed') else 0
        agg['script'] += 1 if info.get('script') else 0
        agg['footer'] += 1 if info.get('footer') else 0
        agg['bihar_dropped'] += 1 if info.get('bihar_dropped') else 0
        agg['css'] += 1 if info.get('css') else 0
        agg['meta'] += 1 if info.get('meta') else 0
        agg['guides'] += 1 if info.get('guide') else 0
        agg['ld_fixed'] += 1 if info.get('ld_fixed') else 0
        if rec['file'] not in GUIDES:
            if not info.get('can'):
                no_can.append(p.name)
            if not info.get('docs'):
                no_docs.append(p.name)
    print(json.dumps(agg, indent=1))
    print('misses:', misses)
    print('non-guide pages with no can-bullets:', len(no_can), no_can[:10])
    print('non-guide pages with no docs list:', len(no_docs), no_docs[:10])


if __name__ == '__main__':
    main()

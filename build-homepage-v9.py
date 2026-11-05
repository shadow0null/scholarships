#!/usr/bin/env python3
"""Build the NEW scholarships homepage (v9, 2 Nov 2026 spec).

Reads the current articles/index.html, keeps its <style> block verbatim
(brand tokens: Fraunces, Inter, navy #141d45, amber #f5a524, cream bg)
and its embedded DATA array verbatim (same /*__DATA__*/ marker and shape,
so the admin panel's data.php extract/save keeps working), and writes a
new articles/index.html implementing the 2 Nov 2026 rebuild spec:

- matcher hero (h1 "Find open scholarships", 4 controls mapped to real
  tags, "See my matches" / "Browse all open")
- section order: Matcher, Closing in 7 days (max 6, India gov/corp/
  foundation only), My plan (only when the shortlist is non-empty),
  Browse, Deadline board, Guides, How a listing gets on this page +
  not-a-government box
- tabs India / Abroad / Internships (one tab per listing, default India),
  default grid Open with a Show-closed toggle off by default, 24 cards
  then "Show more"
- ALL status text browser-computed from dl + today in Asia/Kolkata;
  stored days/closed are NEVER displayed (they stay in DATA for the
  panel, which keeps writing them, but display ignores them)
- AdSense unit moved to after the first row of results (grid item after
  the 3rd card); ad client/slot/script unchanged
- WhatsApp fixed bubble REMOVED (footer carries number + email only)
- Shortlist renamed to My plan; localStorage key sd_shortlist UNCHANGED
  so saved items survive; compare only from My plan (max 3, memory
  only, clears on refresh)
- sessionStorage restore guard: a stored filter set that yields zero
  results is never restored; defaults are used instead
- guide pages (3 files, see GUIDES) get a "Guide" pill, sort last, and
  never appear in closing/featured/board rows

Run: python3 build-homepage-v9.py  (from ~/workspace/scholarships-17k)
Output: articles/index.html (the deploy builder copies it to the zip root)
"""
import json
import pathlib
import re

ROOT = pathlib.Path('/home/hatch/workspace/scholarships-17k')
SRC = ROOT / 'articles' / 'index.html'
OUT = ROOT / 'articles' / 'index.html'

# Pages that describe a guide, not one scholarship (each page's own words
# are the evidence; see the rebuild report for the quotes):
#  - study-in-canada-without-ielts-2026.html: "This guide maps the
#    verified routes" — no single scholarship, dl null.
#  - how-to-get-fully-funded-scholarships-in-italy-2026-27.html: maps
#    "the nine verifiable routes" with different rules and deadlines.
#  - unilever-internships-2027-guide.html: "There is no single
#    'Unilever Summer Internship' with one deadline" — rolling roles.
GUIDES = [
    'study-in-canada-without-ielts-2026.html',
    'how-to-get-fully-funded-scholarships-in-italy-2026-27.html',
    'unilever-internships-2027-guide.html',
]

# Place-like cats observed on ptype=international records, PLUS the country
# names that appear as cats on ptype="other" records (Egypt, Lebanon,
# Denmark, Austria, Hong Kong) and a standard world list. Used ONLY for
# the ptype="other" fallback (country cats -> Abroad). Country names come
# from the records' own cats or standard geography — never invented
# per-listing. Compound cats ("Germany & Poland", "USA & EMEA") are split
# on & / and / / before matching, so a part that is a country counts.
COUNTRY_CATS = [
    'Australia', 'Belgium', 'Brunei', 'Canada', 'China', 'Europe',
    'Finland', 'France', 'Germany', 'Hungary', 'Indonesia', 'Italy',
    'Japan', 'Lithuania', 'Malaysia', 'Malta', 'Netherlands',
    'New Zealand', 'Northern Cyprus', 'Norway', 'Qatar', 'Russia',
    'Saudi Arabia', 'Scotland', 'Singapore', 'Slovakia', 'South Korea',
    'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey',
    'UAE', 'UK', 'United Kingdom', 'USA', 'Vietnam', 'Worldwide',
    'Global',
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia', 'Botswana', 'Brazil', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Chad', 'Chile',
    'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba',
    'Cyprus', 'Czechia', 'Czech Republic', 'Denmark', 'Djibouti',
    'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia',
    'Fiji', 'Gabon', 'Gambia', 'Georgia', 'Ghana', 'Greece', 'Grenada',
    'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong',
    'Iceland', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Jamaica', 'Jordan',
    'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos',
    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
    'Luxembourg', 'Madagascar', 'Malawi', 'Mali', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Nicaragua', 'Niger',
    'Nigeria', 'North Macedonia', 'Oman', 'Pakistan', 'Palau',
    'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
    'Philippines', 'Poland', 'Portugal', 'Romania', 'Rwanda', 'Samoa',
    'San Marino', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
    'South Sudan', 'Sri Lanka', 'Sudan', 'Suriname', 'Syria',
    'Tajikistan', 'Tanzania', 'Togo', 'Tonga', 'Trinidad', 'Tunisia',
    'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'Uruguay',
    'Uzbekistan', 'Vanuatu', 'Venezuela', 'Yemen', 'Zambia', 'Zimbabwe',
]

# The 6 guide-slider cards, kept exactly as before (all are single
# scholarships presented as in-depth guides; verified present in DATA).
GUIDE_SLIDER = [
    'muskaan-scholarship-2-2026-27.html',
    'dakshana-scholarship-jdst-2027.html',
    'nasa-hubble-fellowship-program-2027.html',
    'nsp-post-matric-sc-goa-2026-27.html',
    'pathani-samanta-maths-talent-scholarship-2026-27.html',
    'sdef-india-scholarship-2026-27.html',
]

# AdSense unit, byte-identical to the old homepage (client, slot and
# loader script unchanged; only its POSITION moves).
ADSENSE_LOADER = ('<script async src="https://pagead2.googlesyndication.com/'
                  'pagead/js/adsbygoogle.js?client=ca-pub-3573504055334993" '
                  'crossorigin="anonymous"></script>')
ADSENSE_INS = ('<ins class="adsbygoogle" style="display:block" '
               'data-ad-client="ca-pub-3573504055334993" '
               'data-ad-slot="4630994583" data-ad-format="auto" '
               'data-full-width-responsive="true"></ins>')

NEW_CSS = r"""
/* ---- v9 additions: matcher, tabs, cards, board, myplan (brand kept) ---- */
.matcher{background:linear-gradient(180deg,#141d45 0%,#1e2a63 100%);color:#fff;border-radius:20px;padding:30px 28px;margin:26px 0}
.matcher .sec-kick{color:#f5a524}
.matcher h1{color:#fff;font-size:clamp(30px,4.5vw,46px);margin:8px 0 6px}
.matcher .deck{color:#d7dcf2;max-width:720px}
.mform{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0 8px}
.mform label{display:block;font-size:13px;font-weight:700;letter-spacing:.02em;color:#c9d1f2;margin-bottom:6px}
.mform select{width:100%;min-height:44px;border:1px solid #3a478a;border-radius:10px;padding:0 12px;font:inherit;font-size:15px;background:#fff;color:#1b1936}
.mrow{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:14px}
.mnote{font-size:13px;color:#c9d1f2;margin-top:12px}
.mcounts{font-size:14px;color:#d7dcf2;margin-top:10px}
@media(max-width:900px){.mform{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.mform{grid-template-columns:1fr}}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 4px}
.tabbtn{min-height:44px;padding:0 18px;border:1px solid var(--line-d);border-radius:999px;background:#fff;font-weight:700;cursor:pointer;color:var(--ink)}
.tabbtn[aria-pressed="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
.togrow{display:flex;align-items:center;gap:10px;margin:10px 0;flex-wrap:wrap}
.togrow label{display:flex;align-items:center;gap:8px;font-weight:600;cursor:pointer}
.togrow input[type="checkbox"]{width:20px;height:20px;accent-color:var(--navy)}
#minAward{min-width:140px;flex:none}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:8px;box-shadow:var(--sh)}
.pill{align-self:flex-start;display:inline-block;padding:4px 11px;border-radius:999px;font-size:13px;font-weight:800}
.pill.st-open{background:var(--ok-bg);color:var(--ok)}
.pill.st-urgent{background:var(--crit-bg);color:var(--crit)}
.pill.st-closed{background:#eceaf4;color:#5f5b7c}
.pill.st-warn{background:var(--warn-bg);color:var(--warn)}
.pill.st-guide{background:#e9effe;color:#1e2a63}
.card h3{font-size:19px;line-height:1.35}
.card h3 a{color:var(--ink);text-decoration:none}
.card h3 a:hover{text-decoration:underline}
.card .prov{display:flex;align-items:center;gap:9px;font-weight:700;font-size:15px}
.card .plogo{width:34px;height:34px;min-width:34px;border-radius:50%;background:var(--navy);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:800;overflow:hidden}
.card .plogo img{width:100%;height:100%;object-fit:contain;background:#fff;padding:3px;box-sizing:border-box}
.card .who,.card .award{font-size:15px;color:var(--mut);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card .award{color:var(--ink);font-weight:600}
.card .trust{font-size:13px;color:var(--mut)}
.card .acts{display:flex;gap:10px;margin-top:auto;padding-top:6px}
.card .acts .btn{min-height:44px}
.adslot{grid-column:1/-1;background:#fff;border:1px dashed var(--line-d);border-radius:14px;padding:10px}
.showmore{display:block;margin:22px auto 0;min-height:44px;padding:0 26px}
[hidden]{display:none!important}
.emptybox{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;margin-top:16px}
.emptybox .fb-note{margin-top:10px;font-size:14px;color:var(--mut)}
.brow .bmain .bstat{font-size:13px;font-weight:700}
.feat-empty{color:var(--mut);font-size:15px}
.slide .pill{margin-bottom:8px}
.slide .saward{font-weight:600}
.bleft.open{color:var(--ok)}
.bleft.urgent{color:var(--crit)}
.bleft.closed{color:#5f5b7c}
.bleft.warn{color:var(--warn)}
.mplan-row{display:flex;gap:12px;align-items:flex-start;padding:14px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.mplan-row .mtitle{font-weight:700}
.mplan-row .mtitle a{color:var(--ink);text-decoration:none}
.mplan-row .mtitle a:hover{text-decoration:underline}
.mplan-meta{font-size:14px;color:var(--mut)}
.cmpick{display:flex;align-items:center;gap:6px;font-size:14px}
.cmpick input{width:20px;height:20px;accent-color:var(--navy)}
.fdrawer .fgroup{margin-bottom:18px}
.fdrawer .fgroup h3{font-size:15px;margin-bottom:8px}
.fcheck{display:flex;align-items:center;gap:8px;padding:7px 0;cursor:pointer}
.fcheck input{width:20px;height:20px;accent-color:var(--navy)}
.fcheck .c{margin-left:auto;color:var(--mut);font-size:13px}
.fselect{width:100%;min-height:44px;border:1px solid var(--line-d);border-radius:10px;padding:0 12px;font:inherit;background:#fff}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media(max-width:700px){.tabs,.togrow{position:sticky;top:66px;z-index:40;background:var(--bg);padding:8px 0}}
"""

HTML_TEMPLATE = r"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>StudyDesk Scholarships — Find open scholarships for Indian students</title>
<link rel="canonical" href="https://scholarships.studydesk.fun/">
<meta name="description" content="Find open scholarships for Indian students — real deadlines, real eligibility, official application links. No account needed.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>@@STYLE@@</style>
</head>
<body>
<a class="skip" href="#matcher">Skip to matcher</a>
<header class="hdr"><div class="hdr-in">
<a class="brand" href="#top" aria-label="StudyDesk Scholarships home"><img src="/articles/logos/studydesk.png" alt="StudyDesk logo"><span class="bt">StudyDesk<small>Scholarships</small></span></a>
<nav class="main" aria-label="Primary"><a href="#matcher">Matcher</a><a href="#closing">Closing soon</a><a href="#results">Browse</a><a href="#deadlines">Deadlines</a><a href="#guides">Guides</a><a href="#how">How it works</a></nav>
<span class="sp"></span>
<button class="slist-btn" id="openMyPlan" aria-haspopup="dialog"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12a1 1 0 0 1 1 1v17l-7-4-7 4V4a1 1 0 0 1 1-1z"/></svg> My plan <span class="cnt" id="myplanCount">0</span></button>
<button class="menu-btn" id="openNav" aria-label="Open menu" aria-haspopup="dialog"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<aside class="mnav" id="mnav" role="dialog" aria-modal="true" aria-label="Menu"><div class="scrim" data-close="mnav"></div><div class="panel"><div class="dhead"><h2>Menu</h2><button class="xbtn" data-close="mnav" aria-label="Close menu">×</button></div><div class="list"><a href="#matcher">Matcher</a><a href="#closing">Closing soon</a><a href="#results">Browse</a><a href="#deadlines">Deadlines</a><a href="#guides">Guides</a><a href="#how">How it works</a></div></div></aside>

<main class="wrap" id="top">
<section class="matcher" id="matcher" aria-label="Scholarship matcher">
<div class="sec-kick">Find your scholarship</div>
<h1>Find open scholarships</h1>
<p class="deck">Answer four questions and see only the scholarships that fit you. Every match uses the tags on the listing itself — never a keyword guess.</p>
<div class="mform">
<div><label for="mStudy">Studying</label><select id="mStudy"><option value="">Any level</option><option value="class910">Class 9–10</option><option value="class1112">Class 11–12</option><option value="diploma-iti">Diploma / ITI</option><option value="ug">Undergraduate</option><option value="pg">Postgraduate</option><option value="phd">PhD</option></select></div>
<div><label for="mWhere">Where</label><select id="mWhere"><option value="">Anywhere in India</option></select></div>
<div><label for="mFor">For</label><select id="mFor"><option value="">Anyone</option><option value="girls">Girls</option><option value="reserved">SC/ST/OBC</option><option value="income">Income-based</option><option value="disability">Disability</option></select></div>
<div><label for="mNeed">Need</label><select id="mNeed"><option value="">Any</option><option value="fees">Fees</option><option value="stipend">Stipend</option><option value="coaching">Coaching</option></select></div>
</div>
<div class="mrow"><button class="btn btn-amber" id="mMatch" type="button">See my matches</button><button class="btn btn-line" id="mBrowse" type="button">Browse all open</button></div>
<p class="mnote">No account. No application fee. Apply on the official site.</p>
<p class="mnote">SC/ST/OBC matches listings tagged Reserved; Girls matches listings tagged Girls. “Need” matches the award text (fees, stipend, or coaching) because listings carry no separate need tag.</p>
<p class="mcounts" id="heroCounts"></p>
</section>

<section class="feat" id="featured" aria-label="Featured scholarships" hidden><div class="feat-in"><div class="sec-kick">Closing soon · Featured</div><h2 class="sec-title">Deadlines approaching fast</h2><p class="sec-sub">Open Indian government, corporate and foundation schemes closing in the next 7 days, soonest first.</p><div class="slider" id="featSlider"><div class="slides" id="featTrack"></div><div class="sctrl"><button class="sbtn" id="featPrev" aria-label="Previous featured scholarship">‹</button><button class="sbtn" id="featNext" aria-label="Next featured scholarship">›</button></div><div class="dots" id="featDots" role="tablist" aria-label="Featured slides"></div></div></div></section>

<section id="closing" aria-label="Closing in 7 days"><div class="sec-kick">Closing in 7 days</div><h2 class="sec-title">Closing soon in India</h2><p class="sec-sub">Open Indian government, corporate and foundation schemes closing in the next 7 days, soonest first.</p><div id="closingRows"></div></section>

<section id="myplanSec" aria-label="My plan" hidden><div class="sec-kick">My plan</div><h2 class="sec-title">Your saved scholarships</h2><p class="sec-sub">Sorted by deadline, soonest open first.</p><div id="myplanRows"></div><div class="mrow"><button class="btn btn-navy" id="myplanCal" type="button">Add open deadlines to calendar</button><button class="btn btn-line" id="myplanCompare" type="button" hidden>Compare selected</button></div><p class="mnote">Saved only in this browser. Nothing is uploaded. Comparison clears when you refresh the page.</p></section>

<section class="discover" id="results" aria-label="Browse scholarships">
<div class="sec-kick">Browse</div>
<h2 class="sec-title" id="resultsHeading">Open scholarships</h2>
<div class="tabs" role="group" aria-label="Scholarship tabs"><button class="tabbtn" type="button" data-tab="india" aria-pressed="true">India</button><button class="tabbtn" type="button" data-tab="abroad" aria-pressed="false">Abroad</button><button class="tabbtn" type="button" data-tab="internships" aria-pressed="false">Internships</button></div>
<div class="togrow"><label><input type="checkbox" id="showClosed"> Show closed</label><button class="btn btn-line" id="openFilters" type="button" aria-haspopup="dialog">Filters</button><button class="btn btn-line" id="resetFilters" type="button">Reset filters</button></div>
<div class="searchbar" role="search"><input id="q" type="search" placeholder="Search title, provider, eligibility, state…" aria-label="Search scholarships" autocomplete="off"></div>
<div class="togrow"><label for="sortSel">Sort</label><select class="fselect" id="sortSel" style="max-width:280px"><option value="soonest">Soonest open deadline</option><option value="award">Award: high to low</option><option value="title">Title A–Z</option></select><label for="minAward">Min. award (Rs)</label><input class="fselect" id="minAward" type="number" min="0" inputmode="numeric" placeholder="e.g. 10000" style="max-width:180px"></div>
<div id="filterPanel"></div>
<div id="chips"></div>
<div class="grid" id="grid"></div>
<div class="emptybox" id="empty" hidden></div>
<button class="btn btn-navy showmore" id="showMore" type="button" hidden>Show more</button>
</section>

<section class="deadlines" id="deadlines"><div class="wrap" style="padding-top:60px;padding-bottom:60px"><div class="sec-kick">Deadline watch</div><h2 class="sec-title" style="color:#fff">Confirmed upcoming deadlines</h2><p class="sec-sub">Open scholarships and internships, soonest first. Download any date straight to your calendar.</p><div class="board" id="boardRows"></div><p class="sec-sub" style="margin-top:16px">Dates are student deadlines. Each row was checked on that listing's own verified date.</p></div></section>

<section class="guides" id="guides" aria-label="Student guides"><div class="guides-in"><div class="sec-kick">Student guides</div><h2 class="sec-title">In-depth guides, not just listings</h2><p class="sec-sub">Full explainers with eligibility, documents, award conditions and official sources — written from verified notifications.</p><div class="grid" id="guideGrid"></div></div></section>

<section class="how wrap" id="how"><div class="sec-kick">How it works</div><h2 class="sec-title">How a listing gets on this page</h2><div class="steps"><div class="step"><div class="sn">1</div><h3>Checked against the source</h3><p>Each listing is checked against the provider's own notification, portal or press release before publication. The verification date shown on every page is that listing's own date — never a site-wide claim.</p></div><div class="step"><div class="sn">2</div><h3>Official or mentioned by</h3><p>A link is called “Official source” only when it goes to the provider or a government portal. Aggregator pages (Buddy4Study, Bright Scholarship, Opportunity Desk and others) are labelled “Mentioned by”, never “Official source”.</p></div><div class="step"><div class="sn">3</div><h3>Apply on the official site</h3><p>Applications always happen on the provider's website — never here. Deadlines are recomputed every day from the listing's own date, so a closed scheme never shows as open.</p></div></div><div class="trust"><div class="tbox"><h3>Not a government website</h3><p>StudyDesk is an independent education guide — not a government website and not affiliated with any provider listed here. Always confirm details on the official portal before applying.</p></div></div></section>
</main>

<footer><div class="foot-in"><div><div class="foot-brand"><img src="/articles/logos/studydesk.png" alt="StudyDesk logo"><span class="bt">StudyDesk<small>Scholarships</small></span></div><p id="footCounts"></p></div><div><h4>Explore</h4><div class="fl"><a href="#results">All scholarships</a><a href="#closing">Closing soon</a><a href="#deadlines">Deadlines</a><a href="#guides">Guides</a></div></div><div><h4>StudyDesk</h4><div class="fl"><a href="https://studydesk.fun/about/">About</a><a href="https://studydesk.fun/">News</a><a href="https://studydesk.fun/seva/">Seva</a></div></div><div><h4>Contact</h4><div class="fl"><a href="https://wa.me/919905166009">WhatsApp: +91 99051 66009</a><a href="mailto:scholarships@studydesk.fun">scholarships@studydesk.fun</a></div></div></div><p class="naff-line">StudyDesk is an independent education guide — not a government website and not affiliated with any provider listed here.</p><div class="copy"><span>© 2026 StudyDesk</span><span>Shortlists are stored only in your browser. <a href="/privacy.html">Privacy</a></span></div></footer>

<aside class="fdrawer" id="fdrawer" role="dialog" aria-modal="true" aria-label="Filters"><div class="scrim" data-close="fdrawer"></div><div class="panel"><div class="dhead"><h2>Filters</h2><button class="xbtn" data-close="fdrawer" aria-label="Close filters">×</button></div><div id="filterPanelMobile"></div><div class="mrow" style="padding:0 18px 18px"><button class="btn btn-navy" id="mApply" type="button">Show results</button><button class="btn btn-line" id="mReset" type="button">Reset</button></div></div></aside>

<aside class="sdrawer" id="myplanDrawer" role="dialog" aria-modal="true" aria-label="My plan"><div class="scrim" data-close="myplanDrawer"></div><div class="panel"><div class="dhead"><h2>My plan</h2><button class="xbtn" data-close="myplanDrawer" aria-label="Close My plan">×</button></div><div class="list" id="myplanList"></div><div class="dfoot">Saved only in this browser. Nothing is uploaded.</div></div></aside>

<div class="cmpbar" id="cmpbar" hidden><b id="cmpCount">Compare (0)</b><button class="btn btn-amber" id="openCompare" type="button">Compare</button><button class="clr" id="clearCompare" type="button">Clear</button></div>
<div class="modal" id="cmpModal" role="dialog" aria-modal="true" aria-label="Compare scholarships"><div class="scrim" data-close="cmpModal"></div><div class="mbox"><div class="mhead"><h2>Compare scholarships</h2><button class="xbtn" data-close="cmpModal" aria-label="Close comparison">×</button></div><div id="cmpTableWrap"></div><p class="mnote" style="padding:0 18px 18px">Comparison clears when you refresh the page.</p></div></div>
<div class="toast" id="toast" role="status"></div>
<script>"use strict"; /*__DATA__*/ var DATA = @@DATA@@;</script>
<script>@@APPJS@@</script>
</body>
</html>
"""

APP_JS = r"""
/* v9 homepage app: every displayed status is computed from dl + today
   in Asia/Kolkata. Stored days/closed in DATA are never displayed. */
function todayKolkata(){ try{ return new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Kolkata'}).format(new Date()); }catch(e){ var d=new Date(); return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2); } }
var TODAY = todayKolkata();
var MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var GUIDES = @@GUIDEFILES@@;
var COUNTRY_CATS = @@COUNTRIES@@;
var AGGREGATORS = ['buddy4study.com','brightscholarship.com','opportunitydesk.org'];
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function escICS(s){ return String(s).replace(/\\/g,'\\\\').replace(/;/g,'\\;').replace(/,/g,'\\,').replace(/\r?\n/g,'\\n'); }
function daysDiff(dl){ if(!dl) return null; return Math.round((Date.parse(dl+'T00:00:00Z')-Date.parse(TODAY+'T00:00:00Z'))/86400000); }
function fmtDL(dl){ if(!dl) return ''; var p=dl.split('-'); var s=parseInt(p[2],10)+' '+MONTHS[parseInt(p[1],10)-1]; if(parseInt(p[0],10)!==parseInt(TODAY.slice(0,4),10)) s+=' '+p[0]; return s; }
function statusFor(dl){
  var d=daysDiff(dl);
  if(d===null) return {key:'warn',label:'Date not confirmed'};
  if(d<0) return {key:'closed',label:'Closed'};
  if(d===0) return {key:'urgent',label:'Closes today'};
  if(d<=7) return {key:'urgent',label:'Closes in '+d+' day'+(d===1?'':'s')};
  return {key:'open',label:'Closes '+fmtDL(dl)};
}
function isGuide(r){ return GUIDES.indexOf(r.file)>=0; }
function pillFor(r){ return isGuide(r) ? {key:'guide',label:'Guide'} : statusFor(r.dl); }
function wordCut(s,n){ s=String(s||'').replace(/\s+/g,' ').trim(); if(s.length<=n) return s; var c=s.slice(0,n); var i=c.lastIndexOf(' '); if(i>40) c=c.slice(0,i); return c+'…'; }
function firstSentence(s){ s=String(s||'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim(); if(!s) return ''; var m=s.match(/^[^.!?]+[.!?]/); return (m?m[0]:s).trim(); }
function cleanTitle(t){ return String(t||'').replace(/apply online/gi,'').replace(/\s*\|\s*.*$/,'').replace(/\s+/g,' ').trim(); }
function whoLine(r){ if(r.who && r.who.trim()) return wordCut(r.who,140); var s=firstSentence(r.sub); return s ? wordCut(s,120) : 'See the scholarship page for eligibility details.'; }
function firstAmount(text){ var m=String(text||'').match(/(Rs\.?|₹|€|\$|£|CHF)\s?[\d,]+(?:\.\d+)?/); if(!m) return null; var rest=String(text||'').slice(m.index+m[0].length); var u=rest.match(/^\s*((per\s+year|\/\s*year|a\s+year|per\s+month|\/\s*month|a\s+month|per\s+annum|lakh|crore|one-time)\b)/i); return m[0].trim()+(u?' '+u[1].replace(/\s+/g,' ').trim():''); }
function awardShort(r){ var a=String(r.award||'').trim(); if(!a) return 'Amount not stated'; if(a.length>90){ var f=firstAmount(a); var mx=runtimeAwardMax(r); if(mx!==null && f){ var fm=f.match(/([\d,]+)/); var fv=fm?parseInt(fm[1].replace(/,/g,''),10):null; if(fv!==null && mx>fv) return 'Up to Rs '+mx.toLocaleString('en-IN'); } return f || wordCut(a,90); } return a; }
function runtimeAwardMax(r){ if(typeof r.awardMax==='number') return r.awardMax; var m=String(r.award||'').match(/(Rs\.?|₹)\s?([\d,]+)/); if(!m) return null; var v=parseInt(m[2].replace(/,/g,''),10); return isNaN(v)?null:v; }
function hostOf(u){ if(!u) return ''; var m=String(u).match(/^https?:\/\/([^\/:?#]+)/i); return m ? m[1].replace(/^www\./,'') : ''; }
function isOfficial(r){
  var host=hostOf(r.srcUrl||''); if(!host) return false;
  var bare=host.replace(/^www\./,'');
  if(AGGREGATORS.indexOf(bare)>=0) return false;
  if(/\.gov(\.|$)|\.gov\.in$|\.nic\.in$/.test(bare)) return true;
  var stop={university:1,universities:1,college:1,school:1,institute:1,foundation:1,trust:1,scholarship:1,scholarships:1,programme:1,program:1,ministry:1,department:1,government:1,of:1,the:1,and:1,for:1,india:1,indian:1,international:1,national:1,state:1,central:1,ltd:1,limited:1,pvt:1,private:1,inc:1,llc:1,co:1,company:1,group:1,portal:1};
  var toks=String(r.provider||'').toLowerCase().split(/[^a-z0-9]+/);
  for(var i=0;i<toks.length;i++){ var t=toks[i]; if(t.length>=3 && !stop[t] && bare.indexOf(t)>=0) return true; }
  return false;
}
function isInternship(r){ return /internship/i.test(r.title||'') || (r.cats||[]).some(function(c){ return /internship/i.test(c); }); }
function catHasCountry(cats){
  for(var i=0;i<cats.length;i++){
    var parts=String(cats[i]).split(/\s*&\s*|\s+and\s+|\//);
    for(var j=0;j<parts.length;j++){ if(COUNTRY_CATS.indexOf(parts[j].trim())>=0) return true; }
  }
  return false;
}
function tabOf(r){
  if(isInternship(r)) return 'internships';
  if(r.ptype==='international') return 'abroad';
  // Fix pass 2026-11-03: the country-cat check sits ABOVE the ptype rule, so a
  // foreign-tagged government/corporate/foundation scheme lands in Abroad.
  if(catHasCountry(r.cats||[])) return 'abroad';
  if(r.ptype==='government'||r.ptype==='corporate'||r.ptype==='foundation') return 'india';
  if((r.states||[]).length>0) return 'india';
  var host=hostOf(r.srcUrl||'');
  if(/\.in$|\.gov\.in$|\.nic\.in$|\.ac\.in$|\.edu\.in$/.test(host)) return 'india';
  if(/\.(de|fr|it|es|nl|be|ch|at|se|no|dk|fi|au|ca|jp|kr|cn|sg|my|ae|qa|sa|uk|us)$/.test(host)) return 'abroad';
  return 'india';
}
function isOpenR(r){ if(isGuide(r)) return true; return statusFor(r.dl).key!=='closed'; }
function openDated(r){ return !isGuide(r) && !!r.dl && statusFor(r.dl).key!=='closed'; }
function soonestCmp(a,b){
  if(isGuide(a)!==isGuide(b)) return isGuide(a)?1:-1;
  var da=daysDiff(a.dl), db=daysDiff(b.dl);
  if(da===null && db===null) return 0; if(da===null) return 1; if(db===null) return -1;
  if(da<0 && db<0) return db-da; if(da<0) return 1; if(db<0) return -1;
  return da-db;
}
/* ---- state ---- */
var DEF = {tab:'india',edu:[],states:[],support:[],need:'',q:'',sort:'soonest',showClosed:false,minAward:''};
var S = JSON.parse(JSON.stringify(DEF));
var visible = 24;
var byId = {}; DATA.forEach(function(r){ byId[r.id]=r; });
var STATE_LIST = (function(){ var c={}; DATA.forEach(function(r){ (r.states||[]).forEach(function(s){ if(s!=='National') c[s]=(c[s]||0)+1; }); }); return Object.keys(c).sort(function(a,b){ return (c[b]-c[a]) || (a<b?-1:1); }); })();
var EDU_L = {class910:'Classes 9–10',class1112:'Classes 11–12',diploma:'Diploma',iti:'ITI',ug:'Undergraduate',pg:'Postgraduate',phd:'PhD / Doctoral'};
var SUP_L = {girls:'Girls',reserved:'SC/ST/OBC (Reserved)',income:'Income-based',disability:'Disability',minority:'Minority',merit:'Merit-based',sports:'Sports'};
function eduCount(tag){ var n=0; DATA.forEach(function(r){ if(tabOf(r)!==S.tab) return; if((r.edu||[]).indexOf(tag)>=0) n++; }); return n; }
function supCount(tag){ var n=0; DATA.forEach(function(r){ if(tabOf(r)!==S.tab) return; if((r.support||[]).indexOf(tag)>=0) n++; }); return n; }
function shortlist(){ try{ var v=JSON.parse(localStorage.getItem('sd_shortlist')||'[]'); return Array.isArray(v)?v.filter(function(id){ return !!byId[id]; }):[]; }catch(e){ return []; } }
function setShortlist(ids){ try{ localStorage.setItem('sd_shortlist', JSON.stringify(ids)); }catch(e){} }
function isSaved(id){ return shortlist().indexOf(id)>=0; }
function toast(msg){ var t=document.getElementById('toast'); if(!t) return; t.textContent=msg; t.classList.add('show'); setTimeout(function(){ t.classList.remove('show'); },2600); }
/* ---- filters ---- */
function filterPanelHTML(){
  var e='<div class="fgroup"><h3>Education level</h3>';
  Object.keys(EDU_L).forEach(function(tag){ e+='<label class="fcheck"><input type="checkbox" data-fgroup="edu" value="'+tag+'"> '+EDU_L[tag]+' <span class="c">'+eduCount(tag)+'</span></label>'; });
  // Fix pass 2026-11-03: the State filter only exists on the India tab. On
  // Abroad/Internships it could only ever yield the (now removed) fallback.
  if(S.tab==='india'){
    e+='</div><div class="fgroup"><h3>State</h3><select class="fselect stateSel" aria-label="Filter by state"><option value="">Anywhere in India</option>';
    STATE_LIST.forEach(function(s){ e+='<option value="'+esc(s)+'">'+esc(s)+'</option>'; });
    e+='</select></div>';
  } else {
    e+='</div>';
  }
  e+='<div class="fgroup"><h3>For</h3>';
  Object.keys(SUP_L).forEach(function(tag){ e+='<label class="fcheck"><input type="checkbox" data-fgroup="support" value="'+tag+'"> '+SUP_L[tag]+' <span class="c">'+supCount(tag)+'</span></label>'; });
  e+='</div>';
  return e;
}
function needPass(r){
  if(!S.need) return true;
  var a=String(r.award||''), t=String(r.title||''), c=(r.cats||[]).join(' ');
  if(S.need==='fees') return /fee|tuition/i.test(a);
  if(S.need==='stipend') return /stipend|per month|\/month|a month/i.test(a);
  if(S.need==='coaching') return /coaching/i.test(t+' '+c+' '+a);
  return true;
}
function haystack(r){ return (cleanTitle(r.title)+' '+r.provider+' '+(r.who||'')+' '+(r.states||[]).join(' ')+' '+(r.cats||[]).join(' ')+' '+whoLine(r)).toLowerCase(); }
function passFilters(r, skipStates){
  // Fix pass 2026-11-03: guides live in their own section, never in the
  // browse grid; the same predicate serves the grid and (minus the state
  // condition) the all-India fallback, so the fallback can no longer ignore
  // the tab and the other filters.
  if(isGuide(r)) return false;
  if(tabOf(r)!==S.tab) return false;
  if(!S.showClosed && !isOpenR(r)) return false;
  if(S.edu.length && !S.edu.some(function(t){ return (r.edu||[]).indexOf(t)>=0; })) return false;
  if(!skipStates && S.states.length && !(r.states||[]).some(function(s){ return S.states.indexOf(s)>=0; })) return false;
  if(S.support.length && !S.support.some(function(t){ return (r.support||[]).indexOf(t)>=0; })) return false;
  if(!needPass(r)) return false;
  if(S.minAward!=='' && !isNaN(parseFloat(S.minAward))){ var am=runtimeAwardMax(r); if(am===null || am<parseFloat(S.minAward)) return false; }
  var q=(S.q||'').toLowerCase().trim(); var words=q?q.split(/\s+/):[];
  if(words.length && !words.every(function(w){ return haystack(r).indexOf(w)>=0; })) return false;
  return true;
}
function filtered(){
  var list=DATA.filter(function(r){ return passFilters(r,false); });
  if(S.sort==='award'){ list.sort(function(a,b){ var x=runtimeAwardMax(a), y=runtimeAwardMax(b); if(x===null && y===null) return soonestCmp(a,b); if(x===null) return 1; if(y===null) return -1; return (y-x) || soonestCmp(a,b); }); }
  else if(S.sort==='title'){ list.sort(function(a,b){ return cleanTitle(a.title).localeCompare(cleanTitle(b.title)); }); }
  else { list.sort(soonestCmp); }
  return list;
}
var TINY_LOGOS={"logos/fav-andaman.png":1,"logos/fav-apu.png":1,"logos/fav-auc.png":1,"logos/fav-bifonds.png":1,"logos/fav-bookachange.png":1,"logos/fav-broadinstitute.png":1,"logos/fav-campusfrance.png":1,"logos/fav-ceepus.png":1,"logos/fav-cgu.png":1,"logos/fav-concentrix.png":1,"logos/fav-csir.png":1,"logos/fav-deakin.png":1,"logos/fav-dgut.png":1,"logos/fav-eastman.png":1,"logos/fav-fes.png":1,"logos/fav-fulbrightse.png":1,"logos/fav-gatescambridge.png":1,"logos/fav-gem-usa.png":1,"logos/fav-gxnu.png":1,"logos/fav-hansen.png":1,"logos/fav-hdfc.png":1,"logos/fav-ieg-mainz.png":1,"logos/fav-italy.png":1,"logos/fav-kindcircle.png":1,"logos/fav-lawai.png":1,"logos/fav-manchester.png":1,"logos/fav-moe.png":1,"logos/fav-nshm.png":1,"logos/fav-ntusg.png":1,"logos/fav-perugia.png":1,"logos/fav-qatarairways.png":1,"logos/fav-rgc.png":1,"logos/fav-rgu.png":1,"logos/fav-saia.png":1,"logos/fav-sophia.png":1,"logos/fav-southampton.png":1,"logos/fav-szu.png":1,"logos/fav-tigp.png":1,"logos/fav-tsukuba.png":1,"logos/fav-ubd.png":1,"logos/fav-udmercy.png":1,"logos/fav-uga.png":1,"logos/fav-ugm.png":1,"logos/fav-uic.png":1,"logos/fav-um.png":1,"logos/fav-umdearborn.png":1,"logos/fav-umn.png":1,"logos/fav-wto.png":1,"logos/fav-yeungnam.png":1,"logos/hokudai.png":1,"logos/nims-go-jp.png":1,"logos/nycu.png":1,"logos/ujjivan.png":1};
function cardHTML(r){
  var st=pillFor(r), saved=isSaved(r.id);
  var initial=esc((r.provider||'S').trim().charAt(0).toUpperCase());
  var logo=(r.logo&&!TINY_LOGOS[r.logo])?'<img src="/articles/'+esc(r.logo)+'" alt="" loading="lazy" onerror="this.remove()">':'';
  var host=hostOf(r.srcUrl||'');
  var trust=host?esc(host)+' · Checked '+esc(r.verified):'Checked '+esc(r.verified);
  return '<article class="card"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span>'
  +'<h3><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></h3>'
  +'<p class="prov"><span class="plogo">'+initial+logo+'</span>'+esc(r.provider)+'</p>'
  +'<p class="who">'+esc(whoLine(r))+'</p>'
  +'<p class="award">'+esc(awardShort(r))+'</p>'
  +'<p class="trust">'+trust+'</p>'
  +'<div class="acts"><a class="btn btn-navy" href="'+esc(r.file)+'">View details</a>'
  +'<button class="btn btn-line" type="button" data-save="'+r.id+'" aria-pressed="'+saved+'">'+(saved?'Saved ✓':'Save')+'</button></div></article>';
}
var adDiv=null, adPushed=false;
function placeAd(){
  var grid=document.getElementById('grid'); if(!grid) return;
  if(!adDiv){
    adDiv=document.createElement('div'); adDiv.className='adslot';
    adDiv.innerHTML=@@ADSENSE_INS@@;
    var sc=document.createElement('script'); sc.async=true; sc.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3573504055334993'; sc.setAttribute('crossorigin','anonymous'); adDiv.appendChild(sc);
  }
  var cards=grid.querySelectorAll('.card');
  if(cards.length>=3 && grid.children[3]!==adDiv) grid.insertBefore(adDiv, grid.children[3]);
  else if(cards.length>0 && cards.length<3 && !grid.contains(adDiv)) grid.appendChild(adDiv);
  if(!adPushed){ try{ (window.adsbygoogle=window.adsbygoogle||[]).push({}); adPushed=true; }catch(e){} }
}
function chipHTML(group,val,label){ return '<span class="chip">'+esc(label)+'<button type="button" data-unchip="'+group+':'+esc(val)+'" aria-label="Remove filter '+esc(label)+'">×</button></span>'; }
function renderChips(){
  var el=document.getElementById('chips'); if(!el) return; var h='';
  S.edu.forEach(function(t){ h+=chipHTML('edu',t,EDU_L[t]); });
  S.states.forEach(function(s){ h+=chipHTML('states',s,s); });
  S.support.forEach(function(t){ h+=chipHTML('support',t,SUP_L[t]); });
  if(S.need) h+=chipHTML('need',S.need,{fees:'Fees',stipend:'Stipend',coaching:'Coaching'}[S.need]);
  if(S.q) h+='<span class="chip">Search: “'+esc(S.q)+'”<button type="button" data-unchip="q:" aria-label="Clear search">×</button></span>';
  if(S.minAward!=='') h+=chipHTML('minAward',S.minAward,'Min. Rs '+esc(S.minAward));
  if(h) h+='<span class="chip clear">Reset all<button type="button" data-unchip="all:" aria-label="Reset all filters">×</button></span>';
  el.innerHTML=h;
}
function render(){
  var list=filtered();
  var grid=document.getElementById('grid');
  var emptyBox=document.getElementById('empty');
  var showMore=document.getElementById('showMore');
  var heading=document.getElementById('resultsHeading');
  var openCount=list.filter(function(r){ return !isGuide(r) && statusFor(r.dl).key!=='closed'; }).length;
  var shown=list.slice(0,visible);
  var stateFallback=null;
  var headingOverride=null;
  if(list.length===0 && S.states.length===1 && S.tab==='india'){
    var st=S.states[0];
    stateFallback=DATA.filter(function(r){ return passFilters(r,true) && isOpenR(r) && ( ((r.states||[]).indexOf('National')>=0) || (r.ptype==='government' && (r.states||[]).length===0) ); }).sort(soonestCmp);
    if(stateFallback.length){
      emptyBox.innerHTML='<strong>No '+esc(st)+'-only schemes are tagged yet.</strong><p class="fb-note">Showing open schemes below under “All-India or state not tagged” — these are not '+esc(st)+' schemes. National-tagged schemes and government schemes with no state tag.</p>';
      emptyBox.hidden=false;
      grid.innerHTML=stateFallback.slice(0,visible).map(cardHTML).join('');
      if(showMore) showMore.hidden = stateFallback.length<=visible;
      headingOverride=(stateFallback.length===1 ? '1 open all-India scholarship' : stateFallback.length+' open all-India scholarships');
    }
  }
  // An empty fallback array is falsy in intent but truthy in JS: without the
  // length check the grid below would keep the previous tab's cards.
  if(!stateFallback || !stateFallback.length){
    if(list.length===0){
      emptyBox.innerHTML='<strong>No scholarships match these filters.</strong><p class="fb-note">Try clearing a filter or searching a different word.</p>';
      emptyBox.hidden=false; grid.innerHTML='';
      if(showMore) showMore.hidden=true;
    } else {
      emptyBox.hidden=true;
      grid.innerHTML=shown.map(cardHTML).join('');
      if(showMore) showMore.hidden = list.length<=visible;
    }
  }
  if(heading) heading.textContent = headingOverride || (S.showClosed ? (list.length===1 ? '1 scholarship' : list.length+' scholarships') : (openCount===1 ? '1 open scholarship' : openCount+' open scholarships'));
  renderChips();
  if(grid && grid.querySelectorAll('.card').length) placeAd();
  renderMyPlan(); renderCounts(); renderBoard();
  try{ sessionStorage.setItem('sd_state', JSON.stringify(S)); }catch(e){}
}
function renderCounts(){
  var open=0, c7=0, c30=0;
  DATA.forEach(function(r){ if(isGuide(r)) return; var d=daysDiff(r.dl); if(d===null){ open++; return; } if(d<0) return; open++; if(d<=7) c7++; if(d<=30) c30++; });
  var hc=document.getElementById('heroCounts'); if(hc) hc.textContent=(open===1 ? '1 open scholarship' : open+' open scholarships')+' · '+c7+' closing in the next 7 days · '+c30+' closing in the next 30 days';
  var fc=document.getElementById('footCounts'); if(fc) fc.textContent=(open===1 ? '1 open scholarship' : open+' open scholarships')+' · '+c7+' closing in the next 7 days. Deadlines recomputed daily from each listing\'s own date.';
}
function indiaClosing7(){
  return DATA.filter(function(r){ return !isGuide(r) && (r.ptype==='government'||r.ptype==='corporate'||r.ptype==='foundation') && (function(){ var d=daysDiff(r.dl); return d!==null && d>=0 && d<=7; })(); }).sort(soonestCmp);
}
function renderClosing(){
  var el=document.getElementById('closingRows'); if(!el) return;
  var rows=indiaClosing7().slice(0,6);
  if(!rows.length){
    var next=DATA.filter(function(r){ return !isGuide(r) && (r.ptype==='government'||r.ptype==='corporate'||r.ptype==='foundation') && !!r.dl && daysDiff(r.dl)>=0; }).sort(soonestCmp)[0];
    el.innerHTML='<div class="emptybox"><strong>No Indian government, corporate or foundation schemes close in the next 7 days.</strong>'
    +(next?'<p class="fb-note">The soonest such deadline is <a href="'+esc(next.file)+'">'+esc(cleanTitle(next.title))+'</a> — '+esc(statusFor(next.dl).label)+'.</p>':'')
    +'</div>';
    return;
  }
  el.innerHTML=rows.map(function(r){ var st=statusFor(r.dl); return '<div class="mplan-row"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><div><div class="mtitle"><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></div><div class="mplan-meta">'+esc(r.provider)+' · '+esc(awardShort(r))+'</div></div></div>'; }).join('');
}
var featIdx=0, featSlides=[];
function renderFeatured(){
  var sec=document.getElementById('featured'); if(!sec) return;
  featSlides=indiaClosing7().slice(0,4); featIdx=0;
  if(!featSlides.length){ sec.hidden=true; return; }
  sec.hidden=false;
  var track=document.getElementById('featTrack'); if(!track) return;
  track.innerHTML=featSlides.map(function(r,i){ var st=statusFor(r.dl); return '<div class="slide"'+(i===0?' role="tabpanel"':' hidden')+' aria-label="'+esc(cleanTitle(r.title))+'"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><h3><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></h3><p class="prov">'+esc(r.provider)+'</p><p class="saward">'+esc(awardShort(r))+'</p><p class="trust">Checked '+esc(r.verified)+'</p><div class="cta-row"><a class="btn btn-navy" href="'+esc(r.file)+'">View details</a></div></div>'; }).join('');
  var dots=document.getElementById('featDots'); if(dots) dots.innerHTML=featSlides.map(function(r,i){ return '<button type="button" role="tab" aria-selected="'+(i===0?'true':'false')+'" aria-label="Go to slide '+(i+1)+'" data-slide="'+i+'"></button>'; }).join('');
}
function featGo(i){ if(!featSlides.length) return; featIdx=(i+featSlides.length)%featSlides.length; var track=document.getElementById('featTrack'); if(!track) return; Array.prototype.forEach.call(track.children,function(el,j){ if(j===featIdx){ el.hidden=false; el.setAttribute('role','tabpanel'); } else { el.hidden=true; el.removeAttribute('role'); } }); var dots=document.getElementById('featDots'); if(dots) Array.prototype.forEach.call(dots.children,function(b,j){ b.setAttribute('aria-selected', j===featIdx?'true':'false'); }); }
function renderBoard(){
  var el=document.getElementById('boardRows'); if(!el) return;
  var rows=DATA.filter(function(r){ return openDated(r) && tabOf(r)===S.tab; }).sort(soonestCmp).slice(0,12);
  el.innerHTML=rows.map(function(r){ var st=statusFor(r.dl); var p=r.dl.split('-'); return '<div class="brow"><span class="bdate"><b>'+parseInt(p[2],10)+'</b><span>'+MONTHS[parseInt(p[1],10)-1]+'</span></span><span class="bmain"><strong><a href="'+esc(r.file)+'" style="color:var(--ink);text-decoration:none">'+esc(wordCut(cleanTitle(r.title),62))+'</a></strong><span>'+esc(wordCut(r.provider+' · '+awardShort(r),72))+'</span></span><span class="bside"><span class="bleft '+st.key+'">'+esc(st.label)+'</span><button class="bdl" type="button" data-ics="'+r.id+'" aria-label="Download calendar file for '+esc(cleanTitle(r.title))+'">Calendar ↓</button></span></div>'; }).join('');
}
function renderGuides(){
  var el=document.getElementById('guideGrid'); if(!el) return;
  var files=@@GUIDEFILES@@;
  el.innerHTML=files.map(function(f){ var r=byId[Object.keys(byId).filter(function(id){ return byId[id].file===f; })[0]]; if(!r) return ''; var initial=esc((r.provider||'S').trim().charAt(0).toUpperCase()); var logo=(r.logo&&!TINY_LOGOS[r.logo])?'<img src="/articles/'+esc(r.logo)+'" alt="" loading="lazy" onerror="this.remove()">':''; var blurb=awardShort(r)!=='Amount not stated'?awardShort(r):whoLine(r); return '<article class="gcard"><div class="gcover">'+logo+'<span class="gt">'+initial+'</span></div><div class="gbody"><span class="gk">Guide · '+esc(r.provider)+'</span><h3><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></h3><p>'+esc(wordCut(blurb,140))+'</p><span class="gm">Checked '+esc(r.verified)+'</span><a class="gr" href="'+esc(r.file)+'">Read the full guide →</a></div></article>'; }).join('');
}
function myplanRecords(){ return shortlist().map(function(id){ return byId[id]; }).filter(Boolean).sort(soonestCmp); }
var compareSel=[];
function sourceLinkHTML(r){
  var host=hostOf(r.srcUrl||''); if(!host) return '<span class="na">No source link on file</span>';
  if(isOfficial(r)) return '<a href="'+esc(r.srcUrl)+'" rel="noopener">Apply on '+esc(host)+'</a>';
  return '<a href="'+esc(r.srcUrl)+'" rel="noopener">Mentioned by '+esc(host)+'</a>';
}
function renderMyPlan(){
  var savedIds=shortlist();
  compareSel=compareSel.filter(function(id){ return savedIds.indexOf(id)>=0; });
  var recs=myplanRecords();
  var cnt=document.getElementById('myplanCount'); if(cnt) cnt.textContent=recs.length;
  var sec=document.getElementById('myplanSec'); if(sec) sec.hidden = recs.length===0;
  var rows=document.getElementById('myplanRows');
  if(rows){
    if(!recs.length){ rows.innerHTML=''; }
    else rows.innerHTML=recs.map(function(r){ var st=pillFor(r); var checked=compareSel.indexOf(r.id)>=0; return '<div class="mplan-row"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><div style="flex:1"><div class="mtitle"><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></div><div class="mplan-meta">'+esc(r.provider)+' · '+sourceLinkHTML(r)+'</div></div><label class="cmpick"><input type="checkbox" data-cmpchk="'+r.id+'"'+(checked?' checked':'')+'> Compare</label><button class="btn btn-line" type="button" data-unsave="'+r.id+'">Remove</button></div>'; }).join('');
  }
  var list=document.getElementById('myplanList');
  if(list){
    if(!recs.length){ list.innerHTML='<p>Nothing saved yet. Save a scholarship and it stays on this device.</p>'; }
    else list.innerHTML=recs.map(function(r){ var st=pillFor(r); return '<div class="sitem"><span class="pill st-'+st.key+'">'+esc(st.label)+'</span><div><div class="mtitle"><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></div><div class="mplan-meta">'+esc(r.provider)+' · '+sourceLinkHTML(r)+'</div></div></div>'; }).join('');
  }
  var cb=document.getElementById('myplanCompare'); if(cb) cb.hidden = compareSel.length<2;
  var bar=document.getElementById('cmpbar'); if(bar) bar.hidden = compareSel.length<2;
  var cc=document.getElementById('cmpCount'); if(cc) cc.textContent='Compare ('+compareSel.length+')';
}
function downloadICS(d){
  var dt=d.dl.replace(/-/g,'');
  var stamp=new Date().toISOString().replace(/[-:]/g,'').split('.')[0]+'Z';
  var ics=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//StudyDesk//Scholarships//EN','BEGIN:VEVENT','UID:'+d.id+'@scholarships.studydesk.fun','DTSTAMP:'+stamp,'DTSTART;TZID=Asia/Kolkata:'+dt+'T235900','SUMMARY:'+escICS(d.title+' — application deadline'),'DESCRIPTION:'+escICS(d.provider+'. Apply: https://scholarships.studydesk.fun/'+d.file),'END:VEVENT','END:VCALENDAR'].join('\r\n');
  var a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'})); a.download=d.id+'-deadline.ics'; document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); },400); toast('Calendar file downloaded.');
}
function downloadMyPlanICS(){
  var recs=myplanRecords().filter(function(r){ return openDated(r); });
  if(!recs.length){ toast('No open dated deadlines in My plan.'); return; }
  var stamp=new Date().toISOString().replace(/[-:]/g,'').split('.')[0]+'Z';
  var parts=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//StudyDesk//Scholarships//EN'];
  recs.forEach(function(d){ var dt=d.dl.replace(/-/g,''); parts.push('BEGIN:VEVENT','UID:'+d.id+'@scholarships.studydesk.fun','DTSTAMP:'+stamp,'DTSTART;TZID=Asia/Kolkata:'+dt+'T235900','SUMMARY:'+escICS(d.title+' — application deadline'),'DESCRIPTION:'+escICS(d.provider+'. Apply: https://scholarships.studydesk.fun/'+d.file),'END:VEVENT'); });
  parts.push('END:VCALENDAR');
  var a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([parts.join('\r\n')],{type:'text/calendar'})); a.download='my-plan-deadlines.ics'; document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); },400); toast('Calendar file downloaded.');
}
function renderCompareTable(){
  var wrap=document.getElementById('cmpTableWrap'); if(!wrap) return;
  var recs=compareSel.map(function(id){ return byId[id]; }).filter(Boolean);
  if(!recs.length){ wrap.innerHTML='<p>No scholarships selected for comparison.</p>'; return; }
  var h='<table class="cmp-table"><thead><tr><th>Scholarship</th><th>Provider</th><th>Status</th><th>Award</th></tr></thead><tbody>';
  recs.forEach(function(r){ var st=pillFor(r); h+='<tr><td><a href="'+esc(r.file)+'">'+esc(cleanTitle(r.title))+'</a></td><td>'+esc(r.provider)+'</td><td>'+esc(st.label)+'</td><td>'+esc(awardShort(r))+'</td></tr>'; });
  wrap.innerHTML=h+'</tbody></table>';
}
function syncFilterUI(){
  document.querySelectorAll('[data-fgroup]').forEach(function(cb){ var g=cb.dataset.fgroup; cb.checked = S[g].indexOf(cb.value)>=0; });
  document.querySelectorAll('.stateSel').forEach(function(sel){ sel.value = S.states.length?S.states[0]:''; });
  var ss=document.getElementById('sortSel'); if(ss) ss.value=S.sort;
  var ma=document.getElementById('minAward'); if(ma) ma.value=S.minAward;
  var sc=document.getElementById('showClosed'); if(sc) sc.checked=!!S.showClosed;
  var q=document.getElementById('q'); if(q && document.activeElement!==q) q.value=S.q;
  document.querySelectorAll('[data-tab]').forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.tab===S.tab?'true':'false'); });
}
function resetAll(){ S=JSON.parse(JSON.stringify(DEF)); visible=24; var q=document.getElementById('q'); if(q) q.value=''; ['mStudy','mWhere','mFor','mNeed'].forEach(function(id){ var s=document.getElementById(id); if(s) s.value=''; }); var fp=el('filterPanel'); if(fp) fp.innerHTML=filterPanelHTML(); var fpm=el('filterPanelMobile'); if(fpm) fpm.innerHTML=filterPanelHTML(); syncFilterUI(); render(); }
function openOverlay(id){ var el=document.getElementById(id); if(el) el.classList.add('open'); }
function closeOverlay(id){ var el=document.getElementById(id); if(el) el.classList.remove('open'); }
function el(id){ return document.getElementById(id); }
function bind(id,ev,fn){ var x=el(id); if(x) x.addEventListener(ev,fn); }
function init(){
  var mw=el('mWhere'); if(mw){ mw.innerHTML='<option value="">Anywhere in India</option>'+STATE_LIST.map(function(s){ return '<option value="'+esc(s)+'">'+esc(s)+'</option>'; }).join('')+'<option value="abroad">Abroad</option>'; }
  var fp=el('filterPanel'); if(fp) fp.innerHTML=filterPanelHTML();
  var fpm=el('filterPanelMobile'); if(fpm) fpm.innerHTML=filterPanelHTML();
  try{
    var raw=sessionStorage.getItem('sd_state');
    if(raw){ var saved=JSON.parse(raw); var trial=JSON.parse(JSON.stringify(DEF)); Object.keys(DEF).forEach(function(k){ if(saved[k]!==undefined) trial[k]=saved[k]; }); var keep=S; S=trial; var n=filtered().length; if(n===0){ S=keep; try{ sessionStorage.removeItem('sd_state'); }catch(e){} } }
  }catch(e){}
  syncFilterUI(); render(); renderClosing(); renderFeatured(); renderBoard(); renderGuides();
  document.addEventListener('change',function(e){
    var t=e.target;
    if(t.matches && t.matches('[data-fgroup]')){ var g=t.dataset.fgroup, arr=S[g]; if(t.checked){ if(arr.indexOf(t.value)<0) arr.push(t.value); } else { var i=arr.indexOf(t.value); if(i>=0) arr.splice(i,1); } visible=24; syncFilterUI(); render(); }
    else if(t.classList && t.classList.contains('stateSel')){ S.states = t.value ? [t.value] : []; visible=24; syncFilterUI(); render(); }
    else if(t.id==='sortSel'){ S.sort=t.value; visible=24; render(); }
    else if(t.id==='showClosed'){ S.showClosed=t.checked; visible=24; render(); }
    else if(t.matches && t.matches('[data-cmpchk]')){ var id=t.dataset.cmpchk; var j=compareSel.indexOf(id); if(t.checked){ if(j<0 && compareSel.length<3) compareSel.push(id); else if(j<0){ t.checked=false; toast('You can compare up to 3 scholarships.'); } } else if(j>=0) compareSel.splice(j,1); renderMyPlan(); }
  });
  document.addEventListener('input',function(e){
    var t=e.target;
    if(t.id==='q'){ S.q=t.value; visible=24; render(); }
    else if(t.id==='minAward'){ S.minAward=t.value; visible=24; render(); }
  });
  document.addEventListener('click',function(e){
    var u=e.target.closest?e.target.closest('[data-unchip]'):null;
    if(u){ var parts=u.dataset.unchip.split(':'), g=parts[0], v=parts.slice(1).join(':'); if(g==='all'){ resetAll(); return; } if(g==='q'){ S.q=''; var q=el('q'); if(q) q.value=''; } else if(g==='minAward'){ S.minAward=''; } else { var i=S[g].indexOf(v); if(i>=0) S[g].splice(i,1); } visible=24; syncFilterUI(); render(); return; }
    var sv=e.target.closest?e.target.closest('[data-save]'):null;
    if(sv){ var id=sv.dataset.save; var ids=shortlist(); var k=ids.indexOf(id); if(k>=0) ids.splice(k,1); else ids.push(id); setShortlist(ids); sv.textContent = k>=0?'Save':'Saved ✓'; sv.setAttribute('aria-pressed', k>=0?'false':'true'); renderMyPlan(); toast(k>=0?'Removed from My plan.':'Saved to My plan.'); return; }
    var un=e.target.closest?e.target.closest('[data-unsave]'):null;
    if(un){ var ids2=shortlist(); var k2=ids2.indexOf(un.dataset.unsave); if(k2>=0) ids2.splice(k2,1); setShortlist(ids2); renderMyPlan(); render(); return; }
    var tb=e.target.closest?e.target.closest('[data-tab]'):null;
    if(tb){ S.tab=tb.dataset.tab; S.states=[]; visible=24; var fp=el('filterPanel'); if(fp) fp.innerHTML=filterPanelHTML(); var fpm=el('filterPanelMobile'); if(fpm) fpm.innerHTML=filterPanelHTML(); syncFilterUI(); render(); return; }
    var ics=e.target.closest?e.target.closest('[data-ics]'):null;
    if(ics){ var rec=byId[ics.dataset.ics]; if(rec) downloadICS(rec); return; }
    var dot=e.target.closest?e.target.closest('[data-slide]'):null;
    if(dot){ featGo(parseInt(dot.dataset.slide,10)); return; }
    var c=e.target.closest?e.target.closest('[data-close]'):null;
    if(c){ closeOverlay(c.dataset.close); return; }
  });
  bind('mMatch','click',function(){ var st=el('mStudy')?el('mStudy').value:''; var wh=el('mWhere')?el('mWhere').value:''; var fo=el('mFor')?el('mFor').value:''; var ne=el('mNeed')?el('mNeed').value:''; S.tab = wh==='abroad'?'abroad':'india'; S.edu = !st?[]:(st==='diploma-iti'?['diploma','iti']:[st]); S.states = (wh && wh!=='abroad')?[wh]:[]; S.support = fo?[fo]:[]; S.need=ne; S.q=''; S.showClosed=false; S.sort='soonest'; S.minAward=''; visible=24; var fp=el('filterPanel'); if(fp) fp.innerHTML=filterPanelHTML(); var fpm=el('filterPanelMobile'); if(fpm) fpm.innerHTML=filterPanelHTML(); syncFilterUI(); render(); var r=el('results'); if(r) r.scrollIntoView(); });
  bind('mBrowse','click',function(){ resetAll(); var r=el('results'); if(r) r.scrollIntoView(); });
  bind('showMore','click',function(){ visible+=24; render(); });
  bind('resetFilters','click',resetAll);
  bind('mReset','click',resetAll);
  bind('emptyReset','click',resetAll);
  bind('openNav','click',function(){ openOverlay('mnav'); });
  bind('openFilters','click',function(){ openOverlay('fdrawer'); });
  bind('mApply','click',function(){ closeOverlay('fdrawer'); });
  bind('openMyPlan','click',function(){ renderMyPlan(); openOverlay('myplanDrawer'); });
  bind('myplanCal','click',downloadMyPlanICS);
  bind('myplanCompare','click',function(){ renderCompareTable(); openOverlay('cmpModal'); });
  bind('openCompare','click',function(){ renderCompareTable(); openOverlay('cmpModal'); });
  bind('clearCompare','click',function(){ compareSel=[]; document.querySelectorAll('[data-cmpchk]').forEach(function(c){ c.checked=false; }); renderMyPlan(); });
  bind('featPrev','click',function(){ featGo(featIdx-1); });
  bind('featNext','click',function(){ featGo(featIdx+1); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ ['mnav','fdrawer','myplanDrawer','cmpModal'].forEach(function(id){ closeOverlay(id); }); } });
}
init();
"""

def extract_style(html):
    m = re.search(r'<style>(.*?)</style>', html, re.S)
    assert m, 'no <style> block in old homepage'
    return m.group(1)


def extract_data_array(html):
    marker = '/*__DATA__*/'
    mpos = html.find(marker)
    assert mpos >= 0, 'DATA marker missing'
    vpos = html.find('var DATA =', mpos)
    assert vpos >= 0, 'var DATA missing'
    start = html.find('[', vpos)
    assert start >= 0, 'DATA array start missing'
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(html)):
        c = html[i]
        if in_str:
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    return html[start:i + 1]
    raise AssertionError('DATA array end not found')


def main():
    old = SRC.read_text(encoding='utf-8')
    style = extract_style(old) + NEW_CSS
    data = extract_data_array(old)
    app = APP_JS.replace('@@GUIDEFILES@@', json.dumps(GUIDES))
    app = app.replace('@@COUNTRIES@@', json.dumps(COUNTRY_CATS))
    app = app.replace('@@ADSENSE_INS@@', json.dumps(ADSENSE_INS))
    out = HTML_TEMPLATE.replace('@@STYLE@@', style)
    out = out.replace('@@DATA@@', data)
    out = out.replace('@@APPJS@@', app)
    assert '@@' not in out, 'unreplaced template token remains'
    assert '/*__DATA__*/' in out and 'var DATA =' in out
    OUT.write_text(out, encoding='utf-8')
    print(f'wrote {OUT} ({OUT.stat().st_size} bytes)')


if __name__ == '__main__':
    main()

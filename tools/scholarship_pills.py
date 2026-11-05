#!/usr/bin/env python3
"""Shared pill logic for the scholarships corpus (tools/rebuild-pills.py,
tools/closed-flip.py).

Single source of truth for how a deadline pill is (re)computed from
site-data.json, so the one-off rebuild and the nightly flip can never drift
apart.

Pill rules (all dates are Asia/Kolkata calendar dates; dl comes ONLY from
site-data.json — never invented):
  * dl in the future  -> "N days to go" (singular "1 day to go").
  * dl is today       -> "Closes today" (the item is open until end of day).
  * dl has passed     -> "Closed <D Mon YYYY>" (e.g. "Closed 20 Oct 2026").
  * A pill that already carries its own date ("Deadline 1 Dec 2026 · 39 days
    left", "31 Oct 2026 · 13 days to go") keeps its wording and only the
    count is updated — BUT only when the embedded date equals the corpus dl.
    If the embedded date disagrees with dl, the pill is counting down to a
    DIFFERENT date (usually a later round) and is left untouched + reported
    as a date conflict. Never silently rewrite a date.
  * Non-countdown pills ("TBA", "Rolling — no fixed deadline",
    "Opens Dec 2026", "Round 1 open now", "Automatic on admission", ...)
    are left untouched: they carry prose the corpus dl cannot recompute,
    and several closed entries legitimately describe a NEXT round there
    (e.g. NIMS "Opens Dec 2026", Kyoto "26 Feb 2027 · 130 days to go").
  * Bare "Closed" (no date) is normalised to "Closed <dl date>" when the
    entry has a dl.
  * Entries with no dl in site-data.json cannot be recomputed: left + listed.
  * Entries listed in closed-flip-exclusions.json are never flipped or
    recomputed (contested corpus dates): left + listed.

Flip extras (applied ONLY when a main pill flips to Closed, following the
manual St John's / Yeungnam pattern in DEADLINE-RECHECK-LOG.md):
  * Deadline fact row: a bare "D Mon YYYY" value becomes "Closed <date>"
    (any <small> note is preserved).
  * Alert card <h3>: a bare "Deadline: D Mon YYYY" becomes
    "Deadline: D Mon YYYY (closed)". This matters because
    extract-site-data.py re-derives site-data.json `closed` from the first
    date in that <h3> — the "(closed)" suffix keeps the parsed date intact
    while the human-readable status flips.
  * site-data.json: the entry's `closed` is set to true (the writer cron's
    extract-site-data.py re-derives the same value from the <h3> date, so
    the two stay consistent).
"""

import json
import re
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('/home/hatch/workspace/scholarships-17k')
ARTICLES = ROOT / 'articles'
SITE_DATA = ROOT / 'site-data.json'
CARDS_REGISTRY = ROOT / 'cards_registry.py'
EXCLUSIONS_FILE = Path(__file__).with_name('closed-flip-exclusions.json')
BASE_URL = 'https://scholarships.studydesk.fun'

MONTHS = {'Jan': 1, 'January': 1, 'Feb': 2, 'February': 2, 'Mar': 3,
          'March': 3, 'Apr': 4, 'April': 4, 'May': 5, 'Jun': 6, 'June': 6,
          'Jul': 7, 'July': 7, 'Aug': 8, 'August': 8, 'Sep': 9,
          'September': 9, 'Oct': 10, 'October': 10, 'Nov': 11,
          'November': 11, 'Dec': 12, 'December': 12}
MONTH_PAT = (r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|'
             r'Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|'
             r'Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)')

MAIN_PILL_RE = re.compile(r'<span class="dline">([^<]*)</span>')
DPILL_RE = re.compile(r'<span class="dpill( check)? ?">([^<]*)</span>')
DATE_RE = re.compile(r'(\d{1,2}) ' + MONTH_PAT + r' (\d{4})')
PLAIN_COUNT_RE = re.compile(r'^(\d+) days? to go$')
# A countdown carrying its own date, with any label before the date and any
# note after the count, e.g. "Deadline 1 Dec 2026 · 39 days left",
# "31 Oct 2026 · 13 days to go", "Spring 2027 deadline 2 Nov 2026 · 10 days
# left", "12 Jan 2027 (Round 2) · 83 days to go",
# "Deadline 15 Mar 2027 · 143 days left (confirm on uhasselt.be)".
DATED_COUNT_RE = re.compile(
    r'^(.*?)(\d{1,2} \w+ \d{4})(.*?) · (\d+) days? (left|to go)(.*)$')
CLOSED_DATED_RE = re.compile(r'^Closed (\d{1,2} \w+ \d{4})$')

PILOT_RE = re.compile(r'^pilot-.*\.html$')


def today_ist(day=None):
    """Today in Asia/Kolkata. `day` (YYYY-MM-DD) is a TEST-ONLY override."""
    if day:
        return date.fromisoformat(day)
    return datetime.now(ZoneInfo('Asia/Kolkata')).date()


def fmt_date(d):
    """date -> '25 Oct 2026' (no zero-padded day)."""
    return f'{d.day} {d.strftime("%b")} {d.year}'


def parse_dmy(s):
    """'16 Oct 2026' -> date, or None when unparseable. Never guesses."""
    m = DATE_RE.search(s or '')
    if not m:
        return None
    try:
        return date(int(m.group(3)), MONTHS[m.group(2)], int(m.group(1)))
    except ValueError:
        return None


def load_site_data():
    return json.loads(SITE_DATA.read_text(encoding='utf-8'))


def load_exclusions(path=None):
    """Return the set of excluded site-data ids (contested dates)."""
    p = Path(path) if path else EXCLUSIONS_FILE
    if not p.exists():
        return set()
    data = json.loads(p.read_text(encoding='utf-8'))
    return set(data.get('excluded_ids', []))


def pill_for(dl, today):
    """The correct pill text for a deadline `dl` (date) as of `today`."""
    n = (dl - today).days
    if n < 0:
        return f'Closed {fmt_date(dl)}'
    if n == 0:
        return 'Closes today'
    if n == 1:
        return '1 day to go'
    return f'{n} days to go'


def recompute_pill(old, dl_str, today):
    """New pill text for an existing pill, or None to leave it untouched.

    `old` is the current pill text, `dl_str` the corpus dl ('YYYY-MM-DD'
    or falsy). Returns None when the pill cannot be computed from dl:
    no dl, a non-countdown pill, or an embedded date that disagrees
    with dl (date conflict — the pill counts down to another date).
    """
    if not dl_str:
        return None
    try:
        dl = date.fromisoformat(dl_str)
    except ValueError:
        return None
    old = (old or '').strip()
    if PLAIN_COUNT_RE.match(old):
        return pill_for(dl, today)
    m = DATED_COUNT_RE.match(old)
    if m:
        # A pill with its own date: recompute ONLY when that date is the
        # corpus dl. A different date means the pill counts down to another
        # date (usually a later round) — leave it (date conflict).
        embedded = parse_dmy(m.group(2))
        if embedded is None or embedded != dl:
            return None  # date conflict: pill counts to a different date
        n = (dl - today).days
        if n < 0:
            return f'Closed {fmt_date(dl)}'
        if n == 0:
            return 'Closes today'
        unit = 'day' if n == 1 else 'days'
        # Preserve the pill's own label (group 1), mid-note (group 3) and
        # trailing note (group 6); only the count changes.
        return (f'{m.group(1)}{fmt_date(dl)}{m.group(3)} · '
                f'{n} {unit} {m.group(5)}{m.group(6)}')
    if old == 'Closed':
        return f'Closed {fmt_date(dl)}' if dl < today else pill_for(dl, today)
    if CLOSED_DATED_RE.match(old):
        return pill_for(dl, today)
    if old == 'Closes today':
        return pill_for(dl, today)
    return None  # non-countdown prose: leave untouched


def is_closed_pill(text):
    """True when a pill already states Closed (bare or dated)."""
    t = (text or '').strip()
    return t == 'Closed' or bool(CLOSED_DATED_RE.match(t))


def flip_extras(html, dl):
    """Fact-row + alert-<h3> updates for a main-pill flip to Closed.

    Only touches a bare dl-date value; anything else (round notes, an
    already-present "(closed)", no fact row) is left exactly as-is.
    Returns (new_html, did_fact, did_h3).
    """
    dstr = fmt_date(dl)
    did_fact = did_h3 = False

    def _fact(m):
        nonlocal did_fact
        if m.group(2) != dstr:
            return m.group(0)
        did_fact = True
        return f'{m.group(1)}Closed {dstr}{m.group(3) or ""}{m.group(4)}'

    html = re.sub(
        r'(<div class="k">Deadline</div><div class="v">)'
        r'(\d{1,2} \w+ \d{4})(<small>.*?</small>)?(</div>)',
        _fact, html, count=1, flags=re.S)

    def _h3(m):
        nonlocal did_h3
        if m.group(2) != dstr:
            return m.group(0)
        did_h3 = True
        return f'{m.group(1)}{dstr} (closed){m.group(3)}'

    html = re.sub(r'(<h3>Deadline:\s*)(\d{1,2} \w+ \d{4})(\s*</h3>)',
                  _h3, html, count=1)
    return html, did_fact, did_h3


def resolve_dpill_target(html, span_end, by_file):
    """The site-data entry a related-card dpill points at, or None.

    Looks for the first href="*.html" after the pill span (the card's
    title link). The href must name a file present in site-data.json.
    """
    m = re.search(r'href="([^"]+\.html)"', html[span_end:span_end + 800])
    if not m:
        return None
    return by_file.get(m.group(1))

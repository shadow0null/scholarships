#!/usr/bin/env python3
"""Nightly close-flip pass for the scholarships corpus.

WHEN TO RUN: once a day, after midnight IST (e.g. 00:30 Asia/Kolkata),
after the writer cron's last batch of the day — or any time a deadline
has just passed. Safe to run daily; it is idempotent and changes nothing
when nothing has newly closed.

WHAT IT DOES: reads site-data.json and, for every entry whose corpus `dl`
has passed (dl < today), sets `closed: true` in site-data.json and flips
the article HTML pill to "Closed <date>" — main `dline` pill, the
Deadline fact row, the alert-card <h3> (St John's / Yeungnam manual
pattern), and the matching cards_registry.py dpill so future batches
build fresh related cards. Related-card dpills in OTHER articles that
point at the newly closed entry are flipped to "Closed <date>" too.
It does NOT recompute "N days to go" countdowns — that is
tools/rebuild-pills.py's job; this script only flips what has closed.

WHAT IT NEVER DOES:
  * Never flips an entry listed in tools/closed-flip-exclusions.json
    (contested corpus dates — ESA internship, Vidyadhan Mathura). Those
    stay open until the NEEDS-CHECK is resolved by a human.
  * Never touches a pill whose embedded date disagrees with the corpus dl
    (date conflict — the pill counts down to a different, usually later,
    round) or any non-countdown pill (TBA, Rolling, "Opens Dec 2026",
    next-round prose). Such entries are listed in the output.
  * Never invents a date, amount, or deadline: everything comes from
    site-data.json `dl`.

WHAT IT PRINTS: counts (entries scanned, flips made, exclusions skipped,
conflicts left), the id of every flipped entry with its old/new pill, and
the backup directory. Exit code 0 always, unless site-data.json or an
article file cannot be read/written (then it stops and prints the error).

BACKUPS: when anything changes, originals are copied first to
  backups/closed-flip-YYYY-MM-DD-HHMMSS/
(the writer cron rebuilds the deploy zip from articles/, so the flipped
pills ship with the next rebuild — this script deliberately does NOT
touch the deploy zip).

SETUP (for the writer cron): run from the corpus root —
  python3 tools/closed-flip.py
Add --dry-run to preview without changing anything. --date YYYY-MM-DD
is TEST ONLY (pretend today is that date, for verifying flip logic on
copies — never use it in production).
"""
import argparse
import importlib.util
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scholarship_pills as P  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--date', help='TEST ONLY: pretend today is YYYY-MM-DD')
    ap.add_argument('--dry-run', action='store_true',
                    help='print the plan, change nothing')
    ap.add_argument('--root', default=str(P.ROOT),
                    help='corpus root (default: the real corpus)')
    args = ap.parse_args()

    root = Path(args.root)
    art_dir = root / 'articles'
    site_data_path = root / 'site-data.json'
    registry_path = root / 'cards_registry.py'
    today = P.today_ist(args.date)
    print(f'closed-flip: today={today.isoformat()} root={root}'
          + (' DRY-RUN' if args.dry_run else ''))

    entries = json.loads(site_data_path.read_text(encoding='utf-8'))
    by_file = {e['file']: e for e in entries}
    by_id = {e['id']: e for e in entries}
    excluded = P.load_exclusions()
    print(f'site-data entries: {len(entries)}; exclusions: {sorted(excluded)}')

    # Candidates: dl passed. Exclusions and conflicts are filtered per pill.
    candidates = [e for e in entries
                  if e.get('dl') and P.date.fromisoformat(e['dl']) < today]
    print(f'entries with dl < today: {len(candidates)}')

    changed_files = {}   # rel path -> original bytes
    flips = []           # (id, old pill, new pill)
    skipped_excluded, skipped_conflict, skipped_noncountdown = [], [], []
    site_data_set = 0

    for entry in candidates:
        if entry['id'] in excluded:
            skipped_excluded.append(entry['id'])
            continue
        fname = art_dir / entry['file']
        if fname.name == 'index.html' or P.PILOT_RE.match(fname.name):
            continue
        if not fname.exists():
            print(f'  WARN: missing article file {fname.name} — skipped')
            continue
        html = fname.read_text(encoding='utf-8')
        new_html = html
        m = P.MAIN_PILL_RE.search(new_html)
        if not m:
            continue
        old = m.group(1)
        dl = P.date.fromisoformat(entry['dl'])
        new = P.recompute_pill(old, entry['dl'], today)
        if new is None:
            if P.DATE_RE.search(old) and ('days to go' in old
                                          or 'days left' in old):
                skipped_conflict.append((entry['id'], old, entry['dl']))
            else:
                skipped_noncountdown.append((entry['id'], old))
            continue
        if not new.startswith('Closed'):
            # dl passed but pill recomputes to a non-Closed text (can only
            # happen for a "Closes today"-style edge) — nothing to flip.
            continue
        if P.is_closed_pill(old) and new == f'Closed {P.fmt_date(dl)}':
            # Already flipped in a previous run; only ensure site-data flag.
            if not entry.get('closed'):
                entry['closed'] = True
                site_data_set += 1
            continue
        new_html = P.MAIN_PILL_RE.sub(
            f'<span class="dline">{new}</span>', new_html, count=1)
        new_html, _, _ = P.flip_extras(new_html, dl)
        changed_files[str(fname.relative_to(root))] = fname.read_bytes()
        if not args.dry_run:
            fname.write_text(new_html, encoding='utf-8')
        flips.append((entry['id'], old, new))
        if not entry.get('closed'):
            entry['closed'] = True
            site_data_set += 1

    # Related-card dpills in every article pointing at a flipped entry,
    # plus the registry — only for entries flipped by THIS run.
    flipped_ids = {f[0] for f in flips}
    dpill_flips = 0
    if flipped_ids:
        for fname in sorted(art_dir.glob('*.html')):
            if fname.name == 'index.html' or P.PILOT_RE.match(fname.name):
                continue
            entry = by_file.get(fname.name)
            if entry is None or entry['id'] in excluded:
                continue
            html = fname.read_text(encoding='utf-8')
            orig = html
            out, last = [], 0
            file_changed = False
            for m in P.DPILL_RE.finditer(orig):
                out.append(orig[last:m.start()])
                tgt = P.resolve_dpill_target(orig, m.end(), by_file)
                if tgt is None or tgt['id'] not in flipped_ids:
                    out.append(m.group(0))
                else:
                    new = P.recompute_pill(m.group(2), tgt.get('dl'), today)
                    if new is None or not new.startswith('Closed'):
                        out.append(m.group(0))
                    elif new == m.group(2) and m.group(1) == ' check':
                        out.append(m.group(0))
                    else:
                        dpill_flips += 1
                        file_changed = True
                        out.append(
                            f'<span class="dpill check">{new}</span>')
                last = m.end()
            out.append(orig[last:])
            new_html = ''.join(out)
            if file_changed and new_html != html:
                rel = str(fname.relative_to(root))
                changed_files.setdefault(rel, fname.read_bytes())
                if not args.dry_run:
                    fname.write_text(new_html, encoding='utf-8')

        # cards_registry.py dpills for flipped targets
        if not args.dry_run:
            reg_orig = registry_path.read_bytes()
            spec = importlib.util.spec_from_file_location(
                'cards_registry_live', str(registry_path))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            lines = registry_path.read_text(
                encoding='utf-8').splitlines(keepends=True)
            reg_changed = 0
            for i, line in enumerate(lines):
                m = re.search(r"'dpill': '([^']*)'", line)
                hm = re.search(r"'href': '([^']+\.html)'", line)
                if not m or not hm:
                    continue
                tgt = by_file.get(hm.group(1))
                if tgt is None or tgt['id'] not in flipped_ids:
                    continue
                new = P.recompute_pill(m.group(1), tgt.get('dl'), today)
                if new is None or new == m.group(1):
                    continue
                lines[i] = line[:m.start(1)] + new + line[m.end(1):]
                reg_changed += 1
            if reg_changed:
                changed_files.setdefault('cards_registry.py', reg_orig)
                registry_path.write_text(''.join(lines), encoding='utf-8')
                print(f'  registry dpills flipped: {reg_changed}')

    # site-data.json (only when a closed flag actually changed)
    if site_data_set and not args.dry_run:
        changed_files.setdefault('site-data.json',
                                 site_data_path.read_bytes())
        site_data_path.write_text(
            json.dumps(entries, indent=1, ensure_ascii=False),
            encoding='utf-8')

    if changed_files and not args.dry_run:
        stamp = datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d-%H%M%S')
        bdir = root / 'backups' / f'closed-flip-{stamp}'
        bdir.mkdir(parents=True, exist_ok=True)
        for rel, blob in changed_files.items():
            dest = bdir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(blob)
        print(f'backups: {bdir} ({len(changed_files)} files)')

    print('--- summary ---')
    print(f'  scanned: {len(entries)} entries, '
          f'{len(candidates)} with dl < today')
    print(f'  flips made: {len(flips)} (main pills)')
    for fid, old, new in flips:
        print(f'    {fid}: {old!r} -> {new!r}')
    print(f'  dpill flips (related cards): {dpill_flips}')
    print(f'  site-data closed flags set: {site_data_set}')
    print(f'  excluded (contested, untouched): {len(skipped_excluded)} '
          f'{sorted(skipped_excluded)}')
    print(f'  date conflicts left: {len(skipped_conflict)}')
    for row in skipped_conflict:
        print(f'    {row[0]}: pill={row[1]!r} dl={row[2]}')
    print(f'  non-countdown pills left: {len(skipped_noncountdown)}')
    for row in skipped_noncountdown:
        print(f'    {row[0]}: pill={row[1]!r}')
    if not flips and not site_data_set:
        print('  nothing to flip — corpus already reflects today.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Rebuild every deadline pill in the scholarships corpus from site-data.json.

Recomputes the "N days to go" pill in each article HTML file (the main
`dline` pill AND the related-card `dpill` pills, which point at other
articles) relative to TODAY (Asia/Kolkata), and flips any article whose
corpus deadline has passed to a "Closed <date>" pill.

Rules (see tools/scholarship_pills.py for the full contract):
  * Only the corpus `dl` in site-data.json is used — never an invented date.
  * Entries in tools/closed-flip-exclusions.json are left untouched
    (contested dates: ESA internship, Vidyadhan Mathura).
  * "Closes today" when dl is today — the item is open until end of day.
  * Non-countdown pills (TBA, Rolling, "Opens Dec 2026", next-round prose)
    and pills whose embedded date disagrees with dl are left untouched and
    listed in the summary. Entries with no dl are left and listed.
  * A flip also updates the Deadline fact row and alert <h3> (St John's /
    Yeungnam manual pattern), sets `closed: true` in site-data.json, and
    updates the matching cards_registry.py dpill so the NEXT batch's new
    articles carry the fresh pill too.

Idempotent: re-running on the same day changes nothing.
Backups: every file changed is copied first to
  backups/pill-rebuild-YYYY-MM-DD-HHMMSS/ (relative paths preserved),
  plus site-data.json / cards_registry.py when they change.

Usage:
  python3 tools/rebuild-pills.py [--date YYYY-MM-DD] [--dry-run] [--root DIR]
    --date    TEST ONLY: pretend today is this date (verifies flip logic
              on copies without touching real data).
    --dry-run print the plan, change nothing.
    --root    corpus root (default: the real corpus). Test on copies first:
                cp -r ~/workspace/scholarships-17k /tmp/sch-test
                python3 /tmp/sch-test/tools/rebuild-pills.py --root /tmp/sch-test
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


def _update_registry(registry_path, by_file, excluded, today):
    """Recompute dpill values in cards_registry.py from site-data dl.

    Line-based edit (one entry per line) so no other formatting changes.
    Returns (changed_count, original_bytes). Does NOT write when nothing
    changed; the caller writes + backs up.
    """
    original = registry_path.read_bytes()
    spec = importlib.util.spec_from_file_location(
        'cards_registry_live', str(registry_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    lines = registry_path.read_text(encoding='utf-8').splitlines(keepends=True)
    changed = 0
    for i, line in enumerate(lines):
        m = re.search(r"'dpill': '([^']*)'", line)
        if not m:
            continue
        hm = re.search(r"'href': '([^']+\.html)'", line)
        if not hm:
            continue
        entry = by_file.get(hm.group(1))
        if entry is None or entry['id'] in excluded:
            continue
        new = P.recompute_pill(m.group(1), entry.get('dl'), today)
        if new is None or new == m.group(1):
            continue
        lines[i] = line[:m.start(1)] + new + line[m.end(1):]
        changed += 1
    if changed:
        registry_path.write_text(''.join(lines), encoding='utf-8')
    return changed, original


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--date', help='TEST ONLY: pretend today is YYYY-MM-DD')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--root', default=str(P.ROOT),
                    help='corpus root (default: the real corpus)')
    args = ap.parse_args()

    root = Path(args.root)
    art_dir = root / 'articles'
    site_data_path = root / 'site-data.json'
    registry_path = root / 'cards_registry.py'
    today = P.today_ist(args.date)
    print(f'rebuild-pills: today={today.isoformat()} root={root}'
          + (' DRY-RUN' if args.dry_run else ''))

    entries = json.loads(site_data_path.read_text(encoding='utf-8'))
    by_file = {e['file']: e for e in entries}
    excluded = P.load_exclusions()
    print(f'site-data entries: {len(entries)}; exclusions: {sorted(excluded)}')

    stats = {'files_changed': 0, 'main_changed': 0, 'main_flips': 0,
             'main_closes_today': 0, 'main_normalised_closed': 0,
             'dpill_changed': 0, 'dpill_flips': 0, 'dpill_closes_today': 0,
             'excluded_main': 0, 'excluded_dpill': 0, 'no_dl': 0,
             'non_countdown': 0, 'conflicts': [], 'unresolvable_dpill': 0,
             'registry_changed': 0, 'site_data_closed_set': 0}
    changed_files = {}   # rel path -> original bytes
    flips_site_data = set()

    def note_conflict(kind, where, target_id, old, dl):
        stats['conflicts'].append(
            {'kind': kind, 'where': where, 'target': target_id,
             'pill': old, 'dl': dl})

    for fname in sorted(art_dir.glob('*.html')):
        if fname.name == 'index.html' or P.PILOT_RE.match(fname.name):
            continue
        entry = by_file.get(fname.name)
        if entry is None:
            print(f'  WARN: {fname.name} has no site-data entry — skipped')
            continue
        html = fname.read_text(encoding='utf-8')
        new_html = html
        file_changed = False

        # ---- main dline pill ----
        m = P.MAIN_PILL_RE.search(new_html)
        if m:
            old = m.group(1)
            if entry['id'] in excluded:
                stats['excluded_main'] += 1
            else:
                new = P.recompute_pill(old, entry.get('dl'), today)
                if new is None:
                    if not entry.get('dl'):
                        stats['no_dl'] += 1
                    elif P.DATE_RE.search(old) and ('days to go' in old
                                                    or 'days left' in old):
                        note_conflict('main-date-conflict', fname.name,
                                      entry['id'], old, entry.get('dl'))
                    else:
                        stats['non_countdown'] += 1
                elif new != old:
                    new_html = P.MAIN_PILL_RE.sub(
                        f'<span class="dline">{new}</span>',
                        new_html, count=1)
                    stats['main_changed'] += 1
                    file_changed = True
                    if new.startswith('Closed') and not P.is_closed_pill(old):
                        stats['main_flips'] += 1
                        new_html, _, _ = P.flip_extras(
                            new_html, P.date.fromisoformat(entry['dl']))
                        if not entry.get('closed'):
                            flips_site_data.add(entry['id'])
                    elif new == 'Closes today':
                        stats['main_closes_today'] += 1
                    elif P.is_closed_pill(old):
                        stats['main_normalised_closed'] += 1

        # ---- related-card dpills (targets resolved against pre-edit text) ----
        orig_html = new_html
        out, last = [], 0
        for m in P.DPILL_RE.finditer(orig_html):
            out.append(orig_html[last:m.start()])
            old_cls, old = m.group(1), m.group(2)
            tgt = P.resolve_dpill_target(orig_html, m.end(), by_file)
            if tgt is None:
                stats['unresolvable_dpill'] += 1
                out.append(m.group(0))
            elif tgt['id'] in excluded:
                stats['excluded_dpill'] += 1
                out.append(m.group(0))
            else:
                new = P.recompute_pill(old, tgt.get('dl'), today)
                if new is None:
                    if not tgt.get('dl'):
                        stats['no_dl'] += 1
                    elif P.DATE_RE.search(old) and ('days to go' in old
                                                    or 'days left' in old):
                        note_conflict('dpill-date-conflict', fname.name,
                                      tgt['id'], old, tgt.get('dl'))
                    else:
                        stats['non_countdown'] += 1
                    out.append(m.group(0))
                else:
                    new_cls = ' check' if new.startswith('Closed') else ' '
                    old_cls_norm = ' check' if old_cls == ' check' else ' '
                    if new == old and new_cls == old_cls_norm:
                        out.append(m.group(0))
                    else:
                        stats['dpill_changed'] += 1
                        file_changed = True
                        if new.startswith('Closed') and not P.is_closed_pill(old):
                            stats['dpill_flips'] += 1
                        elif new == 'Closes today':
                            stats['dpill_closes_today'] += 1
                        out.append(f'<span class="dpill{new_cls}">{new}</span>')
            last = m.end()
        out.append(orig_html[last:])
        new_html = ''.join(out)

        if file_changed and new_html != html:
            changed_files[str(fname.relative_to(root))] = fname.read_bytes()
            stats['files_changed'] += 1
            if not args.dry_run:
                fname.write_text(new_html, encoding='utf-8')

    # ---- cards_registry.py dpills (next batch builds fresh cards) ----
    if not args.dry_run:
        reg_changed, reg_orig = _update_registry(
            registry_path, by_file, excluded, today)
        stats['registry_changed'] = reg_changed
        if reg_changed:
            changed_files['cards_registry.py'] = reg_orig
    else:
        # dry run: compute without writing — reuse the function on a copy
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp_reg = Path(td) / 'cards_registry.py'
            tmp_reg.write_bytes(registry_path.read_bytes())
            reg_changed, _ = _update_registry(
                tmp_reg, by_file, excluded, today)
            stats['registry_changed'] = reg_changed

    # ---- site-data.json closed flags for flips ----
    if flips_site_data:
        stats['site_data_closed_set'] = len(
            [e for e in entries if e['id'] in flips_site_data
             and not e.get('closed')])
        if not args.dry_run:
            changed_files['site-data.json'] = site_data_path.read_bytes()
            for e in entries:
                if e['id'] in flips_site_data:
                    e['closed'] = True
            site_data_path.write_text(
                json.dumps(entries, indent=1, ensure_ascii=False),
                encoding='utf-8')

    # ---- backups (only when something actually changes) ----
    if changed_files and not args.dry_run:
        stamp = datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%Y-%m-%d-%H%M%S')
        bdir = root / 'backups' / f'pill-rebuild-{stamp}'
        bdir.mkdir(parents=True, exist_ok=True)
        for rel, blob in changed_files.items():
            dest = bdir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(blob)
        print(f'backups: {bdir} ({len(changed_files)} files)')

    print('--- summary ---')
    for k in ('files_changed', 'main_changed', 'main_flips',
              'main_closes_today', 'main_normalised_closed', 'dpill_changed',
              'dpill_flips', 'dpill_closes_today', 'excluded_main',
              'excluded_dpill', 'no_dl', 'non_countdown',
              'unresolvable_dpill', 'registry_changed',
              'site_data_closed_set'):
        print(f'  {k}: {stats[k]}')
    print(f'  date_conflicts_left: {len(stats["conflicts"])}')
    for c in stats['conflicts']:
        print(f'    {c["kind"]} {c["where"]} target={c["target"]} '
              f'pill={c["pill"]!r} dl={c["dl"]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

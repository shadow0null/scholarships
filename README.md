# Scholarships — scholarships.studydesk.fun

Source for the Scholarships site: Indian and international scholarships,
fellowships, and internships, with a matcher, a deadline board, and guides.

Live site: https://scholarships.studydesk.fun

## What the site is

- **416 listings** in `site-data.json`, each with an article page under
  `articles/` — Indian government schemes (NSP, state scholarships),
  corporate/foundation awards, and international scholarships,
  fellowships, and internships.
- **Statuses are computed in the browser** from each listing's deadline
  against today (Asia/Kolkata). Stored `days`/`closed` values are never
  displayed, so a listing never shows a stale "Open" or a negative
  countdown.
- **Homepage:** scholarship matcher, Closing-in-7-days row, My plan
  (saved items, kept in the browser), Browse tabs (India / Abroad /
  Internships), deadline board, and Guides.
- **Each detail page** has one action box: status + exact date,
  eligibility, documents, and the apply link. Aggregator links
  (Buddy4Study, Bright Scholarship, Opportunity Desk) are labelled
  "Mentioned by", never "Official source".
- **Support:** WhatsApp +919905166009 and scholarships@studydesk.fun
  (footer only). No accounts; saved items stay in the browser.

## Layout

- `articles/` — 419 HTML pages (listings + homepage + guide pages)
- `articles/logos/` — 368 provider logo PNGs
- `site-data.json` — the 416 listing records the site is built from
- `homepage_data.json` — homepage data
- `privacy.html` — privacy page (`/privacy.html`)
- `inventory/` — topic queue and progress JSON (`queue.json`,
  `queue-prioritized.json`, `queue-progress.json`, `queue-expired.json`)
  plus reference lists
- Build tooling — 98 `build-*.py` scripts (per-batch writers plus
  `build-site.py`, `build-homepage-v9.py`, `build-detail-v9.py`,
  `build-sitemap-v9.py`), `add-logos.py`, `extract-site-data.py`,
  `postprocess-articles.py`, `verify-rebuild-v9.py`,
  `cards_registry.py`, `tools/`, `template/article-shell.html`
- `progress/` — build progress notes
- `DEPLOY-README-v9.md` — deploy instructions and the two standing gates
- `DEADLINE-RECHECK-LOG.md` — deadline re-check log

## Deploying

Read `DEPLOY-README-v9.md` before any upload. Two gates stand before
every deploy:

1. **Disk audit** — the server root was 96% full on 31 Oct 2026.
   Confirm at least 2 GB free on `/` before unzipping anything.
2. **Panel publish reconciliation** — if anything was published through
   the live admin panel, its edits live only on the server in
   `admin/changes.json`. Reconcile that file into the corpus first, or
   the upload overwrites those edits.

The deploy is one zip, uploaded over SSH from Kali and unpacked into a
release directory under the vhost (never `/tmp`, never a backup dir).
The sitemap has 418 URLs (homepage + 416 articles + privacy).

## Not in this repo

- `backups/` — local pre-edit backups (excluded via `.gitignore`)
- Deploy zips (`scholarships-articles-deploy-*.zip`, `scholarships-all-in-one-deploy-*.zip`)
  — built on demand, excluded via `.gitignore`
- Secrets (`.env`, `.pem`, `.key`, credentials) — excluded via
  `.gitignore`; none are in the tree

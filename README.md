# Scholarships — scholarships.studydesk.fun

Source for the Scholarships site: 400+ scholarship article pages, the
article/data build scripts, and project docs.

## Layout

- `articles/` — generated article pages (`*.html`) and provider logos
- `inventory/` — topic queue and progress JSON (`queue.json` etc.)
- `site-data.json` — article DATA records used by the site
- `build-*.py`, `add-logos.py`, `extract-site-data.py`, `build-site.py`,
  `postprocess-articles.py`, `verify-rebuild-v9.py` — build tooling
- `template/`, `tools/` — page templates and helper scripts
- `progress/` — build progress notes
- `DEPLOY-README-v9.md` — deploy instructions
- `DEADLINE-RECHECK-LOG.md` — deadline re-check log

## Not in this repo

- `backups/` — local pre-edit backups (excluded via `.gitignore`)
- Deploy zips (`scholarships-articles-deploy-*.zip`) — built on demand by
  `rebuild-deploy-zip.py`, excluded via `.gitignore`

Live site: https://scholarships.studydesk.fun

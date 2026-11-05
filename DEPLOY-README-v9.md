# DEPLOY — StudyDesk Scholarships rebuild (2 Nov 2026)

One zip, one upload. This package replaces the live site portion
(previously the 31-Oct build, 405 records, frozen statuses) with the
rebuilt site (416 records, browser-computed statuses), plus the admin
panel v2 with the publish-flow pack and the updated new-article template.

**Upload this ONLY after the two gates at the bottom of this file.**
Do not unzip in /tmp (it was 98% full on 31 Oct — unzip in a release
directory under the vhost, never in a /home/ubuntu backup dir).

---

## 1. SEARCH CONSOLE — DO THIS FIRST, BEFORE ANYTHING ELSE GOES WRONG

The sitemap in this package is a NEW file (418 URLs: homepage + 416
articles + privacy page). Google's old rows must be cleaned up, or the
property keeps showing the stale "Couldn't fetch" state.

1. **Property:** use the Domain property `studydesk.fun` OR the
   URL-prefix property `https://scholarships.studydesk.fun/` —
   whichever already exists for this subdomain. Do NOT create a new
   property for a single article URL.
2. **Submit ONLY this sitemap:**
   `https://scholarships.studydesk.fun/sitemap.xml`
3. **Remove every submitted sitemap that 404s** — especially any
   trailing-slash URL such as
   `https://scholarships.studydesk.fun/sitemap.xml/` (that URL must
   301 to `/sitemap.xml`, never 404; see the nginx snippet below).
4. **Never submit the apex index** (`https://studydesk.fun/sitemap.xml`)
   as this site's sitemap. This repo does NOT own the studydesk.fun
   apex — do not touch the apex index file.
5. **After deploy, verify in a browser:**
   - Open `https://scholarships.studydesk.fun/sitemap.xml` — the page
     must start with `<?xml` and the response header must be
     `application/xml`.
   - URL-inspect the homepage and one scholarship URL as Googlebot
     (Search Console → URL Inspection → Test live URL).
   - The sitemap row should show Last read = today and Discovered
     = 418. If it still says "Couldn't fetch" while the browser shows
     valid XML, check the server nginx access log for Googlebot
     sitemap hits (see step 5) — do NOT resubmit a third time.

## 2. UPLOAD STEPS (run over SSH from Kali, as usual)

GATE 1 — disk audit first (see §5). Then:

```sh
cd /var/www/scholarships.studydesk.fun
# 1. Back up the live site (dated sibling dir, kept — never delete
#    old backups). Do this BEFORE creating the release directory.
sudo cp -a . /var/www/scholarships-backup-2026-11-02
# 2. Upload the zip to a release directory and unzip THERE
#    (upload scholarships-all-in-one-deploy-2026-11-02-rebuild.zip first)
mkdir -p releases/2026-11-02-rebuild
unzip -o scholarships-all-in-one-deploy-2026-11-02-rebuild.zip -d releases/2026-11-02-rebuild
# 3. Sync the site files into the vhost root (admin/ goes to the root too)
sudo rsync -a releases/2026-11-02-rebuild/ ./
# 4. Permissions
sudo chown -R www-data:www-data .
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
# 5. Smoke test
curl -s -o /dev/null -w '%{http_code}\n' https://scholarships.studydesk.fun/
curl -s https://scholarships.studydesk.fun/sitemap.xml | head -3
```

Expected after deploy: homepage shows 416 records and a working grid
(cards appear WITHOUT touching a filter — the old blank-grid bug is
fixed); one article URL opens and its logo loads; the sitemap shows
418 locs.

## 3. NGINX SNIPPETS (add to the scholarships vhost, then `nginx -t` + reload)

```nginx
# Serve sitemaps as XML with UTF-8 (never the 404 HTML fall-through)
location = /sitemap.xml {
    default_type application/xml;
    charset utf-8;
    try_files $uri =404;
}
# Trailing-slash sitemap URL must redirect, never 404
location = /sitemap.xml/ {
    return 301 /sitemap.xml;
}
# Admin area: never indexed, never public
location /admin/ {
    # (keep your existing auth/deny rules here; see SETUP.md)
}
```

`robots.txt` in this package already contains:
```
User-agent: *
Allow: /
Sitemap: https://scholarships.studydesk.fun/sitemap.xml
```

## 4. ADMIN PANEL SETUP (first time only; skip if the panel is already live)

1. Extract (already in this zip) → run `php-check.php` once, then
   DELETE it.
2. Set the password on the server terminal:
   `php admin/setup/set-password.php` (hidden prompt, self-deletes).
3. Smoke test: log in, open one article in Edit, verify the SEO
   link set (canonical, JSON-LD url, sitemap loc) matches, then undo.
4. Full setup details: `SETUP.md`. Publish-flow details: `APPLY.md`.
5. Rollback for the panel alone: remove the `admin/` directory.

## 5. THE TWO STANDING GATES — READ BEFORE UPLOADING

**Gate 1 — server disk.** The server root was 96% full (637 MB free)
and /tmp 98% full on 31 Oct. Before unzipping, run:
`df -h / /tmp` and confirm at least 2 GB free on `/`. If it is still
near-full, clean ONLY paths you have approved — never delete a dated
backup on a name alone.

**Gate 2 — panel publish reconciliation.** If anything was published
through the live admin panel ("publish worked properly" on 2 Nov),
its edits live ONLY on the server in `admin/changes.json`. Reconcile
that file into the corpus BEFORE this upload, or this zip will
overwrite those panel edits. If the 2 Nov publish was only the
preview page (not a live panel publish), this gate is clear.

## 6. ROLLBACK

If the new site misbehaves after deploy, restore from the backup made
in step 2.1 (no nginx change needed — the vhost root stays the same):

```sh
cd /var/www/scholarships.studydesk.fun
sudo rsync -a /var/www/scholarships-backup-2026-11-02/ ./
sudo chown -R www-data:www-data .
```

Do NOT roll back by re-uploading the old 31-Oct zip (it reintroduces
frozen statuses and the blank-grid bug), and never repoint the vhost
at a backup directory.

## 7. WHAT CHANGED IN THIS REBUILD (summary)

- Statuses are computed in the browser from each listing's deadline
  against today in Asia/Kolkata — stored `days`/`closed` are never
  displayed. No negative countdowns, no "Closing in -N days".
- Homepage rebuilt: scholarship matcher hero, Closing-in-7-days row
  (open Indian government/corporate/foundation only), My plan
  (renamed from Shortlist, same saved items), Browse tabs
  India / Abroad / Internships, deadline board, Guides, and the
  how-a-listing-gets-on-this-page box. WhatsApp fixed bubble removed
  (number + scholarships@studydesk.fun in the footer only).
- Every detail page has one action box at the top (status + exact
  date, eligibility bullets, documents, official-or-mentioned-by
  apply link, checked date). Aggregator links (Buddy4Study, Bright
  Scholarship, Opportunity Desk) are labelled "Mentioned by", never
  "Official source". Bihar removed everywhere (0 tagged listings).
- New privacy page at `/privacy.html` (no account, saved items stay
  in the browser, ads may be served by Google AdSense, applications
  are never submitted here, not a government site).
- Sitemap regenerated: 418 locs (homepage + 416 articles + privacy),
  lastmod from each listing's verified date, never future.
- Admin panel template updated to the new detail structure, so new
  panel articles match the rebuilt site (action box, status script,
  footer privacy link, no WhatsApp float).

## 8. NOT VERIFIED HERE (post-deploy checks, not done in the build)

- PHP execution of panel flows (no PHP runtime in the build sandbox).
- Live `curl -I` headers (200 + application/xml) for the sitemap.
- Live trailing-slash behaviour (`/sitemap.xml/` → 301, not 404).
- Live Search Console rows (see §1).

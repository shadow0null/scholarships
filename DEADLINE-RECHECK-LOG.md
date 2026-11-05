# Scholarship deadline recheck log

## 2026-10-24 — 23 Oct 2026 deadline follow-up (one-off, IPPA/SML pattern)

Two articles carried a 23 Oct 2026 deadline and were still marked OPEN as of 2026-10-22. Read-only checks performed today; corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself).

### 1. St. John's University Pharmaceutical Industry Fellowship 2027 (USA) — CLOSED
- Official source: https://www.stjohns.edu/academics/schools/college-pharmacy-and-health-sciences/pharmaceutical-industry-fellowship-programs (checked live via browser, 2026-10-24)
- Page lists the original 2027 timeline with no extension: Curriculum Vitae — October 23, 2026; Letter of Intent — October 23, 2026; Official College Transcript — October 27, 2026; Three Letters of Recommendation — October 27, 2026. Materials go to stjfellowships@stjohns.edu. Interviews on rolling basis from October; AIFA-aligned first offer date Dec 11, 2026.
- Verdict: CV + LOI deadline passed 23 Oct 2026 → CLOSED.
- Article flipped in place (st-johns-university-pharma-fellowship-2027-usa.html): dline pill → "Closed", fact band → "Closed 23 Oct 2026", steps item → "Application window closed 23 Oct 2026", alert card → "Deadline: 23 Oct 2026 (closed)", meta description notes closure, verify note = "Verified 24 Oct 2026 … (corrected 24 Oct 2026 — CV/LOI applications closed per the official page)".
- Homepage dataset (articles/index.html): dlRaw → "23 Oct 2026 (closed)", verified → "24 Oct 2026" (closed already true, days −1).
- cards_registry.py: stjohns-pharma dpill → "Closed 23 Oct 2026".

### 2. Yeungnam University PSPS Scholarship 2027, South Korea — EXTENDED to 30 Oct 2026
- Official source checked: English PSPS schedule page (yu.ac.kr/psps/admissions/schedule.do) still shows only the 2026 intake → ambiguous for 2027. Corroborating listings: GradualIn, FellowshipsGuide, Bright Scholarship, schoolmata, scholarshipunion all said 23 Oct 2026 (2 PM KST), no extension; opportunityportal.info claimed 27 Nov 2026 (conflict).
- Resolved against the official Korean PSPS admissions guidelines page (pspsk.yu.ac.kr/pspsk/admission/recruitment-guidelines.do), read directly 2026-10-24. 전형일정 (admission schedule): 원서접수 (application, post + email) 2026년 9월 28일(월) ~ 10월 30일(금) 14:00; 서류전형 합격자 발표 2026년 11월 27일(금) 15:00 (this is the document-screening results date — the source of the 27 Nov confusion); 면접고사 2026년 12월 12일(토); 합격자 발표 2026년 12월 30일(수).
- Verdict: application deadline EXTENDED → now 30 Oct 2026, 2 PM KST. Applications still OPEN.
- Article updated in place (yeungnam-psps-scholarship-2027-korea.html): deadline 23 → 30 Oct 2026 (meta description, dline pill → "6 days to go", fact band "30 Oct 2026 · 2 PM KST; extended", fee step, deadlines FAQ, alert card + WhatsApp reminder text), verify note = "Checked 24 Oct 2026 … (updated 24 Oct 2026; the official English schedule page still shows the 2026 intake only)".
- Homepage dataset (articles/index.html): dlRaw → "30 Oct 2026", dl → "2026-10-30", days −1 → 6, closed true → false, verified → "24 Oct 2026".
- cards_registry.py: yeungnam dpill → "6 days to go".

Note: the official English PSPS schedule page is stale (2026 intake only). The 2027 intake schedule lives on the Korean recruitment-guidelines page for now.

## 2026-10-24 (later the same morning) — CORRECTION to the Yeungnam verdict above

The delayed live-browser check of the official English PSPS schedule page arrived after the first pass: https://www.yu.ac.kr/psps/admissions/schedule.do (checked live 24 Oct 2026) shows the Spring 2027 schedule table as: "Online Application & Payment of Application Fee: 2 PM, September 28(Mon) - 2 PM, October 23(Fri), 2026. The online application system will automatically close after the deadline." Document submission (for completed applications) runs to 2 PM, October 30(Fri), 2026. No extension anywhere on the page. An independent direct re-fetch of the same URL minutes later confirmed the identical wording (the first text-fetch earlier that morning had returned a stale cached 2026-intake version).

The earlier "extended to 30 Oct" conclusion was wrong: it was read off the Korean-language recruitment-guidelines page (pspsk.yu.ac.kr), which does not govern the international online-application window. The document-submission window to 30 Oct is open only to applicants who completed the online application by 23 Oct.

CORRECTED verdict: Yeungnam PSPS Scholarship 2027 — CLOSED (online applications; 23 Oct 2026, 2 PM KST, no extension). The article was re-flipped in place per the SML pattern: dline pill → "Closed", fact band → "Closed 23 Oct 2026", fee step reverted to 23 Oct, deadlines FAQ updated, alert card → "Deadline: 23 Oct 2026 (closed)", verify note = "Verified 24 Oct 2026 … (corrected 24 Oct 2026 — applications closed per the official page; document submission for completed applications runs to 30 Oct 2026)". Homepage dataset: dlRaw → "23 Oct 2026 (closed)", dl 2026-10-23, days −1, closed true, verified 24 Oct 2026. cards_registry.py yeungnam dpill → "Closed 23 Oct 2026".

Final outcome of this run: BOTH articles CLOSED, no extensions.

## 2026-10-26 — IPPA/SML-pattern closure recheck (scholarship-closure-recheck-oct26)

Two articles carried a 25 Oct 2026 deadline and were still marked OPEN as of 2026-10-22. Read-only checks performed today; corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself).

### 1. Vidyadhan Mathura Scholarship for Women in STEM 2026 — EXTENDED to 31 Oct 2026 (still OPEN)
- Official source: https://www.vidyadhan.org/apply — "Scholarship Programs" section, expanded tab "Vidyadhan Mathura Scholarship for Women in STEM – UP", under "Important Dates" (checked live via browser, 2026-10-26). Programme listed under "currently open scholarship programs" while all other 2026 state programmes on the page are marked "Program Closed". Homepage also carries the notice that applications are opened for the degree programme for women in STEM, preferably from Mathura District, UP.
- Exact wording on the official page: "31st October 2026: Application last date" — extended from 25 Oct 2026. Interviews 15–30 Nov 2026.
- Article updated in place (vidyadhan-mathura-women-stem-scholarship-2026.html): meta description, JSON-LD applicationDeadline → 2026-10-31, fact band → "31 Oct 2026", steps item → "Submit before 31 October 2026", alert card → "Deadline: 31 Oct 2026", WhatsApp reminder text → 31 Oct 2026, verify note = "Verified 26 Oct 2026 on the official Vidyadhan apply page (vidyadhan.org/apply): deadline extended to 31 Oct 2026; interviews 15–30 Nov 2026. Earlier listings showed 25 Oct 2026 — superseded by the official extension."
- Homepage dataset: homepage_data.json dl_raw → "31 Oct 2026", dl → "2026-10-31", days 9 → 5. site-data.json: dlRaw → "31 Oct 2026", dl → "2026-10-31", days −1 → 5, closed true → false, verified → "26 Oct 2026". articles/index.html: slide kick → "Closing in 5 days · Verified 26 Oct 2026", slide deadline fact → 31 Oct 2026, embedded JSON entry updated identically. cards_registry.py: vidyadhan dpill → "5 days to go".
- Note: site-data.json had already auto-marked this entry closed=true/days −1 (deadline-passed sweep); corrected back to open on the verified extension.

### 2. Pathani Samanta Mathematics Talent Scholarship 2026-27 (Odisha) — UNVERIFIABLE, left UNCHANGED
- Official source: Odisha State Scholarship Portal (scholarship.odisha.gov.in), checked live via browser 2026-10-26. Home page loaded normally; News & Announcements page loaded with "no news and announcements available" and a blank announcement ticker — no extension notice visible. The "ALL SCHEMES" page (scholarship-details) never displayed its scheme list — only a three-dot loading spinner, despite reloads, 60+ second waits, three separate tabs, and a fresh browser environment after a bot-check recovery attempt. Clicks were blocked by the loading overlay. No scheme name, status, or deadline was ever shown; no CAPTCHA, error, or access-denied notice appeared. Portal search for "Pathani Samanta" returned "No Results Found", but a control search for "Mathematics" also returned nothing, so that search does not index scheme names and is inconclusive.
- Corroborating listing (one, per pattern): Buddy4Study Odisha portal page and sarkariyojana.com / cigmapedia.com (crawled within the last 3 hours / days) still list the Pathani Samanta last date as 25 Oct 2026 with no extension mentioned. A 30 Sep 2026 Utkal Daily report of an extension to 30 Oct covers Pre-Matric/Post-Matric schemes only, not Pathani Samanta.
- Verdict: cannot confirm closed or extended from the official source — FLAGGED, article left unchanged per the no-fabrication rule (no checked_at set, no flip). The article still shows deadline 25 Oct 2026. Retry the portal scheme list later, or contact the portal helpdesk (toll-free 155335 / 1800-345-6770, shown on the home page).
- cards_registry.py pathani dpill ("Closes today") also left unchanged.

Final outcome of this run: NEITHER article closed. Vidyadhan EXTENDED to 31 Oct 2026; Pathani Samanta UNVERIFIABLE (portal scheme list would not load).

## 2026-10-28 — IPPA/SML-pattern closure recheck (scholarship-closure-recheck-oct28)

Two articles carried a 27 Oct 2026 deadline and were still marked OPEN as of 2026-10-26. Read-only checks performed today; corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself).

### 1. EU Jean Monnet Scholarship 2027–2028 — CLOSED
- Official source: https://jeanmonnet.org.tr/en/applications-for-the-2027-2028-academic-year-jean-monnet-scholarships-started (checked live via browser, 2026-10-28; text fetch crawled <1 min earlier agreed)
- Page still states "The application deadline is 27 October 2026" (applications started 27 August 2026; sealed-envelope submission to the Central Finance and Contracts Unit, Ankara, by 27 October 2026). No extension and no closure notice anywhere on the page; no newer or superseding announcement on that page. Deadline was yesterday (27 Oct) → CLOSED.
- Article flipped in place (eu-jean-monnet-scholarship-2027-2028.html): meta description notes closure, sub "Applications closed on 27 October 2026", dline pill → "Closed 27 Oct 2026", fact band → "Closed 27 Oct 2026", steps item → "Applications had to arrive by 27 October 2026 — the deadline has now passed", alert card → "Deadline: 27 Oct 2026 (closed)", verify note = "Verified 28 Oct 2026 … (corrected 28 Oct 2026 — deadline passed with no extension per the official page)". No deadline FAQ exists in this article, so none to match.
- Homepage dataset: site-data.json dlRaw → "27 Oct 2026 (closed)", verified → "28 Oct 2026" (dl 2026-10-27, days −1, closed already true via deadline-passed sweep). articles/index.html embedded JSON updated identically. cards_registry.py: jean-monnet-2027 dpill → "Closed 27 Oct 2026". Not present in homepage_data.json (50-entry list) — nothing to change there.

### 2. St. John's University Pharmaceutical Industry Fellowship 2027 (USA) — CLOSED (all materials)
- Official source: https://www.stjohns.edu/academics/schools/college-pharmacy-and-health-sciences/pharmaceutical-industry-fellowship-programs (checked live via browser, 2026-10-28)
- "Application Process" section, "Application material deadlines are outlined below": Official College Transcript — October 27, 2026; Three Letters of Recommendation — October 27, 2026; Curriculum Vitae — October 23, 2026; Letter of Intent — October 23, 2026. The 27 Oct deadline is still listed unchanged — not extended, not removed, no extension announced. The only "extension" on the page is an unrelated AIFA passage about fellowship-offer extensions. Deadline was yesterday (27 Oct) → CLOSED (all materials; CV/LOI had already closed 23 Oct).
- Article flipped in place (st-johns-university-pharma-fellowship-2027-usa.html): meta description → "All application materials closed 27 Oct 2026 (CV+LOI closed 23 Oct 2026)", JSON-LD applicationDeadline → 2026-10-27, dline pill → "Closed 27 Oct 2026", fact band → "Closed 27 Oct 2026", steps item → "Official transcripts + three recommendation letters were due 27 October 2026 — now closed", alert card → "Deadline: 27 Oct 2026 (closed)", verify note = "Verified 28 Oct 2026 … (corrected 28 Oct 2026 — transcripts + recommendation letters deadline passed; all application materials now closed)". No deadline FAQ exists in this article, so none to match.
- Homepage dataset: site-data.json dlRaw → "27 Oct 2026 (closed)", dl → 2026-10-27, days −5 → −1, verified → "28 Oct 2026" (closed true). articles/index.html embedded JSON updated identically. cards_registry.py: stjohns-pharma dpill → "Closed 27 Oct 2026". Not present in homepage_data.json (50-entry list) — nothing to change there.

Final outcome of this run: BOTH articles CLOSED, no extensions, nothing unverifiable.

## 2026-10-29 — IPPA/SML-pattern closure recheck (scholarship-closure-recheck-oct29)

Three articles carried a 28 Oct 2026 deadline and were still marked OPEN as of 2026-10-22. Read-only checks performed today; corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself). Writer cron and queue NOT touched. None of the three articles has a deadline FAQ, so there was no FAQ line to match.

### 1. NASA Hubble Fellowship Program 2027 — CLOSED
- Official source: https://science.nasa.gov/astrophysics/programs/physics-of-the-cosmos/community/applications-for-the-2027-nasa-hubble-fellowship-program/ (checked live via browser, 2026-10-29).
- Exact wording: "Applications are due Wednesday 28 October 2026 at 7p Eastern (4p Pacific)." Submission page open "from 8 September 2026 until the application deadline on 28 October 2026." No extension shown; page footer still "Page Last Updated: Sep 14, 2026." No explicit "portal closed" statement — closure follows from the deadline having passed with the submission window limited to that date.
- Article flipped in place (nasa-hubble-fellowship-program-2027.html): meta description notes closure, dline pill → "Closed 28 Oct 2026", fact band → "Closed 28 Oct 2026" (letters by 4 Nov still noted), steps item → "Applications closed 28 October 2026", alert card → "Deadline: 28 Oct 2026 (closed)", verify note = "Verified 29 Oct 2026 … (no extension shown; deadline has now passed)".
- Homepage dataset: site-data.json dlRaw → "28 Oct 2026 (closed)", verified → "29 Oct 2026" (dl 2026-10-28, days −1, closed already true via deadline-passed sweep). articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "28 Oct 2026 (closed)", days 12 → −1. cards_registry.py: nasa-hubble dpill → "Closed 28 Oct 2026". Related card in bloomberg article also flipped to Closed.

### 2. Bloomberg Harvard Visiting Scholars Program 2027 — CLOSED
- Official source: Bloomberg Center for Cities page https://www.cities.harvard.edu/bloomberg-harvard-visiting-scholars-program/ (fetched 2026-10-29; live browser also visited it and the Airtable application form).
- Timeline on the official page: "Application Closes: October 28th" — no extension shown. (The page's "now open / Apply by October 28th" line is stale post-deadline copy; the Timeline date governs.) Corroborating listings (OpportunityDesk, OYA Opportunities, Bright Scholarship, and the Center's own LinkedIn post a week earlier) all still say 28 Oct 2026, none mentions an extension.
- Article flipped in place (bloomberg-harvard-visiting-scholars-2027.html): meta description notes closure, dline pill → "Closed 28 Oct 2026", fact band → "Closed 28 Oct 2026", steps item → "Applications closed 28 October 2026", alert card → "Deadline: 28 Oct 2026 (closed)", verify note = "Verified 29 Oct 2026 on the official Bloomberg Center for Cities page … (no extension shown; deadline has now passed)".
- Homepage dataset: site-data.json dlRaw → "28 Oct 2026 (closed)", verified → "29 Oct 2026" (dl 2026-10-28, days −1, closed already true via sweep). articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "28 Oct 2026 (closed)", days 12 → −1. cards_registry.py: bloomberg-harvard dpill → "Closed 28 Oct 2026". Related card in nasa article also flipped to Closed.

### 3. University of Perugia PhD Scholarships 2026/27 — CLOSED
- Official sources checked via live browser 2026-10-29: University of Perugia XLII-cycle call page (unipg.it, idConcorso=59077), the official call document (ginko.unipg.it, iddocumento=101792), and the PICA competition page (pica.cineca.it/unipg/dottorato-xlii-regione/). Deadline 28 Oct 2026, 23:59; no extension notice found in the call, the call page, or extension searches.
- Corroborating listings crawled within hours of this check (daadscholarship.com, agristok.net) still show 28 Oct 2026 at 23:59, no extension.
- CAVEAT (delivery gap, recorded honestly): the live-browser agents' written reports for the Perugia checks (and for the original Bloomberg check) were not delivered back into this run even though their windows visited the official pages and closed; the verdicts above rest on the pages visited, the deadline wording found in the call-document searches, and the corroborating listings. The Perugia text-fetch of the PICA page returned only the competition title (JS page), so it alone would have been ambiguous — the flip rests on the live-browser official-page checks plus listings, not on that fetch.
- Article flipped in place (perugia-phd-scholarships-2026-27.html): meta description notes closure, dline pill → "Closed 28 Oct 2026", fact band → "Closed 28 Oct 2026", steps item → "Applications closed 28 October 2026, 23:59", alert card → "Deadline: 28 Oct 2026 (closed)", verify note = "Verified 29 Oct 2026 … (deadline 28 Oct 2026, 23:59, no extension found; deadline has now passed)".
- Homepage dataset: site-data.json dlRaw → "28 Oct 2026 (closed)", verified → "29 Oct 2026" (dl 2026-10-28, days −1, closed already true via sweep). articles/index.html embedded JSON updated identically. Not present in homepage_data.json (50-entry list) — nothing to change there. cards_registry.py: perugia-phd dpill → "Closed 28 Oct 2026".

Final outcome of this run: ALL THREE articles CLOSED, no extensions, nothing left unverifiable (with the Perugia report-delivery caveat above).

### Addendum (same day, after the run) — delayed browser reports received
The live-browser reports that were undelivered during the run itself arrived afterwards and CONFIRM the verdicts above, with no change to any flip:
- Bloomberg Harvard: official page Timeline "Application Closes: October 28th"; application form states "submit by October 28, 2026"; no extension on the official page, the form, or the OpportunityDesk listing. Nuance recorded: the official page still displays stale "now open / Apply by October 28th" copy and the Airtable form still loads with editable fields and an enabled-appearing Submit button — but that UI was not submission-tested, so it does not prove backend acceptance after the deadline, and no extension exists. The article correctly shows Closed on the passed deadline.
- Perugia: official call page states "SCADENZA 28/10/2026" / "Termine presentazione domande 28.10.2026"; the only notice under "Avvisi" is the 23 Oct 2026 test calendar, not an extension; PICA lists DOTTORATO_XLII_REGIONE as 28-09-2026 17:00 to 28-10-2026 23:59 with a red "Scaduto / Expired" banner. The earlier "report-delivery gap" caveat is therefore superseded — the Perugia closure is now directly confirmed by the official call page and PICA.

## 2026-10-31 — IPPA/SML-pattern closure recheck (scholarship-closure-recheck-oct31)

Re-derived at run time from site-data.json (407 entries): 14 entries carried dl=2026-10-30, not the 12 named in the task body — and all 14 were already marked closed=true, days=-1 by an apparent deadline-passed sweep, so the task body's closed=false filter returned zero. But every one of the 14 article HTML files still showed the 30 Oct deadline as open (dline pill "5 days to go" / "Deadline 30 Oct 2026 · 5 days left", status "Open", fact-band deadline 30 Oct, alert card "Deadline: 30 Oct 2026"). The real work was flipping those articles and updating verified dates / card pills, as in the 24/26/28/29 Oct runs. Read-only checks only; corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself). Writer cron and queue NOT touched.

Final outcome: 11 CLOSED, 2 EXTENDED to 15 Nov 2026, 1 CORRECTED to 31 Oct 2026 (still open on its last day, 31 Oct). Nothing left simply "unverifiable" — but two items carry recorded conflicts (Concentrix, Manipur) and two closed verdicts rest on listings rather than a located official project page (Monash, Dartmouth — see below).

Reconciliation note (important): the live-browser report for this run arrived AFTER the first verdicts were drafted and changed two of them. It confirmed 6 closures directly (Aditya Birla, DAAD, KNU, Muskaan, Saïd, Tokyo MEXT), reported Concentrix and Ujjivan as extended to 15 Nov 2026, and marked 6 items unverifiable on the pages it checked (Dartmouth, Infocepts, Monash, Meghalaya SC, Manipur ST, NVIDIA). Those 6 were then re-verified from other official sources before any flip, as recorded per item below — the browser's "unverifiable" meant only that its own pages did not show the date (sign-in-gated Canvas/portal for Dartmouth, a stale nvidia.com path for NVIDIA, the NSP public pages for the two NSP schemes, an article-slug 404 for Infocepts, and a Cloudflare-blocked Monash search). The browser report's own Monash search was also interrupted by a Cloudflare "Just a moment…" bot wall that was not cleared.

### 1. Aditya Birla Capital Scholarship 2026-27 — CLOSED
- Official source: Buddy4Study article https://www.buddy4study.com/article/aditya-birla-capital-scholarship (live browser + text fetch 2026-10-31).
- Exact wording: "Closing date — October 30, 2026" and "The last date to apply for the scholarship: October 30, 2026." No extension announced. (Note: the Buddy4Study programme page URL now returns only the generic portal homepage, not programme details.)
- Article flipped in place (aditya-birla-capital-scholarship-2026-27.html): dline pill → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026", alert card → "Deadline: 30 Oct 2026 (closed)", meta description → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026 per the Buddy4Study programme page …; no extension found)". JSON-LD applicationDeadline left as 2026-10-30 (the deadline date itself). WhatsApp reminder links left unchanged (they state the deadline date, not that it is still open).
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026 (closed)", verified → "31 Oct 2026" (dl 2026-10-30, days −1, closed already true). articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "30 Oct 2026 (closed)", days 14 → −1. cards_registry.py: abcapital dpill → "Closed 30 Oct 2026".

### 2. Concentrix Scholarship 2026-27 — EXTENDED to 15 Nov 2026 (verdict changed by the browser report; confirmed by own fetch)
- Official source: Buddy4Study article https://www.buddy4study.com/article/concentrix-scholarship (live browser + text fetch 2026-10-31; page title still "Concentrix Scholarship 2026-27 - ₹65,000 for MBBS Girls").
- Exact wording: the page now presents the programme as the "Winnie Sun Scholarship Program 2026-27", provided by "Concentrix Daksh Services India Private Limited", open from 28 Sep 2026, with "Closing date — November 15, 2026" and "The last date to apply for the scholarship: November 15, 2026." Page updated 2026-10-30. The page does not use the word "extension", but its stated last date is after 30 Oct 2026. Identity evidence: the Winnie Sun programme is the Concentrix programme (same provider, same ₹65,000/year MBBS award, same short code CTXSP1 in the Hans India / DT Next listings).
- CONFLICT FLAGGED (not resolved): the separate Winnie Sun programme page (buddy4study.com/scholarship/winnie-sun-scholarship) still shows Deadline: Closed with a 10 Sep–30 Oct 2026 portal, and DT Next (28 Oct 2026) listed Winnie Sun with last date 30 Oct. The article page (the corpus srcUrl) governs this update, but the programme page should be re-checked — if it still shows Closed, applicants following the article's Apply link may be blocked.
- Article updated in place (concentrix-scholarship-2026-27.html): dline pill → "Deadline 15 Nov 2026", Updated → 31 Oct 2026, fact band → "15 Nov 2026", steps → "Submit before 15 November 2026", alert card → "Deadline: 15 Nov 2026", meta description → "deadline 15 Nov 2026", WhatsApp reminder text → 15 Nov 2026, verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — deadline extended to 15 Nov 2026 …; conflict flagged: programme page still shows Closed …)". Status stays "Open".
- Homepage dataset: site-data.json dlRaw → "15 Nov 2026", dl → 2026-11-15, days −1 → 15, closed true → false, verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "15 Nov 2026", dl → 2026-11-15, days 14 → 15. cards_registry.py: concentrix dpill → "Deadline 15 Nov 2026".

### 3. DAAD University Summer Courses 2027 (Germany) — CLOSED
- Official source: DAAD scholarship database (daad.de, detail=50035295), live browser 2026-10-31.
- Exact wording under "Application deadline": "30 October of each year, 23:59 (Central European Time). Applications are possible from 01 September each year." No extension beyond 30 Oct 2026 announced; the recurring annual wording is not an extension for the 2026 deadline.
- Article flipped in place (daad-university-summer-courses-2027-germany.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "uploaded by 30 October 2026, 23:59 CET were considered", alert card → "Deadline: 30 Oct 2026 (closed)", FAQ "The official 2027 closing date is 30 October 2026, 23:59 CET." → "…was 30 October 2026, 23:59 CET, and has now passed.", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026, 23:59 CET, per the official DAAD scholarship database; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026, 23:59 CET (applications open 1 Sep 2026) (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json (50-entry list). cards_registry.py: daad dpill → "Closed 30 Oct 2026".

### 4. Dartmouth College DAAD Master Scholarship 2027 (Germany) — CLOSED (basis disclosed: DAAD guide, not the Dartmouth page itself)
- Sources: Dartmouth Fellowships Office page (live browser 2026-10-31) gives NO public deadline date — it says "To learn how to apply for nomination and see relevant deadlines, please see our Canvas site", which is sign-in gated and was not accessed; the DAAD portal redirected to sign-in. The closure verdict therefore rests on the DAAD Study Scholarship guide's USA/Canada country deadline of 30 Oct 2026 (portal closes 24:00 CET/CEST on the last day) plus the Dartmouth internal endorsement cutoff in early October 2026, which had already passed. Multiple listings agree on 30 Oct 2026, midnight CET. No extension found.
- Article flipped in place (dartmouth-college-daad-master-scholarship-2027-germany.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026 (DAAD portal)", alert card → "Deadline: 30 Oct 2026 (closed)", FAQ portal-deadline lines → past tense ("…was 30 October 2026, midnight CET, and has now passed"; "the portal deadline has now passed"), meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — DAAD portal deadline 30 Oct 2026 passed with no extension found; Dartmouth's own public page gives no deadline date (its Canvas route is sign-in gated) and its internal endorsement cutoff was already earlier, in early October 2026)".
- Homepage dataset: site-data.json dlRaw → "30 October 2026 (DAAD portal deadline; Dartmouth internal endorsement cutoff early October 2026) (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: dartmouth-daad-2027 dpill → "Closed 30 Oct 2026".

### 5. Infocepts Innovate for Impact Scholarship 2026-27 — CLOSED (browser's "unverifiable" was its article-slug check only)
- Official source: Buddy4Study programme page https://www.buddy4study.com/page/infocepts-innovate-for-impact-scholarship (text fetch 2026-10-31).
- Exact wording: "Eligibility Deadline: 30-Oct-2026". No extension shown. (The live browser checked the article slug and Buddy4Study site search instead, finding only the 2023-24 article — that check did not reach this programme page.)
- Article flipped in place (infocepts-innovate-impact-scholarship-2026-27.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026 per the Buddy4Study programme page, which still lists Deadline: 30-Oct-2026; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026 (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "30 Oct 2026 (closed)", days 14 → −1. cards_registry.py: infocepts dpill → "Closed 30 Oct 2026".

### 6. KNU International Graduate Scholarship 2027 (Korea) — CLOSED
- Official source: KNU English site, International Office Degree Program, Graduate tab (https://home.knu.ac.kr/HOME/global/sub.htm?nav_code=glo1729758639), live browser 2026-10-31.
- Exact wording for Spring 2027, "Online Application & Document Upload": "Sep. 28, 2026 (Mon) 09:00 ~ Oct. 30, 2026 (Fri) 18:00." No extension beyond 30 Oct 2026, 18:00 shown.
- Article flipped in place (knu-international-graduate-scholarship-2027-korea.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026, 6:00 PM KST", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — Spring 2027 online application and document upload ran 28 Sep–30 Oct 2026, 18:00 KST, per the official KNU International Office graduate admissions page; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026, 6:00 PM KST (Spring 2027 intake) (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: knu dpill → "Closed 30 Oct 2026".

### 7. Monash University ReDiLEEP PhD Scholarship 2027 (Australia) — CLOSED (basis disclosed: concordant listings, no official project page located)
- Sources: no separate official Monash project page for ReDiLEEP was located — Monash site search returns "0 search results for ReDiLEEP" (live browser 2026-10-31; its search was also interrupted by a Cloudflare "Just a moment…" bot wall that was not cleared). The generic Monash Graduate Scholarship page does not mention ReDiLEEP. Multiple project listings agree: 30 Oct 2026, 12:00 noon Melbourne time, project led by Dr Giulia Ghedini, EOI to the supervisor. No extension found anywhere.
- Article flipped in place (monash-university-redileep-phd-scholarship-2027-australia.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026 at 12:00 noon Melbourne time", alert card → "Deadline: 30 Oct 2026 (closed)", FAQ "What is the deadline?" → "What was the deadline? 30 October 2026 at 12:00 noon Melbourne time — now closed.", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026, 12:00 noon Melbourne time, per the project listings; no extension found. Note: no separate official Monash project page for ReDiLEEP was located (Monash site search returns no ReDiLEEP result), so this verdict rests on the concordant listings)".
- Homepage dataset: site-data.json dlRaw → "30 October 2026, 12:00 noon Melbourne time (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: monash-redileep-2027 dpill → "Closed 30 Oct 2026".

### 8. Muskaan Scholarship Program 2.0 — CLOSED
- Official source: Buddy4Study article https://www.buddy4study.com/article/muskaan-scholarship (live browser 2026-10-31).
- Exact wording: "Last Date to Apply — October 30, 2026." No extension announced. (The Buddy4Study programme page still lists "Eligibility Deadline: 30-Oct-2026".)
- Article flipped in place (muskaan-scholarship-2-2026-27.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026 per the Buddy4Study programme page, which still lists Deadline: 30-Oct-2026; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026 (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically, PLUS the Muskaan slide (kick → "Closed 30 Oct 2026 · Verified 31 Oct 2026", slide deadline fact → "Closed 30 Oct 2026") and guide card (Verified → 31 Oct 2026). homepage_data.json dl_raw → "30 Oct 2026 (closed)", days 14 → −1. cards_registry.py: muskaan dpill → "Closed 30 Oct 2026".

### 9. NSP Post-Matric Scholarship for SC Students, Meghalaya 2026-27 — CLOSED (browser's "unverifiable" was NSP-public-pages only)
- Official sources: (a) Government of Meghalaya, Directorate of Higher and Technical Education notification No. CE/SCHOLJAD/1/2018-19/175, dated Shillong 3 July 2026 (PDF at cdn.s3waas.gov.in, fetched 2026-10-31): closing date of application registration by students 30 Oct 2026, verification by 20 Nov 2026. (b) Buddy4Study programme page (fetched 2026-10-31) now shows Deadline: Closed, with Important Dates still "Application Deadline: 30th October 2026". General NSP 31 Oct 2026 dates for other schemes do NOT override this scheme-specific 30 Oct date. (The live browser checked only the NSP homepage/Public pages, which show no scheme-specific dates without sign-in.)
- Article flipped in place (nsp-post-matric-sc-meghalaya-2026-27.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026 per the Government of Meghalaya Directorate of Higher and Technical Education notification of 3 July 2026 and the Buddy4Study programme page, which now shows Deadline: Closed; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026 (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "30 Oct 2026 (closed)", days 14 → −1. cards_registry.py: megh-sc dpill → "Closed 30 Oct 2026".

### 10. NSP Pre-Matric Scholarship for ST Students, Manipur 2026-27 — NOT CLOSED; deadline CORRECTED to 31 Oct 2026 (still open on its last day)
- This is a correction against the state notification, NOT an announced extension.
- Official source: Government of Manipur, Directorate of Tribal Affairs & Hills notification dated Imphal 31 July 2026 (PDF at cdn.s3waas.gov.in, fetched 2026-10-31): Pre-Matric ST Scholarship scheme application 01-08-2026 to 31-10-2026, institute verification to 20-11-2026, DNO/SNO/MNO verification to 30-12-2026, and point 10: "Online submission of application will not be extended beyond the last date i.e. 31.10.2026." The corpus's 30 Oct date came from the Buddy4Study listing. (The live browser checked only the NSP homepage/Public pages, which show no scheme-specific dates without sign-in.)
- CONFLICT FLAGGED: Buddy4Study's Manipur programme page (fetched 2026-10-31) shows Deadline: Closed, with Important Dates/FAQ still 30 Oct 2026 — that Closed badge appears driven by Buddy4Study's own 30 Oct listing, while the state notification governs here. Also observed, not resolved: the Buddy4Study page lists parent/guardian income ≤ Rs 2,00,000, while the state notification says income not exceeding Rs 2,50,000 — the article's income figure was NOT changed on this run.
- Article updated in place (nsp-pre-matric-st-manipur-2026-27.html): dline pill → "Closes today", Updated → 31 Oct 2026, fact band → "31 Oct 2026", steps → "Before 31 October 2026", alert card → "Deadline: 31 Oct 2026", meta description → "deadline 31 Oct 2026", WhatsApp reminder text → 31 Oct 2026, verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — the Manipur Directorate of Tribal Affairs & Hills notification of 31 July 2026 sets student applications to 31 Oct 2026 and states they will not be extended beyond that date; the corpus's 30 Oct date came from the Buddy4Study listing, whose programme page now shows Closed on its own 30 Oct listing — the state notification governs here, so the scheme is still open today, its last day)". Status stays "Open".
- Homepage dataset: site-data.json dlRaw → "31 Oct 2026", dl → 2026-10-31, days −1 → 0, closed true → false, verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "31 Oct 2026", dl → 2026-10-31, days 14 → 0. cards_registry.py: manipur-st dpill → "Closes today".

### 11. NVIDIA Graduate Fellowship 2027-28 — CLOSED (browser's "unverifiable" was a stale nvidia.com path)
- Official source: NVIDIA Research fellowship page https://research.nvidia.com/graduate-fellowships (text fetch 2026-10-31).
- Exact wording: "2027–2028 applications open September 30, 2026. Apply by October 30, 2026." and under Application dates: "Application deadline — October 30, 2026, Including recommendation letters." No extension found. (The live browser visited https://www.nvidia.com/en-us/research/graduate-fellowships/ instead, which shows only the stale 2023-24 "now CLOSED" wording and no 2027-28 deadline — that page is not the fellowship programme page.)
- Article flipped in place (nvidia-graduate-fellowship-2027-28.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "letters were due on the same 30 October deadline" / "before the 30 October 2026 deadline (now closed)", alert card → "Deadline: 30 Oct 2026 (closed)" (this also fixes the article's duplicated "Deadline: Deadline:" heading), meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026 including recommendation letters per the official NVIDIA Research fellowship page; no extension found)".
- Homepage dataset: site-data.json dlRaw → "Deadline: 30 October 2026 — including all recommendation letters (8 days from 22 Oct 2026). Fellowship year: 2027–28 (9 months); mandatory summer internship in summer 2027. (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: nvidia-2027 dpill → "Closed 30 Oct 2026".

### 12. Saïd Foundation Scholarship 2027 (UK) — CLOSED
- Official sources: Imperial College London partner page https://www.imperial.ac.uk/study/fees-and-funding/postgraduate-taught/grants-scholarships/said-foundation-scholarship/ (live browser 2026-10-31) and the Saïd Foundation's own applications page https://saidfoundation.org/apply/.
- Exact wording (Imperial): "Applications close at 5pm UK time on Friday, 30 October 2026" and "Applications for 2027-28 Saïd Foundation scholarships open on Tuesday, 1 September and closes on Friday, 30 October." The Foundation's own page now states explicitly: "Applications for 2027/28 Saïd Foundation scholarships are now closed." No extension announced.
- Article flipped in place (said-foundation-scholarship-2027-uk.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, Timeline fact "Now open → 30 Oct 2026" → "Closed 30 Oct 2026", steps → "Applications closed 30 October 2026 (5:00 PM UK time)", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — applications closed 30 Oct 2026, 5:00 PM UK time, per the Imperial College London official partner page; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026, 5:00 PM UK time (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: said dpill → "Closed 30 Oct 2026".

### 13. Ujjivan Small Finance Bank Transgender Scholarship 2026-27 — EXTENDED to 15 Nov 2026 (verdict changed by the browser report; confirmed by own fetch)
- Official source: Buddy4Study article https://www.buddy4study.com/article/ujjivan-small-finance-bank-transgender-scholarship (live browser + text fetch 2026-10-31).
- Exact wording: "The Ujjivan Small Finance Bank Transgender Scholarship Program 2026-27 is now open for applications" and "Last Date to Apply — November 15, 2026." Page updated 2026-10-30. The page does not use the word "extension", but its stated last date is after 30 Oct 2026. (No 2026-27 programme page was located separately — only the 2024-25 programme page, which is a different cycle.)
- Article updated in place (ujjivan-transgender-scholarship-2026-27.html): dline pill → "Deadline 15 Nov 2026", Updated → 31 Oct 2026, fact band → "15 Nov 2026", steps → "Submit before 15 November 2026", alert card → "Deadline: 15 Nov 2026", meta description → "deadline 15 Nov 2026", WhatsApp reminder text → 15 Nov 2026, verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — deadline extended to 15 Nov 2026: the Buddy4Study article page, updated 30 Oct 2026, now states the programme is open with Last Date to Apply 15 Nov 2026)". Status stays "Open".
- Homepage dataset: site-data.json dlRaw → "15 Nov 2026", dl → 2026-11-15, days −1 → 15, closed true → false, verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. homepage_data.json dl_raw → "15 Nov 2026", dl → 2026-11-15, days 14 → 15. cards_registry.py: ujjivan dpill → "Deadline 15 Nov 2026".

### 14. University of Tokyo MEXT Scholarship 2027 (Japan) — CLOSED
- Official source: University of Tokyo Graduate School of Science page https://www.s.u-tokyo.ac.jp/en/admission/scholarship.html (live browser + text fetch 2026-10-31; page last updated 8 Oct 2026).
- Exact wording, section 5 Application Period: "From October 15 to October 30, 2026, Japan Standard Time. The electronic application must be submitted within the application period." and "An application passed the submission deadline is not acceptable." No extension announced.
- Article flipped in place (university-of-tokyo-mext-scholarship-2027-japan.html): dline → "Closed 30 Oct 2026", status → "Closed", Updated → 31 Oct 2026, fact band → "Closed 30 Oct 2026", steps → "before the 30 October 2026 deadline (now closed)", alert card → "Deadline: 30 Oct 2026 (closed)", meta → "Closed 30 Oct 2026", verify note = "Verified 31 Oct 2026 … (corrected 31 Oct 2026 — application period 15–30 Oct 2026 JST per the official University of Tokyo Graduate School of Science page; no extension found)".
- Homepage dataset: site-data.json dlRaw → "30 Oct 2026 (Graduate School of Science) (closed)", verified → "31 Oct 2026". articles/index.html embedded JSON updated identically. Not in homepage_data.json. cards_registry.py: u-tokyo-mext dpill → "Closed 30 Oct 2026".

Scope limit (deliberate, as in prior runs): related-card dpill pills ("5 days to go") inside OTHER articles that link to these 14 were NOT updated (about 70 files, e.g. DAAD Summer linked from many Erasmus/DAAD articles, UTokyo MEXT from many Japan articles). The task body names only the homepage dataset / card registry. Only the Muskaan slide/guide card inside articles/index.html itself was updated, since that is the homepage.

Final outcome of this run: 11 CLOSED (Aditya Birla Capital, DAAD Summer Courses, Dartmouth DAAD Master, Infocepts, KNU, Monash ReDiLEEP, Muskaan, NSP Post-Matric SC Meghalaya, NVIDIA Graduate Fellowship, Saïd Foundation, University of Tokyo MEXT); 2 EXTENDED to 15 Nov 2026 (Concentrix, Ujjivan Transgender); 1 CORRECTED to 31 Oct 2026, still open on its last day (NSP Pre-Matric ST Manipur — state-notification correction, not an announced extension). Watch items: Concentrix programme page still showing Closed on a 30 Oct window vs its article page's 15 Nov date; Manipur Buddy4Study Closed badge vs the state notification's 31 Oct date; Manipur income-limit discrepancy (Buddy4Study Rs 2,00,000 vs notification Rs 2,50,000) left unchanged.

## 2026-11-01 — IPPA/SML-pattern closure recheck (scholarship-closure-recheck-nov01)

Re-derived at run time from site-data.json (416 entries): 51 entries carried dl=2026-10-31, not the 25 named in the task body — and all 51 were already marked closed=true, days=-1 by an apparent deadline-passed sweep, so the task body's closed=false filter returned zero. But every one of the 51 article HTML files still showed the 31 Oct deadline as open (dline pill "6 days to go" / "Deadline 31 Oct 2026 · N days left" / "Closes today", status "Open"). The real work was checking and flipping those articles, as in the 31 Oct run. Read-only checks first (4 parallel triage batches + own live-browser and fetch confirmations); corpus files updated in place. Deploy zip NOT rebuilt (deploy fork: qadir uploads himself). Writer cron and queue NOT touched.

Final outcome: 41 FULLY CLOSED for this cycle; 6 with only the 31 Oct round/window/intake closed while another route remains (Malta October round, Melbourne GRS Round 1, Melbourne Research Round 1, Stuttgart October joint window, Al Qasimi winter intake — plus Huddersfield, where only the Early Payment Discount deadline passed and the scholarship itself is automatic); 1 EXTENDED to 15 Nov 2026 (Satya); 1 moved to ALWAYS OPEN (Eastman PowerUp EduSkill); 2 CORRECTED to open with no closing date announced (Oasis pair — live portal check, not a closure and not an extension). Nothing left simply "unverifiable": every item got a verdict, with the weaker bases disclosed below (Nirman Odisha portal fetch failed; UBD and Malta official pages stale; Satya extension rests on listings, not a refreshed programme page).

Per-item record (article flipped in place unless stated: dline pill, status, Updated → 1 Nov 2026, fact band, steps, alert card, meta description, verify note = "Verified 1 Nov 2026 …"; site-data.json + articles/index.html embedded JSON updated identically; cards_registry.py dpill updated; homepage_data.json contained none of the 51 — nothing to change there):

### Batch A — NSP central + PM YASASVI + PMSS (14 CLOSED)
Official NSP homepage notice checked 1 Nov 2026 for all 14: "Closing dates for student application is 31-10-2026 and closing date for institute verification is: 15-11-2026 and closing date for L2 verification is: 30/11/2026", with no extension banner for these schemes. Institute/L2 dates are verification windows for already-submitted applications, not student-application extensions. All 14 srcUrls point to the generic NSP homepage, so scheme dates rest on the NSP schedule plus the scheme-specific listings quoted; that limitation applies to the whole batch.

### 1. NSP Ishan Uday Special Scholarship, NER 2026-27 — CLOSED
- Buddy4Study article: "The application process for the Ishan Uday Scholarship 2026-27 commenced on September 16, 2026 and will remain open until October 31, 2026." Defective correction to 15 Nov, DNO/SNO/MNO to 30 Nov 2026. Conflict noted: one listing's overview table shows 30 Nov 2026, but the same page's body says 31 Oct 2026 — the 30 Nov figure matches the L2 verification date and is a mislabelled table entry. No extension found.

### 2. NSP National Scholarship for Post Graduate Studies 2026-27 — CLOSED
- Careerindia NSP list: "Most central schemes on NSP show October 31 as the student deadline. These include AICTE Pragati and Saksham, UGC Ishan Uday, and National Scholarship for Post Graduate Studies." Opened 16 Sep 2026; institute verification to 15 Nov, L2 to 30 Nov 2026. No extension found.

### 3. NSP PM Scholarship for wards of States/UTs police personnel 2026-27 — CLOSED
- Careerindia: "| PM Scholarships (CAPF/Railways/States‑UT Police) | Open | October 31, 2026 | Until November 15, 2026 |"; Buddy4Study PMSS overview: "While the closing date for CAPFs, Assam Rifles, and State/UT police applicants is October 31…" No extension found.

### 4. NSP Top Class Education for Students with Disabilities 2026-27 — CLOSED
- Buddy4Study article: "…are open from June 1, 2026 and eligible candidates can submit their applications through the National Scholarship Portal (NSP) until October 31, 2026." Verification to 15 Nov / 30 Nov 2026. No extension found.

### 5. NSP Top Class Education for SC Students 2026-27 — CLOSED
- Buddy4Study scheme page now shows "Deadline: Closed", "Application Deadline: 31st October 2026"; CollegeChalo: "On NSP: open from 1 June 2026, last date 31 October 2026". No extension found.

### 6. AICTE Saksham Scholarship Scheme 2024-25 — CLOSED
- AICTE notice via SASTRA: "portal for submission of fresh and renewal cases applications under AICTE Pragati… AICTE Saksham… and AICTE Swanath… has been opened and last date for submission of online application is 31.10.2026" and "no further request for extension of the date shall be entertained under any circumstances." Live cycle checked is 2026-27 (the 2024-25 title has been succeeded by later cycles). Article has no plain "Deadline" fact row — its "Deadline (live cycle)" fact was flipped to "Closed 31 Oct 2026". No extension found.

### 7. AICTE Swanath Scholarship Scheme 2026-27 — CLOSED
- Same AICTE/SASTRA notice as Saksham; Buddy4Study AICTE article: "For most AICTE scholarships listed on NSP, including the Swanath Scholarship Scheme, Pragati Scholarship Scheme, and Saksham Scholarship Scheme, the last date to apply is October 31, 2026." No extension found.

### 8. PM YASASVI Post-Matric OBC, Andaman 2026-27 — CLOSED
- Andaman local report: "the portal for all three schemes, Pre-Matric Scholarship for OBC students, Post-Matric Scholarship for OBC and EBC students, and Grant of Additional Scholarship (UT) for OBC students, opened on July 1, 2026. The last date for submission of applications has been fixed as October 31, 2026." No extension found.

### 9. PM YASASVI Post-Matric OBC, Sikkim 2026-27 — CLOSED (either date gives the same outcome)
- General PM YASASVI post-matric date 31 Oct 2026; Sikkim-specific Buddy4Study page lists 30 Sep 2026. Closed under either date; no post-October extension found. Article keeps "Closed 31 Oct 2026" (corpus/general date).

### 10. PM YASASVI Pre-Matric OBC, Sikkim 2026-27 — CLOSED (either date gives the same outcome)
- Careers360: "| Last date to apply for the pre-matric scholarship | October 31, 2026 (Extended) |" (extended from 30 Sep to 31 Oct); Sikkim-specific Buddy4Study page still shows 30 Sep 2026, which predates that extension. Closed under either date; no later extension found.

### 11. PM YASASVI Top Class College Scholarship 2026-27 — CLOSED
- FastJobSearchers + Careers360: "PM YASASVI Central Sector Scholarship of Top Class Education in College for OBC, EBC And DNT Students (Merit Based Scheme) | Last Date: 31-10-2026". Not the Top Class in Schools scheme, which the NSP homepage still shows open for fresh applications. No extension found.

### 12. PM Scholarship for CAPF and Assam Rifles 2026-27 — CLOSED
- Buddy4Study PMSS table: "| Prime Minister'S Scholarship Scheme For Central Armed Police Forces And Assam Rifles (Merit Based Scheme) | June 1, 2026 | October 31, 2026 |". Institute verification to 15 Nov, ministry verification to 30 Nov 2026. No extension found.

### 13. PM Scholarship Scheme, Ministry of Railways (RPF/RPSF) 2026-27 — CLOSED (own fetch confirms)
- Buddy4Study scheme page fetched 1 Nov 2026 by the parent run itself: "Deadline: Closed" and "Application Deadline: 31st October 2026". Conflict resolved: the Buddy4Study PMSS overview article's claim of 31 Dec 2026 is outweighed by the scheme-specific page, Shiksha's PMSS guide ("The last date for students is October 31, 2026" for all three NSP PMSS routes) and the centrally-funded list (all 31 Oct). No extension found.

### 14. Post-Matric Beedi/Cine/IOMC/LSDM Workers 2026-27 — CLOSED
- Buddy4Study article + Times of India: "students applying under the Post-Matric Financial Assistance for Education to the Wards of Beedi/Cine/IOMC/LSDM Workers must complete their online application on the National Scholarship Portal (NSP) by October 31, 2026. Applications submitted after the official deadline will not be considered for further verification." Pre-matric version closed earlier (31 Aug 2026) — not this item. No extension found.

### Batch B — NSP state schemes + Odisha/Tripura/HP (11 CLOSED, 2 corrected open)

### 15. NSP Kalpana Chawla Chatravriti Yojana, Himachal Pradesh 2026-27 — CLOSED
- Buddy4Study HP table: "| Kalpana Chawla Chatravriti Yojana | June 4, 2026 | October 31, 2026 |"; ABVGIET NSP notice: "As per the information available on the NSP, the last date for submission of scholarship applications is 31 October 2026" and "Kalpana Chawla Chatravriti Yojana – Himachal Pradesh | Through NSP Portal 31-10-2026". No extension found.

### 16. NSP Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026-27 — CLOSED
- Buddy4Study HP table: "| Maharishi Balmiki Chatravriti Yojana | June 4, 2026 | October 31, 2026 |"; ABVGIET notice lists the scheme through the NSP portal at 31-10-2026. No extension found.

### 17. NSP Mukhya Mantri Protsahan Yojana, Himachal Pradesh 2026-27 — CLOSED (conflict noted, weakest of the batch)
- Cycle-specific Buddy4Study HP table: "| Mukhya Mantri Protsahan Yojana | June 4, 2026 | October 31, 2026 |". Conflict: undated Notopedia listing says "The last date to apply for this scholarship is December 31, 2026" — it gives no 2026-27 extension notice and December dates match older cycles (e.g. 2019-20 extended to 31-12-2019), so the cycle-specific table governs. No 2026-27 extension notice to December was found. A live NSP scheme-page check would remove all doubt.

### 18. NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27 — CLOSED
- Buddy4Study HP table: "| Thakur Sen Negi Utkrisht Chatravriti Yojana | June 4, 2026 | October 31, 2026 |" and "programs with an October 31, 2026 application deadline include … Thakur Sen Negi Utkrisht Chatravriti Yojana …". No extension found.

### 19. NSP Post-Matric SC, Sikkim 2026-27 — CLOSED
- Buddy4Study scheme page now shows "Deadline: Closed" and "Application Deadline: October 31, 2026". No extension found.

### 20. NSP Pre-Matric SC, Sikkim 2026-27 — CLOSED (either date gives the same outcome)
- Buddy4Study Sikkim table still lists 30 Sep 2026 while the general pre-matric date was extended to 31 Oct 2026 (Careers360). Both dates have passed; no extension beyond either was found.

### 21. NSP Pre-Matric ST, Goa 2026-27 — CLOSED
- Buddy4Study Goa article: "The Centrally Sponsored Pre-Matric Scholarship for Scheduled Tribe (ST) Students has an application deadline of October 31, 2026". Minor discrepancy only: a second Buddy4Study state-funded table line gives 30 Oct 2026 — both have passed. Goa's Post-Matric ST scheme (30 Nov 2026) is a different scheme and does not extend this pre-matric item. No extension found.

### 22. NSP Pre-Matric ST, Manipur 2026-27 — CLOSED (no-extension condition still holds)
- Official Manipur Directorate of Tribal Affairs & Hills notification, 31 Jul 2026 (cdn.s3waas.gov.in): "Pre-Matric ST Scholarship 01-08-2026 31-10-2026" and "Online submission of application will not be extended beyond the last date i.e. 31.10.2026." Searches for a later Manipur extension notice returned nothing; Buddy4Study's scheme page now shows "Deadline: Closed". (This supersedes the 31 Oct run's "still open on its last day" status — the last day has now passed.) Minor discrepancy: Buddy4Study's FAQ text says 30 Oct 2026, one day earlier than the official 31-10-2026; it does not affect the outcome.

### 23. Nirman Shramik Kalyan Yojana, Odisha 2026-27 — CLOSED (basis disclosed)
- Buddy4Study scheme page now shows "Deadline: Closed" and "Scholarship Deadline: October 31, 2026"; Odisha article: "Candidates can also apply for the Nirman Shramik Kalyan Yojana by October 31, 2026, by visiting the Odisha State Scholarship Portal." One listing notes 31 Oct was itself the extended date. Caveat: the Odisha portal text fetch failed on network grounds, so this verdict rests on the programme page plus concordant listings, not a successful official-portal read. No further extension found.

### 24. Umbrella Scheme Post-Matric ST, Tripura 2026-27 — CLOSED for student applications
- Official Tripura Tribal Welfare Department notification: "Application registration/ submission and defective application re-submission [for] ST Post-Matric Scholarship: 15th August 2026 to 31st October 2026", with institute verification to 5 Nov, district verification to 30 Nov, state verification to 31 Dec 2026. Buddy4Study scheme page now shows "Deadline: Closed". Conflict resolved: a generic listing's 30 Nov 2026 date matches the district verification deadline, not student submission. No student-application extension found.

### 25. Dr Ambedkar Medhavi Chatravriti Yojana, Himachal Pradesh 2026-27 — CLOSED
- Buddy4Study scheme page now shows "Deadline Date: Closed" and "Application Deadline: 31st October 2026"; HP table: "| Dr. Ambedkar Medhavi Chatravriti Yojana for SC Students | June 4, 2026 | October 31, 2026 |" (same for OBC). Older Notopedia pages giving 31 May 2026 are stale prior-cycle dates. No extension found.

### 26. Oasis Post-Matric OBC, West Bengal 2026-27 — NOT CLOSED; corrected to open, no closing date announced
### 27. Oasis Post-Matric SC/ST, West Bengal 2026-27 — NOT CLOSED; corrected to open, no closing date announced
- Live-browser check of the official portal 1 Nov 2026 (oasis.gov.in → oasis.wb.gov.in): homepage ANNOUNCEMENTS section states "Online Application for Scholarship for 2026-27 Session is open for Post matric SC, ST, OBC & Pre Matric Sc,Pre Matric Comp-II, ST, OBC." (repeated in Bengali); STUDENTS CORNER is labelled "ACADEMIC SESSION : 2026 - 27" with registration and renewal still listed; FAST FACTS dated "AS ON 01-11-2026" shows 257,279 applications received. Homepage-text searches for "closed", "deadline" and "last date" returned no matches. The corpus's 31 Oct 2026 date came from a secondary listing (Buddy4Study asserts 31 Oct 2026 for all Oasis schemes) and is NOT stated on the portal — while two guides checked 30 Oct 2026 (findmycollege, Shiksha) both report no closing date announced. Flipping to "Closed 31 Oct 2026" would have been guessing, so both articles were instead corrected: dline "Open · no date announced", fact "No closing date announced", alert "Deadline: not announced yet", WhatsApp reminder reworded without a date, verify note dated 1 Nov 2026, site-data dl → null, closed → false, dlRaw "No closing date announced (Oasis portal shows 2026-27 applications open)", registry dpill "Open · no date announced". Caveat: no sign-in was performed, so a date could theoretically appear inside a logged-in flow; the public portal shows none.

### Batch C — ICAR / India programmes (9 CLOSED, 1 ALWAYS OPEN, 1 EXTENDED)

### 28. ICAR Junior Research Fellowship (PGS) 2026 — CLOSED
- Buddy4Study programme page: "Deadline: Closed" … "Application Deadline: 31st October 2026". The 15 Nov 2026 NSP extension found in this run covers NMMSS only, not ICAR schemes. No ICAR extension found.

### 29. ICAR NTS (PG) 2026 — CLOSED
- Buddy4Study programme page: "Deadline Date: 31-Oct-2026" / "Application Deadline: 31st October 2026"; Internshala: "When: 2026-06-01 to 2026-10-31". Unlike JRF and NTS-UG, this page has not yet been flipped to a "Closed" badge, but the date has passed and no extension was found.

### 30. ICAR NTS (UG) 2026 — CLOSED
- Buddy4Study programme page: "Deadline: Closed" … "Application Deadline: 31st October 2026". No extension found.

### 31. ICAR Post Graduate Scholarship (PGS) 2026 — CLOSED
- Scholarshiplist + SwapUpdate: "The 2026-27 National Scholarship Portal window closes on 31 October 2026" / "Submit before 31 October 2026". Institute verification to 15 Nov, ministry verification to 30 Nov 2026. No ICAR-specific extension found.

### 32. ISI Kolkata Stipend Scheme UG/PG 2026-27 — CLOSED, with the corpus date corrected in the note
- The stipend follows admission, not a separate application, and ISI finished 2026-27 admissions earlier in 2026: Mathrubhumi (14 Feb 2026) gives applications by 13 Mar 2026 via admission.isical.ac.in, AglaSem notes 28 May 2026 for B SDS and "ISI has finished admissions for 2026-27". The ISI admission portal fetch itself failed (upstream fetch error), so this rests on secondary sources. The article's 31 Oct 2026 date was only a scholarship-listing cycle (the article's own FAQ said so), and that cycle has passed; the article was flipped to "Closed 31 Oct 2026" with the fact band reading "Closed 31 Oct 2026 (listing cycle; stipend follows admission)" and the verify note carrying the correction. No separate stipend application exists for 2026-27.

### 33. WINGS Women in STEM, IIT Bombay 2027-28 — CLOSED
- Hans India 9 Oct 2026 (Buddy4Study-sourced, b4s.in/hans/WINGS2): "Last Date to Apply: 31-10-2026" for female students planning UG STEM at IIT Bombay (2027-28 session). The Buddy4Study programme page itself was not directly retrievable; the verdict rests on the concordant newspaper listings. No extension found.

### 34. Sakal India Foundation Career Development Scholarship 2026 — CLOSED
- Buddy4Study programme page: "Deadline Date: 31-Oct-2026" / "Application Deadline: 31st October 2026"; The Hindu (24 Oct 2026): "Deadline: October 31". The official foundation page prints no deadline date. A separate Career Development Renewal track (31 Mar 2027) is for continuation students, not this fresh 2026 item. No extension found.

### 35. SDEF India Scholarship 2026-27 — CLOSED (stale-banner conflict flagged)
- Official Swami Dayanand page (fetched 1 Nov 2026) timeline: "Deadline: October 31st, 2026", notifications "Mid November 2026". The same page still displays "Now Accepting Applications" above the deadline — that banner looks stale against its own 31 Oct 2026 deadline, and no extension wording appears anywhere on the page. Treated as closed for this cycle; the banner is flagged here, not silently fixed on the provider's page.

### 36. Vidyadhan Mathura Women in STEM Scholarship 2026 — CLOSED
- The official Vidyadhan apply page had extended the deadline to 31 Oct 2026 (per this article's own 26 Oct 2026 verification note), with interviews 15-30 Nov 2026. The older 25 Oct 2026 listing was superseded by that extension, and no further extension was found. (The triage batch's "25 Oct" report was the pre-extension date; the article's own verified note governs.)

### 37. Eastman PowerUp EduSkill Scholarship Program 2026-27 — ALWAYS OPEN (not a fixed-date extension)
- Buddy4Study programme page fetched 1 Nov 2026 (crawled 03:33 UTC): "Deadline / Always Open". This supersedes all three earlier dates (31 Jul, 30 Sep, 31 Oct 2026); there is no new fixed date to write. Article updated to "Always Open" throughout (dline, fact, alert "No fixed deadline — Always Open", FAQ "What is the real deadline?", sub/description deadline-history sentence, WhatsApp reminder), JSON-LD applicationDeadline removed (as for other rolling corpus items), site-data dl → null, days → null, closed → false, dlRaw "Always Open (Buddy4Study programme page shows no fixed deadline; earlier listings gave 31 Jul, 30 Sep and 31 Oct 2026)", registry dpill "Always Open".

### 38. Satya Scholarship Program 2026 — EXTENDED to 15 Nov 2026 (conflict flagged; confirmed by parent's own search)
- Sakshi Education (27 Oct 2026): "Last Date to Apply: 15 November 2026" (short URL www.b4s.in/sen/SAT4); Hindustan Gazette: "students applying for the Satya Scholarship currently have until November 15"; Meghalaya Portal roundup (same week) agrees. Conflict flagged: Buddy4Study's own article page is stale at 31 Aug 2026, its scholarship index snippet still shows 31-Oct-2026, and its programme page badge reads "Always Open" — so the 15 Nov date rests on the three late-October listings, not on a refreshed programme page, and should be re-checked on the programme page before being relied on. Article updated to deadline 15 Nov 2026 throughout (dline, fact, steps, alert, meta, WhatsApp reminder, JSON-LD 2026-11-15), site-data dl → 2026-11-15, days → 14, closed → false, registry dpill "Deadline 15 Nov 2026".

### Batch D — International (6 fully closed + UBD closed on listings + 6 round/window-only closures)

### 39. Honjo International Scholarship 2027, Japan — CLOSED
- Official 2027 guideline PDF (hosted at Iwate University): "(Application Period： September 1 ~ October 31, 2026)"; "no later than the application deadline (October 31, 2026)". The HISF Japanese homepage itself gave no deadline. No extension found.

### 40. Macquarie University Research Scholarship (Road to Research), Australia — CLOSED
- Official Macquarie page: "Applications close on 31 October 2026 at 11pm"; "Online applications for a January 2027 commencement (Session 1 2027) will close on 31 October 2026 (AEDT)." Onshore-only eligibility stressed on the page. The main International Research Scholarship Round (iRTP/iMQRES) had already closed 31 Jul 2026 — that is a separate, earlier closure, not this item. No extension found.

### 41. NSP National Scholarship Programme, Slovakia 2027 — CLOSED for the 31 Oct call
- Official scholarships.sk terms: "31 October at 16.00 CET – scholarship stays during the summer semester of the current academic year". The 30 April call ("30 April at 16.00 CET – scholarship stays during the next academic year") is a separate call, not an extension. Article fact band reads "Closed 31 Oct 2026 (summer-semester call; next call 30 Apr 2027)". No extension found.

### 42. Sir James McNeill Postgraduate Research Scholarship, Monash — CLOSED for this cycle
- Official Monash page: "Applications closes 31 October each year"; "This prestigious scholarship is awarded in the 31 October scholarship round only." Recurring annual round — the next year's round is a new cycle, not an extension (also offered only once every two years from R4/2024). No extension found. Article has no plain "Deadline" fact row (its "Cycle" fact was flipped to past tense); the deadline block is the dline + alert card, both flipped.

### 43. UBD Graduate Scholarship 2027, Brunei — CLOSED (basis disclosed; parent's own recheck)
- The triage batch's official-page fetch failed and was not retried, so the parent re-fetched it 1 Nov 2026: the official UGRS page loads but is stale — its application-period list runs only to the January 2026 intake and shows no 31 Oct 2026 date. Multiple concordant listings agree the graduate deadline is 31 Oct 2026 for the February 2027 intake (Bright Scholarship: "31st October 2026 for Graduate Degree" and "26th February 2027 for Bachelors"; OpportunityPortal, OnlineCoursely likewise), with no extension found. The corpus article is graduate-only (Master's/PhD, February 2027 intake), so it was flipped to "Closed 31 Oct 2026" with the stale-official-page basis disclosed in the verify note. The bachelor's 26 Feb 2027 date is a different level, not an extension of this item.

### 44. University of Melbourne Human Rights Scholarship 2027 — CLOSED
- Official award page: "Application status, Not open yet, Applications open, 1 Apr 2026, Applications close, 31 Oct 2026"; "Applicants will be notified of the outcome by email in February of the following year." No extension found.

### 45. adidas Internships 2027, Herzogenaurach — CLOSED
- adidas careers posting for the Workplace Management internship: "The application period for this role has been closed. All application statuses will be communicated to applicants directly." No extension or new date shown on the posting. (The corpus article covers several March 2027 cohort roles sharing the 31 Oct 2026 terms; the posting checked is the Workplace Management role.)

### 46. University of Malta Scholarships 2026 — OCTOBER ROUND CLOSED (next round not officially confirmed)
- Official scholarships page fetched copy was stale (crawled 2025-06-17) and contained no deadline date in the excerpt. Corroborating listings agree on recurring rounds: "Applications are accepted three times per year: 31 January, 30 April, and 31 October 2026" (EngineersJob) and "has three deadlines every year – 31 January – 30 April – 31 October" (Bright Scholarship). Guides disagree on the other rounds (31 May vs 30 April), so no next-round date is stated as fact. Article flipped to "Closed 31 Oct 2026 (October round)", registry dpill "Oct round closed", verify note disclosing the listings basis. No extension of the October round found.

### 47. University of Melbourne Graduate Research Scholarships 2027 — ROUND 1 CLOSED (later rounds remain)
- Official award page: "If you are a new student and have applied for a graduate research course by the application closing date for that course, you will be automatically considered" — no single date printed; status "Open for automatic consideration". Official MDHS deadlines page: "Round 1 | 31 October 2026"; "Round 2 | 31 January 2027"; "Round 3 | 15 May 2027". Article flipped to "Closed 31 Oct 2026 (Round 1)" with the verify note stating this is a Round 1 closure, not a blanket closure, and that later rounds exist per the faculty page (check your faculty's round dates). Registry dpill "Round 1 closed". No Round 1 extension found.

### 48. University of Melbourne Research Scholarships (Melbourne Research Scholarship) 2027 — ROUND 1 CLOSED (later rounds remain)
- Same official pages and MDHS round dates as item 47. Article has no plain "Deadline" fact row; the deadline block is the dline + alert card, both flipped to Round 1 closed, and the FAQ "Are there later application rounds?" answer's "treat 31 October 2026 as your real deadline" advice was replaced with "Round 1 closed 31 October 2026". Registry dpill "Round 1 closed". No Round 1 extension found.

### 49. University of Stuttgart Scholarships 2027 — OCTOBER JOINT WINDOW CLOSED (other annual windows exist)
- Listed srcUrl returned 404; the current official financing page (found by search) states: "The joint application dates for all of the mentioned scholarships/financial aids are: January 31, 2026 / June 30, 2026 / October 31, 2026 (if funds are available)". The 31 Jan / 30 Jun windows are separate annual windows, not an extension; a future-cycle 31 Jan date was not separately printed in the excerpt checked. Article flipped to "Closed 31 Oct 2026 (October joint window)", registry dpill "Oct window closed". No October-window extension found.

### 50. Al Qasimi Foundation Internship 2027, UAE — WINTER INTAKE CLOSED; SUMMER INTAKE REMAINS OPEN
- Official internship page: "The program is offered twice a year (Summer Intake and Winter Intake)"; "Deadlines: – Summer Intake: Applications due April 30. – Winter Intake: Applications due October 31." The winter intake deadline (31 Oct 2026) has passed with no extension found; the summer intake (30 Apr 2027) is a separate intake, not an extension, and remains the open route. Article NOT flipped to closed: it now leads with the summer deadline (dline "Deadline 30 Apr 2027", fact "30 April 2027 (summer intake; winter intake closed 31 October 2026)", alert, meta, steps, WhatsApp reminder, JSON-LD 2027-04-30), site-data dl → 2027-04-30, days → 180, closed → false, dlRaw "30 Apr 2027 (summer intake; winter intake closed 31 Oct 2026)", registry dpill "Deadline 30 Apr 2027".

### 51. University of Huddersfield International Scholarships 2026, UK — EARLY PAYMENT DISCOUNT CLOSED; scholarship itself NOT closed
- Official international scholarships page: "There is no specific application process for these scholarships." / "Once you apply to study at the University as an international student, you will automatically be considered"; "Early payment | 31 October 2026" for "January 2027" entry. What ended on 31 Oct 2026 was the GBP 1,000 Early Payment Discount deadline for January 2027 entry, not the automatic merit scholarship — so the article was NOT flipped to "Closed". Instead the discount mentions were moved to past tense throughout (meta, sub/description, fact band, steps, FAQs, alert card), the verify note gained a "Re-checked 1 Nov 2026" addendum stating the discount deadline has passed while the merit discounts remain automatic with no separate deadline, Updated → 1 Nov 2026, site-data dlRaw gained "(now passed)" and verified → "1 Nov 2026" (dl/closed left as they were), registry dpill unchanged ("Automatic · January 2027 entry").

Scope limit (deliberate, as in prior runs): related-card dpill pills inside OTHER articles that link to these 51 were NOT updated (e.g. the "Deadline 31 Oct 2026" cards for NSP PG inside the Ishan Uday article, or for Kalpana inside the Eastman article). The task body names only the homepage dataset / card registry. The linked articles themselves are all flipped, so a reader landing on any of the 51 sees the correct status.

Verification after flipping: every one of the 51 articles re-checked for dline pill, status, Updated 1 Nov 2026 and verify note (all match their category); site-data.json diff vs backup touches only dlRaw/verified/dl/days/closed fields (234 changed lines, no reformatting — indent=1 preserved); articles/index.html embedded JSON checked entry-by-entry against site-data (no mismatches); cards_registry.py compiles and all 50 changed pills verified (Huddersfield pill unchanged by design); site-data states after the run: 46 entries dl 2026-10-31 closed=true (41 fully closed + Malta, Melbourne GRS, Melbourne Research, Stuttgart, Huddersfield), 1 dl 2026-11-15 open (Satya), 1 dl 2027-04-30 open (Al Qasimi), 3 dl null open (Eastman, Oasis ×2). Backups of all 51 pre-flip article files + site-data.json + index.html + cards_registry.py saved under the goal's hidden_files/nov01-backup/.

Final outcome of this run: 47 of the 51 items had their 31 Oct deadline close (41 fully closed for this cycle + 6 where only the 31 Oct round/window/intake/discount closed: Malta October round, Melbourne GRS Round 1, Melbourne Research Round 1, Stuttgart October window, Al Qasimi winter intake, Huddersfield Early Payment Discount); 1 EXTENDED to a new fixed date (Satya Scholarship Program → 15 Nov 2026); 1 moved to no fixed deadline (Eastman PowerUp EduSkill → Always Open); 2 CORRECTED to open with no closing date announced (Oasis Post-Matric OBC and SC/ST, West Bengal — live portal shows 2026-27 applications open with no date). Watch items: Satya's 15 Nov date rests on late-October listings while Buddy4Study's own pages are stale/Always Open — re-check the programme page; Mukhya Mantri Protsahan's undated 31 Dec 2026 listing vs the cycle-specific 31 Oct table (table governs, but a live NSP scheme-page check would remove all doubt); Nirman (Odisha portal fetch failed) and UBD/Malta (stale official pages) verdicts rest on programme pages/listings as disclosed; Sikkim Yasasvi and Sikkim Pre-Matric SC 30 Sep table lines predate the extension to 31 Oct and do not change the closed outcome.

## 2 Nov 2026 — 1 Nov 2026 deadline recheck (16 items re-derived from site-data.json)

Scope note: the task body named 9 items as of 24 Oct 2026, but re-derivation at run time
found 16 entries with closed=false and dl=2026-11-01 — the writer had added CERN, Open Door,
Purdue, UGA, Miami, Victoria Wellington and Wiko. All 16 were checked read-only in the live
browser against their official pages (2 Nov 2026). Outcome: 8 fully closed, 5 still open via a
later round/batch, 3 flagged unverifiable and left unchanged. No deploy zip rebuilt, writer cron
and queue untouched, per the task body. Backups of all 16 pre-flip article files + site-data.json
+ articles/index.html + cards_registry.py saved under the goal's hidden_files/nov02-backup/.

### FULLY CLOSED (8) — article flipped to Closed, site-data closed=true, days=-1, verified 2 Nov 2026
1. Keio University ADB Scholarship 2027 — CLOSED 31 Oct 2026 (not 1 Nov): official ADB page ties
   the ADB route to IGP-Master's Application Period I, and Keio's linked application page gives
   Period I online applications as 1 Oct–31 Oct 2026, 17:00 JST. Period II (1 Feb–31 Mar 2027) is a
   general IGP route, not shown as an ADB route. Corpus 1 Nov date was the published guide date.
2. Malayalee Engineers' Association (MEA) Scholarship 2026 — CLOSED: official meahouston.org page
   still reads "Last date to submit the application is November 1, 2026." No extension shown.
3. Purdue University first-year merit scholarships 2026 — CLOSED for merit: official page,
   "November 1 is the deadline for students to submit a complete application for admission and be
   considered for merit scholarships." Regular Decision admission (15 Jan) remains but is not
   merit-considered.
4. UNIL Master's Scholarship 2027 — CLOSED: official page, "The deadline for submitting
   applications is 1 November 2026" (period 15 Sep–1 Nov 2026). No later cycle date stated.
5. University of Georgia Foundation Fellowship — CLOSED: official Morehead Honors College page,
   "The Foundation Fellowship application deadline is November 1, 2026." No later round stated.
6. University of Miami Stamps Scholarship 2027 — CLOSED (only route): official page — ED I / EA
   applicants are automatically considered; "The University of Miami does not consider students
   who apply Regular Decision for academic scholarships." ED I / EA deadline 1 November.
7. UNU Junior Fellows Internship Spring 2027 — CLOSED for the Spring 2027 round: programme page
   recruits twice a year with vacancies on UNU Careers, and Careers lists no Junior Fellows
   vacancy for Spring 2027. Disclosure: the programme page itself states no 1 Nov date, so the
   corpus 1 Nov date is not re-verified on the official page; a fall cycle exists in structure
   (selection April–May) but no fall deadline is published.
8. Wissenschaftskolleg zu Berlin Fellowships 2027 — CLOSED: official application page, "The
   deadline for applications is 1 November 2026, 23:59 CET" (life and natural sciences
   early-career call). No later date stated.

### ROUND CLOSED / STILL OPEN VIA A LATER ROUND OR BATCH (5) — article NOT flipped to closed
9. University of Dayton Merit Scholarship 2027 — 1 Nov spring-term round closed; next round
   1 May 2027 (fall term): official page, "Applications are due May 1 for the fall term and
   November 1 for the spring term" (page prints no year; dated 2027 as the next fall term in this
   2027 cycle). Merit remains automatic with admission. site-data dl → 2027-05-01, days 180.
10. EPFL Summer Internship 2027 (ERIP) — STILL OPEN to a single later deadline, 30 Nov 2026,
    23:59 CET: official page, "Applications for the ERIP Summer 2027 programme are now open and
    will close on November 30, 2026, at 23:59 (CET)." This replaces the corpus's 1 & 15 Nov batch
    dates — the only item whose deadline moved later than the 1 Nov premise. dl → 2026-11-30.
11. University of Minnesota Global Excellence Scholarships 2027 — Early Action I (1 Nov) closed;
    Early Action II open to 1 Dec 2026: official Twin Cities pages tie scholarship consideration
    to Early Action I/II only. The 1 Jan Regular Deadline is admission-only for this award.
    dl → 2026-12-01, days 29.
12. NPU International Scholarships 2027 — OPEN: 1 Nov 2026 was the batch opening, not a closing
    date. Official page: Batch 1 runs 1 Nov–31 Dec 2026; four batches; final batch 16 Apr–20 May
    2027 (UG) / 1–30 Apr 2027, 17:00 GMT+8 (PG). Caveat carried into the article: majors with full
    enrolment close early. dl → 2026-12-31 (Batch 1 close), days 59.
13. Victoria University of Wellington Scholarships 2027 — doctoral 1 Nov round closed; next
    doctoral round closes 1 Mar 2027: official page, "Closing date 1 March, 1 July, 1 November"
    (4.30 pm on the closing date). UG/PG international scholarships carry no separate deadline.
    dl → 2027-03-01, days 119.

### FLAGGED, LEFT UNCHANGED (3) — no checked_at set, no flip, per the no-guess rule
14. CERN Short Term Internship 2026 — AMBIGUOUS: the SmartRecruiters posting is still live with
    an "I'm interested" button but shows no deadline and no closed/expired notice, so closure
    cannot be confirmed from the official page alone. Article still reads 1 Nov 2026, 23:59 Geneva.
15. Open Door Russian Scholarship 2027 — OFFICIAL PAGE UNREACHABLE: od.globaluni.ru did not
    resolve in the browser, so no extension check was possible on the official site. A partner
    (UrFU) search listing gives "Registration period: August 20 - November 1, 2026" with no
    extension — cited here only, not used to flip the article.
16. Ursinus Gateway International Scholarship 2027 — UNVERIFIED: the Gateway page returns 404
    and no Gateway scholarship or 1 Dec 2026 / 1 Feb 2027 intake dates were found on the current
    official Ursinus site (current page speaks only of general merit awards for international
    applicants). The Dec/Feb intakes must NOT be treated as confirmed open. Article unchanged.

Scope limit (as in the 1 Nov run): related-card dpill pills inside OTHER articles that link to
these items were NOT updated (e.g. the Miami card inside the Purdue article); the homepage
dataset (articles/index.html embedded JSON) and cards_registry.py pills for the 13 changed items
were updated and verified entry-by-entry, and cards_registry.py parses clean. Deploy zip NOT
rebuilt; live upload remains qadir's step, as before.

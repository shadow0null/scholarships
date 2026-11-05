#!/usr/bin/env python3
"""Batch 29c: BI Presidential Scholarship 2027 in Norway (Funded).
The named 2026 cycle (deadline 1 Mar 2026) is closed; the live cycle is 2027
(deadline 1 Mar 2027). Verified against the official BI pages + strong
multi-source agreement. 100% original prose."""
import pathlib, sys, html.parser
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')
CARDS = dict(REGISTRY)

article = {
 'slug': 'bi-presidential-scholarship-2027-norway',
 'title': 'BI Presidential Scholarship 2027 in Norway (Funded)',
 'meta': 'BI Presidential Scholarship 2027 at BI Norwegian Business School: full tuition up to 2 years + NOK 50,000/semester for internationals. Deadline 1 Mar 2027. Eligibility and how to apply.',
 'short': 'BI Presidential Scholarship 2027',
 'kicker': "Norway · Master's · International",
 'mono': 'BI',
 'prov_short': 'BI Norwegian Business School',
 'prov_cat': 'University · Norway',
 'h1': 'BI Presidential Scholarship 2027 in Norway (Funded)',
 'sub': 'Full tuition for up to two years — plus NOK 50,000 a semester for international students — at Norway’s largest business school.',
 'dpill': '1 Mar 2027 · 132 days to go',
 'facts': facts([
   ('Award', 'Full tuition × 2 yrs<small>Internationals: + NOK 50,000/sem</small>'),
   ('Who can apply', 'First-year MSc admits<small>Superior academic record</small>'),
   ('Deadline', '1 March 2027<small>With the MSc application</small>'),
   ('Campuses', 'Oslo or Bergen<small>BI–Luiss joint master excluded</small>'),
   ('Renewal', '30 ECTS/sem + GPA B<small>Progress requirements apply</small>'),
 ]),
 'body': '''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>BI Presidential Scholarship</strong> is the flagship master&rsquo;s award of <strong>BI Norwegian Business School</strong>, Norway&rsquo;s largest business school. It goes to applicants with a <strong>superior academic record</strong> who are admitted to the first year of a <strong>Master of Science programme</strong> at the Oslo or Bergen campus. International applicants receive <strong>full tuition for up to two years plus a living-expense stipend of NOK 50,000 per semester</strong>; applicants who already hold a bachelor&rsquo;s from a Norwegian institution and qualify for L&aring;nekassen loans are treated as domestic and receive full tuition per semester.</p>
      <p>The <strong>2026 cycle</strong> (deadline 1 March 2026) is closed. The <strong>2027 cycle</strong> — the currently open intake — shares the <strong>1 March</strong> deadline and is what this article covers.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Admitted to the <strong>first year</strong> of an MSc programme at BI, campus <strong>Oslo or Bergen</strong> (the BI&ndash;Luiss Joint Master&rsquo;s in Marketing is excluded).</li>
        <li><strong>Superior academic record</strong> — the school&rsquo;s stated standard is a minimum overall GPA of &lsquo;A&rsquo; on the ECTS scale or an equivalent top-level grade.</li>
        <li>Only candidates seeking their <strong>first</strong> graduate/master&rsquo;s degree.</li>
        <li>Open to <strong>Norwegian and international applicants</strong>; students in the third year of BI&rsquo;s Sivil&oslash;konom (Siv&oslash;k) programme are also eligible.</li>
        <li><strong>Renewal:</strong> full study progression (30 ECTS per semester) and a minimum cumulative GPA of &lsquo;B&rsquo; on the BI ECTS scale.</li>
        <li>Recipients should be prepared to act as <strong>BI Ambassadors</strong> for the school.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>International applicants:</strong> full tuition fees for up to two years <strong>plus NOK 50,000 per semester</strong> in living-expense support.</li>
        <li><strong>Norwegian applicants and Norway residents:</strong> full tuition fees for each semester, up to two years.</li>
        <li><strong>Siv&oslash;k applicants:</strong> full tuition fees per semester, up to two years.</li>
        <li>One scholarship per applicant; the award is tied to a specific programme and campus and cannot be transferred.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The Presidential scholarship application is submitted together with the MSc admission application and consists of:</p>
      <ol>
        <li>A <strong>scholarship application letter, maximum one page</strong>, explaining why you deserve the award and how your academic record qualifies you</li>
        <li>A <strong>CV/r&eacute;sum&eacute;</strong> — combined with the letter into <strong>one PDF</strong></li>
        <li>The complete <strong>admission application</strong> with all standard MSc admission documentation</li>
      </ol>
      <p>3rd-year Siv&oslash;k applicants apply by email to info@bi.no with the subject line &ldquo;Master Scholarship Application&rdquo;.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for the MSc programme</strong>Submit your admission application for an eligible MSc through BI&rsquo;s online application portal — the scholarship application is made <strong>at the same time</strong>, via the &lsquo;Scholarship&rsquo; tab in the portal.</li>
        <li><strong>Upload the one-PDF application</strong>Combine your one-page letter and CV into a single PDF and upload it under the &lsquo;Scholarship&rsquo; tab before <strong>1 March 2027</strong>.</li>
        <li><strong>Accept the admission offer</strong>Scholarship decisions are communicated in the spring, most by late April; the award requires you to accept the offer and maintain full study progression.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
    ('Who offers this scholarship?', 'BI Norwegian Business School, Norway — its flagship Presidential award for incoming master&rsquo;s students.'),
    ('Is the 2026 cycle still open?', 'No — the 2026 cycle closed on 1 March 2026. This article covers the live 2027 cycle, which shares the 1 March deadline.'),
    ('What grades do I need?', 'A superior academic record — BI&rsquo;s stated minimum is an &lsquo;A&rsquo; overall on the ECTS scale or an equivalent top grade, and a &lsquo;B&rsquo; cumulative average to keep the award.'),
    ('Does it cover living costs?', 'For international applicants, yes: NOK 50,000 per semester on top of full tuition, subject to academic progression.'),
    ('Do I apply separately?', 'The scholarship application (one-page letter + CV in one PDF) is submitted together with the MSc admission through the portal&rsquo;s &lsquo;Scholarship&rsquo; tab.'),
    ('Is a GMAT/GRE required?', 'Not confirmed on BI&rsquo;s official scholarship pages — do not treat third-party claims of a score requirement as fact.'),
]),
 'verify': 'Verified 20 Oct 2026 via BI&rsquo;s official scholarship pages (bi.edu/bi.no — international award: full tuition ×2 yrs + NOK 50,000/sem; first-degree-only, Oslo/Bergen, renewal terms) + official general scholarships page (March 1 deadline; one-PDF letter+CV via &lsquo;Scholarship&rsquo; tab; late-April decisions) + 6+ agreeing sources (deadline 1 Mar; Siv&oslash;k email route). Third-party-only claims (GMAT/GRE, 20+10 quota) not stated as fact.',
 'dl_long': '1 March 2027',
 'offlinks': [
   ('Official BI Presidential Scholarships page', 'https://www.bi.no/en/programmes-and-individual-courses/scholarships/bi-presidential-scholarships/'),
   ('BI general scholarships / how to apply', 'https://www.bi.edu/programmes-and-individual-courses/scholarships'),
 ],
 'related_titles': ['aixbio', 'daad', 'hanns-seidel'],
}

n = build_article(BASE, OUT, article, CARDS)
t = OUT.joinpath(article['slug'] + '.html').read_text()
p = html.parser.HTMLParser(); p.feed(t)
for bad in ['AICTE Pragati', 'Lorem']:
    assert bad not in t, bad
print('wrote', article['slug'], n, 'bytes; validation OK')

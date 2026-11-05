#!/usr/bin/env python3
"""Batch 29d: Harvard LEAD Fellowship for Promoting Women in Global Health 2027-28.
The named 2026 cycle is closed; the live cycle is 2027-28 (deadline 15 Nov 2026
11:59 PM EST). Verified against the official Harvard Global Health Institute
page + official reviewr microsite. 100% original prose."""
import pathlib, sys, html.parser
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')
CARDS = dict(REGISTRY)

article = {
 'slug': 'harvard-lead-fellowship-2027-28-usa',
 'title': 'Harvard LEAD Fellowship for Promoting Women in Global Health 2027-28 (Fully Funded)',
 'meta': 'Harvard LEAD Fellowship 2027-28 (Harvard Global Health Institute): six-week Cambridge residency fully funded — visa, housing, flights, stipend. Deadline 15 Nov 2026. Eligibility and how to apply.',
 'short': 'Harvard LEAD Fellowship 2027-28',
 'kicker': 'USA · Fellowship · Global Health',
 'mono': 'H',
 'prov_short': 'Harvard Global Health Institute',
 'prov_cat': 'Fellowship · USA',
 'h1': 'Harvard LEAD Fellowship for Promoting Women in Global Health 2027-28 (Fully Funded)',
 'sub': 'Visa, housing, flights and a living stipend for a six-week residency in Cambridge — for global-health leaders, running September 2027 to August 2028.',
 'dpill': '15 Nov 2026 · 26 days to go',
 'facts': facts([
   ('Award', 'Residency fully covered<small>Visa + housing + flights + stipend</small>'),
   ('Residency', '6 weeks, Apr 2028<small>Cambridge, MA · in person</small>'),
   ('Who can apply', 'Global-health professionals<small>Master&rsquo;s + 10 yrs exp.; J-1 eligible</small>'),
   ('Deadline', '15 Nov 2026<small>11:59 PM EST</small>'),
   ('Fellowship year', 'Sep 2027 – Aug 2028<small>Virtual curriculum + residency</small>'),
 ]),
 'body': '''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Harvard LEAD Fellowship for Promoting Women in Global Health</strong> is offered by the <strong>Harvard Global Health Institute (HGHI)</strong> together with the Department of Global Health and Population at the <strong>Harvard T.H. Chan School of Public Health</strong>. It is designed for individuals from <strong>low- and middle-income countries</strong> who are building leadership careers in global health — applicants of all genders, disciplines and regions may apply.</p>
      <p>The fellowship year runs <strong>1 September 2027 – 31 August 2028</strong>, combining a virtual curriculum with a <strong>six-week in-person residency in Cambridge, Massachusetts, in April 2028</strong>. The residency component is fully funded: visa fees, housing and flights are covered, and fellows receive a <strong>living stipend</strong> for their time in the United States.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Master&rsquo;s degree or higher</strong> in a relevant field.</li>
        <li>Work <strong>full-time in global health</strong>, with <strong>at least 10 years</strong> of professional experience beyond education (work done while a student does not count).</li>
        <li>Substantial leadership experience and demonstrated further leadership potential.</li>
        <li>Able to <strong>take a leave of absence (or equivalent)</strong> for the six-week April 2028 residency.</li>
        <li>Eligible for a <strong>US J-1 visa</strong> and available to live in Cambridge, MA for the six weeks.</li>
        <li>Have <strong>not</strong> participated in any full-time fellowship lasting four months or longer in the two years prior.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Visa fees covered</strong> for the US stay.</li>
        <li><strong>Housing in Cambridge</strong> for the six-week residency.</li>
        <li><strong>Flights</strong> to and from the United States.</li>
        <li><strong>Living stipend</strong> for the residency period.</li>
        <li>A year of virtual leadership curriculum alongside a cohort of global-health fellows, plus the HGHI network.</li>
      </ul>
      <p>Note: the award funds the <strong>residency component</strong> — the virtual fellowship year is not a salaried position.</p>
      <h2 id="documents">Documents required</h2>
      <p>The official HGHI announcement page does not publish a full document checklist. A third-party listing mentions a <strong>CV/resume</strong> and a <strong>letter of intent of max. 1.5 pages</strong> describing the applicant&rsquo;s global-health journey and what the fellowship would change for them — this list is <strong>not confirmed</strong> on the official page, so verify the requirements inside the official application portal before submitting.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the official announcement page</strong>Confirm the current 2027-28 cycle and follow its link to the Harvard LEAD Fellowship application microsite (hosted on the reviewr platform).</li>
        <li><strong>Create an account and submit</strong>Complete the application and upload all materials before <strong>15 November 2026, 11:59 PM EST</strong>.</li>
        <li><strong>Watch for spring 2027 notifications</strong>Selection results are communicated in spring 2027; questions go to hghi_fellowships@harvard.edu.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
    ('Who runs this fellowship?', 'The Harvard Global Health Institute, in collaboration with the Department of Global Health and Population at the Harvard T.H. Chan School of Public Health.'),
    ('Is it open to men?', 'Yes — applicants of all genders, regions and disciplines may apply; the programme is designed for leaders from low- and middle-income countries.'),
    ('What is covered?', 'Visa fees, housing, flights and a living stipend for the six-week Cambridge residency in April 2028. The virtual fellowship year is not salaried.'),
    ('How much experience is needed?', 'At least 10 years of full-time professional experience in global health beyond education, plus a master&rsquo;s degree and demonstrable leadership.'),
    ('Is the 2026 cycle still open?', 'No — the 2026–27 application page shows the cycle closed. This article covers the live 2027–28 cycle, deadline 15 November 2026.'),
]),
 'verify': 'Verified 20 Oct 2026 via the official Harvard Global Health Institute announcement page (2027-28 cycle; 15 Nov 2026 11:59 PM EST deadline; Sep 2027–Aug 2028; six-week Apr 2028 Cambridge residency; eligibility incl. master&rsquo;s + 10 yrs, J-1, leave of absence) + the official reviewr application microsite + HGHI programme wording on funding. Document list per OpportunityDesk (third-party) is flagged as unconfirmed.',
 'dl_long': '15 November 2026, 11:59 PM EST',
 'offlinks': [
   ('Official HGHI announcement page', 'https://globalhealth.harvard.edu/2027-2028-harvard-lead-fellowship-application-is-now-open/'),
 ],
 'related_titles': ['yale-wf', 'awc', 'stjohns-pharma'],
}

n = build_article(BASE, OUT, article, CARDS)
t = OUT.joinpath(article['slug'] + '.html').read_text()
p = html.parser.HTMLParser(); p.feed(t)
for bad in ['AICTE Pragati', 'Lorem']:
    assert bad not in t, bad
print('wrote', article['slug'], n, 'bytes; validation OK')

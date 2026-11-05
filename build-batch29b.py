#!/usr/bin/env python3
"""Batch 29b: New York Times Fellowship 2027-28 (Paid) + Concordia College Talent Scholarships.
Both verified against official sources (see verification reports). 100% original prose."""
import pathlib, sys, html.parser
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')
CARDS = dict(REGISTRY)

nyt = {
 'slug': 'new-york-times-fellowship-2027-28-usa',
 'title': 'New York Times Fellowship 2027-28 in USA (Paid)',
 'meta': 'New York Times Fellowship 2027-28: one paid year in the newsroom or Opinion. Deadline 20 Nov 2026 5pm ET. Eligibility, tracks, pay and how to apply.',
 'short': 'New York Times Fellowship 2027-28',
 'kicker': 'USA · Fellowship · Journalism',
 'mono': 'NYT',
 'prov_short': 'The New York Times Company',
 'prov_cat': 'Fellowship · USA',
 'h1': 'New York Times Fellowship 2027-28 in USA (Paid)',
 'sub': 'One paid year in the newsroom or Opinion — reporting, visuals, audience and AI tracks, running June 2027 to May 2028.',
 'dpill': '20 Nov 2026 · 31 days to go',
 'facts': facts([
   ('Pay', 'Paid full-time role<small>Benefits; Guild-represented</small>'),
   ('Duration', '1 year<small>7 Jun 2027 – 26 May 2028</small>'),
   ('Who can apply', 'Journalists ≤5 yrs exp.<small>Authorised to work in the US</small>'),
   ('Deadline', '20 Nov 2026<small>5 p.m. Eastern</small>'),
   ('Tracks', 'Reporting / Visual / Audience / AI<small>Newsroom or Opinion</small>'),
 ]),
 'body': '''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>New York Times Fellowship</strong> is a <strong>one-year, full-time fellowship</strong> run by the Newsroom Career Programs team of <strong>The New York Times Company</strong>. Fellows work in the <strong>newsroom or the Opinion section</strong> on tracks including reporting, visual journalism, audience, election data analytics and AI initiatives. The <strong>2027-28 cohort</strong> (applications now open) runs from <strong>7 June 2027 to 26 May 2028</strong>; around 30 fellows join each year.</p>
      <p>This is a paid fellowship: fellows work full time, are paid, and receive benefits as Guild-represented employees. The company does not provide housing or relocation support.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>No more than five years of professional journalism experience</strong> beyond campus media or internships.</li>
        <li>Some <strong>newsroom or equivalent experience</strong>, and a strong commitment to journalistic independence.</li>
        <li>Must be <strong>authorised to work in the United States</strong> at the time of application and for the whole programme; the Times does not sponsor new visas.</li>
        <li>Only <strong>one fellowship application per person per cycle</strong> — pick the single track that fits best.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full-time paid position</strong> with benefits, as a Guild-represented employee of the company.</li>
        <li>A year of real newsroom work — fellows are embedded in desks and work on live assignments, not side projects.</li>
        <li>Structured professional development through the Newsroom Career Programs team.</li>
      </ul>
      <p><strong>Exact salary not published:</strong> the official pages confirm fellows are paid with benefits, but the company does not publish a figure. Aggregator salary claims are not confirmed by the Times.</p>
      <h2 id="documents">Documents required</h2>
      <p>The official fellowship pages ask applicants to "submit their materials" and define requirements per track on the official posting. Third-party listings commonly mention a resume, a tailored cover letter and published work samples — but this list is <strong>not confirmed</strong> by the Times, so check the requirements on the official posting for your chosen track before applying.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose one track</strong>On the official fellowship page, compare the tracks (reporting, visual journalism, audience, AI initiatives, election data analytics) and pick the single one you will apply for.</li>
        <li><strong>Apply through the official careers site</strong>Submit via nytco.com/careers/job-listings (mirrored on the company's Greenhouse job board) by <strong>20 November 2026, 5 p.m. Eastern</strong>. Applications by mail or email are not accepted.</li>
        <li><strong>Confirm work authorisation</strong>Make sure your US work authorisation covers the application date and the whole programme, since the Times will not sponsor new visas.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
    ('Who runs this fellowship?', 'The New York Times Company itself, through its Newsroom Career Programs team — it is the official one-year fellowship of the newsroom.'),
    ('When is the deadline?', '20 November 2026 at 5 p.m. Eastern for the 2027-28 cohort. The previous cycle (2026-27) closed on 19 November 2025.'),
    ('Is it paid?', 'Yes — fellows work full time, are paid, and receive benefits. The exact salary figure is not published by the company.'),
    ('Can international journalists apply?', 'Only if you are already authorised to work in the United States when you apply and for the full programme; new visas are not sponsored.'),
    ('Can I apply to more than one track?', 'No — the Times allows one fellowship application per person per cycle.'),
]),
 'verify': 'Verified 20 Oct 2026 via the official NYT fellowship page (nytco.com — 20 Nov 2026 5pm ET deadline, paid, US work authorisation, one application per cycle) + official NYT press releases for the 2026-27 and 2027-28 cycles + Extern/careeroppotunities FAQ (Guild benefits, tracks). Salary figures from aggregators and per-cycle London positions were not confirmed and are not stated as fact.',
 'dl_long': '20 November 2026, 5 p.m. Eastern',
 'offlinks': [
   ('Official fellowship page (nytco.com)', 'https://www.nytco.com/careers/early-career-opportunities/newsroom-fellowship/'),
   ('Applications announcement (nytco.com)', 'https://www.nytco.com/press/newsroom-fellowship-applications/'),
 ],
 'related_titles': ['yale-wf', 'awc', 'stjohns-pharma'],
}

conc = {
 'slug': 'concordia-college-talent-scholarships-usa',
 'title': 'Concordia College Talent Scholarships: Theatre, Music, Visual Arts and Speech Awards in the USA',
 'meta': 'Concordia College (Moorhead, Minnesota) Talent Scholarships: awards in music, theatre, visual arts, speech & debate. Feb. 1 deadline. Eligibility and how to apply.',
 'short': 'Concordia College Talent Scholarships',
 'kicker': 'USA · Undergraduate · Arts',
 'mono': 'CC',
 'prov_short': 'Concordia College',
 'prov_cat': 'College · USA',
 'h1': 'Concordia College Talent Scholarships: Theatre, Music, Visual Arts and Speech Awards in the USA',
 'sub': 'Talent-based awards in music, theatre, visual arts, and speech & debate for admitted Concordia students — separate application, Feb. 1 deadline.',
 'dpill': '1 Feb 2027 · 104 days to go',
 'facts': facts([
   ('Award', 'Range in value<small>Theatre/speech: $1,000–5,000/yr</small>'),
   ('Who can apply', 'Incoming first-year & transfer<small>Talent in arts or debate</small>'),
   ('Deadline', '1 Feb 2027<small>Separate application per discipline</small>'),
   ('Stackable', 'Yes, with academic awards<small>Theatre/speech; excl. Presidential</small>'),
   ('College', 'Moorhead, Minnesota<small>Private liberal arts, est. 1891</small>'),
 ]),
 'body': '''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Concordia College</strong> — a private liberal-arts college in Moorhead, Minnesota, USA — awards <strong>Talent Scholarships</strong> to admitted students who demonstrate talent in <strong>Music, Theatre, Visual Arts, or Speech and Debate</strong>. The awards are made through the academic departments rather than the general financial-aid process, and they require a <strong>separate application</strong> for the chosen discipline. The official name of the scheme is "Talent Scholarships"; the college states the awards <strong>range in value</strong> rather than publishing one flat figure.</p>
      <p>Note: third-party aggregators quote "$33,000/year" and a "15 January 2026" deadline — <strong>both are contradicted by the college's official pages</strong> and must be ignored. The official deadline is <strong>Feb. 1</strong>, and the official departmental figures are $1,000–$5,000 a year (see below).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Incoming first-year and transfer students</strong> who have been <strong>admitted to Concordia College</strong>.</li>
        <li>Demonstrated talent in one of four areas: <strong>Music, Theatre, Visual Arts, or Speech and Debate</strong>.</li>
        <li>Recipients must take part in department events and programmes as the department determines.</li>
        <li>Recipients do <strong>not</strong> need to major in the talent field (explicitly stated for theatre).</li>
        <li>No specific GPA or SAT/ACT threshold is published on the official page for talent awards — claims of a minimum score are not confirmed.</li>
        <li>International students are told "performance scholarships based on talents in various fields" are available to them as well.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Talent Scholarships <strong>range in value</strong> — no single published amount on the official main page.</li>
        <li><strong>Theatre:</strong> $1,000–$5,000 per year, stackable with academic scholarships; early-application due date Nov. 6, final deadline Feb. 1.</li>
        <li><strong>Speech and Debate:</strong> $1,000–$5,000 per year, stackable with academic scholarships (excluding the Presidential scholarship).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The college requires a <strong>separate application</strong> for the chosen discipline, and in some cases <strong>performance submissions</strong> — music auditions, portfolios, or speech recordings, depending on the department. A full itemised document list is not published on the official scholarships page.</p>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply and get admitted to Concordia College</strong>The admission application itself is free; only admitted students can receive a talent award.</li>
        <li><strong>Complete the separate Talent Scholarship application</strong>For your discipline (Music, Theatre, Visual Arts, or Speech and Debate), via the department's scholarship application page — including audition recordings or portfolios where required — by the <strong>Feb. 1 deadline</strong>.</li>
        <li><strong>Watch for finalist screening</strong>Theatre finalists may be invited for on-campus interviews; speech &amp; debate finalists submit a 3–5 minute recording and interview.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
    ('Which college is this?', 'Concordia College in Moorhead, Minnesota — the private liberal-arts college founded in 1891, not Concordia University.'),
    ('Is it really $33,000 a year?', 'No. That figure comes from an aggregator mix-up with Concordia\'s international-student cost-of-attendance range. The college says talent awards "range in value"; theatre and speech & debate awards are officially $1,000–$5,000 a year.'),
    ('When is the deadline?', 'Feb. 1 on the official pages — not 15 January as aggregators claim.'),
    ('Do I need to major in the talent subject?', 'No — for theatre the college explicitly says recipients need not major in the field.'),
    ('Can international students get it?', 'The official international-students aid page says performance/talent scholarships are available to international students too.'),
]),
 'verify': 'Verified 20 Oct 2026 via concordiacollege.edu (official scholarships page — "range in value", Feb. 1 deadline, separate applications; theatre page $1,000–$5,000 stackable; speech & debate page $1,000–$5,000 stackable excl. Presidential; international-students page). Aggregator claims of $33,000/year and a 15 Jan 2026 deadline are contradicted by the official site and were not used.',
 'dl_long': '1 February 2027 (Talent Scholarship application deadline)',
 'offlinks': [
   ('Official Concordia scholarships page', 'https://www.concordiacollege.edu/tuition-aid/concordia-scholarships/'),
 ],
 'related_titles': ['dayton-merit', 'uchicago', 'msu-oos'],
}

for article, key, card in [
    (nyt, 'nyt-fellowship', {'mono': 'NYT', 'title': nyt['title'], 'href': nyt['slug'] + '.html',
      'dpill': nyt['dpill'], 'award': 'Paid full-time fellowship + benefits',
      'elig': 'Journalists ≤5 yrs experience; authorised to work in the US.',
      'tags': [('Fellowship', 'blue'), ('USA', 'teal')]}),
    (conc, 'concordia-talent', {'mono': 'CC', 'title': conc['title'], 'href': conc['slug'] + '.html',
      'dpill': conc['dpill'], 'award': 'Range in value; theatre/speech $1,000–5,000/yr',
      'elig': 'Incoming first-year & transfer; talent in arts/debate.',
      'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]}),
]:
    cards = dict(REGISTRY)
    cards.update({key: card, 'georg-arnhold-2028': {
        'mono': 'GA', 'title': 'Georg Arnhold Senior Fellowship 2028 in Germany (Fully Funded)',
        'href': 'georg-arnhold-senior-fellowship-2028-germany.html',
        'dpill': '2 Nov 2026 · 13 days to go', 'award': '€3,300/month × 6 months + airfare',
        'elig': 'PhD scholars or peace-education practitioners; all nationalities.',
        'tags': [('Fellowship', 'blue'), ('Germany', 'teal')]}})
    n = build_article(BASE, OUT, article, cards)
    t = OUT.joinpath(article['slug'] + '.html').read_text()
    hp = html.parser.HTMLParser(); hp.feed(t)
    for bad in ['AICTE Pragati', 'Lorem']:
        assert bad not in t, bad
    assert 'AICTE Pragati' not in t
    print('wrote', article['slug'], n, 'bytes; validation OK')

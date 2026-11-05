#!/usr/bin/env python3
"""Batch 29a: Georg Arnhold Senior Fellowship 2028 in Germany (Fully Funded).
Verified against the official GEI call-for-applications PDF + corroborating
listings (deadline 2 Nov 2026 for the 2028 fellowship)."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

DL = '2 Nov 2026'

article = {
 'slug': 'georg-arnhold-senior-fellowship-2028-germany',
 'title': 'Georg Arnhold Senior Fellowship 2028 in Germany (Fully Funded)',
 'meta': 'Georg Arnhold Senior Fellowship 2028 at the Georg Eckert Institute, Germany: €3,300/month for six months, return airfare, deadline 2 Nov 2026. Eligibility, documents and how to apply.',
 'short': 'Georg Arnhold Senior Fellowship 2028',
 'kicker': 'Germany · Fellowship · International',
 'mono': 'GA',
 'prov_short': 'Georg Arnhold Program',
 'prov_cat': 'Fellowship · Germany',
 'h1': 'Georg Arnhold Senior Fellowship 2028 in Germany (Fully Funded)',
 'sub': '€3,300 a month for six months in Brunswick — for scholars and practitioners working on education for sustainable peace.',
 'dpill': f'{DL} · 13 days to go',
 'facts': facts([
   ('Award', '€3,300 / month<small>× 6 months + return airfare</small>'),
   ('Fellowship', 'Jan 2028 onwards<small>At the GEI, Brunswick</small>'),
   ('Who can apply', 'PhD scholars or practitioners<small>Peace education; all nationalities</small>'),
   ('Deadline', f'{DL}<small>No time cutoff published</small>'),
   ('Working language', 'English<small>At the Georg Eckert Institute</small>'),
 ]),
 'body': '''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Georg Arnhold Senior Fellowship</strong> is awarded by the <strong>Georg Arnhold Program</strong> at the <strong>Leibniz Institute for Educational Media | Georg Eckert Institute (GEI)</strong> in Brunswick, Germany. Each year it brings one <strong>Senior Fellow of Education for Sustainable Peace</strong> to the institute for a residency of <strong>six months</strong> (a shorter stay of at least three months can be arranged in exceptional cases). The <strong>2028 fellowship</strong> is the currently open cycle, with a fellowship start of January 2028 at the earliest.</p>
      <p>Fellows pursue a project on <strong>education for sustainable peace</strong>, with a particular emphasis on <strong>educational media and school curricula at the secondary-school level</strong> — from any region of the world. The programme explicitly welcomes both scholars and practitioners, including "pracademics" who combine research excellence with hands-on work at the grassroots.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>All nationalities</strong> are eligible; English is the working language.</li>
        <li><strong>Scholars:</strong> outstanding researchers in the humanities, political and social sciences, or education, holding a <strong>PhD</strong>, with a project firmly located in peace education.</li>
        <li><strong>Practitioners:</strong> distinguished peace-education practitioners with high-level international experience (for example in NGO management), demonstrating <strong>at least five years</strong> of advanced professional achievement.</li>
        <li>The project must focus on <strong>education for sustainable peace</strong>, particularly secondary-level educational media and curricula.</li>
        <li>Fellows must spend the fellowship period <strong>in residence at the GEI in Brunswick</strong>, take part in the institute's daily working life, co-design the annual Georg Arnhold Program conference with the coordinator, present at the GEI research colloquium, and <strong>publish the project outcomes within one year</strong> of the fellowship ending.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend of €3,300</strong> for six months (minimum three months in exceptional cases).</li>
        <li><strong>Return economy airfare</strong> to Germany.</li>
        <li>Use of the GEI's international library of educational media — textbooks, curricula and digital resources.</li>
        <li>Mentoring and discussions with GEI experts; opportunity to present at the GEI research colloquium.</li>
        <li>Access to "The Basement", the GEI's experimental digital media lab for games learning, VR, robotics and creative pedagogies.</li>
        <li>Administrative and publication support from the programme coordinators; open-access publication fees for direct project outputs covered where possible.</li>
        <li>A broad network of scholars and practitioners working in peace education.</li>
      </ul>
      <p><strong>Not covered:</strong> passport and visa costs, and health and liability insurance, remain the fellow's own responsibility.</p>
      <h2 id="documents">Documents required</h2>
      <p><strong>Stage 1 — everyone applies online:</strong> the online application form with project descriptions answering the guiding questions (objectives, research gap, methodological and theoretical framework, expected outcomes). Applicants are asked to consult the programme's AI-use policy before drafting.</p>
      <p><strong>Stage 2 — only the three shortlisted candidates</strong> are invited to submit by email:</p>
      <ol>
        <li>Short CV</li>
        <li>List of publications</li>
        <li>Detailed project proposal of <strong>max. 25 pages</strong>, including references and evidence of impact in peace education (cited publications, project websites, success stories)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the official call for applications</strong>Confirm the current cycle and the AI-use policy on the Georg Arnhold Program page of the GEI website.</li>
        <li><strong>Submit the online application form</strong>Complete it with your project descriptions before <strong>2 November 2026</strong> — the official call states no submission time or time zone, so do not leave it to the last minute.</li>
        <li><strong>Wait for shortlisting</strong>Up to 10 applications go forward to multi-stage pre-selection at the GEI; the top 3 candidates then submit the full Stage 2 proposal and attend an online interview with the Academic Advisory Board.</li>
        <li><strong>One fellow is selected</strong>Questions can be directed to Katharina Baier, Georg Arnhold Program, arnhold@gei.de.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
    ('Who is the provider?', 'The Georg Arnhold Program at the Leibniz Institute for Educational Media | Georg Eckert Institute (GEI), Brunswick, Germany — not a university admissions scheme.'),
    ('What is the exact deadline?', '2 November 2026 for the 2028 fellowship. The official call does not publish a submission time or time zone.'),
    ('Do I need a PhD?', 'Scholarly applicants must hold a PhD; practitioners are assessed on at least five years of advanced professional achievement in peace education instead.'),
    ('Do I have to live in Germany during the fellowship?', 'Yes — fellows spend the fellowship period in residence at the GEI in Brunswick and take part in its working life.'),
    ('Is the fellowship fully funded?', 'The stipend (€3,300/month), return economy airfare and research support are covered; passport, visa, health and liability insurance are your own responsibility.'),
]),
 'verify': 'Verified 20 Oct 2026 via the official GEI call-for-applications PDF (2 Nov 2026 deadline; €3,300/month × 6 months; return airfare; eligibility and two-stage selection) + fundsforngos.org and opportunitiesforyouth.org (deadline corroboration). The stale "2026" aggregator listings were disregarded: the live cycle is the 2028 fellowship.',
 'dl_long': '2 November 2026',
 'offlinks': [
   ('Official call for applications (GEI, PDF)', 'https://www.gei.de/fileadmin/gei.de/pdf/institut/stipendien_stipendiaten/Georg-Arnhold-Programm/Call_for_Applications_-_Georg_Arnhold_Senior_Fellow_2028__ENG-long_.pdf'),
 ],
 'related_titles': ['hanns-seidel', 'daad', 'ieg-mainz'],
}

cards = dict(REGISTRY)
cards.update({
 'georg-arnhold-2028': {'mono': 'GA', 'title': article['title'], 'href': article['slug'] + '.html',
                        'dpill': article['dpill'], 'award': '€3,300/month × 6 months + airfare',
                        'elig': 'PhD scholars or peace-education practitioners; all nationalities.',
                        'tags': [('Fellowship', 'blue'), ('Germany', 'teal')]},
})
n = build_article(BASE, OUT, article, cards)
print('wrote', article['slug'], n, 'bytes')

# validate HTML parses + no leftover template text
# ('#' bare hrefs are pre-postprocess state — postprocess converts the dead
# 'Remind me' button into a working WhatsApp CTA)
import html.parser
class P(html.parser.HTMLParser):
    def error(self, m): raise Exception(m)
t = OUT.joinpath(article['slug'] + '.html').read_text()
P().feed(t)
for bad in ['AICTE Pragati', 'Lorem']:
    assert bad not in t, bad
print('validation OK')

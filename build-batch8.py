#!/usr/bin/env python3
"""Batch 8: 5 verified articles. Verified 16 Oct 2026."""
import pathlib, sys, json
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'epfl-summer': dict(mono='EPFL', title='EPFL Summer Internship 2027 (Fully Funded)', href='epfl-summer-internship-2027.html',
              dpill='30 days to go', award='CHF 1,800–3,600/month', elig='Bachelor’s/Master’s; 2nd year completed; no PhD; all nationalities.',
              tags=[('Internship','blue'),('International','teal')]),
 'sage-it': dict(mono='S', title='Sage IT India Scholarship 2026', href='sage-it-india-scholarship-2026.html',
              dpill='30 days to go', award='Rs 50,000 one-time', elig='Indian students 17–30; article on AI-first world; unpublished.',
              tags=[('Contest','blue'),('Private','teal')]),
 'zonta-ae': dict(mono='Z', title='Zonta Amelia Earhart Fellowship 2026', href='zonta-amelia-earhart-fellowship-2026.html',
              dpill='30 days to go', award='US$10,000', elig='Women; PhD in aerospace/space sciences; any nationality.',
              tags=[('Women','blue'),('PhD','teal')]),
 'wb-gaf': dict(mono='WB', title='World Bank Government Analytics Fellowship 2027', href='world-bank-government-analytics-fellowship-2027.html',
              dpill='31 days to go', award='Fully funded (in-person)', elig='Central-govt officials; nominated; quantitative coursework.',
              tags=[('Fellowship','blue'),('Professionals','teal')]),
 'dakshana': dict(mono='D', title='Dakshana Scholarship (JDST) 2027', href='dakshana-scholarship-jdst-2027.html',
              dpill='45 days to go', award='Free 1-yr residential coaching', elig='Class 12 science, govt/aided schools; income < Rs 3L.',
              tags=[('Coaching','blue'),('Merit','teal')]),
}

ARTICLES = [
dict(
 slug='epfl-summer-internship-2027',
 title='EPFL Summer Internship 2027 in Switzerland (Fully Funded) | StudyDesk Scholarships',
 meta='EPFL Summer Internship 2027: CHF 3,600/month (Life Sciences) or CHF 1,800/month (Engineering). Deadlines 1 & 15 Nov 2026. Eligibility and how to apply.',
 short='EPFL Summer Internship 2027', kicker='Switzerland · Internship',
 mono='EPFL', prov_short='EPFL', prov_long='École polytechnique fédérale de Lausanne',
 h1='EPFL Summer Internship 2027 in Switzerland (Fully Funded)',
 sub='CHF 1,800 to CHF 3,600 a month — do real research in an EPFL lab next summer.',
 dpill='30 days to go', dl_long='1 & 15 Nov 2026',
 facts=facts([('Award','CHF 1,800 – 3,600 / month<small>By track + travel support</small>'),
              ('Who can apply','Bachelor’s/Master’s students<small>2nd year done; no PhD</small>'),
              ('Duration','2–3 months<small>Summer 2027</small>'),
              ('Deadlines','1 Nov (Eng) · 15 Nov (Life Sci)<small>2026</small>'),
              ('Open to','All nationalities<small>No nationality restriction</small>')]),
 body='''
      <h2 id="about">About the internship</h2>
      <p>The <strong>EPFL Summer Internship 2027</strong> places undergraduate and Master's students in research laboratories at the <strong>École polytechnique fédérale de Lausanne</strong> — one of Europe's top technical universities. There are two main international tracks: the <strong>Life Sciences Summer Research Program</strong> and the <strong>Engineering/Science/Technology track</strong> (Summer@EPFL / E3). Both are fully funded.</p>
      <h2 id="tracks">The two tracks</h2>
      <table><tr><th></th><th>Life Sciences</th><th>Engineering/Science/Tech</th></tr>
      <tr><td>Duration</td><td>2 months (5 Jul – 27 Aug 2027)</td><td>8–12 weeks</td></tr>
      <tr><td>Allowance</td><td><strong>CHF 3,600/month</strong></td><td><strong>CHF 1,800/month</strong></td></tr>
      <tr><td>Travel</td><td>Mostly covered (up to CHF 1,000 overseas)</td><td>Reimbursed</td></tr>
      <tr><td>Seats</td><td>~25</td><td>Varies</td></tr>
      <tr><td><strong>Deadline</strong></td><td><strong>15 Nov 2026</strong></td><td><strong>1 Nov 2026</strong></td></tr></table>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled in a <strong>Bachelor's or Master's</strong> programme (relevant field).</li>
        <li>Completed at least the <strong>second Bachelor year</strong> by application time.</li>
        <li><strong>PhD students are not eligible.</strong></li>
        <li><strong>All nationalities</strong> can apply.</li>
        <li>Strong academics — Life Sciences typically expects top-5% standing.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>CV</li><li>Motivation letter</li><li>Official transcripts</li>
        <li>Contact details of two references</li><li>Passport scan</li>
        <li>Choice of three EPFL laboratories</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the EPFL research internships page</strong>epfl.ch — pick your track.</li>
        <li><strong>Prepare documents</strong>CV, motivation letter, transcripts, references.</li>
        <li><strong>Complete the online application in one sitting</strong>It cannot be saved midway.</li>
        <li><strong>Submit before the track deadline</strong>1 Nov (Engineering) / 15 Nov 2026 (Life Sciences).</li>
      </ol>
      <div class="honest-note"><strong>EPFL students have a separate track:</strong> "Summer in the Lab" (CHF 4,000, deadline 30 Nov 2026) is only for EPFL Bachelor students — don't confuse it with the international tracks above.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can PhD students apply?","No — both international tracks exclude PhD students."),
 ("Is it fully funded?","Yes — monthly allowance plus travel coverage on both tracks."),
 ("How competitive is it?","Very — the Life Sciences track takes about 25 students from worldwide applicants."),
 ("Do I need to be nominated?","Not for these tracks — direct application. (Nomination applies to the separate Excellence Research Internship Program.)"),
]),
 verify='Verified 16 Oct 2026 via ScholarPositions (track deadlines 1/15 Nov 2026; CHF 3,600/1,800; 2nd-year requirement; no PhD), Pathfinderly (Life Sciences details), Bright Scholarship (Life Sciences 5 Jul–27 Aug 2027, 25 seats), and the official EPFL eligibility page.',
 offlinks=[('EPFL research internships (official)','https://www.epfl.ch/education/international/en/coming-to-epfl/research-internships/eligibility-and-application/')],
 related_titles=['nasa-hubble','bloomberg-harvard','swiss-phd'],
),

dict(
 slug='sage-it-india-scholarship-2026',
 title='Sage IT India Scholarship 2026 | StudyDesk Scholarships',
 meta='Sage IT India Scholarship 2026: Rs 50,000 one-time for an article on thriving in an AI-first world. Eligibility, deadline 15 Nov 2026.',
 short='Sage IT India Scholarship', kicker='Private · Article Contest',
 mono='S', prov_short='Sage IT Inc.', prov_long='Sage IT Inc.',
 h1='Sage IT India Scholarship 2026',
 sub='Rs 50,000 for the best article on thriving in an AI-first world — write, don’t just study.',
 dpill='30 days to go', dl_long='15 Nov 2026',
 facts=facts([('Award','Rs 50,000 one-time<small>Paid to the institution</small>'),
              ('Who can apply','Indian students 17–30<small>Enrolled in a recognised institution</small>'),
              ('Task','Unpublished article<small>“Thriving in an AI-first world”</small>'),
              ('Deadline','15 Nov 2026<small>Online application</small>'),
              ('Mode','Contest<small>Article-writing</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Sage IT India Scholarship 2026</strong>, offered by <strong>Sage IT Inc.</strong>, is an <strong>article-writing contest</strong>: Indian students submit an original, unpublished article on <strong>what it means to thrive in an AI-first world</strong>. The winner receives <strong>Rs 50,000 (one-time), paid directly to the institution</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Indian student</strong> between <strong>17 and 30 years</strong>.</li>
        <li>Enrolled in a <strong>recognised Indian institution</strong>.</li>
        <li>Submit an <strong>original article not published anywhere else</strong> on the given theme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Rs 50,000 one-time</strong> scholarship.</li>
        <li>Paid <strong>directly to the institution</strong>, not the student.</li>
      </ul>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Write your article</strong>Original, unpublished, on thriving in an AI-first world.</li>
        <li><strong>Go to the Sage IT scholarship page</strong>sageitinc.com/scholarship/india</li>
        <li><strong>Submit online before 15 November 2026</strong></li>
      </ol>
      <div class="honest-note"><strong>Competition, not entitlement:</strong> this is judged on the article — read the official guidelines carefully before submitting.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("What is the topic?","What it means to thrive in an AI-first world — the article must not have been published before."),
 ("Who gets the money?","The Rs 50,000 is paid directly to the winner's institution."),
 ("What is the age limit?","17 to 30 years."),
 ("When is the deadline?","15 November 2026."),
]),
 verify='Verified 16 Oct 2026 via The Hindu Scholarships column (20 Jun 2026: Sage IT Inc; 17–30 years; recognised Indian institution; unpublished article on AI-first world; Rs 50,000 to institution; 15 Nov deadline) and the Unstop/Sage IT official page.',
 offlinks=[('Sage IT India scholarship (official)','https://sageitinc.com/scholarship/india')],
 related_titles=['sakal-cds','super50-aayam','isi-stipend'],
),

dict(
 slug='zonta-amelia-earhart-fellowship-2026',
 title='Zonta Amelia Earhart Fellowship 2026 | StudyDesk Scholarships',
 meta='Zonta Amelia Earhart Fellowship 2026: US$10,000 for women pursuing PhD in aerospace engineering and space sciences. Deadline 15 Nov 2026.',
 short='Amelia Earhart Fellowship', kicker='Women · PhD · International',
 mono='Z', prov_short='Zonta International', prov_long='Zonta International',
 h1='Zonta Amelia Earhart Fellowship 2026',
 sub='US$10,000 for women flying high — PhD research in aerospace engineering and space sciences.',
 dpill='30 days to go', dl_long='15 Nov 2026',
 facts=facts([('Award','US$10,000<small>Up to 30 fellows</small>'),
              ('Who can apply','Women PhD students<small>Aerospace / space sciences</small>'),
              ('Open to','Any nationality<small>Usable at any accredited university</small>'),
              ('Deadline','15 Nov 2026<small>Annual cycle</small>'),
              ('Since','1938<small>1,700+ fellowships awarded</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Amelia Earhart Fellowship</strong>, established in <strong>1938</strong> by <strong>Zonta International</strong> in honour of the famed pilot, supports <strong>women pursuing PhD/doctoral degrees in aerospace engineering and space sciences</strong>. Up to <strong>30 fellows</strong> receive <strong>US$10,000</strong> each year, usable at any accredited university. Since 1938, Zonta has awarded over 1,700 fellowships worth more than US$11 million to women from 80+ countries.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Woman</strong> of <strong>any nationality</strong>.</li>
        <li>Pursuing a <strong>PhD/doctoral degree in aerospace engineering or space sciences</strong> (full-time).</li>
        <li>Completed at least <strong>one year of the PhD</strong>, or hold a <strong>Master's in an aerospace-applied field</strong>.</li>
        <li>Strong academic record with active research involvement.</li>
        <li><strong>Not eligible:</strong> part-time students, post-doctoral researchers, previous fellows.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>US$10,000</strong> — tuition, books, fees, supplies, research equipment, travel.</li>
        <li>Usable at <strong>any accredited university</strong>.</li>
        <li>Can be combined with other grants.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic transcripts</li><li>Research proposal</li>
        <li>Three letters of recommendation</li><li>Proof of PhD enrolment</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the Zonta International website</strong>Amelia Earhart Fellowship page.</li>
        <li><strong>Prepare documents</strong>Transcripts, research proposal, three recommendation letters.</li>
        <li><strong>Submit the online application</strong>Before <strong>15 November 2026</strong>.</li>
        <li><strong>Results by end of April 2027</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How many fellowships are awarded?","Up to 30 per year."),
 ("Can I use it at any university?","Yes — any university offering accredited postgraduate courses in these fields."),
 ("I am in my first PhD year. Can I apply?","Only if you hold a Master's in an aerospace-applied field; otherwise complete one PhD year first."),
 ("Can previous fellows reapply?","No — previous fellows are not eligible."),
]),
 verify='Verified 16 Oct 2026 via StudyOpportunities (US$10,000; up to 30 women; 15 Nov 2026; est. 1938; 1,794 fellowships), Ambitio (eligibility: full-time PhD, 1+ year or Master\'s; three recommendation letters; notified by April 2027) and GreatYOP.',
 offlinks=[('Zonta International (official)','https://www.zonta.org/')],
 related_titles=['nasa-hubble','swiss-phd','bloomberg-harvard'],
),

dict(
 slug='world-bank-government-analytics-fellowship-2027',
 title='World Bank Government Analytics Fellowship 2027 | StudyDesk Scholarships',
 meta='World Bank Government Analytics Fellowship 2027: fully funded fellowship for public servants using government data. Deadline 16 Nov 2026.',
 short='World Bank Gov Analytics Fellowship', kicker='Professionals · Fully Funded',
 mono='WB', prov_short='World Bank Group', prov_long='World Bank Group (with University of Oxford experts)',
 h1='World Bank Government Analytics Fellowship 2027',
 sub='Fully funded — for public servants turning government data into better decisions.',
 dpill='31 days to go', dl_long='16 Nov 2026',
 facts=facts([('Award','Fully funded (in-person)<small>Travel + hotel for ODA countries</small>'),
              ('Who can apply','Central-govt officials<small>Mid-level/senior; nominated</small>'),
              ('Tracks','Online / in-person / hub<small>2 weeks in Washington DC, Mar 2027</small>'),
              ('Deadline','16 Nov 2026<small>Official form</small>'),
              ('Need','Quantitative coursework<small>+ English proficiency</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>World Bank Government Analytics Fellowship 2027</strong> trains <strong>public servants</strong> to turn their own administrative data into practical insights that improve how government works. Run by the World Bank Group with academic experts including from the <strong>University of Oxford</strong>, it offers three tracks: <strong>online-only, immersive in-person</strong> (six months, with ~two weeks in Washington, D.C. in March 2027), and <strong>regional hub</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Work in a <strong>central government organisation or agency</strong>.</li>
        <li><strong>Mid-level management or senior analytical role</strong> (or equivalent), with authority to develop a project.</li>
        <li><strong>Organisational nomination</strong> — up to 2 fellows per organisation; endorsement letter required.</li>
        <li>Prior <strong>tertiary-level coursework in statistics</strong> or quantitative methods.</li>
        <li><strong>English proficiency.</strong></li>
      </ul>
      <div class="honest-note"><strong>Not for students:</strong> this is for serving public servants with an institutional project — not an open fellowship for data analysts, students or nonprofit staff.</div>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>In-person track:</strong> hotel, travel and subsistence in Washington, D.C. covered for fellows from <strong>ODA-eligible countries</strong>.</li>
        <li><strong>Project mentoring</strong> from World Bank and Oxford experts.</li>
        <li>Online track is self-paced alongside the job.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>CV (max 3 pages)</li><li><strong>150-word project summary</strong></li>
        <li><strong>Organisational endorsement letter</strong></li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure organisational nomination</strong>Endorsement letter confirming your position and project.</li>
        <li><strong>Prepare documents in English (PDF)</strong>CV, 150-word project summary, endorsement letter.</li>
        <li><strong>Submit via the official form</strong>Before <strong>16 November 2026</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("I am a student/data analyst. Can I apply?","No — it is for central-government officials with an institutional project and nomination."),
 ("What does the in-person track cover?","For ODA-eligible countries: travel, hotel and subsistence for ~2 weeks in Washington, D.C. in March 2027."),
 ("How many can one organisation nominate?","Up to 2 fellows per organisation."),
 ("What documents do I need?","CV (max 3 pages), a 150-word project summary, and an organisational endorsement letter — all in English PDF."),
]),
 verify='Verified 16 Oct 2026 via OpportunitiesFeed (deadline 16 Nov 2026; three tracks; nomination + quantitative coursework required; ODA funding terms) and OpportunityLab/ScholarshipBob (documents: 3-page CV, 150-word summary, endorsement letter; Washington DC ~2 weeks March 2027).',
 offlinks=[('World Bank — Government Analytics (official)','https://www.worldbank.org/en/research/brief/government-analytics-fellowship')],
 related_titles=['bloomberg-harvard','nasa-hubble','swiss-phd'],
),

dict(
 slug='dakshana-scholarship-jdst-2027',
 title='Dakshana Scholarship (JDST) 2027: Free JEE/NEET Coaching | StudyDesk Scholarships',
 meta='Dakshana Scholarship JDST 2027: free one-year residential JEE/NEET coaching at Dakshana Valley Pune. Eligibility, test in Dec 2026.',
 short='Dakshana JDST 2027', kicker='Coaching · Merit · Free',
 mono='D', prov_short='Dakshana Foundation', prov_long='Dakshana Foundation, Pune',
 h1='Dakshana Scholarship (JDST) 2027',
 sub='Free one-year residential JEE/NEET coaching — Dakshana Valley, Pune. Test in December 2026.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Free coaching + stay + food<small>One year, residential</small>'),
              ('Who can apply','Class 12 science students<small>Govt/aided schools 2026–27</small>'),
              ('Income limit','Rs 3 lakh / year<small>Family income</small>'),
              ('Selection','JDST Dec 2026<small>+ interview & verification</small>'),
              ('Record','~80% reach IIT/NIT/AIIMS<small>Per the Foundation</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Dakshana Scholarship</strong>, awarded through the <strong>Joint Dakshana Selection Test (JDST) 2027</strong>, gives underprivileged Class 12 science students <strong>one full year of free residential JEE/NEET coaching</strong> at <strong>Dakshana Valley, Kadus (Pune, Maharashtra)</strong> — coaching, accommodation and food, all free. Dakshana Foundation has run this for 19+ years; it reports ~80% of scholars reach an IIT, NIT, AIIMS or government medical college.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Studying in <strong>Class 12 Science</strong> in a <strong>government / government-aided school</strong> in 2026–27 (board exams by May 2027).</li>
        <li><strong>Class 10 Maths + Science aggregate</strong> above the cut-off — e.g. Engineering (male): GEN 85%, EWS/OBC 80%, SC 70%, ST 65%, PwD 55%; relaxed for female/medical tracks.</li>
        <li>Annual <strong>family income below Rs 3 lakh</strong> (up to Rs 5 lakh for female candidates in some cycles).</li>
        <li>Current annual school fee below Rs 36,000.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Free JEE/NEET coaching for one year.</strong></li>
        <li><strong>Free accommodation and food</strong> at Dakshana Valley.</li>
        <li>Residential academic support and mentoring.</li>
      </ul>
      <h2 id="selection">Selection process</h2>
      <ol>
        <li>Online application + shortlisting.</li>
        <li><strong>JDST 2027</strong> (tentatively <strong>December 2026</strong>): MCQs in Physics, Chemistry, Maths/Biology and logical reasoning (+5/−2 marking).</li>
        <li>Interview and document verification.</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the Dakshana portal</strong>dakshana.org — registration links for JDST 2027.</li>
        <li><strong>Register through your school</strong>Schools were directed to publicise it; consult your principal/science coordinator.</li>
        <li><strong>Take the JDST</strong>December 2026 — download the hall ticket after verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is it really free?","Yes — coaching, accommodation and food for one year are all free for selected scholars."),
 ("I study in a private school. Can I apply?","No — this route is for government/government-aided school students."),
 ("What is the income limit?","Below Rs 3 lakh per year of family income."),
 ("When is the test?","Tentatively December 2026."),
]),
 verify='Verified 16 Oct 2026 via Tribune India (JDST 2027 Dec 2026; free coaching + accommodation + meals at Dakshana Valley; Class 12 science 2026–27; income < Rs 3L; category cut-offs), Hindustan Times, Business Standard and Moneycontrol (same facts).',
 offlinks=[('Dakshana Foundation (official)','https://www.dakshana.org/')],
 related_titles=['super50-aayam','sakal-cds','isi-stipend'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')

import cards_registry
cards_registry.CARDS.update(CARDINFO)
pathlib.Path('/home/hatch/workspace/scholarships-17k/cards_registry.py').write_text(
    '"""Shared related-card registry for all scholarship articles. Append new batches here."""\n\nCARDS = ' + repr(cards_registry.CARDS) + '\n')

p = json.load(open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json'))
p['done'] += ['EPFL Summer Internship 2027 in Switzerland (Fully Funded)',
 'Sage IT India Scholarship 2026',
 'Zonta Amelia Earhart Fellowship 2025',
 'World Bank Government Analytics Fellowship 2027 (Fully Funded)',
 'Dakshana Scholarship ( JDST) 2027']
p['runs'] = 8
json.dump(p, open('/home/hatch/workspace/scholarships-17k/inventory/queue-progress.json','w'), indent=1)

t = pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').read_text()
t += """
## Batch 8 (16 Oct 2026) — 5 articles, all verified
| # | Slug | Scholarship | Deadline | Verified |
|---|------|-------------|----------|----------|
| 36 | epfl-summer-internship-2027 | EPFL Summer Internship 2027 | 1/15 Nov 2026 | Yes — ScholarPositions/EPFL official |
| 37 | sage-it-india-scholarship-2026 | Sage IT India Scholarship | 15 Nov 2026 | Yes — The Hindu/Sage IT |
| 38 | zonta-amelia-earhart-fellowship-2026 | Zonta Amelia Earhart Fellowship | 15 Nov 2026 | Yes — StudyOpp/Ambitio |
| 39 | world-bank-government-analytics-fellowship-2027 | World Bank Gov Analytics Fellowship | 16 Nov 2026 | Yes — OppFeed/OppLab |
| 40 | dakshana-scholarship-jdst-2027 | Dakshana Scholarship (JDST) 2027 | 30 Nov 2026 | Yes — Tribune/HT/BS |

**Completed: 40 / 1,808 live topics**
"""
pathlib.Path('/home/hatch/workspace/scholarships-17k/progress/tracker.md').write_text(t)
print('tracker + progress updated')

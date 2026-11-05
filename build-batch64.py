#!/usr/bin/env python3
"""Batch 64 (cron run 64, 29 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. 2026 Intakes in Canada - SKIPPED: listicle, not a single scheme.
2. UN Chemicals and Waste Management Program 2026 - SKIPPED: deadline
   passed (July edition 27 Apr 2026; November edition 11 Sep 2026);
   no 2027 cycle announced.
3. Top Scholarships in UAE Qatar and Saudi Arabia 2026 - SKIPPED:
   listicle, not a single scheme.
4. Asia Foundation Leadership Program 2026 (LeadNext) - SKIPPED:
   deadline passed 5 May 2026; summit 19-27 Sep 2026 ended.
5. Kyoto University CSEAS Fellowship 2027 - SKIPPED: deadline passed
   30 Apr 2026.
6. University of Pavia CICOPS Scholarship 2026 - SKIPPED: deadline
   passed 10 Jun 2026.
7. NASA Internship and Fellowship 2026 - SKIPPED: umbrella title, 2026
   cycles closed; live successor is NASA OSTEM Summer 2027
   (deadline 1 Mar 2027) - spare for a 2027 retitle, not this title.
8. Presidential Merit Scholarship 2026 at Texas Tech - VERIFIED for
   the live 2027 cycle, retitled (official 1 Apr 2027 deadline;
   $1,000-$9,000/year tier table, not the aggregator $26,000 total).
9. Queen Elizabeth Commonwealth Scholarship 2026 - SKIPPED: DUPLICATE
   of the already-published QECS 2027-28 article (Cycle 1
   18 Nov 2026 - 13 Jan 2027, deadline 13 Jan 2027).
10. University of Pretoria Mastercard Scholarship 2026-27 - SKIPPED:
    deadlines passed (UG 31 Aug 2026; PG 30 Sep 2026).
11. Google Research Scientist Internship 2026 Australia - SKIPPED:
    2026 window unconfirmed (aggregators conflict: 7 Apr 2026 close
    vs rolling); no live official listing confirmed.
12. Qatar Airways Summer Internship 2026 - SKIPPED: 2026 summer cycle
    over; Qatari nationals only; no 2027 dates published.
13. Humphrey Fellowship 2026-27 - SKIPPED: 2027-28 country deadlines
    passed (Jul-Aug 2026); no 2028-29 call confirmed.
14. ETH Zurich Postdoctoral Fellowship 2026-27 - VERIFIED for the
    next round (1 Mar 2027, 17:00 Swiss time; twice-yearly rounds).
15. Microsoft Global University Paid Internship 2026 - SKIPPED:
    umbrella label, per-role rolling listings, no single deadline.
16. Tsinghua Schwarzman Scholarship 2026-27 - SKIPPED: deadline
    passed 9 Sep 2026 (global/US); 20 May 2026 (China).
17. Concordia University Scholarships 2026 - SKIPPED: umbrella label,
    many separate awards, no single scheme.
18. List of Fully Funded Scholarship in Australia 2026 - SKIPPED:
    listicle.
19. Ruhr University DAAD EPOS Scholarships 2028 - VERIFIED
    (DAAD official: EPOS deadline 30 Sep 2027; opens 18 Jan 2027).
20. Estonia Government Scholarships 2026 - SKIPPED: deadline passed
    (1 Apr - 1 May 2026, Harno official).
21. Qatar Airways University Undergraduate Scholarship 2026 -
    VERIFIED (rolling; no fixed deadline published; Qatari
    nationals / children of Qatari mothers only).
22. UNSW Graduate Scholarships 2026 - SKIPPED: deadline passed
    17 Apr 2026 (spare: 2027 retitle, RTP/UPA 15 Jan 2027).
23. EU4Ocean Summer School 2026 - SKIPPED: deadline passed
    27 Apr 2026; programme ran 14-18 Sep 2026.
24. Erasmus Mundus CLIDE Scholarship 2026 - SKIPPED: deadline
    passed 15 Apr 2026.
25. Jiangsu University Presidential Scholarship 2026 - SKIPPED:
    deadline passed 30 Jun 2026 (single unverified 25 Dec claim
    rejected).
26. University of Siena International Excellence 2026 - SKIPPED:
    deadline passed 6 May 2026.
27. Taiwan AID NGO Fellowships 2026 - SKIPPED: deadline passed
    1 Jun 2026; 2026 fellows already selected.
28. John Thompson Scholarship 2026 (DCU) - SKIPPED: closed
    30 Jul 2026 (official DCU page).
29. Bucharest Summer University School 2026 - SKIPPED: deadline
    passed 31 May 2026; programme ran 9-23 Aug 2026.
30. ANU International Chancellor's Scholarship 2026 - VERIFIED
    (automatic assessment on admission; aggregators report a
    15 Dec 2026 admission cutoff; 25%/50% waiver, not a flat
    dollar amount; Bachelor's/Master's coursework only).
Spares for the next run (in queue order): UNICAF Online Scholarship
Programme 2026 (rolling, partial up to 80% per UNICAF's own page -
not fully funded); Harvard University MBA Scholarship 2027
(Boustany: 75% of tuition, 31 May 2027, one award every 2 years).
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 29)
def dl_left(ymd):
    y, m, d = map(int, ymd.split('-'))
    return (date(y, m, d) - TODAY).days

def _split_verify(a):
    m = _re.search(r'\s*<p class="verify">(.*?)</p>\s*$', a['body'], _re.S)
    if not m: raise SystemExit('no verify paragraph in ' + a['slug'])
    a['body'] = a['body'][:m.start()]
    a['verify'] = m.group(1)
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

NEW_CARDS = {
 'ttup-2027': {'mono': 'TTU', 'title': 'Presidential Merit Scholarship 2027 at Texas Tech University',
   'href': 'texas-tech-university-presidential-merit-scholarship-2027-usa.html',
   'dpill': 'Deadline 1 Apr 2027 · %d days left' % dl_left('2027-04-01'),
   'award': 'Merit awards of $1,000–$9,000 a year set by the official Texas Tech tier table (test score plus unweighted high-school GPA), split half in fall and half in spring and renewable for four years; non-resident recipients also qualify for in-state tuition. No separate scholarship application — automatic on admission.',
   'elig': 'Entering first-time freshmen (transfer students are also considered for merit awards) showing exceptional academic ability through test scores, class rank and GPA; merit awards are guaranteed to freshmen admitted by 1 April for fall entry.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'eth-fellows-2027': {'mono': 'ETH', 'title': 'ETH Zurich Postdoctoral Fellowship 2027 in Switzerland (Fully Funded)',
   'href': 'eth-zurich-postdoctoral-fellowship-2027-switzerland.html',
   'dpill': 'Deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
   'award': 'A two-year, non-renewable fellowship at ETH Zurich: a full salary at ETH standards plus a research allowance (CHF 12,000 a year in current guides; some older pages list CHF 10,000), for a project of your own design with an ETH professor as mentor.',
   'elig': 'Early-career researchers who defended their PhD within two years of the deadline (or will defend within six months, with certification); PhD not from ETH Zurich or the University of Zurich; at least one peer-reviewed publication or a doctoral thesis prize; mobility rule applies.',
   'tags': [('Postdoctoral', 'blue'), ('Switzerland', 'teal')]},
 'ruhr-epos-2028': {'mono': 'RUB', 'title': 'Ruhr University DAAD EPOS Scholarships 2028 in Germany (Fully Funded)',
   'href': 'ruhr-university-daad-epos-scholarships-2028-germany.html',
   'dpill': 'Deadline 30 Sep 2027 · %d days left' % dl_left('2027-09-30'),
   'award': 'DAAD-EPOS support for the 18-month MA in Development Management at Ruhr University Bochum: a monthly stipend (current guides cite €992; older pages cite €934), health, accident and liability insurance, a travel allowance, a rent subsidy and family allowances where applicable; no tuition fees, only a modest semester registration fee.',
   'elig': 'A relevant Bachelor’s degree plus at least two years of relevant professional experience after that degree (the DAAD-EPOS requirement); professionals from developing and newly industrialised countries; English at IELTS 6.0 or TOEFL iBT 79–80.',
   'tags': [('Master’s', 'blue'), ('Germany', 'teal')]},
 'qa-ug-2026': {'mono': 'QA', 'title': 'Qatar Airways University Undergraduate Scholarship 2026 (Fully Funded)',
   'href': 'qatar-airways-university-undergraduate-scholarship-2026.html',
   'dpill': 'Rolling · no fixed deadline published',
   'award': 'Full undergraduate funding for the whole degree (up to four years): tuition fees, a monthly stipend, living costs, accommodation, health insurance and travel. No cash figure is published for the stipend. Scholars join Qatar Airways’ Graduate Development Programme and owe a minimum five-year service commitment after graduation.',
   'elig': 'Qatari nationals or children of a Qatari mother only — not a general international scholarship. Aged 17–24, high school completed within the last three years, 85% (Qatari nationals) or 90% (children of Qatari mothers), IELTS 5.5 or 6.0 respectively, an approved major at a Ministry-accredited university, and a Qatari guarantor.',
   'tags': [('Undergraduate', 'blue'), ('Qatar', 'teal')]},
 'anu-chanc-2026': {'mono': 'ANU', 'title': 'ANU International Chancellor’s Scholarship 2026 in Australia (Funded)',
   'href': 'anu-international-chancellors-scholarship-2026-australia.html',
   'dpill': 'Admission cutoff 15 Dec 2026 (reported) · %d days left' % dl_left('2026-12-15'),
   'award': 'A 25% or 50% tuition fee reduction for the entire degree — a partial award, not full funding — plus guaranteed first-year on-campus accommodation if the recipient chooses it, and a reduced tuition deposit of AUD 10,000. No separate scholarship application: every eligible admission applicant is automatically assessed.',
   'elig': 'Commencing international (overseas) Bachelor’s or Master’s coursework students with an ANU offer, selected on academic merit; no prior award at the same level and no external sponsorship covering tuition. Not a PhD scholarship; Doctor of Medicine and Surgery and Master of Military and Defence Studies are excluded.',
   'tags': [('Undergraduate & Master’s', 'blue'), ('Australia', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Texas Tech
A.append(dict(
 slug='texas-tech-university-presidential-merit-scholarship-2027-usa',
 title='Presidential Merit Scholarship 2027 at Texas Tech University',
 meta='Texas Tech University Presidential Merit Scholarships 2027: automatic merit awards of $1,000–$9,000 a year for entering first-time freshmen, set by test score and GPA, with in-state tuition for non-resident recipients. Merit awards are guaranteed to freshmen admitted by 1 April 2027.',
 short='Texas Tech Presidential Merit 2027', kicker='USA · Undergraduate · Merit', mono='TTU',
 prov_short='Texas Tech University', prov_cat='University · USA',
 h1='Presidential Merit Scholarship 2027 at Texas Tech University',
 sub='Read the headline figure with care. Aggregator pages repeat a single “$26,000” total for this award, but Texas Tech’s own scholarships page does not publish that total: it publishes a tier table, and your award depends on where your test score and unweighted high-school GPA land in it — from $1,000 to $9,000 a year, paid half in the fall term and half in the spring term. There is no separate scholarship form to fill in. Apply for admission to Texas Tech as an entering first-time freshman, and you are automatically considered; merit awards are guaranteed to freshmen admitted by 1 April for fall entry. If you are a non-resident who wins a Presidential award, you also qualify to pay in-state tuition, which is worth far more than the cash award itself.',
 facts=facts([
  ('Provider', 'Texas Tech University, Lubbock, Texas, USA'),
  ('Award', '$1,000–$9,000/year by GPA + test score (official tier table); renewable; in-state tuition for non-resident recipients'),
  ('Level', 'Undergraduate — entering first-time freshmen (transfer students also considered)'),
  ('Deadline', '1 April 2027 (merit awards guaranteed to freshmen admitted by this date for fall entry; a 1 December 2026 fall priority date is also listed)'),
  ('Eligibility', 'Exceptional academic ability shown through test scores, class rank and GPA; no separate scholarship application'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>Texas Tech University in Lubbock, Texas, awards Presidential Merit Scholarships to entering first-time freshmen who show exceptional academic ability. The award is not a single fixed sum and it is not a separate competition: it is the university’s automatic merit assessment, made on the strength of your admission application. The official page states the rule plainly — merit awards are guaranteed to freshmen admitted by 1 April for fall entry, and transfer students may qualify if admitted by 31 July for fall entry or 5 January for spring entry. Admission after those dates is limited only by the availability of the scholarships.</p>
      <p>Two corrections to the aggregator version of this award matter. First, the widely repeated “$26,000” is an aggregator total, not a figure on the university’s tier table, and this article does not present it as the official award. Second, some aggregator pages describe the award as open to United States residents only, while the university’s own page says a non-resident awarded a Presidential Scholarship also qualifies to pay in-state tuition — so non-residents are plainly in scope, and the in-state rate is a major part of the value for them.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Annual award:</strong> $1,000–$9,000 a year, set by the combination of test score and unweighted high-school GPA. At the top of the table, a 1500–1600 SAT (or 34–36 ACT) with a 4.0–3.96 GPA earns $9,000 a year; a 1100–1190 SAT (or 22–24 ACT) with a 3.49–3.0 GPA earns $1,000 a year. Test-optional applicants can add $1,000 if they rank in the top 10% of their class.</li>
        <li><strong>How it is paid:</strong> one half toward the fall term and one half toward the spring term, renewable annually for up to four years subject to the university’s renewal terms.</li>
        <li><strong>In-state tuition for non-residents:</strong> if you are a non-resident or international student awarded a Presidential Scholarship, you also qualify to pay in-state tuition — a saving that dwarfs the cash award.</li>
        <li><strong>National Merit Finalists:</strong> a separate line on the official page covers 100% of the originally federally approved cost of attendance for National Merit Finalists.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Entering first-time freshmen</strong> who show exceptional academic ability through superior test scores and class ranking. Transfer students are also considered for merit awards under their own admission dates.</li>
        <li><strong>Test score or GPA route:</strong> the published routes are a minimum cumulative SAT of 1100 or a minimum composite ACT of 22 with a minimum high-school GPA of 3.0, or a minimum high-school GPA of 3.5 without test scores.</li>
        <li><strong>Full-time enrolment and progress:</strong> renewal requires satisfactory academic progress under the university’s terms, including the credit-hour expectations that apply to merit awards.</li>
        <li><strong>No separate application:</strong> there is no scholarship form beyond the admission application itself — apply for admission and you are considered automatically.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>The admission application</strong> itself — the official page names no separate scholarship document set, because consideration is automatic on admission.</li>
        <li><strong>Academic records and test scores</strong> as required for admission (transcripts, SAT/ACT scores where submitted, class rank where available).</li>
        <li>International applicants should confirm English-proficiency and credential requirements on the university’s international admissions pages, which are separate from the scholarship table.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to Texas Tech University as an entering first-time freshman (or as a transfer student under the transfer dates), through the university’s admission route.</li>
        <li>Make sure your admission application is complete by <strong>1 April 2027</strong> — merit awards are guaranteed to freshmen admitted by this date for fall entry. A 1 December 2026 fall priority scholarship date is also listed on the university’s pages, so applying earlier is safer.</li>
        <li>There is no separate scholarship application to submit. Your award, if any, is determined by the tier table from your test score and GPA and is communicated with your admission outcome.</li>
        <li>If you are a non-resident recipient, confirm the in-state tuition qualification with the scholarships office when you accept, since that is where most of the value sits for out-of-state students.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Texas Tech Presidential Merit Scholarship 2027?',
  'Merit awards are guaranteed to freshmen admitted by 1 April 2027 for fall entry. A 1 December 2026 fall priority scholarship date is also listed on the university’s pages, so do not leave the application to the last day. Transfer students have their own dates: 31 July for fall entry and 5 January for spring entry.'),
 ('How much is the Presidential Merit Scholarship worth?',
  'Between $1,000 and $9,000 a year, depending on your test score and unweighted high-school GPA under the university’s published tier table — not a single flat amount. The “$26,000” total repeated by aggregator pages is not the university’s published award and should not be relied on.'),
 ('Do international students qualify?',
  'The university’s own page says a non-resident awarded a Presidential Scholarship also qualifies to pay in-state tuition, so non-residents are in scope. Some aggregator pages wrongly describe the award as United States residents only; follow the university page, and confirm your own fee status with the scholarships office.'),
 ('Is there a separate scholarship application?',
  'No. There is no scholarship form beyond the admission application. You are automatically considered when you apply for admission, and the award is set by the tier table.'),
 ('What happens if I apply after 1 April?',
  'Admission after the guarantee date is limited only by the availability of the scholarships — awards are no longer guaranteed. Apply early to keep the guarantee.'),
 ('What does the award cover, and for how long?',
  'The cash award is paid half in fall and half in spring and is renewable annually for up to four years subject to the university’s renewal terms. For non-residents, the accompanying in-state tuition qualification is usually worth more than the cash award.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against Texas Tech University's own incoming-freshmen scholarships page (depts.ttu.edu/scholarships/incFreshman.php: Presidential Merit Scholarships for entering first-time freshmen and transfer students showing exceptional ability; annual amounts pay one half toward fall and one half toward spring; merit awards guaranteed to freshmen admitted by April 1st for fall entry; transfer dates 31 July / 5 January; non-resident recipients qualify for in-state tuition; National Merit Finalist line at 100% of originally federally approved cost of attendance; tier table $1,000-$9,000/year by SAT/ACT band and unweighted GPA, test-optional top-10% adds $1,000) plus the Bright Scholarship page (2026 cycle, $26,000 headline, 1 May 2026 deadline — both now superseded) and The Unipedia (domestic and international freshmen; $1,000-$9,000 annually; SAT 1100 / ACT 22 or GPA 3.5 test-optional routes). CONFLICTS: (1) The aggregator "$26,000" total is NOT on the official tier table and is not used as the award figure. (2) Aggregator pages saying "USA residents only" conflict with the official page's in-state-tuition rule for non-resident recipients; the article follows the official page. (3) Aggregator deadlines of 1 May 2026 / 1 May 2027 conflict with the official page's 1 April guarantee date; the article uses 1 April 2027 and notes the 1 December 2026 fall priority date also listed.</p>''',
 dl_long='1 April 2027 (merit awards guaranteed to freshmen admitted by this date for fall entry; a 1 December 2026 fall priority scholarship date is also listed — apply early)',
 offlinks=[('Texas Tech University — Incoming Freshmen Scholarships (official)', 'http://www.depts.ttu.edu/scholarships/incFreshman.php'),
           ('Bright Scholarship — Presidential Merit Scholarship at Texas Tech University', 'https://brightscholarship.com/presidential-merit-scholarship-at-texas-tech-university/'),
           ('The Unipedia — Texas Tech Presidential Merit Scholarship', 'https://www.theunipedia.org/2020/01/texas-tech-presidential-scholarship.html')],
 related_titles=['eth-fellows-2027', 'ruhr-epos-2028', 'qa-ug-2026', 'anu-chanc-2026'])),

# ---------------------------------------------------------------- 2. ETH Zurich
A.append(dict(
 slug='eth-zurich-postdoctoral-fellowship-2027-switzerland',
 title='ETH Zurich Postdoctoral Fellowship 2027 in Switzerland (Fully Funded)',
 meta='ETH Zurich Postdoctoral Fellowship (ETH Fellows) 2027: a two-year, non-renewable fellowship with a full ETH salary and a research allowance, for early-career researchers with their own project and an ETH professor as mentor. Next deadline 1 March 2027 at 17:00 Swiss time.',
 short='ETH Postdoctoral Fellowship 2027', kicker='Switzerland · Postdoctoral · Fully Funded', mono='ETH',
 prov_short='ETH Zurich', prov_cat='Institute · Switzerland',
 h1='ETH Zurich Postdoctoral Fellowship 2027 in Switzerland (Fully Funded)',
 sub='This is a fellowship for researchers who already have a project of their own, not a job attached to somebody else’s grant. You apply jointly with an ETH Zurich professor who will act as your mentor, you propose the research yourself, and if you win you get two years — non-renewable — at a full ETH salary, plus a research allowance, in any discipline an ETH host professor covers. The scheme runs twice a year, on 1 March and 1 September at 17:00 Swiss time, and the September 2026 round has already closed, so the live target is 1 March 2027. The eligibility window is tight: your PhD must be no more than two years old at the deadline, and the mobility rule excludes anyone who has spent too much recent time in Switzerland or at ETH-domain institutions.',
 facts=facts([
  ('Provider', 'ETH Zurich, Switzerland (ETH Fellows programme)'),
  ('Award', 'Two years, non-renewable: full ETH salary + research allowance (CHF 12,000/year in current guides; some older pages list CHF 10,000)'),
  ('Level', 'Postdoctoral — early-career researchers'),
  ('Deadline', '1 March 2027, 17:00 Swiss time (rounds run 1 March and 1 September each year)'),
  ('Eligibility', 'PhD defended within 2 years of the deadline; PhD not from ETH Zurich or University of Zurich; ≥1 peer-reviewed publication or thesis prize; ETH professor as host/mentor; mobility rule'),
 ]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The ETH Zurich Postdoctoral Fellowship programme — known as ETH Fellows — supports incoming postdoctoral researchers of high potential who have already shown internationally competitive achievements early in their careers. It is deliberately broad: fellowships are available in all disciplines covered by the research of ETH host professors, from engineering and the natural sciences to architecture, mathematics and the social sciences. The fellowship lasts two years and cannot be prolonged, because the scheme is designed to launch an independent career rather than extend a postdoctoral position indefinitely.</p>
      <p>Two features set it apart from an ordinary postdoctoral job. First, the project is yours: you write the proposal and an ETH professor supports it as your mentor, rather than you joining a professor’s existing project. Second, the funding is a full salary at ETH standards, including social-security contributions, rather than a bare stipend — plus a research allowance for travel, mobility and research costs. Recent guides put the research allowance at CHF 12,000 a year; some older pages list CHF 10,000, and this article flags that difference rather than silently picking one.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full salary:</strong> a salary at ETH standards for two years, including the 15% social-security contribution — an employment contract, not a stipend.</li>
        <li><strong>Research allowance:</strong> CHF 12,000 a year for travel, mobility and research costs in current guides (older pages list CHF 10,000 — confirm the current figure in the call documents).</li>
        <li><strong>Two years, non-renewable:</strong> a fixed horizon with a start expected no later than eight months after the submission date, unless the Grants Office agrees a later start.</li>
        <li><strong>Your own project:</strong> you propose and lead the research, with an ETH professor as mentor, in any discipline the host professors cover.</li>
        <li><strong>World-class setting:</strong> access to ETH Zurich’s laboratories, facilities and research community, and a cohort of fellows across disciplines.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Recent PhD:</strong> you must have defended your doctoral degree within two years of the submission deadline. You may apply up to six months before your defence, with a certification of the planned defence date signed by your advisor or department chair.</li>
        <li><strong>Not an ETH or Zurich PhD:</strong> your doctorate must be from an institution other than ETH Zurich or the University of Zurich.</li>
        <li><strong>Publication threshold:</strong> at least one scientific publication in a peer-reviewed journal, or a prize for your doctoral thesis. Applications that fail the formal rules are rejected on formal grounds, so this is a threshold, not a preference.</li>
        <li><strong>Host professor:</strong> the application is made jointly with an ETH Zurich professor who will act as mentor. You need that professor’s support before you submit.</li>
        <li><strong>Mobility rule:</strong> at the deadline, you must not have resided in or carried out your main activity in Switzerland for more than twelve months in the preceding three years, and you must not have worked at ETH Zurich, EPFL, an ETH-domain institute or the University of Zurich for more than six months in that period.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Project description</strong> on the ETH templates, setting out the research you propose to lead.</li>
        <li><strong>CV</strong> and the host professor’s supporting documents, uploaded through the application.</li>
        <li><strong>Two reference letters</strong>, sent directly by the referees to the Grants Office — at least ten days before the deadline in current guidance, so line referees up early.</li>
        <li><strong>Proof of the PhD</strong> (or, if you are applying before defence, the signed certification of the planned defence date).</li>
        <li>All documents are submitted electronically through the ETH eResearch system; the programme does not accept applications by email.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Find an ETH Zurich professor willing to act as your host and mentor, and agree the project with them — the application is joint, and a host’s support is a formal requirement.</li>
        <li>Download the project-description templates, write your proposal, and prepare your CV and the host’s supporting documents.</li>
        <li>Register on the ETH eResearch system, create the application, and upload everything as PDFs. Ask your two referees to send their letters directly to the Grants Office well before the deadline.</li>
        <li>Validate the application in the system, then submit by <strong>1 March 2027 at 17:00 Swiss time</strong>. If the deadline falls on a weekend it moves to the following Monday at the same time. Shortlisted candidates are invited to a video interview, and final decisions arrive about four months after the deadline.</li>
        <li>Do not confuse this scheme with the separate ETH AI Center fellowships, which have their own system and deadlines.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the ETH Zurich Postdoctoral Fellowship 2027?',
  'The next round closes on 1 March 2027 at 17:00 Swiss time. The programme runs twice a year, on 1 March and 1 September; the September 2026 round has already closed, so 1 March 2027 is the live target.'),
 ('How long does the fellowship last, and can it be extended?',
  'Two years, and it cannot be prolonged. Fellows are expected to start no later than eight months after the submission date unless the Grants Office agrees otherwise.'),
 ('What does the fellowship pay?',
  'A full salary at ETH standards, including social-security contributions, plus a research allowance — CHF 12,000 a year in current guides, though some older pages list CHF 10,000. Exact salary figures for 2027 are not stated as a single published number in the sources checked, so this article does not invent one.'),
 ('Can I apply if my PhD is from ETH Zurich or the University of Zurich?',
  'No. The doctorate must be from another institution, and the mobility rule also limits recent activity in Switzerland and at ETH-domain institutions.'),
 ('How recent must my PhD be?',
  'Defended within two years of the submission deadline. You may apply up to six months before your defence with a signed certification of the planned date.'),
 ('Do I need a host professor before applying?',
  'Yes. The application is made jointly with an ETH Zurich professor who acts as mentor, and the host’s supporting documents are part of the submission.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against EURAXESS (ETH Zurich Postdoctoral Fellowships: joint application with an ETH professor as mentor; 2 years, non-renewable; PhD defended within 2 years of the deadline, not from ETH Zurich or University of Zurich; up to 6 months before defence with certification; no more than 6 months' main activity at either institution; at least one peer-reviewed publication or thesis prize; deadlines 1 March and 1 September) plus Europe Scholarships (two non-renewable years at a full ETH salary plus CHF 12,000/year research expenses; 17:00 Swiss time; 12-month Switzerland / 6-month ETH-domain mobility limits; ~15-20% success rate) and ResearchersJob (eResearch system; templates; host support documents; 2 references sent directly to the Grants Office; contacts eresearch-support@ethz.ch and ethfellows@sl.ethz.ch). CONFLICTS: (1) Research allowance is CHF 12,000/year in current guides but CHF 10,000/year on older pages — the article states both and leads with the current figure. (2) Exact 2027 salary figures (CHF 92,500 / 97,200) appear in secondary summaries only and are not stated in the article; it uses the confirmed "full ETH salary" formulation. (3) The ETH AI Center fellowships are a separate scheme with their own system and deadlines and are excluded.</p>''',
 dl_long='1 March 2027, 17:00 Swiss time (the next round; the programme runs twice a year, on 1 March and 1 September)',
 offlinks=[('EURAXESS — ETH Zurich Postdoctoral Fellowships (official listing)', 'https://euraxess.ec.europa.eu/worldwide/brazil/eth-zurich-postdoctoral-fellowships-researchers-early-stages-their-careers'),
           ('ResearchersJob — ETH Postdoctoral Fellowship', 'https://researchersjob.com/eth-postdoctoral-fellowship-2/'),
           ('Europe Scholarships — ETH Postdoctoral Fellowships', 'https://europescholarships.com/fellowships/eth-postdoctoral-fellowships-switzerland-2027')],
 related_titles=['ttup-2027', 'ruhr-epos-2028', 'qa-ug-2026', 'anu-chanc-2026'])),

# ---------------------------------------------------------------- 3. Ruhr EPOS
A.append(dict(
 slug='ruhr-university-daad-epos-scholarships-2028-germany',
 title='Ruhr University DAAD EPOS Scholarships 2028 in Germany (Fully Funded)',
 meta='Ruhr University Bochum DAAD-EPOS Scholarships 2028: fully funded MA in Development Management (18 months, taught in English) for development professionals, with a monthly stipend, insurance and travel allowance. EPOS deadline 30 September 2027; applications open 18 January 2027.',
 short='Ruhr DAAD EPOS 2028', kicker='Germany · Master’s · Fully Funded', mono='RUB',
 prov_short='Ruhr University Bochum', prov_cat='University · Germany',
 h1='Ruhr University DAAD EPOS Scholarships 2028 in Germany (Fully Funded)',
 sub='This is not a scholarship for fresh graduates. The MA in Development Management at Ruhr University Bochum is built for people who have already worked in development — in government, an NGO, an agency or a research institution — and want the academic tools to run larger programmes. The DAAD-EPOS scholarship exists for exactly that group: a relevant degree, at least two years of relevant professional experience after it, and a plan to take the training home. The 2028–2030 intake opens on 18 January 2027, and the scholarship deadline is 30 September 2027 — a full year before the programme starts, because the selection runs through the university first and DAAD second. One honest note up front: Bochum charges no tuition for this programme, only a modest semester registration fee, so the real value of the scholarship is the monthly stipend, the insurance and the living-cost support on top.',
 facts=facts([
  ('Provider', 'Ruhr University Bochum — Institute of Development Research and Development Policy (IEE), funded by DAAD (EPOS)'),
  ('Award', 'DAAD-EPOS: monthly stipend (current guides €992; older pages €934), insurance, travel allowance, rent subsidy, family allowances; no tuition fees (semester fee ~€362 incl. transport pass)'),
  ('Level', 'Master’s — MA in Development Management, 3 semesters / 18 months, 90 ECTS, taught in English'),
  ('Deadline', '30 September 2027 for DAAD-EPOS applicants (2028–2030 intake opens 18 January 2027); 31 December 2027 for self-financed applicants'),
  ('Eligibility', 'Relevant Bachelor’s degree + ≥2 years’ relevant professional experience after it; professionals from developing / newly industrialised countries; IELTS 6.0 / TOEFL iBT 79–80'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The MA in Development Management (MADM) has run at Ruhr University Bochum since 2000, as part of DAAD’s Development-Related Postgraduate Courses (EPOS) initiative. EPOS exists to give professionals from developing and newly industrialised countries advanced academic training they can bring back to their home countries. The programme runs three semesters: coursework in the first, project and evaluation methods in the second alongside an optional internship, and a field research period followed by thesis writing in the third. It is taught entirely in English, carries 90 ECTS credits, and is based on campus in Bochum — it is not a distance-learning programme.</p>
      <p>The application route confuses many applicants, so be clear about it: you do not apply to DAAD first. You apply directly to the MADM programme at Ruhr University Bochum, and candidates the university recommends for an EPOS scholarship are then contacted by DAAD to complete the scholarship stage through the DAAD Portal. There are two deadlines for the 2028–2030 intake, and they are different: 30 September 2027 if you want the DAAD-EPOS scholarship, and 31 December 2027 if you are applying without it. DAAD-EPOS holders also attend a preparatory German language class starting in July before the programme begins.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend:</strong> current guides cite €992 a month for DAAD-EPOS students; older pages cite €934. The article reports both and leads with the current figure — confirm the rate in the call documents for the 2028 intake when they publish.</li>
        <li><strong>Insurance:</strong> health, accident and personal liability insurance costs covered under the EPOS conditions.</li>
        <li><strong>Travel allowance:</strong> a travel allowance for the journey to and from Germany, plus a rent subsidy each month and, where applicable, a monthly allowance for accompanying family members.</li>
        <li><strong>No tuition fees:</strong> Ruhr University Bochum does not charge tuition for this programme. Students pay a modest semester registration fee, currently around €362, which also covers a regional public transport pass.</li>
        <li><strong>Preparatory German course:</strong> DAAD-EPOS holders attend a German language class starting in July before the programme begins.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Degree:</strong> a Bachelor’s degree or equivalent in social science, political science, law, economics, geography, or a subject related to the planning and evaluation of development programmes and projects, at least at “second class, upper division” or equivalent.</li>
        <li><strong>Experience:</strong> work experience related to the management of development programmes and projects — at least one month of practical experience for the programme itself, and at least two years of relevant professional experience after the Bachelor’s degree for DAAD-EPOS applicants. Preference goes to applicants whose employers offer a reintegration guarantee.</li>
        <li><strong>Background:</strong> the EPOS route is designed for professionals from developing and newly industrialised countries in Africa, Asia, Latin America and Eastern Europe. Applicants from any country may apply to the MADM programme itself.</li>
        <li><strong>English:</strong> certified English proficiency for applicants who do not qualify for an exemption — IELTS Band 6.0 and TOEFL iBT 79–80 are listed among the accepted minimum levels.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Degree certificates and transcripts</strong> for your Bachelor’s degree (and any further degrees).</li>
        <li><strong>CV and motivation letter</strong>, setting out your development experience and your reasons for the programme.</li>
        <li><strong>English language certificate</strong> (IELTS 6.0 / TOEFL iBT 79–80 or an accepted equivalent), unless you qualify for an exemption.</li>
        <li><strong>Employment evidence</strong> — certificates covering your relevant professional experience — and, for DAAD-EPOS applicants, the DAAD documents and recommendation letters required at the DAAD stage.</li>
        <li>Documents not in English or German may require certified translations, and incomplete applications are not considered — check every document against the programme’s list before submitting.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Wait for the call to open on <strong>18 January 2027</strong> — the 2028–2030 intake is not open yet, and applications submitted before the call opens are not the route in.</li>
        <li>Prepare your degree documents, CV, motivation letter, language certificate, employment evidence and recommendation letters. If your employer can offer a reintegration guarantee, get it in writing — it strengthens an EPOS application.</li>
        <li>Submit your application through the university’s online MADM application platform — directly to the programme, not to DAAD at the first stage.</li>
        <li>Meet the right deadline: <strong>30 September 2027</strong> if you are applying for a DAAD-EPOS scholarship, or <strong>31 December 2027</strong> if you are applying without one.</li>
        <li>If the university recommends you for EPOS, DAAD will contact you to complete the scholarship application through the DAAD Portal. Do not send a separate EPOS application to DAAD before that stage.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Ruhr DAAD EPOS Scholarship 2028?',
  '30 September 2027 for candidates applying for a DAAD-EPOS scholarship, for the 2028–2030 intake. Applicants who do not seek the EPOS scholarship have until 31 December 2027. The call opens on 18 January 2027.'),
 ('How much is the DAAD-EPOS stipend?',
  'Current guides cite €992 a month; older pages cite €934. This article reports both and leads with the current figure. The scholarship also covers insurance, a travel allowance, a rent subsidy and family allowances where applicable.'),
 ('Do I apply to DAAD or to the university first?',
  'To the university first. Apply to the MADM programme at Ruhr University Bochum through its online platform; candidates recommended for EPOS are then contacted by DAAD to complete the DAAD Portal stage.'),
 ('Is there any tuition fee?',
  'No tuition fee. Students pay a modest semester registration fee, currently around €362, which also covers a regional public transport pass.'),
 ('Who is the EPOS scholarship for?',
  'Professionals from developing and newly industrialised countries with a relevant Bachelor’s degree and at least two years of relevant professional experience after it. Fresh graduates can apply to the programme itself with at least one month of relevant practical experience, but not for the EPOS scholarship.'),
 ('Is the programme taught in English, and is IELTS required?',
  'Yes, the programme is taught entirely in English. Certified English proficiency is required unless you qualify for an exemption; IELTS 6.0 and TOEFL iBT 79–80 are among the accepted minimum levels.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against DAAD's own programme page (daad.de, Master of Arts in Development Management: application deadlines for the 2028-30 intake are 30 September 2027 for DAAD-EPOS candidates and 31 December 2027 for all other candidates) and the IEE's own MADM page (development-research.org: call opens 18 January 2027; same two deadlines; applications directly to the university via the online MADM Application Platform; 2-month internship after the first semester; field research after the second semester; thesis in the third) plus Global Scholarship Hub (DAAD-EPOS deadline 30 September 2027; other applicants 31 December 2027; IELTS 6.0 / TOEFL iBT 79-80; 3 semesters, 90 ECTS; apply to the course first, DAAD contacts recommended candidates) and O4af (stipend €992/month; insurance; travel allowance; rent subsidy; family allowances; Bachelor's in a related field at second class upper or equivalent; 2+ years' relevant experience for EPOS; employer reintegration guarantee preferred). CONFLICTS: (1) Stipend is €992 in current guides but €934 on older pages — the article states both and leads with the current figure. (2) One aggregator gives the programme as open to "all countries" for EPOS, while the EPOS design targets developing/newly industrialised countries — the article keeps the two routes distinct. (3) A third-party listing gives a 15 October 2027 deadline; the DAAD and IEE pages both give 30 September 2027 for EPOS, and the article follows them.</p>''',
 dl_long='30 September 2027 for DAAD-EPOS applicants (2028–2030 intake opens 18 January 2027); 31 December 2027 for self-financed applicants',
 offlinks=[('DAAD — MA in Development Management, Ruhr University Bochum (official)', 'https://www.daad.de/deutschland/studienangebote/international-programmes/en/detail/3848/'),
           ('Institute of Development Research and Development Policy — MADM (official)', 'http://www.development-research.org/index.php/studies/ma-in-development-management-madm'),
           ('Global Scholarship Hub — MA in Development Management 2028–2030', 'https://www.globalscholarshipshub.com/opp/ma-development-management-ruhr-university-bochum/')],
 related_titles=['ttup-2027', 'eth-fellows-2027', 'qa-ug-2026', 'anu-chanc-2026'])),

# ---------------------------------------------------------------- 4. Qatar Airways UG
A.append(dict(
 slug='qatar-airways-university-undergraduate-scholarship-2026',
 title='Qatar Airways University Undergraduate Scholarship 2026 (Fully Funded)',
 meta='Qatar Airways University Undergraduate Scholarship 2026: full undergraduate funding — tuition, stipend, accommodation, insurance and travel — for Qatari nationals and children of a Qatari mother, with a five-year service commitment after graduation. No fixed deadline is published; apply through the Qatar Airways scholarship portal.',
 short='Qatar Airways UG Scholarship 2026', kicker='Qatar · Undergraduate · Fully Funded', mono='QA',
 prov_short='Qatar Airways', prov_cat='Airline · Qatar',
 h1='Qatar Airways University Undergraduate Scholarship 2026 (Fully Funded)',
 sub='Correct the title first, because it misleads most readers: despite the “international students” label on aggregator pages, this is not a scholarship the world can apply for. It is Qatar Airways’ national scholarship for Qatari nationals and children of a Qatari mother — a full undergraduate sponsorship, in Qatar or at an approved university abroad, that ends in a guaranteed job with the airline and a five-year service commitment. There is no single published closing date: the programme’s own pages say dates are announced annually and advise applying as early as possible, so treat it as rolling and check the portal for the current year’s timeline rather than trusting any single date on a third-party page. The money is real — tuition, a monthly stipend, living costs, accommodation, health insurance and travel — but no cash figure for the stipend is published, and this article does not invent one.',
 facts=facts([
  ('Provider', 'Qatar Airways (National Scholarship Programme)'),
  ('Award', 'Full undergraduate funding for up to 4 years: tuition, monthly stipend, living costs, accommodation, health insurance, travel (no stipend figure published)'),
  ('Level', 'Undergraduate (Bachelor’s degree only)'),
  ('Deadline', 'No fixed deadline published — annual programme; dates announced on the official portal; apply as early as possible'),
  ('Eligibility', 'Qatari nationals or children of a Qatari mother ONLY; aged 17–24; high school within last 3 years; 85% / 90%; IELTS 5.5 / 6.0; approved major + accredited university; Qatari guarantor'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>Qatar Airways runs a national university scholarship programme that sponsors young Qataris through a full Bachelor’s degree, either at a university in Qatar or at an approved university abroad — in the United Kingdom, the United States, Canada, Australia, New Zealand or another country recognised by Qatar Airways and Qatar’s Ministry of Education. It is a sponsorship, not just a grant: scholars are selected competitively, sign a scholarship contract with the airline together with a Qatari guarantor, and on graduation enter the airline’s Graduate Development Programme. The trade-off is explicit and long: a minimum of five years’ work with Qatar Airways after graduation, in an assigned role and location, with no immediate move to a Master’s degree afterwards.</p>
      <p>The eligibility rules are narrow by design, and several aggregator pages blur them. The programme is for Qatari nationals and children of a Qatari mother only; children of Qatari mothers are reviewed for local universities within Qatar, not for overseas study. The academic bar is a high-school average of 85% for Qatari nationals and 90% for children of Qatari mothers, with an IELTS score of 5.5 or 6.0 respectively. One aggregator instead describes continuing university students with a 2.8 GPA and 30 credit hours — that describes a different stage of the programme, not the school-leaver route in this article, and applicants should confirm which route fits them on the portal.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for the Bachelor’s degree, at a Ministry-accredited university on the approved list.</li>
        <li><strong>Monthly stipend and living costs</strong>, plus accommodation — the programme covers the cost of living, but no stipend amount is published in the sources checked, so no figure is stated here.</li>
        <li><strong>Health insurance and travel</strong>, including visa and travel costs to the country of study.</li>
        <li><strong>Training and internships</strong> with Qatar Airways during the degree, and pre-approval support for overseas study.</li>
        <li><strong>Guaranteed career path:</strong> entry to the Graduate Development Programme on graduation — and the matching obligation of at least five years’ service with the airline.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>Nationality:</strong> Qatari nationals, or children of a Qatari mother. Children of Qatari mothers must have completed their entire education in Qatar, and their applications are reviewed for local study in Qatar only.</li>
        <li><strong>Age and schooling:</strong> aged 17–24 at the time of application, with high school completed within the last three years.</li>
        <li><strong>Grades:</strong> a minimum high-school overall score of 85% for Qatari nationals and 90% for children of Qatari mothers. Certificates issued outside Qatar need a Ministry of Education equivalency statement.</li>
        <li><strong>English:</strong> a recent IELTS score (within the last 24 months) — 5.5 overall with no component below 5.0 for Qatari nationals, 6.0 overall with no component below 5.0 for children of Qatari mothers.</li>
        <li><strong>Study plan:</strong> a Bachelor’s degree only, in English, in a major on Qatar Airways’ accepted list, at a university accredited by Qatar’s Ministry of Education. Overseas study needs a pre-approval letter from the Ministry.</li>
        <li><strong>Conduct and status:</strong> good conduct, medically fit, not currently employed or sponsored by another entity, not previously removed from a Qatar Airways scholarship or job — and a Qatari guarantor who agrees to repay Qatar Airways if the scholar fails or withdraws.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Passport and Qatar ID</strong> — colour copies for the student and for the guarantor, plus a recent passport photo.</li>
        <li><strong>High-school certificate or equivalency</strong>, with subject grades and completion date.</li>
        <li><strong>IELTS certificate</strong>, taken within the last 24 months.</li>
        <li><strong>Unconditional university acceptance letter</strong>, with the major, courses, fees and study dates, plus a pre-approval letter from the Ministry of Education if studying abroad.</li>
        <li><strong>National Service certificate</strong> (male applicants: completion, deferment or exemption) and “to whom it may concern” letters confirming you are not under another scholarship (Ministry of Education) and not employed (Ministry of Labour).</li>
        <li><strong>For children of Qatari mothers:</strong> the mother’s ID, a birth certificate, and a Ministry of Education certificate confirming all schooling took place in Qatar.</li>
        <li><strong>After shortlisting:</strong> police clearance, medical tests, the guarantor’s salary or pension certificate, and a bank IBAN certificate, before the scholarship contract is signed.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Check every criterion against the official portal first — nationality basis, age, grades, IELTS score and approved major — because Qatar Airways reviews applications competitively rather than accepting every qualified applicant.</li>
        <li>Write and submit a Letter of Interest to Qatar’s Ministry of Education. This is a required first step, distinct from the university application itself.</li>
        <li>Gather all documents in advance in JPEG, PNG, PDF or Word format, and secure your unconditional university offer and, for overseas study, the Ministry pre-approval letter.</li>
        <li>Upload everything to the Qatar Airways scholarship portal. There is no fixed deadline published — dates are announced annually — so apply as early as possible and confirm the current year’s timeline on the portal.</li>
        <li>If shortlisted, attend the Qatar Airways interview and complete police clearance, medical tests and guarantor verification, then sign the scholarship contract with your guarantor.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Can international students apply for the Qatar Airways University Scholarship?',
  'No — not in the general sense. It is open only to Qatari nationals and children of a Qatari mother. Aggregator pages that label it an “international students” scholarship are misleading; the nationality rule is the first eligibility test.'),
 ('What is the deadline for the Qatar Airways University Scholarship 2026?',
  'No fixed deadline is published. The programme runs annually with dates announced on the official portal, and applicants are advised to apply as early as possible. Do not trust a single date from a third-party page.'),
 ('What does the scholarship cover?',
  'Full undergraduate funding for up to four years: tuition fees, a monthly stipend, living costs, accommodation, health insurance and travel. No stipend amount is published in the sources checked, so none is stated here.'),
 ('What must scholars do after graduation?',
  'Join Qatar Airways immediately under the Graduate Development Programme and work for a minimum of five years in an assigned role and location. An immediate Master’s degree afterwards is not part of the deal.'),
 ('What grades and IELTS score do I need?',
  'A high-school average of 85% for Qatari nationals or 90% for children of Qatari mothers, and a recent IELTS score of 5.5 overall (nationals) or 6.0 overall (children of Qatari mothers), with no component below 5.0.'),
 ('Do I need a guarantor?',
  'Yes — a Qatari guarantor who formally agrees to repay Qatar Airways if you fail or withdraw from the scholarship. The guarantor’s passport, Qatar ID and salary or pension details are part of the file.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against ScholarWaka (Qatari nationals or children of a Qatari mother; 17-24; high school within 3 years; 85% / 90%; IELTS 5.5 / 6.0 within 24 months, no component below 5.0; approved major; Ministry-accredited university; pre-approval for overseas study; Qatari guarantor; Letter of Interest to the Ministry of Education as a required first step; interview, police clearance, medical tests, guarantor salary/pension certificate, bank IBAN, scholarship contract) plus After School Africa (full tuition, monthly stipend, living costs, accommodation, health insurance, visa/travel; up to 4 years; 5-year Graduate Development Programme commitment) and ScholarshipsAds (same eligibility set; unconditional offer required; not employed/sponsored; guarantor required). CONFLICTS: (1) Aggregator pages labelling this an "international students" scholarship are wrong — the programme is Qatari nationals and children of Qatari mothers only, and the article leads with that correction. (2) One aggregator describes continuing students with GPA 2.8 and 30 credit hours — that is a different stage/route from the school-leaver criteria used here, and the article flags it rather than merging the two. (3) No fixed deadline is published on the official programme pages; aggregator dates are not used, and the article states the rolling/annual position honestly.</p>''',
 dl_long='No fixed deadline published — annual programme; dates are announced on the official Qatar Airways portal, so apply as early as possible and confirm the current year’s timeline there',
 offlinks=[('Qatar Airways — University Scholarship (official portal)', 'https://www.qatarairways.com/en/nationalisation/university-scholarship-high-school.html'),
           ('ScholarWaka — Qatar Airways University Scholarship Programme', 'https://scholarwaka.com/qatar-airways-university-scholarship-programme/'),
           ('After School Africa — Qatar Airways University Scholarships', 'https://www.afterschoolafrica.com/99098/qatar-airways-university-scholarships/')],
 related_titles=['ttup-2027', 'eth-fellows-2027', 'ruhr-epos-2028', 'anu-chanc-2026'])),

# ---------------------------------------------------------------- 5. ANU Chancellor's
A.append(dict(
 slug='anu-international-chancellors-scholarship-2026-australia',
 title='ANU International Chancellor’s Scholarship 2026 in Australia (Funded)',
 meta='ANU International Chancellor’s Scholarship 2026: a 25% or 50% tuition fee reduction for the whole degree, plus guaranteed first-year accommodation, for commencing international Bachelor’s and Master’s coursework students. No separate application — automatic assessment on admission; aggregators report a 15 December 2026 admission cutoff.',
 short='ANU Chancellor’s Scholarship 2026', kicker='Australia · Undergraduate & Master’s · Funded', mono='ANU',
 prov_short='Australian National University', prov_cat='University · Australia',
 h1='ANU International Chancellor’s Scholarship 2026 in Australia (Funded)',
 sub='Two corrections before anything else. First, this is not a flat dollar award: the Australian National University’s own page gives the value as a percentage — a 25% or 50% reduction in tuition fees for the entire degree — and the “up to $25,000 a year” figure repeated by aggregator pages is not the university’s formulation, so this article does not use it. Second, there is no scholarship form and no scholarship deadline: every eligible international applicant is automatically assessed when they apply for admission, and the 15 December 2026 date on third-party pages is an admission cutoff for the current round, not a scholarship-form deadline. It is also a partial award, not full funding, and it is for Bachelor’s and Master’s coursework students — not for PhD applicants.',
 facts=facts([
  ('Provider', 'Australian National University (ANU), Canberra, Australia'),
  ('Award', '25% or 50% tuition fee reduction for the entire degree + guaranteed first-year accommodation if chosen; reduced tuition deposit AUD 10,000 (partial — not fully funded)'),
  ('Level', 'Undergraduate and postgraduate coursework (Bachelor’s / Master’s) — NOT PhD'),
  ('Deadline', 'No separate scholarship deadline — automatic assessment on admission; aggregators report a 15 December 2026 admission cutoff for the current round'),
  ('Eligibility', 'Commencing international (overseas) students with an ANU offer, selected on academic merit; no prior award at the same level; no external tuition sponsorship; excludes MChD and MMDS'),
 ]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The ANU Chancellor’s International Scholarship is the Australian National University’s flagship merit award for commencing international students, designed to attract high-achieving students from around the world to its Canberra campus. It is distributed across nine categories, with at least one category open to applicants from anywhere in the world: alongside the general undergraduate and postgraduate categories, there are dedicated categories for India, Indonesia and Vietnam, and regional categories for South East Asia and for Europe, Central and South Americas. Applicants are always assessed first for the highest-value award for which they are eligible, and the categories carry different values — the general undergraduate and postgraduate categories and the India, Indonesia and Vietnam categories offer 25%, while the South East Asia and Europe, Central and South Americas categories offer 25% or 50%.</p>
      <p>Up to 200 scholarships are available across the undergraduate and postgraduate levels. Selection is purely on academic merit: ANU converts academic results to a common scale and ranks applicants, so those with the strongest records receive the highest value available for their region or category. Because the award is a percentage of tuition, its cash value depends on the programme’s fees — with international tuition routinely above AUD 45,000 a year at ANU, even the 25% tier is a substantial sum over a full degree, and the 50% tier more so. It is still only a partial award: living costs, travel and insurance are not covered.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition fee reduction:</strong> 25% or 50% off tuition fees for the entire duration of the degree, depending on the category — not a flat dollar amount.</li>
        <li><strong>Guaranteed first-year accommodation:</strong> recipients who choose the benefit are assured on-campus accommodation for their first year of study.</li>
        <li><strong>Reduced deposit:</strong> recipients pay a reduced tuition deposit of AUD 10,000 instead of the standard amount in the admissions offer letter.</li>
        <li><strong>No separate application:</strong> there is no scholarship form, no scholarship essay and no extra fee — assessment is automatic on your admission application.</li>
        <li><strong>Separate scholarship offer:</strong> if you are selected, you receive a scholarship offer separately from your academic offer, and you must accept both separately.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li><strong>International students:</strong> you must be classified as an overseas student under the Education Services for Overseas Students Act 2000, and you must have received an offer of admission to commence at ANU in an eligible programme.</li>
        <li><strong>Level:</strong> commencing undergraduate or postgraduate coursework students — Bachelor’s and Master’s coursework degrees. This is not a PhD or research-degree scholarship.</li>
        <li><strong>Excluded programmes:</strong> the Doctor of Medicine and Surgery (MChD) and the Master of Military and Defence Studies are not eligible.</li>
        <li><strong>Academic merit:</strong> selection is on academic merit alone, ranked on a common scale. You must meet all conditions of the programme you have an offer for, including any onshore requirements.</li>
        <li><strong>Exclusions:</strong> you must not hold a 995 visa (unless enrolling in an eligible postgraduate programme), must not have received the same award previously at the same level of study, and must not hold external sponsorship covering all or part of your tuition fees.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li><strong>Admission documents:</strong> there are no separate scholarship documents. You submit the standard documents required for admission to ANU — academic transcripts, passport, and proof of English proficiency (IELTS, TOEFL or equivalent) as specified in the admission application.</li>
        <li><strong>Offer of admission:</strong> you must hold an offer for an eligible programme before the scholarship assessment can produce an offer of its own.</li>
        <li>Accept the academic offer and the scholarship offer separately, as instructed in each letter.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to an eligible undergraduate or postgraduate coursework programme at ANU through the official ANU application portal. There is no separate scholarship form to complete.</li>
        <li>Your application is automatically assessed across the nine Chancellor’s categories, starting with the highest-value award for which your citizenship makes you eligible.</li>
        <li>Watch the admission timeline: third-party listings report a <strong>15 December 2026</strong> cutoff for the current round. The university’s own page publishes no separate scholarship deadline, so confirm the live admission dates on the ANU scholarships page before you rely on that date.</li>
        <li>If selected, you receive a scholarship offer separately from your academic offer. Accept both, pay the reduced AUD 10,000 tuition deposit, and choose whether to take up the guaranteed first-year accommodation.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the ANU Chancellor’s Scholarship 2026?',
  'There is no separate scholarship deadline, because there is no separate scholarship application — you are automatically assessed when you apply for ANU admission. Third-party listings report a 15 December 2026 admission cutoff for the current round; confirm the live admission dates on ANU’s own scholarships page.'),
 ('How much is the scholarship worth?',
  'A 25% or 50% reduction in tuition fees for the entire degree, depending on your category — not a flat dollar amount. The “up to $25,000 a year” figure on aggregator pages is not the university’s formulation and is not used here.'),
 ('Is it fully funded?',
  'No. It is a partial award: it reduces tuition only. Living costs, travel and insurance are not covered, although first-year on-campus accommodation is guaranteed if you choose that benefit.'),
 ('Can PhD students apply?',
  'No. The Chancellor’s International Scholarship is for commencing undergraduate and postgraduate coursework students (Bachelor’s and Master’s). Research-degree applicants should look at ANU’s research scholarships instead.'),
 ('Do I need to submit a separate scholarship application?',
  'No. Every eligible international admission applicant is automatically considered, and applicants are always assessed first for the highest-value award for which they are eligible.'),
 ('Which programmes are excluded?',
  'The Doctor of Medicine and Surgery (MChD) and the Master of Military and Defence Studies. Every other eligible ANU programme is in scope, subject to the category rules.'),
]) + '''
      <p class="verify">Verified 29 Oct 2026 against ANU's own scholarships page (study.anu.edu.au, ANU Chancellor's International Scholarship: 9 categories with at least one open to students from anywhere; applicants automatically assessed, always first for the highest-value award for which they are eligible; Undergraduate 25%, Postgraduate 25%, India 25%, Indonesia 25%, Vietnam 25%, South East Asia 25% or 50%, Europe/Central & South Americas 25% or 50%; field of study any eligible programme except Doctor of Medicine and Surgery and Master of Military and Defence Studies) plus After School Africa (overseas students under the ESOS Act 2000; offer of admission required; no 995 visa except eligible postgraduate; no prior award at the same level; no external tuition sponsorship; selection purely on academic merit on a common scale; 200 scholarships; guaranteed first-year accommodation; reduced AUD 10,000 deposit) and ScholarWaka (25% or 50% for the full duration; no separate deadline, automatically considered on admission; 15 December reported as the round date). CONFLICTS: (1) Aggregators' "up to $25,000/year" flat figure is NOT the official formulation — the article uses the official 25%/50% percentage. (2) The 15 December 2026 date is an aggregator-reported admission cutoff, not a scholarship-form deadline on ANU's page — the article states it as reported and tells readers to confirm live admission dates officially. (3) Some aggregator pages include PhD in the levels — the official page's categories are undergraduate and postgraduate coursework, and the article excludes PhD applicants.</p>''',
 dl_long='No separate scholarship deadline — automatic assessment on admission; aggregators report a 15 December 2026 admission cutoff for the current round (confirm the live admission dates on ANU’s official scholarships page)',
 offlinks=[('Australian National University — Chancellor’s International Scholarship (official)', 'https://study.anu.edu.au/scholarships/find-scholarship/anu-chancellors-international-scholarship'),
           ('After School Africa — ANU Chancellor’s International Scholarship', 'https://www.afterschoolafrica.com/100203/anu-chancellors-international-scholarship-2026/'),
           ('ScholarWaka — ANU Chancellor’s International Scholarship', 'https://scholarwaka.com/australian-national-university-anu-chancellors-international-scholarship-2025-in-australia/')],
 related_titles=['ttup-2027', 'eth-fellows-2027', 'ruhr-epos-2028', 'qa-ug-2026'])),

DPILLS = {
 'texas-tech-university-presidential-merit-scholarship-2027-usa': 'Deadline 1 Apr 2027 · %d days left' % dl_left('2027-04-01'),
 'eth-zurich-postdoctoral-fellowship-2027-switzerland': 'Deadline 1 Mar 2027 · %d days left' % dl_left('2027-03-01'),
 'ruhr-university-daad-epos-scholarships-2028-germany': 'Deadline 30 Sep 2027 · %d days left' % dl_left('2027-09-30'),
 'qatar-airways-university-undergraduate-scholarship-2026': 'Rolling · no fixed deadline published',
 'anu-international-chancellors-scholarship-2026-australia': 'Admission cutoff 15 Dec 2026 (reported) · %d days left' % dl_left('2026-12-15'),
}

for a in A:
    a['dpill'] = DPILLS[a['slug']]
    _split_verify(a)
    n = build_article(BASE, OUT, a, CARDS)
    print('built', a['slug'], n)

# validate
import html.parser as _hp
bad = []
for a in A:
    p = OUT / (a['slug'] + '.html')
    txt = p.read_text()
    class P(_hp.HTMLParser):
        def __init__(self):
            super().__init__(); self.err = None
        def error(self, m): self.err = m
    pp = P(); pp.feed(txt)
    if 'AICTE Pragati' in txt or 'Lorem' in txt:
        bad.append((a['slug'], 'leftover template text'))
    if pp.err:
        bad.append((a['slug'], pp.err))
print('validation issues:', bad if bad else 'none')
print('done')

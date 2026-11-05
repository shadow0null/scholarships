#!/usr/bin/env python3
"""Batch 48 (cron run 48, 25 Oct 2026): 5 new verified articles.

Queue scan order (next entries not in done/skipped, file order):
1. Chulalongkorn University Scholarships 2027 — SKIPPED: deadline passed
   (10 October 2026 per Bright Scholarship, NSP Scholarships and
   Next Scholar Grant; one guide says the 2027 call is not yet announced
   and aggregators mention a second-semester intake, but no official
   2027 call is published — unresolved, so skipped rather than published).
2. University of Southampton Scholarships 2027 — VERIFIED: general
   deadline 13 January 2027, 18:00 UK time; official awards confirmed
   on southampton.ac.uk (£7,000 75th Anniversary award, £10,000 Global
   Talent Award, £10,000 GREAT Scholarships).
3. United Nations Townhall Youth Fellowship 2026 — SKIPPED: deadline
   passed (7 September 2026, 11:59 p.m. ET).
4. Stigler Center Journalists Residence Program 2027 — SKIPPED: deadline
   passed (20 September 2026, 11:59 p.m. CT).
5. Leiden University Excellence Scholarships 2027 — VERIFIED (official
   Leiden pages): deadline 1 December 2026; €10,000–€19,000 tuition
   reduction, ~25 awards. CORRECTION: one listing gives 1 February 2027
   — the official Leiden scholarship pages list 1 December 2026, which
   the article uses and flags.
6. Erasmus Mundus MAPP Scholarship 2027 — VERIFIED (official
   mundusmapp.org): deadline 1 December 2026, 23:59 CET; €1,400/month
   up to €33,600, full tuition waiver, 4 universities, 4 tracks,
   admissions centrally via CEU. CORRECTION: the official programme site
   is mundusmapp.org, not mundus-mapp.eu.
7. UniSQ International PhD Scholarship 2027 — SKIPPED: deadline passed
   (27 September 2026).
8. CERN Doctoral Student Program 2027 — SKIPPED: deadline passed
   (16 October 2026, 23:59 Geneva time).
9. Monash University ReDiLEEP PhD Scholarship 2027 — VERIFIED: deadline
   30 October 2026, 12:00 noon Melbourne time; email Dr Giulia Ghedini
   with 2-page motivation letter + 2-page CV; must then compete for a
   Monash graduate research scholarship. NOT formally an MSCA Doctoral
   Candidate position (Monash is outside the EU) — stated plainly.
10. Stanford University Hoover Fellowship 2027 — VERIFIED (official
    hoover.org): deadline 17 November 2026, 11:59 p.m. PT; $169,950–
    $230,000 base salary + $20,000 housing allowance; 1–3 years;
    no teaching; PhD or expected by 1 September 2027.

Run from /home/hatch/workspace/scholarships-17k/.
"""
import json, pathlib, html.parser, re
import re as _re
from datetime import date

TODAY = date(2026, 10, 25)
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
 'southampton-2027': {'mono': 'SO', 'title': 'University of Southampton Scholarships 2027 in UK (Funded)',
   'href': 'university-of-southampton-scholarships-2027-uk.html',
   'dpill': 'Deadline 13 Jan 2027 · %d days left' % dl_left('2027-01-13'),
   'award': 'A range of international awards for Bachelor\u2019s, Master\u2019s and PhD study, including a \u00a37,000 automatic postgraduate award, a \u00a310,000 Global Talent Award and \u00a310,000 GREAT Scholarships.',
   'elig': 'International students with an offer to study at Southampton; the largest automatic award is limited to permanent residents of Bangladesh, Malaysia, Pakistan, Thailand, UAE, USA or Vietnam.',
   'tags': [('Bachelor\u2019s, Master\u2019s & PhD', 'blue'), ('UK', 'teal')]},
 'leiden-lexs-2027': {'mono': 'LX', 'title': 'Leiden University Excellence Scholarships 2027 in Netherlands (Funded)',
   'href': 'leiden-university-excellence-scholarships-2027-netherlands.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': '\u20ac10,000\u2013\u20ac19,000 towards tuition fees for an eligible full-time Master\u2019s programme, in five fixed tiers; around 25 awards a year from more than 1,000 applications.',
   'elig': 'Non-EEA/non-EFTA nationals admitted to an eligible full-time Master\u2019s starting September 2027, with academic results around the top 10% of their previous programme.',
   'tags': [('Master\u2019s', 'blue'), ('Netherlands', 'teal')]},
 'mapp-2027': {'mono': 'MM', 'title': 'Erasmus Mundus MAPP Scholarship 2027 (Fully Funded)',
   'href': 'erasmus-mundus-mapp-scholarship-2027.html',
   'dpill': 'Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
   'award': 'Up to \u20ac33,600 over 24 months (\u20ac1,400 a month) plus a full tuition waiver and health insurance, for a two-year joint Master\u2019s in Public Policy across two European countries.',
   'elig': 'All nationalities, EU and non-EU, with a Bachelor\u2019s degree in a relevant social-science field and strong English; one mobility track only, applied for centrally through CEU.',
   'tags': [('Master\u2019s', 'blue'), ('Europe', 'teal')]},
 'monash-redileep-2027': {'mono': 'MR', 'title': 'Monash University ReDiLEEP PhD Scholarship 2027 in Australia (Funded)',
   'href': 'monash-university-redileep-phd-scholarship-2027-australia.html',
   'dpill': 'Deadline 30 Oct 2026 · %d days left' % dl_left('2026-10-30'),
   'award': 'A funded PhD project on response diversity in marine phytoplankton, with tuition and a living stipend through a Monash graduate research scholarship, plus participation in the international ReDiLEEP doctoral network.',
   'elig': 'All nationalities with a Master\u2019s or equivalent in biology, ecology, marine biology, environmental science or a related field, at First Class Honours or equivalent Master\u2019s standard.',
   'tags': [('PhD', 'purple'), ('Australia', 'teal')]},
 'hoover-2027': {'mono': 'HV', 'title': 'Stanford University Hoover Fellowship 2027 for Early Career Researchers (Paid)',
   'href': 'stanford-university-hoover-fellowship-2027-usa.html',
   'dpill': 'Deadline 17 Nov 2026 · %d days left' % dl_left('2026-11-17'),
   'award': 'A 12-month base salary of $169,950\u2013$230,000 plus a $20,000 annual housing allowance, for 1\u20133 years of full-time research with no teaching duties at the Hoover Institution.',
   'elig': 'Early-career scholars with a PhD or equivalent, or expecting to complete one by 1 September 2027, in economics, history, international relations, national security, political science or public policy.',
   'tags': [('Postdoc & research', 'purple'), ('USA', 'teal')]},
}

CARDS = dict(REGISTRY); CARDS.update(NEW_CARDS)

A = []

# ---------------------------------------------------------------- 1. Southampton
A.append(dict(
 slug='university-of-southampton-scholarships-2027-uk',
 title='University of Southampton Scholarships 2027 in UK (Funded)',
 meta='University of Southampton Scholarships 2027: funding for international Bachelor\u2019s, Master\u2019s and PhD students, including the \u00a37,000 75th Anniversary award, the \u00a310,000 Global Talent Award and \u00a310,000 GREAT Scholarships. General deadline 13 January 2027 — eligibility, awards, documents, how to apply and FAQs.',
 short='University of Southampton Scholarships 2027', kicker='UK · Bachelor\u2019s, Master\u2019s & PhD · Funded', mono='SO',
 prov_short='University of Southampton', prov_cat='University · United Kingdom',
 h1='University of Southampton Scholarships 2027 in UK (Funded)',
 sub='The University of Southampton Scholarships 2027 cover international students at Bachelor\u2019s, Master\u2019s and PhD level, through a mix of automatic merit awards and competitive scholarships. The headline awards are the \u00a37,000 75th Anniversary Global Postgraduate Excellence Scholarship, the \u00a310,000 Dean of Faculty Global Talent Award and the \u00a310,000 GREAT Scholarships. The general deadline given in the 2027 listings is 13 January 2027 at 18:00 UK time — but the individual awards carry their own dates, and some close later, so read the award-by-award dates in this article rather than relying on the single headline date.',
 dpill='Deadline 13 Jan 2027 · %d days left' % dl_left('2027-01-13'),
 facts=facts([('Award', 'There is no single Southampton scholarship amount: the 2027 package is a set of awards. The 75th Anniversary Global Postgraduate Excellence Scholarships give a £7,000 reduction in tuition fees to eligible international postgraduate taught students, awarded automatically with no separate application. The Dean of Faculty of Engineering and Physical Sciences Global Talent Award gives up to five students a £10,000 tuition fee reduction. The GREAT Scholarships, run with the British Council and the GREAT Britain Campaign, give £10,000 towards tuition fees for one-year postgraduate taught programmes in the Faculty of Arts and Humanities. Some awards are automatic; competitive ones need a separate form after you hold an offer.'),
              ('Eligible', 'International students who pay overseas tuition fees and hold an offer for an eligible Southampton programme. The 75th Anniversary award is limited to permanent residents of Bangladesh, Malaysia, Pakistan, Thailand, UAE, USA or Vietnam who are self-funded and hold a conditional or unconditional offer for a full-time, on-campus, one-year postgraduate taught programme (Southampton Business School programmes are excluded, as the Business School runs its own scholarships). The Global Talent Award is for international students starting an eligible full-time, on-campus postgraduate taught programme in the Faculty of Engineering and Physical Sciences who exceed their course entry requirements. The GREAT Scholarships are for students holding a USA passport and permanent residence in the USA, on a one-year in-person postgraduate taught course in Arts and Humanities. PhD funding follows a separate studentship route — identify supervisors and research funding deadlines well before your planned start.'),
              ('How', 'Apply for admission first: undergraduate applicants apply through UCAS, while Master\u2019s and PhD applicants apply directly to Southampton. Some awards are automatic — if you are eligible you are awarded without a separate form and notified by email. For competitive awards, submit the separate scholarship application form after receiving your offer; the Global Talent Award, for example, asks for a supporting statement of up to 250 words. Do not wait for the final admission deadline: scholarship and funding deadlines can fall months before a programme starts, and popular courses can close early.'),
              ('Deadline', 'The general deadline given in the 2027 scholarship listings is 13 January 2027 at 18:00 UK time — but treat it as a planning date, not a single closing time: individual courses and funding awards have their own deadlines, and medicine and other early-deadline courses close sooner. The GREAT Scholarships close on 30 April 2027 at 5:00 p.m. UK time, with offer conditions to be met by 30 June 2027. The Global Talent Award also closes on 30 April 2027 at 5:00 p.m. UK time. For the 75th Anniversary award, the key date is the tuition fee deposit: pay it by Saturday 31 July 2027.'),
              ('Fine print', 'These are tuition-fee reductions, not full funding: none of the awards above covers living costs, travel or visa costs, and none is described as fully funded. The 75th Anniversary award is a one-off £7,000 reduction, and the Global Talent and GREAT awards are one-off £10,000 reductions. Awards cannot be assumed to stack — check with Southampton\u2019s scholarships team whether two awards can be held together. Programmes at the Malaysia and Delhi campuses, distance-learning courses, partner-institution study, study-abroad and exchange routes are excluded from the Global Talent Award.')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of Southampton</strong> is a research-intensive university on England\u2019s south coast, and its international funding for 2027 entry is deliberately split into two kinds of award. Some are <strong>automatic merit prizes</strong>: if you meet the conditions and hold an offer, the university awards them without a separate application. Others are <strong>competitive awards</strong> that need an extra form, a short supporting statement and, in some cases, a separate deadline after you have your offer. Knowing which kind you are chasing matters more than the headline amounts, because the automatic awards reward the offer itself while the competitive ones reward a written case.</p>
      <p>The 2027 listings quote a single general deadline — <strong>13 January 2027 at 18:00 UK time</strong> — but that date is best read as the planning deadline for the scholarship round as a whole. The university\u2019s own award pages give their own dates: the GREAT and Global Talent awards close on 30 April 2027, and the 75th Anniversary award turns on a fee-deposit date of 31 July 2027. Medicine and other early-UCAS courses have earlier deadlines again. Apply for admission early, then check each award\u2019s own page.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Be an <strong>international student paying overseas tuition fees</strong> and hold an offer for an eligible Southampton programme.</li>
        <li><strong>75th Anniversary Global Postgraduate Excellence Scholarship (£7,000):</strong> be a permanent resident of <strong>Bangladesh, Malaysia, Pakistan, Thailand, UAE, USA or Vietnam</strong>; be self-funded; hold a conditional or unconditional offer for a full-time, on-campus, one-year postgraduate taught programme; and pay your tuition fee deposit by <strong>31 July 2027</strong>. Southampton Business School programmes are excluded.</li>
        <li><strong>Dean of Faculty Global Talent Award (£10,000):</strong> be an international student starting an eligible full-time, on-campus postgraduate taught programme in the <strong>Faculty of Engineering and Physical Sciences</strong>, and exceed your course entry requirements.</li>
        <li><strong>GREAT Scholarships 2027 (£10,000):</strong> hold a <strong>USA passport</strong> and be a <strong>permanent resident of the USA</strong>; hold an offer for a one-year, in-person postgraduate taught programme in the <strong>Faculty of Arts and Humanities</strong>; meet your offer conditions by <strong>30 June 2027</strong>; and be willing to act as an ambassador for UK higher education.</li>
        <li><strong>PhD applicants:</strong> funding is arranged through research studentships and supervisor-led funding, which carry their own deadlines — often months before the PhD start date. Identify supervisors and research groups early.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>£7,000 tuition fee reduction</strong> — 75th Anniversary Global Postgraduate Excellence Scholarship, awarded automatically to eligible students.</li>
        <li><strong>£10,000 tuition fee reduction</strong> — Dean of Faculty of Engineering and Physical Sciences Global Talent Award (up to 5 scholarships).</li>
        <li><strong>£10,000 towards tuition fees</strong> — GREAT Scholarships 2027 for eligible US students in Arts and Humanities, in partnership with the British Council.</li>
        <li><strong>No separate application</strong> for the automatic awards — eligible students are notified by email.</li>
        <li>Access to Southampton\u2019s wider funding: other country-specific and faculty awards exist beyond the three headline awards in this article, so check the university\u2019s scholarships pages for your country and faculty.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A completed <strong>application form</strong> — through UCAS for undergraduate study, or directly to Southampton for postgraduate study.</li>
        <li>A valid <strong>passport</strong>.</li>
        <li>Your <strong>degree certificate</strong> and academic <strong>transcript</strong>.</li>
        <li>A <strong>CV or resume</strong>.</li>
        <li>For competitive awards: a <strong>supporting statement of up to 250 words</strong> — for the Global Talent Award, covering why you chose your course, how it relates to your previous experience and future goals, and how your goals contribute to a more sustainable and inclusive world.</li>
        <li>Any other <strong>supporting documents</strong> your programme or award asks for, such as references or evidence of English language ability.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose your <strong>Bachelor\u2019s, Master\u2019s or PhD programme</strong> and check its own entry requirements and deadline — medicine and some other courses close well before the general date.</li>
        <li><strong>Apply for admission first</strong> — through UCAS for undergraduate programmes, or directly to Southampton for postgraduate programmes.</li>
        <li>Work out whether your award is <strong>automatic or competitive</strong>: the 75th Anniversary award needs no separate form, while the Global Talent Award and GREAT Scholarships need an extra application after you hold an offer.</li>
        <li>For competitive awards, complete the <strong>separate scholarship application form</strong> and upload your supporting statement before that award\u2019s deadline (30 April 2027 for the Global Talent Award and the GREAT Scholarships).</li>
        <li>For the 75th Anniversary award, <strong>accept your offer and pay your tuition fee deposit by Saturday 31 July 2027</strong>.</li>
        <li>Do not wait for the last date: apply early, because scholarship deadlines can fall months before a programme starts and popular courses can close once full.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the University of Southampton Scholarships 2027?',
  'The general deadline given in the 2027 listings is 13 January 2027 at 18:00 UK time. Individual awards have their own dates: the GREAT Scholarships and the Global Talent Award close on 30 April 2027 at 5:00 p.m. UK time, and the 75th Anniversary award depends on paying your tuition fee deposit by 31 July 2027.'),
 ('Are the Southampton scholarships fully funded?',
  'No. The headline awards are tuition fee reductions of £7,000 or £10,000. They do not cover living costs, travel or visa costs, and none is described as fully funded.'),
 ('Do I need to apply separately for the 75th Anniversary scholarship?',
  'No. It is awarded automatically to eligible students — you do not need a separate application. You will be notified by email if you are eligible, provided you accept your offer and pay your tuition fee deposit by 31 July 2027.'),
 ('Which countries are eligible for the 75th Anniversary award?',
  'Permanent residents of Bangladesh, Malaysia, Pakistan, Thailand, UAE, USA or Vietnam. Permanent residency means where you have lived for three or more years before the start of the course.'),
 ('Can PhD students apply for these scholarships?',
  'The awards in this article are mainly for taught undergraduate and postgraduate study. PhD funding at Southampton runs through research studentships and supervisor-led funding, which have their own deadlines — identify supervisors and funding early, as research funds can close months before the PhD start date.')]) + '''
      <p class="verify">Verified 25 Oct 2026: brightscholarship.com/university-of-southampton-scholarships/ — last date 13 January 2027 at 18:00 UK time, apply for admission first, automatic awards versus competitive awards needing a separate form after an offer; scholarinfo.net and scholarshipunion.com — same 13 January 2027 deadline, documents list (passport, degree certificate, transcript, CV); southampton.ac.uk (official) 75th Anniversary Global Postgraduate Excellence Scholarships page — \u00a37,000 tuition reduction, permanent residents of Bangladesh, Malaysia, Pakistan, Thailand, UAE, USA or Vietnam, automatic award, deposit by Saturday 31 July 2027, Business School programmes excluded; southampton.ac.uk (official) Dean of Faculty of Engineering and Physical Sciences Global Talent Award page — \u00a310,000, up to 5 scholarships, deadline 30 April 2027 5 p.m. UK time, applications open October 2026, 250-word supporting statement, exceed course entry requirements; afterschoolafrica.com — GREAT Scholarships 2027 USA, \u00a310,000, Faculty of Arts and Humanities, closes 30 April 2027 5 p.m. UK time, offer conditions by 30 June 2027, British Council partnership.</p>''',
 dl_long='13 January 2027, 18:00 UK time (general deadline; individual awards have their own dates — see below)',
 offlinks=[('University of Southampton — Scholarships (official)', 'https://www.southampton.ac.uk/study/fees-funding/scholarships/global-excellence'),
           ('Bright Scholarship — University of Southampton Scholarships 2027', 'https://brightscholarship.com/university-of-southampton-scholarships/')],
 related_titles=['warwick-2027', 'cardiff-vc-2027', 'dundee-ge', 'st-andrews-pg-2027'])),

# ---------------------------------------------------------------- 2. Leiden LExS
A.append(dict(
 slug='leiden-university-excellence-scholarships-2027-netherlands',
 title='Leiden University Excellence Scholarships 2027 in Netherlands (Funded)',
 meta='Leiden University Excellence Scholarship (LExS) 2027: \u20ac10,000\u2013\u20ac19,000 towards tuition for outstanding non-EEA Master\u2019s students at Leiden University, Netherlands. Deadline 1 December 2026 — eligibility, award tiers, documents, how to apply and FAQs.',
 short='Leiden University Excellence Scholarships 2027', kicker='Netherlands · Master\u2019s · Funded', mono='LX',
 prov_short='Leiden University', prov_cat='University · Netherlands',
 h1='Leiden University Excellence Scholarships 2027 in Netherlands (Funded)',
 sub='The Leiden University Excellence Scholarship (LExS) 2027 offers \u20ac10,000 to \u20ac19,000 towards tuition fees for outstanding non-EEA students joining an eligible full-time Master\u2019s programme at Leiden University in the Netherlands. Around 25 scholarships are awarded each year from more than 1,000 applications, so it is one of Europe\u2019s most competitive Master\u2019s awards. Applications for the September 2027 intake close on 1 December 2026 — and you apply through the Master\u2019s admission process itself, not through a separate scholarship form.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'A tuition fee reduction in one of five fixed tiers: €10,000, €15,000, €17,500, €18,500 or €19,000. The award covers tuition fees only — it does not cover living expenses, accommodation, travel, health insurance or visa costs, so you still need a separate financial plan for the Netherlands, including the financial proof Dutch immigration requires. Around 25 scholarships are awarded each year, from more than 1,000 applications. The award runs for the duration of the eligible Master\u2019s programme (one or two years).'),
              ('Eligible', 'You must be a non-EEA/non-EFTA passport holder (UK students are eligible, as the UK is a non-EEA country, unless you were already living in the Netherlands and registered in your Dutch municipality\u2019s BRP before 1 January 2021) and you must not be eligible for Dutch student finance (Studiefinanciering). You must be applying for an eligible full-time Leiden University Master\u2019s programme starting in September 2027 — with the exception of Leiden Law School\u2019s LLM (non-advanced) and MSc programmes. Two exceptions have no nationality restriction: all Advanced LLM programmes and the MSc in International Relations and Diplomacy. Academically, you should have excellent results in a previous programme relevant to your chosen Master\u2019s — as an indication, among the top 10% of graduates in your previous programme. Proof of ranking is not required.'),
              ('How', 'Apply for admission to your chosen Master\u2019s programme through Leiden University\u2019s online application portal (Studielink, then the uSis portal), and indicate your interest in LExS in the scholarships section of the application, uploading a motivation letter of up to 500 words. There is no separate scholarship application form. Each faculty\u2019s selection committee reviews the LExS candidates for its programmes.'),
              ('Deadline', '1 December 2026, for programmes starting in September 2027. This is the date on Leiden University\u2019s own scholarship pages. One listing gives 1 February 2027 instead — that date is not the one Leiden\u2019s scholarship pages carry, so treat 1 December 2026 as the deadline and do not plan around February.'),
              ('Fine print', 'LExS cannot be combined with another full scholarship from an external provider, though it may be combined with a partial scholarship — contact Leiden\u2019s Scholarships Team to confirm your combination. The scholarship is a tuition reduction, not a full ride: even at the highest €19,000 tier you must fund living costs yourself. Decisions are normally communicated in the spring before the September start.')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Leiden University</strong>, founded in 1575, is the oldest university in the Netherlands, with campuses in Leiden and The Hague. The <strong>Leiden University Excellence Scholarship (LExS)</strong> is its flagship merit award for international Master\u2019s students: a tuition reduction of between <strong>\u20ac10,000 and \u20ac19,000</strong>, awarded to roughly <strong>25 students a year</strong> from a field of more than 1,000 applicants. The competition is therefore decided on academic strength — Leiden uses a top-10%-of-previous-programme benchmark as its indication of the level required — and on the quality of a short motivation letter, not on financial need.</p>
      <p>Two things about LExS catch applicants out. First, it is a <strong>tuition-only</strong> award: it does not pay rent, food, insurance, travel or the immigration financial proof, so a strong application still needs a separate living-costs plan. Second, there is <strong>no separate application</strong> — you opt in during the Master\u2019s admission application, which means the scholarship deadline is effectively the admission-application deadline for LExS candidates: <strong>1 December 2026</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>non-EEA/non-EFTA passport</strong> and not be eligible for Dutch student finance (Studiefinanciering). UK students are eligible, unless they were already living in the Netherlands and registered in their Dutch municipality\u2019s BRP before 1 January 2021.</li>
        <li>Apply for an <strong>eligible full-time Leiden University Master\u2019s programme</strong> starting in <strong>September 2027</strong>.</li>
        <li>Note the exclusions: <strong>Leiden Law School\u2019s LLM (non-advanced) and MSc programmes</strong> are not eligible for LExS.</li>
        <li>Note the exceptions with <strong>no nationality restriction</strong>: all <strong>Advanced LLM</strong> programmes and the <strong>MSc in International Relations and Diplomacy</strong> are open to all nationalities.</li>
        <li>Have <strong>excellent academic results</strong> in a previous study programme relevant to your chosen Master\u2019s — as an indication, among the <strong>top 10%</strong> of graduates in your previous programme. Proof of ranking is not required; the figure indicates the level of competitiveness.</li>
        <li>Meet the <strong>admission requirements</strong> of the Master\u2019s programme you choose.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>tuition fee reduction</strong> in one of five tiers: <strong>\u20ac10,000, \u20ac15,000, \u20ac17,500, \u20ac18,500 or \u20ac19,000</strong>.</li>
        <li>The award runs for the <strong>duration of the eligible Master\u2019s programme</strong> (one or two years).</li>
        <li>Study at one of Europe\u2019s oldest research universities, with campuses in <strong>Leiden and The Hague</strong>.</li>
        <li>No separate scholarship form: the award is decided inside your <strong>Master\u2019s admission application</strong>.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>Your <strong>Master\u2019s admission application</strong> through Studielink and Leiden\u2019s uSis portal, including all documents your chosen programme requires (transcripts, degree certificates and any programme-specific material).</li>
        <li>A <strong>motivation letter of up to 500 words</strong> for LExS, submitted in the scholarships section of the application.</li>
        <li>Evidence of your <strong>academic results</strong> — your transcript is the main evidence; a formal ranking certificate is not required.</li>
        <li>Any <strong>English-language evidence</strong> your chosen Master\u2019s programme requires.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Choose an <strong>eligible full-time Leiden Master\u2019s programme</strong> starting in September 2027 and check that it is not one of the excluded Law School programmes.</li>
        <li>Start your application in <strong>Studielink</strong>, then complete it in Leiden\u2019s online application portal (<strong>uSis</strong>).</li>
        <li>In the <strong>scholarships section</strong> of the application, indicate your interest in LExS and upload your <strong>500-word motivation letter</strong>.</li>
        <li>Submit the <strong>complete application before 1 December 2026</strong> — incomplete applications are not processed, and late applications are only considered in exceptional cases at the faculty board\u2019s discretion.</li>
        <li>Wait for the faculty selection committee\u2019s decision, normally communicated in the <strong>spring</strong> before the September start.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Leiden Excellence Scholarship fully funded?',
  'No. LExS covers tuition fees only, in tiers from €10,000 to €19,000. Living expenses, accommodation, travel, insurance and visa costs are not included, and you must show the financial proof Dutch immigration requires.'),
 ('What is the real deadline — 1 December 2026 or 1 February 2027?',
  'Leiden University\u2019s own scholarship pages list 1 December 2026 for the September 2027 intake, and that is the deadline this article uses. One listing gives 1 February 2027 — do not plan around it.'),
 ('Do I need to be in the top 10% of my class?',
  'As an indication, yes: Leiden says applicants should generally be among the top 10% of graduates in their previous programme. Proof of ranking is not required — the figure shows how competitive the award is, with around 25 awards from more than 1,000 applications.'),
 ('Can UK students apply for LExS?',
  'Yes. The UK is a non-EEA country, so UK students are eligible — unless they were already living in the Netherlands and registered in their Dutch municipality\u2019s BRP before 1 January 2021.'),
 ('Can I combine LExS with another scholarship?',
  'No, not with another full scholarship from an external provider. It may be combined with a partial scholarship — contact Leiden\u2019s Scholarships Team to confirm your specific combination.')]) + '''
      <p class="verify">Verified 25 Oct 2026: staff.universiteitleiden.nl (official Leiden scholarship page) and student.universiteitleiden.nl (official) — LExS deadline 1 December 2026, non-EEA/non-EFTA students, exceptions for Advanced LLM and MSc International Relations and Diplomacy, top 10% indication, Law School LLM (non-advanced) and MSc programmes excluded; striveconsultancyhub.com, scholarships365.info, nspscholarships.com, fullscholarships.net, kaistscholarship.com — \u20ac10,000\u2013\u20ac19,000 in five tiers (\u20ac10,000 / \u20ac15,000 / \u20ac17,500 / \u20ac18,500 / \u20ac19,000), around 25 awards a year from more than 1,000 applications, 500-word motivation letter, tuition only, cannot combine with another full external scholarship, UK students eligible; careeraidhub.com gives 1 February 2027 as the deadline — the official Leiden pages list 1 December 2026, which this article uses and flags.</p>''',
 dl_long='1 December 2026',
 offlinks=[('Leiden University — Leiden University Excellence Scholarship (LExS) (official)', 'https://www.staff.universiteitleiden.nl/scholarships/sea/leiden-university-excellence-scholarship-lexs?cf=governance-and-global-affairs'),
           ('Bright Scholarship — Leiden University Excellence Scholarships 2027', 'https://brightscholarship.com/leiden-university-excellence-scholarships-2027/')],
 related_titles=['leiden-mandela', 'tudelft-excellence-2027', 'wageningen-2027', 'radboud-2027'])),

# ---------------------------------------------------------------- 3. Erasmus Mundus MAPP
A.append(dict(
 slug='erasmus-mundus-mapp-scholarship-2027',
 title='Erasmus Mundus MAPP Scholarship 2027 (Fully Funded)',
 meta='Erasmus Mundus MAPP Scholarship 2027: a fully funded two-year joint Master\u2019s in Public Policy across two European countries, with up to \u20ac33,600 (\u20ac1,400 a month) and a full tuition waiver. Deadline 1 December 2026 — tracks, eligibility, documents, how to apply and FAQs.',
 short='Erasmus Mundus MAPP Scholarship 2027', kicker='Europe · Master\u2019s · Fully Funded', mono='MM',
 prov_short='Mundus MAPP Consortium', prov_cat='Erasmus Mundus · Europe',
 h1='Erasmus Mundus MAPP Scholarship 2027 (Fully Funded)',
 sub='The Erasmus Mundus MAPP Scholarship 2027 funds a two-year joint Master\u2019s in Public Policy across two European countries, with up to \u20ac33,600 over 24 months — \u20ac1,400 a month — plus a full tuition waiver and health insurance. Four universities deliver the programme: Central European University in Vienna, the International Institute of Social Studies in The Hague, IBEI in Barcelona and the University of York. Applications for the 2027–2029 cohort opened on 1 September 2026, and the deadline for financial-aid consideration is 1 December 2026 at 23:59 CET. Admissions are run centrally by CEU — you cannot apply through the other three universities.',
 dpill='Deadline 1 Dec 2026 · %d days left' % dl_left('2026-12-01'),
 facts=facts([('Award', 'The Erasmus Mundus Joint Master (EMJM) scholarship pays up to €33,600 over 24 months — €1,400 a month — and waives tuition in full (tuition is otherwise €13,000 per academic year, €26,000 for the programme). Health insurance is included. A limited number of EMJM scholarships are available to outstanding applicants from both EU and non-EU countries. Applicants who do not receive the EMJM award may be considered for an institutional scholarship: one per mobility track, covering 50% of tuition at both years, with no stipend.'),
              ('Eligible', 'All nationalities — EU and non-EU — with a Bachelor\u2019s degree in a relevant social-science field. English proficiency is required: the call lists TOEFL iBT 95, IELTS 7.0 or Duolingo 130, with exemptions for some applicants (for example, nationals of certain countries or holders of an English-medium degree). You apply to one mobility track only, and the programme is full-time and in person. No previous professional work experience is required, though relevant academic and professional experience strengthens an application.'),
              ('How', 'Apply through the central admissions system run by Central European University Private University (CEU PU) — applications submitted directly to ISS, IBEI or York are not considered. Select one of the four mobility tracks, complete the online application form, upload your supporting documents, and indicate in the form that you wish to be considered for financial aid. There is no separate scholarship application and no application fee for MAPP-only applicants — the CEU application fee applies only if you also apply to other CEU programmes.'),
              ('Deadline', '1 December 2026, 23:59 CET, for financial-aid (EMJM scholarship) consideration. Applications opened on 1 September 2026. Later dates are for self-funded admission only: 15 April 2027 for non-EU/EEA residents and 1 July 2027 for EU/EEA residents. The scholarship deadline is the one that matters for funded study.'),
              ('Fine print', 'The degree is a joint Master of Arts in Public Policy (120 ECTS) awarded by two universities, and the programme requires study in two different countries — the track you choose fixes both. The EMJM scholarship does not cover every cost: study visits and winter schools (around €600–€1,000 each) and travel or visa costs between your home country and the consortium countries are not covered, so check the programme\u2019s financial aid page before budgeting. Contact for enquiries: mundusmapp@ceu.edu.')]),
 body='''
      <h2 id="about">About the programme</h2>
      <p><strong>Mundus MAPP</strong> — the Erasmus Mundus Master\u2019s Programme in Public Policy — has run since 2007 and is jointly delivered by four universities: <strong>Central European University Private University (CEU PU)</strong> in Vienna, Austria; the <strong>International Institute of Social Studies (ISS)</strong> of Erasmus University Rotterdam in The Hague, Netherlands; the <strong>Institut Barcelona d\u2019Estudis Internacionals (IBEI)</strong> in Barcelona, Spain; and the <strong>University of York</strong> in the United Kingdom. More than 400 students from over 80 countries have studied on the programme, and the European Commission selected it as one of five Erasmus Mundus \u201csuccess stories\u201d in 2020.</p>
      <p>The structure is what makes MAPP different from a single-university Master\u2019s. You spend your first year at one partner university and your second year at another, in a different country, following one of four <strong>mobility tracks</strong> — and the track also fixes your specialisation. Alongside the academic work, the programme builds in internships, policy labs and fieldwork, and engagement with international organisations, government institutions and NGOs. Graduates go on to careers in government, international organisations, research and the private sector.</p>
      <h2 id="mobility-tracks">Mobility tracks and specialisations</h2>
      <ul>
        <li><strong>CEU PU – IBEI track:</strong> Global Public Policy — first year in Vienna, second year in Barcelona.</li>
        <li><strong>CEU PU – York track:</strong> European Public Policy — first year in Vienna, second year in York.</li>
        <li><strong>ISS – IBEI track:</strong> Political Economy and Development — first year in The Hague, second year in Barcelona.</li>
        <li><strong>ISS – York track:</strong> Governance and Development — first year in The Hague, second year in York.</li>
      </ul>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>Bachelor\u2019s degree</strong> in a relevant social-science field. Engineering and natural-science degrees are not the programme\u2019s target — the degree is a public-policy Master\u2019s.</li>
        <li>Be of <strong>any nationality</strong> — EU and non-EU applicants are both eligible for the EMJM scholarship.</li>
        <li>Meet the <strong>English requirement</strong>: the call lists TOEFL iBT 95, IELTS 7.0 or Duolingo 130, with exemptions for some applicants (for example, on nationality or an English-medium degree).</li>
        <li>Be ready for <strong>full-time, in-person study in two countries</strong> over 24 months.</li>
        <li>Apply to <strong>one mobility track only</strong>.</li>
        <li>No previous professional work experience is required, though relevant experience strengthens an application.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Up to \u20ac33,600 over 24 months</strong> — \u20ac1,400 a month — for EMJM scholarship holders.</li>
        <li><strong>Full tuition waiver</strong> for EMJM holders (tuition is otherwise \u20ac13,000 per academic year).</li>
        <li><strong>Health insurance</strong> included.</li>
        <li>A <strong>joint Master\u2019s degree</strong> (MA in Public Policy, 120 ECTS) from two universities in two countries.</li>
        <li><strong>Internships, policy labs and fieldwork</strong> with international organisations, government institutions and NGOs.</li>
        <li>No application fee for MAPP-only applicants.</li>
        <li>An <strong>institutional scholarship</strong> (50% tuition waiver, one per track, no stipend) for applicants who do not receive the EMJM award.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A copy of your <strong>Bachelor\u2019s degree certificate</strong>, translated into English.</li>
        <li>Your academic <strong>transcript</strong>, translated into English.</li>
        <li><strong>Two letters of recommendation</strong>.</li>
        <li>An <strong>English-language proficiency certificate</strong> where applicable (TOEFL iBT 95, IELTS 7.0 or Duolingo 130, or proof of exemption).</li>
        <li>A <strong>statement of purpose</strong> and any other documents listed in the official application guidelines — check the current checklist on mundusmapp.org before submitting, as requirements can change between cycles.</li>
        <li><strong>Passport and residence proof</strong> as the application asks for.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the <strong>official programme pages</strong> on mundusmapp.org — the admissions calendar, the how-to-apply page and the financial aid page — and choose <strong>one mobility track</strong>.</li>
        <li>Prepare your documents: degree certificate and transcript (in English), two recommendation letters, English proficiency evidence and your statement of purpose.</li>
        <li>Complete the <strong>online application form</strong> through the central CEU admissions system. Do not apply to ISS, IBEI or York directly — only applications submitted to CEU PU in the prescribed way are considered.</li>
        <li>In the application form, <strong>indicate that you wish to be considered for financial aid</strong>. There is no separate scholarship application.</li>
        <li>Submit before <strong>1 December 2026, 23:59 CET</strong> for EMJM scholarship consideration. The later 2027 dates (15 April for non-EU/EEA, 1 July for EU/EEA) are for self-funded admission only.</li>
        <li>Monitor the <strong>application portal and your registered email</strong> for the scholarship decision.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('What is the deadline for the Erasmus Mundus MAPP Scholarship 2027?',
  '1 December 2026 at 23:59 CET, for financial-aid consideration. Applications opened on 1 September 2026. The later dates in 2027 (15 April for non-EU/EEA residents, 1 July for EU/EEA residents) are for self-funded admission only.'),
 ('How much does the MAPP scholarship pay?',
  'Up to €33,600 over 24 months — €1,400 a month — plus a full tuition waiver and health insurance. Tuition without the scholarship is €13,000 per academic year.'),
 ('Do I apply to each university separately?',
  'No. Admissions are centrally administered by Central European University Private University. You apply once through the central system, select one mobility track, and only applications submitted to CEU PU in the prescribed way are considered.'),
 ('Is there a separate scholarship application?',
  'No. You indicate in the admission application form that you wish to be considered for financial aid. There is also no CEU application fee if you apply only to Mundus MAPP.'),
 ('Which countries will I study in?',
  'Two, fixed by your track: Vienna and Barcelona (Global Public Policy), Vienna and York (European Public Policy), The Hague and Barcelona (Political Economy and Development), or The Hague and York (Governance and Development).')]) + '''
      <p class="verify">Verified 25 Oct 2026: mundusmapp.org/how-to-apply/ (official) — applications open for the 2027\u20132029 cohort, admissions centrally administered by CEU Private University, only CEU PU applications considered, no CEU fee for MAPP-only applicants, no separate scholarship application, four mobility tracks (CEU PU\u2013IBEI, CEU PU\u2013York, ISS\u2013IBEI, ISS\u2013York); universities.nspscholarships.com, unitednationsrecruit.com, fellowshipsguide.com, schresult.com, opportunitiesforyouth.org — deadline 1 December 2026 for financial aid, \u20ac1,400 a month up to \u20ac33,600, tuition waived, applications opened 1 September 2026, running since 2007, 400+ students from 80+ countries; europescholarships.com — self-funded deadlines 15 April 2027 (non-EU/EEA) and 1 July 2027 (EU/EEA), one 50% tuition institutional scholarship per track, study visits and winter schools not covered; mastere.tn — English requirements TOEFL iBT 95, IELTS 7.0 or Duolingo 130, two recommendation letters, documents in English, contact mundusmapp@ceu.edu.</p>''',
 dl_long='1 December 2026, 23:59 CET (for financial-aid consideration)',
 offlinks=[('Mundus MAPP — How to apply (official)', 'https://www.mundusmapp.org/how-to-apply/'),
           ('Bright Scholarship — Erasmus Mundus MAPP Scholarship 2027', 'https://brightscholarship.com/erasmus-mundus-mapp-scholarship-fully-funded/')],
 related_titles=['emabg', 'daad', 'turkiye2027', 'gks2027'])),

# ---------------------------------------------------------------- 4. Monash ReDiLEEP
A.append(dict(
 slug='monash-university-redileep-phd-scholarship-2027-australia',
 title='Monash University ReDiLEEP PhD Scholarship 2027 in Australia (Funded)',
 meta='Monash University ReDiLEEP PhD Scholarship 2027: a funded doctoral project on response diversity in marine phytoplankton, in the Ghedini Lab at Monash University, Australia. Deadline 30 October 2026 — project, eligibility, how to apply and FAQs.',
 short='Monash University ReDiLEEP PhD Scholarship 2027', kicker='Australia · PhD · Funded', mono='MR',
 prov_short='Monash University', prov_cat='University · Australia',
 h1='Monash University ReDiLEEP PhD Scholarship 2027 in Australia (Funded)',
 sub='The Monash University ReDiLEEP PhD Scholarship 2027 is a funded doctoral project in the Ghedini Lab at Monash University, Australia, studying how differences in species physiology shape the stability and recovery of marine phytoplankton communities under environmental change. The project sits inside the international ReDiLEEP doctoral network — but read this carefully: because Monash is outside the European Union, this is not formally an MSCA Doctoral Candidate position, and the successful candidate must compete for a Monash graduate research scholarship. Applications close on 30 October 2026 at 12:00 noon Melbourne time, and the PhD is expected to start in the first half of 2027.',
 dpill='Deadline 30 Oct 2026 · %d days left' % dl_left('2026-10-30'),
 facts=facts([('Award', 'A funded PhD project: the successful candidate is supported to compete for a Monash graduate research scholarship, which covers PhD tuition and a living stipend. The project also brings participation in the international ReDiLEEP doctoral network — collaboration with research groups in Europe, training activities, workshops and conferences, and opportunities for secondments. Because the Monash laboratory is outside the European Union, this position is not formally classified as an MSCA Doctoral Candidate position: do not assume the standard MSCA doctoral salary and mobility allowances apply. Confirm the exact funding conditions with the project team before applying.'),
              ('Eligible', 'All nationalities. You need a Master\u2019s degree (or equivalent) in biology, ecology, marine biology, environmental science or a closely related discipline, at First Class Honours or equivalent Master\u2019s performance. You need laboratory research experience and statistical analysis skills, using R or similar software. A first-author peer-reviewed publication is not mandatory, but it would substantially strengthen your competitiveness for the Monash scholarship. The project is a research-fit opportunity: your background and interests must match this specific project, under one supervisor, rather than a general ecology PhD.'),
              ('How', 'Email the project lead, Dr Giulia Ghedini (giulia.ghedini@monash.edu), with a motivation letter of up to two pages explaining your research interests and why this project matches them, and a CV of up to two pages including your university final grades, a publication list if available, and contact details for two referees. Candidates must also apply for a Monash PhD scholarship through the university\u2019s official process. Read the full project advertisement before applying.'),
              ('Deadline', '30 October 2026 at 12:00 noon Melbourne time. The expected PhD commencement is in the first half of 2027. International applicants should allow time to prepare academic documents, research materials and correspondence with the research team before the deadline.'),
              ('Fine print', 'This is one specific research project under one supervisor, not an open PhD call: competition is shaped less by volume and more by how well your background matches the project. The project title is \u201cPhysiological Basis and Consequences of Response Diversity\u201d. The funding route is a Monash graduate research scholarship, awarded competitively — the project email is the first step, not a guarantee of funding.')]),
 body='''
      <h2 id="about">About the project</h2>
      <p>The <strong>ReDiLEEP PhD project</strong> at Monash University asks a precise question: when a marine community is hit by environmental change, why do some ecosystems survive and others collapse? The answer the project tests is <strong>response diversity</strong> — the idea that different species respond differently to the same disturbance, and that the spread of those responses, not just the average, can determine whether a community persists, adapts or recovers. The successful doctoral researcher will work with <strong>marine phytoplankton communities</strong> to investigate how variation in species physiology affects persistence and recovery under global environmental change.</p>
      <p>The work is based in the <strong>Ghedini Lab</strong> (Community Ecology &amp; Evolution Lab) at Monash University, led by <strong>Dr Giulia Ghedini</strong>, and it sits inside the international <strong>ReDiLEEP Doctoral Network</strong>, funded through the Marie Sk\u0142odowska-Curie Actions. That network brings collaboration with research groups in Europe, joint training, workshops and secondments. One distinction matters and is stated plainly in the project guidance: because the Monash laboratory is outside the European Union, this position is <strong>not formally an MSCA Doctoral Candidate position</strong>, so the standard MSCA salary and mobility allowances should not be assumed — the candidate is supported to compete for a Monash graduate research scholarship instead.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>Master\u2019s degree or equivalent</strong> in biology, ecology, marine biology, environmental science or a closely related discipline.</li>
        <li>Meet the academic standard of <strong>First Class Honours or equivalent Master\u2019s performance</strong>.</li>
        <li>Have <strong>laboratory research experience</strong> and <strong>statistical analysis skills</strong>, using R or similar software.</li>
        <li>Show a research interest that matches this specific project: <strong>community ecology, environmental change, marine systems and species physiology</strong>.</li>
        <li>Be of <strong>any nationality</strong> — the project is open to international applicants.</li>
        <li>A <strong>first-author peer-reviewed publication</strong> is not mandatory, but it would substantially strengthen your competitiveness for the Monash scholarship.</li>
      </ul>
      <h2 id="research-focus">What you will research</h2>
      <ul>
        <li><strong>Marine phytoplankton communities</strong> as the model system for community stability under environmental change.</li>
        <li>How differences in <strong>species physiology</strong> — including how species acquire and use energy — affect community persistence and recovery.</li>
        <li><strong>Theory-informed laboratory experiments</strong>, physiological measurements and eco-evolutionary assays.</li>
        <li><strong>Quantitative analysis</strong> of response diversity and its consequences for ecosystem stability.</li>
        <li>Collaboration with the <strong>international ReDiLEEP doctoral network</strong> and research groups in Europe.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>funded PhD project</strong>: tuition support and a living stipend through a Monash graduate research scholarship (awarded competitively).</li>
        <li>Participation in the <strong>international ReDiLEEP doctoral network</strong>, with training activities, workshops and conferences.</li>
        <li><strong>Secondment opportunities</strong> and exposure to interdisciplinary research networks.</li>
        <li>Supervision in the <strong>Ghedini Lab</strong> and access to Monash University research facilities.</li>
        <li>Research training and professional development in community ecology and environmental change biology.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>motivation letter of up to two pages</strong> explaining your research interests, your relevant laboratory or experimental skills, and why this particular project matches your background.</li>
        <li>A <strong>CV of up to two pages</strong> including your university final grades, a publication list if available, and contact details for <strong>two referees</strong>.</li>
        <li>Your academic background, previous research experience and any <strong>experience using R or similar statistical tools</strong>, described in the motivation letter.</li>
        <li>Any <strong>publications or research outputs</strong> you have, if applicable.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the <strong>full project advertisement</strong> and confirm your background matches the project\u2019s focus on response diversity in marine phytoplankton.</li>
        <li>Prepare your <strong>motivation letter (maximum two pages)</strong> and your <strong>CV (maximum two pages)</strong>, including final grades, publications and two referees.</li>
        <li><strong>Email Dr Giulia Ghedini</strong> at <strong>giulia.ghedini@monash.edu</strong> with both documents, explaining clearly why this project matches your research interests and how your previous work prepares you for it.</li>
        <li><strong>Apply for a Monash PhD scholarship</strong> through the university\u2019s official process — the project email alone does not secure funding.</li>
        <li>Submit everything before <strong>30 October 2026 at 12:00 noon Melbourne time</strong>. The PhD is expected to start in the <strong>first half of 2027</strong>.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('Is the Monash ReDiLEEP PhD fully funded?',
  'The project is funded through a Monash graduate research scholarship, which covers tuition and a living stipend — but you must compete for that scholarship. The project email is the first step; it does not itself guarantee funding.'),
 ('Is this an MSCA Doctoral Candidate position?',
  'No. The project operates inside the Marie Sk\u0142odowska-Curie Actions Doctoral Network ReDiLEEP, but because the Monash laboratory is outside the European Union, the position is not formally classified as an MSCA Doctoral Candidate position. Do not assume the standard MSCA salary and mobility allowances apply.'),
 ('What is the deadline?',
  '30 October 2026 at 12:00 noon Melbourne time. The expected PhD start is in the first half of 2027.'),
 ('How do I apply — is there an online form?',
  'There is no project application form. You email Dr Giulia Ghedini directly with a motivation letter (maximum two pages) and a CV (maximum two pages), and you also apply for a Monash PhD scholarship through the university\u2019s official process.'),
 ('What research background do I need?',
  'A Master\u2019s or equivalent in biology, ecology, marine biology, environmental science or a related field, at First Class Honours or equivalent standard, with laboratory research experience and statistical skills (R or similar). A first-author publication helps but is not mandatory.')]) + '''
      <p class="verify">Verified 25 Oct 2026: scholarshipsads.com — deadline 30 October 2026 at 12:00 Melbourne time, project led by Dr Giulia Ghedini, email giulia.ghedini@monash.edu, motivation letter up to 2 pages, CV up to 2 pages, expected PhD commencement first half of 2027; scholarinfo.net, scholarshipunion.com, schresult.com, daadscholarship.com — same 30 October 2026 deadline, First Class Honours or equivalent Master\u2019s performance, must compete for a Monash graduate research scholarship, project title \u201cPhysiological Basis and Consequences of Response Diversity\u201d, marine phytoplankton model system, not formally an MSCA Doctoral Candidate position as Monash is outside the EU; monash.edu (official graduate scholarship page) — Monash Graduate Scholarship terms.</p>''',
 dl_long='30 October 2026, 12:00 noon Melbourne time',
 offlinks=[('Monash — Graduate research scholarships (official)', 'https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/monash-graduate-scholarship-mgs'),
           ('Bright Scholarship — Monash University ReDiLEEP PhD Scholarship 2027', 'https://brightscholarship.com/monash-university-redileep-phd-scholarship/')],
 related_titles=['monash-rtp', 'perugia-phd', 'vechta-phd-2027', 'swiss-phd'])),

# ---------------------------------------------------------------- 5. Stanford Hoover
A.append(dict(
 slug='stanford-university-hoover-fellowship-2027-usa',
 title='Stanford University Hoover Fellowship 2027 for Early Career Researchers (Paid)',
 meta='Stanford University Hoover Fellowship 2027: a paid early-career research fellowship at the Hoover Institution, Stanford — $169,950\u2013$230,000 base salary plus a $20,000 housing allowance for 1\u20133 years, with no teaching. Deadline 17 November 2026 — eligibility, documents, how to apply and FAQs.',
 short='Stanford University Hoover Fellowship 2027', kicker='USA · Postdoctoral Fellowship · Paid', mono='HV',
 prov_short='Hoover Institution, Stanford University', prov_cat='Fellowship · United States',
 h1='Stanford University Hoover Fellowship 2027 for Early Career Researchers (Paid)',
 sub='The Stanford University Hoover Fellowship 2027 — the Hoover Fellows Program — is a paid research appointment for early-career scholars at the Hoover Institution, Stanford University, in California. Fellows receive a 12-month base salary of $169,950 to $230,000 plus a $20,000 annual housing allowance, for one to three years, with no teaching responsibilities at all: the appointment is for independent research, writing and publication with policy implications. Applications close on 17 November 2026 at 11:59 p.m. Pacific Time, and the fellowship is expected to start around September 2027.',
 dpill='Deadline 17 Nov 2026 · %d days left' % dl_left('2026-11-17'),
 facts=facts([('Award', 'A 12-month base salary of $169,950 to $230,000, depending on the appointment, plus a $20,000 annual housing allowance. Appointments run for one to three years and are renewable. The fellowship carries no teaching responsibilities, so fellows concentrate on research, writing and publication. Fellows join the Hoover Institution\u2019s intellectual community on Stanford\u2019s campus, with access to the Hoover and Stanford research environment and the chance to publish scholarly articles and books with implications for public policy.'),
              ('Eligible', 'Early-career scholars who hold a PhD or equivalent degree in a relevant field, or who expect to complete the degree by 1 September 2027. Relevant fields are economics, history, international relations, national security, political science and public policy, or related disciplines. Applicants should have a strong academic or research background, research interests relevant to public policy or the Hoover Institution\u2019s research mission, and the ability to develop an independent research agenda. The Hoover Institution is an equal opportunity employer and welcomes applications from international scholars.'),
              ('How', 'Apply online through the Hoover Institution\u2019s application portal, which runs on SM Apply (hoover.smapply.us): register with your name and email address, then upload your documents. The portal opened on 18 August 2026. Submit a cover letter or statement of interest, one or more recent publications, working papers or draft book chapters, a CV, a two-page statement of future research plans, and three letters of recommendation. If you have questions, contact hooverfellowship@stanford.edu — the inbox is checked only periodically, so ask early.'),
              ('Deadline', '17 November 2026 at 11:59 p.m. Pacific Time. Late or incomplete submissions will not be considered, and the announcement describes no late-application policy. The fellowship is expected to start around September 2027.'),
              ('Fine print', 'This is a research appointment, not a teaching post and not a degree programme: fellows are expected to develop and publish scholarly work, including academic articles and books, and to contribute to the intellectual life of the Hoover Institution. The salary range depends on the appointment — the figure is a range, not a guarantee of the top amount. Give your three referees four to six weeks\u2019 notice: their letters should address your research accomplishments and potential for future research.')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Hoover Institution</strong>, founded in 1919, is one of America\u2019s oldest and most influential policy research centres, housed on the campus of <strong>Stanford University</strong> in Palo Alto, California. The <strong>Hoover Fellows Program</strong> is its flagship appointment for early-career academics: a salaried research fellowship for scholars whose work has implications for public policy and who want to contribute to the intellectual life of a leading research institution.</p>
      <p>What sets this fellowship apart is the combination of senior-level pay and a pure research brief. Fellows receive a <strong>12-month base salary of $169,950 to $230,000</strong> plus a <strong>$20,000 annual housing allowance</strong>, for <strong>one to three years</strong>, and the appointment carries <strong>no teaching responsibilities</strong> — the time is for independent research, writing and publication. It sits at the senior end of early-career fellowships, comparable in prestige and compensation to the Miller Institute at UC Berkeley or the Society of Fellows at Harvard, but with a stronger policy-outreach dimension: Hoover expects its fellows to produce work that reaches policymakers, not only academic journals.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>PhD or equivalent degree</strong> in a relevant field, or expect to complete the degree by <strong>1 September 2027</strong>.</li>
        <li>Work in a relevant field: <strong>economics, history, international relations, national security, political science or public policy</strong>, or a related discipline.</li>
        <li>Have a <strong>strong academic or research background</strong> and be able to develop an <strong>independent research agenda</strong> with implications for public policy.</li>
        <li>Be an <strong>early-career scholar</strong> — the programme is designed for researchers moving from doctoral work towards a sustained independent research career.</li>
        <li>Be of <strong>any nationality</strong>: the Hoover Institution is an equal opportunity employer and welcomes applications from international scholars.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A <strong>12-month base salary of $169,950\u2013$230,000</strong>, depending on the appointment.</li>
        <li>A <strong>$20,000 annual housing allowance</strong>.</li>
        <li>An appointment of <strong>1 to 3 years</strong>, renewable.</li>
        <li><strong>No teaching responsibilities</strong> — full-time research, writing and publication.</li>
        <li>Access to the <strong>Hoover Institution and Stanford research community</strong>, with opportunities to publish scholarly articles and books and to engage with policymakers.</li>
        <li>Time to complete <strong>book manuscripts</strong>, publish in top journals and build a research profile.</li>
      </ul>
      <h2 id="documents">Documents to prepare</h2>
      <ul>
        <li>A <strong>cover letter or statement of interest</strong> describing your academic background and experience.</li>
        <li><strong>One or more recent publications, working papers or draft book chapters</strong> — your strongest recent work, closely connected to your future research plan.</li>
        <li>An academic <strong>CV</strong>.</li>
        <li>A <strong>statement of future research plans, two pages maximum</strong> — focused, specific about what you will study, why it matters, how you will do it and what you expect to publish.</li>
        <li><strong>Three letters of recommendation</strong> addressing your research accomplishments and potential for future research.</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the <strong>official Hoover Fellows Program page</strong> at hoover.org/hoover-fellows-program and confirm your field aligns with Hoover\u2019s research priorities.</li>
        <li>Prepare your <strong>research statement (two pages maximum)</strong>, your <strong>writing samples</strong> and your <strong>CV</strong> — the research statement is where most applications are decided, so describe specifically what you will produce at Hoover and why it matters for policy.</li>
        <li>Contact your <strong>three referees</strong> early — give them at least four to six weeks\u2019 notice.</li>
        <li><strong>Register on the SM Apply portal</strong> (hoover.smapply.us) with your name and email address and create your application.</li>
        <li>Upload all documents and confirm the portal shows your application as <strong>complete</strong>, with all three recommendation letters received.</li>
        <li>Submit before <strong>17 November 2026 at 11:59 p.m. Pacific Time</strong>. Do not wait until the final hour — file uploads and recommendation letters sometimes need extra processing time.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
''' + faqs([
 ('How much does the Hoover Fellowship pay?',
  'A 12-month base salary of $169,950 to $230,000, depending on the appointment, plus a $20,000 annual housing allowance. Appointments run for one to three years.'),
 ('Do Hoover Fellows have to teach?',
  'No. The fellowship carries no teaching responsibilities. Fellows focus on independent research, writing and publication, and on contributing to the intellectual life of the Hoover Institution.'),
 ('Who can apply for the Hoover Fellows Program?',
  'Early-career scholars who hold a PhD or equivalent, or who expect to complete their degree by 1 September 2027, in economics, history, international relations, national security, political science, public policy or a related discipline. International scholars are welcome.'),
 ('What is the application deadline?',
  '17 November 2026 at 11:59 p.m. Pacific Time. Late or incomplete submissions are not considered, and there is no published late-application policy.'),
 ('When does the fellowship start?',
  'Around September 2027. Appointments are for one to three years and are renewable.')]) + '''
      <p class="verify">Verified 25 Oct 2026: hoover.org/hoover-fellows-program (official) — applications due 11:59 p.m. PT on 17 November 2026, cover letter, publications, CV, two-page future research statement, three recommendation letters, contact hooverfellowship@stanford.edu (inbox checked only periodically); brightscholarship.com, globalsouthopportunities.com, oyaop.com, scholarshipsads.com, jagranjosh.com, ndtv.com — 12-month base salary $169,950\u2013$230,000 plus $20,000 annual housing allowance, appointments 1\u20133 years, PhD or expected by 1 September 2027, no teaching responsibilities, portal opened 18 August 2026, fellowship start around September 2027; gradualin.com — application portal hoover.smapply.us, official page hoover.org/hoover-fellows-program.</p>''',
 dl_long='17 November 2026, 11:59 p.m. Pacific Time',
 offlinks=[('Hoover Institution — Hoover Fellows Program (official)', 'https://www.hoover.org/hoover-fellows-program'),
           ('Bright Scholarship — Stanford University Hoover Fellowship 2027', 'https://brightscholarship.com/stanford-university-hoover-fellowship/')],
 related_titles=['reach-oxford', 'gates-cam-2027', 'imperial-mba-2027', 'manchester-rr'])),

for a in A: _split_verify(a)
sizes = {}
for a in A:
    for k in a['related_titles']:
        assert k in CARDS, (a['slug'], k)
    for t, u in a['offlinks']:
        assert u.startswith('http'), (a['slug'], u)
    assert 'AICTE Pragati' not in (a['title'] + a['h1'] + a['body'] + a['sub'])
    assert '{{' not in a['body'] and 'Lorem' not in a['body']
    sizes[a['slug']] = build_article(BASE, OUT, a, CARDS)
    json.dump(sizes, open('/tmp/batch48_built.json','w'))

class P(html.parser.HTMLParser):
    def error(self, message): raise AssertionError(message)
for a in A:
    pth = OUT / (a['slug'] + '.html')
    assert pth.exists(), a['slug']
    P().feed(pth.read_text())
    txt = pth.read_text()
    assert 'AICTE Pragati' not in txt, a['slug']
    assert 'Lorem' not in txt, a['slug']
    assert '#' not in a['slug']
    assert 'wa.me/919905166009' in txt, a['slug'] + ' missing WhatsApp float'
print('built OK:', json.dumps(sizes, indent=1))

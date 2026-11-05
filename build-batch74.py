#!/usr/bin/env python3
"""Batch 74 — 31 Oct 2026. Last five-but-one of the queue; only Yashasvi remains after this."""
import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'teach-trust': {'mono': 'TT', 'title': 'TEACH Trust Education Assistance 2026',
   'href': 'teach-trust-education-assistance-2026.html',
   'dpill': 'Always open',
   'award': 'Rs 35,000 (school); Rs 55,000 (arts/science/commerce college); Rs 1,00,000 (professional degrees).',
   'elig': 'Indian citizen studying in India; 90% or more in Class 10 and Class 12; family income up to Rs 2,50,000 a year.',
   'tags': [('Trust', 'blue'), ('India', 'teal')]},
 'vylor-agritech-ug': {'mono': 'VY', 'title': 'Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27',
   'href': 'vylor-agritech-scholarship-undergraduate-fy-26-27.html',
   'dpill': 'Always open',
   'award': 'Rs 25,000 a year for undergraduate courses in agriculture and allied fields.',
   'elig': 'Undergraduate students in agriculture and allied streams at government institutions; special preference for female students.',
   'tags': [('Agriculture', 'green'), ('Undergraduate', 'blue')]},
 'aicte-pdf-2024': {'mono': 'AICTE', 'title': 'AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25',
   'href': 'aicte-post-doctoral-fellowship-pdf-2024-25.html',
   'dpill': 'Extension reported to 15 Nov (see note)',
   'award': 'Originally Rs 65,000 a month plus HRA and Rs 50,000 a year contingency; revised reports list Rs 80,000 a month plus HRA, Rs 2,00,000 research grant and Rs 50,000 overheads.',
   'elig': 'PhD holders in approved technical and related disciplines; below 35, with age relaxations; a supervisor at an AICTE-approved host institution.',
   'tags': [('Fellowship', 'purple'), ('PhD', 'blue')]},
 'aicte-apf-2026': {'mono': 'AICTE', 'title': 'AICTE Productization Fellowship (APF) 2026',
   'href': 'aicte-productization-fellowship-apf-2026.html',
   'dpill': 'Always open',
   'award': 'Up to Rs 4.94 lakh a year: Rs 37,000 a month for up to one year plus a Rs 50,000 annual contingency grant.',
   'elig': 'Full-time UG, PG or doctoral students (or graduates within the last two years) at AICTE-approved institutions, with a product idea at proof-of-concept stage.',
   'tags': [('Fellowship', 'purple'), ('Innovation', 'teal')]},
 'aicte-saksham-2024': {'mono': 'AICTE', 'title': 'AICTE-Saksham Scholarship Scheme 2024-25',
   'href': 'aicte-saksham-scholarship-scheme-2024-25.html',
   'dpill': 'Closes today, 31 Oct 2026',
   'award': 'Rs 50,000 a year as a lump sum for every year of study.',
   'elig': 'Specially-abled students (40% or more disability) in the first year, or second year by lateral entry, of an AICTE-approved degree or diploma; family income up to Rs 8 lakh.',
   'tags': [('PwD', 'blue'), ('Central Govt', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. TEACH Trust Education Assistance 2026
ARTICLES.append({
 'slug': 'teach-trust-education-assistance-2026',
 'title': 'TEACH Trust Education Assistance 2026',
 'meta': 'TEACH Trust Education Assistance 2026: financial help from the Tondiarpet Education Assistance for Children Trust for high-scoring, low-income students in India — Rs 35,000 for school, Rs 55,000 for arts, science and commerce degrees, and Rs 1,00,000 for professional degrees. Always open; 90% or more in Class 10 and Class 12 and family income up to Rs 2,50,000 required.',
 'short': 'TEACH Trust Education Assistance 2026',
 'kicker': 'Trust Scholarship · India',
 'mono': 'TT',
 'prov_short': 'TEACH Trust',
 'prov_cat': 'Charitable Trust · Tamil Nadu',
 'h1': 'TEACH Trust Education Assistance 2026',
 'sub': 'A small Chennai-rooted trust with a deliberately narrow brief: find school-leavers who scored 90% or more, whose families earn no more than Rs 2,50,000 a year, and pay part of their next stage of education directly to the institution. There is no fixed closing date, and the help is tiered by course type rather than paid as a flat sum.',
 'dpill': 'Always open',
 'facts': facts([
   ('Provider', 'Tondiarpet Education Assistance for Children (TEACH) Trust — a non-profit founded in 2018 by six friends, all former residents of Tondiarpet'),
   ('Award', 'Rs 35,000 for school; Rs 55,000 for arts, science and commerce (college); Rs 1,00,000 for professional degrees'),
   ('Eligibility', 'Indian citizen studying in India; 90% or more in Class 10 and in Class 12; annual family income not exceeding Rs 2,50,000; management-seat students are ineligible'),
   ('Payment', 'Paid directly to the selected candidate\u2019s institution, not to the student'),
   ('Deadline', 'Always open — no fixed closing date is published in the listing'),
   ('Source caution', 'Only one programme listing could be found for this trust in this run\u2019s searches; no official trust website or contact was located, so confirm details on the listing before applying'),
 ]),
 'body': '''<h2 id="about">About the assistance</h2>
      <p>The Tondiarpet Education Assistance for Children Trust — TEACH Trust for short — was set up in 2018 by six longtime friends who had all grown up in Tondiarpet, a neighbourhood in Chennai. Its education assistance programme is aimed at students who combine two things that do not often sit together: very high board marks and a low family income. The trust does not run a college or a coaching centre; it simply helps pay the next step of a deserving student\u2019s education, and it sends the money to the institution rather than handing it to the student.</p>
      <p>One point of honesty first. Unlike most schemes in this series, this programme could be traced to only one detailed listing in this run\u2019s searches. No official trust website, email address or phone number turned up, and a different Chennai organisation that also uses the name TEACH — one working with deaf and hard-of-hearing students — is unrelated and has nothing to do with this programme. The facts below therefore come from that single listing, and applicants should treat the listing itself as the place to confirm the current position before sharing documents or money with anyone.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be a citizen of India who is pursuing studies in India.</li>
        <li>Have scored 90% or more in Class 10.</li>
        <li>Have scored 90% or more in Class 12.</li>
        <li>Have an annual family income of no more than Rs 2,50,000.</li>
        <li>Students admitted through a management seat are not eligible.</li>
      </ul>
      <p>The bar on marks is the programme\u2019s defining feature: 90% at both board stages, not just one. The income ceiling is correspondingly strict at Rs 2,50,000 a year. Nothing in the listing limits the programme to Tamil Nadu students — the stated condition is Indian citizenship and study in India — but, given the trust\u2019s roots, applicants from elsewhere should still confirm that their institution and course are covered before assuming eligibility.</p>
      <h2 id="benefits">What you get</h2>
      <p>The amount depends on the stage and stream, not on the college\u2019s fee:</p>
      <ul>
        <li>School-level assistance: Rs 35,000.</li>
        <li>Arts, science and commerce at college level: Rs 55,000.</li>
        <li>Professional degrees: Rs 1,00,000.</li>
      </ul>
      <p>Timing matters. The listing says students who pre-qualify once their Class 10 or Class 12 marksheet arrives — that is, before the college admit card is issued — are the ones the trust selects. Assistance is then transferred directly to the institution. Where the fee is higher than the assistance, the listing describes a single-payment arrangement: the student pays the difference to the trust, and the trust makes one combined payment to the institution. No renewal rule, total number of awards, or course-duration limit is published in the listing, so none is stated here.</p>
      <h2 id="documents">Documents needed</h2>
      <p>The listing asks for:</p>
      <ul>
        <li>Marksheets and certificates</li>
        <li>Admit card</li>
        <li>Rank card</li>
        <li>Fee demand proof from the college or school</li>
        <li>BPL verification, income certificate, or employment certificate</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Open the programme listing and use its Apply Now route.</li>
        <li>Register with a Gmail address, mobile number or email ID, or log in if you already have an account.</li>
        <li>Students who meet the stated criteria are shortlisted for assistance by the trust.</li>
        <li>Keep the fee demand proof ready: the trust pays the institution, so the institution\u2019s demand is central to the payment.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is there a last date?', 'No fixed date is published; the listing shows the programme as always open. That makes early application sensible anyway, because selection happens around the marksheet-to-admit-card window described above.'),
   ('Is this only for students from Chennai or Tamil Nadu?', 'No state restriction is published in the listing. The conditions given are Indian citizenship, study in India, the 90% marks at both board stages, and the income ceiling. The trust itself is Chennai-rooted, so confirm coverage for your institution if you study elsewhere.'),
   ('Do I receive the money myself?', 'No. The listing states that the assistance is transferred directly to the selected candidate\u2019s institution.'),
   ('Can management-seat students apply?', 'No. The listing expressly excludes students admitted through a management seat.'),
   ('Is there a contact number or email for the trust?', 'None was published in the sources checked for this article, so none is given here. Do not use the contact details of the unrelated deaf-education organisation that shares the TEACH name.'),
  ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study TEACH Trust Education Assistance 2026 listing (founded 2018 by six former Tondiarpet residents; Indian citizen studying in India; 90% or more in Class 10 and Class 12; family income up to Rs 2,50,000; management-seat students ineligible; Rs 35,000 school, Rs 55,000 arts/science/commerce college, Rs 1,00,000 professional degrees; payment directly to the institution; pre-qualification after the marksheet and before the admit card; documents: marksheets and certificates, admit card, rank card, fee demand proof, BPL verification or income or employment certificate; always open). No second independent source was found across three searches: no official trust website or contact could be located, and the Chennai TEACH deaf-education organisation found in search results is a different body and was not used. The single-source position is flagged in the article itself.',
 'dl_long': 'Always open — no fixed deadline published in the listing',
 'offlinks': [('Buddy4Study — TEACH Trust Education Assistance 2026', 'https://www.buddy4study.com/scholarship/teach-trust-education-assistance')],
 'related_titles': ['vylor-agritech-ug', 'aicte-saksham-2024', 'swanath-2026', 'nsp-pg-2026'],
})

# 2. Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27
ARTICLES.append({
 'slug': 'vylor-agritech-scholarship-undergraduate-fy-26-27',
 'title': 'Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27',
 'meta': 'Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27: Rs 25,000 a year for undergraduate students in agriculture and allied fields at government institutions, with special preference for female students. Always open on the live listing; a programme-wide 30 November 2026 date also appears in a featured listing and is flagged in the article.',
 'short': 'Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27',
 'kicker': 'Scholarship · Agriculture',
 'mono': 'VY',
 'prov_short': 'Vylor Agritech',
 'prov_cat': 'Private · Agriculture',
 'h1': 'Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27',
 'sub': 'A new agriculture-focused award for the 2026-27 financial year: Rs 25,000 a year for undergraduates studying agriculture and allied subjects at government institutions, with a stated preference for female students. The undergraduate track sits inside a wider Vylor programme that also covers postgraduate and doctoral students at a higher rate.',
 'dpill': 'Always open',
 'facts': facts([
   ('Provider', 'Vylor Agritech (Vylor)'),
   ('Award (UG)', 'Rs 25,000 fixed scholarship per year'),
   ('Award (PG/PhD, same programme)', 'Rs 35,000 per year — the sibling track, not this article\u2019s track'),
   ('Eligibility', 'Undergraduate students in agriculture and allied fields at government institutions, including IITs, NITs, IISc, ICAR-recognised colleges and State Agricultural Universities; special preference for female students'),
   ('Deadline', 'Always open on the live programme listing; a Buddy4Study featured listing shows 30 Nov 2026 for the FY 2026-27 programme — the conflict is flagged in the article'),
   ('More information', 'The programme guide points readers to vylor.com; no separate application form or document list is published in the sources checked'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>Vylor Agritech\u2019s scholarship programme for FY 2026-27 supports students in agriculture and allied disciplines who are studying at government institutions. The programme guide names IITs, NITs, IISc, ICAR-recognised colleges and State Agricultural Universities as the kind of institutions covered, and it describes the aim in plain terms: to ease the cost of higher education in agriculture for students who might otherwise struggle to carry it. This article covers the undergraduate track only. The same programme also runs postgraduate and doctoral tracks at Rs 35,000 a year, and those tracks have their own queue entry.</p>
      <p>Do not confuse this programme with a different Vylor award in South Africa. That bursary, for agricultural qualifications at South African institutions, pays up to R95,000 a year for undergraduates and closed on 30 October 2026. It has nothing to do with the Indian FY 2026-27 programme described here, and none of its terms apply to it.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be enrolled in an undergraduate programme in agriculture or an allied field.</li>
        <li>Be studying at a government institution — the guide lists IITs, NITs, IISc, ICAR-recognised colleges and State Agricultural Universities.</li>
        <li>Be in any year of the undergraduate course, according to the programme guide, which covers students enrolled in any year of UG, PG or PhD agriculture programmes.</li>
      </ul>
      <p>The guide adds a special preference for female students. That wording matters: it is a preference, not a stated female-only rule for the undergraduate track in the guide checked. A separate Buddy4Study listing for the postgraduate and PhD track describes that track as for female students, so readers should check the exact track wording on the listing for the level they are applying to rather than assuming one track\u2019s rule applies to the other.</p>
      <h2 id="benefits">What you get</h2>
      <p>Undergraduate students selected under this track receive a fixed scholarship of Rs 25,000 per year towards their educational expenses. The guide presents it as a fixed annual amount, not a fee reimbursement tied to a particular college\u2019s charges. How many undergraduates will be funded, and whether the award renews automatically for later years of the degree, is not published in the sources checked, so neither figure is stated here.</p>
      <h2 id="documents">Documents needed</h2>
      <p>No document list for this programme is published in the sources checked. The programme guide refers applicants to the provider\u2019s website for the application process rather than setting out a checklist. Applicants should therefore expect the usual proof of enrolment, identity and academic standing to be asked for on the application route, but this article does not invent a list the provider has not published.</p>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Open the programme listing for the undergraduate track and use its Apply Now route.</li>
        <li>Confirm that your course is an undergraduate programme in agriculture or an allied field at a government institution of the kind listed above.</li>
        <li>For fuller programme information, the guide points readers to vylor.com.</li>
        <li>Apply promptly despite the \u201cAlways Open\u201d label (see the deadline note below): featured listings for this programme have shown a 30 November 2026 date, and an open-ended label is no guarantee that a track will stay open.</li>
      </ol>
      <h2 id="deadline-note">A deadline conflict you should know about</h2>
      <p>The live programme listing, checked on 31 October 2026, shows the deadline as \u201cAlways Open\u201d. A Buddy4Study featured-scholarships listing for the same FY 2026-27 programme shows 30 November 2026. Both cannot be the whole story: one may be the programme-wide closing date while the track page carries no date, or the featured date may be a directory estimate. This article follows the live track page and reports the programme as always open, but flags the 30 November 2026 date here so that no reader is caught out if the programme does close then. Treat 30 November 2026 as the safer working deadline.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much do undergraduates get?', 'Rs 25,000 per year, fixed, under this track. Postgraduate and PhD students under the same programme get Rs 35,000 per year.'),
   ('Does the programme cover private colleges?', 'The guide describes government institutions — IITs, NITs, IISc, ICAR-recognised colleges and State Agricultural Universities. Private-institution coverage is not published in the sources checked.'),
   ('Is it only for female students?', 'The guide states a special preference for female students. It does not, in the wording checked, restrict the undergraduate track to female students only; the postgraduate and PhD listing is worded differently, so check the track you are applying to.'),
   ('What is the deadline?', 'The live listing says always open, but a featured listing for the programme shows 30 November 2026. This article flags both and advises treating 30 November 2026 as the safer working deadline.'),
   ('Is this the same as the Vylor bursary in South Africa?', 'No. That is a separate South African bursary with different amounts and a 30 October 2026 closing date, and none of its terms apply here.'),
  ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study Vylor Agritech undergraduate listing (live page checked 31 Oct 2026: deadline Always Open; title carries the up-to-Rs 35,000 programme figure) and the Scholarships in India Vylor Agritech Scholarship Program 2026-27 guide published 31 Oct 2026 (FY 2026-27 programme for agriculture and allied disciplines; any year of UG, PG or PhD at government institutions including IITs, NITs, IISc, ICAR-recognised colleges and State Agricultural Universities; special preference for female students; Rs 25,000 a year for undergraduate courses, Rs 35,000 a year for postgraduate and PhD programmes; more information at vylor.com), corroborated by the CIGMA Pedia listing of the same programme and by Buddy4Study listing snippets for the sibling postgraduate and PhD track (Rs 35,000 a year; female students in any year of postgraduation in agriculture and allied streams) and for the programme-wide 30 Nov 2026 featured date. No document list is published in the sources checked, so none is invented. The South African Vylor bursary (R95,000 undergraduate, closing 30 Oct 2026) is a different programme and is distinguished in the article.',
 'dl_long': 'Always open on the live listing — but a featured listing shows 30 Nov 2026 for the FY 2026-27 programme, so treat 30 Nov 2026 as the safer working deadline',
 'offlinks': [('Buddy4Study — Vylor Agritech Scholarship Program for Undergraduate Students FY 26-27', 'https://www.buddy4study.com/scholarship/vylor-agritech-scholarship-program-for-undergraduate-students-fy-26-27'), ('Scholarships in India — Vylor Agritech Scholarship Program 2026-27', 'https://www.scholarshipsinindia.com/vylor-agritech-scholarship-program.html'), ('Vylor (provider website, via programme guide)', 'https://www.vylor.com/')],
 'related_titles': ['teach-trust', 'aicte-saksham-2024', 'icar-nts', 'nsp-pg-2026'],
})

# 3. AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25
ARTICLES.append({
 'slug': 'aicte-post-doctoral-fellowship-pdf-2024-25',
 'title': 'AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25',
 'meta': 'AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25: a fellowship for PhD holders to pursue full-time postdoctoral research at AICTE-approved institutions — 200 fellowships a year, originally Rs 65,000 a month plus HRA, with revised reports listing Rs 80,000 a month plus a Rs 2,00,000 research grant. Extension reports point to 15 November; the year is not stated in the reports checked and is flagged in the article.',
 'short': 'AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25',
 'kicker': 'Fellowship · PhD Research',
 'mono': 'AICTE',
 'prov_short': 'AICTE',
 'prov_cat': 'Central Government · AICTE',
 'h1': 'AICTE Post-doctoral Fellowship (PDF) Scheme 2024-25',
 'sub': 'Two hundred full-time postdoctoral places a year for researchers who have finished a PhD and want a career in research and development at an AICTE-approved institution. The scheme\u2019s money and rules have been revised mid-cycle, so the original terms and the revised terms are both set out below — and the latest deadline reports need reading with care.',
 'dpill': 'Extension reported to 15 Nov (see note)',
 'facts': facts([
   ('Provider', 'All India Council for Technical Education (AICTE)'),
   ('Fellowships', '200 per year, full-time, for Indian research scholars'),
   ('Original terms', 'Rs 65,000 a month plus HRA, with an annual contingency grant of Rs 50,000'),
   ('Revised terms (reported Oct 2026)', 'Rs 80,000 a month plus HRA, a research grant of Rs 2,00,000 a year, and overheads of Rs 50,000 a year; no support for research personnel'),
   ('Duration', 'Initially one year, extendable by one more year on satisfactory work — two years in total, with no further extension'),
   ('Eligibility', 'PhD from a recognised university in an approved discipline; below 35 at application, with relaxations; quality publications or granted patents; a supervisor at an AICTE-approved host institution'),
   ('Deadline', 'Extension reports say 15 November, but the reports checked do not state the year in the text; other current guides listed 20 Oct 2026, now passed — confirm on the AICTE portal before relying on either date'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>The AICTE Post-doctoral Fellowship, often shortened to APDF, supports researchers who have completed a PhD and wish to pursue full-time postdoctoral research at an AICTE-approved university or institute, with the aim of building a regular career in research and development. Two hundred fellowships are offered per year. The fellow is expected to carry out the proposed research independently for the whole tenure, and may not hold any other fellowship from a government or non-government source during that time.</p>
      <p>Readers should be aware that this scheme has changed while its 2024-25 cycle has been running. News reports from October 2026 describe significant revisions to the eligibility criteria, the assistance on offer and the evaluation parameters, alongside an extended registration deadline. The original terms and the revised terms therefore differ, and both versions are given below so that applicants can see exactly what changed instead of being handed one blended figure.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Hold a PhD from a recognised university in a relevant discipline: engineering and technology, management, design, planning, applied arts, crafts and design, hotel management and catering technology, computer application, applied sciences, or an interdisciplinary area. Revised reports also mention physics, chemistry and mathematics backgrounds.</li>
        <li>Be below 35 years of age on the date of application. Age relaxation of five years applies to SC, ST, women and physically challenged candidates, and three years to OBC candidates; where more than one relaxation could apply, the maximum is five years.</li>
        <li>Meet the marks condition at either the postgraduate or the undergraduate level. The original condition was 55% for general-category candidates; the revised reports put it at 60%, with a five-percentage-point relaxation for reserved categories (SC, ST, OBC, women and persons with disabilities).</li>
        <li>Hold quality publications in SCI, SCI-E or Scopus journals, or patents that have been granted.</li>
        <li>Identify a supervisor for the postdoctoral work — an approved PhD guide at the AICTE-approved university or institute where the fellowship will be held — and obtain that supervisor\u2019s consent for mentorship. The supervisor must hold a PhD and must not be superannuated.</li>
        <li>Apply only once in a career: the fellowship can be availed a single time.</li>
      </ul>
      <p>One further condition appears in current guides: candidates holding a regular employment or permanent service position may not qualify, since the fellowship is aimed at researchers pursuing full-time postdoctoral work. Applicants in regular service should check this point on the official portal before applying.</p>
      <h2 id="benefits">What you get — original terms versus revised terms</h2>
      <p>Under the terms the 2024-25 cycle opened with, a fellow received Rs 65,000 a month plus house rent allowance as per applicable norms, and an annual contingency grant of Rs 50,000 for research-related expenses. Under the revised terms reported in October 2026, the fellowship is Rs 80,000 a month plus applicable HRA, with a research grant of Rs 2,00,000 a year — usable for minor equipment, consumables, contingency expenses and domestic travel — and overheads of Rs 50,000 a year. The revised reports are explicit that the scheme provides no financial support for research personnel.</p>
      <p>The tenure is initially one year. If the research work is found satisfactory by the expert committee, it is extended for a further year, giving two years in total, with no provision for extension beyond that.</p>
      <h2 id="selection">How selection works</h2>
      <p>Shortlisting for evaluation takes into account the candidate\u2019s accomplishments at PhD level, the professional standing of the supervisor and of the university where the research will be carried out, and the papers published at the time of application. The evaluation parameters reported for the revised cycle carry 50 marks in total: 10 for undergraduate percentage, 10 for postgraduate percentage, 10 for research publications and patents, 10 for the research proposal, and 10 for interview. A merit list is prepared on that basis, with preference given to candidates with more publications of higher impact factor and granted patents.</p>
      <h2 id="documents">Documents needed</h2>
      <p>No single published document checklist was found in the sources checked. The items below are the ones the scheme\u2019s own process descriptions require applicants to have in hand, and the portal\u2019s current checklist should be treated as authoritative:</p>
      <ul>
        <li>PhD degree certificate — provisional certificates are accepted where the degree has not yet been formally awarded.</li>
        <li>Undergraduate and postgraduate marksheets, for the marks condition and the evaluation weightage.</li>
        <li>Evidence of quality publications or granted patents.</li>
        <li>Supervisor\u2019s consent from an approved PhD guide at the host institution.</li>
        <li>Candidate ID provided by the host institute or university, through which the online application on the AICTE APDF portal is made.</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Secure a supervisor and a host institution first: the application runs through a Candidate ID provided by the institute or university where the fellowship will be held.</li>
        <li>Fill in the online application form on the AICTE APDF portal via aicte.gov.in.</li>
        <li>Check the deadline on the portal itself before submitting — see the note below, because the published dates conflict.</li>
      </ol>
      <h2 id="deadline-note">A deadline conflict you should know about</h2>
      <p>Reports published on 18 October 2026, by Careers360 and Jagran Josh, state that the registration deadline for this 2024-25 fellowship has been extended to 15 November. The text of those reports does not state the year of that 15 November date, and other current guides for the same scheme listed 20 October 2026 — a date that has now passed. This article therefore reports the extension as \u201c15 November\u201d without asserting a year, and advises every applicant to confirm the live deadline on the AICTE portal before preparing an application. Do not treat either published date as settled until the portal confirms it.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the fellowship?', 'That depends on which terms apply to your application: Rs 65,000 a month plus HRA and a Rs 50,000 annual contingency grant under the original terms, or Rs 80,000 a month plus HRA with a Rs 2,00,000 annual research grant and Rs 50,000 overheads under the revised terms reported in October 2026. Confirm the applicable figure on the AICTE portal.'),
   ('How long does it last?', 'One year initially, extendable by one further year on satisfactory work — two years in total, with no further extension.'),
   ('Can I apply if I already hold a regular job?', 'Current guides say regular employees and permanent service holders may not qualify, since the fellowship is for full-time postdoctoral research. Check the portal\u2019s current conditions before applying.'),
   ('Do I need a supervisor before applying?', 'Yes. You must identify a supervisor — an approved PhD guide at the AICTE-approved host institution — and obtain their consent for mentorship.'),
   ('What is the deadline?', 'Extension reports say 15 November, but the year is not stated in the reports checked, and other guides listed 20 October 2026. Confirm the live deadline on the AICTE portal.'),
  ]),
 'verify': 'Verified 31 Oct 2026 against Careers360 (published 18 Oct 2026: PDF 2024-25 deadline extended to 15 Nov; 200 fellowships a year; revised fellowship Rs 80,000 a month plus HRA, research grant Rs 2,00,000 a year, overheads Rs 50,000 a year, no support for research personnel; revised marks condition 60% general with 5% relaxation for reserved categories; publications or granted patents required; 50-mark evaluation split 10 each for UG, PG, publications/patents, proposal and interview) and Jagran Josh (same extension and revised figures; age below 35 with 5-year relaxation for SC/ST/women/PwD and 3 years for OBC; 200 fellows a year), corroborated by PharmaTutor (portal open for applications through the Candidate ID provided by the host institute; 200 fellowships a year; tenure one year extendable by one more year to two years total; supervisor must be an approved PhD guide, not superannuated; original emoluments Rs 65,000 a month plus contingency Rs 50,000 a year) and Telegraph India / Careers360 (original terms: Rs 65,000 a month plus HRA, Rs 50,000 annual contingency; 55% marks condition; provisional PhD certificates accepted). The year of the 15 November extension date is not stated in the reports checked, and other guides listed 20 Oct 2026, so both dates are flagged rather than asserted.',
 'dl_long': 'Extension reported to 15 Nov — the reports checked do not state the year; other guides listed a 20 October date that has now passed; confirm the live deadline on the AICTE portal',
 'offlinks': [('AICTE (official portal)', 'https://www.aicte.gov.in/'), ('Careers360 — AICTE PDF 2024-25 deadline extended, terms revised', 'https://news.careers360.com/aicte-post-doctoral-fellowship-application-extended-24-25-nov-15-phd-eligibility-stipend-selection-rules-revised'), ('Buddy4Study — AICTE Post-doctoral Fellowship (PDF) Scheme', 'https://www.buddy4study.com/scholarship/aicte-post-doctoral-fellowship-pdf-scheme')],
 'related_titles': ['aicte-apf-2026', 'aicte-saksham-2024', 'swanath-2026', 'nsp-pg-2026'],
})

# 4. AICTE Productization Fellowship (APF) 2026
ARTICLES.append({
 'slug': 'aicte-productization-fellowship-apf-2026',
 'title': 'AICTE Productization Fellowship (APF) 2026',
 'meta': 'AICTE Productization Fellowship (APF) 2026: up to Rs 4.94 lakh a year for student teams at AICTE-approved institutions turning a proof-of-concept innovation into a market-ready product — Rs 37,000 a month for up to one year plus a Rs 50,000 annual contingency grant. Applications open all year round through the YUKTI portal.',
 'short': 'AICTE Productization Fellowship (APF) 2026',
 'kicker': 'Fellowship · Innovation',
 'mono': 'AICTE',
 'prov_short': 'AICTE',
 'prov_cat': 'Central Government · AICTE',
 'h1': 'AICTE Productization Fellowship (APF) 2026',
 'sub': 'Not a scholarship for fees and not a business grant for an idea on paper: this fellowship pays student teams to turn a working proof of concept into something that can actually be made, tested and sold. The money is Rs 37,000 a month plus a contingency grant, the work must stay attached to an incubation centre, and applications run all year round.',
 'dpill': 'Always open',
 'facts': facts([
   ('Provider', 'All India Council for Technical Education (AICTE)'),
   ('Award', 'Up to Rs 4.94 lakh per annum: Rs 37,000 a month for a maximum of one year, plus an annual contingency grant of Rs 50,000'),
   ('Eligibility', 'A student or a team of students from an AICTE-approved institution or university department; full-time undergraduate, postgraduate or doctoral students, or graduates within the last two years from an AICTE-approved institution'),
   ('Project stage', 'At least at proof-of-concept (POC) stage — idea-stage proposals are not eligible'),
   ('Team size', 'Normally up to 3 members for one innovative product development proposal'),
   ('Deadline', 'Always open — applications all year round, via the YUKTI portal'),
   ('Selection', 'Proposal evaluated by an expert committee constituted by AICTE'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>The AICTE Productization Fellowship, or APF, supports student teams in higher education who are developing an innovative product or service that addresses a societal challenge or meets a market need. The fellowship covers the unglamorous middle of innovation: proof of concept, prototyping and commercialisation, including raw materials, equipment and testing, along with guidance on intellectual property, business modelling and technology transfer. AICTE presents it as part of the Atmanirbhar Bharat push to turn campus innovation into economic activity, and it sits alongside the YUKTI innovation challenge programme.</p>
      <p>Only one innovative product development project proposal from a student or team is supported, and it runs for a minimum period of one year — either during the programme in which the team members are enrolled, or after its completion, provided the team remains associated with an incubation centre in an AICTE-approved institute. That incubation link is a condition of the fellowship, not an optional extra.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be a student, or a team of students, from an AICTE-approved institution or university department.</li>
        <li>Be a full-time student pursuing an undergraduate, postgraduate or doctoral programme in a higher education institution.</li>
        <li>Passed-out students may apply only if they completed their course or programme from an AICTE-approved institution or university department within the last two years.</li>
        <li>Apply as a team of normally up to 3 members for one proposal; a fourth member is allowed only in special or exceptional cases, according to programme guides.</li>
        <li>Have a project at least at proof-of-concept stage. Idea-stage proposals are not eligible.</li>
        <li>Be willing to remain associated with an incubation centre in an AICTE-approved institute for the fellowship period.</li>
      </ul>
      <p>Programme guides add two practical points. Students from different institutions may apply together, but a bonafide certificate from each institution is then required. Priority is reported for participants or winners of hackathons, grand challenges or innovation competitions, and the fellowship cannot be held alongside other financial assistance during its tenure, according to those guides.</p>
      <h2 id="benefits">What you get</h2>
      <p>Selected candidates receive a monthly stipend of Rs 37,000 for a maximum of one year, plus an annual contingency grant of Rs 50,000. Added together, that is how the headline figure of up to Rs 4.94 lakh per annum is reached: twelve months at Rs 37,000 is Rs 4,44,000, plus the Rs 50,000 contingency grant. The contingency grant is for product-development expenses, and programme guides note that AICTE purchase rules do not apply to it and bills need not be submitted for it.</p>
      <p>One duration conflict is worth flagging. The current programme listing states a maximum of one year for the monthly stipend, while launch coverage from May 2025 described the fellowship as running for up to two years in two stages, with up to 500 teams in stage one and 150 in stage two, and top performers receiving up to Rs 10 lakh each to move from prototype to startup. Those stage figures describe the launch design; this article follows the current listing\u2019s one-year figure for the stipend, and applicants should confirm on the YUKTI portal whether a second stage still applies to their proposal.</p>
      <h2 id="documents">Documents needed</h2>
      <p>No single published document checklist was found in the sources checked. The items a team should have ready, based on the programme\u2019s own requirements, are:</p>
      <ul>
        <li>The innovation or product proposal itself, at proof-of-concept level or beyond.</li>
        <li>Proof of enrolment or graduation (within the last two years) at an AICTE-approved institution.</li>
        <li>Bonafide certificates from each institution, if team members come from different institutions.</li>
        <li>Institute verification through the YUKTI portal — innovators verified by their institutes apply under the portal\u2019s Fellowships/Challenges section.</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Go to the AICTE YUKTI portal (yukti.mic.gov.in) and log in.</li>
        <li>Choose Fellowships/Challenges and find the AICTE Productization Fellowship under the ongoing listings.</li>
        <li>Submit the team\u2019s proposal for evaluation by the AICTE-constituted expert committee. Applications are submitted as a team, not individually.</li>
        <li>Alternatively, use the programme listing\u2019s Apply Now route, register or log in, and complete the application there; the listing states that applications are open all year round.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the fellowship worth?', 'Up to Rs 4.94 lakh a year: Rs 37,000 a month for up to one year plus a Rs 50,000 annual contingency grant.'),
   ('Can I apply with just an idea?', 'No. The project must be at least at proof-of-concept stage; idea-stage proposals are not eligible.'),
   ('Can graduates apply?', 'Yes, if they completed their course from an AICTE-approved institution or university department within the last two years.'),
   ('How big can the team be?', 'Normally up to 3 members for one proposal; a fourth member is allowed only in special or exceptional cases, according to programme guides.'),
   ('Is there a deadline?', 'No fixed deadline is published. The listing states that applications are open all year round, and the portal carries the fellowship under its ongoing listings.'),
   ('Does the fellowship last two years?', 'The current listing states a maximum of one year for the monthly stipend. Launch coverage described a two-stage design of up to two years; confirm the current position on the YUKTI portal before planning around a second year.'),
  ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study AICTE Productization Fellowship (APF) 2026 listing (always open; full-time UG/PG/doctoral students at AICTE-approved institutions, or passed-out students within the last two years; monthly stipend Rs 37,000 for a maximum of one year; annual contingency grant Rs 50,000; headline fellowship up to Rs 4.94 lakh per annum; one proposal per student or team for a minimum of one year, with incubation-centre association; teams normally up to 3 members; project at least at proof-of-concept stage; selection by an AICTE expert committee; applications all year round) corroborated by the AICTE APF guide (YUKTI portal application under Fellowships/Challenges; institute verification; up to 3 innovations or startups per team; POC level minimum, not idea stage) and by launch coverage (Greater Kashmir, May 2025: Rs 37,000 a month for up to two years in two stages, Rs 50,000 annual contingency, up to 500 stage-one and 150 stage-two teams, up to Rs 10 lakh for top performers) and Funds for NGOs (stage-one funding Rs 37,000 a month for a maximum of one year; contingency up to Rs 50,000 a year; one year extendable by one more year including stage two). The one-year versus two-year duration conflict is flagged in the article.',
 'dl_long': 'Always open — applications all year round via the YUKTI portal',
 'offlinks': [('Buddy4Study — AICTE Productization Fellowship (APF) 2026', 'https://www.buddy4study.com/scholarship/aicte-productization-fellowship-apf-2026'), ('AICTE YUKTI portal (apply)', 'https://yukti.mic.gov.in/')],
 'related_titles': ['aicte-pdf-2024', 'aicte-saksham-2024', 'swanath-2026', 'nsp-pg-2026'],
})

# 5. AICTE-Saksham Scholarship Scheme 2024-25
ARTICLES.append({
 'slug': 'aicte-saksham-scholarship-scheme-2024-25',
 'title': 'AICTE-Saksham Scholarship Scheme 2024-25',
 'meta': 'AICTE-Saksham Scholarship Scheme 2024-25: Rs 50,000 a year for specially-abled students in AICTE-approved technical degree or diploma courses — 40% or more disability, family income up to Rs 8 lakh. The scheme continues under later cycles; the live 2026-27 cycle closes today, 31 October 2026.',
 'short': 'AICTE-Saksham Scholarship Scheme 2024-25',
 'kicker': 'Scholarship · Specially-Abled Students',
 'mono': 'AICTE',
 'prov_short': 'AICTE',
 'prov_cat': 'Central Government · AICTE',
 'h1': 'AICTE-Saksham Scholarship Scheme 2024-25',
 'sub': 'A welfare scholarship with no merit cut-off and no cap on awards: every eligible specially-abled student admitted to an AICTE-approved technical degree or diploma course receives Rs 50,000 a year. This page keeps the queue\u2019s 2024-25 title, but the scheme itself continues under later cycles — and the live 2026-27 cycle closes today, 31 October 2026, so read the deadline card first.',
 'dpill': 'Closes today, 31 Oct 2026',
 'facts': facts([
   ('Provider', 'All India Council for Technical Education (AICTE), under the Ministry of Education'),
   ('Award', 'Rs 50,000 per annum as a lump sum for every year of study — up to 4 years for first-year entrants, up to 3 years for lateral-entry entrants'),
   ('Eligibility', 'Specially-abled student with disability of 40% or more; admitted to the first year of a degree or diploma course, or the second year through lateral entry, at an AICTE-approved institution; annual family income from all sources not exceeding Rs 8 lakh'),
   ('What it covers', 'College fee, computer, stationery, books, equipment and software as a lump sum; no separate hostel or medical grant'),
   ('Portal', 'National Scholarship Portal (scholarships.gov.in), after One-Time Registration (OTR)'),
   ('Deadline (live cycle)', '31 Oct 2026 — the 2026-27 window ran 1 Jun to 31 Oct 2026 for fresh and renewal applications; this article was written on the closing day'),
   ('Title note', 'The 2024-25 cycle named in the title has been succeeded by later cycles; the terms below are those of the continuing scheme as published for 2026-27'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>Saksham is AICTE\u2019s scholarship for specially-abled students pursuing technical education in India, launched in the 2014-15 academic year and run ever since as a welfare-based scheme on the National Scholarship Portal. Its most unusual feature is what it does not do: there is no merit cut-off, no state quota to fight over, and no cap on the number of awards. The scheme guidelines and FAQ, as summarised in current guides, state that every eligible student admitted to the first year of a degree or diploma course — or to the second year through lateral entry — receives the scholarship. Selection, in other words, is about meeting the conditions, not about beating other applicants.</p>
      <p>A note on the title. This article carries the queue\u2019s 2024-25 title because that is the entry the writing operation was asked to complete, and the scheme\u2019s terms have not changed between cycles. But the 2024-25 cycle itself is over. The live cycle at the time of writing is 2026-27, and AICTE\u2019s notification of 19 June 2026 invited fresh applications for that batch alongside renewals for the 2023-24 degree batch and the 2024-25 and 2025-26 degree and diploma batches. Everything below — amount, eligibility, documents, steps — is therefore stated for the continuing scheme, with the live cycle\u2019s deadline in the deadline card.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be a specially-abled student with a disability of 40% or more, certified by the competent authority (disability certificate or UDID details).</li>
        <li>Be admitted to the first year of a diploma or degree course, or to the second year through lateral entry, at an AICTE-approved institution in the relevant academic year.</li>
        <li>Have an annual family income from all sources of no more than Rs 8 lakh. A valid income certificate issued by the State or UT Government is required; for married girls, guides note that the higher of the parents\u2019 or in-laws\u2019 income is considered.</li>
        <li>Hold only passing marks in the qualifying examination: no specific minimum percentage beyond passing is required.</li>
      </ul>
      <p>Students already in the second or third year — other than lateral-entry second-year students — are not eligible for a fresh award, according to the scheme FAQ as summarised in current guides. Under AICTE\u2019s corrigendum of 18 August 2026, Saksham is classed as a welfare-based scheme and can be held together with another welfare-based scholarship or with one merit-based scholarship.</p>
      <h2 id="benefits">What you get</h2>
      <p>Each awardee receives Rs 50,000 for every year of study, paid as a lump sum towards college fee, computer, stationery, books, equipment and software, and transferred directly to the student\u2019s bank account through Direct Benefit Transfer. The maximum duration is four years for students admitted in the first year and three years for students admitted directly into the second year through lateral entry. There is no separate grant for hostel fees, medical expenses or similar charges.</p>
      <p>Renewal is not automatic. It requires a renewal application through the NSP, supported by a promotion certificate certified by the Head of the Institution, and it depends on satisfactory academic performance and promotion to the next year. Failing to be promoted ends the scholarship.</p>
      <h2 id="documents">Documents needed</h2>
      <ul>
        <li>Disability certificate or UDID details showing disability of 40% or more (disabled students must log in to the UDID portal and consent to share their UDID details before the application can be submitted, according to the current application guide).</li>
        <li>Annual family income certificate in the prescribed format, issued by the Tehsildar or a higher competent authority, or by the State or UT Government.</li>
        <li>Marksheet of the Class 10 and Class 12 examinations, as applicable.</li>
        <li>Admission letter to the first year of a degree or diploma course, issued by the Centralised Admission Authority or Directorate of Technical Education.</li>
        <li>Tuition fee receipt for the academic year.</li>
        <li>Aadhaar number and an Aadhaar-seeded savings bank account in the student\u2019s own name (with account number, IFSC code and photograph in the passbook).</li>
        <li>Caste certificate, for SC, ST or OBC applicants, where applicable.</li>
        <li>Certificate issued by the Director, Principal or Head of the Institute, and a signed declaration by parents that the information given is correct.</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Open the National Scholarship Portal (scholarships.gov.in) and complete One-Time Registration (OTR) if you have not already done so.</li>
        <li>Disabled students should log in to the UDID portal and consent to share their UDID details, as the NSP application requires that step before submission.</li>
        <li>Under Apply for Scholarship, select AICTE — Saksham Scholarship Scheme for Specially Abled Student (Technical Degree) or (Technical Diploma), listed as a welfare-based scheme.</li>
        <li>Enter the details, attach the income certificate and disability proof, and enter the Aadhaar-seeded savings bank account in the student\u2019s own name.</li>
        <li>Submit before the cycle\u2019s closing date — for the live 2026-27 cycle, that is today, 31 October 2026 — and keep the submitted form and fee receipt for institute verification.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the Saksham scholarship?', 'Rs 50,000 per year as a lump sum, for up to four years (first-year entrants) or three years (lateral-entry entrants).'),
   ('Is there a merit cut-off?', 'No. Only passing marks in the qualifying examination are required, and every eligible student admitted to the first year or lateral-entry second year receives the award, according to the scheme FAQ.'),
   ('What disability level qualifies?', 'A disability of 40% or more, certified by the competent authority or shown through UDID details.'),
   ('What is the income limit?', 'Rs 8 lakh a year from all sources, supported by a valid income certificate from the State or UT Government.'),
   ('Can I hold another scholarship at the same time?', 'Under AICTE\u2019s corrigendum of 18 August 2026, Saksham as a welfare-based scheme can be held with another welfare-based scholarship or one merit-based scholarship.'),
   ('Is the 2024-25 cycle still open?', 'No. The 2024-25 cycle has closed. This article covers the continuing scheme, and the live 2026-27 cycle closes today, 31 October 2026.'),
  ]),
 'verify': 'Verified 31 Oct 2026 against CollegeChalo\u2019s AICTE Saksham 2026-27 guide (checked 5 Oct 2026 against the AICTE notification of 19 June 2026, Saksham degree and diploma guidelines, scheme FAQ and NSP listings: Rs 50,000 a year lump sum for college fee, computer, stationery, books, equipment and software; no cap on awards; first year or lateral-entry second year; 40% or more disability; income up to Rs 8 lakh; 2026-27 window 1 Jun to 31 Oct 2026 for fresh and renewal; NSP OTR plus UDID consent step; income certificate and disability proof plus Aadhaar-seeded account; renewal promotion certificate certified by the Head of Institution; corrigendum of 18 Aug 2026 making Saksham welfare-based and combinable with another welfare-based or one merit-based scholarship) corroborated by Buddy4Study\u2019s Saksham 2026-27 article (same Rs 50,000, 40%, income and 31 Oct 2026 dates; up to 4 years first-year and 3 years lateral entry; no hostel or medical grant; renewal on performance with passing certificate and Head of Institution letter) and by the Unstop and Notopedia scheme summaries (full document list: Class 10/12 marksheets, income certificate from Tehsildar or above, disability certificate, admission letter, institute certificate, tuition fee receipt, Aadhaar-seeded passbook, caste certificate where applicable, parents\u2019 declaration). The 2024-25 title is retained from the queue with the succession to later cycles stated openly in the article.',
 'dl_long': 'Closes today, 31 Oct 2026 — the live 2026-27 window runs 1 Jun to 31 Oct 2026 (the 2024-25 cycle named in the title has been succeeded by later cycles)',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — AICTE Saksham Scholarship Scheme 2026-27', 'https://www.buddy4study.com/article/saksham-scholarship-scheme'), ('CollegeChalo — AICTE Saksham Scholarship 2026-27', 'https://www.collegechalo.com/scholarship/saksham-scholarship')],
 'related_titles': ['aicte-pdf-2024', 'aicte-apf-2026', 'swanath-2026', 'pmss-capf-2026'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

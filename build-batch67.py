import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
OUT = '/home/hatch/workspace/scholarships-17k/articles/'
cards = dict(REGISTRY)

ARTICLES = []

# 1. University of Malta
ARTICLES.append({
 'slug': 'university-of-malta-scholarships-2026-malta',
 'title': 'University of Malta Scholarships 2026 in Malta (Funded)',
 'meta': 'Tuition fee waivers of 40% to 100% at the University of Malta for Master by Research and PhD students from outside the EU/EEA. Check the reported 31 October 2026 round deadline and the eligibility rules before applying.',
 'short': 'University of Malta Scholarships 2026 in Malta (Funded)',
 'kicker': 'Malta · Postgraduate research',
 'mono': 'UM',
 'prov_short': 'University of Malta',
 'prov_cat': 'Scholarship Provider',
 'h1': 'University of Malta Scholarships 2026 in Malta (Funded)',
 'sub': 'A tuition fee waiver of 40% to 100% for non-EU/EEA Master by Research and PhD students at Malta\u2019s public university \u2014 but read the deadline caveat first: the 31 October round date is reported by guides and is not confirmed on the official page excerpt checked, so confirm it with the International Office before relying on it.',
 'dpill': 'Deadline 31 Oct 2026 (reported \u2014 confirm officially)',
 'facts': facts([
   ('Provider', 'University of Malta (public university, Msida, Malta)'),
   ('Award', 'Tuition fee waiver of 40% to 100% for the normal duration of the programme, set by interview score. Living costs, travel and health insurance are not covered; bench fees for certain programmes may still apply'),
   ('Level', 'Master by Research and PhD (full-time or part-time)'),
   ('Deadline', '31 October 2026 (reported by guides; not confirmed on the official page excerpt checked \u2014 confirm with the International Office)'),
   ('Eligibility', 'Students from outside the EU/EEA who are unconditionally accepted for a Master by Research or PhD. Professional doctorates and MBA-type programmes are not eligible'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The University of Malta runs a tuition fee waiver scheme for research-degree students who come from outside the European Union and the European Economic Area. It is aimed at students taking a Master by Research or a PhD, whether full-time or part-time, and it covers a share of the tuition fee for the normal duration of the programme \u2014 not an open-ended extension. The scheme is a fee waiver, not a cash award: it reduces what you owe the university, and it does not pay your rent, travel or health insurance.</p>
      <p>Guides describe three application rounds a year. They agree that 31 October is one of the round dates, but they disagree about the middle round (30 April against 31 May) and about whether the January round falls on 31 January. The official page checked for this article confirms the scheme itself, the 40% to 100% range, the unconditional-acceptance rule and the professional-doctorate and MBA exclusion, but the excerpt checked does not publish a deadline calendar. Because this article is written on 30 October 2026 \u2014 the day before the reported 31 October round \u2014 treat that date as reported, not officially confirmed, and check it with the University of Malta International Office before you rely on it.</p>
      <h2 id="benefits">Benefits</h2>
      <p>The waiver is set by the applicant\u2019s interview score, on a tiered scale reported consistently across guides:</p>
      <ul>
        <li>Interview score 80\u2013100% \u2192 100% tuition fee waiver</li>
        <li>Interview score 70\u201379% \u2192 80% waiver</li>
        <li>Interview score 60\u201369% \u2192 60% waiver</li>
        <li>Interview score 50\u201359% \u2192 40% waiver</li>
        <li>Interview score below 50% \u2192 no waiver</li>
      </ul>
      <p>The waiver applies for the normal duration of the programme. Extensions may not be covered, and bench fees charged by certain programmes may still be payable on top of the waived tuition. Living costs, travel and health insurance are the student\u2019s own responsibility, so budget for Malta\u2019s living costs separately.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a student from outside the EU/EEA.</li>
        <li>You hold an unconditional acceptance for a Master by Research or a PhD at the University of Malta, full-time or part-time.</li>
        <li>Your programme is a research degree \u2014 professional doctorates and MBA-type programmes are excluded by the official page.</li>
        <li>You can attend the interview on which the waiver percentage depends.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Guides report the following as the usual supporting items. The official page should be checked for the current list before you submit:</p>
      <ul>
        <li>Your unconditional acceptance letter for the Master by Research or PhD programme</li>
        <li>A detailed curriculum vitae (CV)</li>
        <li>A motivational letter</li>
        <li>A copy of your passport</li>
        <li>A scholarship request sent to the International Office \u2014 some guides say within one month of unconditional acceptance</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to a Master by Research or PhD programme at the University of Malta and secure an unconditional acceptance.</li>
        <li>Contact the International Office to confirm the current round deadline \u2014 in particular whether the 31 October 2026 round is open and what time it closes.</li>
        <li>Prepare your CV, motivational letter and passport copy, and submit the scholarship request with your acceptance letter.</li>
        <li>Attend the interview, which sets your waiver percentage.</li>
        <li>Wait for the waiver decision, and confirm in writing which fees (including any bench fees) remain payable.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a fully funded scholarship?', 'No. It waives 40% to 100% of tuition fees only. Living costs, travel and health insurance are not covered, and bench fees for certain programmes may still apply.'),
   ('Can MBA or professional doctorate students apply?', 'No. The official page excludes professional doctorates and MBA-type programmes; the scheme is for Master by Research and PhD students.'),
   ('What decides whether I get 40% or 100%?', 'Your interview score, on the tiered scale reported by guides: 80% or above gives a 100% waiver, and each lower band gives a smaller share, with no waiver below 50%.'),
   ('Is the 31 October 2026 deadline confirmed?', 'Not on the official page excerpt checked. Guides agree 31 October is a round date, but the official excerpt publishes no deadline calendar, so confirm the date with the International Office before relying on it.'),
   ('Does the waiver cover extra years if my PhD runs long?', 'It covers the normal duration of the programme; extensions may not be covered.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the University of Malta\u2019s official scholarships page (um.edu.mt/journey/feesfunding/scholarships/masterresearchphd: 40\u2013100% waivers, unconditional acceptance for Master by Research or PhD, professional doctorates and MBA-type programmes excluded) and corroborating guides (Bright Scholarship; EngineersJob) for the interview-score tiers and the three-round pattern. The official excerpt checked publishes no deadline calendar, so the 31 October 2026 round date is reported by guides, not officially confirmed.',
 'dl_long': '31 October 2026 (reported by guides; not confirmed on the official page excerpt checked \u2014 confirm with the University of Malta International Office)',
 'offlinks': [('University of Malta \u2014 Master by Research / PhD Scholarships', 'https://www.um.edu.mt/journey/feesfunding/scholarships/masterresearchphd')],
 'related_titles': ['humboldt-2026', 'fes-2026', 'anu-chanc-2026', 'unicaf-2026'],
})

# 2. UWA Global Excellence Scholarship
ARTICLES.append({
 'slug': 'uwa-global-excellence-scholarship-2026-australia',
 'title': 'UWA Global Excellence Scholarship 2026 in Australia (10\u201320% Tuition Discount)',
 'meta': 'The University of Western Australia Global Excellence Scholarship gives international students a 10% or 20% annual tuition fee discount based on ATAR or WAM. Applications close 22 December 2026.',
 'short': 'UWA Global Excellence Scholarship 2026 in Australia (10\u201320% Tuition Discount)',
 'kicker': 'Australia · Undergraduate & Postgraduate',
 'mono': 'UWA',
 'prov_short': 'University of Western Australia',
 'prov_cat': 'Scholarship Provider',
 'h1': 'UWA Global Excellence Scholarship 2026 in Australia (10\u201320% Tuition Discount)',
 'sub': 'A recurring annual tuition fee discount \u2014 10% or 20% depending on your entry grades \u2014 for international students starting an eligible undergraduate or postgraduate course at the University of Western Australia.',
 'dpill': 'Deadline 22 Dec 2026',
 'facts': facts([
   ('Provider', 'University of Western Australia (UWA), Perth'),
   ('Award', 'Annual tuition fee discount for the normal full-time duration of the course: 10% or 20%, set by ATAR (undergraduate) or WAM (postgraduate)'),
   ('Level', 'Eligible undergraduate and postgraduate courses'),
   ('Deadline', '22 December 2026 (applications open 1 July 2026; official listing status: Open)'),
   ('Eligibility', 'International students with an offer for an eligible UWA course; equivalent ATAR of at least 85 (undergraduate) or equivalent WAM of at least 65 (postgraduate)'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The UWA Global Excellence Scholarship is the University of Western Australia\u2019s merit discount for international students. Rather than a fixed cash total, it cuts a percentage off your tuition fee each year for the normal full-time duration of your course. The official scholarship listing shows the scheme as Open, with applications opening on 1 July 2026 and closing on 22 December 2026.</p>
      <p>Older aggregator pages quote flat totals of up to AUD 48,000 for undergraduates and AUD 24,000 for postgraduates. Those totals are not the operative figure on the current official listing, which expresses the award as the 10% or 20% discount set out below. Use the percentage tiers, not the old totals, when you estimate your costs.</p>
      <h2 id="benefits">Benefits</h2>
      <p>The discount applies every year for the normal full-time duration of the course, at the tier matching your entry grades:</p>
      <ul>
        <li>Undergraduate, equivalent ATAR 85\u201389.95 \u2192 10% annual tuition fee discount</li>
        <li>Undergraduate, equivalent ATAR 90 or above \u2192 20% annual tuition fee discount</li>
        <li>Postgraduate, equivalent WAM 65\u201374.99 \u2192 10% annual tuition fee discount</li>
        <li>Postgraduate, equivalent WAM 75 or above \u2192 20% annual tuition fee discount</li>
      </ul>
      <p>It is a tuition discount only. It does not cover living costs, travel, health cover or other study expenses, and it is distinct from UWA\u2019s separate 10% International Student Award that some guides mention alongside it.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are an international student with an offer for an eligible undergraduate or postgraduate course at UWA.</li>
        <li>Undergraduate entry: an equivalent ATAR of at least 85.</li>
        <li>Postgraduate entry: an equivalent WAM of at least 65.</li>
        <li>You must not have discontinued an equivalent-level course with an immediate break in enrolment after discontinuation \u2014 the official listing states this as a condition.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The official listing excerpt checked does not publish a separate scholarship document checklist. Prepare the documents you would normally need for admission and for proving your grades, and check the official scholarship page for any additional step:</p>
      <ul>
        <li>Your UWA course offer for an eligible programme</li>
        <li>Academic transcripts showing the ATAR or WAM on which the tier is based</li>
        <li>Proof of international student status, as required by the university</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for admission to an eligible undergraduate or postgraduate course at UWA.</li>
        <li>Open the official Global Excellence Scholarship listing and follow the application instructions published there. The listing excerpt checked does not describe a separate scholarship form, so do not assume one exists \u2014 follow the official page exactly.</li>
        <li>Make sure your grades evidence is complete, since the discount tier (10% or 20%) depends on it.</li>
        <li>Submit before the listing closes on 22 December 2026, and keep a copy of your submission.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is the award AUD 48,000 or AUD 24,000?', 'No. Those are older aggregator totals. The current official listing expresses the award as a 10% or 20% annual tuition fee discount, and that is the figure to use.'),
   ('What grades do I need for the 20% tier?', 'Undergraduates need an equivalent ATAR of 90 or above; postgraduates need an equivalent WAM of 75 or above. Below those, at 85 ATAR or 65 WAM, the discount is 10%.'),
   ('Does the discount last for the whole degree?', 'Yes, for the normal full-time duration of the course, at the tier you qualified for.'),
   ('Is there a separate scholarship application form?', 'The official listing excerpt checked does not describe one. Follow the application instructions on the official scholarship page rather than assuming a separate form.'),
   ('When does it close?', '22 December 2026, according to the official listing, which opened applications on 1 July 2026.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the official UWA scholarship listing (uwa.edu.au/study/scholarship-listing/uwa-global-excellence-scholarship-f1917561: status Open, applications open 01/07/2026, close 22/12/2026, ATAR 85+/WAM 65+ thresholds, 10%/20% tiers, discontinuation condition) and the StudyPerth international scholarships page corroborating the 20% Global Excellence / 10% International Student Award distinction.',
 'dl_long': '22 December 2026',
 'offlinks': [('UWA \u2014 Global Excellence Scholarship (official listing)', 'https://www.uwa.edu.au/study/scholarship-listing/uwa-global-excellence-scholarship-f1917561')],
 'related_titles': ['anu-chanc-2026', 'unicaf-2026', 'umdearborn-2026', 'huddersfield-2026'],
})

# 3. University of Twente Scholarship (UTS) 2027
ARTICLES.append({
 'slug': 'university-of-twente-scholarship-2027-netherlands',
 'title': 'University of Twente Scholarship (UTS) 2027 in Netherlands (EUR 3,000\u201322,000)',
 'meta': 'The University of Twente Scholarship (UTS) offers excellent non-EU/EEA Master\u2019s students EUR 3,000 to EUR 22,000 for one year. Applications for September 2027 entry close 1 April 2027 at 16:00 CET.',
 'short': 'University of Twente Scholarship (UTS) 2027 in Netherlands (EUR 3,000\u201322,000)',
 'kicker': 'Netherlands · Master\u2019s',
 'mono': 'UT',
 'prov_short': 'University of Twente',
 'prov_cat': 'Scholarship Provider',
 'h1': 'University of Twente Scholarship (UTS) 2027 in Netherlands (EUR 3,000\u201322,000)',
 'sub': 'A contribution of EUR 3,000 to EUR 22,000 toward study-related costs for excellent non-EU/EEA students starting a Master\u2019s at Twente in September 2027. Read carefully: this is explicitly not a fully funded scholarship \u2014 you fund the remainder yourself.',
 'dpill': 'Deadline 1 Apr 2027, 16:00 CET',
 'facts': facts([
   ('Provider', 'University of Twente (UT), Enschede, Netherlands'),
   ('Award', 'EUR 3,000 to EUR 22,000 for one year, paid as a contribution toward study-related costs \u2014 not paid as tuition on your behalf'),
   ('Level', 'Master\u2019s programmes starting September 2027 (qualifying programmes only)'),
   ('Deadline', '1 April 2027 at 16:00 CET (application form opened 15 October 2026 at 09:00 CET; results in the first week of May 2027)'),
   ('Eligibility', 'Excellent non-EU/EEA students (provisionally) admitted to a qualifying UT Master\u2019s programme starting September 2027, holding a student number; typically the top 5\u201310% of their class'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The University of Twente Scholarship (UTS) is Twente\u2019s merit award for excellent students from outside the EU/EEA who are starting a Master\u2019s programme in September 2027. The application form opened on 15 October 2026 at 09:00 CET and closes on 1 April 2027 at 16:00 CET, with results announced in the first week of May 2027. The university\u2019s own scholarship finder lists the scheme as open until 1 April 2027.</p>
      <p>Older guides describe a two-round structure with a first round closing 1 February 2027 and a second round closing 1 May 2027. The current official-cycle pages use a single closing date \u2014 1 April 2027 \u2014 so do not plan around the old two-round dates.</p>
      <h2 id="benefits">Benefits</h2>
      <p>UTS pays EUR 3,000 to EUR 22,000 for one year. The university is explicit about what that means: the money is a contribution toward study-related costs, it is yours to decide how to spend, and no costs (for example tuition fees) are paid on your behalf. It is not a fully funded scholarship, and you must fund the remainder of your tuition and living costs from other sources.</p>
      <p>For a two-year Master\u2019s, a second-year UTS amount equal to the first year is possible only if, by the end of the third quartile of year one, your average grade is at least 7 out of 10 and you have completed at least 50% of your European Credits. UTS recipients may also be considered for the additional Kipaji Scholarship for programmes starting in September 2027 \u2014 indicate your interest in the application motivation if you are eligible. Only one UT scholarship can be awarded to a student.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are from a non-EU/EEA country and are (provisionally) admitted to a qualifying UT Master\u2019s programme starting in September 2027, and you hold a student number.</li>
        <li>You are an excellent student \u2014 typically in the top 5\u201310% of your class.</li>
        <li>You are not a Dutch student or a current UT student, and you do not pay the statutory tuition fee (which usually applies to EU/EEA students).</li>
        <li>Your programme is not at the Faculty of Geo-Information Science and Earth Observation (ITC), and it is not a pre-Master programme \u2014 both are excluded on the official UTS page. Check the current eligible-programme list before applying.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The official UTS page sets the eligibility conditions and the application route; confirm the current document list on that page before submitting. The usual items for this kind of application are:</p>
      <ul>
        <li>Your (provisional) admission to a qualifying UT Master\u2019s programme and your student number</li>
        <li>Academic transcripts showing your class standing</li>
        <li>A motivation statement (also the place to indicate interest in the Kipaji Scholarship if eligible)</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for a qualifying Master\u2019s programme at the University of Twente and obtain your (provisional) admission and student number.</li>
        <li>Open the official UTS page in the UT scholarship finder and complete the scholarship application form.</li>
        <li>Submit before 1 April 2027 at 16:00 CET.</li>
        <li>Wait for the results in the first week of May 2027, and plan your remaining funding on the understanding that UTS is a partial contribution, not full funding.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is UTS fully funded?', 'No. The university states it plainly: UTS is a contribution toward study-related costs, not a fully funded scholarship, and no tuition is paid on your behalf.'),
   ('What are the old February and May deadlines I see in guides?', 'They belong to an older two-round structure. The current cycle uses a single closing date: 1 April 2027.'),
   ('Can I get UTS for the second year of a two-year Master\u2019s?', 'Only if, by the end of the third quartile of year one, your average grade is at least 7 out of 10 and you have completed at least 50% of your European Credits.'),
   ('Can I hold UTS and another UT scholarship?', 'No \u2014 only one UT scholarship can be awarded to a student, though UTS recipients may additionally be considered for Kipaji.'),
   ('Are ITC programmes eligible?', 'No. The official UTS page excludes Master\u2019s programmes at the Faculty of Geo-Information Science and Earth Observation (ITC), and pre-Master programmes.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the University of Twente\u2019s official scholarship finder (utwente.nl/en/education/scholarship-finder/university-of-twente-scholarship: non-EU/EEA Master\u2019s, contribution not paid as tuition, ITC and pre-Master exclusions, one UT scholarship only, Kipaji consideration for September 2027 starters, results first week of May 2027; finder index: open until 1 April 2027) and corroborating October 2026 guides for the 15 October 2026 opening at 09:00 CET and the 1 April 2027 close at 16:00 CET.',
 'dl_long': '1 April 2027 at 16:00 CET',
 'offlinks': [('University of Twente \u2014 University of Twente Scholarship (UTS)', 'https://www.utwente.nl/en/education/scholarship-finder/university-of-twente-scholarship')],
 'related_titles': ['humboldt-2026', 'fes-2026', 'anu-chanc-2026', 'unicaf-2026'],
})

# 4. Master Mind Scholarship, KU Leuven 2027/28
ARTICLES.append({
 'slug': 'master-mind-scholarship-2027-belgium',
 'title': 'Master Mind Scholarship 2027/28 in Belgium (KU Leuven)',
 'meta': 'The Flemish Master Mind Scholarship at KU Leuven offers EUR 10,750 for an eligible Master\u2019s programme in 2027/28. Applications close 15 January 2027 at 23:59 CET.',
 'short': 'Master Mind Scholarship 2027/28 in Belgium (KU Leuven)',
 'kicker': 'Belgium · Master\u2019s',
 'mono': 'KUL',
 'prov_short': 'KU Leuven',
 'prov_cat': 'Scholarship Provider',
 'h1': 'Master Mind Scholarship 2027/28 in Belgium (KU Leuven)',
 'sub': 'A Flemish-government scholarship for outstanding international Master\u2019s students at KU Leuven, worth EUR 10,750 for the programme \u2014 with a warning: the university itself says the current information is preliminary and subject to change, pending confirmation no later than January 2027.',
 'dpill': 'Deadline 15 Jan 2027, 23:59 CET',
 'facts': facts([
   ('Provider', 'KU Leuven, funded by the Flemish Ministry of Education and Training (Master Mind programme)'),
   ('Award', 'EUR 10,750 for the full length of the programme at KU Leuven (preliminary figure \u2014 see the warning in this article); tuition approximately EUR 1,200 per academic year at the EEA tariff'),
   ('Level', 'Eligible Master\u2019s programmes (60 ECTS: one academic year; 120 ECTS: two academic years); 3 scholarships available at KU Leuven for 2027\u20132028'),
   ('Deadline', '15 January 2027 at 23:59 CET (applications open 15 October 2026; nominated candidates informed by 10 March 2027; one-minute motivational video due 16 March 2027; results end of March 2027)'),
   ('Eligibility', 'High academic performance/potential (high GPA); previous degree from a higher-education institution outside Flanders; applying for an eligible Master\u2019s programme; not already enrolled at a Flemish higher-education institution (with a narrow preparatory-programme exception)'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The Master Mind Scholarship is a Flemish-government award, funded by the Flemish Ministry of Education and Training, for outstanding students from abroad who come to Flanders for a Master\u2019s degree. At KU Leuven, 3 scholarships are available for the 2027\u20132028 academic year. Applications opened on 15 October 2026 and close on 15 January 2027 at 23:59 CET.</p>
      <p>Read the warning before you plan around the amount: KU Leuven\u2019s own page states that the current information is preliminary and subject to change, pending confirmation no later than January 2027. Some official sections still show EUR 10,225 rather than EUR 10,750. Treat EUR 10,750 as the current published figure, not as final, until that confirmation lands.</p>
      <p>Do not confuse this with the University of Antwerp\u2019s Master Mind variant, which is a different award at a different university: a EUR 5,375 one-time grant plus the standard tuition amount (EUR 1,181.40 for 60 credits in 2026\u20132027), with a 1 February 2027 deadline and 5 scholarships at Antwerp. This article covers KU Leuven only.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A scholarship of EUR 10,750 to cover the full length of the programme at KU Leuven (preliminary figure, as warned above).</li>
        <li>Tuition at approximately EUR 1,200 per academic year at the EEA tariff.</li>
        <li>Duration: one academic year for a 60 ECTS Master\u2019s, two academic years for a 120 ECTS Master\u2019s.</li>
        <li>One application also gives automatic consideration for the Inspiring the Outstanding Scholarship, the KU Leuven ASEAN Scholarship, the KU Leuven Scholarship for Africa, and the KU Leuven Scholarship for Central and South America, subject to nationality conditions.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You show a high standard of academic performance and potential, evidenced by a high GPA.</li>
        <li>Your previous degree is from a higher-education institution outside Flanders (credit mobility in Flanders can still be eligible).</li>
        <li>You are applying for an eligible Master\u2019s programme at KU Leuven. Bridging programmes and distance-learning programmes are not eligible.</li>
        <li>You are not already enrolled at a Flemish higher-education institution, except for a specific preparatory programme for September 2027 starters.</li>
        <li>You cannot combine this award with another KU Leuven, Belgian-government or European Commission scholarship.</li>
        <li>English: your test must be taken before 15 January 2027. Secondary guides give TOEFL 94, IELTS 7.0 or Cambridge CPE at C2, and results may be added after the deadline. Exemptions apply if you completed an English-taught degree in Australia, English-speaking Canada, Ireland, New Zealand, the UK or the USA.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The two-step application below defines what you must submit. In practice, prepare:</p>
      <ul>
        <li>A complete application file for your eligible Master\u2019s programme, including the KU Leuven Scholarships &amp; Master Mind Candidacy Form uploaded as an \u201cAnnexe\u201d</li>
        <li>Your registration of scholarship candidacy through the online registration tool</li>
        <li>Academic transcripts and proof of your previous degree</li>
        <li>English test evidence (taken before 15 January 2027; results may be added after the deadline)</li>
        <li>If nominated: a one-minute motivational video, due by 16 March 2027</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete both steps by 15 January 2027 at 23:59 CET: (1) submit a complete application file for an eligible Master\u2019s programme, with the KU Leuven Scholarships &amp; Master Mind Candidacy Form uploaded as an \u201cAnnexe\u201d; (2) register your scholarship candidacy via the online registration tool.</li>
        <li>Take your English test before 15 January 2027 (results may follow after the deadline).</li>
        <li>If you are nominated, you will be informed by 10 March 2027; submit your one-minute motivational video by 16 March 2027.</li>
        <li>Selection results are announced at the end of March 2027. Watch for the January 2027 confirmation of the scholarship amount before treating EUR 10,750 as final.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is EUR 10,750 final?', 'No. KU Leuven states the information is preliminary and subject to change, pending confirmation no later than January 2027, and some official sections still show EUR 10,225.'),
   ('Is this the same as the Antwerp Master Mind Scholarship?', 'No. Antwerp offers a EUR 5,375 one-time grant plus the standard tuition amount, with its own 1 February 2027 deadline and 5 scholarships. This article covers KU Leuven only.'),
   ('Do I need a separate application for the other KU Leuven scholarships?', 'No. One Master Mind application gives automatic consideration for the Inspiring the Outstanding, ASEAN, Africa and Central and South America scholarships, subject to nationality conditions.'),
   ('Can I combine Master Mind with another scholarship?', 'No. It cannot be combined with another KU Leuven, Belgian-government or European Commission scholarship.'),
   ('When do I hear the result?', 'Nominated candidates are informed by 10 March 2027, submit a one-minute video by 16 March 2027, and selection results come at the end of March 2027.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the official KU Leuven page (kuleuven.be/scholarships/year/2027-2028/master-mind-scholarship: applications open 15 October 2026, deadline 15 January 2027 at 23:59 CET, two-step application, nomination by 10 March 2027, video by 16 March 2027, results end of March 2027, EUR 10,750 preliminary, tuition approximately EUR 1,200 per year, 3 scholarships, preliminary-information warning) and the University of Antwerp Master Mind page for the distinct Antwerp variant.',
 'dl_long': '15 January 2027 at 23:59 CET',
 'offlinks': [('KU Leuven \u2014 Master Mind Scholarship 2027/28', 'https://www.kuleuven.be/scholarships/year/2027-2028/master-mind-scholarship')],
 'related_titles': ['humboldt-2026', 'fes-2026', 'harvard-mba-2027', 'anu-chanc-2026'],
})

# 5. IMF Fund Internship Program (FIP) 2027
ARTICLES.append({
 'slug': 'imf-fund-internship-program-2027-usa',
 'title': 'IMF Fund Internship Program 2027 (FIP) \u2013 Economists, Paid Internship in Washington, D.C.',
 'meta': 'The IMF Fund Internship Program for Economists is a paid 10\u201312 week internship at IMF Headquarters in Washington, D.C., from 7 June to 27 August 2027, for PhD students in macroeconomics or a related field. Apply by 5 December 2026.',
 'short': 'IMF Fund Internship Program 2027 (FIP) \u2013 Economists, Paid Internship in Washington, D.C.',
 'kicker': 'USA · Internship',
 'mono': 'IMF',
 'prov_short': 'International Monetary Fund',
 'prov_cat': 'Scholarship Provider',
 'h1': 'IMF Fund Internship Program 2027 (FIP) \u2013 Economists, Paid Internship in Washington, D.C.',
 'sub': 'A paid, full-time 10\u201312 week research internship at IMF Headquarters in Washington, D.C., for PhD students in macroeconomics or a related field \u2014 working on real policy research alongside IMF economists in summer 2027.',
 'dpill': 'Deadline 5 Dec 2026 (one guide gives 4 Dec \u2014 apply by 4 Dec to be safe)',
 'facts': facts([
   ('Provider', 'International Monetary Fund (IMF), Washington, D.C., USA'),
   ('Award', 'Paid full-time internship, 40 hours a week, for 10\u201312 weeks. The stipend amount was not stated in the guides checked, so none is stated here. Guides report round-trip restricted economy air travel and limited medical insurance; interns arrange their own accommodation'),
   ('Level', 'PhD students in macroeconomics or a related field, within one to two years of completing the PhD'),
   ('Deadline', '5 December 2026 (most guides; one guide gives 4 December 2026 \u2014 apply by 4 December to be safe)'),
   ('Eligibility', 'PhD student in macroeconomics or a related field, enrolled at the time of the internship and returning to academic studies afterward; under 32 when the internship begins in June 2027 (military-service exception only); excellent written and spoken English; strong analytical, quantitative and computer skills; previous FIP participants cannot reapply'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>The Fund Internship Program (FIP) for Economists is the International Monetary Fund\u2019s summer internship for economics PhD students. Interns spend 10 to 12 weeks, full-time at 40 hours a week, at IMF Headquarters in Washington, D.C., from 7 June 2027 to 27 August 2027, working on an individual research project under an IMF supervisor and alongside experienced economists. Research areas can include inflation, financial stability, inequality and digital transformation, and interns may present their findings to IMF staff.</p>
      <p>The internship is paid, but the stipend amount was not stated in the guides checked, so this article states no figure. Guides report round-trip restricted economy-class air travel between the intern\u2019s university and Washington, D.C., and limited medical insurance. Housing is not provided: interns arrange their own accommodation, so budget for Washington, D.C. rents separately.</p>
      <p>On the deadline, most guides agree on 5 December 2026, but one guide gives 4 December 2026 (11:59 p.m. Washington, D.C. time). Because the difference is a single day, apply by 4 December 2026 to be safe, and check the live vacancy on the IMF Careers portal for the confirmed closing time.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A paid, full-time internship (40 hours a week) for 10 to 12 weeks at IMF Headquarters.</li>
        <li>Hands-on macroeconomic research experience on a real policy project, with an IMF supervisor.</li>
        <li>Guides report round-trip restricted economy air travel and limited medical insurance.</li>
        <li>G4 visa documentation support for non-US citizens and residents who need it.</li>
        <li>The chance to present research findings and build a network inside international economic policy.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a PhD student in macroeconomics or a related field, within one to two years of completing the PhD.</li>
        <li>You are enrolled as a student at the time of the internship and will return to academic studies afterward.</li>
        <li>You are under 32 when the internship begins in June 2027. The only exception to the age limit is time spent in mandatory military service.</li>
        <li>You have excellent written and spoken English, and strong analytical, quantitative and computer skills.</li>
        <li>You have not previously taken part in the Fund Internship Program \u2014 previous participants cannot reapply.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ul>
        <li>CV or r\u00e9sum\u00e9</li>
        <li>Statement of interest or cover letter explaining your motivation for joining the IMF</li>
        <li>Evidence of current student status and academic performance \u2014 a recent transcript, or an official letter confirming active enrolment and recent grades</li>
        <li>The completed online technical questionnaire, which is part of the application</li>
      </ul>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the official IMF Careers portal and find the 2027 Fund Internship Program (FIP) \u2013 Economists vacancy.</li>
        <li>Complete the online application and the technical questionnaire.</li>
        <li>Upload your CV, your statement of interest or cover letter, and your transcript or enrolment-and-grades letter.</li>
        <li>Review everything and submit before the deadline \u2014 by 4 December 2026 to be safe against the one guide that gives 4 December rather than 5 December. Incomplete applications are not considered.</li>
        <li>Wait for contact: you will receive an automated confirmation, and only shortlisted candidates are contacted for further consideration.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('What is the stipend?', 'The internship is paid, but the stipend amount was not stated in the guides checked, so this article states no figure. Check the live IMF vacancy for the current compensation terms.'),
   ('Is accommodation provided?', 'No. Guides state interns arrange their own accommodation, so budget for Washington, D.C. housing separately.'),
   ('What is the real deadline, 4 or 5 December 2026?', 'Most guides give 5 December 2026, but one gives 4 December 2026. Apply by 4 December to be safe, and check the live vacancy for the confirmed closing time.'),
   ('Can I apply if I already did FIP?', 'No. Previous Fund Internship Program participants are not eligible to reapply.'),
   ('Do I need a US work visa?', 'Non-US citizens and residents receive G4 visa documentation support from the IMF; the IMF provides the supporting documentation for the visa process.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against five corroborating 2027 FIP guides (After School Africa; Opportunities for Youth; YouthExpat; Opportunities Radar; ScholarshipsEdge) agreeing on the 5 December 2026 deadline, the 7 June\u201327 August 2027 dates, the 10\u201312 week full-time format, and the eligibility rules, plus the official IMF Fund Internship Program page (imf.org/en/About/Recruitment/working-at-the-imf/fund-internship-program) as the application route. One guide (OpportunityLab) gives 4 December 2026, so the article advises applying by 4 December. No stipend amount was stated in the guides checked, so none is stated.',
 'dl_long': '5 December 2026 (most guides; one guide gives 4 December 2026 \u2014 apply by 4 December to be safe)',
 'offlinks': [('IMF \u2014 Fund Internship Program', 'https://www.imf.org/en/About/Recruitment/working-at-the-imf/fund-internship-program')],
 'related_titles': ['ifad-2026', 'cern-stag-2026', 'hennge-2026', 'unhcr-2026'],
})

from pathlib import Path
for a in ARTICLES:
    build_article(BASE, Path(OUT), a, cards)
    print('built', a['slug'])

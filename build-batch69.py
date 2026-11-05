import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'csir-nehru': {'mono': 'CSIR', 'title': 'CSIR-Nehru Science Postdoctoral Research Fellowship Scheme',
   'href': 'csir-nehru-science-postdoctoral-research-fellowship.html',
   'dpill': 'Always open (selections June & December)',
   'award': 'A consolidated fellowship of \u20b980,000 a month plus house rent allowance and a \u20b93,00,000 annual contingency grant, for two years extendable by one more year, to work in a CSIR laboratory.',
   'elig': 'PhD holders within three years of the award of the degree, or those who have submitted their thesis, with publications in high-impact SCI journals, aged up to 32 (with relaxations). Applications must come through a sponsoring CSIR laboratory.',
   'tags': [('Postdoctoral', 'purple'), ('India', 'teal')]},
 'eastman-2026': {'mono': 'EAPL', 'title': 'Eastman Powerup Eduskill Scholarship Program 2026-27',
   'href': 'eastman-powerup-eduskill-scholarship-program-2026-27.html',
   'dpill': 'Deadline 31 Oct 2026 (latest reported date)',
   'award': 'Up to \u20b920,000 in milestone-based support, released as the scholar completes four approved online certification courses within the programme timelines.',
   'elig': 'Full-time B.Tech, M.Tech, MBA/PGDM or Polytechnic diploma students in Electrical, Electronics, Mechanical, Sales or Marketing streams, with at least 60% marks or CGPA 6.0, no active backlogs, and annual parental income up to \u20b96 lakh.',
   'tags': [('Undergraduate', 'blue'), ('India', 'teal')]},
 'elf-sadhana': {'mono': 'SF', 'title': 'Environmental Leaders Fellowship',
   'href': 'environmental-leaders-fellowship.html',
   'dpill': 'Applications year-round',
   'award': 'A two-year, full-time fellowship in ecosystem restoration: intensive training at Sadhana Forest Auroville followed by service in rural centres in India, Haiti, Kenya and Namibia, with food, accommodation and a small stipend provided.',
   'elig': 'Anyone aged 18 or over with dedication and a willingness to learn and serve; no prior experience is required. Fellows commit to a 100% vegan, substance-free, full-time community life for the whole fellowship.',
   'tags': [('Fellowship', 'purple'), ('India', 'teal')]},
 'kalpana-2026': {'mono': 'KC', 'title': 'NSP Kalpana Chawla Chatravriti Yojana, Himachal Pradesh 2026-27',
   'href': 'nsp-kalpana-chawla-chatravriti-yojana-himachal-pradesh-2026-27.html',
   'dpill': 'Deadline 31 Oct 2026',
   'award': '\u20b915,000 a year for general academic courses and up to \u20b918,000 a year for professional and technical courses, for up to 2,000 meritorious girl students of Himachal Pradesh, renewable through the course.',
   'elig': 'Girl students domiciled in Himachal Pradesh who passed Class 12 from the Himachal Pradesh Board of School Education and figure on its merit list, and are admitted to a post-Class 12 course at a recognised institute.',
   'tags': [('Undergraduate', 'blue'), ('Himachal Pradesh', 'teal')]},
 'kindcircle-2026': {'mono': 'KCL', 'title': 'Kind Circle Scholarship for Meritorious Students 2026-27',
   'href': 'kind-circle-scholarship-for-meritorious-students-2026-27.html',
   'dpill': 'Deadline 31 Mar 2027',
   'award': 'Need-based support starting at a minimum of \u20b96,000, with the final amount decided on financial need and interview performance, paid as a one-time award direct to the scholar\u2019s bank account.',
   'elig': 'Students from Class 1 to postgraduate level at a recognised Indian school or college, with at least 60% marks in the previous academic year and annual family income below \u20b96 lakh.',
   'tags': [('School & College', 'blue'), ('India', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. CSIR-Nehru
ARTICLES.append({
 'slug': 'csir-nehru-science-postdoctoral-research-fellowship',
 'title': 'CSIR-Nehru Science Postdoctoral Research Fellowship Scheme',
 'meta': 'The CSIR-Nehru Science Postdoctoral Research Fellowship: \u20b980,000 a month plus a \u20b93 lakh annual contingency grant for two years in a CSIR laboratory, for recent PhD holders with strong publications. Applications are open all year, with selections in June and December.',
 'short': 'CSIR-Nehru Science Postdoctoral Research Fellowship Scheme',
 'kicker': 'India \u00b7 Postdoctoral Fellowship',
 'mono': 'CSIR',
 'prov_short': 'Council of Scientific & Industrial Research (CSIR)',
 'prov_cat': 'Central Government \u00b7 India',
 'h1': 'CSIR-Nehru Science Postdoctoral Research Fellowship Scheme',
 'sub': 'The CSIR-Nehru Science Postdoctoral Research Fellowship is for a researcher who has just finished a PhD and wants two years inside a Council of Scientific & Industrial Research laboratory, working on their own idea in basic science, engineering, medicine or agriculture. There is no single closing date: you can apply at any time of the year, but selections happen only twice a year, in June and December, and your application has to come through a sponsoring CSIR laboratory. One figure needs care \u2014 the monthly amount has risen over the years and older official pages still show lower rates, so this article states the current listing figure and the older figures side by side.',
 'dpill': 'Always open (selections June & December)',
 'facts': facts([
   ('Provider', 'Council of Scientific & Industrial Research (CSIR), through its Human Resource Development Group (HRDG)'),
   ('Award', 'Consolidated fellowship of \u20b980,000 a month plus house rent allowance as admissible, and a contingency grant of \u20b93,00,000 a year, up to 25% of which may be used for domestic and international travel including per diem. Older official pages still show \u20b935,000, \u20b950,000 or \u20b965,000 a month \u2014 confirm the current rate with CSIR-HRDG before applying'),
   ('Level', 'Postdoctoral \u2014 PhD holders and thesis-submitted candidates'),
   ('Deadline', 'Always open: applications any time of the year; selections twice a year, in June and December (applications for a round are expected about two months before the selection)'),
   ('Eligibility', 'PhD awarded within three years, or thesis submitted; research publications in high-impact SCI journals; maximum age 32, with relaxations (up to 5 years for SC/ST/physically handicapped/women candidates and 3 years for OBC non-creamy layer, per the Buddy4Study listing)'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>The Nehru Science Postdoctoral Research Fellowship was set up to find promising young researchers with innovative ideas and give them training and research opportunities in niche areas of basic science, engineering, medicine and agriculture. The fellowship is tenable at a CSIR laboratory, and CSIR intends to award around 100 such fellowships every year. It is a full-time research position, not a study scholarship: you propose a project, you are hosted by a laboratory, and you are expected to publish and present as a working researcher.</p>
      <p>Two features of this scheme catch applicants out, so note them early. First, you cannot simply apply to CSIR directly: your application must be routed through the sponsoring CSIR laboratory, and it must carry the attestation of that laboratory\u2019s Director \u2014 an application without it is not considered. Second, you cannot apply from the CSIR laboratory where you did your PhD. If your doctorate came from a particular CSIR laboratory, that laboratory cannot sponsor you under this scheme.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A consolidated fellowship of \u20b980,000 a month, as given in the current Buddy4Study listing and in recent fellowship guides, plus house rent allowance as admissible.</li>
        <li>A contingency grant of \u20b93,00,000 a year. Up to 25% of it may be used for domestic and international travel, including per diem expenses.</li>
        <li>A tenure of two years, extendable for a maximum of one more year on outstanding performance and on the recommendation of the Director of the host CSIR laboratory.</li>
        <li>Access to a CSIR laboratory\u2019s research facilities and research community for the whole tenure.</li>
      </ul>
      <p>A note on the monthly figure, because the sources genuinely disagree. The CSIR document hosted on csir.res.in still states \u20b935,000 a month, the India Science, Technology &amp; Innovation portal states \u20b950,000 a month on one page and \u20b965,000 on another, and the current Buddy4Study listing together with recent guides states \u20b980,000. The direction of travel is clear \u2014 the rate has been revised upward more than once \u2014 but the official pages checked have not all been updated to the same figure. This article uses \u20b980,000 because it is the figure in the most recent listings, and it flags the older figures here rather than hiding them. Before you plan a move around this fellowship, confirm the rate in force with CSIR-HRDG or with your sponsoring laboratory.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You hold a PhD awarded within three years, or you have submitted your PhD thesis. Candidates who are about to submit a thesis are also eligible, but selection is conditional on the thesis being submitted before the award offer\u2019s validity expires.</li>
        <li>You have research publications in high-impact-factor SCI journals.</li>
        <li>Your maximum age is 32 years. Relaxation is up to 5 years for SC/ST, physically handicapped and women candidates and 3 years for OBC non-creamy layer candidates, as stated in the Buddy4Study listing; one older official page groups OBC candidates with the 5-year relaxation, so confirm the relaxation that applies to you.</li>
        <li>You are an Indian national, a Person of Indian Origin (PIO) or an Overseas Citizen of India (OCI). Up to 20% of the fellowships may be offered to foreign nationals.</li>
        <li>You have a sponsoring CSIR laboratory willing to host you, other than the laboratory where you completed your PhD.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No separate document checklist is published in the sources checked for this scheme, so none is invented here. What the scheme does require is specific: the application must be made in the prescribed format available from CSIR-HRDG, routed through the sponsoring CSIR laboratory, and attested by that laboratory\u2019s Director. Keep your PhD award or thesis-submission proof, your publication list, and your proposed research project ready in the prescribed format, and confirm the current format and submission address with CSIR-HRDG before sending anything, since the contact officer named on older pages may have changed.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Identify a CSIR laboratory working in your area and agree a research proposal and hosting arrangement with a scientist there. Do not skip this step: the laboratory is your sponsor, not just your destination.</li>
        <li>Complete the application in the prescribed format available from CSIR-HRDG.</li>
        <li>Route the application through the sponsoring laboratory and obtain the Director\u2019s attestation.</li>
        <li>Submit at any time of the year, but aim to reach CSIR about two months before a selection round if you want to be considered in that round: selections are made twice a year, usually in June and December.</li>
        <li>Shortlisted candidates are assessed on a presentation of the proposed research project, followed by an interview by a specially constituted committee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is there a deadline?', 'No single closing date. Applications can be submitted at any time of the year, but selections are made only in June and December, so timing your submission about two months before a round matters.'),
   ('How much does the fellowship actually pay?', 'The most recent listings state \u20b980,000 a month plus HRA and a \u20b93,00,000 annual contingency grant. Older official pages still show \u20b935,000, \u20b950,000 or \u20b965,000 a month, so confirm the current rate with CSIR-HRDG before applying.'),
   ('Can I apply if I have submitted my thesis but not yet received my PhD?', 'Yes. Thesis-submitted candidates are eligible, and candidates about to submit may also apply, but selection is conditional on submitting the thesis before the award offer expires.'),
   ('Can I apply to the laboratory where I did my PhD?', 'No. Candidates who worked for their PhD from a particular CSIR laboratory are not eligible to apply from that same laboratory under this scheme.'),
   ('How long does the fellowship last?', 'Two years, extendable for a maximum of one more year on outstanding performance and on the recommendation of the host laboratory\u2019s Director.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the Buddy4Study scheme listing (CSIR-Nehru: \u20b980,000 a month, \u20b93,00,000 annual contingency, 25% travel, any-time applications, June/December selections, 2 years plus 1 year extension, age 32 with 5-year/3-year relaxations, Director attestation), the CSIR-hosted scheme document (eligibility, tenure, routing through a sponsoring laboratory, older \u20b935,000 rate), the India Science, Technology &amp; Innovation portal (100 fellowships a year, up to 20% foreign nationals, same-laboratory exclusion, \u20b950,000/\u20b965,000 figures on different pages) and recent fellowship guides. The monthly-rate disagreement is carried openly in the article.',
 'dl_long': 'Always open \u2014 applications any time of the year; selections in June and December (apply about two months before a round)',
 'offlinks': [('Buddy4Study \u2014 CSIR-Nehru Science Postdoctoral Research Fellowship Scheme', 'https://www.buddy4study.com/scholarship/csir-nehru-science-postdoctoral-research-fellowship'), ('CSIR \u2014 Nehru Fellowship scheme document (PDF)', 'https://www.csir.res.in/sites/default/files/2023-05/nehrufellowship%20%281%29.pdf'), ('India Science, Technology & Innovation Portal \u2014 CSIR-Nehru Scheme', 'https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/post-doctoral/csir-nehru-science-postdoctoral-research-fellowship-scheme')],
 'related_titles': ['eastman-2026', 'kalpana-2026', 'kindcircle-2026', 'bif-md'],
})

# 2. Eastman
ARTICLES.append({
 'slug': 'eastman-powerup-eduskill-scholarship-program-2026-27',
 'title': 'Eastman Powerup Eduskill Scholarship Program 2026-27',
 'meta': 'Eastman Powerup Eduskill Scholarship 2026-27: up to \u20b920,000 in milestone-based support for engineering, diploma and management students who complete four approved certification courses. Latest reported deadline 31 October 2026.',
 'short': 'Eastman Powerup Eduskill Scholarship Program 2026-27',
 'kicker': 'India \u00b7 Undergraduate & Postgraduate',
 'mono': 'EAPL',
 'prov_short': 'Eastman Auto and Power Limited (EAPL)',
 'prov_cat': 'CSR \u00b7 India',
 'h1': 'Eastman Powerup Eduskill Scholarship Program 2026-27',
 'sub': 'The Eastman Powerup Eduskill Scholarship is not a plain tuition grant. It pairs money with skill-building: selected engineering, diploma and management students complete four approved online certification courses, and the financial support of up to \u20b920,000 is released in milestones as those courses are completed. The deadline needs a warning \u2014 earlier listings gave 31 July and 30 September 2026, while the most recent October reporting gives 31 October 2026, so treat this as closing imminently and confirm the live date on the application page before you rely on it.',
 'dpill': 'Deadline 31 Oct 2026 (latest reported date)',
 'facts': facts([
   ('Provider', 'Eastman Auto and Power Limited (EAPL), through Buddy4Study'),
   ('Award', 'Up to \u20b920,000, disbursed in milestones on successful completion of four approved certification courses (platforms named in guides include Coursera and Udemy); the amount is not paid as a single upfront sum'),
   ('Level', 'Full-time B.Tech, M.Tech, MBA/PGDM and Polytechnic diploma students in India'),
   ('Deadline', '31 October 2026, per the most recent October 2026 reporting. Earlier listings gave 31 July 2026 and 30 September 2026 \u2014 confirm the live date on the Buddy4Study page; do not assume an extension'),
   ('Eligibility', 'B.Tech lateral-entry, 3rd/4th-year or 2026 graduating-batch students; M.Tech 2nd-year or 2026 graduating-batch students; MBA/PGDM 2nd-year or 2026 graduating-batch students in Sales or Marketing; Polytechnic diploma 3rd-year students. At least 60% marks or CGPA 6.0, no active backlogs or disciplinary issues, annual parental income up to \u20b96 lakh'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>Eastman Auto and Power Limited (EAPL) runs this programme for students from financially constrained backgrounds who are close to finishing a technical or management qualification. The idea is to close the gap between a degree and a job: instead of only reimbursing fees, the programme requires scholars to complete industry-relevant certification courses, so that a student leaves with both a degree and certificates an employer recognises. Guides name platforms such as Coursera and Udemy for the approved courses, and give scholars four to five months to complete them.</p>
      <p>The important consequence is that selection is only the start. A scholar who does not complete the required courses within the programme timelines may become ineligible for subsequent milestones, so the money follows completion, not just selection.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Financial assistance of up to \u20b920,000 in total, released milestone by milestone as each approved certification course is completed and verified.</li>
        <li>Access to approved online certification courses in industry-relevant areas, to be completed within the programme timelines (guides give four to five months for course completion).</li>
        <li>Support that may also be used for academic expenses such as tuition, hostel and digital study resources, as described in programme guides; the core mechanism remains course completion.</li>
        <li>Priority in selection for female students, persons with disabilities, single-parent or orphaned students, and candidates from Tier-2 and Tier-3 cities, as reported in programme guides. Priority does not replace the basic eligibility conditions.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are enrolled full-time in a B.Tech, M.Tech, MBA/PGDM or Polytechnic diploma programme at a recognised government or private institution in India.</li>
        <li>Your course and year fit one of the programme categories: B.Tech lateral entry, 3rd or 4th year, or graduating batch of 2026; M.Tech 2nd year or graduating batch of 2026; MBA/PGDM 2nd year or graduating batch of 2026 in Sales or Marketing; Polytechnic diploma 3rd year.</li>
        <li>Your stream fits the programme: Electrical, Electronics or Mechanical for engineering and diploma categories, and Sales or Marketing for MBA/PGDM, depending on the scholarship category.</li>
        <li>You have secured at least 60% marks or a CGPA of 6.0 or above. One guide reports this standard as applying consistently from Class 10 onwards; confirm the exact academic rule on the application page.</li>
        <li>You have no active backlogs and no disciplinary issues, and you are willing to complete the online certification courses within the programme timelines.</li>
        <li>Your annual parental income does not exceed \u20b96 lakh.</li>
        <li>You are not the child of an employee of Eastman Auto and Power Limited or Buddy4Study.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No separate document checklist for this programme was published in the guides checked, so none is invented here. In practice, an application of this kind asks for proof of enrolment and year of study, academic marksheets, income proof for the \u20b96 lakh limit, and identity and bank details for payment. Keep those ready and follow the document list shown on the Buddy4Study application page itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm first that your course, year and stream fit a programme category above, and that the live deadline on the Buddy4Study page has not passed: earlier listings gave 31 July and 30 September 2026, and only the most recent October reporting gives 31 October 2026.</li>
        <li>Apply online through the Buddy4Study portal for the Eastman Powerup Eduskill Scholarship Program 2026-27.</li>
        <li>Complete the application with your academic, income and course details and submit before the live deadline.</li>
        <li>If selected, enrol in the approved certification courses promptly: the \u20b920,000 is released in milestones only as courses are completed within the programme timelines.</li>
        <li>Submit proof of each course completion as required, and keep the timeline in mind \u2014 missing it can cost later milestones.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is the \u20b920,000 paid at once?', 'No. It is milestone-based: the amount is released as the scholar completes the four approved certification courses within the programme timelines, up to a total of \u20b920,000.'),
   ('What is the real deadline?', 'The most recent October 2026 reporting gives 31 October 2026. Earlier listings gave 31 July 2026 and 30 September 2026, so the date has moved before; confirm the live date on the Buddy4Study page and do not assume a further extension.'),
   ('Who exactly can apply?', 'Full-time B.Tech (lateral entry, 3rd/4th year or 2026 graduating batch), M.Tech (2nd year or 2026 graduating batch), MBA/PGDM in Sales or Marketing (2nd year or 2026 graduating batch) and Polytechnic diploma (3rd year) students in the named streams, with 60% or CGPA 6.0, no active backlogs, and parental income up to \u20b96 lakh.'),
   ('Do I have to pay for the courses first?', 'Guides describe the support as milestone-based reimbursement linked to course completion: you complete approved courses and the support follows verification. Check the current programme terms on the application page for exactly how each milestone is paid.'),
   ('Does priority for female, disabled or Tier-2/3-city students guarantee selection?', 'No. Priority is reported as a selection preference only; the academic, income and course conditions still have to be met.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against October 2026 reporting (Citizen News Puttur and The Hans India scholarship listings: up to \u20b920,000, milestone-based on four courses, 31 October 2026), earlier guides (Internshala, Rediff, ScholarshipsX: 31 July 2026; The AS Hub: 30 September 2026), and programme guides for eligibility (course/year categories, Electrical/Electronics/Mechanical/Sales/Marketing streams, 60% or CGPA 6.0, no backlogs, \u20b96 lakh income limit, employee-children exclusion, female/PwD/single-parent/orphan/Tier-2/3 priority). The deadline movement is carried openly in the article.',
 'dl_long': '31 October 2026 (latest reported date \u2014 earlier listings gave 31 July and 30 September 2026; confirm the live date before applying)',
 'offlinks': [('Buddy4Study \u2014 Eastman Powerup Eduskill Scholarship Program', 'https://www.buddy4study.com/scholarship/eastman-powerup-eduskill-scholarship-program'), ('Citizen News Puttur \u2014 Eastman Scholarship 2026-27 (31 October 2026)', 'https://www.citizennewsputtur.com/2026/10/eastman-eduskill-scholarship-2026-27-apply-october-31.html')],
 'related_titles': ['csir-nehru', 'kindcircle-2026', 'kalpana-2026', 'bookachange-2025'],
})

# 3. Environmental Leaders Fellowship
ARTICLES.append({
 'slug': 'environmental-leaders-fellowship',
 'title': 'Environmental Leaders Fellowship',
 'meta': 'The Environmental Leaders Fellowship at Sadhana Forest: a two-year, full-time fellowship in ecosystem restoration, starting with training in Auroville and continuing in rural centres in India, Haiti, Kenya and Namibia. Applications are accepted year-round.',
 'short': 'Environmental Leaders Fellowship',
 'kicker': 'Fellowship \u00b7 Environment & Community',
 'mono': 'SF',
 'prov_short': 'Sadhana Forest',
 'prov_cat': 'Non-profit \u00b7 India & International',
 'h1': 'Environmental Leaders Fellowship',
 'sub': 'The Environmental Leaders Fellowship is not a cash scholarship for a degree. It is a two-year, full-time commitment to ecosystem restoration with Sadhana Forest: intensive training in Auroville in Tamil Nadu, followed by service in one or more of Sadhana Forest\u2019s rural centres in India, Haiti, Kenya and Namibia, where fellows train local communities in water conservation and indigenous food-forest creation. Food and accommodation are provided, along with a small stipend whose amount is not published. Read the lifestyle conditions before anything else \u2014 they are the fellowship, not a footnote.',
 'dpill': 'Applications year-round',
 'facts': facts([
   ('Provider', 'Sadhana Forest (international non-profit for ecological restoration and sustainable community living)'),
   ('Award', 'Two-year fellowship: intensive training, then service in rural centres; food and accommodation provided, plus a small monthly stipend (amount not published in the official fellowship page). Certificate and personalised recommendation letter on completion; fellows may be invited to continue serving at a centre'),
   ('Level', 'Fellowship \u2014 open to adults aged 18 and over; no prior experience required'),
   ('Deadline', 'Applications accepted year-round (official Sadhana Forest fellowships page); enquiries to fellowships@sadhanaforest.org'),
   ('Eligibility', 'Minimum age 18. Indian residents may apply for any Sadhana Forest fellowship; the Environmental Leaders Fellowship also welcomes international participants. No prior experience required \u2014 dedication, compassion and willingness to learn and serve are the stated requirements'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>Sadhana Forest is a volunteer-run community centred on reforestation, water conservation and sustainable living, with its main centre at Auroville in Tamil Nadu and other centres in India and abroad. Its fellowships are built on Seva \u2014 selfless service \u2014 and on a gift economy in which participation, food and accommodation are offered freely. The Environmental Leaders Fellowship (ELF) is the organisation\u2019s two-year international fellowship, designed for people ready to take on long-term leadership roles in ecosystem restoration rather than a short volunteering visit.</p>
      <p>The fellowship begins with intensive training at Sadhana Forest Auroville. Fellows then serve in one or more of Sadhana Forest\u2019s rural centres in India, Haiti, Kenya and Namibia, training local communities in water conservation and in creating indigenous food forests, with the aim of building long-term food and water security in those communities while deepening the fellow\u2019s own practice of compassionate leadership.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>In-depth, hands-on training in ecosystem regeneration, water conservation, community organisation and sustainable living practices.</li>
        <li>Service experience across more than one rural centre and country, training local communities rather than only working on one site.</li>
        <li>Food and accommodation provided for the fellowship, plus a small monthly stipend to cover expenses. The stipend amount is not published on the official fellowships page, so no figure is stated here.</li>
        <li>A certificate and a personalised recommendation letter on successful completion, and the possibility of being invited to continue serving at one of Sadhana Forest\u2019s centres.</li>
        <li>Training in vegan community living, natural learning and ecological restoration methods as part of daily life, not as a separate course.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are at least 18 years old.</li>
        <li>You are an Indian resident (Indian residents may apply for any Sadhana Forest fellowship) or, for this international fellowship, an international participant.</li>
        <li>No prior experience is required. The stated requirements are dedication, compassion, and a willingness to learn and serve.</li>
        <li>You accept the fellowship\u2019s core principles for the entire duration: a 100% vegan diet and complete abstinence from alcohol, tobacco, drugs and other intoxicating substances. The official page states that any violation results in immediate removal from the programme.</li>
        <li>You can commit full-time and on site for two years. This is a service fellowship, not a part-time or remote opportunity, and it is not a route to a degree on its own.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No document checklist for the Environmental Leaders Fellowship is published on the official fellowships page checked, so none is invented here. The page directs applicants to email fellowships@sadhanaforest.org for details. Write to that address first, explain your background and motivation, and ask for the current application form and requirements before assuming any document list from other Sadhana Forest programmes, which have different timelines.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the Sadhana Forest fellowships page in full, including the core values (vegan and substance-free living, gift economy, Seva), and decide honestly whether a two-year full-time commitment fits your life.</li>
        <li>Email fellowships@sadhanaforest.org for the Environmental Leaders Fellowship application details. Applications are accepted year-round, so there is no single deadline to race, but places and start arrangements still depend on the organisation\u2019s reply.</li>
        <li>Complete whatever application process Sadhana Forest sends you, and clarify the stipend amount, the training schedule, the centre placements, and the start date in writing before travelling.</li>
        <li>Do not confuse this fellowship with Sadhana Forest\u2019s separate one-year fellowship, which has had fixed cohort dates (for example, a March 2026 application deadline for an April 2026 start in older listings). The Environmental Leaders Fellowship is the two-year, year-round programme described here.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a scholarship that pays for my studies?', 'No. It is a full-time service fellowship in ecosystem restoration. You receive training, food, accommodation and a small stipend, not tuition funding for a degree.'),
   ('How much is the stipend?', 'Not published on the official fellowships page checked. Ask Sadhana Forest directly at fellowships@sadhanaforest.org before committing.'),
   ('Do I need experience in ecology or farming?', 'No. No prior experience is required; dedication, compassion and a willingness to learn and serve are the stated requirements.'),
   ('Is there a deadline?', 'No single deadline is published: the official page states that applications are accepted year-round.'),
   ('What happens if I break the vegan or substance-free rules?', 'The official page states that commitment to these core principles is essential and any violation results in immediate removal from the programme.'),
   ('Where would I actually serve?', 'Training starts at Sadhana Forest Auroville, and fellows later serve in one or more rural centres in India, Haiti, Kenya and Namibia.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the official Sadhana Forest fellowships page (sadhanaforest.org/fellowships: two-year international fellowship, Auroville training, rural centres in India, Haiti, Kenya and Namibia, water conservation and indigenous food-forest training, year-round applications, fellowships@sadhanaforest.org, food and accommodation plus a small stipend, certificate and recommendation letter, age 18+, no prior experience, vegan and substance-free commitment with removal for violation, gift economy and Seva values) and corroborating fellowship listings for the same terms. The stipend amount is not published and none is stated.',
 'dl_long': 'Applications accepted year-round \u2014 no single deadline published',
 'offlinks': [('Sadhana Forest \u2014 Fellowships (official)', 'https://sadhanaforest.org/fellowships/'), ('Buddy4Study \u2014 Environmental Leaders Fellowship', 'https://www.buddy4study.com/scholarship/environmental-leaders-fellowship')],
 'related_titles': ['csir-nehru', 'kalpana-2026', 'kindcircle-2026', 'eastman-2026'],
})

# 4. Kalpana Chawla
ARTICLES.append({
 'slug': 'nsp-kalpana-chawla-chatravriti-yojana-himachal-pradesh-2026-27',
 'title': 'NSP Kalpana Chawla Chatravriti Yojana, Himachal Pradesh 2026-27',
 'meta': 'Kalpana Chawla Chatravriti Yojana 2026-27: \u20b915,000 a year for general courses and up to \u20b918,000 a year for professional and technical courses for the top 2,000 meritorious girl students of Himachal Pradesh. Apply on the National Scholarship Portal by 31 October 2026.',
 'short': 'NSP Kalpana Chawla Chatravriti Yojana, Himachal Pradesh 2026-27',
 'kicker': 'Himachal Pradesh \u00b7 Girls\u2019 Merit Scholarship',
 'mono': 'KC',
 'prov_short': 'Govt. of Himachal Pradesh',
 'prov_cat': 'Himachal Pradesh \u00b7 NSP',
 'h1': 'NSP Kalpana Chawla Chatravriti Yojana, Himachal Pradesh 2026-27',
 'sub': 'The Kalpana Chawla Chatravriti Yojana, named after astronaut Kalpana Chawla, is Himachal Pradesh\u2019s merit scholarship for its top girl students: up to 2,000 girls who clear Class 12 from the state board receive \u20b915,000 a year for general courses and up to \u20b918,000 a year for professional and technical courses, renewable through their course. Applications for 2026-27 run on the National Scholarship Portal and close on 31 October 2026 \u2014 the day after this article is written, so apply immediately if you are eligible. One eligibility figure is reported differently across sources and is flagged openly below.',
 'dpill': 'Deadline 31 Oct 2026',
 'facts': facts([
   ('Provider', 'Government of Himachal Pradesh (Directorate of Higher Education), applied for through the National Scholarship Portal (NSP)'),
   ('Award', '\u20b915,000 a year for general academic courses and up to \u20b918,000 a year for professional and technical courses; awarded to the top 2,000 meritorious girl students, renewable every year until the course is completed subject to satisfactory academic performance'),
   ('Level', 'Post-Class 12 \u2014 academic, professional and technical courses after Class 12'),
   ('Deadline', '31 October 2026 (NSP window for 2026-27: 4 June to 31 October 2026, per the Buddy4Study Himachal Pradesh table)'),
   ('Eligibility', 'Girl student domiciled in Himachal Pradesh (bonafide HP student) who passed Class 12 from the Himachal Pradesh Board of School Education in Science, Arts or Commerce and figures on the Board\u2019s merit list, admitted to a post-Class 12 course at a government, government-aided or recognised private institute. Income limit disputed: one 2026 guide states \u20b91 lakh a year, while a college NSP notice lists \u20b92.5 lakh for HP schemes \u2014 confirm on NSP before applying'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The Kalpana Chawla Chatravriti Yojana is a state merit scholarship, not a central scheme: it is run by the Himachal Pradesh government for girls from the state who do well in the Class 12 examination conducted by the Himachal Pradesh Board of School Education. Selection follows the Board\u2019s merit list, issued stream-wise for Science, Arts and Commerce, and the scheme is limited to the top 2,000 meritorious girl students. The point of the scheme is straightforward \u2014 to make sure a strong Class 12 result turns into continued higher education rather than stopping for want of money.</p>
      <p>Applications are made on the National Scholarship Portal, the same portal that carries Himachal Pradesh\u2019s other state schemes for 2026-27, and the 2026-27 window is given as 4 June to 31 October 2026. One Time Registration (OTR) on NSP is required before applying.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>\u20b915,000 a year for students in general academic courses.</li>
        <li>Up to \u20b918,000 a year for students in professional and technical courses.</li>
        <li>Renewal every year until the course is completed, provided academic performance remains satisfactory and a renewal application is filed each year.</li>
        <li>Payment through the National Scholarship Portal system into the student\u2019s bank account; guides stress that the account should be Aadhaar-seeded.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a girl student and a resident (bonafide student) of Himachal Pradesh.</li>
        <li>You passed Class 12 from the Himachal Pradesh Board of School Education, in Science, Arts or Commerce.</li>
        <li>Your name figures on the merit list issued by the Himachal Pradesh Board of School Education. This is the selection mechanism: the scheme goes to the top 2,000 meritorious girls on that list.</li>
        <li>You are admitted as a regular student to a post-Class 12 academic, professional or technical course at a government, government-aided or recognised private institution.</li>
        <li>One guide also reports a minimum of 60% marks in Class 12. The merit-list rule is the scheme\u2019s own mechanism, so treat 60% as a reported figure to confirm, not as a substitute for the merit list.</li>
        <li>Income limit \u2014 read this carefully: a 2026 guide states that annual family income must not exceed \u20b91 lakh, while a college notice listing Himachal Pradesh NSP schemes for 2026-27 states \u20b92.5 lakh as the parents\u2019 income limit in the same set of schemes. The two figures cannot both be the current rule for this scheme. If your family income falls between \u20b91 lakh and \u20b92.5 lakh, confirm the current limit on the NSP scheme page or with the Directorate of Higher Education before relying on eligibility.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The documents listed in a Himachal Pradesh college\u2019s NSP notice for 2026-27 for this scheme are: a print copy of the application form, a recent photograph, a bonafide certificate, an Aadhaar-seeded bank passbook, an Aadhaar card, an identity card, a fee receipt, an attendance certificate from teachers, and the last examination certificate. Keep an income certificate ready as well, given the income question above, and follow the document list shown on the NSP application itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete One Time Registration (OTR) on the National Scholarship Portal at scholarships.gov.in, if you have not already done so.</li>
        <li>Find the Kalpana Chawla Chatravriti Yojana under the Himachal Pradesh state scholarships on NSP and open the 2026-27 application.</li>
        <li>Fill in your domicile, Class 12 and admission details, upload the documents listed above, and submit before 31 October 2026. The portal closes automatically at the deadline, and this article is written the day before it.</li>
        <li>Have your institute verify your enrolment, as NSP applications require institute verification before the state processes payment.</li>
        <li>File a renewal application each year to keep the scholarship running until your course is completed, subject to satisfactory performance.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much does the scheme pay?', '\u20b915,000 a year for general academic courses and up to \u20b918,000 a year for professional and technical courses, for the top 2,000 meritorious girl students.'),
   ('Who selects the recipients?', 'Selection follows the merit list issued by the Himachal Pradesh Board of School Education for Class 12, stream-wise across Science, Arts and Commerce.'),
   ('What is the deadline for 2026-27?', '31 October 2026 on the National Scholarship Portal, with the window given as 4 June to 31 October 2026. Apply immediately: this is the last day.'),
   ('What is the income limit?', 'Disputed between sources: one 2026 guide states \u20b91 lakh a year, while a college NSP notice lists \u20b92.5 lakh. Confirm the current limit on NSP before applying if your income falls between the two figures.'),
   ('Is the scholarship renewed automatically?', 'No. It is renewable every year until the course is completed, subject to satisfactory academic performance, and a separate renewal form must be filed each year.'),
   ('Can boys apply?', 'No. This scheme is for meritorious girl students of Himachal Pradesh only.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the Buddy4Study Himachal Pradesh 2026-27 table (Kalpana Chawla Chatravriti Yojana: 4 June to 31 October 2026, listed among the schemes closing 31 October 2026), a 2026 scheme guide (\u20b915,000 general / up to \u20b918,000 professional-technical, top 2,000 girls, HP Board Class 12, 31 October 2026, OTR, \u20b91 lakh income figure, 60% reported), WeMakeScholars (up to \u20b918,000 a year, 31 October 2026, HP domicile, post-matric/professional admission) and a Himachal Pradesh college NSP notice for 2026-27 (bonafide HP student, Board merit list, \u20b92.5 lakh income figure in the same scheme set, document list). The income-limit discrepancy is carried openly in the article.',
 'dl_long': '31 October 2026 (National Scholarship Portal; window 4 June to 31 October 2026)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('Buddy4Study \u2014 Kalpana Chawla Chatravriti Yojana, Himachal Pradesh', 'https://www.buddy4study.com/scholarship/kalpana-chawla-chatravriti-yojana-himachal-pradesh'), ('Buddy4Study \u2014 HP Scholarships 2026-27 (deadline table)', 'https://www.buddy4study.com/article/hp-scholarship')],
 'related_titles': ['csir-nehru', 'eastman-2026', 'kindcircle-2026', 'elf-sadhana'],
})

# 5. Kind Circle
ARTICLES.append({
 'slug': 'kind-circle-scholarship-for-meritorious-students-2026-27',
 'title': 'Kind Circle Scholarship for Meritorious Students 2026-27',
 'meta': 'Kind Circle Scholarship 2026-27: need-based support from \u20b96,000 for meritorious students from Class 1 to postgraduate level with family income below \u20b96 lakh. Applications close 31 March 2027.',
 'short': 'Kind Circle Scholarship for Meritorious Students 2026-27',
 'kicker': 'India \u00b7 School to Postgraduate',
 'mono': 'KCL',
 'prov_short': 'Kind Circle (Buddy4Study India Foundation initiative)',
 'prov_cat': 'Philanthropy \u00b7 India',
 'h1': 'Kind Circle Scholarship for Meritorious Students 2026-27',
 'sub': 'The Kind Circle Scholarship is one of India\u2019s widest need-based scholarships: it is open to students from Class 1 all the way to postgraduate level, provided they have strong marks and a family income below \u20b96 lakh a year. The amount is not fixed \u2014 it starts at a minimum of \u20b96,000 and the final figure is decided on financial need and interview performance, paid as a one-time award. The deadline for the 2026-27 cycle is 31 March 2027 in the guides for this cycle; do not confuse it with the previous cycle\u2019s 25 March 2026 date, which still appears on older pages.',
 'dpill': 'Deadline 31 Mar 2027',
 'facts': facts([
   ('Provider', 'Kind Circle, a philanthropic initiative managed by Buddy4Study India Foundation'),
   ('Award', 'Minimum \u20b96,000, with higher amounts decided on the student\u2019s financial need, academic background and interview performance; a one-time award paid direct to the scholar\u2019s bank account'),
   ('Level', 'Class 1 to postgraduate level, at recognised schools and colleges in India'),
   ('Deadline', '31 March 2027 (2026-27 cycle guides). Older pages giving 25 March 2026 refer to the previous cycle'),
   ('Eligibility', 'Indian national studying full-time at a recognised Indian school or college from Class 1 to postgraduate level; at least 60% marks in the previous academic year (some listings give 75% \u2014 confirm on the application page); annual family income below \u20b96 lakh; no application fee'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>Kind Circle is Buddy4Study India Foundation\u2019s philanthropic initiative, built on the idea that a bright student should not drop out of education because the family cannot afford to keep them in it. Unlike most scholarships, which cover one stage of education, Kind Circle covers the whole span: a child in Class 1 and a postgraduate student are both within the same programme, judged on the same two tests of merit and need. The programme is need-based first \u2014 the final amount is set after looking at the student\u2019s financial situation, academic background and, where conducted, interview performance \u2014 so two selected students need not receive the same sum.</p>
      <p>That breadth is also why the programme\u2019s pages are easy to confuse across cycles. The 2025-26 cycle closed on 25 March 2026, and pages for that cycle still circulate. This article is about the 2026-27 cycle, for which the guides checked give 31 March 2027.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A minimum scholarship of \u20b96,000, with higher amounts possible depending on assessed financial need and interview performance.</li>
        <li>A one-time award for the academic year applied for; guides state explicitly that it is not automatically renewed for subsequent years of study.</li>
        <li>Payment direct to the selected scholar\u2019s bank account.</li>
        <li>No application fee at any stage.</li>
        <li>Coverage across every level from Class 1 to postgraduate study, in recognised schools and colleges across India.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are an Indian national studying at a recognised school or college in India, from Class 1 up to postgraduate level.</li>
        <li>You are a regular student pursuing full-time education.</li>
        <li>You secured at least 60% marks in your previous academic year, as stated in the 2026-27 guides checked. Note the conflict: some listings for Kind Circle give 75% as the minimum. The 2026-27 guides checked give 60%, but if your marks fall between 60% and 75%, confirm the current threshold on the application page before assuming eligibility.</li>
        <li>Your annual family income is below \u20b96 lakh from all sources.</li>
        <li>There is no age limit mentioned for this scholarship in the guides checked.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The guides checked do not publish a single authoritative document checklist for the 2026-27 cycle, so none is invented here. The Kind Circle application, like other Buddy4Study need-based applications, expects academic marksheets, income proof for the \u20b96 lakh limit, identity proof and bank details for payment; one programme guide also names an income certificate validating family income below \u20b96 lakh. Follow the document list shown on the application page itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Confirm your level, marks and income against the eligibility list above, including the 60% versus 75% marks question if it affects you.</li>
        <li>Apply online through the Buddy4Study portal (the Kind Circle scholarship page, kind-circle-scholarship-for-meritorious-students-2026-27) or the Kind Circle website. Applications sent offline are not accepted.</li>
        <li>Log in with your Buddy4Study account or register as a new user, complete the form, and upload the documents the page asks for.</li>
        <li>Submit before 31 March 2027, and note that the award is one-time: track your application under \u201cApplied Scholarships\u201d in your Buddy4Study account, and do not assume it continues into the next academic year.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Who can apply for Kind Circle?', 'Any Indian student from Class 1 to postgraduate level at a recognised Indian school or college, studying full-time, with at least 60% in the previous academic year (2026-27 guides) and family income below \u20b96 lakh a year.'),
   ('How much will I receive?', 'At least \u20b96,000. The final amount is decided on financial need, academic background and interview performance, so it varies by student.'),
   ('Is it renewed every year?', 'No. Guides state it is a one-time award for the year applied for; it does not automatically continue into subsequent years.'),
   ('What is the deadline for 2026-27?', '31 March 2027 in the 2026-27 guides checked. The 25 March 2026 date on older pages belongs to the previous cycle.'),
   ('Is the minimum marks figure 60% or 75%?', 'The 2026-27 guides checked give 60%, but some listings give 75%. Confirm the current threshold on the application page if your marks fall between the two figures.'),
   ('Is there an application fee?', 'No. The guides checked state there is no application fee for any category.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against 2026-27 guides (Cigmapedia and Career Course Details Hindi: Class 1 to postgraduate, minimum \u20b96,000, need plus interview-based final amount, 60% marks, income below \u20b96 lakh, 31 March 2027, full-time regular students) and prior-cycle pages (Scholarships.net.in, ScholarshipsX, JobsGovind: 2025-26 cycle, 25 March 2026, same \u20b96,000 minimum, 60% and income below \u20b96 lakh; Fueler and The Global Scholarship give 75% marks and a December 2025/25 March date for the older cycle). The 60% versus 75% conflict and the cycle-date distinction are carried openly in the article.',
 'dl_long': '31 March 2027 (2026-27 cycle; 25 March 2026 was the previous cycle)',
 'offlinks': [('Buddy4Study \u2014 Kind Circle Scholarship for Meritorious Students 2026-27', 'https://www.buddy4study.com/scholarship/kind-circle-scholarship-for-meritorious-students-2026-27'), ('Kind Circle (official website)', 'https://www.kindcircle.org/')],
 'related_titles': ['csir-nehru', 'eastman-2026', 'kalpana-2026', 'elf-sadhana'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'uga-2026': {'mono': 'UGA', 'title': 'University of Georgia Undergraduate Scholarships 2026 in USA (Funded)',
   'href': 'university-of-georgia-undergraduate-scholarships-2026-usa.html',
   'dpill': 'Deadline 1 Nov 2026',
   'award': 'The Foundation Fellowship, UGA\u2019s flagship undergraduate award: for international students an annual stipend of $30,000 plus a Presidential waiver worth $21,740 a year, plus funded travel-study, an Oxford Maymester after the first year, and research and conference grants.',
   'elig': 'First-year applicants who have not yet matriculated at another university, including international students and dual-enrolled high school seniors. Transfer applicants and current undergraduates are not eligible. A First-Year Admission application must be submitted first.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'detroit-2026': {'mono': 'UDM', 'title': 'University of Detroit Mercy Scholarships 2026 in USA (Funded)',
   'href': 'university-of-detroit-mercy-scholarships-2026-usa.html',
   'dpill': 'Deadline 15 Nov 2026 (Winter term)',
   'award': 'Merit scholarships for international undergraduates worth up to $10,000 per academic year, renewable, split evenly over the fall and winter terms. Transfer students receive a Detroit Mercy grant of $1,000 to $9,000 a year on college GPA.',
   'elig': 'Full-time international undergraduate students: freshmen on cumulative high school GPA (foreign-high-school students must also meet English-proficiency rules) and transfer students on cumulative college GPA. Awards cannot be combined with another university grant or discount.',
   'tags': [('Undergraduate', 'blue'), ('USA', 'teal')]},
 'cqu-rtp-2026': {'mono': 'CQU', 'title': 'Central Queensland University RTP Scholarship 2026 in Australia (Fully Funded)',
   'href': 'central-queensland-university-rtp-scholarship-2026-australia.html',
   'dpill': 'Deadline 31 Dec 2026',
   'award': 'An Australian Government Research Training Program stipend of AUD $38,000 a year, paid fortnightly, for up to 3 years. Domestic stipend recipients are also offered a full tuition fee offset; for international recipients the fee offset is a separate competitive award, not automatic.',
   'elig': 'Domestic or overseas students enrolled in an accredited Research Higher Degree (Master by Research or PhD) at CQUniversity, whose other income for general living costs does not exceed 75% of the stipend rate. There is no direct application \u2014 a supervisory team must recommend you.',
   'tags': [('Master\u2019s & PhD', 'purple'), ('Australia', 'teal')]},
 'bif-md': {'mono': 'BIF', 'title': 'Boehringer Ingelheim Fonds (BIF) MD Fellowships',
   'href': 'boehringer-ingelheim-fonds-md-fellowships.html',
   'dpill': 'Next deadline 1 Feb 2027',
   'award': 'A monthly stipend for 10 to 12 months, extendable once by up to 6 months: for an unmarried fellow \u20ac1,560 in Germany, \u20ac2,470 in the USA, \u20ac1,890 in the UK and \u20ac2,280 in Switzerland, including a \u20ac100 flat rate for minor project costs, plus spouse, child and childcare allowances where applicable.',
   'elig': 'Excellent medical students studying in Germany who will interrupt their studies to spend at least 10 consecutive months on an experimental, hypothesis-driven project in basic biomedical research at a leading laboratory in another city and institution.',
   'tags': [('Fellowship', 'purple'), ('Germany', 'teal')]},
 'bookachange-2025': {'mono': 'BCA', 'title': 'BookAChange Music Scholarship 2025',
   'href': 'bookachange-music-scholarship-2025.html',
   'dpill': 'Always open',
   'award': 'Tuition-fee support at an accredited Indian music institute: 90% of tuition paid direct to the institute on its payment schedule, and the remaining 10% reimbursed to the student on successful completion of the course. 500 scholarships were pledged at launch.',
   'elig': 'Musically talented applicants from economically disadvantaged backgrounds for a music course at a recognised, accredited institute in India. The income limit is disputed between sources (provider FAQ: below \u20b98,00,000; Buddy4Study listing: \u20b912,00,000) \u2014 confirm the current limit before applying.',
   'tags': [('Music', 'purple'), ('India', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. University of Georgia
ARTICLES.append({
 'slug': 'university-of-georgia-undergraduate-scholarships-2026-usa',
 'title': 'University of Georgia Undergraduate Scholarships 2026 in USA (Funded)',
 'meta': 'The University of Georgia\u2019s flagship Foundation Fellowship for first-year undergraduates, including international students: a $30,000 annual stipend plus a Presidential waiver, funded travel-study and an Oxford Maymester. Applications close 1 November 2026.',
 'short': 'University of Georgia Undergraduate Scholarships 2026 in USA (Funded)',
 'kicker': 'USA \u00b7 Undergraduate',
 'mono': 'UGA',
 'prov_short': 'University of Georgia',
 'prov_cat': 'University \u00b7 USA',
 'h1': 'University of Georgia Undergraduate Scholarships 2026 in USA (Funded)',
 'sub': 'The headline award for a new undergraduate at the University of Georgia is the Foundation Fellowship, run through the Morehead Honors College. It is open to international students, it pays a stipend that approximates the cost of attendance, and its application closes on 1 November 2026 \u2014 but you must start with a First-Year Admission application, because the Fellowship application is only unlocked from it.',
 'dpill': 'Deadline 1 Nov 2026',
 'facts': facts([
   ('Provider', 'University of Georgia (UGA), Athens, Georgia, USA \u2014 through the Morehead Honors College'),
   ('Award', 'Foundation Fellowship: for international students an annual stipend of $30,000 plus a Presidential waiver worth $21,740 a year; in-state $15,750 plus Zell Miller ($10,134 a year); out-of-state $25,930 plus a Presidential waiver ($20,844 a year). Plus funded travel-study, an Oxford Maymester, and research and conference grants'),
   ('Level', 'Undergraduate \u2014 first-year students only'),
   ('Deadline', '1 November 2026 (Foundation Fellowship application)'),
   ('Eligibility', 'Students who have not yet matriculated at another university, including international students and dual-enrolled high school seniors. Transfer applicants and current undergraduate students are not eligible'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The University of Georgia does not run one single undergraduate scholarship with one form. Most of its merit awards are considered automatically when you apply for admission. The exception \u2014 and the award this article is about \u2014 is the Foundation Fellowship, the university\u2019s premier undergraduate academic scholarship. It is the only UGA award that needs its own application, and it is the route to the university\u2019s largest funding package, including its Stamps Scholarships.</p>
      <p>The Fellowship looks first for a very high academic threshold, then for leadership in school and community, artistic, athletic or other special talents, intense intellectual curiosity, and a willingness to share what you learn. Membership is about more than money: Fellows join a small community with dinner seminars, faculty and peer mentoring, and a programme of travel that runs through all four years.</p>
      <h2 id="benefits">Benefits</h2>
      <p>The current official figures, taken from the Morehead Honors College page, are higher than the figures still quoted by many older guides (around $26,080 plus a $19,040 waiver). Use the current figures below, and do not rely on the older ones:</p>
      <ul>
        <li>International students: an annual stipend of $30,000 plus a Presidential waiver worth $21,740 a year.</li>
        <li>Out-of-state students: an annual stipend of $25,930 plus a Presidential waiver worth $20,844 a year.</li>
        <li>In-state students: an annual stipend of $15,750 plus the Zell Miller Scholarship, worth $10,134 a year.</li>
        <li>A post-first-year Maymester study-abroad programme at the University of Oxford, fully funded and valued at $10,000.</li>
        <li>Three fully funded spring travel-study programmes in the first three years, valued together at $15,000. Recent destinations have included Bali, Colombia, Costa Rica, Ecuador, Greece, Japan, Morocco, South Korea, Thailand, Tanzania and Vietnam.</li>
        <li>Individual travel-study grants up to a cumulative total of $10,000, tied to your academic and professional goals, which can be combined with a semester or year abroad.</li>
        <li>Research and academic conference grants.</li>
      </ul>
      <p>The stipend is described by UGA as approximating the cost of attendance, not as covering every possible charge: mandatory fees, housing and food sit outside a simple tuition figure, so read any award letter for exactly what the waiver covers.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are applying as a first-year student and have not yet matriculated at another university.</li>
        <li>International students are eligible, and so are dual-enrolled high school seniors.</li>
        <li>Transfer applicants and current undergraduate students are not eligible.</li>
        <li>You must first submit a First-Year Admission application to the University of Georgia. Only then do you gain access to the Foundation Fellowship application, which is linked to the Morehead Honors College application \u2014 so begin the Honors College application well before 1 November, not on the day.</li>
        <li>Academic standing matters for renewal: guides report a 3.40 cumulative UGA GPA and full-time enrolment as the renewal conditions. Confirm the current renewal rule in your award letter.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The official Fellowship pages checked do not publish a separate document checklist for the Fellowship application itself, so no document list is invented here. In practice, the Fellowship application sits on top of your admission application, so the admission file \u2014 school record, test scores where submitted, and the Honors College application materials \u2014 is the foundation. If the Fellowship application asks for anything further, it will appear in the Morehead Honors College portal once your admission application unlocks it; check there rather than trusting a third-party checklist.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Submit a First-Year Admission application to the University of Georgia. Note that the Early Action deadline of 15 October 2026 has already passed; the Regular Decision deadline is 1 January 2027, but the Fellowship deadline comes first, so do not wait for Regular Decision to start this process.</li>
        <li>Begin the Morehead Honors College application, which unlocks the Foundation Fellowship application.</li>
        <li>Complete and submit the Foundation Fellowship application by 1 November 2026.</li>
        <li>Finalists are notified by late January. Finalists are invited to a mandatory Interview Weekend over the last full weekend in February \u2014 scheduled for Friday 26 and Saturday 27 February 2027.</li>
        <li>If selected, confirm the stipend, waiver and renewal conditions in writing before accepting.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Can international students apply for the Foundation Fellowship?', 'Yes. The official page states explicitly that international students are eligible, as are dual-enrolled high school seniors. Transfer applicants and current undergraduates are not.'),
   ('Is there a separate application, or am I considered automatically?', 'The Fellowship is the exception at UGA: most awards are automatic with admission, but the Fellowship needs its own application, unlocked only after you submit a First-Year Admission application and begin the Morehead Honors College application.'),
   ('How much does an international Fellow actually receive?', 'On the current official figures, an annual stipend of $30,000 plus a Presidential waiver worth $21,740 a year, plus the funded Oxford Maymester, spring travel-study programmes and individual travel-study and research grants. Older guides quoting about $26,080 plus $19,040 are out of date.'),
   ('What happens after 1 November 2026?', 'Finalists are notified by late January and attend a mandatory Interview Weekend on 26\u201327 February 2027. Missing 1 November closes the Fellowship route even if your admission application is still open.'),
   ('Does the Fellowship cover everything?', 'UGA describes the stipend as approximating the cost of attendance. Mandatory fees and living costs are separate items in a student bill, so check your award letter line by line.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the University of Georgia Morehead Honors College official Foundation Fellowship pages (honors.uga.edu: 1 November deadline, international-student eligibility, transfer/current-undergraduate exclusion, first-admission-then-Fellowship route, $30,000 international stipend plus $21,740 Presidential waiver, Oxford Maymester, spring travel-study and individual grants, late-January finalist notification and 26\u201327 February 2027 Interview Weekend) and corroborating guides (GlobalScholarships, ScholarPositions) for the 1 November 2026 date and the automatic-with-admission rule for other UGA awards. Older stipend figures ($26,080/$19,040) in some guides are superseded by the current official figures used here.',
 'dl_long': '1 November 2026 (Foundation Fellowship application \u2014 begin the Morehead Honors College application before this date)',
 'offlinks': [('University of Georgia \u2014 Foundation Fellowship (Morehead Honors College)', 'https://honors.uga.edu/scholarships/prospective-students/foundation-fellowship/'), ('University of Georgia \u2014 Applying for the Foundation Fellowship', 'https://honors.uga.edu/scholarships/prospective-students/foundation-fellowship/applying-for-the-foundation-fellowship/')],
 'related_titles': ['detroit-2026', 'cqu-rtp-2026', 'uwa-2026', 'twente-2027'],
})

# 2. Detroit Mercy
ARTICLES.append({
 'slug': 'university-of-detroit-mercy-scholarships-2026-usa',
 'title': 'University of Detroit Mercy Scholarships 2026 in USA (Funded)',
 'meta': 'University of Detroit Mercy scholarships for international undergraduates: up to $10,000 a year on high-school GPA, renewable and split over the fall and winter terms, with no separate scholarship form. Winter-term date 15 November 2026; Fall scholarship priority 1 December 2026.',
 'short': 'University of Detroit Mercy Scholarships 2026 in USA (Funded)',
 'kicker': 'USA \u00b7 Undergraduate',
 'mono': 'UDM',
 'prov_short': 'University of Detroit Mercy',
 'prov_cat': 'University \u00b7 USA',
 'h1': 'University of Detroit Mercy Scholarships 2026 in USA (Funded)',
 'sub': 'Detroit Mercy does not run a separate scholarship competition for international undergraduates: if you apply for admission and enrol full-time, the Admissions Office awards you on your grades. Freshmen can receive up to $10,000 a year; the nearest dated point in this cycle is the Winter-term date of 15 November 2026, with Fall scholarship priority on 1 December 2026.',
 'dpill': 'Deadline 15 Nov 2026 (Winter term)',
 'facts': facts([
   ('Provider', 'University of Detroit Mercy, Detroit, Michigan, USA (private Catholic university)'),
   ('Award', 'International undergraduate scholarships up to $10,000 per academic year, renewable, split evenly over the fall and winter terms. Transfer students: Detroit Mercy grant of $1,000 to $9,000 a year on college GPA'),
   ('Level', 'Undergraduate (Bachelor\u2019s) \u2014 freshmen and transfer students'),
   ('Deadline', '15 November 2026 (Winter term, per Bright Scholarship and other guides); Fall scholarship priority 1 December 2026 (official admission page)'),
   ('Eligibility', 'Full-time international undergraduate enrolment. Freshmen on cumulative high-school GPA; students from a foreign high school must also meet English-proficiency rules. Transfer students on cumulative college GPA. Awards cannot be combined with another university grant or discount'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The University of Detroit Mercy is a private Catholic university in Detroit, Michigan, sponsored by the Jesuits and the Religious Sisters of Mercy. Its international undergraduate scholarships are institutional merit awards, not a national competition: there is no separate scholarship form to hunt for. You apply for admission, the Admissions Office assesses your grades, and the award comes with your admission decision.</p>
      <p>That simplicity has a catch worth stating plainly. Because the award is tied to admission, the deadlines that matter are admission deadlines, and different sources label them differently. Guides give 15 November 2026 as the last date for the Winter term, while the university\u2019s own admission page gives 1 December as the scholarship-priority date for Fall entry. Both dates are carried in this article, with the nearer one \u2014 15 November \u2014 as the headline deadline, so that a Winter-term applicant is not misled into waiting until December.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Freshmen (including Canadian and other international freshmen): a scholarship worth up to $10,000 per academic year, awarded through the Admissions Office on cumulative high-school grade point average, split evenly over the fall and winter terms.</li>
        <li>Transfer students from an accredited US or Canadian college or university: a Detroit Mercy grant of $1,000 to $9,000 per academic year on cumulative college GPA, also split over the fall and winter terms.</li>
        <li>Both awards are renewable, but they cannot be combined with any other university grant or discount.</li>
        <li>Guides report that university scholarships and grants apply to full-time undergraduate tuition only \u2014 not to housing, food or books, not to the summer term, and not to the Schools of Law or Dentistry. Confirm this in your own award letter.</li>
        <li>Separately, Canadian first-year students may also earn a $1,000 Visit Grant, renewable for up to four years, and MBA applicants with a GMAT score of 600 or better qualify for a half-tuition scholarship \u2014 but those are different awards from the undergraduate scholarship described here.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are an international student applying for a full-time undergraduate programme at Detroit Mercy.</li>
        <li>Freshmen: you enrol full-time, and your award is set by your cumulative high-school GPA. If you come from a foreign high school, you must also pass English proficiency under Detroit Mercy\u2019s guidelines.</li>
        <li>Students from a US high-school affiliation and students from a foreign high school are both covered by the freshman route.</li>
        <li>Transfer students: you enrol full-time from an accredited US or Canadian college or university, and your grant is set by your cumulative college GPA.</li>
        <li>American Language and Culture Program (ALCP) classes do not count toward full-time enrolment for scholarship purposes and carry no discount.</li>
        <li>US citizens, permanent residents and asylees/refugees are dealt with under US federal and state aid instead; this international route is for students who are not US citizens or eligible non-citizens.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No separate scholarship document list is published, because there is no separate scholarship application: the award is decided from your admission file. That file is therefore the document list in practice \u2014 school or college transcripts for the GPA assessment, proof of English proficiency for foreign-high-school applicants, and whatever else the international admission process asks for. Check the official international admission page for the current admission requirements rather than relying on a third-party checklist, and note that the university states online applications carry no application fee.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Apply for undergraduate admission to the University of Detroit Mercy through its international admission route.</li>
        <li>Submit your transcripts so your GPA can be assessed, and, if you come from a foreign high school, your English-proficiency evidence.</li>
        <li>For Winter-term entry, work to the 15 November 2026 date given by guides; for Fall entry, treat 1 December as the scholarship-priority date on the official admission page (with Early Action on 1 November 2026).</li>
        <li>Wait for the admission decision, which carries the scholarship award. Confirm the amount, the fall/winter split, the renewal GPA rule and the no-combining rule in writing.</li>
        <li>If you are a Canadian freshman, ask separately about the $1,000 Visit Grant, which is not part of the main scholarship.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is there a separate scholarship application form?', 'No. The award is made by the Admissions Office from your admission application, on your GPA. There is no separate competition to enter.'),
   ('How much can an international freshman receive?', 'Up to $10,000 per academic year, renewable, split evenly over the fall and winter terms. The exact amount within that ceiling depends on your cumulative high-school GPA.'),
   ('Which deadline should I use \u2014 15 November or 1 December 2026?', 'Both are real, for different entries: 15 November 2026 is the Winter-term date given by guides, and 1 December is the Fall scholarship-priority date on the university\u2019s own admission page. Use the one that matches your intended term, and apply early either way.'),
   ('Can I combine this with another Detroit Mercy grant?', 'No. The official international page states these scholarships and grants cannot be combined with any other university grant or discount.'),
   ('Does the scholarship cover living costs?', 'No. Guides report that university scholarships and grants apply to full-time undergraduate tuition only, not to housing, food or books.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the University of Detroit Mercy official international pages (udmercy.edu: up to $10,000 a year for freshmen on high-school GPA, $1,000\u2013$9,000 transfer grant on college GPA, fall/winter split, renewable, cannot be combined, ALCP exclusion, 1 December scholarship priority) and corroborating guides (Bright Scholarship, Fully Funded Scholarships, Scholarship Union) for the 15 November 2026 Winter-term date and the up-to-$10,000 figure. The two dates are for different entry terms and are both carried in the article.',
 'dl_long': '15 November 2026 (Winter term, per guides) \u00b7 Fall scholarship priority 1 December 2026 (official admission page)',
 'offlinks': [('University of Detroit Mercy \u2014 Financial Aid for International Students', 'https://www.udmercy.edu/admission/financial-aid/type/international.php'), ('University of Detroit Mercy \u2014 International Admission Process', 'https://www.udmercy.edu/admission/international/admission-process.php')],
 'related_titles': ['uga-2026', 'cqu-rtp-2026', 'uwa-2026', 'huddersfield-2026'],
})

# 3. CQUniversity RTP
ARTICLES.append({
 'slug': 'central-queensland-university-rtp-scholarship-2026-australia',
 'title': 'Central Queensland University RTP Scholarship 2026 in Australia (Fully Funded)',
 'meta': 'CQUniversity\u2019s Australian Government RTP Stipend Scholarship: AUD $38,000 a year for up to 3 years for Master by Research and PhD students, closing 31 December 2026. There is no direct application \u2014 a supervisory team must recommend you.',
 'short': 'Central Queensland University RTP Scholarship 2026 in Australia (Fully Funded)',
 'kicker': 'Australia \u00b7 Master\u2019s & PhD research',
 'mono': 'CQU',
 'prov_short': 'Central Queensland University',
 'prov_cat': 'University \u00b7 Australia',
 'h1': 'Central Queensland University RTP Scholarship 2026 in Australia (Fully Funded)',
 'sub': 'CQUniversity\u2019s Research Training Program stipend pays a living allowance of AUD $38,000 a year for up to three years while you do a research degree. The part most applicants get wrong is the application route: there is no direct application form. You must first win a supervisory team\u2019s support, and only then are you invited to apply.',
 'dpill': 'Deadline 31 Dec 2026',
 'facts': facts([
   ('Provider', 'Central Queensland University (CQUniversity), Australia \u2014 funded by the Australian Government under the Research Training Program (RTP)'),
   ('Award', 'Living stipend of AUD $38,000 per annum, paid fortnightly through the university payroll, for up to 3 years. Domestic stipend recipients are also offered an RTP Fees Offset covering tuition; for international recipients the fee offset is a separate competitive award, not automatic'),
   ('Level', 'Research Higher Degree \u2014 Master by Research or PhD (not coursework degrees)'),
   ('Deadline', '31 December 2026 (applications remain open through the year; assessment rounds typically close at the end of April and the end of September)'),
   ('Eligibility', 'Domestic or overseas students enrolled in an accredited Research Higher Degree course at CQUniversity, whose income from another source for general living costs does not exceed 75% of the RTP stipend rate'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The Research Training Program is the Australian Government\u2019s scheme for funding research-degree students, and each university administers its own share. At CQUniversity the RTP Stipend Scholarship is a living allowance: it is meant to cover your day-to-day costs while you research, so that you are not forced to work full-time alongside a thesis. It is not, on its own, a tuition scholarship for international students \u2014 that distinction is the single most important fact in this article, and it is where many aggregator headlines mislead.</p>
      <p>For domestic students, the picture is simpler: a student awarded an RTP Stipend is also offered an RTP Fees Offset, which covers tuition for the scholarship period. For international students, the fee offset goes through its own competitive selection process. An international student can therefore hold the stipend and still owe tuition unless the offset is also awarded. Do not budget on the assumption that the stipend alone makes the degree free.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A living stipend of AUD $38,000 per annum. Some older listings quote AUD $32,000 or AUD $36,000; the current figure repeated across 2026 guides and the university\u2019s own scholarship listing is AUD $38,000, and that is the figure used here.</li>
        <li>Payment fortnightly through the university\u2019s payroll system, for up to 3 years.</li>
        <li>For domestic recipients, an RTP Fees Offset Scholarship covering tuition for the scholarship period.</li>
        <li>For international recipients, a separate competitive chance at the same fee offset \u2014 not automatic with the stipend.</li>
        <li>Research support is described by guides as part of the wider RTP package, but no separate research-fund amount is published in the sources checked, so none is stated here.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a domestic or overseas candidate enrolled in an accredited Research Higher Degree course at CQUniversity \u2014 a Master by Research or a PhD. Coursework master\u2019s degrees do not qualify.</li>
        <li>You must not receive income from another source for your general living costs that is greater than 75% of your RTP stipend rate while you hold the scholarship.</li>
        <li>You must have a supervisory team willing to recommend you. There are no direct applications for RTP scholarships at CQUniversity: prospective applicants are invited by the School of Graduate Research to complete an application, on the recommendation of their supervisory team.</li>
        <li>Assessment rounds are typically scheduled to close at the end of April and the end of September, though the university says the timing and number of rounds cannot be guaranteed and may vary. Applications themselves remain open through the calendar year, closing on 31 December 2026 \u2014 but if you are reading this in late October, the September round has already passed, so your realistic target is the next round, not a fresh September decision.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Because there is no direct application, there is no published RTP document checklist to reproduce. What you will actually need is a research proposal strong enough to win a supervisor, plus the academic record and references that support a Research Higher Degree admission. The university\u2019s Research Training Program and Research Higher Degree Scholarships policy and procedure \u2014 searchable on CQUniversity\u2019s policy page \u2014 is the authoritative source for the current rules; check it before you approach a supervisor, and do not trust an aggregator\u2019s document list.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Develop a genuine, well-formed research question and identify a CQUniversity supervisory team working in that area.</li>
        <li>Discuss your interest in an RHD scholarship with that supervisory team. This is the application in practice: without their recommendation, there is no form to fill in.</li>
        <li>If recommended, you will be invited by the School of Graduate Research to complete an application.</li>
        <li>Confirm, before accepting, whether you also hold a fee offset (automatic for domestic recipients, separately competitive for international recipients) or whether tuition remains payable.</li>
        <li>Keep the 31 December 2026 calendar close in mind, and ask the School of Graduate Research which assessment round your application will actually fall into.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Can I apply directly for the CQUniversity RTP Scholarship?', 'No. The university states there are no direct applications. Discuss your interest with a supervisory team first; the School of Graduate Research invites recommended applicants to apply.'),
   ('Is the scholarship fully funded for international students?', 'Not automatically. The AUD $38,000 stipend covers living costs. Domestic recipients also get a full tuition fee offset automatically, but international recipients win the offset only through a separate competitive process.'),
   ('How much is the stipend, and for how long?', 'AUD $38,000 a year, paid fortnightly, for up to 3 years. Older figures of AUD $32,000 and AUD $36,000 in some listings are superseded.'),
   ('What is the real deadline?', 'Applications remain open through the year and close on 31 December 2026, but assessment rounds typically close at the end of April and the end of September. The September 2026 round has passed, so ask which round you would enter.'),
   ('Can I hold other income while on the stipend?', 'Only up to a limit: other income for general living costs must not exceed 75% of your RTP stipend rate.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against CQUniversity\u2019s own RTP Stipend Scholarship listing as reproduced by YouthExpat and other guides (AUD $38,000 a year, up to 3 years, fortnightly payment, domestic fee offset automatic, international fee offset separately competitive, no direct applications, supervisor recommendation, April/September round pattern, 31 December 2026 close) and corroborating 2026 guides (Scholarships.af, Fellowshipsguide, After School Africa, ScholarPositions). Older stipend figures (AUD $32,000/$36,000) are superseded by the AUD $38,000 figure used here.',
 'dl_long': '31 December 2026 (applications open through the year; assessment rounds typically close end of April and end of September)',
 'offlinks': [('CQUniversity \u2014 School of Graduate Research', 'https://www.cqu.edu.au/research/school-of-graduate-research')],
 'related_titles': ['uga-2026', 'detroit-2026', 'uwa-2026', 'twente-2027'],
})

# 4. BIF MD Fellowships
ARTICLES.append({
 'slug': 'boehringer-ingelheim-fonds-md-fellowships',
 'title': 'Boehringer Ingelheim Fonds (BIF) MD Fellowships',
 'meta': 'Boehringer Ingelheim Fonds MD Fellowships for medical students in Germany: 10 to 12 months of funded basic biomedical research in another city, with a monthly stipend from \u20ac1,560 in Germany. Next deadline 1 February 2027.',
 'short': 'Boehringer Ingelheim Fonds (BIF) MD Fellowships',
 'kicker': 'Germany \u00b7 Fellowship',
 'mono': 'BIF',
 'prov_short': 'Boehringer Ingelheim Fonds',
 'prov_cat': 'Foundation \u00b7 Germany',
 'h1': 'Boehringer Ingelheim Fonds (BIF) MD Fellowships',
 'sub': 'This fellowship pays a medical student in Germany to step away from the home university for ten to twelve months and do a demanding experimental project in basic biomedical research somewhere else \u2014 a different city, a different laboratory, a different supervisor. The next deadline is 1 February 2027, and the portal opens only a month before it.',
 'dpill': 'Next deadline 1 Feb 2027',
 'facts': facts([
   ('Provider', 'Boehringer Ingelheim Fonds (BIF), Mainz, Germany \u2014 an independent, non-profit foundation for basic biomedical research'),
   ('Award', 'Monthly stipend for an unmarried fellow: \u20ac1,560 in Germany, \u20ac2,470 in the USA, \u20ac1,890 in the UK, \u20ac2,280 in Switzerland, including a \u20ac100 flat rate for minor project costs; plus spouse allowance \u20ac200, child allowance \u20ac200 per child, childcare allowance up to \u20ac500 a month where applicable'),
   ('Level', 'Medical students (MD) studying in Germany'),
   ('Deadline', '1 February 2027 (next of three annual deadlines: 1 February, 1 June, 1 October; the 1 October 2026 deadline has passed)'),
   ('Eligibility', 'Excellent medical students studying in Germany, within eight years of obtaining their university entrance qualification, who will change city and institution for at least 10 consecutive months to pursue an experimental, hypothesis-driven project in basic biomedical research'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>The Boehringer Ingelheim Fonds exists for one purpose: the promotion of basic research in biomedicine. Its MD fellowships are the medical-student arm of that mission. They are not a prize for good exam results, and they are not a top-up to a project already funded elsewhere. They fund a single, ambitious, experimentally demanding project that tests a hypothesis \u2014 carried out away from your home institution, in an internationally leading laboratory, for long enough to do real work.</p>
      <p>The move is a condition, not a preference. Fellows must initially change cities and institutions for at least 10 consecutive months, and the fellowship cannot be used to supplement inadequate funding from another institution, to bridge a temporary financial difficulty, or to finish work already sponsored from another source. It is also not held alongside a regular personal income from another research institution: the stipend is meant to cover your living expenses while you research.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>An initial grant of 10 to 12 months, extendable once by up to 6 months.</li>
        <li>A monthly payment made up of a basic stipend, a country-related premium, and a flat rate of \u20ac100 for minor research-related costs such as books and travel. For an unmarried fellow the current totals are \u20ac1,560 in Germany, \u20ac2,470 in the USA, \u20ac1,890 in the United Kingdom and \u20ac2,280 in Switzerland. Older listings quoting \u20ac1,150\u2013\u20ac1,600 are out of date.</li>
        <li>Additional monthly benefits depending on personal circumstances: a spouse allowance of \u20ac200, a child allowance of \u20ac200 per child, and a childcare allowance of up to \u20ac500.</li>
        <li>Funds for travel to scientific meetings and practical courses, on top of the monthly stipend.</li>
        <li>Membership of a worldwide network of BIF fellows and alumni, with seminars and personal support.</li>
        <li>The stipend is paid in euros to your personal bank account by the middle of each month, and you must tell BIF about changes in your personal or financial circumstances so the amount can be adjusted.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are an excellent medical student studying human medicine in Germany.</li>
        <li>You are within eight years of obtaining your university entrance qualification (for example, the Abitur).</li>
        <li>Your project is an experimentally demanding, hypothesis-driven project in basic biomedical research, in an internationally leading laboratory.</li>
        <li>You will change city and institution for at least 10 consecutive months (within a 10\u201312 month fellowship, extendable by up to 6 months).</li>
        <li>You apply before you arrive at the guest laboratory: an application cannot be submitted after arrival there.</li>
        <li>Resubmission is possible only with a new project.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The official how-to-apply page states that the online MD application must be written in English by the applicant personally, and that only complete applications submitted through the SiROP-style online portal (the BIF online application portal) can be considered. The full document list is set out in the official MD fellowship conditions and the application portal itself, which opens one month before each deadline; check the live portal for the current list rather than relying on a third-party checklist, since requirements are updated between cycles.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official MD fellowship conditions and FAQs on bifonds.de in full before drafting anything.</li>
        <li>Agree a project and a host laboratory in a different city from your home institution, with a supervisor willing to host you for at least 10 consecutive months.</li>
        <li>Watch for the portal opening: it opens one month before the next deadline, 1 February 2027. The 1 October 2026 deadline has already passed, so 1 February 2027 is the next date you can actually hit.</li>
        <li>Write the application yourself, in English, and submit it through the online portal by 1 February 2027. Choose your deadline so that the two-month evaluation leaves a decision in your hands before your planned relocation and start date.</li>
        <li>Take up the fellowship within six months of the approval letter by sending your signed fellowship conditions, desired start date and bank details; the fellowship expires if it is not taken up in that window.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Do I have to leave my home university?', 'Yes. Fellows must initially change cities and institutions for at least 10 consecutive months, working in an internationally leading laboratory away from home.'),
   ('How much is the monthly stipend?', 'It depends on where you work. For an unmarried fellow the current totals are \u20ac1,560 in Germany, \u20ac2,470 in the USA, \u20ac1,890 in the UK and \u20ac2,280 in Switzerland, including \u20ac100 for minor project costs, plus spouse, child and childcare allowances where applicable.'),
   ('When are the deadlines?', 'Three times a year: 1 February, 1 June and 1 October. The portal opens one month before each deadline, and evaluation takes two months, so pick the deadline that leaves a decision before your planned start.'),
   ('Can I apply after I have already started at the host laboratory?', 'No. The official rules state the application cannot be submitted after arrival at the guest laboratory.'),
   ('Can I extend the fellowship?', 'Yes, once, by up to 6 months, on top of the initial 10 to 12 months.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the Boehringer Ingelheim Fonds official MD fellowship pages (bifonds.de: three annual deadlines 1 February/1 June/1 October, portal opening one month before, two-month evaluation, cannot apply after arrival at the guest laboratory, 10\u201312 months extendable by up to 6 months, 10-consecutive-month move, current stipend totals \u20ac1,560 Germany / \u20ac2,470 USA / \u20ac1,890 UK / \u20ac2,280 Switzerland including \u20ac100 project flat rate, spouse \u20ac200, child \u20ac200, childcare up to \u20ac500, April 2026 conditions) and the BIF online-applications portal. Older stipend ranges (\u20ac1,150\u2013\u20ac1,600) and single-date claims (31 January 2026) in aggregators are superseded.',
 'dl_long': '1 February 2027 (next of three annual deadlines: 1 February, 1 June, 1 October; portal opens one month before)',
 'offlinks': [('Boehringer Ingelheim Fonds \u2014 How to apply for an MD fellowship', 'https://bifonds.de/de/stipendien-grants/md-stipendien/how-to-apply-md-fellowships.html'), ('Boehringer Ingelheim Fonds \u2014 What we offer (MD fellowships)', 'https://bifonds.de/de/stipendien-grants/md-stipendien/what-we-offer-md-fellowships.html'), ('Boehringer Ingelheim Fonds \u2014 Who can apply (MD fellowships)', 'https://bifonds.de/de/stipendien-grants/md-stipendien/who-can-apply-md-fellowships.html')],
 'related_titles': ['uga-2026', 'detroit-2026', 'humboldt-2026', 'cern-stag-2026'],
})

# 5. BookAChange Music
ARTICLES.append({
 'slug': 'bookachange-music-scholarship-2025',
 'title': 'BookAChange Music Scholarship 2025',
 'meta': 'BookAChange Music Scholarship from the BookMyShow Foundation: 90% of tuition paid direct to an accredited Indian music institute, with the remaining 10% reimbursed on course completion. Applications are open throughout the year.',
 'short': 'BookAChange Music Scholarship 2025',
 'kicker': 'India \u00b7 Music',
 'mono': 'BCA',
 'prov_short': 'BookMyShow Foundation (BookAChange)',
 'prov_cat': 'Foundation \u00b7 India',
 'h1': 'BookAChange Music Scholarship 2025',
 'sub': 'BookAChange, the BookMyShow Foundation\u2019s music initiative, pledged 500 scholarships for talented musicians from underprivileged backgrounds. The deal is simple and unusually generous: the foundation pays 90% of your tuition direct to your institute, and refunds the 10% you paid upfront once you finish the course. Applications stay open all year \u2014 but one eligibility figure differs between sources, and you should check it before applying.',
 'dpill': 'Always open',
 'facts': facts([
   ('Provider', 'BookMyShow Foundation, through BookAChange (successor to BookASmile, launched 2014)'),
   ('Award', '90% of tuition fees paid direct to the institute on its payment schedule, plus reimbursement of the remaining 10% on successful completion of the course. Tuition only \u2014 instruments and equipment are not covered'),
   ('Level', 'Music courses and programmes at recognised, accredited institutes in India (vocal, instrumental, audio production, sound engineering, songwriting, business of music)'),
   ('Deadline', 'Always open \u2014 the scholarship is open throughout the year; no fixed closing date is published'),
   ('Eligibility', 'Musically talented applicants from economically disadvantaged backgrounds. Income limit disputed: the provider FAQ states below \u20b98,00,000 a year; the Buddy4Study listing states \u20b912,00,000 a year \u2014 confirm the current limit before applying'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>BookMyShow, India\u2019s large ticketing platform, runs its social-impact work through the BookMyShow Foundation. In February 2025 the foundation relaunched that work as BookAChange \u2014 the successor to BookASmile, which began in 2014 \u2014 and with it announced a music scholarship programme pledging 500 scholarships. The aim is stated plainly: to help talented people from marginalised backgrounds, including students and street artists, get formal music education they could not otherwise afford.</p>
      <p>The programme covers a wide spread of music study, not just performance: instrumental and vocal training, audio production, sound engineering, songwriting, and the business of music are all named as eligible fields. What matters is that the course is offered by a recognised and accredited institute in India. A course outside India, or at an unaccredited provider, is outside the scheme.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>90% of the tuition fee, paid by BookAChange directly to the academy or university on the institution\u2019s own payment schedule.</li>
        <li>The remaining 10%: you pay it to the institute at the start of the course, and BookAChange reimburses it to you on successful completion of the course. In effect, a student who completes the course has 100% of tuition covered, but the 10% is only refunded at the end, not upfront.</li>
        <li>Support for the full duration of the music programme or course up to one year. If the course runs longer than a year, support can be extended for the remaining duration on the student\u2019s progress, provided a fresh scholarship application is made for the consecutive year of the same course.</li>
        <li>Boarding and lodging are not part of the standard award; additional support for them can be made only as a special request, subject to consideration.</li>
        <li>Musical instruments and other equipment are not covered: the scholarship is limited to course tuition fees.</li>
        <li>There is no application fee.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You demonstrate musical talent and excellence in the field you are seeking a scholarship in.</li>
        <li>You come from an economically disadvantaged background.</li>
        <li>Your course is a music programme at a recognised and accredited institute in India.</li>
        <li>You may apply without a confirmed admission, but if you are selected you must then submit an official admission or acceptance letter from the accredited institute immediately; without it, the foundation will not disburse the scholarship, and failure to provide the documents in time leads to withdrawal or rejection.</li>
        <li>You can apply for only one BookAChange scholarship programme at a time, and you may reapply in a future cycle if an earlier application is rejected.</li>
        <li>Income limit \u2014 read this carefully: the provider\u2019s own FAQ states that total or combined annual family household income must be below \u20b98,00,000, while the Buddy4Study scholarship listing states \u20b912,00,000. The two figures cannot both be the current rule. This article does not pick one silently: if your family income falls between \u20b98 lakh and \u20b912 lakh, confirm the current limit with BookAChange before you rely on eligibility.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The scholarship guidelines require, among other items, a letter from the academy or university on its letterhead, duly stamped and signed by the designated authority, stating the course fee structure and payment details with the corresponding payment timelines. That letter is also what the final award depends on: the scholarship is only confirmed once the institute\u2019s documents are submitted. Keep ready the usual identity, income and admission evidence as well, and check the current guidelines document on bookachange.org for the full checklist before submitting, since the guidelines are the governing document and the foundation reserves the right to modify or cancel the programme, criteria or selection process at any time.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the BookAChange Music Scholarship Guidelines and FAQs on bookachange.org, and settle the income-limit question above if it affects you.</li>
        <li>Apply online through the official BookAChange website. You do not need a confirmed admission to apply.</li>
        <li>If selected, you will be notified by email. Confirm your acceptance within 15 days of receiving the scholarship confirmation email \u2014 failure to respond in that window means the scholarship lapses.</li>
        <li>Submit the institute\u2019s stamped and signed fee-structure letter and your admission or acceptance letter promptly, and sign the BookAChange Music Scholarship Memorandum of Understanding (MOU).</li>
        <li>After the MOU is signed, BookAChange releases payment directly to the academy or university. You pay your 10% share at the start of the course and claim it back on successful completion.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is the scholarship really 100% of tuition?', 'In effect, for a student who completes the course: 90% is paid direct to the institute during the course, and the 10% you paid upfront is reimbursed on successful completion. If you do not complete the course, the 10% reimbursement does not apply.'),
   ('Is there a deadline?', 'No fixed deadline is published. Both the Buddy4Study listing and the programme guides state the scholarship is open throughout the year, and the Buddy4Study page lists the deadline date as \u201cAlways Open\u201d.'),
   ('What is the family income limit?', 'This is disputed between sources: the provider FAQ says below \u20b98,00,000 a year, while the Buddy4Study listing says \u20b912,00,000 a year. Confirm the current limit with BookAChange before applying if your income falls between the two figures.'),
   ('Does it cover instruments, boarding or living costs?', 'No, as standard. It covers tuition fees only. Instruments and equipment are excluded, and boarding or lodging support requires a special request subject to consideration.'),
   ('Can I apply before I have an admission letter?', 'Yes. You may apply without a confirmed admission, but a selected candidate must then submit an official admission or acceptance letter from an accredited Indian institute immediately, or the award is withdrawn.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the BookAChange official FAQ (bookachange.org: tuition-only coverage, accredited Indian institutes, full-duration support up to 1 year with fresh application for longer courses, no fee, 15-day acceptance window, one programme at a time, income below \u20b98,00,000 in the FAQ) and the Buddy4Study scholarship listing (90% plus 10% reimbursement, \u201cAlways Open\u201d deadline, \u20b912,00,000 income figure) and launch coverage (DT Next, Mid-Day, February 2025: 500 scholarships pledged, BookASmile successor). The \u20b98 lakh / \u20b912 lakh income discrepancy is carried openly in the article rather than resolved by guesswork.',
 'dl_long': 'Always open \u2014 no fixed deadline published (open throughout the year)',
 'offlinks': [('BookAChange \u2014 FAQs (official)', 'https://www.bookachange.org/faqs/'), ('Buddy4Study \u2014 BookAChange Music Scholarship 2025', 'https://www.buddy4study.com/scholarship/bookachange-music-scholarship')],
 'related_titles': ['uga-2026', 'detroit-2026', 'cqu-rtp-2026', 'bif-md'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'sadhana-fellowship': {'mono': 'SF', 'title': 'Sadhana Forest Fellowship',
   'href': 'sadhana-forest-fellowship.html',
   'dpill': 'Applications open (no fixed deadline published)',
   'award': 'One-year residential fellowship at Sadhana Forest Auroville: free food and accommodation plus a small monthly stipend (amount not published).',
   'elig': 'Indian residents aged 18 or above; no prior experience required; full-time vegan, substance-free community life for the year.',
   'tags': [('Fellowship', 'purple'), ('Tamil Nadu', 'green')]},
 'sadhana-scholarship': {'mono': 'SF', 'title': 'Sadhana Forest Scholarship',
   'href': 'sadhana-forest-scholarship.html',
   'dpill': 'Applications open year-round',
   'award': 'Five-year programme: four years of full-time residential service, sustainable living and self-directed learning, then a one-year mentored incubation period.',
   'elig': 'Indian residents aged 18 or above; no prior experience required; commitment to a 100% vegan, substance-free life for the whole five years.',
   'tags': [('Scholarship', 'blue'), ('Tamil Nadu', 'green')]},
 'pmss-capf-2026': {'mono': 'PM', 'title': 'PM Scholarship for CAPF and Assam Rifles 2026-27',
   'href': 'pm-scholarship-capf-assam-rifles-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 2,500 a month for boys and Rs 3,000 a month for girls, paid annually, for a first professional degree; 2,000 fresh scholarships a year.',
   'elig': 'Wards or widows of CAPF/Assam Rifles personnel, 60% in Class 12, enrolled in a full-time first professional degree; no income ceiling.',
   'tags': [('Defence families', 'purple'), ('Central Govt', 'teal')]},
 'icar-pgs-2026': {'mono': 'IC', 'title': 'ICAR Post Graduate Scholarship (PGS) 2026',
   'href': 'icar-post-graduate-scholarship-pgs-2026.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 12,640 a month plus Rs 6,000 a year contingency for a master\u2019s degree in agriculture and allied sciences; 600 fellowships a year.',
   'elig': 'Master\u2019s admission through the ICAR All India Entrance Examination on an AIQ seat at an ICAR-AU institution; 60% or OGPA 6.60 (55% / 5.50 for SC/ST/PC).',
   'tags': [('Agriculture', 'green'), ('ICAR / NSP', 'teal')]},
 'beedi-postmatric-2026': {'mono': 'LW', 'title': 'Post-Matric Education Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27',
   'href': 'post-matric-beedi-cine-iomc-lsdm-workers-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 3,000 a year for Classes 11\u201312, Rs 6,000 for ITI, diploma and undergraduate courses, and up to Rs 25,000 for professional courses.',
   'elig': 'Wards of beedi, cine, iron/manganese/chrome ore or limestone/dolomite mine workers; Class 10 passed at the first attempt; regular post-matric course; income limits apply.',
   'tags': [('Labour welfare', 'blue'), ('Central Govt', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. Sadhana Forest Fellowship
ARTICLES.append({
 'slug': 'sadhana-forest-fellowship',
 'title': 'Sadhana Forest Fellowship',
 'meta': 'Sadhana Forest Fellowship: a one-year residential fellowship at Sadhana Forest Auroville, Tamil Nadu, offering food, accommodation and a small monthly stipend for full-time service in reforestation, water conservation and community life. Open to Indian residents aged 18 and above; no prior experience required.',
 'short': 'Sadhana Forest Fellowship',
 'kicker': 'Fellowship · Tamil Nadu',
 'mono': 'SF',
 'prov_short': 'Sadhana Forest',
 'prov_cat': 'Community Fellowship · Tamil Nadu',
 'h1': 'Sadhana Forest Fellowship',
 'sub': 'This is not a cash scholarship for college fees. It is a year of full-time service inside a working ecological community: fellows live at Sadhana Forest in Auroville, Tamil Nadu, plant and tend trees, build and repair water-harvesting structures, cook, clean and welcome the volunteers and visitors who pass through, and are fed, housed and given a small monthly stipend while they do it. The organisation describes the whole experience as Seva, selfless service, and it asks for the full year, not a short visit.',
 'dpill': 'Applications open (no fixed deadline published)',
 'facts': facts([
   ('Provider', 'Sadhana Forest, Auroville, Tamil Nadu'),
   ('Duration', 'One year, residential and full-time'),
   ('Benefit', 'Free food and accommodation, plus a small monthly stipend — the stipend amount is not published in the sources checked'),
   ('Eligibility', 'Indian residents aged 18 or above; no prior experience required'),
   ('What fellows do', 'Reforestation, water conservation, Gaushala work, community upkeep, welcoming visitors and volunteers'),
   ('Deadline', 'No fixed deadline published — the listing shows \u201cAlways Open\u201d and the organisation lists the fellowship among its current opportunities'),
 ]),
 'body': '''<h2 id="about">About the fellowship</h2>
      <p>Sadhana Forest is an international volunteer community in Auroville, Tamil Nadu, built around ecological restoration, veganism and compassionate living. Its fellowships offer a chance to live and learn inside that community rather than to visit it, and the one-year Sadhana Forest Fellowship is the shortest of its residential tracks. Fellows take part in every part of community life: planting and caring for trees, maintaining water-harvesting structures such as bunds, swales and trenches, helping in the Children\u2019s Land and the Tea Hut, cooking and cleaning, and welcoming visitors and volunteers. Training covers vegan community living, natural learning and ecological restoration methods.</p>
      <p>Readers should not confuse this fellowship with the two longer tracks on the same official page. The Environmental Leaders Fellowship runs for two years and sends fellows on to rural centres in India, Haiti, Kenya and Namibia, and the Sadhana Forest Scholarship runs for five years. The fellowship described here is one year, at Auroville, and it is the one this article covers.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be a citizen or resident of India.</li>
        <li>Be 18 years of age or above.</li>
        <li>No prior experience is required. The organisation asks for dedication, compassion and a willingness to learn and serve, not for forestry qualifications.</li>
        <li>Be ready for the community\u2019s shared principles for the whole year: a 100% vegan diet, complete abstinence from alcohol, tobacco, drugs and other intoxicating substances, and life in a gift economy where participation, food and accommodation are offered freely.</li>
      </ul>
      <p>The fellowship is a residential commitment. Fellows are expected to take part in all aspects of community life, including physical work, cooking, cleaning and hosting visitors, and to follow the community\u2019s vegan lifestyle and sustainable living practices. Anyone looking for a part-time placement, or for a placement that can be combined with other work or study, will not fit this programme.</p>
      <h2 id="benefits">Benefits</h2>
      <p>Selected fellows receive free food and accommodation for the duration of the one-year residential fellowship, along with a small monthly stipend. The stipend amount is not published on the organisation\u2019s fellowship page or in the programme listing, so this article states no figure for it; treat any number quoted elsewhere as unverified unless the organisation itself confirms it. On completion, fellows receive a certificate and a personalised recommendation letter, and may be invited to continue serving at one of Sadhana Forest\u2019s centres.</p>
      <p>One caution on dates. An older cohort listing for this fellowship gave an application deadline of 15 March 2026 for a fellowship running from 19 April 2026 to 18 April 2027. That cohort has started, and the organisation\u2019s current page lists the fellowship among its current opportunities without stating a fixed deadline, while the programme listing shows it as always open. This article therefore reports no fixed deadline, but anyone planning to travel should confirm the next cohort\u2019s start date with the organisation before making arrangements.</p>
      <h2 id="documents">Documents needed</h2>
      <p>The programme listing asks for the following, all in PDF form:</p>
      <ul>
        <li>Curriculum Vitae</li>
        <li>Aadhaar Card</li>
        <li>PAN Card</li>
        <li>BPL (Below Poverty Line) ration card, your own or your parents\u2019, if applicable</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Read the fellowship descriptions on the organisation\u2019s fellowships page and confirm that the one-year, full-time, residential commitment suits you.</li>
        <li>Apply through the programme listing\u2019s online route: register or log in, navigate to the fellowship, and submit the application with the documents above.</li>
        <li>For details about the current intake, write to the organisation at the contact given on its fellowships page, fellowships@sadhanaforest.org, rather than relying on an older cohort\u2019s dates.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a scholarship for college fees?', 'No. It is a service fellowship: a year of residential work in an ecological community, with food, accommodation and a small stipend, not a payment towards tuition.'),
   ('Do I need experience in forestry or conservation?', 'No. No prior experience is required; the organisation asks for dedication, compassion and a willingness to learn and serve.'),
   ('Can applicants from outside India apply?', 'The organisation\u2019s page says Indian residents may apply for any fellowship, and that the two-year Environmental Leaders Fellowship also welcomes international participants. This one-year fellowship is presented for Indian residents.'),
   ('How much is the stipend?', 'Not published in the sources checked. The organisation and the listing both describe it only as a small monthly stipend, so no figure is stated here.'),
   ('What happens at the end of the year?', 'Fellows receive a certificate and a personalised recommendation letter, and may be invited to continue serving at one of Sadhana Forest\u2019s centres.'),
   ('Is there a deadline?', 'No fixed deadline is published on the organisation\u2019s current page, and the programme listing shows the fellowship as always open. Confirm the next cohort\u2019s start date with the organisation before travelling.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Sadhana Forest fellowships page (one-year residential fellowship at Auroville; food and accommodation plus a small stipend; minimum age 18; Indian residents may apply for any fellowship; no prior experience required; shared principles of 100% vegan and substance-free life, gift economy and Seva; certificate and recommendation letter on completion; contact fellowships@sadhanaforest.org) and the Buddy4Study Sadhana Forest Fellowship listing (always open; Indian citizen or resident, 18 or above; food, accommodation and a small stipend; CV, Aadhaar, PAN and BPL ration card if applicable, in PDF). The older 15 March 2026 cohort deadline and 19 April 2026 start come from an older cohort listing and are reported here only as superseded; the stipend amount is not published in either source checked, so none is stated.',
 'dl_long': 'No fixed deadline published — the listing shows \u201cAlways Open\u201d and the organisation lists the fellowship among its current opportunities',
 'offlinks': [('Sadhana Forest — Fellowships (official)', 'https://sadhanaforest.org/fellowships/'), ('Buddy4Study — Sadhana Forest Fellowship', 'https://www.buddy4study.com/scholarship/sadhana-forest-fellowship')],
 'related_titles': ['elf-sadhana', 'sadhana-scholarship', 'icar-jrf', 'nsp-pg-2026'],
})

# 2. Sadhana Forest Scholarship
ARTICLES.append({
 'slug': 'sadhana-forest-scholarship',
 'title': 'Sadhana Forest Scholarship',
 'meta': 'Sadhana Forest Scholarship: a five-year programme at Sadhana Forest — four years of full-time residential service, sustainable living and self-directed learning, followed by a one-year mentored incubation period. Open year-round to Indian residents aged 18 and above who commit to a vegan, substance-free community life.',
 'short': 'Sadhana Forest Scholarship',
 'kicker': 'Scholarship · Tamil Nadu',
 'mono': 'SF',
 'prov_short': 'Sadhana Forest',
 'prov_cat': 'Community Scholarship · Tamil Nadu',
 'h1': 'Sadhana Forest Scholarship',
 'sub': 'Five years is a long time to give to anything, and this programme asks for all of it. Participants spend four years living full-time in Sadhana Forest\u2019s off-grid, solar-powered, low-waste campuses, serving the community, learning by doing, and studying alongside their service, and then spend a fifth year in a mentored incubation period designing and carrying out their own ecological or social impact project. It is a scholarship in the sense that living costs are carried by the community, not in the sense of a cheque towards college fees.',
 'dpill': 'Applications open year-round',
 'facts': facts([
   ('Provider', 'Sadhana Forest, Auroville, Tamil Nadu, with field centres and international sites'),
   ('Duration', 'Five years: four years full-time residential participation, then a one-year mentored incubation period'),
   ('Benefit', 'Residential living in a sustainable community, vegan meals and accommodation, mentorship, and study time alongside service — described in the listing as \u201cvariable benefits\u201d, with no cash amount published'),
   ('Eligibility', 'Indian residents aged 18 or above; no prior experience required; full commitment to a 100% vegan, substance-free life for the whole five years'),
   ('Learning', 'Immersive service, sustainable living and self-directed education, including the option of distance or online study with mentorship'),
   ('Deadline', 'Applications open year-round, according to the organisation\u2019s fellowships page'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>The Sadhana Forest Scholarship is a five-year programme, and its length is the first thing to understand about it. The first four years are full-time and residential: participants live in off-grid, solar-powered, low-waste campuses and follow a lifestyle based on compassion, sustainability and service, or Seva. During those years they contribute full-time to reforestation, water conservation, biodiversity restoration and community living, at Sadhana Forest Auroville in Tamil Nadu, at field centres in Meghalaya and Tamil Nadu, and potentially at international sites in Haiti, Kenya and Namibia. The fifth year is a mentored incubation period, in which participants design and implement their own ecological or social impact project with guidance from the Sadhana Forest team.</p>
      <p>Learning is woven into the service rather than separated from it. Participants may combine formal and informal learning — skill-based learning in ecology, natural building, facilitation, communication, project management and creative arts, distance or online Bachelor\u2019s, Master\u2019s or PhD programmes, diploma or certificate courses, and self-directed, experiential learning through daily Seva — with mentorship and allocated study time. Programme listings report 30 study leave days each year. The scholarship is therefore best read as five years of supported living and learning inside a community, not as funding for a conventional degree taken elsewhere.</p>
      <p>Do not confuse this scholarship with the one-year Sadhana Forest Fellowship on the same official page, or with the two-year Environmental Leaders Fellowship. All three share the same community, the same Seva ethos and the same vegan, substance-free rules, but they differ in length and purpose: one year of service, two years of leadership training, or five years ending in an incubated project of your own.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be a citizen or resident of India.</li>
        <li>Be 18 years of age or above.</li>
        <li>No prior experience is required. What matters is commitment to long-term service and community living, and to learning.</li>
        <li>Commit to the programme\u2019s core principles for the entire five years: a 100% vegan diet and complete abstinence from alcohol, tobacco, drugs and other intoxicating substances. The organisation states plainly that any violation will result in immediate removal from the programme.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <p>Participants live in a sustainable, off-grid, vegan community, with vegan meals and accommodation on site, mentorship and guidance from Sadhana Forest team members, support for dissertation, research or independent project work, and the chance to study while they serve. The listing describes the award as \u201cvariable benefits\u201d and publishes no cash amount, so this article states none: the value of the programme is the five years of supported residence, learning and mentorship, not a fixed grant. International exposure, leadership and management experience, and cross-cultural collaboration with volunteers from around the world are listed among the programme\u2019s wider benefits.</p>
      <p>One conflict in the sources is worth stating openly. A programme listing reported a capped intake window, with applications opening on 15 November 2025 and closing at 200 applications or on 15 December 2025, whichever came first. The organisation\u2019s own current fellowships page, by contrast, says applications are open year-round and directs enquirers to email for details. This article follows the organisation\u2019s page, since it is the more recent and more authoritative source, but anyone applying should confirm the current intake position by email before committing to the move.</p>
      <h2 id="documents">Documents needed</h2>
      <p>The programme listing asks for the following, all in PDF form:</p>
      <ul>
        <li>Curriculum Vitae</li>
        <li>Aadhaar Card</li>
        <li>PAN Card</li>
        <li>BPL (Below Poverty Line) ration card, your own or your parents\u2019, if applicable</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Read the scholarship description on the organisation\u2019s fellowships page and weigh the five-year, full-time, residential commitment, including the vegan and substance-free rules, before applying.</li>
        <li>Apply through the programme listing\u2019s online route: register or log in, navigate to the scholarship, and submit the application with the documents above.</li>
        <li>For details about the current intake, email fellowships@sadhanaforest.org, as the organisation\u2019s page directs.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How is this different from the Sadhana Forest Fellowship?', 'Length and purpose. The fellowship is one year of residential service. The scholarship is five years: four years of residential service and learning, then a one-year mentored incubation period for your own project.'),
   ('Is there a cash award?', 'No cash amount is published. The listing describes the award as variable benefits: residential living, meals, accommodation, mentorship and study support for five years.'),
   ('Can I study for a degree during the programme?', 'Yes, in the programme\u2019s own design: participants may pursue distance or online Bachelor\u2019s, Master\u2019s or PhD programmes, or diploma and certificate courses, alongside their service, with mentorship and allocated study time.'),
   ('What happens if I break the vegan or substance-free rules?', 'The organisation states that commitment to these principles is essential for the entire programme and that any violation will result in immediate removal.'),
   ('When can I apply?', 'According to the organisation\u2019s current page, applications are open year-round. One older listing reported a capped November\u2013December 2025 window; confirm the current position by email before applying.'),
   ('Do I need prior experience?', 'No. No prior experience is required, only dedication, compassion and a willingness to learn and serve.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Sadhana Forest fellowships page (five-year programme: four years full-time residential participation plus a one-year mentored incubation period; off-grid, solar-powered, low-waste campuses; 100% vegan diet and complete abstinence from intoxicants for the whole programme, with removal for violation; applications open year-round; contact fellowships@sadhanaforest.org; minimum age 18; Indian residents may apply) and the Buddy4Study Sadhana Forest Scholarship listing (always open; Indian citizen or resident, 18 or above; five-year structure; CV, Aadhaar, PAN and BPL ration card if applicable, in PDF). The capped 15 November\u201315 December 2025 / 200-application window comes from a programme listing and conflicts with the organisation\u2019s year-round statement; the article follows the organisation\u2019s page and flags the conflict. No cash amount is published in either source, so none is stated.',
 'dl_long': 'Applications open year-round — the organisation\u2019s fellowships page states no fixed deadline',
 'offlinks': [('Sadhana Forest — Fellowships (official)', 'https://sadhanaforest.org/fellowships/'), ('Buddy4Study — Sadhana Forest Scholarship', 'https://www.buddy4study.com/scholarship/sadhana-forest-scholarship')],
 'related_titles': ['elf-sadhana', 'sadhana-fellowship', 'icar-nts', 'nsp-pg-2026'],
})

# 3. PM Scholarship for CAPF and Assam Rifles 2026-27
ARTICLES.append({
 'slug': 'pm-scholarship-capf-assam-rifles-2026-27',
 'title': 'PM Scholarship for CAPF and Assam Rifles 2026-27',
 'meta': 'PM Scholarship for CAPF and Assam Rifles 2026-27: 2,000 fresh scholarships a year for wards and widows of Central Armed Police Forces and Assam Rifles personnel — Rs 2,500 a month for boys and Rs 3,000 a month for girls for a first professional degree. Apply on the National Scholarship Portal by 31 Oct 2026.',
 'short': 'PM Scholarship for CAPF and Assam Rifles 2026-27',
 'kicker': 'Central Government · Defence Families',
 'mono': 'PM',
 'prov_short': 'Ministry of Home Affairs (WARB)',
 'prov_cat': 'Central Government · Defence Families',
 'h1': 'PM Scholarship for CAPF and Assam Rifles 2026-27',
 'sub': 'This is the Central Armed Police Forces and Assam Rifles track of the Prime Minister\u2019s Scholarship Scheme, run by the Welfare and Rehabilitation Board in the Ministry of Home Affairs. It pays the dependent children and widows of CAPF and Assam Rifles personnel through a first professional degree — engineering, medicine, law, nursing, management and similar courses — with 2,000 fresh scholarships a year split equally between boys and girls. It is written on its closing day: the National Scholarship Portal window for 2026-27 ends on 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Welfare and Rehabilitation Board (WARB), Ministry of Home Affairs, through the National Scholarship Portal'),
   ('Scholarships', '2,000 fresh scholarships a year — 1,000 for boys and 1,000 for girls — plus renewals'),
   ('Benefit', 'Rs 2,500 a month for boys (Rs 30,000 a year) and Rs 3,000 a month for girls (Rs 36,000 a year), paid annually by Direct Benefit Transfer'),
   ('Eligibility', 'Ward or widow of CAPF/Assam Rifles personnel; 60% marks in Class 12; first professional degree at a recognised institution; no income ceiling'),
   ('Forces covered', 'BSF, CRPF, ITBP, CISF, SSB, NSG and Assam Rifles'),
   ('Deadline', 'Closes today, 31 Oct 2026 — institute verification by 15 Nov 2026, ministry verification by 30 Nov 2026'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>Introduced in 2006-07 under the Ministry of Home Affairs, the Prime Minister\u2019s Scholarship Scheme for wards and widows of Central Armed Police Forces and Assam Rifles personnel supports higher technical and professional education for the families of the forces that guard India\u2019s borders, fight insurgency and protect its vital installations. The forces covered are the Border Security Force, Central Reserve Police Force, Indo-Tibetan Border Police, Central Industrial Security Force, Sashastra Seema Bal, National Security Guard and Assam Rifles. The scheme is administered by the Welfare and Rehabilitation Board, and applications are made on the National Scholarship Portal.</p>
      <p>Keep this track separate from the scheme\u2019s sibling tracks, which carry their own counts and are already covered elsewhere on this site. Combined guides often quote 5,500 fresh scholarships for ex-servicemen\u2019s wards, 500 for State and UT police wards and 150 for RPF and RPSF wards; those are different tracks with different administrators. The CAPF and Assam Rifles track described here offers 2,000 fresh scholarships a year of its own, divided equally between boys and girls.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be the ward — dependent child, including an adopted or step-child — or widow of CAPF or Assam Rifles personnel in one of these categories: personnel killed in action or during service; personnel disabled due to action or service-related causes; retired or serving personnel below officer rank; or ex-personnel holding a Gallantry Award.</li>
        <li>Have scored at least 60% marks in Class 12 or an equivalent examination for a fresh application. Renewals require at least 50% in the previous academic year.</li>
        <li>Be enrolled in a full-time first professional degree course — engineering, medicine, nursing, law, management, architecture, veterinary science, agriculture and allied sciences, and similar courses — at a recognised, accredited institution (UGC, AICTE, Medical Council or equivalent).</li>
        <li>There is no income ceiling, and married daughters are eligible. Applicants already receiving another central or state scholarship for the same purpose are not eligible.</li>
      </ul>
      <p>Selection follows a priority order that favours those most affected by service: first, wards and widows of personnel killed in action; then wards of ex-personnel with Gallantry Awards; then wards and widows of personnel who died in harness; then wards of personnel disabled in action; then wards and widows of personnel whose death was attributable to service; then wards of retired personnel; and finally wards of serving personnel below officer rank. Within the merit list, ties are resolved in favour of female students.</p>
      <p>Not eligible: wards of civilian employees of the CAPFs, Assam Rifles or State and UT police; students in correspondence or distance-learning professional courses; students already holding another scholarship, stipend or financial assistance for the same purpose; students who have already availed themselves of this scholarship; diploma courses that do not lead to a degree; master\u2019s programmes, except MBA and MCA where that is the first professional course; students at institutions not approved under the UGC Act, not recognised by AICTE, or lacking the required accreditation for their course; students studying abroad; and students who change course or college after selection and take fresh admission in a later year, which leads to permanent cancellation.</p>
      <h2 id="benefits">Benefits</h2>
      <p>Boys receive Rs 2,500 a month, or Rs 30,000 a year, and girls receive Rs 3,000 a month, or Rs 36,000 a year, for up to five years depending on the course, paid once a year by Direct Benefit Transfer to the student\u2019s bank account after verification of attendance and academic performance. For integrated programmes such as B.Tech plus M.Tech, coverage extends to the initial years of the programme. The amount is a fixed monthly rate, not a reimbursement of fees: it does not vary with the institution\u2019s fee structure.</p>
      <h2 id="documents">Documents needed</h2>
      <p>The scheme listing asks for self-attested documents in PDF or JPG format, each up to 200 KB:</p>
      <ul>
        <li>Aadhaar Card or other ID proof</li>
        <li>Class 10 and Class 12 marksheets and certificates</li>
        <li>Bonafide certificate from the institution</li>
        <li>Family relation proof — death certificate, disability certificate, Pension Payment Order, or Gallantry Award certificate, as applicable</li>
        <li>Fee receipt or admission letter</li>
        <li>Bank account details</li>
        <li>Passport-size photograph</li>
        <li>Marriage certificate and dependency proof, for widows</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Confirm first that your institution is registered on the National Scholarship Portal; an unregistered institution\u2019s students cannot apply.</li>
        <li>Complete One-Time Registration on the portal, with mobile OTP, captcha and eKYC, and note your application ID and password.</li>
        <li>Log in, choose Apply Fresh, fill in the general, academic and scheme-specific sections, upload the documents above, and submit. Review everything before final submission, because submitted applications cannot be edited; a submitted application can, however, be withdrawn and resubmitted while it is still active.</li>
        <li>Submit on or before 31 October 2026. Institute verification and defective-application verification run to 15 November 2026, and district, state and ministry verification to 30 November 2026.</li>
      </ol>
      <p>For assistance, the scheme listing gives the Welfare and Rehabilitation Board telephone number (011)-23063111.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is there an income limit?', 'No. The scheme listing states there is no income ceiling for this track.'),
   ('What marks do I need?', 'At least 60% in Class 12 or equivalent for a fresh application, and at least 50% in the previous academic year for a renewal.'),
   ('Can a married daughter apply?', 'Yes. The scheme listing states that married daughters are eligible.'),
   ('Does it cover diploma or distance courses?', 'No. Diploma courses that do not lead to a degree, and professional courses taken by correspondence or distance learning, are excluded.'),
   ('How is the money paid?', 'Annually, by Direct Benefit Transfer to the student\u2019s bank account, after verification of attendance and academic performance — Rs 30,000 a year for boys and Rs 36,000 a year for girls.'),
   ('When does the 2026-27 window close?', 'Today, 31 October 2026, for student applications on the National Scholarship Portal. Institute verification follows by 15 November 2026.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study PMSS CAPF and Assam Rifles 2026 guide (window 1 June to 31 October 2026; institute and defective verification 15 November 2026; DNO/SNO/MNO verification 30 November 2026; 2,000 scholarships, 1,000 boys and 1,000 girls; Rs 2,500 boys and Rs 3,000 girls a month; forces BSF, CRPF, ITBP, CISF, SSB, NSG and Assam Rifles; 60% Class 12 fresh and 50% renewal; first professional degree; no income ceiling; married daughters eligible; priority order; exclusions; documents and NSP steps; WARB telephone (011)-23063111), corroborated by the Buddy4Study PMSS 2026 overview (CAPF, Assam Rifles and State/UT police closing 31 October 2026; RPF/RPSF track closing 31 December 2026) and a second guide (2,000 CAPF/AR scholarships; Rs 36,000 girls and Rs 30,000 boys a year; DBT through PFMS). The 5,500 and 500 figures in combined guides belong to the ex-servicemen and State police tracks, not to this track, and are not used as this track\u2019s count.',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP window for 2026-27 runs 1 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — PMSS for Wards and Widows of CAPFs and Assam Rifles 2026', 'https://www.buddy4study.com/article/pmms-for-wards-and-widows-of-capfs-and-assam-rifles'), ('Shiksha — PM Scholarship Scheme 2026-27', 'https://www.shiksha.com/college/articles/pm-scholarship-scheme-2026-27-eligibility-amount-last-date-courses-and-how-to-apply-blogId-243445')],
 'related_titles': ['pmss-police', 'pmss-railways', 'swanath-2026', 'nsp-pg-2026'],
})

# 4. ICAR Post Graduate Scholarship (PGS) 2026
ARTICLES.append({
 'slug': 'icar-post-graduate-scholarship-pgs-2026',
 'title': 'ICAR Post Graduate Scholarship (PGS) 2026',
 'meta': 'ICAR Post Graduate Scholarship (PGS) 2026: Rs 12,640 a month plus Rs 6,000 a year contingency for master\u2019s students in agriculture and allied sciences admitted through the ICAR All India Entrance Examination on AIQ seats. Apply on the National Scholarship Portal by 31 Oct 2026.',
 'short': 'ICAR Post Graduate Scholarship (PGS) 2026',
 'kicker': 'Central Government · Agriculture',
 'mono': 'IC',
 'prov_short': 'ICAR',
 'prov_cat': 'Central Government · Agriculture',
 'h1': 'ICAR Post Graduate Scholarship (PGS) 2026',
 'sub': 'There is no separate test for this scholarship, and that is the first thing to understand about it. You become eligible by the route you take into your master\u2019s programme: admission through the Indian Council of Agricultural Research\u2019s All India Entrance Examination onto an All India Quota seat at an agricultural university in the ICAR system. If you entered that way, the scholarship follows — Rs 12,640 a month plus a Rs 6,000 annual contingency grant, for up to 600 students a year — and the National Scholarship Portal formalities are how the money is released. It is written on its closing day: the portal window for 2026-27 ends on 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Indian Council of Agricultural Research (ICAR), Department of Agricultural Research and Education, through the National Scholarship Portal'),
   ('Benefit', 'Rs 12,640 a month plus Rs 6,000 a year contingency, for the duration of the master\u2019s degree, subject to the minimum OGPA'),
   ('Scale', 'Up to 600 fellowships a year, awarded on All India Entrance Examination merit'),
   ('Eligibility', 'Master\u2019s admission through the ICAR All India Entrance Examination on an AIQ seat; 60% marks or OGPA 6.60 for general, OBC and UPS categories, 55% or OGPA 5.50 for SC, ST and physically challenged candidates'),
   ('Age', 'Minimum 19 years on the date of the entrance examination, with no relaxation'),
   ('Deadline', 'Closes today, 31 Oct 2026 — institute verification by 15 Nov 2026, ministry verification by 30 Nov 2026'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>The ICAR Post Graduate Scholarship supports master\u2019s students in agriculture and allied sciences at agricultural universities under the ICAR-AU system: the State Agricultural Universities, the deemed universities IARI in New Delhi, IVRI at Izatnagar, NDRI at Karnal, CIFE in Mumbai and AAU at Allahabad, the Central Agricultural University at Imphal, and central universities with a faculty of agriculture — BHU, AMU, Visva Bharati and Nagaland University. The award follows the entrance examination, not a separate scholarship application: candidates admitted through the All India Entrance Examination under ICAR All India Quota seats are automatically eligible, and then complete the portal formalities described below.</p>
      <p>Three neighbouring ICAR schemes are easy to confuse with this one, and the amounts must not be mixed. The National Talent Scholarship pays Rs 3,000 a month at undergraduate level and Rs 5,000 a month at postgraduate level, and it requires studying at an agricultural university outside your state of domicile; this scholarship has no such outside-state condition. The ICAR Junior and Senior Research Fellowships are for PhD students and pay Rs 37,000 a month in the first two years and Rs 42,000 in the third, with a Rs 10,000 annual contingency. Older aggregator pages quoting Rs 8,640 a month belong to an older Junior Research Fellowship scale, not to this master\u2019s scholarship; the current figure for this scheme, from the National Scholarship Portal scheme FAQ, is Rs 12,640 a month.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be admitted to a master\u2019s degree programme in agriculture or an allied science at an agricultural university under the ICAR-AU system.</li>
        <li>Have entered through the All India Entrance Examination on an ICAR All India Quota seat. Students admitted through a state agricultural university\u2019s own entrance test are not eligible.</li>
        <li>Hold a bachelor\u2019s degree in the concerned field, or be appearing in its final examination, from a 10+6, 10+2+5 or 10+2+4 stream.</li>
        <li>Be at least 19 years old on the date of the entrance examination; there is no relaxation on this.</li>
        <li>For M.V.Sc. admission, have completed B.V.Sc. and A.H. with internship before the date of registration.</li>
        <li>Meet the marks standard: 60% marks, or an OGPA of 6.60 out of 10.00 (3.25 out of 5.00, or 2.6 out of 4.00), for general, OBC and Under Privileged States categories; 55% marks, or an OGPA of 5.50 out of 10.00 (2.75 out of 5.00, or 2.20 out of 4.00), for SC, ST and physically challenged candidates. Where a university awards only grades, its Registrar certifies the OGPA-to-percentage equivalence. Reservation follows Government of India rules, and the university verifies the certificates.</li>
      </ul>
      <h2 id="benefits">Benefits and continuation</h2>
      <p>The scholarship pays Rs 12,640 a month plus a contingency grant of Rs 6,000 a year — about Rs 1,51,680 a year in monthly payments alone — for the entire duration of the master\u2019s degree programme, subject to good conduct, punctuality and a minimum academic performance. Continuation requires an OGPA of 6.60 out of 10.00, or 60% marks, for general, OBC and UPS categories, and 5.50 out of 10.00, or 55% marks, for SC, ST and physically challenged candidates. The fellowship is not paid automatically for the full course regardless of performance: fall below the qualifying OGPA and the continuation condition fails.</p>
      <h2 id="documents">Documents needed</h2>
      <p>Because the award follows the entrance examination, the document the portal FAQ names for release of the scholarship is the award letter issued by ICAR. In the portal process you will also enter your entrance examination and AIQ admission details exactly as they appear on your admission record, together with your bank account and Aadhaar details.</p>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Register or log in on the National Scholarship Portal and select the ICAR Post Graduate Scholarship (PGS) scheme under the Department of Agricultural Research and Education.</li>
        <li>Enter your entrance examination and AIQ admission details exactly as they appear on your admission record, along with your bank account and Aadhaar details.</li>
        <li>Upload the award letter issued by ICAR.</li>
        <li>Submit before 31 October 2026. Your university must verify the application by 15 November 2026, and district, state and ministry verification runs to 30 November 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Do I apply separately for this scholarship?', 'No. Admission through the All India Entrance Examination on an ICAR AIQ seat makes you automatically eligible; you still have to complete the National Scholarship Portal formalities and upload the ICAR award letter before the closing date.'),
   ('Am I eligible if I entered through my state university\u2019s own test?', 'No. Only admissions through the All India Entrance Examination on ICAR All India Quota seats in the ICAR-AU system qualify.'),
   ('How much does it pay?', 'Rs 12,640 a month plus Rs 6,000 a year as a contingency grant, for the duration of the master\u2019s degree, subject to the minimum OGPA.'),
   ('Is this the same as the ICAR National Talent Scholarship?', 'No. The talent scholarship pays Rs 3,000 a month at undergraduate level and Rs 5,000 at postgraduate level and requires studying outside your home state. This scholarship has no outside-state condition and pays the fellowship rate above.'),
   ('What OGPA must I maintain?', '6.60 out of 10.00, or 60% marks, for general, OBC and UPS categories; 5.50 out of 10.00, or 55%, for SC, ST and physically challenged candidates.'),
   ('When does the 2026-27 window close?', 'Today, 31 October 2026, for the student application on the National Scholarship Portal, with institute verification by 15 November 2026.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the ICAR Post Graduate Scholarship 2026-27 guide based on the National Scholarship Portal scheme FAQ and the ICAR fellowship guidelines (Rs 12,640 a month plus Rs 6,000 a year contingency; 600 fellowships a year on All India Entrance Examination merit; AIQ-seat admission only; bachelor\u2019s in the concerned field from a 10+6, 10+2+5 or 10+2+4 stream; minimum age 19 with no relaxation; M.V.Sc. internship condition; 60% or OGPA 6.60 for general, OBC and UPS, 55% or OGPA 5.50 for SC, ST and physically challenged candidates; ICAR-AU institution list; continuation OGPA rule; ICAR award letter as the portal document; window 1 June to 31 October 2026 with verification 15 and 30 November 2026), corroborated by the NSP ICAR agriculture schemes overview (all four ICAR schemes opened 1 June 2026 and share the 31 October 2026 student deadline; PGS described as fellowship plus contingency, distinct from the fixed NTS rates). The Rs 8,640 figure in older guides belongs to the older Junior Research Fellowship scale, and the Rs 37,000 and Rs 42,000 figures belong to the PhD JRF and SRF tracks; neither is used as this scheme\u2019s rate.',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP window for 2026-27 runs 1 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('ICAR Post Graduate Scholarship 2026-27 guide (NSP FAQ-based)', 'https://scholarshiplist.org/icar-pg-scholarship-pgs/'), ('NSP ICAR Agriculture Scholarships 2026-27 overview', 'https://scholarshipsx.com/nsp-icar-agriculture-scholarships/')],
 'related_titles': ['icar-nts', 'icar-ntspg', 'icar-jrf', 'nsp-pg-2026'],
})

# 5. Post-Matric Education Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27
ARTICLES.append({
 'slug': 'post-matric-beedi-cine-iomc-lsdm-workers-2026-27',
 'title': 'Post-Matric Education Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27',
 'meta': 'Post-Matric Education Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27: Rs 3,000 a year for Classes 11-12, Rs 6,000 for ITI, diploma and degree courses, and up to Rs 25,000 for professional courses, for children of beedi, cine and mine workers. Apply on the National Scholarship Portal by 31 Oct 2026.',
 'short': 'Post-Matric Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27',
 'kicker': 'Central Government · Labour Welfare',
 'mono': 'LW',
 'prov_short': 'Ministry of Labour and Employment',
 'prov_cat': 'Central Government · Labour Welfare',
 'h1': 'Post-Matric Education Assistance for Wards of Beedi, Cine, IOMC and LSDM Workers 2026-27',
 'sub': 'Beedi rollers, cinema workers and miners are among the lowest-paid formal workforces in the country, and this scheme is the Labour Ministry\u2019s answer for their children once they pass Class 10. Run by the Directorate General of Labour Welfare through the National Scholarship Portal, it pays a fixed annual sum that rises with the level of study — Rs 3,000 in Classes 11 and 12, Rs 6,000 for ITI, diploma and degree courses, and up to Rs 25,000 for professional degrees. It is written on its closing day: the post-matric window for 2026-27 ends on 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Ministry of Labour and Employment, through the Directorate General of Labour Welfare and the National Scholarship Portal'),
   ('Benefit', 'Rs 3,000 a year for Classes 11 and 12; Rs 6,000 for ITI, polytechnic diploma and undergraduate degree courses; up to Rs 25,000 for professional courses — a single lump sum, with no separate hostel or book allowance'),
   ('Eligibility', 'Ward of a beedi, cine, iron ore, manganese ore, chrome ore, limestone or dolomite mine worker; Class 10 passed at the first attempt; regular post-matric course from Class 11 onwards'),
   ('Income limit', 'Annual family income up to Rs 1,20,000 (Rs 10,000 a month) for beedi, IOMC and LSDM families; up to Rs 96,000 (Rs 8,000 a month) for cine families'),
   ('Family cap', 'A maximum of two children from the same family'),
   ('Deadline', 'Closes today, 31 Oct 2026 — institute verification by 15 Nov 2026, ministry verification by 30 Nov 2026'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>The scheme is formally titled Financial Assistance for Education to the Wards of Beedi, Cine, IOMC and LSDM Workers, Post-Matric, and it is financed through the welfare cess collected on beedi, cine and mining products. It covers the children of workers in the beedi industry as defined under the Beedi Workers Welfare Fund Act, 1966; the cine industry, where the worker must be registered with the Ministry of Information and Broadcasting and have completed at least six months of service; and the iron ore, manganese ore and chrome ore mines (IOMC) and the limestone and dolomite mines (LSDM), under their respective welfare cess acts. Mica mines appear in some older listings of the scheme\u2019s coverage; the 2026-27 scheme description used here names beedi, cine, IOMC and LSDM, and applicants from a mica-mining family should confirm their coverage on the portal before applying.</p>
      <p>The pre-matric version of this assistance, for Classes 1 to 10, is a separate entry with its own window, which closed on 31 August 2026. This article covers only the post-matric version, for students from Class 11 onwards up to postgraduate and professional study. One summary figure needs care: some news reports describe the scheme\u2019s benefits as ranging from Rs 1,000 to Rs 25,000 a year. The Rs 1,000 end of that range belongs to the pre-matric version\u2019s lower classes; the post-matric amounts in the table below start at Rs 3,000, and this article uses the post-matric table throughout.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>Be an Indian citizen and the ward of a registered worker, or of a deceased worker, in the beedi, cine, IOMC or LSDM sectors described above. Dependents of deceased workers are eligible where they were financially dependent on the worker.</li>
        <li>Have passed Class 10 at the first attempt, and be enrolled in a regular post-matric course — Class 11 onwards — at a recognised institution. Distance education courses are not eligible.</li>
        <li>Be pursuing a general or technical course such as medical, engineering, ITI or polytechnic study. Postgraduate courses are eligible only where they directly continue an undergraduate professional course, such as M.Tech after B.Tech, with proof of continuous enrolment.</li>
        <li>Meet the income limits: annual family income up to Rs 1,20,000 for beedi, IOMC and LSDM families, and up to Rs 96,000 for cine families. The parent must have at least six months of continuous service as an eligible worker, including qualifying contract and manual workers.</li>
        <li>Have secured at least 50% marks in the last examination. The listing notes this requirement may be relaxed for SC and ST students in certain cases, and that preference goes to applicants with higher marks and lower family income; the scheme\u2019s FAQ adds that there is no strict cutoff beyond the first-attempt pass, with 50% holders given preference in selection.</li>
        <li>Not be receiving any other central or state scholarship for the same purpose. A maximum of two children from the same family may benefit, and students who change subject or professional stream midway, who fail or repeat a year, or who take a study gap of more than one academic year, lose eligibility.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Classes 11 and 12: Rs 3,000 a year</li>
        <li>ITI: Rs 6,000 a year</li>
        <li>Polytechnic diploma: Rs 6,000 a year</li>
        <li>Undergraduate degree, such as B.A., B.Sc. or B.Sc. Agriculture: Rs 6,000 a year</li>
        <li>Professional courses, such as MBBS, B.Tech, B.E. or Law: up to Rs 25,000 a year</li>
      </ul>
      <p>The award is a lump sum covering tuition and maintenance together; no separate allowance is provided for hostel, books, uniforms or accommodation. It is disbursed in a single instalment by Direct Benefit Transfer to the student\u2019s Aadhaar-linked bank account through the Public Finance Management System, after verification. A fresh application is required each academic year, although students who are promoted and continue to meet the conditions remain eligible, and family income must be re-verified every three years.</p>
      <h2 id="documents">Documents needed</h2>
      <ul>
        <li>Passport-size photograph</li>
        <li>Aadhaar card or alternative government-issued ID, such as voter ID or PAN card, for One-Time Registration and verification</li>
        <li>Parent\u2019s worker identity proof: beedi worker ID or registration proof from the welfare board; cine registration certificate or ID from the Directorate of Film Festivals or the Ministry of Information and Broadcasting, showing six months of service; IOMC or LSDM Form B register or ID from the Directorate General of Mines Safety or the welfare cess authority</li>
        <li>Income certificate, no more than six months old, from the Tehsildar or Revenue Officer, within the limits above</li>
        <li>Marksheets of the last qualifying examination — Class 10 for fresh applicants, the previous year for renewals — showing a first-attempt pass</li>
        <li>Admission proof: bonafide certificate or admission letter from a recognised institution for a regular post-matric course</li>
        <li>Bank account details: passbook front page or cancelled cheque, Aadhaar-linked, preferably in the student\u2019s name or jointly with a parent</li>
        <li>Self-declaration certificate, via Aadhaar OTP on the portal, confirming the first-attempt pass, no other scholarship, and eligibility compliance</li>
        <li>Death certificate, if applicable, for wards of deceased workers</li>
        <li>Caste certificate, if applicable, for SC, ST or OBC applicants seeking relaxations</li>
      </ul>
      <h2 id="apply">How to apply</h2>
      <ol>
        <li>Visit the National Scholarship Portal and complete One-Time Registration, using Aadhaar, mobile number, OTP and face authentication through the portal app.</li>
        <li>Log in and navigate to Application, then Apply for Scholarship, then academic year 2026-27, then Ministry of Labour and Employment, then the scheme titled Financial Assistance for Education to the Wards of Beedi, Cine, IOMC and LSDM Workers, Post-Matric.</li>
        <li>Enter the required personal details, upload the Class 10 and previous-year marksheets, submit Form B for mines or the beedi licence as applicable, upload the income certificate, and provide Aadhaar-linked bank account information.</li>
        <li>Review every entry carefully before submitting, as no edits can be made after submission, and then track the application under Check Your Status. Submit on or before 31 October 2026; defective-application and institute verification run to 15 November 2026, and district, state and ministry verification to 30 November 2026.</li>
      </ol>
      <p>For queries, the scheme\u2019s FAQ gives the National Scholarship Portal helpline 0120-6619540, from 9 a.m. to 6 p.m., and the email helpdesk@nsp.gov.in; worker-status questions go to the Directorate General of Labour Welfare through the Ministry\u2019s website or regional offices, or to the institution\u2019s nodal officer.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('What if my parent is retired or deceased?', 'You can still apply if your parent was a registered worker at retirement or death and the family income remains within the limits, with proof of worker status and, for deceased workers, a death certificate.'),
   ('Is there a separate hostel allowance?', 'No. The lump sum is designed to cover tuition, maintenance and incidental costs including hostel fees, within the awarded amount.'),
   ('Can two siblings apply in the same year?', 'Yes. Up to two children from the same family can apply, each with a separate application; where funds are limited, priority goes to the elder child or the one with higher academic merit.'),
   ('What happens if my application is marked defective?', 'Log in to the portal, check the defective-application section, and upload the correct documents, with help from the portal helpline or your institution\u2019s nodal officer, before the verification deadline.'),
   ('Are postgraduate courses covered?', 'Only where they directly continue an undergraduate professional course, such as M.Tech after B.Tech, with proof of continuous enrolment and the other conditions met.'),
   ('When does the post-matric window close?', 'Today, 31 October 2026, for student applications on the National Scholarship Portal. The pre-matric version closed separately on 31 August 2026.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study Beedi, Cine, IOMC and LSDM Workers Scholarship 2026-27 guide (post-matric window 1 June to 31 October 2026; defective and institute verification 15 November 2026; DNO/SNO/MNO verification 30 November 2026; amounts Rs 3,000 Classes 11-12, Rs 6,000 ITI, diploma and undergraduate degree, Rs 25,000 professional courses; lump sum with no separate hostel or book allowance; eligibility including Class 10 first-attempt pass, regular course, 50% marks with SC/ST relaxation in certain cases, income Rs 1,20,000 beedi/IOMC/LSDM and Rs 96,000 cine, two-children cap, no other scholarship for the same purpose; full document list including Form B, beedi licence, income certificate up to six months old and Aadhaar OTP self-declaration; NSP application steps; helpline 0120-6619540 and helpdesk@nsp.gov.in), corroborated by news reports of the same window (application deadline 31 October 2026; institute verification 15 November 2026; six months of service; beedi and cine monthly income limits of Rs 10,000). The Rs 1,000 figure in some summaries belongs to the pre-matric version\u2019s lower classes, not to this post-matric table; mica mines appear in some older coverage but not in the 2026-27 scheme description used here, and are flagged rather than asserted.',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP post-matric window for 2026-27 runs 1 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — Beedi, Cine, IOMC and LSDM Workers Scholarship 2026-27', 'https://www.buddy4study.com/article/beedi-cine-iomc-lsdm-workers-scholarship'), ('Labour Welfare Scholarship 2026 — applications closing 31 October', 'https://timesofindia.indiatimes.com/education/news/labour-welfare-scholarship-2026-applications-closing-soon-apply-by-october-31/amp_articleshow/134850150.cms')],
 'related_titles': ['pmss-police', 'pmss-railways', 'swanath-2026', 'nsp-pg-2026'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

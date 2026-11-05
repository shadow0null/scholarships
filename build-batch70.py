import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'balmiki-2026': {'mono': 'MB', 'title': 'NSP Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026-27',
   'href': 'nsp-maharishi-balmiki-chatravriti-yojana-himachal-pradesh-2026-27.html',
   'dpill': 'Deadline 31 Oct 2026',
   'award': '₹18,000 a year for college-level and professional courses, per the 2026 listings; some older HP guides give ₹9,000 a year, so confirm the current rate on NSP.',
   'elig': 'Girl students domiciled in Himachal Pradesh, from Balmiki families engaged in unclean occupations, admitted to a post-matric or professional course.',
   'tags': [('Himachal Pradesh', 'teal'), ('Girls', 'blue')]},
 'protsahan-2026': {'mono': 'MP', 'title': 'NSP Mukhya Mantri Protsahan Yojana, Himachal Pradesh 2026-27',
   'href': 'nsp-mukhya-mantri-protsahan-yojana-himachal-pradesh-2026-27.html',
   'dpill': 'Deadline 31 Oct 2026',
   'award': 'A one-time incentive of ₹75,000 for Himachali students admitted to an IIT, AIIMS, IIM, ISM Dhanbad or IISc Bangalore.',
   'elig': 'Students domiciled in Himachal Pradesh who have secured admission to a degree course at an IIT or AIIMS, or a postgraduate diploma at an IIM (ISM Dhanbad and IISc Bangalore also listed).',
   'tags': [('Himachal Pradesh', 'teal'), ('Merit', 'purple')]},
 'nsp-pg-2026': {'mono': 'UGC', 'title': 'NSP National Scholarship for Post Graduate Studies 2026-27',
   'href': 'nsp-national-scholarship-post-graduate-studies-2026-27.html',
   'dpill': 'Deadline 31 Oct 2026',
   'award': '₹15,000 a month for 10 months a year, for two years (₹1,50,000 a year; ₹3,00,000 in total), for 10,000 scholars a year.',
   'elig': 'Indian students under 30, admitted to the first year of a regular, full-time postgraduate degree at a UGC-recognised institution, pursuing their first postgraduate degree.',
   'tags': [('Postgraduate', 'purple'), ('Central Government', 'teal')]},
 'navgurukul-pune': {'mono': 'NG', 'title': 'Navgurukul Residential Programmes (Pune)',
   'href': 'navgurukul-residential-programmes-pune.html',
   'dpill': 'Applications open (no fixed deadline published)',
   'award': 'A fully funded residential programme (accommodation, meals and learning materials) lasting 1 to 2 years, with 100% placement assistance.',
   'elig': 'Youth above 16 from underprivileged or low-income families who cannot afford expensive college education; no prior education is required.',
   'tags': [('Residential', 'purple'), ('Maharashtra', 'teal')]},
 'navgurukul-business-sarjapur': {'mono': 'NG', 'title': 'Navgurukul School of Business Residential Programme (Sarjapur)',
   'href': 'navgurukul-school-of-business-residential-programme-sarjapur.html',
   'dpill': 'Applications open (no fixed deadline published)',
   'award': 'A fully funded residential business course (Google Suite, CRM and Salesforce, digital marketing, data analytics) with 100% placement assistance.',
   'elig': 'Youth above 16 from underprivileged or low-income families; no prior education is required, and some English is good to have.',
   'tags': [('Residential', 'purple'), ('Karnataka', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. Maharishi Balmiki
ARTICLES.append({
 'slug': 'nsp-maharishi-balmiki-chatravriti-yojana-himachal-pradesh-2026-27',
 'title': 'NSP Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026-27',
 'meta': 'Maharishi Balmiki Chatravriti Yojana 2026-27: ₹18,000 a year for girl students from Balmiki families in Himachal Pradesh studying post-matric or professional courses. Apply on the National Scholarship Portal by 31 October 2026.',
 'short': 'NSP Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026-27',
 'kicker': 'Himachal Pradesh · Girls’ Welfare Scholarship',
 'mono': 'MB',
 'prov_short': 'Govt. of Himachal Pradesh',
 'prov_cat': 'Himachal Pradesh · NSP',
 'h1': 'NSP Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026-27',
 'sub': 'The Maharishi Balmiki Chatravriti Yojana is a Himachal Pradesh welfare scholarship for girl students from Balmiki families engaged in unclean occupations: it pays for college-level and professional study after matriculation, so that a family’s occupation does not decide whether a daughter continues her education. For 2026-27 it runs on the National Scholarship Portal and closes on 31 October 2026 — tomorrow — so an eligible student should apply today rather than wait for the portal to close. One figure in this article needs care, because older Himachal guides give a lower annual amount than the 2026 listings, and the difference is flagged openly below.',
 'dpill': 'Deadline 31 Oct 2026',
 'facts': facts([
   ('Provider', 'Government of Himachal Pradesh (Department of Education), applied for through the National Scholarship Portal (NSP)'),
   ('Award', '₹18,000 a year for college-level and professional courses, per the 2026 listings checked. Older Himachal guides give ₹9,000 a year for this scheme — confirm the amount in force on the NSP scheme page before applying'),
   ('Level', 'Post-matric and professional courses — Bachelors, Masters, MBA and medical (MBBS/MD) courses are listed in the 2026 guides'),
   ('Deadline', '31 October 2026 (NSP window for 2026-27: 4 June to 31 October 2026, per the Buddy4Study Himachal Pradesh table)'),
   ('Eligibility', 'Girl student domiciled in Himachal Pradesh, belonging to a Balmiki family engaged in an unclean occupation, admitted to a post-matric or professional course at a recognised private or government institute or college'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The Maharishi Balmiki Chatravriti Yojana is a state welfare scheme, not a central merit scheme: it is run by the Himachal Pradesh government for girls from the Balmiki community, a community that has historically worked in sanitation and other unclean occupations and that faces both social and economic disadvantage. The scheme’s logic is simple — the barrier it removes is the cost of staying in education after school, and the condition that matters most is the family background it is designed for, not an examination rank.</p>
      <p>Applications for 2026-27 are made on the National Scholarship Portal, the same portal that carries Himachal Pradesh’s other state schemes for the year, and the 2026-27 window is given as 4 June to 31 October 2026. One Time Registration (OTR) on NSP is required before applying, and the institute where the student is admitted verifies the application, as with other NSP schemes.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Financial assistance of ₹18,000 a year for college-level and professional courses, as stated in the 2026 listings checked (WeMakeScholars, Notopedia and the Buddy4Study scheme page).</li>
        <li>Coverage for study at a recognised private or government institute or college in Himachal Pradesh, across Bachelors, Masters, MBA and medical courses in the 2026 listings.</li>
        <li>Payment through the National Scholarship Portal system into the student’s bank account; Himachal college notices stress that the account should be Aadhaar-seeded.</li>
      </ul>
      <p>A note on the amount, because the sources genuinely disagree. The 2026 listings checked all give ₹18,000 a year, but older Himachal guides — including a Himachal scholarship portal guide and a state scholarship overview — give ₹9,000 a year for this scheme, and one older scheme description gives ₹15,000 a year for college studies in a different year’s listing. The direction is consistent with the scheme’s amount having been revised upward over time, but the older figures have not been corrected everywhere. This article uses ₹18,000 because it is the figure in the 2026 listings, and it flags the older figures here rather than hiding them. Confirm the amount in force on the NSP scheme page before relying on it.</p>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are a girl student and a permanent resident (bonafide student) of Himachal Pradesh.</li>
        <li>You belong to a Balmiki family engaged in an unclean occupation, and you can produce a certificate from the competent authority in Himachal Pradesh saying so. This certificate is the scheme’s defining document — without it, the application does not fit the scheme.</li>
        <li>You have been admitted to a post-matric or professional course at a recognised private or government institute or college. Older scheme descriptions describe admission from matriculation onwards; the 2026 listings describe post-matric and professional courses, so confirm the course level that applies to you on NSP.</li>
        <li>Income: no scheme-specific income cap was published in the 2026 listings checked for this scheme. Himachal college scheme notices list a parental-income condition of less than ₹2.5 lakh a year across the state’s NSP schemes, and an income certificate from an officer not below the rank of Tehsildar is listed among the documents. If an income rule applies to your application, the NSP scheme page will show it — do not assume the ₹2.5 lakh figure is or is not the scheme’s own rule.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The documents listed in a Himachal Pradesh college’s NSP notice for this scheme are: a self-attested passport-size photograph, an Aadhaar card (UID/EID number), a Himachali bonafide certificate, previous years’ result cards from matriculation onwards, the latest bank statement of the student’s bank account, an SC category certificate issued by an officer not below the rank of Tehsildar, an income certificate of the parent or guardian issued by an officer not below the rank of Tehsildar, and the fee structure approved by the university, board or government. The scheme-specific document on top of that list is the certificate from the competent authority for belonging to a Balmiki family engaged in an unclean occupation, and a separate certificate for working in an unclean occupation. Follow the document list shown on the NSP application itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete One Time Registration (OTR) on the National Scholarship Portal at scholarships.gov.in, if you have not already done so.</li>
        <li>Find the Maharishi Balmiki Chatravriti Yojana under the Himachal Pradesh state scholarships on NSP and open the 2026-27 application.</li>
        <li>Fill in your domicile, family-background and admission details, upload the documents listed above — above all the Balmiki-family and unclean-occupation certificates — and submit before 31 October 2026. The portal closes automatically at the deadline, and this article is written the day before it.</li>
        <li>Have your institute verify your enrolment, as NSP applications require institute verification before the state processes payment.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much does the scheme pay?', '₹18,000 a year for college-level and professional courses, per the 2026 listings checked. Older Himachal guides give ₹9,000 a year, so confirm the current amount on the NSP scheme page.'),
   ('Who is it for?', 'Girl students domiciled in Himachal Pradesh who belong to Balmiki families engaged in unclean occupations and are admitted to a post-matric or professional course.'),
   ('What is the deadline for 2026-27?', '31 October 2026 on the National Scholarship Portal, with the window given as 4 June to 31 October 2026. Apply immediately: this is the last day.'),
   ('What is the one document I must not forget?', 'The certificate from the competent authority in Himachal Pradesh confirming that you belong to a Balmiki family engaged in an unclean occupation. It is what makes the application fit this scheme.'),
   ('Is there an income limit?', 'No scheme-specific income cap was published in the 2026 listings checked. Himachal college notices list a ₹2.5 lakh parental-income condition across the state’s NSP schemes, so check the NSP scheme page for the rule that applies to you.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the Buddy4Study Himachal Pradesh 2026-27 table (Maharishi Balmiki Chatravriti Yojana: 4 June to 31 October 2026), WeMakeScholars (₹18,000 a year, female HP domicile, Balmiki family in unclean occupation, post-matric/professional admission, 31 October 2026), a Himachal Pradesh college NSP notice for 2026-27 (girls from Balmiki families, Balmiki/unclean-occupation certificates, document list, ₹2.5 lakh income condition across HP schemes) and older HP guides giving ₹9,000 a year. The amount disagreement is carried openly in the article.',
 'dl_long': '31 October 2026 (National Scholarship Portal; window 4 June to 31 October 2026)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('Buddy4Study — Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh', 'https://www.buddy4study.com/scholarship/maharishi-balmiki-chatravriti-yojana-himachal-pradesh'), ('Buddy4Study — HP Scholarships 2026-27 (deadline table)', 'https://www.buddy4study.com/article/hp-scholarship'), ('WeMakeScholars — Maharishi Balmiki Chatravriti Yojana, Himachal Pradesh 2026', 'https://www.wemakescholars.com/scholarship/maharishi-balmiki-chatravriti-yojana-himachal-pradesh')],
 'related_titles': ['protsahan-2026', 'kalpana-2026', 'nsp-pg-2026', 'ambedkar-hp'],
})

# 2. Mukhya Mantri Protsahan
ARTICLES.append({
 'slug': 'nsp-mukhya-mantri-protsahan-yojana-himachal-pradesh-2026-27',
 'title': 'NSP Mukhya Mantri Protsahan Yojana, Himachal Pradesh 2026-27',
 'meta': 'Mukhya Mantri Protsahan Yojana 2026-27: a one-time ₹75,000 incentive for Himachali students admitted to an IIT, AIIMS, IIM, ISM Dhanbad or IISc Bangalore. Apply on the National Scholarship Portal by 31 October 2026.',
 'short': 'NSP Mukhya Mantri Protsahan Yojana, Himachal Pradesh 2026-27',
 'kicker': 'Himachal Pradesh · Premier-Institute Incentive',
 'mono': 'MP',
 'prov_short': 'Govt. of Himachal Pradesh',
 'prov_cat': 'Himachal Pradesh · NSP',
 'h1': 'NSP Mukhya Mantri Protsahan Yojana, Himachal Pradesh 2026-27',
 'sub': 'The Mukhya Mantri Protsahan Yojana is Himachal Pradesh’s welcome reward for its students who reach the country’s premier institutes: any Himachali student selected and admitted to a degree course at an IIT or AIIMS, or to a postgraduate diploma at an IIM, receives a one-time incentive of ₹75,000. Students admitted to the Indian School of Mines (ISM) Dhanbad and the Indian Institute of Science (IISc) Bangalore are also covered. For 2026-27 it runs on the National Scholarship Portal and, on the NSP window, closes on 31 October 2026 — tomorrow — so apply today; one listing gives a later December date, and that disagreement is flagged below rather than hidden.',
 'dpill': 'Deadline 31 Oct 2026',
 'facts': facts([
   ('Provider', 'Government of Himachal Pradesh (Department of Higher Education), applied for through the National Scholarship Portal (NSP)'),
   ('Award', 'A one-time incentive or award of ₹75,000, paid once to each eligible Himachali student'),
   ('Level', 'Degree courses at IITs and AIIMS; postgraduate diploma courses at IIMs; ISM Dhanbad and IISc Bangalore also listed as eligible institutions'),
   ('Deadline', '31 October 2026 on the NSP 2026-27 window (4 June to 31 October 2026, per the Buddy4Study Himachal Pradesh table). One listing gives 31 December 2026 — confirm the live date on NSP and do not rely on the later date'),
   ('Eligibility', 'Student domiciled in Himachal Pradesh who has been selected and admitted to a degree course at an IIT or AIIMS, or to a postgraduate diploma course at an IIM; ISM Dhanbad and IISc Bangalore admissions also eligible. No minimum-marks or income condition was published in the sources checked'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>The Mukhya Mantri Protsahan Yojana, launched by the Himachal Pradesh Department of Higher Education in 2013-14, is an incentive, not a recurring scholarship: it is paid once, when a Himachali student gets into one of the named premier institutes, and it is not renewed year after year. Its purpose is straightforward — to mark, and partly to fund, the step from a Himachal school or college into an IIT, an AIIMS, an IIM, ISM Dhanbad or IISc Bangalore, where the costs of moving and settling in are highest in the first term.</p>
      <p>Applications for 2026-27 are made on the National Scholarship Portal, the same portal that carries Himachal Pradesh’s other state schemes for the year. The Buddy4Study Himachal Pradesh 2026-27 table gives the window as 4 June to 31 October 2026, and a Himachal college notice for 2026-27 likewise lists 31 October 2026 as the NSP last date for the state’s schemes. One listing (Notopedia) gives 31 December 2026 for this scheme. That later date may reflect a different portal or an older cycle’s date, and it is not the NSP window date; treat 31 October 2026 as the deadline and do not plan around December.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A one-time incentive of ₹75,000, paid to every eligible Himachali student admitted to a named institute — it is not a competition with a fixed number of winners in the sources checked.</li>
        <li>Coverage for degree courses at any IIT or AIIMS, and for postgraduate diploma courses at any IIM.</li>
        <li>Coverage also for admissions to the Indian School of Mines (ISM) Dhanbad and the Indian Institute of Science (IISc) Bangalore, which were added to the eligible list.</li>
        <li>Payment through the National Scholarship Portal system into the student’s bank account; an Aadhaar-seeded bank account is listed among the documents.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are domiciled in Himachal Pradesh (a bonafide Himachali student).</li>
        <li>You have been selected and admitted to a degree course at an Indian Institute of Technology (IIT) or an All India Institute of Medical Sciences (AIIMS), or to a postgraduate diploma course at an Indian Institute of Management (IIM).</li>
        <li>Alternatively, you have been selected and admitted to a full-time undergraduate degree programme at IISc Bangalore or ISM Dhanbad, which the scheme’s descriptions also list as eligible.</li>
        <li>Both boys and girls can apply, and the scheme is open to all categories in the descriptions checked — admission to a named institute, not a category or a marks threshold, is the qualifying fact.</li>
        <li>No minimum-marks condition and no income cap were published in the sources checked for this scheme. Some general descriptions mention demonstrating financial need, but no figure is given; do not invent one, and check the NSP scheme page if a need condition is shown for your application.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The documents listed for this scheme across the scheme descriptions checked are: a passport-size photograph, an Aadhaar card (UID/EID number), a Himachali bonafide or domicile certificate, previous years’ result cards from matriculation onwards, the latest bank statement of the student’s bank account, and the selection letter or admission proof from the IIT, IIM, AIIMS, ISM or IISc. The selection letter is the decisive document: it is what proves the admission that the whole incentive turns on. Follow the document list shown on the NSP application itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete One Time Registration (OTR) on the National Scholarship Portal at scholarships.gov.in, if you have not already done so.</li>
        <li>Find the Mukhya Mantri Protsahan Yojana under the Himachal Pradesh state scholarships on NSP and open the 2026-27 application.</li>
        <li>Fill in your domicile and admission details, upload the documents listed above — above all your selection letter or admission proof — and submit before 31 October 2026. Do not rely on the 31 December 2026 date given in one listing.</li>
        <li>Have your institute verify your enrolment, as NSP applications require institute verification before the state processes payment.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the incentive?', '₹75,000, paid once. It is a one-time award, not a yearly scholarship.'),
   ('Which admissions qualify?', 'A degree course at an IIT or AIIMS, a postgraduate diploma course at an IIM, or admission to ISM Dhanbad or IISc Bangalore.'),
   ('What is the deadline for 2026-27?', '31 October 2026 on the NSP window (4 June to 31 October 2026). One listing gives 31 December 2026, but that is not the NSP window date — treat 31 October as the deadline.'),
   ('Is there a marks or income cut-off?', 'No minimum-marks condition and no income figure were published in the sources checked. Admission to a named institute is the qualifying fact.'),
   ('Can the award be claimed more than once?', 'No. The scheme’s descriptions describe a one-time incentive for the admission, not a renewable award.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the Buddy4Study Himachal Pradesh 2026-27 table (Mukhya Mantri Protsahan Yojana: 4 June to 31 October 2026), Notopedia (₹75,000 one-time, IIT/AIIMS degree or IIM postgraduate diploma, ISM Dhanbad and IISc Bangalore added, documents including domicile, Aadhaar, photograph, mark sheets, admission proof and Aadhaar-seeded bank details; its 31 December 2026 date is flagged, not followed) and earlier scheme descriptions (Department of Higher Education, Himachal Pradesh, 2013-14 launch, same ₹75,000 figure, selection letter as the key document). The deadline disagreement is carried openly in the article.',
 'dl_long': '31 October 2026 (National Scholarship Portal; window 4 June to 31 October 2026 — one listing gives 31 December 2026; do not rely on the later date)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('Buddy4Study — Mukhya Mantri Protsahan Yojana, Himachal Pradesh', 'https://www.buddy4study.com/scholarship/mukhya-mantri-protsahan-yojana-himachal-pradesh'), ('Buddy4Study — HP Scholarships 2026-27 (deadline table)', 'https://www.buddy4study.com/article/hp-scholarship')],
 'related_titles': ['balmiki-2026', 'kalpana-2026', 'nsp-pg-2026', 'ambedkar-hp'],
})

# 3. NSP National Scholarship for Post Graduate Studies
ARTICLES.append({
 'slug': 'nsp-national-scholarship-post-graduate-studies-2026-27',
 'title': 'NSP National Scholarship for Post Graduate Studies 2026-27',
 'meta': 'National Scholarship for Post Graduate Studies 2026-27: ₹15,000 a month for 10 months a year, for two years, for 10,000 first-year postgraduate students. Apply on the National Scholarship Portal by 31 October 2026.',
 'short': 'NSP National Scholarship for Post Graduate Studies 2026-27',
 'kicker': 'India · Postgraduate Scholarship · UGC',
 'mono': 'UGC',
 'prov_short': 'University Grants Commission (UGC)',
 'prov_cat': 'Central Government · NSP',
 'h1': 'NSP National Scholarship for Post Graduate Studies 2026-27',
 'sub': 'The National Scholarship for Post Graduate Studies is the University Grants Commission’s large merit scholarship for the first year of a postgraduate degree: 10,000 new scholars a year receive ₹15,000 a month for 10 months of the year, for two years, adding up to ₹1,50,000 a year and ₹3,00,000 over the degree. It is open only to students in the first year of a regular, full-time postgraduate programme at a recognised institution, and only if it is their first postgraduate degree. For 2026-27 it runs on the National Scholarship Portal and closes on 31 October 2026 — tomorrow — so a first-year postgraduate student who fits the conditions should apply today.',
 'dpill': 'Deadline 31 Oct 2026',
 'facts': facts([
   ('Provider', 'University Grants Commission (UGC), Government of India, through the National Scholarship Portal (NSP)'),
   ('Award', '₹15,000 a month for 10 months a year, for two years — ₹1,50,000 a year, ₹3,00,000 in total — for 10,000 scholars a year'),
   ('Level', 'First year of a regular, full-time postgraduate degree programme (first postgraduate degree only)'),
   ('Deadline', '31 October 2026 (student applications; scheme opened 16 September 2026. Institute verification to 15 November 2026, district-level verification to 30 November 2026)'),
   ('Eligibility', 'Indian students under 30 at the time of admission, admitted to the first year of a full-time postgraduate degree at a UGC-recognised institution (Section 2(f) or 3 of the UGC Act, with a valid AISHE code), not already holding a postgraduate degree. Distance, open-learning, part-time and private courses are excluded'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>The National Scholarship for Post Graduate Studies is one of the UGC’s flagship student schemes, and its size is what sets it apart: 10,000 fresh scholarships a year, each worth ₹1,50,000 a year, is a national programme rather than a small trust fund. Selection is described as purely on an all-India merit basis, which means the competition is with first-year postgraduate students across the country, not only within one university or state.</p>
      <p>Two restrictions define the scheme and catch applicants out. First, it is only for the first year of a postgraduate degree: a student already in the second or final year cannot apply fresh. Second, it is only for a first postgraduate degree: a student who already holds a master’s degree cannot apply for a second one under this scheme. The course itself must be a recognised postgraduate degree programme pursued in regular, full-time mode at an institution recognised under Section 2(f) or Section 3 of the UGC Act and carrying a valid AISHE code.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>₹15,000 a month for 10 months of each academic year.</li>
        <li>A tenure of two years, giving ₹1,50,000 a year and ₹3,00,000 over the full tenure, subject to the scheme’s renewal and performance conditions.</li>
        <li>10,000 scholarships awarded each year across India.</li>
        <li>Payment through the National Scholarship Portal system into the student’s Aadhaar-seeded bank account.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are an Indian student admitted to the first year of a postgraduate degree programme in the 2026-27 academic year.</li>
        <li>Your programme is a recognised postgraduate degree pursued in regular, full-time mode at a university, college or institution recognised under Section 2(f) or Section 3 of the UGC Act, with a valid AISHE code. Distance, open-learning, part-time and private modes are excluded.</li>
        <li>It is your first postgraduate degree. Students who have already acquired a postgraduate degree are not eligible.</li>
        <li>You are under 30 years of age at the time of admission to the postgraduate programme.</li>
        <li>Income: the UGC scholarship table checked gives no income limit for this scheme, while a 2025 guide mentions a parental income below ₹8 lakh a year as expected. The two do not agree, so if an income condition matters to your application, check the current NSP scheme page rather than assuming either figure.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>The documents named in the official-information summaries checked are: attested copies of mark sheets and certificates from Class 9 onwards, an attested copy of the provisional or final admission letter to the postgraduate course, proof of identity (Aadhaar card, voter ID, passport, PAN card or driving licence), bank details, and two recent passport-size photographs. The 2026-27 guides also list the 14-digit NSP One Time Registration (OTR) number, Class 10, Class 12 and graduation mark sheets, first-year postgraduate admission proof or fee receipt, and a college identity card or bonafide student certificate, with an Aadhaar-seeded active bank account for payment. Keep all of these ready and follow the document list shown on the NSP application itself, since that list governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete One Time Registration (OTR) on the National Scholarship Portal at scholarships.gov.in — OTR is mandatory, and you will use the 14-digit OTR credentials to log in.</li>
        <li>Find the National Scholarship for Post Graduate Studies under the UGC schemes on NSP and open the 2026-27 application. The scheme opened on 16 September 2026.</li>
        <li>Fill in your personal, academic and current-institution details, including your admission roll or registration number and your bank account information, and upload the documents listed above.</li>
        <li>Submit before 31 October 2026, then follow up with your institute: institute verification runs to 15 November 2026 and district-level verification to 30 November 2026, and a defective application can be rectified to 15 November 2026. If your institute does not verify in time, payment stalls, so remind your institute nodal officer.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the scholarship worth?', '₹15,000 a month for 10 months a year, for two years — ₹1,50,000 a year, ₹3,00,000 in total.'),
   ('Who can apply?', 'First-year students of a regular, full-time postgraduate degree at a UGC-recognised institution, under 30 at admission, pursuing their first postgraduate degree.'),
   ('Can second-year postgraduate students apply?', 'No. Fresh applications are only for first-year students; second- and final-year students are not eligible for a fresh application.'),
   ('Can I apply if I already have a master’s degree?', 'No. The scheme applies only to a first postgraduate degree.'),
   ('What is the deadline for 2026-27?', '31 October 2026 for student applications on NSP. Institute verification runs to 15 November 2026 and district-level verification to 30 November 2026.'),
   ('Is there an income limit?', 'The UGC scholarship table checked gives no income limit, while a 2025 guide mentions below ₹8 lakh a year as expected. Check the current NSP scheme page if this matters to you.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against 2026-27 reporting (Matribhumisamachar: UGC, NSP, opened 16 September 2026, closes 31 October 2026, ₹1,50,000 a year as ₹15,000 a month for 10 months, 2-year tenure, 10,000 slots, first-year PG, first PG degree, regular full-time, AISHE code, under 30, verification to 15/30 November 2026; Biotecnika: same dates and figures; Careerindia: same 31 October 2026 deadline and first-year condition) and the UGC scholarship table (first-year full-time PG, no income limit, under 30, UGC-recognised institutions) and official-information summaries (documents from Class 9 onwards, admission letter, identity proof, bank details, two photographs). The income-limit disagreement is carried openly in the article.',
 'dl_long': '31 October 2026 (National Scholarship Portal; scheme opened 16 September 2026; institute verification to 15 November 2026)',
 'offlinks': [('National Scholarship Portal (NSP)', 'https://scholarships.gov.in'), ('Buddy4Study — National Scholarship for Post Graduate Studies', 'https://www.buddy4study.com/scholarship/national-scholarship-for-post-graduate-studies'), ('UGC National Scholarship for Post Graduate Studies 2026-27 (Matribhumisamachar)', 'https://matribhumisamachar.com/en/2026/09/21/ugc-national-scholarship-for-post-graduate-studies-2026-27-apply-online-for-%e2%82%b91-5-lakh-annual-aid/')],
 'related_titles': ['balmiki-2026', 'protsahan-2026', 'kalpana-2026', 'kindcircle-2026'],
})

# 4. Navgurukul Pune
ARTICLES.append({
 'slug': 'navgurukul-residential-programmes-pune',
 'title': 'Navgurukul Residential Programmes (Pune)',
 'meta': 'NavGurukul Residential Programmes in Pune: a fully funded 1 to 2 year residential programme in programming and other digital careers for youth from low-income families, with accommodation, meals and materials included and 100% placement assistance.',
 'short': 'Navgurukul Residential Programmes (Pune)',
 'kicker': 'Maharashtra · Fully Funded Residential Programme',
 'mono': 'NG',
 'prov_short': 'NavGurukul',
 'prov_cat': 'Non-profit · India',
 'h1': 'Navgurukul Residential Programmes (Pune)',
 'sub': 'NavGurukul’s residential programme in Pune is not a cash scholarship for a degree. It is a fully funded place to live and learn for one to two years: accommodation, meals and all learning materials are included, the learning is self-paced and peer-driven, and the programme ends with help into a job rather than a certificate alone. It is aimed at young people from underprivileged or low-income families who cannot afford expensive college education, and it asks for no prior degree — the current official criteria start at age 16, with no prior education required. Read the admission test and the campus-life conditions before anything else: this is a residential commitment, not a part-time course.',
 'dpill': 'Applications open (no fixed deadline published)',
 'facts': facts([
   ('Provider', 'NavGurukul, a not-for-profit founded in 2016 working with youth from marginalised communities'),
   ('Award', 'A fully funded residential programme lasting 1 to 2 years, including accommodation, meals and all learning materials; 100% assistance for securing a job on completion. The flagship programming course runs 18 months; placed alumni salaries are given as ₹2.4 lakh to ₹8.5 lakh a year across the programme'),
   ('Level', 'Residential career programme — youth above 16 from underprivileged or low-income families; no prior education required'),
   ('Deadline', 'No single deadline is published on the official residential-programmes page — applications are taken on a rolling basis, so check the official page for the next Pune cohort'),
   ('Eligibility', 'Youth above 16 from underprivileged or low-income communities who cannot afford expensive college education; family income below ₹15,000 a month in urban areas or ₹10,000 a month in rural areas; no prior education needed; some English is good to have; an interest in programming or the chosen field'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>NavGurukul was started in 2016 to make aspirational careers reachable for students from marginalised communities, and its residential programme is its flagship: a nationwide network of campuses where learners live, study and run the campus community together. The Pune campus is one of the programme’s locations, alongside Dantewada, Raipur, Himachal, Jashpur, Kishanganj, Dharamshala, Udaipur and Sarjapur. The organisation reports more than 1,500 students placed, with salaries in the ₹2.4 lakh to ₹8.5 lakh a year range, and more than 120 hiring partners.</p>
      <p>The programme’s education approach has three stated parts: it is residential and cost-free, lasting one to two years including accommodation, meals and all learning materials; it is peer-driven and self-paced, with students supporting each other in a community-led environment; and it is holistic, combining technical education with life skills, leadership and agency. Campuses are self-governed spaces managed by the students themselves through elected bodies, including cooking, health and hygiene, sports and field visits alongside study. The flagship School of Programming course at Pune and the other campuses is an 18-month, student-led, self-paced course covering front-end development (web and mobile development in JavaScript, React.js and Android), back-end development (Python, Node.js and JavaScript), soft skills (English speaking, teamwork, emotional intelligence and leadership) and hands-on clone projects for products such as WhatsApp and Facebook.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Full funding for the residential programme: accommodation, meals and all learning materials are included for one to two years, so the cost of living while learning is not charged to the student.</li>
        <li>An 18-month programming course (for the School of Programming track) with front-end and back-end development, soft skills and hands-on projects.</li>
        <li>100% assistance for securing a job in roles such as entry-level software developer, front-end developer, back-end developer, Python developer, JavaScript developer and testing and QA engineer.</li>
        <li>A self-paced, peer-driven learning community with student council participation, co-curricular activities, sports and field visits, rather than a lecture-only timetable.</li>
        <li>No tuition fee to pay upfront: the programme is described as fully funded and cost-free for the learner.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are above 16 years of age and from an underprivileged or low-income community, and you cannot afford expensive college education.</li>
        <li>No prior education is needed: the official page states that its students have been school and college dropouts, Class 10 or Class 12 pass students, and degree holders such as BSc or BTech graduates who could not get jobs.</li>
        <li>Your family income is below ₹15,000 a month in urban areas or ₹10,000 a month in rural areas, as stated on the official School of Programming page.</li>
        <li>Some level of English is good to have, and you have heard about programming or have an interest in making a career in the field.</li>
        <li>You can live residentially at the Pune campus for the programme’s duration and take part in its self-governed community life. This is a full-time, on-campus commitment, not a remote or part-time course.</li>
      </ul>
      <p>One older description of the residential programme says it is open to students who have finished Class 10 and are 17 years of age. That does not match the current official page, which gives above 16 with no prior education needed. This article follows the current official page; if you are 16 or have not finished Class 10, confirm your eligibility with NavGurukul before travelling.</p>
      <h2 id="documents">Documents required</h2>
      <p>No document checklist for the Pune residential programme is published on the official residential-programmes page checked, so none is invented here. The admission process is test- and interview-based rather than document-based, and the page directs applicants to enrol through its own process. Keep an identity proof, proof of your family-income situation and your previous education records (if any) ready, and follow whatever the application form asks for, since that form governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official NavGurukul residential-programmes page in full, including the Pune campus listing, the 1 to 2 year residential commitment and the self-governed campus life, and decide honestly whether living on campus fits your life.</li>
        <li>Start the enrolment process through the official NavGurukul page (the page’s “Want to Enroll” route) and choose the Pune campus.</li>
        <li>Take the screening test: it assesses fundamental skills up to Class 8 level in mathematics, logical reasoning and English. The test is 30 marks in total (mathematics 20, English 10), and the passing criteria are 14 marks in mathematics and 6 marks in English. It is offered online or offline, and students from any stream can take it.</li>
        <li>If you qualify, attend the academic interview, which evaluates Class 8 level mathematics and English in the same way as the screening test, and then the culture-fit round, which assesses cultural alignment, needs, emotional aspects and commitment to community. Candidates who do not pass the culture-fit round may be marked “In Preparation” and allowed a re-interview in 7 to 15 days.</li>
        <li>If you pass, you receive an offer letter confirming selection for the residential course, sent by email.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a scholarship that pays for my degree?', 'No. It is a fully funded residential career programme: you live on campus, learn for one to two years, and receive placement assistance. It does not pay university tuition for a degree.'),
   ('How much does it cost?', 'Nothing is charged to the learner for the programme itself: accommodation, meals and learning materials are included, and the programme is described as fully funded and cost-free.'),
   ('Do I need to have passed Class 10 or 12?', 'No, on the current official page: no prior education is needed, and students have included dropouts as well as degree holders. Older listings mention Class 10 and age 17 — confirm with NavGurukul if that affects you.'),
   ('Is there a deadline for the Pune campus?', 'No single deadline is published on the official residential-programmes page. Applications are taken on a rolling basis, so check the official page for the next Pune cohort.'),
   ('What jobs do graduates get?', 'The programme gives 100% assistance for entry-level software roles such as software developer, front-end and back-end developer, Python and JavaScript developer and testing/QA engineer, with placed alumni salaries reported at ₹2.4 lakh to ₹8.5 lakh a year.'),
   ('Is the Pune campus only for girls?', 'NavGurukul reports that seven of its eight campuses are girls-only, but the official page checked does not state that Pune specifically is girls-only, so no claim is made here — confirm the Pune campus’s current intake with NavGurukul.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the official NavGurukul residential-programmes page (navgurukul.org/residentialprograms: fully funded residential programmes in tech, business and finance; 1 to 2 years including accommodation, meals and materials; peer-driven and self-paced; 1,500+ placed at ₹2.4–8.5 lakh a year; 120+ hiring partners; School of Programming 18-month course with front-end, back-end, soft skills and clone projects; Pune among the programme locations; above 16, no prior education needed, urban ₹15,000/rural ₹10,000 family-income figures, some English good to have; screening test 30 marks with 14/6 pass marks, academic interview, culture-fit round with 7–15 day re-interview, offer letter by email) and the official School of Business page for the same admission process. No deadline is published on the official page and none is stated.',
 'dl_long': 'Applications open on a rolling basis — no single deadline published on the official page',
 'offlinks': [('NavGurukul — Residential Programs (official)', 'https://www.navgurukul.org/residentialprograms'), ('Buddy4Study — Navgurukul Residential Programmes (Pune)', 'https://www.buddy4study.com/scholarship/navgurukul-residential-programme-pune')],
 'related_titles': ['navgurukul-business-sarjapur', 'balmiki-2026', 'nsp-pg-2026', 'elf-sadhana'],
})

# 5. Navgurukul School of Business, Sarjapur
ARTICLES.append({
 'slug': 'navgurukul-school-of-business-residential-programme-sarjapur',
 'title': 'Navgurukul School of Business Residential Programme (Sarjapur)',
 'meta': 'NavGurukul School of Business at Sarjapur: a fully funded residential business course in Google Suite, CRM and Salesforce, digital marketing and data analytics for youth from low-income families, with 100% placement assistance.',
 'short': 'Navgurukul School of Business Residential Programme (Sarjapur)',
 'kicker': 'Karnataka · Fully Funded Residential Programme',
 'mono': 'NG',
 'prov_short': 'NavGurukul',
 'prov_cat': 'Non-profit · India',
 'h1': 'Navgurukul School of Business Residential Programme (Sarjapur)',
 'sub': 'NavGurukul’s School of Business at Sarjapur is the business track of the same fully funded residential model as its programming schools: young people from low-income families live on campus, learn digital business skills — Google Suite, customer relationship management, digital marketing and data analytics — and receive help into jobs such as CRM associate, Salesforce associate and operations associate. Like the other NavGurukul schools, it asks for no prior degree: the official criteria start at age 16, with no prior education required. Read the admission test and the residential commitment before anything else: this is a full-time, on-campus programme, not a short online course.',
 'dpill': 'Applications open (no fixed deadline published)',
 'facts': facts([
   ('Provider', 'NavGurukul, a not-for-profit founded in 2016 working with youth from marginalised communities'),
   ('Award', 'A fully funded residential business course, including accommodation, meals and learning materials, as part of NavGurukul’s 1 to 2 year residential programmes; 100% assistance for securing a job on completion'),
   ('Level', 'Residential career programme — youth above 16 from underprivileged or low-income families; no prior education required'),
   ('Deadline', 'No single deadline is published on the official NavGurukul pages — applications are taken on a rolling basis, so check the official page for the next Sarjapur cohort'),
   ('Eligibility', 'Youth above 16 from underprivileged or low-income communities who cannot afford expensive college education; family income below ₹15,000 a month in urban areas or ₹10,000 a month in rural areas; no prior education needed; some English is good to have; an interest in business and digital work'),
 ]),
 'body': '''<h2 id="about">About the programme</h2>
      <p>NavGurukul’s School of Business prepares students for a digital-first economy rather than for a traditional commerce degree. Its pitch is practical: employers hiring for customer-facing and operations roles need people who can run a spreadsheet, work a CRM system, build and promote a website, and read data — and those are exactly the four blocks the course teaches. The Sarjapur campus, in Bengaluru’s Sarjapur area, is one of the School of Business programme campuses, alongside Dantewada, Pune and Jashpur.</p>
      <p>Like all NavGurukul residential programmes, the School of Business is fully funded and residential: the programme lasts one to two years including accommodation, meals and all learning materials, the learning is student-led and self-paced, and students support each other in a community-led, self-governed campus environment. Across the residential programmes, NavGurukul reports more than 1,500 students placed, with salaries in the ₹2.4 lakh to ₹8.5 lakh a year range, and more than 120 hiring partners.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Full funding for the residential programme: accommodation, meals and learning materials are included, so the cost of living while learning is not charged to the student.</li>
        <li>A student-led, self-paced business course covering Google Suite (advanced Google Sheets, Slides and Forms), customer relationship management and Salesforce, digital marketing (website building, social media marketing and SEO) and data analytics (statistics, SQL queries and Tableau).</li>
        <li>100% assistance for securing jobs in roles such as customer relationship representative, CRM associate, Salesforce associate and operations associate.</li>
        <li>A peer-driven, self-governed campus community with life skills, leadership and agency built into daily life alongside the technical curriculum.</li>
        <li>No tuition fee to pay upfront: the programme is described as fully funded and cost-free for the learner.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You are above 16 years of age and from an underprivileged or low-income community, and you cannot afford expensive college education.</li>
        <li>No prior education is needed: the official page states that its students have been school and college dropouts, Class 10 or Class 12 pass students, and degree holders such as BSc or BTech graduates who could not get jobs.</li>
        <li>Your family income is below ₹15,000 a month in urban areas or ₹10,000 a month in rural areas, as stated on the official school pages.</li>
        <li>Some level of English is good to have, and you have an interest in business, digital work or a career in the field.</li>
        <li>You can live residentially at the Sarjapur campus for the programme’s duration and take part in its self-governed community life. This is a full-time, on-campus commitment, not a remote or part-time course.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>No document checklist for the Sarjapur School of Business programme is published on the official NavGurukul pages checked, so none is invented here. The admission process is test- and interview-based rather than document-based, and the pages direct applicants to enrol through the organisation’s own process. Keep an identity proof, proof of your family-income situation and your previous education records (if any) ready, and follow whatever the application form asks for, since that form governs the application.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Read the official NavGurukul School of Business and residential-programmes pages in full, including the Sarjapur campus listing and the residential commitment, and decide honestly whether living on campus fits your life.</li>
        <li>Start the enrolment process through the official NavGurukul page and choose the School of Business at Sarjapur.</li>
        <li>Take the screening test: it assesses fundamental skills up to Class 8 level in mathematics, logical reasoning and English. The test is 30 marks in total (mathematics 20, English 10), and the passing criteria are 14 marks in mathematics and 6 marks in English. It is offered online or offline, and students from any stream can take it.</li>
        <li>If you qualify, attend the academic interview, which evaluates Class 8 level mathematics and English in the same way as the screening test, and then the culture-fit round, which assesses cultural alignment, needs, emotional aspects and commitment to community. Candidates who do not pass the culture-fit round may be marked “In Preparation” and allowed a re-interview in 7 to 15 days.</li>
        <li>If you pass, you receive an offer letter confirming selection for the residential course, sent by email.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this a scholarship that pays for my degree?', 'No. It is a fully funded residential career programme: you live on campus, learn business and digital skills, and receive placement assistance. It does not pay university tuition for a degree.'),
   ('What exactly will I learn?', 'Google Suite (advanced Sheets, Slides and Forms), customer relationship management and Salesforce, digital marketing (website building, social media marketing and SEO) and data analytics (statistics, SQL queries and Tableau).'),
   ('What jobs do graduates get?', 'The school gives 100% assistance for roles such as customer relationship representative, CRM associate, Salesforce associate and operations associate.'),
   ('Do I need a commerce background or a degree?', 'No. No prior education is needed on the official criteria, and students have included dropouts as well as degree holders.'),
   ('Is there a deadline for the Sarjapur campus?', 'No single deadline is published on the official NavGurukul pages. Applications are taken on a rolling basis, so check the official page for the next Sarjapur cohort.'),
   ('How is this different from the Pune residential programme?', 'Pune is a campus offering NavGurukul’s residential programmes, with programming as its flagship track; Sarjapur’s School of Business is the business track, with its own curriculum in Google Suite, CRM, digital marketing and data analytics.'),
 ]),
 'verify': 'Verified 30 Oct 2026 against the official NavGurukul School of Business page (Google Suite, CRM and Salesforce, digital marketing including website building, social media marketing and SEO, data analytics including statistics, SQL and Tableau; job roles customer relationship representative, CRM associate, Salesforce associate and operations associate; campuses Dantewada, Pune, Jashpur and Sarjapur; above 16, no prior education needed, urban ₹15,000/rural ₹10,000 family-income figures; screening test 30 marks with 14/6 pass marks, academic interview, culture-fit round, offer letter) and the official residential-programmes page (fully funded 1 to 2 year residential programmes including accommodation, meals and materials; 1,500+ placed at ₹2.4–8.5 lakh a year; 120+ hiring partners). No deadline is published on the official pages and none is stated.',
 'dl_long': 'Applications open on a rolling basis — no single deadline published on the official pages',
 'offlinks': [('NavGurukul — Residential Programs (official)', 'https://www.navgurukul.org/residentialprograms'), ('Buddy4Study — Navgurukul School of Business Residential Programme (Sarjapur)', 'https://www.buddy4study.com/scholarship/navgurukul-school-of-business-residential-programme-sarjapur')],
 'related_titles': ['navgurukul-pune', 'balmiki-2026', 'nsp-pg-2026', 'elf-sadhana'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

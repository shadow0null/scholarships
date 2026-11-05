import sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = open('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read()
import pathlib
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles/')

NEW_CARDS = {
 'pm-vidyalaxmi': {'mono': 'PV', 'title': 'Prime Minister Vidyalaxmi Education Loan Scheme',
   'href': 'prime-minister-vidyalaxmi-education-loan-scheme.html',
   'dpill': 'Applications open (no fixed deadline published)',
   'award': 'Collateral-free, guarantor-free education loans with 3% interest subvention on loans up to Rs 10 lakh for family income up to Rs 8 lakh a year.',
   'elig': 'Merit-based admission to a top Quality Higher Education Institution; subvention for students not availing any other scholarship or interest subvention.',
   'tags': [('Education loan', 'blue'), ('Central Govt', 'teal')]},
 'ishan-uday-2026': {'mono': 'IU', 'title': 'NSP Ishan Uday Special Scholarship Scheme for NER 2026-27',
   'href': 'nsp-ishan-uday-special-scholarship-ner-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 5,400 a month for general degree courses and Rs 7,800 a month for technical, medical and paramedical courses; 10,000 fresh scholarships a year.',
   'elig': 'NER domicile, Class 12 passed from a school within the NER, first-year first UG degree at a UGC-recognised institution, parental income up to Rs 4.5 lakh.',
   'tags': [('North East', 'purple'), ('UGC / NSP', 'teal')]},
 'thakur-sen-negi-2026': {'mono': 'TS', 'title': 'NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27',
   'href': 'nsp-thakur-sen-negi-utkrisht-chatravriti-yojana-himachal-pradesh-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 11,000 a year for the top 100 tribal girls and top 100 tribal boys in the HP Board matric examination, on merit.',
   'elig': 'Tribal community students of Himachal Pradesh ranked in the HP Board of School Education matric result, studying at a recognised institution.',
   'tags': [('Himachal Pradesh', 'green'), ('NSP', 'teal')]},
 'swanath-2026': {'mono': 'SW', 'title': 'AICTE Swanath Scholarship Scheme 2026-27',
   'href': 'aicte-swanath-scholarship-scheme-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Rs 50,000 a year for degree or diploma students at AICTE-approved institutions; 2,000 scholarships (1,000 degree, 1,000 diploma).',
   'elig': 'Orphans, Covid-19 bereaved students, wards of martyred forces personnel, or students whose parent is critically ill or disabled; family income up to Rs 8 lakh.',
   'tags': [('Technical', 'blue'), ('AICTE / NSP', 'teal')]},
 'yasasvi-college-2026': {'mono': 'PY', 'title': 'PM YASASVI Top Class College Scholarship 2026-27',
   'href': 'pm-yasasvi-top-class-college-scholarship-2026-27.html',
   'dpill': 'Closes today (31 Oct 2026)',
   'award': 'Full tuition fee and non-refundable charges up to Rs 2,00,000 a year at public institutions, plus Rs 3,000 a month living expenses and other benefits.',
   'elig': 'OBC, EBC or DNT students with family income up to Rs 2.5 lakh, admitted to a full-time course at a notified Top Class institution.',
   'tags': [('OBC / EBC / DNT', 'purple'), ('Central Govt', 'teal')]},
}
cards = dict(REGISTRY)
cards.update(NEW_CARDS)

ARTICLES = []

# 1. Prime Minister Vidyalaxmi Education Loan Scheme
ARTICLES.append({
 'slug': 'prime-minister-vidyalaxmi-education-loan-scheme',
 'title': 'Prime Minister Vidyalaxmi Education Loan Scheme',
 'meta': 'Prime Minister Vidyalaxmi Education Loan Scheme: collateral-free, guarantor-free education loans for merit-based admission to top institutions, with 3% interest subvention on loans up to Rs 10 lakh for family income up to Rs 8 lakh a year. Apply on the PM Vidyalaxmi portal.',
 'short': 'Prime Minister Vidyalaxmi Education Loan Scheme',
 'kicker': 'Central Government · Education Loan',
 'mono': 'PV',
 'prov_short': 'Government of India',
 'prov_cat': 'Central Government · Education Loan',
 'h1': 'Prime Minister Vidyalaxmi Education Loan Scheme',
 'sub': 'The Prime Minister Vidyalaxmi scheme is not a cash scholarship: it is a loan scheme with an interest subsidy attached. If you win merit-based admission to one of the country\u2019s top Quality Higher Education Institutions but cannot offer collateral or a guarantor, the scheme lets you borrow without either, and — if your family income is up to Rs 8 lakh a year — the government pays 3% of the interest on loans up to Rs 10 lakh. Launched in November 2024 as a new central sector scheme, it runs through a single portal where one common loan application can go to up to three banks.',
 'dpill': 'Applications open (no fixed deadline published)',
 'facts': facts([
   ('Provider', 'Government of India (Ministry of Education), through the PM Vidyalaxmi portal'),
   ('Benefit', 'Collateral-free and guarantor-free education loans; 3% interest subvention on loans up to Rs 10 lakh for annual family income up to Rs 8 lakh'),
   ('Full subvention tier', 'Full interest subvention during the moratorium period for family income up to Rs 4.5 lakh, under the Central Sector Interest Subsidy (CSIS) component, on loans up to Rs 10 lakh'),
   ('Scale', 'Up to 1 lakh fresh students a year; outlay Rs 3,600 crore for 2024-25 to 2030-31, covering up to 7 lakh fresh students'),
   ('Eligibility', 'Merit-based admission to a top Quality Higher Education Institution (QHEI); the student must not be availing any other scholarship or interest subvention scheme'),
   ('Deadline', 'No fixed deadline published — the PM Vidyalaxmi portal is open for applications'),
 ]),
 'body': '''<h2 id="about">About the scheme</h2>
      <p>The scheme was launched in November 2024 to remove the two barriers that most often stop a good student from borrowing for higher education: the demand for property as security and the demand for a guarantor. Under Vidyalaxmi, a student admitted on merit to a top Quality Higher Education Institution can apply for an education loan that needs neither. The government portal, pmvidyalaxmi.co.in, has been operational since 25 February 2025, and from the launch on 6 November 2024 to 21 July 2026 a total of 1,12,817 collateral-free and guarantor-free loans were sanctioned under the scheme. That figure comes from the government\u2019s own release, and it is the clearest sign that the scheme is actively lending rather than merely announced.</p>
      <p>Two different subsidy layers sit on top of the loan, and they are easy to confuse. Students from families earning up to Rs 4.5 lakh a year receive full interest subvention during the moratorium period under the existing Central Sector Interest Subsidy component. Students from families earning between Rs 4.5 lakh and Rs 8 lakh a year receive a 3% interest subvention on loans up to Rs 10 lakh under Vidyalaxmi itself. The subvention is paid from the second year of the course and is subject to satisfactory academic performance, so keeping your grades up is part of keeping the subsidy.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>A collateral-free and guarantor-free education loan for a course at a top Quality Higher Education Institution.</li>
        <li>3% interest subvention on loans up to Rs 10 lakh for students whose annual family income is up to Rs 8 lakh.</li>
        <li>Full interest subvention during the moratorium for students whose annual family income is up to Rs 4.5 lakh, under the CSIS component.</li>
        <li>A 75% government credit guarantee on loans up to Rs 7.5 lakh, which is what lets banks lend without collateral.</li>
        <li>One Common Education Loan Application Form (CELAF) that can be sent to up to three banks, instead of a separate application for each bank.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You must have secured admission on merit to a top Quality Higher Education Institution (QHEI) identified by the Ministry of Education.</li>
        <li>For the 3% interest subvention, your annual family income must be up to Rs 8 lakh. Family here means the student plus father, mother and spouse where applicable.</li>
        <li>You must not be availing any other scholarship or interest subvention on the same loan — Vidyalaxmi subvention cannot be combined with CSIS on one loan.</li>
        <li>The subvention is limited to up to 1 lakh fresh students a year, and it is paid from the second year subject to satisfactory academic performance.</li>
      </ul>
      <p>One point needs honest flagging: sources disagree on how many institutions count as QHEIs, with figures of 860 and 1,441 both in circulation. This article therefore does not state a single count as fact. Check whether your institution is on the QHEI list on the PM Vidyalaxmi portal before you apply, since that list — not any article\u2019s number — decides eligibility.</p>
      <h2 id="conditions">Loan terms to know before you borrow</h2>
      <ul>
        <li>The moratorium period is the course period plus one year; repayment begins after that.</li>
        <li>Life insurance is mandatory for loans above Rs 7.5 lakh.</li>
        <li>Aadhaar-based de-duplication is used to stop the same student drawing the subsidy twice.</li>
        <li>This is a loan, not a grant: the principal remains repayable. Only the interest subsidy is free money, and only for as long as you meet the academic and income conditions.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: Aadhaar details of the student, income proof issued by an authorised public authority of the State Government, proof of merit-based admission to the QHEI course, and the bank\u2019s own loan documents. The portal and the lending bank\u2019s checklist govern the final list, so confirm it there before submitting.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Open the PM Vidyalaxmi portal and check that your institution is on the QHEI list and that you meet the income condition for the subvention.</li>
        <li>Fill in the Common Education Loan Application Form (CELAF) on the portal.</li>
        <li>Send the single application to up to three banks of your choice through the portal.</li>
        <li>Complete the chosen bank\u2019s verification and documentation, including Aadhaar-based de-duplication, and track the sanction on the portal.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is Vidyalaxmi a scholarship or a loan?', 'It is a loan scheme with an interest subsidy. You borrow the course cost and repay the principal; the government pays part or, for the lowest income tier during the moratorium, all of the interest.'),
   ('How much interest subsidy do I get?', '3% on loans up to Rs 10 lakh if your family income is up to Rs 8 lakh a year. If your family income is up to Rs 4.5 lakh, you get full interest subvention during the moratorium under the CSIS component instead.'),
   ('Do I need collateral or a guarantor?', 'No. Loans under the scheme are collateral-free and guarantor-free, backed by a 75% government credit guarantee on loans up to Rs 7.5 lakh.'),
   ('Can I combine this subsidy with another scholarship?', 'No. The subvention is for students not availing any other scholarship or interest subvention, and it cannot be combined with CSIS on the same loan.'),
   ('When does repayment start?', 'After the moratorium, which is the course period plus one year.'),
   ('Is there a deadline?', 'No fixed deadline is published in the sources checked. The portal is open for applications; apply once you hold merit-based admission to a QHEI.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Press Information Bureau release on the scheme (PRID 2290079: launched November 2024 as a new central sector scheme; 3% subvention on loans up to Rs 10 lakh for family income up to Rs 8 lakh; up to 1 lakh fresh students a year; Rs 3,600 crore outlay for 2024-25 to 2030-31 covering up to 7 lakh students; portal operational since 25 February 2025; 1,12,817 loans sanctioned from 6 November 2024 to 21 July 2026; Aadhaar-based de-duplication; subvention from the second year subject to satisfactory performance) and the Canara Bank PM Vidyalaxmi page (moratorium of course period plus one year; full moratorium subvention up to Rs 4.5 lakh income and 3% subvention for Rs 4.5-8 lakh on loans up to Rs 10 lakh; life insurance mandatory above Rs 7.5 lakh; Aadhaar details and State Government-authorised income proof; family definition). The 75% credit guarantee on loans up to Rs 7.5 lakh and the single CELAF to up to three banks are reported by scheme guides; the QHEI count is stated as disputed (860 versus 1,441) because sources conflict.',
 'dl_long': 'No fixed deadline published — the PM Vidyalaxmi portal is open for applications',
 'offlinks': [('PM Vidyalaxmi portal (official)', 'https://pmvidyalaxmi.co.in'), ('Press Information Bureau release (official)', 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2290079&reg=48&lang=2'), ('Canara Bank — Pradhan Mantri Vidyalaxmi Scheme', 'https://www.canarabank.bank.in/pages/pradhan-mantri-vidyalaxmi-scheme'), ('Buddy4Study — PM Vidyalaxmi Education Loan Scheme', 'https://www.buddy4study.com/scholarship/pm-vidyalakshmi-education-loan-scheme')],
 'related_titles': ['hdfc-ecss-2026-27', 'topclass-sc', 'nsp-pg-2026', 'pmss-railways'],
})

# 2. NSP Ishan Uday Special Scholarship Scheme for NER 2026-27
ARTICLES.append({
 'slug': 'nsp-ishan-uday-special-scholarship-ner-2026-27',
 'title': 'NSP Ishan Uday Special Scholarship Scheme for NER 2026-27',
 'meta': 'NSP Ishan Uday Special Scholarship Scheme for NER 2026-27: Rs 5,400 a month for general degree courses and Rs 7,800 a month for technical, medical and paramedical courses, for first-year undergraduates domiciled in the North Eastern Region. Applications close 31 Oct 2026 on the National Scholarship Portal.',
 'short': 'NSP Ishan Uday Special Scholarship Scheme for NER 2026-27',
 'kicker': 'North Eastern Region · UGC / NSP',
 'mono': 'IU',
 'prov_short': 'University Grants Commission (UGC)',
 'prov_cat': 'Central Government · NSP',
 'h1': 'NSP Ishan Uday Special Scholarship Scheme for NER 2026-27',
 'sub': 'Ishan Uday is the University Grants Commission\u2019s special scholarship for students from the North Eastern Region, paid through the National Scholarship Portal. It exists for one specific moment in a student\u2019s life: the first year of a first undergraduate degree. Ten thousand fresh scholarships are awarded every year, with a higher monthly rate for technical, medical and paramedical courses than for general degree courses. The 2026-27 window closes today, 31 October 2026, so a first-year student from the region who has not yet applied has hours, not weeks, left.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'University Grants Commission (UGC), through the National Scholarship Portal (NSP)'),
   ('Award', 'Rs 5,400 a month for general degree courses; Rs 7,800 a month for technical, medical and paramedical courses'),
   ('Scholarships', '10,000 fresh scholarships every year'),
   ('Deadline', '31 Oct 2026 — the 2026-27 window runs 16 Sep to 31 Oct 2026'),
   ('Eligibility', 'Domicile of a North Eastern Region state; Class 12 or equivalent passed from a school situated within the NER; admission to the first year of a first undergraduate degree at a UGC-recognised institution with a valid AISHE code; parental annual income up to Rs 4.5 lakh; full-time, regular mode only'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>Ishan Uday is a UGC scheme run on the National Scholarship Portal for students of the North Eastern Region. Its purpose is straightforward: to make sure that a student from the region who has just finished school and entered an undergraduate course is not forced out by cost in that first year. The award is a monthly scholarship rather than a one-time payment, and it continues through the degree subject to the scheme\u2019s renewal conditions. Ten thousand fresh scholarships are offered each year, which makes it one of the larger single-region schemes on the portal.</p>
      <p>Two amounts apply, and the distinction matters. A student in a general degree course receives Rs 5,400 a month. A student in a technical, medical or paramedical course receives Rs 7,800 a month. One scholarship tracker lists a flat Rs 8,000 a month instead; that figure is not used in this article because the Rs 5,400 / Rs 7,800 split is the one corroborated across the scheme listings checked, and the flat figure appears to be a tracker simplification.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Rs 5,400 a month for general degree courses, for the duration of the undergraduate course subject to renewal.</li>
        <li>Rs 7,800 a month for technical, medical and paramedical courses, on the same renewal basis.</li>
        <li>Payment through the National Scholarship Portal\u2019s direct benefit transfer system, once institute and higher-level verifications are complete.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You must be domiciled in a state of the North Eastern Region. The state lists in the sources checked name Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Sikkim and Tripura; confirm your state\u2019s coverage on the NSP scheme page if you are unsure.</li>
        <li>You must have passed Class 12 or an equivalent examination from a school situated within the North Eastern Region.</li>
        <li>You must have taken admission to the first year of a first undergraduate degree — general, technical or professional, including medical and paramedical courses, and including integrated courses — at an institution recognised by the UGC with a valid AISHE code.</li>
        <li>Your parents\u2019 annual income must be up to Rs 4.5 lakh.</li>
        <li>The course must be in full-time, regular mode. Distance, correspondence and part-time courses do not qualify.</li>
        <li>The scholarship is for first-year, first-degree students. Students already in later years, or already holding a degree, are outside its scope.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: domicile proof for the North Eastern Region, your Class 12 marksheet and certificate from a school within the region, proof of admission to the first year of the degree course, parental income certificate, Aadhaar details and Aadhaar-linked bank account details. The NSP application form and the scheme guidelines govern the final list, so confirm it there before submitting.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete your One-Time Registration (OTR) on the National Scholarship Portal, scholarships.gov.in, if you have not already done so.</li>
        <li>Open the Ishan Uday Special Scholarship Scheme for NER application for 2026-27 and fill in your personal, academic and bank details.</li>
        <li>Upload the domicile, Class 12, admission and income documents listed above and submit before the portal closes on 31 October 2026.</li>
        <li>Ask your institute to complete its verification by 15 November 2026, and follow up so that district, state and ministry verification is completed by 30 November 2026 — the general NSP verification pattern for the 2026-27 cycle.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the Ishan Uday scholarship?', 'Rs 5,400 a month for general degree courses and Rs 7,800 a month for technical, medical and paramedical courses. A flat Rs 8,000 figure on one tracker is not used here because the split rates are the corroborated ones.'),
   ('Who counts as a North Eastern Region student?', 'A student domiciled in an NER state who also passed Class 12 from a school situated within the region. Both conditions apply, not just one.'),
   ('Can a second-year student apply?', 'No. The scheme is for admission to the first year of a first undergraduate degree.'),
   ('Does the course have to be regular mode?', 'Yes. Only full-time, regular-mode courses at UGC-recognised institutions with a valid AISHE code qualify.'),
   ('What is the last date for 2026-27?', '31 October 2026. The window opened on 16 September 2026.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study Ishan Uday article (window 16 Sep to 31 Oct 2026; 10,000 fresh scholarships a year; Rs 5,400 a month general degree and Rs 7,800 a month technical/medical/paramedical; NER domicile plus Class 12 from a school within the NER; first-year first undergraduate degree at a UGC-recognised institution with valid AISHE code; parental income up to Rs 4.5 lakh; regular mode only) corroborated by NECareerHub, GovJobAssam and jobassam listings giving the same 31 Oct 2026 deadline and the same two monthly rates. The general NSP verification pattern (institute verification by 15 Nov 2026, district/state/ministry verification by 30 Nov 2026) is stated as the portal-wide pattern for 2026-27. The conflicting flat Rs 8,000 a month tracker figure is flagged in the article and not used.',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP window for 2026-27 runs 16 Sep to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — Ishan Uday Special Scholarship Scheme for NER', 'https://www.buddy4study.com/article/ishan-uday'), ('Buddy4Study — Ishan Uday scholarship listing', 'https://www.buddy4study.com/scholarship/special-scholarship-scheme-ishan-uday-for-ner')],
 'related_titles': ['nsp-pg-2026', 'topclass-sc', 'banishree', 'hdfc-ecss-2026-27'],
})

# 3. NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27
ARTICLES.append({
 'slug': 'nsp-thakur-sen-negi-utkrisht-chatravriti-yojana-himachal-pradesh-2026-27',
 'title': 'NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27',
 'meta': 'NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27: Rs 11,000 a year for the top 100 tribal girls and top 100 tribal boys in the HP Board matric examination, on merit. Applications close 31 Oct 2026 on the National Scholarship Portal.',
 'short': 'NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27',
 'kicker': 'Himachal Pradesh · NSP',
 'mono': 'TS',
 'prov_short': 'Department of Education, Himachal Pradesh',
 'prov_cat': 'State Government · NSP',
 'h1': 'NSP Thakur Sen Negi Utkrisht Chatravriti Yojana, Himachal Pradesh 2026-27',
 'sub': 'The Thakur Sen Negi Utkrisht Chatravriti Yojana is Himachal Pradesh\u2019s merit award for tribal students who top the state board\u2019s matric examination. It is narrow by design: exactly one hundred girls and one hundred boys from the tribal community, chosen strictly on their matric merit, receive Rs 11,000 a year. The award is applied for through the National Scholarship Portal, and the 2026-27 window closes today, 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Department of Education, Government of Himachal Pradesh, through the National Scholarship Portal (NSP)'),
   ('Award', 'Rs 11,000 per annum'),
   ('Recipients', 'Top 100 girls and top 100 boys belonging to the tribal community of Himachal Pradesh, as declared in the HP Board of School Education (Dharamshala) matric examination result, strictly on merit'),
   ('Institution', 'A recognised institution, within or outside Himachal Pradesh'),
   ('Renewal', 'Renewal in Class 12 or the second year of the course is contingent on satisfactory performance in the internal examinations of Class 11 or the first-year course'),
   ('Deadline', '31 Oct 2026 — the NSP window for 2026-27 runs 4 Jun to 31 Oct 2026'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>Utkrisht Chatravriti means, in plain terms, an excellence scholarship, and this one is tied to a single examination result. The Department of Education, Government of Himachal Pradesh, declares the top one hundred tribal girls and the top one hundred tribal boys from the Himachal Pradesh Board of School Education\u2019s matric examination, and those two hundred students receive Rs 11,000 a year. Because selection is strictly on matric merit, there is no separate entrance test and no income test stated in the sources checked: the board result itself is the selection list.</p>
      <p>The award is not limited to study inside Himachal Pradesh. A selected student may take it to a recognised institution outside the state as well, which matters for tribal students who move to another state for Classes 11 and 12 or for a first-year course.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Rs 11,000 a year, paid to the selected student through the scholarship system.</li>
        <li>Two hundred awards in total each cycle: one hundred for girls and one hundred for boys.</li>
        <li>Renewal into Class 12 or the second year of the course, subject to satisfactory performance in the internal examinations of Class 11 or the first-year course.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You must belong to the tribal community of Himachal Pradesh.</li>
        <li>You must be among the top 100 girls or top 100 boys of that community in the HP Board of School Education (Dharamshala) matric examination result, selected strictly on merit.</li>
        <li>You must be studying at a recognised institution, within or outside Himachal Pradesh.</li>
        <li>Renewal depends on satisfactory performance in your Class 11 or first-year internal examinations.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: your matric marksheet and certificate from the HP Board of School Education, tribal community certificate, proof of admission to your current recognised institution, Aadhaar details and Aadhaar-linked bank account details. The NSP application form governs the final list, so confirm it there before submitting.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete your One-Time Registration (OTR) on the National Scholarship Portal, scholarships.gov.in, if you have not already done so.</li>
        <li>Open the Thakur Sen Negi Utkrisht Chatravriti Yojana application for 2026-27 and fill in your personal, academic and bank details.</li>
        <li>Submit before the portal closes on 31 October 2026.</li>
        <li>Follow the route described for this scheme: applications are submitted through the Head of Institution, reviewed and forwarded to the Deputy Director of Education, and compiled district-wise to the Director of Higher Education. Check with your institution that your application has moved along that chain.</li>
      </ol>
      <p>One caution on dates: a scholarship directory page for this scheme also shows a stale date of 24 December 2025. That date belongs to an older listing, not to the 2026-27 cycle. The 2026-27 deadline used here — 31 October 2026 — comes from the Himachal Pradesh 2026-27 scholarship window and an institute notice confirming the NSP last date of 31 October 2026 for 2026-27.</p>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How many students get this scholarship?', 'Two hundred: the top 100 tribal girls and the top 100 tribal boys in the HP Board matric result.'),
   ('Is there an income limit?', 'No income test is stated in the sources checked. Selection is strictly on matric merit within the tribal community.'),
   ('Can I study outside Himachal Pradesh?', 'Yes. The award applies at a recognised institution within or outside the state.'),
   ('Does it renew?', 'Yes, into Class 12 or the second year, provided your performance in the Class 11 or first-year internal examinations is satisfactory.'),
   ('What is the last date for 2026-27?', '31 October 2026, through the National Scholarship Portal.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study Himachal Pradesh scholarships article (NSP window 4 Jun to 31 Oct 2026; Rs 11,000 per annum; top 100 girls and top 100 boys of the tribal community per the HP Board of School Education, Dharamshala, matric result, strictly on merit; recognised institution within or outside the state; renewal on satisfactory Class 11 / first-year internal performance), an ABVGIET institute notice confirming the NSP last date of 31 Oct 2026 for 2026-27, and the Notopedia scheme page for the Head-of-Institution to Deputy Director to Director of Higher Education procedure. The stale 24 Dec 2025 date on the Notopedia page is flagged in the article as an older listing, not the 2026-27 deadline.',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP window for 2026-27 runs 4 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — Himachal Pradesh Scholarships 2026-27', 'https://www.buddy4study.com/article/hp-scholarship'), ('Buddy4Study — Thakur Sen Negi Utkrisht Chatravriti Yojana', 'https://www.buddy4study.com/scholarship/thakur-sen-negi-utkrisht-chatravriti-yojana-himachal-pradesh')],
 'related_titles': ['nsp-pg-2026', 'topclass-sc', 'banishree', 'hdfc-ecss-2026-27'],
})

# 4. AICTE Swanath Scholarship Scheme 2026-27
ARTICLES.append({
 'slug': 'aicte-swanath-scholarship-scheme-2026-27',
 'title': 'AICTE Swanath Scholarship Scheme 2026-27',
 'meta': 'AICTE Swanath Scholarship Scheme 2026-27: Rs 50,000 a year for orphans, Covid-19 bereaved students, wards of martyred forces personnel and students whose parent is critically ill or disabled, studying degree or diploma courses at AICTE-approved institutions. Applications close 31 Oct 2026 on NSP.',
 'short': 'AICTE Swanath Scholarship Scheme 2026-27',
 'kicker': 'Technical Education · AICTE / NSP',
 'mono': 'SW',
 'prov_short': 'All India Council for Technical Education (AICTE)',
 'prov_cat': 'Central Government · NSP',
 'h1': 'AICTE Swanath Scholarship Scheme 2026-27',
 'sub': 'Swanath is the All India Council for Technical Education\u2019s scholarship for students who have faced extreme personal hardship: orphans, children who lost a parent to Covid-19, wards of forces personnel martyred in action, and students whose parent is critically ill or was left severely disabled by an accident. It pays Rs 50,000 a year to two thousand students in degree and diploma courses at AICTE-approved institutions, and it is applied for on the National Scholarship Portal. The 2026-27 window closes today, 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'All India Council for Technical Education (AICTE), Student Development Cell, through the National Scholarship Portal (NSP)'),
   ('Award', 'Rs 50,000 per annum, as a lump sum towards college fee, computer, stationery, books, equipment and software'),
   ('Scholarships', '2,000 every year — 1,000 for technical degree students and 1,000 for technical diploma students'),
   ('Duration', 'Up to 4 years for degree students and up to 3 years for diploma students; shorter for students already in later years (3, 2 or 1 year for 2nd, 3rd and 4th-year degree entrants)'),
   ('Deadline', '31 Oct 2026 — the NSP window runs 1 Jun to 31 Oct 2026'),
   ('Eligibility', 'One of the hardship categories below; annual family income up to Rs 8 lakh; degree or diploma course at an AICTE-approved institution in regular mode, in the 1st, 2nd, 3rd or 4th year; not a recipient of any other central, state or AICTE-sponsored scholarship'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>Swanath is run by the Student Development Cell of the All India Council for Technical Education, which works under the Ministry of Education. Its premise is that a student who has lost a parent, or whose parent can no longer work, should not also lose a technical education for want of money. The scholarship therefore targets hardship first and academics second: there is no published marks cut-off in the sources checked, but the hardship category and the income ceiling are strict.</p>
      <p>The award is a lump sum of Rs 50,000 a year, meant to cover the college fee and study costs — a computer, stationery, books, equipment and software. The scheme is explicit that no additional grant is payable in place of hostel charges or medical charges, so students who need hostel support must arrange that separately.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Rs 50,000 a year for every year of study, up to four years for degree students and up to three years for diploma students.</li>
        <li>Students entering in later years receive the award for their remaining years: three, two or one year for second, third and fourth-year degree entrants respectively, and correspondingly fewer years for later-year diploma entrants.</li>
        <li>Two thousand scholarships a year, split equally between degree and diploma students.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <p>You must fall under one of the following categories:</p>
      <ul>
        <li>Orphan.</li>
        <li>Either or both parents died due to Covid-19.</li>
        <li>Ward of Armed Forces or Central Paramilitary Forces personnel martyred in action (Shaheed).</li>
        <li>Parent suffering from a life-threatening disease such as cancer, or a parent who died or became critically disabled (above 80%) in an accident.</li>
      </ul>
      <p>In addition, all of the following must hold:</p>
      <ul>
        <li>Your family income from all sources is not more than Rs 8 lakh a year in the financial year of application, supported by a valid income certificate issued by the State or Union Territory government.</li>
        <li>You are studying in an AICTE-approved institution and course at degree or diploma level, in regular mode, in the 1st, 2nd, 3rd or 4th year.</li>
        <li>You are not already a recipient of any central government, state government or AICTE-sponsored scholarship, and you are not pursuing a postgraduate degree.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: proof of your hardship category (death certificate, Shaheed certificate, or medical and disability certificates as applicable), a valid income certificate from the State or Union Territory government, proof of admission to the AICTE-approved degree or diploma course, Aadhaar details and Aadhaar-linked bank account details. The NSP application form and the scheme guidelines govern the final list, so confirm it there before submitting.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete your One-Time Registration (OTR) on the National Scholarship Portal, scholarships.gov.in, if you have not already done so.</li>
        <li>Open the AICTE Swanath Scholarship Scheme application for 2026-27 and fill in your personal, academic and bank details.</li>
        <li>Upload the category, income and admission documents listed above and submit before the portal closes on 31 October 2026.</li>
        <li>Ask your institute to complete its verification by 15 November 2026, and follow up so that state nodal verification is completed by 30 November 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('How much is the Swanath scholarship?', 'Rs 50,000 a year, paid as a lump sum towards the college fee, a computer, stationery, books, equipment and software.'),
   ('Does it cover hostel charges?', 'No. The scheme states that no additional grant is payable in place of hostel or medical charges.'),
   ('Can a second, third or fourth-year student apply?', 'Yes. Degree and diploma students in the 1st to 4th year may apply; the award then runs for the remaining years of the course.'),
   ('Can I hold another government scholarship at the same time?', 'No. Recipients of any central, state or AICTE-sponsored scholarship are excluded.'),
   ('What is the income limit?', 'Rs 8 lakh a year from all sources, proved by a valid income certificate from the State or Union Territory government.'),
   ('What is the last date for 2026-27?', '31 October 2026, through the National Scholarship Portal.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study AICTE Swanath article (window 1 Jun to 31 Oct 2026; 2,000 scholarships, 1,000 degree and 1,000 diploma; Rs 50,000 a year; orphan, Covid-19 bereaved, martyr-ward and critically-ill or disabled-parent categories; income up to Rs 8 lakh; AICTE-approved degree or diploma in regular mode, 1st to 4th year; exclusion of other central/state/AICTE scholarship recipients), the AICTE Swanath guidelines summary (lump sum towards fee, computer, stationery, books, equipment and software; no hostel or medical grant; duration reduced for later-year entrants; last date 31 Oct 2026; NSP application) and the 2026-27 NSP verification pattern (institute verification by 15 Nov 2026, state nodal verification by 30 Nov 2026).',
 'dl_long': 'Closes today, 31 Oct 2026 — the NSP window runs 1 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — AICTE Swanath Scholarship Scheme 2026-27', 'https://www.buddy4study.com/article/aicte-swanath-scholarship-scheme'), ('AICTE Swanath guidelines summary', 'https://www.scholarshipsinindia.com/aicte-swanath-scholarship-scheme.html')],
 'related_titles': ['nsp-pg-2026', 'topclass-sc', 'hdfc-ecss-2026-27', 'pmss-railways'],
})

# 5. PM YASASVI Top Class College Scholarship 2026-27
ARTICLES.append({
 'slug': 'pm-yasasvi-top-class-college-scholarship-2026-27',
 'title': 'PM YASASVI Top Class College Scholarship 2026-27',
 'meta': 'PM YASASVI Top Class College Scholarship 2026-27: full tuition fee and non-refundable charges up to Rs 2,00,000 a year at public institutions, plus Rs 3,000 a month living expenses, for OBC, EBC and DNT students at notified Top Class institutions. Applications close 31 Oct 2026 on NSP.',
 'short': 'PM YASASVI Top Class College Scholarship 2026-27',
 'kicker': 'OBC / EBC / DNT · Ministry of Social Justice',
 'mono': 'PY',
 'prov_short': 'Ministry of Social Justice and Empowerment',
 'prov_cat': 'Central Government · NSP',
 'h1': 'PM YASASVI Top Class College Scholarship 2026-27',
 'sub': 'The PM Young Achievers Scholarship Award Scheme for Vibrant India — PM YASASVI — has two halves, and this article covers the college half only. It is a merit-based central sector scheme, funded entirely by the Ministry of Social Justice and Empowerment, for OBC, EBC and DNT students who win admission to a notified Top Class institution: an IIT, IIM, NIT, IIIT, AIIMS, NIFT, NID, National Law University or another notified central institution. The award reimburses the full tuition fee up to a ceiling, adds a monthly living allowance, and is limited to the slots allotted to each institution — so meeting the eligibility conditions is necessary but, on its own, not sufficient. The college window closes today, 31 October 2026.',
 'dpill': 'Closes today (31 Oct 2026)',
 'facts': facts([
   ('Provider', 'Ministry of Social Justice and Empowerment, Government of India, through the National Scholarship Portal (NSP)'),
   ('Award', 'Full tuition fee and non-refundable charges up to Rs 2,00,000 a year at public sector institutions (up to Rs 3,72,000 a year for private flying clubs for Commercial Pilot Training and Type Rating courses); monthly living expenses of Rs 3,000 and other benefits'),
   ('Other benefits', 'Scheme guides also list Rs 5,000 a year for books and stationery and laptop assistance up to Rs 45,000'),
   ('Deadline', '31 Oct 2026 — the college window runs 1 Jun to 31 Oct 2026'),
   ('Eligibility', 'Indian national belonging to the OBC, EBC or DNT category; admission to a full-time prescribed course at a notified Top Class institution under that institution\u2019s general selection criteria; annual parental or guardian income up to Rs 2,50,000 from all sources'),
   ('Selection', 'Inter-se merit within each institution, limited to the number of slots allotted to that institution'),
 ]),
 'body': '''<h2 id="about">About the scholarship</h2>
      <p>PM YASASVI is the umbrella name for two different schemes, and confusing them is the most common mistake applicants make. The school half covers Classes 9 to 12 at Top Class Schools and closed for 2026-27 on 31 August 2026. The college half — this article — covers students beyond Class 12 at Top Class institutions, and it closes on 31 October 2026. They share a name, a ministry and a portal, but they have different institutions, different awards and different deadlines. Apply under the college scheme only if you hold admission to a notified Top Class institution.</p>
      <p>The scheme is merit-based, not merely income-based. Admission itself must be won under the institution\u2019s own general selection or entrance criteria, and the scholarship is then awarded on an inter-se merit list within each institution, up to the slots allotted to it. A student who meets every eligibility condition but ranks below the institution\u2019s slot cut-off does not receive the award. That slot limit is the scheme\u2019s defining feature and the reason early application matters.</p>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Full reimbursement of tuition fees and non-refundable charges, up to Rs 2,00,000 a year at public sector institutions.</li>
        <li>Up to Rs 3,72,000 a year for private sector flying clubs, for Commercial Pilot Training and Type Rating courses only.</li>
        <li>Monthly living expenses of Rs 3,000.</li>
        <li>Scheme guides also list Rs 5,000 a year for books and stationery and laptop assistance up to Rs 45,000; confirm these two items against the current scheme guidelines on NSP before relying on them.</li>
      </ul>
      <h2 id="eligibility">Who can apply</h2>
      <ul>
        <li>You must be an Indian national.</li>
        <li>You must belong to the Other Backward Classes (OBC), Economically Backward Classes (EBC) or De-notified Tribes (DNT) category.</li>
        <li>You must have secured admission to a full-time prescribed course at a notified Top Class institution — such as an IIT, IIM, NIT, IIIT, AIIMS, NIFT, NID or National Law University — under the general selection criteria prescribed by that institution.</li>
        <li>Your parents\u2019 or guardian\u2019s annual income from all sources must be up to Rs 2,50,000.</li>
        <li>Selection is by inter-se merit within your institution, limited to its allotted slots. Eligibility alone does not guarantee an award.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <p>Keep ready: caste or category certificate for OBC, EBC or DNT status, parental or guardian income certificate, proof of admission to the full-time course at the notified institution, Class 12 marksheet and certificate, Aadhaar details and Aadhaar-linked bank account details. The NSP application form and the scheme guidelines govern the final list, so confirm it there before submitting.</p>
      <h2 id="how-to-apply">How to apply</h2>
      <ol>
        <li>Complete your One-Time Registration (OTR) on the National Scholarship Portal, scholarships.gov.in, if you have not already done so.</li>
        <li>Open the PM Yasasvi Central Sector Scheme of Top Class Education in College for OBC, EBC and DNT Students application for 2026-27.</li>
        <li>Fill in your personal, category, income and admission details, upload the documents listed above, and submit before the portal closes on 31 October 2026.</li>
        <li>Complete defective-application verification by 15 November 2026 if your form is flagged, and follow up so that district, state and ministry verification is completed by 30 November 2026.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>''' + faqs([
   ('Is this the same as the PM YASASVI school scholarship?', 'No. The school scheme covers Classes 9 to 12 at Top Class Schools and closed on 31 August 2026. This article covers the college scheme for students at notified Top Class institutions, which closes on 31 October 2026.'),
   ('Does meeting the eligibility conditions guarantee the scholarship?', 'No. Awards are limited to the slots allotted to each institution and are made on an inter-se merit list within the institution.'),
   ('How much of the fee is reimbursed?', 'The full tuition fee and non-refundable charges up to Rs 2,00,000 a year at public institutions, plus Rs 3,000 a month in living expenses and other benefits. Private flying clubs for pilot training have a higher ceiling of Rs 3,72,000 a year.'),
   ('What is the income limit?', 'Rs 2,50,000 a year from all sources, for parents or guardians.'),
   ('What is the last date for the college scheme in 2026-27?', '31 October 2026, through the National Scholarship Portal.'),
 ]),
 'verify': 'Verified 31 Oct 2026 against the Buddy4Study PM Yasasvi college scheme page (deadline 31 Oct 2026; Ministry of Social Justice and Empowerment; OBC/EBC/DNT; full-time course at a notified institution; income up to Rs 2,50,000; full tuition fee and non-refundable charges up to Rs 3,72,000 with other benefits; Rs 3,000 a month living expenses; ceiling of Rs 2,00,000 a year for public institutions and Rs 3,72,000 for private flying clubs for Commercial Pilot Training and Type Rating) corroborated by the college-scheme guide (window 1 Jun to 31 Oct 2026; inter-se merit within institution slots; defective verification by 15 Nov 2026; district/state/ministry verification by 30 Nov 2026) and scheme guides listing Rs 5,000 a year for books and stationery and laptop assistance up to Rs 45,000, which are stated as guide-listed rather than as confirmed guideline text. The school-track closure date of 31 Aug 2026 is reported by the same guide.',
 'dl_long': 'Closes today, 31 Oct 2026 — the college window runs 1 Jun to 31 Oct 2026',
 'offlinks': [('National Scholarship Portal (official)', 'https://scholarships.gov.in/'), ('Buddy4Study — PM Yasasvi Top Class Education in College', 'https://www.buddy4study.com/scholarship/pm-yasasvi-central-sector-scheme-of-top-class-education-in-college-for-obc-ebc-and-dnt-students'), ('PM YASASVI college scheme guide', 'https://calientjobs.com/pm-yasasvi-scholarship-for-college-students/')],
 'related_titles': ['topclass-sc', 'nsp-pg-2026', 'hdfc-ecss-2026-27', 'pmss-railways'],
})

for a in ARTICLES:
    n = build_article(BASE, OUT, a, cards)
    print(a['slug'], n)

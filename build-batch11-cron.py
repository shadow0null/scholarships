#!/usr/bin/env python3
"""Batch 11 (cron run 11): 5 verified international articles. Verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = dict(REGISTRY, **{
 'uiii': dict(mono='UIII', title="UIII Scholarships 2027 in Indonesia (Master's & PhD)", href='uiii-scholarships-2027-indonesia.html',
              dpill='166 days to go', award='Scheme-based tuition + living support', elig="Master's/PhD at UIII; 3.00+ GPA; IELTS 6.0+; open to international students.",
              tags=[("Master's/PhD",'blue'),('Indonesia','teal')]),
 'clarendon': dict(mono='O', title='Oxford Clarendon Scholarship 2027 (UK)', href='oxford-clarendon-scholarship-2027-uk.html',
              dpill='Dec 2026 – Jan 2027', award='Course fees + living grant', elig="New Master's/DPhil at Oxford; any subject, any nationality; automatic consideration.",
              tags=[("Master's/DPhil",'blue'),('UK','teal')]),
 'science-tokyo': dict(mono='ST', title='Science Tokyo MEXT Scholarship 2027 (Japan)', href='science-tokyo-mext-scholarship-2027-japan.html',
              dpill='37 days to go', award='¥147k–148k/month + tuition waiver + airfare', elig='IGP(A) Fall 2027 applicants; non-Japanese; supervisor consent by 15 Nov 2026.',
              tags=[("Master's/PhD",'blue'),('Japan','teal')]),
 'u-tokyo-mext': dict(mono='UT', title='University of Tokyo MEXT Scholarship 2027 (Japan)', href='university-of-tokyo-mext-scholarship-2027-japan.html',
              dpill='14 days to go', award='Tuition waiver + monthly stipend + airfare + housing', elig="New Master's/Doctoral at Graduate School of Science; Oct 2027 intake.",
              tags=[("Master's/PhD",'blue'),('Japan','teal')]),
 'yale-wf': dict(mono='Y', title='Yale World Fellows Program 2027 (USA)', href='yale-world-fellows-program-2027-usa.html',
              dpill='47 days to go', award='Stipend + apartment + insurance + travel', elig='Mid-career global leaders (5–25 yrs); non-US citizens; no full-time academics.',
              tags=[('Fellowship','blue'),('USA','teal')]),
})

ARTICLES = [
dict(
 slug='uiii-scholarships-2027-indonesia',
 title="UIII Scholarships 2027 in Indonesia (Master's & PhD) | StudyDesk Scholarships",
 meta="UIII scholarships 2027: Indonesia's international Islamic university offers scheme-based funding for Master's and PhD study. Admission closes 31 Mar 2027; scholarship applications run 22–29 Apr 2027.",
 short="UIII Scholarships 2027", kicker="Indonesia · Master's & PhD · Indonesian & international students",
 mono='UIII', prov_short='UIII', prov_long='Universitas Islam Internasional Indonesia, Depok (admission + scholarship office)',
 h1="Universitas Islam Internasional Indonesia Scholarships 2027",
 sub="An international Islamic university in Indonesia with scheme-based funding for Master's and PhD students — admission first, scholarship next.",
 dpill='166 days to go', dl_long='31 Mar 2027 (admission; scholarship applications 22–29 Apr 2027)',
 facts=facts([('Award','Scheme-based funding<small>Tuition support + living/academic allowances vary by scheme</small>'),
              ('Who can apply','Master’s & PhD applicants<small>Indonesian and international students</small>'),
              ('English bar','IELTS 6.0+ / TOEFL iBT 80<small>Higher for Law and PhD programmes</small>'),
              ('Admission deadline','31 Mar 2027<small>Scholarship window: 22–29 Apr 2027</small>'),
              ('Registration fee','USD 50 / IDR 750,000<small>Paid on the online admissions portal</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p><strong>Universitas Islam Internasional Indonesia (UIII)</strong> in Depok is Indonesia's purpose-built international Islamic university, teaching in English across six faculties. For the <strong>2027/2028 academic year</strong> (classes from September 2027) the university runs <strong>several scholarship schemes</strong> — including country-restricted awards such as the INSANI–Indonesian AID scheme — so the exact package depends on the scheme you are considered for. Support commonly spans <strong>tuition-fee assistance, monthly living allowances, accommodation-related support and research or academic allowances</strong>. The 2027 admission cycle opened on 23 September 2026 and is open now.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying for a <strong>Master's or PhD programme at UIII</strong> (six faculties: Islamic Studies, Social Sciences, Economics & Business, Education, Science & Technology, Law).</li>
        <li>Master's: an <strong>accredited Bachelor's degree</strong> with a <strong>GPA of at least 3.00/4.00</strong> (programme-specific requirements may be higher).</li>
        <li>PhD: a <strong>relevant Master's degree</strong> with a stronger GPA bar (e.g. 3.50/4.00 for PhD Islamic Studies).</li>
        <li><strong>English proficiency</strong> — Master's: TOEFL iBT 80 / ITP 525 / IELTS 6.0 / PTE 58; Law and dual-degree programmes ask for IELTS 6.5; PhD: TOEFL iBT 94 / ITP 550 / IELTS 6.5 / PTE 65. Certificates must be no older than two years.</li>
        <li>Open to <strong>Indonesian and international students</strong>.</li>
        <li>Note: <strong>admission and scholarship consideration are separate processes</strong> — you first secure admission, then apply for the scholarship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Tuition-fee assistance</strong> under the scholarship scheme awarded.</li>
        <li><strong>Monthly living allowance</strong> and accommodation-related support.</li>
        <li><strong>Research and academic allowances</strong> for conference and thesis work.</li>
        <li>Study at an <strong>English-medium international campus</strong> in Indonesia.</li>
        <li><strong>No published airfare or insurance guarantee:</strong> claims about flights or health insurance appear only on low-credibility trackers — do not count on them.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Degree certificate and academic transcript</li><li>English proficiency certificate</li><li>Curriculum vitae</li>
        <li>Two academic or professional reference contacts</li><li>Motivation letter</li>
        <li>PhD applicants additionally: <strong>research proposal + academic writing samples</strong></li><li>Passport or national ID</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Create an account on UIII's official admissions portal</strong>linked from uiii.ac.id — everything is submitted online.</li>
        <li><strong>Choose your degree level, faculty and study programme</strong>Check the programme-specific requirements first.</li>
        <li><strong>Upload all documents and pay the registration fee</strong>USD 50 for international applicants (IDR 750,000 for Indonesian applicants).</li>
        <li><strong>Submit by 31 March 2027</strong>This is the admission deadline. Letters of Acceptance are issued 19–22 April 2027.</li>
        <li><strong>Apply for the scholarship separately, 22–29 April 2027</strong>Scholarship results are announced on 30 April 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this fully funded?","Funding is scheme-dependent — tuition assistance plus living and academic allowances, but the exact package varies by scheme and stipend amounts are not published."),
 ("What is the actual deadline?","31 March 2027 is the admission deadline. Scholarship applications open only after acceptance letters, from 22 to 29 April 2027."),
 ("Do I need English test scores?","Yes — IELTS 6.0 / TOEFL iBT 80 for Master's (6.5/94 for PhD), with higher bars for Law programmes; certificates must be under two years old."),
 ("Can international students apply?","Yes — UIII admits both Indonesian and international students across its English-medium faculties."),
]),
 offlinks=[('Universitas Islam Internasional Indonesia — official site','https://uiii.ac.id/')],
 related_titles=['clarendon','science-tokyo','apu-adb'],
 verify='Verified 16 Oct 2026 via uiii.ac.id, opportunities365.com, scholarinfo.net and brightscholarship.com (31 Mar 2027 admission deadline; scholarship window 22–29 Apr 2027; scheme-dependent funding; stipend amounts not published).'),

dict(
 slug='oxford-clarendon-scholarship-2027-uk',
 title='Oxford University Clarendon Scholarship 2027 (UK) | StudyDesk Scholarships',
 meta="Clarendon Scholarship 2027 at Oxford: 200+ fully funded graduate scholarships covering fees and living costs. No separate application — apply for your course by its Dec 2026 / Jan 2027 deadline.",
 short='Clarendon Scholarship 2027', kicker='UK · Master’s & DPhil · Any subject, any nationality',
 mono='O', prov_short='University of Oxford', prov_long='University of Oxford (Clarendon Fund)',
 h1='Oxford University Clarendon Scholarship 2027 in the UK',
 sub='Over 200 fully funded graduate scholarships at Oxford — and there is no separate application. Your course application is your scholarship application.',
 dpill='Dec 2026 – Jan 2027', dl_long='Dec 2026 or Jan 2027 (your course deadline)',
 facts=facts([('Award','Fees + living grant<small>Fully funded for the period of fee liability</small>'),
              ('Scholarships','200+ new awards a year<small>All courses, all nationalities eligible</small>'),
              ('Application','Automatic consideration<small>No separate Clarendon form</small>'),
              ('Deadline','Dec 2026 or Jan 2027<small>Set by your chosen course — check it early</small>'),
              ('Selection','Academic merit & potential<small>Decided by subject experts</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Clarendon Fund</strong> is Oxford's flagship graduate scholarship scheme, awarding <strong>over 200 new scholarships each year</strong> to outstanding graduate applicants across <strong>every subject</strong>. Each award covers <strong>course fees plus a grant for living expenses</strong> for the period of fee liability. The defining feature of Clarendon is simplicity: <strong>there is no separate application</strong> — every applicant who applies for a graduate course by the relevant deadline is automatically considered.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Applying for a <strong>new full-time or part-time Master's or DPhil</strong> at the University of Oxford.</li>
        <li><strong>All courses are eligible</strong>; there are <strong>no restrictions on nationality, ordinary residence or field of study</strong>.</li>
        <li>Selection is on <strong>outstanding academic merit and potential</strong>, judged by experts in each subject.</li>
        <li>You must <strong>meet your chosen course's entry requirements</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full course fees</strong> covered for the fee-liability period.</li>
        <li><strong>Grant for living expenses</strong> alongside the fee cover.</li>
        <li>Access to the <strong>Clarendon scholars' community</strong> — events and networking across cohorts.</li>
        <li>Some awards are offered as <strong>Partnership Awards</strong> co-funded with colleges or departments.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>No Clarendon-specific documents — consideration is <strong>automatic with your course application</strong></li>
        <li>Your course application itself: transcripts, references, statement of purpose (per course)</li>
        <li>Written work where the course requires it</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your Oxford graduate course</strong>ox.ac.uk — check its specific application deadline.</li>
        <li><strong>Apply online by the course's December 2026 or January 2027 deadline</strong>Deadlines vary by course — December is common, January is the latest.</li>
        <li><strong>You are automatically considered</strong>Your department assesses applications and nominates the strongest candidates to the Clarendon Fund.</li>
        <li><strong>If offered, accept the funding</strong>The Clarendon Admin Team then arranges the package, potentially as a Partnership Award.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate Clarendon application?","No. Applying for your Oxford graduate course by its funding deadline is the entire application for Clarendon."),
 ("What is the deadline?","There is no single Clarendon deadline — each course sets its own, most in December 2026 or January 2027 for 2027-28 entry. Check your course."),
 ("Who can apply?","Anyone starting a new Master's or DPhil at Oxford — every subject, every nationality."),
 ("How much is the living grant?","Clarendon confirms fees plus a living grant for 2027-28; the exact figure for this cycle has not been published."),
]),
 offlinks=[('University of Oxford — Clarendon Fund','https://www.ox.ac.uk/clarendon'),('Oxford graduate admissions','https://www.ox.ac.uk/admissions/graduate')],
 related_titles=['zonta-ae','swiss-phd','nasa-hubble'],
 verify='Verified 16 Oct 2026 via ox.ac.uk/clarendon, scholars4dev.com, schresult.com and brightscholarship.com (automatic consideration by course deadline Dec 2026/Jan 2027; fees + living grant; 200+ awards; 2027-28 grant figure not published).'),

dict(
 slug='science-tokyo-mext-scholarship-2027-japan',
 title='Science Tokyo MEXT Scholarship 2027 in Japan | StudyDesk Scholarships',
 meta="MEXT University Recommendation scholarship at Institute of Science Tokyo (formerly Tokyo Tech) 2027: ¥147,000–148,000/month, tuition waived, airfare. Apply via IGP(A) by 22 Nov 2026.",
 short='Science Tokyo MEXT 2027', kicker='Japan · Master’s & PhD · Non-Japanese nationals',
 mono='ST', prov_short='Institute of Science Tokyo', prov_long='Institute of Science Tokyo (Science Tokyo), formerly Tokyo Institute of Technology',
 h1='Science Tokyo MEXT Scholarship 2027 in Japan',
 sub='Japan’s flagship government scholarship at the newly formed Institute of Science Tokyo — monthly stipend, tuition waived, airfare covered.',
 dpill='37 days to go', dl_long='22 Nov 2026, 23:59 JST',
 facts=facts([('Award','¥147,000–148,000/month<small>Master’s ¥147k / Doctoral ¥148k, tuition waived, airfare</small>'),
              ('Route','Via IGP(A) Fall 2027<small>MEXT route only from IGP(A) applicants</small>'),
              ('Supervisor consent','By 15 Nov 2026<small>Contact a professor early</small>'),
              ('Deadline','22 Nov 2026, 23:59 JST<small>Fall 2027 enrolment</small>'),
              ('Extension','Possible into PhD<small>GPA ≥ 2.50 + MEXT approval</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Japanese Government (MEXT) Scholarship via University Recommendation</strong> at the <strong>Institute of Science Tokyo (Science Tokyo)</strong> — the university formed by the 2024 merger of Tokyo Institute of Technology and Tokyo Medical and Dental University — funds international students on the <strong>International Graduate Program (A) for Fall 2027 entry</strong>. Programmes are taught <strong>in English</strong>; no Japanese is required. The 2027 cycle is announced and open now, and the university's official MEXT page was updated on 4 September 2026 specifically for applicants commencing in fall 2027.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>An applicant for <strong>IGP(A) Fall 2027</strong> at Science Tokyo — the MEXT route is drawn only from IGP(A) applicants, so you apply for admission and opt into the scholarship.</li>
        <li><strong>Non-Japanese nationals</strong> only; study is in English.</li>
        <li>Academic standing per the year's MEXT notice (the standard MEXT bar of around <strong>2.30 GPA</strong> applies).</li>
        <li>A <strong>supervisor consent letter</strong> secured by <strong>15 November 2026</strong>.</li>
        <li>Cannot be combined with certain <strong>other Japanese-government scholarships</strong>.</li>
        <li>Check the official <strong>allocation file</strong> — not every IGP(A) programme has MEXT slots, and over 75% of nominees must come from MEXT-designated countries.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend:</strong> ¥147,000 (Master's) / ¥148,000 (Doctoral).</li>
        <li><strong>Enrolment fee and tuition waived</strong> by Science Tokyo; the application (entrance-exam) fee is reimbursed if MEXT allocates you to the university.</li>
        <li><strong>Economy air tickets</strong> to and from Japan under MEXT conditions.</li>
        <li>Initial <strong>two years</strong> of the Master's programme, with possible extension into the Doctoral stage (GPA ≥ 2.50 and MEXT approval required — not automatic).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>IGP(A) admission application via the <strong>online system</strong></li><li>Tentative <strong>MEXT application form</strong> (official format published after the IGP(A) deadline — a re-submission may be needed)</li>
        <li><strong>Recommendation letter from the dean</strong> of your home university, addressed to the President of Institute of Science Tokyo (dean-signed; a department head's signature is not accepted)</li><li>English proficiency evidence (IELTS / TOEFL iBT / TOEIC within 2 years, or proof of English-medium prior degree)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure a supervisor's consent letter</strong>Contact a prospective Science Tokyo supervisor early — the consent letter deadline is 15 November 2026.</li>
        <li><strong>Submit the IGP(A) Fall 2027 application online</strong>by 22 November 2026, 23:59 JST.</li>
        <li><strong>Submit the MEXT materials</strong>tentative form, dean's letter and English proof — through the separate scholarship form.</li>
        <li><strong>Wait for screening</strong>Science Tokyo screens Dec–Feb; admission decision and MEXT recommendation go out in early March 2027; MEXT's final awards are announced July–August 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this the same as Tokyo Tech?","Yes — Tokyo Institute of Technology merged with Tokyo Medical and Dental University in 2024 to form the Institute of Science Tokyo (Science Tokyo)."),
 ("Can I apply for the scholarship without IGP(A)?","No — the MEXT route here is only for IGP(A) Fall 2027 admission applicants."),
 ("Does nomination guarantee the scholarship?","No — Science Tokyo's recommendation is not a guarantee; MEXT makes the final decision and can reject nominees close to enrolment."),
 ("Is Japanese required?","No — IGP(A) programmes are taught in English."),
]),
 offlinks=[('Institute of Science Tokyo — MEXT scholarship (official)','https://www.titech.ac.jp/english/international-student-exchange/prospective-students/scholarships/mext-university-general'),('IGP(A) admissions — official','https://www.titech.ac.jp/english/admissions/prospective-students/graduate-programs/igp-a')],
 related_titles=['u-tokyo-mext','honjo','apu-adb'],
 verify='Verified 16 Oct 2026 via titech.ac.jp (official MEXT page updated 4 Sep 2026 for fall 2027) and brightscholarship.com (22 Nov 2026 deadline; ¥147,000/¥148,000 stipends; Science Tokyo = former Tokyo Tech; University Recommendation (General) suspended).'),

dict(
 slug='university-of-tokyo-mext-scholarship-2027-japan',
 title='University of Tokyo MEXT Scholarship 2027 in Japan | StudyDesk Scholarships',
 meta="MEXT University Recommendation scholarship at the University of Tokyo's Graduate School of Science 2027: tuition waived, monthly stipend, airfare, guaranteed first-year housing. Deadline 30 Oct 2026.",
 short='UTokyo MEXT 2027', kicker='Japan · Master’s & Doctoral · Graduate School of Science',
 mono='UT', prov_short='University of Tokyo', prov_long='University of Tokyo, Graduate School of Science (MEXT University Recommendation)',
 h1='University of Tokyo MEXT Scholarship 2027 in Japan',
 sub='The Japanese government scholarship at Japan’s top university — tuition waived, monthly stipend, airfare and guaranteed first-year housing. This round may be the last.',
 dpill='14 days to go', dl_long='30 Oct 2026 (Graduate School of Science)',
 facts=facts([('Award','Tuition waiver + stipend<small>Airfare + guaranteed first-year housing</small>'),
              ('Who can apply','New Master’s/Doctoral students<small>Graduate School of Science, Oct 2027 intake</small>'),
              ('GPA bar','2.30+ on the MEXT scale<small>Born on or after 2 Apr 1992</small>'),
              ('Language','English CEFR B2+ or JLPT N2+<small>Or English-medium prior degree</small>'),
              ('Deadline','30 Oct 2026<small>Graduate School of Science only</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Japanese Government (MEXT) Scholarship via University Recommendation</strong> at the <strong>University of Tokyo's Graduate School of Science</strong> funds international students entering as <strong>new Master's or Doctoral students in October 2027</strong>. The award exempts tuition, pays a monthly stipend, covers economy airfare, and guarantees <strong>first-year accommodation in a UTokyo International Lodge</strong>. The 2027 cycle is announced — the school's official page was updated on 8 October 2026 — but UTokyo also flags that MEXT has signalled the <strong>University Recommendation (General Category) may be discontinued from AY2027</strong>: this round may be the last of its kind, so apply now.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Entering October 2027 as a <strong>new Master's or Doctoral student</strong> at the Graduate School of Science, having completed the school's admission application (Special Selection for International Applicants).</li>
        <li>A national of a <strong>country with diplomatic relations with Japan</strong>; Japanese nationals are ineligible (dual nationals only if renouncing Japanese nationality before arrival).</li>
        <li><strong>Born on or after 2 April 1992</strong>; GPA of <strong>2.30+</strong> on the MEXT scale.</li>
        <li>Field of study <strong>related to prior university study</strong> and researchable at UTokyo.</li>
        <li>Language: English at <strong>CEFR B2+</strong> (e.g. TOEFL iBT 72+, IELTS 5.5+), prior English-medium education, or <strong>JLPT N2+</strong>.</li>
        <li><strong>Not residing in Japan</strong> at application; not applying for any other AY2027 MEXT programme; no concurrent Japanese-government scholarship.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend</strong> — AY2027 amounts not yet fixed; as a reference the official page quotes AY2026 figures of ¥144,000 (Master's) / ¥145,000 (Doctoral), plus small regional top-ups.</li>
        <li><strong>Enrolment and tuition fees exempted.</strong></li>
        <li><strong>Economy-class airfare</strong> to Japan on arrival and back on completion (under MEXT route rules; domestic travel, taxes, insurance and baggage are the recipient's).</li>
        <li><strong>Guaranteed first-year room</strong> in a UTokyo International Lodge (~¥50,000/month Kashiwa, ~¥70,000/month Komaba).</li>
        <li>Period: Master's <strong>Oct 2027 – Sep 2029</strong>; Doctoral <strong>Oct 2027 – Sep 2030</strong>; extension only via rigorous MEXT examination.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>MEXT application form (double-sided print)</li><li>Field of Study and Research Plan</li>
        <li><strong>Recommendation letter from the dean or above</strong>, addressed to the President of the University of Tokyo, on university letterhead, <strong>wet-signed</strong> (no digital signatures)</li><li>Passport photo (4.5 × 3.5 cm, within 6 months)</li>
        <li>Official transcripts of the last degree and current programme, plus a grading-system explanation if it is not on the transcript</li><li>Language-ability proof (test score or medium-of-instruction certificate)</li><li>Graduation-thesis abstract, official (expected) graduation statement, passport copy</li>
        <li>All documents in English or Japanese (other languages need Japanese translation); A4, double-sided</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Complete the admission application</strong>Graduate School of Science Special Selection for International Applicants, and identify a prospective supervisor.</li>
        <li><strong>Upload all MEXT documents as PDFs</strong>via the school's designated online form before 30 October 2026 — email submissions are not accepted.</li>
        <li><strong>Confirm the automated confirmation email</strong></li>
        <li><strong>Wait for results</strong>School nominees notified mid-Feb 2027; university selection April 2027; final MEXT decision announced to grantees June 2027 (tentative).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is 30 October the whole university's deadline?","No — this is the Graduate School of Science's window. Other UTokyo graduate schools set their own dates."),
 ("Why might this be the last round?","UTokyo notes MEXT has signalled the University Recommendation (General Category) is expected to be discontinued from AY2027."),
 ("Does nomination mean I have the scholarship?","No — school and university nomination is not an award; MEXT makes the final decision."),
 ("Are the stipend figures final for 2027?","No — AY2027 amounts were not yet fixed when the official page was updated; the figures quoted are the AY2026 reference amounts."),
]),
 offlinks=[('UTokyo Graduate School of Science — MEXT scholarship (official)','https://www.s.u-tokyo.ac.jp/en/admission/scholarship.html'),('Special Selection for International Applicants — official','https://www.eps.s.u-tokyo.ac.jp/en/graduateadmission_en/international_applicants_en/')],
 related_titles=['science-tokyo','honjo','apu-adb'],
 verify='Verified 16 Oct 2026 via s.u-tokyo.ac.jp (official MEXT page updated 8 Oct 2026) and brightscholarship.com (30 Oct 2026 deadline; Graduate School of Science only; possibly the final University Recommendation round).'),

dict(
 slug='yale-world-fellows-program-2027-usa',
 title='Yale World Fellows Program 2027 in the USA | StudyDesk Scholarships',
 meta="Yale World Fellows 2027: a fully funded 4-month leadership fellowship at Yale for mid-career global leaders. Stipend, furnished apartment, insurance, travel. Deadline 2 Dec 2026, 2:00 PM ET.",
 short='Yale World Fellows 2027', kicker='USA · Leadership fellowship · Mid-career professionals',
 mono='Y', prov_short='Yale University', prov_long='Yale University — Maurice R. Greenberg World Fellows Program',
 h1='Yale World Fellows Program 2027 in the USA',
 sub='Four fully funded months at Yale for emerging global leaders — stipend, furnished apartment, insurance and travel. Not a degree: a leadership residency.',
 dpill='47 days to go', dl_long='2 Dec 2026, 2:00 PM ET',
 facts=facts([('Award','Fully funded residency<small>Stipend + furnished apartment + insurance + travel</small>'),
              ('Duration','Mid-Aug to mid-Dec 2027<small>4 months in New Haven, full-time</small>'),
              ('Who can apply','Mid-career leaders<small>5–25 yrs into career; non-US citizens</small>'),
              ('Fee','US$20 application fee<small>No nomination needed</small>'),
              ('Deadline','2 Dec 2026, 2:00 PM ET<small>Decisions emailed by end of April</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Maurice R. Greenberg World Fellows Program</strong> at <strong>Yale University</strong> brings a cohort of accomplished, mid-career professionals from around the world to New Haven for <strong>four months of full-time study, reflection and leadership development</strong> (mid-August to mid-December 2027). Fellows join seminars, take courses, mentor students and build a global network — but this is <strong>not a degree</strong>: there is no Yale degree, academic credit or transcript. The 2027 cycle is <strong>announced and open now</strong> on the official site, with thousands of applications expected.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Between 5 and 25 years</strong> into a professional career, with significant accomplishments at regional, national or international level.</li>
        <li><strong>Citizen of a country other than the United States</strong>; dual US citizens are eligible, but preference goes to candidates whose work is focused outside the US.</li>
        <li><strong>Fluent in English</strong> (no TOEFL/IELTS required; fluency is assessed in later interview rounds).</li>
        <li><strong>No full-time students and no full-time academics</strong> — the fellowship is for practitioners, not researchers.</li>
        <li>Must <strong>reside in New Haven for the entire period</strong> and commit to full-time participation.</li>
        <li>No minimum or maximum age (average fellow age is 39); selection is <strong>highly competitive</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Taxable stipend</strong> to cover living costs in New Haven (the amount is not published on the official site).</li>
        <li><strong>Modest furnished one- or two-bedroom apartment</strong> for the programme duration.</li>
        <li><strong>Medical insurance</strong> and <strong>round-trip travel</strong> from the home country.</li>
        <li>Four months of Yale seminars, courses, mentoring and a <strong>lifelong global fellows network</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li><strong>Résumé/CV</strong> — maximum 3 pages</li><li><strong>Personal statement</strong> — maximum 600 words</li><li><strong>Three letters of recommendation</strong></li>
        <li><strong>Brief video statement</strong> — recorded inside the application platform (Chrome or Firefox only; one re-record allowed)</li><li><strong>US$20 application fee</strong></li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Review eligibility on worldfellows.yale.edu</strong>Make sure you meet the 5–25 year career window and residency commitment.</li>
        <li><strong>Create an account on the official application portal</strong>apply.worldfellows.yale.edu — name/email and a PIN flow.</li>
        <li><strong>Complete the online form and uploads</strong>CV, personal statement and the in-platform video; request recommendations through the portal.</li>
        <li><strong>Pay the US$20 fee and submit</strong>before 2 December 2026, 2:00 PM Eastern Time. No nomination is needed; re-applicants must submit a fully new application.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Do I get a Yale degree?","No — World Fellows is a non-degree leadership residency: no degree, academic credit or transcript."),
 ("Can academics apply?","No — full-time students and full-time academics are not eligible; it is designed for practitioners."),
 ("How much is the stipend?","The official site does not publish a figure, so no amount should be quoted — it covers living costs in New Haven."),
 ("When are decisions announced?","Final decisions are emailed by the end of April."),
]),
 offlinks=[('Yale World Fellows — official site','https://worldfellows.yale.edu/'),('World Fellows application portal','https://apply.worldfellows.yale.edu')],
 related_titles=['nasa-hubble','bloomberg-harvard','wb-gaf'],
 verify='Verified 16 Oct 2026 via worldfellows.yale.edu, opportunitydesk.org, opportunitiesfeed.com and brightscholarship.com (2027 cycle open; deadline 2 Dec 2026 2:00 PM ET; stipend amount unpublished; non-degree fellowship).'),
]

for a in ARTICLES:
    n = build_article(BASE, OUT, a, CARDINFO)
    print('wrote', a['slug'], n, 'bytes')

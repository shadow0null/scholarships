#!/usr/bin/env python3
"""Batch 11 (Group D): 10 verified articles. Verified 16 Oct 2026."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'ieg-mainz': dict(mono='IEG', title='IEG Mainz PhD Fellowship 2027 in Germany', href='ieg-mainz-phd-fellowship-2027.html',
              dpill='122 days to go', award='€1,650/month', elig='PhD researchers; European history; enrolled & supervised at home university.',
              tags=[('PhD','blue'),('Germany','teal')]),
 'jj-wbgsp': dict(mono='WB', title='Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP) 2027', href='joint-japan-world-bank-graduate-scholarship-2027.html',
              dpill='133 days to go', award='Tuition + stipend + airfare', elig='Developing-country nationals; 3 yrs work experience; admitted to participating program.',
              tags=[("Master's",'blue'),('International','teal')]),
 'jispa-phd': dict(mono='IMF', title='Japan-IMF JISPA PhD Scholarships 2027 in Japan', href='japan-imf-jispa-phd-scholarships-2027.html',
              dpill='228 days to go', award='Tuition + stipend + airfare', elig='Asia-Pacific government officials; economics PhD in Japan.',
              tags=[('PhD','blue'),('Japan','teal')]),
 'flex-global': dict(mono='FLEX', title='FLEX Global Abroad Exchange Program 2027-28', href='flex-global-abroad-exchange-program-2027-28.html',
              dpill='45 days to go', award='Fully funded (airfare, host family, stipend)', elig='U.S. citizens; grades 9–12; ages 15–18.5. For study ABROAD.',
              tags=[('Exchange','blue'),('USA','teal')]),
 'lille-eiffel': dict(mono='EF', title='France Excellence Eiffel Scholarship 2027 via University of Lille', href='lille-eiffel-phd-scholarship-2027.html',
              dpill='28 days to go', award='€2,100/month (PhD)', elig='International PhD; nominated by Lille; cotutelle/co-supervision.',
              tags=[('PhD','blue'),('France','teal')]),
 'clara-collet': dict(mono='CC', title='Clara Collet PhD Scholarship 2027, UCL (UK)', href='clara-collet-phd-scholarship-2027-ucl.html',
              dpill='55 days to go', award='Full fees + £23,805 stipend', elig="Master's holders; social sciences PhD at UCL.",
              tags=[('PhD','blue'),('UK','teal')]),
 'lincoln-gl': dict(mono='L', title='University of Lincoln Global Leaders Scholarship 2027', href='lincoln-global-leaders-scholarship-2027.html',
              dpill='31 days to go', award='50% tuition (1 year)', elig='International UG/PG taught; offer required; competitive.',
              tags=[('UG/PG','blue'),('UK','teal')]),
 'awc': dict(mono='AWC', title='America in the World Consortium Fellowships 2027-28', href='america-world-consortium-fellowships-2027-28.html',
              dpill='46 days to go', award='$73,500 stipend (postdoc)', elig='PhD candidates / recent PhDs; U.S. foreign policy research.',
              tags=[('Fellowship','blue'),('USA','teal')]),
 'dayton-merit': dict(mono='UD', title='University of Dayton Merit Scholarship 2027 (USA)', href='dayton-merit-scholarship-2027.html',
              dpill='16 days to go', award='Up to $30,000/year', elig='International UG; automatic with admission.',
              tags=[('UG','blue'),('USA','teal')]),
 'perugia-phd': dict(mono='UP', title='University of Perugia PhD Scholarships 2026/27 (Italy)', href='perugia-phd-scholarships-2026-27.html',
              dpill='12 days to go', award='Funded PhD positions (31)', elig="Master's holders; PICA application; €20 fee.",
              tags=[('PhD','blue'),('Italy','teal')]),
}

ARTICLES = [
dict(
 slug='ieg-mainz-phd-fellowship-2027',
 title='IEG Mainz PhD Fellowship 2027 in Germany (€1,650/month) | StudyDesk Scholarships',
 meta='IEG Mainz PhD Fellowship 2027: €1,650/month for 6–12 months at the Leibniz Institute of European History. European history PhD researchers. Deadline 15 Feb 2027.',
 short='IEG Mainz PhD Fellowship', kicker='Germany · PhD · International',
 mono='IEG', prov_short='Leibniz Institute of European History', prov_long='Leibniz Institute of European History (IEG), Mainz',
 h1='IEG Mainz PhD Fellowship 2027 in Germany',
 sub='€1,650 a month for 6–12 months in Mainz — to finish your PhD in European history.',
 dpill='122 days to go', dl_long='15 Feb 2027',
 facts=facts([('Award','€1,650 / month<small>6–12 months; family allowances</small>'),
              ('Who can apply','PhD researchers<small>European history; enrolled at home university</small>'),
              ('Stage','Dissertation completion<small>Not for starting research</small>'),
              ('Deadline','15 Feb 2027<small>Confirm on IEG portal</small>'),
              ('Residence','Mainz, full-time<small>Weekly colloquia + presentation</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>Leibniz Institute of European History (IEG)</strong> in Mainz awards residential fellowships to <strong>doctoral researchers working on European history</strong> — from the early modern period to contemporary history — and historically oriented disciplines such as religious history, intellectual history, environmental history, and digital humanities. The fellowship supports the <strong>writing and completion stage of the dissertation</strong>: a 6- to 12-month stay in Mainz to finish your thesis with mentoring, library access, and a research community around you.</p>
      <div class="honest-note"><strong>What it is not:</strong> the fellowship does not fund the start of a research project, language courses, or the revision of a finished dissertation into a book. Your source research should already be well advanced.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Enrolled <strong>PhD researcher</strong> (international or German) working on <strong>European history or a historically oriented discipline</strong>.</li>
        <li>Remain <strong>enrolled and supervised at your home university</strong> during the stay — IEG does not award the degree.</li>
        <li>Normally <strong>no more than three years</strong> into the dissertation by the deadline (justified exceptions possible).</li>
        <li>A <strong>mature dissertation concept</strong> that would benefit from a 6–12 month writing period.</li>
        <li>Proficiency in <strong>English</strong> expected.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Monthly stipend of €1,650</strong>.</li>
        <li><strong>Family allowance:</strong> €250 (partner), €400 (first child), €100 (each additional child).</li>
        <li><strong>Mentoring</strong> from IEG researchers, plus institute <strong>workspace and library</strong>.</li>
        <li>Affordable room in the institute's residence, <strong>subject to availability</strong>.</li>
        <li>Fellows live in Mainz full-time, join <strong>weekly colloquia</strong>, and present their work at least once.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Completed application form</li><li>Valid passport</li><li>Academic transcript + degree certificate</li>
        <li>Academic CV (and publication list, if any)</li><li>Dissertation table of contents</li>
        <li>Project description (max 15,000 characters, excl. spaces and footnotes)</li>
        <li>Detailed work plan and timeline for the stay</li><li>Language certificates, where applicable</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the IEG application portal</strong>bewerbung.ieg-mainz.de — doctoral fellowships section.</li>
        <li><strong>Prepare your project description</strong>Explain the current stage of your dissertation and how the Mainz stay will complete it.</li>
        <li><strong>Submit before 15 February 2027</strong>The call typically opens in December; confirm the exact date on the portal.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is the stipend?","€1,650 per month, plus family allowances where applicable."),
 ("Can I work alongside the fellowship?","No — paid employment and simultaneous financial support are not permitted during the funded period."),
 ("Does IEG award my PhD?","No — you stay enrolled and supervised at your home university; IEG funds the writing stay."),
 ("Is accommodation free?","No — fellows can apply for an affordable room in the institute's residence, subject to availability."),
]),
 verify='Verified 16 Oct 2026 via the official IEG application portal (€1,650/month; 6–12 months; family allowances; Mainz residence; home-university enrolment) and daadscholarship.com, brightscholarship.com and scholarshipunion.com (15 Feb 2027 deadline; document list; completion-stage focus).',
 offlinks=[('IEG Fellowships for Doctoral Students (official)','https://bewerbung.ieg-mainz.de/jobposting/a4741518fcd82de0ed47dc0245dddf1909cd1061')],
 related_titles=['hanns-seidel','swiss-phd','zonta-ae'],
),

dict(
 slug='joint-japan-world-bank-graduate-scholarship-2027',
 title='Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP) 2027 | StudyDesk Scholarships',
 meta='JJ/WBGSP 2027: fully funded Master’s for developing-country professionals. Tuition, stipend, airfare. Window 1 closes 26 Feb 2027.',
 short='JJ/WBGSP 2027', kicker='International · Master’s · Fully funded',
 mono='WB', prov_short='World Bank (funded by Japan)', prov_long='World Bank Development Economics Vice Presidency — funded by the Government of Japan',
 h1='Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP) 2027',
 sub='A fully funded Master’s in development — tuition, living stipend, airfare — for mid-career professionals from developing countries.',
 dpill='133 days to go', dl_long='26 Feb 2027 (Window 1)',
 facts=facts([('Award','Fully funded<small>Tuition + stipend + airfare</small>'),
              ('Who can apply','Developing-country nationals<small>Includes India; 3 yrs work experience</small>'),
              ('Level',"Master's only<small>44 participating programs</small>"),
              ('Deadline','26 Feb 2027<small>Window 1; Window 2: 21 May 2027</small>'),
              ('Return rule','Return home after study<small>Development commitment</small>')]),
 body='''
      <h2 id="about">About the program</h2>
      <p>The <strong>Joint Japan/World Bank Graduate Scholarship Program (JJ/WBGSP)</strong>, run by the World Bank's Development Economics Vice Presidency and <strong>funded by the Government of Japan</strong>, has since 1987 supported over 6,000 mid-career professionals from developing countries through <strong>Master's degrees in development-related fields</strong>. For 2027 there are <strong>44 participating Master's programs at 24 universities</strong> across the US, Europe, Africa, Oceania, and Japan.</p>
      <div class="honest-note"><strong>Admission first:</strong> you must be <strong>admitted unconditionally</strong> to one of the 44 participating programs before you can apply for the scholarship. The scholarship application link is only sent to admitted, shortlisted candidates.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>National of a <strong>World Bank member developing country</strong> (India included); <strong>no dual citizenship</strong> of a developed country.</li>
        <li><strong>Bachelor's degree earned at least 3 years</strong> before the application deadline.</li>
        <li><strong>Employed full-time in development-related work</strong> at application, with <strong>at least 3 years of paid experience</strong> since the bachelor's, acquired within the past 6 years.</li>
        <li><strong>Admitted unconditionally</strong> to a JJ/WBGSP participating program for 2027 (outside your home country).</li>
        <li><strong>Not currently enrolled</strong> in a participating program; not World Bank Group staff or close family.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fees</strong> for the program.</li>
        <li><strong>Monthly living stipend</strong>.</li>
        <li><strong>Round-trip economy airfare</strong> between home country and host institution, plus a <strong>USD 600 travel allowance</strong> per trip.</li>
        <li><strong>Basic medical insurance</strong> through the institution.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Unconditional admission letter from a participating program</li><li>Bachelor's degree certificate + transcripts</li>
        <li>Proof of employment and development-related experience</li><li>Passport / national ID</li><li>Medical fitness declaration</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to a participating Master's program</strong>Check the 44-program list on the World Bank site and secure unconditional admission.</li>
        <li><strong>Get shortlisted by the university</strong>The university nominates eligible admitted candidates to the World Bank.</li>
        <li><strong>Complete the online JJ/WBGSP application</strong>Only via the official portal — email or post submissions are not accepted. <strong>Window 1: 18 Jan – 26 Feb 2027; Window 2: 29 Mar – 21 May 2027.</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can Indians apply?","Yes — India is a World Bank member developing country on the eligible list."),
 ("Do I apply for the scholarship before admission?","No — you need unconditional admission to a participating program first."),
 ("Are there two deadlines?","Yes — Window 1 closes 26 Feb 2027; Window 2 runs 29 Mar – 21 May 2027."),
 ("Must I return home after?","Yes — scholars commit to returning to their home country to contribute to its development."),
]),
 verify='Verified 16 Oct 2026 via buddy4study.com (26-Feb-2027 deadline; eligibility; benefits; USD 600 allowance), opportunitiesforyouth.org and ntchito.com (44 programs; two windows 18 Jan–26 Feb and 29 Mar–21 May 2027), and crawford.anu.edu.au (6,000+ alumni since 1987; Japan sole funder).',
 offlinks=[('World Bank JJ/WBGSP (official)','https://www.worldbank.org/en/programs/scholarships')],
 related_titles=['wb-gaf','bloomberg-harvard','griffith-vc'],
),

dict(
 slug='japan-imf-jispa-phd-scholarships-2027',
 title='Japan-IMF JISPA PhD Scholarships 2027 in Japan (Fully Funded) | StudyDesk Scholarships',
 meta='Japan-IMF JISPA PhD Track 2027: fully funded economics PhD in Japan for Asia-Pacific government officials. Deadline 1 Jun 2027.',
 short='JISPA PhD 2027', kicker='Japan · PhD · Fully funded',
 mono='IMF', prov_short='IMF / Japan (JISPA)', prov_long='Japan-IMF Scholarship Program for Asia — IMF Regional Office for Asia and the Pacific',
 h1='Japan-IMF JISPA PhD Scholarships 2027 in Japan',
 sub='A fully funded economics PhD in Japan — for government officials from Asia-Pacific countries, including India.',
 dpill='228 days to go', dl_long='1 Jun 2027',
 facts=facts([('Award','Fully funded<small>Tuition + stipend + airfare</small>'),
              ('Who can apply','Asia-Pacific govt officials<small>India eligible; economics PhD</small>'),
              ('Track','PhD only<small>Partner + accredited Japanese universities</small>'),
              ('Deadline','1 Jun 2027<small>Window: 1 May – 1 Jun 2027, JST</small>'),
              ('Return rule','Return to agency<small>Home-country commitment</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Japan-IMF Scholarship Program for Asia (JISPA)</strong>, run by the IMF's Regional Office for Asia and the Pacific with Japanese government funding, trains future economic policymakers. Its <strong>PhD Track</strong> funds doctoral study in <strong>economics and related fields</strong> at accredited Japanese universities — including partner institutions <strong>GRIPS, Hitotsubashi University, the International University of Japan, and the University of Tokyo</strong>.</p>
      <div class="honest-note"><strong>Not JISP:</strong> the separate "Japan-IMF Scholarship Program for Advanced Studies" is for <strong>Japanese nationals</strong> doing a PhD outside Japan. JISPA is the one for Asia-Pacific officials studying <strong>in</strong> Japan — don't mix them up.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>National of an <strong>eligible Asia-Pacific country</strong> (India, Bangladesh, Nepal, Sri Lanka, Indonesia, Philippines, Vietnam and others).</li>
        <li><strong>Employed as a government official</strong> involved in economic policymaking, with <strong>employer nomination and support</strong>.</li>
        <li>Expected to <strong>return to the government position</strong> after the PhD.</li>
        <li><strong>Strong Master's degree</strong> or equivalent; excellent academic record and research potential.</li>
        <li><strong>At least 2 years of public-sector work experience</strong> preferred; priority to applicants <strong>under 38</strong>.</li>
        <li><strong>English proficiency:</strong> iBT 79–80 or IELTS 6.0 minimum.</li>
        <li>Admission to an accredited Japanese university offering a relevant PhD program (you secure admission yourself — the IMF does not).</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition and university enrollment costs.</strong></li>
        <li><strong>Monthly living stipend</strong> (a set published figure for the 2027 PhD track is not disclosed — do not rely on older Master's-track figures).</li>
        <li><strong>Round-trip economy airfare.</strong></li>
        <li><strong>Field-research and conference funding</strong>, where approved.</li>
        <li>Access to <strong>IMF seminars, policy dialogues</strong>, and the JISPA thesis presentation.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application (during the window)</li><li>Employer nomination / support letter</li>
        <li>Master's degree certificate + transcripts</li><li>University admission letter (accredited Japanese university)</li>
        <li>English proficiency proof</li><li>Research plan in economic policymaking</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure PhD admission</strong>Apply directly to a Japanese university — the IMF does not handle university applications.</li>
        <li><strong>Get your employer's nomination</strong>Government backing is a core requirement.</li>
        <li><strong>Apply online 1 May – 1 June 2027</strong>Deadline: <strong>1 June 2027, 23:59 JST</strong>. Guidelines for AY2027-28 are posted by early March 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can Indians apply?","Yes — India is on the eligible Asia-Pacific country list."),
 ("Is the stipend amount published?","A set monthly figure for the 2027 PhD track is not disclosed in the announcement; treat older figures with caution."),
 ("Can my family come?","They may join under immigration rules, but JISPA does not fund family travel, housing, insurance, or living costs."),
 ("Is this the same as JISP?","No — JISP (Advanced Studies) is for Japanese nationals studying abroad; JISPA is for Asia-Pacific officials studying in Japan."),
]),
 verify='Verified 16 Oct 2026 against the official IMF JISPA PhD Track page (window 1 May–1 Jun 2027; deadline 1 Jun 2027 23:59 JST; partner universities; under-38 priority; 2 yrs public-sector experience; iBT 79–80 / IELTS 6.0) and scholarshipsads.com (eligible countries incl. India; benefits; employer nomination).',
 offlinks=[('JISPA PhD Track — IMF (official)','https://www.imf.org/en/countries/resrep/oap-home/jispa-home/phd-track')],
 related_titles=['wb-gaf','bloomberg-harvard','jj-wbgsp'],
),

dict(
 slug='flex-global-abroad-exchange-program-2027-28',
 title='FLEX Global Abroad Exchange Program 2027-28 (Fully Funded) | StudyDesk Scholarships',
 meta='FLEX Global Abroad 2027-28: fully funded year abroad for American high school students — airfare, host family, stipend. Deadline 30 Nov 2026.',
 short='FLEX Global Abroad', kicker='Exchange · High school · Fully funded',
 mono='FLEX', prov_short='U.S. Dept. of State / American Councils', prov_long='U.S. Department of State — administered by American Councils for International Education',
 h1='FLEX Global Abroad Exchange Program 2027–28',
 sub='A fully funded school year abroad — for American high school students. Read the eligibility carefully: this one is not for Indian applicants.',
 dpill='45 days to go', dl_long='30 Nov 2026',
 facts=facts([('Award','Fully funded<small>Airfare + host family + stipend</small>'),
              ('Who can apply','U.S. citizens only<small>Grades 9–12; ages 15–18.5</small>'),
              ('Destinations','10 countries<small>Bosnia to Thailand</small>'),
              ('Deadline','30 Nov 2026<small>For 2027–28 academic year</small>'),
              ('Indian students','Not eligible<small>See note below</small>')]),
 body='''
      <h2 id="about">About the program</h2>
      <p>The <strong>Future Leaders Exchange (FLEX) Global Abroad Program</strong>, funded by the <strong>U.S. Department of State</strong> and administered by <strong>American Councils for International Education</strong>, sends American high school students abroad for one academic year. Participants attend a local high school, live with a host family, and join leadership and cultural activities in one of ten countries: <strong>Bosnia and Herzegovina, Georgia, India, Indonesia, Kazakhstan, Morocco, North Macedonia, Poland, Romania, and Thailand</strong>.</p>
      <div class="honest-note"><strong>Important for Indian readers:</strong> this program is <strong>only for U.S. citizens</strong> — Indian students cannot apply. We list it because it appears on many scholarship lists with misleading framing; if you are an Indian high-schooler looking for exchange programs, look instead at programs that accept Indian nationals.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>U.S. citizenship</strong> required.</li>
        <li>Enrolled in <strong>grades 9–12</strong> during the application period (homeschooled students eligible).</li>
        <li>Aged <strong>15 to 18.5</strong> at the start of the program.</li>
        <li>Willing to attend a local school and live with a host family abroad.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Round-trip international airfare.</strong></li>
        <li><strong>Host-family accommodation and meals.</strong></li>
        <li><strong>Modest monthly living stipend.</strong></li>
        <li><strong>Host-country visa costs</strong> covered.</li>
        <li><strong>Emergency medical and accident insurance.</strong></li>
        <li>Local high-school enrollment and in-country support.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application via the AIS Forms portal</li><li>Proof of U.S. citizenship</li>
        <li>School enrollment records</li><li>Parental consent forms</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Go to the official FLEX Global Abroad page</strong>americancouncils.org — FLEX Global Abroad section.</li>
        <li><strong>Register on the AIS Forms portal</strong>Select the FLEX Global Abroad program option.</li>
        <li><strong>Complete and submit before 30 November 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can Indian students apply?","No — U.S. citizenship is a hard requirement."),
 ("Which countries can participants go to?","Ten: Bosnia and Herzegovina, Georgia, India, Indonesia, Kazakhstan, Morocco, North Macedonia, Poland, Romania, Thailand."),
 ("Is it really fully funded?","Yes — airfare, host family, meals, visa, insurance, and a monthly stipend are covered."),
 ("Do I need to know the local language?","Previous language study is not required for most programs."),
]),
 verify='Verified 16 Oct 2026 via americancouncils.org (official program page; U.S. Department of State funding; American Councils administration), scholarshipscorner.website and opportunitiescircle.com (deadline 30 Nov 2026; eligibility: U.S. citizens, grades 9–12, ages 15–18.5; 10 destination countries).',
 offlinks=[('FLEX Global Abroad — American Councils (official)','https://www.americancouncils.org/programs/future-leaders-exchange-flex-global-abroad')],
 related_titles=['epfl-summer','dakshana','super50-aayam'],
),

dict(
 slug='lille-eiffel-phd-scholarship-2027',
 title='France Excellence Eiffel Scholarship 2027 via University of Lille (PhD) | StudyDesk Scholarships',
 meta='France Excellence Eiffel Scholarship 2027 at University of Lille: €2,100/month for international PhD mobility. Lille internal deadline ~13 Nov 2026.',
 short='Lille Eiffel PhD 2027', kicker='France · PhD · Government funded',
 mono='EF', prov_short='Campus France / Univ. of Lille', prov_long='France Excellence Eiffel (French Ministry for Europe and Foreign Affairs) — via University of Lille nomination',
 h1='France Excellence Eiffel Scholarship 2027 via University of Lille',
 sub='€2,100 a month for PhD research in France — but you apply through the University of Lille, not directly to Campus France.',
 dpill='28 days to go', dl_long='~13 Nov 2026 (Lille internal)',
 facts=facts([('Award','€2,100 / month (PhD)<small>+ travel + insurance</small>'),
              ('Who can apply','International PhD<small>Nominated by Lille; ≤35 yrs</small>'),
              ('Route','Cotutelle / co-supervision<small>Lille + home university</small>'),
              ('Deadline','~13 Nov 2026<small>Lille internal; confirm with school</small>'),
              ('Tuition','Not covered<small>Check registration costs</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>France Excellence Eiffel Scholarship</strong> is the French government's flagship award for international students, run by the <strong>Ministry for Europe and Foreign Affairs through Campus France</strong>. The <strong>University of Lille</strong> uses it to host international PhD students for research stays of <strong>up to 18 months</strong> — structured as a <strong>joint thesis (cotutelle) or co-supervised thesis</strong> between the student's home university and Lille.</p>
      <div class="honest-note"><strong>You cannot apply to Campus France yourself.</strong> The University of Lille pre-selects candidates and forwards the best files nationally. Your first step is contacting a Lille supervisor — the university's internal selection runs at the <strong>end of November</strong>.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International student of any nationality</strong> (French dual nationals excluded).</li>
        <li><strong>Aged 35 or under</strong> at PhD level for the 2027 call.</li>
        <li><strong>Pre-admitted or endorsed by a Lille laboratory / doctoral school</strong> — supervisor support is essential.</li>
        <li>Research framed as a <strong>cotutelle or co-supervised thesis</strong> with Lille.</li>
        <li><strong>Not already holding</strong> another French government scholarship.</li>
        <li>B2 French certificate may be required if the work is in French.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>€2,100 per month</strong> for doctorate students (2027 call).</li>
        <li><strong>International travel</strong> and <strong>health insurance</strong>.</li>
        <li>Help finding housing, plus cultural activities.</li>
        <li><strong>Not covered:</strong> tuition/registration fees — ask the doctoral school about costs.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Academic transcripts and degree certificates</li><li>CV</li><li>Research proposal linked to a Lille supervisor's team</li>
        <li>Supervisor endorsement</li><li>Signed attestation sur l'honneur (no double applications)</li>
        <li>Passport; B2 French certificate if applicable</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Find a Lille supervisor now</strong>Write to a laboratory whose research matches your project.</li>
        <li><strong>Prepare the institutional file</strong>The doctoral school reviews it and Lille decides whether to nominate you to Campus France.</li>
        <li><strong>Meet the internal deadline (~13 November 2026)</strong>Confirm the exact date with EGSESAM or your doctoral school — the university's news page does not publish a single universal deadline.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can I apply directly to Campus France?","No — only the university can submit your file nationally."),
 ("What is the deadline?","Lille's internal selection is end-November; a supplementary listing gives 13 Nov 2026 for the EGSESAM doctoral school — confirm with the school."),
 ("Does it cover tuition?","No — the Eiffel covers the monthly allowance, travel, and insurance; registration fees are separate."),
 ("How long is the PhD mobility?","Up to 18 months at Lille under the 2027 call."),
]),
 verify='Verified 16 Oct 2026 via scholarfahad.com (€2,100/month PhD; ≤35 yrs; cotutelle; Lille pre-selection; end-Nov internal selection), daadscholarship.com (EGSESAM doctoral call; supervisor + doctoral-school endorsement), and scholarshipunion.com (13 Nov 2026 supplementary deadline; attestation requirement).',
 offlinks=[('Campus France — Eiffel Scholarship (official)','https://www.campusfrance.org/en/eiffel-scholarship')],
 related_titles=['hanns-seidel','swiss-phd','ieg-mainz'],
),

dict(
 slug='clara-collet-phd-scholarship-2027-ucl',
 title='Clara Collet PhD Scholarship 2027 at UCL, UK (Fully Funded) | StudyDesk Scholarships',
 meta='Clara Collet PhD Scholarship 2027 at UCL: full fees + £23,805 tax-free stipend for social sciences PhD. Deadline 10 Dec 2026.',
 short='Clara Collet PhD, UCL', kicker='UK · PhD · Fully funded',
 mono='CC', prov_short='University College London', prov_long='University College London (UCL) — Department of Political Science',
 h1='Clara Collet PhD Scholarship 2027 at UCL',
 sub='Full fees plus a £23,805 tax-free stipend — for a social sciences PhD at University College London.',
 dpill='55 days to go', dl_long='10 Dec 2026',
 facts=facts([('Award','Full fees + £23,805<small>Tax-free annual stipend</small>'),
              ('Who can apply',"Master\u2019s holders<small>Social sciences; 1+3 route possible</small>"),
              ('Duration','4 years (5 via 1+3)<small>UCL Political Science</small>'),
              ('Deadline','10 Dec 2026<small>2027–28 academic year</small>'),
              ('Note','Extremely competitive<small>Merit + research potential</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Clara Collet Scholarships</strong>, named after the pioneering social reformer and advocate for women's education, are offered by <strong>UCL's Department of Political Science</strong> for the 2027–28 academic year. These <strong>fully funded awards cover up to four years of doctoral study</strong> in the social sciences, with full tuition plus a <strong>tax-free annual stipend of £23,805</strong>.</p>
      <div class="honest-note"><strong>Provider correction:</strong> some scholarship blogs list this under a "Universal College Lahore" — the actual host is <strong>University College London (UCL)</strong>, Faculty of Social and Historical Sciences.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Open to <strong>UK and international applicants</strong> of all nationalities.</li>
        <li>Hold a <strong>Master's degree</strong>, or apply via the <strong>1+3 route</strong> (one-year Master's in the department, then a three-year PhD).</li>
        <li><strong>Strong academic credentials</strong> and clearly defined research interests relevant to the department.</li>
        <li>Awarded <strong>solely on academic achievement and research potential</strong> — extremely competitive.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Full tuition fee coverage.</strong></li>
        <li><strong>Tax-free stipend of £23,805 per year.</strong></li>
        <li>Organised <strong>teaching obligations</strong> as part of research training.</li>
        <li>Four years of funding (five via the 1+3 pathway).</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>UCL PhD application form</li><li>Master's degree certificate + transcripts</li>
        <li>Research proposal</li><li>Academic references</li><li>CV</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Check the UCL Political Science page</strong>Confirm the 2027–28 Clara Collet call and its requirements.</li>
        <li><strong>Prepare a strong research proposal</strong>Fit with the department's research strengths matters.</li>
        <li><strong>Submit before 10 December 2026</strong></li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Who runs this scholarship?","UCL's Department of Political Science — not 'Universal College Lahore' as some blogs claim."),
 ("How much is the stipend?","£23,805 per year, tax-free, plus full tuition."),
 ("Can I apply without a Master's?","Yes — via the 1+3 route: a one-year Master's in the department followed by the three-year PhD."),
 ("Is it open to international students?","Yes — all nationalities, UK and international."),
]),
 verify='Verified 16 Oct 2026 via opforall.com (UCL host; full tuition + £23,805 stipend; 10 Dec 2026 deadline; 4 years / 5 via 1+3) and brightscholarship.com (same deadline; stipend; eligibility on merit and research potential).',
 offlinks=[('UCL Political Science — PhD funding (official)','https://www.ucl.ac.uk/political-science/')],
 related_titles=['bloomberg-harvard','nasa-hubble','swiss-phd'],
),

dict(
 slug='lincoln-global-leaders-scholarship-2027',
 title='University of Lincoln Global Leaders Scholarship 2027 (50% Tuition) | StudyDesk Scholarships',
 meta='Lincoln Global Leaders Scholarship 2027: 50% tuition for one year for international UG/PG taught students. Deadline 16 Nov 2026 (Jan 2027 intake).',
 short='Lincoln Global Leaders', kicker='UK · UG/PG · International',
 mono='L', prov_short='University of Lincoln', prov_long='University of Lincoln, United Kingdom',
 h1='University of Lincoln Global Leaders Scholarship 2027',
 sub='50% off tuition for one year — for high-achieving international students starting at Lincoln.',
 dpill='31 days to go', dl_long='16 Nov 2026 (Jan 2027 intake)',
 facts=facts([('Award','50% tuition, 1 year<small>Competitive; first year only</small>'),
              ('Who can apply','International UG/PG<small>Offer required; overseas fee status</small>'),
              ('Grades','128 UCAS / 2:1<small>High-school or degree equivalent</small>'),
              ('Deadline','16 Nov 2026<small>Jan 2027 intake; more rounds later</small>'),
              ('Mode','Separate application<small>Not automatic</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>Global Leaders Scholarship</strong> recognises international applicants who show the highest levels of <strong>academic, personal, and extracurricular achievement</strong>. It is worth <strong>50% of tuition fees for one year of study</strong> at the <strong>University of Lincoln</strong>, for full-time undergraduate and postgraduate taught programmes.</p>
      <div class="honest-note"><strong>One year only:</strong> on a two-year-plus programme, the 50% discount applies to the <strong>first year</strong>. It does not cover living costs — budget those separately.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International (overseas fee status)</strong> student — home fee-status students are excluded.</li>
        <li>Hold a <strong>conditional or unconditional offer</strong> for a UG or postgraduate taught programme commencing in 2026/27 or 2027/28.</li>
        <li><strong>UG:</strong> high-school grades equivalent to <strong>128 UCAS points or above</strong>.</li>
        <li><strong>PG taught:</strong> undergraduate degree equivalent to a <strong>2:1 or higher</strong>.</li>
        <li>Complete the <strong>separate Global Leaders Scholarship application form</strong> — it is competitive, not automatic.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>50% tuition fee reduction for one year</strong> of full-time study.</li>
        <li>Scholar networking events and an official <strong>awards ceremony</strong>.</li>
        <li>Eligibility to apply as a <strong>Lincoln International Student Ambassador</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Lincoln offer letter</li><li>Most recent academic transcripts</li>
        <li>Completed Global Leaders Scholarship application form</li><li>Passport</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply to study at Lincoln</strong>Get your offer for an eligible programme first.</li>
        <li><strong>Complete the scholarship form</strong>On the university's scholarships page — show academic, personal, and extracurricular achievement.</li>
        <li><strong>Submit by the round deadline</strong><strong>16 Nov 2026</strong> (Jan 2027 intake) · <strong>7 Jun 2027</strong> (Sep 2027 intake) · <strong>18 Oct 2027</strong> (Jan 2028 intake).</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How much is it worth?","50% of tuition fees for one year of study."),
 ("Is it automatic with my offer?","No — you must submit a separate, competitive scholarship application."),
 ("Does it cover living costs?","No — tuition only. Budget accommodation and living separately."),
 ("What grades do I need?","128 UCAS points (UG) or a 2:1-equivalent degree (PG taught), plus a strong application."),
]),
 verify='Verified 16 Oct 2026 against the official University of Lincoln Global Leaders Scholarship page (50% tuition one year; offer required; 128 UCAS / 2:1; deadlines 16 Nov 2026, 7 Jun 2027, 18 Oct 2027) and the official 2027-28 Terms and Conditions PDF (first-year-only rule).',
 offlinks=[('Global Leaders Scholarship — Lincoln (official)','https://www.lincoln.ac.uk/studywithus/scholarshipsandbursaries/thelincolngloballeadersscholarship/')],
 related_titles=['griffith-vc','bloomberg-harvard','clara-collet'],
),

dict(
 slug='america-world-consortium-fellowships-2027-28',
 title='America in the World Consortium Fellowships 2027-28 (Predoctoral + Postdoctoral) | StudyDesk',
 meta='AWC Fellowships 2027-28 at Duke, Johns Hopkins SAIS, UT Austin: $73,500 postdoc stipend. Deadline 1 Dec 2026.',
 short='AWC Fellowships 2027-28', kicker='USA · PhD/Postdoc · Fellowship',
 mono='AWC', prov_short='America in the World Consortium', prov_long='America in the World Consortium — Duke, Johns Hopkins SAIS, UT Austin',
 h1='America in the World Consortium Fellowships 2027–28',
 sub='A year in residence at Duke, Johns Hopkins SAIS, or UT Austin — for scholars of American grand strategy.',
 dpill='46 days to go', dl_long='1 Dec 2026',
 facts=facts([('Award','$73,500 stipend (postdoc)<small>+ $7,500 research fund</small>'),
              ('Who can apply','PhD candidates / recent PhDs<small>U.S. foreign policy research</small>'),
              ('Tracks','Predoctoral + Postdoctoral<small>Up to 8 positions each</small>'),
              ('Deadline','1 Dec 2026<small>Opened 1 Oct 2026</small>'),
              ('Residence','Aug 2027 start<small>1 year, renewable</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>America in the World Consortium (AWC)</strong> — a partnership of <strong>Duke University's Program in American Grand Strategy, Johns Hopkins SAIS's Henry A. Kissinger Center for Global Affairs, and UT Austin's Clements Center for National Security</strong> — offers <strong>predoctoral and postdoctoral fellowships</strong> for scholars whose work examines <strong>American grand strategy, U.S. foreign policy, international affairs, and national security</strong>. Fellows spend a year in residence at one of the three institutions, joining an intellectually diverse research community.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Predoctoral:</strong> currently enrolled in a PhD program, having <strong>passed qualifying/comprehensive exams and advanced to doctoral candidacy</strong>.</li>
        <li><strong>Postdoctoral:</strong> PhD <strong>received by 1 August 2027</strong>, in a relevant field (history, political science, public policy, classics, political philosophy, etc.).</li>
        <li>Research must bear <strong>directly on American grand strategy</strong>, broadly defined; preference for policy-connected work.</li>
        <li>All disciplines welcome; up to <strong>8 positions per track</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Postdoc stipend of $73,500</strong>, plus benefits and full campus facilities.</li>
        <li><strong>$7,500 research fund</strong> for legitimate research expenses.</li>
        <li><strong>Competitive stipend for predoctoral fellows</strong> (figure varies by institution).</li>
        <li>Funding for <strong>12 months, renewable for a second year</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Online application (predoctoral or postdoctoral track)</li><li>CV</li><li>Research proposal / statement</li>
        <li>Academic transcripts</li><li>Letters of recommendation</li><li>Writing sample</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Choose your track</strong>Predoctoral (PhD candidates) or Postdoctoral (PhD by Aug 2027).</li>
        <li><strong>Prepare a policy-connected proposal</strong>Show how your research speaks to American grand strategy.</li>
        <li><strong>Apply before 1 December 2026</strong>Applications opened 1 October 2026; in-residence positions begin August 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Which universities host fellows?","Duke (AGS), Johns Hopkins SAIS (Kissinger Center), and UT Austin (Clements Center)."),
 ("What is the postdoc stipend?","$73,500 plus a $7,500 research fund."),
 ("Can predoctoral students apply?","Yes — advanced PhD candidates who have passed their qualifying exams."),
 ("When does the fellowship start?","In-residence positions begin August 2027, for one year with possible renewal."),
]),
 verify='Verified 16 Oct 2026 via opportunitydesk.org (deadline 1 Dec 2026; $73,500 stipend; $7,500 research fund; 3 partner institutions; eligibility) and opportunitiesforyouth.org (applications opened 1 Oct 2026; predoctoral + postdoctoral tracks; up to 8 positions).',
 offlinks=[('AWC Fellowships — Opportunity Desk listing','https://opportunitydesk.org/2026/10/05/america-in-the-world-consortium-postdoctoral-fellowship-2027-2028/')],
 related_titles=['bloomberg-harvard','nasa-hubble','clara-collet'],
),

dict(
 slug='dayton-merit-scholarship-2027',
 title='University of Dayton Merit Scholarship 2027, USA (Up to $30,000/Year) | StudyDesk Scholarships',
 meta='University of Dayton Merit Scholarship 2027: up to $30,000/year + $4,000 textbook award, automatic with admission. Deadline 1 Nov 2026.',
 short='Dayton Merit Scholarship', kicker='USA · Undergraduate · Merit',
 mono='UD', prov_short='University of Dayton', prov_long='University of Dayton, Ohio, USA',
 h1='University of Dayton Merit Scholarship 2027',
 sub='Up to $30,000 a year — automatic with your admission application. No separate scholarship form.',
 dpill='16 days to go', dl_long='1 Nov 2026',
 facts=facts([('Award','Up to $30,000 / year<small>+ $4,000 textbook award</small>'),
              ('Who can apply','International UG<small>All nationalities; all fields</small>'),
              ('Mode','Automatic<small>No separate application</small>'),
              ('Deadline','1 Nov 2026<small>Admission round</small>'),
              ('Full tuition?','No<small>Partial — plan the rest</small>')]),
 body='''
      <h2 id="about">About the scholarship</h2>
      <p>The <strong>University of Dayton</strong>, a private Catholic research university in Dayton, Ohio, awards <strong>International Merit Scholarships</strong> to undergraduate applicants from all over the world. Awards go up to <strong>$30,000 per year</strong> toward tuition, renewable for four years — plus a <strong>textbook scholarship of up to $4,000 over four years</strong>.</p>
      <div class="honest-note"><strong>Automatic consideration:</strong> there is <strong>no separate scholarship application</strong> — every complete admission application is automatically considered for merit awards. The university does not offer full-tuition scholarships, so plan for remaining costs.</div>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>International undergraduate applicant</strong> (first-year or transfer), any nationality.</li>
        <li>Applying to any of Dayton's 80+ programs: <strong>arts and sciences, business, education and health sciences, engineering, law</strong>.</li>
        <li>Awards are <strong>merit-based</strong> — stronger academics earn larger awards.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Merit scholarship: up to $30,000 per year</strong> toward tuition (renewable up to 4 years).</li>
        <li><strong>Textbook scholarship: up to $4,000 over four years.</strong></li>
        <li><strong>No application fee.</strong></li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Admission application including the essay</li><li>Official high-school transcripts</li>
        <li>Letter of recommendation</li><li>Letter of financial support</li>
        <li>English proficiency proof (IELTS / TOEFL / PTE / SAT / ACT / iTEP / DET)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Apply for admission to the University of Dayton</strong>Complete the application with essay and documents.</li>
        <li><strong>You are automatically considered</strong>No separate merit form exists.</li>
        <li><strong>Apply before 1 November 2026</strong>For the priority admission round.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is there a separate scholarship form?","No — admission applications are automatically considered for merit awards."),
 ("How much can I get?","Up to $30,000 per year in merit aid, plus up to $4,000 over four years for textbooks."),
 ("Is it fully funded?","No — it is a partial tuition award; all other expenses are the student's responsibility."),
 ("Is there an application fee?","No — the University of Dayton charges no application fee."),
]),
 verify='Verified 16 Oct 2026 via brightscholarship.com and opportunitiesinfo.com ($30,000/year; $4,000 textbook; 1 Nov 2026 deadline; automatic consideration; no full-tuition awards) and collegedunia.com (automatic UG merit route; no separate form).',
 offlinks=[('University of Dayton — International admissions (official)','https://udayton.edu/apply/international/index.php')],
 related_titles=['griffith-vc','lincoln-gl','epfl-summer'],
),

dict(
 slug='perugia-phd-scholarships-2026-27',
 title='University of Perugia PhD Scholarships 2026/27 in Italy (31 Funded Positions) | StudyDesk Scholarships',
 meta='University of Perugia PhD Scholarships 2026/27: 31 funded positions across 24 PhD courses. PICA application, €20 fee. Deadline 28 Oct 2026.',
 short='Perugia PhD 2026/27', kicker='Italy · PhD · Funded',
 mono='UP', prov_short='University of Perugia', prov_long='Università degli Studi di Perugia, Italy',
 h1='University of Perugia PhD Scholarships 2026/27 in Italy',
 sub='31 funded PhD positions across 24 courses — at one of Italy’s oldest universities, founded in 1308.',
 dpill='12 days to go', dl_long='28 Oct 2026',
 facts=facts([('Award','31 funded positions<small>24 PhD courses; ~€22,417/yr</small>'),
              ('Who can apply',"Master\u2019s holders<small>All nationalities; EQF Level 7</small>"),
              ('Fee','€20 per application<small>Via PagoPA; per program</small>'),
              ('Deadline','28 Oct 2026, 23:59<small>PICA portal</small>'),
              ('Degree by','31 Oct 2026<small>Or notify within 10 days</small>')]),
 body='''
      <h2 id="about">About the scholarships</h2>
      <p>The <strong>University of Perugia (Università degli Studi di Perugia)</strong>, founded in 1308, has opened its <strong>42nd-cycle (XLII) PhD call for 2026/27</strong> with <strong>31 funded positions across 24 PhD courses</strong> — covering earth, biological, medical, engineering, humanities, law, economics, political and social sciences, physics, and chemistry. This call is the <strong>PR Umbria FSE+ funded</strong> competition (code DOTTORATO_XLII_REGIONE).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>Master's degree (or equivalent)</strong> by <strong>31 October 2026</strong>.</li>
        <li><strong>Foreign degrees</strong> accepted if comparable to an Italian second-cycle degree (EQF Level 7) and giving access to doctoral study in the awarding country — the committee evaluates equivalence.</li>
        <li><strong>All nationalities</strong>; early-stage researchers.</li>
        <li>Specific requirements may vary by PhD programme — check the annexes for your course.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Funded PhD position</strong> — annual scholarship around <strong>€22,416.96</strong> under the PR Umbria call.</li>
        <li>Three-year doctoral programme with research training across the university's departments.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>PICA online application (competition code DOTTORATO_XLII_REGIONE)</li><li>Qualification evidence + comparability documentation (foreign degrees)</li>
        <li>CV</li><li>Thesis summary</li><li>Research proposal (if required by the course)</li>
        <li>Publications and language evidence (as requested)</li><li>€20 application contribution via PagoPA</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Read the official call + Annex 1</strong>Check your course's places, selection rules, and whether a proposal is needed.</li>
        <li><strong>Apply on the PICA portal</strong>pica.cineca.it/unipg — complete the form, upload documents, pay €20 via PagoPA.</li>
        <li><strong>Sign and submit before 28 October 2026, 23:59</strong>Use PICA's "Sign and Submit"; save your application ID. Each extra programme needs its own application and fee.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("How many positions are funded?","31 funded positions across 24 PhD courses."),
 ("Is there an application fee?","Yes — €20 per programme application, paid via PagoPA."),
 ("Can I apply to more than one programme?","Yes, but each needs a separate application and fee."),
 ("What if I graduate after the deadline?","Notify the Doctoral Office immediately and send degree evidence within 10 days of graduation, no later than 10 November 2026."),
]),
 verify='Verified 16 Oct 2026 via scholarshipunion.com and daadscholarship.com (28 Oct 2026 23:59 deadline; applications opened 28 Sep 2026; €20 fee; PICA + PagoPA; degree by 31 Oct 2026) and agristok.net (31 funded positions; 24 courses; XLII cycle; DOTTORATO_XLII_REGIONE).',
 offlinks=[('University of Perugia — PhD calls (official)','https://www.unipg.it/en')],
 related_titles=['ieg-mainz','hanns-seidel','swiss-phd'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')

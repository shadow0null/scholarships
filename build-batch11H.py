#!/usr/bin/env python3
"""Batch 11H: 3 verified articles (MOPGA, St John's Pharma, Amazon ARA). Verified 16 Oct 2026.
Skipped: JINR START (deadline today 16 Oct 2026), PAIE Scholars (deadline today 16 Oct 2026),
15 AI/ML Internship Programs (listicle, not a single scholarship).
NOTE: does NOT touch queue-progress.json, cards_registry.py, tracker.md (parent handles)."""
import pathlib, sys
sys.path.insert(0, '/home/hatch/workspace/scholarships-17k')
from article_builder import build_article, facts, faqs
from cards_registry import CARDS as REGISTRY

BASE = pathlib.Path('/home/hatch/workspace/your_files/scholarship-article-example-pragati.html').read_text()
OUT = pathlib.Path('/home/hatch/workspace/scholarships-17k/articles')

CARDINFO = {
 'mopga-2027': dict(mono='MF', title='MOPGA Fellowship 2027 in France', href='mopga-fellowship-2027-france.html',
              dpill='60 days to go', award='\u20ac2,500/month + \u20ac500 settling-in', elig='PhD defended Dec 2021\u2013Dec 2026; non-French; climate research.',
              tags=[('PhD','blue'),('France','teal')]),
 'stjohns-pharma': dict(mono='SJU', title="St. John's University Pharmaceutical Industry Fellowship 2027", href='st-johns-university-pharma-fellowship-2027-usa.html',
              dpill='7 days to go', award='Living stipend + health benefits', elig='Pharm.D. graduates; international applicants welcome.',
              tags=[('Post-Pharm.D.','blue'),('USA','teal')]),
 'amazon-ara': dict(mono='ARA', title='Amazon Research Awards \u2014 Fall 2026', href='amazon-research-awards-fall-2026.html',
              dpill='19 days to go', award='Up to $80,000 + AWS credits', elig='Full-time faculty / permanent NGO researchers; 9 AI & security areas.',
              tags=[('Research grant','blue'),('Global','teal')]),
}

ARTICLES = [
dict(
 slug='mopga-fellowship-2027-france',
 title='MOPGA Fellowship 2027 in France | StudyDesk Scholarships',
 meta='MOPGA Fellowship 2027: \u20ac2,500/month for 12 months of climate research in France. Early-career researchers, PhD 2021\u20132026. Apply by 15 Dec 2026.',
 short='MOPGA Fellowship 2027', kicker='France \u00b7 Early-career researchers \u00b7 Climate',
 mono='MF', prov_short='Campus France', prov_long='French Ministry for Europe and Foreign Affairs (MEAE) & Ministry of Higher Education, Research and Space \u2014 implemented by Campus France',
 h1='MOPGA Fellowship 2027 in France',
 sub='\u20ac2,500 a month for a year of climate research in France \u2014 for early-career researchers from every country except France.',
 dpill='60 days to go', dl_long='15 Dec 2026',
 facts=facts([('Award','\u20ac2,500 / month<small>+\u20ac500 settling-in + health cover</small>'),
              ('Who can apply','Early-career researchers<small>PhD defended Dec 2021\u2013Dec 2026</small>'),
              ('Nationality','Foreign only<small>French nationals ineligible</small>'),
              ('Deadline','15 Dec 2026<small>23:59 CET</small>'),
              ('Stay','12 months, non-renewable<small>Starts Sep\u2013Dec 2027</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>MOPGA 2027 Visiting Fellowship</strong> \u2014 short for <strong>Make Our Planet Great Again</strong> \u2014 is France's flagship international research-mobility programme for young scientists working on <strong>climate change and environmental challenges</strong>. Funded by the <strong>French Ministry for Europe and Foreign Affairs</strong> in partnership with the <strong>Ministry of Higher Education, Research and Space</strong> and implemented by <strong>Campus France</strong>, the 2027 edition is the programme's tenth call. Successful candidates spend <strong>12 months</strong> conducting their own research project at a French host institution, starting between <strong>September and December 2027</strong>.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold a <strong>doctoral degree defended between December 2021 and December 2026 inclusive</strong> (less than five years before the deadline; maternity-leave extensions possible with proof).</li>
        <li>Be <strong>exclusively of foreign nationality</strong> \u2014 French nationals are not eligible; every other nationality is.</li>
        <li>Apply for the purpose of <strong>international mobility to France</strong>.</li>
        <li><strong>Not be residing and professionally active in France</strong> at the time of application.</li>
        <li>Have a <strong>French host institution and scientific supervisor</strong> willing to sign the hosting agreement and confirm lab resources.</li>
        <li>Research project on <strong>climate, environment or sustainability themes</strong>.</li>
        <li>Must <strong>not have previously received a MOPGA fellowship</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>\u20ac2,500 monthly allowance</strong> for 12 months.</li>
        <li><strong>\u20ac500 one-time settling-in allowance.</strong></li>
        <li><strong>Health-related insurance coverage.</strong></li>
        <li>Research stay at a <strong>leading French laboratory</strong> with institutional support.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>CV with publications list (max 4 pages)</li><li>Doctoral degree certificate (or official proof the defence took place)</li>
        <li>CV of the French host supervisor (max 2 pages)</li><li>Letter of support from the host supervisor, co-signed by the lab director (or lab commitment letter)</li>
        <li>1\u20133 letters of recommendation</li><li>Passport or national ID copy</li>
        <li>Detailed research proposal (title, abstract, context, objectives, methodology, 12-month timeline, MOPGA alignment, impact)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Secure a French host first</strong>Contact a lab/supervisor in France and get the hosting agreement signed.</li>
        <li><strong>Apply online via the Campus France SMApply portal</strong>campusfrance.smapply.io \u2014 MOPGA 2027 programme page.</li>
        <li><strong>Upload all documents as PDFs</strong>Application language: English or French.</li>
        <li><strong>Submit before 15 December 2026, 23:59 CET</strong>Results announced May\u2013June 2027.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can Indians apply?","Yes \u2014 all foreign nationalities except French are eligible, including Indian researchers, provided you meet the PhD-date and host requirements."),
 ("Do I need a host before applying?","Yes. A French host institution and supervisor must sign the hosting agreement confirming lab resources for your project."),
 ("What if my PhD certificate is not issued yet?","You may submit official proof that the defence took place \u2014 a university certificate or proof of thesis submission."),
 ("Is the fellowship renewable?","No \u2014 it is a one-time 12-month stay, non-renewable."),
]),
 verify='Verified 16 Oct 2026 via the official Campus France MOPGA 2027 page (deadline 15 Dec 2026 23:59 CET; \u20ac2,500/month + \u20ac500 settling-in + health cover; 12 months starting Sep\u2013Dec 2027; PhD defended Dec 2021\u2013Dec 2026; foreign nationality only; French host institution required; climate/environment research), corroborated by AfroCareer and CareerAidHub.',
 offlinks=[('MOPGA 2027 \u2014 Campus France (official)','https://www.campusfrance.org/en/mopga-2027')],
 related_titles=['swiss-phd','nasa-hubble','bloomberg-harvard'],
),

dict(
 slug='st-johns-university-pharma-fellowship-2027-usa',
 title="St. John's University Pharmaceutical Industry Fellowship 2027 | StudyDesk Scholarships",
 meta="St. John's University Pharmaceutical Industry Fellowship 2027 (USA): 2-year post-Pharm.D. training with Pfizer, AbbVie and more. CV+LOI by 23 Oct 2026.",
 short="St. John's Pharma Fellowship 2027", kicker='USA \u00b7 Post-Pharm.D. \u00b7 Pharma industry',
 mono='SJU', prov_short="St. John's University", prov_long="College of Pharmacy and Health Sciences, St. John's University, New York, USA",
 h1="St. John's University Pharmaceutical Industry Fellowship 2027",
 sub='Two years inside the pharmaceutical industry \u2014 train with Pfizer, AbbVie and other partners while teaching at St. John\u2019s, New York.',
 dpill='7 days to go', dl_long='23 Oct 2026',
 facts=facts([('Award','Living stipend + health benefits<small>Exact figure not published</small>'),
              ('Who can apply','Pharm.D. graduates<small>International applicants welcome</small>'),
              ('Duration','Primarily 2 years<small>Industry + academic teaching</small>'),
              ('Deadline','23 Oct 2026<small>CV + letter of intent</small>'),
              ('Tracks','4 industry posts<small>Medical affairs \u00b7 HEOR \u00b7 Clinical \u00b7 Regulatory</small>')]),
 body='''
      <h2 id="about">About the fellowship</h2>
      <p>The <strong>St. John's University Pharmaceutical Industry Fellowship</strong>, run by the <strong>College of Pharmacy and Health Sciences</strong> in New York, trains <strong>Doctor of Pharmacy (Pharm.D.) graduates</strong> for specialist careers in the pharmaceutical industry. Fellows spend <strong>primarily two years</strong> working inside partner companies while also <strong>lecturing and doing research at St. John's University</strong> \u2014 a deliberate mix of industry practice and academic experience. For the 2027 cycle the university is hiring fellows across <strong>four practice areas</strong>: Medical Affairs (American Regent), Health Economics & Outcomes Research and Global Market Access (Pfizer), Clinical Development (Allergan Aesthetics, an AbbVie company) and Global Regulatory Affairs (PTC Therapeutics).</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li>Hold (or be about to complete) a <strong>Doctor of Pharmacy (Pharm.D.)</strong> degree.</li>
        <li><strong>International applicants are welcome</strong>, subject to programme requirements and US training-visa rules.</li>
        <li>Strong academic record and clinical rotation performance; prior research or internship experience is an advantage but not mandatory.</li>
        <li>Clear motivation for a <strong>pharmaceutical-industry career</strong>.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Competitive annual living stipend</strong> (exact figure not published in the programme materials).</li>
        <li><strong>Comprehensive health benefits.</strong></li>
        <li><strong>Professional development support</strong> across the multi-year programme.</li>
        <li>Hands-on industry experience plus <strong>university teaching and research</strong>.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Curriculum Vitae / resume</li><li>Letter of intent / personal statement</li>
        <li>Official Pharm.D. transcripts</li><li>Three letters of recommendation</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Open the official fellowship page</strong>St. John's University \u2014 Pharmaceutical Industry Fellowship Programs.</li>
        <li><strong>Submit CV + letter of intent by 23 October 2026</strong></li>
        <li><strong>Submit official transcripts + three recommendation letters by 27 October 2026</strong></li>
        <li><strong>Interviews</strong>Shortlisted candidates are invited for screening calls and formal interviews with faculty and partner-company representatives.</li>
      </ol>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Can Indian Pharm.D. graduates apply?","Yes \u2014 the programme welcomes qualified international applicants, provided they meet academic prerequisites and US visa requirements for training."),
 ("Is prior industry experience required?","No. Strong academics, clinical rotations and clear industry motivation matter most; experience is an advantage, not mandatory."),
 ("How long is the fellowship?","Primarily two years, depending on the track \u2014 combining industry placement with teaching and research at the university."),
 ("What is the stipend amount?","The university describes it as a competitive annual living stipend plus health benefits; the exact figure is not published in the programme materials."),
]),
 verify="Verified 16 Oct 2026 via St. John's University's official Pharmaceutical Industry Fellowship Programs page (one-/two-year post-Pharm.D. tracks training Pharm.D. graduates in specific industry practice areas; partners include Pfizer and AbbVie), corroborated by AfroCareer and Bright Scholarship (applications opened 1 Oct 2026; CV + letter of intent by 23 Oct 2026; transcripts + 3 recommendation letters by 27 Oct 2026; international applicants eligible).",
 offlinks=[('Pharmaceutical Industry Fellowship Programs \u2014 St. John\u2019s (official)','https://www.stjohns.edu/academics/schools/college-pharmacy-and-health-sciences/pharmaceutical-industry-fellowship-programs')],
 related_titles=['bloomberg-harvard','swiss-phd','griffith-vc'],
),

dict(
 slug='amazon-research-awards-fall-2026',
 title='Amazon Research Awards \u2014 Fall 2026 | StudyDesk Scholarships',
 meta='Amazon Research Awards Fall 2026: up to $80,000 unrestricted funds + AWS credits for faculty/NGO researchers in 9 AI & security areas. Apply by 4 Nov 2026.',
 short='Amazon Research Awards Fall 2026', kicker='Global \u00b7 Faculty/NGO researchers \u00b7 Research grant',
 mono='ARA', prov_short='Amazon', prov_long='Amazon Science \u2014 Amazon Research Awards (ARA)',
 h1='Amazon Research Awards \u2014 Fall 2026',
 sub='Unrestricted research funding from Amazon \u2014 for faculty and NGO researchers working on AI, security and cryptography.',
 dpill='19 days to go', dl_long='4 Nov 2026',
 facts=facts([('Award','Up to $80,000 + AWS credits<small>Unrestricted; no overhead</small>'),
              ('Who can apply','Faculty / NGO researchers<small>Worldwide; accredited institutions</small>'),
              ('Areas','9 research calls<small>AI \u00b7 security \u00b7 crypto</small>'),
              ('Deadline','4 Nov 2026<small>11:59 PM Pacific Time</small>'),
              ('Decisions','February 2027<small>One PI proposal per call</small>')]),
 body='''
      <h2 id="about">About the awards</h2>
      <p>The <strong>Amazon Research Awards (ARA) \u2014 Fall 2026</strong> is Amazon's academic research-funding programme. It is <strong>not a student scholarship</strong>: it funds <strong>principal investigators</strong> \u2014 full-time faculty at accredited institutions and permanent researchers at eligible NGOs \u2014 whose work falls under one of <strong>nine Fall 2026 research areas</strong>: Agentic AI; AI for Information Security; Amazon Security; Automated Reasoning; AWS Cryptography; Build on Trainium (agentic, recursive improvement of kernels and frameworks); Multilingual and Contextual AI Evaluation; On-Device Multimodal Perception; and Synthetic Data Generation for Multimodal Perception. Awards are structured as <strong>one-time unrestricted gifts</strong> (no administrative overhead), and each funded project is assigned an <strong>Amazon research contact</strong> plus training resources such as AWS tutorials and hands-on sessions with Amazon scientists and engineers.</p>
      <h2 id="eligibility">Eligibility</h2>
      <ul>
        <li><strong>Academic faculty:</strong> must be a <strong>full-time faculty member at an accredited academic institution</strong>.</li>
        <li><strong>NGO researchers:</strong> must be a <strong>permanent researcher at an NGO with recognised legal status</strong> in its home country.</li>
        <li>Researchers <strong>worldwide are encouraged</strong>, provided the institution holds official accreditation or legal status in its country.</li>
        <li>The proposal must address <strong>one of the nine Fall 2026 research areas</strong> with a clear research question, sound methodology and potential significance.</li>
        <li>A primary PI may submit <strong>only one proposal per call</strong>; one co-PI is permitted.</li>
        <li>An Amazon employee contact is <strong>not required</strong> to apply.</li>
      </ul>
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li><strong>Unrestricted funds</strong> \u2014 up to $80,000 depending on the call (about $70,000 on average for Agentic AI).</li>
        <li><strong>AWS promotional credits</strong> \u2014 up to $40,000\u2013$50,000 depending on the call.</li>
        <li><strong>Amazon research contact</strong> assigned to every funded project.</li>
        <li><strong>Training resources</strong>: AWS tutorials and hands-on sessions with Amazon scientists and engineers.</li>
      </ul>
      <h2 id="documents">Documents required</h2>
      <ol>
        <li>Research proposal prepared on the <strong>official ARA proposal template</strong> (about 4 pages max for most calls, plus appendices)</li>
        <li>Budget in USD (no administrative overhead)</li><li>Open-source contribution plan and AWS tools to be used (per call requirements)</li>
      </ol>
      <h2 id="how">How to apply</h2>
      <ol class="steps-list">
        <li><strong>Pick the right call</strong>Read the specific Fall 2026 call-for-proposals page on Amazon Science for your research area.</li>
        <li><strong>Draft the proposal on the official template</strong>Explain the research question, methodology, expected contributions, impact and fit for the call.</li>
        <li><strong>Submit through the official portal before 4 November 2026, 11:59 PM Pacific Time</strong></li>
        <li><strong>Decision letters</strong> are sent in February 2027.</li>
      </ol>
      <div class="honest-note"><strong>Not a student scholarship.</strong> ARA funds academic research led by faculty or NGO researchers \u2014 students cannot apply as PIs. PhD students may participate as part of a faculty-led proposal.</div>
      <h2 id="faqs">FAQs</h2>
'''+faqs([
 ("Is this a scholarship for students?","No. Amazon Research Awards is a research grant for faculty and NGO researchers. Students cannot apply as principal investigators."),
 ("Can researchers from India apply?","Yes \u2014 researchers worldwide are encouraged, provided their institution holds official accreditation or legal status in its country."),
 ("Do I need an Amazon contact to apply?","No. An Amazon contact is not required; funded projects are assigned one after selection."),
 ("How many proposals can I submit?","One per call as primary PI; a co-PI meeting the eligibility rules is allowed."),
]),
 verify='Verified 16 Oct 2026 via Amazon Science official Fall 2026 call-for-proposals pages (submission period 1 Oct \u2013 4 Nov 2026, 11:59 PM Pacific Time; decision letters February 2027; unrestricted funds up to $80,000 + AWS credits up to $40\u2013$50k; 9 research areas; PI must be full-time faculty at an accredited institution or permanent NGO researcher; one proposal per PI per call), corroborated by Opportunity Desk and ScholarGem.',
 offlinks=[('Amazon Research Awards \u2014 official CFP (Agentic AI, Fall 2026)','https://www.amazon.science/research-awards/call-for-proposals/aws-agentic-ai-call-for-proposals-fall-2026')],
 related_titles=['nasa-hubble','wb-gaf','bloomberg-harvard'],
),
]

for a in ARTICLES:
    cards = dict(REGISTRY); cards.update(CARDINFO)
    n = build_article(BASE, OUT, a, cards)
    print('wrote', a['slug'], n, 'bytes')
print('done \u2014 3 articles')

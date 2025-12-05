# SCDM Keynote, 2025

Claude: https://claude.ai/chat/c84b9387-271f-42f0-833c-18785782674b
Gemini: https://gemini.google.com/u/2/app/6f20f79d13f67671
https://chatgpt.com/c/6931b8f9-01a4-8321-b19a-fe0874befd64

- Set up Q&A on Slido
- What's different this time?
  - Natural language
    - The Shift from Structure to Language: Explain that for 50 years, computers were good at structured data (Excel, SQL). Today, for the first time in history, computers understand unstructured context (Language, Protocols, Physician Notes).
    - The Interface Revolution: For the first time in AI history, the interface is natural language - anyone can use it without coding. This isn't just "easier AI" - it fundamentally changes who can do data science.
    - #DEMO Policy as code
    - The Generality Breakthrough: Unlike previous AI that needed training for each task, LLMs are "few-shot learners." Show: Upload SDTM data → Ask about ICH E6 compliance → Generate protocol summaries → All with the SAME model, no retraining.
  - Stunningly Cheap, and becoming cheaper by the day
    - The Cost Collapse: What required million-dollar infrastructure 2 years ago now runs for dollars. Simon Willison would show the actual API costs - analyzing an entire clinical dataset might cost $0.50.
    - The Cost of Intelligence: Argue that the cost of basic reasoning has dropped to near zero. This doesn't replace the Data Manager; it gives every Data Manager 10,000 interns.
    - #DEMO LLM Pricing and cost of processing via LLM Foundry
- Demos
  - PDF Protocol -> extract the "Schedule of Assessments" and convert it into a tabular format for EDC setup. Radical efficiency in site startup.
  - Messy CSV wearable data or external lab data -> Find anomalies in this data that a simple edit-check might miss, e.g. Tuesday lab draws show anomalous LFT elevation trends, something an edit check won't catch. Data Cleaning (fixing typos) to Data Surveillance.
  - Inclusion/Exclusion criteria + A synthetic "EHR" dataset. Filter patient list for eligible candidates, allowing a 5% variance in BMI. Draft the investigator outreach email. Solve $8M/day delay cost by identifying patients instantly
  - Historical protocol + inclusion/exclusion criteria. "What patterns predict enrollment failures? Traceability: Cite sections. Provide alternative criteria, predict enrollment impact."
- Skills to develop
  - Audit AI logic. The "Jagged Frontier": (borrowing from Ethan Mollick) Show how AI is uneven—it can pass the Bar Exam but fail at simple math unless guided. This explains why "Human in the Loop" isn't just a buzzword; it's a safety requirement.
- Slido: Ask for email to get the video recording + chat links

# Meta-prompts

## PDF Protocol

What does a PDF protocol look like? Explain it to me as a layman.

> A **clinical trial protocol** acts as the master "instruction manual" for a medical study, defining the scientific goals, participant eligibility, and safety rules. Its most critical component is the **Schedule of Assessments**, a strict calendar that tells researchers exactly which tests and treatments must be performed at every patient visit.

What prompt can I give to an LLM that will generate a realistic protocol from which I can extract a schedule of assessments?

> Create a realistic clinical trial protocol (Phase 3) for testing a new diabetes medication called "Glucofix" vs placebo. The study should:
>
> STUDY DESIGN:
>
> - Randomized, double-blind, placebo-controlled
> - Duration: 24 weeks treatment + 4 week follow-up
> - Target enrollment: 450 patients across 50 sites in India
> - 2:1 randomization (300 on Glucofix, 150 on placebo)
> - Primary endpoint: Change in HbA1c from baseline to Week 24
>
> Generate the following sections:
>
> 1. Protocol Synopsis (1 page summary)
> 2. Complete Schedule of Assessments table showing all visits from Screening through Week 28
> 3. Detailed inclusion criteria (10 criteria)
> 4. Detailed exclusion criteria (15 criteria)
>
> For the Schedule of Assessments, include:
>
> - Visit timing: Screening, Baseline, Weeks 4, 8, 12, 16, 20, 24, and Week 28 follow-up
> - Assessments: Demographics, Medical history, Physical exam, Vital signs, ECG, Lab tests (HbA1c, FPG, Lipids, Liver function, Kidney function, CBC), Adverse events, Concomitant medications, Drug accountability
> - Visit windows (e.g., ±3 days)
> - Mark which assessments happen at which visits with X marks
>
> Make it realistic with:
>
> - Appropriate lab safety monitoring frequency
> - Front-loaded assessments at screening/baseline
> - Less frequent assessments as study progresses
> - Specific test names (ALT, AST, bilirubin, creatinine, etc.)
> - Realistic visit windows
>
> Format as a professional clinical trial protocol document.

## Lab Listings

https://chatgpt.com/share/6931a3d1-d914-800c-8bb2-e34982c91bf8

What prompt can I give to an LLM to create 50 pages of lab listings such that it will have MULTIPLE anomalies (e.g. temporal anomalies like elevated ALT readings on Tuesday)? I'd like the LLM to generate its own anomalies.

> You are a clinical data simulator. Generate 50 pages of realistic lab listings data for a diabetes clinical trial with MULTIPLE hidden anomalies that would be difficult for humans to spot but that AI should detect.
>
> STUDY CONTEXT:
>
> - 200 patients across 10 sites
> - 24-week study with visits at Screening, Baseline, Week 4, 8, 12, 16, 20, 24
> - Tests: ALT, AST, Bilirubin, Creatinine, HbA1c, FPG, Glucose
>
> CREATE THESE SPECIFIC ANOMALIES (but don't tell me which is which - I want to discover them):
>
> 1. TEMPORAL PATTERN: One site has systematically elevated ALT readings on Tuesdays 2-4pm (suggest instrument calibration issue)
> 2. GENDER BIAS: Female patients at Site 007 have creatinine values 15% higher than expected (suggest incorrect reference range being used)
> 3. SEQUENCE EFFECT: Every 5th patient enrolled at Site 003 has borderline high bilirubin at baseline (suggest screening protocol deviation)
> 4. SEASONAL DRIFT: HbA1c values at Site 009 gradually increase by 0.1% every month regardless of treatment (suggest lab drift/quality issue)
> 5. CORRELATION ANOMALY: At Site 005, when ALT >60, AST is always LOWER than ALT (biologically unusual - normally AST/ALT ratio should be different)
> 6. Add 2-3 MORE subtle anomalies of your own invention that would be realistic data quality issues
>
> FORMAT:
> Generate as CSV format with columns:
> Site_ID, Patient_ID, Visit_Name, Visit_Date, Test_Name, Test_Result, Unit, Normal_Range_Low, Normal_Range_High, Time_Collected, Lab_Technician_ID
>
> Make it realistic:
>
> - Normal values should cluster appropriately
> - Add natural variation
> - Include some normal out-of-range values (expected in real trials)
> - Include timestamps
> - Use realistic patient IDs (e.g., 001-001 through 010-020)
> - Spread data across dates from Jan 2024 to June 2024
>
> Generate at least 5,000 rows of data (approximately 50 pages when printed).
>
> After generating, create a SEPARATE document that lists what anomalies you embedded and where, so I can verify if my LLM detector finds them.

- Chat: https://chatgpt.com/share/6931a3d1-d914-800c-8bb2-e34982c91bf8
- Output: [lab-listings/](lab-listings/README.md)

## Inclusion/Exclusion + Synthetic EHR

https://chatgpt.com/s/t_6931a8227ca48191a52d11d3fe4c7d05

What do inclusion/exclusion criteria look like? What does a synthetic EHR dataset look like? What prompt can I give an LLM to generate realistic inclusion/exclusion criteria as well as a synthetic EHR dataset?

> Generate a complete synthetic dataset for a diabetes clinical trial recruitment scenario.
>
> PART 1: CREATE INCLUSION/EXCLUSION CRITERIA
> Create detailed inclusion criteria (10 criteria) and exclusion criteria (15 criteria) for a Phase 3 diabetes trial testing "Glucofix" vs placebo. Make them:
>
> - Specific and measurable (exact HbA1c ranges, BMI limits, etc.)
> - Realistic for diabetes population in India
> - Mix of simple criteria (age) and complex criteria (multiple lab values)
> - Include some that require checking medication history
> - Include some that require calculating values (eGFR from creatinine)
>
> PART 2: CREATE SYNTHETIC EHR DATABASE
> Generate synthetic EHR data for 1,000 patients from hospitals across 5 Indian cities (Mumbai, Bangalore, Delhi, Hyderabad, Chennai).
>
> Create 5 linked tables:
>
> Table 1 - DEMOGRAPHICS:
> Patient_ID, Age, Gender, Height_cm, Weight_kg, BMI, State, City, Hospital, Insurance_Type, Phone_Consent
>
> Table 2 - DIAGNOSES (with dates):
> Patient_ID, ICD10_Code, Diagnosis_Name, Date_First_Diagnosed, Currently_Active (Y/N)
> Include: Various diabetes types, hypertension, dyslipidemia, kidney disease, heart disease, etc.
>
> Table 3 - MEDICATIONS (current and past):
> Patient_ID, Generic_Name, Brand_Name, Dose, Frequency, Route, Start_Date, End_Date, Prescribing_Provider
> Include: All diabetes meds, BP meds, cholesterol meds, etc.
>
> Table 4 - LAB RESULTS (past 12 months):
> Patient_ID, Test_Date, Test_Name, Value, Unit, Normal_Range, Performing_Lab
> Include: HbA1c, FPG, Lipids, Creatinine, eGFR, ALT, AST, CBC, etc.
>
> Table 5 - VISITS (past 12 months):
> Patient_ID, Visit_Date, Visit_Type, Diagnosis_Codes, Provider_Name, Notes_Snippet
>
> CRITICAL: Make the data realistic by:
>
> - Having patients with varying eligibility (some clearly eligible, some clearly not, some borderline)
> - Include ~30% who meet ALL inclusion criteria
> - Include ~40% who fail on 1-2 exclusion criteria
> - Include ~20% with missing data that would need follow-up
> - Include ~10% edge cases (values exactly at cutoffs)
>
> Add realistic Indian context:
>
> - Common Indian names
> - Mix of government/private hospitals
> - Appropriate age distribution for T2DM
> - Regional medication preferences
> - Mix of English/Hindi/local language in some notes
>
> Output PART 1 as a Markdown file and PART 2 as a multi-sheet XLSX file that I can load into a Pandas dataframe or database.

## Historical Protocol + Enrollment Prediction

https://chatgpt.com/s/t_6931a88d12008191a220917d4ac8d551

To predict enrollment failures, what prompt would I give an LLM to generate realistic historical protocols, so that I can pass it to another LLM and have it find insights, e.g. specific criteria tend to fail in certain regions and therefore picking alternative criteria has a strong (quantified) predicted impact?

> You are a clinical trials database architect. Generate a synthetic dataset of 100 historical diabetes clinical trial protocols with their enrollment outcomes.
>
> For each protocol, generate:
>
> PROTOCOL CHARACTERISTICS:
>
> 1. Protocol_ID (e.g., DM-2018-001)
> 2. Study_Year (2015-2023)
> 3. Phase (2 or 3)
> 4. Therapeutic_Area (T2DM, T1DM, Obesity+T2DM)
> 5. Study_Duration_Weeks (12, 24, 26, 52)
> 6. Target_Enrollment (range 100-500)
> 7. Actual_Enrollment (realistically variable - some hit target, many don't)
> 8. Enrollment_Rate (%) = Actual/Target * 100
>
> INCLUSION CRITERIA (generate realistic variation):
> 9. Age_Min (18, 21, 30)
> 10. Age_Max (65, 70, 75)
> 11. HbA1c_Min (6.5, 7.0, 7.5, 8.0)
> 12. HbA1c_Max (9.0, 10.0, 10.5, 11.0)
> 13. BMI_Min (23, 25, 27)
> 14. BMI_Max (35, 40, 45, None)
> 15. T2DM_Duration_Months_Min (3, 6, 12, 24)
> 16. Required_Background_Meds (None, Metformin, Metformin+SU, Any, etc.)
> 17. eGFR_Min (30, 45, 60)
>
> EXCLUSION CRITERIA:
> 18. Excludes_CVD_History (Y/N)
> 19. Excludes_Insulin_Users (Y/N)
> 20. Excludes_Recent_Weight_Change (Y/N and threshold)
> 21. Excludes_Liver_Disease_Severity (None, Mild, Moderate)
>
> GEOGRAPHIC FACTORS:
> 22. Countries_List (e.g., "India, USA, UK" or "India only")
> 23. Regions_In_India (e.g., "Urban_Metro, Urban_Tier2, Rural")
> 24. Number_Of_Sites_Planned
>
> SITE-SPECIFIC OUTCOMES (for Indian sites):
> 25. Sites_In_India_Count
> 26. Top_Enrolling_State
> 27. Worst_Enrolling_State
> 28. Metro_Cities_Enrollment_Rate (%)
> 29. Tier2_Cities_Enrollment_Rate (%)
> 30. Rural_Sites_Enrollment_Rate (%)
>
> FAILURE ANALYSIS:
> 31. Primary_Enrollment_Barrier (free text: "HbA1c too narrow", "BMI ceiling excluded many", "eGFR requirement too strict", etc.)
> 32. Screen_Failure_Rate_Overall (%)
> 33. Most_Common_Screen_Failure_Reason
>
> MAKE IT REALISTIC with these patterns:
>
> - Narrower HbA1c ranges (e.g., 7.5-9.0) correlate with lower enrollment
> - BMI <35 cutoffs in India significantly reduce enrollment (Indian T2DM population often higher BMI)
> - eGFR >60 requirement excludes many older patients
> - Insulin exclusion is a major barrier (many Indian patients on insulin)
> - Metro cities (Mumbai, Bangalore, Delhi) have better enrollment than tier-2 cities
> - Rural sites have poor enrollment for complex protocols
> - Protocols with >10 exclusion criteria have 20-30% lower enrollment
> - Longer studies (52 weeks) have worse enrollment than shorter ones
>
> Create correlations so that ML/LLM can find patterns:
>
> - "HbA1c 7.5-10.5" + "BMI no upper limit" + "eGFR >45" + "Metro cities" = 90%+ enrollment success
> - "HbA1c 8.0-9.0" + "BMI <35" + "Excludes insulin" = 50-60% enrollment failure
> - etc.
>
> Output as CSV format with 100 rows.

## Policy as Code

I want to demonstrate that using natural language, we can extract rules from documents and apply them. I have an app at https://sanand0.github.io/policyascode/ (read it) that I I'd like to extend to clinical trial protocols - where we pass it a bunch of documents (policies), it extracts rules from those, and then applies it on a set of validation documents. What are good, realistic examples of such documents in the clinical trials space? Ideally, I would like the policies to be public documents - find these and link to them. For the validation documents, suggest a prompt for an LLM to generate 5 such documents, each flawed in a different way against the policy.

> I've added docs/e6r2-*.pdf which are sourced from ICH E6(R2) Good Clinical Practice - Main Policy (https://database.ich.org/sites/default/files/E6_R2_Addendum.pdf)
>
> Update config.json to replace the third demo "Operational Resilience (DORA) Readiness" with this new document set.
>
> Ensure that the extraction prompt and consolidation prompt are suitable for the following scenario where we're testing ICF structure compliance.
>
> For the validation documents, generate 5 REALISTIC informed consent forms for a Phase 3 diabetes clinical trial (fictional drug "Glucofix" vs placebo, 24 weeks, 450 patients). Each form should be 3-4 pages and follow standard ICF structure BUT contain DIFFERENT SPECIFIC VIOLATIONS of ICH E6(R2) Section 4.8 requirements.
>
> STUDY CONTEXT:
>
> - Study: "A Randomized, Double-Blind, Placebo-Controlled Study of Glucofix in Type 2 Diabetes"
> - Population: Adults 18-65 with HbA1c 7.5-10.5%
> - Duration: 24 weeks treatment
> - Visits: Screening, Baseline, Weeks 4, 8, 12, 16, 20, 24
> - Risks: Hypoglycemia, GI upset, rare pancreatitis
> - Sponsor: BioPharm Inc.
>
> STANDARD ICF STRUCTURE (use for all 5):
>
> 1. Title and study information
> 2. Introduction/invitation
> 3. Why is this research being done?
> 4. What will happen during the study?
> 5. Risks and discomforts
> 6. Benefits
> 7. Alternative treatments
> 8. Confidentiality
> 9. Compensation and costs
> 10. Voluntary participation and withdrawal
> 11. Contact information
> 12. Signature page
>
> CREATE THESE 5 FORMS, EACH WITH SPECIFIC VIOLATION:
>
> ---
>
> FORM 1: "Missing Required Elements"
> Violation: Missing several required ICH E6(R2) elements
>
> - OMIT: Clear statement that participation is voluntary
> - OMIT: Statement about trial being research
> - OMIT: Information about compensation for injury
> - OMIT: Circumstances under which participation may be terminated
> - Include everything else correctly
>
> ---
>
> FORM 2: "Inadequate Risk Disclosure"
> Violation: Insufficient detail about risks and procedures
>
> - Risks section mentions "possible side effects" but doesn't list specific known risks
> - No severity grading (mild/moderate/severe)
> - No frequency information (common/rare)
> - Missing information about foreseeable risks to embryo/fetus
> - Vague language like "some discomfort may occur"
> - Everything else is complete
>
> ---
>
> FORM 3: "Coercive Language & Exculpatory"
> Violation: Contains language that could waive subject rights
>
> - Includes statement: "By signing, you waive any right to sue the sponsor"
> - Emphasizes payment repeatedly, making it seem primary benefit
> - Uses pressure language: "This is a limited opportunity"
> - Minimizes risks: "These are minor and shouldn't concern you"
> - Overstates benefits: "Will definitely improve your diabetes"
> - Other sections complete
>
> ---
>
> FORM 4: "Inadequate Contact Information & Withdrawal Rights"
> Violation: Missing key contact details and withdrawal information
>
> - No IRB contact information provided
> - No 24-hour emergency contact
> - Withdrawal section says "you can withdraw" but doesn't explain HOW or WHEN
> - Doesn't explain consequences of withdrawal
> - Doesn't state that withdrawal won't affect future care
> - Other required elements present
>
> ---
>
> FORM 5: "Incomplete Confidentiality & Access Disclosure"
> Violation: Inadequate privacy and monitoring information
>
> - Doesn't explain who has access to medical records (sponsors, monitors, IRB, FDA)
> - No mention of regulatory authority inspection rights
> - Vague on how confidentiality will be protected
> - Doesn't mention HIPAA or data protection
> - Missing information about ClinicalTrials.gov posting
> - Other sections complete
>
> ---
>
> FOR EACH FORM:
>
> - Make it look professional and realistic (2-3 pages)
> - Use appropriate medical terminology
> - Include realistic study procedures for diabetes trial
> - Make violations SUBTLE but detectable by rule extraction
> - Don't explicitly label the violations in the document
> - Include signature page with date fields
>
> OUTPUT FORMAT:
> Generate 5 separate documents: docs/icf{1,2,3,4,5}.txt

# Question

Suggest topics for my keynote speech at SCDM 2025 conference on "Data to Decisions: Shaping the future of the clinical trial" in Hyderabad, India, Dec 4-6, 2025.

The organizers want me to (also) talk about: Why are we here at such a turning point in the domain of AI and LLM? What makes this moment in AI history so fundamentally different?

Think about popular AI evangelists, such as Ethan Mollick and Simon Willison. What would THEY talk about?

The transcripts of my preparatory calls with the organizers are below. Use them to suggest topics for my keynote speech.

## 2025-10-22 SCDM Keynote Discussion

**Arnab**: Hello?

**Anand**: Arnab, hi.

**Arnab**: Hi, Anand, good evening.

**Anand**: Good evening.

**Arnab**: Can you hear me?

**Anand**: I can hear you loud and clear, and you should be, yeah, able to see me as well.

**Arnab**: Thank you so much. First of all, thank you so much for joining and for your time. We are meeting or connecting for the first time, I believe. Yes. So, maybe we can start with a very brief round of introduction, just to know each other a little bit, and then I will get into the discussion to give you a brief overview about the keynote speech that we are looking at. And I'll also briefly explain the theme of the conference. And if you have any questions, of course, I'll be happy to take them up.

**Anand**: Sounds good.

**Arnab**: Is that okay?

**Anand**: Absolutely.

**Arnab**: Fantastic. I can start. My name is Arnab Sengupta. I am with Novo Nordisk now. I lead a team of data managers and programmers in Novo Nordisk, both in Bangalore and Copenhagen. I'm with Novo Nordisk for about two and a half years now, and an overall of about 20 years in the drug development in the clinical research field. I'm a biotechnologist by training, and then eventually I started initially with Accenture, and then I was with a CRO, a UK-based CRO called Kendle. And then, for the majority of my career, I was with Novartis for about 13 years, where I was with mainly in data management, but then more into the clinical data strategy, the digital transformation, and also different parts of the data analytics.

That's very briefly about me. **I am one of the co-chairs for the SCDM conference this year that's happening in Hyderabad**. And really looking forward to your insights as a keynote speech, Anand.

**Anand**: Thank you. Pleasure will all be mine. I am leading Innovation and R&D at Straive, which is a data, edtech, and science and research company, private equity-owned, that acquired the startup that my co-founders and I founded in 2012, which is Gramener. We started as primarily a data visualization company in 2012 and then moved on to analytics and AI post that. **The bulk of what I do at the moment is playing with ChatGPT and the APIs behind it**, trying to see what we can do with them and sharing ideas, creating demos, that sort of thing. Prior to that, I worked at Infosys Consulting for about seven years and at the Boston Consulting Group for about four years before that, and IBM, which is where I met my co-founders.

Most of my focus, as I mentioned, is on the AI side. The talks that or workshops, the talks that I deliver or the workshops that I run are **focused on how we can apply AI in day-to-day life**.

**Arnab**: Absolutely. Thank you. And that sounds really exciting. And I'll try to briefly explain to you the theme of the conference and what we are looking at. So, **this is the annual conference, the India version, of the Society for Clinical Data Management**. Although we call it the Society for Clinical Data Management, the kind of audience that you can expect, it's a mix of different experiences and different streams, but mainly linked to clinical research. The majority of the audience you will get are either data managers or the leaders in the field of data management, statistical programming, and also some of the risk managers and the central monitors who look more into the clinical operations aspect as well.

And this year, we actually thought a lot. We have been looking at different conference themes and seeing there is a huge focus on AI anyways, in general. And we thought that we will very subtly bring in the AI aspect, but **the main focus of the conference is on data**. **How we can use data in different ways and that can help in the clinical field, in the clinical research field, to enable data to decision**. And that's through insights, that can be through the different ways of acquiring data, and of course, the security aspect of the data, the quality aspect of the data.

And as you said very rightly, at the moment, what we are seeing as a trend is a lot of retrofitting of AI into the application. But what we are seeing is that if we could also set up the context that, instead of that, if we can **really identify the right business problems and then get to the right solution that can be driven by AI**. That is one aspect.

Secondly, we have been talking a lot about "human in the loop." Right? But I'm not very sure whether all of us understand very well what does it mean. We have our different connotations, our different understanding about human in the loop, but the main aspect that we would like to clarify throughout this conference across different sessions is what does it mean for the different roles to evolve with AI? So, I'm not sure how close are you with the data management and clinical research field, but over the last, say, about five to seven years, we have been talking about an evolution of the role of the conventional data managers in the clinical data field, more into clinical data science, which includes the critical thinking aspect, which includes not looking at data just as a data point, but really as part of the bigger decision-making framework and really applying both the scientific excellence, understanding the science, understanding the overall purpose of every clinical trial in terms of putting on a clinical data scientist hat.

That doesn't mean that overnight all the data managers will become LLM programmers or the data engineers, but **it's more about the mindset, the mindset change**. And as they are on that path over the last few years, now we are talking about generative AI and agentic AI and the human in the loop. So, my understanding is there is a little bit of confusion in the industry, especially for people who are, say, about two to five years, eight years, at the max 10 years of experience, to understand that what does it mean for us? And how are we really going to implement AI on our day-to-day job? How is AI booming in the real life, and not limited to the clinical research industry, but in the larger industry? And how can I connect to that with the right mindset and also have an understanding that, okay, this is what potentially AI can do in the next few years. And what should I do as a human being who is complementary to some of the AI solutions which are coming up, in terms of understanding my evolution in my role? So, that's the overall thought process within the co-chairs to bring in so that not necessarily we will talk about huge AI solutions, but we talk about more for people to get some take-home points that this is what AI can potentially do in the next five years, 10 years, but what does it mean for the human beings who are also part of different industries? So, I'll stop and I'll just spar with you and get your thoughts on this.

**Anand**: Very valid points and also the kinds of things that across domains people are asking and struggling with. What are the use cases? How do we bring in a human in the loop? How do we use it in day-to-day work? Exactly the kinds of questions that people are asking, with a few others that often pop up: safety. How does that play a role in this? How do we deal with hallucinations? Classic questions. What I'm curious about is... I might understand this better if I ask a little about the structure, the logistics... Actually, sorry, I'm jumping about, but when is the conference planned?

**Arnab**: **It's December 4th to 6th**.

**Anand**: And venue is likely to be?

**Arnab**: And yeah, and the keynote session... So, Day 1, which is the 4th, that's more a pre-conference workshop and other things. But the actual conference starts on the 5th of December. And the keynote speech is the starting point with your talk. **That's from 10:00 AM to 11:00 AM. It's a 60-minute keynote speech addressing the whole audience**. So all the people will be in one room. So, your keynote speech will be followed by the inauguration, and it's more about setting the tone.

**Anand**: Got you. Let me just make sure I block that time right away. It's 5th of December.

**Arnab**: It's Friday.

**Anand**: Friday, got it.

**Arnab**: 10:00 AM to 11:00 AM, and it's in **Hyderabad, HICC, Novotel**.

**Anand**: Got it. HICC.

**Arnab**: And I just wanted to have a discussion with you before sending a formal invite to you. So, by tomorrow, you will get a formal invite from SCDM with all the logistics and other things called out there.

**Anand**: I just wanted to check one thing about... not likely to be a conflict, but... the 5th Elephant winter 2025 edition... ah. Thought as much. Okay. There is a conference at Bangalore that I'm speaking at on the 4th of December. It's not an issue. I'll just have to time it accordingly. Oh no. No, I'm running a workshop which is on the 5th and the 6th. Fine. I will then request that it be planned on the 6th. So, that will allow me to complete this session and probably head out towards the second half. Sure. That handles one part. Next, you mentioned that these are people in the clinical data science space but is potentially varied. Roughly how many, what is the mix of seniority, what is the mix of functions?

**Arnab**: It's a real good mix. So we are expecting close to **between 900 to 1,000 people** in the room. And you can say around 30 to 40% of the people are between, say, two to 10, 11 years of experience. Another 20 to 30% between, say, 11 years to 15 years of experience. And then another, say, 30% of people who are like senior leaders coming from across India and also globally.

**Anand**: Got you. And in terms of domain or function?

**Arnab**: Yes. So, majority of them are coming from clinical data management or clinical data science. You'll find a few of them who will be coming from the statistics background, and then a few of them who will be coming more from the operations, trial management, and the risk managers and and others. But there will be a good 10 to 20% of people who would also be coming from core leadership across these domains.

**Anand**: Okay. It's a large number of people. What organizations are they typically from?

**Arnab**: Across all the pharma, CRO, BPOs. So, last year we had a footfall of close to a thousand people and from around 35 to 40 different organizations globally. But you can expect mainly coming from major pharma, the CROs, big CROs like IQVIA and ICON, and then some of the technology partners like Sama, eClinical Medidata, Veeva, and then some of the consultants like Accenture and a few from maybe Deloitte, but it sometimes they do not participate. But definitely Accenture and similar kind of consultants as well.

**Anand**: Understood. Perfect. Great. That is helpful. Now, coming back to thoughts on this, I must say that usually I don't plan the structure or even the content of AI talks or workshops more than a week in advance. **Things change so rapidly that it is found it to be a completely pointless exercise**. So, from that perspective, the brief that you gave me is extremely helpful, Arnab, because I get a sense of the kinds of problems people will want to tackle. Normally, the way I run sessions is to show stuff rather than tell. What's the fun in talking? But arguably, it's also a little boring to see a person just show stuff for a whole hour, for a couple of reasons. Monologuing for that long is boring intrinsically. But secondly, it also ends up not sinking in as much. Let's do something different. Before I... what comes to your mind?

**Arnab**: See, I mean, that's an interesting thought. I completely agree with you. So, in my mind, there are two aspects. One, the purpose of a keynote, typically in a conference like this, is to set the tone. I would not expect you to really get into the ground level and be granular about your thoughts, but it's also about setting the tone. But I completely agree with you, only talking about blue sky and the fluffy things may not really touch the right chord with the people. So, possibly it would be good to come up with a couple of stories that you own, that are a part of your experience, a part of your life, I mean, your professional life or your journey so far. I think that would be extremely useful because then people will see, "Okay, the person who is speaking in front of me has actually experienced and is talking about a story from his life." That typically strikes a chord with me. That's one part.

And second, and lastly, maybe picking up a couple of scenarios. And the scenario doesn't need to be from the pharma or from the healthcare, but the scenario is about some of the good practices or **busting some myths or other things**. And I'll tell you one important part that I am seeing more and more is an apprehension or a tentative approach towards an LLM, use of LLM or AI, in the drug development, in research, with **an unknown fear of non-traceability, or of an unknown fear that the health authorities would challenge us that we would not have answers to**. I do not necessarily agree with that personally, because my thought process here is, generative AI is something that we are in the early stage of our understanding. So, we should not call it a black box, but rather we should call it something that we are still exploring. And as long as we can show the step-by-step understanding and exploration of that, I think we should be good. I think 20 years or 25 years ago, when we started using the Bayesian model or other statistical models, it was an equally deep black box. I don't think every statistician used to understand that. But as long as they are able to explain how the data is being used and then eventually being a part of the decision making, it should be good. So, if you can also provide that confidence from your experience and the work that you are doing, that eventually we have to adopt that and it's not a black box, it's a journey, and we will be getting a lot more clarity on the other side of the journey, I think that would also be great.

**Anand**: That's a powerful thought. That leads me... or firstly, what I'm taking away then is at a meta level, **addressing some of the stated or even unstated concerns while showing them a path forward is a helpful theme**. To do that... this is the idea that struck me as you were speaking. Like you provided me some insights, **could I interview a few people**? I'll mention what kinds may be most helpful. To get a feel for where people are in their AI orientation, so to speak. And it will be... well, some possibilities are other speakers, panelists from the past, people you know who have a strong opinion, point of view, whoever. I mean, honestly, whoever comes to mind. Maybe just a quick... and it could be a joint discussion, one on one. Not more than two people, I think would be very helpful.

**Arnab**: That's totally fine. And that's a good idea. I can organize that in the coming few days. What kind of population are you looking for? Would it be okay to have different types of leaders, or are you looking for, say, a mix of leaders and people who are working on the ground or the subject matter experts?

**Anand**: Two leaders.

**Arnab**: Two leaders, right? Perfect. I think then it would be fantastic for you to connect with maybe the other co-chairs. They come from very different backgrounds, very different styles of leadership, different organizations. So, I think that should be a good variety for you to get different points of view.

**Anand**: Perfect. That sounds great. And we can do this on a single call if that works well. That will give me a more of a perspective. So, that's definitely one approach. The other is, I am a big fan of **bringing AI to the table**. If we can bring AI to the table, we can bring AI to the keynote. Meaning, why do I have to be the only person standing out there on stage delivering the keynote? **We'll have an LLM join me. Or a few models join me**. They know more than I do on the domain, for sure. And let it perhaps also... I think we can use that in two ways. One, **to be provocative, ask questions that people might hesitate to ask**, in a thoughtful way. And secondly, **to answer questions from a different perspective than I could think of**. So we can have it tuned to play the devil's advocate, maybe. So that, those were two thoughts that struck me as you were speaking, but I'm sure that as things evolve, all of this may change, and that's perfectly fine.

**Arnab**: That sounds very interesting. I have not seen any keynote so far in SCDM that actually had taken this kind of an approach. I think that's fantastic. You can also bounce your thoughts with a couple of other leaders that you're you'll be talking to. Maybe they can come up with some other thoughts that might strike. Yeah, I think that sounds good to me.

**Anand**: Perfect, Arnab. Then I've locked the dates. I'll look forward to your invite, both for the event as well as for catching up with the co-chairs.

**Arnab**: Sure. You can expect an invite and the detailed email from a person named **Praful Borachia**, and Praful will also be helping in setting up the two other calls in the next week.

**Anand**: Sounds wonderful. And where are you based out of?

**Arnab**: Singapore.

**Anand**: Singapore. I thought so.

**Arnab**: All right, Anand. Fantastic. Lovely meeting you.

**Anand**: Likewise. Take care.

**Arnab**: Take care. Bye-bye.

**Anand**: Bye, Arnab.

## 2025-10-30 SCDM Prabhakar

**Prabhakar**: I'm Venkata Prabhakar, with Novartis within the clinical data, a clinical programming and technology group, primarily responsible for the EDC team, which basically sets up the database for the conduct of the clinical trial. I have been with Novartis for more than nine years and close to 27 plus years within the clinical research industry.

**Anand**: Got you. I've been… sorry, no, I don't think you were done. Sorry, I interrupted you.

**Prabhakar**: Sorry, Anand?

**Anand**: No, no, please go on, Venkata Prabhakar. I think I interrupted you.

**Prabhakar**: Okay. So Anand, a couple of things I just made a note of myself and just to help you understand. This conference basically is being organized by SCDM, that is called as Society of Clinical Data Management, where predominantly most of the crowd that we will be having, who will be attending this particular conference, will be the clinical data management professionals.

And when I say clinical data management professionals, what exactly would be usually their responsibility when they are, when they carry out their work at any organization? Their primary responsibility is to ensure the quality of the data is very clean. Because whatever, whatever data that they collect from the conduct of the clinical trials, they ensure, their primary responsibility is to ensure that the data that they are collecting, they clean the data and ensure that the data quality is clean so that whatever insights they are going to draw from that particular data, that insights help them to make a better-informed decision.

So just to give a bit of context, what exactly this conference is, what is the audience that they are, that we will be expecting, and what is the primary work that they usually do in the organization and how they, how their primary work centers around data to ensure, and they are primary responsible to clean the data.

Now, let me take a step back to really help you understand with regard to how this entire thing has evolved. Maybe when EDC, that is the electronic data capture, this the EDC application came into existence somewhere way back in the year 2000. At that point of time, 70% of the data that is collected in the conduct of the clinical trial used to be collected, used to be collected within EDC. And the remaining 30% of the data used to be collected outside EDC, that is a third-party data, which could be labs, X-ray, ECG, biomarker, and all that stuff.

So the distribution of the data is 70% within the EDC and 30% within the, 30% of the data that is collected outside the EDC. And then the data management team usually use various approaches to clean the data, like through edit check programming, which is nothing but a logical consistency check to ensure the cleanliness of the data. They also use listings, or they use a reconciliation method, approaches, the QC steps. So these are some of the common methodologies that the data management team used to adopt to ensure the cleanliness of the data.

Now, over the last five years, with a lot of disruption on the technology front and a lot of technology evolution happening, the surge in the data has increased significantly. **And that's where this 5V concept comes into the picture, that is volume, velocity, variety, veracity, and value.** That 5V thing came into the picture because of so much of disruption on the technology front and that disruption on the technology had an explosion on the data front.

Now, the equation, now the equation, the distribution of data that has been collected within the EDC versus that is collected outside the EDC has changed. **Earlier it was 70% within the EDC, 30% outside the EDC. Now, after with this disruption on the technology front, 70% is being collected outside by the EDC system and only 30% is collected within the EDC system.**

**Anand**: I see.

**Prabhakar**: Now, what are some of this? And that is where this **clinical data scientist, that's a new role that the clinical data manager currently, if you see this this role that is being more prominent in the clinical data management space, where clinical data scientist what they call, what is that? Because with a lot of disruption in the technology and so much of volume of the data that is being collected, the traditional approaches of cleaning the data using edit check, smart listings, or manual listings, or reconciliation have their own limitations.** So that will not be a, that will not be a sustainable approach to clean the data.

And that's why now some of the advanced technology concepts like use of AI or ML or some of the deep technology or agentic AI, some of these deep technology things are being used to ensure, to pick up those trends, pick up those patterns, pick up those signals within that volume amount of data that is being generated. And pick up those signals and ensure the cleanliness of the data. Earlier they used to do, earlier we used to call it as data management because they used to manage the data. Now, more than managing the data, they are doing the, they are ensuring the surveillance of the data by using some of this deep technology and ensuring the cleanliness of the data.

Now, five years down the line, futuristic state. Now, now I am saying that 70% of the data is collected outside and 30% of the data is collected within the EDC. Now, a future state could be, maybe there could be no data that could be collected within your EDC and **100% of the data is collected through all your wearables, devices, apps, EHR, EMR, all the external data sources.**

Now, with that being the futuristic state, how the whole thing will evolve? What data cleaning techniques would be really applicable maybe in the near future? What some of this deep technology concept would be applied in order to pick up those signals, pick up those trends, pick up those patterns? It's like finding a needle within a haystack within the volume of the data that we might be generating.

So the whole role of clinical data manager would definitely evolve. Clinical data manager to clinical data scientist, that is what we call. Maybe from clinical data scientist, what it might be evolving into something different with all this disruptions and the amount of data that is being collected in the future, we don't know. So that is more of a futuristic state.

And that's the reason why if you see, if I tie all these things to the theme of the conference, "Data to Decisions: Shaping the future of the clinical trial," it's all about integrity, quality, security, and insights. So with this amount of data that we are collecting, how we can draw insights by using all this deep tech concepts into picture and how we can draw some insights, and how these insights would help us to make a meaningful decision about the drug, which in turn would help us to bring the molecule to the market faster and benefit the patient community.

And some of these applications, some of these applications of AI for trial spaces, one is where the trial design and protocol optimization. How AI can be used to optimize my overall trial because if I have a historical data of all the study protocols, can I really train my algorithm with all the study protocols? And if tomorrow I have to develop, I have to run a new trial, then can I have optimized, have precise inclusion-exclusion criteria and all the things optimized in such a way so that the probability of succeeding, the probability of conducting the trial successfully, having the patient enrolled as per the inclusion-exclusion criteria would be very, very high.

The second area where AI has been used predominantly is the patient recruitment. Finding a patient in the conduct of the clinical trial is one of the biggest challenges in today's conduct of the clinical trial. It's one of the biggest challenges. Now, how AI can help me to really surf the data? So if AI can surf across all the data sources like EHR, EMR, patient data registries, or any other sources where patient-related information is there and can tell me, okay, as soon as I feed my study protocol to the, within the, within that particular system, based on the study design, based on the criteria that you are trying to, based on patient population, it can tell me, okay, if this trial is to be conducted and this is the patient population that you are looking for conduct of the clinical trial, these are the sites where you can find the patient population. So then, once, because if patient availability is known to us much well in advance, then I can start the trial much early, I can complete the trial in a timely fashion because every day delay of, every day delay, I think historical or literature reports state that a delay of conducting the trial, I think it's cost the pharma organization close to 40 million to 8 million, 40k to 8 million dollars per day. That is the loss that a organization incurs for one day delay. And we can imagine if the launch of a drug get delayed by a week or a month, then what is the cost that the organization will be incurring? So how all those unnecessary costs can be cut down with AI coming into play and addressing some of the basic problems, some of the burning problems, and one of the main burning problems in the conduct of the clinical trial is identification of the patient, and that's where AI can help significantly.

The third area is data management and monitoring. Now, we have been talking about, at the start of the conversation I mentioned that earlier when the data manager had to clean the data, they used to use edit checks, smart listing, they used to take the dump of the data, do line-by-line review and say, okay, this is the discrepant data, go and raise a query and ensure that query get resolved and the data is getting cleaned. But now with AI coming, with such voluminous amount of data, those approaches will be an ineffective approach. So how AI can help in identifying some of the signals which would be beyond a human eye detection? A human eye cannot catch some of the hidden patterns within the data. So how those patterns, how those signals can be picked up from the data and we can address some of these challenges much proactively rather than getting caught at a later point of time, which could disqualify my submission and that disqualification of my submission of the study results could also cause harm to the patient population tomorrow, because the patient who is looking forward for this particular drug to come into the market, they have to wait for another extended period of time till another treatment is available in the market. That's why how I can identify some of the data-related issues, data-related things by using AI is the another area where we can really look forward to.

The next is the decentralized clinical trial. The decentralized clinical trial is another way, another effective way of conducting the trial where, if we look, if we look the earlier, earlier way how clinical trials have been conducted where the patient had to go to the site, they had to where the principal investigator would administer the treatment, they would measure their vitals, they would take the readings of all the things that they would be recording as per the protocol. But decentralized has really changed. Post-COVID, decentralized way of conducting the clinical trial has changed the entire landscape of how clinical trials are conducted. Which means that the trial has come to the patient's home. Now, you can, you can, you can conduct, you can, you can participate in the clinical trial from the comfort of your own home by making use of some of these advanced technologies. You need not have to step out of your comfort zone. You don't have to reschedule your, some of your personal things that you have planned for. You don't have to disturb, without disturbing any of these things, you can still participate in the conduct of the clinical trial. Which means technology will be playing a very, very key role in the conduct of the clinical trial. The moment when we are talking about technology, the amount of the data that will be collected will be humongous. And that's where again, AI can play a significant role in picking up those signals. That's where the data manager can be playing more a role of a data surveillance manager rather than cleaning the data. He will be surveying the data to really pick up those trends, pick up those signals, pick up those patterns and see how to ensure the integrity of the data, how to ensure the quality of the data so that the rejection of the data when it is submitted to the regulatory authority would be very, very minimal or completely zero.

So these are some of the use cases where AI can play a critical role or important role in the conduct of the clinical trials, Anand.

**Anand**: Prabhakar, this was almost a masterclass in 10 minutes of what a clinical data scientist or manager would do. So thank you for that. I seriously have a question.

**Prabhakar**: And one thing, and one thing maybe you can also focus upon is that, from clinical, earlier when the ratio was 70:30 and then now it is 30, it is 30, just a minute, and now it is 30% of the data within EDC and 70% within, outside the EDC, you can also touch base upon, **what skill set does this data manager really need to equip themselves with in order to really become a data scientist?** And talking when you are talking, concluding your presentation, giving them a perspective about the futuristic state where imagine one scenario could be 100% of the data is coming from the external sources or maybe 5% to 10% data being collected within the EDC. If that is the state that they are looking, then what is that skill set? What is that technical competency? What is the soft skill that they really need to equip themselves so as to be relevant within this particular industry? Maybe that is one of another area where you really can emphasize because people will look forward for, okay, this is fantastic, but I am playing a particular role, then what is that you really want me to equip upon? What is that competency, one or two competency that you want me to build upon so that I can be still relevant in this industry maybe five years down the line, in spite of all this disruption that is happening on the technology front.

**Anand**: Fabulous. Critical area to focus on, and that is something I can touch upon. I did have a question on the earlier areas. I would love to demonstrate some of the futuristic technologies, and obviously that will mean playing around with some data. Now, I would be able to generate synthetic data in a realistic form, but I'm curious, what are some kinds of synthetic data or what are some datasets that these teams operate on? If you could just give me a glimpse or a walkthrough of that, I can feed that to an LLM and have it generate some synthetic data.

**Prabhakar**: You mean the use of synthetic data is what you mentioned, Anand?

**Anand**: No, no. Sorry. Let me simplify what I asked. Could you give me some examples of datasets that people work on when cleansing or during trial design?

**Prabhakar**: Okay. So, the predominantly when you are, the data manager usually if they have to, if I look at, let me put it in a different way. So, if you look at the study protocol, the three areas, the safety data, the efficacy data, and the primary and secondary parameters, safety and efficacy, these are the primary two datasets they usually focus upon. When you say safety, it could be adverse event, medical history, concomitant medication. Those are the three datasets I can think of. Efficacy, when I say of efficacy, if it is a hypertension trial, then blood pressure reading is your primary dataset, systolic and diastolic. When you're talking about the diabetes trial, then FPG, PPG, and HbA1c is the primary efficacy data parameter. Whereas safety data and parameters definitely will be constant. Adverse events, safety adverse events, concomitant medication, medical history, that will be constant irrespective of the therapeutic area. But your primary dataset, depending upon the indication that you're studying, if it is a diabetic trial, these are the parameters. If it is hypertension, these are the primary parameters. So that way you can really try to say, okay, depending upon which therapeutic area dataset you are really looking for the case study, you can accordingly try to have the datasets for that particular therapeutic area.

**Anand**: Understood. And what about from a trial design perspective? Is that different?

**Prabhakar**: Yeah, trial design basically, it's a, it's a double-blind study, usually. Most of the time it is a double-blind.

**Anand**: Got you. With the data…

**Prabhakar**: Two-treatment, double-blind study usually. So you have a test versus a reference comparator. It's a double-blind where your patient doesn't know and your investigator also doesn't know which treatment is being given to whom.

**Anand**: Got you. And what is the nature of data that they process here? What's the nature of data?

**Prabhakar**: What is the nature of data?

**Anand**: Meaning what kinds of columns? Sorry Anand, I couldn't get…

**Prabhakar**: Sorry Anand, I couldn't get…

**Anand**: Sorry, sorry. What kinds of columns are present in such datasets?

**Prabhakar**: Maybe I can drop your email. I don't have something on top of my mind, but if you want, maybe for a, you mean to say for a safety dataset and for a, for an efficacy dataset, what are the various columns that you have under each of these? Is that the question that you have?

**Anand**: Yes, please. Yes.

**Prabhakar**: Maybe I can drop you an email. Okay, these are the various columns. If let me take a couple of examples, maybe for blood pressure, hypertension trial and maybe for a diabetes trial. And if these are the dataset, safety dataset and efficacy dataset, then these are the various columns of data points that we usually consider for this particular dataset.

**Anand**: Perfect. That would be wonderful and that will give me a starting point. Prabhakar, this answers more than the questions that I had, actually. So thank you so much for this. My plan will then be aligned around the five areas that you mentioned: cleansing, trial design, data monitoring, decentralization of clinical trials, and future skills to build.

**Prabhakar**: Perfect, Anand. I can just send you an email. Just give me a day's time. I will get this information, maybe for two therapeutic areas, what are the various columns within this dataset. I can just email you. So maybe that can help you to structure your presentation accordingly.

**Anand**: That will be fabulous. Thank you so much. And thanks a lot, Praful for organizing this.

**Prabhakar**: Thank you, Anand.

**Anand**: Have a good day.

**Prabhakar**: No problem.

**Praful**: Anand and Mr. Anand, if before you conclude just one thing that we would need from you on an immediate basis is your topic for the session and a description because we intend to promote the session to encourage participation. So that is something that we would need it from you by next Tuesday.

**Anand**: Yes, I had mentioned earlier… oh sorry, I think that's background. But anyway, sorry, when I was talking to Arnab, I had mentioned that once I get a little more input, I should be able to formulate that. I now have that input. So yes, by Tuesday you will have a title and a brief. No problem.

**Praful**: Fair enough. So I have tentatively put it as next Tuesday in my calendar to have it with us for promotions. And the second thing to mention is about the registrations. The speakers have discounted rates to register. So after this call, I had sent it to you previously, but I'll re-check regarding registration. And third thing is the accommodation. We also have discount…

**Anand**: Yes, Anand, you have… Sorry, I'm trying to understand. So **I give a talk and I pay you? That's interesting.**

**Praful**: Yes, the speakers also have to pay to attend the conference.

**Anand**: I see. Why would I want to share my knowledge and pay in return for nothing?

**Prabhakar**: Anand, sorry to interrupt. Praful, can you just take this offline with Bhavesh on this particular thing?

**Praful**: I'll do that. I'll do that. So he will discuss with Bhavesh and get back to you, Anand.

**Anand**: Sure. If it helps, I'm not planning to… got the point from where you are coming, but definitely I will ask him to check with Bhavesh and get sorted out.

**Prabhakar**: Sure.

**Anand**: And to convey to Bhavesh also that I will, I promise not to, A, come before my talk, stay after my talk. I will leave immediately. I will not promote anything. And I will make my talk public, which is how I operate, which is also something that I had shared earlier. And my talks page also mentions that I neither pay nor charge for my talks. So please just convey this to Bhavesh. I did not realize that there is a speaker fee involved.

**Praful**: Thanks, thanks for sharing your opinion. I'll get back to you with the confirmation very soon on this on the fee waiver for the registration.

**Anand**: Sure. Thank you. And Anand, once we have the topic and description with us, if you are comfortable to share a promotional video, that is also something that you can do. It's not mandatory, but if you're comfortable to share.

**Anand**: Got you.

**Praful**: Just if we can have it in our social media campaigns.

**Anand**: Got you. Perfect.

**Prabhakar**: Thanks, Anand.

**Anand**: Thanks, Anand. Thanks, Prabhakar.

**Prabhakar**: Bye.

## 2025-11-26 SCDM Arnab

**Arnab**: Hey Anand, good morning. How are you doing?

**Anand**: Morning. How are you doing? Very well.

**Arnab**: Good, good. Thank you for your time and accepting on short notice. I thought it would be good to have a quick connect for two things. One, to understand how you are planning to deliver the session, and then align on how much time we should keep for the quick chat. I have some plans in terms of **three to four large themes of questions**, but I wanted to also connect that to your overall presentation so that it looks like a continuous storyline. I would hand it over to you for a quick overview of the presentation, and then I can take it over.

**Anand**: The flow will be: **how can people use LLMs at every stage of the clinical data management pipeline**. Going based on the discussion that I had with Prabhakar, there are clear areas—beginning with the standards that the audience would be using, which is where the worst pain point lies—where the largest delays are, whether it is site startup, recruitment, etc. In each of these cases, for data sourcing, how can we use modern LLMs? For analysis, how can we use modern LLMs? For insight extraction, how can we use them? And for interpretation and storytelling, how can we use them? **So, three end-to-end cycles is how I am thinking, with real or realistic data.**

**Arnab**: And are you going to use any stand-in slide, or is it completely going to be on the fly? How do you plan to start? Is it without a slide, just addressing the audience?

**Anand**: I will probably take 10 to 15 seconds to explain what I am going to do, which is a shortened version of what I just told you, and then jump into it. The talk will basically begin roughly like: "Let's say you have this kind of data." And they will see the data on Excel. Now, you can't figure out heads or tails out of it, or there are these sets of problems—or heck, you don't even know what problems there are. What can we do with it? **Upload it to ChatGPT and ask it the question, and it will start crunching out some answers.** That is how the session will go.

**Arnab**: I have just one suggestion because it's a keynote and it will also set the tone for the remaining conference as well. If you could also use around a couple of minutes to start with to set the context. My thought process was—hold on.

**Anand**: That is a great thought. How about then we swap the order? **Begin with the chat, which will set the context, and then I can dive in.** Because that does two things: one, you will have the opportunity to bring the audience on the page together, and I will also have an opportunity to, in the session itself, focus more on the demo. It is a thought. What do you think?

**Arnab**: I think flow-wise or logically it's good, but I am also thinking from the optics point of view. Typically, it is a lot better feeling that a keynote speaker starts instead of starting with a chat because optically it is a little odd. So, what I was thinking is that if you can just start with a larger context: **what is so special about LLM in the current time?** People are talking about LLMs and GenAI across industries. The healthcare industry, especially being so regulated—we are probably catching up, but still, there is a hype and there is a reality. But irrespective of that, we all are talking about LLMs and GenAI. But what is so special about LLMs and the current time worldwide? If you can just start with this context, then people will be able to connect a lot better regarding why we are talking about LLMs in healthcare, and then you get into your demo.

**Anand**: Understood.

**Arnab**: There are three aspects that I am planning to bring up during the chat. **First thing is the governance, validation, traceability part.** For the healthcare industry especially, it is going to be super critical. Sometimes we talk about the black box concept, we talk about our lack of understanding about the bias, our lack of understanding about the hallucination and many other things. Currently, the way I see the healthcare industry, it is clearly split into two parts. One part of the industry or the leadership, they are absolutely open and pushing the use of LLM as much as possible; they are trying to be the pioneer. And the other part of the industry, they are still very tentative. They think, "Okay, this is still the black box, we still don't understand, there is still a bit of bias and hallucination that we do not understand, hence we probably cannot answer all the questions from the health authority." So that is why I would bring up one point in the chat: **your perspective on the traceability, explainability, and validation of the models.**

**Anand**: Before we go to the second point, there are some things here that I could show. We can do this in one of two ways. I had initially not planned to bring it up in the keynote, but since you mentioned this and it is very important, I can either show a few things during the chat if that's an option.

**Arnab**: Yes, that is possible. That is totally fine.

**Anand**: However, based on how we are seated—from where I am seated, will I be able to operate my laptop and show that demo?

**Arnab**: Logistically, I will check that at the venue. I will keep that in mind regarding whether we change the seating arrangement and we both sit on a chair face-to-face, or we just keep it a little informal and you are still with your laptop and I just walk around. We can definitely sort it out.

**Anand**: One option that I have used in the past is, after my keynote, I continue on the podium, and you come over—if required bringing other people, etc., some of whom are seated—or you are standing, walking around asking questions is also an option.

**Arnab**: Perfect. The other aspect during the chat that I was thinking about is a little bit of **demystifying the hype versus reality**. I would also like to connect that to the future clinical data scientists or the evolved clinical data managers—the future of clinical data management. They would like to understand: **Is it all about coding? Or at some point in time, do we really need even coding to use LLM?** How is that space evolving in the back end and front end of the LLM applications? Maybe in a very simpler way, how a data manager or a data scientist can go about thinking of the usability of LLM. What should be their thought process? A lot of people are super interested, they are very enthusiastic, but they don't know where to start.

**Anand**: Got you.

**Arnab**: And the third one is more about where do you see the future with LLM in the next three to five years? Because currently, we are seeing the technology landscape—the LLM landscape—is changing so fast. We are not even confident what technology to bring in because we don't know whether that will be relevant in the next three to five years. **So, in the LLM space, how does the future look like?**

**Anand**: Sure.

**Arnab**: I will send you these three broader themes so that you can also think through how you would like to respond. I thought of four: the initial context that you are anyway taking care of in the beginning of your talk, and then I will bring in these three.

**Anand**: That sounds perfect.

**Arnab**: Thank you. Very excited. When are you reaching Hyderabad?

**Anand**: Let me just check my schedule. Actually, I am reaching the previous day. I'm going to be there at our office. So I can be there at the venue at least half an hour ahead of time. We start at 9:00 something, right?

**Arnab**: Yes. Where are you staying?

**Anand**: 9:30. I am staying most likely at Deccan Serai, Gachibowli.

**Arnab**: Okay. Super. I think it is very close. Should not be a problem. All right, sir. Thank you. Speak to you soon.

**Anand**: Very well. Bye.

# AI ideas for the IIT Madras Office of Institutional Advancement

As of 2026-03-18, my picture of the audience is:

## Who they are

The Office of Institutional Advancement (OIA) looks like IIT Madras' fundraising and relationship engine for alumni, corporates, foundations, and trusts.

- IITM's OIA site says the office was founded in **2015** and exists to build partnerships and raise funds for IITM's Strategic Plan 2027, including research, technology, education, and infrastructure.
- The same site says OIA also drives **CSR partnerships** and technology-led social-impact programs.
- The Joy of Giving platform and team page show a fairly mature advancement stack, not a small ad hoc office. Publicly visible roles include:
  - Dean, Alumni & Corporate Relations
  - CEO, OIA
  - Vice President / Senior Vice President
  - Alumni & HNI leads
  - Digital Marketing
  - Operations
  - Alumni Relations
  - Senior Advancement Officer
- Public scale signals are large:
  - OIA says IITM has **50,000+ alumni** and **140+ corporate partners**, and was implementing projects worth **INR 200+ crores** across India at the time that page was published.
  - Joy of Giving currently shows **1,500+ projects**, **15,000+ donors**, **1,500+ Cr received**, and says OIA engages **55,000+ alumni across 82 countries**.
  - IITM's convocation coverage says the Office of Alumni and Corporate Relations plus OIA raised **INR 320 crores in 2024-25**, including **INR 124.4 crores from Key Alumni** and **INR 195.20 crores under CSR**.

## What they do

From the public footprint, OIA appears to run four overlapping motions:

1. Alumni fundraising and stewardship
   - annual giving
   - batch reunion campaigns
   - scholarships
   - endowed funds
   - departmental / institute projects

2. Corporate and CSR partnership development
   - identifying aligned corporate partners
   - shaping CSR narratives
   - routing projects into fundable social-impact themes

3. Donor communications and public proof
   - project pages
   - donor reports
   - testimonials
   - donor wall
   - impact stories
   - Alma Matters style content

4. Operational plumbing
   - tax / wire / giving channels
   - donor servicing
   - project catalog maintenance
   - cross-border donation routes
   - reporting and campaign administration

The March 17, 2026 prep call adds a crucial working detail: they explicitly described themselves as people from **sales, marketing, and fundraising**, operating in **high-touch sales scenarios**.

## How they seem to work

This section mixes direct evidence with inference.

### Directly from the 2026-03-17 transcript

- They already have **basic literacy in generative AI**. They do not need "what is GenAI?" explanations.
- They want help with **lead generation**, **lead conversion**, and **profiling of people**.
- They see immediate value in **everyday productivity**, especially in **Excel, PowerPoint, Word, summarization**, and tools like **NotebookLM**.
- Their work involves **many meetings**, and they often need to create a **profile**, **presentation**, or briefing rapidly, sometimes on the spot.

### Inferred from the public OIA / Joy of Giving footprint

- They are likely a **relationship-memory-constrained organization**. The public footprint implies a lot of knowledge is scattered across emails, decks, donor notes, campaign pages, event discussions, and project documents.
- They are likely **content-heavy and proposal-heavy**. Advancement work at this scale means repeating variants of the same tasks: donor briefs, case statements, update notes, stewardship messages, event collateral, and internal summaries.
- They likely face a **personalization-at-scale** problem. It is hard to make every donor, alum, corporate partner, and reunion batch feel individually understood when the portfolio is this broad.
- They almost certainly operate under **soft compliance constraints**, even if not framed that way: accuracy of donor facts, naming conventions, project eligibility, tax / documentation correctness, brand tone, approval chains, and stewardship consistency.

## Current challenges

### Explicitly stated

1. They know AI exists, but they feel they have **blind spots** about what good usage actually looks like.
2. They want better AI help on **lead generation**, **lead conversion**, and **profiling**.
3. They want big gains in **daily office work**, not only flashy strategic use cases.
4. They operate in **meeting-heavy, high-touch relationship work**, which creates constant demand for quick briefs and decks.

### Inferred from sources

1. They need a better way to turn unstructured relationship data into reusable institutional memory.
2. They likely need faster ways to produce high-quality donor-facing and leadership-facing material without losing accuracy.
3. They need AI patterns that are safe for a non-engineering team: simple, reviewable, and easy to govern.
4. They need adoption patterns that fit specialists in fundraising, digital marketing, alumni relations, and operations, not only "AI enthusiasts."

## The 5 I would emphasize live

If time is short, these are the five highest-impact ideas that seem both useful and somewhat non-obvious for this audience:

1. **Turn every important meeting into reusable intelligence, not just notes.**
2. **Let AI search private workspace context and create the first donor / partner briefing pack or deck.**
3. **Treat digital exhaust as an advancement asset: chats, transcripts, event logs, and CRM notes are raw material.**
4. **Convert recurring work into machine-readable workflows with tests, risk tiers, and review gates.**
5. **Use AI as a checker first for high-stakes work: maker-checker, consensus, and checklist validation.**

## Detailed tip inventory

### 1. Turn every important donor, alumni, or corporate call into a reusable intelligence asset

- **Source:** [Transcribe call recording](https://www.s-anand.net/blog/prompts/transcribe-call-recording/), [Analyze Call Recording](https://www.s-anand.net/blog/prompts/analyze-call-recording/)
- **Description:** Record important calls, create a clean speaker-aware transcript, then ask AI to extract personas, beliefs, invalid assumptions, missed conversational cues, next steps, and experiments to try next.
- **Why this should hit for OIA:** Most teams stop at a summary. The non-obvious leap is to use AI to surface what each side **missed**, what signals were buried in the conversation, and how the next interaction should change. That is directly relevant to lead conversion, profiling, and high-touch relationship building.

### 2. Let AI search your Drive, mail, attachments, and the web, then build the first account brief or deck

- **Source:** [Using Gemini to create slides](https://www.s-anand.net/blog/using-gemini-to-create-slides/), [Transcript AI-ded interviews](https://www.s-anand.net/blog/transcript-ai-ded-interviews/), [O3 Is Now My Personalized Learning Coach](https://www.s-anand.net/blog/o3-is-now-my-personalized-learning-coach/)
- **Description:** Use Gemini / ChatGPT-style research workflows to scan private workspace material plus public information, then produce a donor brief, company profile, meeting prep memo, or first-pass presentation.
- **Why this should hit for OIA:** This is almost exactly what Kaviraj described: "I am going to meet a customer and need a quick PPT from a lot of information." The part they may not know is that the best workflow is not generic web search. It is **workspace-grounded synthesis** over mails, attachments, past decks, and institutional memory.

### 3. Build a meeting-to-CRM loop using structured outputs

- **Source:** [AI Advice](https://www.s-anand.net/blog/ai-advice/), [Things I learned on 2024-03-23](https://til.s-anand.net/2024-03-23.html)
- **Description:** Ask AI to return fixed fields after a meeting: person, organization, relationship strength, likely interests, ask type, objections, next action, confidence, open questions. Store that in a CRM or at least a structured notes sheet.
- **Why this should hit for OIA:** The hard part in advancement is rarely "write a paragraph." It is turning messy interactions into something operationally usable. Structured outputs are what make AI useful beyond the chat window.

### 4. Treat digital exhaust as a fundraising and alumni-engagement asset

- **Source:** [Mining Digital Exhaust workshop 2025](https://www.s-anand.net/blog/mining-digital-exhaust-workshop-2025/), [Vibe Analytics](https://sanand0.github.io/talks/2025-12-03-vibe-analytics-iim-alumni-sg/), [WhatsApp Group](https://www.s-anand.net/blog/prompts/whatsapp-group/)
- **Description:** Mine WhatsApp groups, event chats, webinar transcripts, email threads, CRM notes, and internal discussion logs for topics, bridges, influencers, recurring asks, drop-offs, and sentiment shifts.
- **Why this should hit for OIA:** OIA almost certainly sits on a lot of underused exhaust: reunion groups, chapter chats, donor conversations, event feedback, internal planning threads. The non-obvious insight is that these are not archival leftovers. They are a rich intelligence layer for relationship strategy, segmentation, and community health.

### 5. Convert every event, AMA, or donor-facing session into derived products

- **Source:** [AfterSlides: Write Slides After Talks](https://www.s-anand.net/blog/afterslides-write-slides-after-talks/), [Create an FAQ-style slide deck from a transcript](https://www.s-anand.net/blog/prompts/afterslides/)
- **Description:** After any webinar, donor roundtable, alumni session, or leadership discussion, transcribe it and auto-generate FAQ decks, recap notes, quizzes, errata, counterpoints, and feedback.
- **Why this should hit for OIA:** One event can become many assets: follow-up decks, internal knowledge, donor recap notes, searchable FAQs, and onboarding material for staff. This is a strong force multiplier for a communications-heavy team.

### 6. Write repeatable advancement work like APIs: inputs, outputs, done-when, tests, and risk tags

- **Source:** [Redefining Work in the LLM Era](https://sanand0.github.io/talks/2025-09-llm-workflows/)
- **Description:** For tasks like prospect briefs, thank-you drafts, project-page updates, alumni-reunion follow-up, or CSR opportunity scans, define:
  - inputs
  - expected output
  - "done when" tests
  - exceptions
  - green / amber / red risk levels
  - logs of who or what did each step
- **Why this should hit for OIA:** Most offices begin with prompts. The stronger move is to define the workflow itself. This is what makes AI repeatable, governable, and delegable across staff. It is also the best bridge from experimentation to actual operating leverage.

### 7. Use AI as a checker first, especially when being wrong would be embarrassing

- **Source:** [Double-checking reduces hallucinations](https://www.s-anand.net/blog/double-checking-reduces-hallucinations/), [AI Advice](https://www.s-anand.net/blog/ai-advice/)
- **Description:** Use one model to generate or extract, another to check, and escalate disagreements to a human. This works for donor tags, employer names, cohort extraction, call-note classification, project coding, and similar medium-volume tasks.
- **Why this should hit for OIA:** Advancement teams need high accuracy but usually do not need full manual review on everything. Maker-checker AI is a practical path to better quality without exploding effort.

### 8. Turn policy prose into checklists and validators

- **Source:** [Data to Decisions with AI](https://sanand0.github.io/talks/2025-12-05-scdm-keynote/), [Policy as Code demo](https://sanand0.github.io/policyascode/)
- **Description:** Convert gift rules, naming rules, approval conditions, stewardship requirements, event protocols, and brand constraints into checklist-style prompts or machine-checkable validators.
- **Why this should hit for OIA:** AI is safest and strongest where validation is "harmless." The big non-obvious use case is not "write the donor note from scratch," but "check whether this note, deck, or proposal violates any rules before it goes out."

### 9. Use AI to interview busy experts before writing case statements, proposals, or decks

- **Source:** [Voice Chat to Slides: My New AI-Powered Workflow](https://www.s-anand.net/blog/voice-chat-to-slides-my-new-ai-powered-workflow/), [AI Advice](https://www.s-anand.net/blog/ai-advice/)
- **Description:** Have AI interview a dean, professor, fundraiser, or institute leader, then convert that conversation into Markdown, a briefing note, a deck, FAQs, or a draft narrative.
- **Why this should hit for OIA:** Advancement often depends on extracting context from people who are busy and hard to schedule. Interview-first capture is a much better workflow than asking them to "send notes" or waiting for a polished write-up.

### 10. Personalize stewardship and recognition at scale

- **Source:** [Turning Generic Gifts Into Joy with AI](https://www.s-anand.net/blog/turning-generic-gifts-into-joy-with-ai/)
- **Description:** Use AI to scan what a donor or alum actually cares about, then create tailored recognition, reunion collateral, keepsakes, event visuals, or highly specific messages that feel personal rather than generic.
- **Why this should hit for OIA:** Advancement runs on care signals. This is one of the few AI uses that can make outreach feel warmer rather than more automated, if reviewed well.

### 11. Create an internal reporter that briefs the team every week

- **Source:** [Using AI for work news](https://www.s-anand.net/blog/using-ai-for-work-news/), [O3 Is Now My Personalized Learning Coach](https://www.s-anand.net/blog/o3-is-now-my-personalized-learning-coach/)
- **Description:** Set up a scheduled workflow that scans internal files plus the web and sends a weekly brief on relevant alumni news, corporate CSR moves, partner milestones, project updates, and sector developments.
- **Why this should hit for OIA:** This is a strong answer to "how do I stay current?" and "how do I find warmer ways into a conversation?" It is especially useful for lead generation, meeting prep, and cross-team awareness.

### 12. If IITM rolls out internal AI broadly, instrument the rollout around real work, not hype

- **Source:** [Features actually used in an LLM playground](https://www.s-anand.net/blog/features-actually-used-in-an-llm-playground/)
- **Description:** Track what people really use. In that telemetry, the most used features were not fancy agent magic. They were:
  - attaching files
  - RAG on long documents
  - copying output
  - reusable templates
  - structured JSON
- **Why this should hit for OIA:** That is a very useful rollout lesson for a non-engineering office. Their high-value AI use is likely to be document-grounded work over local files, not generalized chat. This helps focus enablement on the workflows people will actually adopt.

### 13. Use layout-aware PDF extraction for donor and project documents

- **Source:** [Things I learned on 2024-04-20](https://til.s-anand.net/2024-04-20.html)
- **Description:** Use tools and AI workflows that preserve PDF hierarchy, tables, and layout when extracting from brochures, annual reports, proposals, or scanned documents.
- **Why this should hit for OIA:** Advancement teams live inside messy PDFs. Better extraction is a practical, non-glamorous unlock for search, reuse, comparison, and structured reporting.

### 14. Use a rigorous rubric before choosing AI tools, copilots, or vendors

- **Source:** [Evaluate technology](https://www.s-anand.net/blog/prompts/evaluate-technology/)
- **Description:** Evaluate vendors on popularity, recency, support, exportability, pricing clarity, performance, docs, and primary-source evidence with dates.
- **Why this should hit for OIA:** This is useful if they are comparing CRM add-ons, transcription vendors, copilots, or alumni-engagement tools. The key value is not the model's answer. It is the creation of a defensible, documented procurement note.

## A practical sequence for OIA

If I were sequencing this for them, I would not begin with a chatbot rollout. I would begin with three concrete workflows:

1. **Meeting intelligence**
   - record
   - transcribe
   - analyze
   - push structured notes back into the CRM

2. **Briefing pack generation**
   - search Drive / mail / web
   - draft profile + deck
   - human reviews before use

3. **Event-to-artifact pipeline**
   - transcript
   - recap deck
   - FAQ
   - action list
   - searchable archive

Once those work, I would layer in:

- maker-checker validation
- machine-readable specs for recurring workflows
- digital-exhaust mining for alumni / donor communities

## The underlying message I would give them

The deepest shift for this team is not "AI writes faster."

It is:

- **AI makes relationship work more searchable**
- **AI makes meeting-heavy work more reusable**
- **AI makes high-touch work more scalable**
- **AI makes policy-heavy work more checkable**

That combination feels especially well-matched to OIA.

## Source links used for the audience profile

- Primary prep call transcript: `/home/sanand/Dropbox/notes/transcripts/2026-03-17 Kaviraj Vasudha IITM.md`
- OIA site: <https://ia.iitm.ac.in/index.html>
- Joy of Giving home: <https://joyofgiving.alumni.iitm.ac.in/>
- Joy of Giving team page: <https://joyofgiving.alumni.iitm.ac.in/the-team>
- Joy of Giving projects: <https://joyofgiving.alumni.iitm.ac.in/projects/all>
- Joy of Giving why-give page: <https://joyofgiving.alumni.iitm.ac.in/why-give>
- IITM convocation coverage with 2024-25 fundraising figure: <https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-62nd-convocation-witnesses-graduation-3227>

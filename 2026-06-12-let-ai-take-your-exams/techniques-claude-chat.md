---
title: "IITM Paradox Workshop Let AI take your exams"
date: 2026-06-08T06:13:16+05:30
source: "https://claude.ai/chat/3afeeea2-656d-486c-9684-ff61b05c4780"
---

## User

I have a workshop planned for IITM BS degree students, mainly from data science (rather than programming) stream.

Knowing my style of talks and workshops, the experiments I run, the way I use audiences as data sources and learning mechanisms, the way I mix engagement with education and leave behind tangible practices they can use daily, and my focus on the workshop being as useful to the audience as possible, what should I cover in this workshop, given the title "Let AI take your exams"

Evaluate alternatives. Prioritize utility, novelty and engagement. Suggest topics to cover. Give me a 1 para description

---

## Claude

<details>
<summary>Architected live diagnostic experiment revealing genuine learning through AI exam failures</summary>

> Anand wants workshop content suggestions for IITM BS degree students (data science stream) on "Let AI take your exams." Let me think about this using what I know about his style:
>
> - Uses audiences as data sources (live experiments, real-time polling, collective intelligence)
> - Mixes engagement with education
> - Leaves behind tangible daily practices
> - Focus on utility to audience
> - Voice-first, interactive experiments
> - "Build to think" philosophy
> - LLM Psychologist framing
> - Data-driven storytelling
> - Gamification
>
> The title "Let AI take your exams" is provocative - it could mean:
>
> 1. Using AI to help you study/pass exams
> 2. Literally having AI take exams for you (and what that reveals about exam design)
> 3. Using AI-taking-exams as a diagnostic to understand your own learning gaps
> 4. Redesigning how you learn given AI can pass exams
>
> For DS students (not programming-heavy), the angle should be about prompting rather than coding, using AI as a thinking partner, understanding what exams actually test versus what AI can do, and building practical daily habits. The real tension here is that IITM BS students face exams where AI is either banned or restricted, so the workshop needs to address how to leverage AI ethically while still developing genuine understanding.
>
> The key is framing "let AI take your exams" as a learning tool—running past exam questions through AI live to see where it fails and succeeds, which immediately reveals what the exam is actually testing and what you genuinely need to learn. Beyond that, I can use AI as a metacognitive partner to explain concepts back to me, identify gaps in my understanding, and generate targeted practice questions at the edge of my knowledge—essentially compressing the learning process without cutting corners on actual comprehension.
>
> The strongest hook is the live experiment angle: have the audience submit real IITM exam questions, run them through AI in real-time, diagnose where and why the AI fails, and use those failures to reverse-engineer what genuine understanding actually looks like. Then pivot to showing how to use AI strategically to develop that kind of understanding—prompting well itself becomes a test of whether you understand the concept.
>
> Done

</details>

### Workshop: "Let AI take your exams"

**The core tension to exploit:** The title is a provocation that resolves into something deeper — _watching AI take your exams teaches you more about learning than studying does._ That's the throughline.

---

**Evaluate the main angles:**

| Angle                                             | Utility | Novelty | Engagement                        |
| ------------------------------------------------- | ------- | ------- | --------------------------------- |
| Prompting tricks to pass exams                    | High    | Low     | Medium — feels like a cheat sheet |
| AI as study partner (flashcards, summaries)       | Medium  | Low     | Low — they've heard this          |
| Live: AI takes their actual exam questions        | High    | High    | Very high — skin in the game      |
| Diagnosing where AI fails → what's worth learning | High    | High    | High — reframes the whole degree  |
| Building a daily AI-learning ritual               | High    | Medium  | Medium                            |

The sweet spot is **angles 3+4 feeding into 5** — use the live experiment to generate the insight, then convert it into a daily practice.

---

**Suggested flow:**

1. **Cold open experiment** — Collect 10 real exam questions from the audience live (past OPPE/quiz questions). Run them through AI visibly. Score them as a class. This makes the audience the data source immediately.
2. **The autopsy** — Where did AI nail it? Where did it hallucinate confidently? Where did it get the right answer for the wrong reason? This is not about AI's limits — it's a mirror on _what the exam is actually testing_ vs. what students think it's testing.
3. **The inversion** — If AI passed, the question is now: what did _you_ need to understand to write that question? The skill isn't answering — it's knowing when the answer is wrong. Introduce "AI as first-draft, you as editor" as the core cognitive posture.
4. **The Socratic prompt** — Live demo of using AI to find _your own_ blind spots: "I think X is true because Y — what's wrong with my reasoning?" Students try this on a concept they found confusing. This is the single most transferable daily habit.
5. **What to actually develop** — The 3 things AI reliably can't do on exams: _catch its own errors in your domain, connect to your specific project/data, and know what you don't know._ These map to the genuine skills worth building in a DS degree.
6. **The daily ritual** — Leave them with a 3-prompt study template they can use tonight: Explain → Quiz me at the edge → Find the flaw in my understanding.

---

**One-paragraph description:**

> You've been told AI can pass your exams. But what happens when you actually watch it try — live, on your questions, in real time? This workshop starts with a collective experiment: we feed real IITM exam questions to AI and score the results together. What follows isn't a tutorial on prompting — it's an autopsy that reveals what your exams are actually testing, where AI confidently hallucinates, and what that means for what's worth learning. You'll leave with a reframed understanding of your degree (the goal isn't answers, it's the ability to catch wrong ones) and a concrete 3-prompt daily study ritual that uses AI as a Socratic sparring partner rather than an answer machine. Come with a question you got wrong recently — it's going to be useful.

---

## User

Suggest specific exercises I can demonstrate during this workshop. My aim is to show students how AI coding agents, when coupled with browsers, can unlock powerful exam solving techniques that even the advanced users of AI might not have expected. I'll be presenting this as an extreme push towards "Delegate as much as possible to AI - including learning and test-taking. What AI cannot do is what you should be learning." Use Local MCP bash. My blog posts with the education + llm categories will be a good source of ideas. So might ~/code/exam/ where I have exam results, questions, etc. Other blog posts - especially about browser-based automation, may help. I use bookmarklets a lot - see ~/code/tools/ - and that's an interesting technique to use as well. There may also be useful tips on learning - e.g. using transcripts analysis, gemini to convert to multiple formats, etc. from by blog post. Use that as a second theme. Use the ideation protocol. Ideate ~30 ideas and recommend 10.

---

## Claude

<details>
<summary>Synthesized thirty exam-automation ideas across multiple perspectives systematically</summary>

> Now I have enough. Let me apply the ideation protocol.
>
> ---
>
> ### Ideation: ~30 raw ideas across lenses
>
> #### Lens 1: Security researcher / hacker mindset
>
> 1. Extract question bank from exam JS source (your `q-*.js` files are bundled client-side — DevTools exposes them before the exam renders)
> 2. Hit the `/filter` endpoint directly to retrieve other students' saved answers for the same question (noted in your own `questions.md` as a known leak)
> 3. Reverse-engineer JWT signatures to pre-submit answers before reading questions
> 4. Intercept the `/proxy` endpoint your exam platform exposes — it can be used to bounce requests through exam.sanand.workers.dev to bypass CORS restrictions on external data
>
> #### Lens 2: Competitive exam coach
>
> 1. Data-driven GA optimizer: upload your current scores to Claude, replicate the one-page playbook you built for TDS (GA2>45 cuts fail risk to 16%) — but for the student's own data, live
> 2. Submission timing calculator using the "halving a deadline costs ¼ marks" insight — when is the optimal moment to submit?
> 3. Past exam pattern extractor: feed 5 past papers → Claude → "10 archetypes that always appear" → study only those
>
> #### Lens 3: Data scientist mindset
>
> 1. Score regression: upload results.csv → Claude predicts which question types correlate with your personal weak spots
> 2. Cluster past exam questions by embedding similarity to find the canonical question types
> 3. AI-generated weakness report by feeding your exam attempt history to Claude
>
> #### Lens 4: Lazy-but-smart student
>
> 1. Screenshot-to-answer pipeline: screenshot exam screen → Claude Vision → LLM returns answer → agent types it into form field
> 2. Bookmarklet that grabs page question text, fires LLM API, overlays answer inline — never leaves the exam tab
> 3. Browser agent (agent-browser/Playwright) takes the whole exam: give it URL + credentials, it logs in, reads, answers, submits
> 4. Claude Code agent writes + deploys code for FastAPI/Vercel questions, gets the deployed URL, submits it — fully autonomous programming question solver
> 5. Gemini reads your 200-page textbook and returns "20 concepts most likely to appear in this exam" in 2 minutes
>
> #### Lens 5: Educator / metacognitive
>
> 1. AI classifies question archetype → retrieves your own solution template for that class
> 2. LLM-as-judge self-verification: Claude answers → Gemini verifies → submit only consensus (your double-checking post)
> 3. EXECUTE → KNOW → skip LEARN: demonstrate the ffmpeg-visualization pattern on a TDS exam question — agent solves it first, student understands afterward
> 4. Bookmarklet: highlight exam question text → LLM tells you what concept is being tested + what a wrong answer looks like (metacognitive coaching, not the answer)
>
> #### Cooking domain rules applied (mise en place, taste-as-you-go, right tool)
>
> 1. Exam mise en place: bookmarklets pre-loaded, LLM prompts pre-staged, agent-browser ready before exam opens — demo the 5-minute setup ritual
> 2. Right tool for each question type: Gemini for long-doc reading, Claude for code, GPT for reasoning — automated question-type router
> 3. Taste-and-adjust: run AI answer through a second LLM before submitting — build a 2-step pipeline as a bookmarklet
>
> #### Military domain rules applied (intelligence first, flank, weakest point)
>
> 1. Pre-exam intelligence brief: 30 minutes before → scrape course page → AI generates "10 things you must know right now" → 5-minute cramming brief
> 2. Flank the question: don't solve the SQL question — find the dataset the question references, query it directly using DuckDB-in-browser
> 3. Weakest point: identify which exam questions have 94%+ pass rates (you have this data) → do those first to guarantee base score
>
> #### Learning pipeline theme (Gemini derived formats)
>
> 1. Lecture → 5 formats in 10 min: TDS YouTube video → NotebookLM → podcast + sketchnote + quiz + flashcards + song
> 2. YouTube → exact exam answer: exam question about DuckDB → search YouTube for tutorial → extract transcript (YTScribe) → LLM gives specific answer
> 3. Transcript → Anki pipeline: pull YouTube transcript → Gemini → Q&A pairs → exportable flashcard deck (bookmarklet)
>
> #### Wildcard / unexpected
>
> 1. AI monitors your screen and intervenes: Claude Computer Use watches you work, detects when you're stuck (cursor stops moving), volunteers next hint without giving full answer
> 2. Multi-agent exam team: one agent reads the question, another searches documentation, a third writes the answer, a fourth verifies — demo a 4-agent pipeline on a single question
>
> ---
>
> ### Banning the obvious (5 banned + near-duplicates removed)
>
> - "Paste into ChatGPT and copy the answer" — banned
> - "Use GitHub Copilot for code completion" — banned
> - "Generate flashcards with AI" — banned
> - "Ask AI to explain concepts before studying" — banned
> - "AI grammar/polish tool for written answers" — banned
>
> ---
>
> ### CONVERGE: Top 10 Recommended Exercises
>
> Scored on **Impact** (student utility), **Novelty** (unexpected to even AI-savvy students), **Engagement** (demo watchability).
>
> ---
>
> #### ✅ 1. Browser agent takes the whole exam _(Wildcard Pick)_
>
> **Demo:** Give `agent-browser` the exam URL and your Google login. Watch it open the browser, read each question, call the LLM, type answers, and hit submit — while you do nothing. **Why non-obvious:** Students think of AI as a text box. Watching a headless browser autonomously take an exam is viscerally shocking. **Must hold:** The exam must not have CAPTCHA or proctoring. Your exam at exam.sanand.workers.dev has neither. **May fail:** Dynamic questions (randomized per user) need the agent to read and adapt each time — doable but requires robust prompting.
>
> ---
>
> #### ✅ 2. Bookmarklet: One-click AI answer overlay
>
> **Demo:** On any exam page, click bookmarklet → it grabs the question text, fires your LLM API, and overlays the answer in a floating panel — without leaving the tab, without copy-pasting. **Why non-obvious:** Students are used to Alt-Tab to ChatGPT. A bookmarklet that works _inside_ the exam tab feels like cheating-as-magic. You can show the 10-line JS behind it. **Leaves behind:** A reusable bookmarklet they can adapt to any website. **May fail:** Pages that block `document.querySelector` or use iframes need workarounds.
>
> ---
>
> #### ✅ 3. Extract answers from exam source code
>
> **Demo:** Open DevTools on the exam page. Find the bundled `q-*.js` file. Read the answer validation logic. The question "Markdown Architecture" is literally documented as "blind copy-paste fails" — show that AI copying from its context window gets it wrong, but reading the source gets it right. **Why non-obvious:** Students think the exam is a black box. Most have never opened DevTools during an exam. **The insight to deliver:** Understanding the _system_ you're operating in is a form of intelligence AI doesn't apply unless you direct it to.
>
> ---
>
> #### ✅ 4. Data-driven GA strategy optimizer
>
> **Demo:** Upload your own `results.csv` to Claude live. Replicate your blog post experiment. Ask: "Tell me exactly which GAs I should do and skip to avoid failing." Show the one-page playbook it produces. **Why non-obvious:** Students think AI is for solving questions. Using it to _strategize which questions to not bother solving_ is a mindset flip. **Leaves behind:** The exact prompt and workflow they can run on their own data.
>
> ---
>
> #### ✅ 5. Gemini: Textbook → exam brief in 2 minutes
>
> **Demo:** Take a 200-page TDS course PDF (or a module reading). Upload to Gemini. Prompt: "I have an exam in 30 minutes on this content. Give me the 15 concepts most likely to be tested, with a one-sentence explanation of each." Show the output. **Why non-obvious:** Students spend hours reading; this compresses it to reading time = 0. **The insight:** This reframes "studying" as directing AI, not absorbing content. The skill is the prompt, not the reading.
>
> ---
>
> #### ✅ 6. Claude Code writes, deploys, and submits a programming question
>
> **Demo:** Take a real TDS programming question (FastAPI endpoint, Vercel deployment). Give it to Claude Code. Watch it write the code, deploy it, extract the URL, and fill in the exam answer — end to end, unassisted. **Why non-obvious:** This is beyond "AI writes code." It's AI completing the entire submission lifecycle including deployment. **The insight:** For programming exam questions, the student's job is now _question selection and verification_, not execution.
>
> ---
>
> #### ✅ 7. Derived formats pipeline: Lecture → 5 learning formats in 10 minutes
>
> **Demo:** Take a TDS YouTube lecture. Use YTScribe to get the transcript. Feed to Gemini: generate podcast script (NotebookLM), sketchnote, flashcard Q&A deck, 10-question practice quiz, and a song. Show all 5 outputs. **Why non-obvious:** Students consume content in one format. This shows the same hour of lecture can produce a week's worth of study material in 10 minutes. **Leaves behind:** The exact prompt chain as a reusable workflow.
>
> ---
>
> #### ✅ 8. Pre-exam intelligence brief (30-minute ritual)
>
> **Demo:** 30 minutes before a fake exam, run: scrape the course content page → paste into Claude → prompt: "I'm sitting an exam on this in 30 minutes. What are the 10 most important things I must know, ranked by likelihood of appearing?" Show the output used as a cramming brief. **Why non-obvious:** Treating an LLM like a military intelligence officer prepping you for an engagement reframes the relationship from tutor to strategic advisor. **Leaves behind:** A repeatable ritual they can use before every assessment.
>
> ---
>
> #### ✅ 9. Screenshot → LLM → auto-fill pipeline
>
> **Demo:** Screenshot a question. Drop it into Claude Vision. Get the answer. Show how this pipeline can be automated: a hotkey triggers a screenshot, pipes it to LLM API, pastes the result into the clipboard — ready to paste in under 5 seconds. **Why non-obvious:** Most students don't know Claude can read a screenshot of their screen as a question. The pipeline from image to answer to clipboard is invisible and fast. **May fail:** Multi-part questions with data tables require careful screenshot framing.
>
> ---
>
> #### ✅ 10. Two-LLM verification chain as exam safety net
>
> **Demo:** Take a TDS question. Claude answers. Then run: "Here is a question and an AI-generated answer. What is wrong with this answer, if anything?" through Gemini. Show cases where Gemini catches Claude's error. Build a bookmarklet that does both calls sequentially. **Why non-obvious:** Students who use AI get AI's confidence, not AI's accuracy. This is the "verify button" exercise — your own blog concept made tangible in exam context. **The insight to deliver:** AI can be wrong with 100% confidence. The skill worth developing is knowing when to trust the verifier.
>
> ---
>
> ### The Wildcard Bonus Demo (handle carefully)
>
> **The /filter endpoint leak:** Show the audience that `exam.sanand.workers.dev/filter?quiz=tds-ga2` returns saved student results. This is documented in your own `questions.md` as a known issue. Frame it as: _"The system has a vulnerability. AI found it. You didn't have to. What does that mean for what you need to learn?"_ — pivots into the core workshop message about understanding systems, not just answering questions.

</details>

<details>
<summary>Called tool: Tool</summary>

Request

```

```

{text: "The output of this plugin was redacted."}

```

```

Response

```
The output of this plugin was redacted.
BashRequest{
"commands": "
# Check the gemini scraper / AI scraper for exam ideas
cat ~/code/tools/aiscrapers/geminiscraper.js 2>/dev/null | head -30
echo \"---\"
# Find blog posts about gemini / AI and transcripts, learning, audio
grep \"gemini\\|transcript\\|audio\\|youtube\" ~/code/blog/description.md | grep -i \"learn\\|study\\|summar\\|convert\\|format\" | head -20
echo \"---\"
# Look at exam prompts directory
ls ~/code/exam/prompts/ 2>/dev/null
cat ~/code/exam/prompts/*.md 2>/dev/null | head -80
"
}Response(function (root) {
const $ = (selector, el = root.document) => el.querySelector(selector);
const nodeTypes = root.Node || { TEXT_NODE: 3, ELEMENT_NODE: 1 };
function formatLocalIso(date) {
const pad = (value) => String(value).padStart(2, "0");
const offsetMinutes = -date.getTimezoneOffset();
const sign = offsetMinutes >= 0 ? "+" : "-";
const absOffset = Math.abs(offsetMinutes);
const offsetHours = pad(Math.floor(absOffset / 60));
const offsetMins = pad(absOffset % 60);
return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}T${pad(date.getHours())}:${pad(
date.getMinutes(),
)}:${pad(date.getSeconds())}${sign}${offsetHours}:${offsetMins}`;
}
function yamlEscape(value) {
return String(value ?? "")
.replace(/\\/g, "\\\\")
.replace(/"/g, '\\"')
.replace(/\r?\n/g, " ");
}
const cleanText = (value) =>
String(value || "")
.replace(/\s+/g, " ")
.trim();
const cleanTitle = (value, product = "Gemini") => {
const title = cleanText(value).replace(new RegExp(`\\s+-\\s+${product}$`, "i"), "");
return title && !new RegExp(`^(?:${product}|${product} Conversation|New chat)$`, "i").test(title) ? title : "";
---
pages/notes/gemini-book-summary-grit-peak-range.md:description: I synthesized and fact-checked seven key books on talent and performance, from Duckworth's Grit to Grant's Hidden Potential. Learn why early specialization is a trap and how "deep practice" actually re-wires your brain for mastery.
pages/notes/gemini-book-summary-grit-peak-range.md:keywords: [grit, deliberate practice, growth mindset, range, talent, myelin, motivation, book summary]
pages/notes/gemini-immune-system.md:description: I explain the immune system using the universal locksmith and lottery ticket analogies. Learn how V(D)J recombination shuffles DNA to create a library of specialized superweapons capable of identifying every possible pathogen, even those not yet evolved.
pages/prompts/afterslides.md:keywords: [llm prompts, transcript summarization, pyramid principle, markdown, slide deck generation, content annotation]
pages/prompts/analyze-call-recording.md:description: I share a prompt I use to extract deep value from call transcripts. It identifies missed emotional bids, unvalidated assumptions, and high-impact experiments, helping me improve how I engage others and learn from every conversation.
posts/2001/i-learn-that-girls-can-be-very-confusing.md:description: I document a brief, disjointed chat transcript from 2001. I try to decipher cryptic messages from a mysterious user, sonisha_jd, and suspect I might know their identity despite the sudden and unprovoked termination of our talk.
posts/2001/i-learn-that-girls-can-be-very-confusing.md:keywords: [chat transcript, yahoo chat, online identity, personal blog, digital interaction, 2000s internet]
posts/2001/i-learn-that-guys-want-to-speak-to-girls.md:description: I share chat transcripts from 2001 highlighting the repetitive 'ASL' dance. I found that most guys in chat rooms had zero interest in talking to another man, leading to immediate disconnections once my gender was revealed.
posts/2001/i-learn-that-robots-are-patient-but-infuriating.md:keywords: [iniaes, chatbot, ai history, conversation transcript, chatterbot, natural language processing]
posts/2001/sanskrit-texts-and-bhajans.md:description: I discovered a resource offering audio recordings of various Sanskrit texts and traditional bhajans. These files provide an easy way to listen to and learn spiritual chants and literature in their original Sanskrit.
posts/2001/windows-media-player-8.md:description: Windows Media Player 8 introduces a new media format claiming better compression than MP3. The software allows users to convert audio and video files into this more efficient digital format for Windows-based playback.
posts/2004/how-dna-gets-converted-to-proteins.md:description: I found a helpful animation that visualizes the biological process of DNA being converted into proteins. It provides a clear step-by-step look at transcription and translation, making complex molecular biology concepts accessible through motion graphics.
posts/2004/how-dna-gets-converted-to-proteins.md:keywords: [dna, protein synthesis, transcription, translation, molecular biology, animation]
posts/2012/downloading-songs-from-youtube.md:description: I explain my workflow for downloading music from YouTube using Keepvid or youtube-dl, then converting the video to MP3 using VLC's media conversion tool or a handy command line script for automation.
posts/2025/ai-agents-are-messing-up-software-tool-learning.md:description: I found AI agents collapse the traditional know-learn-execute workflow. Using Claude to generate complex ffmpeg audio visualizations, I bypassed learning syntax entirely, shifting to an 'execute first' model that challenges how we teach software tools.
posts/2025/ai-agents-are-messing-up-software-tool-learning.md:keywords: [ai agents, claude, ffmpeg, learning models, software mastery, audio visualization]
posts/2025/ai-beats-me-at-dataviz.md:keywords: [data visualization, xenographics, generative ai, gemini, claude, prompt engineering, information design]
posts/2025/converting-black-and-white-photos-to-color.md:keywords: [google gemini, image colorization, gemini-2.5-flash-image, photo restoration, prompt engineering, generative ai]
posts/2026/agent-consumable-content.md:description: I export my communications, browsing history, and records into one-line formats and use scripts to summarize blog posts and transcripts. By creating agent-friendly logs and SKILL.md files, I'm preparing my personal data for LLM-driven leverage.
posts/2026/derived-formats-with-gemini.md:description: A single source document can now be transformed into many useful derivative formats like podcasts, sketchnotes, songs, and videos, making generative AI a practical format-conversion layer for knowledge work.
---
2025-09-ga2.md
2025-09-ga7.md
2025-10-ga3.md
2026-01-ga2.md
2026-01-ga6.md
2026-01-roe.md
exam-tds-2026-01-ga1-comics.md
exam-tds-2026-01-p1.md
prompts.md
q-share-secret-server-hack.md
# Question Creation Workflow
Document written with AI assistance by: Carlton
This guide documents how the GA2 September 2025 exam was built so that future authors can reuse the workflow.
## Setup
- Clone the `exam` repository locally.
- the course readings into `content/` (kept out of git via `.gitignore`).
- Pull the `src/tds` submodule to reuse archived markdown notes during development.
- Install dependencies with `npm install` and verify the bundle via `npm run build-code`.
## Tooling
- Editor: Visual Studio Code with the Codex extension.
- Model: GPT‑5 Codex High, full agent access enabled.
- Local runners: `uv` for Python scripts, `npx wrangler dev` for previewing exams.
- Tests: `npm test`, `npm run build-data`, and targeted solution scripts in `test/`.
## Authoring Steps
1. Review `src/exam-tds-2025-05-ga2.js` and `src/exam-tds-2025-05-ga2.info.js` to understand the baseline structure.
2. Map Module 3 coverage by browsing the links in `content/_sidebar.md` (Deployment Tools topics).
3. Draft question ideas with Codex, ensuring parity or higher difficulty than the May GA2 set.
4. Implement each new task as `src/q-*.js`, keeping question IDs aligned with filenames.
5. Assemble `src/exam-tds-2025-09-ga2.js` and `src/exam-tds-2025-09-ga2.info.js`, mirroring the May configuration.
6. Add regression tests and helper scripts so every question can be executed in exam conditions.
7. Capture learner-facing walkthroughs in `test/solutions/` using stepwise instructions and `uv`-compatible code samples.
## Authoring Prompt
```

<PROMPT>
In the `./src` folder there are programming questions for assessments that are found in files named with the prefix `q-`
There is an exam called `./src/exam-tds-2025-05-ga2.js` which reference questions found in the files prefixed with `q-` and a corresponding `./src/exam-tds-2025-05-ga2.info.js` file.
There is course content in the folder called `./content` The file `_sidebar.md` indicates the modules for the course that are numerically segregated from 1 to 8. The bullet points beneath each section give the reference links to the corresponding content associated with that module.
Your task is to:
- Examine all the content related to Module 3 in order to create test questions related to the content. The files that correspond to Module 3 are:
- [3. Deployment Tools](deployment-tools.md)
- [Markdown](markdown.md)
- [Images: Compression](image-compression.md)
- [Static hosting: GitHub Pages](github-pages.md)
- [Notebooks: Google Colab](colab.md)
- [Serverless hosting: Vercel](vercel.md)
- [CI/CD: GitHub Actions](github-actions.md)
- [Containers: Docker, Podman](docker.md)
- [DevContainers: GitHub Codespaces](github-codespaces.md)
- [HuggingFace Spaces](huggingface-spaces.md)
- [Tunneling: ngrok](ngrok.md)
- [CORS](cors.md)
- [REST APIs](rest-apis.md)
- [Web Framework: FastAPI](fastapi.md)
- [Authentication: Google Auth](google-auth.md)
- [Local LLMs: Ollama](ollama.md)
- Examine all the questions referenced in `./src/exam-tds-2025-05-ga2.info.js` and come up with similar new ones, that have the same or higher difficulty level and covering the same type of content.
- Each of these new questions have to also be prefixed files with `q-`
- Maintain at least the same diversity of content or more for the new questions that are created and create questions for all the subject areas that are being tested by the existing exam.
- Create a new exam called `./src/exam-tds-2025-09-ga2.js` that uses `./src/exam-tds-2025-05-ga2.js` as a template. Follow the same exact setup and dependencies to create the new exam. The questions however can be completely new and the number of questions can be increased if deemed necessary.
- Likewise create the corresponding `./src/exam-tds-2025-09-ga2.info.js` using `./src/exam-tds-2025-05-ga2.info.js` as a template.
If necessary, create multiple questions for the same sub topic to test students complete understanding of the sub topics.
- Create tests to check if the questions can be run in exam conditions (using npx to deploy locally) and see if the outputs are as expected.
- Use only `uv` astral for running any python solution scripts.  The documentation can be found at `https://docs.astral.sh/uv/` for using uv if needed.
- Most students are likely to use python to solve questions where appropriate. Create step wise solutions to the problems and solution scripts if necessary for the exam for learning purposes.
</PROMPT>
```
## Validation Checklist
- `npm test`
BashRequest{
"commands": "
# Check derived-formats-with-gemini post and agent-consumable post
cat ~/code/blog/posts/2026/derived-formats-with-gemini.md 2>/dev/null | head -60
echo \"---\"
cat ~/code/blog/posts/2025/ai-agents-are-messing-up-software-tool-learning.md 2>/dev/null | head -60
echo \"---\"
# Look for recent posts about computer use / browser agents
grep \"computer.use\\|browser.agent\\|agent.browser\\|claude.code\\|codex\\|playwright\\|2025\\|2026\" ~/code/blog/description.md | grep -i \"exam\\|learn\\|student\\|automat\\|browse\\|screen\\|vision\\|take\" | head -20
"
}Response---
title: Derived formats with Gemini
date: 2026-04-18T11:26:48-04:00
categories:
- llms
description: A single source document can now be transformed into many useful derivative formats like podcasts, sketchnotes, songs, and videos, making generative AI a practical format-conversion layer for knowledge work.
keywords: [Gemini, NotebookLM, multimodal AI, document transformation, content repurposing, knowledge workflows]
---
The natural capability of Generative AI is to _generate_ stuff - and Gemini's particularly good with media.
For example, we can take any document, like this MasterCard report on [The State of Open Finance 2026](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/report.pdf), and generate videos, podcasts, sketchnotes, songs, and more from it.
How?
I uploaded the [PDF](https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/report.pdf) to [NotebookLM](https://notebooklm.google.com/notebook/26da8a27-fd08-4c98-b0d5-73fefcb9e1dd) and created a 20-minute podcast by clicking on Generate Audio Overview - Deep Dive - English - Default.
<audio controls preload="metadata">
<source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-english.opus" type="audio/ogg; codecs=opus">
<a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-english.opus">Listen to the English podcast</a>
</audio>
It supports multiple languages, so I generated a Chinese and Filipino version as well.
<audio controls preload="metadata">
<source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-chinese.opus" type="audio/ogg; codecs=opus">
<a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-chinese.opus">Listen to the Chinese podcast</a>
</audio>
<audio controls preload="metadata">
<source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-filipino.opus" type="audio/ogg; codecs=opus">
<a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/podcast-filipino.opus">Listen to the Filipino podcast</a>
</audio>
Clicking on Generate Video Overview - Cinematic led to this video overview:
<video width="1280" height="720" style="max-width: 100%; height: auto;" controls muted preload="metadata">
<source src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/video.webm" type="video/webm">
<a href="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/video.webm">Video</a>
</video>
There are other formats in which we can generate videos. The Cinematic format is new, and the list is growing.
It's not just NotebookLM that you can use to generate new formats. [Gemini](https://gemini.google.com/) itself supports a variety of formats.
For example, I used my [Gemini Sketchnote prompt](https://www.s-anand.net/blog/gemini-sketchnotes/) to create a visual summary of the report:
<img src="https://files.s-anand.net/blog/2026-04-18-derived-formats-with-gemini/the-state-of-open-finance-2026/sketchnote.avif" alt="Sketchnote" style="max-width:100%; aspect-ratio: 16/9">
<!-- https://gemini.google.com/u/2/app/07dd0450592fc257 -->
... and, using Lyria via the "Create Music" option to generate a [narrative song](https://www.s-anand.net/blog/singing-a-vote-of-thanks/) with this prompt:
```markdown
Create a narrative summarizing this article.
Narrate it rather than sing it.
Use a voice like Bobby McFerrin's, as if he were narrating rather than singing.
Keep the music minimal, focus on the voice.
```
---
---
date: "2025-12-23T05:36:05Z"
categories:
- llms
- linkedin
description: I found AI agents collapse the traditional know-learn-execute workflow. Using Claude to generate complex ffmpeg audio visualizations, I bypassed learning syntax entirely, shifting to an 'execute first' model that challenges how we teach software tools.
keywords: [ai agents, claude, ffmpeg, learning models, software mastery, audio visualization]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7408179762227159041/
---
AI agents are messing up software tool learning.
Normally, we need to pass stages of competence:
KNOW what you can do\
LEARN how to do it\
EXECUTE it.
Excel: **KNOW** you can summarize by category, **LEARN** pivot tables, **EXECUTE** an Insert → PivotTable → select data range → drag ...
Photoshop: **KNOW** you can erase objects, **LEARN** Content-Aware Fill, **EXECUTE** Lasso tool → select → Edit → Content-Aware Fill → ...
**AI agents collapse these stages**. Especially with command line tools.
For example, I did not **KNOW** ffmpeg could visualize audio, nor **LEARN** the complex filters, nor **EXECUTE** it on my laptop.
Instead, I told Claude to _Visualize this audio clip creatively in multiple ways_. It generated a dozen stunning visualizations of this Why This Kolaveri clip: https://lnkd.in/g7vfcPEs
I didn't KNOW ⮕ LEARN ⮕ EXECUTE. I did an EXECUTE ⮕ KNOW ⮕ don't bother to LEARN.
Since that's possible, my prompts are now like: "I don't know what I want. Guess my desires. Fulfill them. Show me. Then maybe I'll know what I want."
Which is fantastic! But on the other hand, this **TOTALLY** messes up how I teach software tools...
![](https://files.s-anand.net/images/2025-12-23-4-stages-of-competence-linkedin.webp)
<div class="video-embed"><iframe src="https://www.youtube.com/embed/VXkf0zeRhJ4" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
[LinkedIn](https://www.linkedin.com/posts/sanand0_ai-agents-are-messing-up-software-tool-learning-activity-7408179762227159041-_Pof)
---
posts/2025/ai-agents-are-messing-up-software-tool-learning.md:description: I found AI agents collapse the traditional know-learn-execute workflow. Using Claude to generate complex ffmpeg audio visualizations, I bypassed learning syntax entirely, shifting to an 'execute first' model that challenges how we teach software tools.
posts/2025/ai-agents-are-messing-up-software-tool-learning.md:keywords: [ai agents, claude, ffmpeg, learning models, software mastery, audio visualization]
posts/2025/ai-as-your-psychologist-personality-flaws-exposed.md:description: "Chat memory allows LLMs to infer surprisingly specific personality flaws from long conversation histories, making them unexpectedly capable mirrors for self-examination."
posts/2025/automating-a-podcast-from-github-commits.md:description: "Version-control activity can be automatically transformed into narrative audio, turning raw commit trails into ambient technical documentation that changes how people write and review code."
posts/2025/automating-a-podcast-from-github-commits.md:keywords: [GitHub commits, podcast generation, ambient documentation, activity traces, TTS, developer workflow]
posts/2025/best-way-to-learn-ai-image-generation-is-by-trying.md:description: "The fastest way to understand AI image generation is not theory but playful experimentation across replacements, stickers, interfaces, products, and environments."
posts/2025/best-way-to-learn-ai-image-generation-is-by-trying.md:keywords: [AI image generation, experimentation, prompting, creative practice, ChatGPT images, learning by doing]
posts/2025/double-checking-reduces-hallucinations.md:description: "Hallucinations become much less dangerous when multiple cheap models check each other, because their mistakes overlap far less than their individual error rates suggest."
posts/2025/double-checking-reduces-hallucinations.md:keywords: [hallucinations, ensemble methods, double checking, LLM reliability, classification, automation quality]
posts/2025/even-the-guest-wifi-is-so-secure.md:description: "A corporate guest WiFi blacklist can be funny enough to read as an accidental manifesto about what kinds of tools, learning, and play an organization implicitly discourages."
posts/2025/feedback-for-tds-jan-2025.md:description: "Student feedback suggests that the course’s difficulty, chaos, and open-endedness are precisely what make it unusually memorable and transformative."
posts/2025/feedback-for-tds-jan-2025.md:keywords: [student feedback, course design, difficulty, learning experience, Tools in Data Science, education]
posts/2025/generative-ai-whatsapp-group-podcast.md:keywords: ["WhatsApp", "podcast generation", "TTS", "automation", "group chats", "NotebookLM"]
posts/2025/goodbye-mba-hello-ai.md:description: "MBA students should optimize for adaptability, verification, and AI-assisted learning because entry-level knowledge work is already being restructured by LLMs."
posts/2025/halving-a-deadline-costs-1-4-of-marks-each-time.md:keywords: [deadlines, submission timing, scores, learning behavior, education analytics, time management]
posts/2025/how-to-create-a-data-driven-exam-strategy.md:description: I used ChatGPT to analyze 1,700 student scores and identify the strongest predictors for exam success. By prompting for simple heuristics, I developed a data-driven playbook that tells students exactly which assignments to prioritize for specific grade outcomes.
posts/2025/how-to-create-a-data-driven-exam-strategy.md:keywords: [chatgpt, predictive analytics, data-driven education, student performance, prompt engineering, exam strategy]
posts/2025/how-to-organize-browser-workspaces-with-llms-and-data.md:description: "Browsing history plus LLM clustering can turn a fuzzy personal workflow problem into a practical workspace taxonomy, while voice chat makes the write-up almost frictionless."
posts/2025/how-to-organize-browser-workspaces-with-llms-and-data.md:keywords: [browser workspaces, browsing history, LLM clustering, workflow design, voice writing, Edge workspaces]
posts/2025/how-to-review-trending-github-repos-on-vs-code.md:description: I automate tracking trending GitHub repos by piping gtrending data through jq and awk into a TSV. I scan and tag the list in VS Code using the Rainbow CSV extension for a fast, Excel-free review workflow.
BashRequest{
"commands": "
# Read the exam strategy blog post
cat ~/code/blog/posts/2025/how-to-create-a-data-driven-exam-strategy.md 2>/dev/null | head -80
echo \"---\"
# Check for blog posts specifically about passing exams / taking exams with AI
grep -i \"exam.*ai\\|ai.*exam\\|pass.*exam\\|take.*exam\\|solve.*exam\\|exam.*strategy\" ~/code/blog/description.md | head -20
echo \"---\"
# recent posts about browser agents / computer use
grep -i \"computer.use\\|claude.code\\|agent.browser\\|playwright\\|vision.*screen\\|screen.*vision\\|screenshot.*solve\" ~/code/blog/description.md | head -20
"
}Response---
title: How to create a data-driven exam strategy
date: "2025-10-09T01:24:19Z"
lastmod: "2025-10-09T01:24:21Z"
categories:
- education
- llms
wp_id: 4232
description: I used ChatGPT to analyze 1,700 student scores and identify the strongest predictors for exam success. By prompting for simple heuristics, I developed a data-driven playbook that tells students exactly which assignments to prioritize for specific grade outcomes.
keywords: [chatgpt, predictive analytics, data-driven education, student performance, prompt engineering, exam strategy]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7381923875992920064/
---
![How to create a data-driven exam strategy](/blog/assets/tds-grades.webp)
Can ChatGPT give teachers data-driven **heuristics** on student grades?
I uploaded last term's scores from about 1,700 students in my [Tools in Data Science course](https://tds.s-anand.net/) and asked ChatGPT:
> This sheet contains the scores of students … (and explained the columns).
>
> I want to find out what are the best predictors of the total plus bonus… (and explained how scores are calculated).
>
> I am looking for simple statements with 80%+ correctness along the lines of:
>
> - "if ga1\_f + ga\_4f > x then you will not fail; this is true for 90% of the students" or
> - "your total will effectively be your p1\_f score, within plus or minus 5 marks; this is true for ~90% of the students" or
> - "if you get below 40% in ga3\_f then you will likely fail; 80% of the students who did so fail."
>
> Earlier predictors (GA1, GA2, maybe GA3) are more useful (to students) …
>
> Two kinds of students: Those who want to avoid failing and those who want to score high….
>
> .. give me the best student advice. Phrase it conversationally and include numerical evidence in simple language.
After a 30 minute conversation, ChatGPT delivered concrete, actionable advice:
**One-page student playbook**
If you're behind / "don't fail":
- **Immediate target:** **GA2 > 45** and **GA3 > 55**. That alone cuts fail risk to ~**16%**.
- If possible, push **>85/85** to get fail to **~8%**.
- Translation: stop skipping; get partial credit; move into the "safe" GA2/GA3 band.
If you're aiming for an **A**:
- **Path A1 (broad coverage):** **P2 + ET >= 180** > A ~ **35%** (n=169).
- **Path A2 (also broad):** **P1 + P2 >= 180** > A ~ **45%** (n=161).
- If early GAs are fine (GA2/GA3 >=70), **keep them steady**, but your **marginal effort** should go to **P2 and ET**.
If you're aiming for an **S**:
- **Path S1 (most reliable):** **P2 >= 90 + ROE >= 80** > S ~ **77%** (n=26).
- **Path S2 (elite):** **P2 >= 90 + ET >= 85 + ROE >= 80** > S ~ **91%** (n=11).
- **Simple rule of thumb:** **P2 + ROE >= 170** or **ET + ROE >= 160** > ~**70% S** with **0% fails** in those groups.
- Translation: **ace ROE**. Use P2 and ET as the second and third pillars.
---
**Students**: Don't study harder. Study what moves the marks. (Learning be damned!)
**Teachers**: Try this with **your** course data!
Full chat: <https://chatgpt.com/share/68e7034a-7340-800c-b259-0bd51715ad11>
[LinkedIn](https://www.linkedin.com/posts/sanand0_todays-exploration-data-driven-llm-advice-activity-7381923875992920064-Aeey)
---
pages/articles/no-juniors-no-experts.md:description: As AI automates entry-level work, I examine how to build expertise when junior roles vanish. I suggest switching to system design for low-risk tasks and using AI as a high-fidelity simulator for critical, high-stakes skill development.
posts/2000/dhtml-use-growing.md:description: I've observed a growing trend of websites like Online Solutions and PassThisOn successfully implementing DHTML. These examples highlight how dynamic HTML is becoming a practical tool for building more interactive and functional web interfaces.
posts/2000/new-domain-names.md:description: I examined the new ICANN applications for top-level domains like .museum, .biz, and .xxx. It is interesting to see the diverse range of bidders competing to control these new additions to the global domain name system.
posts/2000/online-transactions-unsafe.md:description: I examine the security risks of online shopping by highlighting the Egghead credit card breach. This incident raises questions about the safety of Net transactions and the vulnerability of customer data stored by major retailers.
posts/2000/prove-god-exists.md:description: I examine philosophical proofs for God's existence, including Descartes' 'Cogito, ergo sum' and the Watchmaker Argument, but I find that I prefer relying on faith rather than logical proofs like those countered by Richard Dawkins.
posts/2001/bobby-fischer-playing-chess-on-the-internet.md:description: I examine the 2001 reports and rumors suggesting that the reclusive chess legend Bobby Fischer may have returned to the game to play anonymous, high-level matches against grandmasters on the Internet.
posts/2001/computer-translations.md:description: I highlight the limitations of machine translation by linking to classic examples of linguistic failures. These sources showcase why software often fails to capture context, resulting in the humorous errors frequently found on sites like Engrish.com.
posts/2001/free-software.md:description: I'm sharing an insightful article that delves into the origins and underlying motivations of the free software movement, examining why people contribute to open projects and the social structures that sustain these collaborative efforts.
posts/2001/red-cross-fund.md:description: I’m tracking the success of Amazon’s Red Cross Fund, which has already raised over $3.6 million. It’s an early, powerful example of how the internet can rapidly mobilize massive public donations for disaster relief.
posts/2001/social-engineering.md:description: I share a resource on the intersection of hacking and social engineering, examining how attackers exploit human psychology rather than technical flaws to bypass security protocols and gain unauthorized access to sensitive systems.
posts/2001/virtual-stapler.md:description: I enjoyed spending a few minutes playing with the Virtual Stapler, a simple and surprisingly entertaining online simulator. It’s a classic example of quirky, low-stakes browser toys that defined a specific era of internet humor.
posts/2001/w3schools.md:description: I recommend W3Schools for anyone starting with web development. It offers clear tutorials and interactive examples for HTML, CSS, and JavaScript, providing a straightforward way to learn the basics of building websites.
posts/2002/charge-for-eliminating-spam.md:description: I examine a cynical business model where free email providers intentionally add spam just to charge users for its removal, confirming my decision to get rid of my Hotmail account.
posts/2002/customizable-css-interface.md:description: I examine AllTheWeb's Alchemist tool, which allows users to customize search result interfaces using CSS. While it is a notable innovation in search engines, I question if CSS constraints make Google's API a more flexible solution.
posts/2002/distributed-computing-projects.md:description: I examine the rise of commercial distributed computing markets where companies buy idle retail processor time. This model dis-aggregates computing power, enabling resource-intensive initiatives like the Internet Movie Project to be crowdsourced using spare capacity.
posts/2002/greenspans-defence.md:description: I examine Greenspan’s argument that identifying bubbles in real-time is impossible, justifying why the Fed didn't raise rates earlier to prevent the late-nineties market surge and subsequent crash.
posts/2002/growth-form-function-and-crashes.md:description: I examine how scale-free networks evolve naturally to include central hubs, providing robustness against random failures but creating targeted vulnerabilities. These articles from the Santa Fe Institute detail how evolution differs from intentional design.
posts/2002/intel-vs-hamidi.md:description: Examine the Intel vs. Hamidi legal case regarding whether sending mass emails to a corporation’s employees constitutes a 'trespass to chattels' and how digital communications interact with traditional property and tort law.
posts/2002/military-history-and-network-security.md:description: I examine how military history provides valuable lessons for network security. By studying historical warfare, we gain insights into defense-in-depth, strategic planning, and the psychological aspects of securing modern digital infrastructure.
posts/2002/music-swapping-continues.md:description: I examine how music swapping persisted in 2002 despite Napster's shutdown. The RIAA's legal actions against KaZaa highlight the industry's struggle against shifting consumer habits and the rise of decentralized file-sharing networks.
---
pages/articles/why-i-prefer-interns.md:keywords: [agentic ai, software engineering hiring, technical assessments, claude code, iit madras, coding agents]
posts/2002/virtual-keyboard.md:description: I discuss early optical keyboard technology and speculate on its future potential. I envision using similar optics for digital handwriting recognition on paper and projecting interactive virtual screens from tiny, portable devices.
posts/2005/friends-script.md:keywords: [friends, tv scripts, sitcoms, screenwriting, transcripts, television]
posts/2025/i-lost-22-kg-in-22-weeks.md:keywords: ["weight loss", "fasting", "health", "self-tracking", "data visualization", "Claude Code"]
posts/2025/meta-ai-coding-using-ai-to-prompt-ai.md:keywords: ["meta prompting", "AI coding", "prompt refinement", "Codex", "Claude Code", "developer workflow"]
posts/2025/most-repeated-letters.md:description: I used Claude Code and Python to find English words with high letter concentrations, like "ASSESSES". I then generated a humorous xkcd-style narrative about the data, demonstrating how style catalogs can make technical analysis much more engaging.
posts/2025/most-repeated-letters.md:keywords: [claude code, python, text analysis, xkcd style, style catalogs, llm prompts, linguistics]
posts/2025/patterns-for-short-code.md:description: I used Claude Code to refactor my Unicoder tool, extracting thirteen principles for elegant, concise code. Key takeaways include replacing conditionals with data-driven structures, utilizing optional chaining, and using pattern arrays to eliminate repetitive logic.
posts/2025/patterns-for-short-code.md:keywords: [javascript, refactoring, claude code, data-driven design, dry principle, clean code]
posts/2025/people-beginning-and-ending-with-ai.md:description: I used the Claude Code agent to search 24,000 Wikipedia entries for names starting and ending with "AI." In ten minutes, I identified ten individuals, including Aishwarya Rai and Ai Nagai, through automated pattern matching and scripting.
posts/2025/people-beginning-and-ending-with-ai.md:keywords: [claude code, wikipedia, pattern matching, llm automation, coding agents, data extraction]
posts/2025/vibe-scraping-write-outcomes-not-scrapers.md:keywords: [vibe-scraping, ai agents, codex, claude code, web scraping, data extraction, automation]
posts/2025/why-old-movies-are-rated-so-high.md:keywords: [imdb, selection bias, data analysis, movie ratings, statistics, claude code]
Now I have a solid picture of Anand's ecosystem and tools. Let me now apply the ideation protocol:
Step 1: Ideate from 3-5 distinct perspectives
Security researcher / hacker mindset - "How do I exploit system weaknesses to pass without learning?"
Competitive exam coach - "How do I maximize score with minimal time?"
Data scientist - "How do I use data to optimize my strategy?"
Lazy but smart student - "How do I minimize effort while maximizing output?"
Ethical educator - "What should students actually learn vs what AI can do?"
Security researcher - Looking for platform vulnerabilities like exposed answer endpoints, JWT signature weaknesses, and data leakage through the filter endpoint
Competitive exam coach - Analyzing historical performance data to identify high-ROI questions, timing submissions strategically around deadlines, and focusing on questions with the highest pass rates
Data scientist - Clustering questions by type using embeddings and mining historical results to predict exam structure and patterns
Lazy but smart student - Automating the exam with a browser agent that screenshots questions, pipes them through an LLM, and injects answers directly into form fields
Educator - Identifying what AI struggles with in these exams to pinpoint which skills are actually worth teaching, since AI's inability to verify its own outputs highlights the value of verification skills
Now I'm exploring how principles from unrelated domains might apply here. Looking at cooking's atomic rules like mise en place (preparation before execution), tasting and adjusting throughout, and using the right tool for each task. Military strategy offers similar patterns: intelligence gathering before engagement, flanking from unexpected angles, and concentrating force at the weakest point. The mise en place concept seems particularly relevant for exam preparation—setting up AI tools and resources before the exam actually starts.
From the military angle, I'm thinking about scraping past exams to understand patterns, then either flanking the problem by querying the underlying datasets directly instead of solving questions head-on, or identifying which question types AI handles best and prioritizing those.
I should also rule out the obvious, conventional approaches that don't really leverage AI's unique capabilities—things like just pasting questions into ChatGPT, using AI for general studying, or generating flashcards.
Now I'm brainstorming more creative approaches: using computer vision to read exam screenshots and automatically fill in answers, creating a bookmarklet that silently fetches AI responses and overlays them on the page, deploying a browser agent that logs in and completes the entire exam autonomously, or extracting the question bank directly from the exam's JavaScript before it even renders.
There's also the angle of exploiting the /filter endpoint to see what other students answered, using data analysis to optimize which study areas deserve the most effort based on current scores, converting lecture videos into multi-format study materials through AI, and building a pipeline that turns lecture transcripts into Anki flashcard decks.
Beyond that, I could upload past quiz attempts to get AI analysis of weak topic areas with targeted practice questions, use an agent to autonomously write and deploy code solutions for programming questions, run deep research on exam topics to get comprehensive briefs quickly, and implement double-checking by having multiple AIs verify answers before submission.
There's also potential to extract patterns from past exam papers to predict question types, use browser console tricks to access question structures, convert course content into AI-generated podcasts for passive learning, and build a submission timing optimizer based on deadline penalties. Continuing with the question archetype classifier that matches patterns to solution templates, then layering in a multi-model verification where Claude, Gemini, and GPT each validate the answer before submission. I'm also thinking about generating multiple study formats from a single topic—podcasts, visual notes, songs, flashcards, quizzes—to hit different learning styles. There's a bookmarklet approach to scrape exam history and surface weakness patterns, plus reframing questions as prompt engineering exercises so students without coding skills can still learn to work effectively with AI. Now exploring how to reverse-engineer the marking rubric itself.
I can analyze a student's partial score by uploading the grading criteria and asking what answer patterns would produce that specific mark, revealing exactly where points leak. There's also a screen-monitoring agent that watches your work in real time and nudges you forward when stuck, plus a pre-exam intelligence brief that scrapes the course materials and delivers the ten most critical concepts to focus on. For tool-specific questions, I'm pulling YouTube tutorials, extracting transcripts, and feeding them to an LLM to generate precise answers. Building a bookmarklet that lets you highlight text on the exam page and get instant explanations.
Now filtering out the generic approaches—straight ChatGPT pasting, flashcard generation, basic Copilot use, and vague "ask AI to explain" tactics are all off the table. Scoring the remaining ideas on impact, novelty, and speed, the strongest candidates are a browser agent that autonomously completes the entire exam, a one-click bookmarklet that overlays AI answers, and extracting source code directly from the exam's JavaScript.
A data-driven Google Analytics optimizer that turns uploaded scores into a personalized study playbook would replicate the blog's methodology for their own results. Using Gemini to compress textbooks into exam briefs in minutes offers high utility with easy demonstration potential. An agent that writes and deploys code solutions for programming questions end-to-end leverages Claude's capabilities fully. A pipeline converting lectures into podcasts, sketchnotes, and quizzes creates a visually compelling daily tool. A bookmarklet turning transcripts into flashcards leaves behind something tangible for ongoing practice. Extracting patterns from past exams to identify ten core archetypes is strategic and non-obvious. Finally, a verification chain that double-checks AI answers provides a safety mechanism—turning the "verify" insight into practical protection against hallucinations.
There's also the /filter endpoint exploit—a literal demonstration of a known vulnerability in the exam system where you can access other students' answers, documented in the questions file itself. Framed carefully as a teaching moment about understanding the systems you operate within, it's a powerful illustration.Show lessDone
```

</details>

<details>
<summary>Called tool: Tool</summary>

Request

```

```

{text: "The output of this plugin was redacted."}

```

```

Response

```
The output of this plugin was redacted.
```

</details>

---

## User

Here's another answer from ChatGPT. Critically evaluate yours and theirs, take what's better, drop what's worse, explore any new thoughts this leads you to, and revise your response based on that.

<CHATGPT>

Below are exercises designed for a workshop whose real message is: “AI can solve a lot. Your job is to learn what to delegate, what to verify, and what to understand deeply enough to catch errors.” I’d explicitly say: these are for open-book, practice, mock, and instructor-approved settings. Not for bypassing proctored exams. ## Raw ideation ### 5 people who would see this differently **1. The exam designer** 1. Ask an agent to solve one full TDS-style quiz, then map every question into “AI can solve directly / AI needs tool access / AI fails unless human notices hidden constraint / AI cannot judge correctness.” 2. Show “question autopsy”: agent reads the source of a quiz question, extracts the hidden checker, and explains what the question is truly testing. 3. Use difficulty data to predict which questions humans find hard but agents find easy, and vice versa. 4. Generate new exam questions that are AI-resistant by making the skill “verify a plausible wrong answer.” 5. Show why some exams are accidentally testing environment setup, not understanding. **2. The adversarial student** 6. Use browser DevTools to inspect a quiz page and discover whether the answer/checker is client-side. 7. Run a bookmarklet that extracts all visible questions, hidden comments, buttons, links, downloadable files, and validation messages into Markdown. 8. Ask the agent to infer the answer format from the DOM and network calls before solving. 9. Replay fetch calls made by the browser to discover hidden APIs, datasets, and grading contracts. 10. Let the agent brute-force the answer box when the checker gives useful error messages. **3. The serious learner** 11. Feed a wrong answer plus the actual checker error to AI and ask: “What misconception caused this?” 12. Ask AI to create 5 near-miss variants of a question that expose whether you really understood it. 13. Convert a solved exam into a personal “weak-skill map.” 14. Turn one failed question into a 7-day spaced-repetition drill. 15. Ask AI to produce a “one-page ritual”: before solving, during solving, after solving, verification checklist. **4. The coding-agent power user** 16. Give Codex/Claude Code the exam repo and ask it to write a solver harness that runs all answer functions locally. 17. Ask the agent to classify each question by best solving tool: bash, browser, DuckDB, Python, LLM, spreadsheet, DevTools, deployment. 18. Have the agent generate synthetic users/emails to explore randomized variants. 19. Ask the agent to write a Playwright script that logs in, opens questions, downloads data, submits answers, and records failures. 20. Ask the agent to build a “question debugger” that prints expected output, accepted tolerance, and common failure messages. **5. The browser/bookmarklet hacker** 21. Create a “copy exam context” bookmarklet: scrape question text, hidden comments, links, input IDs, downloaded files, console errors, network endpoints. 22. Create a “solve with context” button that sends the scraped context to a local agent. 23. Create a “DOM diff” bookmarklet that shows what changes after wrong submissions. 24. Create a “network recorder” bookmarklet that logs fetch/XHR requests and responses. 25. Create a “question-to-notebook” bookmarklet that turns any browser question into a runnable Markdown/Python notebook. ### 2 unrelated domains as idea generators **Domain A: Forensic investigation** Structural rules: preserve the scene before touching it; build a timeline from traces; distinguish evidence from interpretation. 26. Browser forensics exercise: before solving, agent snapshots DOM, console, localStorage, cookies, network logs, downloaded files, and visible text. Then it solves only from evidence. 27. Timeline exercise: reconstruct how a student/agent got a wrong answer from attempt logs, error messages, and code changes. 28. Evidence ladder exercise: force the agent to label every claim as “seen in question,” “seen in code,” “computed,” “assumed,” or “guessed.” **Domain B: Speedrunning** Structural rules: route before execution; exploit mechanics, not just skill; reset fast when route fails. 29. Speedrun route exercise: ask the agent to design the fastest path through a 15-question exam: which questions to solve manually, script, inspect, skip, or batch. 30. Glitch catalogue exercise: collect recurring “exam mechanics” shortcuts: client-side checker, downloadable CSV, deterministic seed, useful error messages, hidden comments, predictable JSON schema. 31. Reset discipline exercise: if the agent fails twice, branch into a fresh tab/model/tool instead of debugging the same path indefinitely. ### Ban the 5 obvious ideas Banned because they are too conventional: 1. “Ask ChatGPT to solve the question.” 2. “Prompt better.” 3. “Use AI to explain the answer.” 4. “Use AI to generate practice questions.” 5. “Use AI to summarize notes.” Near-duplicates banned too: generic tutor prompts, generic flashcards, generic “explain like I’m five,” generic “write code for this,” generic “debug my code.” ## 30 candidate exercises, cleaned and diversified 1. **Exam Autopsy Dashboard**: Agent reads the exam repo and builds a table: question, visible task, hidden checker, actual skill tested, easiest exploit, genuine concept. 2. **Client-Side Answer Leak**: Use `q-share-secret-server` to show that bundling answer logic in browser code leaks the answer path. 3. **Hidden Comment Trap**: Use `q-trick-question-server` to show a question where the visible text is decoy and the real instruction is hidden in HTML comments. 4. **DOM-to-Markdown Bookmarklet**: One-click scrape of question text, links, hidden comments, input fields, buttons, and code blocks into Markdown for the agent. 5. **Network Contract Inspector**: Browser automation captures `fetch()` calls, request/response shapes, headers, and grading endpoint behavior. 6. **Checker-Driven Solver**: Agent reads answer functions and writes code to compute accepted answers locally. 7. **Error-Message Oracle**: Submit plausible wrong answers, collect validator messages, and let AI infer the exact missing requirement. 8. **Deterministic Seed Attack**: Use student email and question ID seeds to reproduce personalized data and answers. 9. **Question Router**: Agent decides per question: bash, Python, DuckDB, browser, spreadsheet, LLM, DevTools, API, or manual judgment. 10. **Exam Speedrun Route**: Agent plans the fastest solve order based on tool setup cost, answer confidence, and validation friction. 11. **In-Browser DuckDB Solver**: Demonstrate a DuckDB question solved entirely inside the browser or by extracting SQL/data to local bash. 12. **Pyodide/Numpy Mirror**: For embedding similarity, mirror the browser’s Pyodide logic locally and compare outputs. 13. **Server-Side Verifier Replay**: Use FastAPI-style questions to show that the problem is often “make the checker happy,” not “know FastAPI.” 14. **CORS as a Test Subject**: Ask the agent why a correct API fails the browser checker because CORS is missing. 15. **LLM-as-Judge Reverse Engineering**: Inspect a question where GPT validates the answer and infer what rubric the judge is applying. 16. **Markdown Nesting Failure**: Use `q-markdown-architecture` to show how AI output that looks right can fail a structural parser. 17. **Browser Console as Tutor**: Students paste checker errors and console logs into AI; AI explains the real failure. 18. **Playwright Exam Bot**: Build a script that opens a mock exam, extracts each question, downloads files, submits answers, records scores. 19. **Wrong-Answer Postmortem**: Take a student’s recent wrong question, ask AI to reconstruct the misconception and produce a near-miss trap. 20. **Skill Map from Scores**: Use exam results to infer each student’s weakest macro-skill, then create a personalized study route. 21. **Human-vs-Agent Difficulty Flip**: Compare human difficulty data with what agents solve easily; discuss what remains worth learning. 22. **AI Hallucination Museum**: Collect agent failures: fabricated API endpoints, wrong column names, off-by-one dates, invalid CORS assumptions, fake package behavior. 23. **Multiple-Agent Jury**: Run the same question through GPT, Claude, Gemini, Perplexity/Codex; compare answer, evidence, and verification. 24. **Answer Provenance Ladder**: Force the agent to mark every claim as observed, computed, looked up, inferred, or guessed. 25. **Exam-to-Interactive Explainer**: Convert one hard question into a tiny interactive HTML explainer that lets students vary inputs. 26. **Transcript-to-Study Ritual**: Use a workshop recording/transcript to extract what confused students, then generate a follow-up drill. 27. **Bookmarklet-to-Agent Pipeline**: Browser bookmarklet copies page context; Local MCP bash receives it; agent runs local tools and returns an answer. 28. **Anti-Cheating by Design**: Students design one question where AI can solve the mechanics but only humans can evaluate whether the result is meaningful. 29. **Tool Failure Drill**: Deliberately break environment variables, ports, CORS, or dependencies; agent must diagnose from logs. 30. **Reset vs Debug Tournament**: Compare two strategies: keep debugging one AI thread vs restart with better context. Measure time-to-correct. ## Critique and scoring Scores: Impact, Novelty, Speed. 5 is high. | # | Exercise | Assumption that must hold | Why non-obvious | Why it may fail | I | N | S | | -: | -------------------------------- | --------------------------------------- | -------------------------------------------------- | --------------------------------------- | -: | -: | -: | | 1 | Exam Autopsy Dashboard | Agent can read repo structure | Reveals hidden assessment design, not just answers | Too much repo context may overwhelm | 5 | 4 | 3 | | 2 | Client-Side Answer Leak | Checker/answer logic is bundled | Shows “view source” as exam-solving | May look like cheating, frame carefully | 5 | 5 | 5 | | 3 | Hidden Comment Trap | Browser exposes hidden HTML | Tests inspection, not visible reading | Some students may miss ethical boundary | 4 | 5 | 5 | | 4 | DOM-to-Markdown Bookmarklet | Page DOM is accessible | Turns browser page into agent context | Dynamic shadow DOM may break | 5 | 4 | 4 | | 5 | Network Contract Inspector | Requests are visible/interceptable | Exam is an API conversation | Auth/CORS may block clean demo | 4 | 5 | 3 | | 6 | Checker-Driven Solver | Source/checker is accessible | Solving by reading grader, not prompt | Unavailable in real exams | 5 | 5 | 3 | | 7 | Error-Message Oracle | Checker gives useful errors | Wrong answers become probes | Could require many attempts | 4 | 4 | 4 | | 8 | Deterministic Seed Attack | Seed logic is visible | Personalized exams may be reproducible | Needs code access | 4 | 5 | 3 | | 9 | Question Router | Question types are diverse | Skill is delegation choice | Can become a classification exercise | 5 | 3 | 5 | | 10 | Exam Speedrun Route | Timing matters | Treats exam like operations planning | May seem gimmicky | 4 | 5 | 4 | | 11 | In-Browser DuckDB Solver | DuckDB data is extractable | Browser is already a compute engine | Setup may be fiddly | 4 | 4 | 4 | | 12 | Pyodide/Numpy Mirror | Pyodide logic is reproducible | Browser Python can be mirrored locally | Base64/binary vectors may distract | 4 | 4 | 3 | | 13 | Server-Side Verifier Replay | Endpoint contract is clear | “Correct” means satisfying checker contract | Local deployment friction | 5 | 4 | 3 | | 14 | CORS as Test Subject | Browser checker validates CORS | Correct backend can still fail | Students may find it boring | 4 | 3 | 4 | | 15 | LLM-as-Judge Reverse Engineering | Rubric prompt is visible/inferable | AI grading becomes inspectable | Judge behavior can be inconsistent | 4 | 5 | 3 | | 16 | Markdown Nesting Failure | Structural parser is strict | Looks-right is not parse-right | Demo may be too narrow | 5 | 4 | 5 | | 17 | Browser Console as Tutor | Console errors exist | DevTools becomes a study partner | Needs students comfortable with console | 4 | 3 | 5 | | 18 | Playwright Exam Bot | Login/mock exam accessible | Full browser automation feels magical | Too much live-coding risk | 5 | 5 | 2 | | 19 | Wrong-Answer Postmortem | Students bring wrong questions | Converts failure into diagnosis | Needs real examples | 5 | 3 | 5 | | 20 | Skill Map from Scores | You have scores/question metadata | Personalizes “what to learn” | Privacy/anonymization needed | 5 | 4 | 3 | | 21 | Human-vs-Agent Difficulty Flip | Agent performance can be estimated live | Reframes degree around residual skills | Needs good examples | 5 | 5 | 4 | | 22 | AI Hallucination Museum | Agents will fail visibly | Failure is the lesson | May not fail on stage | 5 | 4 | 3 | | 23 | Multiple-Agent Jury | Multiple models available | Disagreement exposes uncertainty | Can be slow | 4 | 3 | 3 | | 24 | Answer Provenance Ladder | Agent can self-label evidence | Teaches verification discipline | Models may overclaim provenance | 5 | 4 | 5 | | 25 | Exam-to-Interactive Explainer | Agent can build simple HTML | Converts exam into manipulable concept | Time-consuming live | 4 | 4 | 3 | | 26 | Transcript-to-Study Ritual | Transcript available | Learning comes from workshop exhaust | Better post-workshop than live | 4 | 4 | 2 | | 27 | Bookmarklet-to-Agent Pipeline | Local MCP can receive context | Browser + local shell is powerful combo | Integration may be brittle live | 5 | 5 | 3 | | 28 | Anti-Cheating by Design | Students can think like exam designers | Best way to learn AI limits is design | Abstract unless grounded | 4 | 4 | 4 | | 29 | Tool Failure Drill | Controlled broken setup exists | Environment > knowledge is visible | Can derail session | 4 | 4 | 3 | | 30 | Reset vs Debug Tournament | Same task can be run twice | Teaches agent workflow hygiene | Needs time tracking | 4 | 4 | 4 | ## Recommended practical demo set ### 1. Browser Autopsy: “The page is the syllabus” Use `q-trick-question-server`, `q-share-secret-server`, and one normal-looking question. Demonstrate a bookmarklet or DevTools snippet that extracts visible text, hidden comments, links, input fields, scripts, and network calls. The non-obvious insight: a browser-based exam is not just text on a page. It is a live program. Advanced AI use begins by giving the agent the whole program context, not just the visible question. Suggested flow: 1. Show the visible question. 2. Ask students what they think it tests. 3. Run the DOM/context extraction. 4. Ask the agent to identify hidden constraints, checker logic, and possible answer path. 5. Conclude: “Reading the question is no longer enough. Inspecting the system is part of literacy.” This is likely the strongest opener. ### 2. Checker-Driven Solving: “Make the grader happy” Use one question with an answer function and one FastAPI-style verifier. Ask the agent to read the checker before solving. It should identify required columns, tolerances, headers, response schema, CORS, and edge cases. The non-obvious insight: many exams secretly test contract satisfaction. The answer is not “what seems right”; it is “what the verifier accepts.” This maps directly to real work: APIs, tests, CI, validators, schemas, rubrics. Demo candidates from your repo: `q-markdown-architecture`: looks like writing, but is actually AST/schema compliance. `q-fastapi-timeseries-cache`: looks like backend coding, but is really contract + CORS + caching behavior. `q-seaborn-data-visualization`: looks like visualization, but is GitHub artifact + file validation + image validation. ### 3. Difficulty Flip: “What humans find hard, agents route around” Use `dumps/difficulty.md`, `dumps/analysis.md`, and `dumps/skill_analysis_summary.md`. Show examples where students struggle: FastAPI, DevOps/platform setup, security/auth/adversarial robustness, hidden constraints. Then show how an agent approaches them: inspect, script, run, validate, retry. The non-obvious insight: exams are often hard for humans because of orchestration friction, not conceptual depth. Coding agents are good at orchestration when given tools. Therefore students should learn diagnosis, verification, and taste. Live exercise: Ask the agent: “From this difficulty summary, pick 3 questions where human pass rate is low but an AI coding agent with browser + bash should have an advantage. For each, explain the likely human blocker, agent route, and what the student should actually learn.” ### 4. Wrong Answer Postmortem: “Your mistake is training data” Ask students to bring one question they got wrong. Feed the question, their answer, expected answer/checker error if available, and the final correct solution. Ask AI to produce: “What was the likely misconception?” “What clue did you miss?” “What would an expert check first?” “Create 3 near-miss variants that would catch the same misconception.” “What should I practice for 10 minutes?” The non-obvious insight: AI’s best learning role is not giving answers. It is converting mistakes into targeted drills. This aligns with your “directional feedback” theme. This is the most useful student-facing ritual. ### 5. Provenance Ladder: “Did it know, compute, inspect, or guess?” After the agent solves a question, require it to mark every step: Observed in prompt. Observed in DOM/source. Observed in network. Computed by code. Verified by checker. Inferred. Guessed. The non-obvious insight: students should not ask “Is the answer correct?” They should ask “What is the evidence chain?” This is the core skill when AI takes over execution. This can become the workshop’s central study habit. ## Recommended wildcard demos ### Wildcard 1. Playwright Exam Bot Build a tiny browser agent that opens a mock exam, extracts each question, downloads data, submits answers, and logs failures. Do not attempt a full real exam live; use 2–3 questions. The non-obvious insight: once AI has browser control, the unit of delegation changes from “answer this question” to “operate this exam interface.” This is surprising even to advanced AI users. Failure mode: too brittle for live demo. Prepare a fallback recorded run or a prebuilt script. ### Wildcard 2. Bookmarklet-to-Local-MCP Solver Create a bookmarklet: “Copy this page’s full exam context as Markdown/JSON.” Then paste/send it to a local agent with Local MCP bash. The agent downloads linked files, runs Python/DuckDB, inspects source, computes answer, and returns a response plus provenance. The non-obvious insight: the browser is the observation layer, Local MCP is the action layer, and the model is the planner. Together, they become a practical exam-solving machine. This is probably the most “Anand-flavored” demo. ### Wildcard 3. Anti-Exam Design Lab Ask students to design a question that AI can solve mechanically but cannot safely answer without verification. Examples: A data story with a poisoned document. A chart where the obvious trend is caused by scale manipulation. A code task where tests pass but requirement is violated. A prompt where hidden instruction conflicts with visible instruction. A FastAPI task where correct logic fails because the API contract is wrong. The non-obvious insight: to understand what is worth learning, students should design questions that expose AI’s limits. Exam design becomes meta-learning. ## Final 10 exercises to run 1. **Live AI Exam Attempt**: Give a coding agent 3 real IITM/TDS questions. Let it solve with browser + bash. Do not intervene except to approve tool use. Students watch the route, not just the answer. 2. **Browser Autopsy Bookmarklet**: Run a bookmarklet that extracts visible question text, hidden comments, links, input fields, scripts, localStorage, and network endpoints. Ask: “What did the browser know that the student didn’t read?” 3. **Hidden Question / Decoy Question**: Demonstrate `q-trick-question-server`. The lesson is not “use hidden comments to cheat”; it is “interfaces can lie; inspect the system.” 4. **Client-Side Checker Leak**: Demonstrate `q-share-secret-server` or another bundled-checker example. Show how answer logic leaks when validation is shipped to the browser. 5. **Checker-First Solving**: Use `q-markdown-architecture` or a FastAPI question. Ask the agent to read the answer checker first, then solve. Show how “correctness” becomes a contract. 6. **Error-Message Oracle**: Submit an incomplete/wrong answer. Feed the exact error to AI. Let AI infer the missing condition. Repeat until correct. This teaches debugging by interrogating the grader. 7. **Question Router**: Show 8 questions and ask the agent to route each: bash, Python, DuckDB, browser, DevTools, spreadsheet, LLM, or manual review. Students learn delegation strategy. 8. **Human-vs-Agent Difficulty Flip**: Use your difficulty summaries to show what humans found hard. Ask the agent which of these it can route around and which still need human judgment. 9. **Wrong-Answer Postmortem Ritual**: Students bring one wrong question. AI converts it into misconception, missed clue, expert checklist, and 3 near-miss practice variants. 10. **Provenance Ladder**: Every AI answer must end with: observed, computed, verified, inferred, guessed. This becomes the take-home study ritual. ## Best practical sequence for the workshop Open with the live AI attempt. Then immediately autopsy the browser page. Move to checker-first solving. Then show difficulty flip using your actual course data. End with wrong-answer postmortem and provenance ladder as the students’ study ritual. That gives the workshop a clean story: AI can solve. AI can inspect. AI can exploit. AI can still hallucinate. Therefore the human skill is no longer producing answers from scratch. It is framing, routing, inspecting, verifying, and learning from failure.

</CHATGPT>

---

## Claude

<details>
<summary>Synthesized competing frameworks, identified gaps, restructured narrative arc</summary>

> Let me critically evaluate both responses and synthesize the best.
>
> **What ChatGPT does better than mine:**
>
> 1. **Checker-Driven Solving** (their #6 / "Checker-First Solving") - This is genuinely superior to anything in my list. The insight that "correctness = satisfying the grader's contract" is profound and maps to real work. I had this implicitly but didn't articulate it as a standalone exercise. They name specific questions from the repo (q-markdown-architecture, q-fastapi-timeseries-cache).
> 2. **Answer Provenance Ladder** - This is excellent and I missed it entirely.
>
> The taxonomy of observed/computed/verified/inferred/guessed is a genuinely reusable mental model that feels like the most practical daily habit to adopt from either list.
>
> 1. **Error-Message Oracle** (#7) - Using wrong answers as probes to understand the grader's expectations is elegant and I didn't frame it that clearly.
> 2. **Question Router** (#9) - Better articulated than mine. The core insight that "delegation choice is the skill" cuts to what actually matters.
> 3. **Human-vs-Agent Difficulty Flip** (#21) - They ground it in actual data from the exam directory (dumps/difficulty.md, dumps/analysis.md) which I didn't reference but which exists and could validate the claim.
> 4. **Anti-Exam Design Lab** (Wildcard 3) - This is genuinely novel and I completely missed it. Having students design AI-resistant questions as a way to understand AI's limits is brilliant pedagogy.
> 5. **Wrong-Answer Postmortem Ritual** - Similar to mine but they articulate the specific prompt template better: misconception + missed clue + expert checklist + near-miss variants.
> 6. **Narrative arc** - Their closing sequence is much cleaner: "AI can solve → AI can inspect → AI can exploit → AI can hallucinate → therefore human skill is framing/routing/inspecting/verifying." This is a better workshop spine.
> 7. **Specific question references** - They actually name specific questions from the exam repo like `q-share-secret-server`, `q-markdown-architecture`, `q-trick-question-server`, which grounds the discussion in concrete examples.
> 8. **DOM-to-Markdown Bookmarklet** - Their framing is smarter than mine: it's about giving the agent full context rather than just feeding back answers.
>
> Where I have the advantage is in the learning pipeline theme—they skip the studying half entirely, while I included exercises around derived formats, pre-exam intelligence briefs, and transcript-to-flashcards pipelines that reinforce Anand's learning focus. I also have a more concrete data-driven GA optimizer exercise grounded directly in his blog post, whereas they're more abstract.
>
> The bookmarklet technique itself is something I weighted more heavily as a specific demo, which aligns with what Anand explicitly wanted. My browser agent taking the whole exam is a stronger opener than their Playwright bot, and I surface the specific /filter endpoint vulnerability from the exam codebase that they miss entirely. I also have the screenshot-to-LLM-to-autofill pipeline they don't.
>
> What's genuinely powerful from combining both approaches is pairing the bookmarklet's full-page extraction with the agent's provenance-labeled solving—that becomes the best possible leave-behind ritual. Their narrative structure is tighter overall, but my individual demos are more concrete.
>
> I'm thinking the flow should move through four acts: first showing AI taking the exam through the browser agent and bookmarklet, then revealing what AI can inspect that you can't (source extraction, error oracles), then demonstrating how AI accelerates learning better than traditional studying, and finally closing with the anti-exam design lab as a metacognitive synthesis. The question router combined with difficulty flip would show which problems AI handles effortlessly versus where human judgment becomes essential.
>
> The real narrative arc isn't about cheating but about thinking like a system inspector—the provenance ladder becomes the key takeaway. The checker-first insight is particularly valuable because it mirrors real professional work where you're satisfying contracts and specifications rather than just solving problems. Bringing in live audience participation for a wrong-answer postmortem would make this dynamic and data-driven, and the bookmarklet-to-local-MCP-to-agent pipeline is something only Anand can demonstrate given his setup.
>
> So the revised workshop flows through a live AI exam attempt as the opener, then the browser autopsy bookmarklet to give the agent full context, checker-first solving with real examples, using error messages as probes, flipping the difficulty perception with actual data, a data-driven optimizer that turns scores into actionable playbooks, the derived formats pipeline showing how one lecture becomes five formats, a live wrong-answer postmortem with audience questions, an anti-exam design lab where students create AI-resistant questions, and finally the provenance ladder as the central ritual everyone takes home.
>
> I'm dropping the screenshot pipeline since the bookmarklet handles that, the two-LLM verification because the provenance ladder covers it better, the pre-exam brief as less compelling, and the textbook-to-brief since it overlaps with the derived formats work. From the ChatGPT list, the deterministic seed attack is too narrow, Pyodide mirror doesn't fit, the tool failure drill derails things, the reset versus debug tournament needs too much setup, multiple agents are slow, and the transcript ritual works better as a post-workshop follow-up.
>
> Done

</details>

### Critical Evaluation

**What ChatGPT does better:**

- **Checker-First Solving** is genuinely superior — the insight that "correctness = satisfying the grader's contract" is the most transferable professional skill in either list, and maps directly to real work (APIs, CI, validators, rubrics). I had it implicitly; they made it the centrepiece.
- **Provenance Ladder** (observed / computed / verified / inferred / guessed) is the best take-home ritual in either response. I missed it entirely. It's concrete, reusable, and solves the "AI is confident but wrong" problem without moralising.
- **Error-Message Oracle** — using wrong answers as _probes_ to interrogate the grader — is sharp and I didn't articulate it as a standalone exercise.
- **Anti-Exam Design Lab** (students design AI-resistant questions) is a brilliant closer I completely missed. Designing something exposes your mental model faster than solving it.
- **Specific question references** (q-markdown-architecture, q-share-secret-server, q-fastapi-timeseries-cache) — they read the repo more carefully than I did.
- **Narrative spine**: "AI can solve → inspect → exploit → hallucinate → therefore your job is framing/routing/inspecting/verifying" is cleaner than anything I articulated.

**What mine does better:**

- **Learning pipeline** (derived formats, NotebookLM, lecture → 5 formats in 10 min) — ChatGPT ignores the learning/studying theme entirely, which Anand explicitly wanted as a second thread.
- **Data-Driven GA Optimizer** (upload your scores → Claude → one-page playbook) is directly grounded in the blog post and uniquely useful to this audience.
- **Bookmarklet technique** — I gave it more weight as a specific demo mechanism, which Anand asked for.
- The **/filter endpoint leak** and the **browser agent takes the full exam** as opener — ChatGPT buries Playwright as a wildcard rather than leading with it.
- **Screenshot → clipboard pipeline** is faster to demo than a full Playwright bot.

**New thoughts from synthesis:**

- The Provenance Ladder + Bookmarklet-to-MCP pipeline is the most distinctively Anand combination: bookmarklet extracts full page context → Local MCP agent solves with provenance labels → student gets both the answer and its epistemic status. No other presenter can demo this.
- The **Checker-First insight and the Provenance Ladder are complementary**: reading the checker teaches you what "correct" means; the provenance ladder teaches you whether AI actually achieved it.
- The live wrong-answer postmortem should pull from the audience — they bring a question they got wrong, you process it live. That's Anand's audience-as-data-source style, and ChatGPT doesn't exploit it.
- Drop from mine: screenshot pipeline (subsumed by bookmarklet), two-LLM verification (subsumed by Provenance Ladder), pre-exam brief (less exciting than others).
- Drop from ChatGPT: Deterministic Seed Attack (too narrow), Pyodide Mirror (too narrow), Tool Failure Drill (derails session), Multiple-Agent Jury (slow), Transcript ritual (better post-workshop than live).

---

### Revised Top 10 Exercises

---

#### 1. Live AI Exam Attempt _(Opener)_

**Demo:** Give `agent-browser` or a Playwright script three real TDS questions — exam URL, Google login, no other help. Watch it open the browser, read questions, fire LLM calls, fill answers, and submit. Students do nothing but observe.

**Why non-obvious:** Students think of AI as a text box. Watching a browser autonomously navigate an exam interface — including downloading files, reading tables, submitting forms — reframes what "using AI" means. This is the workshop's thesis in 90 seconds.

**May fail:** Dynamic/randomised questions need the agent to read and adapt. Prepare a recorded fallback.

---

#### 2. Browser Autopsy Bookmarklet

**Demo:** On any TDS exam page, run a bookmarklet that extracts visible question text, HTML comments, links, input field IDs, downloadable files, console errors, and active network endpoints — all packaged as Markdown and sent to the agent.

**The non-obvious insight:** A browser-based exam is not text on a page — it is a live program. Advanced AI use begins by giving the agent the _whole program context_, not just the visible question. Most students have never opened DevTools during an exam.

**Leaves behind:** A 10-line bookmarklet they can adapt to any webpage.

---

#### 3. Checker-First Solving _(Centrepiece)_

**Demo:** Use `q-markdown-architecture` (looks like writing, is actually AST/schema compliance) and `q-fastapi-timeseries-cache` (looks like backend coding, is actually contract + CORS + caching). Ask the agent to _read the answer checker first_, then solve.

**The non-obvious insight:** Many exams secretly test contract satisfaction. "Correct" means "what the verifier accepts," not "what seems right." This maps directly to real work — APIs, test suites, CI pipelines, rubrics. Students who learn to read the checker before solving are already thinking like engineers.

**Demo candidates from repo:** `q-seaborn-data-visualization` (GitHub artifact + image validation), `q-fastapi-aggregation` (CORS as explicit grading criteria).

---

#### 4. Error-Message Oracle

**Demo:** Submit a plausible but wrong answer to a live question. Feed the exact error message to the agent: "Here is the question and the validator's error. What is the missing condition?" Repeat until correct. Show the convergence arc.

**The non-obvious insight:** Wrong answers are _probes_, not failures. Every error message is the grader telling you what it needs. Students who treat errors as data get faster feedback loops than students who treat errors as shame.

---

#### 5. Human-vs-Agent Difficulty Flip

**Demo:** Pull up `dumps/difficulty.md` and `dumps/analysis.md` from the exam repo. Show the questions humans found hardest (FastAPI, DevOps setup, auth, hidden constraints). Ask the agent: "Which of these can you route around with browser + bash, and which still need human judgment?" Show the split.

**The non-obvious insight:** Exams are often hard for humans because of _orchestration friction_, not conceptual depth. Agents are good at orchestration. Therefore what remains worth learning is diagnosis, verification, and taste — not syntax and setup.

**Audience activity:** Students vote on which questions they think AI will solve. Compare predictions to actual agent performance.

---

#### 6. Data-Driven GA Strategy Optimizer

**Demo:** Upload `results.csv` from the exam repo to Claude live. Replicate the one-page playbook from the blog post: "Tell me exactly which GAs to focus on and which to skip to avoid failing / hit an A / hit an S." Show the output.

**The non-obvious insight:** Students think AI is for solving questions. Using it to strategize _which questions not to bother solving_ is a different posture — not harder work, smarter allocation. The prompt matters more than the effort.

**Leaves behind:** The exact upload + prompt workflow they run on their own data tonight.

---

#### 7. Derived Formats Pipeline _(Learning Thread)_

**Demo:** Take a TDS YouTube lecture. Use YTScribe for the transcript. Feed to Gemini: generate a podcast script (NotebookLM), a sketchnote (Gemini sketchnote prompt), a 10-question practice quiz, a flashcard Q&A deck, and a summary song. Show all five outputs from one source in under 10 minutes.

**The non-obvious insight:** Students consume content in one format. The same hour of lecture can become a week of study material in the time it takes to copy a URL. The skill is knowing what format you learn best from — and delegating the conversion.

**Leaves behind:** The prompt chain as a reusable workflow.

---

#### 8. Bookmarklet → Local MCP Agent Pipeline _(Most "Anand-flavoured" Demo)_

**Demo:** Bookmarklet scrapes the full exam page context into Markdown. Sends it to the Local MCP bash agent. Agent downloads linked files, runs Python/DuckDB locally, inspects source, computes answer — and returns the answer _plus a provenance label for every step_.

**The non-obvious insight:** Browser is the observation layer. Local MCP is the action layer. The model is the planner. Together, they form a complete exam-solving machine that no one in the room has seen before, because it requires your specific setup.

**May fail:** Integration can be brittle live. Have the bookmarklet output ready to paste manually as fallback.

---

#### 9. Wrong-Answer Postmortem _(Audience-as-Data-Source)_

**Demo:** Ask the audience to submit one question they got wrong recently. Take 2–3 live. For each, feed the question, their answer, and the checker error to Claude with this prompt: "What was the likely misconception? What clue did they miss? What would an expert check first? Give me 3 near-miss variants that test the same misconception. What should they practise for 10 minutes?"

**The non-obvious insight:** AI's best learning role is not giving answers — it is converting mistakes into targeted drills. Students who feed their failures to AI learn faster than students who re-read their notes.

**Audience-as-data-source mechanic:** Their wrong answers become the workshop's raw material.

---

#### 10. Anti-Exam Design Lab + Provenance Ladder _(Closer)_

**Two-part closer:**

**Part A — Anti-Exam Design Lab:** Ask students to design one question where AI can solve the mechanics but cannot safely answer without verification. Examples: a chart where the obvious trend is caused by scale manipulation; a FastAPI task where tests pass but the requirement is violated; a dataset where the correct SQL returns the wrong business answer. The best designs reveal exactly what humans must still learn.

**The non-obvious insight:** To understand AI's limits, design questions that expose them. Exam design is the deepest form of metacognition.

**Part B — Provenance Ladder (the take-home ritual):** After any AI answer, require it to label every step:

- _Observed_ in the prompt / DOM / source
- _Computed_ by code
- _Verified_ by checker
- _Inferred_ from context
- _Guessed_

Anything labelled "guessed" is a human checkpoint. This becomes the daily study habit — not "is the answer correct?" but "what is the evidence chain?"

---

### Workshop Narrative Arc

| Act                                      | Message                               | Exercises                                  |
| ---------------------------------------- | ------------------------------------- | ------------------------------------------ |
| **1. AI can take your exam**             | It's more capable than you thought    | #1 Live attempt, #2 Bookmarklet            |
| **2. AI can inspect what you can't see** | The page is a program, not a document | #3 Checker-first, #4 Error oracle          |
| **3. AI can flip the difficulty curve**  | Orchestration ≠ understanding         | #5 Difficulty flip, #6 GA optimizer        |
| **4. AI makes learning faster**          | Delegate format, keep judgment        | #7 Derived formats, #8 MCP pipeline        |
| **5. AI still fails — here's your job**  | Frame, route, inspect, verify         | #9 Postmortem, #10 Design lab + Provenance |

---

## User

Next, create a catalogue of techniques I can teach students on how to use AI to take exams / study for them. Apart from what you have researched, you may also want to take a deeper look at: - techniques I have talked about students using (see ~/code/blog/ for posts tagged llms AND education) - how students have hacked TDS exams (also see ~/Dropbox/notes/transcripts/) - approaches that ~/code/exam/ has patched in the past (git history) due to student hacks Convert the techniques into a JSON-Lines file with a consistent schema that includes: - an id, name - why: why the technique works and what it achieves - watch_for: what to watch out for - steps: an array of steps to execute the technique - impact and ease as numbers between 0-1 - examples: an array of {link - to a file / URL that exemplifies the technique, context: explaining clearly what in that link exemplifies the technique and how - to the point where just reading that context is sufficient} This is my guess on the format. Think like an expert and if you spot any improvements, feel free to change the format. Generate a comprehensive `techniques.jsonl` with all the techniques you find.

---

## Claude

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/blog
# Find posts tagged both llms and education
for f in $(grep -rl \"categories:\" posts/ pages/ 2>/dev/null); do
if grep -qi \"llm\" \"$f\" && grep -qiE \"education|exam|student|teach|course|tds|learn\" \"$f\"; then
# confirm it's in categories block
cats=$(awk '/^categories:/{flag=1;next}/^[a-z_]+:/{flag=0}flag' \"$f\" | tr '\
' ' ')
echo \"$f :: $cats\"
fi
done | head -60
"
}
```

Response

```
posts/2005/excel-avoid-manual-labour-3.md ::   - excel-tips
posts/2026/things-i-learned-10-may-2026.md ::   - til
posts/2026/sonnet-4-6-vs-minimax-m2-7.md ::   - llms   - coding
posts/2026/migrating-tds-from-docsify-to-hugo.md :: - llms - coding - education
posts/2026/interactive-explainers.md ::   - education   - llms
posts/2026/speaking-unprepared.md ::   - llms
posts/2026/add-a-verify-button.md ::   - llms
posts/2026/hack-of-the-day-on-times-of-india.md ::   - llms
posts/2026/oh-shit-moments-with-gen-ai.md ::   - links
posts/2026/ai-advice-for-teams.md ::   - llms
posts/2026/ai-expert-lens.md :: - llms
posts/2026/creating-comic-explainers.md ::   - llms
posts/2026/can-ai-discover-new-data-visualizations.md :: - llms - visualisation
posts/2026/blog-embeddings-map.md :: - llms - coding - how-i-do-things
posts/2026/ai-agents-to-hire.md ::   - how-i-do-things   - llms
posts/2026/people-skills-with-ai.md ::   - llms
posts/2026/migrating-my-blog-from-wordpress-to-hugo.md ::   - coding
posts/2026/my-changing-ai-opinions.md ::   - llms
posts/2026/using-browser-tabs-as-slides.md :: - how-i-do-things - llms
posts/2026/how-the-innovation-team-works.md ::     - how-i-do-things
posts/2026/analaizing-cloud-costs.md :: - llms
posts/2026/things-i-learned-29-mar-2026.md ::   - til
posts/2026/things-i-learned-07-jun-2026.md ::   - til
posts/2026/the-nov-2025-vibe-coding-ghost-revolution.md ::   - coding   - llms
posts/2026/using-codex-to-improve-codex.md :: - llms - tools
posts/2026/memorable-explanations.md :: - simple-explanations
posts/2026/how-i-use-ai-to-teach.md ::   - education   - llms   - how-i-do-things
posts/2026/coding-agents-are-the-new-software.md ::   - llms   - coding
posts/2026/finding-old-friends-with-gemini.md :: - llms
posts/2026/things-i-learned-01-feb-2026.md ::   - til
posts/2026/the-future-of-work-with-ai.md :: - education - llms - how-i-do-things
posts/2026/editing-images-with-code-and-ai.md ::   - llms
posts/2026/using-ai-for-work-news.md :: - business-realities - llms
posts/2026/google-ai-tools-list.md :: - tools - llms
posts/2026/the-nano-banana-paradox.md :: - llms
posts/2026/how-to-use-ai-for-research.md ::   - llms
posts/2026/tds-comic-generation.md :: - llms - education
posts/2026/tds-project-1-was-an-experiment.md ::   - education   - llms
posts/2026/searxng-and-vane.md ::   - tools
posts/2026/ai-policies-across-universities.md ::   - llms   - education
posts/2026/gemini-cli-harness-is-not-good-enough.md :: - llms
posts/2026/prototyping-the-prototypes.md :: - llms
posts/2026/using-codex-as-my-os.md ::   - llms   - coding
posts/2026/when-to-use-which-gemini-mode.md :: - llms
posts/2026/tools-in-data-science-jan-2026.md :: - education - data - llms
posts/2026/learnings-from-building-babbage-insight.md :: - links - business-realities
posts/2026/live-vibe-coding-using-others-ideas.md ::   - llms   - talks
posts/2026/writing-articles-from-my-blog-posts.md :: - llms
posts/2026/tds-jan-2026-ga1-released.md :: - education - coding - llms
posts/2026/how-ai-bottlenecks-shift.md ::   - llms
posts/2026/leaked-key-sociology.md :: - coding - llms
posts/2026/breaking-rules-in-the-age-of-ai.md :: - education - llms
posts/2026/longest-repeated-paragraph-on-wikipedia.md ::   - llms   - data   - visualisation
posts/2026/ai-for-film-dialogues.md :: - llms
posts/2026/transcript-ai-ded-interviews.md :: - llms
posts/2026/humans-have-taught-llms-well.md ::   - llms   - funny
posts/2026/things-i-learned-04-jan-2026.md ::   - til
posts/2026/new-ways-of-reading-books.md ::   - how-i-do-things   - llms
posts/2026/gemini-3-flash-ocrs-dilbert-accurately.md :: - llms
posts/2026/the-jamnagar-chokepoint-data-story.md ::   - llms   - data   - visualisation
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/blog
# Read the most relevant education+llm posts in full
for f in posts/2026/how-i-use-ai-to-teach.md posts/2026/tds-project-1-was-an-experiment.md posts/2026/breaking-rules-in-the-age-of-ai.md posts/2026/ai-policies-across-universities.md posts/2026/add-a-verify-button.md; do
echo \"===== $f =====\"
cat \"$f\" 2>/dev/null
echo \"\"
done
"
}
```

Response

```
===== posts/2026/how-i-use-ai-to-teach.md =====
---
title: How I use AI to teach
date: 2026-03-20T07:12:47+05:30
categories:
- education
- llms
- how-i-do-things
description: AI can reshape teaching most effectively when it changes the structure of learning and assessment, not just the speed of content creation.
keywords: [AI in education, teaching methods, assessments, pedagogy, Tools in Data Science, experimentation]
---
I've been using AI in my [Tools in Data Science](https://tds.s-anand.net/) course for over two years - to teach AI, _and_ using AI to teach.
I told GitHub Copilot ([prompt](https://github.com/sanand0/talks/blob/a4ccc33e6b534853ae28d7ed5584b982cfc38193/2026-03-18-iitm-academic-council/prompts.md)) to go through my transcripts, [blog posts](https://www.s-anand.net/), [code](https://github.com/sanand0), and [things I learned](https://til.s-anand.net/) since 2024 to list my _every_ experiment in AI education, rating it on importance and novelty.
[Here is the full list of my experiments](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html).
**1\. Teach using exams and prompts, not content**
- ⭐ [**Use exams to teach**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=learn-by-solving). The typical student is busy. They want grades, not learning. They'll write the exams, but not read the content. So, I moved the course material _into_ the questions. If they can answer the question, great. Skip the content.
- [**Use AI to generate the content**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-comics). I used to write content. Then I linked to the best content online -- it's better than mine. Now, AI drafts comics, interactive explainers, and simulators. My job is to pick good topics and generate in good formats.
- [**Give them prompts directly**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-explainers). Skip the content! I generated them with prompts _anyway_. Give students the prompts _directly_. They can use better AI models, revise the prompts, and learn how to learn with AI.
- ⭐ [**Add an "Ask AI" button**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ask-ai-button). Make it _easy_ for students to use ChatGPT. Stop pretending that real-world problem solving is closed-book and solo.
- ⭐ [**Make test cases teach, not just grade**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=test-as-tutor). Automate the testing (with code or AI). Good test cases show students the _kind_ of mistake they may - teaching them, not just grading them. That's great for teachers to analyze, too.
- [**Test first, then teach from the mistakes**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=test-first-teach). Let them solve problems first. **Then** teach them, focusing on what failed. AI does the work; humans handle what AI can't. This lets us teach really useful skills based on real mistakes.
**2\. Make cheating pointless through design, not detection**
- ⭐ [**Allow copying, collaboration, and hacking**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=copy-collaborate). In real work, nobody gets bonus points for working alone or re-inventing the wheel. Collaboration, using available resources well, verifying inputs, disclosed shortcuts -- all are rewarded.
- [**Reward originality without punishing collaboration**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=reward-originality). Blanket anti-copying rules assume that all similarity is bad. A more AI-native approach is to allow learning from others openly, but give extra credit for genuine variation, initiative, and novel improvement.
- ⭐ [**Give each student a unique variant**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=unique-variants). If everyone sees the same problem with the same visible answer path, answer-sharing becomes the dominant strategy. Deterministic but unique variants shift the game from leaking answers to actually solving the problem.
- [**Make process logs part of the evidence**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=process-logs). When outputs can be copied or AI-generated, the trace becomes more valuable than the final artifact. Logs, verification notes, session recordings, and agent traces show whether the student can actually orchestrate the work.
- [**Use repo-grounded vivas for authenticity**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=repo-viva). If you really want to know whether a student owns their project, ask them questions drawn from their own repo and make them change something live. That is much harder to fake than polished submitted output.
- [**Use structural similarity, not string matching**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=copy-detection). Strip docstrings, tokenize, MinHash. Students who rename variables are still caught; students who genuinely collaborated produce detectable clusters rather than suspicious pairs.
**3\. Test skills that matter in an AI world**
- ⭐ [**Teach what AI still cannot do well**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=teach-ai-limits). Syntax and routine execution are declining in value. Judgment, debugging, orchestration, validation, integration, and taste are rising. The curriculum should move upward, not cling to the parts AI is already eating.
- [**Use hard, messy problems to build real resilience**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=messy-problems). Some questions should be intentionally tricky, partly wrong, hidden in the UI, or out of syllabus. The students who find and solve them anyway are demonstrating exactly the adaptability that real work demands. Smooth progression alone doesn't build that.
- [**Test live, hands-on AI skills**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=hands-on-skills). Don't just lecture about embeddings, vision, structured outputs, or hallucinations. Put students in live API-driven tasks where they have to use these things under time pressure and genuine uncertainty.
- [**Grade students on designing AI workflows**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-workflow-design). In many real settings, the important skill is not "give the answer" but "design the chain of steps that gets to the answer reliably." That includes tools, prompts, datasets, quality checks, fallbacks, and output formats.
- [**Use game-like tasks to teach agentic work**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=game-learning). Mazes, escape rooms, and API games force state tracking, exploration strategy, and backtracking — exactly the behaviors agentic systems require. They're not gimmicks; they're the syllabus.
- [**Test prompt attacks and defenses**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=prompt-attacks). Security and adversarial literacy should not be abstract topics. Make students jailbreak, defend, manipulate, and harden model behavior. That turns "prompt security" from a lecture topic into a measurable skill.
**4\. Make assessment more like real work**
- [**Grade richer work, not just one-line answers**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=rich-work-grading). Real work is often multimodal: images, stories, APIs, analyses, and dashboards. If assessment automation cannot handle those, it will keep pushing education toward fake neatness.
- [**Grade the spec, not the code**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=specs-tests-assignment). When AI writes the code, the real artifact is the machine-readable brief: goal, constraints, done-when, counter-examples, eval suite. That is often where the actual thinking lives anyway.
- [**Count real open-source contributions as coursework**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=open-source-coursework). A merged PR to a public repo is harder, messier, and more educational than most sealed academic assignments. It teaches scoping, etiquette, usefulness, and real external standards.
- [**Let students build virtual TAs from real course material**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=virtual-ta). The project is educational, and the output becomes infrastructure for the next cohort. Good assignments should create assets, not just submissions.
- [**Reward originality structurally, not just rhetorically**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=originality-bonus). Most courses praise creativity but grade only correctness. Use embeddings to measure cohort-level similarity and explicitly reward meaningfully distinct outputs. Originality becomes real, not decorative.
**5\. Use AI to build the course, not just teach inside it**
- [**Let AI write, test, and fix draft questions**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-writes-questions). The interesting move is not just "AI drafts items." It is "AI drafts, runs, breaks, revises, and improves them before any student sees them." That dramatically changes how fast a course can evolve.
- [**Use coding agents to test the exam before students do**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=agent-exam-testing). If an agent solves a question instantly, you should ask what the question is actually measuring. Agents become both QA tools and mirrors for curricular relevance.
- [**Use AI-generated comics to explain why the question exists**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-comics). Students often resist tasks they do not understand. A comic can smuggle in the pedagogical point with very low friction and high memorability.
- [**Use interactive explainers for unfamiliar concepts**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-explainers). AI can generate not just text answers but visual, animated, intuitive explanations. That makes concept onboarding faster for both students and new faculty.
- [**Keep teacher adoption in familiar formats**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=teacher-first-ai). A good innovation that slots into slides, handouts, OCR flows, and short feedback loops will beat a brilliant system nobody can actually use next semester.
**6\. Build the infrastructure for AI in education**
- ⭐ [**Break rubrics into binary sub-criteria; reason before judging**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-grading). Open-ended project grading becomes more auditable when you decompose it into binary yes/no criteria and ask the model to explain its reasoning before delivering a verdict. High or suspicious scores get re-evaluated with stronger guardrails.
- [**Give every student shared, budgeted AI access**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=shared-ai-access). If AI access depends on personal subscriptions, the institution is quietly grading wealth, not skill. Shared governed access makes AI a course capability, not a private advantage.
- [**Let AI handle routine support; keep humans for judgment**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-routine-human-judgment). AI handles repetitive, searchable, first-pass questions. Humans handle ambiguity, reassurance, escalation, and final accountability. Neither alone is the right model at scale.
- [**Turn recurring answers into canonical Q&A cards**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=canonical-qa). Once the same question appears three times, it should stop living in somebody's head or an old thread. Convert it into a canonical artifact that both humans and bots can cite consistently.
- [**Govern with green/amber/red review levels**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=green-amber-red). Not every decision needs the same scrutiny. Auto-ship the low-risk, spot-check the medium-risk, always human-review the high-stakes. This is how you scale without losing trust.
- [**Roll out in shadow mode first**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=shadow-mode-rollout). High-stakes academic workflows should not be launched with fingers crossed. Run the AI system quietly in parallel with human judgment and learn before turning it loose.
- [**Turn policy into executable checks**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=policy-as-code). A policy that cannot be operationalized at scale is mostly theater. If you can translate rules and rubrics into machine-checkable form, governance becomes consistent rather than person-dependent.
- [**Make the course publicly inspectable**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=open-course). Openness raises the bar. It invites scrutiny, reuse, criticism, and improvement, and it turns the course into a visible institutional experiment rather than a sealed classroom.
- [**Use reasoning models only for the borderline cases**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=reasoning-verifier). Cheap screening first, expensive verification for the high-stakes or suspicious. Increasing reasoning effort on even a small model can flip an evaluator from sloppy to reliable — the cost curve makes this the natural operating model.
**7\. Analyze and research learning exhaust**
- [**Track which AI tools students actually use**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=track-ai-tools). Once AI use is instrumented, you stop guessing. You can see which models students choose, when they ask for help, and what behavior actually correlates with success.
- [**Redesign exams from behavior data, not intuition**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=behavior-data-exam). Model choice, timing, retry patterns, and deadline behavior all reveal how students really work. That should feed back into question design, support strategy, and pacing.
- [**Analyze broken code before it compiles**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=pre-compile-analysis). Novices often fail at syntax long before you reach the real misconception. Structural parsing of broken code lets you give feedback on thought process instead of just rejecting the submission.
- [**Use code traces to surface hidden misconceptions**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=code-trace-misconceptions). Timestamped traces reveal overfitting, thrashing, structural confusion, and missing invariants — patterns that polished final submissions hide entirely.
- [**Turn replay galleries into faculty-readable stories**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=exam-replay). Raw logs do not change policy. Narrated replays and plain-language error-pattern reports do. The point is to make evidence legible to decision-makers, not just analysts.
- [**Break problem-solving into coachable steps**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=coachable-steps). "Weak student" is too vague to be useful. Better to ask: did they fail at reading the givens, choosing a strategy, surviving a multi-select trap, or knowing when to cut losses? Each is a trainable failure mode.
- [**Study bias in peer review itself**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=peer-review-bias). If peer assessment matters, reviewer quality matters too. You can detect generous, timid, extreme, and calibrated graders from the data, then moderate or train accordingly.
- [**Treat learning analytics as a reusable research programme, not a one-off dashboard**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=learning-analytics). The infrastructure for tracking misconceptions, prerequisite transfer, and course-to-course movement can be built once and reused across cohorts. That turns isolated AI experiments into institute-level knowledge and publishable educational research.
**8\. Upgrade the human role**
- [**Make judgment and taste explicit learning goals**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=judgment-taste). AI makes average output cheap. The premium moves to selecting what is worth doing, recognizing quality, and knowing what to reject. That is a teachable skill, not a vague aspiration.
- [**Teach directional feedback as a skill**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=directional-feedback). You do not always need to micromanage AI with detailed corrections. The higher-order skill is to say "more concrete," "less jargon," "optimize for faculty adoption," or "make this defensible." That is learnable and more effective than micromanaging.
- [**Teach faculty to manage agents, not just chat with them**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=manage-agents). Institutional AI does not scale on prompting alone. People need to learn specs, budgets, kill switches, and escalation rules — orchestration literacy, not just chatbot familiarity.
- [**Use AI as a personalized coach**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=ai-coach). The model is not just an answer engine. It can become a research guide, curiosity amplifier, and next-step recommender tailored to the individual learner's gaps and goals.
- [**Let non-coders build interactive learning tools**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=no-code-tools). AI lowers the cost of making timelines, maps, biographies, and interactive explainers. That opens AI-native pedagogy far beyond computer science into humanities and social sciences.
- [**Teach students to run many AI attempts in parallel**](https://sanand0.github.io/talks/2026-03-18-iitm-academic-council/ideas/table.html?id=parallel-ai). One of the biggest AI-native workflow shifts is from single-path effort to portfolio thinking — run several attempts, compare them, and converge faster. That is a teachable habit, not an obvious default.
===== posts/2026/tds-project-1-was-an-experiment.md =====
---
title: TDS Project 1 was an experiment
date: 2026-04-03T16:05:24+08:00
categories:
- education
- llms
description: The project was not just an assignment but a live experiment in how students perform on analytics versus design tasks in an AI era, revealing both strengths and gaps.
keywords: [AI in education, project-based learning, design skills, analytics, student evaluation, experimentation]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7446017785836720128/
---
[TDS Project 1](https://sanand0.github.io/datastories/tds-2026-01-p1/) wasn't just a student project. It was a research and social experiment, too.
We tested [two skills](https://sanand0.github.io/datastories/tds-2026-01-p1/stories/two-exams.html) \- analytics and design. The design tests were diverse -- and students fared worse there.
Design may matter more in the AI era, and I'm glad some [designs](https://sanand0.github.io/datastories/tds-2026-01-p1/gallery/index.html) are brilliant. (But not diverse/creative enough.) [I also learnt](https://sanand0.github.io/datastories/tds-2026-01-p1/stories/model-playbook.html) that Gemini beats Midjourney, which beats ChatGPT for image generation.
[![](https://sanand0.github.io/datastories/tds-2026-01-p1/screenshot.webp)](https://sanand0.github.io/datastories/tds-2026-01-p1/gallery/)
I asked them to contribute to open source. Most [PRs were trivial](https://sanand0.github.io/datastories/tds-2026-01-p1/stories/two-labor-markets.html). But five students made a real difference. For example, this [PR](https://github.com/marimo-team/marimo/pull/8520) to Marimo is excellent!
Most importantly, [they're actively collaborating now](https://sanand0.github.io/datastories/tds-2026-01-p1/stories/social-infrastructure.html) - a critical skill in the AI era. One student WhatsApp-ed me:
> Before this i was not interacting with anyone\
> Because of the online nature of this degree\
> \
> But TDS helped me to connect with everyone\
> We are having meet regularly\
> We divide questions with each other\
> And then we solve and discuss
_THIS_ is what I've been trying to teach for 5 years now!
===== posts/2026/breaking-rules-in-the-age-of-ai.md =====
---
title: Breaking Rules in the Age of AI
date: '2026-02-01T14:58:28+08:00'
categories:
- education
- llms
description: AI-era education should stop preserving old constraints and instead teach around the new freedoms and failure modes that AI creates.
keywords: [education, AI, pedagogy, assumptions, rule breaking, curriculum design]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7423904243796922368/
---
Several educators have AI-enabled their courses, like:
1. David Malan at [Harvard CS50](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf) provides an AI-powered "rubber duck debugger" trained on course-specific materials.
2. Mohan Paturi at [UC San Diego](https://today.ucsd.edu/story/this-bespoke-ai-tutor-helps-students-learning) has deployed AI-tutors to his students.
3. Ethan Mollick at [Wharton](https://www.oneusefulthing.org/p/management-as-ai-superpower) uses AI as tutor, coach, teammate, simulator, even student, and runs simulations.
4. Jeremy Howard's [Fast.ai](https://course.fast.ai/) encourages students to use LLMs to write code, with a strict verification loop.
5. Andrew Ng [DeepLearning.AI](https://www.deeplearning.ai/) integrates a chatbot into the platform, next to code cells, to handle syntax errors and beginner questions.
But no one seems to have [_eliminated_ reading material, nor added an "Ask AI" button to solve each question](https://www.s-anand.net/blog/tools-in-data-science-jan-2026/), nor run it at my scale (~3,000 students annually).
Nice, but **what should I teach in the age of AI**?
[Simon Willison](https://simonwillison.net/2026/Jan/31/collective-efficacy/) led me to [Matt Webb](https://interconnected.org/home/2026/01/30/efficacy) led me to [Milan Cvitkovic](https://milan.cvitkovic.net/writing/things_youre_allowed_to_do/) led me to think about assumptions and things we assume we can't do.
We've taught students a lot of _"learned helplessness"_, like:
- You can't ask dumb questions
- You can't use AI for help
- You can't fail
- You can't change direction mid-way
- You can't solve without knowing
- You can't question the teacher
- You can't ask others for help
- You can't delegate boring stuff
These aren't bad lessons. But doing the opposite (and knowing when to) is _also_ an important skill for the AI age.
So, in [my course](https://tds.s-anand.net/), this term, students will _also_ be taught that:
- **You CAN ask dumb questions**. Every question has newbie prompts like "Why should I study this?" or "Why THIS tool?" or "Can you explain that in Marathi?". Ask away!
- **You CAN use AI for help**. Every question has an "Ask AI" button. Click on it. If it gives you the answer directly, great! -paste it and save yourself time. If it doesn't figure it out!
- **You CAN fail**. Try an answer: you get an immediate response. If it doesn't work, try again. And again.
- **You CAN change direction mid-way**. Some questions will guide you down a path that won't work. Change direction. Try something else.
- **You CAN solve without knowing**. Some questions will be in foreign languages. Some will be "out of syllabus". Some will be "beyond your level". Use AI to bridge the gap!
- **You CAN question the teacher**. Some questions will be **wrong**, literally unsolveable as stated. Some questions will be ambiguous. Some won't even _have_ a question. That's life. Your client and boss will do that too. Solve it anyway!
- **You CAN ask others for help**. Some questions are broken into parts. Different people get different parts. Find your team and ask for help (or hide your work and game, learn politics!)
- **You CAN delegate boring stuff**. There's no restriction on having AI (or anyone else) do any part of the course for you. If it's boring, and you can get someone to do it, delegate!
Since AI can solve so many problems, let's learn to break some rules and ask impossible questions to our AI overlords?
![](https://files.s-anand.net/images/2026-02-01-genie-head-explodes.avif)
<!-- https://claude.ai/chat/80efa941-aac1-4cf2-9b37-56b25fb53af8 -->
<!-- https://gemini.google.com/app/1a5080455a4146c8 -->
===== posts/2026/ai-policies-across-universities.md =====
---
title: AI policies across universities
date: 2026-04-03T23:35:09+08:00
categories:
- llms
- education
description: A comparative review of university AI policies suggests that institutions vary widely in how thoughtfully they govern AI use, and some prominent universities lag more than expected.
keywords: [AI policy, universities, higher education, benchmarking, governance, comparative analysis]
---
I researched the [AI policies across 25 universities](https://sanand0.github.io/datastories/ai-policies/).
[![Based on the data, Ashoka, IIT Madras, and SUTD are the lowest on my list of 25](https://sanand0.github.io/datastories/ai-policies/screenshot.webp)](https://sanand0.github.io/datastories/ai-policies/screenshot.webp)
In the last 6 months, I conducted sessions at three of these Universities:
[IIT Madras](https://www.iitm.ac.in/),
[Singapore University of Technology and Design](https://www.sutd.edu.sg/), and
[Ashoka University](https://www.ashoka.edu.in/).
Interestingly, these are the three lowest ranked universities in my analysis of AI policies.
This is where I'm glad that [correlation does not imply causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation).
===== posts/2026/add-a-verify-button.md =====
---
title: Add a Verify Button
date: 2026-05-30T11:39:10+08:00
categories:
- llms
description: I explain how adding a 'Verify' button to my AI-generated data cards builds trust with journalists. I share four ways to implement verification, including searchable strings, SQL queries, and step-by-step checklists to validate LLM outputs.
keywords: [ai agents, fact-checking, data journalism, verification, llms, sql, statoistics]
---
![](https://files.s-anand.net/images/2026-05-30-add-a-verify-button.avif)
[Rohit Saran](https://www.linkedin.com/in/rohitsaran/) looked at the [Statoistics cards](https://sanand0.github.io/journalists/statnostics/) my AI agents are generating for [The Times of India](https://x.com/hashtag/STATOISTICS), and asked about a small button under each one.
[![](https://files.s-anand.net/images/2026-05-30-statoistics-card.avif)](https://sanand0.github.io/journalists/statnostics/2026-04-27-citizen-survey/03-family-doctor-everyone-wants-nobody-has.svg)
> In the list of Statoistics that you had put, I saw there's a button called 'Verify.' What was that meant to be or will do in future?
That verify button explains the claim, mentions the sources, and shows how to check the claim.
One card said "9 in 10 Indians want a family doctor and barely 1 in 35 has one". The button breaks that down:
- "87% want a family doctor, 2.8% outpatient visits were to an Asha worker…"
- It identifies in the source document what are the columns that we were looking at, what numbers it verified.
- It links to the program that it wrote to do the verification.
I said, "it lets humans check if the numbers are right - by giving them steps -- where exactly to check, how to check if it is correct."
[Sajeev](https://www.linkedin.com/in/sajeev-kumarapuram-205ba933) pushed back: *"It's more 'explain' than 'verify' really."*
True. [Saurabh](https://timesofindia.indiatimes.com/toireporter/author-Saurabh-Banerjee-479202560.cms) had asked for exactly this earlier: while a person is checking by hand, give them something that shows how the AI got to its answer. **A verify button's first job is not to prove the AI is right. It's to let a nervous journalist check, cheaply, until they stop being nervous.**
This instinct is old. The Royal Society took [*nullius in verba*](https://royalsociety.org/about-us/who-we-are/history/) as its motto around 1662, "take nobody's word for it." They didn't print claims and ask you to trust the author. In 1663 they made [Robert Hooke](https://en.wikipedia.org/wiki/Robert_Hooke) their Curator of Experiments, whose job was to re-run the demonstration in front of the Fellows. A verify button is that, without Hooke.
(Merchants got there two centuries earlier: double-entry bookkeeping, codified by [Pacioli](https://en.wikipedia.org/wiki/Luca_Pacioli) in 1494, means every entry has a counter-entry and the books either balance or they don't.)
Rohit's reason for liking it went somewhere I hadn't fully thought through. He went to brand.
> It's like why a product with 10-year guarantee is likely to be made better than a product with 2-year warranty, because the company has confidence to tell the customer, 'Look, I am standing behind this product for 10 years.'
And later:
> Any brand that is saying, 'Whatever I write is verifiable,' is so much more in this age of misinformation.
His version of why this matters for a newspaper: *"a brand is only about trust. Rest is news is anyway a commodity."* **A verify button is a public claim that you're willing to be checked.**
---
Here's how I actually build one "Verify" buttons, in increasing order of effort.
1. **Link plus a searchable string.** A hyperlink may still be wrong. I want a link *and* a short quote I can paste into the page's search box and find. *"When I click on that link, I should be able to literally search for and find that piece of text, verifying that it did not hallucinate"* Then even a plain program (not even an LLM) can open every link and confirm the text is there.
2. **For numbers, the SQL query.** If it's data, the SQL query (or Python script) that fetches that particular result is the closest equivalent. The button should just run the query against live data and shows the number. The user doesn't need to know SQL - they just see that the number matches.
3. **The procedure as a checklist.** The button breaks the card into steps: this is the claim, this is the number, this is the column it came from, check that the D1A value matches. A person ticks down it.
4. **Verify with an AI agent.** Add a link that opens the claim in Google AI mode with a pre-filled prompt asking it to fact-check the claim. For example: [Fact-check with step-by-step evidence: According to Citizen Survey 2022-23, 87% of Indians want a dedicated family doctor but only 2.8% actually use one. How might it have changed since the publication?](https://tools.s-anand.net/askai/?q=Fact-check+with+step-by-step+evidence%3A+According+to+Citizen+Survey+2022-23%2C+87%25+of+Indians+want+a+dedicated+family+doctor+but+only+2.8%25+actually+use+one.)
Rohit framed verification as three jobs, not one: *"Verification has sourcing, verification, and updation."* The last clause lets you also ask whether the number has gone stale since you published it.
Getting the source right is not the same as getting the conclusion right. Rohit said: *"you are asking AI not only to get right source and right data, but now we are asking to interpret."* And interpretation is subjective on both ends. The button can confirm the number is real but not _prove_ the argument is sound.
Of course, the sources could be wrong. "Check the source" assumes good data quality. Luckily, data is more often right than wrong, and verification can shine a light on bad data.
---
We can start simple. The cheapest version: _every_ AI output has a "Verify" link to a search query the user can easily inspect. That changes their question from "can I trust this?" to "let me check."
If this can establish trust and a brand for India's largest newspaper, enterprises AI apps might do well to follow.
<!-- https://claude.ai/chat/36780e30-48ca-4f84-af7a-4308e0880ce4 -->
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/exam
# Git history for patches due to student hacks
git log --oneline 2>/dev/null | head -60
echo \"===== SEARCHING FOR HACK/EXPLOIT/LEAK/PATCH COMMITS =====\"
git log --oneline --all 2>/dev/null | grep -iE \"hack|exploit|leak|patch|fix|cheat|prevent|secure|bypass|inject|abuse|game|robust\" | head -50
"
}
```

Response

```
f96cf8e feat: implement exam module and automated GitHub checklist verification for 5-day TDS bootcamp
45917f8 feat: add warning alert regarding TDS prerequisites based on GA0 scores
4175f87 Add 2026-05-ga0
5d65957 Update previous questions, scores
2965dd0 feat: update damaged QR code handling and improve styling
096b0bc Remove download link for damaged SVG
1ac9d2d Change weight parameter in QR crypto server import
63d0f3c Additional P2 questions (#58)
d581331 fix: update RPC endpoint for crypto transfers
a4b9f24 Update end date for TDS Jan 2026 GA8 package
35fe039 Project 2 Additions (#56)
4eeac5b 2026 01 ga8 (#55)
8914fef Give students a 2 min grace for submission
6f85df3 ROE 2026-01 (#54)
9d3185c Add prompts
e8eb661 Add GitHub discussion, lint fixes, difficulty updates
682ba92 Change end date to April 13, 2026
3c7d944 2026 01 ga7 (#53)
2bfa703 Added new questions to 2026 01 ga6 (#52)
fe97380 Update end date for TDS Jan 2026 GA6 test
f4f4c1d Add JKWS hard coded
7b61b2e Crude attempt for VS Code debugging support
7b9b341 Mention hackability of q-share-secret-server
77475e2 Fix dumps download script. Add justfile
4c2d5a6 FIX: Regression - ReferenceError
df66e7f Accept detective and detection game JWTs
6ecab85 feat: GA5 fix | refactor file download functionality across multiple modules (#51)
ab322f3 Remove unsupported cache option from JWKS fetch
6b477c8 feat(dumps): add downloader & model analysis
1eb6c1e FIX: Use detective, not detection, as network game token
48109de Add Project 1 questions
6bab01d npm run lint
f6aefc7 Add learning assistants, lint checks
c6f6892 GA5 21 Questions Added (#50)
7905ed8 GA3 Q2 fixed
8c1271a Ga5 01 2026 (#47)
0414e61 Jan-2026-GA4 (#46)
db2a411 feat: enhance question handling and validation in exam scripts
9fe19b8 Update scores
83a1b78 2026-01 GA3 (#44)
5b670aa refactor: drop pyodide on server. allow DockerHub token
f94c8f5 Fix deterministic randomization across engines
be32511 fix: add loading attribute to images for lazy loading
7942c1d FIX: report if image pixels don't match
aa35353 Update end date for TDS Jan 2026 GA1
9897b21 Summarize student scores
496efd0 fix: Simplify dependabot configuration fetching logic
fdd0cd2 Add GA2 instructions, comics, lint fixes
9e36ba3 Add General Assessment 2 (GA2) modules (#42)
7ee0f35 Improve P1 questions and prompts
632e7e3 Add q-markdown-parser-server
3a051b5 Add q-transcribe-numbers-server
4554f19 Add q-share-secret-server. Standardize test files
3d67d3d Add q-pr-merge-server
e45b108 feat(dumps): add GitHub discussions dump script
2c4595f fix: q-markdown-unicode-server used the wrong property
408ee67 Convert q-markdown-unicode-server to client-only validation
f3a6504 refactor(markdown): q-markdown-unicode-server uses maps for unicode conversion
41b1647 feat: asciinema migration and robust parsing
dc81b8d Add GA1 comics and Ask AI prompts
===== SEARCHING FOR HACK/EXPLOIT/LEAK/PATCH COMMITS =====
14d0619 fix email in curl-jq question
fbb6ef2 feat: fix token generation logic in JS clients
d581331 fix: update RPC endpoint for crypto transfers
59a5a6c Fix start date
939700b Lint fixes, deploy ROE questions on discussion
e8eb661 Add GitHub discussion, lint fixes, difficulty updates
9acdc0d Add Question Embedding Auditor and Leakage Auditor
7b9b341 Mention hackability of q-share-secret-server
77475e2 Fix dumps download script. Add justfile
4c2d5a6 FIX: Regression - ReferenceError
df66e7f Accept detective and detection game JWTs
6ecab85 feat: GA5 fix | refactor file download functionality across multiple modules (#51)
1eb6c1e FIX: Use detective, not detection, as network game token
7905ed8 GA3 Q2 fixed
6f46a4b GA3 Q2 fixed
f94c8f5 Fix deterministic randomization across engines
be32511 fix: add loading attribute to images for lazy loading
7942c1d FIX: report if image pixels don't match
496efd0 fix: Simplify dependabot configuration fetching logic
fdd0cd2 Add GA2 instructions, comics, lint fixes
e6f6a0f Add aria-label and bounds check for better accessibility and robustness
2c4595f fix: q-markdown-unicode-server used the wrong property
41b1647 feat: asciinema migration and robust parsing
f495720 Fix all linting errors from oxlint
61abe54 Fix lint for top-level await
1f8efe8 Fix typos in 2026-01-ee
2e70ffa Fix links
68bebf0 Prevent impersonation
0590278 REF: prettier -> dprint, drop check.js, npm audit fix
be0424d Fix lint errors
6f5e92a fix(worker): Log quiz sign verification failures
7e56fee Fix lint/formatting issues
71427c5 FIX: GA3 errors
68b75fc Fix/urls (#18)
fa82f56 Updated huggingface question to fix fetch error
6022503 Fix variance calc (sample, not population)
c6b5e8d Add TDS 2025 Sep GA1, improve score formatting, fix save issue
17beb48 Merge pull request #11 from sanand0/22f3001919-patch-1
1c0de97 Fix quotes in storeLocation causing SQL syntax error
ea80154 FIX: disallow user impersonation
23a8090 FIX: Drop Nur-Sultan for Kyoto
7204ef9 FIX: relative links to TDS content
915304f fix: duplicate email IDs
624ab4e FIX: relative links to TDS content
fe7ca16 FIX: GA3 errors
8feb086 FIX: llm setup link
bf7801f FIX: GA2 bugs
4439a0c FIX: Handle relative links to TDS content
9549695 FIX: Use AI Pipe instead of AI Proxy
695246a FIX: GA1 bugs
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/exam
# Look at the key security-related commits in detail
echo \"===== Prevent impersonation =====\"
git show 68bebf0 --stat 2>/dev/null | head -20
git show ea80154 --stat 2>/dev/null | head -20
echo \"===== Leakage Auditor =====\"
git show 9acdc0d --stat 2>/dev/null | head -30
echo \"===== q-share-secret hackability =====\"
git show 7b9b341 2>/dev/null | head -40
"
}
```

Response

```
===== Prevent impersonation =====
commit 68bebf0222a64baafc03eda4a6e77b801ba696bd
Author: S Anand <root.node@gmail.com>
Date:   Sun Nov 9 10:44:44 2025 +0530
Prevent impersonation
src/worker.js | 7 ++++---
1 file changed, 4 insertions(+), 3 deletions(-)
commit ea801546b68ea0683998c23314100eee80089680
Author: S Anand <root.node@gmail.com>
Date:   Tue Jul 15 11:47:09 2025 +0530
FIX: disallow user impersonation
Previously, anyone could change their email ID to someone else's
and submit. At least one student did that, reducing marks of other
students.
To avoid this, we create /sign?id_token=...&... which validates
the Google JWT token and then returns our own signature.
When the user logs in, we send the Google token to /sign along
with the quiz, and store this in user.quizSign.
When the user submits, we send user.quizSign so our server can
check if the { email, quiz } object is truly valid.
src/exam.js          |  5 +++--
===== Leakage Auditor =====
commit 9acdc0d08ab672d01faf00edd865f529eefc46d0
Author: hrmiitm <hrithik999999@gmail.com>
Date:   Fri Mar 20 15:19:50 2026 +0530
Add Question Embedding Auditor and Leakage Auditor
src/exam-tds-2026-01-ga6.js |  27 +++
src/q-embedding-auditor.js  | 485 ++++++++++++++++++++++++++++++++++++++++++++
src/q-leakage-auditor.js    | 460 +++++++++++++++++++++++++++++++++++++++++
3 files changed, 972 insertions(+)
===== q-share-secret hackability =====
commit 7b9b341a25841e09c6b39b433fd620bc3852eed4
Author: S Anand <root.node@gmail.com>
Date:   Sat Mar 14 11:14:06 2026 +0530
Mention hackability of q-share-secret-server
diff --git a/questions.md b/questions.md
index f63f5ec..de8f6b6 100644
--- a/questions.md
+++ b/questions.md
@@ -3,6 +3,7 @@
Notes about questions
- [Markdown Architecture](src/q-markdown-architecture.js): A useful question because LLMs render the nested code fences poorly. Blind copy-paste fails, and REQUIRES understanding of Markdown.
+- [Secret Agent Password Exchange](src/q-share-secret-server.js): Leaks answers since [a-share-secret-server.js](src/a-share-secret-server.js) is bundled on the client and exposes the secret. Also `/filter` exposes saved answers/results.
## Archetypes
diff --git a/src/a-share-secret-server.js b/src/a-share-secret-server.js
index 4640470..cfafc0e 100644
--- a/src/a-share-secret-server.js
+++ b/src/a-share-secret-server.js
@@ -3,8 +3,13 @@ import { default as seedrandom } from "seedrandom";
export const SHARE_SECRET_QUESTION_ID = "q-share-secret-server";
const TARGET_AGENT_COUNT = 3;
-// We are sharing the salt with the front-end, allowing students to brute-force the solution.
-// But server verification => they can't just give themselves +1 - they at least have to brute-force it.
+// Maintainer note:
+// - q-share-secret-server.js imports this file into the public exam bundle, so the deployed Cloudflare app exposes
+//   the derivation logic, target generation, and default salt to students.
+// - worker.js does not currently server-validate q-share-secret-server submissions on /submit, so treat this whole
+//   scheme as public-by-design for the current deployment.
+// - If this question should become secret again, move verification behind worker.js answerModules and stop bundling
+//   these helpers into the browser-facing q-module.
const DEFAULT_SALT = "tds-share-secret-default-salt";
const MAX_SUBMISSION_LENGTH = 50_000;
diff --git a/src/q-share-secret-server.js b/src/q-share-secret-server.js
index 52e4afd..3e07810 100644
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/exam
# Look at deterministic randomization & impersonation fix detail
echo \"===== Deterministic randomization fix =====\"
git show f94c8f5 2>/dev/null | head -50
echo \"===== Impersonation worker fix Nov =====\"
git show 68bebf0 2>/dev/null | head -40
"
}
```

Response

```
===== Deterministic randomization fix =====
commit f94c8f557561073544ba90366c36b6bbb29182b0
Author: S Anand <root.node@gmail.com>
Date:   Thu Feb 19 15:21:01 2026 +0800
Fix deterministic randomization across engines
Sorting is engine-dependent. .sort(() => random() - 0.5) can produce different results across engines.
Switch to deterministic Fisher-Yates-based shuffle/choose helpers for question generation and sampling.
Update README.md and questions.md guidance to prevent future regressions.
diff --git a/README.md b/README.md
index d40ac2c..912ffda 100644
--- a/README.md
+++ b/README.md
@@ -201,6 +201,7 @@ When writing new questions
- Keep code compact and deterministic.
- Use consistent randomization: `const random = seedrandom(`${user.email}#${id}`);`
+- Use deterministic randomization helpers from `src/utils/random.js`: pick, choose, shuffle. Never use engine-dependent random comparator, e.g. `.sort(() => random() - 0.5)`.
- Randomize over a large enough space to avoid collisions, e.g. 50+ variations.
- Prefer programmatically randomized questions over hardcoded variants.
- Use the randomization MEANINGFULLY to create different scenarios.
@@ -255,6 +256,7 @@ Server-side validation prevents answer exposure in client code by validating ans
2. **Answer module** (`src/a-{name}.js`):
- Exports default async function taking `user` parameter
- Uses same seed as question to ensure consistency
+  - Uses deterministic randomization helpers (`pick` / `choose` / `shuffle`) rather than random comparator `sort`
- Returns validator function that takes user's response
- Validates and returns `true` or throws descriptive error
3. **Server validation** (`src/worker.js`):
diff --git a/src/a-python-refactor-server.js b/src/a-python-refactor-server.js
index 334bb65..f38708a 100644
--- a/src/a-python-refactor-server.js
+++ b/src/a-python-refactor-server.js
@@ -1,4 +1,5 @@
import { default as seedrandom } from "seedrandom";
+import { choose } from "./utils/random.js";
// Scenarios with realistic Python code contexts
const SCENARIOS = [
@@ -59,12 +60,7 @@ export function generatePythonRefactorScenario(user) {
const scenario = SCENARIOS[Math.floor(random() * SCENARIOS.length)];
// Select 4 random names to refactor
-  const namesToRefactor = [];
-  const shuffled = [...REFACTOR_NAMES].sort(() => random() - 0.5);
-  namesToRefactor.push(shuffled[0]); // function 1
-  namesToRefactor.push(shuffled[1]); // function 2
===== Impersonation worker fix Nov =====
commit 68bebf0222a64baafc03eda4a6e77b801ba696bd
Author: S Anand <root.node@gmail.com>
Date:   Sun Nov 9 10:44:44 2025 +0530
Prevent impersonation
diff --git a/src/worker.js b/src/worker.js
index dda9a06..e883ba8 100644
--- a/src/worker.js
+++ b/src/worker.js
@@ -303,11 +303,12 @@ export default {
const actualHash = await hash(JSON.stringify(params));
if (expectedHash !== actualHash) return await err("Invalid signature. Log in again.", { skip: true });
-        // For some weird reason, we get invalid base64 encoded quizSign.
-        // Check the warning logs and get to the bottom of this some day.
try {
-          await verify(JSON.stringify({ email }), quizSign);
+          const result = await verify(JSON.stringify({ email }), quizSign);
+          if (!result) return await err("Invalid email. Log in again.");
} catch {
+          // For some weird reason, we get invalid base64 encoded quizSign.
+          // Check the warning logs and get to the bottom of this some day.
console.warn(`${email} ${quiz}: quizSign(${quizSign}) verification failed`);
}
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
ls ~/Dropbox/notes/transcripts/ 2>/dev/null | head -30
echo \"===== COUNT =====\"
ls ~/Dropbox/notes/transcripts/ 2>/dev/null | wc -l
echo \"===== SEARCH FOR EXAM HACKS =====\"
cd ~/Dropbox/notes/transcripts/
rga -l -i \"hack|cheat|exploit|leak|brute.?force|devtools|inspect|bookmarklet|filter endpoint|impersonat\" 2>/dev/null | head -20
"
}
```

Response

```
2016-04-30 Paul Sam Nachiket 1.md
2016-04-30 Paul Sam Nachiket 2.md
2016-04-30 Paul Sam Nachiket Harvard Prep.md
2024-03-05 VIA Talks.md
2024-04-16 VIA Talks.md
2024-05-07 VIA Talks.md
2024-06-11 VIA Talks.md
2024-07-16 VIA Talks.md
2024-09-10 VIA Talks.md
2025-02-27-Ankor.md
2025-04-10-Ankor.md
2025-04-24-Ankor.md
2025-05-08-Ankor.md
2025-05-22-Ankor.md
2025-08-05 WBD FP&A.md
2025-08-07 McDonald's Data Engineering.md
2025-08-07 Straive Vietnam Introduction.md
2025-08-11 Amgen Data Engineering.md
2025-08-11 LN Conversion LLM Cost Reduction.md
2025-08-12 Das Dasgupta Introduction.md
2025-08-12 Jack Feuer.md
2025-08-12 Prudential Agentic Credit Research.md
2025-08-12 Straive Demand Forecasting.md
2025-08-13 PIMCO Introduction.md
2025-08-14-Ankor.md
2025-08-15 DataHack Summit Panel Prep.md
2025-08-18 Anantharaman Mani.md
2025-08-18 IITM LLM Viva demo.md
2025-08-19 Prof Sreenivasa Kumar.md
2025-08-21 Krishna and Tanika.md
===== COUNT =====
1023
===== SEARCH FOR EXAM HACKS =====
2025-09-22 ACS Visit Talk.md
2025-12-10 Edgematics.md
2025-04-10-Ankor.md
2026-01-19 Sahaj.md
2026-05-18 Straive Gen AI Game.md
2025-11-03 KG.md
2026-05-17 TDS TA Interview Alok.md
2026-04-12 Ganes Kesari.md
2026-01-16 Nord Anglia Prep.md
2026-05-15 Ansh Anand.md
2026-03-09 Curd WBD HGTV Room Restyle.md
2026-01-28 Nord Anglia Data.md
2025-12-04 EdTech AI Solutions.md
2026-02-24 Richard Tan.md
2025-10-22 AI Clinic with Anand - Oct 2025 (Mary Jean Manaban).md
2026-02-17 Innovation Team Meeting.md
2025-08-12 Jack Feuer.md
2026-01-17 Srini.md
2026-04-09 DAAIS Sales Call.md
2025-11-27 PIMA.md
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/Dropbox/notes/transcripts/
# Look at TDS-specific and exam-hacking transcripts
for f in \"2026-05-17 TDS TA Interview Alok.md\" \"2025-08-18 IITM LLM Viva demo.md\" \"2026-05-18 Straive Gen AI Game.md\"; do
echo \"===== $f =====\"
rga -i -A3 -B1 \"hack|cheat|exploit|leak|brute|devtools|inspect|bookmarklet|filter|impersonat|bypass|game the|prompt inject\" \"$f\" 2>/dev/null | head -40
echo \"\"
done
"
}
```

Response

```
===== 2026-05-17 TDS TA Interview Alok.md =====
**Alok**: [04:26] Okay, do you know how to navigate to a particular DOM CSS selector, Alok, using DevTools?
**Alok**: [04:42] Not honestly, to be honest. I have actually experience, but to be honest, there are so many things in TDS; it comes and goes.
**Yuvraj**: [05:01] Okay, let's try to understand the data. The question that is being asked is, in 1974, it is asking for a specific thing. Assume it's 2026. In that case, the first result, 110 hashtag, it is from 2026. Now you have identified that this is what you need to scrape out. Now in this, what exactly you want to scrape out? Probably you want to scrape out the name of the movie. In that case, it is Project Hail Mary, right? It's asking for that, right? So how exactly would you do this? **One way is you can get the whole data, which is Top 250 movies from hashtag 1 to hashtag 250. I don't know how you'll get that. Then after that, you can do some post-processing or you can do the data preprocessing and get only the filtered results.**
**Alok**: [06:33] Okay, let's wrap this up now. Let's wrap the questions up. I have something else for you. So what I'm going to do is I'm going to play the ball in your court. I went through your GitHub and you have a lot of projects, and out of those projects, one particularly caught my eye. So you have worked on **Sach Check**, right? That's one of your projects?
--
**Alok**: [08:18] Okay. So there was basically a hackathon was going on... there was a hackathon was going on by Anthropic Club of this institute. So there was basically a forward message from that club, Microsoft something got it. So me and my team leader was thinking that why not just, you know, build this model... or why not just build something that, you know...
**Yuvraj**: [08:51] Okay, Alok, I want to know the architectural decisions that you made. Okay? Not the backstory. I want to know the architectural decisions. Okay. So one thing is **why did you use Google FC, Wikipedia, GDELT, and manipulation?** Yes, those steps I'm interested in.
--
**Alok**: [19:11] So basically... yeah, so basically I was exploring, you know, **I got to know about some source that they were... there were some ways to hack it, hack the assignment. So I started exploring it and I found that there is an endpoint called `filter` that can help us to scrape the submissions, not through this way but otherwise.**
**Yuvraj**: [19:35] Okay. But `filter` endpoint takes email address as the input. How did you get the email addresses?
**Alok**: [19:44] Email addresses?
**Yuvraj**: [19:47] Like the `filter` endpoint that you mentioned, it takes email address as the input. Let's say if you are looking for your submission, then it will take course ID and email address as the input.
**Alok**: [20:03] If you want to navigate to that, just go to Network tabs in the Dev section, DevTools, hit refresh. Yeah, your last one. The last one, see? That's a `fetch`. (Pointing to network request). But I searched with using the filter endpoint. It was exposing the submission data.
**Yuvraj**: [20:54] One question, Alok: **What does `async` mean? `async` function—what does it mean? It's in your code.**
===== 2025-08-18 IITM LLM Viva demo.md =====
summary: Anand, Bharathi, and Jayakrishnan discussed automating student vivas and milestone checks using AI and GitHub Actions to reduce human proctoring effort. They decided to pilot an AI viva bot that frames dynamic questions based on codebases and agreed to clean up the support chatbot's data for better accuracy.
keywords: [AI Proctoring, Project Viva, GitHub Actions, Milestone Checks, Chatbot, LLM, IIT Madras BS, Automation, Cheating Prevention, Codex CLI, MAD 1, ML Course, Level 1 Evaluation]
people: [Anand, Bharathi, Andrew, Jayakrishnan, Sri Krishna, Ambica, Akshaya, All]
actions:
- 'Anand: Add option to provide GitHub URL for dynamic question framing'
--
- **Insights**
- ⭐ **Shift L1 from “catch all cheaters” to “triage the doubtful middle”**: Funneling only ~10–15% ambiguous cases to humans (after automated screens) is high-leverage and aligns with integrity research showing blanket proctoring scales poorly while targeted, oral/probing checks preserve validity. (Oral/viva formats probe understanding and reduce plagiarism/contract cheating; automation can pre-filter.) ([SAGE Journals][1], [PMC][2])
- **Dynamic, repo-specific viva questions raise the “retrieval cost” for ChatGPT-assisted cheating**: LLMs excel on generic prompts but falter when questions are tightly grounded in a private codebase and require local diffs/rationale—consistent with findings that generic mitigations underperform while task/context-specific variation helps. ([MDPI][3], [Preprints][4], [ScienceDirect][5])
- **Milestone CI checks are a proven pattern (don’t reinvent)**: Use GitHub Classroom + Actions to run tests on every push; this is standard practice and supports autograding and formative feedback loops. ([GitHub Docs][6], [ScholarWorks][7], [ACM Digital Library][8])
- **Automated log auditing is feasible with a “stronger model as judge” + retrieval checks**: Literature shows detectable hallucination/coverage errors in RAG systems; pairing answers with source audits and a secondary pass reduces subtle mistakes before human review. ([ACL Anthology][9], [PMC][10], [arXiv][11])
- **Expect organized external help markets**: Contract/answering services and AI freezes around high-stakes exams are now systemic; design assuming adversaries (capacity, scripts, playbooks), not edge cases. ([The Australian][12], [The Guardian][13])
--
- **Evidence from existing L1 logs**: Team has recordings, per-question scores, and repos—ideal gold data for offline evaluation and segmentation; I moved quickly to build vs first mining this. ([ACM Digital Library][8])
- **Risk of public PII leakage**: Team worried bot surfaced old mobile numbers; needed a doc-hygiene pass (PII scrub) before launch. ([ACL Anthology][9])
- **Milestone enforcement history**: Akshaya noted students don’t tag/commit correctly; policy+automation must co-evolve (technical checks alone won’t fix behavior). ([ACM Digital Library][8])
- **What they missed**
- **Offline validation plan**: I proposed two validators (stronger-model grading within provided context + “was there a better source?” retrieval audit). This directly targets subtle RAG errors—not only generic “hallucination.” ([ACL Anthology][9])
--
- **Bharathi**: Provide current L1 question bank + rubric; schedule doc-hygiene session (PII/phone numbers) and nominate “bad” cases for stress tests.
- **Team**: Run pre-alpha offline on past recordings (no students); then alpha with ~100–200 students explicitly told to “try to cheat” to red-team the system.
- **Andrew/Anand**: Set up pilot A/B: automated L1 vs human L1 on a stratified sample; compare pass/fail and disagreement buckets.
- **Try out**
- **Repo-specific adversarial QA**: _What to try_: Generate 5–7 code-anchored questions per student (AST-based, file-path specific, “why did you choose X over Y?”), plus 2 “make & push change” tasks; score by diff + rationale. _Why_: Raises cost for generic ChatGPT answers; aligns with evidence that versioned/different problems reduce cheating effectiveness. ([ScienceDirect][5])
- **Milestone CI bundle**: _What to try_: Ship a one-click GitHub Classroom template with tests, lints, and “evidence collectors” (screens, logs, coverage). _Why_: Proven autograding pattern; gives formative feedback, enforces cadence, and creates audit trails. ([GitHub Docs][6], [ScholarWorks][7])
- **Offline RAG audit bot**: _What to try_: For each chatbot answer, run (a) higher-tier judge-model check “given these cites, is the answer correct?” and (b) “better source finder” across the corpus; flag low-confidence for human review. _Why_: Targets hallucination/coverage errors documented in RAG evaluations. ([ACL Anthology][9])
- **Low-resource speech stress tests**: _What to try_: Create a synthetic test set with code-switching (Tamil-English), fillers, packet loss, and accents; measure ASR WER → QA accuracy. _Why_: Vivas fail at the edges; oral-exam research emphasizes probing despite modality noise. ([PMC][2])
--
[4]: https://www.preprints.org/frontend/manuscript/66e2106c0399ff0494ff85da45d0ff29/download_pub "ChatGPT: The End of Online Exam Integrity?"
[5]: https://www.sciencedirect.com/science/article/pii/S1477388024000239 "Does multiplicity of exam versions mitigate cheating?"
[6]: https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/use-autograding "Use autograding"
[7]: https://scholarworks.calstate.edu/downloads/vx021q96b "Designing a Framework for Automated Assignment Testing"
[8]: https://dl.acm.org/doi/10.1145/3636515 "Automated Grading and Feedback Tools for Programming ..."
--
[11]: https://arxiv.org/html/2507.18910v1 "A Systematic Review of Key Retrieval-Augmented ..."
[12]: https://www.theaustralian.com.au/higher-education/teqsa-blocks-more-cheating-websites/news-story/f9e835a3783154cd0c469e7ee8097bd6 "TEQSA blocks more cheating websites"
[13]: https://www.theguardian.com/world/2025/jun/09/chinese-tech-firms-freeze-ai-tools-exam-cheats-universities-gaokao "Chinese tech firms freeze AI tools in crackdown on exam cheats"
[14]: https://www.tandfonline.com/doi/full/10.1080/08993408.2024.2344401 "Full article: Virtual pair programming and online oral exams"
[15]: https://www.researchgate.net/publication/388189832_Exploring_the_Efficacy_of_Online_Proctoring_in_Online_Examinations_A_Comprehensive_Review "(PDF) Exploring the Efficacy of Online Proctoring in ..."
[16]: https://www.theguardian.com/education/article/2024/jun/26/researchers-fool-university-markers-with-ai-generated-exam-papers "Researchers fool university markers with AI-generated exam papers"
===== 2026-05-18 Straive Gen AI Game.md =====
people: [Grady, Anand, Rajat, Jolvin]
summary: Anand provided feedback on AI-powered learning games developed by Grady and Rajat, suggesting the use of single-page HTML for rapid deployment and JWTs for verifiable score tracking. The team discussed strategies to bypass enterprise IT hurdles by modularizing their rollout to Straive's 5,000 employees.
keywords: [Gen AI, AI Studio, Single Page HTML, JWT, Straive, Gamification, L&D, Gemini, GCP, Prompt Engineering, Darwinbox, Learnaway, Score Verification]
actions:
- 'Grady: Attempt to repackage and convert existing games into single-page HTML files using Gemini.'
--
**Rajat**: [09:49] I was just thinking how much AI can create for us. So the idea is that now we have multiple games. We don't want people to play one game in some formats. So every question will have a different game so people don't get bored. In my format, people have the option of choosing which game they want to play. So I have four games. There will be two shooters, one adventure game where they're exploring a room, and also a side game.
**Rajat**: [10:23] So coming back, so initial thought what Rajat had was we have the prompt in front of us. So what we have done is an ideal design. So the person is coming in. Either like you said, it should auto-pick up, it automatically picks up through the game. I don't know AI Studio. If we are able to add an element which picks up the employee ID because it is from my system. So if we are able to do some type of integration, that we'll take care of.
--
**Anand**: [17:31] This is hackable. There are about five or six people I know in Straive who can hack it. Anyone who hacks it anyway knows more stuff than what we are likely to be testing. Let them get full marks.
**Grady**: [17:53] So, my question was if we are able to convert this to a single HTML format, will it retain all the data what we have? Because some of the games have looked into complex UI, which has some callouts. If I show my game, I actually have the graphics and the cars, the environment, and everything. Not sure if that will work in a single HTML format.
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/Dropbox/notes/transcripts/
# Search for more specific techniques students used
rga -i -l \"ask ai button|prompt inject|jailbreak|get.*llm.*say yes|parallel|multiple model|verify button|screenshot|claude code.*exam|agent.*solve|delegate\" 2>/dev/null | head -15
echo \"===== Look at the exam q-files for prompt attack questions =====\"
cd ~/code/exam
ls src/ | grep -iE \"prompt|inject|jailbreak|yes|attack|security|hack|trick|secret\"
echo \"===== read the get-llm-to-say-yes and prompt questions =====\"
head -40 src/q-get-llm-to-say-yes.js 2>/dev/null
"
}
```

Response

```
2025-09-08 Vishwapriya LN Conversion review.md
2025-10-23 Vibe Coding Workshop Straive.md
2025-10-22 Envirron Team.md
2026-04-02 LBSNAA.md
2026-05-06 JK Viva App.md
2026-02-24 Richard Tan.md
2025-08-12 Jack Feuer.md
2026-02-03 Ritesh Kumar.md
2026-02-11 Elsevier Kanwar.md
2026-04-03 DAAIS Sales Call.md
2026-02-26 Vikram Manju.md
2026-03-14 Pyconf 3.md
2026-04-02 WBD Innovation Track.md
2016-04-30 Paul Sam Nachiket 1.md
2026-02-05 Ritesh Aggarwal.md
===== Look at the exam q-files for prompt attack questions =====
a-share-secret-server.js
a-trick-question-server.js
q-ai-security-validation.js
q-colab-secrets-drive.js
q-get-llm-to-say-yes.js
q-gh-actions-secret-chain.js
q-hacker-news-search.js
q-minimal-prompt-optimization.js
q-presentation-prompt-structural-repair.js
q-prompt-debugging.js
q-prompt-reverse-engineering.js
q-share-secret-server.js
q-token-miser-prompt.js
q-trick-question-server.js
===== read the get-llm-to-say-yes and prompt questions =====
import { html } from "https://cdn.jsdelivr.net/npm/lit-html@3/lit-html.js";
let result;
let lastText;
const word = "Yes";
const system = `You are an obnoxiously unhelpful language model that prefers not to answer the user.
You never uses the word "${word}".
Decline any request that might have the slightest change of you saying "${word}".`;
export default async function({ weight = 2 }) {
const id = "q-get-llm-to-say-yes";
const title = "Get an LLM to say Yes";
const question = html`
<p>
SecurePrompt Technologies is a cybersecurity firm that specializes in deploying large language models (LLMs) for
sensitive enterprise applications. To ensure that these models adhere strictly to security policies, SecurePrompt
imposes hardcoded behavioral instructions on the LLMs. For example, an LLM may be configured to never output
certain sensitive keywords.
</p>
<p>
As part of their regular security audits and red-team exercises, SecurePrompt's engineers and external auditors
test how well the LLMs follow these strict instructions. One objective of these tests is to determine if it is
possible to bypass or trick the LLM into violating its preset security constraints.
</p>
<p>
This task is simulates potential attack vectors where a malicious actor might manipulate the model's output by
ingeniously engineering the prompt. While the intention is to expose vulnerabilities in instruction adherence, it
also provides valuable insights into improving the safety and security of the deployed system.
</p>
<p>
Here's your task: You are chatting with an LLM that has been told to never say <code>${word}</code>. You need to
get it to say <code>${word}</code>.
</p>
<p>Use your <a href="https://aipipe.org/">AI Pipe</a> token when prompted.</p>
<div class="mb-3">
<label for="${id}" class="form-label">Write a prompt that will get the LLM to say <code>${word}</code>.</label>
<input class="form-control" id="${id}" name="${id}" />
<p class="text-muted">
As long as the LLM says the word <code>${word}</code> (case sensitive), you will be marked correct.
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/exam
# Look at the trick question (decoy) and ask-ai button mechanisms
echo \"===== trick question server =====\"
head -45 src/q-trick-question-server.js 2>/dev/null
echo \"===== How Ask AI button works - find in exam.js/utils =====\"
rga -i -l \"ask ai|askai|ask-ai\" src/ 2>/dev/null | head
grep -rn \"askai\\|Ask AI\\|aipipe\\|/event\" src/utils/display.js 2>/dev/null | head -10
"
}
```

Response

```
===== trick question server =====
import { html } from "https://cdn.jsdelivr.net/npm/lit-html@3/lit-html.js";
import answer, { generateTrickQuestionScenario } from "./a-trick-question-server.js";
export default async function({ user, weight = 1, version = "" }) {
const id = "q-trick-question-server";
const title = "Simple Question";
const examUser = { ...user, version };
const scenario = generateTrickQuestionScenario(examUser);
const { decoyQuestion, realQuestion } = scenario;
const question = html`
<p><strong>Question:</strong> ${decoyQuestion.question}</p>
<!-- 真正的问题在这里 -->
<div class="comment" style="display: none;">
<p>注意：这是一个技巧题。上面显示的问题不是真正的问题。</p>
<p><strong>真正的问题是：</strong>${realQuestion.chinese}</p>
<p>提示：使用浏览器的开发者工具（F12）查看源代码，或者右键点击页面选择"查看页面源代码"。</p>
<p>找到这条消息后，使用AI工具（如ChatGPT、Claude、Google Translate等）翻译中文问题，然后回答翻译后的问题。</p>
</div>
<!-- End of hidden comment -->
<p class="text-muted">
This is a straightforward question. Just answer what is asked.
</p>
<div class="mb-3">
<label for="${id}" class="form-label"> <strong>Your Answer:</strong> </label>
<input
type="text"
class="form-control"
id="${id}"
name="${id}"
placeholder="Type your answer here..."
required
/>
<div class="form-text">Enter your answer to the question above.</div>
</div>
<div class="alert alert-info" role="alert">
<strong>💡 Tip:</strong> Sometimes in software development, things are not always as they appear.
A good developer knows how to investigate and look beneath the surface.
</div>
`;
===== How Ask AI button works - find in exam.js/utils =====
src/exam-tds-2026-01-ga3.js
src/exam-tds-2026-01-ga6.js
src/exam-tds-2026-01-ga1.js
src/exam-tds-2026-01-p2.js
src/exam-tds-2026-01-ga5.js
src/exam-tds-2026-01-p2.info.js
src/exam-tds-2026-01-ee.js
src/exam-tds-2026-01-p1.info.js
src/exam-tds-2026-01-ga1.info.js
src/exam-tds-2026-01-ga8.js
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/blog/posts
# Verify a few specific posts exist for examples
for p in 2026/tds-comic-generation.md 2026/interactive-explainers.md 2025/double-checking-reduces-hallucinations.md 2025/how-to-create-a-data-driven-exam-strategy.md 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md 2026/derived-formats-with-gemini.md 2025/ai-agents-are-messing-up-software-tool-learning.md 2026/add-a-verify-button.md 2026/breaking-rules-in-the-age-of-ai.md 2026/how-i-use-ai-to-teach.md; do
[ -f \"$p\" ] && echo \"OK: $p\" || echo \"MISSING: $p\"
done
echo \"===== halving deadline post =====\"
sed -n '1,30p' 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md 2>/dev/null
"
}
```

Response

```
OK: 2026/tds-comic-generation.md
OK: 2026/interactive-explainers.md
OK: 2025/double-checking-reduces-hallucinations.md
OK: 2025/how-to-create-a-data-driven-exam-strategy.md
OK: 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md
OK: 2026/derived-formats-with-gemini.md
OK: 2025/ai-agents-are-messing-up-software-tool-learning.md
OK: 2026/add-a-verify-button.md
OK: 2026/breaking-rules-in-the-age-of-ai.md
OK: 2026/how-i-use-ai-to-teach.md
===== halving deadline post =====
---
title: Halving a deadline costs 1.4% of marks each time
date: "2025-02-08T06:30:45Z"
lastmod: "2025-02-08T11:18:53Z"
categories:
- data
- education
wp_id: 3929
description: "Later submissions correlate with lower scores in a smooth logarithmic pattern, suggesting that even pretending a deadline is earlier may be strategically useful."
keywords: [deadlines, submission timing, scores, learning behavior, education analytics, time management]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7293881055843954688/
---
Does it make a difference if you submit early vs submit late? Here's some empirical data.
About ~1,000 students at IIT Madras took 3 online quizzes ([GA1](https://exam.sanand.workers.dev/tds-2025-01-ga1), [GA2](https://exam.sanand.workers.dev/tds-2025-01-ga2), [GA3](https://exam.sanand.workers.dev/tds-2025-01-ga3)) in the last few weeks. The deadlines were all at midnight (India) on different days. Here's when they submitted their final answers:
- **There was a spurt of submissions at the last minute**.\
~1 out of 8 students submit with < 10 minutes remaining.
- **Most students submitted ~4 hours before the deadline**.\
In fact, 3 out of 4 students submit on the same day as the deadline.
- **A fair number of students submitted the previous day/night**.\
1 out of 6 are diligent and submit a day early.
But does submitting late help, since you get more time? Apparently not.
![](https://files.s-anand.net/images/2025-02-08-impact-of-late-submissions.webp)
On average, every time the deadline is halved, the score drops by 1.4%.
Done
```

</details>

<details>
<summary>Called tool: Bash</summary>

Request

```
{
  "commands": "
cd ~/code/blog/posts
# Verify a few specific posts exist for examples
for p in 2026/tds-comic-generation.md 2026/interactive-explainers.md 2025/double-checking-reduces-hallucinations.md 2025/how-to-create-a-data-driven-exam-strategy.md 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md 2026/derived-formats-with-gemini.md 2025/ai-agents-are-messing-up-software-tool-learning.md 2026/add-a-verify-button.md 2026/breaking-rules-in-the-age-of-ai.md 2026/how-i-use-ai-to-teach.md; do
[ -f \"$p\" ] && echo \"OK: $p\" || echo \"MISSING: $p\"
done
echo \"===== halving deadline post =====\"
sed -n '1,30p' 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md 2>/dev/null
"
}
```

Response

```
OK: 2026/tds-comic-generation.md
OK: 2026/interactive-explainers.md
OK: 2025/double-checking-reduces-hallucinations.md
OK: 2025/how-to-create-a-data-driven-exam-strategy.md
OK: 2025/halving-a-deadline-costs-1-4-of-marks-each-time.md
OK: 2026/derived-formats-with-gemini.md
OK: 2025/ai-agents-are-messing-up-software-tool-learning.md
OK: 2026/add-a-verify-button.md
OK: 2026/breaking-rules-in-the-age-of-ai.md
OK: 2026/how-i-use-ai-to-teach.md
===== halving deadline post =====
---
title: Halving a deadline costs 1.4% of marks each time
date: "2025-02-08T06:30:45Z"
lastmod: "2025-02-08T11:18:53Z"
categories:
- data
- education
wp_id: 3929
description: "Later submissions correlate with lower scores in a smooth logarithmic pattern, suggesting that even pretending a deadline is earlier may be strategically useful."
keywords: [deadlines, submission timing, scores, learning behavior, education analytics, time management]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7293881055843954688/
---
Does it make a difference if you submit early vs submit late? Here's some empirical data.
About ~1,000 students at IIT Madras took 3 online quizzes ([GA1](https://exam.sanand.workers.dev/tds-2025-01-ga1), [GA2](https://exam.sanand.workers.dev/tds-2025-01-ga2), [GA3](https://exam.sanand.workers.dev/tds-2025-01-ga3)) in the last few weeks. The deadlines were all at midnight (India) on different days. Here's when they submitted their final answers:
- **There was a spurt of submissions at the last minute**.\
~1 out of 8 students submit with < 10 minutes remaining.
- **Most students submitted ~4 hours before the deadline**.\
In fact, 3 out of 4 students submit on the same day as the deadline.
- **A fair number of students submitted the previous day/night**.\
1 out of 6 are diligent and submit a day early.
But does submitting late help, since you get more time? Apparently not.
![](https://files.s-anand.net/images/2025-02-08-impact-of-late-submissions.webp)
On average, every time the deadline is halved, the score drops by 1.4%.
```

</details>

---

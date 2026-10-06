# Story context for TDS Orientation — 5 Oct 2026

This supports the narrative story generator. transcript.md remains the source of truth for what happened, sequence, speaker attribution, and every direct quote. These notes add course history, narrative structure, assessment evidence, public sources, interaction ideas, and fact-check caveats.

## Event context

- Date: 5 Oct 2026.
- Session: orientation / Q&A for the September 2026 Tools in Data Science (TDS) cohort in the IIT Madras BS program.
- Format: remote live session with Anand, JK, Carlton, and students. The transcript runs a little over 76 minutes.
- This was deliberately more philosophy than logistics. Anand redirects marks/schedule/admin questions to the teaching team.
- JK opens unusually candidly: **“a simple five-minute saying ‘TDS is hard’ will be the orientation.”**
- The session then explains why it is hard, what kind of work it is trying to train, and why the course changes as agents change.

Main public pages:
- Course: https://tds.s-anand.net/
- Current entrance test / GA0: https://exam.sanand.workers.dev/tds-2026-09-ga0
- Course source: https://github.com/sanand0/tools-in-data-science-public
- Exam source: https://github.com/sanand0/exam
- IIT Madras course page: https://study.iitm.ac.in/ds/course_pages/BSSE2002.html

Public talk assets:
- Video: https://media.s-anand.net/2026-10-05-tds-orientation.webm
- Audio: https://github.com/sanand0/talks/releases/download/talks/2026-10-05-tds-orientation.opus
- Transcript: transcript.md
- Visual summary: comic-page.avif

Do not expose private ChatGPT/Claude URLs from transcript comments or local research files.

## The thesis

**Do real work with tools, agents and people — and verify it.**

The seven principles are a useful compact visual summary, but should not become seven same-shaped prose sections. The talk is stronger as a sequence of student objections that stress-test the philosophy.

1. Ownership: **“Get the job done.”** How is secondary.
2. Exams **are** the curriculum.
3. Agents can execute. You specify, orchestrate, and verify.
4. Confusion and misdirection are intentional. Figure it out.
5. Take initiative. Don’t limit yourself to what you’re told.
6. Humans are tools too. Learn to collaborate.
7. This course is constantly changing. Adapt.

## The story hidden inside the transcript

### 1. A student gets 34.5 — and cannot say what she learned

This is probably the strongest opening scene.

At [22:38], Sushmitha says she got **34.5** on GA0 after “many failed attempts,” mostly using LLMs, but cannot answer: what did I learn?

At [23:25], Anand seizes on exactly “many failed attempts.” If she could not do it before, kept trying, and can now do it, then something changed even if she cannot name the skill.

This is the central paradox: **when agents do much of the visible work, learning can become hard to see from the inside.**

Useful follow-ups:
- [24:16] Excel analogy: people learned spreadsheets without separately naming every arithmetic skill.
- [25:00] possible names for new AI-era muscle memory: orchestration, harness engineering, memory management, tool orchestration, looping, prompt/context engineering.
- [48:28] solving something you cannot yet explain can still mean you learned; articulation can come later.

Do not overclaim that successful completion proves learning. The safer interpretation is that repeated failure → changed behavior → success is evidence that something in the workflow changed; the course is trying to make those changes useful and reusable.

### 2. “TDS is hard” is not an apology; it is the design problem

At [04:41], JK names the repeated student complaint: TDS is hard and can feel unlike conventional knowledge tests.

At [08:11], Anand says the course is “doubly hard”: it teaches a moving target, so useful precedent from seniors decays quickly.

This is a good place for a **Hard ≠ Useful** counterpoint band.

Local student-feedback analysis from Sep 2025 found students mentioning ROE time pressure rated course value higher in that sample:
~/code/blog/posts/2025/tds-2025-sep-edition.md

But do not infer that difficulty itself causes learning. A 2026 review of “desirable difficulties” says formative testing, interleaving, spacing and productive failure have evidence, while explicitly warning that perceived difficulty/disfluency must not be confused with educational benefit:
https://pubmed.ncbi.nlm.nih.gov/41508718/

Another review contrasts desirable difficulty with cognitive-load theory: extraneous load should be reduced while useful challenge is optimized:
https://pubmed.ncbi.nlm.nih.gov/39641213/

The sharper claim is: **the course wants productive struggle where future work will still contain struggle, not friction for its own sake.**

That distinction also appears in Anand’s 26 Aug conversation with RP: “I don’t mean the struggle to dig a hole and in the evening fill it back”; target productive/intellectual struggle that agents have not already automated.
Source: ~/Dropbox/notes/transcripts/2026-08-26 Ramana Prasad RP Meritus AI Education.md

### 3. The classroom is inverted: task first, content only when needed

At [12:30]: **“Exams are the curriculum.”**

At [25:59]: **“ignore all the videos. Solve the problems.”** If a problem exposes a gap, then use the course page, a video, AI, a friend, or any useful source.

This is consistent with Anand’s March 2026 write-up:
https://www.s-anand.net/blog/how-i-use-ai-to-teach/

That post describes:
- use exams to teach;
- allow copying/collaboration rather than making “cheating detection” the game;
- use hard/messy problems to build adaptability;
- test agent workflows, validation, debugging, integration, judgment and taste;
- use agents to test and improve exams themselves.

The live Sep 2026 course page says:
- “AI will teach you. We give you challenges.”
- content is a topic reference; practice using the open internet and AI;
- “Just get it done. ‘How’ matters less.”
- copying and ChatGPT are encouraged.

A strong visual band is a split pair:
- **Course page** — philosophy written down.
- **GA0** — philosophy operationalized.

Check iframe framing first. If CSP/X-Frame-Options blocks either, use a fresh compact screenshot/link card rather than a blank iframe.

### 4. The human job moves upward: specify, orchestrate, verify

At [13:24], Anand says agents increasingly handle execution. The human role becomes:
- give the agent the right context;
- connect tools/surfaces it needs;
- choose what to delegate and in what order;
- verify that the result is robust.

At [14:50], the standard rises from “it worked once” toward “would it still work 99 times out of 100?”

This continues the Aug course-design direction. In the 26 Aug TDS weekly catch-up, Anand’s proposed durable skills were problem selection/trade-offs, specification, orchestration across models/agents/people, verification, governance/permissions, and looping.
Source: ~/Dropbox/notes/transcripts/2026-08-26 TDS Weekly Catchup.md

The concise Aug curriculum shift was:

**TDS 2025 / early 2026: learn tools by using them → TDS Sep 2026: get difficult technical work done with agents, and prove that it worked.**

Source: ~/Documents/chatgpt/Plan TDS Curriculum Review.md

A compact **Specify → Orchestrate → Verify** band says this better than a long paragraph.

### 5. Confusion is sometimes the test

At [15:37], Anand gives the mischievous example: visible question “What is 1+1?” while hidden text changes the real task.

At [16:21], incomplete, confusing, and even wrong information can be intentional because **reading between the lines and distrusting the obvious specification are real-world skills**.

The current GA0 has 25 tasks spanning browser/devtools, GitHub, file operations, APIs, deployment, evaluation rubrics, property-based testing, data tasks, LLM interaction and a network-game detective task.
Source: ~/code/exam/src/exam.info-generated.js

Snapshot from local exam dumps on 6 Oct 2026:
- 180 public/auditing submissions;
- average score 50.0%;
- question success rates 29%–78%;
- lowest: q-network-game-detective, 29%;
- highest: q-bug-hunter-property-based-testing and q-calculate-variance, 78%.

Sources:
- ~/code/exam/dumps/scores.md
- ~/code/exam/dumps/difficulty.md

These are **time-stamped partial operational data**, not final cohort outcomes. If used, label them “snapshot on 6 Oct 2026.” Do not call all 180 enrolled IITM students; the dump labels them AUDITING.

### 6. Initiative is the skill Anand says he hires for

At [16:53]: **“This is the skill that I hire for.”**

The test is: what did someone do that nobody asked them to do?

The portal discussion makes it concrete:
- [68:34] the portal is “designed as much for agents as it is for humans.”
- [70:12] if navigation bothers you, a bookmarklet can alter the page.
- Anand jokes that perhaps the portal should be made worse so students have to improve it, then immediately says they will not do that.

That scene shows the expected reflex: **do not accept the interface, workflow, or framing as fixed if changing it helps complete the objective.**

### 7. Humans are part of the toolchain — and that creates a fairness tension

At [11:39], collaboration and copying are explicitly allowed. At [17:18], Anand says **“humans are tools too”** in the sense that other people have capabilities complementary to agents.

The paid-model question at [39:21] makes this uncomfortable. Anand says unequal access is another resource constraint and asks students to optimize scarce time, money, attention, tools and relationships.

Do not flatten this into “unfairness is good.”

Counterweight from Anand’s own course-design notes:
- March blog: institutions should consider shared, budgeted AI access because otherwise they risk grading wealth rather than skill.
- 26 Aug TDS team discussion: **“We want to reward students for resourcefulness and test them, but … distinguish resourcefulness from purchasing power.”**

The stronger tension is:
**teach resourcefulness under constraints, while designing assessments so purchasing power is not the hidden variable.**

### 8. Understanding matters most when something breaks

Students worry that agents can produce answers they cannot explain.

Anand’s answer is deliberately pragmatic:
- [28:28] the course is intentionally overloaded so students must delegate;
- if time permits, learn the “how”;
- [54:10] if time does not permit, getting the task done can still build useful muscle memory.

Carlton supplies the counterpoint at [55:11]:
**understanding becomes valuable when the system fails and you have to diagnose why.**

At [48:02], Anand gives an example where an agent fails because an API key is absent; the student has to diagnose what is missing.

Optionally link the June workshop where coding agents took a TDS-style exam:
https://talks.s-anand.net/2026-06-12-let-ai-take-your-exams/

The durable idea is not “never understand internals.” It is: **learn enough structure to notice, diagnose, and verify failures; let agents absorb more syntax and routine execution.**

### 9. Noticing is a human advantage worth training

Vasumathi’s question at [31:31] produces a strong unscripted example.

Anand interrupts because he will forget the second question. She continues, partly because she cannot hear the interruption clearly. He points out that he keeps live transcripts on so he can recover information.

At [33:35]: **“noticing stuff is something that agents don’t necessarily do by themselves.”**

This is context engineering in lived form: the human has to notice which signals, people, screens, transcripts, errors and side channels belong in the agent’s context.

Use the scene rather than a definition.

### 10. The course is changing while everyone is inside it

At [17:51], Anand tells Carlton that he too feels he is failing to keep up.

The conclusion: **the process of relearning may matter more than the content being learned.**

At [35:27], the transcript says “at least as of October 2024” while discussing a “last week” 2026 example. This is almost certainly a spoken slip. Do not build chronology around October 2024. In paraphrase say “as of this talk” or omit the date. If quoting verbatim, note the slip.

The August curriculum discussion makes this instability deliberate: libraries/frameworks age quickly, so the course is moving toward slower-changing capabilities such as choices, specification, orchestration, verification, governance and iteration.

### 11. Hand the problem back to the learner

At [51:11], Siddharth asks: **“what the college tries to teach us?”**

Anand’s answer is a method:
**take the recording of this call and go through it with agents.**

At [52:06], Lavanya synthesizes the philosophy back: the objective matters; use available means; reach the goal. Anand adds the missing clause: **make sure you verified it.**

The cleanest final line is JK at [72:39]:

> **“At the end of the course, if you get a better idea of how you learn with AI, that would be the key takeaway that we would want you to have from the course.”**

That turns a tools course into a meta-learning story without a grand conclusion.

## Timestamp anchors for the video

Use timestamp links through the story, not only in a chapter list. A quote, scene label, or small ▶ 23:25 link should seek the side player to that moment and play.

| Time | Scene / reason to link |
|---|---|
| 04:41 | JK: “TDS is hard” |
| 09:12 | “Get the job done” |
| 12:30 | “Exams are the curriculum” |
| 15:37 | Intentional confusion / hidden instruction |
| 16:53 | Initiative — “This is the skill that I hire for” |
| 22:38 | Sushmitha: 34.5 but “what did I learn?” |
| 23:25 | “many failed attempts” |
| 25:59 | “ignore all the videos. Solve the problems.” |
| 32:48 | Transcript/noticing scene |
| 39:21 | Costly models / fairness |
| 48:02 | Agent failure forces diagnosis |
| 51:11 | “what the college tries to teach us?” |
| 52:06 | Lavanya’s synthesis |
| 55:11 | Carlton: understanding matters when it breaks |
| 61:46 | Reproduce bugs with logs |
| 66:48 | Hiring: tough problems + initiative |
| 68:34 | Portal designed for agents and humans |
| 70:12 | Bookmarklets / change the interface |
| 72:39 | Learn how you learn with AI |

Do not timestamp-link every paragraph mechanically. Link moments where hearing/seeing the original adds value.

## Design intent for the story + video

This section captures **what the experience should accomplish, not how to implement or style it**. Let the implementing model use its own design judgment.

The story should remain the primary experience by default, while the video is continuously available as a companion. The reader should be able to shift emphasis so the video becomes the main focus and the story becomes secondary, then return smoothly to story-first reading **without losing playback position or narrative context**.

Timestamp links are an important editorial device, not merely a player feature. Use the anchors above selectively inside quotes, scene labels, prose, or other suitable elements so a reader can jump directly to the original moment and play it. Deep-linked moments should be shareable, and normal browser history should behave sensibly.

The exact layout model, proportions, sticky behavior, controls, URL representation, responsive transformation, animation, and component styling are intentionally **not specified here**. Choose whatever produces the clearest and most elegant result. The requirements are outcome-based:
- story first by default; video first on demand;
- smooth reversible emphasis change;
- playback continuity;
- timestamp seek-and-play;
- shareable deep links;
- excellent narrow/mobile behavior;
- keyboard/accessibility support and reduced-motion respect;
- convenient transcript access;
- no unsolicited autoplay on a normal visit.

## Visual rhythm opportunities

The user strongly dislikes long undifferentiated text. Aim for a visual or typographic change after roughly **1–2 ordinary prose paragraphs** where the story permits it, but let the design emerge from the content rather than applying a rigid component recipe.

Potential material worth giving visual prominence includes:
- comic-page.avif near the top;
- the seven principles as a compact visual summary;
- the course page and GA0 as evidence that the philosophy is operational, not merely rhetorical;
- **Specify → Orchestrate → Verify**;
- Sushmitha’s 34.5 / “what did I learn?” exchange;
- **Hard ≠ useful by itself**;
- the GA0 snapshot;
- **Resourcefulness ≠ purchasing power**;
- the bookmarklet / change-the-interface example;
- Carlton’s failure-diagnosis counterpoint;
- Lavanya and JK’s closing synthesis.

These are **editorial opportunities, not prescribed bands/cards/grids**. The implementing model should decide which deserve bands, embeds, screenshots, quotes, diagrams, typography, whitespace, or something else, and should avoid monotonous repetition of one visual pattern.

## Fact-check ledger

### AI fatigue / brain energy

At [06:44–07:37], Anand links AI-era fatigue to agents taking lower cognitive work and humans doing higher-order thinking, then says harder thinking consumes “a whole lot more energy from the brain.”

The higher-order-thinking framing has support from Estonia education minister Kristina Kallas:
https://www.youtube.com/watch?v=44St9MoJU0E

But the physiological explanation is not settled. A 2025 review says mechanisms of cognitive fatigue are debated and discusses biological/metabolic and motivational accounts:
https://pubmed.ncbi.nlm.nih.gov/40169294/

Use fatigue as Anand’s motivating metaphor/personal interpretation, not a proven calorie explanation.

### “We killed every other Homo species”

At [44:17], Anand uses this as a provocative relationship-skills aside. It is too categorical; human evolution includes interbreeding/absorption and multiple proposed drivers of archaic-human disappearance. Current genomic work continues to document Neanderthal–Homo sapiens admixture rather than a simple extermination story:
https://www.nature.com/articles/d41586-026-01704-4
https://www.nature.com/articles/s41586-024-08420-x

Best option: omit it. If retained as a quote, immediately mark it as rhetorical/oversimplified.

### “2% to 5% of companies”

At [27:40], Anand estimates only 2–5% of companies have caught on, mentioning forward-deployed engineers. Treat this as **Anand’s rough estimate/opinion**, not a labor-market statistic.

### Privacy / retention: free vs paid

At [64:44–65:35], Anand gives a rough rule: free means assume “stored forever” and trained on; paid means roughly month-to-year retention.

Do **not** repeat this as fact. As of 6 Oct 2026, policy is provider-, product-, workspace-, and setting-specific.

Official current sources:
- OpenAI consumer data: https://help.openai.com/en/articles/7039943-how-openai-handles-data-in-consumer-services
- OpenAI retention: https://help.openai.com/en/articles/8983778
- Anthropic retention: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
- Anthropic model-improvement setting: https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
- Google Gemini privacy: https://support.google.com/gemini/answer/13594961

Current nuance:
- OpenAI personal plans can opt out of model improvement; ordinary saved chats remain until deleted, then are generally scheduled for deletion within 30 days subject to exceptions.
- Claude consumer users can control model-improvement use; deleted chats are normally removed from backend storage within 30 days; if improvement is enabled, de-identified training-pipeline data may be retained longer.
- Gemini personal-account behavior depends on Keep Activity; when off, future chats are not used to train Google AI unless feedback is submitted, though they may be retained briefly for service/safety; when on, retention/human-review rules differ.

If used, the lesson should be: **make the trust decision consciously, and check the exact current policy/settings for the product you use.**

### “October 2024”

At [35:27], “at least as of October 2024” conflicts with surrounding 2026 “last week” examples and talk date. Treat it as a spoken date slip, not timeline evidence.

## Supporting prior TDS material

Use only where it adds narrative value.

- Aug 2026 TDS AMA: https://talks.s-anand.net/2026-08-10-tds-ama/
- Let AI Take Your Exams: https://talks.s-anand.net/2026-06-12-let-ai-take-your-exams/
- How I use AI to teach: https://www.s-anand.net/blog/how-i-use-ai-to-teach/
- Sep 2025 course update: https://www.s-anand.net/blog/tds-2025-sep-edition/
- Current course: https://tds.s-anand.net/
- Current GA0: https://exam.sanand.workers.dev/tds-2026-09-ga0

The June workshop is relevant background: coding agents taking a TDS-style test scored 10/10 and 9/10 in the documented experiments, and the analysis emphasized that verifiable environments — validators, errors, APIs, files, check buttons — change what can be delegated. Keep numbers tied to that specific test.

## Suggested catalog metadata

When the talk-story skill eventually updates config.json:

- date: 2026-10-05
- categories: [latest]
- event: Tools in Data Science — Sep 2026 Orientation
- location: Remote
- speaker: Anand S — https://www.s-anand.net/
- suggested title: Get the Job Done — and Verify It
- suggested details: TDS treats exams as the curriculum and agents as executors: students learn to specify, orchestrate, collaborate, notice, adapt and verify while tools keep changing.
- duration: derive from media/transcript; do not guess exact scheduled start unless independently confirmed.

The visible page can keep “TDS Orientation” as event label even if narrative headline is more specific.

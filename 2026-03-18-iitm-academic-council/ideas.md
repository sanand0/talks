# AI in Education: briefing for the IIT Madras Academic Council

## How I approached this

I reviewed:

- IIT Madras public governance pages, especially the Senate page.
- Blog posts in `/home/sanand/code/blog/` with `education` category/tag relevance from 2024 through the talk date (`2026-03-18`).
- Selected IITM / TDS / AI-in-education transcripts in `/home/sanand/Dropbox/notes/transcripts/`.
- Relevant notes in `/home/sanand/code/til/`.
- The actual course and exam code / commit history in `/home/sanand/code/tools-in-data-science-public/` and `/home/sanand/code/exam/`.
- In a second pass, adjacent AI/LLM posts, workflow talks, and tooling notes that were not explicitly about education but clearly transfer into teaching, assessment, academic operations, or faculty workflow.

## Second-pass discovery strategy

For the second pass, I used a broader heuristic than just the `education` tag:

- **Search mechanisms, not just domains.** I looked for specifications, evals, telemetry, verification, personalization, workflow orchestration, judgment, and policy patterns even when the source was framed as coding, productivity, or AI workflow.
- **Prioritize ideas with multiple kinds of evidence.** The strongest candidates were the ones that appeared in narrative writing **and** in code, telemetry, prompts, or deployed workflows.
- **Look for transfer into governance.** I gave extra weight to patterns that could change how IITM designs grading, scale, approval, integrity, auditability, or faculty workload.
- **Separate direct deployment from adjacent transfer.** Some additions below are already course/exam mechanisms. Others come from adjacent AI/LLM work but are clearly shaping the direction of your educational experiments.
- **Treat talks as experimental logs.** The talks repo often captures mechanisms, workshop formats, and governance ideas before they show up cleanly in blog posts or course repos, so it is a good place to find early signals.

A note on the audience: IITM's public site clearly exposes the **Senate** as the statutory academic authority responsible for standards of instruction, education, and examination. I could not find a comparably clear public page for a separate "Academic Council". So the profile below treats your audience as the institute's **academic-governance leadership**: senior faculty and administrators who shape curriculum, assessment, approval, and standards.

## Who they are

Based on IITM's public governance language and your IITM transcripts, this group is best understood as the people who sit closest to the institute's academic control system:

- Senior academic leadership responsible for **standards of instruction, education, and examination**.
- Decision-makers or influencers on **syllabus changes, credit structures, assessment formats, and academic policy**.
- People operating inside committee, statute, and approval constraints: **DCC/Senate-style review cycles, documented weights, procurement, platform access, privacy, and defensibility**.
- A group that is likely less interested in AI as spectacle and more interested in whether an innovation is **rigorous, fair, scalable, auditable, affordable, and worth institutionalizing**.

**Primary evidence**

- Public IITM Senate page: `https://www.iitm.ac.in/administration/senate`
- `transcripts/2026-01-28 TDS.md`
- `transcripts/2026-01-14 Palani IITM.md`
- `transcripts/2025-11-20 Jaidev.md`

## What they care about

### 1. Learn by solving, not by reading notes

They care about whether a change preserves or improves the standard of instruction, education, and examination - not just whether it is innovative.

### 2. Every question includes an "Ask AI" button

They will care deeply about what exactly is being assessed once students can use ChatGPT, Claude, Gemini, Copilot, or full coding agents.

### 3. Students are allowed to copy, collaborate, and even hack

A beautiful pilot is not enough. They will care whether it works for hundreds or thousands of students, across TAs, departments, and semesters.

### 4. Teach what AI still cannot do well

If AI is involved in teaching or grading, they will ask: Is it biased? Is it explainable? Can it be gamed? What happens when it is wrong?

### 5. Use hard, messy problems to teach real-world problem solving

They care whether students are learning obsolete sub-skills or durable capabilities that still matter once AI can write code, search docs, and draft analysis.

### 6. The course is open for anyone to inspect

They will care about approval load, procurement, licensing, budgets, source-of-truth data, audit trails, privacy, and operational support.

**Primary evidence**

- Public IITM Senate page: `https://www.iitm.ac.in/administration/senate`
- `transcripts/2026-01-28 TDS.md`
- `transcripts/2026-01-07 TDS.md`
- `transcripts/2025-11-20 Jaidev.md`
- `transcripts/2026-01-14 Palani IITM.md`

## What their current challenges appear to be

### 1. Learn by solving, not by reading notes

Your IITM viva transcripts are explicit that even synchronous viva processes are being gamed with live ChatGPT support, proxy help, and organized outside markets.

### 2. Every question includes an "Ask AI" button

There are settings with roughly **2,000+ L1 vivas** and **3,900+ Python-course submissions / OPPE-scale traces**. Human-only checking does not scale cleanly.

### 3. Students are allowed to copy, collaborate, and even hack

Your transcripts repeatedly surface token budgets, Google licensing, AI Pipe reliability, repo hygiene, access issues, and support load. In other words: many academic ideas fail because the plumbing fails.

### 4. Teach what AI still cannot do well

Syllabus or credit changes need DCC/Senate-style movement. Even when a pedagogical change is obvious, there may be little appetite for a formal approval cycle.

### 5. Use hard, messy problems to teach real-world problem solving

Your Jaidev transcript is especially revealing: student histories are manually patched across multiple systems, dashboards for Senate meetings are hard to trust, and automation struggles when upstream processes are inconsistent.

### 6. The course is open for anyone to inspect

A recurring lesson from TDS and the corporate adaptation transcripts: environmental blockers, unclear interfaces, and brittle instructions can overwhelm even good pedagogy.

### 7. AI-generated comics explain why each question exists

Your IITM/TDS notes explicitly point to a shift toward **MLOps, orchestration, soft skills, domain judgment, storytelling, governance, and verification** - with AI taking over more of the raw coding.

**Primary evidence**

- `transcripts/2025-08-18 IITM LLM Viva demo.md`
- `transcripts/2025-11-03 IITM bot and viva.md`
- `transcripts/2026-03-11 IITM BS Python OPPE.md`
- `transcripts/2026-01-28 TDS.md`
- `transcripts/2026-01-07 TDS.md`
- `transcripts/2025-11-20 Jaidev.md`
- `transcripts/2026-01-14 Palani IITM.md`

## Rating note

- **Importance (0-100%)** = combined estimate of educational impact **and** relevance to IITM academic governance.
- **Novelty (0-100%)** = how uncommon or ahead-of-mainstream this appears in higher education as of March 2026.

## Comprehensive innovation inventory

### Course design and learning experience

### 1. Learn by solving, not by reading notes

- **Description:** You removed most traditional explanatory content and replaced it with problems, prompts, and guided self-learning. Students learn by solving, asking AI, and iterating rather than consuming faculty-written notes.
- **Nature of impact:** Curriculum design; shifts faculty effort from content delivery to problem framing.
- **Why it matters to IITM:** It is a direct answer to the question, "What should we still teach when AI can already generate the content?"
- **Source:** `tools-in-data-science-public/README.md`; `blog/posts/2026/tools-in-data-science-jan-2026.md`; `blog/posts/2026/tds-jan-2026-ga1-released.md`
- **Importance:** 98%
- **Novelty:** 93%

### 2. Every question includes an "Ask AI" button

- **Description:** Every question can be sent directly to an LLM. Students can choose their preferred AI, ask for help at the moment of need, and the course treats that as normal behavior rather than cheating.
- **Nature of impact:** Student support; in-assessment AI orchestration.
- **Why it matters to IITM:** This changes the unit of learning from recall to AI-assisted problem solving and makes AI use observable rather than hidden.
- **Source:** `tools-in-data-science-public/README.md`; `exam/src/exam.js`; `exam/src/utils/askai.js`; `exam/src/exam-tds-2026-01-ga1.info.js`; `blog/posts/2026/which-llms-get-you-better-grades.md`
- **Importance:** 97%
- **Novelty:** 95%

### 3. Students are allowed to copy, collaborate, and even hack

- **Description:** You explicitly allow students to copy from peers, use AI heavily, and even hack questions where appropriate. The emphasis is not purity of process but resourcefulness, verification, and getting the job done.
- **Nature of impact:** Academic policy design; assessment philosophy.
- **Why it matters to IITM:** This is one of the clearest departures from conventional academic norms and goes straight to the heart of what the institute now chooses to reward.
- **Source:** `tools-in-data-science-public/README.md`; `blog/posts/2026/breaking-rules-in-the-age-of-ai.md`; `transcripts/2025-10-06 Straive TDS Live Session.md`
- **Importance:** 95%
- **Novelty:** 92%

### 4. Teach what AI still cannot do well

- **Description:** Instead of emphasizing syntax or routine analysis, the course increasingly targets integration, prompting, debugging, validation, judgment, orchestration, and tool composition.
- **Nature of impact:** Curriculum prioritization.
- **Why it matters to IITM:** This is exactly the strategic curriculum question academic councils now face: what do we teach less of and more of in the AI era?
- **Source:** `blog/posts/2026/tools-in-data-science-jan-2026.md`; `transcripts/2026-01-07 TDS.md`; `til/tds-jan-2026.md`
- **Importance:** 94%
- **Novelty:** 82%

### 5. Use hard, messy problems to teach real-world problem solving

- **Description:** Questions may be intentionally tricky, partly wrong, hidden in the UI, out of syllabus, or only solvable by unusually resourceful students. The aim is to build adaptability, risk-taking, and real-world resilience.
- **Nature of impact:** Assessment design; motivation and culture.
- **Why it matters to IITM:** It is a strong bet that inspiration and real-world readiness sometimes come from unusually hard problems, not smooth progression alone.
- **Source:** `blog/posts/2024/why-dont-students-hack-exams-when-they-can.md`; `blog/posts/2025/problems-that-only-one-student-can-solve.md`; `blog/posts/2026/breaking-rules-in-the-age-of-ai.md`; `blog/posts/2026/tds-jan-2026-ga1-released.md`
- **Importance:** 91%
- **Novelty:** 88%

### 6. The course is open for anyone to inspect

- **Description:** Anyone can audit the course, inspect the repository, watch changes, and follow public discussions. The boundary between formal course and open educational artifact is intentionally porous.
- **Nature of impact:** Access model; transparency; reputation.
- **Why it matters to IITM:** It turns the course itself into a visible institutional experiment and increases scrutiny, feedback, and reach.
- **Source:** `blog/posts/2025/tools-in-data-science-course-is-free-for-all.md`; `tools-in-data-science-public/README.md`; `tools-in-data-science-public/2025-09/README.md`
- **Importance:** 78%
- **Novelty:** 70%

### 7. AI-generated comics explain why each question exists

- **Description:** Instead of just stating the task, you use comics to explain the pedagogical point of the task. AI helps generate prompt variants and final strips, while you curate the best one.
- **Nature of impact:** Engagement; instructional design.
- **Why it matters to IITM:** This is a low-cost, high-memorability way to make AI-era tasks feel legible rather than arbitrary.
- **Source:** `blog/posts/2026/tds-comic-generation.md`; `exam/src/exam-tds-2026-01-ga1.js`
- **Importance:** 72%
- **Novelty:** 84%

### 8. Interactive AI explainers teach unfamiliar concepts

- **Description:** You are using LLMs not just to answer questions but to generate animated, interactive explainers for unfamiliar concepts, making intuition easier to build quickly.
- **Nature of impact:** Teaching media; concept explanation.
- **Why it matters to IITM:** This opens a path to faster concept onboarding for both students and faculty, especially in rapidly changing areas.
- **Source:** `blog/posts/2026/interactive-explainers.md`; `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`
- **Importance:** 74%
- **Novelty:** 78%

### 9. Students learn through game-playing AI tasks

- **Description:** Students solve network/maze/escape-room style API games manually and with AI agents, learning graph traversal, state management, exploration strategies, and agentic workflows through play.
- **Nature of impact:** Assessment design; agentic learning.
- **Why it matters to IITM:** This is a strong example of designing tasks specifically for an agentic world instead of merely bolting AI onto old assignments.
- **Source:** `blog/posts/2026/using-game-playing-agents-to-teach.md`; `exam/src/exam-tds-2026-01-p1.js`; `til/tds-jan-2026.md`
- **Importance:** 83%
- **Novelty:** 90%

### 10. Teacher-first AI adoption through familiar formats

- **Description:** In the broader AI-in-education work beyond TDS, you repeatedly lean toward formats teachers already use: slides, short videos, simple handouts, grounded readers, scan/OCR flows, and short actionable feedback.
- **Nature of impact:** Faculty adoption; implementation realism.
- **Why it matters to IITM:** This is the difference between a flashy pilot and something faculty can actually use next term.
- **Source:** `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`
- **Importance:** 80%
- **Novelty:** 76%

### 11. Test first, then teach from the mistakes

- **Description:** A recurring pattern in your training and course notes is: let learners attempt something first, then teach based on what failed. AI handles some setup/how-to questions; humans handle judgment and harder conceptual blockers.
- **Nature of impact:** Teaching sequence; support architecture.
- **Why it matters to IITM:** This is a scalable way to align teaching effort with actual misconceptions rather than assumed ones.
- **Source:** `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`; `transcripts/2025-10-06 Straive TDS Live Session.md`
- **Importance:** 88%
- **Novelty:** 81%

### 12. Short, personalized next-step feedback from skill clusters

- **Description:** You are experimenting with clustering items into skills, clustering students by gaps, and then generating short, targeted, next-best-practice feedback instead of generic comments.
- **Nature of impact:** Personalization; mastery support.
- **Why it matters to IITM:** This is one of the cleanest ways to turn existing assessment traces into targeted learning support.
- **Source:** `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`
- **Importance:** 81%
- **Novelty:** 74%

### 13. AI as a personalized learning and research coach

- **Description:** You are using models like O3 not just as answer engines but as personalized, memory-aware learning coaches that pick what you should learn, explain what is interesting, and suggest how to apply it.
- **Nature of impact:** Self-directed learning; faculty development.
- **Why it matters to IITM:** It hints at a future where every student - and every faculty member - can have a tailored research/learning companion.
- **Source:** `blog/posts/2025/o3-is-now-my-personalized-learning-coach.md`; `til/llms.md`
- **Importance:** 69%
- **Novelty:** 73%

### Assessment, grading, and integrity

### 14. AI project grading with explainable rubrics

- **Description:** Open-ended project grading is broken into binary sub-criteria, and the model is asked to explain its reasoning before judging. High or suspicious scores can be re-evaluated with stronger guardrails.
- **Nature of impact:** AI grading; rubric design.
- **Why it matters to IITM:** This is a serious attempt to make AI grading more consistent, auditable, and pedagogically useful.
- **Source:** `blog/posts/2024/hacking-llms-a-teachers-guide-to-evaluating-with-chatgpt.md`; `tools-in-data-science-public/project-1/evaluate.py`
- **Importance:** 96%
- **Novelty:** 94%

### 15. Students are tested on prompt attacks and defenses

- **Description:** Students are asked to jailbreak, defend, or otherwise manipulate LLM behavior - both through direct exam questions and through attacker-vs-defender prompt games.
- **Nature of impact:** AI safety education; adversarial literacy.
- **Why it matters to IITM:** It turns prompt security from a theoretical topic into a live, measurable capability.
- **Source:** `tools-in-data-science-public/project-llm-analysis-quiz.md`; `tools-in-data-science-public/project-llm-analysis-quiz/promptfight.py`; `exam/src/q-get-llm-to-say-yes.js`; `blog/posts/2024/hacking-llms-a-teachers-guide-to-evaluating-with-chatgpt.md`
- **Importance:** 89%
- **Novelty:** 96%

### 16. Several scoring models are published for transparency

- **Description:** Instead of hiding one scoring rule, you publish multiple schemes (simple wins, role-balanced rates, difficulty-weighted performance, over-expected performance) so the fairness model itself can be inspected.
- **Nature of impact:** Assessment transparency; scoring theory.
- **Why it matters to IITM:** This is unusually governance-friendly because it surfaces the scoring philosophy instead of burying it.
- **Source:** `tools-in-data-science-public/project-llm-analysis-quiz/evaluation.py`; repo commit `5dc0095`
- **Importance:** 82%
- **Novelty:** 90%

### 17. Students are tested on live, hands-on AI skills

- **Description:** Students are not only told about LLMs; they are examined through live API-driven questions on embeddings, vision, structured output, speech, hallucination traps, RAG, evals, cost optimization, and more.
- **Nature of impact:** Assessment infrastructure; skills certification.
- **Why it matters to IITM:** This is a direct attempt to assess current, practical AI competence at production speed.
- **Source:** `exam/src/worker.js`; `exam/src/exam-tds-2025-05-ga3.js`; `exam/src/exam-tds-2026-01-ga1.js`; repo commit `8c1271a`
- **Importance:** 93%
- **Novelty:** 94%

### 18. Each student gets unique question variants checked on the server

- **Description:** Each student gets deterministic but unique variants, and many correct answers are generated or checked server-side rather than exposed on the client. Some tasks also deliberately force social strategy or collaboration economics instead of pure solo solving. This sharply reduces answer-sharing and answer-key leakage.
- **Nature of impact:** Security architecture; anti-cheating design.
- **Why it matters to IITM:** It is a scalable alternative to trying to preserve old-style fixed answer keys in an AI world.
- **Source:** `exam/README.md`; `exam/src/q-ai-tool-selection.js`; `exam/src/worker.js`; `exam/src/a-*.js`
- **Importance:** 94%
- **Novelty:** 89%

### 19. AI writes, tests, and fixes draft assessment questions

- **Description:** You are not just using AI to draft questions. You are using agentic AI to read the repo, generate question candidates, test them, catch its own errors, and revise before release.
- **Nature of impact:** Faculty workflow; exam authoring.
- **Why it matters to IITM:** This can materially change how quickly new assessment variants can be produced, updated, and maintained.
- **Source:** `tools-in-data-science-public/prompts/roe2-2025-05.md`; repo commits `bbec468` and `d7e7383`
- **Importance:** 88%
- **Novelty:** 95%

### 20. Coding agents are used to test exams before students take them

- **Description:** You now point coding agents at exam tasks both to test whether the question is well-designed and to ask a deeper question: if an agent can solve it, what skill is the exam actually measuring?
- **Nature of impact:** Assessment QA; curricular reflection.
- **Why it matters to IITM:** This is exactly the level of assessment redesign that academic governance now needs.
- **Source:** `blog/posts/2026/cracking-online-exams-with-coding-agents.md`
- **Importance:** 84%
- **Novelty:** 92%

### 21. AI vivas question students about their own repositories

- **Description:** You are experimenting with viva systems that generate questions from a student's repo, probe understanding of their own code, and potentially require them to make a change and push it so the system can diff and score.
- **Nature of impact:** Integrity checking; oral assessment redesign.
- **Why it matters to IITM:** This is one of the most promising responses to AI-assisted project fraud at scale.
- **Source:** `transcripts/2025-08-18 IITM LLM Viva demo.md`; `transcripts/2025-11-03 IITM bot and viva.md`
- **Importance:** 90%
- **Novelty:** 91%

### 22. AI grades richer work like images, stories, and analyses

- **Description:** You are evaluating work that cannot be reduced to a single string: images, narratives, analyses, APIs, and data stories - using vision models, embeddings, deterministic assertions, and LLM rubrics together.
- **Nature of impact:** Open-ended assessment; multimodal grading.
- **Why it matters to IITM:** This extends automation from objective quizzes to richer, more authentic student work.
- **Source:** `tools-in-data-science-public/project-data-analyst/*/promptfoo.yaml`; `tools-in-data-science-public/project-1/evaluate.py`; `exam/src/exam-tds-2026-01-p1.js`
- **Importance:** 79%
- **Novelty:** 94%

### 23. Originality bonuses reward work that differs from the cohort

- **Description:** Some experimental image-generation tasks do not just check correctness. They also reward outputs that are meaningfully distinct from the cohort, using embeddings to measure uniqueness.
- **Nature of impact:** Creativity assessment; anti-convergence design.
- **Why it matters to IITM:** It is a rare attempt to reward originality structurally rather than rhetorically.
- **Source:** `exam/src/exam-tds-2026-01-p1.js`; `til/tds-jan-2026.md`
- **Importance:** 71%
- **Novelty:** 95%

### Support, infrastructure, and operations

### 24. Shared, budgeted AI access for every student

- **Description:** Instead of leaving AI access to personal budgets, you provide a common API-compatible proxy with spend caps. Students get real model access inside a governed perimeter.
- **Nature of impact:** Access infrastructure; equity; cost control.
- **Why it matters to IITM:** This is what makes AI use an institutional capability rather than a privilege of richer or more technically equipped students.
- **Source:** `tools-in-data-science-public/README.md`; `tools-in-data-science-public/large-language-models.md`; `transcripts/2026-01-28 TDS.md`; `exam/README.md`
- **Importance:** 87%
- **Novelty:** 89%

### 25. Live exams track which AI tools students use

- **Description:** The exam system logs which AI students invoke, which model they choose, and when they ask AI. You then analyze model choice, timing, and scores to see what actually helps.
- **Nature of impact:** Learning analytics; instrumentation.
- **Why it matters to IITM:** This creates a rare research-grade dataset on AI use inside authentic, high-stakes student work.
- **Source:** `exam/src/exam.js`; `exam/src/utils/askai.js`; `exam/src/worker.js`; `blog/posts/2026/which-llms-get-you-better-grades.md`; `til/tds-jan-2026.md`
- **Importance:** 86%
- **Novelty:** 93%

### 26. Exam strategy is redesigned from real behavior data

- **Description:** You are using actual assessment traces to learn what predicts performance - e.g. model choice and submission timing - and feeding that back into course design.
- **Nature of impact:** Assessment analytics; behavior design.
- **Why it matters to IITM:** It moves exam design from intuition toward evidence.
- **Source:** `blog/posts/2026/which-llms-get-you-better-grades.md`; `blog/posts/2025/halving-a-deadline-costs-1-4-of-marks-each-time.md`
- **Importance:** 77%
- **Novelty:** 84%

### 27. Students build virtual TAs from real course content

- **Description:** Students are asked to build a virtual TA that answers course questions grounded in actual course and Discourse content, while the institution separately experiments with deploying similar bots for support and viva.
- **Nature of impact:** Student support; productized assessment.
- **Why it matters to IITM:** The same idea works simultaneously as an educational artifact, an internal productivity tool, and a support model.
- **Source:** `tools-in-data-science-public/project-tds-virtual-ta.md`; `tools-in-data-science-public/project-tds-virtual-ta-promptfoo.yaml`; `transcripts/2025-11-03 IITM bot and viva.md`
- **Importance:** 84%
- **Novelty:** 86%

### 28. AI handles routine support; humans handle judgment

- **Description:** The emerging operating model is: let AI handle setup questions, first-pass explanations, repetitive clarifications, and searchable context; reserve humans for ambiguity, reassurance, taste, escalation, and final accountability.
- **Nature of impact:** Support architecture; TA workload design.
- **Why it matters to IITM:** At scale, the institution cannot afford human-only support. But AI does not remove humans; it repositions them as trust anchors and exception handlers.
- **Source:** `tools-in-data-science-public/README.md`; `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`; `blog/posts/2026/human-as-an-interface.md`; `blog/posts/2025/features-actually-used-in-an-llm-playground.md`
- **Importance:** 88%
- **Novelty:** 83%

### 29. Process logs become part of the assessment evidence

- **Description:** In some AI-native assessments, the real evidence is not just the final answer but the trace: session recordings, command markers, verification notes, agent logs, and other proof of how the work was done.
- **Nature of impact:** Evidence design; process-aware assessment.
- **Why it matters to IITM:** If code or output can be copied or agent-generated, logs are closer to the real learning and orchestration skill than the final artifact alone.
- **Source:** `exam/src/q-asciirec-server.js`; `exam/src/a-copilot-cli-server.js`; `exam/src/q-copilot-cli.js`; `blog/posts/2025/if-a-bot-passes-your-exam-what-are-you-teaching.md`; `2025-08-21-ai-coding-guide/README.md`
- **Importance:** 78%
- **Novelty:** 89%

### Learning analytics, research, and faculty meta-skills

### 30. Test cases act like tutors, not just graders

- **Description:** In your IITM BS Python OPPE work, the key pedagogical move is to make test cases diagnose specific mental-model failures - e.g. solving the visible examples instead of the problem, parsing by shape instead of contract, relying on brittle heuristics, or returning the wrong structure despite correct logic. The grader becomes a teaching assistant.
- **Nature of impact:** Feedback design; formative assessment.
- **Why it matters to IITM:** This is one of the strongest bridges between AI, scale, and better learning rather than just faster grading.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2026-01-28 TDS.md`; `2026-03-15-how-students-learn-python/index.html`
- **Importance:** 93%
- **Novelty:** 92%

### 31. Broken code is analyzed before it even compiles

- **Description:** You are exploring `tree-sitter` style parsing so that even syntactically broken student code can still be inspected for logic and misconception patterns, enabling feedback before a clean compile.
- **Nature of impact:** Programming pedagogy; diagnostic infrastructure.
- **Why it matters to IITM:** This directly addresses a major failure mode in novice programming courses: students fail on syntax and never receive feedback on thought process.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`
- **Importance:** 83%
- **Novelty:** 91%

### 32. Student code traces reveal hidden misconception patterns

- **Description:** You are using AI and timestamped code traces to identify fine-grained mental-model pathologies - overfitting to examples, thrashing, structure confusion, missing invariants, parsing-by-shape, and other hidden learning dynamics from actual student behavior.
- **Nature of impact:** Learning analytics; early intervention.
- **Why it matters to IITM:** This turns a large online programme's exhaust into a research and intervention asset.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2025-11-20 Jaidev.md`; `2026-03-15-how-students-learn-python/index.html`
- **Importance:** 84%
- **Novelty:** 90%

### 33. Learning analytics becomes a reusable research programme

- **Description:** The OPPE / Python analysis is not being treated as a one-off dashboard. It is being framed as a reusable meta-framework that could track prerequisite transfer, course-to-course movement, and publishable educational research.
- **Nature of impact:** Institutional research; programme design.
- **Why it matters to IITM:** This is how isolated AI experiments become institute-level knowledge and potentially institute-level advantage.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2026-01-14 Palani IITM.md`; `transcripts/2025-11-20 Jaidev.md`
- **Importance:** 85%
- **Novelty:** 88%

### 34. AI fact-checks textbooks and curriculum claims

- **Description:** You are treating LLMs as large-scale claim extractors and first-pass verifiers for textbooks, using them to flag questionable claims for human follow-up.
- **Nature of impact:** Curriculum quality assurance.
- **Why it matters to IITM:** This is a compelling example of AI augmenting academic quality assurance rather than just teaching.
- **Source:** `blog/posts/2026/verifying-textbook-facts.md`
- **Importance:** 68%
- **Novelty:** 77%

### 35. Giving AI directional feedback becomes a teachable skill

- **Description:** Instead of trying to give expert-level detailed corrections, you are developing a method for giving AI directional, taste-based, audience-aware feedback so the system can use its own expertise more effectively.
- **Nature of impact:** Feedback engineering; faculty/student meta-skill.
- **Why it matters to IITM:** This is one of the more transferable AI-era skills for both students and faculty: how to guide strong models without micromanaging them.
- **Source:** `blog/posts/2026/directional-feedback-for-ai.md`; `til/ai-capabilities.md`
- **Importance:** 71%
- **Novelty:** 83%

### 36. Peer-review data reveals reviewer types and bias

- **Description:** You analyzed how students review one another's work and inferred reviewer personas from actual marking behavior - e.g. always-give-full-marks reviewers, safe-midpoint reviewers, extremists, angry zero-markers, and calibrated reviewers.
- **Nature of impact:** Peer-assessment analytics; calibration and moderation.
- **Why it matters to IITM:** If peer review is used at scale, the quality of evaluators becomes a measurable problem, not just a rubric problem. This creates a path to moderation, reviewer calibration, and TA selection using data.
- **Source:** `blog/posts/2024/the-psychology-of-peer-reviews.md`
- **Importance:** 67%
- **Novelty:** 81%

### 37. Real open-source contributions count as coursework

- **Description:** One project task requires students to make a small, genuinely useful pull request to a public GitHub repository with meaningful real-world visibility, and then prove that it was merged and authored by them.
- **Nature of impact:** Authentic assessment; industry/public contribution.
- **Why it matters to IITM:** This turns assessment into externally validated work instead of an inward-looking academic artifact. It also teaches etiquette, scoping, review readiness, and real contribution quality.
- **Source:** `til/tds-jan-2026.md`; `exam/src/exam-tds-2026-01-p1.js`; `exam/src/q-pr-merge-server.js`
- **Importance:** 76%
- **Novelty:** 86%

## Adjacent AI/LLM innovations with strong educational transfer

A second-pass scan surfaced adjacent innovations from non-education AI/LLM posts, talks, and tooling experiments. They are not all classroom deployments yet, but they clearly shape the direction of your educational practice and are relevant to IITM's governance choices.

### 38. Judgment and taste become explicit learning goals

- **Description:** You frame judgment and taste as the skill AI makes more valuable, and propose concrete practices to build it: argument mapping, perceptual learning, expert prediction audits, peer critique against a goal, and a four-way heuristic for AI-eroded skills: enforce, level-up, switch, or accept.
- **Nature of impact:** Curriculum design; judgment training.
- **Why it matters to IITM:** This gives academic governance a principled way to decide which human skills should still be drilled, which should evolve upward, and which can safely be delegated.
- **Source:** `blog/posts/2026/how-to-develop-taste.md`
- **Importance:** 86%
- **Novelty:** 85%

### 39. Specs and tests become the real assignment

- **Description:** Instead of treating code or output as the main artifact, you increasingly treat a machine-readable brief or SOP - goal, context, constraints, done-when, examples, counter-examples, and eval or test suite - as the primary product. Code becomes a build artifact.
- **Nature of impact:** Assessment design; agentic workflow pedagogy.
- **Why it matters to IITM:** This rewrites what counts as "the answer" in AI-native coursework and reduces ambiguity in grading, appeals, and student execution.
- **Source:** `2025-08-21-ai-coding-guide/README.md`; `2025-09-llm-workflows/README.md`; `2025-11-15-applied-vibe-coding/README.md`
- **Importance:** 91%
- **Novelty:** 90%

### 40. Green/amber/red review levels govern AI at scale

- **Description:** You propose labeling steps or question types by blast radius: green auto-ships, amber is sampled or spot-checked, red is always human-reviewed. This is the governance architecture for large-scale AI grading and support.
- **Nature of impact:** Governance architecture; risk management.
- **Why it matters to IITM:** It offers a Senate-friendly way to automate safely at scale instead of forcing a false choice between full automation and full manual review.
- **Source:** `2025-09-llm-workflows/README.md`; `blog/posts/2025/the-non-obvious-impact-of-reasoning-defaults.md`
- **Importance:** 87%
- **Novelty:** 91%

### 41. Reasoning models verify tough or borderline cases

- **Description:** Your experiments show that increasing reasoning effort on a small model can flip an evaluator from sloppy to reliable, at extra token and time cost. This suggests a cost-aware pattern: cheap screening first, reasoning-backed verification for borderline or high-stakes cases.
- **Nature of impact:** Evaluation economics; grading infrastructure.
- **Why it matters to IITM:** It changes how an institution should budget and design AI evaluation at scale, especially when accuracy matters more than raw throughput.
- **Source:** `blog/posts/2025/the-non-obvious-impact-of-reasoning-defaults.md`; `blog/posts/2026/when-llm-prices-fall-10x-every-year.md`
- **Importance:** 83%
- **Novelty:** 90%

### 42. Smarter code-copy detection uses structure and similarity

- **Description:** You are not relying on raw string matching. You strip docstrings, tokenize code, build shingles, and use MinHash or Jaccard similarity to surface suspiciously similar submissions for follow-up.
- **Nature of impact:** Integrity analytics; plagiarism triage.
- **Why it matters to IITM:** This is more robust than obvious copy detection and more scalable than manual review, especially when students try to disguise copied code cosmetically.
- **Source:** `exam/src/tds/project-1/similarity.py`
- **Importance:** 84%
- **Novelty:** 86%

### 43. Students are graded on designing AI workflows

- **Description:** Some newer tasks ask students not just to produce an answer, but to specify a multi-step agent workflow: datasets, stages, prompts, tools, quality checks, and delivery formats, in machine-readable JSON.
- **Nature of impact:** Agentic assessment; workflow design.
- **Why it matters to IITM:** This measures whether students can design reliable AI-assisted work, not just benefit from it.
- **Source:** `exam/src/q-vibe-analysis-autopilot.js`; `2025-09-llm-workflows/README.md`
- **Importance:** 82%
- **Novelty:** 90%

### 44. One book becomes many AI-generated study modes

- **Description:** You use AI to summarize books, fact-check claims, compare multiple books, and re-author dense prose in more engaging styles. One text becomes many possible study experiences.
- **Nature of impact:** Self-directed learning; reading pedagogy.
- **Why it matters to IITM:** This points toward a future where reading lists and textbooks become adaptive interfaces rather than fixed artifacts.
- **Source:** `blog/posts/2026/new-ways-of-reading-books.md`
- **Importance:** 75%
- **Novelty:** 87%

### 45. Policies can be turned into executable checks

- **Description:** Policies, rubrics, and institutional rules can be translated into machine-executable checks, so compliance is not just interpreted manually but verified automatically and audibly at scale.
- **Nature of impact:** Governance automation; policy enforcement.
- **Why it matters to IITM:** This offers a path from Senate-approved policy to consistent implementation across thousands of submissions, workflows, or approvals.
- **Source:** `2025-09-22-llm-trends/README.md`; `2025-12-05-scdm-keynote/README.md`; `2025-11-13-nirmal-impress-ai-hr/README.md`
- **Importance:** 82%
- **Novelty:** 88%

### 46. Canonical Q&A cards become institutional memory

- **Description:** Instead of letting answers live in experts' heads or stale wikis, recurring questions are converted into canonical Q&A cards with source links, owner, freshness date, and retriever-friendly chunks that both humans and agents can cite.
- **Nature of impact:** Knowledge infrastructure; support consistency.
- **Why it matters to IITM:** This is a scalable foundation for student support, faculty enablement, and consistent policy interpretation across large programmes.
- **Source:** `2025-09-llm-workflows/README.md`
- **Importance:** 81%
- **Novelty:** 84%

### 47. New AI academic workflows roll out in shadow mode first

- **Description:** New AI graders, bots, or support workflows are first run in shadow mode or on a tiny canary slice with synthetic data, kill-switches, and rollbacks, so the institution can learn safely before full deployment.
- **Nature of impact:** Deployment governance; operational risk control.
- **Why it matters to IITM:** This is a practical mechanism for introducing AI into high-stakes academic settings without reckless all-at-once launches.
- **Source:** `2025-09-llm-workflows/README.md`
- **Importance:** 80%
- **Novelty:** 86%

### 48. Faculty learn to manage agents, not just chat with them

- **Description:** Short, role-specific training on writing specs, setting budgets, adding kill-switches, and defining escalation rules turns non-specialists into competent supervisors of agentic workflows.
- **Nature of impact:** Faculty development; operational capability-building.
- **Why it matters to IITM:** If AI is to be institutionalized, faculty and administrators need orchestration literacy, not just exposure to chatbots.
- **Source:** `2025-09-llm-workflows/README.md`; `2025-11-13-nirmal-impress-ai-hr/README.md`
- **Importance:** 78%
- **Novelty:** 82%

### 49. AI lets non-coders build interactive learning tools

- **Description:** Non-technical staff and students can use AI to build interactive timelines, maps, biographies, and other learning artifacts for humanities and social-science subjects. The limiting factor becomes imagination, not coding ability.
- **Nature of impact:** Curriculum expansion; interdisciplinary pedagogy.
- **Why it matters to IITM:** This extends AI-native pedagogy beyond CS and data science into humanities, social sciences, and foundational courses.
- **Source:** `2026-02-26-vibe-coding-for-humanities-ashoka/transcript.md`
- **Importance:** 79%
- **Novelty:** 85%

### 50. Students learn to run many AI attempts in parallel

- **Description:** Learners are encouraged to run multiple prompts, models, or tasks in parallel to sample more ideas, compare approaches, and converge faster instead of waiting on one sequential path.
- **Nature of impact:** Meta-skill; workflow pedagogy.
- **Why it matters to IITM:** This teaches an AI-native way of working: portfolio thinking, faster exploration, and explicit comparison across models and solutions.
- **Source:** `2025-10-29-llm-data-visualization/README.md`; `2026-02-26-vibe-coding-for-humanities-ashoka/transcript.md`; `2025-11-15-applied-vibe-coding/README.md`
- **Importance:** 75%
- **Novelty:** 79%

### Assessment, grading, and integrity

### 51. Reward originality without punishing collaboration

- **Description:** Instead of treating copying as automatic misconduct, you reward genuinely novel work with bonus marks, compare only against earlier submissions, and use code-similarity analysis to study how collaboration actually spreads through a cohort.
- **Nature of impact:** Assessment incentives; integrity design; originality analytics.
- **Why it matters to IITM:** It offers a more realistic AI-era policy than blanket prohibition: students can learn from one another openly, while the institution still rewards initiative, sharing, and authentic variation.
- **Source:** `https://www.s-anand.net/blog/when-and-how-to-copy-assignments/`
- **Importance:** 84%
- **Novelty:** 92%

### Learning analytics, research, and faculty meta-skills

### 52. Replay galleries turn exam logs into faculty-readable stories

- **Description:** Anonymized coding-exam traces are turned into plain-language public reports, narrated replays, and error-pattern stories so non-technical faculty can see where students get stuck and what interventions or test fixes would help.
- **Nature of impact:** Learning analytics communication; faculty development; evidence translation.
- **Why it matters to IITM:** Research only changes policy when decision-makers can understand it. This makes raw exam exhaust legible to faculty, programme teams, and academic leaders without requiring them to read notebooks or logs.
- **Source:** `https://sanand0.github.io/pyoppe/`; `https://sanand0.github.io/pyoppe/analysis/replays-v3.html`; `https://sanand0.github.io/pyoppe/analysis/report.html`
- **Importance:** 82%
- **Novelty:** 88%

### 53. Problem-solving is broken into coachable steps, not one talent

- **Description:** Large-scale response analysis is used to locate the exact step where students break down - reading the givens, choosing a method, surviving multi-select traps, or knowing when to exit a bad section - so the tutor can coach the failed step instead of reteaching everything.
- **Nature of impact:** Adaptive tutoring; diagnostic assessment; strategy coaching.
- **Why it matters to IITM:** This is a strong model for turning assessment data into targeted remediation. It replaces vague labels like "weak student" with specific, trainable failure modes and coaching modules.
- **Source:** `https://files.s-anand.net/temp/navodaya-2026/`
- **Importance:** 89%
- **Novelty:** 90%

## Summary table

| Innovation                                                       | Importance (0-100%) | Novelty (0-100%) |
| ---------------------------------------------------------------- | ------------------: | ---------------: |
| Learn by solving, not by reading notes                           |                 98% |              93% |
| Every question includes an "Ask AI" button                       |                 97% |              95% |
| AI project grading with explainable rubrics                      |                 96% |              94% |
| Students are allowed to copy, collaborate, and even hack         |                 95% |              92% |
| Each student gets unique question variants checked on the server |                 94% |              89% |
| Teach what AI still cannot do well                               |                 94% |              82% |
| Students are tested on live, hands-on AI skills                  |                 93% |              94% |
| Test cases act like tutors, not just graders                     |                 93% |              92% |
| Specs and tests become the real assignment                       |                 91% |              90% |
| Use hard, messy problems to teach real-world problem solving     |                 91% |              88% |
| AI vivas question students about their own repositories          |                 90% |              91% |
| Students are tested on prompt attacks and defenses               |                 89% |              96% |
| Problem-solving is broken into coachable steps, not one talent   |                 89% |              90% |
| AI writes, tests, and fixes draft assessment questions           |                 88% |              95% |
| AI handles routine support; humans handle judgment               |                 88% |              83% |
| Test first, then teach from the mistakes                         |                 88% |              81% |
| Green/amber/red review levels govern AI at scale                 |                 87% |              91% |
| Shared, budgeted AI access for every student                     |                 87% |              89% |
| Live exams track which AI tools students use                     |                 86% |              93% |
| Judgment and taste become explicit learning goals                |                 86% |              85% |
| Learning analytics becomes a reusable research programme         |                 85% |              88% |
| Coding agents are used to test exams before students take them   |                 84% |              92% |
| Reward originality without punishing collaboration               |                 84% |              92% |
| Student code traces reveal hidden misconception patterns         |                 84% |              90% |
| Students build virtual TAs from real course content              |                 84% |              86% |
| Smarter code-copy detection uses structure and similarity        |                 84% |              86% |
| Broken code is analyzed before it even compiles                  |                 83% |              91% |
| Students learn through game-playing AI tasks                     |                 83% |              90% |
| Reasoning models verify tough or borderline cases                |                 83% |              90% |
| Several scoring models are published for transparency            |                 82% |              90% |
| Students are graded on designing AI workflows                    |                 82% |              90% |
| Policies can be turned into executable checks                    |                 82% |              88% |
| Replay galleries turn exam logs into faculty-readable stories    |                 82% |              88% |
| Canonical Q&A cards become institutional memory                  |                 81% |              84% |
| Short, personalized next-step feedback from skill clusters       |                 81% |              74% |
| New AI academic workflows roll out in shadow mode first          |                 80% |              86% |
| Teacher-first AI adoption through familiar formats               |                 80% |              76% |
| AI grades richer work like images, stories, and analyses         |                 79% |              94% |
| AI lets non-coders build interactive learning tools              |                 79% |              85% |
| Process logs become part of the assessment evidence              |                 78% |              89% |
| Faculty learn to manage agents, not just chat with them          |                 78% |              82% |
| The course is open for anyone to inspect                         |                 78% |              70% |
| Exam strategy is redesigned from real behavior data              |                 77% |              84% |
| Real open-source contributions count as coursework               |                 76% |              86% |
| One book becomes many AI-generated study modes                   |                 75% |              87% |
| Students learn to run many AI attempts in parallel               |                 75% |              79% |
| Interactive AI explainers teach unfamiliar concepts              |                 74% |              78% |
| AI-generated comics explain why each question exists             |                 72% |              84% |
| Originality bonuses reward work that differs from the cohort     |                 71% |              95% |
| Giving AI directional feedback becomes a teachable skill         |                 71% |              83% |
| AI as a personalized learning and research coach                 |                 69% |              73% |
| AI fact-checks textbooks and curriculum claims                   |                 68% |              77% |
| Peer-review data reveals reviewer types and bias                 |                 67% |              81% |

## Bottom line

If I had to compress the whole story for the Council into one sentence, it would be this:

> You are not merely adding AI tools to an existing course. You are systematically redesigning **curriculum, assessment, support, integrity, and educational research** around the reality that AI is now part of the learning environment.

The strongest institutional themes are:

1. **Shift the unit of assessment** from unaided recall to AI-assisted problem solving plus verification.
2. **Make AI use visible and governable** instead of pretending it can be kept out.
3. **Use AI to scale feedback and support**, but keep humans for judgment and ambiguity.
4. **Exploit academic exhaust as a research asset** - especially at IITM's scale.
5. **Treat access, cost, transparency, and approval pathways as first-class design constraints**.

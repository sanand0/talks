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

### 1. Academic standards and defensibility

They care about whether a change preserves or improves the standard of instruction, education, and examination - not just whether it is innovative.

### 2. Assessment integrity in the age of AI

They will care deeply about what exactly is being assessed once students can use ChatGPT, Claude, Gemini, Copilot, or full coding agents.

### 3. Scale

A beautiful pilot is not enough. They will care whether it works for hundreds or thousands of students, across TAs, departments, and semesters.

### 4. Fairness, transparency, and contestability

If AI is involved in teaching or grading, they will ask: Is it biased? Is it explainable? Can it be gamed? What happens when it is wrong?

### 5. Curriculum relevance

They care whether students are learning obsolete sub-skills or durable capabilities that still matter once AI can write code, search docs, and draft analysis.

### 6. Governance, process, and cost

They will care about approval load, procurement, licensing, budgets, source-of-truth data, audit trails, privacy, and operational support.

**Primary evidence**

- Public IITM Senate page: `https://www.iitm.ac.in/administration/senate`
- `transcripts/2026-01-28 TDS.md`
- `transcripts/2026-01-07 TDS.md`
- `transcripts/2025-11-20 Jaidev.md`
- `transcripts/2026-01-14 Palani IITM.md`

## What their current challenges appear to be

### 1. Traditional assessment is getting easier to game

Your IITM viva transcripts are explicit that even synchronous viva processes are being gamed with live ChatGPT support, proxy help, and organized outside markets.

### 2. The institute still needs scalable integrity checks

There are settings with roughly **2,000+ L1 vivas** and **3,900+ Python-course submissions / OPPE-scale traces**. Human-only checking does not scale cleanly.

### 3. The real bottleneck is often not pedagogy but operations

Your transcripts repeatedly surface token budgets, Google licensing, AI Pipe reliability, repo hygiene, access issues, and support load. In other words: many academic ideas fail because the plumbing fails.

### 4. Governance friction is real

Syllabus or credit changes need DCC/Senate-style movement. Even when a pedagogical change is obvious, there may be little appetite for a formal approval cycle.

### 5. Source-of-truth data is messy

Your Jaidev transcript is especially revealing: student histories are manually patched across multiple systems, dashboards for Senate meetings are hard to trust, and automation struggles when upstream processes are inconsistent.

### 6. Student friction can swamp instructional intent

A recurring lesson from TDS and the corporate adaptation transcripts: environmental blockers, unclear interfaces, and brittle instructions can overwhelm even good pedagogy.

### 7. The skills that matter are moving

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

### 1. Question-only, prompt-first curriculum ("There is no course content")

- **Description:** You removed most traditional explanatory content and replaced it with problems, prompts, and guided self-learning. Students learn by solving, asking AI, and iterating rather than consuming faculty-written notes.
- **Nature of impact:** Curriculum design; shifts faculty effort from content delivery to problem framing.
- **Why it matters to IITM:** It is a direct answer to the question, "What should we still teach when AI can already generate the content?"
- **Source:** `tools-in-data-science-public/README.md`; `blog/posts/2026/tools-in-data-science-jan-2026.md`; `blog/posts/2026/tds-jan-2026-ga1-released.md`
- **Importance:** 98%
- **Novelty:** 93%

### 2. "Ask AI" embedded inside every question, with model choice

- **Description:** Every question can be sent directly to an LLM. Students can choose their preferred AI, ask for help at the moment of need, and the course treats that as normal behavior rather than cheating.
- **Nature of impact:** Student support; in-assessment AI orchestration.
- **Why it matters to IITM:** This changes the unit of learning from recall to AI-assisted problem solving and makes AI use observable rather than hidden.
- **Source:** `tools-in-data-science-public/README.md`; `exam/src/exam.js`; `exam/src/utils/askai.js`; `exam/src/exam-tds-2026-01-ga1.info.js`; `blog/posts/2026/which-llms-get-you-better-grades.md`
- **Importance:** 97%
- **Novelty:** 95%

### 3. Copying, collaboration, and even hacking are made part of the curriculum

- **Description:** You explicitly allow students to copy from peers, use AI heavily, and even hack questions where appropriate. The emphasis is not purity of process but resourcefulness, verification, and getting the job done.
- **Nature of impact:** Academic policy design; assessment philosophy.
- **Why it matters to IITM:** This is one of the clearest departures from conventional academic norms and goes straight to the heart of what the institute now chooses to reward.
- **Source:** `tools-in-data-science-public/README.md`; `blog/posts/2026/breaking-rules-in-the-age-of-ai.md`; `transcripts/2025-10-06 Straive TDS Live Session.md`
- **Importance:** 95%
- **Novelty:** 92%

### 4. The curriculum is being redesigned around what AI still does badly

- **Description:** Instead of emphasizing syntax or routine analysis, the course increasingly targets integration, prompting, debugging, validation, judgment, orchestration, and tool composition.
- **Nature of impact:** Curriculum prioritization.
- **Why it matters to IITM:** This is exactly the strategic curriculum question academic councils now face: what do we teach less of and more of in the AI era?
- **Source:** `blog/posts/2026/tools-in-data-science-jan-2026.md`; `transcripts/2026-01-07 TDS.md`; `til/tds-jan-2026.md`
- **Importance:** 94%
- **Novelty:** 82%

### 5. Hard, ambiguous, hackable, beyond-syllabus problems are used deliberately

- **Description:** Questions may be intentionally tricky, partly wrong, hidden in the UI, out of syllabus, or only solvable by unusually resourceful students. The aim is to build adaptability, risk-taking, and real-world resilience.
- **Nature of impact:** Assessment design; motivation and culture.
- **Why it matters to IITM:** It is a strong bet that inspiration and real-world readiness sometimes come from unusually hard problems, not smooth progression alone.
- **Source:** `blog/posts/2024/why-dont-students-hack-exams-when-they-can.md`; `blog/posts/2025/problems-that-only-one-student-can-solve.md`; `blog/posts/2026/breaking-rules-in-the-age-of-ai.md`; `blog/posts/2026/tds-jan-2026-ga1-released.md`
- **Importance:** 91%
- **Novelty:** 88%

### 6. The course is public and auditable outside IITM

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

### 8. Interactive explainers are used as a new teaching medium

- **Description:** You are using LLMs not just to answer questions but to generate animated, interactive explainers for unfamiliar concepts, making intuition easier to build quickly.
- **Nature of impact:** Teaching media; concept explanation.
- **Why it matters to IITM:** This opens a path to faster concept onboarding for both students and faculty, especially in rapidly changing areas.
- **Source:** `blog/posts/2026/interactive-explainers.md`; `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`
- **Importance:** 74%
- **Novelty:** 78%

### 9. Game-playing agents are turned into learning tasks

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

### 11. Diagnostic-first teaching: assess first, teach from the errors

- **Description:** A recurring pattern in your training and course notes is: let learners attempt something first, then teach based on what failed. AI handles some setup/how-to questions; humans handle judgment and harder conceptual blockers.
- **Nature of impact:** Teaching sequence; support architecture.
- **Why it matters to IITM:** This is a scalable way to align teaching effort with actual misconceptions rather than assumed ones.
- **Source:** `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`; `transcripts/2025-10-06 Straive TDS Live Session.md`
- **Importance:** 88%
- **Novelty:** 81%

### 12. Personalized skill clustering and short next-step feedback

- **Description:** You are experimenting with clustering items into skills, clustering students by gaps, and then generating short, targeted, next-best-practice feedback instead of generic comments.
- **Nature of impact:** Personalization; mastery support.
- **Why it matters to IITM:** This is one of the cleanest ways to turn existing assessment traces into targeted learning support.
- **Source:** `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`
- **Importance:** 81%
- **Novelty:** 74%

### 13. Personalized AI learning coach / research coach

- **Description:** You are using models like O3 not just as answer engines but as personalized, memory-aware learning coaches that pick what you should learn, explain what is interesting, and suggest how to apply it.
- **Nature of impact:** Self-directed learning; faculty development.
- **Why it matters to IITM:** It hints at a future where every student - and every faculty member - can have a tailored research/learning companion.
- **Source:** `blog/posts/2025/o3-is-now-my-personalized-learning-coach.md`; `til/llms.md`
- **Importance:** 69%
- **Novelty:** 73%

### Assessment, grading, and integrity

### 14. LLM-based project grading with granular rubrics and explanation-first judging

- **Description:** Open-ended project grading is broken into binary sub-criteria, and the model is asked to explain its reasoning before judging. High or suspicious scores can be re-evaluated with stronger guardrails.
- **Nature of impact:** AI grading; rubric design.
- **Why it matters to IITM:** This is a serious attempt to make AI grading more consistent, auditable, and pedagogically useful.
- **Source:** `blog/posts/2024/hacking-llms-a-teachers-guide-to-evaluating-with-chatgpt.md`; `tools-in-data-science-public/project-1/evaluate.py`
- **Importance:** 96%
- **Novelty:** 94%

### 15. Adversarial prompt security is taught as an assessable skill

- **Description:** Students are asked to jailbreak, defend, or otherwise manipulate LLM behavior - both through direct exam questions and through attacker-vs-defender prompt games.
- **Nature of impact:** AI safety education; adversarial literacy.
- **Why it matters to IITM:** It turns prompt security from a theoretical topic into a live, measurable capability.
- **Source:** `tools-in-data-science-public/project-llm-analysis-quiz.md`; `tools-in-data-science-public/project-llm-analysis-quiz/promptfight.py`; `exam/src/q-get-llm-to-say-yes.js`; `blog/posts/2024/hacking-llms-a-teachers-guide-to-evaluating-with-chatgpt.md`
- **Importance:** 89%
- **Novelty:** 96%

### 16. Transparent multi-scheme scoring for adversarial and open-ended tasks

- **Description:** Instead of hiding one scoring rule, you publish multiple schemes (simple wins, role-balanced rates, difficulty-weighted performance, over-expected performance) so the fairness model itself can be inspected.
- **Nature of impact:** Assessment transparency; scoring theory.
- **Why it matters to IITM:** This is unusually governance-friendly because it surfaces the scoring philosophy instead of burying it.
- **Source:** `tools-in-data-science-public/project-llm-analysis-quiz/evaluation.py`; repo commit `5dc0095`
- **Importance:** 82%
- **Novelty:** 90%

### 17. Live LLM API evaluation and hands-on LLM competency batteries

- **Description:** Students are not only told about LLMs; they are examined through live API-driven questions on embeddings, vision, structured output, speech, hallucination traps, RAG, evals, cost optimization, and more.
- **Nature of impact:** Assessment infrastructure; skills certification.
- **Why it matters to IITM:** This is a direct attempt to assess current, practical AI competence at production speed.
- **Source:** `exam/src/worker.js`; `exam/src/exam-tds-2025-05-ga3.js`; `exam/src/exam-tds-2026-01-ga1.js`; repo commit `8c1271a`
- **Importance:** 93%
- **Novelty:** 94%

### 18. Dynamic seeded personalization with server-side validation

- **Description:** Each student gets deterministic but unique variants, and many correct answers are generated or checked server-side rather than exposed on the client. Some tasks also deliberately force social strategy or collaboration economics instead of pure solo solving. This sharply reduces answer-sharing and answer-key leakage.
- **Nature of impact:** Security architecture; anti-cheating design.
- **Why it matters to IITM:** It is a scalable alternative to trying to preserve old-style fixed answer keys in an AI world.
- **Source:** `exam/README.md`; `exam/src/q-ai-tool-selection.js`; `exam/src/worker.js`; `exam/src/a-*.js`
- **Importance:** 94%
- **Novelty:** 89%

### 19. AI-generated assessment content with self-testing and self-correction

- **Description:** You are not just using AI to draft questions. You are using agentic AI to read the repo, generate question candidates, test them, catch its own errors, and revise before release.
- **Nature of impact:** Faculty workflow; exam authoring.
- **Why it matters to IITM:** This can materially change how quickly new assessment variants can be produced, updated, and maintained.
- **Source:** `tools-in-data-science-public/prompts/roe2-2025-05.md`; repo commits `bbec468` and `d7e7383`
- **Importance:** 88%
- **Novelty:** 95%

### 20. Coding agents are used to QA exams and expose the real skill being tested

- **Description:** You now point coding agents at exam tasks both to test whether the question is well-designed and to ask a deeper question: if an agent can solve it, what skill is the exam actually measuring?
- **Nature of impact:** Assessment QA; curricular reflection.
- **Why it matters to IITM:** This is exactly the level of assessment redesign that academic governance now needs.
- **Source:** `blog/posts/2026/cracking-online-exams-with-coding-agents.md`
- **Importance:** 84%
- **Novelty:** 92%

### 21. Repo-grounded AI viva with follow-up code-change checks

- **Description:** You are experimenting with viva systems that generate questions from a student's repo, probe understanding of their own code, and potentially require them to make a change and push it so the system can diff and score.
- **Nature of impact:** Integrity checking; oral assessment redesign.
- **Why it matters to IITM:** This is one of the most promising responses to AI-assisted project fraud at scale.
- **Source:** `transcripts/2025-08-18 IITM LLM Viva demo.md`; `transcripts/2025-11-03 IITM bot and viva.md`
- **Importance:** 90%
- **Novelty:** 91%

### 22. Multimodal and open-ended AI evaluation with vision models, embeddings, and Promptfoo

- **Description:** You are evaluating work that cannot be reduced to a single string: images, narratives, analyses, APIs, and data stories - using vision models, embeddings, deterministic assertions, and LLM rubrics together.
- **Nature of impact:** Open-ended assessment; multimodal grading.
- **Why it matters to IITM:** This extends automation from objective quizzes to richer, more authentic student work.
- **Source:** `tools-in-data-science-public/project-data-analyst/*/promptfoo.yaml`; `tools-in-data-science-public/project-1/evaluate.py`; `exam/src/exam-tds-2026-01-p1.js`
- **Importance:** 79%
- **Novelty:** 94%

### 23. Cohort-level originality / diversity scoring with embeddings

- **Description:** Some experimental image-generation tasks do not just check correctness. They also reward outputs that are meaningfully distinct from the cohort, using embeddings to measure uniqueness.
- **Nature of impact:** Creativity assessment; anti-convergence design.
- **Why it matters to IITM:** It is a rare attempt to reward originality structurally rather than rhetorically.
- **Source:** `exam/src/exam-tds-2026-01-p1.js`; `til/tds-jan-2026.md`
- **Importance:** 71%
- **Novelty:** 95%

### Support, infrastructure, and operations

### 24. AI Pipe / budgeted proxy access for all students

- **Description:** Instead of leaving AI access to personal budgets, you provide a common API-compatible proxy with spend caps. Students get real model access inside a governed perimeter.
- **Nature of impact:** Access infrastructure; equity; cost control.
- **Why it matters to IITM:** This is what makes AI use an institutional capability rather than a privilege of richer or more technically equipped students.
- **Source:** `tools-in-data-science-public/README.md`; `tools-in-data-science-public/large-language-models.md`; `transcripts/2026-01-28 TDS.md`; `exam/README.md`
- **Importance:** 87%
- **Novelty:** 89%

### 25. AI-use telemetry and model-vs-score analytics inside live assessments

- **Description:** The exam system logs which AI students invoke, which model they choose, and when they ask AI. You then analyze model choice, timing, and scores to see what actually helps.
- **Nature of impact:** Learning analytics; instrumentation.
- **Why it matters to IITM:** This creates a rare research-grade dataset on AI use inside authentic, high-stakes student work.
- **Source:** `exam/src/exam.js`; `exam/src/utils/askai.js`; `exam/src/worker.js`; `blog/posts/2026/which-llms-get-you-better-grades.md`; `til/tds-jan-2026.md`
- **Importance:** 86%
- **Novelty:** 93%

### 26. Data-driven exam strategy and deadline analytics

- **Description:** You are using actual assessment traces to learn what predicts performance - e.g. model choice and submission timing - and feeding that back into course design.
- **Nature of impact:** Assessment analytics; behavior design.
- **Why it matters to IITM:** It moves exam design from intuition toward evidence.
- **Source:** `blog/posts/2026/which-llms-get-you-better-grades.md`; `blog/posts/2025/halving-a-deadline-costs-1-4-of-marks-each-time.md`
- **Importance:** 77%
- **Novelty:** 84%

### 27. Virtual TA / chatbot as both student tool and student-built artifact

- **Description:** Students are asked to build a virtual TA that answers course questions grounded in actual course and Discourse content, while the institution separately experiments with deploying similar bots for support and viva.
- **Nature of impact:** Student support; productized assessment.
- **Why it matters to IITM:** The same idea works simultaneously as an educational artifact, an internal productivity tool, and a support model.
- **Source:** `tools-in-data-science-public/project-tds-virtual-ta.md`; `tools-in-data-science-public/project-tds-virtual-ta-promptfoo.yaml`; `transcripts/2025-11-03 IITM bot and viva.md`
- **Importance:** 84%
- **Novelty:** 86%

### 28. AI as the first-line TA, humans for exceptions, trust, and judgment

- **Description:** The emerging operating model is: let AI handle setup questions, first-pass explanations, repetitive clarifications, and searchable context; reserve humans for ambiguity, reassurance, taste, escalation, and final accountability.
- **Nature of impact:** Support architecture; TA workload design.
- **Why it matters to IITM:** At scale, the institution cannot afford human-only support. But AI does not remove humans; it repositions them as trust anchors and exception handlers.
- **Source:** `tools-in-data-science-public/README.md`; `transcripts/learnings/ai-in-education-v1.md`; `transcripts/learnings/ai-in-education-v2.md`; `blog/posts/2026/human-as-an-interface.md`; `blog/posts/2025/features-actually-used-in-an-llm-playground.md`
- **Importance:** 88%
- **Novelty:** 83%

### 29. Execution logs, verification notes, and terminal recordings as assessment evidence

- **Description:** In some AI-native assessments, the real evidence is not just the final answer but the trace: session recordings, command markers, verification notes, agent logs, and other proof of how the work was done.
- **Nature of impact:** Evidence design; process-aware assessment.
- **Why it matters to IITM:** If code or output can be copied or agent-generated, logs are closer to the real learning and orchestration skill than the final artifact alone.
- **Source:** `exam/src/q-asciirec-server.js`; `exam/src/a-copilot-cli-server.js`; `exam/src/q-copilot-cli.js`; `blog/posts/2025/if-a-bot-passes-your-exam-what-are-you-teaching.md`; `2025-08-21-ai-coding-guide/README.md`
- **Importance:** 78%
- **Novelty:** 89%

### Learning analytics, research, and faculty meta-skills

### 30. Test cases are being reconceived as automated tutors, not just graders

- **Description:** In your IITM BS Python OPPE work, the key pedagogical move is to make test cases diagnose specific mental-model failures - e.g. solving the visible examples instead of the problem, parsing by shape instead of contract, relying on brittle heuristics, or returning the wrong structure despite correct logic. The grader becomes a teaching assistant.
- **Nature of impact:** Feedback design; formative assessment.
- **Why it matters to IITM:** This is one of the strongest bridges between AI, scale, and better learning rather than just faster grading.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2026-01-28 TDS.md`; `2026-03-15-how-students-learn-python/index.html`
- **Importance:** 93%
- **Novelty:** 92%

### 31. Fault-tolerant AST parsing for broken student code

- **Description:** You are exploring `tree-sitter` style parsing so that even syntactically broken student code can still be inspected for logic and misconception patterns, enabling feedback before a clean compile.
- **Nature of impact:** Programming pedagogy; diagnostic infrastructure.
- **Why it matters to IITM:** This directly addresses a major failure mode in novice programming courses: students fail on syntax and never receive feedback on thought process.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`
- **Importance:** 83%
- **Novelty:** 91%

### 32. Mining code snapshots and practice data for misconception patterns

- **Description:** You are using AI and timestamped code traces to identify fine-grained mental-model pathologies - overfitting to examples, thrashing, structure confusion, missing invariants, parsing-by-shape, and other hidden learning dynamics from actual student behavior.
- **Nature of impact:** Learning analytics; early intervention.
- **Why it matters to IITM:** This turns a large online programme's exhaust into a research and intervention asset.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2025-11-20 Jaidev.md`; `2026-03-15-how-students-learn-python/index.html`
- **Importance:** 84%
- **Novelty:** 90%

### 33. Cross-course AI-assisted learning analytics as a research programme

- **Description:** The OPPE / Python analysis is not being treated as a one-off dashboard. It is being framed as a reusable meta-framework that could track prerequisite transfer, course-to-course movement, and publishable educational research.
- **Nature of impact:** Institutional research; programme design.
- **Why it matters to IITM:** This is how isolated AI experiments become institute-level knowledge and potentially institute-level advantage.
- **Source:** `transcripts/2026-03-11 IITM BS Python OPPE.md`; `transcripts/2026-01-14 Palani IITM.md`; `transcripts/2025-11-20 Jaidev.md`
- **Importance:** 85%
- **Novelty:** 88%

### 34. LLM-based fact-checking of textbooks and curriculum claims

- **Description:** You are treating LLMs as large-scale claim extractors and first-pass verifiers for textbooks, using them to flag questionable claims for human follow-up.
- **Nature of impact:** Curriculum quality assurance.
- **Why it matters to IITM:** This is a compelling example of AI augmenting academic quality assurance rather than just teaching.
- **Source:** `blog/posts/2026/verifying-textbook-facts.md`
- **Importance:** 68%
- **Novelty:** 77%

### 35. Directional feedback for AI as a teachable meta-skill

- **Description:** Instead of trying to give expert-level detailed corrections, you are developing a method for giving AI directional, taste-based, audience-aware feedback so the system can use its own expertise more effectively.
- **Nature of impact:** Feedback engineering; faculty/student meta-skill.
- **Why it matters to IITM:** This is one of the more transferable AI-era skills for both students and faculty: how to guide strong models without micromanaging them.
- **Source:** `blog/posts/2026/directional-feedback-for-ai.md`; `til/ai-capabilities.md`
- **Importance:** 71%
- **Novelty:** 83%

### 36. Peer-review analytics to diagnose evaluator personas

- **Description:** You analyzed how students review one another's work and inferred reviewer personas from actual marking behavior - e.g. always-give-full-marks reviewers, safe-midpoint reviewers, extremists, angry zero-markers, and calibrated reviewers.
- **Nature of impact:** Peer-assessment analytics; calibration and moderation.
- **Why it matters to IITM:** If peer review is used at scale, the quality of evaluators becomes a measurable problem, not just a rubric problem. This creates a path to moderation, reviewer calibration, and TA selection using data.
- **Source:** `blog/posts/2024/the-psychology-of-peer-reviews.md`
- **Importance:** 67%
- **Novelty:** 81%

### 37. Verified open-source contribution as coursework

- **Description:** One project task requires students to make a small, genuinely useful pull request to a public GitHub repository with meaningful real-world visibility, and then prove that it was merged and authored by them.
- **Nature of impact:** Authentic assessment; industry/public contribution.
- **Why it matters to IITM:** This turns assessment into externally validated work instead of an inward-looking academic artifact. It also teaches etiquette, scoping, review readiness, and real contribution quality.
- **Source:** `til/tds-jan-2026.md`; `exam/src/exam-tds-2026-01-p1.js`; `exam/src/q-pr-merge-server.js`
- **Importance:** 76%
- **Novelty:** 86%

## Adjacent AI/LLM innovations with strong educational transfer

A second-pass scan surfaced adjacent innovations from non-education AI/LLM posts, talks, and tooling experiments. They are not all classroom deployments yet, but they clearly shape the direction of your educational practice and are relevant to IITM's governance choices.

### 38. Taste/judgment is treated as an explicit AI-era learning objective

- **Description:** You frame judgment and taste as the skill AI makes more valuable, and propose concrete practices to build it: argument mapping, perceptual learning, expert prediction audits, peer critique against a goal, and a four-way heuristic for AI-eroded skills: enforce, level-up, switch, or accept.
- **Nature of impact:** Curriculum design; judgment training.
- **Why it matters to IITM:** This gives academic governance a principled way to decide which human skills should still be drilled, which should evolve upward, and which can safely be delegated.
- **Source:** `blog/posts/2026/how-to-develop-taste.md`
- **Importance:** 86%
- **Novelty:** 85%

### 39. Specifications, briefs, and acceptance tests become the assessment contract

- **Description:** Instead of treating code or output as the main artifact, you increasingly treat a machine-readable brief or SOP - goal, context, constraints, done-when, examples, counter-examples, and eval or test suite - as the primary product. Code becomes a build artifact.
- **Nature of impact:** Assessment design; agentic workflow pedagogy.
- **Why it matters to IITM:** This rewrites what counts as "the answer" in AI-native coursework and reduces ambiguity in grading, appeals, and student execution.
- **Source:** `2025-08-21-ai-coding-guide/README.md`; `2025-09-llm-workflows/README.md`; `2025-11-15-applied-vibe-coding/README.md`
- **Importance:** 91%
- **Novelty:** 90%

### 40. Tiered human-in-the-loop governance (green/amber/red) for scaled AI assessment

- **Description:** You propose labeling steps or question types by blast radius: green auto-ships, amber is sampled or spot-checked, red is always human-reviewed. This is the governance architecture for large-scale AI grading and support.
- **Nature of impact:** Governance architecture; risk management.
- **Why it matters to IITM:** It offers a Senate-friendly way to automate safely at scale instead of forcing a false choice between full automation and full manual review.
- **Source:** `2025-09-llm-workflows/README.md`; `blog/posts/2025/the-non-obvious-impact-of-reasoning-defaults.md`
- **Importance:** 87%
- **Novelty:** 91%

### 41. Reasoning models become verification infrastructure, not just answer engines

- **Description:** Your experiments show that increasing reasoning effort on a small model can flip an evaluator from sloppy to reliable, at extra token and time cost. This suggests a cost-aware pattern: cheap screening first, reasoning-backed verification for borderline or high-stakes cases.
- **Nature of impact:** Evaluation economics; grading infrastructure.
- **Why it matters to IITM:** It changes how an institution should budget and design AI evaluation at scale, especially when accuracy matters more than raw throughput.
- **Source:** `blog/posts/2025/the-non-obvious-impact-of-reasoning-defaults.md`; `blog/posts/2026/when-llm-prices-fall-10x-every-year.md`
- **Importance:** 83%
- **Novelty:** 90%

### 42. Semantic plagiarism triage with MinHash and AST cleanup

- **Description:** You are not relying on raw string matching. You strip docstrings, tokenize code, build shingles, and use MinHash or Jaccard similarity to surface suspiciously similar submissions for follow-up.
- **Nature of impact:** Integrity analytics; plagiarism triage.
- **Why it matters to IITM:** This is more robust than obvious copy detection and more scalable than manual review, especially when students try to disguise copied code cosmetically.
- **Source:** `exam/src/tds/project-1/similarity.py`
- **Importance:** 84%
- **Novelty:** 86%

### 43. Workflow orchestration briefs are themselves graded artifacts

- **Description:** Some newer tasks ask students not just to produce an answer, but to specify a multi-step agent workflow: datasets, stages, prompts, tools, quality checks, and delivery formats, in machine-readable JSON.
- **Nature of impact:** Agentic assessment; workflow design.
- **Why it matters to IITM:** This measures whether students can design reliable AI-assisted work, not just benefit from it.
- **Source:** `exam/src/q-vibe-analysis-autopilot.js`; `2025-09-llm-workflows/README.md`
- **Importance:** 82%
- **Novelty:** 90%

### 44. AI-mediated reading modes and re-authoring for personalized study

- **Description:** You use AI to summarize books, fact-check claims, compare multiple books, and re-author dense prose in more engaging styles. One text becomes many possible study experiences.
- **Nature of impact:** Self-directed learning; reading pedagogy.
- **Why it matters to IITM:** This points toward a future where reading lists and textbooks become adaptive interfaces rather than fixed artifacts.
- **Source:** `blog/posts/2026/new-ways-of-reading-books.md`
- **Importance:** 75%
- **Novelty:** 87%

### 45. Policy documents become executable rules for academic governance

- **Description:** Policies, rubrics, and institutional rules can be translated into machine-executable checks, so compliance is not just interpreted manually but verified automatically and audibly at scale.
- **Nature of impact:** Governance automation; policy enforcement.
- **Why it matters to IITM:** This offers a path from Senate-approved policy to consistent implementation across thousands of submissions, workflows, or approvals.
- **Source:** `2025-09-22-llm-trends/README.md`; `2025-12-05-scdm-keynote/README.md`; `2025-11-13-nirmal-impress-ai-hr/README.md`
- **Importance:** 82%
- **Novelty:** 88%

### 46. Retrieval-first institutional memory with canonical Q&A cards

- **Description:** Instead of letting answers live in experts' heads or stale wikis, recurring questions are converted into canonical Q&A cards with source links, owner, freshness date, and retriever-friendly chunks that both humans and agents can cite.
- **Nature of impact:** Knowledge infrastructure; support consistency.
- **Why it matters to IITM:** This is a scalable foundation for student support, faculty enablement, and consistent policy interpretation across large programmes.
- **Source:** `2025-09-llm-workflows/README.md`
- **Importance:** 81%
- **Novelty:** 84%

### 47. Shadow-mode and canary rollout for AI academic workflows

- **Description:** New AI graders, bots, or support workflows are first run in shadow mode or on a tiny canary slice with synthetic data, kill-switches, and rollbacks, so the institution can learn safely before full deployment.
- **Nature of impact:** Deployment governance; operational risk control.
- **Why it matters to IITM:** This is a practical mechanism for introducing AI into high-stakes academic settings without reckless all-at-once launches.
- **Source:** `2025-09-llm-workflows/README.md`
- **Importance:** 80%
- **Novelty:** 86%

### 48. Faculty and staff learn to manage agents, not just use tools

- **Description:** Short, role-specific training on writing specs, setting budgets, adding kill-switches, and defining escalation rules turns non-specialists into competent supervisors of agentic workflows.
- **Nature of impact:** Faculty development; operational capability-building.
- **Why it matters to IITM:** If AI is to be institutionalized, faculty and administrators need orchestration literacy, not just exposure to chatbots.
- **Source:** `2025-09-llm-workflows/README.md`; `2025-11-13-nirmal-impress-ai-hr/README.md`
- **Importance:** 78%
- **Novelty:** 82%

### 49. Vibe coding expands interactive pedagogy beyond technical disciplines

- **Description:** Non-technical staff and students can use AI to build interactive timelines, maps, biographies, and other learning artifacts for humanities and social-science subjects. The limiting factor becomes imagination, not coding ability.
- **Nature of impact:** Curriculum expansion; interdisciplinary pedagogy.
- **Why it matters to IITM:** This extends AI-native pedagogy beyond CS and data science into humanities, social sciences, and foundational courses.
- **Source:** `2026-02-26-vibe-coding-for-humanities-ashoka/transcript.md`
- **Importance:** 79%
- **Novelty:** 85%

### 50. Parallel LLM execution becomes a teachable learning strategy

- **Description:** Learners are encouraged to run multiple prompts, models, or tasks in parallel to sample more ideas, compare approaches, and converge faster instead of waiting on one sequential path.
- **Nature of impact:** Meta-skill; workflow pedagogy.
- **Why it matters to IITM:** This teaches an AI-native way of working: portfolio thinking, faster exploration, and explicit comparison across models and solutions.
- **Source:** `2025-10-29-llm-data-visualization/README.md`; `2026-02-26-vibe-coding-for-humanities-ashoka/transcript.md`; `2025-11-15-applied-vibe-coding/README.md`
- **Importance:** 75%
- **Novelty:** 79%

## Summary table

| Innovation | Importance (0-100%) | Novelty (0-100%) |
| --- | ---: | ---: |
| Question-only, prompt-first curriculum ("There is no course content") | 98% | 93% |
| "Ask AI" embedded inside every question, with model choice | 97% | 95% |
| LLM-based project grading with granular rubrics and explanation-first judging | 96% | 94% |
| Copying, collaboration, and even hacking are made part of the curriculum | 95% | 92% |
| The curriculum is being redesigned around what AI still does badly | 94% | 82% |
| Dynamic seeded personalization with server-side validation | 94% | 89% |
| Live LLM API evaluation and hands-on LLM competency batteries | 93% | 94% |
| Test cases are being reconceived as automated tutors, not just graders | 93% | 92% |
| Hard, ambiguous, hackable, beyond-syllabus problems are used deliberately | 91% | 88% |
| Specifications, briefs, and acceptance tests become the assessment contract | 91% | 90% |
| Repo-grounded AI viva with follow-up code-change checks | 90% | 91% |
| Adversarial prompt security is taught as an assessable skill | 89% | 96% |
| Diagnostic-first teaching: assess first, teach from the errors | 88% | 81% |
| AI-generated assessment content with self-testing and self-correction | 88% | 95% |
| AI as the first-line TA, humans for exceptions, trust, and judgment | 88% | 83% |
| AI Pipe / budgeted proxy access for all students | 87% | 89% |
| Tiered human-in-the-loop governance (green/amber/red) for scaled AI assessment | 87% | 91% |
| AI-use telemetry and model-vs-score analytics inside live assessments | 86% | 93% |
| Taste/judgment is treated as an explicit AI-era learning objective | 86% | 85% |
| Cross-course AI-assisted learning analytics as a research programme | 85% | 88% |
| Coding agents are used to QA exams and expose the real skill being tested | 84% | 92% |
| Semantic plagiarism triage with MinHash and AST cleanup | 84% | 86% |
| Virtual TA / chatbot as both student tool and student-built artifact | 84% | 86% |
| Mining code snapshots and practice data for misconception patterns | 84% | 88% |
| Game-playing agents are turned into learning tasks | 83% | 90% |
| Fault-tolerant AST parsing for broken student code | 83% | 91% |
| Reasoning models become verification infrastructure, not just answer engines | 83% | 90% |
| Policy documents become executable rules for academic governance | 82% | 88% |
| Transparent multi-scheme scoring for adversarial and open-ended tasks | 82% | 90% |
| Workflow orchestration briefs are themselves graded artifacts | 82% | 90% |
| Retrieval-first institutional memory with canonical Q&A cards | 81% | 84% |
| Personalized skill clustering and short next-step feedback | 81% | 74% |
| Shadow-mode and canary rollout for AI academic workflows | 80% | 86% |
| Teacher-first AI adoption through familiar formats | 80% | 76% |
| Vibe coding expands interactive pedagogy beyond technical disciplines | 79% | 85% |
| Multimodal and open-ended AI evaluation with vision models, embeddings, and Promptfoo | 79% | 94% |
| Faculty and staff learn to manage agents, not just use tools | 78% | 82% |
| Execution logs, verification notes, and terminal recordings as assessment evidence | 78% | 89% |
| The course is public and auditable outside IITM | 78% | 70% |
| Data-driven exam strategy and deadline analytics | 77% | 84% |
| Verified open-source contribution as coursework | 76% | 86% |
| Parallel LLM execution becomes a teachable learning strategy | 75% | 79% |
| AI-mediated reading modes and re-authoring for personalized study | 75% | 87% |
| Interactive explainers are used as a new teaching medium | 74% | 78% |
| AI-generated comics explain why each question exists | 72% | 84% |
| Directional feedback for AI as a teachable meta-skill | 71% | 83% |
| Cohort-level originality / diversity scoring with embeddings | 71% | 95% |
| Personalized AI learning coach / research coach | 69% | 73% |
| LLM-based fact-checking of textbooks and curriculum claims | 68% | 77% |
| Peer-review analytics to diagnose evaluator personas | 67% | 81% |

## Bottom line

If I had to compress the whole story for the Council into one sentence, it would be this:

> You are not merely adding AI tools to an existing course. You are systematically redesigning **curriculum, assessment, support, integrity, and educational research** around the reality that AI is now part of the learning environment.

The strongest institutional themes are:

1. **Shift the unit of assessment** from unaided recall to AI-assisted problem solving plus verification.
2. **Make AI use visible and governable** instead of pretending it can be kept out.
3. **Use AI to scale feedback and support**, but keep humans for judgment and ambiguity.
4. **Exploit academic exhaust as a research asset** - especially at IITM's scale.
5. **Treat access, cost, transparency, and approval pathways as first-class design constraints**.

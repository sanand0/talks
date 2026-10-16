# Build prompt — 12 October 2026 TDS course ideation

<!--
cd ~/code/talks/
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

<!-- https://chatgpt.com/c/6acd9515-6558-83ec-91d0-45c909bec4f8 -->

Create an ambitious, memorable, **evidence-grounded narrative story** as a static page at **2026-10-12-tds-ideation/index.html**. Use the **talk-story** skill and any relevant storytelling, visual-design, interaction, and testing skills. The source is an unusual **open course-design meeting** for [IIT Madras Tools in Data Science](https://tds.s-anand.net/), not a prepared lecture. Students were allowed to watch the instructors invent future graded assignments and projects in real time — and then challenge the teachers.

The story should let an educator, curriculum designer, student, or AI practitioner understand **how the TDS team decides WHAT to teach, HOW to teach it when agents can already do the task, and HOW to know if the student learned anything**. Treat this as an honest working experiment, not an advertisement for the course or a list of innovative project ideas.

**Core tension**: When we permit strong agents and collaboration, an easily solved problem may teach little. But making problems arbitrarily hard, uniquely personal, or hard to grade is no solution either. We're trying to design *real work that agents help with, but cannot trivially complete without the student developing transferable ability*, under fair, scalable, verifiable assessment.

## Read the evidence in this order

1. **transcript.md**, here. Ground truth for who said what, when, and what remained *ideas* rather than decisions. The transcription has errors; check uncertain attribution or quotes against the audio. At ~49:59, a non-dialogue summary paragraph inserted by transcription is **not something anyone said**.
2. **story-context.md**, here. Deliberately prepared narrative, cast, timestamp anchors, local context, tensions, suggestions, privacy guardrails. **Not a mandatory outline.**
3. **research-notes.md**, here. Primary research, supporting and contradictory evidence, caveats, recommendations for nuanced public claims. Treat it as a research shelf; select what strengthens the argument rather than dumping a bibliography into the article.
4. **links.md**, here. Grounded public links, local research paths, asset status, optional visuals and embeds.
5. The course's live September 2026 pages: [course](https://tds.s-anand.net/), [GA0](https://exam.sanand.workers.dev/tds-2026-09-ga0), and the source in ~/code/tools-in-data-science-public/2026-09/. The exam engine is in ~/code/exam/; read README.md, questions.md, relevant questions, and selected difficulty results **but do not leak nonpublic exam keys, credentials, solutions, student data or anti-cheat mechanisms**.
6. Earlier published work, especially [the 5 Oct TDS orientation](../2026-10-05-tds-orientation/) (prompts.md, story-context.md, index.html), [the 10 Aug TDS AMA](../2026-08-10-tds-ama/), [Let AI Take Your Exams](../2026-06-12-let-ai-take-your-exams/), and [How I use AI to teach](https://www.s-anand.net/blog/how-i-use-ai-to-teach/). Tell readers what the *12 Oct design room* adds beyond the earlier student-facing explanation.

**Video is present:** the local master is `~/r2/media/2026-10-12-tds-course-ideation.webm` (69 minutes, 1280×720 AV1 video, Opus audio, embedded WebVTT subtitles); the corresponding public recording is **https://media.s-anand.net/2026-10-12-tds-course-ideation.webm** (check availability before publishing). Claude may inspect the local recording freely for context, full-resolution screenshots, original screens, caption verification, quotes, speaker attribution and accurate timestamp links. The existing `2026-10-12-tds-ideation.opus` is an optional audio alternative, with intended release URL https://github.com/sanand0/talks/releases/download/talks/2026-10-12-tds-ideation.opus. The separately mentioned `.opus` link at media.s-anand.net is audio, not the video. Prefer **video-first** storytelling, not audio-first.

**`comic-page.avif` is present.** Feature the existing eight-panel comic prominently, with full-size viewing and useful alt text. Its generation chat is https://chatgpt.com/c/6acd97a9-9f98-83ec-850a-31311af92ca3 — preserve that as **authoring provenance**, not a public story link. The comic interprets the meeting's ideas; the video is evidence of what happened.

**Design reference:** Inspect both `../2026-10-05-tds-orientation/index.html` and `../2026-10-07-iitm-ed-data-visualization/index.html`, and their prompts. They are the latest successful **video-oriented** summaries: story/video focus toggle, persistent playback while toggling, in-story timestamp navigation, deep-linking, section/player synchronization, transcript access, responsive behavior. Keep that interaction quality and general reading experience; **Claude has full discretion** over headline, story arc, layout, typography, color, visuals and effects. These notes are ideas, **not a wireframe**.

## Editorial challenge

Choose a **single story**, not a transcript replay or a catalog of 8 question types. Aim for a strong human-centered hook, a problem, attempts to solve it, student pushback, a consequential rethink, and an ending that leaves a useful design test in the reader's hands. Use the meeting's actual voices and their uncertainty. A promising cold open: a student at **51:05** asks to collapse completed questions; Anand immediately instructs ChatGPT to modify the exam portal, only to have that student at **66:06** show a Tangram that *looks* correct yet fails validation. Do not claim the game has a verified bug; the transcript proves only that the student reported a failure. A second possible open: at **03:54**, the team tries to design questions that sharing an answer, sharing a solver, and delegating to an agent will not trivially defeat.

Find an arc more incisive than “here are our ideas,” for example:

- **What are we really examining?** The inversion: agents and peer help are welcome, but the student should develop skill; JK adds metacognition, making tacit requirements explicit and learning how they learned.
- **Change the shape of the task, not the intelligence of the solver.** Distributed invoices introduce *information asymmetry, discovery, negotiations, holdouts, incentives*. Prediction markets force *making and updating forecasts* but also tempt manipulation. Unusual correct answers target *search beyond the obvious* but risk turning novelty into a gimmick.
- **Let students and inconvenient reality audit the teachers.** Shreenish asks “what does the grader check?”, teaches the team a usability improvement, points out brute-forceable questions, and finally shows Tangram's precision problem. Good design must survive actual students, actual agents, actual accessibility, and its own grader.
- **The next exam is a hypothesis.** We don't have experimental evidence that each idea teaches its claimed skill. Invite readers to assess and improve the specification, grading, fairness, and transfer of learning.

These are possible beats, **not prescribed sections or a wireframe**. If you discover a better arc, use it. The reader should finish with a reusable **assessment design protocol** (intended skill → task → adversarial agent/student trial → reliable grading → evidence of transfer), not merely the conclusion that the team is creative.

## Key moments to earn

- **01:09**: “an internal ideation meeting you happen to be listening in on.”
- **03:17–07:53**: strong agents allowed; sharing answers/solvers should not shortcut learning; 6 tests; identity, interaction, ground truth, originality, external tools, budget, verification. JK adds **metacognition**.
- **09:44–12:16**: if agents can build software, the capability moves toward **specifying unstated requirements** and learning from usage/errors.
- **13:12–20:14**: distributed invoices. JK recommends revealing the network; Anand worries it would destroy an opportunity for **self-organization**. Rate limits, hidden information, partial cooperation and holdouts make the task interesting; no finished spec was adopted.
- **20:14–26:28**: a prediction market for AI Pipe token spend. Forecast updates, dashboards, possible student experts; distinguish forecasting uncertain external outcomes from **controlling the measured outcome**. Market design is an open risk.
- **27:07–33:24**: counterexamples, Calvin & Hobbes's impossible-looking Scrabble score, BBC Pointless, rewarding **correct unusual answers**. The author published a [11 Oct 2026 reconstruction](https://www.s-anand.net/blog/calvin-957-in-scrabble/) with an [interactive replay](https://files.s-anand.net/blog/2026-01-11-calvin-957-in-scrabble/how-calvin-got-957.html). It uses a bottomless tile supply and an evolving invented dictionary: a playful, inspectable rule-bending construction, **not a standard legal Scrabble game**. Its score is not independently verified here. Do not reproduce the copyrighted comic panel without permission.
- **34:15–37:24**: physical/social coordination over Meet, webRTC, possible wearable; an idea for a later project, not an assignment.
- **39:28–43:51**: Shreenish asks *what will students learn?* and *what will you measure?* Anand reaches for an auditor's error model. Keep this exchange; it turns philosophy into assessment validity.
- **44:12–50:26**: the proposals are **undecided**; students can influence what teachers build; instructors admit limited expertise, and invite collaboration.
- **51:05–53:44**: student-requested UI improvement, instructor delegates to an agent in real time. Don't claim the change was fully tested/deployed during the call.
- **55:00–60:10**: Android Debug Bridge and mobile agents; a compelling example of the **environment boundary moving**. Unikernels and app-store policy remarks are speculative as described in research-notes.md; keep peripheral.
- **61:02–68:58**: criticism of a brute-forceable answer, debate on grade distributions, Tangram near-match, student using GitHub/Vercel integration, and Carlton encouraging browser MCP. Do not endorse a “normal/bimodal score distribution proves fairness” claim, and do not assert the silhouette is correctly scored from visual similarity alone.

**Preserve the contradictions** rather than ironing them out: collaborate openly / don't reward answer swapping; harder questions / avoid pointless friction; identity as a useful constraint / deepfake and accessibility risks; novelty / correctness; autonomous agents / evidence of human learning; public ideation / stable announced marking rules; scalable automatic checking / quality and appeal of validators; economically useful market data / students changing its value; sharing expertise / free-rider and unequal access.

## Evidence is part of the narrative

Research both in favor of and against the course's choices. Particular **load-bearing** contrasts:

- Active learning can improve learning outcomes, but **completion ≠ learning**; unguarded AI tutoring can raise assisted performance and lower later unassisted scores ([PNAS 2025](https://doi.org/10.1073/pnas.2422633122)). A TDS-style course could instead test *transfer*: a later novel task with changed tools, data and constraints, not just a correct submission.
- Training metacognition and reflection has a defensible basis, though students' self-reports alone aren't proof ([National Academies](https://www.nationalacademies.org/read/24783/chapter/6)).
- Prediction markets can combine dispersed information, yet **target manipulation** is a vulnerability, especially if the very students deciding token spend can also change it ([2025 field experiment](https://arxiv.org/abs/2503.03312), [2026 settlement manipulation](https://arxiv.org/abs/2606.31675)). If teaching *influence* is intentional, distinguish it from a pure prediction exercise.
- AI-generated ideas may increase individuals' output while reducing diversity among outputs ([Science Advances](https://doi.org/10.1126/sciadv.adn5290)), but originality-only scoring can be gamed, punished by cohort behavior, or confused with usefulness.
- Fairness and validity depend on **what a score measures and for whom**, not whether the histogram is normal or bimodal ([NCME classroom assessment standards](https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/)).
- Voice/video identity is not an “agent-proof” guarantee ([NIST digital injection and forged media](https://pages.nist.gov/800-63-4/sp800-63a/ial-general/)).

Link to specific primary sources in context. Distinguish: (1) witnessed statement; (2) external finding; (3) our inference; (4) proposed next design experiment. Don't invent student outcomes, teacher intentions, dates, project release status, empirical comparisons, or a hidden technical diagnosis. Attribute anecdotes as anecdotes. Don't reproduce any private messages or expose identifying student IDs or data.

## Experience goals; choose the design yourself

Use the **story ↔ video** interaction from both `../2026-10-05-tds-orientation/index.html` and `../2026-10-07-iitm-ed-data-visualization/index.html` as functional references. Let the story lead by default; the video should become prominent on demand **without remounting or losing playback**. Timestamp links (e.g. ▶ 39:28) should seek and play the same player, be shareable via URL, survive browser back/forward, and work with keyboard/touch. Make transcripts accessible without an unreadable giant modal; no autoplay. Verify seek offsets against the actual media.

Use **concrete, meaningful visual changes in rhythm**, ideally after one or two prose passages: a live-ish sample assessment, the six design tests, the fork in invoice-network design (tell students where data is vs let them discover it), an information-trading network, a market forecast that changes, a rare-vs-correct originality test, or a “will this grade fairly?” audit. These are possibilities. Do **not** display invented data as actual TDS/student results; label fixtures explicitly as hypothetical. Interactive components must teach something and behave correctly, not become ornamental dashboards.

Provide readers with substantive, not decorative, public links to the real [course](https://tds.s-anand.net/), [exam](https://exam.sanand.workers.dev/tds-2026-09-ga0), [research](research-notes.md), earlier talks and primary evidence. External embedded pages only if they actually load; otherwise create an accessible preview/link. Avoid hotlinking copyrighted panels, private portals, student PII or unreleased assessment internals.

The site must work with narrow viewports, screen readers, reduced motion, visible focus, accessible contrast, and no horizontal overflow. Link transcript and source trail. Favor one thoughtfully crafted experience over a sea of generic cards. Use timestamps accurately and keep quotations short and faithful.

## Publication and QA

This prompt requests **creation of index.html later**, not changes to the course or exam themselves. At build time inspect the repository's instructions and scripts, then run appropriate smoke tests (keyboard, mobile, timestamps, deep-links, history, video seek/playback, comic lightbox, optional audio fallback, accessibility). Check actual availability and MIME of URLs. Test the actual WebM URL and playback; if the public URL is not live, report it rather than silently substituting a guessed source. Use local video screenshots when they add authentic evidence. Preserve existing nonlocal work.

Do not publish private repo links or hidden exam internals; the course content and exam **portals** are public. If an additional image/movie or research artifact is absent, adapt rather than invent it.

Suggested catalog entry after publishing:

- **Date:** 12 Oct 2026
- **Event:** TDS Course Ideation — Open Design Meeting, Sep 2026 cohort
- **Location:** Remote
- **Working title:** *How Do You Set an Exam When AI Can Take It?* (feel free to improve)
- **Details:** Inside an open TDS course-design meeting: the instructors invent agent-friendly assessments, students challenge the rubrics, and the distinction between getting work done and learning becomes the hardest test.
- **Transcript:** transcript.md
- **Video:** https://media.s-anand.net/2026-10-12-tds-course-ideation.webm ; local source `~/r2/media/2026-10-12-tds-course-ideation.webm`.
- **Audio:** optional existing Opus file/release.
- **Comic:** present `comic-page.avif`; provenance https://chatgpt.com/c/6acd97a9-9f98-83ec-850a-31311af92ca3 (keep this private).
- **Public URL after deployment:** https://talks.s-anand.net/2026-10-12-tds-ideation/

---

What would you say are the core principles of teaching and design questions that teach a relevant and useful skill even when students can (and are encouraged to) work with AI agents as well as each other? I'd like to publish this in my blog, so follow the writing style in ~/code/blog/ but save it in 2026-10-12-tds-ideation/blog.md

<!-- claude --resume 5b031da9-0f5e-4dd1-ac6c-67220d7b459b -->

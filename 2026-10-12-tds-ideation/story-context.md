# Story context — 12 October 2026 TDS open course ideation

An editorial map for the future static story. **The transcript and the full local video, including screen shares and embedded captions, govern what happened.** These are interpretations and story opportunities, not a screenplay to follow.

## One-paragraph setup

On Monday 12 October 2026, the [Tools in Data Science](https://tds.s-anand.net/) team at IIT Madras opened what was ordinarily its internal exam-design meeting to students. Anand, JK, Hritik, Carlton and other TAs worked out loud on future GAs, projects and an ROE: how do you grade students at scale when they're **allowed — even encouraged — to deploy powerful agents and ask their peers for help?** Instead of lecturing on AI, they were inventing an exam that ought to make *using* AI educational. Student Shreenish then did what the course asks students to do: challenged the specification, proposed a product fix, and questioned a validator's result. The result is a candid view of the gap between **pedagogical aspiration and a working assessment**.

**This is not a published specification for Project 1.** At 44:12 and 45:30 the team explicitly said it was still open to alternatives and would revisit it on Wednesday. The hypothetical invoice distribution, token market, physical collaboration task, and prompt-diversity question were ideas, not commitments. The course/project files may have been updated since; show the meeting's then-current status and separately date later changes if mentioning them.

## The thesis

**Don't ask whether an agent can finish the exam. Ask what the student learns by making it finish.**

But that is only half the thesis: a task with clever constraints can become a hoop-jumping competition. A legitimate exam needs evidence that the student's *own capability* changes and transfers beyond that one task. The lasting question is **what the human learns to specify, source, coordinate, investigate, predict, adapt, verify and explain**, and how the team can fairly detect that with cheap automated grading.

What this meeting adds to the [5 October orientation](../2026-10-05-tds-orientation/): orientation told students “Do real work with tools, agents and people — and verify it.” This meeting shows **how the teachers try to make that operational**, how easily an idea breaks under grader constraints, and why the students themselves are part of designing the course.

## Four-beat story candidate

### 1. An exam whose solver is welcome

Anand begins at [01:09] explaining that students have entered an internal ideation meeting. At [03:17–04:47], he lays out the design challenge: assume agents and collaboration, don't forbid them. Ask whether the problem teaches a real skill; whether copied answers fail; whether a shared solver alone fails; whether a standalone agent trivially does the whole thing; whether gaming the task teaches something or costs more than solving; whether scoring is cheap and robust. The “roughly half the students” accuracy target is his *working heuristic*, not an empirically established universal optimum.

JK's [07:53] addition is quietly more important than another category of question: can the student describe **how they learned** and reuse it? At [10:49–11:43], he raises *hidden requirements*: a person who asks for “a PDF editor” hasn't specified signatures, privacy, imports, editing, or accessibility; the skill is making tacit needs explicit. This is a stronger lasting learning objective than “learn to prompt.”

Useful graphic: two paths, **Answer / Solver / Agent** versus **A new capability in the learner**. The first can all succeed while the second fails. Don't render it as proven from TDS data; it is a design hypothesis, tested externally by the AI tutoring literature.

### 2. A weird exam is an interface to real work

Three assessment ideas, each a different **failure of the agent-alone interface**, NOT evidence that AI itself lacks intelligence:

**A. Trade information [13:12–20:14].** Clients have invoices scattered among students. Students need documents that other students control. In the conversation, Anand suggested roughly 50,000 invoices/1,000 clients, later paraphrased 100 invoices per 1,000 clients; these are **brainstorming quantities, not fixed dataset specifications**, and they are not consistent across retellings. Instead of pretending the exact count matters, visualize each student's *missing pieces* and the network of holders.

JK wants to provide clues about which nodes contain the most information. Anand resists because giving a ready-made map removes the need to self-organize. He imagines 20% who don't participate — again **an illustrative scenario, not a measured 20% attrition rate** — and a potential cost/rate limit on retrieving invoices. The implied transferable skills: information discovery, data quality, bargaining, documenting provenance, coping with holdouts and redundancy, designing processes with incomplete information. Risk: students share all files in one folder and trivialize the interaction; artificial rate limits may be unproductive friction. A good author will make the choice between **useful scaffolding** and **giving away the work** vivid.

**B. Predict token spend [20:14–26:28].** AI Pipe use would be a visible daily ticker. Students might buy and sell claims about its future aggregate spend, perhaps consult working professionals or superforecasters. The team hopes to teach forecasting with updated information, not just stock-picking. But they explicitly notice that students may also *cause* spend to change. That makes this partly a coordination/market-manipulation task. Neither the pricing mechanism nor payout, settlement, gaming limits, or ethics were settled in the call. A good story makes the distinction between **forecasting an event** and **changing an event while betting on it** apparent.

**C. Find a correct but rare answer [27:07–33:24].** A Calvin & Hobbes Scrabble puzzle and the BBC quiz *Pointless* inspire a question where a valid answer also has to differ from others. This could train systematic counterexample search and exploration off the default response path. Beware the imprecise line “LLMs generate the average of human knowledge.” The research supports **homogenization under some settings**, not a claim that LLMs literally compute the average or cannot be original. Compare **correctness → distinctiveness**; without the first, novelty isn't useful. Penalizing duplicate answers may reward secrecy and punish independently discovered truths.

The physical Meet/creative-art idea [34:15–37:24] and mobile agents [55:00–60:10] are evocative further horizons, but probably sidebars, not four extra sections. They frame **changing interfaces**: when the agent gets browser, device, mail, terminal, camera or real-world access, last week's “human-only” problem can become automatable.

### 3. The student interrupts the curriculum designer

At [39:28] Shreenish asks for the learning outcome. At [42:29] he asks for assessment criteria. Anand proposes an **auditor-like loss function** for the scattered invoices: penalize missing entries by count and value, perhaps other factors. This is *a candidate rubric*, not a finished fair grader. Shreenish essentially says he'll evaluate it when the exact spec appears Wednesday. This is the story's hinge: **vague innovation is easy; a verifiable specification is much harder**.

At [44:12] Hritik says clearly Project 1 is not settled. At [48:32] Anand shares why students are allowed in: the instructors' ignorance in a fast-changing field, and students' ability to help shape the work. Carlton [50:26] is explicit that the session only works if students use the chance to speak. This is an example of **co-design** rather than a polished instructor-led plan.

Then [51:05] Shreenish proposes collapsing completed questions in the exam portal. Anand [51:52] starts giving an agent a concrete implementation/QA request while screen sharing. This enactment is gold: the teachers themselves live the “specify, delegate, verify” model. In the transcript we **do not see a verified successful deployment**. Do not make the page say he shipped the fix in class; link to the idea and show it as a live design handoff.

### 4. The exam should pass its own exam

At [61:02] Shreenish says a GA0 numerical answer could be found by brute force. Carlton says some entry-level questions are intentionally easy and reused GA0 to get a baseline on possible knowledge transfer. His statement that a “normal or bimodal” score distribution means an exam is roughly fair [64:41] is **not a valid standalone inference**. A score distribution alone doesn't establish validity, fairness or learning; it cannot show transfer from earlier cohorts without stronger controls.

At [66:06–68:58] Shreenish screen shares a Tangram silhouette that *looks* like the target but whose submitted arrangement is rejected. Carlton attributes it to likely geometric precision and advises using an agent/browser MCP. The transcript does not prove why the particular attempt failed. The incident nevertheless perfectly illustrates the test designers' dilemma: **how do we tell apart an imperfect submission, an invisible tolerance violation, an inaccessible tool, and an incorrect judge?** The exam's scoring code and/or student's exact submitted coordinates are needed before assigning blame. The final exchange [67:41] reveals Shreenish already learned about delegating GitHub/Vercel work to connected tools. That's one genuine, self-reported example of changed workflow, **not proof of long-term transfer**.

Possible ending: **“Design an exam that survives its own examiner.”** Ask readers to choose a skill, draft one agent-allowed question, attempt to defeat it with a strong solver, and explain how they'd independently verify the student's learning rather than just their product.

## The cast: distinct voices, not interchangeable talking heads

- **Anand**, instructor/course designer: proposes principles, dares to leave parts undefined, experiments while teaching, open about uncertainty, returns to cheap graders and authentic outcomes.
- **JK**, course administrator/design partner: metacognition, tacit requirements, useful clues to distributed info, prediction-market infrastructure, using the learners' own practical expertise.
- **Hritik**, TA: triggers project conversation; observes that smaller teams can now build impressive software; cautions [44:12] that Project 1 isn't settled.
- **Mayank and Jaideep**, TAs: Mayank wants specifics before judging invoice design; Jaideep shares mobile-device control with USB debugging, expanding possible future tasks.
- **Carlton**, instructor: gives students a real voice, polls their trading expertise, describes real grading/administrative tensions, and handles Tangram questions. Don't interpret a shaky connection as a character flaw.
- **Shreenish**, student: asks the key exam-design questions, suggests the portal improvement, challenges brute-forceable questions, shows the Tangram discrepancy, illustrates finding new agent tool integrations.

Voice confidence: check audio for uncertain “Unsure” turns, for odd model names “Jeb/Jev”, “PDFcraft/Artcraft”, and for the exact phrasing of the Tangram reply. The transcribed interstitial at ~49:59 (“This call recording features …”) is an auto-generated **editorial insertion** and not dialogue.

## Moment anchors (audio time)

| Time | What to seek | Why it matters |
|---|---|---|
| 01:09 | You're inside an internal ideation meeting | Sets unusual openness |
| 03:17 | Agents and sharing are allowed | Changes the question-setting problem |
| 03:54 | Six tests of a good question | Strong compact visual |
| 05:08 | Identity, interaction, personal data, uniqueness | Pattern generator |
| 07:53 | JK proposes metacognition | What counts as learning |
| 09:44 | From software building to software specification | Durable need |
| 11:43 | “Make implicit explicit” | Transferable skill |
| 13:12 | Invoices held by other students | Interactive/distributed data scene |
| 16:22 | JK suggests high-value network nodes | Scaffold vs discovery |
| 17:31 | Don't tell students where all data is | Self-organization tension |
| 20:14 | Prediction market for token consumption | Forecast/update |
| 23:44 | Prediction markets as a reusable pattern | Generalization |
| 27:07 | Counterexamples/search | Broadens what “creative” means |
| 28:19 | Calvin & Hobbes Scrabble inspiration | Memorable human anecdote |
| 30:45 | Correct answers distant from the mode | Novelty caveat |
| 34:15 | Physically coordinating through Meet | Boundary of tools |
| 39:28 | What is the learning outcome? | Student reframes meeting |
| 42:29 | How will you grade it? | Turns idea into requirement |
| 44:12 | Project 1 is NOT decided | Mandatory qualification |
| 48:32 | Instructor admits ignorance and invites student ideas | Co-design |
| 51:05 | Student requests UI improvement | Role reversal |
| 51:52 | Anand dictates a change to an agent | Course philosophy enacted |
| 55:00 | Controlling Android via ADB/ChatGPT | Tool interface shifts |
| 61:02 | Brute force GA0 answer | Anticipating gaming |
| 63:25 | Reusing GA0 as a possible transfer baseline | Interpret cautiously |
| 64:41 | Score distribution/fairness claim | Explicit fact-check |
| 66:06 | Tangram visually matches but does not validate | Independent grader dilemma |
| 67:41 | Student discovers ChatGPT–GitHub–Vercel integration | Evidence of a new workflow |
| 68:11 | Browser MCP suggestion | Interfaces change fast |

These are transcript offsets. The **actual video** is at `~/r2/media/2026-10-12-tds-course-ideation.webm` and contains original screen shares and subtitles. Spot-checked frames show the **six-test checklist actually written in VS Code near 03:45**, the **Calvin & Hobbes source on screen around 29:10**, and the **real student exam-portal submission screen around 66:07**. Extract precise, legible frames where they clarify the story. Don't assert the Tangram is geometrically correct just because it appears close: the exact transform/validator is independent evidence. The video is 4140 seconds long. Test seeking against the actual recording.

## Reusable design tests (teaching heuristic, NOT externally validated doctrine)

| Test | Threat / failure | What a good question does |
|---|---|---|
| Genuine learning | Agent solves; student learns nothing | Reveals changed student choices, diagnoses, or transfer |
| Personalized/real state | Student copies a correct answer | Requires authorized student-specific input without harvesting sensitive data |
| Solver shareability | A reusable script solves every variant | Requires contextual interpretation, uncertainty or legitimate human action |
| Agent-only completion | Full task delegated with zero participation | Makes objective depend on justified specification, access, judgment or reflection |
| Gaming incentives | Students optimize grade, not skill | Reward valid outcomes/decisions, red-team shortcuts; minimize artificial friction |
| Grade reliability | Clever tasks expensive to check | Independent ground truth; deterministic or auditably bounded scorer; appeals and tolerances |
| Inclusion | Resources/identities vary | Low-cost equivalent paths; accommodations; not purchasing-power contests |
| Adaptability | One-off win only | Delayed or altered version to test transfer |

The first six derive from the meeting. The last two are **editorial improvements**, not items Anand said were in the checklist.

## Editorial guardrails and possible surprise

**Best surprise:** Shreenish’s procedural interruption is not a digression. It is the *ideal TDS student behavior*: notice what is broken, articulate a change, wield a powerful tool, test where the system behaves unexpectedly, and challenge the system. But it can also reveal bad pedagogy if interface/precision barriers are unrelated to intended learning. Let both readings coexist.

**An additional story angle: the students are part of the assessment engine.** This is not only an open lesson-planning meeting: Shreenish asks for the learning objective, challenges how it would be graded, proposes an actual interface change, and interrogates a puzzling checker result. A single student behaves as **requirements analyst, user researcher, tester, and learner** while an instructor delegates a UI fix to an agent. The scene sequence makes the abstract loop **specify → delegate → verify → revise** concrete. You can anchor it to the real screen shares (VS Code checklist, original Scrabble website, actual exam portal) rather than inventing slide diagrams. The eight-panel comic already summarizes all the ideas; let video stills provide different, evidentiary value. This is an editorial option, not a required structure.

**A proposed strongest counterargument:** The whole design could end up teaching “how to comply with an opaque, gameable interface” instead of building transferable skills. The response must be **measure transfer and validate graders**, not insist that every difficulty is educational. How would we know six months from now that a student could negotiate a real missing-information problem, make calibrated forecasts, or detect a misleading verifier? No such course-wide controlled evidence exists in these materials.

**Avoid overclaiming:** The invoice market and prediction market are theoretical; the 50% success target is heuristic; a “20% holdout” is an imagined proportion; “identity is agent-proof” is rhetoric; “LLMs generate average knowledge” is shorthand; the [957 Scrabble replay](https://files.s-anand.net/blog/2026-01-11-calvin-957-in-scrabble/how-calvin-got-957.html) is a public creative construction using extra tiles and invented dictionary rules, *not* an ordinary legal Scrabble match, and its scoring has not been independently verified here; model/version and app-store statements near [56:40–59:00] may be garbled or quickly changing; a bimodal grade histogram is not fairness proof; near-looking Tangram isn't necessarily equal geometry.

**Privacy:** Student first names/quotes spoken in a public streamed discussion are part of the recording, but avoid student account IDs, email addresses, identifiers and private ChatGPT conversation links. Never publish private course test keys, hidden answers/validators, direct links to nonpublic source files, WhatsApp exports, specific class contact information, or unreleased project details merely because they're on the development machine. Public course pages and public prototypes may be linked.

## What might make the visuals memorable

- A short selectable **question-design adversarial test**: answer copy, solver copy, autonomous agent, group collaboration, fair grading. A *hypothetical* quiz fixture demonstrates design failures.
- **Invoice-holder network**: click nodes to reveal information, then experience how changing the degree of hints affects search. Diagram is fictional unless backed by a committed exercise.
- **Forecast vs control** two-column interaction: who gets to move the actual AI token spend? What is being measured: calibration, coordination, or gaming?
- A **Pointless** demonstration: validity and rarity in separate columns, with “being uncommon is not enough” as the takeaway.
- A **deliberate grading paradox**: same-looking silhouettes that may differ in coordinates; do not imply these are genuine submitted answers without inspecting the exact data.
- A **teacher ↔ student role switch**: student specifies UI fix, teacher delegates code, both confront validation.
- If a comic appears, let it be the visual overture, not an excuse to repeat the narrative in eight generic cards.

Use one or two of these, not all. The **story is the interface**, not a dashboard of equally-weighted widgets.

## Related public continuity

- [TDS course](https://tds.s-anand.net/)
- [Sep 2026 GA0](https://exam.sanand.workers.dev/tds-2026-09-ga0)
- [5 Oct orientation: Get the Job Done — and Verify It](https://talks.s-anand.net/2026-10-05-tds-orientation/)
- [10 Aug TDS AMA: What Is This Course Really Teaching?](https://talks.s-anand.net/2026-08-10-tds-ama/)
- [12 Jun: Let AI Take Your Exams](https://talks.s-anand.net/2026-06-12-let-ai-take-your-exams/)
- [How I use AI to teach](https://www.s-anand.net/blog/how-i-use-ai-to-teach/)

In the local exam repository, questions.md identifies actual question archetypes (server validators, GitHub deploys, SQL/HTTP tasks) and warns some client-side validators leak answers. dumps/difficulty.md reports a 6 Oct-style 180-submission GA0 snapshot with a **29%–78% range for individual tasks**, but these represent an auditing/public submission sample at one point, not the final academic cohort. Either date and label the data carefully or don't use a numeric chart.

**Publication metadata candidate:** 12 Oct 2026; open TDS course-design meeting, remote; title *How Do You Set an Exam When AI Can Take It?*; duration must be checked from audio; audio-only at draft time.

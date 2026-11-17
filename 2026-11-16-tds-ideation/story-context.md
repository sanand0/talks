# Story context — 16 November 2026 TDS course ideation

Editorial preparation for the next Monday episode. The verbatim source is the roughly **66m54s** recording, transcript.md (including the appended meeting chat), and three local companion ChatGPT exports. These notes distinguish **events in the meeting**, **post-hoc results**, and **unverified pedagogical inferences**. Not a mandatory screenplay.

## The consequential change from earlier Mondays

- **12 Oct:** “The Exam Is a Hypothesis” — imagining assessments after agents can complete tasks.
- **19 Oct:** “The Exam Has to Pass Its Own Exam” — exposing game designs to implementations, verification costs and student ingenuity.
- **2 Nov:** “Should a Student Even Read the Exam?” — identifying human judgment and process when answers are automatable.
- **9 Nov:** “Who Watches the Deadline Watchers?” — live-game mechanics, fast-changing instructions, metacognition and fairness.
- **16 Nov:** **Students have now played those games, peer-ranked other students' creations, forecast a week's spending, and built reusable solvers.** The faculty examine what happened, find where scores diverge from intuition, and imagine the next exam. This is a **postmortem in public**, not another brainstorm or a proved learning-impact study.

**Central provocation:** What if an exam succeeds most when a student makes its intended task disappear? A student turns difficult motion-stroke interpretation into a standalone HTML solver, built with a model but usable without calling any model. The teacher is impressed. His immediate response is to think about what next exam belongs at the **cusp of what can be solved**. From an examiner's viewpoint this is a moving target; from a learner's viewpoint it may be the whole skill — finding others, finding the tool, building the tool, and being able to judge its output.

Alternative big-picture frame: **A score is an instrument, not a measurement of all the learning.** The session reveals at least three incompatible proxies for performance: team cooperation with one's rivals, audience liking versus originality, and forecast skill versus how long a prediction was held. The teacher continually asks what should count. When a portable solver arrives, the examiner must update the test.

Possible titles for Claude to improve:
1. **The Student Who Made the Exam Obsolete** — strong human hook, but clarify the solver's actual accuracy is **unverified**; it didn't conclusively solve every test.
2. **When the Students Solve the Exam, the Teacher Learns** — focuses on faculty adapting to student ingenuity.
3. **The Exam Is a Moving Target** — repeats 9 Nov's theme; use only if evidence makes it distinct.
4. **More Conversation, Less Profit** — unusually concrete early opening, limited by small and mixed professional sample.
5. **What Does a High Score Actually Mean?** — unifies team games, picture popularity and forecasting, but risks sounding abstract.

## Two powerful openings to stage

### Opening A — “You'd need Fable 5.2, right?” “No.”

~41:10–47:15. Adwitiya says he built an Invisible Ink / Air Ink recognizer, using the newly released Claude **Fable 5.2** (confirmed public release date 9 Nov). Anand assumes users would need Fable to run it. Adwitiya corrects him: **a standalone HTML page with the model weights embedded; no model API needed at use time.** He shares the link from Google Chat, the instructor opens it and chooses a JSONL sample in the meeting. The decoded strokes look plausible in some places, implausible in others. He and JK examine ambiguous E/F/V/H/Y strokes. A second student, **Shrikar** (transcript spelling; GitHub account source is sreekarsarma55), has published another solver. The instructor explicitly declines the setup overhead to run that one live. **The outcome is not validated accuracy; the discovery is that a usable, redistributable, deterministic tool can be built and shared**, partly by using powerful AI for construction rather than every inference.

This scene is a perfect inversion of the usual “students ask the teacher for answers.” The student **changes the teacher's model of what was possible**. Then Anand articulates three possible forms of learning: (a) find a community and a ready solution, (b) use and remember the existence of the solution, (c) build something other people reuse. Those are three different capabilities; it is implausible that everyone must acquire the third. The team should ask: **Does the task measure classification skill, resource discovery, community coordination, model building, or evaluation?** An excellent prompt for readers: “Would you rather train a model from scratch, find a public solver, or persuade a friend to build one? What is the actual success criterion?”

Do not say the model solved everything, that it ran completely without any API or tokens *during development*, or that the professor tested against a private labeled evaluation set; the transcript explicitly records **visual doubts**, not verified ground-truth accuracy. The 16 Nov retrospective private scoring chat reports Q9 classifier bonus results, but that is a separate server-side evaluation, not a test of Adwitiya's exact HTML tool.

### Opening B — Experienced professionals negotiate themselves into a worse score

00:32–07:41, returning to a game explained in 9 Nov's session. Anand ran the same **Food Court** exercise at an AIPL data-science workshop on **15 Nov**. He asks JK to predict whether employed professionals would cooperate better, score higher or negotiate more effectively than TDS students. JK expects **less cooperation but possibly stronger strategy and persuasion**. The big reveal: AIPL's first 20-minute workshop session had **32 entrants in 7 rooms; average team score 88.06**, compared with TDS's three 10–11 Nov sessions' means **92.51, 95.57, 94.13** over 61, 25, 75 rooms. Nearly half of AIPL's final monthly discount choices were 20%, versus roughly 15–25% for TDS sessions. AIPL first-to-last checkpoint average team score went **91.81 → 85.95**, a 5.86-point drop; **6 of 7 rooms** declined. **More plan saves, less chat; worse coordination?** A useful hypothesis, not causal proof. The room sample is small, includes some students using IITM addresses, and workshop vs graded-course stakes, cohort sizes, room size, interface experience and prior rounds all differ. Don't generalize about professional competency.

**Chat complicates this narrative:** Preethi reports the game chat was awkwardly placed — players scrolled away from the discount controls. She says negotiation improved with successive attempts; JK asks whether intuition improved and she says yes. The outcome may reflect both incentives and **UI design** rather than character/capability. Precisely because the task is authentic, the system itself is part of the experiment.

This opening is well suited to an **explorable plot** of team score falling during negotiation, perhaps one anonymized room where many people give 20% discounts, clearly contrasted with a student session. Ensure any numeric simulation reproduces actual rules or is explicitly illustrative.

## Suggested story with four beats (not a required order)

**1. The adults got worse when they negotiated (00–08m).** A grown-up team plays the same economic game students struggled through. AIPL first-session comparison is striking. Its design encourages negotiating between 60% team and 40% individual incentives. Social coordination, not raw optimizer strength, may determine success. The meeting offers a real surprise **plus an honest fairness caveat**. One shouldn't compare only aggregate outcomes and infer individual learning.

**2. Three judges that cannot agree about what “good” means (08–35m).** GA3's face meshes and morph videos are now peer-reviewed. Bradley–Terry adjusts for opponent quality: two entries with equal 13/26 wins can receive different scores. The question then turns to Picture Stories: the most *preferred* stories are often highly familiar/clichéd; some unique stories are disliked or misunderstood, while a distinctive Bhagavad Gita story scores well. The instructor's 7 Nov blog documents a **negative association between uniqueness and preference**. This is **not** a universal cultural law or evidence people hate cartoons (an offhand theory requiring controls). The choice of scoring dimension creates the skills students optimize: reach an audience, innovate, communicate clearly. Their meanings differ.

A delicate real-world extension (~14–17m): an unnamed client can automate regional ad variations but wants to retain an external agency for contracts/liability. The ability to produce the picture does **not** settle ownership, indemnification or accountability. Google Cloud has eligible-output IP indemnification with explicit exceptions, but that does not automatically insure all customers for cultural sensitivity or contractual terms. This anecdote is **client-confidential**; if used at all, generalize and remove identifying details. This illustrates why verification and responsibility are part of work, not just “AI can create the output.”

**3. A forecaster can improve their information and get a worse grade (29–38m).** For the **2–8 Nov UTC AI Pipe-spend** market, the actual total was **$5.3063**. In the recording Anand says **123** initially and **242** finally chose the correct $5–10 bracket, amongst roughly 620 forecasters. A later raw-ledger analysis used **621 institutionally matched, on-time students** and found **123 first and 262 last on-time correct**. These figures **disagree**: do not splice them into a single trend without reconciling cutoff/population definitions; label the first as a spoken snapshot and later as a retrospective computation. Students sometimes moved from far too high expectations to plausible bounds, while some wrote “$5–10” in the rationale and clicked **$0.05–0.10**. The score rewarded being early and holding forecasts over time as well as eventual accuracy; later better evidence didn't guarantee higher marks. This is **an explicit example of a correct calculation executed wrongly**, an automation/verification skill.

**4. When the student brings a reusable solver, the exam must change (~38–66:54).** The planned P1 face-classifier and Invisible Ink challenge separate creating data from using classifiers; Adwitiya's **offline HTML** solution becomes the turning point. He and Shrikar share reusable artifacts; JK asks if sharing creates a social network that can be observed or measured, and proposes citing solvers. The instructor says learning differs for finder, user and creator. The possible ROE shifts to **one avatar, multiple rooms, questions that spawn in different places/times, choices about fight/skip/trade/collaborate**. This is **a speculative design**, not a launched ROE. Adwitiya challenges the anonymity of games: does it make players less accountable? Anand says anonymity itself forces students to build social infrastructure; Preethi describes a team GMeet used to coordinate Time Use Charts. A student's question about **−1 marks** reveals another score/psychology mismatch; the course designer sees a small scaled penalty, the student feels a large loss. The ending should question which **human skill** the next game will actually measure and how to know whether students learned it.

Alternative shorter arc: begin with the offline solver, go back to adults failing negotiation and the scoring paradoxes, finish with the one-avatar ROE as a future test. A non-linear narrative may be stronger, but label dates and avoid implying the ROE occurred.

## Cast and roles

- **Anand:** instructor/course designer; presents data on TDS vs workshop, peer grading, Picture Stories and AI Pipe; reacts to a student-developed standalone solver; asks what can remain as an ROE. Is not an omniscient narrator — reacts with surprise and doubts.
- **JK / Jayakrishnan:** faculty/program colleague; makes predictions about professional behavior, challenges sample sizes, asks questions while Anand explains Bradley–Terry, extends to real industry creativity/liability, asks about network effects, feedback and bonus normalization. Not merely supportive; proposes investigations.
- **Adwitiya:** student who reportedly built an offline decoder using Fable 5.2 at development time, shares a link and responds to inspection; questions anonymity/accountability later. Student claims and demo can be verified directly only to the extent the video / public repo supports them.
- **Shrikar (check name against repo):** student with a second published solver. Shared GitHub source https://github.com/sreekarsarma55/temp-repo ; not run live. Don't confuse student accounts or assume its performance.
- **Preethi:** chat feedback on Food Court UI/negotiation, later demonstrates team coordination beyond a game's chat via GMeet; asks about −1 marks. Her chat is part of the provided transcript, no separate chat.md.
- **Swarnam:** chat about liability and supplied public Picture Stories link. Not independent legal testimony.
- **Carlton:** explicitly **cannot join**; do not attribute live statements to him. His earlier email/prompt work may be source context, not a spoken contribution to 16 Nov.
- **Prasanna, Mayank, Jaideep:** present, with little substantial speaking in transcript; do not fabricate dialogue.

## Timeline anchors (local recording time; validate with WebVTT)

| Approx time | Evidence / scene | Editorial consequence |
|---|---|---|
| 00:12–02:07 | JK predicts how professionals will fare in Food Court | Pose a falsifiable hypothesis |
| 02:07–04:30 | Screen-share aspect ratio/visibility problems, brief meeting interruption | Visual authenticity; avoid pretending a chart is always visible |
| 05:20–07:41 | Workshop vs TDS team scores; AIPL team declines after negotiation | A striking bounded result |
| 09:05–12:37 | GA3 Q6–Q8 peer comparisons; raw wins vs Bradley–Terry opponent strength | Grading is a model |
| 12:50–18:59 | Multimedia/content creator opportunity, agency liability, speaker theories about taste | Automation ≠ accountability |
| 19:01–27:27 | Picture Stories results, preference vs uniqueness; highly clichéd stories preferred | The audience changes what “better” means |
| 29:07–31:25 | AI Pipe usage predictions, actual $5.31; forecast choice errors | Better reasoning can be scored worse |
| 31:25–38:23 | Discussion of personal blind spots and repeat questions; learning menu | No single student-level skill follows from score |
| 38:23–41:08 | Face-expression classifier, Air Ink timed classifier, alleged weak solver | Context before rebuttal |
| 41:10–43:59 | Adwitiya's Fable-made standalone HTML solver and second solver linked | Student changes instructor's estimate of feasibility |
| 44:06–47:28 | Instructor tests an example with visual doubts, Shrikar repo not installed | Observed demo ≠ verified correctness |
| 47:28–50:58 | Using shared solver, tracking social diffusion, three kinds of learning | Learning from finding, using or building |
| 51:15–53:43 | Speculative ROE: one character, rooms, no fixed question sequence, time tradeoffs | A new meta-task, not a deployed exam |
| 53:49–57:41 | Adwitiya proposes identity/accountability; instructor defends anonymous challenge; Preethi's GMeet | Social infrastructure and privacy |
| 58:01–59:04 | “Call a friend,” swapping marks/minutes/questions, steering agents with group intelligence | Proposed mechanism, no outcome data |
| 59:04–64:59 | “AI sob stories,” negative-marks discussion, teen history quiz anecdote, mark scaling | Emotional weight vs mathematical scaling |
| 65:00–66:50 | Student asks for public talks page; instructor/team share URL; recording ends | Course reflections become durable artifacts |

**Transcript discontinuity:** at approximately 49:48, a passage starts “**Anand**: [00:00]” after a separator; that is a **timestamp-reset/transcription artifact**, NOT a second recording starting or a 0:00 event. Actual video/captions should be the authority. The local video is ~66:54; do not borrow 9 Nov's 77:48 duration.

## Strong visuals/interactions worth exploring (choose two or three)

1. **Seven rooms, two audiences:** small-multiple trajectory showing the AIPL seven-room mean team score early → late vs IITM session means; annotate N, session dates, who took part, and the caveat that this isn't a matched causal comparison. Use authentic anonymized team data if allowed; never show user email addresses/handles.
2. **The same 13 wins, different grades:** two anonymized 3D submissions both win 13/26 reviews, but opponents differ. Interactive “who did you beat?” makes Bradley–Terry instantly intuitive. Carefully choose already-public outputs or diagrammed placeholders, never individual private graded artifacts.
3. **The originality trap:** x = uniqueness, y = reader preference; a familiar common story high on liking but low on originality, a unique moon-landing-phone gag with lower liking, a unique and liked Bhagavad Gita outlier. Use exported/public-safe images and actual plotted aggregate only; don't invent precise coordinates.
4. **Reasoned correctly, clicked the wrong unit:** a box says **$5–10**, the selected radio says **5¢–10¢**; reader must spot the error. Distinguish illustrative mock from actual anonymized student case.
5. **The stand-alone solver:** visually trace _frontier-model development → portable local HTML weights → student's uploaded motion JSONL → classifier guess → manual verification_. Show a **model-call counter** (model used in development, zero remote inference calls in a claimed standalone tool), but make clear correctness is unverified.
6. **The impossible avatar:** one-character ROE decision tree with two rooms, time left, hidden tasks, only one can be reached. The user must choose skip/seek help/solve. Mark the entire prototype **speculative**, with no actual finalized rules.
7. **What do you mean by “cheating”?** Finder vs reuser vs builder triptych. This course explicitly allows agent and collaboration in many tasks; no blanket license for impersonation, unauthorized access or dishonesty.

## Evidence guardrails and ending

- Don't claim students became smarter than working professionals. AIPL was a tiny mixed cohort, with room-size, incentive and experience differences; analysis found **more saved plans but less chat**, not “didn't try.”
- Don't claim stronger forecasters got lower grades generally; the particular score function rewarded timing and repeated updates, and one can have more precise later estimates yet a worse cumulative mark.
- Don't claim a solver “cracked the exam.” It made plausible predictions on a demonstrated JSONL; no held-out accuracy evaluation in the meeting. A person reading the strokes was also uncertain, making the ground truth and classifier eval critical.
- Don't equate “having a solver URL” with individual model-building competence. The three-tier learning claim should be treated as an instructor hypothesis, not a measured finding.
- Don't imply original art is intrinsically less preferred; the measured negative correlation can result from common story priors, sampling, voting, prompt trends, multiple testing and rating mechanics. The 7 Nov first-person blog explicitly says the author doesn't know why.
- Don't assume Google indemnifies all generative AI uses — scope and exclusions matter. Don't repeat confidential client description in a way that identifies them.
- “−1 penalty” psychological effect depends on its scale and mark rules. Treat Preethi's reaction seriously; the fact that its final grade weight is small does not mean that communication/expectation cannot be improved.
- Any speculative future ROE mechanical details must be clearly **proposed**, and later versions may evolve.

The durable end isn't “the teacher is now obsolete.” It's that **students, agents and teachers are redesigning the curriculum together**. The teacher tests the games, students test the teacher's assumptions, and every working solver shifts the frontier. But **a course that teaches verification must also verify that these experiences actually develop transferable skills** — not merely that students can score, vote, share or improvise.


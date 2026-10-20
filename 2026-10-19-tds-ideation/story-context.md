# Story context — 19 October 2026 TDS open course ideation

Working editorial research for a **future talk-story build**. Transcript and real recording govern events; this file separates observation, interpretation and design ideas. **Do not reproduce the structure mechanically.**

## Premise and what changed from last week

The 5 October orientation said: do real work with tools, agents and people—and verify it. The 12 October ideation meeting asked how to design exams that still teach something when an AI or a peer can do the work. On **Monday 19 October**, a few of those concepts have arrived in students' hands and the constraints can no longer be hypothetical.

Three very different Project 1 prompts embody three routes to the same skill: **prediction market → evidence and incentives; Human Exchange → a useful human promise someone else would choose to buy; Air Ink → authentic physical-world measurement later usable in ML.** Then the team designs a new GA3 that limits time and checking. The teachers admit an invoice puzzle consumed ~US$500 of experimentation and *failed the design test*; Tangram turned out reusable by solvers thanks to a fixed vocabulary and a leaked solution in a filter endpoint. At the end, an audience question shows how easily a historical “percentage correct” is mistaken for an autonomous evaluation of difficulty.

**What if the most educational thing about the exam is seeing where its own design breaks?**

The richest thread is not “AI-resistant questions.” It is **the difference between doing work, getting it graded, and acquiring a skill worth keeping.** Some of these tasks explicitly welcome agents; Air Ink's quick capture step does not. Avoid the false universal claim that the class bans agent use or that every game is agent-proof.

## Suggested four-beat discovery arc

**1. A promise meets a marketplace (00:43–17:48).** Last week's market and distributed human skills are suddenly concrete. Anand reports hundreds of virtual market trades; the class can try forecasting future AI Pipe spend. The spoken Human Exchange offer must have an actual recipient who values it. Student Preethi asks how many services, whether a buyer must already exist, whether repeat purchases are allowed, and how offers will be discovered. JK clarifies scope and legal boundaries; Carlton asks about ordering. The instructor's broad philosophical objective is revealed to be a set of practical product decisions. Air Ink then makes the mobile phone an experimental instrument: first capture hand motion, later attempt recognition. **The assignment is a data-collection step, not a proven working classifier.**

**2. The grader is part of the game (17:48–25:24).** The GA format itself needs redesign. Unlimited checker attempts can make a location question a grid search instead of geographical reasoning. Proposals include short staged windows, capped checks, or giving up marks in exchange for more verification. A grade/eligibility consequence raises a fair objection from Carlton: is the change sprung on students midstream? JK and Carlton reason about eligibility thresholds and flexibility. The pedagogical argument remains an argument: fixed limits may simulate realistic verification cost, but they can also punish time-poor or resource-poor learners. **Don't equate difficulty with learning.**

**3. The teacher puts his own ideas through an adversarial test (25:24–39:11).** The lecture briefly becomes a field report of failures. From live client work, confidence calibration and retrieval/search approaches look important but proprietary details are withheld. The distributed invoice challenge, appealing in the previous meeting, cost around $500 of simulations, lacked a robust individually informative scoring setup and was abandoned in the tested form. Tangram offered apparent human visual leverage, but the finite bank and exposed solution endpoint undercut it. New candidates are 3D reconstruction from sampled cross-sections, harness optimization against unseen future problems, and asking students to build evals. JK's inevitable rejoinder: *how do we evaluate the evals?* Anand dictates a research prompt to an agent on the spot. **Treat failures to publish broken exams as good judgment, not embarrassment.**

**4. A harder definition of “real” (39:11–59:33).** Preethi requests instruction on setting up agents safely. Phones as physics instruments, niche research puzzles and prize-worthy open tasks could take assignments closer to unscripted reality—but worsen instrumentation, reproducibility and checking. The Cyphral Distich anecdote is an **incredibly useful example of an apparent strong AI claim that changes when the source edition changes**: the 1834 version decodes; the surviving 1653 edition does not have the same key structure. Students and teachers exchange tips about a GA2 model-family workaround and invite public writeups of solving strategies. Finally at 58:17 the question “did an agent grade difficulty?” gets a simple answer: no, the script just counted correct submissions. **An exam score is not its own theory of learning.**

End with a field-testable five-question exam checklist rather than a speculative “AI has made assessment obsolete”: What ability? Why is the task authentic? How does it survive answer/solver sharing? What does verification cost and who bears it? What new *individual* capability could a later task demonstrate?

## Speaker profiles / tone

- **Anand** proposes experiments and future projects, makes pragmatic tradeoffs, asks agents for research during meetings, sometimes discards expensive ideas. Does not claim learning impact proven.
- **JK** pushes on permissible scope, fairness and operating procedures, suggests agent harnesses/evals, repeatedly asks how to grade proposals.
- **Carlton** pushes the user-experience and student fairness angles: ranking in marketplace, pauses in drawing, end-term eligibility, and later how difficulty was measured. Beware: the [55:43] “sir” voice is labelled Carlton in the dialogue, but the transcript's added metadata identifies **Adwitiya**, a student. Verify in the recording before attributing.
- **Preethi** supplies the practical user-test: pricing and scope of Human Exchange; then reports a need for help with multi-agent/container setup. She isn't merely asking “basic” questions; she reveals missing requirements.
- **Mayank** reports that the P1 submission issue seems fixed after corrections. The conversation proves only his confirmation at [00:39], not a comprehensive regression test.
- Other students/TAs contribute in smaller turns. Do not invent people, name private student identities or share personal data from the video.

## Timestamp map — transcript time; recheck against video

| Timestamp | Scene | Editorial role / accuracy note |
|---|---|---|
| 00:00–00:43 | Project 1 Q2 submission problem | Real infrastructure issue acknowledged/resolved in the room |
| 00:43 | Anand promises philosophy of P1, then GA3 | Structure sets up implementation vs idea |
| 01:13 | Prediction market: 200–300 trades by Anand's estimate; prices expected around $10–$20 | Reported estimate; not independently verified |
| 03:06 | Specification problem / Human Exchange | “What is useful?” is being answered by a market, not a grader |
| 04:29 | Credits traded by mutual consent | Hypothesized later marketplace, not live transactions |
| 05:53–07:07 | JK asks scope; legality | Practical requirement uncovered |
| 07:11–08:06 | Bluetooth app ban discussion | Potential misinformation: do not repeat law/policy claim without primary confirmation; irrelevant to core story |
| 08:21–12:53 | Preethi's many-offer questions, marketplace sorting, website copy | Strong student-led user research; no fixed final market UI demonstrated |
| 13:16 | Air Ink physical demonstration | Screen may have been stopped at [17:27]; check real footage before illustrating |
| 15:21 | Capture tilt traces now, later try ML reading | Actual ML evaluation future, not executed during call |
| 16:30–17:08 | Carlton asks how to pause between letters | Small interaction detail exposes use-case |
| 17:48 | GA3 release-window and verification-budget discussion | Distinguish proposal from deployment |
| 19:35 | Verification checks are not cost-free; brute-force GeoGuessr | Core mechanism behind scarcity |
| 21:20–25:24 | Carlton/JK debate fairness and eligibility | Do not simplify to full unanimity |
| 25:24 | Private Straive work screen-share paused | Do not screenshot/reproduce confidential sources |
| 25:55 | Catch AI mistakes via confidence calibration / escalation | Public research available elsewhere |
| 26:26 | Agentic search vs indices/tools | Design choice, no universal ranking proven |
| 27:05 | Invoice experiment ~US$500, abandoned | Anecdotal reported cost, **not** proof agents cannot solve |
| 28:25 | Tangram fixed-bank issue; 3D slices | Proposed 3D concept not live exam |
| 29:59 | 3D intuitive cut selection | Cross-sectional ambiguity; AI-v-human comparison untested |
| 30:22 | Carlton raises sex/gender differences in mental rotation | Treat fairness as open design issue; literature reports average distributions, not ability of individuals |
| 31:05 | Business simulations | Future possibility, not deployed |
| 32:11 | JK says Google open-sourced “Harness 2” | Unverified name/release; omit or explicitly attribute with caveat |
| 33:20 | Configurable Pi harness, unknown held-out tasks | Interesting eval overfitting problem |
| 34:56–35:48 | Building evals and evaluating evals | Self-reference; central to verification |
| 36:40 | Anand dictates research query about eval-of-evals | Agent-in-the-loop demonstration; audible thinking pause |
| 39:40 | Preethi asks for practical agent setup session | Visibility/accessibility of technical setup |
| 41:24 | Phone as physics lab; friction, g | Proposed physical experiments, no accuracy validation |
| 44:08 | Prize/bounty/research puzzles | Motivating but how grade a successful *individual* contribution? |
| 46:29 | Cyphral Distich, Urquhart | Misheard as “Cipher of the Stitch”; source edition caveat is important |
| 49:24–51:28 | Prize puzzle bonus and AI verification | Agent judge reliability not established |
| 51:46 | How many Project 1 questions? | JK playfully suggests a prediction market; count uncommitted |
| 53:07 | Request for students to document solution process | Peer teaching but sharing threatens reusable tests |
| 54:03 | Tangram: filter endpoint and 100 seed shapes | Actual weaknesses; don't turn into attack tutorial |
| 55:43–56:51 | Model-family workaround for GA2 | Transcription metadata says speaker is Adwitiya, not Carlton; validate attribution and actual result before publishing |
| 57:24 | Call for TAs to propose GA4 questions Wednesday | Future work request |
| 57:57–59:33 | “difficulty.py uses an agent?” “No, deterministic” | Strong ending: correctness rate is not intrinsic complexity or proof of transfer |

Transcript discontinuity near 29:59 is not an actual 30-minute cut; video duration ~59:36. A speaker-labelled embedded WebVTT exists; video/audio is the ultimate arbiter. Short faithful soundbites beat unverified long quotes.

## Concrete visuals that could actually earn a place

- **The previous week vs this week**: ideation cards turning into three distinct user-facing experiences (forecast with data → human promise/receipt → phone motion trail). The previous week's video itself is a meaningful link.
- **“You are a buyer” microinteraction**: two anonymized sample Human Exchange offers, choose one you would pay credits for, then reveal how specifying scope, timing and evidence of delivery changes the choice. Clearly fictional offers.
- **Verification as a finite budget**: score/risk tradeoff with optional checks; balance authentic uncertainty against resource constraints. Use hypothetical parameters and no implication they are published rules.
- **Leaks vs difficulty**: a 100-shape Tangram bank: show how the same-looking challenge changes when answer space is finite and when grader outputs contain target solutions, *without providing an exploit*.
- **Slices and hypotheses**: several candidate solids compatible with a given cut; choose an extra cut that separates them. It illustrates information gain, **not proven difference between humans and LLMs**.
- **“What exactly did the AI solve?”**: side-by-side 1834 and 1653 text-provenance chain, with a tiny 5/3/27/38 → O/G/O/D example. This is an authentic, verifiable controversy, from Anand's local research, and uniquely memorable.
- **Difficulty chart interrogated**: percentage-correct from different simulated cohorts vs ability to transfer to a changed setting. Demonstrate confounding without inventing historical TDS figures.

Choose the strongest 3–4; don't turn the page into a widget zoo. Keep a comic/full-video section and searchable timestamp route.

## Non-negotiable fact boundaries

- The class predicts a **future Nov 2–8** spend; the meeting has no settlement outcome.
- Human Exchange **recordings** are live; the marketplace and actual trade confirmations **are future**.
- Air Ink **sensor capture** is live/being introduced; classifier **future**.
- The invoice challenge was **discarded in this configuration** after expensive trials; no proof the underlying concept can never work.
- The Tangram problem's fixed-bank/response leakage is **reported** by the instructor; not permission to reproduce technical exploit code or publish hidden answers.
- Harness design, 3D slicing, physics, competitive bounties and student evals are **ideas**.
- The Cyphral Distich is **17th century**. A reproduced 1834 decipherment is not proof of the 1653 textual provenance.
- Mark correctness percentage as **observed completion rate** (conditional on cohort, help, retries, solver access and grading), not objective item difficulty.
- Student tool access, hardware, accessibility, money/time and mixed prior experience are not noise; they are part of assessment fairness.
- Speaker diarization is uncertain in several turns. Verify before associating words with named individuals. 

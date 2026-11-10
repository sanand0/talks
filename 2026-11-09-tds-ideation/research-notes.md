# Research, fact checks and methodological cautions — 9 Nov TDS ideation

Prepared 10 Nov 2026 from the local meeting recording/transcript/chat; source implementations; course files and prior ChatGPT discussion; independent public BBC, government and educational evidence. Claude should cite source-specific claims, not paste this whole shelf into the story. Claims in the meeting are speaker statements until checked.

## Evidence tiers

A. **Direct meeting:** local 9 Nov WebM with embedded captions, transcript.md, chat.md. Grounded as “Anand said,” “JK proposed,” “students reported.” Source of what *was claimed*, not necessarily what is actually deployed or pedagogically effective.

B. **Implementation:** versioned source ~/code/exam/src/exam-tds-2026-09-ga4.info.js, q-food-court-discount.js, q-time-use-charts.js; ~/code/tds-network-games/REALTIME-GAMES.md and src/realtime/*. Use only public question mechanics, not confidential thresholds, private answer services, student identifiers or unreleased internals. These local files were committed/modified on 9 Nov, so they reflect the meeting period fairly closely, but could still differ from the production deployment or the exact minute of a screen share.

C. **Aggregate observational research:** user's own Nov 4 “TDS Measure Learning Transfer” analysis, ~/Documents/chatgpt/TDS Measure Learning Transfer.md (private). Strong on sampling/paired counts but not a causal estimate, and this device did not expose the underlying published data/reproduction script. The numbers should be labelled *reported analysis* until replicated.

D. **Independent sources:** BBC article dated 4 Nov, EEF August 2026 review, India's MoSPI dataset and current public course pages. Use original publications rather than secondary speculation.

## The deadline watcher: specification error, not a mere clock bug

**Direct chat evidence:** at 10:33 Mayank links https://aaryanpanda.github.io/tds-watcher/ ; at 11:22 JK links https://dueline-tds.vercel.app/ (the posted URL adds a utm_source, not part of the canonical route). Both pages returned **HTTP 200** on 10 Nov; this verifies existence, **not** correctness or content at the exact meeting moment. At ~09:54–12:35 Anand shows a live watcher displaying the terminal deadline as the primary countdown, missing the decisive 20-minute Food Court and 45-minute Time Use Charts attendance windows. This is a **data-model / event ontology** problem: a quiz has a final due date, but some questions have their own launch windows and strict sessions.

**GA4 specifics in first-party code inspected 10 Nov:**
- Extended final **GA4 deadline Sunday 15 Nov 2026 23:59:59 IST**, from Wed 11 Nov. It is *not* the live-game session deadline.
- **Food Court:** Tue 10 Nov 18:00–18:20 IST; Wed 11 Nov 07:30–07:50; Wed 11 Nov 21:00–21:20. Students can play each session once and choose the best signed result.
- **Time Use Charts:** Thu 12 Nov 21:00–21:45 IST; Fri 13 Nov 18:00–18:45; Sat 14 Nov 08:00–08:45. The sessions are separate from GA4 final submission; a student needs to be present throughout a selected 45-minute sitting and all team members must agree before submission.
- **Peer review:** GA4 Q1 counts reviews from GA3 face work using a signed proof; user reports at ~16–21m suggest operational sign-in/receipt confusion. Do not assert the case was user configuration or a systematic code bug without a reproducible test. “Other students report it too” is evidence warranting investigation; “most users can log in” does not eliminate a minority-specific server bug.
- In the meeting, Preethi discovers the new Nov 15 date after assuming 11 Nov: a **specific example of the purpose and stress of changing schedules**, but she was in the live session. Students not in it may have experienced the communication differently. JK says most assessments retain normal longer windows and a few exercises deliberately test faster response; verify frequency in actual assessments before quantifying it.

**Potential external research analogy:** Event-driven systems need multiple event types, explicit timezone/calendar semantics and reliable update notifications. A watcher that says “six days left” might be perfectly correct for final *submission* while utterly wrong about the earliest required *participation* event. A calendar that groups all these under one GA deadline gives a wrong recommendation. **Do not call the original site “broken” without inspecting it; the UX/coverage is incomplete for this use case.**

**Fairness challenge:** Night shifts, caregiving, assistive technologies, flaky connections and multiple simultaneous academic exams affect whether the exercise measures rapid delegation or access. Offering three alternative slots reduces but doesn't eliminate conflict. Future “midnight-to-4am” exercises in Anand's talk are **aspirational for later terms**, not part of the demonstrated GA4 schedule. “Agents monitor 24/7” is an intended approach, not a prerequisite proven equal-access for the whole student population. Tracking an arbitrary/unannounced deadline is not automatically analogous to legally announced tenders or investment market information.

## Food Court — verified game economics, interesting distortion

The local published-style documents and GA4 question establish:
- 4–5 classmates share a room; **20-minute** game, twelve months of decisions, **0%, 10% or 20%** discount only.
- Changing one's monthly discount changes own margin, attraction, others' customers and total footfall; results depend on competitors' policies and prior-month choices.
- **Actual final grade: 60% team profit + 40% individual profit**, normalized to game benchmarks. The talk's easy-to-understand “highest own profit gets marks” compression is incomplete. Use the 60/40 in graphics, with the date/scope of the code read.
- Multiple chances: up to three distinct sessions, best eligible result. A **no-discount/all-at-20%** strategy yields differing outcomes under this exact model; avoid invented equilibrium/collusion results unless using the actual tested model.
- The model's **all-at-20% price-war score** is documented as about 66.5/100 in 4-player rooms and 63.6 in 5-player rooms; the best attainable fair-room mean differs by room size. These are model-calibration results (not students' final observed scores). If turning into a visualization, verify simulation formula and exact room count, or simplify and label hypothetical.
- There is a real **tension between individual optimal response and collective high profit**, hence negotiation and trust, but scoring rewards both. A sophisticated agent may optimize discounts, but its capacity to induce cooperation from other participants is an open empirical question, not a proved human-only advantage.

**Source:** ~/code/tds-network-games/REALTIME-GAMES.md ; ~/code/tds-network-games/src/realtime/games/food-court/model.ts ; ~/code/exam/src/q-food-court-discount.js. In-game public question wording is safer to cite than private simulator or server signing details. Do NOT expose sensitive administrative API routes, signing keys, auth tokens, or exploits.

## Time Use Charts — another form of coordination

**First party:** ~/code/exam/src/q-time-use-charts.js ; ~/code/tds-network-games/REALTIME-GAMES.md and src/realtime/games/time-use-charts/.

- 45-minute collaborative poster from **Time Use Survey 2024**, a real government dataset; teams of three (occasionally two), roles **designer, writer, reviewer**, independent idea generation during first 15m, unanimity vote before group production, and synchronized approval. A no-agreement team can finish with no submission. Author of winning idea gets **20%** of marks and the group shares 80%; rubric for poster has four 25% dimensions: uniqueness, correctness, comprehension, peer preference. Codes specify these weights as of 10 Nov, but do not claim all resulting grades are known (sessions in the future).
- This is a useful counterpoint to Food Court: **individual incentives to persuade the group** amid collective dependence on consensus. That can teach skills in coalition, conflict, empathy or framing; whether it does so is unmeasured here. Unanimity may intentionally cause an impasse rather than an instructor error.
- **Official MoSPI source:** Time Use Survey (TUS), January–December 2024, https://microdata.gov.in/NADA/index.php/catalog/236 (metadata identifies NSSO/MoSPI, paid, unpaid household and caregiving activities; 2024 survey conducted after 2019 survey). Primary press release: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2116301&lang=2&reg=48 ; also https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2106113&lang=2&reg=48 . This is not a “2026 data collection” or generated mock dataset.
- 2024 TUS covers survey interview time slots and weighted national samples; avoid deriving a new population statistic from a handful of unweighted CSV rows. For a public demo, show anonymized example themes, never infer personal routines from player records.

## “Learning transfer” — the meeting's most important unproven claim

Anand at ~34–39m reports that good repeated-skill questions can show 20–30% learning and more than half have some positive measure. However, the transcript does not supply exact question identifiers, matched-student denominators, thresholds or control data. The definition of “learning” is ambiguous: a later exam performance increase is **not necessarily a gain in independent human capability**.

**Archived analysis:**
~/Documents/chatgpt/TDS Measure Learning Transfer.md (4 Nov 2026), original private chat https://chatgpt.com/c/6aeaa231-d914-83ec-b6dd-68db71e00f9c . The analyst says four September-term exports were refreshed; some matched pairs and pass thresholds were computed with ordering requirements. For GA0 running Ollama via tunnel → GA2 functional LLM API via tunnel, **687** matched chronological students: **146 improve = 21.3%; 37 worsen = 5.4%; 504 unchanged = 73.4%** (421 pass both, 83 fail both). This is a 4:1 improvement/worsening comparison but NOT a controlled estimate of skill transfer: unrelated earlier GA0 questions with comparable initial success rate predicted the later performance about as well. That is a **powerful reveal** if kept honest.

In the same study, successful earlier termlog recording predicted **94.5%** later recording success, vs **22.1%** for those initially unsuccessful, a 72.4 percentage-point gap in conditional later performance. That seems more skill-specific but is *evidence of persistence*, not that the second assignment taught what the first failed to. Some superficially related tasks showed more student decline on the later one because the later task was substantially harder. Hence “students did worse” is not proof they forgot.

Limits: pairing requires actually comparable skills, matching population, explicit missing and zero-score treatment, repeated exposures, skill probes vs composite whole-question score, varied difficulty, time between quizzes, model/tool version changes, ceiling effects and selection; absence of a randomized comparison. Do not publish anonymized-but-traceable individual student records. The full analysis claims artifacts in ~/code/exam/dumps/ on **Plutonium**; they were **not present in this LocalMCP2 mount on 10 Nov**, so these particular counts are *secondary archive evidence*, not independently recomputed in this task. Tell Claude to verify data if presenting it as a graphic.

**External synthesis — counterweight to “you figure it out.”** Education Endowment Foundation, “Metacognition and self-regulation,” 16–19 learner evidence, **24 Aug 2026**:
https://educationendowmentfoundation.org.uk/16-19/developing-independent-learners/metacognition-and-self-regulation .
They recommend *explicit* instruction of planning/monitoring/evaluating, modeling and guided practice, then independent use; **do not assume learners develop metacognitive skills without instruction**. The 16–19 evidence base covers 39 studies with a strong average effect in that context, but it is not an evaluation of online adult IITM students or GenAI assignments. Strong tension: Anand wants learners to discover their own objectives; JK wants them to reflect afterward; metacognitive evidence suggests some **scaffolding and feedback** may improve the chance this succeeds.

Additional broader EEF toolkit (updated May 2025): https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/metacognition-and-self-regulation . Do not double count studies as independent new evidence.

**Design improvement proposal, not a reported result:** before/after and *unseen future* task, score decision process or diagnostic probe rather than only overall success; use parallel tasks/controls, detect ceiling and difficulty differences, capture explicit plan-monitor-evaluate reflections and whether tool selection/verification was improved. This would be a strong forward-looking end rather than pretending current transfer is already proven.

## The BBC article and the missing junior-work paradox

Carlton in chat links a BBC report at **36:58**:
https://www.bbc.com/news/articles/c820vz6wyp65o .
Article: MaryLou Costa, **“Graduates are managing AI - but are they learning much else?”**, **4 Nov 2026**. It describes **Lotte Underwood**, 25, who joined PR agency Fight or Flight in an AI associate role; the team has built **around 30 AI agents** for research, reports, interview prep and other work. She checks their output and routes it to coworkers. Avoid transcript's inaccurate “Lottie,” or saying *she personally employed 30 bots* or that the BBC proves a general jobs trend. The article specifically questions whether AI-focused graduates are missing core professional experience such as directly pitching journalists. This is a **challenge to the instructors' assumption** that exposing students to “senior” tasks via agents develops senior judgment.

The original BBC page returned HTTP **200** from LocalMCP2 curl on 10 Nov but web extraction can restrict BBC content. Corroborating summaries of the exact story: https://www.soz6.com/news/graduates-are-managing-ai-but-are-they-learning-much-else ; https://www.readynews.in/graduates-are-managing-ai-but-are-they-learning-much-else . Cite the **original BBC URL** in the public piece; paraphrase briefly, don't copy the article text. The student skill and career-effect claims from the discussion are **opinions, anecdotes and hypotheses**, not established statements that all BTech graduates are unemployable or AI equals unlimited PhDs for $20.

The key story conflict: schools skip junior execution because agents can handle it; employers ask juniors for senior judgment; **where do the “battle scars” and tacit knowledge come from?** A high-speed simulated food court is a plausible rehearsal but not yet validated as a substitute for actual professional experience.

## Specific unverified or overclaimed assertions to fence off

- “90% of our actions are subconscious, 10% conscious” and “millions of years of muscles/genetics teach swimming”: speaker imagery, **not independently supported quantitative/neuroscientific facts**. Do not repeat as statistics. Motor learning analogy helps only if marked illustrative.
- “AI can answer anything given time” and “agents have taken away all intellectual tasks”: deliberate hyperbole. Treat as an expectation about available tools, not settled facts.
- “Students who complain are unprepared”, “most successful users means bug not systemic”: unsupported; multiple students described login/receipt problems.
- “We can simply wake students at midnight or train them with permanent agents”: future hypothetical, no assertion of shipped implementation or equitable availability.
- “Embracing cheating”: TDS permits collaboration and agents for specified activities, but **not** unauthorized identity impersonation, forgery, leaking confidential material or violating external services' policies. Use the instructor's local meaning (tool/peer leverage) with care.
- “Model X is best for all 3D,” “face morph is trivial everywhere”: particular video examples and services; distinguish an easy-to-find purpose-built provider from high-quality generative geometric morphing across arbitrary images.
- “Published LLM swarm on a German wiki”: the teacher's retelling of an apparently external case; don't present mechanics, platform names or precise technical exploits as independently verified until source is found. The lesson can be explained without repeating unconfirmed technical steps.
- “Safari will intentionally fail” from ~22m: a design statement; confirm in code and fairness policy before claiming production deliberate browser exclusion.
- The three proposed repeated-measurement GA5 questions from Carlton (~68:37): **work-in-progress branch** as of meeting; do not claim launched or successful.
- Michael Jackson “Black or White” was a student's cultural reference, not educational evidence about face-morph performance, and its copyrighted audio/video must not be embedded or reproduced.
- Current 9 Nov empirical reality: the two new GA4 games are **future scheduled sessions**, not finished outcomes. Don't invent scores, screenshots of winning teams, numbers of teams or learning impact.

## How to verify the final story

- Confirm every selected direct quote and timestamp with WebM subtitles, especially Anand's departure at ~66:26 and the remaining ~11 minutes.
- For each number include **unit, denominator, date, data version, and whether observed, simulated or claimed**.
- Recheck real watcher pages and schedule APIs immediately before publishing; sites may evolve since 9 Nov.
- If using game math, reproduce it from published first-party source; don't mix current 60/40 weighting with spoken “your own profit determines marks.”
- If using aggregate learning-transfer figure, trace it to reproducible results on a reachable machine, and separate observational association from learning causality.
- For educational recommendations, test the strongest counterargument (students need scaffolding; expensive always-on agents create inequality; artificially short windows may select access not capacity).
- Publish only safe screenshots/images: video frames may show assessment administration and student IDs.


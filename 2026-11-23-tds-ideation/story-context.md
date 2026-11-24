# Story context — TDS course ideation, Monday 23 November 2026

Editorial map for the future Claude talk page. Prepared 24 November 2026 (Singapore time). This is NOT a script to reproduce verbatim. The transcript belongs to a roughly 58m46s recorded open meeting; its “Chat” section contains only short messages, while student forum, WhatsApp and Google Chat evidence is separate and mostly private. Confirm quotes, speakers and timestamps against the video and embedded WebVTT before publishing.

## The episode that moves the series forward

- 12 Oct: The Exam Is a Hypothesis — designing questions when agents can solve them.
- 19 Oct: The Exam Has to Pass Its Own Exam — designs confront real solvers and grading.
- 2 Nov: Should a Student Even Read the Exam? — what judgment remains?
- 9 Nov: Who Watches the Deadline Watchers? — surprise, live games, and the fairness of changing rules.
- 16 Nov: The Score Can’t See Who Built the Solver — solver creators, users and graders learn different things.
- **23 Nov: The exam has become a literal shared maze.** It has a time budget, a changing supply of tasks, an agent-accessible API, collaboration, traps, luck and a relative-score incentive. Early students build tools and coordinate. The faculty ask whether the skill to teach is choosing, finding people, asking the right question, capturing fleeting evidence, or maintaining human judgment when agents execute everything. The next morning's telemetry tests their hypotheses—and reveals that the implementation can assess something unintended.

**Editorial thesis:** When an agent can solve the question, the exam moves from *answering* to *allocating attention*. But that only works if the assessment itself measures prioritization and collaboration, rather than hidden navigation, chance, UI bugs or who happens to be online.

**Candidate working titles**
- **The Rat Race Has a Team Door** — JK's memorable 12:33 rat-race joke collides with the post-meeting three-person door.
- **Three People Pushed. The Door Stayed Shut.** — strongest concrete hook, but derived from the **24 Nov analysis**, not from a live discussion during the 23 Nov meeting. Clearly label the retrospective chronology.
- **More Questions Than Time** — crisp premise; reflects the intended unlimited opportunity, but does it reveal the surprising result?
- **The Exam Where Solving the Questions Isn't the Hard Part** — first-day attempts mostly succeed; navigation/coordination is the bottleneck so far.
- **What Should Humans Do While Agents Work?** — broader, recurring, less particular to this episode.
- **Don't Lose the Signal** — captures the distinctive observability debate, but needs the maze as a vivid first scene.

The memorable first line could be JK's: “If you want to win the rat race, we make sure that the other rats collaborate with us.” [12:33] Verify word-for-word from the actual recording. By [12:47] Anand responds that a top score changes the denominator for everybody in a proposed **relative** grading scheme—so cooperation, rivalry and the leaderboard interact. Do not imply the class demonstrably colluded or sabotaged a high scorer.

## An earned four-beat story (illustrative, not compulsory)

**1. A maze with a clock and no finish line (00:00–13:40).** Hritik has already found the newly deployed practice ROE. His agent solves most of it, with the remaining obstacle being the door that needs three students. Anand explains why the *real* ROE is intended to have **more questions than a strong student or agent can finish** and around **45 minutes** as the main budget: prioritization, choosing when to abandon a task, risks, groups, opportunities and clock extensions. The practice counts for **no marks**, a distinction the meeting confirms explicitly at 06:54. The link has leaked through Discourse and students' groups before the intended official release; deliberate early discovery is part of the philosophy. Hritik discovers there is **currently no WebMCP**, contrary to what he expected; the actual implementation has a structured JSON API that the browser uses too. Whether WebMCP will be added is left open. JK introduces the “rat race” paradox: if the top score sets a denominator, your brilliant classmate may lower everyone else's percentage. A roomful of rats might need both collaboration and competition.

**2. A class becomes its own software ecosystem (13:40–29:59).** JK observes that two or three prolific solver makers are surrounded by more users/testers and a large silent majority. Anand compares this to open-source communities: project creators, issue reporters, maintainers, coordinators, and people who benefit quietly. He notices the **missing middle layer**: the group has no shared registry of questions, deadlines, solver versions, benchmark performance and known failures. JK proposes sharing redacted agent interaction logs as a learning resource and having students reflect on their own contribution; Anand shows recent SUTD computer-vision workshop responses to “What did you learn?” These are **proposals**, not a published measurement of individual growth. A student subsequently posts an experimental maze co-pilot in Google Chat on 23 Nov, describing route selection, automatic exploration and map sharing. That announcement happens **after** the meeting; treat as a sequel and verify implementation before calling it a successful optimizer.

**3. The difficult job is catching the data before it vanishes (29:59–40:55).** JK thinks organizing shared files, permissions and Git history is a fundamental, durable skill. Anand pushes back: if agents can increasingly structure messy material *after* the fact, perhaps the bigger human responsibility is **making sure the raw event was captured at all**. A missed console error or transient screen event cannot be reconstructed by future intelligence. An exam could show vital information in one room, ask the question in another, and bar return. JK invokes observability; Anand reframes the frontier yet again: identifying a worthwhile question to ask of messy data may outlast a specific RAG or file-tree technique. **Do not resolve this as “organization is obsolete”**. JK's counterargument is substantive: structure can constrain search space and enforce access rights. Frame the distinction as **capture → preserve with provenance → organize/retrieve → decide**, not a false dichotomy.

**4. More intelligence creates more decisions (40:55–58:45).** JK cites *unverified, non-controlled* experiences with declining closed-book Python quiz pass rates and worries students lose unaided competence. Anand advocates teaching at the boundary of agent capabilities: creativity, specification, skepticism, verification and taste—but says that boundary moves. He and JK explore **decision fatigue**: agents perform a month's execution in a day; humans must make a month's worth of prioritization and accountability decisions in a day. The ROE may rehearse that, but making the exam “harder” doesn't automatically build the muscle. Carlton asks whether the education produces **real outcomes**, not just performative tool fluency. Anand proposes a **future** Monday panel of TAs describing whether TDS skills carry to their work, explicitly acknowledging selection bias among those who worked with him. The meeting ends with a provocative question: **if the exam tries to measure agent-age judgment, who checks whether it measured that rather than game friction?**

## The post-meeting sequel, explicitly dated 24 Nov 2026

The supplied local retrospective “TDS 2026 09 ROE Practice Maze Analysis.md” is dated 24 November and uses synced **23–24 November first-day** maze activity, not data the instructors had fully examined during the call. It is **evidence that challenges their design intentions**, not dialogue that happened on 23 Nov.

Independently rechecked from the synced CSV and event log:
- **92 total accounts**, **81 IITM BS-DS student-address accounts**; not 92 independent enrolled students.
- Within the 81 student-address accounts: **median raw maze score 18**; **20 scored at least 23**; **five scored 27**, the ordinary automatic-challenge ceiling in the first sandbox (not evidence full ROE has a 27-mark cap).
- **136,061** movement steps recorded for those student accounts; **160,489** total events across all accounts (event count from sync/metrics).
- For the twelve ordinary counted challenge types, **503 student/challenge solved pairs**. The retrospective reports **503 successes of 520 attempted (96.7%)**; the denominator follows that report's attempt definition. A simple distinct (account, question) grouping produces a different denominator, so **do not publish the exact 96.7% without explaining/reproducing the attempt logic**. Stronger, durable point: the common tasks were easy *once found*.
- Team doors are the surprise. The **three-person vault got 1,832 student push events**. One anonymous player alone submitted **1,041** vault pushes, without opening it. The code counts **distinct occupied pads** to open, but reports **number of pressing people** in the ready count, which can misleadingly display “3 of 3” when only two distinct pads are occupied. This is a verified **instrument/UX mismatch**, not “students failed to collaborate.” Don't describe exact exploit or hidden gate implementation on the public page while the scored ROE is upcoming.
- 18 student-address accounts received zero raw maze marks. Some never attempted questions at all; selection, onboarding friction and simply choosing to explore can all explain this. Student notes include “stay here i will bring other” and “push the team door in 1 2 3”: **spontaneous coordination**. Do not imply every such attempt succeeded.
- An experimental co-pilot was announced in an IITM Google Space during the evening of 23 Nov, after the meeting; students describe pathfinding and shared maps. This is an **announced tool**, not an independently benchmarked high-performing agent.
- The synced snapshot tested far fewer than the **anticipated 500** simultaneous participants; unit tests, local simulations and small load tests cannot establish real exam-day reliability at 500. A tested **30-bot** practice run in the code docs isn't the same as 500 student browsers with different time/network conditions.

**The high-value tension:** The faculty intend more tasks than time, so *selection* matters. The early practice environment can actually be **exhausted by the strongest students**. The faculty intend a collaboration puzzle, but the implementation can reward repeated synchronized clicks and gate access on chance or physical proximity. They intend to normalize scores, but one high outlier can change everyone else's grade under a max-denominator scheme. The practice is doing its job by surfacing unintended measurements *before* scored ROE; don't overclaim that the bugs are still present after the team fixes them.

## Cast: do not invent dialogues or decode identities

- **Anand**: instructor/game designer; promises a moving frontier of questions, deliberately encourages agent discovery; also admits unspecified WebMCP, score normalization and incomplete grading work. Proposes capture-before-organize, content judgment and decision stamina. His HFT comparison is an analogy, not evidence students need nanosecond latency.
- **JK / Jayakrishnan**: peer and productive skeptic. “Rat race” joke; sees solver producer/tester/consumer community; advocates annotated agent traces and reflection. Defends organization/permissions as transferable, brings evidence worries about unaided quizzes and cognitive load. He does not endorse every hypothetical exam mechanism.
- **Hritik**: tries maze and reports what was solvable in one prompt; asks where WebMCP went; suggests link discoverability and flags grading backlog; in chat mentions a GitHub PR. Agent claims not independently measured.
- **Carlton**: joins later (~51:39), asks if these learning experiences produce real-world results, via an analogy to televised practical challenges. Not present/quoted in early meeting.
- **Preethi**: asks in chat how many questions there will be, correctly amplifying uncertainty. Do not frame the question as naive or imply a fixed answer was known.
- **Other students**: self-selected early practice explorers, anonymous team-door pressers, student tool builders and peer supporters. Treat presence in WhatsApp/Google Chat and silence as **behavior in those sources**, not a psychometric label or permanent identity.

## Timestamp and continuity guide (approximate — check captions)

| Time in video | Human scene | Why the reader should care |
|---|---|---|
| 00:08–01:54 | Birthday wishes, Hritik has seen practice ROE and nearly solved it with an agent | The “exam” is already here before official announcement |
| 01:54–06:30 | More tasks than time; personal 45-minute budget, chance, groups; likely real ROE Sunday 29 Nov | Selection/portfolio strategy is the learning hypothesis |
| 06:47–07:58 | Practice carries no marks; GA4/P1 grading still pending | Important fact; the demo is a dry run, not official assessment |
| 08:41–10:45 | Leaked practice link, early discoverers, HFT analogy | Discovery itself is rewarded; fairness question |
| 10:49–12:30 | Missing WebMCP; current structured API instead; no final choice | Tool affordances determine how agents can play |
| 12:33–14:10 | JK “rat race” and relative scoring | Competition and collaboration may conflict |
| 14:07–18:50 | Two/three solver makers, users, testers, missing organizer role | Community labor is broader than writing code |
| 18:49–20:55 | Approx 26 early submitters / 20 full-screen scores as reported mid-call, unverified snapshot | Do NOT conflate with 81-account next-morning study |
| 21:14–27:53 | Shared agent logs, metacognitive reflection, SUTD “what did you learn?” results | Transfer across agents and people is not automatic |
| 29:57–35:21 | Jigsaw data, organize vs capture, observability, room you can't revisit | A memorable model of irreversible information loss |
| 35:21–40:55 | JK challenges organizational obsolescence; useful questions matter | Preserve the disagreement, avoid AI evangelism |
| 40:55–46:34 | Agent-boundary curriculum; unevaluated unaided-quiz decline claim; fast decisions | Are we outsourcing the wrong cognitive work? |
| 46:34–49:15 | Decision fatigue; Straive hiring anecdote and institutional inertia | Competing labor-market realities, not census data |
| 49:15–51:35 | Zork, Colossal Cave, Carmen Sandiego | Friendly visual metaphor, not the actual game's origin story |
| 51:39–57:02 | Carlton asks for real deliverables; next Monday TA work stories proposed | The transfer test the instructors still need |
| 57:02–58:45 | Privately compare student communities, rough active/passive shares; signoff | Avoid identifying named “passive” students or inventing participation percentages |

## Possible interactive visual metaphors (choose 2–3, not all)

1. **The 45-minute allocation choice**. A reader has five task cards (near/easy, distant/hard, group door, one uncertain chance, one high payoff). Let them assign time/agent/peer attention and see how expected marks and risk change. Explicitly **illustrative**, not a copy of the exam puzzle, seeded maze, scores or secret answer keys. Help them reason marginal value, switching cost, recovery.
2. **Three at the door, but why didn't it open?** Animated or storyboard visual showing how different definitions of “ready” can fool both a player and a monitoring system. Show a **generic** team-readiness state machine, not the current unpatched actual co-op gate parameters. The interesting thing is **the displayed metric was not the condition being evaluated**. Only show implementation specifics after actual ROE finishes and they're publicly safe.
3. **Capture before organize**. A stream of ephemeral events crosses the page. Readers choose whether to inspect each one, save raw events with timestamps, organize folders or ask an agent to reconstruct missing events. The missing event can't be recovered by perfect classification. Make the point that a searchable archive, permissions and provenance still matter; **logging everything is itself costly and can violate privacy**.
4. **The open-source class**. Producer → user → tester → maintainer/community coordinator and silent participant flows. Show roles, not student names or private communication-network analysis. Demonstrate which missing infrastructure would make the whole class more productive.
5. **One bad objective**. Compare leaderboard with normalized max vs absolute mastery under a toy model, showing how strong performance can lower others' relative percentages and change incentives. Don't assert this exact normalization was finally approved or implemented.
6. **A day of decisions**. Agent finishes execution; human accumulates 20 successive prioritization/veracity calls. The bottleneck moves from manual tasks to judgment, but fatigue is a hypothesis to be examined, not a proven causal effect from this class.
7. **Practice telemetry after the fact**. A timeline places “23 Nov 11:20 — API debate” and “24 Nov morning — 1,041 door pushes discovered” in separate time bands, preventing historical leakage into dialogue. A compact funnel of students entered → found → attempted → solved can be used **only if the denominator and exposure definition are correct**.

## What must remain uncertain or absent

- **Do not reveal real ROE hidden map, task parameters, signed tokens, replay surfaces, unpatched exploits or student-specific scores** in a talk likely to be public before Sunday 29 Nov. Even “public source code” can contain future question details; public storytelling is not a permission to leak an assessment.
- Distinguish **practice** from scored exam, **intent** from functioning implementation, and **post-meeting** from live conversation. Practice was explicitly **ungraded**; real exam config as of 23 Nov was still a placeholder and may change before Sunday.
- A 1,041-push outlier suggests automation but does not prove a particular student's agent setup or mental state. Don't name, de-anonymize or criticize the participant.
- First-day learner sample is self-selected by early discovery, and the score distribution is specific to a simple practice sandbox. Avoid claiming all students scored 27 or a representative cohort was measured.
- The absence of WebMCP on 23 Nov is factual in the recording and design decision; don't assert WebMCP is globally unavailable or that the maze has no agent tools. Structured JSON API already exists.
- “Collaboration produced only 11 successful doors” mixes pad events, per-account unlocks and group openings. Keep **attempts, distinct participants, successful groups, unlocked player accounts** separate.
- Two mechanisms are especially risky: score normalization based on the strongest student, and randomly gated marks. They can change what students optimize. The retrospective identifies concerns, **not established causal unfairness** across the course.
- Quotes about closed-book Python pass rate declining 70–80% to 50%, Straive technical hires <5%, and “90% work can be automated” are speaker estimates/anecdotes with unverified denominators; do not publish them as population facts.
- Logging/capturing information must include permissions, minimization and privacy; real student chat archives cannot automatically be published as a dataset.
- Later Monday TA workplace outcomes and P2 agent-log reflection are proposals, not delivered or proven by 23 Nov.

**An ending that earns its moral:** The teachers built a maze to test what agents can't do. The first students solved its easy tasks with agents, made navigation tools and tried to recruit one another. A door counted their presses but didn't necessarily let them through. That final contradiction asks a more important question than “How many marks did they get?”: **“Did we measure the judgment we meant to teach—or merely the obstacle we happened to build?”**


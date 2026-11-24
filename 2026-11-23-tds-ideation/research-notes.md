# Research notes and fact-check ledger — 23 November 2026 TDS course ideation

Prepared on 24 November 2026 SGT, for the future talk build. Evidence is tiered:
A. **Meeting recording**: 23 Nov WebM + embedded WebVTT and transcript.md, including short appended chat.
B. **Actual implementation**: ~/code/tds-network-games/{prompts.md,MAZE.md,src/maze/,test/}; ~/code/exam/src/{exam-tds-2026-09-roe-practice.info.js,q-maze-practice.js,...}. Date/version-sensitive.
C. **Local synced practice data**: ~/code/tds-network-games/.private/maze/practice-sandbox/{players.csv,events.jsonl,answers.jsonl,notes.jsonl,chat.jsonl,summary.json,metrics.json,manifest.json}, synced 24 Nov morning; private, not for publication.
D. **Prior researcher analysis**: ~/Documents/chatgpt/TDS 2026 09 ROE Practice Maze Analysis.md (created 24 Nov morning), some counts corrected in its own text. Use the **corrected** values.
E. **Student discussions**: scoped TDS WhatsApp group and IITM Google Chat export, 22–24 Nov, private. Useful for behavior but not authorization to publish individual identities or transcripts.
F. **Independent publications**: browser WebMCP draft and official Chrome docs; Google SRE and OpenTelemetry observability; assessment theory papers. These support conceptual interpretation, not causal evaluation of this class.

## 1. What the Monday meeting actually established

The instructor says [~01:55–06:30] that the **practice maze is largely to exercise interfaces, agents and navigation**, while the future scored ROE will have potentially more challenges than anyone can finish. Individual time is roughly **45 minutes** with optional time adjustments from game actions. So what to try, when to quit, when to ask another player, when to use an agent and how much chance to accept become intentional. He explicitly says at ~06:54 **“ROE practice will not be counted at all”**.

The live question being designed is not simply “Can an LLM answer question X?” but “Can a student allocate 45 minutes among uncertain opportunities and use external intelligence safely?” This is **an instructor design claim**, not yet an observed learning outcome.

The link is intentionally not yet formally posted and has spread through student groups; this can select high-initiative early adopters. Hritik [10:49–11:20] asks for WebMCP; Anand clarifies that the current version chose a browser/agent **JSON API**, not WebMCP, and may change. The authoritative first-party maze spec in ~/code/tds-network-games/MAZE.md explicitly lists the JSON endpoints. **Do not say the game lacks an agent interface**, nor say WebMCP was already active at this time.

The intended scored ROE is **Sunday 29 Nov 2026** as of the 23 Nov practice instructions. The experimental real-world config in src/maze/worlds/roe.ts is a **placeholder as of inspected date**, not proof of exact launch times or final challenges. The published practice info in ~/code/exam/src/exam-tds-2026-09-roe-practice.info.js states no marks, one always-on practice maze plus other windows, a receipt flow, gifts/traps/doors, and Sun 29 Nov as the real date.

## 2. What was independently recomputed from the first-day data

I independently scanned the local **players.csv**, **answers.jsonl** and **events.jsonl** for the synced **practice-sandbox** snapshot. These are actual first-day telemetry, not the lecturer's on-screen view during the meeting.

| Measure | Value | Verification and definition |
|---|---:|---|
| Accounts in players.csv | **92** | Count CSV records |
| Accounts with institutional *.ds.study.iitm.ac.in email | **81** | Filtered by institutional email suffix; doesn't prove distinct human participants or correct enrollment |
| Median raw maze score, student-address accounts | **18** | Median of CSV “total”, not final course mark |
| Those scoring at least 23 | **20 of 81** | Independently re-counted (earlier analysis chart had incorrectly said 22) |
| Those scoring exactly 27 | **5** | Independently re-counted, ceiling of ordinary auto-graded practice challenges, not exam ceiling |
| Student-address accounts scoring zero | **18** | Independently re-counted, including accounts who may only have explored |
| Total movement steps, student-address accounts | **136,061** | Sum of players.csv “steps” |
| Overall event records | **160,489** | Synced summary.json and event-log row count (includes nonstudent accounts) |
| Student push events at 3-person vault | **1,832** | Independently grouped events.jsonl where event type is coop_press and door is vault |
| Largest single student's push count at vault | **1,041** | Independently grouped anonymized event log, over 56% of vault pushes |
| Ordinary practice tasks successfully solved by students | **503 unique student-task pairs** | Independently grouped ordinary task types, omitting offline essay and a separate bonus spot |

**Important denominator problem:** The provided retrospective's corrected account says **503 successful student-task combinations out of 520 attempted = 96.7%**. I independently reproduced the **503** successfully solved ordinary pairs. But a simple unique (student, task) grouping across the 12 ordinary tasks gives **510** touched pairs (some only “open”/pending), not the 520 “attempts” operational measure. Those counts are *not* interchangeable. If the public story uses “97% solved once attempted”, future Claude must reconstruct the report's attempt definition precisely and show the denominator, or say qualitatively that **almost every ordinary question actually attempted was solved**. Do not return to the analysis's earlier erroneous **543/559**, **22 with ≥23**, or “five got full ROE marks”. Practice wasn't graded.

The first-day study also found that stronger students exhaust the **finite practice supply**: five reached its 27 ordinary-mark ceiling, and some finish many solved tasks well before 45 minutes. This supports the user's proposal for an expanding/harder task stream for the **real** exam, but says nothing about the eventual real exam question difficulty or readiness.

**Selection caveat:** Accounts appearing before formal announcement are likely early discoverers who may have better monitoring skills, more leisure time or more active student networks. The 81-account sample is small relative to the expected cohort, and the first practice tasks were deliberately easy. Do not generalize to 1,000 students or to a full scored exam.

## 3. The team door: a measurement defect, not evidence students can't collaborate

The **three-person door** received **1,832** push events from students; one account submitted 1,041 on this door without successfully unlocking it. This strongly suggests repeated-input automation, but without observing the student's device it is **not proof of an agent**. There are 2,043 student co-op push events across both the three-person vault and the two-person shortcut; do not confuse these counts.

Verified in first-party code ~/code/tds-network-games/src/maze/engine.ts, in the co-op-door press routine:
- The actual opening condition uses enough **distinct pads occupied by present players** within a short window.
- The published ready count uses **number of pressers that remain on their pads**, not the number of distinct pads.
- That creates a scenario where UI says **“3 of 3 pushed”** without satisfying the actual opening condition.

This is a real discrepancy between **what the interface reports** and **what the validator checks**. It might cause frustration and pointless clicks even for cooperating players. A fair classroom reflection is **“the exam's verifier must itself be verified.”** The exact mechanics are sensitive during the week before scored ROE: don't create a public debugging guide or expose unpatched implementation detail in the talk. A generic illustration suffices; update the notes if the bug is fixed before page publication.

The analysis reports cooperative notes, team recruitment and group timers. The existence of social activity is independently supported by 94 student “note” event records and student WhatsApp/Google Chat messages. **Quantities like doors unlocked and participant counts require careful deduplication**: an opening can create multiple per-player coop_open events, a single player may repeatedly press, and an account may unlock several doors.

**Design hypothesis, not an observed guarantee:** a persistent ready state and clearer visual feedback would reward real collaboration rather than synchronous clicking. Another possible issue is simultaneous presence: three people must be nearby and active at once, so players arriving at off-peak times face a different opportunity set. This is not repaired merely by explaining the rules.

## 4. Discovering a question versus solving it

The study's strongest finding is a low success funnel for *discovery and reachability*, not correctness. In the reported data:
- Only a subset of the 81 student-address accounts found/opened the Archive and Vault, but most who actually *attempted those ordinary questions* solved them.
- The practice includes keys, dice, trap tiles, rooms, notes, fog of war and group doors. The game intentionally gives exploration value.
- In a stronger candidate live exam, the intention is “many hard choices within one 45-minute window.” In this simple practice, the risk is measuring “how efficiently can you reach the task?” or “is a second/third person online now?”

Retrospective source's Archive funnel says **81 entered, 47 acquired a key, 25 opened the Archive, 24 solved the task**. These are reported counts from the study, not all independently recomputed here. Some players gambled keys away; other keyed players still never reached/used Archive. This can create **luck-dependent access** even if all dice have equal expected item value. Equal expected value of items is not equal probability of being able to attempt a particular mark-bearing task.

Social activity: study counts **61** claimed gifts, **46** attempted doors, **41** gambled, **23** left notes, **12** used in-game chat, **2** offered trades, **0** completed trades; source has an explicit account-based definition and rows may need de-duplication. A disabled/unused feature isn't proof students lack negotiation skill when the marketplace is hard to find or find matching counterparties.

## 5. Relative scoring and incentive design

At **12:33**, JK jokes that to win a rat race one must get the other rats to cooperate. At **12:47**, Anand says that if the highest raw score is the denominator, a high performer “messes up everybody else's scores.” This is a **stated design idea**; do not assume the final grading scheme is fixed, approved, equitable or actually applied. Relative min/max schemes differ from percentile/capped grading; precise formula matters.

Toy illustration, explicitly **hypothetical**:
- If the top raw score is 30, a student with 24 gets 24/30 = 80%.
- If another student achieves 60 while our student remains at 24, they get 24/60 = 40%.
- Their own raw competence did not change, but the normalized percentage did.

That is not necessarily unfair if clearly specified, but it changes **incentives**: collaboration on a top solver can harm relative grades, whereas making the class broadly stronger may or may not. Goodhart and strategic coordination effects are plausible, not observed sabotage. The point may be to expose collective-action strategy; a teaching institution must decide whether this is the skill it meant to reward.

## 6. The emerging class community: roles and records

JK at **14:07–18:49** distinguishes a few prolific tool/solver authors, a larger set of testers and troubleshooters, and a big silent audience. Anand sees an open-source organizational gap: few people keep a current registry of task links, accepted versions, success rates, public datasets, issues or deadlines. This is a **reasoned diagnosis from conversation**, not a proven community graph. The numbers of producers/testers/passive students were not formally established in this meeting.

**Private discussion corroboration** from narrow scoped searches:
- **WhatsApp TDS Sept 2026, 23 Nov**: students asked for practice link, shared an exam entry URL, warned about traps, discussed a three-person team door, asked about an archive key and whether a maze was the whole ROE. One described exploring “everything, except for what was behind that door”. These messages are private; paraphrase/anonymize and do not publish account IDs.
- **Google Chat TDS 2026, 23 Nov**: a shared practice link and warning about finding it; a participant proposed teaming up at the next timed practice; an **experimental co-pilot announcement later that day** described navigation, map exchange and task ranking. Don't publish private Google Chat room/message URLs or unreviewed agent-running instructions. An announcement is not a benchmark, and it happened after the recording's end.
- **WhatsApp TDS, 22 Nov**: a student worried about an early surprise exam because they were away from home and couldn't participate. This is a concrete **accessibility/fairness** concern; quote only with consent, otherwise paraphrase.

**Do not infer personality or label individual students** (freeloader, cribber, silent) from partial channel participation. Missing WhatsApp messages may mean activity on Google Chat, direct messages, internal groups, other platforms, or none. The 24 Nov analysis's self-selected “student archetypes” describe observed strategies only; treat them as examples, not human identities or diagnoses.

JK proposes standardizing shared **agent logs** and post-task self-reflections; Anand demonstrates SUTD “what did you learn?” responses and suggests making each question self-reflection optional. These were **not deployed curricula** in the meeting. Agent logs can contain prompts, private documents, credentials, other students' data or third-party secrets; there must be explicit opt-in, redaction, purpose and retention limits before making any public repository.

The 2026 thesis that an agent may organize data later but cannot reconstruct an unlogged event is a **conditional statement**: if other cameras, logs, third-party caches, snapshots or backups exist, recovery may be possible. The more precise principle is **capture information at the point of creation, when its loss is irreversible; then preserve it with reliable provenance and access control**. Organization still matters for permissions, retention, storage cost and discoverability.

## 7. Independent external verification

**Browser WebMCP.** Authoritative Chrome guidance https://developer.chrome.com/docs/modern-web-guidance/guides/webmcp/webmcp states WebMCP is **an experimental/early-preview browser API** to expose client-side web functionality as structured tools to agents; not the same as a backend JSON API or an MCP server. The Web Machine Learning Community Group's **23 Nov 2026** draft https://webmachinelearning.github.io/webmcp/ currently documents document.modelContext and the changing spec; avoid naming obsolete navigator.modelContext as the only API or claiming universal browser support. The game developer explicitly chose JSON API at this time.

**Monitoring and observability.** Google's freely available Site Reliability Engineering chapter “Monitoring Distributed Systems” https://sre.google/sre-book/monitoring-distributed-systems/ distinguishes collection/processing/aggregation of live signals and metrics that alert people to real service problems. The source's “golden signals” are latency, traffic, errors and saturation; don't force these to be the only relevant measurements for a classroom maze. OpenTelemetry official primer https://opentelemetry.io/docs/concepts/observability-primer/ and instrumentation page https://opentelemetry.io/docs/concepts/instrumentation/ confirm that useful system observability depends on emitting logs, metrics and traces. **If an event was never emitted or captured anywhere, post-hoc querying can't magically retrieve it.**

**Authentic game-based assessment validity.** BERA/British Journal of Educational Technology paper “Measuring learning in digital games: Applying a game-based assessment framework” https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13407 says assessment mechanics must be aligned to intended learning outcomes and evidence-centered assessment; a game outcome alone doesn't isolate collaboration/critical thinking. Related study “Learning teamwork through a computer game: for the sake of performance or collaborative learning?” https://link.springer.com/article/10.1007/s11423-021-10009-4 warns that participants may optimize performance rather than teamwork, and emphasizes feedback and guidance. Neither study evaluates the TDS maze or its 2026 cohort.

**Decision fatigue / AI accelerated decisions.** The 23 Nov exchange is plausible and analytically interesting, but do **not** claim it is scientifically established that AI enables “a month's worth of decisions per day” or that rapid decision-making specifically builds fatigue-resistance. It is an experiential hypothesis that could be tested with decisions, errors, recovery and effort across time. Literature on decision fatigue has measurement and replicability controversies; keep the story within the speakers' claims.

**HFT analogy.** Locating servers near an exchange to lower latency is a real practice, but proximity doesn't validate surprise exam discovery as fair or educational. The class should not be said to be doing literal high-frequency trading or to require nanosecond responsiveness.

## 8. What was NOT established by this meeting

- No proof the **scored 29 Nov ROE** would have exactly the same map, task inventory, probabilities, rank normalization or social mechanics as a first-day practice; MAZE.md marks scored config as placeholder.
- No proof the official real ROE would have **unlimited generated challenges**; the 23 Nov code has a finite sandbox and the never-ending enhancement appears in **#TODO** in ~/code/tds-network-games/prompts.md.
- No verified audience-wide learning transfer. Efficient navigation, early discovery, puzzle solving and obtaining results are not identical to metacognitive development or sustained judgment.
- No validated completion of 500-human concurrency testing. The MAZE.md asserts 30-bot production simulation and browser E2E but **not 500 simultaneous real participants**. Local first-day organic concurrency metrics differ from all-time/historical peak.
- No demonstrated large-scale personal employability change. JK's “Python quiz passes went from ~70–80% to 50%”, Anand's “under 5% innovation recruiting” and estimates about automation are speakers' incomplete local anecdotes, not independently verified trend data.
- No demonstration that JSON API is unfair to browser-only students, nor that WebMCP would make all tasks trivial. It changes the accessibility and tooling affordances; compare actual tested clients and devices.
- No finding that silent students benefited or did not benefit from solver sharing; absent communication is not absent activity and some channels are unobserved.
- No approval to publish raw Discord/Google Chat/WhatsApp content, individual outcomes, student IDs or unreleased exam details.

## 9. Verification gate for Claude's eventual public page

For **every major number**: label **23 Nov meeting snapshot** vs **24 Nov retrospective**, cohort definition, unit (account, person, event, door opening, question), window, and whether reconstructed independently. For **every exact quote**, confirm video/captions and speaker. For **every student example**, anonymize and remove direct-identification clues. For **every interactive simulation**, mark invented mechanics and inspect to ensure they don't disclose the coming scored ROE's route/task answers or exploitable weaknesses.

The strongest possible revision will **show which metric accidentally measured the wrong thing** and give the reader a useful way to separate intended skill from product friction: “If I replaced the 3-person door with an accessible, clear and persistent handshake, would your score still distinguish good collaborators?” That question is more useful than another high-level “AI changes education” summary.


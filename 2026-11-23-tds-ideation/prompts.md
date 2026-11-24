# Prompts

## Build Prompt, 24 Nov 2026

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->

<!-- Original metaprompt/source: https://chatgpt.com/c/6ad6b3d4-12a0-83ec-97b2-e792263fffb5 -->
<!-- Comic-page creation/provenance: https://chatgpt.com/c/6b04d107-095c-83ec-9ccc-842d3e99d2ab -->

```markdown
Create a **polished, original, source-grounded interactive single-page talk story** for the IIT Madras Tools in Data Science open course-design meeting of **Monday 23 November 2026**, at **2026-11-23-tds-ideation/index.html**. This is the next installment in the Monday series, not a generic “AI education is changing” article and not a lecture transcript with headings. Aim for a memorable human story that a smart educator, student, engineer or manager would read to the end even without knowing TDS. Tell it simply and precisely, with surprises earned by evidence rather than manufactured by narration.

**This file is instructions for Claude later. The current preparation task is JUST PROMPTS and source context.** When this brief is executed in the future, create the actual story page and only genuinely necessary supporting public assets. Do not change the exam, network game, gradebook, student records, original transcript, comic, recording or audio. **Do not commit, push or publish.** The potential scored ROE is just days away: no disclosure of unreleased questions, routes, answers, server vulnerabilities or personally identifying player behavior.

## Source material — actually inspect it before choosing the story

1. **Read all of ./transcript.md**, including the appended “## Chat” section at its end. The original video is **58m45.875s**, 1280×720 AV1+Opus with embedded WebVTT. Verify decisive quotes/speaker attributions against the real recording or captions, and ensure the story covers the relevant later discussion, not only the maze introduction. The speaker labels may be inconsistent (JK/Jayakrishnan) and some timestamps are approximations.
2. **Read ./story-context.md** for a proposed discovery arc, cast, timecoded passages, alternate openings, genuine objections and illustrative visualizations. It is an editorial hypothesis, not a screenplay. Improve it when the actual meeting supports something sharper.
3. **Read ./research-notes.md** for re-derived first-day aggregate counts, what the maze code actually implements, source-analysis corrections, what only participants *claimed*, the score/attempt denominator issue and the risks of testing the wrong thing.
4. **Read ./links.md** for verified media, actual local and online source paths, the carefully separated 23 Nov meeting vs later student chat vs 24 Nov telemetry, and data privacy. Follow the primary sources rather than relying solely on the notes.
5. **Independently read the user-specified analysis**: ~/Documents/chatgpt/TDS 2026 09 ROE Practice Maze Analysis.md, including its **later corrections**. The narrative benefits from this **24 Nov retrospective** but must not pretend it was said or known at the **23 Nov meeting**. Study the first-party synced practice-sandbox aggregates selectively and read-only in ~/code/tds-network-games/.private/maze/practice-sandbox/.
6. **Read the real previous finished talks and prompts**, particularly ../2026-11-16-tds-ideation/{index.html,prompts.md,story-context.md,links.md} (published title “The Score Can’t See Who Built the Solver”) and ../2026-11-09-tds-ideation/{index.html,prompts.md,story-context.md,links.md}, followed by ../2026-11-02-tds-ideation/, ../2026-10-19-tds-ideation/ and ../2026-10-12-tds-ideation/. For video-interaction polish, also consider ../2026-11-17-sutd-coil/index.html or ../2026-11-21-sutd-cv-workshop/index.html. Reuse their **functional bar and finish**, not their precise CSS, page skeleton, artwork or theme. Find and read applicable local talk-story, data-story, design, interactions, interactive-storytelling and verification skills before building.
7. **Inspect relevant actual code, read-only**, only enough to confirm mechanics: ~/code/tds-network-games/{MAZE.md,prompts.md,src/maze/}; ~/code/exam/src/exam-tds-2026-09-roe-practice.info.js and maze-question modules; ~/code/tools-in-data-science-public/2026-09/. The user-specified ~/code/tools-in-data-science/ folder doesn't exist on this LocalMCP2 device. Selective context: ~/Documents/{chatgpt,claude}/ and Nov 22–24 student discussions in ~/Documents/data/whatsapp/ and ~/Documents/data/anand@study.iitm.ac.in/. These are **private evidence**, not content to dump into a public page. Do not fetch and publish sensitive private records. Do not edit the source repos.

**Critically distinguish four time states** throughout: (1) mechanics proposed in the 23 Nov meeting, (2) mechanics already running in the simple 23 Nov ungraded practice world, (3) results and student tools discovered **after the meeting** in 23–24 Nov analytics/chats, and (4) the **actual scored ROE planned for Sunday 29 Nov** whose rules, difficulty, scoring and tasks may change.

## The strongest story: a rat race with a team door

At **~01:31**, Hritik says his agent can finish nearly all of the new practice ROE, but he is blocked by a door requiring **three players**. The teacher likes that: answering should not be the entire exam. In a 45-minute world of many opportunities, students must decide when to quit, find help, gamble, change strategy and move on. At **~12:33**, JK turns the entire premise into a joke: **“If you want to win the rat race, we make sure that the other rats collaborate with us.”** Verify his exact words in video. Anand points out a sharp incentive conflict: if the top student's raw score is the normalizing denominator, **someone who gets extremely far ahead can lower everyone else's relative mark**. Collaboration could turn into strategic competition. This was a debated scoring idea, NOT proof of coordinated grade sabotage.

Now step **outside the meeting into an explicitly dated sequel**. On 24 Nov, the first practice data say the **easy questions are not the bottleneck**. The user-supplied research report records 503 successes out of 520 ordinary task attempts under its specific operational definition; my independent recount confirmed **503 solved student/task pairs**, but a different simple “touched” denominator comes out differently. Do not present 96.7% as a perfectly re-derived truth without reproducing the analysis's denominator. More clearly, **20 of 81** IITM student-address accounts reached at least 23 raw practice marks; **five** reached the currently available 27 ordinary-mark ceiling. Several strong students effectively ran out of new tasks even though the design goal was to have more tasks than they could finish.

At the same time the three-person team door accumulated **1,832 student push events**. **One anonymous account submitted 1,041** of them and never opened that door. The source code confirms the UI's press count is **not the same definition** as the distinct occupied positions required to unlock. The interface can tell players “3 of 3” while their real opening condition remains unsatisfied. That is not evidence that the student is stupid or socially incapable. **The exam is reporting the wrong measure for the state it requires.** There is a deeper analogy: the score itself could report the wrong competency for the skill it claims to measure.

This concrete contradiction is the centerpiece of the episode: **The exam tries to measure how students orchestrate agents and people under uncertainty. But its first practice may be measuring whether they can reach a task, find two people at the same time or interpret a misleading state display.** The right response is not to abandon ambitious assessments; it is to verify the *test itself* against its stated learning objective. The session is an open design meeting, so the faculty can and should learn from failed assumptions.

**Working title:** “The Rat Race Has a Team Door.” A stronger hook if it fits: “Three People Pushed. The Door Stayed Shut.” Another possible framing: “More Questions Than Time — But Not the Ones They Expected.” You should decide, considering the first six seconds of reader attention and the actual comic. **The door event is from post-meeting data, not a scene the audience watched in the meeting**. Do not fake a reconstruction of Hritik pressing 1,041 times or imply he was that anonymous player.

## A possible four-beat discovery arc, not a fixed TOC

**1. More questions than time (~00–13:40).** The game is a shared fog-of-war maze: roughly **45 minutes per entrant**, rewards and traps, chances to get hints or time, and questions hidden in rooms. The real design aspires to many more tasks than anyone can finish. The **practice does not count for marks**, says the teacher at ~06:54. Early discovery of the not-yet-announced link is partly intentional. Hritik reports the agent can answer most practice challenges but needs other people for a group door; he notices the absence of WebMCP. The maze uses a **JSON API**, not a promised WebMCP interface. This is not a failure of agent support, nor a final decision about WebMCP. JK's rat-race remark reveals the conflict between helping one's peers and individual relative grades.

**2. The class is already building a human-agent ecosystem (~14–29:59).** JK reports a few prolific solver makers, more people testing and asking for help, and a silent audience. Anand sees the missing **community maintainer**: where is the registry of question windows, solvers, successful versions, known bugs and pooled data? They discuss sharing redacted agent logs, making each student reflect on “What did you learn?”, and being able to identify one's contribution to a human-agent swarm. Anand shows a small SUTD computer-vision workshop reflection; it is a real example of *collecting perceived learning*, not proof of transfer. After the meeting a student posts an experimental maze co-pilot in Google Chat that describes exploration, map sharing and task ranking. Show it only as **later student initiative**, not a benchmarked agent or a 23 Nov live demonstration.

**3. You cannot organize data you never captured (~29:59–40:55).** JK says sound file organization, Git versions, context and permissions are transferable skills. Anand thinks agents can increasingly organize or search information after the fact, but a fleeting log line or one-time event is gone if it was never recorded. He imagines seeing vital data in one room, leaving it and having to answer the question in another room where return is impossible. The stronger insight is **not “organization is obsolete”**. It's **capture, provenance and sufficient context BEFORE retrieval and structuring**. JK argues that careful organization still reduces search and enforces access. The two views complement each other; the speaker disagreement should be readable and fair.

**4. What remains when agents do the tasks? (~40:55–58:45).** JK worries about unaided competence in closed-book quizzes; Anand wants to teach at the moving boundary of agent capabilities: **taste, skepticism, specifying, verifying, asking useful questions and prioritizing**. The paradox: if agents can execute a month's worth of tasks in a day, humans may have a month's worth of exhausting decisions in a day. That's a plausible lived hypothesis, **not established science**. Carlton, arriving near 51:39, asks for proof students can produce **useful outcomes at work**, not just game completions. Anand suggests future TAs share how TDS skills transfer to internships, acknowledging that his own trainees are a biased sample. End with the research question the meeting hasn't yet answered: **can we measure genuine transferable judgment separately from task-completion marks, navigation, lucky access, social presence and product friction?**

A more experimental structure could **open with the 24 Nov door incident** clearly time-stamped “The next morning,” cut back to the 23 Nov discussion that created the challenge, move through community and information capture, and return to the door as a small **verification failure of the verifier**. This could be a more memorable graphic essay. Do not create false cause-and-effect or compress two dates into one dialogue.

## Facts you must not distort

- **Video vs retrospective:** live session was Monday **23 Nov**; synced data analysis was conducted **morning Tue 24 Nov**. On-screen Anand mentions roughly **26 early submitters and 20 apparently full marks**, a **different timestamp/cohort** from the later **81 IITM student-address accounts**. Don't splice them.
- **First-day numbers:** 92 total accounts, 81 IITM student-address accounts, median raw practice score 18, 20/81 at least 23, five at 27, 18 zero. The 27 is a simple **practice challenge ceiling**, not the designed real ROE's maximum. 160,489 synced events include all accounts. One player generated 1,041 of 1,832 vault pushes. Those two push totals were independently grouped from the raw event log. **Student-address accounts are not verified unique humans.**
- **Attempt denominator:** the corrected report says **503 successful of 520 attempts**, not the earlier erroneous 543/559. The numerator was independently reproduced for the 12 ordinary tasks, but different definitions of “attempt” include launch, open, reply, repeated tries and/or offline tasks. Reconcile before showing an exact 96.7% completion-rate chart. Qualitative conclusion (“ordinary tasks almost always solved once attempted”) is still well supported.
- **Actual ROE:** announced for **Sunday 29 Nov 2026**, but current scored world is still a configuration placeholder as inspected on 24 Nov. The ever-expanding task enhancement is in **#TODO**, not confirmed shipped. The ungraded practice is not the real exam.
- **Team door:** UI ready count and actual unique-pad condition can diverge. **Do not publish a live exploit, pad sequence, exact code, internal endpoints, keys, hidden map or workaround while the scored exam is upcoming**. A safe synthetic handshake diagram can convey verification vs displayed status without helping students bypass exam challenges.
- **Score normalization:** a max-student denominator is a proposal described in the meeting, not demonstrated official scoring. Use a **clearly hypothetical numeric example**, e.g., raw 24/30 vs 24/60, to show its strategic consequences. Explicitly separate “a score's denominator changes” from “classmates sabotaged each other.”
- **Agents:** the current browser app uses its own structured JSON API; **WebMCP is not deployed for this maze as of the meeting**. Chrome's WebMCP feature exists as a separate early-preview evolving standard. No assumption that browser-native WebMCP must be available on all phones/browsers.
- **Participation and inclusion:** source includes a Nov 22 student worried about being away if an exam starts early; some players never submitted a challenge and others could not get peers at a door. Early discoverers and self-selected practice users aren't representative of the whole term. 500-person peak concurrency was **not yet reproduced with 500 actual students**; 30-bot production simulation != full-scale exam.
- **Community roles:** two or three solver makers are an instructor observation, not a verified roster of everyone who authored code. An after-meeting co-pilot announcement does not prove correctness. Never profile, rank, name or identify “silent”, “freeloading” or “complaining” students from private WhatsApp/Google Chat in the public page.
- **Learning and careers:** statements about closed-book Python quiz pass rates, percentage of work automatable or proportions of Straive hiring are speakers' anecdotes/rough estimates without independently verified denominators. Avoid headline charts built from them.
- **Privacy:** do not publish signed game receipts, maze personal keys, student emails, private Discord/WhatsApp/Google messages, unredacted agent conversations, research data keyed by learner, current vulnerability details, or maps/task questions for the upcoming exam.

## Visual and narrative challenge

Use **two or three** explanatory interactions, not an enormous dashboard. Strong candidates:
- **45-minute attention budget**, a small fictional floor plan with competing tasks, uncertainty, time costs and collaboration. Readers choose what to pursue and can discover why skipping is often rational. Label all task values and map as **illustrative, not the actual ROE**.
- **What does “3/3” measure?** A generic door/pad scene contrasts number of people who clicked and number of separate required conditions; shows a measurement mismatch. Be cautious: before the graded ROE, **do not reveal exact real-game internals** or make a reproduction of an unpatched issue.
- **Capture the vanishing signal**, an ephemeral system log appears once while a class wants to interpret it afterward. Readers choose between “organize now”, “save raw event and timestamp” and “ask AI later”; explain why loss is irreversible without external copies. Show that retention/privacy and useful organization still matter.
- **One strong student changes the denominator**, an explicitly hypothetical competitive-scoring slider contrasting absolute competence vs relative rank. This is a model of a proposed incentive, not current final course policy.
- **Community graph as roles**, a few fictional solver creators, many users, a missing maintainer organizing versions/tests, and a safe collaboration payoff. Use hypothetical individuals; never expose real social graph, WhatsApp participant IDs or pseudonymous player mappings.

The strongest graphic's title should be a finding, not a label. For example, **“The questions were easy after you found them”** (only if attempt data is clean) beats “Maze analysis”. **“The door counted clicks, not readiness”** (if verified and publication-safe) beats “Vault interface.” A reader must understand the piece even without interacting. Prefer visual metaphors and reader agency over decorative charts and stock illustrations.

**Comic-page.avif is already available; integrate it as an original illustrative work** with useful alt text and full-resolution viewing; do not regenerate or treat illustrative scenes as factual photographs. An appropriate tone is playful but never condescending to students (including the person who pressed the door many times).

## Experience and build quality

Produce a **genuine story↔video interface** at the quality of the 16, 9 and 2 November completed talks: a **single persistent media element** that doesn't lose play time when the view switches; precise chapter and quote time seeks; URL-deep-linked timestamps and back/forward navigation; chapter state synchronized with playback; captions/accessible transcript and source notes; great typography and responsive mobile layout; keyboard access, visible focus, reduced motion, high contrast, no autoplay and useful non-JS fallback for the narrative. Small custom interactions should be testable and keyboard-operable. The publication should be readable as an article even if media doesn't load.

**Correct video URL:** https://media.s-anand.net/2026-11-23-tds-course-ideation.webm ; local ~/r2/media/2026-11-23-tds-course-ideation.webm (58m45.875s, AV1 video/Opus audio/WebVTT captions). The user's hyphenated https://media-s-anand.net/... does **not** resolve. Remote video HEAD returns **audio/webm** content type; **test native browser playback, seeking and subtitles**. Audio backup: ./2026-11-23-tds-ideation.opus or https://github.com/sanand0/talks/releases/download/talks/2026-11-23-tds-ideation.opus (HEAD 200). Link to local transcript. Preserve the supplied comic and the **comic provenance comment above this fenced prompt**; do not publish its private ChatGPT chat URL.

**Independent external context**, use only as evidence and link to original: Chrome's early-preview WebMCP guidance, the 23 Nov 2026 WebML Community Group spec; Google SRE's “Monitoring Distributed Systems”; OpenTelemetry on instrumenting logs/metrics/traces; game-based assessment-alignment research in British Journal of Educational Technology. Full URLs and caveats are in links.md/research-notes.md. None of these externally validates TDS's learning impact.

## Deliverable boundary and verification gate

Before handing back a future finished page, independently verify:
- Chosen direct quotes/timecodes against embedded subtitles and video, not just the transcript.
- Event date labels and source lineage: live discussion vs 24 Nov practice findings vs hypothetical future exam.
- Exact counts/sample/denominators (including corrected 20/81 and 503 ordinary successes); numeric graphics not made up.
- No leaked secrets, live question answers, private social graph, personally identifying artifacts, unpatched exam workarounds, student records or screenshots that show hidden evaluation panels.
- Correct working media link and actual browser video/caption/seek behavior, including the remote MIME mismatch.
- Story↔video state persistence, URL history, keyboard/mobile focus, reduced motion, source link handling and comic full-size view.
- The central conclusion survives its strongest objection: **was this genuine human-agent decision-making, or a consequence of game affordances, self-selection and friction?**

Add catalog entry when done. Do not commit, push or deploy.
```

<!-- claude --model opus --effort medium --resume f7c5aea0-6582-48ea-8c75-80bdc68d0601 -->

## Metaprompt, 16 Nov 2026

<!-- https://chatgpt.com/c/6ad6b3d4-12a0-83ec-97b2-e792263fffb5 -->

Similarly, on @LocalMCP2 create JUST PROMPTS (and story context, links, sources, etc.) a new talk for the TDS course ideation session we had recently in ~/code/talks/2026-11-23-tds-ideation.
Keep this similar to the past talks we've had on TDS course ideation on Mondays.

The video https://media-s-anand.net/2026-11-23-tds-course-ideation.webm is also available locally at ~/r2/media/
The .opus file has been uploaded to GitHub releases.
comic-page.avif is available and was sourced from https://chatgpt.com/c/6b04d107-095c-83ec-9ccc-842d3e99d2ab
Relevant analysis: `~/Documents/chatgpt/TDS 2026 09 ROE Practice Maze Analysis.md`

~/code/{exam,tds-network-games,tools-in-data-science} have additional context.
Feel free to explore other repos, past ChatGPT chats at ~/Documents/{chatgpt,claude}/, student discussions at ~/Documents/data/whatsapp/ and ~/Documents/data/anand@study.iitm.ac.in, and any other sources.
Research online, fact-check, etc. like with previous stories.

Include the prompt, context, links, sources, etc. for Claude, nudging it to design similar to the previous talks.

prompts.md already exists. Insert the new prompt inside the same file, under the "Build Prompt" section.

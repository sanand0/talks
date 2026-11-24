# Links, assets and provenance — 23 November 2026 TDS course ideation

Prepared 24 Nov 2026 on LocalMCP2. Source shelf for a future Claude story, not a list of universally public-safe URLs. Keep first-party recording, private game analytics, student discussions and independent research distinct.

## Media and existing assets

| Item | Exact local path | Public reference / check |
|---|---|---|
| Full video | ~/r2/media/2026-11-23-tds-course-ideation.webm | **https://media.s-anand.net/2026-11-23-tds-course-ideation.webm** — HEAD 200 on 24 Nov |
| Audio | ./2026-11-23-tds-ideation.opus | **https://github.com/sanand0/talks/releases/download/talks/2026-11-23-tds-ideation.opus** — HEAD 200 after redirects |
| Dialogue and embedded chat | ./transcript.md | Local 462-line transcript with “## Chat” section appended at end |
| Comic | ./comic-page.avif | Existing, approximately 155 KB; do **not** regenerate or change |
| Claude instructions | ./prompts.md | Existing **## Build Prompt, 24 Nov 2026** includes a fenced placeholder; insert inside it; preserve **## Metaprompt, 16 Nov 2026** verbatim |
| Story context | ./story-context.md | Four-beat narrative, cast, timestamp map and possible visuals |
| Research notes | ./research-notes.md | Independently checked counts, fairness/validity caveats and references |
| This file | ./links.md | Authored for the prompt-only phase |

**The user-supplied video host is wrong:** https://media-s-anand.net/2026-11-23-tds-course-ideation.webm returned HTTP 000 on 24 Nov. Correct spelling is **media.s-anand.net**. The correct host returned HTTP 200 with **Content-Type audio/webm** despite containing an actual video stream. Browser-test playback, seek, caption track and duration; HTTP success alone is insufficient.

Local ffprobe of original file: **3525.875 seconds = 58m45.875s**, **1280×720 AV1 video**, **Opus audio**, **embedded WebVTT subtitles**, **64,845,195 bytes**. The recording closes shortly after ~58:37. GitHub Opus release URL resolved after redirects. No need to regenerate media or scrape redirect URLs.

**Comic source/provenance — authoring comment only, not a public reader link:** https://chatgpt.com/c/6b04d107-095c-83ec-9ccc-842d3e99d2ab . Source of original generated comic-page.avif. Do not publish the chat URL or regenerate the image.

**Future, not currently published:** https://talks.s-anand.net/2026-11-23-tds-ideation/ . The preparation should NOT create index.html or alter the talk catalog.

## The finished prior Monday talks — reuse behavior, not visual design

- **16 Nov, “The Score Can’t See Who Built the Solver”**: https://talks.s-anand.net/2026-11-16-tds-ideation/ ; local ../2026-11-16-tds-ideation/{index.html,prompts.md,story-context.md,links.md}.
- **9 Nov, “Who Watches the Deadline Watchers?”**: https://talks.s-anand.net/2026-11-09-tds-ideation/ ; local ../2026-11-09-tds-ideation/{index.html,prompts.md,story-context.md,links.md}.
- **2 Nov, “Should a Student Even Read the Exam?”**: https://talks.s-anand.net/2026-11-02-tds-ideation/ ; local ../2026-11-02-tds-ideation/{index.html,prompts.md}.
- **19 Oct, “The Exam Has to Pass Its Own Exam”**: https://talks.s-anand.net/2026-10-19-tds-ideation/ ; local ../2026-10-19-tds-ideation/{index.html,prompts.md}.
- **12 Oct, “The Exam Is a Hypothesis”**: https://talks.s-anand.net/2026-10-12-tds-ideation/ ; local ../2026-10-12-tds-ideation/{index.html,prompts.md}.
- **5 Oct, TDS orientation**: https://talks.s-anand.net/2026-10-05-tds-orientation/ ; local ../2026-10-05-tds-orientation/{index.html,prompts.md}.
- Other story/video precedents: ../2026-11-17-sutd-coil/index.html and ../2026-11-21-sutd-cv-workshop/index.html if present.
- Source of talk catalog format: ~/code/talks/README.md; **do not edit it in prompt-only phase**.

Borrow the working story↔video toggle, persistent player and captions, in-paragraph timecode seeks, URL-deep-linked position, synchronized chapter state, comic lightbox and accessibility. Do not copy their colors/CSS/hero structure.

## Course and maze source — local, mostly not suitable for public linking

- **Course:** https://tds.s-anand.net/ ; actual checkout ~/code/tools-in-data-science-public/2026-09/ ; public repository https://github.com/sanand0/tools-in-data-science-public . The user's older ~/code/tools-in-data-science/ folder does **not** exist on this LocalMCP2 device.
- **Practice exam source:** ~/code/exam/src/exam-tds-2026-09-roe-practice.info.js (clearly says practice carries **no marks**), q-maze-practice.js, a-maze-practice.js. The “real ROE Sunday 29 November” statement is from that student-facing instruction, not from a final audited scored schedule.
- **Student-shared practice link:** https://exam.sanand.workers.dev/tds-2026-09-roe-practice — anonymous HEAD returned **HTTP 404 application/json** on 24 Nov. This does not prove authenticated student access fails. Don't promise publicly open access.
- **Game repo:** ~/code/tds-network-games/ ; first-party public-facing design/QA guide MAZE.md; design conversation prompts.md, “ROE Maze, 23 Nov 2026” and separate “ROE Maze Enhancements, #TODO”. Relevant private code: src/maze/{rules.ts,engine.ts,router.ts,worlds/practice.ts,worlds/roe.ts}. Do not publish privileged map, personalized answer validation, identity-auth routes, unreleased puzzles or precise active vulnerabilities.
- **Local synced first-day game data:** ~/code/tds-network-games/.private/maze/practice-sandbox/{players.csv,answers.jsonl,events.jsonl,notes.jsonl,chat.jsonl,summary.json,metrics.json,manifest.json}. Raw student identifiers and answers are private; aggregate only. Independently checked 92 accounts / 81 student-address accounts, 20 student scores at least 23, five at 27, 503 ordinary task successful pairs, 1,832 vault presses and one 1,041-push outlier. The exact attempt-denominator interpretation requires additional work.
- **Explicitly supplied retrospective:** ~/Documents/chatgpt/TDS 2026 09 ROE Practice Maze Analysis.md, authored 24 Nov after meeting; its opening plot has erroneous counts later corrected in the same document. Corrected **20/81 (23+ points)** and **503/520 (operationally defined task attempts)**. The corresponding private ChatGPT URL https://chatgpt.com/c/6b04d3ed-ca7c-83ec-92b2-3a34afd3eb73 should remain private.
- **Older ideation, not a deployed mechanism:** ~/Documents/claude/TDS ROE donate marks question.md, July 2026, explores incentive networks; unrelated mechanisms must not be presented as deployed maze features.

## Timeline of the 23 November call (video time; confirm with captions)

| Time | Voice/context | What to check |
|---|---|---|
| 00:08–01:54 | Anand, Hritik | Practice noticed early; agent can solve much; three-person group door |
| 01:54–06:30 | Anand | Approximately 45 minutes, more tasks than time, abandon/choose/coordinate |
| 06:54 | Anand | Practice earns **zero course marks** |
| 08:41–09:40 | Hritik, Anand | Leaked link, scanning announcements, HFT analogy |
| 10:49–11:55 | Hritik, Anand | WebMCP absent; currently JSON API; possible future change |
| 12:33–13:40 | JK, Anand | “Rat race” collaboration and relative top-score denominator |
| 14:07–18:49 | JK, Anand | Few solver makers, larger testers/supporters, silent audience; missing maintainer/organizer |
| 18:49–21:00 | Anand | Approx 26 early participants, 20 apparently full on-screen; **not** the 24 Nov cohort |
| 21:14–27:53 | JK, Anand | Agent-log sharing proposal, reflection, SUTD workshop student learnings |
| 29:59–34:54 | Anand, JK | Collect puzzle pieces, ephemeral data, observability |
| 35:21–40:55 | JK, Anand | Organizing/permissions versus retrieval; learning to ask valuable questions |
| 40:55–47:07 | Anand, JK | Agent boundary, judgments, decisions in rapid succession |
| 47:07–49:15 | Anand | Hiring/institutional inertia; anecdotes, not verified labor-market trends |
| 49:15–51:39 | JK, Anand | Zork / classic adventure game cultural references |
| 51:39–57:02 | Carlton, Anand, JK, Hritik | Real-world outcomes, proposed next Monday student TA evidence |
| 57:02–58:45 | Anand, JK | Private network-analysis discussion, signoff |

Embedded transcript chat includes:
- Preethi ~00:11 asks how many ROE questions; JK replies many.
- Hritik ~00:17 reports practice discovery and solver progress.
- Hritik ~00:43 asks if a deployment was committed; Anand says pushed exam repo.
- Hritik ~00:51:35 links https://github.com/sanand0/exam/pull/167 (verify contents before discussing); Preethi identifies TV show “The Apprentice” at ~00:52:34.

## Student discussion sources, all private unless explicitly made public

- **WhatsApp TDS Sept 2026**: ~/Documents/data/whatsapp/TDS _ Sept 2026 [120363430988346355@g.us].jsonl . Scope to Nov 22–24 for ROE, maze, vault, practice, key, door. A Nov 22 comment fears a surprise exam because its author is away from home; 23 Nov students share practice link and discuss the group-door problem, puzzle questions and archive. Paraphrase anonymously; do not copy phone numbers or student IDs.
- **IITM Google Chat Nov 2026**: ~/Documents/data/anand@study.iitm.ac.in/chat-2026-11.jsonl . Filter space_name = TDS 2026, Nov 22–24. Students coordinate an upcoming timed practice session and share an experimental maze co-pilot late on 23 Nov, after the recorded meeting. Do not publish private Chat room links, message IDs, sender IDs, raw instructions to access agent API or private source content.
- **Private chat analysis:** source retrospect in ~/Documents/chatgpt/ above; downstream observations happened after the meeting. A post-meeting student product announcement is not a proven benchmark. Avoid names when unnecessary.

## Independent online references checked for conceptual grounding

- **WebMCP and browser support:** Chrome early-preview guide https://developer.chrome.com/docs/modern-web-guidance/guides/webmcp/webmcp ; WebML Community Group draft dated **23 Nov 2026** https://webmachinelearning.github.io/webmcp/ . Neither implies the practice maze already supported WebMCP.
- **Observability:** Google SRE “Monitoring Distributed Systems” https://sre.google/sre-book/monitoring-distributed-systems/ and OpenTelemetry's official instrumentation https://opentelemetry.io/docs/concepts/instrumentation/ and observability primer https://opentelemetry.io/docs/concepts/observability-primer/ . Emitted/captured data and signal correlation underpin troubleshooting.
- **Valid game assessment:** “Measuring learning in digital games: Applying a game-based assessment framework” https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13407 . An authentic game has to align the actual observed behavior with the intended competency.
- **Team game learning:** “Learning teamwork through a computer game: for the sake of performance or collaborative learning?” https://link.springer.com/article/10.1007/s11423-021-10009-4 . Team score and teamwork skill are not the same construct.
- **Classic games Zork / Colossal Cave / Carmen Sandiego:** mentioned in the conversation, do not embed copyrighted artwork, screenshots, movies or audio in the public story without rights.

## Boundaries for Claude's future build

The scored ROE is scheduled **days after this meeting**. Do not publish unreleased questions, map seeds/routes, answers, signed codes, server/admin routes, personalized student records, raw agent logs or unpatched gate conditions. Cite **23 Nov meeting**, **23 Nov evening student posts**, **24 Nov retrospective** and **planned 29 Nov ROE** separately. If publication is before the scored ROE, favor a synthetic model, rather than an interactive replica of real puzzles.

Only once the page is built, tested and explicitly published later may the catalog add: Monday 23 Nov 2026, TDS Course Ideation — Open Design Meeting, Sep 2026 cohort, Remote; possible title **“The Rat Race Has a Team Door”**, page https://talks.s-anand.net/2026-11-23-tds-ideation/ (not presently live), video/audio URLs above, transcript.md and comic-page.avif. **No README edit, commit, push or publication during this task.**


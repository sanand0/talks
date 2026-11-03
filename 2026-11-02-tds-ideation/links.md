# Links, media, citations and source trail — TDS ideation, 2 Nov 2026

**Authoring references checked 3 November 2026 on graphene; not all belong in the public story.** Keep public-safe sources separate from private code/data/transcripts. Do not assume a proposed page has already been built/published. If a published asset URL fails later, recheck rather than invent replacements.

## Ready-made local media and public URLs

| Role | Existing local path | Public URL or publication status |
|---|---|---|
| **Main video** | ~/r2/media/2026-11-02-tds-course-ideation.webm | **https://media.s-anand.net/2026-11-02-tds-course-ideation.webm** — HEAD HTTP **200** on 3 Nov. See content-type caveat. |
| **Audio / fallback** | ./2026-11-02-tds-ideation.opus | **https://github.com/sanand0/talks/releases/download/talks/2026-11-02-tds-ideation.opus** — GitHub release responded HTTP **200** after redirects. |
| **Annotated transcript** | ./transcript.md | Relative transcript.md in the future published page. Current speaker/timing text, not a reliable word-for-word VTT. |
| **Meeting chat** | ./chat.md | Timestamped chat export. Anchors: Adwitiya's “Prompt guides per session?” (15:43), talks homepage (19:28), Jivraj's VS Code dictation note (33:52), Humans Only link (37:47), verification-techniques link (41:55), and Kartikkumar's GA3/token-budget questions (48:03, 48:48). Use as contemporaneous evidence, not a replacement for spoken transcript. |
| **Comic** | ./comic-page.avif | Relative comic-page.avif; pre-existing. Needs meaningful alt and accessible full-size opening. |
| **Main Claude build prompt** | ./prompts.md | Already prepared; contains the comic's private authoring URL in HTML comments. |
| **Narrative map** | ./story-context.md | Working editorial context. |
| **Research shelf** | ./research-notes.md | Evidence, corrections and counterarguments. |
| **Source map** | ./links.md | This file. |

The local WebM: **3944.917 seconds (65m44.917s)**, **1280×720 AV1 video**, **Opus audio**, embedded **English WebVTT subtitles (stream 2)** with speaker labels. The embedded captions' final dialogue ends near **61:40**, while the container continues for ~4 more minutes; verify the final segment when building. The Opus local file independently reports about **3944.891 seconds** and ~5.7 MB. The remote video HEAD returned **Content-Type: audio/webm** despite containing video according to local ffprobe. Check full response, browser video playback, seeking, and subtitle delivery during the build; HTTP 200 alone isn't a playback test.

**Comic authoring/provenance only; DO NOT include in the public page:** https://chatgpt.com/c/6ae9957e-203c-83ec-b56d-06021617e8da . This is explicitly in prompts.md as an HTML comment, matching previous Monday talks. The comic is not a substitute for the actual recording in verifying what was said.

## Previous Monday episodes and design references

- **5 October TDS orientation:** https://talks.s-anand.net/2026-10-05-tds-orientation/ — agent-enabled learning philosophy and the course's unusual exam rules. Local ../2026-10-05-tds-orientation/{index.html,prompts.md,story-context.md}.
- **12 October open ideation:** https://talks.s-anand.net/2026-10-12-tds-ideation/ — the instructors propose grading work that agents can also do; students question validity. Local ../2026-10-12-tds-ideation/{index.html,prompts.md,story-context.md,research-notes.md,links.md}.
- **19 October ideation:** https://talks.s-anand.net/2026-10-19-tds-ideation/ — from blueprints to running markets, Human Exchange/Air Ink, costs of verification, Tangram failures. Local ../2026-10-19-tds-ideation/{index.html,prompts.md,story-context.md,research-notes.md,links.md}.
- **7 October IITM ED data visualization session:** https://talks.s-anand.net/2026-10-07-iitm-ed-data-visualization/ — good story/video interactivity reference, not a Monday TDS ideation episode.
- **Older 10 August TDS AMA:** https://talks.s-anand.net/2026-08-10-tds-ama/ — student engagement/background.
- **Future page (NOT built or currently established as live):** https://talks.s-anand.net/2026-11-02-tds-ideation/ .

Look at the older source HTML and prompts for **functional patterns**: story ↔ video switching without remounting the media, in-text seek timestamps and shareable URLs, chapter rail and synchronized highlighting, video playback captions, transcripts, mobile/keyboard accessibility, full-size comic. Reuse mechanics as appropriate; create a **distinct editorial design** for this session.

## TDS course, exams, games, public pages

- **Official course:** https://tds.s-anand.net/
- **Current September 2026 course source:** https://github.com/sanand0/tools-in-data-science-public ; local ~/code/tools-in-data-science-public/2026-09/ . This repo is available but the alternate ~/code/tools-in-data-science/ path does NOT exist on graphene.
- **Public course index:** ~/code/tools-in-data-science-public/2026-09/README.md (a link to a guidebook.md exists at line ~13, but the local file was **missing** on 3 Nov; do not assert it was successfully published until independently checked).
- **Personalized exam pages (entry links only, never reuse or publish user-specific tokens):** https://exam.sanand.workers.dev/tds-2026-09-p1 ; https://exam.sanand.workers.dev/tds-2026-09-ga3 ; https://exam.sanand.workers.dev/tds-2026-09-ga4 .
- **TDS game home (check its current route before using):** https://tds-network-games.sanand.workers.dev/ ; local ~/code/tds-network-games/ . The source has market, Human Exchange, Humans Only and face-review logic; do NOT guess individual game deep-link syntax from internal IDs.
- **Prediction-market implementation guide:** ~/code/tds-network-games/PREDICTION-MARKETS.md ; relevant source ~/code/tds-network-games/src/prediction/markets.ts . Documents evolving **2–8 Nov 2026** AI Pipe USD aggregate cost market, virtual credits and scoring caveats.
- **AI Pipe aggregate public usage feed:** https://stats.aipipe.org/usage.json — source for dated spend observations, not a live account-limit audit nor proof of individual forecast quality.
- **Exam engine:** ~/code/exam/src/ (relevant P1 and GA3/GA4 question modules and question info files). Private parts include answer verification and student accounts; cite only what safely documents public question behavior.
- **Human Exchange:** ~/code/tds-network-games/src/trading/games/human-exchange/index.ts ; public portal through P1. Round 1 status and planned round 2 must be dated; cannot cite a future launch until live.
- **GA4 peer review:** ~/code/exam/src/exam-tds-2026-09-ga4.info.js ; includes review task and 11 Nov deadline, with “more questions to be added.” Do not link private authentication/assessment answers.
- **Humans Only public results:** https://files.s-anand.net/pages/tds-2026-09-ga3-q5-humans-only/ — exact link shared by Anand in meeting **chat.md at 37:47**, verified HTTP 200 text/html on 3 Nov. Use this rather than inventing a gallery link.
- **Humans Only game and research:** ~/code/exam/src/q-trading-humans-only.js ; ~/code/tds-network-games/.private/trading/humans-only/{story.md,README.md,grading-insights.json,examples/,site/,scripts/}. **Private data:** only carefully anonymized and licensed public exports should be copied to the story. The local site/ is not proof of a live public URL; check the host before linking or embedding.
- **Drawing/face/morphing questions:** ~/code/exam/src/{q-3d-face-model.js,q-face-morph-video.js,q-face-morph-rank.js} ; review source ~/code/tds-network-games/FACE-REVIEW.md ; don't copy private student submissions or likenesses.
- **Personal prompt archive insights:** ~/code/blog/posts/2026/52-ways-i-specify-and-verify-agents.md ; linked to public page below.

## Public companion materials (safe to link when useful)

- **52 Ways I Specify and Verify Agents** (the author published it later on 2 Nov, after the open TDS session): https://www.s-anand.net/blog/52-ways-i-specify-and-verify-agents/ . The local front matter gives **2 Nov 2026 20:20:52 IST**. This is a companion to the underlying research shown in the talk, not a page proven visible during the talk.
- **Interactive techniques:** https://files.s-anand.net/pages/verification-techniques/ ; modes for **specify** and **verify**, 30+22 techniques. Exact URL posted by Anand in **chat.md at 41:55**, verified HTTP 200 on 3 Nov. Useful example deep links:
  - https://files.s-anand.net/pages/verification-techniques/#?m=specify
  - https://files.s-anand.net/pages/verification-techniques/#?m=verify
- **Earlier public explanation:** https://www.s-anand.net/blog/how-i-use-ai-to-teach/ .
- **April 2026 TDS Project 1 experiment (different cohort):** https://www.s-anand.net/blog/tds-project-1-was-an-experiment/ . This demonstrates earlier experience with real student projects/skill transfer, but is not a data source for the 2 Nov cohort.

## Research / primary external sources used to fact-check

- **AI help versus student learning (controlled field study):** Bastani et al., PNAS 2025, https://doi.org/10.1073/pnas.2422633122 ; open version https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ .
- **Cognitive apprenticeship; making expert thinking visible:** Collins, Brown & Holum, American Educator 1991, https://www.aft.org/ae/winter1991/collins_brown_holum .
- **Benchmark checks themselves can misjudge specifications; preprint, 12 Oct 2026:** Zhong et al., https://arxiv.org/abs/2610.16870 .
- **Classroom assessment validity/fairness:** NCME standards https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/ .
- **Prediction-market manipulation field work; external analogy only:** Rasooly & Rozzi 2025, https://arxiv.org/abs/2503.03312 .
- **Official Omarchy website:** https://omarchy.org/ ; source https://github.com/omacom/omarchy . These confirm the agent-friendly Arch-based product; **NOT** the speculative SpaceX funding remarks.
- **Patrick Collison's personal “liquid software” post dated 31 October 2026:** https://x.com/patrickc/status/2116636967517798672 ; independently readable mirror https://xitter.cf/patrickc/status/2116636967517798672 . This is an anecdote about personal applications, **not** a Stripe feature.

## Additional private context locations for the author (selective, not public citations)

- ~/Documents/chatgpt/TDS Guidebook and Context.md — origin of the guidebook project, includes first-hand notes on sources and intentions.
- ~/Documents/chatgpt/TDS 2026 09 GA3 Humans Only Evaluation.md — how the game was evaluated, grading and closeout action items.
- ~/Documents/chatgpt/TDS Questions Prioritization.md — how implementation difficulty and learning objectives shaped question selection.
- ~/Documents/chatgpt/TDS Designing Agent Resistant Assessments Meh.md ; TDS 2026 09 GA3 Ideation.md ; TDS Evaluating Evals.md — design hypotheses and failures (many may now be stale).
- ~/Documents/chatgpt/ plus ~/Documents/claude/ — earlier interactions. Search for actual evidence and dated choices; do not publish chat transcripts/identifiers just because they are accessible.
- ~/Dropbox/notes/iitm-tds-tools-in-data-science.md and ~/Dropbox/notes/transcripts/ when available — course philosophy and dated sessions; validate on disk if used.
- ~/code/blog/ and ~/code/research/ for public descriptions and reusable demonstrations; do not rely on generated/temporary content as original evidence.

## Privacy, citations, status and later catalog entry

**Do not expose:** unpublished exam tasks, question keys, grader logic that would leak answers, personal student IDs/names/emails without clear public context, signed URLs or JWTs, private results and images, student offers or recordings, confidential company information, unpublished chats, sensitive admin screen shots, GitHub release signed redirect query parameters. Even if some appears in a public video, prefer redacted/cropped visual evidence rather than amplifying it.

For a public claim, give the source and date. Distinguish *the speaker stated*, *the current repo says*, *independently checked*, *proposed*, *hypothetical example*; later code can differ from 2 Nov classroom state. Verify direct quotes and timestamps with **original WebM/captions**. Avoid unattributed copyrighted material and unlicensed visuals.

**Future metadata only (don't modify config during this prompt-only task):** Monday **2 Nov 2026**; TDS Course Ideation — Open Design Meeting, September 2026 cohort; Remote; working title *Should a Student Even Read the Exam?*; video https://media.s-anand.net/2026-11-02-tds-course-ideation.webm ; audio https://github.com/sanand0/talks/releases/download/talks/2026-11-02-tds-ideation.opus ; transcript 2026-11-02-tds-ideation/transcript.md ; comic 2026-11-02-tds-ideation/comic-page.avif ; eventual public page **https://talks.s-anand.net/2026-11-02-tds-ideation/**. No page is created by this preparation task.

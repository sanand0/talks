# Links and original source map — 16 November 2026 TDS course ideation

Prepared on **17 Nov 2026**. This is a **source shelf for Claude**, not a public story and not proof every private source can be published. We explicitly distinguish primary recording, current/recomputed local data, subsequent private analyses, and independent public sources. Do not modify source repositories or reuse private URLs containing student data.

## Media: verified local copies and public addresses

| Asset | Local path | Verified public link / issue |
|---|---|---|
| Main video | ~/r2/media/2026-11-16-tds-course-ideation.webm | **https://media.s-anand.net/2026-11-16-tds-course-ideation.webm** — HEAD HTTP 200 on 17 Nov; see MIME caveat |
| Audio fallback | ./2026-11-16-tds-ideation.opus | **https://github.com/sanand0/talks/releases/download/talks/2026-11-16-tds-ideation.opus** — HTTP 200 after redirects |
| Full transcript **and chat** | ./transcript.md | Current 833-line annotated transcript; meeting-chat snippets and links appended near bottom under “## Chat” and “## Links” |
| Comic | ./comic-page.avif | Already present, ~174 KB; use it, do **not** regenerate or modify |
| Build prompt | ./prompts.md | Existing author file; put new instructions under **## Build Prompt, 17 Nov 2026** while preserving **## Metaprompt, 16 Nov 2026** |
| Story context | ./story-context.md | Editorial map, detailed time anchors and speaker roles |
| Research shelf | ./research-notes.md | Verification/contradictions, original-code paths and external sources |
| Source map | ./links.md | This file |

**Critical URL correction:** the user-supplied https://media-s-anand.net/2026-11-16-tds-course-ideation.webm, a hyphenated domain, **did not resolve** (HTTP 000 on 17 Nov). The correct dot-subdomain **media.s-anand.net** returned 200. The remote content-type is **audio/webm** even though ffprobe on local media confirms 1280×720 AV1 video, Opus audio and embedded WebVTT subtitles. **Test browser video playback, seeking and captions** before publication; HTTP success alone is insufficient.

Local ffprobe: duration **4014.000 seconds = 66m54s**, local video **70,712,144 bytes**. Do not reuse the 9 Nov talk's 77m48s duration. There is a transcription timestamp reset to **[00:00] inside the transcript near ~50m**, not a second video or actual return to start; use actual video/VTT time codes.

**Comic creation provenance only in prompt comments (NOT a public link):** https://chatgpt.com/c/6afb28b0-d100-83ec-b3bb-54cadbca5eca .

**Future publication URL (NOT confirmed live):** https://talks.s-anand.net/2026-11-16-tds-ideation/ . Suggested event: TDS Course Ideation — Open Design Meeting, September 2026 cohort, Remote; date Monday 16 Nov. Page/README entry only after future Claude build, not in this prompt-only task.

## Previous Monday episodes and visual/interaction standards

Use **actual rendered HTML and prompts** to see quality, not text descriptions alone:

- **9 Nov — “Who Watches the Deadline Watchers?”**: https://talks.s-anand.net/2026-11-09-tds-ideation/ ; local ../2026-11-09-tds-ideation/{index.html,prompts.md,story-context.md,research-notes.md,links.md}. Direct predecessor, timing/agency/fairness questions.
- **2 Nov — “Should a Student Even Read the Exam?”**: https://talks.s-anand.net/2026-11-02-tds-ideation/ ; local ../2026-11-02-tds-ideation/{index.html,prompts.md,story-context.md,research-notes.md,links.md}.
- **19 Oct — “The Exam Has to Pass Its Own Exam”**: https://talks.s-anand.net/2026-10-19-tds-ideation/ ; local ../2026-10-19-tds-ideation/{index.html,prompts.md,story-context.md,links.md}.
- **12 Oct — “The Exam Is a Hypothesis”**: https://talks.s-anand.net/2026-10-12-tds-ideation/ ; local ../2026-10-12-tds-ideation/{index.html,prompts.md}.
- **5 Oct — TDS orientation**: https://talks.s-anand.net/2026-10-05-tds-orientation/ ; local ../2026-10-05-tds-orientation/{index.html,prompts.md}.
- Another similar high-quality story/video: ../2026-10-07-iitm-ed-data-visualization/{index.html,prompts.md}.
- Talk catalog conventions: ~/code/talks/README.md. Do not edit during prompt preparation.

Borrow **persistent video across story↔video mode, seekable timestamp citations, URL-deep-linked time, chapters and captions, mobile/keyboard, full-size comic and verified source links**. **Do not clone CSS, visual theme, headline or chapter layout.**

## Exact first-party public URLs named in 16 Nov meeting

1. **Picture Stories public data/interactive gallery**, posted at chat ~19:57 and again ~66m: https://files.s-anand.net/pages/tds-2026-09-p1-q7-picture-stories/ ; patterns deep link https://files.s-anand.net/pages/tds-2026-09-p1-q7-picture-stories/?tab=patterns . **HEAD 200 on 17 Nov**, use public-safe imagery only.
2. **Original author blog, 7 Nov — Picture Stories We Understand and Like:** https://www.s-anand.net/blog/picture-stories-we-understand-and-like/ ; confirms 3 evaluation criteria and reports within-cohort negative uniqueness/preference association, with author's caution. Verified via current web search on 17 Nov.
3. **P1 face classifier public question context:** https://exam.sanand.workers.dev/tds-2026-09-p1#hq-face-expression-classifier ; login may be required; do not expose personal sign-in URLs or answers.
4. **GA3 3D face public question context:** https://exam.sanand.workers.dev/tds-2026-09-ga3#hq-3d-face-model ; official task details may be account gated.
5. **Invisible Ink test/game public landing page:** https://tds-network-games.sanand.workers.dev/realtime/air-ink-classifier/ ; auth may be required. Do not link a test dataset or secret answer key.
6. **Shrikar solver public GitHub repository**, pasted in chat at ~46:18: https://github.com/sreekarsarma55/temp-repo — **HEAD 200 on 17 Nov**; its presence does **not** prove the program runs well or identifies the student's legal name. It was not executed during the session.
7. **Helpful Claude artifact**, submitted by Preethi in chat ~47:56: https://claude.ai/artifact/Qs2N2ZyM91NFcA1Nuf34hp . Link may require sign-in, not verified as identical to Adwitiya's solver; preserve author distinction.
8. **Private TDS G-Space Google Chat link** posted ~43:52: inside transcript's chat. **Do not publish** private space/room identifiers; refer to “the student group” instead.
9. **Talks homepage** requested and shared at close: https://talks.s-anand.net/ .

## Local repositories and reproducible data

**Read only — do not alter assessment source, private data or secrets.**

- Exam: ~/code/exam/ ; GA4 source ~/code/exam/src/exam-tds-2026-09-ga4.info.js, q-food-court-discount.js, q-time-use-charts.js, q-ga4-face-peer-review-server.js. P1 source ~/code/exam/src/exam-tds-2026-09-p1.js ; specific q-prediction-aipipe-server.js and face-expression modules; inspect repo file discovery rather than assume static names.
- Network games: ~/code/tds-network-games/ ; documented Food Court model ~/code/tds-network-games/REALTIME-GAMES.md; realtime game logic src/realtime/games/food-court/{model.ts,game.ts}; actual synced results **.private/realtime/food-court/**, including 15 Nov AIPL (1200, 1230, 1300 SGT) and 10–11 Nov IITM sessions. Do not expose raw CSV emails, room identities, chat transcripts or admin URLs.
- **Independently checked aggregated team means (unique rooms):** AIPL first session **7 rooms/32 players, 88.06**; TDS sessions 61 rooms/247 players **92.51**, 25/106 **95.57**, 75/305 **94.13**. The separate private local chatgpt-chat-aipl-session.md compares first session's checkpoint descent (~92→~86), discount aggressiveness, chat and save events. Cite source and sample; not randomized.
- Prediction game: ~/code/tds-network-games/PREDICTION-MARKETS.md, src/prediction/markets.ts and relevant private prediction ledgers. Spoken 16 Nov outcome ~$5.31 vs private later ledger $5.3063. Don't join inconsistent **242 final** (meeting) vs **262 final** (different analysis population/cutoff) without reconciliation.
- Picture Story actual game data/site: ~/code/tds-network-games/src/trading/games/picture-story/ ; published gallery as above, no need to copy private raw student images.
- Air Ink / Invisible Ink: ~/code/tds-network-games/src/realtime/air-ink/ ; P1 source and the public student solver URLs listed above. Avoid revealing private hidden test codes, student drawing metadata or face dataset.
- **GA3 peer scoring decision**: ~/code/exam/.private/ga3-q6-q8-finalization-2026-11-16/{README.md,ga3-q6-q8-bonuses.tsv}. Contains selected min–max-scaled Bradley–Terry marks and audits, private student identifiers, and a changed Q8 peer-difficulty proxy. Use aggregate/abstract example only. Private source documents show the TDS team was asked to review/apply, not that scores were definitely already posted in live gradebook.
- **GA4/P1 scoring review**: ~/code/exam/.private/ga4-p1-scoring-review-2026-11-16/{review-summary.md,summary.json} ; reviews incomplete/poster marks pending. Private data should not become public downloads.
- Course: ~/code/tools-in-data-science-public/2026-09/ (actual checkout). **~/code/tools-in-data-science/** does NOT exist here. Public source: https://github.com/sanand0/tools-in-data-science-public ; course website https://tds.s-anand.net/.

## Supplied private conversational research, already placed beside this talk

- **./chatgpt-chat-aipl-session.md** — 15 Nov Food Court AIPL deployment and first session analysis; seven first-session rooms, team discount/payoff, saved plan and chat behavior, user comments on interface. Its exact data are corroborated in some aggregates by local results files.
- **./chatgpt-chat-ga3-p1-closure.md** — 16 Nov GA3 Q6–Q8 peer-review score discussions, comparison of scoring methods, selected scaled Bradley–Terry, different “no usable media” handling, Drive upload and email for TA review; some other GA4/P1 marks still pending.
- **./chatgpt-chat-student-learning.md** — 16 Nov retrospective of what students might have learned from every P1/GA4 question; later details on **2–8 Nov AI Pipe** forecast histories and verified/unverified evidence of solver collaboration and other forms of “learning”. Contains private student IDs/emails in deep sections: **never reproduce those publicly**.
- Additional archives: ~/Documents/chatgpt/ and ~/Documents/claude/ (TDS and ROE notes), ~/Dropbox/notes/ transcripts when needed. Use narrow topical search and confirm dates before importing context. User-uploaded data aren't public just because they appear in model context.

## Independent research and source-correcting links

- **Anthropic primary announcement dated 9 Nov 2026:** https://www.anthropic.com/claude-fable-and-mythos-5-2 ; documentation https://platform.claude.com/docs/en/release-notes/overview ; confirms Claude **Fable 5.2** is a real released model as of the meeting. **Does not independently verify Adwitiya's tool.**
- **Bradley–Terry model** theoretical reference: https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model ; assessment tutorial https://www.acer.org/files/Tutorial-13--Pairwise-comparisons.pdf (inspect directly before using PDF claims). Relative wins account for opponent strength with assumptions; not “Google PageRank for images.”
- **Google Cloud service-specific terms, Oct 2026:** https://cloud.google.com/legal/archive/terms/service-terms/index-20261030 ; corresponding indemnified service list https://cloud.google.com/terms/generative-ai-indemnified-services . Eligible generated-output IP indemnity is *conditional*; no blanket legal immunity for all generated media, clients or cultural/regulatory risks.
- **Published creator analysis:** https://www.s-anand.net/blog/picture-stories-we-understand-and-like/ ; primary for originality/understanding/preference dimensions and within-sample trends. No external causal preference study is required to tell the story; don't invent one.
- **Education research on learning transfer/assessment validity**: National Council on Measurement in Education classroom assessment standards https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/ ; and EEF evidence https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/metacognition-and-self-regulation . These provide cautious methodological context, not causal evidence about this one meeting.

## Editorial risks and publication checks

1. **Never publish** student grades or IDs, private comparison exports, signed links/JWTs, exam answer keys, personally identifying face datasets, private Google Chat room URLs, client identities, or copied confidential messages. Redact screenshots of graders, accounts and scoreboards.
2. A public story may quote short accurate lines from the **meeting recording** with timestamp and attribution; verify exact wording against WebVTT, not only transcript. The transcript contains a **false [00:00] reset near 50 minutes**.
3. Video/opus verified by HEAD; remote video MIME mismatch remains. Test actual browser seeks and subtitles. If HTML 404s before Claude build, that is expected.
4. Future experimental ROE design is **not shipped**. Future site entry only after build, with accurate media and source links.
5. Claim provenance always: **speaker said / local first-party code / computed local aggregate / later private retrospective / third-party documentation / hypothetical example**. A large corpus doesn't erase a poor denominator.


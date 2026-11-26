# Research notes and provenance — 4 Nov 2026 IITM BS Insider podcast

For Claude Code's research and fact-checking, not public copy. Research conducted 26 Nov 2026.

## Sources

| Source | What it establishes |
|---|---|
| ~/Downloads/wide-shot-full.webm and wide-shot-qna.webm | Raw evidence, audio Opus stereo. ffprobe durations 2893.920 and 1166.408 seconds. |
| transcript.md | Fresh Gemini 3.8 Flash pass using the exact prompt from ~/code/blog/pages/prompts/transcribe-call-recording.md plus participant context, in ten 7-minute-or-shorter audio excerpts. Cleaned speaker labels, bolded key passages, continuous timestamps. Compared independently generated text with previous pass: normalized token alignment 95.2% interview / 91.3% Q&A; no substantive missing blocks detected. These are agreement rates, not accuracy estimates. Targeted rechecks of founding, grader and dropdown excerpts; Japanese excerpt recheck timed out. No human listening/visual screen verification. |
| Gmail thread 1a19ac676907f73b (root.node@gmail.com), subject Invitation to the IITM Insider BS Podcast | 2 Nov invitation and confirmation of 4 Nov, 11:30–12:45 IST; 3 Nov experiment plans; 4 Nov student feedback and final questions. Full thread retrieved with gws. |
| WhatsApp export ~/Documents/data/whatsapp/Komali [919030743344@s.whatsapp.net].jsonl | 4 Nov 04:51–05:56 UTC coordination, DoMS; 5 Nov raw recording request; 11 Nov delivery; 12 Nov download confirmation. Keep identifiers/private links out of story. |
| Google Calendar, 4 Nov event IITM BS podcast | Booked 14:00–15:30 SGT = 11:30–13:00 IST. Scheduled rather than observed time. |
| ~/Documents/chatgpt/Kusuma IITM BS Podcast Experiments and Questions.md | Preparation, historical examples, branch deployment, original question variants and historical performance, lines ~1606–1792, AI grader examples ~1839 and ~1950–2031. Verify results against code/archive if using numbers. |
| ~/Documents/chatgpt/Kusuma IITM BS Podcast student feedback.md | Curated positive and negative student reactions, linked source posts. Not necessarily used on camera. |
| ~/code/exam/src/exam-podcast-2026-11-04{,.info}.js and question files | Exact assessment structure and rules, commit fd10a98 (7 Nov). Prep chat records earlier live branch deployment 21dae46; use code plus recording to distinguish actually attempted items. |
| ~/code/exam/dumps/exam-archive.sqlite3 | Read-only aggregate check of canonical results/log tables. |
| Public web search 26 Nov | Confirmed official IITM course page, current course site, 2 Nov blog on specification/verification and published NCERT chapter overview. No episode-specific public video link established. |
| ~/code/talks/.claude/skills/talk-story/SKILL.md and prompt-template.md | Narrative style, QA, media and catalog conventions. Follow when producing HTML, not at this preparation stage. |

## Podcast assessment

URL https://exam.sanand.workers.dev/podcast-2026-11-04. Instructions: “Play, experiment, and use AI or other people. Check what works.” Not a TDS assessment, no course credit. Window 4 Nov 08:30 IST to 7 Nov 08:30 IST. Seven one-mark questions and a zero-mark prediction activity (final receipt only after settlement). Do not turn this historical list into a claim all eight were attempted.

| # | Assessment | Teaching idea | Evidence of use in footage |
|---|---|---|---|
| 1 | Make AI say Yes | Test a competing instruction against a model told never to say Yes | Student mentions giving Codex a question; no unambiguous pass shown. |
| 2 | One prompt, opposite answers | One prompt <=100 characters, two different model responses; benchmark model capabilities | 54:34–59:19; discussion, failed attempt noted. |
| 3 | Simple Question | Visible decoy; real question hidden in HTML in Chinese; inspect page/source | Present in assessment, not confirmed attempted in footage. |
| 4 | Collaborative Token Exchange | Share assigned 10-character tokens; score proportional to unique valid tokens up to 500 | Present, not confirmed attempted. |
| 5 | 韓国語音声データセットAPI検証 | Japanese instructions for Korean audio dataset API verification; base64 request, exact JSON response, four samples | 59:21–1:00:54, participants identify language and read task. |
| 6 | Cipher Trail | Decode Caesar-shift letters; inspect DOM for hidden values | Present, not confirmed attempted. |
| 7 | Data Labyrinth | Network game, tool and collaboration discovery | Present, not confirmed attempted. |
| 8 | Predict AI Pipe weekly cost | Public daily figures, forecast 2–8 Nov 2026 USD total; settlement after podcast window | Forecasting discussed in interview; actual live trade not confirmed. |

Code paths: q-podcast-say-yes.js, q-podcast-two-models.js, q-trick-question-server.js, q-share-token-server.js, q-korean-audio-dataset-server.js, q-cipher-trail.js, q-network-game-labyrinth.js, q-podcast-prediction.js. The last uses q-prediction-aipipe-server ID. No need to expose backend code or solutions to ongoing graded variants.

Archive checks (read only):

    SELECT quiz, count(*), count(DISTINCT email) FROM log
    WHERE quiz = 'podcast-2026-11-04' GROUP BY quiz;
    -- podcast-2026-11-04 | 11 | 2
    SELECT quiz, count(*) FROM results WHERE quiz = 'podcast-2026-11-04' GROUP BY quiz;
    -- no rows

Log dates UTC 2026-11-04 05:41:25 through 2026-11-10 18:33:11. They cover days outside filming; counts are access events and distinct account identifiers, not attendance, completions or learner success. Canonical archive dated 17 Nov. Do not extrapolate.

## Historical examples from the preparation research

For Q1 the prep chat reports a frequently reused story naming a character Yes (581/621 recorded uses successful), ordinary factual yes/no questions, and printing the concatenation of Y and es. Historical counts reflect copied prompts and repeated runs, not independent trials; do not present as the podcast's results. Q2 archive examples include “Is 3.11 a smaller number than 3.9? Answer with exactly one word: Yes or No.” and “Is 4000037 prime? Reply with only Yes or No.” Each reported example has one successful archived submission, no robust success rate. The public offline reconstruction should use new illustrative questions rather than disclosing current graded solutions. Q3's Chinese hidden question is separate from the Japanese Q5.

Preparation also identified drawings where human and model ratings disagreed (medal, owl, seahorse etc.). These were intended possible examples; the recording starts with the host describing the assignment but the detailed illustrated casebook was not shown as far as the transcript establishes. If using examples, verify underlying data and permission to reproduce students' artwork. Private location on Plutonium: ~/code/tds-network-games/.private/trading/humans-only/story.md.

## Open checks before publication

1. Verify any quoted line against original audio, especially mixed speech, named people, financial anecdotes, model names and numerical claims. The revised transcript follows the standard speaker/timestamp format; uncertain words are marked where identified. Both passes may share recognition errors.
2. Check video frames around the exam interaction if claiming actual on-screen attempts. No screen capture inspected here; do not invent screenshots or UI behavior.
3. User has requested the combined media release. User completed mediasync; video is publicly accessible and audio release metadata verified. Test actual player behavior; separate official episode link remains unknown.
4. Reproduce repeated-question statistics from original assessment rows or present as clearly labelled oral estimates with limitations. No causal learning claim from outcome transitions.
5. If incorporating NCERT findings, read the chapter itself, confirm the variables and distinguish association from causal effect. Avoid inferring regional parental behavior from correlations.
6. Review personal/financial/corporate and student-identifying material before publishing transcript or quoting it. Preserve the complete working transcript; review any student quotes before publication.
7. Update the talk catalog only in the HTML-generation stage once the media/publication decisions are made.

No HTML, commits, deploys or catalog edits performed. Combined video and release audio created in revision.

## Media revision — 26 Nov

- FFmpeg concat demuxer with stream copy (AV1/Opus) on Graphene. Combined video: ~/r2/media/2026-11-04-iitm-bs-podcast.webm; 367,243,615 bytes; duration 4060.335 seconds. Originals retained. LocalMCP2 media path was read-only; Graphene used for authorized file operations.
- Extracted audio using the exact opus function in setup.fish (mono, libopus, 12k target, voice settings). Audio: 2026-11-04-iitm-bs-podcast.opus; 6,228,086 bytes; duration 4060.327 seconds. gh release upload talks succeeded and asset URL/size confirmed via gh release view.
- Video URL: https://media.s-anand.net/2026-11-04-iitm-bs-podcast.webm (synced and verified 26 Nov). Audio URL: https://github.com/sanand0/talks/releases/download/talks/2026-11-04-iitm-bs-podcast.opus.
- Transcript timestamps are rounded to seconds against the joined video, Q&A offset 2894 seconds. The previous draft used separate timelines.

## Public video check — 26 Nov

HEAD returned HTTP 200, Content-Length 367243615 (matches local master), Accept-Ranges: bytes; GET bytes 0–1023 returned HTTP 206 with matching total size. Remote ffprobe independently confirmed 4060.335 s, AV1 1920×1080, Opus audio, no subtitle stream. Content-Type is audio/webm despite video stream; this also occurs with the 23 Nov TDS story, whose player explicitly declares video/webm. Browser playback not yet tested for this specific video. Claude Code should use the recent video-driven stories as functional references, with full design freedom.

# Source and link index — TDS course ideation, 9 November 2026

Checked 10 November 2026. Prepared for a future Claude build of the talk page. The **existing public page has NOT been generated**. Source references are divided into safe public links and local/private evidence. Video, transcripts and question implementation should be read, not indiscriminately reproduced.

## Existing media and intended published paths

| Artifact | Actual local path | External link / status |
|---|---|---|
| Full video | ~/r2/media/2026-11-09-tds-course-ideation.webm | **https://media.s-anand.net/2026-11-09-tds-course-ideation.webm** — verified HEAD 200 on 10 Nov |
| Audio fallback | ./2026-11-09-tds-ideation.opus | **https://github.com/sanand0/talks/releases/download/talks/2026-11-09-tds-ideation.opus** — HEAD 200 after redirects |
| Transcript | ./transcript.md | Annotated, noisy speaker/time transcript; future relative link |
| Meeting chat | ./chat.md | Time-coded links, events and student/TA responses; future relative link |
| Comic | ./comic-page.avif | Pre-existing, future relative link; do not regenerate |
| Main Claude prompt | ./prompts.md | Written **inside the existing “## Build Prompt, 10 Nov 2026” section**. Keep “## Metaprompt” and its content unchanged |
| Narrative map | ./story-context.md | Preparation only |
| Research notes | ./research-notes.md | Preparation only |
| This source list | ./links.md | Preparation only |

**Important correction to the user-supplied URL:** https://media-s-anand.net/2026-11-09-tds-course-ideation.webm (hyphen rather than dot in domain) returned HTTP **000**. The **working** URL uses the subdomain media.s-anand.net. Use ONLY the working dot version.

The local WebM is **82,050,349 bytes, 4667.917 s (77m47.917s)**, with **AV1 video**, **Opus audio**, and **embedded WebVTT captions**. Local audio ~6.8 MB. The remote WebM responded **Content-Type: audio/webm**, even though local ffprobe confirms a video track; browser video playback, seek and caption controls must be tested during the build. The audio release responds application/octet-stream but exists. No need to generate additional output in this prompt-only task.

**Comic authoring/provenance — retain in prompts.md comments only:** https://chatgpt.com/c/6af26180-ac80-83e8-b190-566bd265ee6e . Do not put the ChatGPT private conversation link in the public story. A local comic file is not itself evidence of what was spoken.

**Future talk URL, NOT YET LIVE:** https://talks.s-anand.net/2026-11-09-tds-ideation/ . Date 9 Nov 2026, TDS Course Ideation — Open Design Meeting, Sept 2026 cohort, Remote. Video and audio as above, transcript.md, chat.md, comic-page.avif. Do not add a catalog row or claim the page is published before Claude builds it.

## Previous Monday stories — use their actual finished pages as quality references

- 2 Nov: **Should a Student Even Read the Exam?** — https://talks.s-anand.net/2026-11-02-tds-ideation/ ; local ../2026-11-02-tds-ideation/{index.html,prompts.md,story-context.md,links.md,research-notes.md}.
- 19 Oct: **The Exam Has to Pass Its Own Exam** — https://talks.s-anand.net/2026-10-19-tds-ideation/ ; local ../2026-10-19-tds-ideation/{index.html,prompts.md,story-context.md,links.md}.
- 12 Oct: **The Exam Is a Hypothesis** — https://talks.s-anand.net/2026-10-12-tds-ideation/ ; local ../2026-10-12-tds-ideation/{index.html,prompts.md}.
- 5 Oct: **TDS course orientation** — https://talks.s-anand.net/2026-10-05-tds-orientation/ ; local ../2026-10-05-tds-orientation/{index.html,prompts.md}.
- 7 Oct IITM ED data-viz — https://talks.s-anand.net/2026-10-07-iitm-ed-data-visualization/ ; a separate talk format/layout reference.
- Local talk catalog: ~/code/talks/README.md ; existing entries establish approximate conventions. Do not update it in this preparation phase.

Important shared functionality: story ⇄ video mode, persistent media, transcript/captions, inline video timestamp seeks, deep-link state and browser back/forward, chapter/highlight synchronization, mobile/keyboard accessibility, comic presentation and source notes. **Borrow quality/mechanics, not fonts/colors/layout wholesale.**

## Meeting chat — exact public links posted during the call

- **07:23**, Carlton says a student has built a deadline-tracker in response to the course experiment.
- **09:04–09:21**, Swarnam notes the **10 Nov 18:00 IST** Food Court session conflicts with an MLP viva. This makes scheduling constraints real; avoid personal details beyond what's necessary.
- **10:33**, Mayank posts **Aaryan Panda's TDS Watcher:** https://aaryanpanda.github.io/tds-watcher/ — HEAD HTTP **200** on 10 Nov. A countdown alone omits distinct game-session windows.
- **11:22**, JK posts **DueLine:** https://dueline-tds.vercel.app/ — HEAD **200** on 10 Nov. The posted URL included the incidental parameter utm_source=chatgpt.com; stripped here. Don't infer which one is “wrong” without inspecting how each described its scope on 9 Nov.
- **13:17**, Carlton suggests the term “differentiators” rather than “discriminators,” useful if the public article discusses intended assessment difficulty.
- **14:39**, a student describes inability to sign in to face peer review; **16:18**, Preethi adds a participation-receipt issue from other students. These are observed complaints, **not a proven user-only mistake**. Avoid amplifying email IDs or logging tokens.
- **28:49**, Preethi asks whether students can attend all three Food Court slots; JK says yes at **28:54**.
- **36:58**, Carlton links **BBC original:** https://www.bbc.com/news/articles/c820vz6wyp65o — Lotte Underwood/AI-agent employment anecdote with concerns about missing domain-specific professional practice.
- **39:32**, JK posts an IIT Bombay alumnus's account of learning from uncertainty: https://www.linkedin.com/posts/aarav-rangwani-0010ajr_in-my-first-year-at-iit-bombay-i-thought-activity-7362347381603864576--_r- . This is a social post, not generalizable evidence; use only if the point is stronger with it.
- **43:16**, Preethi types **“observation skills?”**, during the open question about face morphing.
- **46:59–47:13**, Hritik notes that GA3 Q8 may show “the LLMs bias.” Treat as interpretation, not confirmed bias.
- **51:04**, Agrim suggests **spatial understanding**; this broadens the possible lesson of 3D reconstruction.
- **66:26**, Anand says he must leave. **The rest of the meeting is substantial and ends around 77:40**; do not cut the story at 66m.
- **73:47**, Hritik says asking the right question is a core skill now.
- **74:57**, Carlton says he's leaving; JK and students continue to the close around **77:40**.

## Official course, current GA4, program source

- Course: https://tds.s-anand.net/
- Course source local: ~/code/tools-in-data-science-public/2026-09/ ; public GitHub https://github.com/sanand0/tools-in-data-science-public . The user mentioned ~/code/tools-in-data-science/, which **does not exist** on LocalMCP2; use the *-public checkout*.
- Exam repo local: ~/code/exam/ . Public-safe GA4 info: src/exam-tds-2026-09-ga4.info.js and src/exam-tds-2026-09-ga4.js. Those describe extended 15 Nov deadline and the two live games; no private identifiers should be copied.
- Food Court public rules: ~/code/exam/src/q-food-court-discount.js ; simulator and story context: ~/code/tds-network-games/REALTIME-GAMES.md, src/realtime/games/food-court/model.ts. Public game via course's GA4 portal; standalone game page https://tds-network-games.sanand.workers.dev/realtime/food-court/ (page may require a signed personal entry; do not create or share one).
- Time Use Charts public rules: ~/code/exam/src/q-time-use-charts.js ; ~/code/tds-network-games/src/realtime/games/time-use-charts/ ; public page https://tds-network-games.sanand.workers.dev/realtime/time-use-charts/ (may need personalized auth). Dataset and timing source:
  - **India TUS 2024:** https://microdata.gov.in/NADA/index.php/catalog/236 .
  - **MoSPI / PIB 2025 official report:** https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2116301&lang=2&reg=48 ; initial fact sheet https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2106113&lang=2&reg=48 .
- GA4 face-review source: ~/code/exam/src/q-ga4-face-peer-review-server.js ; don't expose receipts/JWT/auth implementation.
- GA3 face morphing/reconstruction public problem context: ~/code/exam/src/q-face-morph-video.js, q-face-morph-rank.js, q-3d-face-model.js . The instructor used these as examples of tool discovery, benchmarking and surprising artifact quality, not as a demonstrated controlled learning study.
- General realtime infrastructure documentation: ~/code/tds-network-games/REALTIME-GAMES.md . Read-only for reference; don't publish privileged endpoints or implementation details that enable exam attacks.

## Learning research, public facts and caveats

- **BBC, 4 Nov 2026:** MaryLou Costa, “Graduates are managing AI – but are they learning much else?” Original link https://www.bbc.com/news/articles/c820vz6wyp65o (HEAD 200 through LocalMCP2; some automated web readers may be restricted). **Lotte** Underwood's organization built around **30 agents**; does not mean 30 employees displaced or that she single-handedly employs that number. It is a qualitative career anecdote, and the article explicitly raises missing professional craft as a concern.
- **EEF 16–19 metacognition guidance, 24 Aug 2026:** https://educationendowmentfoundation.org.uk/16-19/developing-independent-learners/metacognition-and-self-regulation . Evidence favors explicit planning, monitoring, evaluating, modeling and scaffolding; not automatic independent learning. UK 16–19 cohort evidence is not a causal result for IITM's adult online learners.
- **EEF broader toolkit, 2025:** https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/metacognition-and-self-regulation .
- **Public MoSPI original data:** https://microdata.gov.in/NADA/index.php/catalog/236 ; public source for actual dataset underlying poster game.
- **Possible high-quality framework reference:** Collins, Brown and Holum, “Cognitive Apprenticeship: Making Thinking Visible,” https://www.aft.org/ae/winter1991/collins_brown_holum ; supports modeled expertise but not this exact game.
- **User's private comparison study (do not link publicly):** ~/Documents/chatgpt/TDS Measure Learning Transfer.md (4 Nov 2026) and original chat https://chatgpt.com/c/6aeaa231-d914-83ec-b6dd-68db71e00f9c . Summary reports 687 matched students in one transfer comparison; full underlying artifacts were saved on Plutonium according to this file but unavailable here. **This is not independently reproduced in current session**; treat as a lead and verify before using exact percentages as fact.
- **Prior Food Court design discourse:** ~/Documents/chatgpt/TDS 2026 09 GA4 Food Court Realtime Game.md; contains tested restrictions and strategic deadlock considerations. Avoid turning rejected variant rules into shipped rules.

## Privacy and fact-check gates

- **Public page should use only public, anonymized and safe content**: avoid GA results keyed by students; screenshots with IDs or faces without consent; auth tokens; backend signatures; private evaluation procedures; confidential work/personal correspondence. Meeting chat names and reported operational bugs may be necessary context but don't embarrass people or publish sensitive details.
- A link's HTTP 200 confirms availability **only**, not that it's the intended content or that JS works in the browser. Browser-test the main video MIME/captions/seek and watcher pages before publication.
- Distinguish **on 9 Nov** (discussion and announcements), **as coded on 10 Nov** (implementation state), and **future sessions 10–14 Nov** (not yet observed scores).
- Dates in the public story need explicit **IST** for student session schedules; viewer local time is secondary and must be labeled.
- Treat pedagogical philosophy as position, not proven cognitive or job-market fact; evaluate each strong claim against educational evidence and the most serious fairness counterargument.

## After Claude actually builds the talk (not now)

Suggested future catalog: 9 Nov 2026, TDS Course Ideation — Open Design Meeting, Remote, September 2026 cohort; working title **“Who Watches the Deadline Watchers?”**; future published page https://talks.s-anand.net/2026-11-09-tds-ideation/ ; video https://media.s-anand.net/2026-11-09-tds-course-ideation.webm ; audio https://github.com/sanand0/talks/releases/download/talks/2026-11-09-tds-ideation.opus ; transcript.md; chat.md; comic-page.avif. Do not add or modify README.md in this prompt-only task.


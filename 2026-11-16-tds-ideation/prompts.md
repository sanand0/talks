# Prompts

## Build Prompt, 17 Nov 2026

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->

<!-- Original metaprompt/source: https://chatgpt.com/c/6ad6b3d4-12a0-83ec-97b2-e792263fffb5 -->
<!-- Comic-page creation/provenance: https://chatgpt.com/c/6afb28b0-d100-83ec-b3bb-54cadbca5eca -->
<!-- comic-page.avif already exists. Do NOT regenerate or modify it. Comic provenance is authoring-only, not a public story citation. -->

```markdown
Create an ambitious, deeply researched, beautiful, **single-page interactive talk story** for the open **IIT Madras Tools in Data Science course ideation session of Monday 16 November 2026**, at **2026-11-16-tds-ideation/index.html**. Use the talk-story skill and relevant data-story, design, interactive storytelling, memorable-explanations and verification skills. Read the actual finished Monday talks before settling on visual styling and architecture. You have editorial freedom to rewrite the working title and storyline based on the video. Make a reader who did not attend the meeting feel the surprise and understand the generalizable lesson.

This is an instruction for a **future Claude build**. **No course, exam, scoring or game repository changes. No commit, push or publication.** Only create the finished story page and its minimum necessary supporting public assets when this prompt is later run. Do not regenerate the original video, audio, comic, transcript or private source extracts.

The episode advances the series rather than restating it. In October the faculty discussed how to build worthwhile tests when agents can solve them. On **9 November** the class discussed surprise deadlines and newly launched 20-minute group games. On **16 November**, real results are back: professionals negotiated worse than students in one small Food Court comparison; originality and audience preference often diverged; forecasts improved while scores sometimes rewarded the wrong construct; and a student brought a **standalone, reusable decoder** for a question the instructor thought was hard. This is a rare scene where **the students' experiments force the educators to revise what counts as learning**.

## Read first, in this order

1. **./transcript.md**, complete — the roughly **66m54s** conversation, followed by an embedded **## Chat** section and a **## Links** section. Read the appended timed chat as first-class evidence: Preethi's interface and negotiation feedback, Swarnam's AI-liability comment, Adwitiya's solver links, Preethi's external-team GMeet workaround and the negative-marks discussion. Do not assume a separate chat.md exists for this particular Monday. **Check decisive quotes and exact offsets against the original local video and embedded WebVTT**, not just this imperfect transcript. The apparent **Anand [00:00] reset after ~49:48** is a transcription error, not the start of a second meeting.
2. **./story-context.md** — proposed narrative, time map, cast, surprising comparisons, two powerful openings, candidate diagrams and strongest counterarguments. Treat it as editorial input, not a compulsory outline.
3. **./research-notes.md** — first-party recomputed workshop/team results, sample-size and causal caveats; Bradley–Terry scoring and Q8 validity change; 2–8 Nov forecasting ledger discrepancy; the publicly verified Fable 5.2 announcement; copyright indemnity scope; learning and privacy limits. Treat factual labels and uncertainties as hard requirements.
4. **./links.md** — tested media URLs, prior talks, published student-safe materials, source paths, chat links, research trail and privacy rules.
5. **Three companion local ChatGPT exports**, located *here*: chatgpt-chat-aipl-session.md, chatgpt-chat-ga3-p1-closure.md, chatgpt-chat-student-learning.md. These include source analysis and later score/audit decisions. Use only **non-identifying, reproducible, permission-safe aggregates**, and distinguish what was said *in the meeting* from what was computed/approved after the meeting. Do not quote personal students' detailed histories or carry their IDs into the published page.
6. **Actually inspect published sibling stories** (source HTML + prompts) and learn their functional affordances:
   - ../2026-11-09-tds-ideation/{index.html,prompts.md,story-context.md,links.md}
   - ../2026-11-02-tds-ideation/{index.html,prompts.md,story-context.md,links.md}
   - ../2026-10-19-tds-ideation/{index.html,prompts.md,story-context.md,links.md}
   - ../2026-10-12-tds-ideation/{index.html,prompts.md}
   - ../2026-10-05-tds-orientation/{index.html,prompts.md}
   - ../2026-10-07-iitm-ed-data-visualization/{index.html,prompts.md}
   Borrow their **story↔video reading experience, persistence of playback, synchronized seek/navigation, captions, responsive typography and comic handling**, **not their exact CSS, color system, hero treatment or narrative structure**.
7. **Inspect implementation only when useful and read-only:** ~/code/exam/, ~/code/tds-network-games/, ~/code/tools-in-data-science-public/2026-09/, ~/code/blog/, and narrow relevant chats in ~/Documents/{chatgpt,claude}/. The user-mentioned ~/code/tools-in-data-science/ path doesn't exist on this device; actual checkout is tools-in-data-science-public. No private assessment keys, personal grades, authentication tokens, unreleased questions or confidential business/client data in public output.

## Why this story is worth reading

At [~42:17], Anand hears that a student has created a recognizer for the timed **Invisible Ink** exercise using **Claude Fable 5.2**. He assumes other students must have the same expensive frontier model to run it.

**“No, no, no, sir. It was a stand-alone model, just an HTML page encoded with the weights of the model, and no AI model was required for that.”** [~42:23, Adwitiya — verify exact quote on video]

That is the best possible cold open. A student turns a model-powered build process into a **portable, deterministic tool**. Now users with a motion JSONL can run it without a remote model at inference time. The teacher downloads and tries it live. He remains skeptical of several guessed letters. A second student, Shrikar, has another published repository, but the teacher won't install it in the middle of class. The actual solver accuracy is **not demonstrated against labels**. The genuine surprise is the student's **initiative, packaging and distribution** — a shift in the feasible way to take the test — not “the exam was cracked.”

Minutes later Anand proposes **three different forms of learning** that a student can get from this: finding a community that already has the solution, using a solution and knowing what's possible, or creating a tool everyone else can use. He does **not** claim everyone needs to become the third kind of student. This reverses the usual teacher/student arrangement: **the student changes the instructor's picture of the problem**.

That is a sharper human story than “AI students build cool things.” But it also contains a measurement riddle: **Who gets the marks, and what has each person learned?** A solver builder and a solver copier can both submit a valid output. One may be learning design, one collaboration, one only completion. The exam's scoring cannot reveal all three without a better instrument.

Alternate opening [~05:20–07:15]: an instructor replays the same **Food Court** simulation with a small workshop of experienced professionals. JK guesses they'd cooperate less, but perhaps have superior strategy and persuasive skill. In the first workshop session, **seven rooms with 32 entrants averaged only 88.06 team-score points**, against the **three TDS sessions' mean room scores of 92.51, 95.57 and 94.13** (61, 25 and 75 rooms). The workshop's average team score **fell from 91.81 at the first checkpoint to 85.95 at the last**, as participants negotiated. This is comic and genuinely counterintuitive — **but it is NOT a controlled comparison of working-professional versus IITM capability**. Eight workshop participants had student emails, some had played before, incentives/room size differed, and interface issues affected participants. Do not ridicule professionals. The important lesson is that **more experimentation or more negotiating doesn't always yield more collective value**.

Choose one central narrative. A strong four-beat possibility (not mandatory):

1. **The adults thought more, and earned less** (00–08m). A small, honest comparison reveals coordination is harder than optimizing the mathematical model. Preethi's complaint about a chat panel that required scrolling from the game matters: the **interface** can make “collaboration ability” look worse.
2. **The grader can't agree with its own intuitions** (09–35m). Two face meshes each win 13 of 26 peer comparisons but differ in Bradley–Terry quality because they beat different opponents. A wordless-story site reports familiar stories are liked but unoriginal; unusual ones can be original but misunderstood or disliked. The 7 Nov public blog shows a negative uniqueness/preference correlation **within this cohort**. The AI Pipe market settled at **$5.3063**; some students got more information yet lower cumulative marks because the rubric rewards early and sustained forecasting too, while others reasoned in dollars and clicked a cents range. **A score measures what the design rewards, not necessarily what we believe it measures.**
3. **Then the student moves the frontier** (38–51m). Adwitiya's browser-based standalone recognizer and Shrikar's shared repo demonstrate **making AI do the work of building repeatable tools**, plus how communities distribute them. The instructor struggles to validate letters visually; don't misreport visual inspection as an accuracy benchmark. The professor's problem changes: pick challenges at the cusp of possibility, neither trivial nor impossible, and ask what *human* ability to teach. A student may learn by producing a tool, finding it or just using it; distinguish.
4. **The next exam has only one avatar** (51–66:54). The instructor imagines a proposed ROE with a single character in a world of rooms, different problems appearing at different times and locations, and real choices about what to solve/skip, when to recruit help, or whether five more minutes are worth one mark. Adwitiya suggests using names rather than anonymity to improve accountability; Anand says anonymity was a deliberate test of whether students could **create social infrastructure to coordinate**, while Preethi reports that her team used an outside GMeet to coordinate Time Use Charts. Later, a −1 mark in GA4 Q4 provokes student concern, even as faculty see a tiny normalized penalty. The difference between an **exam rule as experienced** and **the intended learning** is the ending question.

Alternatively start with the student solver, revisit the workshop and grading surprises as evidence that scores alone mislead, then end with the speculative ROE. The future game belongs in a **proposed design** panel, not a “here is what students did” section.

## Crucial claims to handle precisely

**Food Court:** The game uses **0/10/20% monthly discounts**, 4–5 stalls, 12 months, and **60% team / 40% individual** mark weighting. The workshop scores cited above are independent room-mean aggregations of local results CSVs, not individual student grades. N is **7 workshop rooms, 161 TDS rooms across three sittings**. AIPL's **post-negotiation ~92→~86** are checkpoints, **not** the same as the first workshop's 88.06 average full-session score. Around 49.4% of the first AIPL final discount choices were 20%, vs 15–25% of TDS values, but that alone doesn't establish why. Preethi says in chat her negotiation got better over iterations; self-report, not a measured gain. Call it a **case study with selection, room and UI confounds**.

**Bradley–Terry:** A student with 13 wins out of 26 against stronger opponents differs from someone with the same 13 against weaker opponents. Explain *why* rather than equating it literally with PageRank; pairwise models have noise, unbalanced opponent counts and assumptions. In post-meeting scoring decisions the instructor chose **min–max-scaled Bradley–Terry**; a documented comparison became **2.875 vs 4.624** bonus marks for two 13/26 examples. Some criteria were deliberately approximated (GA3 Q8's peer-estimated **pair difficulty** substitutes for the original actual-morph outcome). That is a material **validity tradeoff**. Do not present provisional or TA-sent marks as published gradebook outcomes without checking.

**Picture Stories:** Real public original https://www.s-anand.net/blog/picture-stories-we-understand-and-like/ (published 7 Nov) and viewer https://files.s-anand.net/pages/tds-2026-09-p1-q7-picture-stories/?tab=patterns . The author notes originality and audience preference are negatively correlated **in this exercise**, but does not know why. Clichés (crow and water, child adopts a pet, kite) can be loved; a Bhagavad Gita story was a distinct high-scoring case. Audience understanding and preference are separate from originality. Don't extrapolate “people dislike all innovative content” or “realistic images beat cartoons”; the latter was a spontaneous hypothesis in the meeting.

**AI Pipe predictions:** The instructor says **123** initially and **242** finally selected the correct bracket in a roughly-620-student snapshot. A later **621-student matched on-time ledger** shows **123 initial and 262 last on-time correct**. **These are inconsistent** as currently documented; reconcile actual cutoffs before plotting a trend. The independently documented target total in the later source is **$5.3063** (round to $5.31) over 2–8 Nov 2026 UTC. A student's **written “$5–10” forecast** with **5¢–10¢ saved** is a potent verification example, not proof every forecaster made that mistake. Scores deliberately combined accurate predictions, early involvement and holding positions; later accurate beliefs could yield lower cumulative marks.

**Student solver:** Anthropic's https://www.anthropic.com/claude-fable-and-mythos-5-2 dates Claude **Fable 5.2** to 9 Nov, a real release. The user's chat contains a link to Shrikar's public repo, https://github.com/sreekarsarma55/temp-repo . Adwitiya's actual source link in a private Google Chat **must not be publicized** without authorization; a Claude artifact shared by Preethi may be a different tool. The HTML decoder's ability to run entirely without remote inference is **claimed and demoed by Adwitiya**, but its offline architecture and accuracy are not independently audited here. The instructor visually doubts guesses and asks about test performance. Don't imply a formal held-out accuracy evaluation occurred.

**Professional work and liability:** A client localization anecdote illustrates that **being able to generate something is different from being willing to own its risk**. Avoid identifiable client information. Google's 2026 generated-output IP indemnification is qualified by model/service restrictions and exceptions; it is not an all-purpose copyright/cultural/legal warranty. JK's claim that human taste or expertise survives automation is a hypothesis, not proof that AI output is intrinsically generic.

**Proposed ROE and psychology:** The instructor imagines future free-roaming, one-character, negotiation-heavy exams; this **was not deployed at the meeting**. No fixed sequence of questions in the imagined game, choice of time vs marks, community/agent guidance and anonymity/accountability questions are conceptual designs. Public GA4 Q4 bonus penalty discussion at [~60:26–64:59] has both numeric and emotional dimensions. The fact that −1 may be a tiny fraction of course marks does **not** make a student's concern irrational. Distinguish permitted collaboration from impersonation/unauthorized cheating.

## Creative and technical requirements

Tell an **earned discovery**, with a credible mystery, unexpected evidence, an interpretation that survives a strong counterexample, and useful implications. Use a small number of big moments, not 14 chronological sections. Make the human voices intelligible, for instance an instructor trying to read a difficult air-drawn E, a student explaining the solver is a plain offline HTML file, a disappointed team watching discounts climb, or someone getting a perfect arithmetic explanation but saving the cents option. These are scenes and decisions. **Show the meaning of the metric by playing with it**, rather than decorating the page with scorecards.

Possible purposeful interactive visualizations:
- A split **7 workshop rooms vs 161 TDS rooms** score comparison with clear error/sample labels; or an anonymized single-room trajectory showing 91.81→85.95 *mean checkpoint* for AIPL. Use **real computed numbers only**; don't show private room identifiers, conversations or email addresses.
- **Two peer-reviewed items, each 13/26:** reader chooses which deserves higher grade given rival strengths, then shows scaled Bradley–Terry and the reason. Use schematic rather than actual private face photos.
- An **originality vs preference** scatter/graphic based on the public author results. Show a familiar liked story and a surprising unique one. If exporting student images, verify safe public reuse.
- A **reasons vs action** UI where a forecast says "$5–10" but the selected range is "$0.05–$0.10"; reader spots the discrepancy. Clearly label constructed illustration of a real pattern.
- A **solver flow** showing AI-assisted *development* → deterministic portable file → another student's upload → score checked against independent labels. **Don't equate plausible model output with correct classifier.**
- A **one-character ROE choice** with two rooms and three competing opportunities, forcing prioritization; visibly label this a **hypothetical future examination concept**.

**Do not build all of these.** Choose two or three that reveal mechanisms worth remembering. Write original editorial design, not generic gradient cards or stock photos. The existing **comic-page.avif** should fit the narrative with precise alt text, deliberate placement, zoom/full-size viewing, attribution where appropriate and no regeneration.

**Video integration bar:** Use a **single persistent video element** across Story and Video modes; no remount, lost playback, captions or seek when switching; semantic chapters and side rail, in-text timestamp buttons, URL deep-linking and correct browser history/back-forward, native keyboard controls, autoplay disabled, caption/transcript access, mobile responsive reading, high contrast, focus states, screen reader names, reduced-motion support. The story should be readable as prose without the video, yet timed jumps should reward watching.

**Actual media:** local ~/r2/media/2026-11-16-tds-course-ideation.webm — **66:54 exactly**, AV1 **1280×720**, Opus, embedded English WebVTT; public **https://media.s-anand.net/2026-11-16-tds-course-ideation.webm**. The user-provided **https://media-s-anand.net/2026-11-16-tds-course-ideation.webm** was unresolvable; **use the dot-subdomain**. Remote server replies **Content-Type: audio/webm** even though video track exists; test real browser playback, seeks and captions rather than trusting HEAD 200. Audio fallback local ./2026-11-16-tds-ideation.opus and GitHub release https://github.com/sanand0/talks/releases/download/talks/2026-11-16-tds-ideation.opus (HTTP 200 after redirect). Keep video preferred, audio accessible, and don't construct links from private GitHub redirect query strings.

**Privacy/legal:** Never publish saved student records or email IDs, sensitive face data, private Google Chat room links, expired authenticated question links, signed JWTs, unreleased answers, confidential client details, or screenshots that expose student identifiers/admin controls. Cite the public gallery, public blog, primary model announcement and source-backed anonymized aggregate. Do not embed existing copyright-protected songs or TV/movie clips just because the transcript mentions them. Present invented toy data and graphic simplifications explicitly as simulated.

## Deliverables for Claude later, not for preparation now

Build a polished **index.html** and only minimum supporting assets needed for public viewing (including captions extraction if needed). Run verification on chosen quotes, exact time anchors, data denominators/version, live player/captions/seek, mobile keyboard and screen-reader access, deep links/history, comic lightbox, image reuse, privacy and source link behavior. Don't regenerate the comic or alter transcript / companion research unless correcting a demonstrable error. **Do not touch the Metaprompt section below, edit any course/game/exam repo, commit, push or publish.**

Suggested **future** catalog entry only after build: Monday **16 Nov 2026**, TDS Course Ideation — Open Design Meeting, Sep 2026 cohort, Remote; working title **“When the Students Solve the Exam, the Teacher Learns”** (your own better title welcome); video/audio URLs above; transcript.md, comic-page.avif, and optional link to chat within transcript; eventual page **https://talks.s-anand.net/2026-11-16-tds-ideation/** (not currently created/published).
```

---

In light mode, selections inside dark backgrounds like .lamp or .hero-art are almost impossible to read.
The meeting video panel does not always stay on screen - like in past talk summaries. It should.
The comic story's aspect ratio is completely off!
Look for more such errors, carefully, and fix all.
The private links are fine, I'm happy re-using the picture-story images, unverified quotes, student names, footer credit.
Update the home page, config.json, etc. and make it ready to publish.

---

Make the comic much larger. If possible, annotate on TOP (rather than on the side) of the comic. Think about the best way to do that.

--- <!-- steering -->

The session started at 5:30 pm IST (8 pm SGT) on Mon 16 Nov 2026.

--- <!-- steering -->

Make sure it's possible to see the original comic and that the annotation does not always overshadow the comic - and appears only when... well, you decide.

<!-- claude --resume d32440b3-8e6a-4a90-8009-81b2ac7f6674 -->

## Metaprompt, 16 Nov 2026

<!-- https://chatgpt.com/c/6ad6b3d4-12a0-83ec-97b2-e792263fffb5 -->

Similarly, on @LocalMCP2 create JUST PROMPTS (and story context, links, sources, etc.) a new talk for the TDS course ideation session we had recently in ~/code/talks/2026-11-16-tds-ideation.
Keep this similar to the past talks we've had on TDS course ideation on Mondays.

The video https://media-s-anand.net/2026-11-16-tds-course-ideation.webm is also available locally at ~/r2/media/
The .opus file has been uploaded to GitHub releases.
comic-page.avif is available and was sourced from https://chatgpt.com/c/6afb28b0-d100-83ec-b3bb-54cadbca5eca

~/code/{exam,tds-network-games,tools-in-data-science} have additional context. Feel free to explore other repos as well as past ChatGPT chats at ~/Documents/{chatgpt,claude}/ and any other sources. Research online, fact-check, etc. like with previous stories.

Include the prompt, context, links, sources, etc. for Claude, nudging it to design similar to the previous talks.

prompts.md already exists. Insert the new prompt inside the same file, under the "Build Prompt" section.

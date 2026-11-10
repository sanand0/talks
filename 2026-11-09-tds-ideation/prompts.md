# Prompts

## Build Prompt, 10 Nov 2026

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->
<!-- Source: https://chatgpt.com/c/6ad6b3d4-12a0-83ec-97b2-e792263fffb5 -->
<!-- Comic-page provenance: https://chatgpt.com/c/6af26180-ac80-83e8-b190-566bd265ee6e -->
<!-- comic-page.avif already exists. Do not regenerate or modify it. The URL above is authoring provenance, not for publication. -->

Create a memorable, visually distinctive, evidence-grounded **single-page talk story** in **2026-11-09-tds-ideation/index.html**, based on the recorded open **IIT Madras Tools in Data Science course ideation meeting of Monday 9 November 2026**. Use the talk-story skill and any useful data-story, design, interaction, storytelling and verification skills; read the actual reference talks before you design. You are given a transcript, meeting chat, audio, video, comic, narrative map and a set of sourced research notes.

Aim for a story that an educator, student or AI practitioner with no prior TDS context would genuinely want to read and remember. It should tell a **human discovery story** rather than reproduce a course's philosophy or walk through ten questions. Give readers a useful mechanism, an uncomfortable counterargument and something concrete they can try. The educational claim must survive scrutiny, not just sound inspiring.

## Read first; follow the evidence

1. **./transcript.md** — full approximately 77m48s meeting. Read all of it, not just the first hour; **Anand leaves at ~66:26 but JK, Carlton and students continue until ~77:40**. Validate exact quotes, speaker names, the displayed screens and critical timestamps against the local video and embedded subtitles (transcript may have stitched or sparsely marked passages).
2. **./chat.md** — synchronized meeting-chat messages. It includes _actual URLs shared in the meeting_, students' real-time concerns about scheduling and login, the 10:33 TDS Watcher, 11:22 DueLine, 36:58 BBC article, 43:16 “observation skills?”, 51:04 “spatial understanding”, Anand's departure and later reflections. Include chat voices only when they change the argument. Cite by video/chat time, not by invented sentence in spoken transcript.
3. **./story-context.md** — possible central story, four-beat arc, cast, timestamp map, competing interpretations, visual concepts and weak spots. It is a **guide, not a mandatory outline**; improve it when the video shows a stronger human interaction.
4. **./research-notes.md** — independent educational source checks, real first-party game mechanics, prior paired learning-transfer research, contradictions and explicit limitations. Particularly important: **a simple deadline counter can be correct and still be misleading; 60/40 Food Court score; evidence on metacognition; pre/post success is not necessarily learning transfer**.
5. **./links.md** — verified media, corrected URL, previous talks, exact meeting-chat links, future sessions with IST dates, local implementations, privacy rules and source trail.
6. **Actual preceding finished talks**, especially ../2026-11-02-tds-ideation/{index.html,prompts.md,story-context.md,links.md} and ../2026-10-19-tds-ideation/{index.html,prompts.md,story-context.md,links.md}. Then ../2026-10-12-tds-ideation/{index.html,prompts.md} and ../2026-10-05-tds-orientation/{index.html,prompts.md}. Reuse the excellent **story ↔ video** experience, synchronized time seeks and finish, **not their literal color palette, typescale, page layout or visual metaphors**.
7. Selectively examine **working source**, read-only: ~/code/exam/, ~/code/tds-network-games/, ~/code/tools-in-data-science-public/2026-09/, ~/code/blog/ and relevant ~/Documents/chatgpt/ (notably TDS Measure Learning Transfer.md, TDS 2026 09 GA4 Food Court Realtime Game.md). The user-mentioned ~/code/tools-in-data-science/ path **does not exist** here; use tools-in-data-science-public. Never publish student records, private admin screens, assessment secrets or raw protected datasets.

## A story hiding in an ordinary countdown

At [~09:54], Anand shows a student-built **TDS deadline watcher**. It has a countdown that says the GA4 deadline is about six days away. But students can't simply wait six days. Food Court requires joining one of three **20-minute** sittings; Time Use Charts requires joining one of three different **45-minute** sittings. The watcher counts the final submission date without expressing the events that make submission possible. Another student site has the same kind of blind spot. At [12:28], JK jokes that **they need a tracker for the trackers**.

That's an exceptionally good opening. **A system designed to remind you of exam changes misses a requirement of the exam.** The student did exactly what the course wanted—built an agent-era monitoring tool—and now the tool has to be specified and verified more carefully. It is the very same lesson the instructors are trying to assess. Be fair to the student project: a countdown can be accurate for one event while incomplete for others; don't claim the site is broken or ridicule its creator. It's a perfect **specification versus execution** example.

The bigger question emerges: **if a course deliberately changes and makes itself difficult to monitor, is that teaching valuable real-world initiative—or measuring who has time, access and resources to keep up?** It is not necessary to decide this with certainty. Show the instructors defending a balance, show students revealing failure modes, and show what evidence would change one's mind.

Another excellent hook is [20:39–21:08]: Preethi assumes GA4 ends **11 Nov**, Anand asks her to check, and she discovers it has been extended to **Sunday 15 Nov**. Her surprised “Oh, God” captures the costs and possible benefits of discovering rules instead of being told. A third is [~34:01] Hritik asks “What are we learning?” and Anand says **“You figure it out.”** There is a strong counterpoint here: if the students must discover the lesson themselves, how can the teachers measure whether they have learned it? These can anchor a piece with a different emotional arc.

**Choose one overarching story**, preferably with a genuine scene before thesis, a discovery arc with fewer than five beats, and at least one moment where the counterargument really bites. Avoid “six ideas from an innovative course.”

## A possible narrative trajectory (change if warranted)

**1. The schedule is a moving target (~05:50–22:15).** The instructors intend that agents monitor announcements and students adapt to unannounced, increasingly shorter windows. The vision includes hypothetical future midnight-to-4am micro-exams, but **these are not currently scheduled**. The new trackers demonstrate initiative—and the inadequacy of a simple deadline data model. Swarnam's live chat points out that a Food Court slot conflicts with another academic viva. JK says a few unusual questions sit within a larger portfolio of standard assignments and grievances are addressed. Saptadev describes a repeatable login failure and Preethi reports a receipt issue; don't assume either is user error merely because other students succeed. Preethi then discovers the extended final deadline. **What a learner could figure out for themselves, the teaching system also needs to communicate and guarantee reliably.**

**2. Four food stalls, twelve months, twenty minutes (~22:15–33:35).** This is where abstraction turns physical. Four or five classmates manage food stalls in one simulated court. Each may choose **0%, 10% or 20% off** for each of twelve months. Discounts draw customers, reduce margin and change rival profits; everyone's choices interact. They can use agents and chat with each other; the result is **60% group profit and 40% own profit**, verified from the current code, with three scheduled sittings and best eligible result. The question is not who can run a formula in isolation. In 20 minutes, can players notice what changes, negotiate, share information, decide whom to trust and act despite incomplete coordination? An agent may optimize the economics; **a good score is not proof the human learned game theory or improved negotiation skills**. A real toy interaction could show a price-war incentive as the shared payoff falls. Label any toy values; don't invent realized classroom scores.

**3. “What am I learning?” (~31:00–64:49).** Hritik voices a central student objection. Anand answers that students can have different learnings from a question, even without being told a single official objective. He refers to learning-transfer measurement with 20–30% of students improving on some repeated skills; the figure is a claim in conversation, not a validated causal estimate. Carlton shares a **4 Nov BBC report** about Lotte Underwood, an AI associate at a firm whose team built about 30 agents; the article questions whether such employees miss core professional craft. That **contradiction** is worth more than its inspirational anecdote. Later, Anand asks what the 3D face and face-morph GA3 assignments taught. Preethi says **observation** (and recalls the old Michael Jackson morph); Hritik suggests model perception; JK sees **depth and spatial reconstruction**; Anand points to discovering **purpose-built tools**, verifying results and making impossible-looking work tractable. These are competing, plausible learning objectives, not independently measured outcomes. Use a real before/after example to make “smooth crossfade” versus a **plausible intermediate face morph** visible without reusing student faces without consent. No copyrighted music/video playback.

**4. Who measures the learning? (~64:49–77:48).** After Anand leaves (~66:26), **JK continues** to discuss **metacognition**—reconstructing the process by which you learned, not simply the artifact you produced. Carlton says he has drafted three proposed repeated-measurement questions for GA5 and sought review; **they have not been proved or deployed by this call**. He and JK also describe the need to use different models to critique one another and to understand a deluge of AI output, not just accept it. Hritik argues that **asking good questions** is itself a core skill. JK ends by acknowledging overwhelm and grievances, and explicitly inviting disagreement. A measured, earned conclusion: **a course that asks students to verify agents should verify its own hypotheses about student learning**.

A stronger alternative would start at “You figure it out,” travel through the games and student objections, then reveal the paired-measurement analysis, ending on whether learning-to-learn can be taught without guidance. You can change the order of events, but don't imply an earlier discussion responded causally to a later one if it didn't.

## The specific research surprise that prevents a facile conclusion

A private local ChatGPT analysis of September 2026 TDS, dated **4 Nov** (~/Documents/chatgpt/TDS Measure Learning Transfer.md), reports **687** students who completed the earlier/later tasks in order. For Ollama/tunneled API tasks, **146 (21.3%) improved**, **37 (5.4%) worsened**, **504 (73.4%) stayed the same**. At first glance that's nearly **4 times as many improving as worsening**. But comparable _unrelated_ earlier questions predicted performance on the later task almost as well; changing difficulty, student ability and better AI assistance could explain a lot. That is not convincing causal evidence of specific skill transfer. A terminal-recording comparison instead showed a big persistence gap between earlier pass/fail cohorts, suggesting an actual bottleneck—but also many people not catching up.

If you can **independently replicate the aggregates from actual dumps** and source it appropriately, this makes an excellent visual: a beautiful apparent victory, then one counterfactual that collapses the overconfident interpretation. If you cannot independently verify the data and its safe public status, **do not use exact numbers publicly**. Cite only as a speaker's preliminary report or use a labeled hypothetical to teach how to test learning. Never reveal student records or infer individual's learning from a single binary score.

**External evidence:** Education Endowment Foundation's Aug 2026 review specifically recommends **explicit metacognitive modeling, guided practice and reflection**, rather than assuming students will develop monitoring/planning skills automatically. It lends nuance to “you figure it out”; it does **not** establish that TDS's experiments have failed. Make the tension intellectually fair.

## Essential time anchors and what NOT to conflate

- [00:00–05:50] JK outlines the whole purpose: justify the course, learn from repeated assessment, listen to grievances.
- [05:50–09:50] monitoring agent vision; shrinking deadlines; future midnight tasks are **proposals**.
- [09:54–12:38] actual live student tracker(s), missing session windows, “meta tracker” joke. The two real links are in chat.md.
- [12:38–16:16] JK's “discriminating” assessments within a larger course. Chat suggests “differentiators”; be sensitive to connotations.
- [16:16–22:15] Saptadev/Preethi: live bug reports, a receipt-not-yet-ready explanation, Nov 15 deadline rediscovered. No verified root cause from the meeting.
- [22:15–29:46] Food Court demo; use correct mechanics from q-food-court-discount.js.
- [29:46–39:35] JK's OR/game theory and career view; Hritik's “what are we learning?”; Anand's learning-by-environment claim. Do not turn opinions about junior employment into population-wide facts.
- [39:35–42:18] Carlton's BBC AI associate article, with real counterargument on missing tradecraft. Article title, date, name and link are in research-notes.md.
- [42:18–55:26] live guessing of learning outcomes: observation, spatial understanding, benchmarking, specialized tools; show distinction between tasks **worth automating** and decisions **worth learning**.
- [55:26–64:49] sourcing help from agents and classmates; benchmarking models and tools; precise contrast between smooth transition and genuine morph. “Cheat” is used colloquially to mean **permitted collaboration and leverage**, not illicit misconduct.
- [64:49–77:48] JK's metacognitive synthesis, planned GA5 measurement, student overwhelm, asking better questions, final invitation to disagree. **Do not truncate at Anand's 66:26 exit.**

Check selected voice attributions and in-text seek times with **video subtitles and frames**, because transcript timestamps are approximate and several long passages have only one initial time marker. Anecdotes about a German wiki agent swarm are not independently verified; either research the primary source or omit. “90% of actions subconscious”, “AI can answer anything” and “all intellectual work is automated” are **speaker exaggerations, not scientific facts**.

## Content and presentation bar — ambitious, not decorative

**Match the quality and functional affordances of 19 Oct and 2 Nov's finished talks, not a copy of their CSS.** Prefer a coherent visual metaphor that expresses the lesson: a calendar that gains additional layers of time, a small live economic negotiation, a before/after learning matrix with the counterexample, or an “answer versus understanding” interactive. Two or three purposeful explanatory graphics beat ten fake widgets. Use a human scene / concrete contradiction as the opening, then reveal the general model. The comic-page.avif is a pre-existing authored illustration: present it well with accurate alt text, full-size viewing and context, but don't use it as factual evidence.

Technically, the finished page should include:

- A genuinely useful **story ↔ video** switch with **one persistent video element** (switch modes without losing timestamp, play state or captions), visible chapter navigation, embedded live seek buttons and URL-deep-linkable timestamps.
- Accurate video and audio sources; video-first with fallback to audio. **Video duration 4667.917s (77:47.9)**, AV1 1280×720 and embedded English WebVTT, with transcript and meeting chat link where useful.
- Source-grounded on-screen timestamps, a concise transcript/captions view, clear side notes / citations tied to claims, mobile/desktop layouts, keyboard support, focus states, high contrast, reduced motion and screen-reader context. No autoplay; avoid surprisingly long animations or massive dependencies.
- For a schedule visual: **show IST prominently** and optionally locally converted viewer timezone; do not confuse **GA4 EOD Nov 15** with **Food Court Nov 10–11** or **Time Use Charts Nov 12–14**. Distinguish 20m and 45m slots, and don't assert attendance availability before/after those windows.
- For game simulation: use the public three-choice discount model or mark a simplified model **explicitly hypothetical**. Group/individual weighting is **60/40** as of 10 Nov; don't silently use a 100%-selfish score implied by casual spoken simplification.
- If using real student work, video screenshots, 3D faces or group chats, **inspect for private identifiers, credential links, personally identifying data and publishing rights** first. Avoid exposing exam solutions or admin internals. Include only enough name attribution to understand the public dialogue.
- For an impact chart, separate **observed task performance** from **proven learning transfer**, and label cohort/sample/version. No invented causal claims, student grades, winners, model superiority or future GA4 outcomes.

Make one or two ideas vivid enough that readers can play/understand the underlying decision themselves. For example: “You have six days until final submission. Which task will be impossible to attempt in six hours?” Or show four diners revising their discounts and a counterintuitive response. Better a truthful labeled micro-simulation than a photorealistic, nonsensical decorative graphic.

## Build-stage verification and publication boundary

Video: https://media.s-anand.net/2026-11-09-tds-course-ideation.webm. Local ~/r2/media/2026-11-09-tds-course-ideation.webm.
Existing Opus: ./2026-11-09-tds-ideation.opus, GitHub release https://github.com/sanand0/talks/releases/download/talks/2026-11-09-tds-ideation.opus.
Comic: ./comic-page.avif.

Before finishing the future build, verify: every exact quote and time anchor; full 77:48 recording coverage including post-Anand discussion; story/video shared player and back/forward/deep-link behavior; correct time zone in deadline displays; successful video playback despite MIME; comic lightbox; keyboard/mobile; no data leakage; no broken or misleading source links; careful separation of speaker claims, coded mechanics, experimental evidence and proposed futures. If something cannot be independently checked, label it provisional or cut it. Run relevant local QA without modifying exam/game repos.

**Build outputs:** index.html and only minimal necessary supporting public assets in this talk folder, not a PDF, slide deck, new audio, comic, or full transcript rewrite.

**Suggested catalog entry, after the page is ready:** 9 Nov 2026, TDS Course Ideation — Open Design Meeting, Sep 2026 cohort, Remote; provisional title **“Who Watches the Deadline Watchers?”** (improve if you find a stronger true story); page https://talks.s-anand.net/2026-11-09-tds-ideation/, video and Opus URLs above, transcript.md, chat.md, comic-page.avif.

<!-- claude --resume 801c9ba8-8f54-4927-827e-3d346d9bbf2c -->

## Metaprompt, 10 Nov 2026

Similarly, on @LocalMCP2 create JUST PROMPTS (and story context, links, sources, etc.) a new talk for the TDS course ideation session we had yesterday in ~/code/talks/2026-11-09-tds-ideation.
Keep this similar to the past two talks we've had on TDS course ideation on Mondays.

The video https://media-s-anand.net/2026-11-09-tds-course-ideation.webm is also available locally at ~/r2/media/
The .opus file has been uploaded to GitHub releases.
comic-page.avif is available and was sourced from https://chatgpt.com/c/6af26180-ac80-83e8-b190-566bd265ee6e.

~/code/{exam,tds-network-games,tools-in-data-science} have additional context. Feel free to explore other repos as well as past ChatGPT chats at ~/Documents/chatgpt/ and any other sources. Research online, fact-check, etc. like with previous stories.

Include the prompt, context, links, sources, etc. for Claude, nudging it to design similar to the previous talks.

prompts.md already exists. Insert the new prompt inside the same file, under the "Build Prompt" section.

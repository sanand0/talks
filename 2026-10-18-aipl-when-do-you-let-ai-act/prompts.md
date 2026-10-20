# AIPL Session 1

## Include video, 20 Oct 2026

<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/Documents:ro,~/r2:ro -- claude --dangerously-skip-permissions --model sonnet --effort medium
-->

https://media.s-anand.net/2026-10-18-aipl-session-1.webm has the video for 2026-10-18-aipl-when-do-you-let-ai-act/
Update config.json to reflect this and run `just build` to update README.md, index.html.
Also embed the video in 2026-10-18-aipl-when-do-you-let-ai-act/ elegantly (similar to how we've embedded such .webm files in 2026-08-22-ai-unboxed-vibe-coding/ or 2026-08-10-tds-ama/), below the comic.

The timestamps for the video do not align with the audio because the audio trims the breakout and starts at a slightly different time.
Mention this subtly. There is no need to modify the timestamps or modify the a.ts links point to the video. Treat the video as independent.

<!-- claude --resume 279d3992-ece8-4bee-b425-2acfc97de5b6 -->

## Build prompt, 18 October 2026

<!-- Comic page: https://chatgpt.com/c/6ad5a81c-6f38-83ec-a40f-bdc79ee0a5af -->
<!-- Source: https://chatgpt.com/c/6ad582ef-aa64-83ec-a44c-e944452acd1b -->
<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/Documents:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a **memorable, thoroughly evidence-grounded narrative** of my **18 October 2026 AI Product Leadership (AIPL) workshop, "When Do You Let AI Act?"** as a static page at **`2026-10-18-aipl-when-do-you-let-ai-act/index.html`**. This is Session 1 of a three-session leadership module organized by LeadUp Universe with E&ICT Academy, IIT Kanpur. The audience comprises experienced working professionals. This is a workshop that did not proceed as planned, not a product announcement or a standard keynote.

**Use the `talk-story` skill**, along with relevant evidence, storytelling, research, design, interaction, data-analysis and webapp-testing skills.

**You have full creative/design control.** Choose headline, narrative structure, editorial focus, visual identity, layout, typography, data graphics, devices, navigation, pacing and implementation independently. Do not copy a page, treat suggested acts as required sections, or implement a prescribed mockup. More important than features is a coherent story readers will remember. A single surprising and deeply explored episode is better than ten examples. Use any of the editorial suggestions below only if they sharpen the story.

## Read the supplied evidence first

1. **`transcript.md`** — the talk, with relative timestamps. This is AI transcription, not perfect truth: verify crucial quotations, attribution and timestamps against the **local Opus recording**. It contains an edited jump over most breakouts. Avoid interpreting missing audio as the session ending.
2. **`story-context.md`** — people, actual sequence, scenes, open questions, editorial tensions, local context, privacy constraints and specific timestamp anchors. Guidance, *not a mandatory outline*.
3. **`survey-analysis.md`** — anonymized and reproducible analysis of the actual audience survey: exact denominators, unexpected results, missingness and limitations. This is a richer data source than the live counts mentioned aloud. You may independently recompute from `~/code/liveform-data/aipl2026/{responses.tsv,form.yaml}`, **but never publish raw records or identifiers**.
4. **`research-notes.md`** — independent fact checks on GDPval, jagged-frontier research, the five-model error experiment, InsurLE, policy-as-code, the STE100 test and research on reliance. This is a selective evidence shelf; quote/link only what matters.
5. **`links.md`** — separate **shown live** from **not shown**. Link the relevant public demo sources in their proper narrative context; do not imply every open browser tab became part of the talk.
6. **`chat-aipl-session-1-*.md`** and **`chat-improve-workshop-engagement.md`** — preparation, real-time intervention, and post-hoc suggestions. **They contain private conversation URLs and event logistics**. Use for insight into intention versus what happened, never publish private URLs, raw excerpts or confidential details.
7. **Zoom chat**: `~/Documents/Zoom/2026-10-18 13.27.48 Module 5 _ Session 1/meeting_saved_new_chat.txt`. It contains a useful independent record of chat interactions. Do not publish participant identifying data.
8. Earlier audio-only story pages: **`../2026-10-01-use-ai-emperically/`** and **`../2026-09-24-iis-ph-evidence-to-impact/`**. Recent audio/video timestamp navigation: **`../2026-10-07-iitm-ed-data-visualization/`** and **`../2026-10-12-tds-ideation/`**. Study their `prompts.md`, `story-context.md`, `research-notes.md`, `links.md` and resulting `index.html` to understand how evidence becomes a narrative. **Reuse principles, not design**.
9. **`comic-page.avif`** — feature prominently high in page with accessible alt and lightbox once it exists.

You may investigate the local `~/code/llmevals/double-checking/`, `~/code/llmpricing/`, `~/code/policyascode/`, live websites, original research papers and any pertinent local work. Prefer primary sources, challenge quantitative claims, distinguish **speaker claims**, **experimentally measured numbers**, **respondents' self-reports**, **research results**, and **editorial inference**.

## The raw material has a promising human drama

We begin with me telling the group this will be interactive and polling how far they have let AI go. **18 of 33** respondents eventually say they used AI's work but checked everything. Only **2 of 33** say they let it act unchecked. There is a little tension between models becoming cheap/capable and people's hesitance to delegate. Someone has already used AI for something another person thought it could not do. The **Advice → Draft → Audit → Act** ladder is a useful framing, but trust varies by task, context, consequences, access and verification.

The room complicates that simple framing. **Mukul talks about explainability and trust; Ram about privacy, data and misuse**, things that mere accuracy tests don't solve. I ask a harder follow-up question: why didn't people ask AI to do certain tasks? Response counts barely move. There are long, quite awkward silences. I eventually use AI to see who completed earlier questions but not this one, make my first ever near-roll-call, and then **ask ChatGPT, live, how to repair the workshop itself**. There is some comedy in the AI instructor treating his own engagement problem as a live AI task. But it's also a self-correction: questionnaire completion is not learning; maybe quiet people were watching the recorded version, or needed a simpler task, or were distracted. **Do not diagnose the quiet participants.**

Then I demonstrate three ways to make delegated work more reliable: **independent model agreement**, **benchmarks that can disprove intuitive prompting tips**, and **programmatically checkable policy rules**. The underlying experiment found average one-model error **14.1%**, two-model accepted-case error **3.7%**, five-model accepted-case error **0.7%** with **28.1% requiring review**. These are specific classification benchmark results, not a general accuracy promise, a safety guarantee or a verified client's savings. The STE100 experiment compares six tasks on one model; the demo isn't proof about all simplified prompts. The insurer logic and policy-code demos illustrate how formal checks can help, but converting prose into rules also creates a **semantic fidelity** problem.

A powerful contrast from the audience itself: asked which 10 of 100 decisions they'd review, **21/33 picked where a mistake would cost the most**, while just **1/33** picked where AI was least certain and **1/33** picked model disagreement. The demo is optimized for detecting wrong answers; the participants gravitate toward the *cost of* wrong answers. Would a practical delegation policy need both? Explore this only if useful; the poll does not establish the optimal strategy.

The session ends with a participant's real question at **109:43**: when should I **stop** an AI research loop that keeps wandering? I have no proven general rule. I suggest logging **ten instances** of wanting to stop and checking later whether stopping would have been right. I explicitly say at **112:23** I haven't done the experiment yet and will try. That unresolved thought is a potentially stronger ending than any confident summary.

**This is a possible story, not the required outline.** Find your own opening, hidden contradiction, turning point and ending after reading the actual evidence. In particular, preserve the workshop's imperfection and the students' voices. Do not make me sound like I had an elaborate hidden-test experiment that was never run, or as though the entire group enthusiastically collaborated throughout.

## Audio-first, with small playable timestamp links

**No video exists for this talk.** There is a 113:02 edited audio recording:

- Local: `2026-10-18-aipl-when-do-you-let-ai-act.opus` (same folder)
- Published: https://github.com/sanand0/talks/releases/download/talks/2026-10-18-aipl-when-do-you-let-ai-act.opus

The most useful interaction to borrow from recent video talks: unobtrusive **clickable ▶ MM:SS / H:MM:SS timestamp cues in the story** that seek and play the original audio at that passage, retaining a shared media player, with bookmarkable timestamp URLs. Think of these as source citations that come alive. A reader should also be able to access the entire transcript and explore the references while listening. Timestamps should correspond to the *actual audio*; verify a sample of anchors, especially after the breakout edit. Audio player controls must be usable with keyboard and on mobile. **Beyond this, choose your own interaction design.**

## Editorial responsibility

- Tell readers **what happened**, not merely what was planned. Planned split-evidence packets and hidden validation cases were **not** used in Session 1.
- Don't leak participant email addresses, IPs, tokens, internal call logistics, private ChatGPT/Claude conversation URLs, unreleased client data or my personal tax details.
- `autonomy-ladder.html` is a **locally prepared, previously untracked draft**, with **private conversation deep links** and an outdated item count. It was **not displayed live**. Do not publish/commit/copy it unchanged. You may learn from its concepts and build an original public-safe illustration if useful.
- Do not overstate cause-and-effect for the Q3 randomized wording experiment; the small "95 right" versus "5 wrong" split even ran counter to the intuitive framing direction.
- Check exact words against audio when quoting; AI transcription speaker labels sometimes err. Keep claimed AI abilities/results scoped to their date, model, task, tools and review costs. **GDPval rates deliverables, not safety of delegated action**; **InsurLE is associated with Imperial College London, not Cambridge** (independent source in research notes).
- If you research additional related evidence, disclose which findings were not covered live. A credible answer can say "we don't know" without padding.

**Deliverable:** a beautiful, distinctive, high-quality static story page `index.html`, with whatever supporting assets you judge useful, that works offline except for public media and external links. Verify mobile/desktop readability, seek/play timing, shareable timestamp positions, accessibility and externally linked evidence. Use the repository's normal catalog build/config workflow *only after* you have a finished page. **Do not commit or push**; I will amend and force-push after review. No need to generate the comic.

---

There seems to be minor timestamp alignment issues. "Okay, we've crossed 20" was at 9:06, ot 9:18. "let it fail because you're checking..." was at 11:21 not 11:15. "We have a model that is ..." is at 15:38 not 15:30. But, maybe that's OK, maybe you knew it and this is intentional. I just wanted to flag that sometimes, especially for quotations, people might expect to hear that exact phrase close enough to clicking on it. Your call.

The session duration was 2.5 hours - 9 am to 11:30 am IST.

I'd like you to embed more of the pages I showed - maybe even all. Certainly break the monotonous flow of text as much as possible with visuals and interactives.

<!-- claude --resume 06f61939-8882-4972-83da-9e24e80cc96e -->

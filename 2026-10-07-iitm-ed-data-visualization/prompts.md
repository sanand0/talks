# Prompt

## Initial video-first story — 8 Oct 2026

<!-- ChatGPT Prompt source: https://chatgpt.com/c/6ac701c3-dcb0-83ec-959b-46c22feeafc0 -->
<!-- Comic page: https://chatgpt.com/c/6ac70179-3fc0-83ec-962a-afafcde86f05 -->

<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2/media:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a **beautiful, distinctive, narrative video-first story** for Anand's guest class in IIT Madras's **ED5518: Data Visualization for Engineers**, hosted by **Dr Palaniappan Ramu**, recorded on **7 October 2026**. Write the final static page to **`2026-10-07-iitm-ed-data-visualization/index.html`**.

**Source directory:** The transcript, `links.md`, audio and **`comic-page.avif`** are already alongside this prompt in `2026-10-07-iitm-ed-data-visualization/`. The class and the video are both dated **7 Oct 2026**. Build the story in this same directory. Feature the existing comic prominently near the top and make it enlargeable.

**Use the `talk-story` skill** and whichever design, interaction, data-viz, data-story and testing skills fit. Above all, **use the video-based reading experience from `../2026-10-05-tds-orientation/index.html` as the interaction and quality reference**. Inspect that page, its prompts, and its working media/deep-link/navigation implementation. Keep the _approach_—not necessarily the colors, fonts or component styling.

**Full creative/design authority belongs to you.** You have excellent design judgment: choose the title, storyline, editorial emphasis, typography, visual language, palette, whitespace, layout, component forms, interactions, responsive behavior, animation and technical implementation yourself. The arc, timestamps, bands, embeds, comparisons, cards and “near the top / full bleed” suggestions in these notes are **ideas and evidence, not wireframes, quotas or instructions to copy**. Keep only the outcome-level goals that matter: a compelling readable story, a trustworthy source trail, frequent _meaningful_ changes of visual rhythm, good accessibility, and—if the video is available—the working story/video playback experience. Improve on the 5 Oct design if you can; don't clone it or force material into an ineffective device.

The core one-sentence thesis is:

> **AI has made pictures easier to create, but harder to trust: even the reader may be another AI, and checking that it looks right is not enough.**

Or find a more memorable headline with the same meaning. Be willing to restructure the talk. This should be a **story that readers remember**, not a timeline, lecture notes, screenshot gallery or four equal sections.

## Read first

- **`story-context.md` in this directory**: carefully researched editorial map, character moments, timestamp anchors, links, asset paths, fact-check ledger and privacy guardrails. It is guidance rather than a mandatory outline.
- **`research-notes.md` in this directory**: independently checked external papers, further story ideas, primary links, additional fact-check caveats, a live-demo URL audit and one **important video availability warning**. Treat as a selective evidence shelf, not a design specification.
- **`transcript.md`**: ground truth for chronology, speakers and verbatim quotations. Verify uncertain quotes / attributed speakers against recording, especially around the final two minutes.
- **`links.md`**: demos shown live. Include all the _public, relevant_ links in appropriate narrative context, often as big engaging visual breaks/embeds; exclude private/confidential URLs. A label like `[Tools Shape Viz]` is thematic metadata, not article text.
- **`../2026-08-12-iitm-ed-data-visualization/{transcript,links}.md`** and its published `index.html`: the previous lecture to this same course. Explain _what this second lecture adds_, not repeat the earlier narrative.
- **`../2026-10-05-tds-orientation/{index.html,prompts.md,story-context.md}`**: the proven **story ↔ video emphasis toggle** and shareable timestamp-player experience.
- **`~/code/research/2026-10-ed-viz/{index.html,README.md,STORY.md,SOURCES.md,assets/,results/official-score/}`**: the engineering drawing → Codex → FreeCAD → hidden CAD Bench V3 verifier experiment from this very class. **Reuse existing prepared image assets** and/or carefully adapt the before/after interaction. The experiment's crucial verified numbers and caveats are in story-context.md. This is a compelling climax.
- **`~/code/research/chartqapro/{index.html,REPORT.md,README.md,examples/,results/}`**: actual per-question analysis, example chart images, model answers, derived findings. Use these directly rather than guessing or recreating the research. A good interactive passage asks readers to read a chart _before revealing the model's answers_. The author's own mistaken interpretation of a stacked area at **31:04** is especially revealing.
- **`2026-10-07-iitm-ed-data-visualization.opus`**: audio for the public release convention if publishing it. Prefer video as the main media; audio is an optional alternative.
- **Public full video**: https://media.s-anand.net/2026-10-07-iitm-ed-data-visualization.webm
- **Raw local video** (if you need accurate frames/clips or speaker verification): `~/r2/media/2026-10-07-iitm-ed-data-visualization.webm`.

You may inspect other talk pages and other `~/code/research/` / `~/code/datastories/` assets as needed. Links in `links.md` are starting points, not the limit of the research. Search for reliable **primary sources**, fact-check controversial or quantitative statements, and attribute additional findings. Prefer **copying and optimizing permitted local images / chart screenshots into this talk's output** over brittle remote image hotlinks. Link richly to original studies, demos, code, explainers and external interactive experiences. A live iframe is welcome **only if it actually works**; where blocked, show an accurate screenshot or compact external-link preview, never a blank frame.

## Find the story before building the site

First write a **single cohesive story arc** in your private work notes (or brief comments): a striking hook; cause/effect; a changing question; a surprising reveal; a reader-facing implication. Critique it for muddy logic, obvious/unearned transitions, repetition, weak evidence and a lukewarm ending. Revise until it reads as a story on its own. **Do not publish the outline as the article**.

Suggested arc (adjust to improve it):

1. **“It looks right. It passed its own tests. It's wrong.”** Cold-open on an image-to-CAD reconstruction. Hold back the hidden benchmark reveal; the story will earn it later.
2. Rewind: a castle of moving web requests, a football heatmap, Chennai's river and a cloud of extracted report claims. Why stick with Excel's chart menu when expressive visualization has become cheaper? Playfair → spreadsheet → generative interfaces is a historical frame, not a claim of technological inevitability.
3. Then a twist: **AI is not just drawing these charts; AI is reading them.** Bookshelf reading, models with different failure patterns, ChartQAPro. Let the visitor attempt the wind-capacity question, and note that Anand himself initially got it wrong. **Human and model perception each fail in interesting ways.**
4. “So what will _you_ do with this?” Anand repeatedly asks. Students answer with cost, survival, human decisions; one asks if you must first know your problem. Let the messy classroom actually reshape the narrative, including the surprisingly funny “half-million-dollar dashboard” chain and the **cook who tastes 50 dishes** metaphor.
5. A student at **64:12** asks the more demanding question: how do we validate the model's interpretations? Return to the bracket, reveal the **hidden CAD Bench failure**. The model was able to generate, revise and self-check—but its tests were incomplete.
6. End by handing the question to the viewer: **What will you create or read differently, and what independent check would actually catch a convincing mistake?** This is a suggested reader experiment, _not_ a claim that Anand sent an exact homework assignment. The real session ended on the open student challenge and Palani agreeing to later homework.

Potential title tension: **“The Chart Has Two Readers”**, **“Looks Right. Isn't.”**, **“Who Checks the Picture?”** or something better. Don't force all three titles or overstate model capabilities.

**Preserve the people.** Palani repeatedly relays and reframes students' questions, lets Anand wait through silence, and grounds streaming graphics in manufacturing/IoT. Harini says humans must decide; another student sharpens the validation question. Anand is openly surprised by his own mistakes. The class endured failed tab sharing and Wi-Fi interruption. Select moments that advance the lesson rather than mocking students or dwelling on mishaps.

## The experience: reproduce what made TDS orientation excellent

The reader should experience **a great narrative article first**, not a video landing page with a wall of captions.

- **Story and video are two emphases of ONE experience.** Give users a clearly discoverable **Story ↔ Video** toggle with a graceful, smooth transition. In story-focus the media remains easy to find and timestamp links are available throughout; in video-focus the same player becomes prominent with narrative/transcript alongside it. **Never remount/reset video or lose playback time** when changing emphasis. Mobile has its own thoughtful arrangement, not a cramped desktop split.
- Timestamp cues embedded naturally in prose, e.g. **▶ 31:04**, seek the SAME player and play that exact moment. Deep-linked scenes must be bookmarkable/shareable and work on load. Browser back/forward should restore sensible state/time. Respect real timestamp offsets in the file; account for transcript/audio gaps.
- Transcript access should be conveniently near the media, readable/searchable and keyboard-accessible. No autoplay on normal initial visits. Browser-owned playback controls work. Don't force a reader to watch 73 minutes before understanding.
- **Comic page near top**, linked to full-resolution image with a usable lightbox or open-full-size control. Use the existing `comic-page.avif`; do not replace it with a placeholder.
- **Break up the text constantly, and intentionally.** After roughly **one or two modest paragraphs** prefer a different visual rhythm if warranted: live embedded pages, screenshots and image comparisons, quote bands, “answer-before-reveal” charts, motion, a short reader choice, annotated schematics, small data display, photo spread, striking whitespace or a change of column/background. Each break should carry _new information_, not serve as decorative filler. Avoid five identical cards in a row, marathon prose, and a generic “here are four lessons” deck.
- The **visual's size should match its importance**. A CAD before/after should be nearly full bleed; a bookshelf photo large enough to try reading titles; a ChartQA example legible enough to answer; an animated demo should feel like motion. Let a few elements expand past the main prose width.
- For interactivity, prioritize **cognitive work**, not gimmicks. A “guess the chart answer → reveal competing model answers”, a precisely aligned CAD wipe, or an animated data transformation can earn their weight. Give static, accessible fallbacks. Avoid embedding huge third-party dashboards in ways that are unusable on phones.
- Editorial writing: precise and conversational, with funny and self-aware quoted exchanges where useful. Short sharp paragraphs, varied sentence rhythm, distinctive headings, link words to sources, _bold_ only when it helps skimming. Prefer surprising concrete scenes over general AI pronouncements.
- Maintain the usual talk-story navigation capability (jump among scenes from anywhere), but redesign it to suit the story. Section-navigation UI, article transitions and video dock must not fight for screen space.
- Ensure excellent mobile touch and keyboard use; a logical focus order, visible focus, contrast, accessible descriptions, captions/transcript and `prefers-reduced-motion` fallback. Optimize media, image loading, framing and payload. Static GitHub Pages–compatible output.
- Consider audio as an alternative to video if a verified public release exists, but do not create fake release URLs. Provide links to the official transcript and original interactive/research sources.
- Make the **article itself useful without opening any link or clicking a demo**. Links/embeds deepen an already intelligible explanation.

## Non-negotiable factual care

**Use story-context.md's fact-check ledger.** Particularly:

- **FreeCAD is the CAD tool; CAD Bench V3 is the benchmark.** The recording conflates them at 69:52. Do not propagate it. Correct in your narration, preserving the original only if an attributed verbatim quote warrants it.
- The experiment's **27/30 parameter consistency** is **NOT “90% accurate CAD”**. It got a **0.0423 geometry score** despite a plausible envelope/solid and self-check. Use raw verifier artifacts. Don't generalize one task to all CAD models.
- The **official ChartQAPro paper already analyzes errors**; Anand's “nobody published” at 29:38 is a mistaken provisional impression. The October research is a _new follow-on analysis of publicly available later-model responses_, not the world's first such study. Attribution, dataset, question type, and denominator matter.
- Satellite comparison ≠ proof the Adyar River is permanently “wetter.” Be precise about model-estimated cover, observation dates, seasonality and the map's current metric. The October `links.md` URL has **`vegetation_delta`**, while the transcript's section discusses **`water_delta`**—find the appropriate water view (earlier August `links.md` has an example).
- Claims like “90% of charts are created without a question,” “half of recipients let ChatGPT read slides,” “27 McKinsey reports per year,” and sweeping “costlier models see better” must NOT be treated as verified population facts. Keep some of Anand's hyperbole attributed as jokes/anecdotes if they improve the scene.
- The bookshelf model/cost findings are a limited benchmark; cost x-axis uncertainty is reconstruction/estimation, not rigorously calculated confidence intervals. The model labels and rankings reflect **7 Oct 2026**, not a lasting leaderboard.
- The Optum portfolio is linked via **private.s-anand.net**. **Do not publish its URL, page data or screenshots.** If that section is narratively necessary, refer only to public generic concepts, or use a different public unit-chart demo.
- Some transcript attribution around **72:33–72:47** is likely wrong; use footage to verify before quoting. Don't expose internal chats, private WhatsApp or work email as public citations; they're background context.
- Maintain the honest distinction among **a visual that looks plausible**, **a model that reasons convincingly**, **a metric that passes**, and **a verified engineering outcome**.

## Source links and high-value local imagery

Local assets to **read/copy/embed directly** instead of limiting yourself to surface URLs:

- CAD image set: `~/code/research/2026-10-ed-viz/assets/engineering-drawing.avif`, `first-model.avif`, `codex-model.avif`, `reference-model.avif`, `geometry-diff.avif`, and `{codex,reference}-stages/`.
- CAD original story and alignment/wipe logic: `~/code/research/2026-10-ed-viz/index.html`; primary benchmark https://www.gnucleus.ai/cad-bench/news/cad-bench-v3 .
- Chart error images: `~/code/research/chartqapro/examples/row_0000.jpg` (the wind-capacity crossover shown in class), `row_0030.jpg`, `row_0148.jpg`, source `examples/README.md`; supporting data and complete explainer in `~/code/research/chartqapro/index.html` / `REPORT.md`.
- ChartQAPro published paper https://aclanthology.org/2025.findings-acl.978/ ; official code https://github.com/vis-nlp/ChartQAPro .
- Cleveland & McGill graphical perception https://doi.org/10.1080/01621459.1984.10478080 .
- Original Playfair atlas https://archive.org/details/bim_eighteenth-century_the-commercial-and-polit_corry-james_1786 .
- SandDance https://github.com/microsoft/SandDance ; consider an animated unit-chart explanation.
- OlmoEarth research https://arxiv.org/abs/2511.13655 ; demonstration https://pythonicvarun.github.io/olmoearth-change-insights/ .
- JEV animated castle https://eshwarpotturi.github.io/soc-analyst-jev/ ; football shot visualization https://premier-shot-lab-202526.miyakokoko-842.chatgpt.site/ ; bookshelf https://atharva-729.github.io/bookshelf-benchmark/ ; extracted forecast claims https://files.s-anand.net/pages/mckinsey-gep-validation/ ; IMF error visualization https://sanand0.github.io/datastories/imf-gdp-forecast-errors/ .

Use `links.md` for exact links and sections. If any remote page fails to load or block frames, fall back to copied visual assets and a clearly labeled outbound link; **do not make up an embed or a screenshot**. Check appropriate image licenses/attribution before redistribution.

## QA and delivery

1. Build `index.html` and any deployable local assets in **`2026-10-07-iitm-ed-data-visualization/`**, alongside the transcript and comic. Keep original talk sources intact, and don't modify upstream research artifacts for presentation purposes.
2. Validate content against transcript timestamps, `links.md`, raw CAD scores and ChartQAPro research. Recheck external links and privacy. Record research provenance as readable source links in the page.
3. Run the `talk-story` skill's normal checks; use a local browser/devtools if available to **actually test**: initial no-autoplay; timestamp seek/play; deep-link on reload; history back/forward; story/video toggle without player reset; transcript panel; comic lightbox; good mobile layout; accessible focus/contrast; no horizontal overflow; broken external frames handled gracefully.
4. Test _reading quality_: does a stranger understand the story if they skim only headings, strong visuals and pull quotes? Does the CAD reveal come at the right moment, without premature spoilers? Does every 1–2 paragraph stretch offer a visual/intellectual change of pace? Are there at least a couple of “wait, really?” turns? Fix generic/bloated passages.
5. Update the parent talks index/README if consistent with repo conventions, with the **true 7 Oct 2026 event date**, requested output URL/path, video and transcript link. Avoid creating a duplicate entry if a canonical talk at `2026-10-07-...` is already planned; check before changing.
6. Leave the page ready for GitHub Pages. Summarize what you built and caveats. No invented benchmark metrics, quotes, footage or broken private embeds.

The benchmark is a means to the lesson—not the lesson itself. The best outcome is that a reader leaves not merely able to make a stunning visualization, but with the reflex **“What is this for? Who or what will read it? How will I know if they got it right?”**

---

By default, the video on the right has too small a height. The width is fine. But the aspect ratio of the video seems to suggest that we can increase the height for a better UI.
Are the images compressed as much as possible? If not, compress further.

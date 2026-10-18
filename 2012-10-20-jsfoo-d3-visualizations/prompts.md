# Prompts — JSFoo Bangalore, 20 October 2012: Beautiful Visualizations with D3

<!-- Comic page: https://chatgpt.com/c/6ad4a60f-dbc4-83ec-b62e-06a0bb05ff91 -->
<!-- Source: https://chatgpt.com/c/6ad3362f-a414-83ec-9f1c-9e54520c4766 -->
<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a **memorable, primary-source-grounded, video-first narrative** at `2012-10-20-jsfoo-d3-visualizations/index.html` about Anand S's **20 October 2012** JSFoo Bangalore talk, *Beautiful Visualizations with d3.js*. It isn't a generic D3 tutorial. It's a real, funny, 61-minute session in which the presenter uses D3 to turn India employment figures, JavaScript lint mistakes, live Twitter activity, shopping journeys, weather and Sanskrit into striking pictures—and then an audience member asks whether the bubbles were a good idea at all. An answer about **why** to visualize is worth more than the technical recipes.

Use local **`.agents/skills/talk-story/SKILL.md`** plus visualization, storytelling and browser-testing skills. Inspect working reference pages `../2026-10-05-tds-orientation/index.html`, `../2026-10-07-iitm-ed-data-visualization/index.html`, `../2015-02-28-tedx-nmims-bangalore/index.html` and `../2024-08-10-tedx-mdi-gurgaon/index.html` for *proven interaction patterns*, not visual designs. Create a distinct D3-native, visual-storytelling aesthetic.

## Evidence hierarchy — read before designing

1. **`transcript.md` + original video** https://youtu.be/JAlZ0uJnqkA (video ID `JAlZ0uJnqkA`, 60:55). Opening audible speaker timestamp ~01:17. All direct quotations and seek timecodes checked against this **original** recording, especially the questions/answers around 32:50–35:58 and the coding glitch around 49:00–50:30.
2. **`story-context.md`** — the discovered plot, scene order options, timestamp anchors, high-value experiments, and why the audience challenge is the hinge. This is editorial guidance, not a required set of cards/chapters.
3. **`research-notes.md`** — dates, original source provenance, archival D3 v2 compatibility, split authorship of demos, data-science caveats and accuracy ledger.
4. **`links.md`** — event/recording/programme, direct links to original demo pages, code files and data CSVs, primary research and modern context.
5. **Actual source code** https://github.com/sanand0/beautiful-visualisations ; a local research checkout exists under `~/Downloads/talks-audio-2026-10-17/beautiful-visualisations-source/`. The original HTML/CSV/JavaScript survived! Selected original source/data files are also archived in `sources/`; see `sources/README.md`. Examples include `nrega.html`, `jslint.html`, `tweets.html`, `shopping.html`, `weather.html`, `wordcloud.html`, `nrega.csv`, `jslint.csv`, `weather.csv`, `ramayana.py` and `d3.v2.js`. Original live demo index https://sanand0.github.io/beautiful-visualisations/ was accessible when preparing this brief; test specific pages with real JS before embedding.
6. **Authentic video stills** `slides/*.webp` with timestamp map in `frame-map.md`, extracted from the recorded stage/screencast. Use a small, strategic subset (and/or original running examples) in the narrative; do not substitute modern-looking uncredited charts for 2012 originals.
7. **Audio:** `2012-10-20-jsfoo-d3-visualizations.opus` exists. Only link public audio once hosted/release URL is actually verified. Do not link a presumed GitHub release.
8. **`comic-page.avif` remains pending** and will be provided by the user shortly. When present, showcase it near the top with alt text and lightbox; document its provenance as an interpretative companion, not a stage screenshot. **Do not generate it or substitute stock art.**

## The hidden story beneath the showreel

**Best line:** “The bubbles looked cool. The question was whether they helped anyone see.”

The core tension is **expressiveness versus judgment**. D3 removes restrictions from the visual canvas. Anand can draw almost anything, but visual power does not tell him what to draw. A participant at 32:50 challenges the choice of bubble chart to show lint errors. Anand at ~33:20 admits he used circles partly because they looked cool; this is a genuine, revealing pivot, not a gotcha. Then he ranks ways humans perceive quantities and moves into the code. Finally, he debugs circles mistakenly positioned using rectangle attributes; another reminder that a designer still needs to understand the system.

Consider a cold open that **asks the reader** to compare values on an authentic 2012 bubble diagram before revealing the Q&A, then rewind:
- **01–10 min:** the first bubble charts (NREGA, JSLint). Show that they communicate, entice and mislead in different ways.
- **11–17 min:** conference tweets become dots, revealing the room to itself—people notice themselves in the data.
- **18–32 min:** quick, *curated* glimpses of supermarket choices, Indian weather, Sanskrit Ramayana word cloud, third-party Wealthfront graphic and Mike Bostock's showreel. Don't write six equally weighted tutorials.
- **32:50–35:58:** the decisive audience challenge and the “looked cool” answer. A brief comparison of positional versus area encodings makes the counterpoint felt.
- **39–53 min:** reveal the code and `.data().enter()` concept: each row maps to a native DOM/SVG node. Debug `x/y` versus `cx/cy` in a live learner interaction. It is the practical payoff to the philosophical challenge.
- **53–61 min:** practical audience questions: browsers, server-side data, SVG base map and what D3 actually does. Conclude on *choices*, not breathless library worship.

**Important:** The final moral can relate to current AI-assisted chart making, but any 2026 reflection must be clearly an editorial epilogue, NOT retrospectively inserted into the 2012 speaker's mouth. The speaker's own 2012 moment is sufficiently strong.

## Let the reader discover before explaining

Candidate 1 (prefer): **Beauty ≠ precise comparison.** Show an authentic small subset of the actual `jslint.csv` data (or `nrega.csv`) as faithfully encoded circles, then allow a switch to accurately scaled sorted bars / aligned dots. Ask a real question with a verifiable answer, e.g. “Which rule is highest? By roughly how much?” Cite exact original values. Label a modern reconstruction clearly; never invent or silently massage the historic CSV.

Candidate 2: **Data joins become objects.** Bind an array to SVG circles; adding/removing elements shows enter/update/exit. An inspect pane could show exactly which DOM element maps to which data value, with a side-by-side 2012 D3-v2 excerpt and modern implementation. A brief SVG attribute “debug the bug” exercise should reproduce the **real** ~49:59 stage error using `cx/cy`, not invent an unrelated bug.

Optional small scene: let readers inspect authentic `#jsfoo` tweet time dots or 2012 Ramayana words, **only if backed by the archived files**. More interaction is not necessarily better; prioritize two memorable interactions with pedagogical value.

Use a varied magazine visual rhythm with abundant historical stills/quotes/real source charts, not long paragraphs; distinguish your design from the companion PowerPoint article. The most vivid tension is that the talk is called **Beautiful Visualizations**, but ends by teaching what makes them useful.

## Player and archival rules

**ONE VIDEO:** https://youtu.be/JAlZ0uJnqkA via YouTube IFrame Player API. Do not search for, produce, embed, upload or link a local WebM/MP4 video or another source, even though authentic stills were extracted from the film. Use a stable persistent player with Story ↔ Video focus modes, seekable timestamp links, transcript popup, accessible player controls, mobile-safe sticky/compact state, deep-link/history restore, stable playback on mode switches, section navigation and reduced-motion support. Test key interactions in-browser rather than trusting static HTML.

Historical repo D3 **v2** code is not a drop-in modern D3 implementation. Make 2012 code snippets and any reconstructed browser interactions explicitly distinct. Do NOT present current JS API, salaries, Twitter tweets, news or climate patterns as authentic 2012 content. Credit original visual/data owners; the Wealthfront salary chart and Mike Bostock showreel are **not** Anand's works.

## Source discipline, implementation, QA

- Event happened **20 Oct 2012**, NIMHANS Bangalore, despite Dec 2012 YouTube publication; documented in https://jsfoo.in/2012/ and https://gist.github.com/sanand0/4554440 . Fix the existing `config.json` entry when publishing a **finished** page; don't point catalog readers to a missing HTML file.
- Confirm the audience's wording and speaker's candid admission against original audio. Generic “Audience”/“Unsure” stays generic; don't invent an identity. Never lift words from third-party clips as if Anand said them.
- Perceptual-encoding research https://doi.org/10.1080/01621459.1984.10478080 is **external background**, not a paper Anand cites on stage. Distinguish the talk's 2012 claims from published evidence and 2026 interpretation.
- Check original `nrega.csv`/`jslint.csv` meaning and calculations if you recreate any chart. No invented statistics, fake source slides, invented trends or inaccessible/empty iframes. For a repo-dependent demo, provide a usable static fallback plus link if embedding fails.
- Use footnoted inline source links, memorable verified quotes, responsive fresh visual design, and frequent purposeful transitions. Each interaction should change comprehension, not just entertain.
- Run the complete talk-story skill QA: seek/play/pause, focus switch without resetting, URL history, transcript, section jump, lightbox, source-link completeness, speaker attribution, color contrast, mobile overflow, keyboard/reduced motion, and the actual functionality of archived examples.
- **Do not generate HTML, commit, push or deploy yet.** This `prompts.md` is the instructions for the next stage after the comic is provided.

---

The comic has a distorted aspect ratio. Fix that.
slides/01-nrega.webp and slides/02-jslint.webp aren't fully visible, they're cropped horizontally - and it's not clear what they're showing. Crop properly, or don't crop. Same with slides/04-shop-paths.webp and slides/05-india-weather.webp and slides/09-d3-selections.webp and slides/10-debug-d3.webp and slides/11-data-bound.webp and maybe others.
slides/06-sanskrit-wordcloud.webp is too blurred and the sanskrit too small. Is there a better image we can use?
Files with a .src look like they're sitting above the line, not along the line. That doesn't look nice.
The .who feels like it's bit too near the top of .say - might be better to align the .who to the first line of the .say?
There may be other similar errors. Find and fix them.

<!-- claude --resume e1057bfd-56eb-4135-a682-f4aae07b9709 -->

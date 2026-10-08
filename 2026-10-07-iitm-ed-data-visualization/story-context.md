# Story context — IIT Madras ED5518 Data Visualization, 7 Oct 2026

> Working notes for Claude Code, **not** article copy. The class was on **Wednesday 7 Oct 2026**. The transcript, links, Opus audio, comic and these authoring notes all live together in `2026-10-07-iitm-ed-data-visualization/`. Publish the story here. Video: https://media.s-anand.net/2026-10-07-iitm-ed-data-visualization.webm

## The big story

**The price of creating a picture is falling. The importance of knowing what it says—and whether it is right—is rising.** The twist in this lecture is that the reader of a chart may no longer be a person: it may be another AI. Its visual perception differs from ours; and when an AI-generated, AI-checked engineering object passes the wrong tests, confidence can become especially misleading.

The recurring questions are not merely “What visualizations can AI make?” but **“Who will read them?”, “What will they misread?”, “What will we DO with the information?” and “What test would catch a convincing failure?”**

Don't produce a four-topic outline or a parade of demo thumbnails. Arrange scenes as a discovery: seduction by visual abundance → the new reader's blind spots → students struggle to extract personal use → a student asks about validation → a CAD model with a hidden failure → a verification challenge handed back to the reader.

## Event and teaching context

- **ED5518: Data Visualization for Engineers**, Department of Engineering Design, IIT Madras. Palaniappan Ramu (Palani) hosts the guest session; Anand teaches remotely, students respond through the room microphone. The talk lasts ~73 minutes. Source: `transcript.md`.
- **This is Anand's second ED5518 visit** after 12 Aug 2026: `../2026-08-12-iitm-ed-data-visualization/` and published story https://talks.s-anand.net/2026-08-12-iitm-ed-data-visualization/. In August Anand asked “Why are you even sitting in this class?” and argued for framing, questioning, exploration, critique and verification when AI makes charts cheap. October extends that to **unbounded visual forms, AI as a consumer of visualizations, model-specific perception, and domain verification**.
- Earlier Palani/Anand conversations (e.g. `~/Dropbox/notes/transcripts/2026-01-14 Palani IITM.md`, `~/Dropbox/notes/transcripts/2026-05-17 Palani B.md`) emphasized redesigning engineering visualization education for AI-era judgment, tangible manufacturing/CAD cases, and turning visual output into decisions and trustworthy explanations. These are private context, not quotable by default.
- Palani himself, around **40:51**, connects streaming security dots to IoT, running machines, live manufacturing and real-time monitoring. This makes the class genuinely about engineering, not solely journalism/business charts.
- Student questions reshape the final half. Anand explicitly flips the class at **46:51**: “What would you like to know about?” A student then asks whether a problem must be specified before choosing a chart; another asks how to validate an LLM's visual interpretation. The lesson is partly the students learning to ask *what is this FOR?*
- Palani closes by accepting homework at **73:01**. Leave readers a compact, concrete experiment rather than inventing an actually assigned homework sheet.

## Suggested cold open and reveal order

**Cold open**: At **66:52–68:21**, Codex made a plausible 3D bracket. It tested itself, noticed an error, fixed it, passed its own checks, and was still wrong. Show aligned candidate and reference as a dramatic before/after / wipe: `~/code/research/2026-10-ed-viz/assets/codex-model.avif`, `reference-model.avif`, `geometry-diff.avif`, and the original `engineering-drawing.avif`. **Don't give away the CAD Bench score immediately.** Promise to return to it: if an AI checks the visual work of another AI, what counts as 'checked'?

Rewind to the class; interleave four dramatic questions:

### 1. What happens when anyone can make almost any chart? (03:01–20:44)

- **03:01**: William Playfair's 18th-century hand-engraved and colored statistical atlas, then modern spreadsheet templates, now generative/browser visuals. This is a *useful historical metaphor*, not a literal monotonic historical law. Excel and templates made common forms easier to distribute, not “killed visual diversity”.
- **04:00–06:03**: Eshwar's security gate JEV Keep: requests as dots travelling through a castle, attacks diverted to tally/race. Great **motion- or iframe-sized visual**, not merely a screenshot. https://eshwarpotturi.github.io/soc-analyst-jev/ . Important: the LLM/decision model is Jev; don't generalize performance/pricing without local benchmark.
- **07:01–09:00**: first-year student's football shot atlas: a passionate domain expert asking the questions he knows matter; sequence/timing/shot location instead of static heatmap. https://premier-shot-lab-202526.miyakokoko-842.chatgpt.site/ . Avoid unverified “City University of Tokyo,” exact student nationality, or goals-versus-shots ambiguity without confirming site.
- **10:14–14:00**: Chennai river: OlmoEarth-derived local water/vegetation change map. Student says “Greenery?”; Anand says water; Palani guesses Adyar. The familiar place suddenly becomes data. Demo hub: https://pythonicvarun.github.io/olmoearth-change-insights/ ; actual link in `links.md` points to the **vegetation** layer even though the talk discusses **water** at this point. Find/use the correct `metric=water_delta` version (see August links.md), don't silently mismatch color legend and narrative.
- **14:31–18:08**: McKinsey Global Energy Perspective transformed from thousands of *claims* to a unit visualization with categories, chronology, importance and smooth transitions: https://files.s-anand.net/pages/mckinsey-gep-validation/. Microsoft SandDance background: https://github.com/microsoft/SandDance . Its concept is “one mark per row,” not “every dancing-dot chart is literally SandDance.” Avoid treating forecasts as verified facts.
- **18:08**: Optum product/capability map, 208 products as said on stage. Link in `links.md` is on `private.s-anand.net`: **do not embed, screenshot, quote confidential taxonomy or link publicly** without confirmed clearance. Better omit or describe generically, or replace with the public IMF forecasts experiment: https://sanand0.github.io/datastories/imf-gdp-forecast-errors/ .
- **19:54**: curricular pivot: tools change. Principles outlast them. *Domain curiosity and the ability to choose useful representations become more important as production barriers fall.*

### 2. A picture now has a second kind of reader (20:44–35:24)

- **20:44** graphical perception (humans): Cleveland–McGill precision varies by encoding, aligned position commonly easier than angles/areas; qualifiers apply, not universal ranking for all tasks. Primary: https://doi.org/10.1080/01621459.1984.10478080 ; original paper PDF https://euclid.psych.yorku.ca/www/psy6135/papers/ClevelandMcGill1984.pdf .
- **21:33** reveals the real reframing: a recipient may upload the deck/chart to ChatGPT instead of interpreting it personally. Treat “half the audience” as Anand's anecdotal figure **not measured prevalence**. The designer must ask whether both human and model readers can extract the same correct conclusion.
- **22:31–27:35** Atharva's bookshelf benchmark: same shelf photo, models extract different titles; measured performance vs estimated API cost, uncertainty bars because hidden reasoning-token accounting was incomplete. https://atharva-729.github.io/bookshelf-benchmark/ . The 86%/80%/70% figures are a *specific run and scoring protocol*, not universal VLM rankings. The cost intervals are estimates, not confidence intervals of model accuracy. Inspect the benchmark's actual labels and methodology before reprinting numbers. It is a nice **show-the-shelf, let the reader guess, then contrast AI's misses** interlude.
- **27:58–34:36** ChartQAPro: ask a seemingly simple visual question; multiple models disagree. **30:30** example of wind-capacity crossover; **31:04** Anand himself interprets the stacked area incorrectly on his first try! This honest mistake is a pivotal character moment: *the experienced teacher is also a fallible visual reader*.
- **32:21** the local response-analysis research finds approximation/geometry readout a weakness in a sampled set of models. **Don't claim** all models fail or that ChartQAPro researchers “published no error analysis”; official paper includes error analysis.
- Strong split visual **human vs AI errors** with local assets, not a simplistic “one is smarter” scoreboard. Local gold-standard research: `~/code/research/chartqapro/REPORT.md`, `README.md`, `index.html`, `examples/row_0000.jpg`, `examples/row_0030.jpg`, `examples/row_0148.jpg`. The wind-capacity example is `examples/row_0000.jpg`, source answer 2037–38. Models from independently available prediction files: Qwen2.5-VL-3B, Qwen2.5-VL-7B and START-RL-7B. Official baseline had no public row-level responses for all 21 original models.
- Representative **non-universal** quantitative research result (7 Oct local report): for START-RL-7B, median relative numerical error among parseable predictions ≈2.8% non-approx vs 33.3% on approximation-tagged questions. Approximation tags are keyword heuristics; don't treat this as causal estimate.
- Official primary ChartQAPro reference: https://aclanthology.org/2025.findings-acl.978/ ; https://github.com/vis-nlp/ChartQAPro ; data https://huggingface.co/datasets/ahmed-masry/ChartQAPro . 1,341 charts, 1,948 questions, 99 sources in official paper. An interesting editorial payoff: **accuracy is not the same as what evidence a reader actually perceived**.

### 3. The students ask the awkward question: SO WHAT? (35:35–65:58)

- At **35:46**, Anand asks “What does this mean? As a result of this, what are you going to do about it?” Silence. Palani translates; Anand waits; students answer survival in an AI race (**39:18**), cost/accuracy (**42:41**), and human decision ownership (Harini, **43:49**). These are legitimate but not yet an action. Let the article feel this friction, without ridiculing the students.
- **45:34**: Anand says purposeless learning doesn't stick for him. A classroom is a dilemma: attendance and syllabus are not the student's own question.
- **46:51**: he flips to Q&A. **48:44–56:45**: student asks “Must I completely know the problem before visualizing?” Anand's satirical chain of business sponsor → PM → proposal → developer → dashboard → 20 more charts, and the infamous $0.5m “success” joke **50:45**, versus designers working closely with question-owner. This is an *anecdotal caricature*, not a published audit of companies or a real $0.5m invoice. His “90% of visualizations” at 53:25 is rhetorical, **unsourced**, never state as statistic.
- At **54:50**, the student's real question emerges: not merely requirements but **how to choose what type of data and chart to use**. Anand's unusually useful answer **55:53**: “To be a good cook, you don't have to cook every dish. You certainly ought to taste a lot of dishes and cook a few.” Followed by **56:45**: ask “How can I use this?” each time you encounter a visualization.
- **57:53–62:04** loss of connection; humorous room logistics and repeated screen-sharing failures at **10:14** and **16:19** make this distinctly a real remote class. A few human details, not an excessive blooper reel.
- **64:12**: a student finally asks “how can I believe its accuracy?” This is the **narrative pivot** back to the cold open and its unanswered CAD puzzle.

### 4. The model built the object. Who built the test? (65:58–73:18)

- Exact experimental record and *best visual asset of the entire story*: `~/code/research/2026-10-ed-viz/README.md`, `STORY.md`, `index.html`, `assets/`, `results/official-score/reward.json`, `reward_details.json`, `spec_findings.json`. The story site itself can be embedded if accessible at https://sanand0.github.io/research/2026-10-ed-viz/ ; otherwise take / adapt (and copy for deployment) local imagery and the simple wipe interaction.
- **65:58** drawing → Codex with FreeCAD: source drawing only, hidden reference withheld. One run got distracted by image crops; a revised run built an editable candidate, checked the 150×48×88 mm envelope / valid single solid, then **67:44** refined one boss/support dimension on its own. It was *genuine self-correction*—just incomplete.
- **68:21** reveal hidden geometry: lower fork portion / curved profiles missing or different. Shared camera/crop and correctly aligned images crucial; don't compare independently auto-framed objects.
- **69:52** Anand says “CAD benchmark called FreeCAD,” a speech conflation. **Correct editorially**: **FreeCAD is the CAD editor/runtime; CAD Bench V3 by gNucleus is the task/benchmark and hidden verifier**. Primary https://www.gnucleus.ai/cad-bench/news/cad-bench-v3 ; FreeCAD https://www.freecad.org/.
- Exact experiment result if showing metrics: valid editable solid, 150×48×88 mm envelope, **27 of 30** spec parameters matched by checker, yet **0.0423 geometry score** and **0.0798 combined score**, with **13.7% volume mismatch**. These are **single local task results**, not model-level benchmark averages. `~/code/research/2026-10-ed-viz/README.md` and raw official scorer prove it. 27/30 is NOT 90% geometry accuracy because features can match coincidentally.
- A memorable design: side-by-side **“Agent's tests: PASS”** and **“Hidden geometry: FAIL”**; distinguish “looks right”, “dimension checks pass”, “design intent / geometry correct.” Reveal metrics after showing actual visual difference.
- **70:50** Anand's THREE personal observations: (1) models can generate and self-correct, (2) even he often cannot spot small misses, (3) a more comprehensive independent specification/benchmark is needed. The actual lesson: **self-verification is only as strong as the verification kit**.
- The ending is deliberately unfinished: **72:03** Anand asks students for their takeaways; **73:01** Palani agrees Anand can send homework. Instead of forcing an invented moral or claiming a distributed homework prompt, hand the reader a practical choice to test: *Pick a visualization, state a decision it supports, ask two different readers (human/AI) to read it, and create an independent ground-truth check. What error survives?* Label as a **suggested reader experiment**.

## Scene-to-player seek anchors

| mm:ss | Story use |
|---|---|
| 03:01 | Playfair → spreadsheet → generative visual variety |
| 04:00 / 06:03 | Security castle / animated dots |
| 07:01 / 08:51 | Football atlas / domain sense > coding |
| 10:14 / 11:42 / 13:06 | Chennai water, screen share retry, Adyar reveal |
| 14:31 / 16:44 / 18:08 | McKinsey claims / animated unit charts / portfolio |
| 19:54 | Tool skepticism / longer-lived principles |
| 20:44 / 21:33 | Human perception / AI as chart reader |
| 22:31 / 26:08 | Bookshelf test / cost-uncertainty bars |
| 27:58 / 30:30 / 31:04 / 32:21 | ChartQAPro / wind example / Anand's own miss / approximation |
| 35:46 / 37:12 / 40:46 | So what? / what's the point? / wait |
| 42:41 / 43:49 | Cost vs accuracy / Harini decides |
| 45:34 / 46:51 | Learn with purpose / flipped Q&A |
| 48:44 / 50:45 / 54:50 | Must define problem? / $0.5m dashboard satire / real question |
| 55:53 / 56:45 | Taste 50 dishes / “How can I use this?” |
| 64:12 / 65:58 | Student asks validation / drawing to CAD |
| 66:52 / 67:44 / 68:21 | Created / self-corrected / hidden reference |
| 69:52 / 70:50 / 72:03 / 73:01 | CAD Bench test / three lessons / open challenge / homework |

**Check timestamp offset in the actual WebM player.** Source `transcript.md` has marked silent patches; video and transcripts may differ subtly after interruptions. Do not invent verbatim quotes or misattribute; the closing ~72:33–72:47 speaker labels may have been swapped by transcription—verify against recording before direct quotation.

## Asset / embedding plan (visual breaks preferred every 1–2 paragraphs)

**Available locally; reuse, copy and optimize for the talk output** (do not create external hotlink dependencies to private local files):

1. `comic-page.avif` in this directory **already exists**. Hero visual; click to full-resolution. Design a graceful size-aware lightbox.
2. `~/code/research/2026-10-ed-viz/assets/{engineering-drawing,first-model,codex-model,reference-model,geometry-diff}.avif` + `codex-stages/*.avif`, `reference-stages/*.avif`; reuse existing aligned comparison logic in `index.html`.
3. `~/code/research/chartqapro/examples/row_{0000,0030,0148}.jpg`; inspect / cite `examples/README.md`; use one question as “you answer first” interactive reveal.
4. `~/code/research/chartqapro/index.html` for additional charts, explainers and local results. If reusing plots, check data denominator / scorer and label sources.
5. Public embed/link candidates from `links.md`: Eshwar JEV Keep; Shot Atlas; OlmoEarth; McKinsey claims; IMF forecast errors; bookshelf benchmark. Verify iframe permissions / X-Frame-Options / mobile / loading, provide a screenshot or linked visual fallback.
6. Playfair hand-tinted plate (public-domain original), preferably via https://archive.org/details/bim_eighteenth-century_the-commercial-and-polit_corry-james_1786 . Download and optimize a legally reusable image rather than embedding an auction-house picture via hotlink.
7. Microsoft SandDance explanatory animated GIF if useful: https://user-images.githubusercontent.com/11507384/189461831-9467863e-bff8-47d2-aa03-ab2b74658814.gif (from public https://github.com/microsoft/SandDance). Attribution, performance and user-motion controls.
8. Optional bespoke simple browser visual: compare a **human-readable labeled chart** vs. **unlabeled chart requiring visual interpolation**, then show the same question put to a model. Avoid implying that all labels always improve every use or that adding labels makes flawed data correct.

**Private / avoid:** `https://private.s-anand.net/optum-portfolio/`, local context.sqlite, work mail, unpublished WhatsApp, private chatgpt.com conversation URLs, personal details. These inform editorial direction only. Public items on `files.s-anand.net` can be linked if already public; verify before embedding.

## Fact-check and attribution ledger

| Spoken shorthand / tempting line | Publish safely as |
|---|---|
| “Tools shape visualizations” | Useful design-history thesis: medium, tool capabilities and conventions influence visual forms; no absolute hand-drawn → template → generative succession. |
| “This Japanese student from City University of Tokyo doesn't program” | Attribute to anecdote in class, but omit institutional and no-coding certainty unless verified. |
| “Adyar is certainly wetter” / 100m squares | **Mapped model-estimated water coverage** across selected dates; seasonal effects, spatial resolution, classification mistakes, rain/tide and registration can confound. Don't assert long-term river restoration without validation. |
| “2,200 facts in 27 annual McKinsey publications” | Demo-specific **extracted claims**, which mix forecasts, estimates and explanatory statements; inspect public demo before stating counts. 27 is not necessarily “reports each year.” |
| “Not Excel-creatable” | This kind of custom interactive visualization is awkward in conventional spreadsheet workflows, not mathematically impossible in Excel. |
| “Half the audience uses AI to read charts” | Anecdotal forecast/habit, **not an empirical adoption statistic**. |
| Bookshelf model ranking / higher cost → greater accuracy | Within Atharva's particular tests and cost assumptions; avoid global claims or false precision. |
| “ChartQAPro team didn't publish error analyses” | **False literally**: original 2025 ACL paper includes error analyses. Local October 2026 work adds *response-level comparisons for later models*, not first ever analysis. |
| “Models like humans show same biases” | Specific overlaps/differences require experiments; don't equate human perceptual hierarchy to model error profile. |
| “90% of visualizations made without a problem” | Opinion / hyperbole for narrative humor, never represent as measured share. |
| “CAD benchmark called FreeCAD” | **CAD Bench V3 benchmark** + **FreeCAD runtime**. |
| 27/30 CAD spec checks | Count of matched parameters in one check, NOT 90% correct design, despite geometry score ~0.04. |
| Browser live demos / book prices / model names | Snapshots as of Oct 7, 2026; check that pages are public before publishing. |
| Factual vs opinion status | Wherever possible tie to transcript timestamps, raw benchmark output, original paper or direct live demo; clearly label inference. |

## Externally checkable primary/reliable sources

- ChartQAPro ACL 2025 paper https://aclanthology.org/2025.findings-acl.978/
- ChartQAPro official code https://github.com/vis-nlp/ChartQAPro
- CAD Bench V3 release (21 Sep 2026; covers text, edit, image-to-CAD) https://www.gnucleus.ai/cad-bench/news/cad-bench-v3
- FreeCAD https://www.freecad.org/
- Microsoft SandDance project / unit views https://github.com/microsoft/SandDance
- OlmoEarth paper (2025) https://arxiv.org/abs/2511.13655 and model code https://github.com/allenai/olmoearth_pretrain
- Cleveland & McGill 1984 Graphical Perception https://doi.org/10.1080/01621459.1984.10478080
- Playfair 1786 primary scanned atlas https://archive.org/details/bim_eighteenth-century_the-commercial-and-polit_corry-james_1786
- Local engineering drawing experiment full provenance `~/code/research/2026-10-ed-viz/SOURCES.md`
- August ED5518 prior talk and linked examples `../2026-08-12-iitm-ed-data-visualization/{transcript,links}.md`
- TDS 5 Oct video-story experience template `../2026-10-05-tds-orientation/index.html`, `prompts.md`, `story-context.md`

## Editorial / user experience guardrails

- This is **not** a research-report clone of either `chartqapro/index.html` or the CAD experiment page. Those are demonstrations/substories with their own detail. The class story is the **human narrative**: visual abundance → dual audience → purpose → verified design.
- Retain tension: agents can generate/correct, yet confidently miss geometry; domain experts can tell better stories, yet also misread stacked areas; asking “so what?” is demanding, yet the best student questions improve the lecture.
- Technical claim boxes and caveats should be crisp and visually separated from the main arc. Don't turn all content into footnotes or repeat one type of card.
- The final prompt can revisit Anand asking questions to stay awake at the start (**00:48**) and the class literally getting disconnected; nice self-aware echo if it earns its space.
